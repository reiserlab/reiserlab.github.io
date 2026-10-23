# dudmanlab.org — design analysis (fetched 2026-10-23)

Reference notes for the reiserlab.org redesign. dudmanlab.org is the main inspiration, but the new site should not copy it. Statements below come from the site's HTML and CSS source, not from a rendered screenshot.

## 1. Site map

Flat, six-item navigation. All pages share one header (logo + hamburger that opens a 360px right-side drawer) and one footer.

| Nav label | Path | Notes |
|---|---|---|
| Home | `/index.html` | Landing page |
| Team | `/html/about.html` | Current Members, Collaborators, Visiting Scientists, Our values, Alumni, Work With Us |
| Research | `/html/research.html` | Intro + 4 themes + "Projects for Students"; in-page sub-nav |
| Publications | `/html/publications.html` | Selected work, Complete archive (by year), Commentary & Press, Other publications |
| Resources | `/html/resources.html` | 12 tools/datasets/hardware items |
| News | `/html/news.html` | Featured post (placeholder), Lab News, Newsletter (Substack, not wired), Commentary & Press |

Secondary pages linked from Research/Resources: dynamics, learning, models, rivets. Per-paper "project resources" pages live off-site on Notion. Footer on every page: three link columns (Lab / Connect / Institution), Janelia logo, social icon row (Google Scholar, GitHub, Bluesky, ResearchGate, ORCID), copyright.

## 2. Home page layout

Above the fold (100vh): a full-bleed background animated GIF (800x800 px, 55 MB) of a multiplex in situ hybridization section, stretched to cover the viewport, with a left-weighted darkening gradient. Left-aligned on top:
- Wordmark h1 "**Dudman**Lab" (serif, `clamp(64px, 9vw, 128px)`, "Dudman" weight 780, "Lab" weight 300, letter-spacing -0.06em).
- Tagline "neural circuits · behavior · computation · physiology", each word in a different accent color (teal / rose / gold / violet).
- One outlined button "Get Started" that smooth-scrolls to the tiles; a chevron scroll cue.
- The fixed top nav is hidden on the home page until you scroll past the hero. Subpages always show the nav.

Section order below the fold:
1. Tiles: six full-bleed image tiles in alternating 60/40 then 40/60 widths, 400–480px tall, image + dark overlay + bottom-left text (eyebrow, title, short rule, one-line description). Whole tile clickable.
2. About band: 2x2 grid of icon + one-sentence statements (location, who we are, Janelia community, open science). About 90 words total.
3. Latest News: 4-column grid of 8 text-only cards (10px uppercase tag, 14px light text, 12px link). No dates, no images.
4. CTA band: "Explore our research program in depth" + outlined button.
5. Get in Touch: recruiting paragraph + 4-field contact form (PHP) + mailto; right column with location and a Spotify playlist embed.
6. Footer.

Text volume is low: mostly imagery, labels and one-liners.

## 3. Content presentation

**Research**: short dark banner; an intro essay (the longest prose on the site); four theme sections, each with 2–3 paragraphs, an animated GIF or banner image, and a "Featured Papers" row of three paper thumbnails; "Read more" links to deeper pages. A "Projects for Students" section is text only.

**Publications**:
- "Selected work": 4-column grid of 360px-tall image cards with a year badge, "Project Resources" badge, people pills, and a hover overlay with journal, one-sentence summary and a link to Notion.
- "Complete archive": two-column CSS grid, year heading in column 1 (teal, 13px uppercase), rows in column 2. Each row: 104x70 thumbnail, title, italic venue, right-aligned icon links (Link, PDF, Open Access, Materials, bioRxiv, GitHub, DOI, Figshare, Data). Authors are not listed. About 43 entries, 2009–2026, no search or filter.
- "Commentary & Press" and "Other publications".

**People**: banner + one-line tagline; "Current Members" (8) and "Collaborators" as a 4-column card grid: 350px-tall portrait (`object-fit: cover`, `filter: grayscale(70%) brightness(0.9)`, colorizes on hover), name, role, icon links. No bios. "Our values" prose. "Alumni" (20) as a 4-column text grid: name / former role / current position. "Work With Us" repeats the recruiting blurb and form.

**Resources**: 12 items, each with image, name, one-line description, and outbound links; grouped loosely with a "Software & Hardware" subheading.

**News**: single-column stacked entries with small label + title + "Read" link, undated. Visibly unfinished (placeholder featured post, Substack block stuck loading).

## 4. Visual design

**Typography**
- Serif (`"Iowan Old Style", "Palatino Linotype", Palatino, Georgia`) only for page-title h1s and the wordmark. Banner h1: `400 clamp(58px, 7vw, 104px)/0.94`, letter-spacing -0.052em.
- Sans (`Inter, Outfit, ui-sans-serif, system-ui`) for body at `15px/1.62`. Only Outfit (300–700) is actually loaded from Google Fonts.
- Eyebrows/section titles: `700 10px/1.3`, letter-spacing 0.18em, uppercase, teal. Year headings: 700 13px, 0.13em.
- Body weights lean light (300) for descriptive text, 500–600 for links and names.
- Icon fonts: Font Awesome and Academicons.

**Color palette** (CSS custom properties; dark theme default, light theme defined for subpages)

| Token | Dark | Light |
|---|---|---|
| ground | `#171a1e` | `#e9ebe7` |
| ground-2 | `#202328` | `#f4f3ee` |
| panel | `#272b30` | `#fffefa` |
| panel-2 | `#2d3137` | `#f6f5f0` |
| ink | `#f1f4f3` | `#182220` |
| muted | `#a6b0ad` | `#5d6966` |
| faint | `#77817f` | `#7b8582` |
| rule | `rgba(255,255,255,.12)` | `rgba(23,35,32,.15)` |
| teal | `#70b9c9` | `#176f77` |
| rose | `#d98fa2` | `#a64f67` |
| gold | `#dfb66b` | `#9a6818` |
| violet | `#a99bd4` | `#66559c` |

Each accent also has a soft 10–13% tint for card accents. The logo is a circle containing a line-drawn mouse and a brain whose branches are circuit traces in the same four colors, so tagline, icons, and logo share one four-color system.

**Whitespace, grid, images**: content column max 1180px; section padding 80px/60px desktop, 50px/24px mobile. Grids are 4 columns collapsing to 3/2/1 at 1100/991/768/640px. Corners nearly square (2–6px). Dividers are 1px low-alpha rules; cards near-transparent with a 2–3px colored left border on hover. Nav uses `backdrop-filter: blur(16px)`. Imagery is almost all the lab's own microscopy plus one Janelia campus photo, used as dark full-bleed backgrounds behind white text. Portraits desaturated. `prefers-reduced-motion` respected; focus rings in the teal accent.

## 5. Tech stack and hosting

- Hand-written static HTML, no generator, no build tooling. Class names come from the HTML5 UP "Forty" template; a newer "Studio" CSS layer restyles it with CSS variables (`last-modified: 20 Oct 2026`, so the redesign is in progress).
- CSS: Bootstrap 3.3.2 (unused for layout), Font Awesome, Academicons, Google Fonts (Outfit). JS: a few inline vanilla scripts.
- Analytics: dead Universal Analytics tag.
- Dynamic pieces: PHP mail handler; Spotify embed; Substack embed (not working); Notion for per-paper materials pages.
- Hosting: DreamHost shared hosting (Apache), no CDN. Domain registered 2011.
- Performance liabilities: 55 MB hero GIF, 10.6 MB publications background PNG, several 2–4 MB tile PNGs, 578 KB logo SVG, unused Bootstrap.

## 6. Assessment

**Why it feels clean and modern**
- A single dark, low-contrast neutral scale with text at graded alpha levels; hierarchy from weight and opacity rather than boxes.
- One restrained four-color accent system used consistently and never as large fills.
- Big display type against tiny letter-spaced uppercase eyebrows, with few intermediate sizes.
- Near-square corners, 1px rules, hover-only color, generous section padding.
- The lab's own fluorescence microscopy as full-bleed photography; no stock photos.
- Sparse copy on the home page; prose pushed to Research.

**Ideas worth borrowing in spirit**
1. Design tokens first: ground/panel/ink/muted/rule plus a small accent set as CSS variables, with a real light theme alongside.
2. A one-line tagline naming the lab's three or four pillars, each tied to an accent color that recurs.
3. Research themes as large clickable image tiles with eyebrow + title + one line, leading to deeper pages with featured papers.
4. Publications as two levels: a few featured projects with image and resources link above a compact year-indexed archive with an icon row (PDF / preprint / code / data) instead of a wall of citations.
5. Alumni as a dense name / former role / where-now grid.
6. The lab's own data imagery as backgrounds, darkened, with text on top.
7. Free accessibility touches: reduced-motion, visible focus rings, aria labels.

**Do deliberately differently**
- Go light-first (or warm paper tone) with dark mode as the alternate.
- Avoid the serif-display + Outfit pairing; pick a different type voice.
- Not teal/rose/gold/violet; two accents, not four.
- Hero: a muted still or a short video loop under 2 MB, or a type-led intro; keep the nav visible from the start.
- Skip the alternating 60/40 tile mosaic and the hidden-until-scroll nav.
- People: short bios, portraits in color.
- Publications: include authors; add year or topic filter.
- News: date every item.
- Resources: group explicitly (Hardware / Software / Data / Protocols) with version and license lines.
- Engineering: static site generator with publications and people as data files; optimized images; no Bootstrap.
- Avoid the Spotify embed and the circular animal-brain logo concept.
