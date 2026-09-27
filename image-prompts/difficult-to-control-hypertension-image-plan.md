# Image Plan Blueprint — *When Blood Pressure Stays High*

**Guide:** [`guides/difficult-to-control-hypertension.html`](../guides/difficult-to-control-hypertension.html) · dual-mode (Patients & Families EN/TL/CEB/KAP · Clinicians EN) · 24 sections
**Prepared:** 2026-09-27 · **Total assets:** 10 (8 in-body figures + 1 hero + 1 OG card) · **Status:** all slots wired in the HTML; images not yet generated
**Where to generate:** ChatGPT **Image Generator** GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Skills used:** `williamriveromd-image-planner` (architecture, style taxonomy, 10-point spec) · `williamriveromd-hero-vignette` ·
`williamriveromd-infographic-skill` · `williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure` ·
`williamriveromd-algorithm-generator-skill` · `medical-teaching-standard` (clinical accuracy of every label)
**Visual anchor:** `images/ckd-understanding-overview.webp` — teal header bars, navy text, one idea per panel, calm Filipino realism.

---

## Part A — Architecture

### A1. Why 10 images (image-planner rubric)
The planner's rubric caps a guide at 6 images unless it is a multi-chapter reference. This guide is one: 11 patient
sections plus 13 clinician sections, with two distinct clinician decision pathways (the consultation sequence and the
medication ladder). The planner also adds one flowchart per major decision tree. Each image covers one thematic
**cluster**, not one section:

| Cluster | Sections covered | Image |
|---|---|---|
| First impression | hero | Vignette hero |
| Why BP stays high | `#why`, `#raisers`, `#medicines` | 01 six reasons |
| Measure correctly | `#numbers`, `#measure`, `#visit` | 02 home technique |
| Safety | `#urgent` | **08 urgent-help card (new)** |
| Food | `#food`, `#kidney` | 07 sodium swaps |
| Confirm the phenotype | `#md-problem`, `#md-confirm`, `#md-regimen` | 03 funnel |
| Mechanism | `#md-secondary`, `#md-addon`, `#md-lifestyle` | 04 aldosterone mechanism |
| Decision pathway 1 | `#md-urgent` → `#md-specialist` | 05 consultation algorithm |
| Decision pathway 2 | `#md-ladder`, `#md-ckd`, `#md-philippines` | 06 PH medication ladder |
| Social share | meta tags | OG card |

Sections deliberately left **without** raster images, because an HTML table is sharper, searchable, and translatable:
the framework comparison (`#md-problem`), the phenotype table, the contributor table, the MRA pre-check table, and the
emerging-therapies table. `#faq` and `#md-pearls` are text-first by design.

### A2. Placement and style map

| # | File (`images/…`) | Placement anchor | Mode | Planner style | Authoring skill | Size | Batch |
|---|---|---|---|---|---|---|---|
| 1 | `difficult-to-control-hypertension-vignette-hero` | Hero, right of the title, inside `figure.hero-figure.mode-patient` (hidden in Clinician mode) | Patients (hero) | EDITORIAL_PHOTO | williamriveromd-hero-vignette (Scaffold A, Archetype J) | 2048 × 2048 (1:1) | 1 |
| 2 | `difficult-to-control-hypertension-01-why-bp-stays-high` | `#why` section, after the garden-hose paragraph | Patients | CLINICAL_FLAT_VECTOR | williamriveromd-infographic-skill (Archetype 4) | 1536 × 1152 (4:3) | 1 |
| 3 | `difficult-to-control-hypertension-02-home-bp-technique` | `#measure` section, after the 5-step list | Patients | CLINICAL_FLAT_VECTOR | williamriveromd-infographic-skill (Archetype 4, numbered steps) | 1536 × 1152 (4:3) | 1 |
| 4 | `difficult-to-control-hypertension-08-urgent-help-card` | `#urgent` section, directly after the red emergency alert | Patients | CLINICAL_FLAT_VECTOR (reference card) | williamriveromd-infographic-skill (Archetype 5, reference card) | 1536 × 1152 (4:3) | 1 |
| 5 | `difficult-to-control-hypertension-07-filipino-sodium-swaps` | `#food` section, after the WHO sodium paragraph | Patients | CLINICAL_FLAT_VECTOR (food matrix) | williamriveromd-infographic-skill (Archetype 6) | 1536 × 1152 (4:3) | 1 |
| 6 | `difficult-to-control-hypertension-03-apparent-vs-true-resistance` | `#md-confirm`, after the phenotype table | Clinicians | ALGORITHM_FLOWCHART (funnel) | williamriveromd-simple-figure (Scaffold D) | 1792 × 1024 (16:9) | 2 |
| 7 | `difficult-to-control-hypertension-04-volume-aldosterone-mechanism` | `#md-secondary`, after the Filipino PA pilot paragraph | Clinicians | MINIMAL_MEDICAL_3D (review-article mechanism) | williamriveromd-biomedical-mechanism-figure | 1792 × 1024 (16:9) | 2 |
| 8 | `difficult-to-control-hypertension-05-consultation-algorithm` | `#md-optimize`, after the dosing-time paragraph | Clinicians | ALGORITHM_FLOWCHART | williamriveromd-algorithm-generator-skill (Style Mode A, AHA) | 1152 × 1536 (3:4 portrait) | 2 |
| 9 | `difficult-to-control-hypertension-06-ph-medication-ladder` | `#md-ladder`, after the hierarchy table | Clinicians | ALGORITHM_FLOWCHART (treatment ladder) | williamriveromd-simple-figure (Scaffold C) | 1792 × 1024 (16:9) | 2 |
| 10 | `difficult-to-control-hypertension-og` | `og:image` + `twitter:image` meta (not placed in the body) | Mixed | EDITORIAL_PHOTO + title | williamriveromd-infographic-skill (Archetype 1, OG) | 1200 × 630 (fixed) | 2 |

> **Dimensions note.** The planner's generic size policy (1536×1024, 1280×960, 1400×1000) is overridden by the
> house skills' canonical sizes, which the guide's `<img width/height>` attributes already declare. If the GPT
> returns a different size, see C2 before uploading.

### A3. House rules baked into every prompt
- **Light backgrounds only** (white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, pale teal `#eef6f7`). Navy is for text and accents only.
- **Fonts on the image:** Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never serif or decorative.
- **Palette:** navy `#0f1e2e` text · teal `#1a6b72` headings · green `#1f7a4d` safe/do · amber `#b8860b` caution · red `#b91c1c` urgent · purple `#6c3d8e` specialist.
- **Attribution:** `renalcarematters.com` (`© renalcarematters.com` on algorithms/mechanisms), bottom-right; bottom-center on the portrait algorithm. The wordless hero is the only exception.
- **American English** on every label.

### A4. Clinical guardrails (checked against the published guide text)
- **No blame.** "Medicines not taken as prescribed," "refills hard to get," never "noncompliant."
- **Apparent before true.** Out-of-office BP gates every "resistant" label.
- **Generic names only.** No brands, doses, or mg strengths.
- **ACE inhibitor OR ARB, never both.**
- **Spironolactone limits are guideline-attributed:** AHA/ACC 2025 eGFR ≥45; ESC 2024 eGFR ≥30 and K⁺ ≤4.5 mmol/L.
- **Investigational stays investigational:** baxdrostat, lorundrostat; aprocitentan and renal denervation = specialist / limited availability.
- **Sodium figure:** the only number is the WHO adult goal (<2,000 mg sodium ≈ 5 g salt ≈ 1 teaspoon); the potassium salt-substitute caution is always present.
- **Urgent card:** symptom-first; 911 is the Philippine national emergency hotline; no rescue dosing. The 180/110 example matches the guide's conservative same-day-call threshold (the 2024 Philippine acute-severe-BP guideline's 110-vs-120 DBP inconsistency is flagged in the clinician text, not resolved on the card).
- **No fear imagery** in patient art.

---

## Part B — Production prompts (paste each PROMPT block into the Image Generator GPT)

### 1 · Circular vignette hero

**Placement:** Hero, right of the title, inside `figure.hero-figure.mode-patient` (hidden in Clinician mode) · **Mode:** Patients (hero) · **Batch:** 1
**Style:** EDITORIAL_PHOTO · **Skill:** williamriveromd-hero-vignette (Scaffold A, Archetype J)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Hero |
| PRIMARY VISUAL STYLE | EDITORIAL_PHOTO |
| SUBJECT | Filipino woman in her late 50s measuring BP correctly at home with her son logging the reading |
| COMPOSITION | Side profile at seated eye level, 60–70% hero subject, 20–25% empty title-safe zone upper-left, circle 85–90% of canvas with white margin |
| BACKGROUND | Bright Philippine home kitchen, soft daylight |
| LIGHTING | Soft natural window light, documentary realism |
| COLOR PALETTE | Teal #1a6b72 / navy #0f1e2e harmony on a light scene |
| MEDICAL DETAILS | Textbook posture: back supported, feet flat, legs uncrossed, arm at heart level, cuff on bare upper arm; no readable digits |
| MOOD | Calm, capable, hopeful |
| DIMENSIONS | 2048 × 2048 |

**Live `alt` (in guide):** A Filipino woman in her late 50s seated at a sunlit kitchen table measuring her blood pressure with an upper-arm cuff while her adult son writes the reading in a notebook beside a weekly pill organizer.

```
FILE NAME: difficult-to-control-hypertension-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A clinical people scene
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling (one cohesive home scene, no floating panels)
CAMERA: side profile at seated eye level, slightly over the table, shallow depth of field
HUMAN VARIATION (vs. previous guide): late-50s Filipino woman (not a clinician, not eating) with shoulder-length
  wavy hair tied loosely at the nape and a few silver strands, medium-tan skin, oval face, softly defined
  cheekbones, straight dark eyebrows, slim reading glasses pushed up on her head, small gold stud earrings,
  sleeveless-cardigan-over-sleeveless-top in muted coral and cream (upper arm bare for the cuff), average build;
  her son in his early 30s — lean, clean-shaven, short textured undercut, light olive gray t-shirt, wristwatch —
  sits beside her writing in a notebook. Home kitchen (not a clinic), side-profile framing (not a three-quarter
  seated portrait), calm focused expression rather than a posed smile; no teal polo, no beige blouse, no plated
  meal — at least 12 traits differ from the previous guide's cast.
AUDIENCE: mixed (patients, families, clinicians)
VISUAL GOAL: "Checking BP at home, done right and done together" — a hopeful, capable, unhurried home scene.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR
vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle
must never touch the canvas edges). Composition archetype: Environmental Storytelling — one cohesive scene, no
floating panels. Camera: side profile at seated eye level, looking slightly across the tabletop, gentle shallow
depth of field.

Subject: a Filipino woman in her late 50s, shoulder-length wavy dark hair with a few silver strands tied loosely
at the nape, medium-tan skin, reading glasses resting on her head, muted coral cardigan open over a cream
sleeveless top, seated CORRECTLY for a home blood-pressure reading in a bright, clean Philippine home kitchen:
back resting against a chair with a supportive backrest, both feet flat on the floor, legs uncrossed, her left
forearm relaxed and supported on a pale laminate table so the upper arm is at heart level, a snug upper-arm BP
cuff wrapped on her BARE upper arm about two finger-widths above the elbow crease, a compact automatic
upper-arm monitor on the table (its display softly out of focus, no readable digits). Her expression is calm
and quietly focused; she is not talking. Beside her, her son in his early 30s (lean, short textured undercut,
olive-gray t-shirt) sits close and writes in an open paper notebook — the BP log — with a pen. On the table in
the foreground: a seven-day plastic pill organizer with small colored compartments and a glass of water.
Soft natural morning daylight from a side window with light sheer curtains, a few potted herbs on the sill.

Visual hierarchy: the woman, cuff, and monitor occupy 60–70% of the circle; 2–3 supporting elements (the son
with the notebook, the pill organizer, the window light) fill 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft
out-of-focus pale kitchen wall and diffuse daylight in the upper-left of the circle (no faces, hands, objects,
or text inside that zone). Warm, hopeful, documentary-realistic color grade harmonizing with clinical teal
#1a6b72 and navy #0f1e2e on a light background; gentle edge falloff toward a slightly deeper neutral at the
rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, readable monitor digits, readable
notebook handwriting, readable pill-box letters, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels,
infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy,
edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in
text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black
backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy.
Also avoid: cuff over a sleeve or on the forearm or wrist, arm dangling below heart level, crossed legs,
feet off the floor, person talking or on a phone, coffee cup or cigarette in view, worried or distressed
expression, hospital setting, white coat, plated meal, wooden dining table identical to other guides.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant hero
subject (the woman measuring correctly) at 60–70% of the circle, 2–3 supporting elements, 20–25% empty
upper-left title-safe zone. Posture is textbook-correct (back supported, feet flat, legs uncrossed, arm
supported at heart level, cuff on bare upper arm). Filipino home context, ≥12 traits visibly different from the
last guide. Camera framing (side profile) not repeated from the previous guide. Wordless; crops cleanly inside
the circle.
```

---

### 2 · Why BP can stay high: six reasons

**Placement:** `#why` section, after the garden-hose paragraph · **Mode:** Patients · **Batch:** 1
**Style:** CLINICAL_FLAT_VECTOR · **Skill:** williamriveromd-infographic-skill (Archetype 4)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Inline |
| PRIMARY VISUAL STYLE | CLINICAL_FLAT_VECTOR |
| SUBJECT | Six blame-free, fixable reasons BP stays above goal |
| COMPOSITION | 3 × 2 equal tile grid, teal accent bars, header band, green footer |
| BACKGROUND | White |
| LIGHTING | Flat, no directional light |
| COLOR PALETTE | Teal / navy, green footer, one amber accent (tile 5), no red |
| MEDICAL DETAILS | Patis, toyo, bagoong spelled correctly; NSAIDs named generically; no brand logos |
| MOOD | Reassuring, non-judgmental |
| DIMENSIONS | 1536 × 1152 |

**Live `alt` (in guide):** Six-tile infographic showing common reasons blood pressure stays high: measurement problems, white-coat effect, medicines not taken as prescribed, hidden salt, interfering substances, and another hidden condition.

**Live `fig-desc`:** Six common reasons blood pressure can stay above goal: the reading itself may be off (wrong cuff or technique), the clinic may raise it (white-coat effect), medicines may be missed or hard to refill, salt may be hidden in food, some pain relievers such as NSAID (nonsteroidal anti-inflammatory drug) medicines or supplements may push it up, and another condition such as excess aldosterone, sleep apnea, or kidney disease may be driving it.

**Live `fig-abbrevs`:** BP — Blood pressure · NSAID — Nonsteroidal anti-inflammatory drug

```
FILE NAME: difficult-to-control-hypertension-01-why-bp-stays-high.png
IMAGE TYPE: Multi-panel patient education infographic (Archetype 4) — 6-tile grid
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: Six friendly, blame-free tiles that name the common, fixable reasons BP stays high.

PROMPT:
Patient education infographic, 4:3 landscape, 1536×1152, clean WHITE (#ffffff) background, modern nephrology
clinic aesthetic, calm and reassuring. All text set in Inter (titles bold) and Nunito Sans (body), navy #0f1e2e.

Header band (soft pale teal #eef6f7, rounded): title in bold Inter navy "Why BP can stay high", subtitle in teal
#1a6b72 "Six common reasons — most can be fixed".

Body: a balanced 3 × 2 grid of SIX equal rounded cards on very soft gray #f3f4f6, each with a thin teal top
accent bar, one simple flat or softly semi-3D icon, a bold short heading, and 1–2 short plain-language lines:

1) Icon: upper-arm BP cuff and a small ruler. Heading "How it's measured". Lines: "Cuff too small or too loose ·
   arm hanging down · talking during the reading."
2) Icon: a clinic door with a small heartbeat line. Heading "White-coat effect". Lines: "BP rises at the clinic
   from nerves. Home readings show the real picture."
3) Icon: a weekly pill organizer and a pharmacy bag. Heading "Medicines not taken as prescribed". Lines:
   "Doses missed, cost, side effects, or refills hard to get — tell your doctor, there are options."
4) Icon: small realistic Filipino condiments — a bottle of patis, a bottle of toyo, a small jar of bagoong, and an
   instant-noodle pack (generic, NO brand logos or readable labels). Heading "Hidden salt in food". Lines:
   "Patis, toyo, bagoong, instant noodles, and processed foods add up fast."
5) Icon: a blister pack, a nasal decongestant box, and a small herbal-product bottle (all generic, unlabeled).
   Heading "Products that raise BP". Lines: "Pain relievers (NSAIDs), decongestants, some herbal products."
6) Icon: a simple kidney, an adrenal gland on top of the kidney, and a sleeping person with a soft snore wave.
   Heading "Another hidden condition". Lines: "Aldosterone excess, sleep apnea, kidney disease — tests can find
   them."

Footer strip (renal green #1f7a4d text on pale green-white): "Bring your home BP log and ALL your medicines and
supplements to your next visit." Use calm color logic — teal and green accents, one amber accent only on tile 5;
no red. Generous whitespace, rounded corners, mobile-readable labels (never smaller than ~11pt equivalent).
Small semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No brand
names or logos on any product. No blaming words ("noncompliant," "failed," "lazy"), no red danger gauges, no
distressed faces. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
4:3, 1536×1152, white background. Exactly six equal tiles with the headings above, spelled correctly
(patis, toyo, bagoong). Blame-free wording. Mobile-readable. renalcarematters.com visible bottom-right.
```

---

### 3 · Home BP technique

**Placement:** `#measure` section, after the 5-step list · **Mode:** Patients · **Batch:** 1
**Style:** CLINICAL_FLAT_VECTOR · **Skill:** williamriveromd-infographic-skill (Archetype 4, numbered steps)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Inline |
| PRIMARY VISUAL STYLE | CLINICAL_FLAT_VECTOR |
| SUBJECT | Correct home BP measurement |
| COMPOSITION | Central correctly seated figure with leader callouts, 7 numbered step cards clockwise |
| BACKGROUND | White |
| LIGHTING | Flat |
| COLOR PALETTE | Teal badges, navy text, amber strike-throughs |
| MEDICAL DETAILS | Upper-arm validated device; 5 min rest; 2 readings 1 min apart morning and evening; ~7 days |
| MOOD | Instructional, calm |
| DIMENSIONS | 1536 × 1152 |

**Live `alt` (in guide):** Illustrated step-by-step guide to correct home blood pressure measurement with an upper-arm cuff.

**Live `fig-desc`:** Correct home blood pressure technique: a validated upper-arm monitor and properly sized cuff, five quiet minutes seated with back supported and feet flat, the cuff at heart level, two readings a minute apart morning and evening, and every reading written down.

**Live `fig-abbrevs`:** BP — Blood pressure

```
FILE NAME: difficult-to-control-hypertension-02-home-bp-technique.png
IMAGE TYPE: Multi-panel patient education infographic (Archetype 4) — numbered step sequence with central posture figure
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: A single glance teaches correct home BP technique — posture in the center, seven numbered steps around it.

PROMPT:
Patient education infographic, 4:3 landscape, 1536×1152, clean WHITE (#ffffff) background, calm modern clinic
aesthetic. All text in Inter (bold headings) and Nunito Sans (short body lines), navy #0f1e2e.

Title at top in bold Inter navy: "Home BP: how to measure it right". Subtitle in teal #1a6b72: "Good readings =
better decisions".

CENTER: a clean, semi-photorealistic illustration of a Filipino adult (middle-aged man, short gray-flecked hair,
light polo shirt, sleeve rolled up) seated correctly at a small table — back against the chair, both feet flat on
the floor, legs uncrossed, left forearm resting on the table so the cuff sits at heart level, snug upper-arm cuff
on the bare arm, mouth closed (not talking). Thin teal leader callouts point to: "Back supported", "Feet flat,
legs uncrossed", "Cuff at heart level", "Bare upper arm". The monitor display shows no readable numbers.

Around the central figure, SEVEN numbered rounded step cards (teal number badges 1–7, soft gray #f3f4f6 cards,
one small flat icon each), reading clockwise from top-left:
1) "Use a validated upper-arm device" (icon: upper-arm monitor with a small checkmark seal; note: "Wrist and
   finger devices are less reliable").
2) "Right cuff size, at heart level" (icon: three cuffs small / regular / large).
3) "Sit quietly for 5 minutes first" (icon: chair and a 5-minute timer). Line: "Back supported, feet flat, legs
   uncrossed, no talking."
4) "30 minutes before: no coffee, exercise, or smoking" (icon: coffee cup, running shoe, cigarette, each with a
   soft strike-through in amber #b8860b).
5) "2 readings, 1 minute apart — morning and evening" (icon: sun and moon). Line: "Morning: before your medicines
   and before breakfast."
6) "Write every reading down" (icon: paper log and pen). Line: "Even the high ones and the low ones."
7) "About 7 days before your visit" (icon: small 7-day calendar strip). Line: "Bring the log to your doctor."

Footer strip in renal green #1f7a4d on a pale green-white band: "Keep every reading — your doctor needs the
whole week, not just the best one." Generous whitespace, balanced layout, mobile-readable labels.
Small semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Do NOT show a
wrist cuff as the recommended device, a cuff over clothing, an arm hanging down, crossed legs, or a person
talking. No readable numbers on the monitor, no brand names. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
4:3, 1536×1152, white background. Posture in the central figure is correct in every detail. Exactly seven
numbered steps with the wording above ("5 minutes," "30 minutes," "2 readings, 1 minute apart," "7 days").
Mobile-readable. renalcarematters.com visible bottom-right.
```

---

### 4 · Urgent-help action card (NEW)

**Placement:** `#urgent` section, directly after the red emergency alert · **Mode:** Patients · **Batch:** 1
**Style:** CLINICAL_FLAT_VECTOR (reference card) · **Skill:** williamriveromd-infographic-skill (Archetype 5, reference card)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Reference Card |
| PRIMARY VISUAL STYLE | CLINICAL_FLAT_VECTOR |
| SUBJECT | Symptom-first triage: go now vs. call today |
| COMPOSITION | Two lanes side by side with lane labels, icon rows, bottom pregnancy strip |
| BACKGROUND | White |
| LIGHTING | Flat |
| COLOR PALETTE | Red lane + amber lane, each with text labels and icons (never color alone) |
| MEDICAL DETAILS | 911 as the PH emergency number; no BP-lowering instructions; no rescue dosing |
| MOOD | Clear, steady, not frightening |
| DIMENSIONS | 1536 × 1152 |

**Live `alt` (in guide):** Two-lane action card. Left lane, labeled Go now: chest pain, severe breathlessness, sudden weakness or face drooping, trouble speaking, confusion, sudden severe headache, or vision loss means calling 911 or going to the emergency room. Right lane, labeled Call today: a very high reading with no symptoms means resting 5 minutes, measuring again, and calling the doctor the same day if it stays high. A bottom strip warns pregnant or recently delivered women to seek same-day care.

**Live `fig-desc`:** Symptoms decide how fast to act, not the number alone. Warning symptoms with high blood pressure mean emergency care now; a very high reading without symptoms means a careful recheck and a same-day call to your doctor. Never take extra tablets on your own, and during pregnancy or after delivery, seek same-day care.

```
FILE NAME: difficult-to-control-hypertension-08-urgent-help-card.png
IMAGE TYPE: Clinician-style reference card adapted for patients (Archetype 5) — two-lane symptom-first action card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: In one glance, a patient knows whether high BP means "go to the emergency room now" or "recheck and call the doctor today."

PROMPT:
Patient safety reference card, 4:3 landscape, 1536×1152, clean WHITE (#ffffff) background, calm modern clinic
aesthetic, large mobile-readable type. All text in Inter (bold headings) and Nunito Sans (body), navy #0f1e2e.

Title at top in bold Inter navy: "High BP: when to get help". Subtitle in teal #1a6b72: "Your symptoms decide how
fast to act — not the number alone".

Two equal rounded vertical LANES side by side, each with a bold text label in a colored header band AND an icon, so
the meaning never depends on color alone:

LEFT LANE — header band clinical red #b91c1c with white bold text "GO NOW" and a small ambulance icon. Subheader in
navy: "High BP with ANY of these → call 911 or go to the emergency room". Six icon rows, each a simple flat
line icon in red plus a short navy label:
- chest outline with a pressure mark: "Chest pain or pressure"
- lungs: "Severe shortness of breath"
- face with one-sided droop and an arm: "Sudden weakness, numbness, or face drooping"
- speech bubble with a break: "Trouble speaking"
- head with a small swirl: "Confusion or a seizure"
- eye with a lightning mark: "Sudden severe headache or vision loss"
Bottom line inside the lane, bold navy: "Do not take extra tablets. Do not wait to finish your BP log."

RIGHT LANE — header band amber #b8860b with navy bold text "CALL TODAY" and a small phone icon. Subheader in navy:
"Very high reading (e.g., 180/110 or above) but you feel well". Three numbered steps with teal number badges:
1) chair and 5-minute timer icon: "Sit quietly for 5 minutes"
2) upper-arm cuff icon: "Measure again the correct way"
3) phone icon: "Still very high? Call your doctor or clinic the SAME DAY"
Bottom line inside the lane, navy: "BP is lowered gradually over hours to days — not all at once."

BOTTOM STRIP, full width, soft pale purple (#f3eef8) rounded band with a small pregnant-figure icon and bold navy
text: "Pregnant or gave birth in the last 6 weeks? BP of 140/90 or higher, severe headache, vision changes, or
upper-belly pain → same-day assessment by your obstetric team."

Generous whitespace, strong left–right symmetry, icons simple and consistent line weight, labels never smaller
than ~12pt equivalent. Small semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No photos of
people in distress, no clutching-chest poses, no sirens or flashing lights, no BP dial gauges, no drug names or
doses, no "take this pill now" instructions, no US-specific numbers other than 911 (which is also the Philippine
national emergency hotline). Never omit the renalcarematters.com attribution.

QUALITY CHECK:
4:3, 1536×1152, white background. Two lanes with TEXT labels "GO NOW" and "CALL TODAY" plus icons (not color
alone). Six red-lane symptoms, three amber-lane steps, pregnancy strip present. "911", "180/110", "140/90",
"5 minutes", and "SAME DAY" spelled exactly. Mobile-readable. renalcarematters.com visible bottom-right.
```

---

### 5 · Filipino sodium swaps

**Placement:** `#food` section, after the WHO sodium paragraph · **Mode:** Patients · **Batch:** 1
**Style:** CLINICAL_FLAT_VECTOR (food matrix) · **Skill:** williamriveromd-infographic-skill (Archetype 6)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Inline |
| PRIMARY VISUAL STYLE | CLINICAL_FLAT_VECTOR |
| SUBJECT | Hidden sodium sources in Filipino food and realistic swaps |
| COMPOSITION | Instead-of → Try two-column matrix, goal bar, amber kidney caution panel |
| BACKGROUND | White |
| LIGHTING | Flat with realistic food renders |
| COLOR PALETTE | Amber "Instead of", green "Try", teal goal bar |
| MEDICAL DETAILS | Only number is the WHO goal (<2,000 mg sodium ≈ 5 g salt); potassium-substitute caution |
| MOOD | Appetizing, practical |
| DIMENSIONS | 1536 × 1152 |

**Live `alt` (in guide):** Infographic of common high-sodium Filipino foods and lower-salt swaps, with the daily sodium goal.

**Live `fig-desc`:** Common high-sodium foods in Filipino kitchens (patis, toyo, bagoong, seasoning cubes, instant noodles, dried fish, processed meats) paired with lower-salt swaps such as calamansi, garlic, onion, ginger, fresh fish and vegetables, and using half the noodle seasoning packet. The adult goal is under 2,000 mg sodium a day from all sources.

**Live `fig-abbrevs`:** WHO — World Health Organization

```
FILE NAME: difficult-to-control-hypertension-07-filipino-sodium-swaps.png
IMAGE TYPE: Food matrix / nutrition infographic (Archetype 6) — "instead of → try" swap grid
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: Make hidden Filipino sodium sources recognizable and each one paired with a realistic, tasty swap.

PROMPT:
CKD and hypertension nutrition infographic, clean educational food matrix, 4:3 landscape, 1536×1152, WHITE
(#ffffff) background. All text in Inter (bold headings) and Nunito Sans (body), navy #0f1e2e.

Title at top in bold Inter navy: "Cut the hidden salt — Filipino swaps". Subtitle in teal #1a6b72: "Flavor stays.
Sodium goes down."

GOAL BAR directly under the title, a soft pale-teal rounded band with a simple teaspoon icon: "Adult goal (WHO):
less than 2,000 mg sodium a day ≈ 5 g salt ≈ 1 teaspoon — from ALL food and condiments combined."

MAIN GRID: two columns joined by small green right-arrows. Left column header in amber #b8860b "Instead of…",
right column header in renal green #1f7a4d "Try…". Seven rows, each with realistic, appetizing small food
renders (generic, NO brand logos or readable labels):
1) Patis (fish sauce bottle) → calamansi squeeze, garlic, and a little patis only at the table, not in the pot.
2) Toyo (soy sauce bottle) → calamansi, garlic, onion, and a splash of vinegar.
3) Bagoong (small jar) → a small side portion shared, with fresh green mango or vegetables.
4) Seasoning cubes / powdered seasoning → garlic, onion, ginger, tanglad (lemongrass), and black pepper.
5) Instant noodles (generic cup and pack) → cook with HALF the seasoning packet and add fresh vegetables and egg.
6) Tuyo and daing (dried salted fish) → fresh fish — grilled, steamed, or sinigang with plenty of vegetables.
7) Processed meats — hotdog, longganisa, corned beef (can) → fresh chicken or pork; if using canned goods,
   rinse and drain them first.
Show NO sodium numbers on any individual food item.

CAUTION PANEL at bottom-right, pale amber rounded box with a small kidney icon and amber accent: "Kidney disease?
Ask your doctor before using 'lite' or potassium-based salt substitutes — they can raise potassium."

FOOTER strip, soft gray, navy text: "Taste food before salting · read labels · keep condiments off the table."
Rounded category cards, generous whitespace, mobile-readable labels. Small semi-transparent navy
"renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid overprocessed
HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black
backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or
Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No brand names or readable
packaging, no per-food sodium milligram values, no shaming words ("bad food," "forbidden"). Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
4:3, 1536×1152, white background. Seven instead-of → try rows with Filipino items spelled correctly (patis, toyo,
bagoong, tuyo, daing, longganisa, calamansi, tanglad). The only number is the WHO goal. Potassium-substitute
caution present. Mobile-readable. renalcarematters.com visible bottom-right.
```

---

### 6 · Apparent vs. true resistance funnel

**Placement:** `#md-confirm`, after the phenotype table · **Mode:** Clinicians · **Batch:** 2
**Style:** ALGORITHM_FLOWCHART (funnel) · **Skill:** williamriveromd-simple-figure (Scaffold D)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Inline |
| PRIMARY VISUAL STYLE | ALGORITHM_FLOWCHART |
| SUBJECT | Filtering pseudoresistance before labeling true resistance |
| COMPOSITION | Vertical funnel, 5 filter bands with amber side exits, green outlet to secondary-cause box |
| BACKGROUND | White |
| LIGHTING | Flat |
| COLOR PALETTE | Pale teal funnel, amber exits, green outlet |
| MEDICAL DETAILS | No prevalence numbers, no drugs or doses |
| MOOD | Analytical, publication-grade |
| DIMENSIONS | 1792 × 1024 |

**Live `alt` (in guide):** Funnel diagram filtering apparent resistant hypertension down to true resistant hypertension.

**Live `fig-desc`:** From apparent to true resistant hypertension: uncontrolled office BP on three drugs passes through filters for measurement error, white-coat effect (checked with home or ambulatory monitoring), nonadherence and access, a suboptimal regimen without an appropriate diuretic, and interfering substances. What remains is true resistant hypertension, which prompts screening for secondary causes such as primary aldosteronism (PA) and obstructive sleep apnea (OSA).

**Live `fig-abbrevs`:** BP — Blood pressure · HBPM — Home blood pressure monitoring · ABPM — Ambulatory blood pressure monitoring · OSA — Obstructive sleep apnea · CKD — Chronic kidney disease · PA — Primary aldosteronism · NSAIDs — Nonsteroidal anti-inflammatory drugs

```
FILE NAME: difficult-to-control-hypertension-03-apparent-vs-true-resistance.png
IMAGE TYPE: Simple figure — Scaffold D single-concept poster (vertical funnel with side filter labels)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show that pseudoresistance is filtered out step by step before anyone is labeled "true resistant."

PROMPT:
Clinical education figure, AJKD/NEJM graphical-abstract style, landscape 16:9, 1792×1024, clean WHITE (#ffffff)
background. Title at top-left in bold Inter navy #0f1e2e: "Apparent vs. true resistant hypertension".
Subtitle in teal #1a6b72 IBM Plex Sans: "Filter out pseudoresistance first".

CENTER: a large, clean, flat-vector funnel drawn with thin navy outlines and a soft pale teal (#eef6f7) fill,
wide at the top and narrowing to a small outlet at the bottom. At the funnel mouth, a wide rounded navy-outlined
entry card: "Uncontrolled office BP on 3 drugs".

Five horizontal filter bands cross the funnel from top to bottom, each band slightly narrower than the one above,
each with a small flat icon on the left edge and a label card to the right of the funnel connected by a thin
dashed teal leader. On the LEFT side of each band, a small amber (#b8860b) arrow exits the funnel with a short
gray note "apparent — correct & recheck":
Filter 1 — icon: cuff and ruler — "Measurement error" · note: "cuff size, posture, technique".
Filter 2 — icon: small clock with a home — "White-coat effect" · note: "confirm with HBPM or ABPM".
Filter 3 — icon: pill organizer and a pharmacy bag — "Nonadherence / access" · note: "cost, supply, side effects,
  complexity".
Filter 4 — icon: three stacked pill shapes — "Suboptimal regimen" · note: "no diuretic, doses not optimized,
  short-acting agents".
Filter 5 — icon: blister pack and small herbal bottle — "Interfering substances" · note: "NSAIDs, decongestants,
  alcohol, some herbal products".

BOTTOM OUTLET: a rounded renal-green (#1f7a4d) outlined card: "True resistant hypertension", with a thin arrow
into a pale-blue (#eef6f7) rounded box titled "Screen for secondary causes" listing four short items with small
icons: "Primary aldosteronism (PA)" · "Obstructive sleep apnea (OSA)" · "CKD" · "Renovascular disease".

Generous whitespace, perfectly aligned bands, muted clinical palette; mobile-readable labels (≥11pt equivalent).
Small semi-transparent navy "© renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black
backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or
Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No percentages or prevalence
numbers anywhere on the figure, no drug names or doses. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9, 1792×1024, white background. Entry card, five filters in the stated order, amber "apparent" exits, green
true-resistance outlet, four secondary causes. Mobile-readable, publication-grade. © renalcarematters.com visible
bottom-right.
```

---

### 7 · Volume and aldosterone mechanism

**Placement:** `#md-secondary`, after the Filipino PA pilot paragraph · **Mode:** Clinicians · **Batch:** 2
**Style:** MINIMAL_MEDICAL_3D (review-article mechanism) · **Skill:** williamriveromd-biomedical-mechanism-figure

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Inline |
| PRIMARY VISUAL STYLE | MINIMAL_MEDICAL_3D |
| SUBJECT | Aldosterone and sodium excess driving resistant hypertension, with drug sites of action |
| COMPOSITION | Organ panel → dashed principal-cell inset → pink / white / blue bottom flow |
| BACKGROUND | White |
| LIGHTING | Soft semi-3D, flat vector |
| COLOR PALETTE | Muted clinical: gray-blue anatomy, yellow principal cell, red drivers, blue benefit |
| MEDICAL DETAILS | ENaC + ROMK apical, Na⁺/K⁺-ATPase basolateral, MR intracellular; CYP11B2 inhibitors = investigational |
| MOOD | Scientific, calm |
| DIMENSIONS | 1792 × 1024 |

**Live `alt` (in guide):** Mechanism schematic of aldosterone and sodium retention in the collecting duct driving resistant hypertension, with sites of drug action.

**Live `fig-desc`:** Why volume and aldosterone drive resistant hypertension: aldosterone from the adrenal gland acts on the mineralocorticoid receptor in collecting-duct principal cells, increasing sodium reabsorption through ENaC and potassium secretion through the renal outer medullary potassium channel (ROMK). High salt intake, sleep apnea, and CKD add to the sodium and volume load. Spironolactone blocks the receptor, thiazide-like diuretics and salt restriction reduce the sodium load, and investigational aldosterone synthase inhibitors block aldosterone production upstream.

**Live `fig-abbrevs`:** MR — Mineralocorticoid receptor · ENaC — Epithelial sodium channel · ROMK — Renal outer medullary potassium channel · CYP11B2 — Aldosterone synthase · OSA — Obstructive sleep apnea · CKD — Chronic kidney disease

```
FILE NAME: difficult-to-control-hypertension-04-volume-aldosterone-mechanism.png
IMAGE TYPE: Biomedical mechanism figure — organ panel → dashed magnified principal-cell inset → bottom injury → intervention → benefit flow
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Make sodium/volume excess and aldosterone excess visible as the shared engine of resistant hypertension, and show where each therapy acts.

PROMPT:
Create a publication-grade biomedical mechanism schematic, 16:9 landscape, 1792×1024, WHITE background,
scientific review-article style: flat vector illustration with soft semi-3D shading, thin dashed boxes for
magnified panels, muted clinical palette (light gray-blue anatomy, soft yellow highlighted tubular segment, red
for injury drivers, blue for protective/therapeutic effects, pale pink pathology box, pale blue benefit box).
All labels in clean sans-serif IBM Plex Sans (bold only for key terms), navy text.

Topic: Volume and aldosterone in resistant hypertension.
Title top-left in bold IBM Plex Sans navy: "Sodium, volume, and aldosterone: why BP resists treatment".

LEFT PANEL — organ-level context: a simplified kidney in coronal section with renal artery (red) and vein (blue),
the adrenal gland sitting on its upper pole highlighted in soft amber, a small label "Adrenal gland (zona
glomerulosa)" and a curved red arrow "Aldosterone ↑" from adrenal to the kidney. Three small driver icons feed
into the panel with thin red arrows, each with a short label:
- a salt shaker: "High sodium intake"
- a sleeping head with an airway narrowing: "OSA — sympathetic surges, aldosterone ↑"
- a small scarred kidney outline: "CKD — less sodium excretion"
A small dashed connector box on the kidney's medulla points to the magnified inset.

CENTER-RIGHT PANEL — dashed magnified inset "Collecting duct — principal cell": one large epithelial cell drawn
between a tubular lumen (left, labeled "Tubular lumen — urine side") and the peritubular blood side (right,
labeled "Blood side"). Inside the cell: aldosterone (small hexagon icon) entering from the blood side and binding
the "Mineralocorticoid receptor (MR)" in the cytoplasm, arrow to the nucleus "↑ gene transcription". On the
apical (lumen) membrane: multiple "ENaC" channels with Na⁺ arrows moving INTO the cell ("Na⁺ reabsorption ↑")
and a "ROMK" channel with a K⁺ arrow moving OUT into the lumen ("K⁺ secretion ↑"). On the basolateral membrane:
a "Na⁺/K⁺-ATPase" pump moving Na⁺ to blood and K⁺ into the cell. Small callouts on the right edge:
"↑ Na⁺ and water retention", "↑ plasma volume", "↑ BP", "↓ serum K⁺ (may be normal)".
Highlight the principal cell in soft yellow.

UPSTREAM NOTE (small, above the adrenal in the left panel): a pale purple (#6c3d8e outline) tag attached to the
adrenal: "CYP11B2 (aldosterone synthase) — blocked by aldosterone synthase inhibitors (baxdrostat,
lorundrostat): INVESTIGATIONAL". Keep it clearly separate and labeled investigational.

BOTTOM SUMMARY FLOW (three boxes left → right joined by arrows):
Left, pale pink box "Drivers": "Sodium / volume excess" · "Aldosterone excess (primary aldosteronism or
secondary)" · "OSA, CKD" · bold final line "**Volume-dependent hypertension**".
Center, white box with three small therapy icons, each labeled with its site of action:
"Spironolactone — blocks MR (monitor K⁺ and kidney function)" · "Thiazide-like diuretic — distal Na⁺
excretion" · "Sodium restriction — less Na⁺ load".
Right, pale blue box "Benefit": "↓ Na⁺ and fluid retention" · "↓ plasma volume" · bold final line "**Lower BP**".

Thin dashed connector lines, generous whitespace, no overcrowding, all labels legible at slide size.
Small semi-transparent navy "© renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, shadows, cartoonish styling, excessive icons,
overcrowding, gibberish text. NEVER use a navy, charcoal, or black background. Use ONLY Inter, Nunito Sans,
IBM Plex Sans, or Manrope — never a serif font. Do not place ENaC or ROMK on the basolateral side, do not place
the Na⁺/K⁺-ATPase on the apical side, do not draw aldosterone synthase inhibitors as approved routine therapy,
do not print drug doses or any numeric lab thresholds, no brand names. Never omit the © renalcarematters.com
attribution.

QUALITY CHECK:
16:9, 1792×1024, white background. Organ panel → dashed principal-cell inset → pink/white/blue bottom flow.
ENaC and ROMK apical, Na⁺/K⁺-ATPase basolateral, MR intracellular. CYP11B2 inhibitors clearly labeled
investigational. Labels medically precise and legible. © renalcarematters.com visible bottom-right.
```

---

### 8 · Consultation algorithm

**Placement:** `#md-optimize`, after the dosing-time paragraph · **Mode:** Clinicians · **Batch:** 2
**Style:** ALGORITHM_FLOWCHART · **Skill:** williamriveromd-algorithm-generator-skill (Style Mode A, AHA)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Flowchart |
| PRIMARY VISUAL STYLE | ALGORITHM_FLOWCHART |
| SUBJECT | Stepwise consultation for persistently high BP |
| COMPOSITION | Top-to-bottom, two early exits, dashed divider between verify/correct and treat/escalate |
| BACKGROUND | White |
| LIGHTING | Flat |
| COLOR PALETTE | Peach assessment, pink diamonds, blue treatment, green verification, purple referral |
| MEDICAL DETAILS | Exits before verification; spironolactone limits attributed (AHA/ACC eGFR ≥45; ESC eGFR ≥30, K⁺ ≤4.5) |
| MOOD | Authoritative, uncluttered |
| DIMENSIONS | 1152 × 1536 |

**Live `alt` (in guide):** Clinical algorithm for evaluating and managing difficult-to-control hypertension, from urgent exits through measurement, regimen review, secondary causes, optimization, add-on therapy, and referral.

**Live `fig-desc`:** Consultation algorithm: exclude urgent organ injury and pregnancy, confirm with out-of-office BP, reconcile the actual regimen and access, address contributors, screen for secondary causes, optimize the RAS blocker plus long-acting CCB plus thiazide-like diuretic, add spironolactone if kidney function and potassium allow under the named framework, and refer when control or safety remains uncertain &mdash; including for renal denervation (RDN) at expert centers.

**Live `fig-abbrevs`:** HBPM — Home blood pressure monitoring · ABPM — Ambulatory blood pressure monitoring · PA — Primary aldosteronism · RAS — Renin&ndash;angiotensin system · CCB — Calcium-channel blocker · eGFR — Estimated glomerular filtration rate · K+ — Potassium · RDN — Renal denervation · NSAIDs — Nonsteroidal anti-inflammatory drugs · OSA — Obstructive sleep apnea · CKD — Chronic kidney disease · AHA/ACC — American Heart Association / American College of Cardiology · ESC — European Society of Cardiology

```
FILE NAME: difficult-to-control-hypertension-05-consultation-algorithm.png
IMAGE TYPE: Clinical algorithm — Style Mode A (AHA provider-algorithm aesthetic), portrait
ASPECT RATIO: 3:4 portrait
PIXEL DIMENSIONS: 1152 × 1536
AUDIENCE: clinicians
VISUAL GOAL: A single top-to-bottom consultation pathway that exits emergencies and pregnancy early and only escalates drugs after verification.

PROMPT:
Create a polished medical guideline algorithm flowchart in the style of an American Heart Association provider
algorithm, portrait 3:4, 1152×1536. Use a white background, clean sans-serif typography set in Inter (bold
black/navy titles, regular body), thin black arrows, pastel rounded boxes, and pink decision diamonds. Layout
portrait, centered, spacious, and easy to read.

Visual conventions:
- Peach/orange rounded boxes for initial assessment steps
- Pink diamond boxes for decision questions
- Blue rounded boxes for active treatment steps
- Green rounded boxes for verification, monitoring, and supportive steps
- Gray capsule boxes for transitional steps
- Red bold labels beside arrows for emergency branches
- A dashed horizontal divider separating "Verify & correct" (upper) from "Treat & escalate" (lower)

Title at top-left in bold Inter: "Persistently high BP: consultation algorithm".

Content to render (top to bottom):
1. Peach box: "Persistently high BP"
2. Pink diamond: "Urgent symptoms or acute organ injury?" → right branch, red bold label "YES" → red-outlined
   box "Emergency care now" (small note: "chest pain, breathlessness, neurologic deficit, vision change,
   confusion"). Down arrow "NO".
3. Pink diamond: "Pregnant or postpartum?" → left branch, red bold label "YES" → rounded box "Obstetric /
   maternal-medicine pathway". Down arrow "NO".
4. Green box: "Verify measurement + out-of-office BP (HBPM or ABPM)" · note: "correct cuff & technique; exclude
   white-coat effect".
5. Green box: "Reconcile the ACTUAL regimen & access" · note: "what is taken, cost, supply, side effects".
6. Green box: "Address contributors" · note: "sodium · alcohol · NSAIDs/decongestants · sleep".
7. Gray capsule: "Screen secondary causes" with four short bullets: "PA (aldosterone/renin)" · "OSA" ·
   "CKD / albuminuria" · "Renovascular".
   — dashed horizontal divider here —
8. Blue box: "Optimize: RAS blocker (ACE inhibitor OR ARB) + long-acting CCB + thiazide-like diuretic".
9. Pink diamond: "Still uncontrolled?" → side branch "NO" → green box "Continue & monitor". Down arrow "YES".
10. Blue box: "Add spironolactone if eGFR & K⁺ allow" · small gray note beneath in Nunito Sans:
    "AHA/ACC: eGFR ≥45 · ESC: eGFR ≥30 and K⁺ ≤4.5 · recheck K⁺ and creatinine".
11. Pink diamond: "Still uncontrolled?" → "YES" →
12. Purple-outlined box (#6c3d8e): "Refer: hypertension specialist / nephrology" · note: "renal denervation only at
    expert centers".

Design requirements: title at top; no decorative icons; no photos; no 3D; no dark background; no excessive
shadows; short readable text in every box; strict alignment and consistent spacing; maximum branch depth kept
tidy with side exits returning cleanly. Include a small professional footer reading "© renalcarematters.com"
positioned at the bottom-center in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, spaghetti arrows, overlapping branches.
NEVER use a dark, navy, charcoal, or black background. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope —
no serif fonts. No brand names, no doses, no ACE-inhibitor-plus-ARB combination. Never omit the
© renalcarematters.com footer.

QUALITY CHECK:
3:4, 1152×1536, white background. Emergency and pregnancy exits come BEFORE verification; verification,
regimen, contributors, and secondary causes come BEFORE drug escalation. Spironolactone thresholds attributed to
AHA/ACC and ESC exactly as written. © renalcarematters.com visible bottom-center.
```

---

### 9 · Philippine medication ladder

**Placement:** `#md-ladder`, after the hierarchy table · **Mode:** Clinicians · **Batch:** 2
**Style:** ALGORITHM_FLOWCHART (treatment ladder) · **Skill:** williamriveromd-simple-figure (Scaffold C)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Inline |
| PRIMARY VISUAL STYLE | ALGORITHM_FLOWCHART |
| SUBJECT | Stepwise resistant-hypertension medication ladder, Philippine availability |
| COMPOSITION | Ascending 8-step staircase with CKD overlay tag and 3A side step |
| BACKGROUND | White |
| LIGHTING | Flat |
| COLOR PALETTE | Green L0, teal L1–4, amber L3A/L5, purple L6 |
| MEDICAL DETAILS | Generic names only, no doses; ACE inhibitor OR ARB; investigational items labeled |
| MOOD | Practical, orderly |
| DIMENSIONS | 1792 × 1024 |

**Live `alt` (in guide):** Stepped ladder of resistant-hypertension medication levels using generic drugs obtainable in the Philippines.

**Live `fig-desc`:** Philippine medication hierarchy for resistant hypertension, by generic name: fix the reason first, then one ACE inhibitor or ARB with amlodipine, then a thiazide-like diuretic such as indapamide SR (loop diuretic in advanced CKD or volume overload), then spironolactone, with alternatives, beta-blockers, clonidine, and specialist options as conditional later steps.

**Live `fig-abbrevs`:** ACE — Angiotensin-converting enzyme · ARB — Angiotensin receptor blocker · SR — Sustained release · HCTZ — Hydrochlorothiazide · CKD — Chronic kidney disease · MRA — Mineralocorticoid-receptor antagonist · K+ — Potassium

```
FILE NAME: difficult-to-control-hypertension-06-ph-medication-ladder.png
IMAGE TYPE: Simple figure — Scaffold C step sequence rendered as an ascending staircase ladder
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: One glance shows the escalation order — fix the reason first, then add one class per step — adapted to Philippine availability.

PROMPT:
Clean clinical education infographic, landscape 16:9, 1792×1024, WHITE (#ffffff) background, publication-grade
nephrology design. Title at top-left in bold Inter navy #0f1e2e: "Resistant hypertension: a Philippine
medication ladder". Subtitle in teal #1a6b72: "Generic names · one step at a time · no doses shown".

Draw an ascending STAIRCASE of eight rounded step cards rising from bottom-left to top-right, each card resting on
the step below and connected by a thin navy up-arrow, each with a colored top accent band, a bold level badge,
and 1–3 short lines in Nunito Sans:

Level 0 (green #1f7a4d band) — "Fix the reason": "measurement · adherence · access · secondary causes".
Level 1 (teal #1a6b72 band) — "ACE inhibitor OR ARB + amlodipine". Small red (#b91c1c) note: "never ACE inhibitor
  + ARB together".
Level 2 (teal band) — "Add thiazide-like diuretic": "indapamide SR" · "HCTZ in combination (access
  alternative)" · "chlorthalidone only if locally available".
  Attached below Level 2 as a small side tag with a dashed outline in amber #b8860b: "CKD overlay: loop
  diuretic (furosemide) for volume overload or advanced CKD".
Level 3 (teal band) — "Add spironolactone": "check K⁺ and kidney function first and after".
Level 3A (amber band, drawn as a small side step off Level 3) — "If spironolactone not tolerated":
  "eplerenone or amiloride — verify local supply".
Level 4 (teal band) — "Add bisoprolol or carvedilol": "earlier if a compelling indication (heart failure,
  coronary disease, rate control)".
Level 5 (amber band) — "Clonidine": "use carefully — rebound BP if stopped abruptly".
Level 6 (soft purple #6c3d8e band, top step) — "Specialist": "doxazosin · hydralazine · minoxidil · renal
  denervation (expert centers)" · small italic gray line "Emerging: aprocitentan, aldosterone synthase
  inhibitors (investigational)".

Cards on very soft gray (#f3f4f6), generous whitespace, balanced diagonal composition, mobile-readable labels
(≥11pt equivalent). Bottom strip, full width, soft gray: navy text "Move up only after confirming true BP and
adherence at the current step." Small semi-transparent navy "renalcarematters.com" attribution in the
bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid overprocessed
HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no
decorative or handwritten typefaces. No brand names, no doses, no mg strengths, no pill photos with imprints.
Do not show ACE inhibitor and ARB combined. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9, 1792×1024, white background. Eight steps in order 0 → 1 → 2 (+CKD overlay) → 3 → 3A (side) → 4 → 5 → 6.
Generic names spelled correctly (indapamide, hydrochlorothiazide, chlorthalidone, furosemide, spironolactone,
eplerenone, amiloride, bisoprolol, carvedilol, clonidine, doxazosin, hydralazine, minoxidil, aprocitentan).
Investigational items labeled. renalcarematters.com visible bottom-right.
```

---

### 10 · OG / social share card

**Placement:** `og:image` + `twitter:image` meta (not placed in the body) · **Mode:** Mixed · **Batch:** 2
**Style:** EDITORIAL_PHOTO + title · **Skill:** williamriveromd-infographic-skill (Archetype 1, OG)

**10-point spec (image-planner)**

| | |
|---|---|
| IMAGE TYPE | Hero (social) |
| PRIMARY VISUAL STYLE | EDITORIAL_PHOTO |
| SUBJECT | Home BP scene with the guide title |
| COMPOSITION | Left ~52% photo fading to white, right ~48% title panel, 48 px safe margins |
| BACKGROUND | White / off-white |
| LIGHTING | Soft daylight |
| COLOR PALETTE | Navy title, teal subtitle and accent rule |
| MEDICAL DETAILS | Correct posture; no readable monitor digits |
| MOOD | Hopeful, credible |
| DIMENSIONS | 1200 × 630 |

**Meta already in guide:** `og:image` → `https://renalcarematters.com/images/difficult-to-control-hypertension-og.png`, `og:image:width` 1200, `og:image:height` 630.

```
FILE NAME: difficult-to-control-hypertension-og.png
IMAGE TYPE: Editorial hero + title OG / social share card (Archetype 1, with baked title text)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630  (FIXED — never any other size for an OG card)
AUDIENCE: mixed (patients, families, clinicians)
VISUAL GOAL: One glance says "high BP that won't come down has fixable reasons" — calm home measurement scene plus a clear, legible title.

PROMPT:
Photorealistic medical editorial OG / social share card, exactly 1200×630 px, for a nephrology and hypertension
education guide, on a clean WHITE / off-white (#fafafa) background. Split composition:

LEFT ~52%: a bright, naturally lit, photorealistic scene of a Filipino woman in her late 50s seated correctly at a
light kitchen table — back supported, feet flat, forearm resting on the table, snug upper-arm BP cuff on her bare
upper arm, a compact automatic monitor with no readable digits, a seven-day pill organizer and an open paper
notebook beside her — calm, hopeful, documentary-realistic, soft daylight. The scene fades softly into the white
background on its right edge (no hard border).

RIGHT ~48%: a clean off-white panel carrying the text, left-aligned, with a thin teal #1a6b72 vertical accent rule:
- Small teal label in Manrope uppercase tracking: "renalcarematters.com guide"
- Title in bold Inter, navy #0f1e2e, large and mobile-legible, on two lines: "When Blood Pressure Stays High"
- Subtitle in Nunito Sans, teal #1a6b72, medium weight: "Difficult-to-control & resistant hypertension · A guide
  for Filipino patients and clinicians"
- A tiny row of three simple flat line icons in teal and renal green #1f7a4d below the subtitle: upper-arm cuff,
  salt shaker with a downward arrow, pill organizer.

Strong hierarchy, generous negative space, rounded soft panel edges, publication-grade editorial look. Keep all
text within a safe margin of at least 48 px from every edge so social-platform cropping never clips it. Small
semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic
anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No red BP
gauge, no alarm imagery, no clutching-chest pose, no readable monitor numbers, no brand logos. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Title "When Blood Pressure Stays High" and the subtitle spelled exactly as given, legible at
thumbnail size. Light background, calm Filipino home-measurement scene with correct posture. renalcarematters.com
visible bottom-right. Pair with og:image:width="1200" og:image:height="630".
```

---

## Part C — Production pipeline

### C1. Run order in the GPT (patients see these first)
- **Batch 1 (patient view):** 1 hero → 2 six reasons → 3 home technique → 4 urgent card → 5 sodium swaps
- **Batch 2 (clinician view + social):** 6 funnel → 7 mechanism → 8 algorithm → 9 medication ladder → 10 OG card

One prompt per GPT turn. If a render garbles text, reply in the same thread with a targeted fix ("re-render with the
label exactly: …") instead of starting over, so the layout is kept. If you move to the `/generate-image` API later,
keep to 5 requests per minute (the planner's rate limit).

### C2. Save, convert, and check sizes
Save each download under `images/` with the exact file name. Then, from the repo root:

```bash
cd images && for f in difficult-to-control-hypertension-*.png; do cwebp -quiet -q 82 "$f" -o "${f%.png}.webp"; sips -g pixelWidth -g pixelHeight "$f" | tail -2 | tr '\n' ' '; echo " $f"; done
```

If a PNG's pixel size differs from the table in A2 (the GPT sometimes returns 1536×1024 or 1024×1536), keep the
image and update that figure's `width`/`height` attributes in the guide to the real size. Do not stretch it. The OG
card is the exception: it must be exactly 1200 × 630, so crop or pad it to that size.

### C3. Wire and verify
All 10 slots are already in the guide HTML with their `alt`, `fig-desc`, and `fig-abbrevs`. After uploading:

```bash
python3 patch_hero_fetchpriority.py --guide difficult-to-control-hypertension.html
python3 patch_hero_fullwidth.py --guide difficult-to-control-hypertension.html
python3 patch_hero_maxwidth.py --guide difficult-to-control-hypertension.html
python3 patch_image_lightbox.py --guide difficult-to-control-hypertension.html
python3 audit_acronym_expansion.py --guide difficult-to-control-hypertension.html
```

For the Stage 2 manifest and folder layout, run the `williamriveromd-local-image-generator` skill on this file.

### C4. Per-image QA before upload
- [ ] Text spelled exactly as in the prompt (patis, toyo, bagoong, tuyo, daing, longganisa, calamansi, tanglad; every generic drug name)
- [ ] American spelling on every label
- [ ] No brand names, doses, or readable monitor digits
- [ ] ACE inhibitor OR ARB only; investigational labels intact
- [ ] ENaC and ROMK apical, Na⁺/K⁺-ATPase basolateral (mechanism)
- [ ] Emergency and pregnancy exits before verification (algorithm)
- [ ] "GO NOW" / "CALL TODAY" carry text labels and icons, not color alone (urgent card)
- [ ] Light background; approved fonts; attribution present (except the hero)
- [ ] Every acronym on the image appears in that figure's `fig-abbrevs` and in the guide Glossary
- [ ] Hero circle not cropped; title-safe zone empty
