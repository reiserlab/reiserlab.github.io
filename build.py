#!/usr/bin/env python3
"""Static site generator for reiserlab.org.

Reads YAML in data/, media in media/, templates in templates/, static assets in
static/, and writes the finished site to site/. Run `uv run build.py` (or
`python build.py` with jinja2, pyyaml and pillow installed). `--serve` builds
and then serves site/ on http://localhost:8000. `--no-mockups` skips the
design mockups under /mockups/.
"""
from __future__ import annotations

import argparse
import datetime as dt
import http.server
import shutil
import sys
from functools import partial
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader
from PIL import Image

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
MEDIA = ROOT / "media"
STATIC = ROOT / "static"
TEMPLATES = ROOT / "templates"
MOCKUPS = ROOT / "mockups"
OUT = ROOT / "site"

FIGURE_WIDTHS = (400, 800, 1600)
PILLARS = {"anatomy", "behavior", "neurophysiology", "methods", "modeling"}


class BuildError(Exception):
    pass


# ----------------------------------------------------------------------------
# data


def load_yaml(name: str):
    path = DATA / name
    with path.open() as fh:
        data = yaml.safe_load(fh)
    return data if data is not None else []


def require(entry: dict, keys: tuple[str, ...], where: str) -> None:
    missing = [k for k in keys if not entry.get(k)]
    if missing:
        raise BuildError(f"{where}: missing {', '.join(missing)}")


def check_pillars(entry: dict, where: str) -> None:
    bad = set(entry.get("pillars", [])) - PILLARS
    if bad:
        raise BuildError(f"{where}: unknown pillars {sorted(bad)}; allowed {sorted(PILLARS)}")


def load_data() -> dict:
    site = load_yaml("site.yaml")
    pubs = load_yaml("publications.yaml")
    people = load_yaml("people.yaml")
    news = load_yaml("news.yaml")
    resources = load_yaml("resources.yaml")
    join = load_yaml("join.yaml") if (DATA / "join.yaml").exists() else {}

    ids = set()
    for p in pubs:
        where = f"publications.yaml entry {p.get('id', '?')}"
        require(p, ("id", "title", "authors", "year", "venue", "pillars"), where)
        if not (p.get("doi") or p.get("url")):
            raise BuildError(f"{where}: needs a doi or a url")
        if p["id"] in ids:
            raise BuildError(f"{where}: duplicate id")
        ids.add(p["id"])
        check_pillars(p, where)
        p.setdefault("links", {})
        p.setdefault("selected", False)
        p.setdefault("type", "journal")
        if p.get("doi") and "doi" not in p["links"]:
            p["links"]["doi"] = f"https://doi.org/{p['doi']}"
        if p.get("figure"):
            src = MEDIA / "figures" / p["figure"]
            if not src.exists():
                raise BuildError(f"{where}: figure {src.relative_to(ROOT)} not found")
    pubs.sort(key=lambda p: (p["year"], str(p.get("date") or "")), reverse=True)
    # Preprints with a published version become a "preprint" link on that version and drop out of the list.
    by_id = {p["id"]: p for p in pubs}
    for p in pubs:
        target = by_id.get(p.get("preprint_of") or "")
        if target is not None:
            target["links"].setdefault("preprint", f"https://doi.org/{p['doi']}" if p.get("doi") else p.get("url"))
            if not target.get("figure") and p.get("figure"):
                target["figure"] = p["figure"]
    pubs_all = pubs
    pubs = [p for p in pubs if not p.get("preprint_of")]

    for person in people:
        where = f"people.yaml entry {person.get('name', '?')}"
        require(person, ("name", "role", "status"), where)
        check_pillars(person, where)
        if person.get("photo") and not (MEDIA / "people" / person["photo"]).exists():
            raise BuildError(f"{where}: photo not found")

    for item in news:
        where = f"news.yaml entry {item.get('title', '?')}"
        require(item, ("date", "title"), where)
        if not isinstance(item["date"], dt.date):
            raise BuildError(f"{where}: date must be YYYY-MM-DD")
    news.sort(key=lambda n: n["date"], reverse=True)

    for r in resources:
        where = f"resources.yaml entry {r.get('name', '?')}"
        require(r, ("group", "name", "url", "line"), where)

    return {
        "site": site,
        "publications": pubs,
        "publications_all": pubs_all,
        "selected": [p for p in pubs if p["selected"]],
        "people": people,
        "current": [p for p in people if p["status"] == "current"],
        "alumni": [p for p in people if p["status"] == "alumni"],
        "news": news,
        "resources": resources,
        "resource_groups": group_resources(resources, site.get("resource_groups", [])),
        "join": join,
        "built": dt.date.today(),
    }


def group_resources(resources: list[dict], order: list[str]) -> list[tuple[str, list[dict]]]:
    groups: dict[str, list[dict]] = {}
    for r in resources:
        groups.setdefault(r["group"], []).append(r)
    names = [g for g in order if g in groups] + [g for g in groups if g not in order]
    return [(g, groups[g]) for g in names]


# ----------------------------------------------------------------------------
# media


def newer(src: Path, dst: Path) -> bool:
    return not dst.exists() or src.stat().st_mtime > dst.stat().st_mtime


def process_figures() -> None:
    """Write WebP renditions of every figure at the layout's widths."""
    src_dir = MEDIA / "figures"
    if not src_dir.exists():
        return
    out_dir = OUT / "media" / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted(src_dir.iterdir()):
        if src.suffix.lower() not in {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp"}:
            continue
        for width in FIGURE_WIDTHS:
            dst = out_dir / f"{src.stem}-{width}.webp"
            if not newer(src, dst):
                continue
            with Image.open(src) as im:
                im = im.convert("RGB")
                if im.width > width:
                    im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
                im.save(dst, "WEBP", quality=82, method=6)


def copy_tree(src: Path, dst: Path, ignore=None) -> None:
    if src.exists():
        shutil.copytree(src, dst, dirs_exist_ok=True, ignore=ignore)


# ----------------------------------------------------------------------------
# rendering

PAGES = [
    ("index.html", "index.html"),
    ("publications.html", "publications/index.html"),
]


def make_env(search: list[Path]) -> Environment:
    env = Environment(
        loader=FileSystemLoader([str(p) for p in search]),
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["month_year"] = lambda d: d.strftime("%B %Y")
    env.filters["long_date"] = lambda d: d.strftime("%B %-d, %Y")
    return env


def render_pages(ctx: dict) -> None:
    env = make_env([TEMPLATES])
    for template_name, out_name in PAGES:
        html = env.get_template(template_name).render(**ctx)
        target = OUT / out_name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(html)


def render_mockups(ctx: dict) -> None:
    """Design mockups: one home-page template rendered against several CSS variants."""
    variants = yaml.safe_load((MOCKUPS / "variants.yaml").read_text())
    env = make_env([MOCKUPS / "templates", TEMPLATES])
    out = OUT / "mockups"
    out.mkdir(parents=True, exist_ok=True)
    copy_tree(MOCKUPS / "shared", out / "shared")
    copy_tree(MOCKUPS / "img", out / "img")
    copy_tree(MOCKUPS / "hero-frames", out / "hero-frames")
    copy_tree(MOCKUPS / "media", out / "media")
    for key, v in variants.items():
        (out / key).mkdir(exist_ok=True)
        html = env.get_template("home.html").render(variant=key, v=v, **ctx)
        (out / key / "index.html").write_text(html)
        (out / key / "publications").mkdir(exist_ok=True)
        pubs = env.get_template("publications.html").render(variant=key, v=v, **ctx)
        (out / key / "publications" / "index.html").write_text(pubs)
    index = env.get_template("mockups-index.html").render(variants=variants, **ctx)
    (out / "index.html").write_text(index)


# ----------------------------------------------------------------------------


def build(include_mockups: bool = True) -> None:
    ctx = load_data()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    copy_tree(STATIC, OUT / "static")
    copy_tree(MEDIA / "people", OUT / "media" / "people")
    copy_tree(MEDIA / "loops", OUT / "media" / "loops")
    process_figures()
    render_pages(ctx)
    if include_mockups and MOCKUPS.exists():
        render_mockups(ctx)
    # Only emit CNAME once DNS for the custom domain exists. Publishing a CNAME
    # earlier would redirect reiserlab.github.io (and every project site under
    # it) to a domain that does not resolve yet.
    domain = ctx["site"].get("domain")
    if domain and ctx["site"].get("domain_live"):
        (OUT / "CNAME").write_text(domain + "\n")
    (OUT / ".nojekyll").write_text("")
    (OUT / "robots.txt").write_text("User-agent: *\nDisallow: /mockups/\n")
    n_pages = len(PAGES)
    print(f"built {n_pages} page(s), {len(ctx['publications'])} publications, "
          f"{len(ctx['current'])} current people, {len(ctx['news'])} news items -> {OUT.relative_to(ROOT)}/")


def serve(port: int) -> None:
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    print(f"serving {OUT.relative_to(ROOT)}/ at http://localhost:{port}  (Ctrl-C to stop)")
    http.server.ThreadingHTTPServer(("", port), handler).serve_forever()


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--serve", action="store_true", help="build, then serve site/ locally")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--no-mockups", action="store_true", help="skip the design mockups")
    args = ap.parse_args()
    try:
        build(include_mockups=not args.no_mockups)
    except BuildError as e:
        print(f"build error: {e}", file=sys.stderr)
        return 1
    if args.serve:
        serve(args.port)
    return 0


if __name__ == "__main__":
    sys.exit(main())
