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

## 6. Prompts

### 6A. Hero

#### 000 · calcium-disorders-and-kidney-stones-vignette-hero.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Hero, circular vignette beside the title (patient view) (`hero`) |
| Skill | williamriveromd-hero-vignette (v3, Scaffold A) |
| Archetype | Circular vignette hero — composition H (Clinical), camera over-the-shoulder |
| Audience | Mixed (patients first) |
| Size | 2048 × 2048 (1:1) |
| Reader takeaway | Real people are sorting out a calcium question together; this guide is calm and practical. |
| Why it works for every reader | No words at all, so it reads the same in all four languages. One scene, one action (pointing at a scan) that every reader understands. |

**PROMPT**

```text
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder from behind the clinician, slightly above desk height. Subject: a Filipina patient in her early forties with a round face, short wavy shoulder-length dark-brown hair tucked behind one ear, light-brown skin and a slim build, wearing a mustard-yellow knit cardigan over a white tee and small gold stud earrings, sitting upright and attentive with one hand resting on a capped, translucent 24-hour urine collection container on the desk. Across from her, seen over his shoulder, a Filipino male nephrologist in his late thirties with close-cropped black hair and rimless glasses, pale-blue shirt sleeves rolled under a white coat, pointing with a pen to a grayscale kidney ultrasound image on a tablet (no readable text). Bright modern Philippine outpatient clinic, soft side-window daylight, one potted snake plant and a water tumbler as the only props, gentle shallow depth of field. Hierarchy: people and desk fill 60–70% of the circle; supporting context 20–30%; a 20–25% TITLE-SAFE ZONE of softly blurred pale-teal wall in the upper left with no faces or objects. Calm documentary color grade harmonizing with teal #1a6b72 and navy #0f1e2e on a light background, soft falloff at the rim. Absolutely NO text, labels, screen text, logo or watermark.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid collage, more than four supporting elements, duplicated people, a cropped circle or anything touching the circular border, content in the title-safe zone, baked-in text, logos, watermarks, rectangular frames, dark backgrounds, cartoon style, HDR, distorted hands or faces. Avoid the overused site archetypes: older diner, couple at a dining table, teal polo shirt, beige blouse, wooden dining table, salmon plate.
```

**QUALITY CHECK:** Square 2048×2048; circle 85–90% with white margin; no text anywhere; title-safe zone empty; at least 12 human traits differ from recent heroes.

**ALT TEXT:** A Filipina in her forties sits with her nephrologist at a bright clinic desk, holding a 24-hour urine collection container while the doctor points to a kidney ultrasound image on a tablet

---

### 6B. Patients & Families

#### 001 · calcium-disorders-and-kidney-stones-07-red-flag-signs.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Patients · Start Here — top, directly under the red emergency box (`#p-start`) |
| Skill | williamriveromd-simple-figure (Scaffold: square quick-look card) |
| Archetype | Square reference card / quick-look |
| Audience | Patients and families |
| Size | 1024 × 1024 (1:1) |
| Reader takeaway | These six signs mean go to the emergency room now. |
| Why it works for every reader | Pictures carry the meaning; each word label is 1–3 words. Red frame plus a hospital icon signals urgency without relying on color. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Square 1:1 quick-look card, 1024×1024, titled "Go to the ER now" with a small hospital-cross icon. Two rounded red-outlined groups of large friendly illustrated icons, each with a 1–3 word label beneath: Group 1 header "Low calcium signs": "Seizure", "Hand or face spasm" (fingers drawn into a cramp), "Hard to breathe", "Fainting or racing heart". Group 2 header "Blocked, infected kidney": "Side pain + fever" (person holding the flank with a thermometer), "Little or no urine", "Cannot stop vomiting". A bottom strip in pale amber: "One kidney, a transplant, or pregnant? Go sooner." Icons depict a Filipino adult in simple semi-realistic style; generous spacing; labels large enough to read on a phone. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Exactly seven icons with the labels as written; red framing paired with icons; readable at 360 px wide; attribution present.

**ALT TEXT:** Emergency warning card with icons: seizure, hand or face spasm, trouble breathing, fainting or racing heart, side pain with fever, little or no urine, and nonstop vomiting

---

#### 002 · calcium-disorders-and-kidney-stones-01-three-tests-three-questions.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Patients · Start Here — after the four-word cards (`#p-start`) |
| Skill | williamriveromd-infographic-skill (multi-panel educational) |
| Archetype | Multi-panel Educational |
| Audience | Patients and families |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Blood, urine and a scan each answer a different calcium question, and they can disagree. |
| Why it works for every reader | Three big objects that people already know (tube, jug, scan) anchor three short questions. The key surprise, "low in blood, high in urine", sits alone in the bottom band with up and down arrows. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 infographic, 1792×1024, title "Three tests, three questions". Three equal rounded panels, each with one large illustrated object and a short question underneath: (1) a blood collection tube in a gloved hand — "Blood test: How much calcium is in my blood now?"; (2) a translucent 24-hour urine container beside a small clock face — "24-hour urine: How much calcium do my kidneys let go?"; (3) a soft 3D kidney cutaway with fine white specks in the inner pyramids labeled "Specks inside the kidney" and a small stone in the ureter labeled "Stone in the urine tube" — "Scan: Where did calcium settle?". Bottom band in light teal with a blood-drop icon and a down arrow, a urine-drop icon and an up arrow: "Calcium can be LOW in blood and HIGH in urine at the same time." Short labels only. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Three equal panels; labels spelled exactly; specks in pyramids, stone in ureter; arrows unambiguous; attribution present.

**ALT TEXT:** Three panels: a blood tube asking how much calcium is in the blood, a 24-hour urine container asking how much the kidneys release, and a kidney scan showing specks inside the kidney and a stone in the urine tube

---

#### 003 · calcium-disorders-and-kidney-stones-08-calcium-three-helpers.png

| Field | Value |
|---|---|
| Priority | P1 |
| Placement | Patients · Low Blood Calcium — after the first paragraph (`#p-blood`) |
| Skill | williamriveromd-simple-figure (circular / loop diagram) |
| Archetype | Circular Workflow |
| Audience | Patients and families |
| Size | 1024 × 1024 (1:1) |
| Reader takeaway | Three helpers keep blood calcium steady: parathyroid hormone, activated vitamin D and magnesium. |
| Why it works for every reader | A thermostat analogy (calcium as the room temperature, PTH as the thermostat) gives every reader a model; arrows show "pulls from bone, holds in kidney, absorbs from food". |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Square 1:1 circular diagram, 1024×1024, title "Three helpers keep blood calcium steady". Center: a large blood drop containing a simple dial gauge labeled "Blood calcium". Around it, three soft 3D helper icons connected by teal arrows: the four small parathyroid glands behind a semi-transparent thyroid in the neck labeled "Parathyroid hormone (PTH)"; a kidney labeled "Kidney makes active vitamin D"; a small sparkle-like mineral icon labeled "Magnesium (helps PTH work)". Outer ring with three action arrows feeding the center: from a bone "Releases calcium from bone", from the kidney "Keeps calcium in", from the gut "Absorbs calcium from food". Small amber note at the bottom: "If a helper is missing, calcium falls: tingling, cramps". Labels short and large. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution. Show four parathyroid glands behind the thyroid, not inside the kidney.
```

**QUALITY CHECK:** Four parathyroid glands correctly placed; three helpers and three actions; arrows point into the blood-calcium center; attribution present.

**ALT TEXT:** Circular diagram of three helpers that keep blood calcium steady: parathyroid hormone from the neck glands, activated vitamin D from the kidney, and magnesium, acting on bone, kidney and gut

---

#### 004 · calcium-disorders-and-kidney-stones-09-kidney-recovers-calcium.png

| Field | Value |
|---|---|
| Priority | P1 |
| Placement | Patients · High Urine Calcium — after the "Common drivers" paragraph (`#p-urine`) |
| Skill | williamriveromd-simple-figure (side-by-side comparison) |
| Archetype | Side-by-side comparison |
| Audience | Patients and families |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | The kidney normally takes back almost all the calcium it filters; salt and some conditions make it let more slip into the urine. |
| Why it works for every reader | A recycling sieve analogy: many drops go through the filter, almost all are caught and returned. Left = normal, right = leaky. No percentages, so nothing to calculate. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 comparison, 1792×1024, title "Your kidney recycles calcium". Left panel header in green with a check icon: "Normal": a soft 3D kidney filter shown as a fine sieve; many small white calcium drops pass in, a curved teal arrow returns almost all of them to a blood vessel labeled "Back to blood", and only a few drops fall into a urine cup labeled "A little in urine". Right panel header in amber with a caution icon: "Too much in urine": the same sieve with more drops falling into a fuller urine cup; around it four small labeled icons: a salt shaker over patis and toyo bottles "Salty food", a meat platter "Lots of meat", a pill bottle "Too much calcium or vitamin D pills", a neck-gland icon "Overactive parathyroid". Bottom line: "Less salt = less calcium lost in urine." Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Left shows few drops lost, right shows more; four causes with labels; no numbers; attribution present.

**ALT TEXT:** Side-by-side picture of the kidney as a recycling sieve: normally almost all calcium returns to the blood, while salty food, lots of meat, excess pills or an overactive parathyroid let more calcium spill into the urine

---

#### 005 · calcium-disorders-and-kidney-stones-10-calcium-binds-oxalate-myth.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Patients · High Urine Calcium — inside or right after the myth box (`#p-urine`) |
| Skill | williamriveromd-simple-figure (side-by-side comparison) |
| Archetype | Side-by-side comparison |
| Audience | Patients and families |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Eating normal calcium with meals protects against stones; cutting calcium backfires. |
| Why it works for every reader | Myth on the left with a cross, fact on the right with a check. The mechanism is shown as calcium "catching" oxalate in the gut so it leaves in the stool, a picture most readers can follow without the chemistry. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 myth-versus-fact figure, 1792×1024, title "Do not cut calcium to prevent stones". Left panel with a red cross icon, header "Myth: avoid calcium": a plate with rice and a vegetable dish but no milk; a soft 3D intestine where loose orange oxalate particles pass through the gut wall toward a kidney, small label "More oxalate reaches the urine", plus a faded bone icon "Weaker bones". Right panel with a green check icon, header "Fact: calcium WITH meals": a Filipino meal of rice, ginisang gulay and a glass of milk (or a small dish of tokwa); in the intestine, white calcium particles hook onto orange oxalate particles and exit toward the stool, label "Calcium catches oxalate in the gut", and a strong bone icon "Stronger bones". Bottom strip: "Extra calcium PILLS are different — ask your doctor." Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Cross/check icons present; calcium–oxalate binding drawn inside the gut, not the kidney; pill caveat present; attribution present.

**ALT TEXT:** Myth versus fact: avoiding calcium lets more oxalate reach the urine and weakens bones, while calcium eaten with meals binds oxalate in the gut and protects bones

---

#### 006 · calcium-disorders-and-kidney-stones-02-nephrocalcinosis-versus-stone.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Patients · Specks vs Stones — under the section heading (`#p-kidney`) |
| Skill | williamriveromd-biomedical-mechanism-figure (patient-simplified organ panel) |
| Archetype | Pathophysiology Mechanism Poster |
| Audience | Patients and families |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Specks inside the kidney tissue are different from a stone in the urine pipes, and a blocked stone causes swelling above it. |
| Why it works for every reader | Uses the kettle analogy from the text as a small inset (scale on the walls versus a loose lump in the spout), then the real anatomy. Card text is three short lines each. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 medical illustration, 1792×1024, title "Specks inside the kidney vs a stone in the pipes". Left two-thirds: semi-photorealistic 3D coronal cutaway of one kidney showing outer cortex, inner pyramids, calyces, renal pelvis and upper ureter. Fine white granular calcium specks inside several pyramids, leader label "Specks inside kidney tissue (nephrocalcinosis)". A tan crystalline stone in the renal pelvis labeled "Stone in the collecting space", and a second small stone in the upper ureter with the ureter and pelvis visibly swollen above it, labeled "Stone blocking urine — swelling above". Small round inset at top left: a kettle with mineral scale coating its inner walls ("specks") and one loose lump in the spout ("stone"). Right third: two stacked cards — "Specks": "Usually silent", "Seen on ultrasound or CT", "A clue to a chemistry problem"; "Stone": "Can move and hurt", "Blood in urine or infection", "Fever + blockage = emergency" (with a small red warning icon). Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Specks in pyramids, not in the pelvis; obstruction shows proximal dilation; kettle inset small; card text exact; attribution present.

**ALT TEXT:** Cutaway kidney contrasting fine calcium specks in the inner pyramids with a stone in the renal pelvis and another blocking the ureter, with a small kettle analogy inset

---

#### 007 · calcium-disorders-and-kidney-stones-11-how-to-collect-24-hour-urine.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Patients · Tests — replaces or sits beside the 24-hour collection steps (`#p-tests`) |
| Skill | williamriveromd-simple-figure (horizontal step sequence) |
| Archetype | Horizontal step sequence |
| Audience | Patients and families |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Flush the first morning urine, collect everything for 24 hours, and add the last urine at the same time next morning. |
| Why it works for every reader | Five numbered pictures with a clock in each, so the sequence is clear even if the words are skipped. The two error-prone moments (discard the first, KEEP the last) are highlighted with a cross and a check. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 five-step picture strip, 1792×1024, title "How to collect a 24-hour urine". Five numbered rounded cards left to right connected by teal arrows, each with a simple semi-realistic illustration, a small clock face and a 2–5 word caption: 1 clock at 7:00 on day 1, a person flushing the toilet, red cross over a container — "Day 1, 7 AM: flush it"; 2 a pen writing on a label — "Write the start time"; 3 urine poured into a large translucent container, sun and moon icons — "Collect ALL urine, day and night"; 4 the container in a cool shaded spot or a cooler with ice — "Keep it cool"; 5 clock at 7:00 on day 2, a green check over the container — "Day 2, 7 AM: ADD this one". Bottom note in amber: "Missed or spilled some? Tell the lab — do not guess." Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Five steps in order; step 1 shows discard (cross), step 5 shows keep (check); both clocks at the same time; attribution present.

**ALT TEXT:** Five-step picture guide to a 24-hour urine collection: flush the first morning urine, write the start time, collect all urine day and night, keep it cool, and add the final urine at the same time the next morning

---

#### 008 · calcium-disorders-and-kidney-stones-12-filipino-stone-smart-plate.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Patients · Prevention — after the habits table (`#p-prevent`) |
| Skill | williamriveromd-infographic-skill (food matrix) |
| Archetype | Food Matrix |
| Audience | Patients and families |
| Size | 1536 × 1152 (4:3) |
| Reader takeaway | Keep calcium foods with meals, cut salty condiments and processed foods, keep meat portions moderate, and drink water if your doctor agrees. |
| Why it works for every reader | Real Filipino foods instead of nutrient names; three columns with plain verbs ("Keep", "Cut down", "Watch"). Works for readers who think in dishes, not milligrams. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 4:3 food matrix, 1536×1152, title "A stone-smart Filipino plate". Three columns of realistically rendered foods on light cards. Column 1, green header with a check icon, "Keep (with meals)": glass of milk, plain yogurt, small dried fish with bones (dilis), tokwa, a bowl of rice with ginisang gulay, a glass of water. Column 2, red header with a down-arrow icon, "Cut down": patis, toyo and bagoong bottles, instant noodles, chichirya, canned meat (corned beef, luncheon meat), longganisa, soft drinks. Column 3, amber header with an eye icon, "Watch the portion": a large meat serving, organ meats, sardines; small note "If your urine oxalate is high: strong tea, spinach, nuts"; a vitamin C pill bottle "No high-dose vitamin C". Bottom band: a water glass icon with "Drink enough to pass about 2.5 liters of urine a day — if your doctor says it is safe for your heart and kidneys". No brand names or readable packaging text. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution. No real brand logos or readable product labels.
```

**QUALITY CHECK:** Foods recognizable and Filipino; three columns with icons; 2.5 L phrase includes the safety condition; no brands; attribution present.

**ALT TEXT:** Food chart of a stone-smart Filipino plate: keep milk, yogurt, small fish with bones, tokwa and water with meals; cut down patis, toyo, bagoong, instant noodles, processed meats and soft drinks; watch large meat portions and high-dose vitamin C

---

### 6C. Clinicians

#### 009 · calcium-disorders-and-kidney-stones-03-renal-calcium-handling.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Clinicians · Physiology — under the section heading (`#md-physio`) |
| Skill | williamriveromd-biomedical-mechanism-figure |
| Archetype | Pathophysiology Mechanism Poster |
| Audience | Clinicians |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | About 65% of filtered calcium is reclaimed proximally with sodium, 20–25% in the TAL under CaSR control, and 5–10% distally under PTH; thiazides raise and loops lower reabsorption. |
| Why it works for every reader | Organ → nephron → cell zoom keeps the scale clear; one summary row translates the physiology into what raises or lowers urine calcium. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Publication-grade biomedical mechanism figure, landscape 16:9, 1792×1024, title "How the kidney decides how much calcium to keep", dashed connector lines. Left panel: a small kidney with one nephron highlighted; dashed box links to the main panel. Center panel (dashed border): one nephron from glomerulus to collecting duct; three segments highlighted pale yellow with callouts: Proximal tubule "~65% of filtered Ca2+ · paracellular · follows Na+ and water"; Thick ascending limb "20–25% · paracellular via claudin-16/19 · lumen-positive voltage", a basolateral receptor icon "CaSR activated → less Ca2+ reabsorbed", drug tag "Loop diuretic → more urine Ca2+"; Distal convoluted and connecting tubule "5–10% · transcellular via TRPV5 · regulated by PTH and calcitriol", drug tag at NCC "Thiazide → less urine Ca2+". Right inset (dashed circle): one distal tubular cell with apical TRPV5 channel, calbindin shuttle, basolateral NCX1 exchanger and PMCA pump, and a basolateral PTH receptor. Bottom flow of three boxes: pink "More urine calcium: high sodium intake · loop diuretics · no PTH (HypoPT) · activating CASR variants (ADH1)" → white "Tubular calcium reabsorption" → blue "Less urine calcium: thiazide · lower sodium · PTH replacement". Use only these numbers. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution. Do not place TRPV5 in the proximal tubule or claudin-16/19 in the distal tubule; do not draw thiazide action in the loop of Henle.
```

**QUALITY CHECK:** Percentages exactly 65%, 20–25%, 5–10%; CaSR basolateral in TAL; TRPV5 apical in DCT; drug sites correct; superscripts legible; attribution present.

**ALT TEXT:** Nephron schematic of calcium reabsorption in the proximal tubule, thick ascending limb and distal tubule, showing the calcium-sensing receptor, TRPV5, PTH and calcitriol regulation, and the opposite effects of thiazide and loop diuretics

---

#### 010 · calcium-disorders-and-kidney-stones-13-hypocalcemia-workup-algorithm.png

| Field | Value |
|---|---|
| Priority | P1 |
| Placement | Clinicians · Hypocalcemia — replaces or sits beside the workup algorithm card (`#md-lowca`) |
| Skill | williamriveromd-algorithm-generator-skill (house-style algorithm) |
| Archetype | Clinical Algorithm |
| Audience | Clinicians |
| Size | 1024 × 1536 (2:3) |
| Reader takeaway | Triage symptoms, confirm with ionized calcium, fix magnesium, then classify by PTH and phosphate. |
| Why it works for every reader | One vertical spine with red, teal and navy nodes; PTH-branch outcomes are short disease names with one next step each. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Portrait 2:3 clinical algorithm, 1024×1536, renalcarematters.com house style: thin teal arrows, pastel rounded boxes, red escalation nodes, teal decision diamonds, generous margins. Title "Low calcium: confirm, then classify". Top red node: "Seizure, tetany, laryngospasm, arrhythmia? → ER: ECG monitoring, IV calcium gluconate per protocol, correct magnesium". Then teal node: "Confirm: repeat; measured ionized calcium if albumin, CKD, critical illness or acid–base will change management". Then navy node: "Draw together: intact PTH, Ca, Mg, phosphate, creatinine/eGFR, albumin, 25-OHD; review neck surgery, denosumab, PPIs, transfusion". Amber node: "Correct magnesium first". Decision diamond "PTH?" splits: left "Low or inappropriately normal" → boxes "High phosphate → hypoparathyroidism (postsurgical >12 months = chronic)" and "Young, familial, high urine Ca → ADH1/ADH2: genetic testing; do not chase normal calcium"; right "High" → boxes "Low phosphate, low 25-OHD → vitamin D deficiency or malabsorption", "High phosphate, low eGFR → CKD-MBD pathway", "High phosphate, normal eGFR → PTH resistance". Side note in gray: "Denosumab on dialysis: check calcium within weeks of the dose". Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-center corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Emergency node first; magnesium before PTH branch; five outcomes correct; only stated numbers (>12 months); attribution bottom-center.

**ALT TEXT:** Clinical algorithm for low calcium: emergency triage, confirmation with ionized calcium, magnesium correction, then classification by PTH and phosphate into hypoparathyroidism, ADH1, vitamin D deficiency, CKD-MBD or PTH resistance

---

#### 011 · calcium-disorders-and-kidney-stones-14-hypopt-balance.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Clinicians · Chronic HypoPT — after the ESE table (`#md-hypopt`) |
| Skill | williamriveromd-simple-figure (single mechanism / one-panel poster) |
| Archetype | Single mechanism poster |
| Audience | Clinicians (and advanced patients) |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Without PTH, pushing blood calcium higher sends more calcium into the urine; aim low-normal and keep urine calcium normal. |
| Why it works for every reader | A balance scale makes the trade-off visible: blood calcium on one pan, urine calcium on the other. The "do not" arrow is the single message. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 concept figure, 1792×1024, title "Hypoparathyroidism: the calcium balancing act". Center: a soft 3D balance scale. Left pan labeled "Blood calcium" with a gauge needle in a green band marked "low-normal target"; right pan labeled "Urine calcium" with a filling urine cup. Below the scale, a kidney icon with a crossed-out PTH key at the distal tubule labeled "No PTH: distal tubule cannot hold calcium". A large amber arrow from a stack of calcium tablets and an active vitamin D capsule pushes the left pan up while the right cup overflows, labeled "Pushing blood calcium higher → more urine calcium → stones, nephrocalcinosis". Right side card titled "If urine calcium is high" with icons: "Rebalance calcium + active vitamin D together", "Lower sodium", "Consider a thiazide (monitor K, Mg, creatinine)", "Recheck in 1–2 weeks", "Persistent? Consider PTH replacement". Small footer box: "ESE 2025 hypercalciuria: >250 mg/24 h women, >300 mg/24 h men, or >4 mg/kg/24 h". Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Thresholds exactly as given with ">" signs; scale direction logical; five response icons; attribution present.

**ALT TEXT:** Balance-scale illustration showing that in hypoparathyroidism, raising blood calcium with tablets and active vitamin D increases urine calcium, with the ESE thresholds and the recommended responses

---

#### 012 · calcium-disorders-and-kidney-stones-15-reading-24-hour-urine-card.png

| Field | Value |
|---|---|
| Priority | P1 |
| Placement | Clinicians · Stone Risk Testing — after the context-threshold table (`#md-urine`) |
| Skill | williamriveromd-infographic-skill (clinician reference card) |
| Archetype | Compact Reference Card |
| Audience | Clinicians |
| Size | 1536 × 1152 (4:3) |
| Reader takeaway | Validate the collection first, read volume, then calcium beside sodium, then oxalate, citrate, uric acid and pH, and apply only the threshold that fits the context. |
| Why it works for every reader | A numbered reading order on the left and a three-row threshold table on the right; each threshold carries its source badge so it is never generalized. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 4:3 clinician reference card, 1536×1152, title "Reading a 24-hour urine". Left half: six numbered rounded steps with small icons: "1 Valid? Timing, missed voids, creatinine vs body size", "2 Volume first", "3 Calcium beside sodium", "4 Oxalate · citrate · uric acid · pH", "5 Optional: sulfate/urea N, ammonium, Mg, cystine, supersaturation", "6 Exclude secondary causes before 'idiopathic'". Right half: a clean three-row table titled "Urine calcium thresholds depend on context" with source badges: "Adult hypoparathyroidism — >250 mg/24 h women · >300 mg/24 h men · >4 mg/kg/24 h — ESE 2025"; "Recurrent calcium stones — ≥200 mg/24 h women · ≥250 mg/24 h men (examples) — AUA 2026"; "Calcium phosphate stones — >8 mmol/24 h → thiazide — EAU". Footer line: "Children: age-specific Ca/Cr ratios; adult cutoffs do not apply." Use only these numbers. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Six steps in order; three threshold rows exactly as given with correct > and ≥ signs and sources; attribution present.

**ALT TEXT:** Clinician reference card with a six-step reading order for a 24-hour urine and a table of context-specific urinary calcium thresholds from ESE 2025, AUA 2026 and EAU

---

#### 013 · calcium-disorders-and-kidney-stones-04-nephrocalcinosis-phenotype-map.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Clinicians · Nephrocalcinosis — under the section heading (`#md-nc`) |
| Skill | williamriveromd-algorithm-generator-skill (wide house-style algorithm) |
| Archetype | Wide Clinical Algorithm |
| Audience | Clinicians |
| Size | 1536 × 1152 (4:3) |
| Reader takeaway | The scan says where calcium settled; the labs say why — and most medullary causes are treatable. |
| Why it works for every reader | Two-branch tree (medullary versus cortical) with six phenotype boxes, each ending in a named cause and one action. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 4:3 clinical algorithm, 1536×1152, thin teal arrows, pastel rounded boxes, small grayscale ultrasound thumbnails as icons only. Title "Nephrocalcinosis: find the cause". Top node "Nephrocalcinosis on imaging" splits into "Medullary" (large, left) and "Cortical" (small, right). Cortical → "Prior cortical injury: cortical necrosis, chronic glomerulonephritis, transplant rejection". Medullary → teal box "Check serum Ca, PTH, phosphate, Mg, bicarbonate, K; 24-h urine Ca, oxalate, citrate, pH; urine β2-microglobulin" → six boxes in two rows: "High Ca + non-suppressed PTH → primary hyperparathyroidism → parathyroidectomy evaluation"; "High Ca + suppressed PTH → vitamin D excess, granulomatous disease, CYP24A1"; "Normal anion gap acidosis, low K, alkaline urine, low citrate → distal RTA (exclude infection)"; "Marked urine oxalate or CKD out of proportion → primary or enteric hyperoxaluria"; "Low Ca + low PTH + high urine Ca → ADH1 or over-treated hypoparathyroidism"; "Low Mg or low-molecular-weight proteinuria → claudin-16/19 or Dent disease". Footer strip: "Escalate early: early onset, family history, bilateral or progressive calcification, falling eGFR". Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Branch logic matches; abbreviations spelled correctly; boxes aligned; attribution present.

**ALT TEXT:** Diagnostic map pairing medullary or cortical nephrocalcinosis with laboratory patterns that point to primary hyperparathyroidism, vitamin D excess, distal renal tubular acidosis, hyperoxaluria, ADH1 or tubular disorders

---

#### 014 · calcium-disorders-and-kidney-stones-16-acute-stone-pathway.png

| Field | Value |
|---|---|
| Priority | P1 |
| Placement | Clinicians · Acute Stones — after the imaging and analgesia paragraphs (`#md-acute`) |
| Skill | williamriveromd-algorithm-generator-skill (house-style algorithm) |
| Archetype | Clinical Algorithm |
| Audience | Clinicians |
| Size | 1024 × 1536 (2:3) |
| Reader takeaway | Infection or obstruction red flags mean drain first; otherwise analgesia, imaging, and expulsive therapy mainly for distal stones over 5 mm. |
| Why it works for every reader | A red "stop" branch at the top makes the emergency override impossible to miss; the routine branch is three boxes. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Portrait 2:3 clinical algorithm, 1024×1536, thin teal arrows, pastel rounded boxes, red escalation nodes. Title "Acute kidney stone: first decisions". Top diamond "Fever, sepsis, anuria, AKI, solitary or transplanted kidney?" YES (red) → "Cultures + antibiotics → urgent stent or percutaneous nephrostomy → treat the stone after infection clears". NO → navy box "Analgesia: NSAID if safe (kidney function, bleeding, pregnancy); no forced fluids" → teal box "Imaging: low-dose non-contrast CT (adults); ultrasound first in pregnancy and children" → diamond "Distal ureteral stone >5 mm, uncomplicated?" YES → green box "Offer alpha-blocker (off-label), planned reassessment"; NO → gray box "Small stones usually pass; MET adds little". Bottom box: "Refractory pain, persistent obstruction or no passage → urology: SWL, ureteroscopy, or PCNL (renal stones >20 mm)". Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-center corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Emergency branch first and red; >5 mm and >20 mm exact; abbreviations correct; attribution bottom-center.

**ALT TEXT:** Clinical algorithm for an acute kidney stone: drain first if infection or obstruction red flags are present; otherwise analgesia, imaging, and alpha-blocker therapy mainly for distal stones larger than 5 mm, with urology referral when needed

---

#### 015 · calcium-disorders-and-kidney-stones-05-stone-prevention-levers.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Clinicians · Prevention — under the section heading (`#md-prevent`) |
| Skill | williamriveromd-algorithm-generator-skill (wide house-style algorithm) |
| Archetype | Wide Clinical Algorithm |
| Audience | Clinicians |
| Size | 1536 × 1152 (4:3) |
| Reader takeaway | General measures for everyone, a drug matched to the 24-hour urine abnormality, then re-measure. |
| Why it works for every reader | Top-down funnel: one green box for everyone, four amber branches by abnormality, one navy box to re-measure. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 4:3 clinical algorithm, 1536×1152, thin teal arrows, pastel rounded boxes. Title "Calcium stone prevention". Top green box "All calcium stone formers (if eligible)": "Urine output about 2.5 L/day (individualize for heart failure, advanced CKD, dialysis)", "Dietary calcium 1,000–1,200 mg/day with meals", "Limit sodium: patis, toyo, instant noodles, processed meats", "Moderate animal protein", "Limit soft drinks; no high-dose vitamin C". Arrow to teal diamond "Complete 24-hour urine on usual diet: what is abnormal?" → four amber boxes: "High urine calcium → thiazide or thiazide-like diuretic (shared decision; monitor K, Na, Mg, uric acid, glucose, creatinine)"; "Low citrate or distal RTA → potassium citrate (check K, eGFR; watch urine pH in calcium phosphate stones)"; "High uric acid, normal calcium, calcium oxalate stones → allopurinol"; "High oxalate after bowel or bariatric surgery → calcium with meals, lower fat, more fluid, dietitian". All converge on navy box "Repeat 24-hour urine 8–12 weeks after starting drug prevention, then about yearly". Gray side note: "Fever with obstruction or anuria overrides this pathway". Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** Numbers only 2.5 L, 1,000–1,200 mg, 8–12 weeks; drug pairings exact; attribution present.

**ALT TEXT:** Clinical algorithm for calcium stone prevention: general measures for all patients, then a medicine matched to the 24-hour urine abnormality, then a repeat collection

---

#### 016 · calcium-disorders-and-kidney-stones-17-absolute-effects-icon-arrays.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Clinicians · Absolute Effects — above the trials table (`#md-absolute`) |
| Skill | williamriveromd-infographic-skill (multi-panel educational, icon arrays) |
| Archetype | Multi-panel Educational |
| Audience | Clinicians and patients (shared decisions) |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Diet changed outcomes; hydrochlorothiazide and a hydration-coaching program did not clearly reduce stone events. |
| Why it works for every reader | 100-person icon arrays let any reader see "20 versus 38 out of 100" without understanding relative risk; the same picture works for shared decision-making in clinic. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 figure, 1792×1024, title "What the trials mean for 100 people". Three panels, each with two 10×10 grids of simple person icons; filled amber icons = people who had a stone event, outlined gray icons = no event. Panel 1 "Diet (Borghi, 5 years)": left grid "Low-calcium diet: 38 of 100", right grid "Normal calcium, less salt and meat: 20 of 100", green badge "About 18 fewer per 100". Panel 2 "Hydrochlorothiazide (NOSTONE, ~3 years)": left "Placebo: 59 of 100", right "50 mg daily: 49 of 100", gray badge "Difference not statistically certain · more side effects". Panel 3 "Hydration coaching (PUSH, 2 years)": left "Usual care: 20 of 100", right "Coaching program: 19 of 100", gray badge "No real difference". Each grid must show exactly the stated number of filled icons. Small footer: "Randomized trials; events = symptomatic or radiologic recurrence as defined by each trial." Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution. Fill exactly 38, 20, 59, 49, 20 and 19 icons; do not round or invent other numbers.
```

**QUALITY CHECK:** Icon counts exactly 38/20, 59/49, 20/19; badges as written; attribution present.

**ALT TEXT:** Icon arrays for 100 people: a normal-calcium low-salt diet lowered five-year stone recurrence from 38 to 20, while hydrochlorothiazide (59 versus 49) and a hydration coaching program (20 versus 19) showed no clear difference

---

#### 017 · calcium-disorders-and-kidney-stones-18-three-case-snapshots.png

| Field | Value |
|---|---|
| Priority | P2 |
| Placement | Clinicians · Cases — under the section heading (`#md-cases`) |
| Skill | williamriveromd-infographic-skill (case snapshot) |
| Archetype | Case Snapshot |
| Audience | Clinicians |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Three patterns: low blood + high urine calcium after surgery; dRTA with nephrocalcinosis; low volume + high sodium in a stone former. |
| Why it works for every reader | One card per case with three lab chips and one teaching pearl, so learners compare patterns side by side. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Landscape 16:9 case snapshot, 1792×1024, title "Three patients, three patterns". Three equal cards. Card 1 (neck-gland icon) "After thyroid surgery": chips "Ionized Ca: low", "PTH: low", "Urine Ca: 320 mg/day"; pearl "Do not add calcium — rebalance, lower salt, consider thiazide". Card 2 (kidney with medullary specks icon) "Specks + calcium phosphate stones": chips "Bicarbonate 17 mmol/L", "K 3.1 mmol/L", "Urine pH 6.1 fasting · 6.7 (24 h)"; pearl "Suspect distal RTA — specialist confirmation". Card 3 (urine container icon) "Recurrent calcium oxalate stones": chips "Volume 1.6 L/day", "Sodium 220 mmol/day", "Calcium 290 mg/day"; pearl "Close the 0.9 L output gap, cut sodium, then reassess". Use only these numbers. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** All numbers exactly as given; three cards equal; attribution present.

**ALT TEXT:** Three case cards: low blood and high urine calcium after thyroid surgery, suspected distal renal tubular acidosis with nephrocalcinosis, and a recurrent stone former with low urine volume and high sodium

---

#### 019 · calcium-disorders-and-kidney-stones-19-randall-plaque-to-stone.png

| Field | Value |
|---|---|
| Priority | P1 |
| Placement | Clinicians · Physiology — after the Randall plaque paragraph (`#md-physio`) |
| Skill | williamriveromd-biomedical-mechanism-figure |
| Archetype | Pathophysiology Mechanism Poster |
| Audience | Clinicians (with a lay-reader analogy inset) |
| Size | 1792 × 1024 (16:9) |
| Reader takeaway | Many calcium oxalate stones grow on Randall plaque, a calcium phosphate patch that starts around the thin loops of Henle; higher urine calcium and lower volume go with more plaque. |
| Why it works for every reader | A four-step left-to-right story (start, spread, exposed, stone grows) with a small barnacle-on-a-rock inset gives non-specialists a model; the contrast panel separates plaque from intratubular plugs for clinicians. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Publication-grade biomedical mechanism figure, landscape 16:9, 1792×1024, title "From Randall plaque to kidney stone", dashed connector lines. Left panel (organ context): a small kidney cutaway with one papilla circled; dashed box leads to the main panel. Main panel (dashed border): a magnified longitudinal section of one renal papilla tip in four numbered stages from left to right: 1 "Starts here": tiny white calcium phosphate granules in the basement membrane of a thin loop of Henle (label "Thin loop of Henle"); 2 "Spreads": the granules merge through the interstitium toward the papillary surface; 3 "Exposed": the plaque reaches just beneath the urothelium, which is breached; 4 "Stone grows": layered tan calcium oxalate crystals build outward from the exposed white plaque, forming an attached stone. Keep plaque white (calcium phosphate) and stone tan (calcium oxalate) consistently. Right contrast card titled "A different path": collecting ducts filled with crystal plugs, labeled "Plugs inside collecting ducts: after bowel bypass surgery, distal RTA". Small round inset at top right for lay readers: a barnacle starting on a rock and growing, caption "Like a barnacle on a rock". Bottom flow of three boxes: pink "More plaque: higher urine calcium · lower urine volume" → white "More plaque area" → blue "More stones over time"; beneath it a gray note: "Lowering urine calcium and raising volume target these drivers; shrinking existing plaque is unproven." No numbers. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution. Do not place the plaque origin inside the tubule lumen or in the cortex; keep calcium phosphate white and calcium oxalate tan; do not state that treatment dissolves plaque.
```

**QUALITY CHECK:** Four stages in order; origin at thin-limb basement membrane; contrast card shows intratubular plugs; "unproven" note present; no numbers; attribution present.

**ALT TEXT:** Papilla cross-section in four stages: calcium phosphate plaque starts in the basement membrane of a thin loop of Henle, spreads under the urothelium, becomes exposed, and anchors a growing calcium oxalate stone, contrasted with crystal plugs inside collecting ducts

---

### 6D. Social share card

#### 018 · calcium-disorders-and-kidney-stones-og.png

| Field | Value |
|---|---|
| Priority | P0 |
| Placement | Open Graph / social share card (head meta og:image) (`head`) |
| Skill | williamriveromd-infographic-skill (OG card) |
| Archetype | OG card |
| Audience | Mixed |
| Size | 1200 × 630 (1.91:1) |
| Reader takeaway | What the guide is about, readable as a phone-size link preview. |
| Why it works for every reader | Title plus three objects; nothing else to read. |

**PROMPT**

```text
Polished illustrated medical-textbook style with soft shading and gentle semi-3D depth (not flat clip-art, not cartoon), white #ffffff background with soft gray #f3f4f6 or light teal #eef6f7 cards, navy #0f1e2e text, clinical teal #1a6b72 headings, renal green #1f7a4d for safe or helpful, amber #b8860b for caution, clinical red #b91c1c for danger, all text set in Inter (bold for titles). Social share card exactly 1200×630 (1.91:1), white-to-pale-mint background. Left 55%: navy title "Calcium in the Blood, Calcium in the Urine, and Kidney Stones" with "and Kidney Stones" in warm orange #c55a11; teal subtitle "Hypocalcemia · Hypercalciuria · Nephrocalcinosis · Stones". Right 45%: a softly lit semi-photoreal 3D kidney cutaway with faint white medullary specks and a small stone in the pelvis, beside a blood tube and a translucent 24-hour urine container. Keep all text inside a 60 px safe margin. Add a small semi-transparent navy footer reading "renalcarematters.com" (about 10–11 px, 70% opacity) in the bottom-right corner, never covering content; it is the only mark allowed.
```

**NEGATIVE INSTRUCTIONS**

```text
Avoid flat clip-art, cartoon style, clutter, paragraphs of text, tiny unreadable labels, AI gibberish or misspelled words, invented numbers, unrealistic anatomy, HDR, neon, glossy gradients, excessive saturation and generic stock-photo looks. NEVER use navy, charcoal, black or any dark background. Use ONLY the sans-serif font Inter (approved list: Inter, Nunito Sans, IBM Plex Sans, Manrope); no serif, condensed-display, decorative or handwritten type. Do not rely on color alone: pair every red/amber/green cue with an icon or shape. Never omit the renalcarematters.com attribution.
```

**QUALITY CHECK:** 1200×630; title spelled exactly; legible at thumbnail size; nothing clipped; attribution present.

**ALT TEXT:** Calcium in the Blood, Calcium in the Urine, and Kidney Stones — renalcarematters.com

---

## 7. Options and notes

- **Tagalog-label variants.** For images 001, 007 and 008, a second version with Tagalog labels can be generated for print handouts at the dialysis units; the web version keeps English labels with four-language captions.
- **Print.** Images 001, 007 and 012 are designed to stay legible when printed in grayscale on A4.
- **Consistency.** Generate all patient figures in one ChatGPT conversation so the illustration style stays uniform; do the same for the clinician algorithms.
- **Clinical review.** Image 016 shows trial counts and image 011 shows guideline thresholds. Check each rendered number against the guide before publishing.

## 8. Stage 2 validation

All 20 prompts were checked against the williamriveromd-local-image-generator schema: every required field is present, every text-bearing prompt names the Inter typeface, and every figure carries the renalcarematters.com attribution (the text-free hero is exempt). Per-image files are in `image-prompts/`, with `image-manifest.csv` and `image-manifest.json` alongside.
