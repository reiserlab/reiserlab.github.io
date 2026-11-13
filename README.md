# reiserlab.org

New Reiser Lab website: a static site hosted on GitHub Pages from `reiserlab/reiserlab.github.io`, served at https://reiserlab.org.

Status (2026-11-13): the site is live at https://reiserlab.github.io/ in design E (warm scientific journal), with Home, Publications, People and Resources. The custom domain is not switched on yet; see docs/plan.md section 10 for the go-live checklist.

## Build

```bash
uv run build.py --serve
```

Builds `site/` from `data/`, `media/`, `templates/` and `static/`, then serves it at http://localhost:8000. GitHub Actions runs the same build on every push to `main` and deploys to GitHub Pages. See [HOW-TO-UPDATE.md](HOW-TO-UPDATE.md) for adding papers, people, news and resources.

## Layout

- `build.py` — the generator (Python, Jinja2, Pillow). `data/*.yaml` — all content (site settings and home-page wording, publications, people, news, resources, join). `media/` — paper figures, portraits, hero frames, and `credits.yaml`.
- `mockups/` — templates (`templates/`), styles and scripts (`shared/`), loops (`media/`) and stills (`img/`). The design named by `design:` in `data/site.yaml` is rendered at the site root; all six variants are also rendered under `/mockups/` for reference. The folder name is historical.
- `tools/merge_figures.py` — merges figure records into the publication data and credits.
- `docs/` — plan, media plan, research notes, drafts.

- [docs/plan.md](docs/plan.md) — the plan: goals, hosting and DNS, site structure, design direction, technical approach, how to keep it updated, half-day work plan, open decisions.
- [docs/media-plan.md](docs/media-plan.md) — one proposed figure per paper, videos to use, media processing spec, collection checklist.
- [docs/research/current-site-inventory.md](docs/research/current-site-inventory.md) — the Janelia page today, every lab resource URL, publications 2023–2026, members.
- [docs/research/dudmanlab-design-analysis.md](docs/research/dudmanlab-design-analysis.md) — the main design inspiration, analyzed from its source.
- [docs/research/inspiration-sites.md](docs/research/inspiration-sites.md) — other clean lab sites (with screenshots) and template options.
- [docs/drafts/marisa-blender-request.md](docs/drafts/marisa-blender-request.md) — draft note asking for the Blender files behind the eye-map animations (not sent).
- [docs/research/hero-source/](docs/research/hero-source/) — contact sheets of the two candidate hero animations.
