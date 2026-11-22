# Image Plan Blueprint — Calcium in the Blood, Calcium in the Urine, and Kidney Stones

**Guide:** https://renalcarematters.com/guides/calcium-disorders-and-kidney-stones
**Slug:** `calcium-disorders-and-kidney-stones` · dual-mode (Patients & Families in EN/TL/CEB/KAP; Clinicians in EN)
**Prepared:** November 22, 2026 · for production in ChatGPT image generation (https://chatgpt.com/)
**Skills used:** williamriveromd-hero-vignette · williamriveromd-infographic-skill · williamriveromd-simple-figure · williamriveromd-biomedical-mechanism-figure · williamriveromd-algorithm-generator-skill · williamriveromd-local-image-generator (Stage 2 validation and manifests)

---

## 1. Goal

Every image should let a reader understand one idea faster than the text alone, whether that reader finished grade school or a nephrology fellowship. The set is built around the guide's central teaching point: **blood calcium, urine calcium and a scan answer three different questions, and they can disagree.**

## 2. Design principles for readers of all educational levels

1. **One idea per image.** Each prompt states a one-sentence reader takeaway; anything that does not serve it is cut.
2. **Picture first, words second.** Patient images carry meaning through familiar objects (blood tube, urine container, kettle, sieve, Filipino dishes) so they still work if the words are skipped.
3. **Few words, plain words.** Patient labels are 1–6 words. No percentages or units appear in patient images except the 2.5 L urine goal, which always carries its safety condition.
4. **Language-neutral by design.** On-image text cannot be translated, so patient images keep English text minimal and the four-language captions in the HTML do the explaining. Optional Tagalog-label variants are noted in §7.
5. **Analogy, then anatomy.** The same mental models used in the text reappear in the images (thermostat for PTH, recycling sieve for the kidney, kettle scale for specks versus stones), and each analogy is shown beside the real anatomy so it never replaces it.
6. **Absolute numbers, not relative ones.** Trial results are shown as "out of 100 people" icon arrays (image 016).
7. **Danger is unmistakable.** Red flags use icons, shapes and red together, never color alone (color-blind safe).
8. **Layered for clinicians.** Clinician figures move organ → nephron → cell, or symptom → test → cause, with every threshold labeled by its source so it is never generalized.
9. **No invented numbers.** Prompts contain only figures already stated and cited in the guide.
10. **House style.** Illustrated, GPT-rendered textbook look with soft shading (no flat SVG or clip-art), light backgrounds only, Inter typeface, site palette, and the `renalcarematters.com` attribution on every figure (the text-free hero is exempt by spec).

## 3. Narrative arc

| Reader step | Patient tab | Clinician tab |
|---|---|---|
| Is this an emergency? | 001 Red-flag card | (urgent table in text) |
| What is the big idea? | 002 Three tests, three questions | 009 Renal calcium handling |
| Why does it happen? | 003 Three helpers · 004 Kidney recycles calcium | 010 Hypocalcemia workup · 011 HypoPT balance · 019 Randall plaque to stone |
| What does the scan mean? | 006 Specks vs stones | 013 Nephrocalcinosis phenotype map |
| What test do I do, and how? | 007 How to collect a 24-hour urine | 012 Reading a 24-hour urine card |
| What do I do about it? | 005 Calcium myth · 008 Stone-smart Filipino plate | 014 Acute stone pathway · 015 Prevention levers |
| How sure are we? | — | 016 Absolute effects icon arrays · 017 Case snapshots |

## 4. Production order and placement map

**P0** = produce first (core understanding or already wired in the guide) · **P1** = high value · **P2** = nice to have.

| # | Priority | File | Section anchor | Size | Skill | Status |
|---|---|---|---|---|---|---|
| 000 | P0 | vignette-hero.png | `hero` | 2048×2048 | williamriveromd-hero-vignette | Wired in guide |
| 001 | P0 | 07-red-flag-signs.png | `#p-start` | 1024×1024 | williamriveromd-simple-figure | Wired in guide |
| 002 | P0 | 01-three-tests-three-questions.png | `#p-start` | 1792×1024 | williamriveromd-infographic-skill | Wired in guide (revised prompt — simpler wording) |
| 003 | P1 | 08-calcium-three-helpers.png | `#p-blood` | 1024×1024 | williamriveromd-simple-figure | Wired in guide |
| 004 | P1 | 09-kidney-recovers-calcium.png | `#p-urine` | 1792×1024 | williamriveromd-simple-figure | Wired in guide |
| 005 | P0 | 10-calcium-binds-oxalate-myth.png | `#p-urine` | 1792×1024 | williamriveromd-simple-figure | Wired in guide |
| 006 | P0 | 02-nephrocalcinosis-versus-stone.png | `#p-kidney` | 1792×1024 | williamriveromd-biomedical-mechanism-figure | Wired in guide (revised prompt — adds kettle analogy) |
| 007 | P0 | 11-how-to-collect-24-hour-urine.png | `#p-tests` | 1792×1024 | williamriveromd-simple-figure | Wired in guide |
| 008 | P0 | 12-filipino-stone-smart-plate.png | `#p-prevent` | 1536×1152 | williamriveromd-infographic-skill | Wired in guide |
| 009 | P0 | 03-renal-calcium-handling.png | `#md-physio` | 1792×1024 | williamriveromd-biomedical-mechanism-figure | Wired in guide |
| 010 | P1 | 13-hypocalcemia-workup-algorithm.png | `#md-lowca` | 1024×1536 | williamriveromd-algorithm-generator-skill | Wired in guide |
| 011 | P0 | 14-hypopt-balance.png | `#md-hypopt` | 1792×1024 | williamriveromd-simple-figure | Wired in guide |
| 012 | P1 | 15-reading-24-hour-urine-card.png | `#md-urine` | 1536×1152 | williamriveromd-infographic-skill | Wired in guide |
| 013 | P0 | 04-nephrocalcinosis-phenotype-map.png | `#md-nc` | 1536×1152 | williamriveromd-algorithm-generator-skill | Wired in guide |
| 014 | P1 | 16-acute-stone-pathway.png | `#md-acute` | 1024×1536 | williamriveromd-algorithm-generator-skill | Wired in guide |
| 015 | P0 | 05-stone-prevention-levers.png | `#md-prevent` | 1536×1152 | williamriveromd-algorithm-generator-skill | Wired in guide |
| 016 | P0 | 17-absolute-effects-icon-arrays.png | `#md-absolute` | 1792×1024 | williamriveromd-infographic-skill | Wired in guide |
| 017 | P2 | 18-three-case-snapshots.png | `#md-cases` | 1792×1024 | williamriveromd-infographic-skill | Wired in guide |
| 019 | P1 | 19-randall-plaque-to-stone.png | `#md-physio` | 1792×1024 | williamriveromd-biomedical-mechanism-figure | Wired in guide |
| 018 | P0 | og.png | `head` | 1200×630 | williamriveromd-infographic-skill | Referenced in head meta |

Images marked **Wired in guide** already have `<picture>` slots in the HTML and appear as soon as the files land in `images/`. Images marked **New** need a figure slot added; send the generated files and they will be wired with the four-language captions.

## 5. Production workflow

1. Open https://chatgpt.com/ (the retired "Image Generator" GPT link must not be used).
2. Paste one prompt per message: the **PROMPT**, then the **NEGATIVE INSTRUCTIONS**. Ask for the stated pixel size.
3. Check the result against the **QUALITY CHECK** line, especially spelling and numbers. Regenerate rather than accept a misspelled label.
4. Save as the exact **FILE NAME** in `~/Downloads/calcium-disorders-and-kidney-stones/generated-images/`.
5. Drop the files in a chat; they will be converted to WebP, given 800 px responsive copies, wired into the guide with alt text and captions, and checked in light and dark mode.

---

