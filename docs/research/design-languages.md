# Design languages beyond lab sites (survey 2026-10-23)

Round two of inspiration, after the first three mockups felt competent but not loved. Screenshots (900 px) are in [screenshots2/](screenshots2/). Font names come from each site's CSS unless noted.

## Five languages

### 1. Warm scientific journal: serif display, mono labels, paper
- **Quanta Magazine** (quanta.jpg): Noe Display headlines, Merriweather text, Pangram labels. White, hairline rules, commissioned illustration only, small uppercase red-brown section labels over each headline. Carry over: eyebrow-over-headline for pillars and papers; illustration-only image policy (connectome renders qualify); one warm accent used only for labels and links.
- **Asterisk** (asterisk.jpg): Noe Standard and Text, Atlas Grotesk UI. Split screen: a tall botanical plate left, a flat hot-pink field with a short summary right, almost nothing else. Carry over: the two-panel moment right after the hero, a tall scientific plate beside one flat color field with a short manifesto.
- **Works in Progress** (worksinprogress.jpg): Editor (sharp Scotch serif) plus GT America Mono for everything small. Cream paper, ruled lines, red and ink-blue rectangles, duotone cut-outs on flat color. Carry over: mono for metadata, serif for titles; flat-color panels with a cut-out image for papers without a good figure; the ruled "author on topic" list for news.
- **Aeon** (aeon.jpg): same type family. Dark photo hero with a one-word headline, then a grid where each card has a mono breadcrumb ("Essay / Philosophy of mind"). Carry over: the mono breadcrumb is exactly "Paper / eLife 2026" or "Resource / Dataset".
- **Simons Foundation / Flatiron Institute** (simons.jpg, flatiron.jpg): Noe serif plus Atlas Grotesk; Flatiron uses Founders Grotesk, Tiempos, Founders Grotesk Mono. Two-column skeleton: a narrow left rail of tiny mono labels with a colored dot ("QUICK LINKS", "CENTERS", "LATEST NEWS"), content in a wide right column; research centers as a ruled list with bold sans title and serif one-line description. Carry over: the most directly reusable skeleton; maps one to one onto pillars, resources, papers, people, news.
- **Santa Fe Institute** (santafe.jpg): Chap and Barlow, Libre Baskerville quotes; stone and oatmeal grays, dark teal. Carry over: a muted stone/teal palette after a dark hero; a quote card for the big question.

### 2. Swiss grotesk with mono labels: quiet, systematic
- **Anthropic Research** (anthropicresearch.jpg): Styrene B and Copernicus, Tiempos Text, JetBrains Mono. Oatmeal off-white, a two-line serif statement, then a loose asymmetric grid of collaged images with mono dates. Carry over: the oatmeal page color; the asymmetric staggered grid for news and papers; a mono article count. Caution: widely copied now.
- **rsms.me** (rsms.jpg): Inter and InterDisplay, IBM Plex Mono. Pure text, three narrow columns, one orange dot. Carry over: a dense text index can still feel designed; the one-dot accent.
- **Truth & Beauty, Moritz Stefaner** (stefaner.jpg): Atlas Grotesk, Atlas Typewriter caps labels, IBM Plex Serif italics. Near-black page, terracotta accent, images on flat color plates. Carry over: a credible all-dark data site; labels in mono caps; figures re-plated on a chosen background.
- Vercel and Linear: restraint only; otherwise the default startup look to avoid.

### 3. Museum poster: flat color blocks, big type, object grids
- **Commercial Type** (commercialtype.jpg): each typeface a full-width flat color band with its name set enormous. Carry over: each pillar as a full-width band with its name in display type and one specimen image; three bands at most, in a restrained family.
- **Cooper Hewitt** (cooperhewitt.jpg): their own condensed grotesk caps, an edge-to-edge grid of objects on flat gray. Carry over: objects-on-flat-background grid for instruments and headshots shot the same way.
- **Letterform Archive** (letterform.jpg): Duplicate Sans and Duplicate Ionic; white with one true red; an events list with label left, date right, hard-edged image, bold title, credit. Carry over: that list for news and talks.
- **Klim Type Foundry** (klim.jpg): one saturated field, one object, two tiny boxed labels. Carry over: the nerve to make the first screen one object on one color; a thin slider as scrub affordance.
- **Pentagram** (pentagram.jpg): a sentence as interface, dark feature band alternating with white grid.

### 4. Dark instrument / blueprint: white line on black
- **Ink & Switch** (inkswitch.jpg): Geogrotesque, Merriweather Sans, Fira Mono. Pure black; the first screen is a grid of white single-weight line drawings (wireframe hourglass, lissajous, oscilloscope trace) with a small paragraph and a chevron. Carry over: the closest relative of a fly-head hero; white 1 px line art on black, small paragraph beside it, chevron, release. Pillar glyphs (ommatidium, T4 neuron, arena) in the same stroke.
- **MIT Media Lab** (medialab.jpg): Neue Haas Grotesk; black page, two bold statements on opposite sides of the screen, then a horizontally scrolling strip of square thumbnails. Carry over: the two-sided question-and-answer; the single-row thumbnail strip for papers.
- Allen Institute: lowercase slash-separated nav, one acid accent. Stripe Press: a warm near-black (#211917) instead of pure black, one rendered object.

### 5. Paper, specimen, illustration: light, drawn, literary
- **Arcadia Science** (arcadia.jpg): Lora, Raleway, Atkinson Hyperlegible Mono. Warm off-white; hand-drawn watercolor organisms drift on empty paper; nav as sparse words in the corners. Carry over: the strongest argument for a light release after a dark hero; a drawn fly specimen plate in the text ink.
- **The Pudding** (pudding.jpg): Gooper heavy serif, Atlas Grotesk, Atlas Typewriter tags. Each story is a flat-colored plate with a screenshot inside, a mono issue number top-left and date top-right. Carry over: the numbered plate as a publications pattern; it makes mismatched figures look deliberate. Keep plates muted and titles sentence case.
- **Distill** (distill.jpg): a plain list with date and tag in a narrow left column, bold title, authors, one-sentence abstract, a figure on the right, a hairline rule. Carry over: the most readable paper list in the survey.
- Butterick's Practical Typography: book-style two-column contents for a resources page. Giorgia Lupi: large centered statement after a hero. Dynamicland: a photographed shelf as navigation, a one-off.

## Scroll-driven pages: how long the pin lasts

Read from Apple's CSS. The AirPods Pro and MacBook Pro heroes are exactly one viewport and autoplay; they are not scrubbed. The scrubs sit lower on the page: 150vh containers (half a viewport of travel) for small ones, 300–400vh (two to three viewports) for the big chip sections, and the release is simply the next section scrolling up in normal flow, no snap, no fade. Linear and Vercel pin nothing. Conclusion for the fly head: a pinned hero of 150–200vh (half to one viewport of scrub) is the generous end of what the best pages do; the question should be legible by about 60 percent of the scrub; the pillars should scroll up over the canvas. The mockups now use 200vh (down from 520vh).

## Three recommended languages for this lab

**1. Dark instrument releasing to paper** (Ink & Switch for the hero, Flatiron for the body). Warm near-black first screen with the fly head as the one object, a small mono label top-left, the question in a sharp grotesk bottom-left as Apple places it; pin at most 1.5 viewports. Then an off-white paper page in the Flatiron skeleton: narrow left rail of mono caps labels with a dot, wide right column, pillars as bold sans title plus serif one-liner plus hairline. Papers in the Distill list. One 1 px line-art glyph per pillar and resource so the hero's language persists. Type: a grotesk with character (free: Instrument Sans or Geist), a text serif (free: Newsreader or Source Serif 4), IBM Plex Mono. One accent from the fly's eye. Strongest continuity with the hero and easiest to build well.

**2. Warm scientific journal** (Quanta, Asterisk, Works in Progress for metadata). Dark hero releasing to cream paper and a true display serif. Right after the hero an Asterisk split: tall plate left (the fly head as engraving or micrograph), flat saturated field right with the one-paragraph statement. Then Quanta's eyebrow system for pillars; Works in Progress's ruled list for papers with mono dates; people on one flat background; single-column news with mono bylines. Type: display serif (free: Fraunces heavy optical size, or Instrument Serif), text serif (Merriweather or Source Serif), mono for every small thing (free: Geist Mono or Commit Mono). Cream (#f6f1e8), near-black ink, one accent (rust, or a hot pink if daring). Most unlike other lab sites; rewards illustration assets.

**3. Numbered plates** (The Pudding, Commercial Type, Letterform Archive for news). Oatmeal page; each pillar a full-width flat band in a restrained family (ink blue, oxide red, ochre, bottle green) with its name very large and one specimen image; papers as numbered plates, a flat rectangle per paper with the key figure inside and mono tags ("#41", "2026 / Nature"); resources the same with a screenshot; news in the Letterform list; headshots on one flat color. Type: a heavy grotesk for bands (free: Archivo Black or Bricolage Grotesque), plain sans body, mono tags. Most scalable for a long publication record; needs discipline on color.
