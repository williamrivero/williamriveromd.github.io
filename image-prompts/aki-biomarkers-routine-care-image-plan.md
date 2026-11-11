# Image Plan — *Kidney Stress Tests: AKI Biomarkers in Routine Care* (`aki-biomarkers-routine-care.html`)

**Guide:** Dual-mode (Patients & Families · Clinicians) guide on when urine TIMP-2×IGFBP7 and NGAL change care, how to read them alongside KDIGO staging, and what the team does next.
**Prepared:** 2026-11-09 · **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the ChatGPT **Image Generator** GPT → https://chatgpt.com/
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` · `williamriveromd-biomedical-mechanism-figure` · `williamriveromd-algorithm-generator-skill`

---

## 1. Design intent — understandable at every reading level

The guide's hardest idea is that **three different signals** (function, stress, damage) can disagree, and that a **positive test is a warning, not a diagnosis**. The image set is built as a ladder so a reader can stop at any rung and still leave with the right message:

| Rung | Reader | What the image must do | Assets |
|---|---|---|---|
| 1 · Feel | Anyone, including a worried relative with no science background | Show a calm, ordinary moment: a small urine sample after surgery. No fear, no machines. | Hero vignette |
| 2 · See the idea | Patients, families, students | One picture of the kidney tubule with three plain-language signals: *filtering · stress · damage* | 01 mechanism figure |
| 3 · Know what happens | Patients, families, ward nurses | Four illustrated steps from sample to protection plan | 05 patient journey |
| 4 · Read the result | Nurses, residents, general physicians | A 2×2 grid that never lets a biomarker overrule creatinine or urine output | 02 four-state matrix |
| 5 · Weigh the evidence | Clinicians | What the big trial did, with 100-person icon arrays instead of odds ratios | 03 BigpAK-2 design |
| 6 · Do the math | Clinicians, trainees | 1,000 people, colored dots, the meaning of a "positive" test | 06 natural frequencies |
| 7 · Act | ICU / perioperative teams | A clean top-to-bottom pathway | 04 decision pathway |

**Dual-layer labeling rule (all in-body figures).** Wherever a technical term appears, pair it with a short plain phrase in the same label — e.g. **"Stress signal"** in bold with *TIMP-2 × IGFBP7* in smaller type underneath. The plain phrase carries the meaning for lay readers; the technical term carries precision for clinicians. Never a technical term alone in a patient-section figure.

---

## 2. House rules baked into every prompt

- **Light backgrounds only** (white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, pale teal `#eef6f7`). Never navy, charcoal or black.
- **Fonts:** on-image type uses **Inter** only in this set (approved list: Inter · Nunito Sans · IBM Plex Sans · Manrope). No serif, no decorative fonts.
- **Palette:** navy `#0f1e2e` (text and lines), clinical teal `#1a6b72` (structure, "protect" actions), renal green `#1f7a4d` (stayed well / safe), amber `#b8860b` (stress / caution), clinical red `#b91c1c` (injury / event). Used as accents on light fills.
- **Attribution:** small semi-transparent `© renalcarematters.com` bottom-right on every image **except the wordless vignette hero**.
- **American English** in every on-image word (e.g., "color," "center," "pediatric").
- **Save** each asset as `.png` plus a `.webp` twin in `images/`, using the exact FILE NAME given.

### Clinical guardrails for THIS guide (must hold in every graphic)

1. **A biomarker never diagnoses or stages AKI.** No image may show a urine score "confirming" kidney injury, and no stage number may be printed next to a biomarker result.
2. **Function and stress are separate axes.** Creatinine and urine output stay visually distinct from the urine stress or damage signal.
3. **One labeled threshold: 0.3.** Show `>0.3` (above) versus `≤0.3` (at or below). The 2.0 literature cutpoint appears **only** in teaching captions, never as a second color tier in the pathway.
4. **Thresholds belong to one assay.** Never put the NGAL 125 ng/mL cutoff on an adult figure, and never place NGAL and TIMP-2×IGFBP7 thresholds on the same scale.
5. **No automatic reflexes.** No arrows from "high score" to "give fluids," "start dialysis," or "cancel the scan." The response is a protection *bundle* chosen by the team.
6. **Honest trial framing.** BigpAK-2 randomized patients who *all* tested positive. Never draw the trial as "tested vs not tested." No survival or dialysis benefit implied.
7. **Calm Filipino clinical context.** No distressed patients, no blood, no needles in the hero, no alarm lights, no neon.

---

## 3. Asset roster

| # | File (`images/…`) | Guide placement | Skill | Size | Wired? |
|---|---|---|---|---|---|
| 1 | `aki-biomarkers-routine-care-vignette-hero.png` | Patient hero disc + current `og:image` | hero-vignette | 2048×2048 | ✅ wired |
| 2 | `aki-biomarkers-routine-care-og.png` | Optional social card (swap into `og:image` when made) | infographic (OG) | 1200×630 | ✅ wired (`og:image`) |
| 3 | `aki-biomarkers-routine-care-01-function-stress-damage.png` | Patient § The Big Idea | biomedical-mechanism | 1792×1024 | ✅ wired |
| 4 | `aki-biomarkers-routine-care-02-four-state-matrix.png` | Clinician § Four States | infographic (reference card) | 1536×1152 | ✅ wired |
| 5 | `aki-biomarkers-routine-care-03-bigpak2-trial-design.png` | Clinician § Trials | infographic (data figure) | 1792×1024 | ✅ wired |
| 6 | `aki-biomarkers-routine-care-04-decision-pathway.png` | Clinician § Respond | algorithm (House style C) | 1024×1536 | ✅ wired |
| 7 | `aki-biomarkers-routine-care-05-patient-journey.png` | Patient § Protection Plan | infographic (multi-panel) | 1792×1024 | ✅ wired |
| 8 | `aki-biomarkers-routine-care-06-natural-frequencies.png` | Clinician § Positive Test Math | infographic (icon array) | 1792×1024 | ✅ wired |

**Wiring status (2026-11-09):** all 8 assets generated, QA-checked against the guide (icon counts, percentages, KDIGO criteria, algorithm branches), committed to `images/` as PNG + WebP, and wired; `og:image` now points to the 1200×630 card.

---

## 4. Prompts

### ASSET 1 — Hero vignette

```
FILE NAME: aki-biomarkers-routine-care-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life with hands (object hero)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: Close hands-only composition, slight low three-quarter angle, shallow depth of field
HUMAN VARIATION (vs. previous guide — Strengthening Kidney Resilience, an overhead no-people kitchen still life): people now present (hands only); clinician rather than household; gloved hands; mid-brown Filipino skin tone visible at the wrist; slim adult hands; no rings; short trimmed nails; pale-teal scrub cuff; intensive-care setting instead of kitchen; vertical object instead of flat-lay; low three-quarter angle instead of overhead; bedside depth instead of tabletop; cool-teal daylight instead of warm window light
AUDIENCE: mixed (patients, families, clinicians)
VISUAL GOAL: A calm, almost quiet moment — one small urine sample held up after surgery — that says "an early, simple check for a stressed kidney."

PROMPT:
Square 1:1 photorealistic editorial still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: I — Object Hero. Camera: close hands-only composition from a slight low three-quarter angle with shallow depth of field.

Subject: the gloved hands of a Filipino intensive-care nurse (slim adult hands, mid-brown skin visible at the wrist between a pale-teal scrub cuff and a light-blue nitrile glove, short trimmed nails, no jewelry) gently holding upright one small clear screw-cap urine sample tube filled with pale straw-yellow urine, at the center of the frame. The tube is the hero: crisp, clean, softly backlit so the urine glows faintly amber. A plain white blank sticker on the tube with no readable writing.

Supporting context (softly blurred, 20–30% of the circle): behind and below the hands, the edge of a crisp white hospital bed sheet and a clear urine collection bag with its tubing hanging from the bed frame; at the far edge, the soft out-of-focus glow of a bedside monitor rendered only as a pale teal-green blur (no numbers, no waveforms readable). Bright modern Philippine surgical intensive care unit, clean and calm, soft natural daylight from a window on the left.

Visual hierarchy: the sample tube and hands occupy 60–70% of the circle, slightly below and right of center; reserve a 20–25% TITLE SAFE ZONE in the upper-left of the circle made of soft pale-teal blurred wall and window light — no hands, objects, bedding, or equipment inside that zone. Gentle edge falloff toward a slightly deeper neutral at the rim.

Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners. Absolutely NO text of any kind: no title, subtitle, caption, label, logo, readable sticker writing, monitor numbers, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or fingers, extra fingers, blood, needles, syringes, alarming red monitor lights, a visible patient face, dark or murky urine.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. One dominant subject (the sample tube in gloved hands) at 60–70% of the circle, 2–3 blurred supporting elements, 20–25% empty title-safe zone upper-left. Hands anatomically correct (five fingers each). No readable text anywhere. Calm, bright, clinical-but-warm mood.
```

---

### ASSET 2 — Social share card (optional)

```
FILE NAME: aki-biomarkers-routine-care-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed
VISUAL GOAL: A thumb-stopping card that tells a scrolling reader "a urine test can warn early — and what to do with it."

PROMPT:
Landscape 1200×630 social share card for a nephrology education guide, premium medical editorial design on a clean WHITE (#ffffff) background with a very soft pale-teal (#eef6f7) panel on the right 45%. Typography set in Inter throughout.

Left side, left-aligned with generous margins:
- Small uppercase eyebrow in clinical teal #1a6b72, letter-spaced: "ACUTE KIDNEY INJURY · EARLY DETECTION"
- Large bold navy #0f1e2e headline on two lines: "Kidney Stress Tests" / "AKI Biomarkers in Routine Care"
- One-line subhead in medium gray-navy: "A warning before creatinine rises — and what the team does next."
- A thin teal rule, then small navy text: "Dr. W. Rivero, MD · Nephrology"

Right panel: a clean photorealistic close-up of a small clear screw-cap urine sample tube with pale straw-yellow urine held upright in a light-blue nitrile-gloved hand (mid-brown Filipino skin visible at the wrist), softly backlit, against a blurred bright intensive-care background in pale teal. Beside the tube, three small flat line icons stacked vertically in teal with one-word labels in Inter: a droplet "Filtering", a pause symbol inside a cell outline "Stress", a cracked cell outline "Damage".

Bottom-right corner: small semi-transparent navy text "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid dark, navy, charcoal, or black backgrounds; avoid cartoon style; avoid clutter; avoid tiny unreadable labels; avoid AI gibberish text; avoid misspellings; avoid needles, blood, or alarming monitors; avoid overprocessed HDR or neon. Use only Inter. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Headline readable at phone-thumbnail size. All text spelled exactly as given. White background. Attribution visible bottom-right.
```

> After generating, change `og:image` (and `twitter:image`, JSON-LD `image`) to `…-og.png` with `og:image:width="1200"` / `og:image:height="630"`.

---

### ASSET 3 — 01 · Function, stress and damage (mechanism figure, patient section)

```
FILE NAME: aki-biomarkers-routine-care-01-function-stress-damage.png
IMAGE TYPE: Biomedical mechanism figure (review-article schematic), dual-layer labels for lay readers
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families first; clinicians second
VISUAL GOAL: Make one idea obvious — the kidney sends three different signals, and they do not arrive at the same time.

PROMPT:
Create a publication-grade biomedical mechanism schematic in a scientific review-article style, flat vector illustration with soft semi-3D shading, on a WHITE background, with generous whitespace. Clean sans-serif typography set in Inter. Muted clinical palette: light gray-blue anatomy, soft yellow highlighted tubule segments, amber #b8860b for stress, clinical red #b91c1c for injury, clinical teal #1a6b72 for structure, navy #0f1e2e for text.

Title across the top in bold navy Inter: "Three signals from a stressed kidney"
Small subtitle in gray: "They can rise at different times — which is why one test cannot tell the whole story"

LEFT PANEL (organ level, about 25% width): a simplified kidney in cross-section, light gray-blue, with renal artery (red) and vein (blue). Label: "Kidney after a major operation". Small icons beside it showing the stressors, each with a short label: a falling arrow "Low blood pressure", a small surgical drape shape "Long surgery", a microbe outline "Infection". A thin dashed connector box zooms from the kidney cortex to the main panel.

CENTER PANEL (magnified functional unit, about 45% width, inside a thin dashed border): one nephron drawn as a clean schematic — glomerulus at top left, proximal tubule highlighted in soft yellow, loop and distal tubule in pale gray-blue. Inside the proximal tubule, show a short row of tubule cells drawn larger, like a magnified inset:
 - First two cells healthy (pale blue-gray).
 - Next two cells "pausing": amber outline with a small pause symbol "||" inside the nucleus, and tiny amber dots leaving into the tubule lumen labeled "TIMP-2 and IGFBP7".
 - Last cell injured: red cracked outline with tiny red dots leaving labeled "NGAL".
The tubule lumen flows downward into a small urine droplet at the bottom of the nephron labeled "Urine sample".

RIGHT PANEL (about 30% width): three stacked rounded cards, aligned top to bottom, each with a bold plain-language heading, a smaller technical line, and a tiny timing bar:
 Card 1, teal border — heading "Filtering (function)"; technical line "Creatinine · urine output"; timing bar note "Rises late — often 1–2 days".
 Card 2, amber border — heading "Stress (cells pausing)"; technical line "Urine TIMP-2 × IGFBP7"; timing bar note "Can rise within hours".
 Card 3, red border — heading "Damage (cells injured)"; technical line "Urine NGAL"; timing bar note "Raised by injury — and by infection or inflammation".

BOTTOM SUMMARY FLOW (three boxes joined by arrows, full width, short height):
 Left pale-pink box: "Stress on the kidney" with bullets "Low blood flow · less oxygen · toxins".
 Center pale-yellow box with a small magnifier icon: "Early warning signal in the urine".
 Right pale-blue box: "Team protects the kidney" with bullets "Check circulation · review medicines · watch closely".
Below the flow, a single small gray line: "A warning is not a diagnosis — kidney injury is still confirmed by creatinine and urine output."

Bottom-right corner: small semi-transparent navy text "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative effects, heavy shadows, cartoon faces on cells, clutter, more than about 40 words of label text outside the title, tiny unreadable labels, AI gibberish text, misspellings, invented pathways, numeric thresholds or cutoffs, any stage numbers, any implication that the urine signal diagnoses kidney injury. Do not place the NGAL and TIMP-2 × IGFBP7 signals on a shared numeric scale. Use only Inter.

QUALITY CHECK:
White background; three signals clearly color-coded (teal function, amber stress, red damage) and visually separate; nephron anatomy plausible (glomerulus → proximal tubule → loop → distal tubule); every technical term paired with a plain phrase; no numbers other than the timing notes given; attribution bottom-right; readable on a phone.
```

---

### ASSET 4 — 02 · Four-state interpretation matrix (clinician reference card)

```
FILE NAME: aki-biomarkers-routine-care-02-four-state-matrix.png
IMAGE TYPE: Clinician reference card (2×2 matrix + uncertainty band)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians, ICU nurses, residents
VISUAL GOAL: A glanceable grid that makes discordant results easy to read and never lets a biomarker overrule functional criteria.

PROMPT:
Clinical reference infographic card, publication-grade nephrology design, on an off-white (#fafafa) background with clean rounded cards. Typography set in Inter. Navy #0f1e2e text, clinical teal #1a6b72 structure lines.

Title top-left in bold navy: "Reading the result: four states, plus one"
Subtitle in gray: "Function and stress are separate axes. Stage AKI by creatinine and urine output — always."

Main element: a 2×2 matrix with clean axis labels.
- Vertical axis (left), bold label: "Creatinine or urine output meets KDIGO criteria?" with row labels "No (enough data)" (top row) and "Yes" (bottom row).
- Horizontal axis (top), bold label: "Urine stress or damage signal" with column labels "Above threshold" (left column) and "At or below threshold" (right column).

The four cells, each a rounded card with a short bold title and one or two short lines:
 Top-left, pale amber fill #fdf6e3 with amber border: title "Early warning"; lines "Higher short-term risk" / "Review causes, exposures · watch closely".
 Top-right, pale green fill #eaf5ee with green border: title "Lower short-term risk"; lines "Keep usual surveillance" / "Risk is not zero".
 Bottom-left, pale red fill #fbeaea with red border: title "AKI present"; lines "Stage conventionally" / "Marker adds context · find the cause".
 Bottom-right, pale red fill #fbeaea with red border and a small "≠" badge: title "AKI present — discordant"; lines "Low marker does not cancel AKI" / "Check timing, assay, mechanism".

Below the matrix, a full-width soft-gray band #f3f4f6 with a dashed border and a small question-mark icon: title "Function data missing or unreliable"; line "Status uncertain — get a credible baseline and fix urine-output measurement first. A test not run is 'not measured,' not 'negative.'"

Small footer note in gray, left: "KDIGO 2012: SCr ≥0.3 mg/dL in 48 h · ≥1.5× baseline in 7 days · urine <0.5 mL/kg/h for 6 h".

Bottom-right corner: small semi-transparent navy text "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, 3D effects, photos, people, clutter, tiny unreadable labels, AI gibberish text, misspellings, extra numeric thresholds beyond the KDIGO footer, stage numbers inside the biomarker column, any arrow from a cell to "fluids" or "dialysis." Use only Inter.

QUALITY CHECK:
Matrix axes unambiguous; colors consistent (amber warning, green lower risk, red AKI present); the fifth uncertainty band clearly separate; KDIGO footer exactly as written; attribution bottom-right; legible at slide size.
```

---

### ASSET 5 — 03 · BigpAK-2 trial design and result (data figure)

```
FILE NAME: aki-biomarkers-routine-care-03-bigpak2-trial-design.png
IMAGE TYPE: Trial-design data figure with 100-person icon arrays
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (readable by motivated patients)
VISUAL GOAL: Show exactly who was studied and what changed — in people, not odds ratios — and make clear what the trial could not answer.

PROMPT:
Clean medical data-visualization figure, journal graphical-abstract style, on a WHITE background with soft-gray (#f3f4f6) panels. Typography set in Inter. Navy #0f1e2e text, clinical teal #1a6b72 for the bundle arm, cool gray #8a94a6 for usual care, clinical red #b91c1c for people who developed the outcome.

Title top-left in bold navy: "BigpAK-2: what the trial tested"
Subtitle in gray: "34 European hospitals · adults after major surgery · Lancet 2025"

LEFT THIRD — a vertical enrollment funnel of three rounded boxes joined by thin navy arrows:
 Box 1: "7,873 screened after major surgery"
 Box 2: "High clinical risk AND urine stress score positive"
 Box 3: "1,180 randomized"
A small teal callout tag beside Box 2: "Everyone randomized had a positive test".
From Box 3, the arrow splits into two arms.

CENTER AND RIGHT — two side-by-side panels, each with a 10×10 grid of 100 simple person icons:
 Left panel, header in gray: "Usual care" — 22 of the 100 icons filled clinical red, 78 filled light gray. Big number under the grid: "22.3%" with small text "131 of 588 developed moderate or severe AKI within 72 h".
 Right panel, header in teal: "Kidney-protection bundle" — 14 of the 100 icons filled clinical red, 86 filled light teal. Big number under the grid: "14.4%" with small text "84 of 584".
Between or below the two panels, a teal ribbon: "About 8 fewer per 100 · treat 12 to prevent 1".
A small legend: red icon = "Moderate or severe AKI (stage 2–3) by 72 h".

Bundle strip along the bottom of the right panel, four small teal line icons with one- or two-word labels: "Hemodynamic monitoring", "Fluid and blood pressure optimization", "Avoid nephrotoxins and contrast", "Glucose control".

FAR-RIGHT or bottom-right small soft-amber box titled "What this trial cannot tell us", three short lines:
 "Testing vs. choosing by clinical risk alone"
 "Effect on dialysis or survival"
 "Results outside major surgery"

Bottom-right corner: small semi-transparent navy text "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, photos, faces on the person icons, 3D effects, clutter, tiny unreadable labels, AI gibberish text, misspellings, wrong counts. Do NOT draw the trial as "tested vs. not tested." Do not imply fewer deaths or less dialysis. Exactly 22 red icons in the usual-care grid and exactly 14 red icons in the bundle grid. Use only Inter.

QUALITY CHECK:
Icon counts exact (22 and 14 red of 100); numbers exactly as given (7,873 · 1,180 · 22.3% · 131 of 588 · 14.4% · 84 of 584 · 8 per 100 · 12); the "everyone tested positive" callout present; limitations box present; attribution bottom-right.
```

---

### ASSET 6 — 04 · Decision pathway (algorithm, House style C)

```
FILE NAME: aki-biomarkers-routine-care-04-decision-pathway.png
IMAGE TYPE: Clinical algorithm — renalcarematters.com house style (Style Mode C)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: ICU and perioperative clinicians
VISUAL GOAL: A clean top-to-bottom pathway where eligibility and timing come first, the result routes to a bundle or usual surveillance, and conventional staging runs through every branch.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. Use a white background, restrained navy and teal typography set in Inter, thin teal connector arrows, and generous margins. Layout centered, symmetrical, portrait.

Color conventions: navy #0f1e2e for title and body text; teal #1a6b72 for decision diamonds and arrows; green #1f7a4d for recommended endpoint actions; amber #b8860b for caution nodes; soft gray #f3f4f6 for side notes. Rounded rectangles for actions and endpoints, diamonds for decisions.

Title (top, bold navy): "Urine stress test after major surgery"
Subtitle (gray): "Adults · labeled assay · locally approved pathway"

Content, top to bottom:
1. Rounded box (navy outline): "Adult after major surgery, now in ICU or equivalent, with clinical risk factors"
2. Diamond (teal): "Already stage 2–3 AKI or on kidney replacement therapy?"
   - "Yes" branch to the RIGHT → gray box: "Test does not answer this question — evaluate and manage AKI directly"
   - "No" continues down.
3. Diamond (teal): "Sample in the protocol window, result in hours, response owner named?"
   - "No" branch to the RIGHT → green box: "Use the clinical pathway: protection bundle by clinical risk"
   - "Yes" continues down.
4. Rounded box (navy outline): "Urine TIMP-2 × IGFBP7 — verify assay, specimen, validity"
5. Diamond (teal): "Result above 0.3?"
   - LEFT branch "Above 0.3" → green box: "Kidney-protection bundle" with four short lines: "Perfusion and fluid responsiveness" / "Medication and nephrotoxin review" / "Contrast only if needed" / "Glucose control · hourly urine output"
   - RIGHT branch "At or below 0.3" → teal-outline box: "Usual careful surveillance — risk is lower, not zero"
6. Both branches merge into one full-width green-outline box at the bottom: "Stage any AKI by creatinine and urine output · find the cause · reassess"

Side note (soft gray box, lower left, small text): "Never: automatic fluid bolus · dialysis by marker · delaying urgent care for a result"
Caution note (small amber-outline box, lower right): "0.3 is the only labeled threshold"

Include a small professional footer reading "© renalcarematters.com" positioned at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No dark background, no clutter, no photorealistic people, no 3D, no extra branches, no second threshold tier (do not add 2.0), no NGAL or pediatric content, no arrows to dialysis, no gibberish text, no misspellings. Use only Inter.

QUALITY CHECK:
Three decision diamonds in order (established AKI → logistics → result); both result branches merge into conventional staging; side and caution notes present; all text exactly as given; footer attribution bottom-right; readable at thumbnail size.
```

---

### ASSET 7 — 05 · From urine sample to protection plan (patient journey)

```
FILE NAME: aki-biomarkers-routine-care-05-patient-journey.png
IMAGE TYPE: Multi-panel patient education infographic (4 steps, mixed media)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families (any reading level)
VISUAL GOAL: Show, step by step, what actually happens after a kidney stress test — so families feel informed, not alarmed.

PROMPT:
Patient education infographic, landscape 16:9, modern Philippine hospital aesthetic, clean WHITE background with four equal rounded soft-gray (#f3f4f6) panels in a single row joined by thin teal chevron arrows. Typography set in Inter. Navy #0f1e2e text, clinical teal #1a6b72 accents, renal green #1f7a4d for the final step.

Title across the top in bold navy: "After the test: what the care team does"
Subtitle in gray: "A small urine sample, a result in hours, four protective steps"

Each panel has a teal step number in a circle, a photorealistic vignette (bright, calm, softly lit), a bold 2–4 word heading, and one short line of plain text:

Panel 1 — Photo: gloved hands drawing a few milliliters of pale urine from the sampling port of a catheter bag tube into a small clear tube at a bedside; no face shown. Heading: "A few drops of urine". Line: "Taken from the catheter tube — no needle".

Panel 2 — Photo: a Filipino woman laboratory scientist in her 40s (round face, short wavy hair, rimless glasses, white lab coat over a maroon top) placing the small tube into a compact bench analyzer in a bright laboratory; the analyzer screen blank. Heading: "A stress score in hours". Line: "The lab compares it with a cut-off".

Panel 3 — Photo: a Filipino male intensivist in his early 50s (tall, graying side-parted hair, clean-shaven, navy scrubs, stethoscope) and a younger Filipina nurse (late 20s, high ponytail, pale-teal scrubs) reviewing a tablet together at the foot of a hospital bed, calm expressions; the patient is out of frame. Heading: "The team reviews the plan". Line: "Circulation, medicines, blood sugar".

Panel 4 — Photo: a clear hourly urine-measuring chamber (urimeter) on a catheter bag with a nurse's gloved hand noting it on a paper chart; soft daylight. Heading: "Close watching". Line: "Blood tests and urine checked often".

Under the four panels, a full-width pale-green banner with a small check icon: "A high score means 'protect and watch closely' — not 'kidney failure.'"

Bottom-right corner: small semi-transparent navy text "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, distressed or crying people, visible patient faces, blood, needles in skin, alarming monitors, readable numbers on any screen, cartoon style, clutter, tiny unreadable labels, AI gibberish text, misspellings, duplicated faces, stock-photo blandness. Do not show fluids being pushed or dialysis machines. Use only Inter.

QUALITY CHECK:
Four panels in one row with clear left-to-right flow; each heading and line spelled exactly as given; people look like distinct individuals with Filipino features and are calm; banner message present; white background; attribution bottom-right; readable on a phone.
```

---

### ASSET 8 — 06 · What a "positive" test means: 1,000 patients (natural frequencies)

```
FILE NAME: aki-biomarkers-routine-care-06-natural-frequencies.png
IMAGE TYPE: Icon-array data figure (natural frequencies)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians and trainees; understandable to motivated patients
VISUAL GOAL: Make post-test probability visible: most people with a high score do not develop severe AKI, while a low score is genuinely reassuring.

PROMPT:
Clean medical data-visualization figure on a WHITE background, flat vector style, typography set in Inter. Navy #0f1e2e text, clinical red #b91c1c for people who develop the outcome, amber #b8860b outline for "above 0.3" group, renal green #1f7a4d outline for "at or below 0.3" group, light gray dots for people who stay well.

Title top-left in bold navy: "What does a result above 0.3 mean? Imagine 1,000 ICU patients"
Subtitle in gray: "Starting risk 10% · urine TIMP-2 × IGFBP7 · moderate or severe AKI within 12 hours"

LEFT, a small top strip: one row showing "1,000 tested → 100 will develop AKI · 900 will not".

MAIN AREA: two large rounded panels side by side, each filled with a neat grid of small dots (one dot = one person):
 Left panel, amber outline, header "Score above 0.3 — 579 people": 579 dots, of which exactly 92 are clinical red and 487 light gray. Large text below: "92 of 579 develop AKI ≈ 1 in 6 (15.8%)".
 Right panel, green outline, header "Score at or below 0.3 — 421 people": 421 dots, of which exactly 8 are clinical red and 413 light gray. Large text below: "8 of 421 develop AKI ≈ 1 in 50 (2.0%)".
Legend: red dot "develops moderate or severe AKI", gray dot "does not".

Bottom band, soft gray, three short takeaways in Inter:
 "A low score is reassuring."
 "A high score is a warning — most people stay well."
 "Act with low-risk protection, not risky treatments."

Tiny source line, bottom-left in gray: "Sensitivity 91.5% · specificity 45.8% (FDA Study A, lab 1). Hypothetical 10% starting risk; rounded."

Bottom-right corner: small semi-transparent navy text "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, 3D, photos, people faces, pie charts, clutter, tiny unreadable labels, AI gibberish text, misspellings, wrong counts. Do not add a 2.0 cutpoint. Use only Inter.

QUALITY CHECK:
Dot counts exact (579 with 92 red; 421 with 8 red; totals 1,000 and 100 red); percentages exactly 15.8% and 2.0%; takeaways spelled as given; source line present; attribution bottom-right.
```

---

## 5. Production checklist

1. Generate each asset in the Image Generator GPT; regenerate any image with misspelled text, wrong counts (Assets 5 and 8), or a cropped hero circle.
2. Save as `images/<FILE NAME>.png` and convert a WebP twin (e.g., `cwebp -q 85 in.png -o out.webp`).
3. Display sizes already set in the guide: hero 2048×2048; 01, 03, 05, 06 at 1792×1024; 02 at 1536×1152; 04 at 1024×1536.
4. If Asset 2 (OG) is made, update `og:image`, `twitter:image`, JSON-LD `image`, and set `og:image:width/height` to 1200/630.
5. Run `python3 generate_latest_guides.py` so the Latest-guides card picks up the hero thumbnail, then commit.
