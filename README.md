# reiserlab.org

New Reiser Lab website: a static site hosted on GitHub Pages from `reiserlab/reiserlab.github.io`, served at https://reiserlab.org.

Status (2026-10-23): scaffold deployed. A placeholder page and three design mockups are live at https://reiserlab.github.io/ (mockups at `/mockups/`). The custom domain is not switched on yet; see docs/plan.md section 2 for the DNS sequence.

## Build

```bash
uv run build.py --serve
```

Builds `site/` from `data/`, `media/`, `templates/` and `static/`, then serves it at http://localhost:8000. GitHub Actions runs the same build on every push to `main` and deploys to GitHub Pages. See [HOW-TO-UPDATE.md](HOW-TO-UPDATE.md) for adding papers, people, news and resources.

## Layout

- `build.py` — the generator (Python, Jinja2, Pillow). `data/*.yaml` — all content. `templates/` — page templates. `static/` — CSS and JS. `media/` — figures, portraits, loops, and `credits.yaml`.
- `mockups/` — home-page design mockups: one template, three token sets (`variants.yaml`, `shared/*.css`), the scroll-hero script (`shared/hero.js`), placeholder stills and frames from the eye-map animation. Remove once a direction is chosen.
- `docs/` — plan, media plan, research notes, drafts.

- [docs/plan.md](docs/plan.md) — the plan: goals, hosting and DNS, site structure, design direction, technical approach, how to keep it updated, half-day work plan, open decisions.
- [docs/media-plan.md](docs/media-plan.md) — one proposed figure per paper, videos to use, media processing spec, collection checklist.
- [docs/research/current-site-inventory.md](docs/research/current-site-inventory.md) — the Janelia page today, every lab resource URL, publications 2023–2026, members.
- [docs/research/dudmanlab-design-analysis.md](docs/research/dudmanlab-design-analysis.md) — the main design inspiration, analyzed from its source.
- [docs/research/inspiration-sites.md](docs/research/inspiration-sites.md) — other clean lab sites (with screenshots) and template options.
- [docs/drafts/marisa-blender-request.md](docs/drafts/marisa-blender-request.md) — draft note asking for the Blender files behind the eye-map animations (not sent).
- [docs/research/hero-source/](docs/research/hero-source/) — contact sheets of the two candidate hero animations.
