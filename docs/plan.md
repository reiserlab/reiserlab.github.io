# reiserlab.org — plan

Status: draft for discussion, 2026-10-23. Nothing has been built yet.

Companion documents in this folder:
- [research/current-site-inventory.md](research/current-site-inventory.md) — what the Janelia page has today, every lab resource URL, publications 2023–2026, members.
- [research/dudmanlab-design-analysis.md](research/dudmanlab-design-analysis.md) — what makes dudmanlab.org work, with its actual fonts, colors, and structure.
- [research/inspiration-sites.md](research/inspiration-sites.md) — other clean, modern neuroscience lab sites and template options.
- [media-plan.md](media-plan.md) — one proposed figure per paper, videos to use, and the collection checklist.

---

## 1. Goals and constraints

- **Emphasize** recent work, the breadth of projects, and above all the shared resources: Cell Type Explorers, the visual pathways galleries, Modular LED Displays (G4/G6), Fly Lab Gear, software.
- **Pillars.** The lab's work spans anatomy, behavior, neurophysiology, methods development, and modeling. Five is right as a tagging taxonomy but too many for a home-page grid (five tiles force a 3+2 layout or shrink to postage stamps). Recommendation: **four tiles**, **Anatomy · Behavior · Neurophysiology · Methods**, with **Modeling** as a cross-cutting tag that appears in the tagline, on publication filter chips, and on the papers it belongs to (T5 conductance model, LPTN optic-flow predictions, pathway predictions, whole-body simulation). Methods earns a tile because it is the resources story the site exists to tell. Alternative: a five-word tagline strip in the hero ("anatomy · behavior · physiology · methods · modeling") with four tiles below it. Every research theme, paper, person, and video is tagged with one or more pillars.
- **Visually striking**: one strong figure per paper; the lab's own videos (published movies and unpublished ones) as the main visual material.
- **Clean and simple**: six pages, little prose, no blog-style sprawl.
- **Time budget**: half-days. Everything that can be delegated to Claude Code or a data file should be. The design should be finishable in roughly four half-day sessions after this one.
- **Host on GitHub, serve at reiserlab.org**, independent of the Janelia template. The Janelia lab page stays as a stub that links to the new site.

## 2. Hosting and domain: what is already in place

Checked on 2026-10-23.

| Item | State |
|---|---|
| Domain | **reiserlab.org** is registered to you at Cloudflare (registered 2026-06-16, expires 2027-06-16), nameservers on Cloudflare, **no DNS records yet**. Note: the request said "riserlab.org"; that name is unregistered, so I assume reiserlab.org is the one. |
| GitHub org | `github.com/reiserlab`, you are an admin. 43 public repos, several already serving GitHub Pages sites under `reiserlab.github.io/<repo>/`. |
| Landing repo | `reiserlab/reiserlab.github.io` exists since 2022 with only a LICENSE (CC0) and .gitignore. Pages is enabled on `main`, but the site is empty, so `https://reiserlab.github.io/` returns 404. |

**Answer to "can GitHub forward to reiserlab.org":** yes, and better than forwarding. GitHub Pages serves the site directly at the custom domain with free HTTPS. Steps:

1. Build the site in `reiserlab/reiserlab.github.io` (the org's root Pages site). Deploy with a GitHub Actions workflow instead of the legacy branch build so a static site generator can run.
2. Add a `CNAME` file containing `reiserlab.org` (or set the custom domain in repo Settings → Pages, which creates it).
3. In Cloudflare DNS, add four `A` records for `reiserlab.org` pointing at GitHub Pages (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153), optionally the matching `AAAA` records, and a `CNAME` for `www` → `reiserlab.github.io`. Set these to **DNS only** (gray cloud), not proxied, so GitHub can issue its own certificate. Then turn on "Enforce HTTPS" in the repo's Pages settings.
4. Verify the domain for the org (Settings → Pages → Verified domains) by adding the TXT record GitHub gives. This prevents anyone else from claiming the domain on GitHub Pages.

**Order matters.** Do not set the custom domain on GitHub (neither in Settings → Pages nor via a `CNAME` file) until the Cloudflare records exist. The moment GitHub knows the custom domain, `reiserlab.github.io` and every project site under it (the Cell Type Explorers, the galleries, the display docs) start redirecting to reiserlab.org, which would be a dead domain until DNS resolves. The build therefore writes `CNAME` only when `domain_live: true` in `data/site.yaml`; flip it after the records are in. Sequence: (1) Cloudflare records, (2) wait for `dig reiserlab.org` to return the GitHub IPs, (3) set the custom domain in Settings → Pages (or flip the flag and push), (4) wait for the certificate, (5) tick "Enforce HTTPS", (6) verify the domain for the org.

Status 2026-10-23: the repo builds and deploys through GitHub Actions; a placeholder page and the three mockups are live at https://reiserlab.github.io/ and https://reiserlab.github.io/mockups/. Cloudflare records are not yet added (no API access from here; add them in the dashboard).

Two side effects worth knowing:

- Once the org root site has a custom domain, **every project site in the org is also served under it**: `reiserlab.github.io/visualpathways/` becomes `reiserlab.org/visualpathways/`, and GitHub redirects the old URLs to the new ones. Existing links keep working, and the resources get shorter, lab-branded URLs. A paper's QR code or DOI link to a `reiserlab.github.io` URL will land on `reiserlab.org`.
- Because of that, the website's own paths must not collide with repo names. Avoid a top-level page called, for example, `/neuDiff/` or `/visualpathways/`. Page names like `/research/`, `/publications/`, `/people/`, `/resources/`, `/news/`, `/join/` are safe.

Costs: zero. GitHub Pages limits (1 GB repo, 100 MB per file, 100 GB/month bandwidth) are fine for a site whose videos are kept small; long videos go on the existing ReiserLab YouTube channel and are embedded.

## 3. Site structure

Six pages plus a footer. Every page is short enough to read in a minute.

| Page | Purpose | Contents |
|---|---|---|
| **Home** | Make the pillars and the resources obvious in one screen each | Hero: the scroll-driven head-to-neurons zoom (see section 4a) with the lab name and a one-sentence statement; falls back to a short muted loop or a still where scroll-scrubbing is not appropriate. Four pillar tiles: Anatomy, Behavior, Neurophysiology, Methods, each a short video or image with one line; Modeling named in the tagline. Resources band: four cards (Cell Type Explorers, Visual Pathways galleries, Modular LED Displays, Fly Lab Gear). Recent papers: the last three or four with their figure. News: four dated one-liners. Join and contact strip. |
| **Research** | The breadth of the program, told through the pillars | One intro paragraph. Four sections, one per pillar, each with two or three paragraphs, a video, and three featured papers; the Methods section links heavily to Resources. A short "Modeling and theory" paragraph closes the page, pointing at the papers tagged Modeling. |
| **Publications** | Every paper with one figure | Featured: four to six recent papers as large image cards with a one-sentence summary and resource links. Archive: by year, each entry with a figure thumbnail, title, authors, venue, and icon links (journal, preprint, PDF, code, data, explorer, video). Filter chips for the five tags (four pillars plus Modeling). |
| **Resources** | The thing the site exists to put front and center | Grouped: **Connectome explorers and galleries** (Optic lobe Cell Type Explorer, Male CNS explorer, Female brain explorer, neuDiff, VPN and VCBN galleries, interactive figure browser, YouTube cell-type videos). **Displays and rigs** (Modular LED Display docs, G6, G4, webDisplayTools, maDisplayTools, Fly Lab Gear). **Software and analysis code** (per-paper repos, neuView, Kinefly). **Datasets** (optic-lobe v1.1, male CNS, neuPrint). Each item: image, name, one line, version or date, license, links. |
| **People** | Current lab with photos and one line each, then alumni | Current members in color portraits with role and one sentence (what they work on, tagged by pillar), links to Scholar, GitHub, ORCID. Collaborators and visiting scientists. Alumni as a dense grid: name, former role, where now. |
| **News** | Dated, short, real | Reverse-chronological list: date, tag (paper, preprint, award, talk, course, new member), one or two sentences, link. Sourced from the lab's own events, no essays. |
| **Join** | Positions and contact | Current openings, how to apply, graduate and undergraduate program notes, address, email. No contact form (no server), just mailto. |

Footer on every page: Janelia / HHMI affiliation and logo, GitHub, YouTube, Scholar, Bluesky, ORCID, address, "Updated <month year>" generated at build time.

A **Gallery** page is tempting given the unpublished videos. Recommendation: do not add a seventh page at launch. Put the best unpublished videos to work as the hero and pillar backgrounds and as section openers on Research. Revisit after launch.

## 4. Design direction

Inspiration: dudmanlab.org (see the analysis). Borrow the principles, not the look.

**Borrow in spirit**
- Design tokens first (ground, panel, ink, muted, rule, two accents) as CSS variables, with dark and light defined together.
- Big display type against small letter-spaced eyebrows; few intermediate sizes.
- Sparse copy on the home page; prose lives on Research.
- The lab's own imagery as full-bleed backgrounds with text on top.
- Publications as featured cards above a compact year-indexed archive with an icon row.
- Alumni as a dense grid.

**Do differently**
- **Light pages with dark media bands.** Neuron renderings and connectome maps look best on black, so the hero, pillar tiles, and video sections are dark; text pages (publications, people, news) are light. Dudman is dark throughout.
- **Two accents, not four.** Suggestion: one warm (for behavior and physiology traces) and one cool (for anatomy). To be picked against the actual videos, since the accents should harmonize with the dominant colors in the renderings.
- **Type**: a humanist or geometric sans for display and body (candidates: Source Sans 3, IBM Plex Sans, Inter Tight, Figtree) and no serif wordmark, to stay away from Dudman's Palatino-plus-Outfit voice. A monospace accent for version numbers and data labels fits the tool-builder side of the lab.
- **Nav always visible**, no hidden-until-scroll trick, no alternating 60/40 tile mosaic. A uniform four-column grid (2x2 on phones) for the pillars.
- **Portraits in color** with a one-line bio.
- **Dated news**, author lists on every paper, explicit resource groups with license lines.
- **Hero video under 2 MB**, muted, looping, with a poster image and a `prefers-reduced-motion` fallback. Dudman's 55 MB GIF is the cautionary example.

Before building, I would make two or three quick home-page mockups (static HTML, real lab imagery, same structure, different type and accent choices) so the choice is made by looking rather than by reading.

## 4a. Hero: scroll-driven zoom from fly head to neurons

Concept: one of the lab's "fly head to inside the visual system" movies, re-cut so that scrolling drives it. As the visitor scrolls, the head comes apart, the view zooms into the brain, then into the optic lobe, then into individual neurons. Scrolling back up reverses it. Short pinned text appears at three stops: the lab name and one sentence at the head; "Anatomy" and a line about the connectome at the brain; the cell-type story at the neurons. After the last stop the page releases into the normal layout (pillars, resources, papers).

How it is built (the technique behind Apple's product pages, no framework needed):

- The movie is exported as a **sequence of still frames**, not played as a video. Scrubbing a `<video>` element by setting its time on scroll stutters, because browsers decode from the nearest keyframe; drawing pre-decoded frames onto a `<canvas>` is smooth and works everywhere.
- Frame budget: about **150–240 frames** (one per roughly 20–30 px of scroll over a 4,000–6,000 px scroll range). Desktop set at 1920 px wide as WebP or AVIF, roughly 60–120 KB each, so 15–25 MB total; a phone set at 960 px wide at a quarter of that. Frames load progressively (the first ones first), with a poster shown until enough are ready.
- Scroll handling: a pinned (`position: sticky`) full-viewport canvas inside a tall section; a `requestAnimationFrame` loop maps scroll progress to a frame index and draws it. About 60 lines of vanilla JavaScript.
- Accessibility and fallbacks: visitors with `prefers-reduced-motion` get a static frame and normal scrolling; browsers without JavaScript get the poster image; the text stops remain real HTML, so the page reads fine without the animation.
- Hosting: the frames live in the repo (well within GitHub Pages limits) and are served with long cache headers by GitHub's CDN.

Source movies (found 2026-10-23 in Dropbox, `WORK/PAPERS/2025/Eye Map Paper/animations/`, both 1920x1080, 24 fps, H.264; Blender renders by Marisa Dreher for Zhao et al. 2025):

- `EyeMap_Animation_wNarration_20240909.mp4` (97 s). Roughly 0–12 s: fly head front view, zoom toward the eye; 12–20 s: into the micro-CT retina; 20–40 s: lenses, photoreceptor tips, view directions on the eye; 40–64 s: photoreceptors → L1 neuron → Mi1 neurons → medulla with M10 columns; 64–80 s: whole medulla with columns; 80–97 s: back out to the head. The first 64 s are the head → eye → neurons move we want. Contact sheet: [research/hero-source/eyemap-animation-contact-sheet.jpg](research/hero-source/eyemap-animation-contact-sheet.jpg).
- `T4_Animation_Final_wNarration_20221202_HighBitrate.mp4` (120 s). 0–10 s: head and eye close-up; 10–15 s: whole brain EM neuropil (FAFB); 15–40 s: medulla and lobula plate with single T4a–d neurons; then medulla columns and preferred directions. The opening 40 s are an alternative head → brain → neurons move with the whole brain as the middle stop. Contact sheet: [research/hero-source/t4-animation-contact-sheet.jpg](research/hero-source/t4-animation-contact-sheet.jpg).
- Also present: `Mi1_Animation_Update_20230314.mp4` (21 s) and the submitted Supplementary Videos 1 and 2. No `.blend` or code files exist in Dropbox. In Slack, Marisa shared the fly head model (`FlyHeadModel_withLenses_20220421.blend`, 408 MB, plus OBJ exports) in the group DM with Stuart Berg on 2025-04-07; that covers the head and lenses but not the animation scenes (camera, retina CT, neurons, columns). The narrowed request to Marisa is in [drafts/marisa-blender-request.md](drafts/marisa-blender-request.md). The same thread records that the model is lab-owned, Marisa wants creator attribution, and a citeable CC-BY repo for it was planned in June 2026 and not yet made.
- Mockup status: three home-page mockups with a working scroll hero (192 frames cut from the eye-map movie at 3 fps) are in `mockups/` and deploy to `/mockups/`. Add `?flat=1` to a mockup URL to see the page as one long scroll without the scrub, which is handy for review.

**Own pipeline (found 2026-10-23).** The October 2026 IAS talk build (`Presentations/2026/IAS_FlyMeeting_Oct2026/talk_v2_build/I_blender/`, README and `code/`) contains a headless Blender 5.2 pipeline written for the talk: `fetch_movie_assets.py` pulls neuPrint meshes (male-cns v1.0), `render_zoom_movie.py` with `zoom_movie.json` renders a continuous 30 s camera move from the whole male CNS to the right optic lobe, into a medulla column with its lamina inputs, down to a T4b dendrite with typed synapses (draft at `I3_zoom/drafts/`, 640x360). EEVEE renders 1080p frames in about 0.2–1 s. Loading Marisa's head model (the .blend in Slack) into that scene gives the full head → brain → neurons move, rendered directly as a frame sequence at any resolution, with no dependence on her animation scenes. This is now the preferred hero source; her scenes remain the fallback for the retina and lens segment. The code lives in the `anatomy-connectome-analysis` repository worktree `peaceful-rubin-c0a638`, `scripts/blender/`.

The movies are generated from code plus Blender files, and having both is the ideal case. With the Blender scene we can:

- Render the frame sequence directly as PNG at exactly the resolution and frame count the scroll range needs, with no video-compression artifacts, and re-render whenever the data or the chosen neurons change.
- Re-time the camera path so it slows or holds at the three rest points (head, brain, neurons), which is what makes the pinned text stops feel deliberate.
- Render a second, portrait-framed camera for phones instead of cropping the landscape frames.
- Keep a clean dark background and leave out any on-screen text, which belongs in HTML.

So: please share the code and the Blender files (and the rendered example movie for reference). If the scene is heavy, a low-sample preview render is enough to build and time the scroll mechanics; the final frames can be rendered once at the end. Only the number of distinct frames matters, not the movie's duration; a 10–20 s move at 24 fps is plenty.

This is the one piece of the site that is a real engineering task. Estimate: half a day for a first working version once the frames exist, including the mobile set and fallbacks.

## 4b. Avoiding the generic "AI-generated page" look

The tells that make a site look machine-made, and the rule that avoids each:

| Tell | Rule for this site |
|---|---|
| Purple-to-blue gradients, gradient text, glowing blobs | Flat color only. Two accents, chosen from the lab's own renderings. No gradients except the darkening scrim over imagery. |
| Three identical cards with icon-in-a-circle and "Learn more" | Pillar tiles use real imagery and video, not icons. Different sections use different layouts (full-bleed band, two-column, dense list), not the same card grid repeated. |
| Rounded 16 px corners and drop shadows on everything | Near-square corners (0–3 px). Hierarchy from type and spacing; shadows only on hover if at all. |
| Default Inter everywhere | One deliberately chosen typeface pairing, set with real typographic care (tight display tracking, sensible measure, hanging eyebrows). |
| Emoji or generic line icons as decoration | Icons only where they carry meaning (link types on publications), from one small consistent set, in the text color. |
| "Welcome to the Reiser Lab" hero copy, "cutting-edge", "unlock" | Specific sentences about flies, vision, and what the lab actually made. The copy is written by the lab, not generated. |
| Stock photography, abstract "neural network" art | Only the lab's own data: renderings, recordings, rigs, flies, people. Every image credited in `credits.yaml`. |
| Perfect symmetry and centered everything | Left-aligned text with a deliberate grid; asymmetric image placement where the content allows. |
| Dark mode toggle as a feature | No toggle. Light pages with dark media bands, one considered design. |
| Pop-ups, cookie banners, chat widgets, newsletter modals | None. No third-party scripts except a YouTube embed where a long video is wanted. |

The strongest antidote is the content itself: real figures, real videos, real people, dated news. Templates look generic because their content is placeholder; this site has none.

## 5. Media plan (summary; details in media-plan.md)

- **One figure per paper.** For papers that had a figure on the old Janelia page, reuse it. For the rest, the media plan proposes a figure or movie still with the reason. Final choice is yours per paper.
- **Videos** are the site's main visual asset. Three sources: supplementary movies from the papers, the per-cell-type renderings on the ReiserLab YouTube channel, and the unpublished videos you have. Each video on the site gets: a 6–12 s loop cut, exported as MP4 (H.264) and WebM, 1280 px wide, under 2 MB, plus a JPEG poster; longer versions are embedded from YouTube where wanted.
- **Images**: WebP at 1600 px for cards, 3:2 crop, stored in the repo under `public/media/` with a `credits.yaml` recording source paper, figure, author, and license for every file. Papers under CC-BY (most recent ones, given HHMI's open access policy) can be reused directly; the media plan flags the ones to check.
- **Presentation and archive footage (inventoried 2026-10-23)**: 24 candidate videos copied to `media/sources/presentations/` with a `SOURCES.md` (git-ignored, 600 MB): the 2026 Blender T4b films and CNS-to-lamina zoom draft, Cell Type Explorer and display-tools screen recordings, the scanner blind-spot animation, 2025 behavior arenas (iris shutter, hide-and-seek), optic-flow and receptive-field maps, EM fly-through, VPNs in the brain, G4 tethered flight and pitching arena, the inexpensive treadmill, gravity assay, place learning, FlyBall VR, high-speed landing and antennae, and the 2008 robotic lab assistant. Ten 8 s loops cut from these drive the mockups' pillar tiles and resource cards (`mockups/media/`).
- **Collection**: a shared folder (Dropbox) where lab members drop candidate videos and images with a filename convention `YYYY_pillar_shortname_author.ext`; Claude Code does the cutting, compressing, and crediting.

## 6. Technical approach

Recommendation: **a small custom static site, generated by a short Python script from data files, deployed by GitHub Actions to GitHub Pages.** This is the architecture behind the best-designed lab site in the survey (Steinmetz Lab: JSON data, a 37 KB `build.py`, Actions, an `EDITING.md` for busy scientists), and it matches how the lab already produces the Cell Type Explorer pages (neuView is a Python static generator). What it buys us:

- **Zero dependency rot.** Python plus Jinja2 templates plus Pillow for image resizing will build unchanged for a decade. No theme to upgrade, no npm major versions, no framework churn (the survey found the Hugo research-group template abandoned and Astro templates with single maintainers).
- **Full design freedom.** The academic themes (al-folio, Hugo Blox, Jekyll group templates) all look like each other and carry features we do not need (blog, CV, teaching). A custom design is also less code to maintain than a large template to fight.
- **Image handling at build time.** The generator resizes every figure to the sizes the layout needs and writes WebP, so contributors can drop in a full-resolution PNG.
- **Validation.** The build fails loudly if a paper entry lacks a DOI or its figure file is missing, instead of rendering a broken card.

Alternative: **Astro**, if a hot-reloading dev server and a component model are wanted; the data files would carry over unchanged. Jekyll via the sbryngelson academic template is the fallback if we decide a ready-made template is acceptable after all.

Content lives in data files, never in HTML:

```
data/
  publications.yaml   one entry per paper: doi, title, authors, venue, year, pillars, figure, summary, selected, links{journal,preprint,pdf,code,data,explorer,video}
  people.yaml         one entry per person: name, role, pillars, photo, line, links, status (current|alumni), where_now
  news.yaml           one entry per item: date, tag, title, link, one or two sentences
  resources.yaml      one entry per resource: group, name, line, url, repo, version, license, image
templates/            Jinja2: base, home, research, publications, resources, people, news, join
media/                full-resolution figures, loops, posters, portraits, credits.yaml
build.py              reads data, resizes media, renders site/ ; also run by the Actions workflow
```

Adding a paper is one YAML entry plus one image. Claude Code can draft the entry from a DOI (Crossref) in a minute; a lab member can also do it from the GitHub web editor. Every push to `main` rebuilds and deploys in two or three minutes.

## 7. Keeping it updated

The failure mode of the old page was not design but staleness (news ended in 2019, two dead tool links). The plan treats upkeep as the main design requirement.

- **Data files, not pages.** All recurring updates (paper, person, news, resource version) are one small file each. No one edits layout to add a paper.
- **A one-page HOW-TO-UPDATE.md** in the repo with four recipes: add a paper, add or move a person, post news, add a resource. Each recipe is "copy this file, change these fields, push".
- **Steward**: one person owns the site besides you (Frank Loesche already maintains the GitHub Pages docs and would be a natural choice). Expectation: 30 minutes per month.
- **Triggers tied to existing events**: a preprint goes up, a paper is accepted, someone joins or leaves, a course runs. The news item and the publication entry are written in the same sitting, by whoever posts the lab Slack message. A Linear ticket template for "website update" would make this routine.
- **Automation, cheap to add later**:
  - Monthly GitHub Action that queries Crossref or PubMed for new items by ORCID and opens a pull request with a drafted publication entry.
  - Monthly link checker (lychee) that opens an issue when a URL dies, which would have caught both dead tool links years ago.
  - Build-time "Updated <date>" in the footer so staleness is visible.
  - Cell Type Explorer and gallery metadata (dataset versions, type counts) read at build time from their repos so the Resources page never lags.
- **Quarterly review**: 20 minutes in a Claude Code session: "what changed since the last update" against Slack and Linear, then a batch of small edits. Put it on the calendar.
- **Photos**: schedule one lab photo session a year, and ask every new member for a portrait at onboarding.

## 8. Work plan in half-days

| Session | Deliverable |
|---|---|
| **1 (today)** | Research, this plan, inspiration set, figure and video proposals. |
| **2** | Decisions on stack, pillar set and wording, palette direction. Two or three static home-page mockups with real imagery. Repo scaffold in `reiserlab.github.io` (generator, templates, data schema), design tokens, Actions deploy, DNS and HTTPS live with a placeholder page at reiserlab.org. |
| **3** | Content: publications data for every lab paper (Claude drafts from DOIs; you confirm figures), people data, resources data, news backfill for 2024–2026. |
| **4** | Media: export and compress the scroll-driven hero frames, cut the pillar loops, process all paper figures, credits file. Build out all six pages. |
| **4b** (if needed) | Second pass on the scroll hero: mobile crop, text-stop timing, reduced-motion and no-JS fallbacks. |
| **5** | Review with the lab, fixes, launch. Point the Janelia page at the new site. Write HOW-TO-UPDATE.md and the link-checker action. |

## 9. Decisions needed from you

1. **Domain**: reiserlab.org, correct?
2. **Repo**: build directly in the existing `reiserlab/reiserlab.github.io` (recommended), accepting that existing project-site URLs will start redirecting to reiserlab.org paths.
3. **Stack**: custom Python generator over data files as recommended, or Astro.
4. **Pillar wording**: four tiles "Anatomy · Behavior · Neurophysiology · Methods" with Modeling as a cross-cutting tag (recommended), or all five as tiles, or a five-word tagline strip over four tiles.
5. **Theme**: light pages with dark media bands (recommended), or dark throughout.
6. **Figures**: go through the per-paper proposals in media-plan.md and mark changes.
7. **Steward**: who co-owns the site after launch.
8. **Hero movie**: send the drafted request to Marisa for the Blender files and code (drafts/marisa-blender-request.md). Decide between the eye-map opening (eye and retina as the middle stop) and the T4 opening (whole brain as the middle stop).
