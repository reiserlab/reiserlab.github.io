# How to update reiserlab.org

Everything on the site comes from the files in `data/` and `media/`. You never edit HTML. Push to `main` and GitHub rebuilds and deploys the site in two or three minutes (watch the Actions tab).

You can make any of these edits in the GitHub web editor (open the file, click the pencil, commit to `main`). Or ask Claude Code: "add this paper to the website" with the DOI.

## Add a paper

1. Open `data/publications.yaml`. Copy an existing entry and change the fields: `id` (unique, e.g. `lastname2026keyword`), `title`, `authors`, `year`, `venue`, `doi`, `pillars`.
2. Pick one or more pillars from: `anatomy`, `behavior`, `neurophysiology`, `methods`, `modeling`.
3. Set `selected: true` if it should be featured on the home page (keep four to six selected at a time; unselect an older one).
4. Add the figure: put a PNG or JPG (at least 2400 px wide, 3:2 crop) in `media/figures/` and set `figure: filename.png`. The build makes the small versions.
5. Add links if you have them: `preprint`, `pdf`, `code`, `data`, `explorer`, `video`.
6. Write the news item (below) in the same sitting.

## Post news

Open `data/news.yaml` and add an entry at the top:

```yaml
- date: 2026-11-02
  tag: paper
  title: One line that stands on its own
  text: One or two sentences.
  link: https://...
```

Tags: `paper`, `preprint`, `resource`, `people`, `course`, `talk`, `award`.

## Add or move a person

Open `data/people.yaml`. New member: copy an entry, set `status: current`, add a portrait to `media/people/` (3:4 crop, at least 1200 px tall) and set `photo:`. Someone leaves: change `status` to `alumni`, add `years: "2021–2026"` and `where_now: "Postdoc, University of X"`.

## Add a resource

Open `data/resources.yaml`, copy an entry, pick an existing `group` (or add a new one to `resource_groups` in `data/site.yaml`), fill in `name`, `url`, `line`, and optionally `repo`, `version`, `license`, `image`.

## Build locally (optional)

```bash
uv run build.py --serve
```

Then open http://localhost:8000. The build fails with a clear message if an entry is missing a required field or a figure file is not found.

## Credits

Every image and video has an entry in `media/credits.yaml` (source paper, figure or movie number, creator, license). Add one when you add a file.
