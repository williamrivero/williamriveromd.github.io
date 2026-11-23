# GPT image prompts — new and missing figures

**Site:** renalcarematters.com · **Prepared:** November 23, 2026 · **Tracks:** Renal Care Academy technician tracks

This file has two parts.

- **Part 1** holds complete prompts for **28 new figures** (18 core ★, 10 optional ○) that illustrate the lessons added to the Hemodialysis Technician track. These are not in the first prompt pack.
- **Part 2** lists every figure from the first prompt pack (`GPT-IMAGE-PROMPTS.md`) that has **not been produced yet**: 0 files that do not exist, plus 11 flat teaching diagrams that are waiting to be replaced. Their prompts are already written; find each one in `GPT-IMAGE-PROMPTS.md` by its ID.

## How to produce

1. One figure per chat. Paste one gray block into a fresh ChatGPT image chat and ask for the canvas size on the entry.
2. Check the text first: compare every label with the verbatim list. If one word is wrong, ask for that word to be fixed, not for a new image.
3. Reject an image with an invented number, a brand, a dark background, flat clip-art rendering, or a missing or altered footer (`© renalcarematters.com`).
4. The one circuit figure is generated with the `dialysis-circuit-schematic` skill, not from a prompt in this file.
5. Save as PNG under the exact filename into `images/`. New figures are not yet referenced by a lesson: after saving, add a key for the file in `tools/techcourses/figs.py` and place it in the lesson with `{{fig:key}}`, then run `python3 generate_tech_courses.py --patch`.
6. Every figure needs Dr. Rivero's review before publication.

# Part 1 — New figures

## Production list

| # | ID | Figure | File | Type |
|---|---|---|---|---|
| 1 | HD-01-D ★ | One patient, one treatment: who does what | `images/hemodialysis-technician-01-patient-journey.png` | flow |
| 2 | HD-01-E ○ | Name alert | `images/hemodialysis-technician-01-name-alert.png` | card |
| 3 | HD-02-D ★ | Measuring blood pressure correctly | `images/hemodialysis-technician-02-blood-pressure-technique.png` | aid |
| 4 | HD-02-E ○ | Weighing accurately | `images/hemodialysis-technician-02-accurate-weight.png` | aid |
| 5 | HD-03-D ○ | Everything that pours counts as fluid | `images/hemodialysis-technician-03-fluid-counts.png` | card |
| 6 | HD-04-E ★ | From prescription to machine | `images/hemodialysis-technician-04-prescription-to-machine.png` | aid |
| 7 | HD-04-F ○ | Where treatment time is lost | `images/hemodialysis-technician-04-time-lost.png` | aid |
| 8 | HD-05-D ★ | Hand hygiene moments at the station | `images/hemodialysis-technician-05-hand-hygiene-moments.png` | aid |
| 9 | HD-05-E ○ | Blood spill response | `images/hemodialysis-technician-05-blood-spill.png` | flow |
| 10 | HD-06-D ★ | Priming: saline pushes the air out | `images/hemodialysis-technician-06-priming-air-out.png` | aid |
| 11 | HD-06-E ★ | The stages of a machine day | `images/hemodialysis-technician-06-machine-day.png` | flow |
| 12 | HD-06-F ★ | Two cleaning jobs after every patient | `images/hemodialysis-technician-06-two-cleaning-jobs.png` | aid |
| 13 | HD-07-D ★ | Total chlorine test, step by step | `images/hemodialysis-technician-07-chlorine-test-steps.png` | flow |
| 14 | HD-07-E ○ | Mixing bicarbonate concentrate | `images/hemodialysis-technician-07-bicarbonate-mixing.png` | flow |
| 15 | HD-08-D ★ | Holding a needle site | `images/hemodialysis-technician-08-holding-needle-site.png` | aid |
| 16 | HD-08-E ★ | Catheter: look, do not open | `images/hemodialysis-technician-08-catheter-look.png` | aid |
| 17 | HD-09-D ★ | Every alarm: patient, lines, screen | `images/hemodialysis-technician-09-alarm-order.png` | flow |
| 18 | HD-09-E ★ | Where each alarm sensor sits | `images/hemodialysis-technician-09-alarm-sensors.png` | circuit |
| 19 | HD-10-D ○ | Emergency cart: the daily check | `images/hemodialysis-technician-10-cart-check.png` | card |
| 20 | HD-10-E ★ | The first five minutes | `images/hemodialysis-technician-10-first-five-minutes.png` | card |
| 21 | HD-11-D ★ | The life of a reprocessed dialyzer | `images/hemodialysis-technician-11-dialyzer-life-cycle.png` | flow |
| 22 | HD-11-E ★ | Total cell volume and the 80 percent rule | `images/hemodialysis-technician-11-total-cell-volume.png` | aid |
| 23 | HD-11-F ○ | Pressure leak test | `images/hemodialysis-technician-11-leak-test.png` | aid |
| 24 | HD-11-G ★ | Three methods: who does which step | `images/hemodialysis-technician-11-three-methods.png` | card |
| 25 | HD-11-H ★ | Two strips, two opposite questions | `images/hemodialysis-technician-11-presence-residual.png` | aid |
| 26 | HD-11-I ○ | Reprocessing room: dirty in, clean out | `images/hemodialysis-technician-11-reprocessing-room.png` | aid |
| 27 | HD-12-D ★ | Opening the shift: one walk-through | `images/hemodialysis-technician-12-opening-walkthrough.png` | flow |
| 28 | HD-12-E ○ | Four levels of competence | `images/hemodialysis-technician-12-four-levels.png` | card |

## Module 1 — The Dialysis Unit and the Technician's Role

### HD-01-D ★ — One patient, one treatment: who does what

**File:** `images/hemodialysis-technician-01-patient-journey.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `journey`

**Job:** U: follows a patient from arrival to departure and names who is responsible at each step.

**Alt:** Seven-step flow of one patient's treatment from arrival to departure, with each step tagged technician or nurse.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · One patient, one treatment: who does what · academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `journey`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Seven steps in one row or two rows, each a small illustrated scene: arrival and identification, weighing, pre-treatment checks, connection by the nurse, treatment with regular rounds, disconnection by the nurse and site care, post-weight and departure. A colored tag on each step shows the lead role: technician or nurse. Connection and disconnection carry the nurse tag only.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: follows a patient from arrival to departure and names who is responsible at each step.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Arrive and identify
  • 2 Weigh
  • 3 Pre-treatment checks
  • 4 Connect (nurse)
  • 5 Treatment and rounds
  • 6 Disconnect (nurse)
  • 7 Post-weight and departure
  • Technician
  • Nurse
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No technician inserting needles or connecting lines
✗ no patient names
✗ no clock times
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Arrive and identify" present and spelled exactly — confirmed
□ Label "2 Weigh" present and spelled exactly — confirmed
□ Label "3 Pre-treatment checks" present and spelled exactly — confirmed
□ Label "4 Connect (nurse)" present and spelled exactly — confirmed
□ Label "5 Treatment and rounds" present and spelled exactly — confirmed
□ Label "6 Disconnect (nurse)" present and spelled exactly — confirmed
□ Label "7 Post-weight and departure" present and spelled exactly — confirmed
□ Label "Technician" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-01-E ○ — Name alert

**File:** `images/hemodialysis-technician-01-name-alert.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `namealert`

**Job:** A: recognizes a name-alert situation and applies two identifiers every time.

**Alt:** Two similar fictional names marked with name-alert stickers, with the two identifiers to check.

```text
Reference card · 1672 × 941, 16:9 landscape · Name alert · academy/hemodialysis-technician-01-dialysis-unit-technician-role.html, section `namealert`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two fictional patient wristbands or chart labels side by side with similar names, each carrying a bright name-alert sticker. Below, two tiles: full name, and date of birth. The same sticker appears on a dialyzer label.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: recognizes a name-alert situation and applies two identifiers every time.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • NAME ALERT
  • Jose Santos
  • Josefina Santos
  • Identifier 1: full name
  • Identifier 2: date of birth
  • Ask, do not suggest
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No real-looking record numbers or dates
✗ no faces
✗ no other names
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "NAME ALERT" present and spelled exactly — confirmed
□ Label "Jose Santos" present and spelled exactly — confirmed
□ Label "Josefina Santos" present and spelled exactly — confirmed
□ Label "Identifier 1: full name" present and spelled exactly — confirmed
□ Label "Identifier 2: date of birth" present and spelled exactly — confirmed
□ Label "Ask, do not suggest" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 2 — Kidneys and Kidney Failure

### HD-02-D ★ — Measuring blood pressure correctly

**File:** `images/hemodialysis-technician-02-blood-pressure-technique.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `vitalsigns`

**Job:** A: positions the patient and cuff correctly and keeps the cuff off the access arm.

**Alt:** Seated patient having blood pressure measured on the non-access arm with the arm supported at heart level.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Measuring blood pressure correctly · academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `vitalsigns`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Adult seated in a dialysis chair, back supported, feet flat, arm supported at heart level, cuff on the bare upper arm of the NON-access arm. The access arm rests uncovered with a small 'no cuff' symbol near it. Skin is opaque.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: positions the patient and cuff correctly and keeps the cuff off the access arm.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Seated and rested
  • Back supported, feet flat
  • Arm at heart level
  • Cuff on bare skin, correct size
  • Never on the access arm
  • Record arm and position
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No cuff on an arm with a fistula, graft, or dressing
✗ no readable monitor values
✗ no anatomy through skin
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Seated and rested" present and spelled exactly — confirmed
□ Label "Back supported, feet flat" present and spelled exactly — confirmed
□ Label "Arm at heart level" present and spelled exactly — confirmed
□ Label "Cuff on bare skin, correct size" present and spelled exactly — confirmed
□ Label "Never on the access arm" present and spelled exactly — confirmed
□ Label "Record arm and position" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-02-E ○ — Weighing accurately

**File:** `images/hemodialysis-technician-02-accurate-weight.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `weightmath`

**Job:** A: obtains a weight that can be trusted and compares it with the last post-treatment weight.

**Alt:** Patient on a platform scale without shoes or bag, and a wheelchair scale with the chair weight subtracted.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Weighing accurately · academy/hemodialysis-technician-02-kidneys-kidney-failure.html, section `weightmath`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
A patient standing on a platform scale in light clothing, no bag, no shoes; beside the scale a bag, jacket, and shoes set down. A second panel shows a wheelchair scale with the empty chair weight subtracted.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: obtains a weight that can be trusted and compares it with the last post-treatment weight.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Same scale every time
  • Scale on a hard, level floor
  • Light clothing, no bag, no shoes
  • Wheelchair: subtract the chair
  • Unexpected weight: weigh again
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No readable weight values
✗ no patient holding a bag
✗ no carpet under the scale
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Same scale every time" present and spelled exactly — confirmed
□ Label "Scale on a hard, level floor" present and spelled exactly — confirmed
□ Label "Light clothing, no bag, no shoes" present and spelled exactly — confirmed
□ Label "Wheelchair: subtract the chair" present and spelled exactly — confirmed
□ Label "Unexpected weight: weigh again" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 3 — Treatment Options and Living with Kidney Failure

### HD-03-D ○ — Everything that pours counts as fluid

**File:** `images/hemodialysis-technician-03-fluid-counts.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `dietfluid`

**Job:** U: recognizes the everyday items that count toward a fluid allowance.

**Alt:** Six everyday items that count as fluid: water, coffee, soup, rice porridge, ice, and water taken with medicines.

```text
Reference card · 1672 × 941, 16:9 landscape · Everything that pours counts as fluid · academy/hemodialysis-technician-03-treatment-options-living-with-kidney-failure.html, section `dietfluid`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six illustrated tiles of common items: a glass of water, a cup of coffee, a bowl of soup, rice porridge, ice cubes, and a small cup of water with tablets. No volumes shown.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: recognizes the everyday items that count toward a fluid allowance.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Water
  • Coffee and tea
  • Soup broth
  • Rice porridge
  • Ice
  • Water with medicines
  • The dietitian sets the allowance
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No volumes or numbers
✗ no brand packaging
✗ no alcohol
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Water" present and spelled exactly — confirmed
□ Label "Coffee and tea" present and spelled exactly — confirmed
□ Label "Soup broth" present and spelled exactly — confirmed
□ Label "Rice porridge" present and spelled exactly — confirmed
□ Label "Ice" present and spelled exactly — confirmed
□ Label "Water with medicines" present and spelled exactly — confirmed
□ Label "The dietitian sets the allowance" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 4 — Principles of Hemodialysis

### HD-04-E ★ — From prescription to machine

**File:** `images/hemodialysis-technician-04-prescription-to-machine.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `rxlines`

**Job:** U: matches each line of the prescription to what is set up or checked at the station.

**Alt:** A prescription sheet linked line by line to the dialyzer, pump, concentrates, and machine settings at a station.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · From prescription to machine · academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `rxlines`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Left: a generic prescription sheet with seven unlabeled lines, each joined by a leader line to an item at the station on the right: dialyzer, session time, blood pump, dialysate flow, concentrate containers, temperature, fluid removal goal. Screen faces are unreadable.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: matches each line of the prescription to what is set up or checked at the station.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Dialyzer
  • Time
  • Blood flow
  • Dialysate flow
  • Dialysate composition
  • Temperature
  • Fluid removal goal
  • Only the prescriber changes the prescription
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No numeric settings
✗ no readable screens
✗ no drug names
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Dialyzer" present and spelled exactly — confirmed
□ Label "Time" present and spelled exactly — confirmed
□ Label "Blood flow" present and spelled exactly — confirmed
□ Label "Dialysate flow" present and spelled exactly — confirmed
□ Label "Dialysate composition" present and spelled exactly — confirmed
□ Label "Temperature" present and spelled exactly — confirmed
□ Label "Fluid removal goal" present and spelled exactly — confirmed
□ Label "Only the prescriber changes the prescription" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-04-F ○ — Where treatment time is lost

**File:** `images/hemodialysis-technician-04-time-lost.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `chairclear`

**Job:** U: sees that late starts, pump stops, and early finishes all shorten the delivered treatment.

**Alt:** A session-length bar with pieces removed for late start, pump stops, and early finish, leaving the delivered time.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Where treatment time is lost · academy/hemodialysis-technician-04-principles-of-hemodialysis.html, section `chairclear`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
A horizontal bar representing the prescribed session, with three pieces cut out and set below it: late start, alarms that stop the blood pump, early finish. The remaining bar is labeled delivered time.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees that late starts, pump stops, and early finishes all shorten the delivered treatment.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Prescribed time
  • Late start
  • Pump stopped by alarms
  • Early finish
  • Delivered time
  • Record the actual start and end
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No minute values
✗ no patient blame imagery
✗ no clocks with readable times
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Prescribed time" present and spelled exactly — confirmed
□ Label "Late start" present and spelled exactly — confirmed
□ Label "Pump stopped by alarms" present and spelled exactly — confirmed
□ Label "Early finish" present and spelled exactly — confirmed
□ Label "Delivered time" present and spelled exactly — confirmed
□ Label "Record the actual start and end" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 5 — Dialysis Infection Prevention and Waste Management

### HD-05-D ★ — Hand hygiene moments at the station

**File:** `images/hemodialysis-technician-05-hand-hygiene-moments.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `handsppe`

**Job:** A: performs hand hygiene at each required moment around a dialysis station.

**Alt:** Overhead view of a dialysis station with five numbered hand hygiene moments.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Hand hygiene moments at the station · academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `handsppe`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Overhead view of one station (chair, machine, side table, supply cart at a distance). Five numbered markers placed where each moment occurs: before touching the patient, before a clean or aseptic task, after contact with blood or body fluid, after touching the patient, after touching the machine or station surfaces.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: performs hand hygiene at each required moment around a dialysis station.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Before touching the patient
  • 2 Before a clean task
  • 3 After blood or body fluid
  • 4 After touching the patient
  • 5 After touching the machine or station
  • Gloves do not replace hand hygiene
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No more than five markers
✗ no needles
✗ no brand of hand rub
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Before touching the patient" present and spelled exactly — confirmed
□ Label "2 Before a clean task" present and spelled exactly — confirmed
□ Label "3 After blood or body fluid" present and spelled exactly — confirmed
□ Label "4 After touching the patient" present and spelled exactly — confirmed
□ Label "5 After touching the machine or station" present and spelled exactly — confirmed
□ Label "Gloves do not replace hand hygiene" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-05-E ○ — Blood spill response

**File:** `images/hemodialysis-technician-05-blood-spill.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `spillsharps`

**Job:** A: contains and cleans a blood spill in the correct order.

**Alt:** Six-step sequence for cleaning a blood spill, from protective equipment to hand hygiene.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Blood spill response · academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `spillsharps`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps as small illustrated panels: put on protective equipment, cover the spill with absorbent material, apply the approved disinfectant, wait the contact time, wipe up and discard as infectious waste, remove protective equipment and perform hand hygiene.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: contains and cleans a blood spill in the correct order.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Protect yourself
  • 2 Cover and absorb
  • 3 Apply disinfectant
  • 4 Wait the contact time
  • 5 Wipe up; infectious waste
  • 6 Remove protection; hand hygiene
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No contact time in numbers
✗ no disinfectant brand
✗ no graphic blood, only a small stylized spill
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Protect yourself" present and spelled exactly — confirmed
□ Label "2 Cover and absorb" present and spelled exactly — confirmed
□ Label "3 Apply disinfectant" present and spelled exactly — confirmed
□ Label "4 Wait the contact time" present and spelled exactly — confirmed
□ Label "5 Wipe up; infectious waste" present and spelled exactly — confirmed
□ Label "6 Remove protection; hand hygiene" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 6 — Machines, Dialyzers, and the Extracorporeal Circuit

### HD-06-D ★ — Priming: saline pushes the air out

**File:** `images/hemodialysis-technician-06-priming-air-out.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `priming`

**Job:** U: understands that saline enters at the bottom of the blood side and drives air out at the top.

**Alt:** Vertical dialyzer being primed with saline entering at the bottom and air leaving at the top, with an inset of air-locked fibers.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Priming: saline pushes the air out · academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `priming`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
A dialyzer held vertically in its holder with blood lines attached, no patient. Saline (clear, pale blue tint) rising from the bottom header through the fibers; small bubbles leaving at the top header toward the venous chamber. An inset shows fibers with trapped air as pale streaks, marked as incorrect.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands that saline enters at the bottom of the blood side and drives air out at the top.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Saline bag
  • Saline enters at the bottom
  • Air leaves at the top
  • Venous chamber: set the level
  • Pale streaks = trapped air
  • No patient connected
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No blood in the lines
✗ no patient
✗ no fluid entering from the top
✗ no readable pump speed
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Saline bag" present and spelled exactly — confirmed
□ Label "Saline enters at the bottom" present and spelled exactly — confirmed
□ Label "Air leaves at the top" present and spelled exactly — confirmed
□ Label "Venous chamber: set the level" present and spelled exactly — confirmed
□ Label "Pale streaks = trapped air" present and spelled exactly — confirmed
□ Label "No patient connected" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-06-E ★ — The stages of a machine day

**File:** `images/hemodialysis-technician-06-machine-day.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `operate`

**Job:** U: places any moment of the day in the sequence from switch-on to shutdown.

**Alt:** Ten-step sequence of a dialysis machine's day from switch-on and self-test to shutdown and record.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · The stages of a machine day · academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `operate`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Ten steps in two rows of five, each a small panel with a simple illustration of the machine at that stage.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: places any moment of the day in the sequence from switch-on to shutdown.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Switch on and self-test
  • 2 Rinse
  • 3 Connect concentrates
  • 4 Stabilize
  • 5 Set up and prime
  • 6 Pre-treatment checks
  • 7 Treatment
  • 8 End and strip
  • 9 Disinfect
  • 10 Shutdown and record
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No readable screen values
✗ no brand design
✗ no patient shown except a simple seated figure at step 7
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Switch on and self-test" present and spelled exactly — confirmed
□ Label "2 Rinse" present and spelled exactly — confirmed
□ Label "3 Connect concentrates" present and spelled exactly — confirmed
□ Label "4 Stabilize" present and spelled exactly — confirmed
□ Label "5 Set up and prime" present and spelled exactly — confirmed
□ Label "6 Pre-treatment checks" present and spelled exactly — confirmed
□ Label "7 Treatment" present and spelled exactly — confirmed
□ Label "8 End and strip" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-06-F ★ — Two cleaning jobs after every patient

**File:** `images/hemodialysis-technician-06-two-cleaning-jobs.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `mdisinfect`

**Job:** U: distinguishes wiping the outside surfaces from disinfecting the inside fluid path.

**Alt:** The same machine shown being wiped on the outside and, in cutaway, having its internal fluid path disinfected.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Two cleaning jobs after every patient · academy/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit.html, section `mdisinfect`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
One machine drawn twice. Left: gloved hand wiping the screen, front panel, clamps, and pole, surfaces shown wet. Right: cutaway showing the internal fluid path highlighted, with a disinfectant container connected and dialysate connectors on their rinse ports, no dialyzer attached.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: distinguishes wiping the outside surfaces from disinfecting the inside fluid path.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Outside: wipe every surface
  • Keep wet for the contact time
  • Inside: run the disinfection program
  • No dialyzer or lines attached
  • Chemical program: residual test before use
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No dialyzer on the machine in the right panel
✗ no contact time in numbers
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Outside: wipe every surface" present and spelled exactly — confirmed
□ Label "Keep wet for the contact time" present and spelled exactly — confirmed
□ Label "Inside: run the disinfection program" present and spelled exactly — confirmed
□ Label "No dialyzer or lines attached" present and spelled exactly — confirmed
□ Label "Chemical program: residual test before use" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 7 — Water Treatment, Concentrates, and Dialysate

### HD-07-D ★ — Total chlorine test, step by step

**File:** `images/hemodialysis-technician-07-chlorine-test-steps.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `chlorinetest`

**Job:** A: performs the total chlorine test correctly and records the result.

**Alt:** Six-step total chlorine test from sampling after the carbon tanks to recording the result.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Total chlorine test, step by step · academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `chlorinetest`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six illustrated steps: water system running, sample taken at the port after the carbon tanks, reagent or strip used as its instructions state, timed wait, color compared with the chart under good light, result recorded with time and initials.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: performs the total chlorine test correctly and records the result.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 System running
  • 2 Sample after the carbon tanks
  • 3 Add reagent or dip strip
  • 4 Wait the stated time
  • 5 Compare with the chart
  • 6 Record result, time, initials
  • Limit: 0.1 mg/L total chlorine
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other numbers
✗ no reagent brand
✗ no sample taken from a sink tap
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 System running" present and spelled exactly — confirmed
□ Label "2 Sample after the carbon tanks" present and spelled exactly — confirmed
□ Label "3 Add reagent or dip strip" present and spelled exactly — confirmed
□ Label "4 Wait the stated time" present and spelled exactly — confirmed
□ Label "5 Compare with the chart" present and spelled exactly — confirmed
□ Label "6 Record result, time, initials" present and spelled exactly — confirmed
□ Label "Limit: 0.1 mg/L total chlorine" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-07-E ○ — Mixing bicarbonate concentrate

**File:** `images/hemodialysis-technician-07-bicarbonate-mixing.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `concentrates`

**Job:** A: mixes bicarbonate concentrate cleanly and labels it.

**Alt:** Five-step sequence for mixing and labeling bicarbonate concentrate.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Mixing bicarbonate concentrate · academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `concentrates`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five steps: clean, disinfected, rinsed container; treated water to the mark; powder added and mixed gently until dissolved; container labeled with date, time, and initials; used within the allowed time, never topped up.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: mixes bicarbonate concentrate cleanly and labels it.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Clean, rinsed container
  • 2 Treated water to the mark
  • 3 Add powder; mix gently
  • 4 Label: date, time, initials
  • 5 Use within the allowed time
  • Never top up an old batch
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No hours or volumes in numbers
✗ no tap water
✗ no vigorous shaking
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Clean, rinsed container" present and spelled exactly — confirmed
□ Label "2 Treated water to the mark" present and spelled exactly — confirmed
□ Label "3 Add powder; mix gently" present and spelled exactly — confirmed
□ Label "4 Label: date, time, initials" present and spelled exactly — confirmed
□ Label "5 Use within the allowed time" present and spelled exactly — confirmed
□ Label "Never top up an old batch" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 8 — Vascular Access Recognition and Protection

### HD-08-D ★ — Holding a needle site

**File:** `images/hemodialysis-technician-08-holding-needle-site.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `needlewatch`

**Job:** A: applies steady two-finger pressure after needle removal without occluding the access.

**Alt:** Two gloved fingertips holding gauze on a fistula needle site, with an inset showing the incorrect whole-hand squeeze.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Holding a needle site · academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `needlewatch`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Close view of a forearm with a fistula after needle removal: gauze under two gloved fingertips, one over the skin puncture and one just beside it along the vessel. A small inset marked incorrect shows a whole hand squeezing the arm. Skin opaque; no blood visible beyond a small spot on the gauze.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: applies steady two-finger pressure after needle removal without occluding the access.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Two fingers, steady pressure
  • Firm enough to stop bleeding
  • You should still feel the thrill
  • Do not peek
  • Hold for the time your unit states
  • Prolonged bleeding: tell the nurse
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No needle in the arm
✗ no tourniquet or clamp
✗ no anatomy through skin
✗ no minutes in numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Two fingers, steady pressure" present and spelled exactly — confirmed
□ Label "Firm enough to stop bleeding" present and spelled exactly — confirmed
□ Label "You should still feel the thrill" present and spelled exactly — confirmed
□ Label "Do not peek" present and spelled exactly — confirmed
□ Label "Hold for the time your unit states" present and spelled exactly — confirmed
□ Label "Prolonged bleeding: tell the nurse" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-08-E ★ — Catheter: look, do not open

**File:** `images/hemodialysis-technician-08-catheter-look.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `cathside`

**Job:** U: checks a dialysis catheter from the outside and leaves opening it to the nurse.

**Alt:** Tunneled dialysis catheter with an intact dressing, closed clamps, and caps, with four points to check.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Catheter: look, do not open · academy/hemodialysis-technician-08-vascular-access-recognition-protection.html, section `cathside`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Upper chest of a clothed adult with a tunneled dialysis catheter: clean dry dressing over the exit site, two limbs each with a closed clamp and a cap. Four callouts point to dressing, clamps, caps, and skin around the dressing. Skin opaque.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: checks a dialysis catheter from the outside and leaves opening it to the nurse.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Dressing clean, dry, intact
  • Both clamps closed
  • Both caps on
  • Skin: no redness or drainage
  • Only the nurse opens the catheter
  • Report anything different
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No open catheter hub
✗ no syringe
✗ no internal vein anatomy
✗ no blood
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Dressing clean, dry, intact" present and spelled exactly — confirmed
□ Label "Both clamps closed" present and spelled exactly — confirmed
□ Label "Both caps on" present and spelled exactly — confirmed
□ Label "Skin: no redness or drainage" present and spelled exactly — confirmed
□ Label "Only the nurse opens the catheter" present and spelled exactly — confirmed
□ Label "Report anything different" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 9 — The Hemodialysis Session

### HD-09-D ★ — Every alarm: patient, lines, screen

**File:** `images/hemodialysis-technician-09-alarm-order.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `alarms`

**Job:** A: responds to any alarm in a fixed order, starting with the patient.

**Alt:** Six-step alarm response that begins with the patient, then the access and lines, then the screen.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Every alarm: patient, lines, screen · academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `alarms`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Six steps as panels. The first shows staff eyes on the patient's face; the second on the access arm and lines; the third on the machine screen. Then a mute symbol, a call to the nurse, and a record sheet.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: responds to any alarm in a fixed order, starting with the patient.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Look at the patient
  • 2 Look at the access and lines
  • 3 Read the alarm
  • 4 Mute; do not reset blindly
  • 5 Call the nurse
  • 6 Record
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No readable screen text
✗ no hand pressing reset in the first three panels
✗ no covered access arm
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Look at the patient" present and spelled exactly — confirmed
□ Label "2 Look at the access and lines" present and spelled exactly — confirmed
□ Label "3 Read the alarm" present and spelled exactly — confirmed
□ Label "4 Mute; do not reset blindly" present and spelled exactly — confirmed
□ Label "5 Call the nurse" present and spelled exactly — confirmed
□ Label "6 Record" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-09-E ★ — Where each alarm sensor sits

**File:** `images/hemodialysis-technician-09-alarm-sensors.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `alarms`

**Job:** U: locates the arterial and venous pressure sensors, air detector and clamp, and blood leak detector on the circuit.

**Alt:** Hemodialysis circuit with the positions of the pressure sensors, air detector and clamp, blood leak detector, and dialysate sensors.

> **Circuit figure.** Do not write a new layout. Generate this prompt with the `dialysis-circuit-schematic` skill (modality: intermittent hemodialysis), which locks the port colors, flow directions, and pressure points. Content to add: Canonical intermittent hemodialysis circuit with sensor positions marked: arterial pressure before the blood pump, venous pressure at the venous chamber, air detector and clamp below the venous chamber, blood leak detector on the used dialysate line, conductivity and temperature on the fresh dialysate line. Labels: Arterial pressure; Venous pressure; Air detector and clamp; Blood leak detector; Conductivity and temperature. Footer: `© renalcarematters.com`.


## Module 10 — Complications and Emergency Response

### HD-10-D ○ — Emergency cart: the daily check

**File:** `images/hemodialysis-technician-10-cart-check.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-10-complications-emergency-response.html, section `cartcheck`

**Job:** A: checks the emergency cart and oxygen at the start of the day and records it.

**Alt:** Emergency cart with oxygen, suction, bag-valve mask, and defibrillator, with a daily checklist.

```text
Reference card · 1672 × 941, 16:9 landscape · Emergency cart: the daily check · academy/hemodialysis-technician-10-complications-emergency-response.html, section `cartcheck`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
A generic emergency cart with drawers closed and a seal, an oxygen cylinder with gauge, suction unit, bag-valve mask, and a defibrillator on top with its indicator showing ready. A checklist clipboard hangs on the side.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: checks the emergency cart and oxygen at the start of the day and records it.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Cart in its place, sealed
  • Oxygen: enough pressure
  • Suction works
  • Bag and masks present
  • Defibrillator ready
  • Medicines: checked by the nurse
  • Sign the checklist
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No readable gauge numbers
✗ no drug names
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Cart in its place, sealed" present and spelled exactly — confirmed
□ Label "Oxygen: enough pressure" present and spelled exactly — confirmed
□ Label "Suction works" present and spelled exactly — confirmed
□ Label "Bag and masks present" present and spelled exactly — confirmed
□ Label "Defibrillator ready" present and spelled exactly — confirmed
□ Label "Medicines: checked by the nurse" present and spelled exactly — confirmed
□ Label "Sign the checklist" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-10-E ★ — The first five minutes

**File:** `images/hemodialysis-technician-10-first-five-minutes.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-10-complications-emergency-response.html, section `firstfive`

**Job:** A: recalls the first actions for power failure, water failure, fire, earthquake, and flood.

**Alt:** Five tiles with the first action for power failure, water failure, fire, earthquake, and flood.

```text
Reference card · 1672 × 941, 16:9 landscape · The first five minutes · academy/hemodialysis-technician-10-complications-emergency-response.html, section `firstfive`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Five tiles, each with a simple illustrated symbol and one line of first action.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: recalls the first actions for power failure, water failure, fire, earthquake, and flood.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Power failure: stay with patients; check battery
  • Water failure: no new starts; tell the nurse
  • Fire: raise the alarm; follow the plan
  • Earthquake: protect, then check patients
  • Flood or typhoon: follow the continuity plan
  • The nurse in charge decides
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No frightening imagery
✗ no specific phone numbers
✗ no times
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Power failure: stay with patients; check battery" present and spelled exactly — confirmed
□ Label "Water failure: no new starts; tell the nurse" present and spelled exactly — confirmed
□ Label "Fire: raise the alarm; follow the plan" present and spelled exactly — confirmed
□ Label "Earthquake: protect, then check patients" present and spelled exactly — confirmed
□ Label "Flood or typhoon: follow the continuity plan" present and spelled exactly — confirmed
□ Label "The nurse in charge decides" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 11 — Dialyzer Reprocessing and Equipment Quality

### HD-11-D ★ — The life of a reprocessed dialyzer

**File:** `images/hemodialysis-technician-11-dialyzer-life-cycle.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `lifecycle`

**Job:** U: follows one dialyzer from first-use labeling to discard.

**Alt:** Loop of eight steps in the life of a reprocessed dialyzer, with an exit to discard.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · The life of a reprocessed dialyzer · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `lifecycle`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Eight steps arranged as a loop with an exit: assign and label, baseline volume, treatment, rinse-back and transport, reprocess, store, pre-use checks, and back to treatment; a side exit labeled discard. One dialyzer with the same fictional label appears throughout.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — U: follows one dialyzer from first-use labeling to discard.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Assign and label
  • 2 Baseline volume
  • 3 Treatment
  • 4 Cap and transport
  • 5 Reprocess
  • 6 Store
  • 7 Pre-use checks
  • Discard when any rule is met
  • One patient only
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No second patient's name
✗ no reuse count limit in numbers
✗ no dialyzer without a label
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Assign and label" present and spelled exactly — confirmed
□ Label "2 Baseline volume" present and spelled exactly — confirmed
□ Label "3 Treatment" present and spelled exactly — confirmed
□ Label "4 Cap and transport" present and spelled exactly — confirmed
□ Label "5 Reprocess" present and spelled exactly — confirmed
□ Label "6 Store" present and spelled exactly — confirmed
□ Label "7 Pre-use checks" present and spelled exactly — confirmed
□ Label "Discard when any rule is met" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-11-E ★ — Total cell volume and the 80 percent rule

**File:** `images/hemodialysis-technician-11-total-cell-volume.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `coresteps`

**Job:** A: calculates percent of original volume and decides pass or discard.

**Alt:** Dialyzer volume measured into a cylinder, and two bars comparing original and current volume against the 80 percent line.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Total cell volume and the 80 percent rule · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `coresteps`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Left: a dialyzer with its fiber fluid being pushed by air into a measuring cylinder read at eye level. Right: two bars, original 115 mL and today 101 mL, with the result 88 percent and a pass mark; a threshold line drawn at 80 percent.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: calculates percent of original volume and decides pass or discard.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Fluid held by the fibers
  • Read at eye level
  • Original: 115 mL
  • Today: 101 mL
  • 101 ÷ 115 = 88 percent: pass
  • Below 80 percent: discard
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No other numbers
✗ no cylinder read from above
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Fluid held by the fibers" present and spelled exactly — confirmed
□ Label "Read at eye level" present and spelled exactly — confirmed
□ Label "Original: 115 mL" present and spelled exactly — confirmed
□ Label "Today: 101 mL" present and spelled exactly — confirmed
□ Label "101 ÷ 115 = 88 percent: pass" present and spelled exactly — confirmed
□ Label "Below 80 percent: discard" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-11-F ○ — Pressure leak test

**File:** `images/hemodialysis-technician-11-leak-test.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `coresteps`

**Job:** U: understands that a held pressure proves the fibers are intact.

**Alt:** Dialyzer on a pressure gauge showing a steady reading for pass and a falling reading with a torn fiber for fail.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Pressure leak test · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `coresteps`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
A dialyzer connected to a pressure source and gauge. Two small panels: gauge needle steady, marked pass; gauge needle falling with bubbles crossing the membrane in a magnified inset of one torn fiber, marked fail and discard.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands that a held pressure proves the fibers are intact.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Apply the stated pressure
  • Watch for the stated time
  • Pressure holds: pass
  • Pressure falls: a fiber is torn
  • Fail = discard
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No pressure or time values
✗ no readable gauge numbers
✗ no blood
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Apply the stated pressure" present and spelled exactly — confirmed
□ Label "Watch for the stated time" present and spelled exactly — confirmed
□ Label "Pressure holds: pass" present and spelled exactly — confirmed
□ Label "Pressure falls: a fiber is torn" present and spelled exactly — confirmed
□ Label "Fail = discard" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-11-G ★ — Three methods: who does which step

**File:** `images/hemodialysis-technician-11-three-methods.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `methods`

**Job:** U: sees which steps a person does in manual, semi-automated, and automated reprocessing.

**Alt:** Grid comparing manual, semi-automated, and automated reprocessing, showing which steps are done by hand and which by machine.

```text
Reference card · 1672 × 941, 16:9 landscape · Three methods: who does which step · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `methods`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
A grid of three columns (manual, semi-automated, automated) and five rows (rinse and clean, volume test, leak test, germicide fill, identity check and label). Each cell holds a small hand icon or a small machine icon. The identity row shows a hand in all three columns.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: sees which steps a person does in manual, semi-automated, and automated reprocessing.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Manual
  • Semi-automated
  • Automated
  • Rinse and clean
  • Volume test
  • Leak test
  • Germicide fill
  • Identity and label
  • Identity is always checked by a person
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No brand of reprocessing machine
✗ no machine icon in the identity row
✗ no numbers
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Manual" present and spelled exactly — confirmed
□ Label "Semi-automated" present and spelled exactly — confirmed
□ Label "Automated" present and spelled exactly — confirmed
□ Label "Rinse and clean" present and spelled exactly — confirmed
□ Label "Volume test" present and spelled exactly — confirmed
□ Label "Leak test" present and spelled exactly — confirmed
□ Label "Germicide fill" present and spelled exactly — confirmed
□ Label "Identity and label" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-11-H ★ — Two strips, two opposite questions

**File:** `images/hemodialysis-technician-11-presence-residual.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `preuse`

**Job:** A: uses the presence test before rinsing and the residual test after, and never confuses them.

**Alt:** Two-panel figure of the germicide presence test before rinsing and the residual test after rinsing.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Two strips, two opposite questions · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `preuse`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two panels in order. First: a stored dialyzer, a sample tested with a strip that changes color, captioned germicide present. Second: after rinsing and priming, a sample tested with a different strip that does not change color, captioned germicide gone. An arrow labeled rinse and prime joins the panels.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: uses the presence test before rinsing and the residual test after, and never confuses them.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Before rinsing: presence test
  • Positive = germicide was there
  • Rinse and prime
  • After rinsing: residual test
  • Negative = germicide is gone
  • Different strips; never swap them
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No strip brand
✗ no color chart values
✗ no patient connected
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Before rinsing: presence test" present and spelled exactly — confirmed
□ Label "Positive = germicide was there" present and spelled exactly — confirmed
□ Label "Rinse and prime" present and spelled exactly — confirmed
□ Label "After rinsing: residual test" present and spelled exactly — confirmed
□ Label "Negative = germicide is gone" present and spelled exactly — confirmed
□ Label "Different strips; never swap them" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-11-I ○ — Reprocessing room: dirty in, clean out

**File:** `images/hemodialysis-technician-11-reprocessing-room.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `room`

**Job:** U: recognizes the one-way flow of a reprocessing room and where safety equipment belongs.

**Alt:** Plan of a reprocessing room with one-way flow from used dialyzers to labeled storage, with eyewash, spill kit, and ventilation.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Reprocessing room: dirty in, clean out · academy/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality.html, section `room`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Overhead plan of a small reprocessing room: used dialyzers entering on one side, rinse and test stations, germicide fill, a storage rack with one labeled slot per patient near the opposite door. Eyewash station, spill kit, exhaust ventilation, and treated water outlet marked. A technician in gown, gloves, and face shield.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: recognizes the one-way flow of a reprocessing room and where safety equipment belongs.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Used dialyzers in
  • Rinse and test
  • Germicide fill
  • Storage: one place per patient
  • Reprocessed dialyzers out
  • Eyewash
  • Spill kit
  • Ventilation
  • Treated water only
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No clean and used dialyzers on the same counter
✗ no technician without eye protection
✗ no brand
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Used dialyzers in" present and spelled exactly — confirmed
□ Label "Rinse and test" present and spelled exactly — confirmed
□ Label "Germicide fill" present and spelled exactly — confirmed
□ Label "Storage: one place per patient" present and spelled exactly — confirmed
□ Label "Reprocessed dialyzers out" present and spelled exactly — confirmed
□ Label "Eyewash" present and spelled exactly — confirmed
□ Label "Spill kit" present and spelled exactly — confirmed
□ Label "Ventilation" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```


## Module 12 — Integrated Practice and Competency Assessment

### HD-12-D ★ — Opening the shift: one walk-through

**File:** `images/hemodialysis-technician-12-opening-walkthrough.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `walkthrough`

**Job:** A: opens a shift in a fixed order that covers water, machines, supplies, and records.

**Alt:** Numbered path through a dialysis unit showing eight opening-shift checks in order.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Opening the shift: one walk-through · academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `walkthrough`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
A path through a simplified unit plan with numbered stops: handoff, water room, chlorine test, concentrates, emergency equipment, machines, stations, records.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: opens a shift in a fixed order that covers water, machines, supplies, and records.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Handoff
  • 2 Water room
  • 3 Chlorine test
  • 4 Concentrates
  • 5 Emergency equipment
  • 6 Machines
  • 7 Stations
  • 8 Records
  • A failed check stops the walk
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No patients in the unit
✗ no readable logs
✗ no times
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Handoff" present and spelled exactly — confirmed
□ Label "2 Water room" present and spelled exactly — confirmed
□ Label "3 Chlorine test" present and spelled exactly — confirmed
□ Label "4 Concentrates" present and spelled exactly — confirmed
□ Label "5 Emergency equipment" present and spelled exactly — confirmed
□ Label "6 Machines" present and spelled exactly — confirmed
□ Label "7 Stations" present and spelled exactly — confirmed
□ Label "8 Records" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

### HD-12-E ○ — Four levels of competence

**File:** `images/hemodialysis-technician-12-four-levels.png` · **Canvas:** 1672 × 941, 16:9 landscape · **Placement:** academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `selfrate`

**Job:** U: rates a skill honestly on four levels.

**Alt:** Four steps from needing supervision to teaching others.

```text
Reference card · 1672 × 941, 16:9 landscape · Four levels of competence · academy/hemodialysis-technician-12-integrated-practice-competency-assessment.html, section `selfrate`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four rising steps, each with a small illustration: a learner beside a preceptor who is doing the task; the learner doing it while the preceptor prompts; the learner alone; the learner teaching a newcomer.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: rates a skill honestly on four levels.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 Needs supervision
  • 2 Performs with prompts
  • 3 Performs independently
  • 4 Can teach others
  • Sign-off is by the preceptor
Attribution footer: `© renalcarematters.com` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy or mirrored equipment
✗ No cartoon style, no flat clip-art icons
✗ No garbled or unreadable text; no text other than the verbatim labels and the footer
✗ No prompt text or production metadata visible in the image
✗ No missing attribution footer — `© renalcarematters.com` appears on the image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864
✗ No anatomy visible through opaque skin
✗ No manufacturer logos, brand names, or recognizable proprietary machine designs
✗ No identifiable real people, patient records, or readable screen values
✗ No dark background
✗ No numbers, limits, doses, or settings other than those written in the label list
✗ No scores or percentages
✗ no medals or trophies
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 Needs supervision" present and spelled exactly — confirmed
□ Label "2 Performs with prompts" present and spelled exactly — confirmed
□ Label "3 Performs independently" present and spelled exactly — confirmed
□ Label "4 Can teach others" present and spelled exactly — confirmed
□ Label "Sign-off is by the preceptor" present and spelled exactly — confirmed
□ Number of panels, steps, or tiles matches the description — confirmed
□ Flow and sequence arrows point the described way — confirmed
□ No numbers other than those in the label list — confirmed
□ No brand names, logos, or readable screens — confirmed
□ Illustrated atlas rendering, not flat vector clip art — confirmed
□ No anatomy visible through skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in the generated image — confirmed
□ Attribution footer present in the bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping content — confirmed
```

# Part 2 — Planned figures not yet produced

Prompts for these are in `GPT-IMAGE-PROMPTS.md` under the same ID. ★ core, ○ optional.

### Flat teaching diagrams waiting to be replaced — 11

These files exist as flat diagrams. Saving the new illustrated figure under the same filename swaps it in with no code change.

| ID | Figure | File | Type |
|---|---|---|---|
| HD-02-A ★ | From blood to urine, and four kidney jobs | `images/hemodialysis-technician-02-kidneys-kidney-failure-teaching-diagram.png` | aid |
| HD-03-A ★ | Five treatment pathways | `images/hemodialysis-technician-03-treatment-options-living-with-kidney-failure-teaching-diagram.png` | aid |
| HD-04-A ★ | Diffusion and ultrafiltration across the membrane | `images/hemodialysis-technician-04-principles-of-hemodialysis-teaching-diagram.png` | aid |
| HD-05-A ★ | Station turnover sequence | `images/hemodialysis-technician-05-infection-prevention-waste-management-teaching-diagram.png` | flow |
| HD-06-A ★ | Two circuits that meet at the dialyzer | `images/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit-teaching-diagram.png` | circuit |
| HD-07-A ★ | From tap to station | `images/hemodialysis-technician-07-water-treatment-concentrates-dialysate-teaching-diagram.png` | aid |
| HD-08-A ★ | Three types of hemodialysis access | `images/hemodialysis-technician-08-vascular-access-recognition-protection-teaching-diagram.png` | aid |
| HD-09-A ★ | One session, three phases | `images/hemodialysis-technician-09-the-hemodialysis-session-teaching-diagram.png` | flow |
| HD-10-A ★ | Your first thirty seconds | `images/hemodialysis-technician-10-complications-emergency-response-teaching-diagram.png` | flow |
| HD-11-A ★ | Traceability: release or hold | `images/hemodialysis-technician-11-dialyzer-reprocessing-equipment-quality-teaching-diagram.png` | flow |
| HD-12-A ★ | Five practical stations | `images/hemodialysis-technician-12-integrated-practice-competency-assessment-teaching-diagram.png` | aid |
