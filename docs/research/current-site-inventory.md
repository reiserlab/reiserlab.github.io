# Reiser Lab web presence: inventory (2026-10-23)

Research notes gathered while planning the new reiserlab.org site. Everything was fetched live on 2026-10-23 unless marked "not verified". The Janelia site has only five lab subpages (Lab Home, Members, Publications, Positions, Tools); `/research`, `/resources`, and `/news` return 404.

---

## Part 1. Content inventory of the current Janelia lab site

### 1.1 Lab Home — https://www.janelia.org/lab/reiser-lab
| Section | Content | Volume | Currency |
|---|---|---|---|
| Tagline | "We study vision in flies in order to understand where behavior comes from." | 15 words | OK, generic |
| Current Research | Summary (~17 words) + body (~170 words): links identified visual pathways to behavioral programs; behavior of walking/flying flies, electrophysiology, calcium imaging, instrument development, computation/modeling; collaborates with Rubin, Card, Jayaraman, Branson labs and FlyEM / Fly Olympiad teams. | ~190 words | Stale. No mention of connectomics, the Cell Type Explorer, G4/G6 displays, or any work after ~2019. Fly Olympiad no longer exists as a project team; Card lab has moved to Columbia. |
| Lab Updates | 6 items dated 11/09/17, 12/18/17, 01/08/18, 06/28/18, 08/02/19, 01/03/19 (two are job ads; one has typo "Neurosicence"). | 6 short blurbs | Very stale: newest item is Aug 2019. |
| Research Gallery | 5 captioned images: fly visual place learning; "Sarcophagus" tether chamber; tethered flying fly; "Direct Observations" composite (James Strother); LaWF2 neuron (Aljoscha Nern). | 5 images | Imagery is pre-2018; many images are lazy-load placeholders. |
| Navigation | Tabs: Lab Home, Lab Members, Publications, Positions, Tools. Related-lab links: Romani, Card. | — | Card lab link stale. |
| Missing | PI name does not appear on the home page; no link to GitHub, Cell Type Explorer, YouTube, Modular LED Display docs, Fly Lab Gear; no news since 2019; no contact block for the lab. | | |

### 1.2 Lab Members — https://www.janelia.org/lab/reiser-lab/members
13 people listed (see Part 4). Each has only a name, title, and "View Bio" link; most photos are generic silhouettes. Alumni headings exist but rendered empty in the fetch (not verified whether populated behind JS). Not listed: Frank Loesche (Senior Engineer; Reiser Lab contact on the Janelia Modular LED Displays page; only visible member of the GitHub org) and Aljoscha Nern (co-author on most lab papers).

### 1.3 Publications — https://www.janelia.org/lab/reiser-lab/publications
- 56 entries, 10 per page, auto-fed from Janelia's publication database (tagged by lab), so it includes items where no lab member is an author and omits several lab papers.
- Problems found:
  - Duplicate entry for Longden et al. 2023 Nat Commun.
  - Missing published versions: Zhao et al. Nature 2025 (only the 2022 bioRxiv is listed); Zhao et al. eLife 2024 LPTN survey (only the 2023 bioRxiv listed).
  - Missing entirely: Longden et al. 2026 bioRxiv mitochondria paper.
  - Truncated title: Kind et al. 2021 eLife shows "...polarization in ." (missing "Drosophila").

### 1.4 Positions — https://www.janelia.org/lab/reiser-lab/positions
One posting, "Postdoctoral / Research Specialist position in Behavioral Neuroscience & Methods Developement" (sic), ~250 words, undated; says connectomes "will soon be available" (now outdated). Unrendered CMS template strings ("node_title | node_title") are visible.

### 1.5 Tools — https://www.janelia.org/lab/reiser-lab/tools
Only two entries, both stale:
- "Modular visual display system" -> bitbucket.org/mreiser/panels/wiki — dead (404). Should point to https://reiserlab.github.io/Modular-LED-Display/.
- "FlyFizz — Drosophila on a ball system" -> flyfizz.org — dead (DNS does not resolve). Should point to https://reiserlab.github.io/Fly-Lab-Gear/.
Nothing about the Cell Type Explorer, Fly Lab Gear, GitHub, or YouTube.

### 1.6 Related Janelia pages
- PI bio: https://www.janelia.org/people/michael-reiser — ~65-word bio; links to ORCID, Google Scholar, Twitter. Headshot present.
- Janelia tool page: https://www.janelia.org/open-science/modular-led-displays — contacts Frank Loesche and Michael Reiser; links to G3, G4, G5 doc pages and Fly Lab Gear. No G6 link.
- Janelia news: "Seeing is believing: Janelia reveals connectome of the fruit fly visual system" (2024-04-18) https://www.janelia.org/node/69370.
- FlyEM optic-lobe dataset page https://www.janelia.org/project-team/flyem/optic-lobe links to the Cell Type Explorer and the ReiserLab YouTube channel.
- Male CNS project site https://male-cns.janelia.org/ links to the Reiser-hosted Male CNS Cell Type Explorer.

### 1.7 Summary of what is stale or missing
1. No research narrative post-2019; nothing on connectomics (optic lobe 2025, male CNS 2026, visual pathways 2026), eye-structure/T4 work, G6 displays, Fly Lab Gear, or Cell Type Explorers.
2. News feed ends Aug 2019; two dead job ads.
3. Tools page: both links dead.
4. Publications list auto-generated with duplicates, missing journal versions of two Nature/eLife papers, and non-lab items.
5. Members: no photos, no bios inline, no alumni populated, Loesche/Nern absent.
6. Template rendering bugs on Positions and Tools pages.
7. No links out to GitHub org, GitHub Pages sites, YouTube, neuPrint.

---

## Part 2. Shared resources and tools (exact URLs)

### 2.1 GitHub organization — https://github.com/reiserlab
43 public repositories, 24 followers, only visible public member @floesche, no org README. `reiserlab.github.io` repo exists (last push 2022-09-07, contains only LICENSE and .gitignore) and https://reiserlab.github.io/ returns 404.

**Connectome / cell type resources**
| Repo | Description | Stars | Last push | Pages |
|---|---|---|---|---|
| celltype-explorer-drosophila-male-cns | Cell Type Explorer, male CNS | 7 | 2026-09-10 | https://reiserlab.github.io/celltype-explorer-drosophila-male-cns/ |
| neuView | Static Celltype Explorer page generator (Python) | 1 | 2026-09-14 | — |
| male-drosophila-visual-system-connectome | Cell Type Explorer, supplement to Nern et al. 2025 | 0 | 2026-07-20 | https://reiserlab.github.io/male-drosophila-visual-system-connectome/ |
| male-drosophila-visual-system-connectome-code | Supplemental source code for Nern et al. 2025 | 13 | 2025-06-17 | — |
| visualpathways | Analysis code + companion resources for Hoeller et al. 2026 | 0 | 2026-08-28 | https://reiserlab.github.io/visualpathways/ |
| celltype-explorer-drosophila-female-adult-fly-brain | Cell Type Explorer, FlyWire FAFB v783b | 0 | 2026-05-19 | https://reiserlab.github.io/celltype-explorer-drosophila-female-adult-fly-brain/ |
| neuDiff | Compares two cell types side by side | 0 | 2025-12-04 | https://reiserlab.github.io/neuDiff/ |
| eyemap_T4 | Code for Zhao et al. 2025 Nature | 3 | 2025-07-09 | — |
| FAFB-photoreceptor-connectivity | Photoreceptor typing/connectivity in FAFB | 0 | 2022-01-18 | — |
| LC6downstream | R code for LC6 downstream analysis (Morimoto 2020) | 0 | 2020-11 | — |
| T5ConductanceModel | Conductance models, Gruntman et al. 2019 | 0 | 2019-12-10 | — |

**Modular LED Display (arena) family**
| Repo | Description | Stars | Last push | Pages |
|---|---|---|---|---|
| Modular-LED-Display | Umbrella: submodules + generated docs | 6 | 2026-10-22 | https://reiserlab.github.io/Modular-LED-Display/ |
| webDisplayTools | Web tools for arena config/pattern editing | 0 | 2026-10-22 | https://reiserlab.github.io/webDisplayTools/ |
| maDisplayTools | MATLAB tools for G4+ displays | 1 | 2026-10-12 | — |
| cshl-2026-course | Shared bench data for CSHL 2026 course | 0 | 2026-10-22 | — |
| LED-Display_G6_* (Hardware_Panel, Hardware_Arena, Hardware_Test_Arena, Firmware_Panel, Firmware_Arena) | G6 hardware (KiCad) and firmware | 0 | 2026 | some |
| LED-Display_G4_* (Firmware_Arena, Firmware, Hardware, Hardware_Arena, Hardware_Driver, Display_Tools) | G4 | 0 | 2026 | — |
| LED-Display_G3_* , LED-Display_G2_* | Legacy G2/G3 | 0 | 2022–2023 | — |

**Behavior rigs / lab hardware / misc**
| Repo | Description | Stars | Last push | Pages |
|---|---|---|---|---|
| Fly-Lab-Gear | Open hardware for fly neurobiology (3D print, laser cut, PCB) | 21 (9 forks) | 2026-10-22 | https://reiserlab.github.io/Fly-Lab-Gear/ |
| kinefly (fork) | ROS wing/head kinematics from tethered-insect video | 0 | 2026-10-21 | — |
| tutl-T4 (fork) | Nested-flash RF mapping stimulus (MATLAB) | 0 | 2026-09-21 | yes |

### 2.2 Cell Type Explorer (Nern, Loesche, Takemura et al., Nature 2025)
- URL: https://reiserlab.github.io/male-drosophila-visual-system-connectome/
- Sections: Cell Types (grouped ONIN / ONCN / VPN / VCN / other), Find Cell Type search, Spatial Coverage plots, Glossary, Publication, Source Code. Dataset optic-lobe:v1.1.
- Sibling explorers built with neuView: Male CNS (11,751 types, 164,838 neurons, snapshot 2026-09-09) https://reiserlab.github.io/celltype-explorer-drosophila-male-cns/ ; Female adult fly brain (flywire-fafb:v783b, 8,840 types) https://reiserlab.github.io/celltype-explorer-drosophila-female-adult-fly-brain/ ; comparison tool neuDiff https://reiserlab.github.io/neuDiff/
- Companion: ReiserLab YouTube channel https://www.youtube.com/@ReiserLab (a video per cell type). neuPrint optic lobe: https://neuprint.janelia.org/?dataset=optic-lobe%3Av1.1&qt=findneurons

### 2.3 Visual pathways galleries (Hoeller, Zhao, Nern, Rogers, Romani, Reiser — Cell 2026)
- VPN gallery: https://reiserlab.github.io/visualpathways/gallery_vpn/
- VCBN gallery: https://reiserlab.github.io/visualpathways/gallery_vcbn/
- Interactive figure browser: https://reiserlab.github.io/visualpathways/results/html_figures/
- Fig. 6c Neuroglancer view of retinotopy-annotated T-bars (link in repo README).
Neither the bioRxiv page nor the Janelia publication page link to these galleries; the new website should.

### 2.4 Modular LED Display documentation
- Main docs: https://reiserlab.github.io/Modular-LED-Display/ (Just-the-Docs Jekyll). Sections: Getting Started; G2; G3; G4 (acquisition, assembly, firmware, Pattern Generator, Function Generator, Protocol Designer, Experiment Conductor, Data Handling, troubleshooting); G6 (Arena, Test Arena, Panels, webDisplayTools, maDisplayTools).
- Web tools: https://reiserlab.github.io/webDisplayTools/ — Pattern Designer (beta), Arena Studio (beta), Arena Layout, Arena 3D View, G6 Panel Patterns, Pattern Icon Generator, G6 Panel Flash Programmer (WebUSB), Panel Serial Monitor.
- MATLAB tools: https://github.com/reiserlab/maDisplayTools
- Papers: Reiser & Dickinson 2008 J Neurosci Methods https://doi.org/10.1016/j.jneumeth.2007.07.019 ; G4 preprint Isaacson et al. 2022 https://doi.org/10.1101/2022.08.02.502550
- Third-party listing: OpenBehavior https://edspace.american.edu/openbehavior/project/modular-led-displays/

### 2.5 Other shared hardware/software
- Fly Lab Gear https://reiserlab.github.io/Fly-Lab-Gear/ — Walking setup (treadmill, sphere holder, illumination PCB, stands); G6 arena integration; Physiology (flyplate, fly pyramid); Tethering (station, sarcophagus, tethers, micromanipulator); guides. Paper: Loesche & Reiser 2021 Front Behav Neurosci https://doi.org/10.3389/fnbeh.2021.689573
- Kinefly fork https://github.com/reiserlab/kinefly
- Datasets: optic-lobe v1.1 (CC-BY 4.0) https://console.cloud.google.com/storage/browser/flyem-optic-lobe ; neuroglancer https://neuroglancer-demo.appspot.com/#!gs://flyem-optic-lobe/v1.1/optic-lobe-v1.1.json ; male CNS portal https://male-cns.janelia.org/
- CSHL 2026 course data repo https://github.com/reiserlab/cshl-2026-course

---

## Part 3. Publications 2023–2026 (Reiser as author unless noted)
High-profile journals marked [HP]. Sources: PubMed, Janelia list, journal pages. Google Scholar could not be fetched.

### 2026
1. [HP] The organization of visual pathways in the Drosophila brain. Hoeller J, Zhao A, Nern A, Rogers EM, Romani S, Reiser MB. *Cell*, 2026-09-03. DOI 10.1016/j.cell.2026.08.014. Preprint bioRxiv DOI 10.64898/2025.12.22.696097. Companion galleries in 2.3.
2. [HP] Sexual dimorphism in the complete Drosophila male central nervous system connectome. Berg S, Beckett IR, … Reiser MB, Hess HF, Rubin GM, Jefferis GSXE. *Cell*, 2026-09-03. DOI 10.1016/j.cell.2026.08.015. Lab members Nern, Hoeller, Loesche, Longden, Rogers, Seenivasan, Zhao, Flynn, Dreher are coauthors. Preprint bioRxiv DOI 10.1101/2025.10.09.680999.
3. Connectomic analysis of mitochondria in the central brain of Drosophila. Longden KD, … Reiser MB, Plaza SM, Berg S. *bioRxiv* 2026, DOI 10.1101/2024.04.21.590464.
4. Population morphology implies a common developmental blueprint for Drosophila motion detectors. Drummond N, Zhao A, Borst A. *PLoS Comput Biol* 2026. DOI 10.1371/journal.pcbi.1014657. (Lab member Arthur Zhao; Reiser not an author.)

### 2025
5. [HP] Eye structure shapes neuron function in Drosophila motion vision. Zhao A, Gruntman E, Nern A, Iyer NA, Rogers EM, Koskela S, Siwanowicz I, Dreher M, Flynn MA, Laughland CW, Ludwig HDF, Thomson AG, Moran CP, Gezahegn B, Bock DD, Reiser MB. *Nature* 646:135–142, 2025. DOI 10.1038/s41586-025-09276-5. Code: https://github.com/reiserlab/eyemap_T4.
6. [HP] Connectome-driven neural inventory of a complete visual system. Nern A, Loesche F, Takemura S-y, … Reiser MB. *Nature* 641:1225–1237, 2025. DOI 10.1038/s41586-025-08746-0. Preprint bioRxiv DOI 10.1101/2024.04.16.589741. Companion: Cell Type Explorer (2.2).
7. [HP] Whole-body physics simulation of fruit fly locomotion. Vaxenburg R, Siwanowicz I, … Turaga SC; Reiser coauthor. *Nature* 2025. DOI 10.1038/s41586-025-09029-4.
8. A competitive disinhibitory network for robust optic flow processing in Drosophila. Erginkaya M, … Reiser M, Chiappe ME. *Nature Neuroscience* 2025. DOI 10.1038/s41593-025-01948-9.
9. Parallel neuronal ensembles control behavior across sensorimotor levels in Drosophila. Liessem S, … Nern A, … Rogers E, … Ache JM. *bioRxiv* 2025, DOI 10.64898/2025.12.13.693955. (Reiser not an author.)

### 2024
10. [HP] A comprehensive neuroanatomical survey of the Drosophila lobula plate tangential neurons with predictions for their optic flow sensitivity. Zhao A, Nern A, Koskela S, Dreher M, Erginkaya M, Laughland CW, Ludwig HDF, Thomson AG, Hoeller J, Parekh R, Romani S, Bock DD, Chiappe E, Reiser MB. *eLife* 13:RP93659, 2024. DOI 10.7554/eLife.93659.
11. [HP] Homeodomain proteins hierarchically specify neuronal diversity and synaptic connectivity. Xu C, Ramos TB, Rogers EM, Reiser MB, Doe CQ. *eLife* 2024. DOI 10.7554/eLife.90133.
12. [HP] Neuronal wiring diagram of an adult brain. Dorkenwald S … FlyWire Consortium. *Nature* 634:124–138, 2024. DOI 10.1038/s41586-024-07558-y. (Reiser via consortium; not verified individually.)

### 2023
13. Different spectral sensitivities of ON- and OFF-motion pathways enhance the detection of approaching color objects in Drosophila. Longden KD, Rogers EM, Nern A, Dionne H, Reiser MB. *Nature Communications* 14:7693, 2023. DOI 10.1038/s41467-023-43566-8.
14. Small-field visual projection neurons detect translational optic flow and support walking control. Isaacson MD, … Branson K, Reiser MB. *bioRxiv* 2023, DOI 10.1101/2023.06.21.546024. No journal version found (not verified).
15. Drosophila antennae are dispensable for gravity orientation. Kladt N, Reiser MB. *bioRxiv* 2023, DOI 10.1101/2023.03.08.531317. No journal version found (not verified).

---

## Part 4. Current lab members (Janelia members page, 2026-10-23)

**Lab Team**
- Michael Reiser — Senior Group Leader
- Arthur Zhao — Research Scientist
- Edward (Ed) Rogers — Research Specialist III
- Pavithraa Seenivasan — Postdoctoral Scientist
- Shubham Rathore — Postdoctoral Scientist
- Grace Biondi — Janelia Graduate Scholar
- Hannah Marie Santos — Janelia Graduate Scholar
- Daniel Chavez-Clemente — Principal AI Robotics Engineer
- Isabel Lehenbauer — Robotics Engineer

**Other Science Contributors**
- Dominic Evans — Visiting Postdoctoral Associate
- Ali Karimi — Visiting Postdoctoral Associate
- Elisa de Launoit — Visiting Postdoctoral Associate

**Lab Coordinator**
- Dianne Pereira — Lab Administration Specialist

Not on the members page but publicly associated with the lab: Frank Loesche (Senior Engineer; GitHub @floesche); Aljoscha Nern (coauthor on nearly all lab papers). Alumni sections exist but appear empty.

---

## Could not verify
- Google Scholar profile URL and ORCID for Michael Reiser.
- YouTube channel video/subscriber counts.
- Whether the visualpathways galleries are fully populated (JS-rendered).
- Journal versions of Isaacson 2022 (G4 display), Isaacson 2023 (small-field VPNs), Kladt 2023 (gravity).
