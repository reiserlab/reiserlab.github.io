# Draft message to Marisa (not sent)

Context found in Slack (2026-10-23): Marisa already shared the fly head model in the group DM with Stuart Berg on 2025-04-07: `FlyHeadModel_withLenses_20220421.blend` (408 MB; head mesh, lens spheres as separate objects, lighting), `FlyHeadModel_wLenses_20220421.obj` (444 MB), and on 2025-04-08 `FlyHead_20220421.obj` (257 MB) and `Lenses_20220421.obj` (67 MB). Permalink to the thread: https://hhmi.enterprise.slack.com/archives/C08LWTADC9H/p1744060995181409. In May–June 2026 the same thread agreed the model is HHMI/lab-owned, Marisa wants creator attribution, and Michael planned to park it in a citeable CC-BY repo on the lab GitHub (not yet done). Stuart has a neuroglancer mesh conversion of the head.

What is still missing for the scroll hero: the animation scenes themselves (camera paths, the micro-CT retina volume and cross-section setup, the L1/Mi1/T4 neuron meshes, the medulla column points, materials) and any scripts that imported the data. Hence the narrower request below.

---

Subject: Blender scenes for the eye-map and T4 animations

Hi Marisa,

I am building a new lab website (it will live at reiserlab.org) and I want the home page to open with a version of your eye-map animation: as the visitor scrolls, the fly head gives way to the eye, the retina, and then the neurons, the way product pages do it. To build that I need to re-render the sequence as still frames rather than cut the existing MP4, so I am after the scene files rather than the movies.

I already have the fly head model you shared with Stuart last year (`FlyHeadModel_withLenses_20220421.blend`). What I am missing are the animation scenes:

- The .blend files for `EyeMap_Animation_wNarration_20240909` and `T4_Animation_Final_wNarration_20221202`, ideally packed (File → External Data → Pack Resources) so the micro-CT volume, neuron meshes, column points and textures travel with them. A Dropbox folder is perfect; size is not a problem.
- Any scripts or notes you used to import Arthur's data (lens coordinates, photoreceptor tips, skeletons, M10 columns), and the Blender version.

The stretches I care about are the opening of the eye-map animation (head, into the eye, down to the L1 and Mi1 neurons and the medulla columns) and the opening of the T4 animation (head, eye, whole brain, lobula plate, single T4 cells). I would re-time the camera to pause at a few points, render at the resolution the page needs plus a portrait version for phones, and credit you on the site. I would run the result by you before it goes live.

This also gives me the push to finally set up the citeable repo for the head model that we discussed with Stuart; I will send you the README and license text to check.

No rush beyond the next few weeks. Thank you!

Michael
