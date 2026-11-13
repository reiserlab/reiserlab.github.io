# media/hero: frame sequences for the home-page scroll hero

Animation by Marisa Dreher, from Zhao et al. 2025 (*Nature*, "Eye structure shapes neuron function in
*Drosophila* motion vision"). The fly head model is lab-owned. No frame contains text, labels or arrows; all
on-screen text belongs in HTML.

Made 2026-11-13. Source files, scripts and the rebuild steps are in `media/sources/hero-marisa/`
(git-ignored); start with `SOURCES.md` there.

## Current hero: `eyet4-desktop` and `eyet4-mobile` (2026-11-14)

196 frames each (12.6 MB and 6.3 MB), assembled by `tools/build_hero_eyet4.py` from the `eyemap-*` sets below
plus Marisa's label-free T4 frames 1730-1954 (in `media/sources/hero-marisa/`, background lifted from black to
#171513). Stages by scroll progress: head 0-0.15; into the eye 0.15-0.24; retina and lens row 0.25-0.36; down
one column 0.37-0.50; Mi1 and medulla columns 0.50-0.63; dissolve 0.64-0.67; one T4 cell turning to show its
dendrite 0.68-0.79; dendrite on the column grid with its input columns lit 0.79-0.87; preferred-direction
arrow 0.87-1.0. On desktop the T4 subject is shifted right of center; on phones the T4 frames zoom from the
whole frame to the dendrite. The set, frame count, scroll length and caption positions are in `data/site.yaml`
(`hero:`). The `eyemap-*` sets are kept because the build script reads them.

## Sets

| Folder | Frames | Size | Pixels | Source |
|---|---|---|---|---|
| `eyemap-desktop/` | `f_0001.webp … f_0180.webp` + `poster.jpg` | 15.4 MB | 1920x1080 | **Re-render** of Marisa's eye-map Blender scene (Blender 5.2.1, EEVEE), new camera timing, background #171513 |
| `eyemap-mobile/` | `f_0001.webp … f_0180.webp` + `poster.jpg` | 7.9 MB | 960x1707 (9:16) | Same re-render with a portrait camera (rendered 1080x1920); the subject stays centered |
| `t4-desktop/` | `f_0001.webp … f_0180.webp` + `poster.jpg` | 13.0 MB | 1920x1080 | **Marisa's rendered frames** of the T4 animation (her frames 1104–1664), re-timed; background #000000 |
| `t4-mobile/` | `f_0001.webp … f_0180.webp` + `poster.jpg` | 5.0 MB | 960x1707 (9:16) | Moving crop of the same frames (not a portrait render) |

`poster.jpg` is frame 1 of its set (the fly head, front view). WebP quality: 84 (desktop sets), 52 (eyemap-mobile),
47 (t4-mobile).

**Recommended hero: `eyemap-desktop` + `eyemap-mobile`.** The `t4-*` sets are an alternative for comparison
(head, whole-brain EM neuropil, lobula plate, T4a–d cells). They are darker and the subject is small. Delete
the pair that is not used before `media/hero/` is committed.

A third option is kept outside the repo history in `media/sources/hero-marisa/sequences/eyemap-frames-*`:
the same eye-map story cut directly from Marisa's own frames (her original shading and black background, one
cross-dissolve in the middle, head centered).

## Camera rests (scroll progress, 0 = top of the hero, 1 = end)

Both `eyemap` sets and both `t4` sets use the same timing. Frame number = `round(p * 179) + 1`.

| Progress | Frames | eyemap | t4 |
|---|---|---|---|
| 0.00–0.16 **rest 1** | 1–30 | Fly head, front view, very slow push-in | Fly head, front view |
| 0.16–0.26 move | 30–48 | Into the right eye; the head dissolves into the micro-CT section | Head dissolves; the brain appears |
| 0.26–0.50 **rest 2** | 48–90 | Retina section: photoreceptors turn orange, tips appear, then the lens row (complete by 0.40) | Whole-brain EM neuropil between the lens arrays |
| 0.50–0.68 move | 90–123 | Along the section to one lens, one photoreceptor, lamina, L1, medulla, Mi1 | Into the optic lobe, to a T4 cell in the lobula plate |
| 0.68–1.00 **rest 3** | 123–180 | Mi1 neurons of neighboring columns and the M10 column markers appear | T4b, T4c, T4d join T4a |

In the rests the picture changes about ten times more slowly than in the moves (measured mean frame-to-frame
difference: 0.4, 1.1, 0.9 in the rests; 9 and 12 in the moves).

Desktop framing of `eyemap-desktop`: the page sets its text in the left half, so the subject sits right of
center. The head is centered at about 68% of the width, the lens row at about 46%, and the Mi1 neurons at
60–90%. In `eyemap-mobile` the subject is centered.

## What to change to use a set

The stop positions in `mockups/templates/home.html` (0.00–0.18, 0.28–0.52, 0.68–0.97 as of 2026-11-13) match
these rests. No change is needed there.

1. `data/site.yaml`: `hero.frames: 180` (was 192).
2. `build.py`: the hero frames are copied from `mockups/hero-frames` in two places
   (`copy_tree(MOCKUPS / "hero-frames", OUT / "media" / "hero" / "v0")` in `render_site` and
   `copy_tree(MOCKUPS / "hero-frames", out / "hero-frames")` in `render_mockups`). Copy
   `media/hero/eyemap-desktop` instead. For phones, also copy `media/hero/eyemap-mobile` (for example to
   `media/hero/v0-mobile/`) and add a path for it (`P.hero_mobile`).
3. `mockups/templates/home.html`: the attributes stay `data-frames="{{ site.hero.frames }}"` and
   `data-pattern="{{ P.hero }}f_%04d.webp"`. The poster can stay `{{ P.hero }}f_0001.webp` or become
   `{{ P.hero }}poster.jpg`. For phones add `data-pattern-mobile="{{ P.hero_mobile }}f_%04d.webp"` to the
   `<section>`, and give the poster a portrait source:
   `<picture><source media="(max-aspect-ratio: 4/5)" srcset="{{ P.hero_mobile }}poster.jpg"><img class="hero-poster" …></picture>`.
4. `mockups/shared/hero.js` reads one pattern. To use the portrait set, replace
   `const pattern = el.dataset.pattern;` with:
   ```js
   const portrait = window.matchMedia('(max-aspect-ratio: 4/5)').matches;
   const pattern = (portrait && el.dataset.patternMobile) || el.dataset.pattern;
   ```
   Without this, a phone shows the center strip of the desktop frames, and the head (right of center) is cut.
5. `mockups/shared/base.css`: `.hero { background: #000; }` → `#171513`, so the hero has the frames' background
   before they load and at the edges. (`t4-*` frames have a pure black background; keep `#000` for those.)
6. Credit: `site.hero.credit` already reads "Animation by Marisa Dreher, from Zhao et al. 2025".
7. The `og:image` of the home page should point at `poster.jpg` of the desktop set.

## Checked in a browser

Chrome, 1614x934 window at 2x, with unmodified copies of `hero.js`, `base.css`, `e.css` and the hero markup
(test page: `media/sources/hero-marisa/browser-test/`):

- All 180 frames load; scrubbing forward and backward shows the expected frame at each of 180 scroll
  positions (in the rests a neighbor that is visually identical was sometimes the closest match).
- A 3 s and a 0.7 s pass over the whole hero, each way, ran at the display rate with no frame over 34 ms.
- With the current stops the text is on screen at 0.00–0.18, 0.285–0.52 and 0.68–0.97. Each text block is up
  only while the camera rests, apart from the first and last 0.02 of a move.
- `eyemap-mobile` in 390x780 viewports: head, lens row and neurons are centered at the three rests. The page
  centers its text too, so on a phone the text lies over the subject. That is a page-layout decision.

## Known differences from Marisa's movie

- The view-direction arrows are left out (they need narration). The whole-eye orbit (her frames 432–780) is
  skipped: the camera goes straight from the lens row to the single-lens view.
- Blender 5.2 (EEVEE Next) no longer draws the crisp shadows that her neurons cast on the section, so L1 and
  Mi1 look a little paler than in her frames. Head, lenses and section match closely.
- The re-render masters are RGBA. Another background color needs only a new composite and encode (two
  commands in `SOURCES.md`), not a new render.
