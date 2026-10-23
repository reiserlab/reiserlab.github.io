# Inspiration: clean, modern neuroscience lab sites (surveyed 2026-10-23)

Method: each site was fetched and screenshotted at 1440 px; the stack was read from HTTP headers, generator meta tags, and CSS class prefixes. Screenshots are in [screenshots/](screenshots/) (for example `steinmetz.png`, `mathis.png`, `behnia.png`). Dudman Lab is covered separately in [dudmanlab-design-analysis.md](dudmanlab-design-analysis.md).

## Top three to emulate

1. **Steinmetz Lab** (UW) — https://www.steinmetzlab.net/ — [screenshot](screenshots/steinmetz.png)
   The best-designed systems-neuroscience lab site found. Dark green-black ground, huge condensed uppercase headline with one accent-color word, a live Neuropixels raster behind the hero text, then numbered "core research questions" cards whose images are real data figures. Publications grouped by year with topic filter chips and an author-copy PDF per paper. People grouped by role; alumni with date ranges and "now at".
   Most relevant of all: its public source, https://github.com/SteinmetzLab/website-v2, is JSON data files (`pubs.json`, `people.json`, `news.json`, `alumni.json`) rendered by a 37 KB Python `build.py` into static HTML, deployed by GitHub Actions on push, with an `EDITING.md` written for busy scientists. That is exactly the low-maintenance GitHub Pages architecture we want.

2. **Mathis Group** (EPFL, Alexander Mathis) — https://cnai.epfl.ch/ — [screenshot](screenshots/mathis.png)
   The cleanest light-theme reference. Bold sans headline with gradient-colored keywords, two buttons, three "Research Directions" cards with icons and project tags, "Latest Research" cards with thumbnails, light/dark toggle, lots of white space. Publications filterable by year and type with link buttons (arXiv, DOI, Code, Website). Stack: Next.js static export on GitHub Pages with a custom domain.

3. **Behnia Lab** (Columbia, fly vision) — https://www.behnialab.neuroscience.columbia.edu/ — [screenshot](screenshots/behnia.png)
   Shows how far a fly-vision lab gets with one great macro photograph (a fly on a rig, credited), a spaced-caps wordmark, and three paragraphs. Calm and confident. Stack: Squarespace, but the look is trivial to reproduce statically. Murthy Lab (Princeton, https://murthylab.princeton.edu/, [screenshot](screenshots/murthy.png)) is the runner-up for the same reasons: spaced-caps nav, thin centered headline, full-width image bands between text blocks.

## Others worth a look

| Lab | URL | Why look | Stack |
|---|---|---|---|
| Pachitariu + Stringer (Janelia) | https://mouseland.github.io/ ([shot](screenshots/mouseland.png)) | A Janelia lab already running a zero-cost GitHub Pages site. Utilitarian, but the two-photon movie as the hero and the "On this page" sidebar are good. | Quarto on GitHub Pages |
| Portugues Lab (Cornell) | https://www.portugueslab.com/ ([shot](screenshots/portugues.png)) | Warm cream ground, one accent color; the home page *is* the news feed, a large featured image with a dated caption and a thumbnail ticker. Publications each have a journal-cover thumbnail. | Hand-written HTML plus one JS data file |
| Takeoka Lab (RIKEN) | https://takeokalab.riken.jp/ ([shot](screenshots/takeoka.png)) | Full-viewport microscopy hero slider with one-phrase captions; the Hugo "research group" look done well. | Hugo Blox |
| Tuthill Lab (UW, fly proprioception) | https://faculty.washington.edu/tuthill/ ([shot](screenshots/tuthill.png)) | Dated template, but the banner is a physiology trace: "data as hero image". | Hand-written HTML (HTML5 UP) |
| Kennedy Lab (Scripps) | https://www.kennedylab.org/ ([shot](screenshots/kennedy.png)) | Research questions as a bulleted list and a dated news list on the home page. | Wix |
| Churchland Lab (UCLA) | https://churchlandlab.dgsom.ucla.edu/ ([shot](screenshots/churchland.png)) | Restraint inside a university CMS: one wide microscopy hero, short text. | Drupal |
| Znamenskiy Lab (Crick) | https://znamlab.org/ ([shot](screenshots/znam.png)) | The minimum viable Jekyll site on GitHub Pages with a custom domain. | Jekyll + Bootstrap on GitHub Pages |
| Dickinson Lab (Caltech) | https://dickinsonlab.caltech.edu/ ([shot](screenshots/dickinson.png)) | Dated, but "latest papers on the home page" as a column works. | WordPress |
| Allen Institute | https://alleninstitute.org/ | Design reference only (type system, card grid, dated news cards); far too heavy for a lab. | Webflow |

Checked and not useful as inspiration: Card, Turner, Jayaraman, Ahrens (all on the Janelia Drupal template); Clandinin (Weebly, one paragraph); Silies (university WordPress skin, footer says "last update 2021"); Frye, Fitzgerald, Luo, Bhandawat, Borst (institutional templates); Engert (Wix, neon on black, charming but not clean); Zador (nearly empty home page with a cookie banner); Datta (text-forward WordPress). Wilson, Sabatini, Maimon could not be fetched. Seelig's group has closed; Scott is emerita.

## Patterns that recur across the good sites

- **A data image as the hero**, not stock photography: a raster, a two-photon movie, a trace, a neuron rendering (Steinmetz, Tuthill, MouseLand). For us: an anatomy video loop.
- **"Selected" papers on the home page driven by a flag in the data file**, full list on its own page with year headers and topic filters (Steinmetz, Mathis).
- **People grouped by role with alumni and "now at"** (all of the top sites).
- **News as a dated list that doubles as the home-page feed** (Portugues, Kennedy, Takeoka).
- **Spaced-caps wordmark, one accent color, lots of white** (Behnia, Murthy).
- **Content in data files, markup generated** (Steinmetz, Portugues, MouseLand), which is what keeps a site updated by non-developers.

## Templates and stacks for a GitHub Pages lab site

| Option | Repo | Stars / last push | Lab features | Weight | Add a paper or news item |
|---|---|---|---|---|---|
| **Hand-rolled generator** (Steinmetz model) | https://github.com/SteinmetzLab/website-v2 as reference | n/a | Whatever we build: people, alumni, news, publications with `selected` and tags | Lightest: a 20-line Actions step running `python build.py`; nothing to upgrade, ever | One JSON or YAML object in the GitHub web editor; Actions rebuilds in 2–3 min |
| sbryngelson/academic-website-template (Jekyll) | https://github.com/sbryngelson/academic-website-template | 387 / 2026-10-17 | Built for groups: team, alumni, news, funders, software YAML; publications from BibTeX; dark mode; search | Jekyll + jekyll-scholar in Actions | Two YAML lines for news; paste BibTeX for a paper. Easiest template for a non-developer |
| al-folio (Jekyll) | https://github.com/alshedivat/al-folio | 16,268 / 2026-10-19 | Personal theme with people page, BibTeX publications, news, projects | Heaviest Jekyll option; long config; frequent upstream releases | Markdown file for news; BibTeX for a paper; occasional upgrade work |
| allanlab/allanlab (Jekyll) | https://github.com/allanlab/allanlab | 317 / 2026-10-23 | The classic lab template (1,350 forks): team, alumni, news, publications as YAML with thumbnails | Plain Jekyll, no Actions needed | YAML blocks; dated look unless restyled |
| Hugo Blox research group | https://github.com/HugoBlox/theme-research-group | 402 / 2024-10-12 | Team, BibTeX import, news, light/dark | Hugo is fast, but the ecosystem has churned (Wowchemy → Hugo Blox → Tailwind rewrite) and the group template is unmaintained | Markdown folders; migration risk is the real cost |
| Quarto website | https://github.com/MouseLand/MouseLand.github.io as example | Quarto 6,118 / active | Listings for news; people as pages; publications hand-written or from .bib via a script | Light; official Actions workflow | `.qmd` per post; Markdown line per paper; natural for R/Quarto users, plain look by default |
| Astro (custom or astro-scholar) | https://github.com/shravanngoswamii/astro-scholar | 31 / 2026-06-10 | Team JSON, BibTeX publications, Markdown blog, search | Node build in Actions; young template, one maintainer | Markdown or BibTeX; Astro majors move quickly |

Not recommended: Minimal Mistakes and academicpages (blog/portfolio themes without people or BibTeX features); any Squarespace/Wix/Webflow plan (recurring cost, no version control, and the good-looking ones above are easy to reproduce statically).

## Recommendation

Do not adopt an academic theme. Build a small custom site in the Steinmetz style: data files plus a short Python generator, deployed by GitHub Actions. It is the only option with zero dependency rot, it matches how the lab already generates the Cell Type Explorer pages (neuView is a Python static generator), and Claude Code can write the generator and templates in one session. If a richer developer experience is wanted later, Astro is the alternative; the data files would carry over unchanged.
