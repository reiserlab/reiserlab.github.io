#!/usr/bin/env python3
"""Assemble the "eye to T4" scroll-hero frame sets.

The sequence joins two of Marisa Dreher's animations for Zhao et al. 2025:

  A-E  the eye-map hero already in media/hero/eyemap-{desktop,mobile} (re-rendered, label-free):
       head -> into the eye -> retina and lens row -> one lens, photoreceptor, L1, Mi1 -> medulla columns
  X    a short cross-dissolve
  F-H  her rendered T4 frames (media/sources/hero-marisa/download/extracted/T4_Frames, label-free):
       one T4 cell -> its dendrite on the medulla column grid, input columns lit -> preferred-direction arrow

Run from the repo root:  uv run tools/build_hero_eyet4.py
Writes media/hero/eyet4-desktop and media/hero/eyet4-mobile (f_0001.webp ..., poster.jpg) and prints the
scroll-progress position of each stage, for the caption stops in data/site.yaml.
"""
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
HERO = ROOT / "media" / "hero"
T4 = ROOT / "media" / "sources" / "hero-marisa" / "download" / "extracted" / "T4_Frames"
BG = (23, 21, 19)  # #171513, the eye-map re-render's background

# (label, source, first, last, number of frames)
STAGES = [
    ("A head (rest)",            "eye", 1,    30,   30),
    ("B into the eye",           "eye", 31,   48,   18),
    ("C retina, lens row (rest)", "eye", 49,   90,   24),
    ("D down one column",        "eye", 91,   123,  26),
    ("E Mi1 and columns (rest)", "eye", 124,  180,  26),
    ("X dissolve",               "mix", None, None, 8),
    ("F one T4 cell, to its dendrite", "t4", 1730, 1794, 22),
    ("G dendrite on the columns (rest)", "t4", 1794, 1858, 16),
    ("H preferred direction (rest)", "t4", 1858, 1954, 26),
]
SHIFT_DESKTOP = 0.18      # T4 subject moves right of center so the caption has room on the left
SUBJECT = (0.445, 0.52)   # dendrite center in the T4 frames (fraction of width, height)


def smooth(t: float) -> float:
    t = min(1.0, max(0.0, t))
    return t * t * (3 - 2 * t)


def t4_frame(k: int) -> Image.Image:
    p = T4 / f"{k}.png"
    if not p.exists():          # one frame is missing from the delivery
        p = T4 / f"{k + 1}.png"
    im = np.asarray(Image.open(p).convert("RGB")).astype(np.uint8)
    im = np.maximum(im, np.array(BG, dtype=np.uint8))   # lift pure black to the hero background
    return Image.fromarray(im)


def t4_desktop(k: int) -> Image.Image:
    """Shift the frame right (ramping in during stage F) and feather the exposed left edge."""
    im = t4_frame(k)
    w, h = im.size
    shift = round(SHIFT_DESKTOP * w * smooth((k - 1740) / (1794 - 1740)))
    if shift <= 0:
        return im
    canvas = Image.new("RGB", (w, h), BG)
    ramp = np.clip((np.arange(w) - 0) / (0.10 * w), 0, 1)           # 0 -> 1 over the first 10% of the frame
    alpha = Image.fromarray((np.tile(ramp, (h, 1)) * 255).astype(np.uint8))
    canvas.paste(im, (shift, 0), alpha)
    return canvas


def t4_mobile(k: int, size=(960, 1707)) -> Image.Image:
    """Portrait: start with the whole frame fitted to the width, then zoom in on the dendrite for stage G."""
    im = t4_frame(k)
    w, h = im.size
    W, H = size
    t = smooth((k - 1750) / (1794 - 1750))
    s0, s1 = W / w, 0.98 * H / h          # fit the width -> nearly fill the height, dendrite in the upper half
    s = s0 * (s1 / s0) ** t
    im2 = im.resize((round(w * s), round(h * s)), Image.LANCZOS)
    # fade the top and bottom edges into the background so nothing is cut off while the frame is letterboxed
    ramp = np.clip(np.minimum(np.arange(im2.height), im2.height - 1 - np.arange(im2.height)) / (0.08 * im2.height), 0, 1)
    alpha = Image.fromarray((np.tile(ramp[:, None], (1, im2.width)) * 255).astype(np.uint8))
    cx = 0.5 + (SUBJECT[0] - 0.5) * t
    cy = 0.5 + (SUBJECT[1] - 0.5) * t
    canvas = Image.new("RGB", size, BG)
    canvas.paste(im2, (round(W / 2 - cx * im2.width), round(H * 0.43 - cy * im2.height)), alpha)
    return canvas


def eye(kind: str, k: int) -> Image.Image:
    return Image.open(HERO / f"eyemap-{kind}" / f"f_{k:04d}.webp").convert("RGB")


def build(kind: str, quality: int) -> list[tuple[str, float, float]]:
    out = HERO / f"eyet4-{kind}"
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("f_*.webp"):
        old.unlink()
    t4 = t4_desktop if kind == "desktop" else t4_mobile
    frames: list = []
    spans = []
    for label, src, a, b, n in STAGES:
        start = len(frames)
        if src == "eye":
            frames += [("eye", int(round(v))) for v in np.linspace(a, b, n)]
        elif src == "t4":
            frames += [("t4", int(round(v))) for v in np.linspace(a, b, n)]
        else:
            frames += [("mix", (i + 1) / (n + 1)) for i in range(n)]
        spans.append((label, start, len(frames) - 1))
    total = len(frames)
    last_eye, first_t4 = eye(kind, 180), t4(1730)
    for i, (src, v) in enumerate(frames, start=1):
        if src == "eye":
            im = eye(kind, v)
        elif src == "t4":
            im = t4(v)
        else:
            im = Image.blend(last_eye, first_t4, smooth(v))
        im.save(out / f"f_{i:04d}.webp", "WEBP", quality=quality, method=6)
        if i == 1:
            im.save(out / "poster.jpg", quality=88)
    size = sum(p.stat().st_size for p in out.glob("f_*.webp")) / 1e6
    print(f"{kind}: {total} frames, {size:.1f} MB")
    return [(label, a / (total - 1), b / (total - 1)) for label, a, b in spans]


if __name__ == "__main__":
    spans = build("desktop", 84)
    build("mobile", 52)
    print("\nscroll progress of each stage:")
    for label, a, b in spans:
        print(f"  {a:0.3f}-{b:0.3f}  {label}")
