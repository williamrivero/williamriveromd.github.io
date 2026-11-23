# GPT image prompts — corrections after the visual accuracy audit

**Site:** renalcarematters.com · **Prepared:** November 23, 2026 · **Scope:** the 135 technician-track figures and heroes already published

## Audit result

All 135 images were checked against their specifications for technical and clinical accuracy, required labels, scope of practice, rendering defects, and American English.

| Result | Count |
|---|---|
| Heroes (26): accurate, no change needed | 26 |
| Figures accurate as published | 58 |
| Figures with a minor, cosmetic issue (publishable; optional edit below) | 37 |
| Figures to regenerate before relying on them (full prompts below) | 14 |

Arithmetic in every worked example and every water-quality limit shown was correct. No figure shows a technician cannulating, connecting, or medicating a patient, and none carries a brand logo or readable patient data.

## How to use this file

1. **Part 1** (must fix): paste each gray block into a fresh ChatGPT image chat. Check the labels against the list, then save the PNG under the **same filename** as the published image, in `~/Documents/HD Technicians/Module images`. It replaces the old figure on the site with no code change.
2. **Part 2** (optional polish): open the published image in ChatGPT and paste the one-line edit request, or regenerate from the original prompt in `GPT-IMAGE-PROMPTS.md` with the edit added.
3. When the replacements are in the folder, ask for them to be processed and pushed.

# Part 1 — Regenerate (14)

| # | ID | Figure | File |
|---|---|---|---|
| 1 | HD-05-C | Sorting waste at the point of use | `images/hemodialysis-technician-05-waste-sorting.png` |
| 2 | HD-07-A | From tap to station | `images/hemodialysis-technician-07-water-treatment-concentrates-dialysate-teaching-diagram.png` |
| 3 | HD-09-B | What to look at on every round | `images/hemodialysis-technician-09-every-round.png` |
| 4 | WATER-02-B | Reading the system drawing | `images/water-treatment-technician-02-system-drawing.png` |
| 5 | WATER-04-A | Worker and polisher | `images/water-treatment-technician-04-worker-polisher.png` |
| 6 | WATER-04-C | Acting on the chlorine result | `images/water-treatment-technician-04-chlorine-decision.png` |
| 7 | WATER-08-B | A log that can be trusted | `images/water-treatment-technician-08-good-log.png` |
| 8 | WATER-09-B | Where to sample | `images/water-treatment-technician-09-sample-points.png` |
| 9 | WATER-11-A | The maintenance calendar | `images/water-treatment-technician-11-maintenance-calendar.png` |
| 10 | BIOMED-04-A | Mixing and checking dialysate | `images/dialysis-biomedical-technician-04-proportioning.png` |
| 11 | BIOMED-04-C | The total, not the recipe | `images/dialysis-biomedical-technician-04-total-not-recipe.png` |
| 12 | BIOMED-05-C | Checking ultrafiltration accuracy | `images/dialysis-biomedical-technician-05-uf-check.png` |
| 13 | BIOMED-08-B | A staggered year | `images/dialysis-biomedical-technician-08-staggered-year.png` |
| 14 | BIOMED-12-B | One machine or several | `images/dialysis-biomedical-technician-12-shared-causes.png` |

### HD-05-C — Sorting waste at the point of use

**Save as:** `images/hemodialysis-technician-05-waste-sorting.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The bins are drawn yellow for sharps and red for infectious waste. Philippine Department of Health coding uses yellow for infectious waste and red for sharps, so the picture teaches the reverse of local practice.

**Alt:** Three waste containers for sharps, infectious waste, and general waste with examples of each.

```text
Reference card · 1672 × 941, 16:9 landscape · Sorting waste at the point of use · academy/hemodialysis-technician-05-infection-prevention-waste-management.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Three containers drawn in NEUTRAL light gray, each with a blank colored tab left white so that no color code is asserted: a rigid puncture-resistant sharps container with a narrow opening (needles), a lidded infectious waste bin (blood-contaminated gauze, used bloodlines and dialyzers), and a lidded general waste bin (clean packaging). A gloved technician drops a used bloodline into the infectious bin. A small no-recapping symbol.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: places each item in the right container at the moment it becomes waste.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Sharps container: needles
  • Infectious waste: blood-contaminated items
  • General waste: clean packaging
  • Follow your facility's color code
  • Never recap needles
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
✗ No yellow, red, black, or green bins or bags
✗ No color named or implied as the code
✗ No hands near an open sharps opening
✗ No overfilled container
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Sharps container: needles" present and spelled exactly — confirmed
□ Label "Infectious waste: blood-contaminated items" present and spelled exactly — confirmed
□ Label "General waste: clean packaging" present and spelled exactly — confirmed
□ Label "Follow your facility's color code" present and spelled exactly — confirmed
□ Label "Never recap needles" present and spelled exactly — confirmed
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

### HD-07-A — From tap to station

**Save as:** `images/hemodialysis-technician-07-water-treatment-concentrates-dialysate-teaching-diagram.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The distribution loop is a closed ring that never returns to the reverse osmosis unit, and the station is fed from the riser rather than from a drop off the loop.

**Alt:** Water treatment train from feed water through filter, softener, two carbon tanks, and reverse osmosis to the distribution loop and station.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · From tap to station · academy/hemodialysis-technician-07-water-treatment-concentrates-dialysate.html, section `part1`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Left-to-right train on one wall: feed water, sediment filter (particles), softener (hardness), carbon tank 1 then carbon tank 2 in series with a sample port after each, reverse osmosis unit with a reject line to drain. From the reverse osmosis product outlet a single distribution loop runs out along the ceiling, passes ABOVE the dialysis station where a short drop feeds the machine, and continues back to the reverse osmosis unit, ending in a clear return arrow at the reverse osmosis inlet. Arrows show one direction of flow throughout.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: traces water through pretreatment, carbon, and reverse osmosis to the loop and names what each stage removes.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Feed water
  • Sediment filter: particles
  • Softener: hardness
  • Carbon tank 1 (worker)
  • Carbon tank 2 (polisher)
  • Sample port
  • Reverse osmosis
  • Reject to drain
  • Distribution loop
  • Dialysis station
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
✗ No single carbon tank
✗ No loop that dead-ends or forms a closed ring disconnected from the reverse osmosis unit
✗ No station fed from anywhere but a short drop off the loop
✗ No numeric limits
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Feed water" present and spelled exactly — confirmed
□ Label "Sediment filter: particles" present and spelled exactly — confirmed
□ Label "Softener: hardness" present and spelled exactly — confirmed
□ Label "Carbon tank 1 (worker)" present and spelled exactly — confirmed
□ Label "Carbon tank 2 (polisher)" present and spelled exactly — confirmed
□ Label "Sample port" present and spelled exactly — confirmed
□ Label "Reverse osmosis" present and spelled exactly — confirmed
□ Label "Reject to drain" present and spelled exactly — confirmed
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

### HD-09-B — What to look at on every round

**Save as:** `images/hemodialysis-technician-09-every-round.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The bloodlines run from the arm straight into the machine body with no blood pump or dialyzer, and the observer wears the nurse's purple scrubs.

**Alt:** Patient in a dialysis chair with five numbered things to check on each round.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · What to look at on every round · academy/hemodialysis-technician-09-the-hemodialysis-session.html, section `part3`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Patient seated in a dialysis chair, access arm uncovered and resting in view, two needles taped in place. Bloodlines run from the arm to the machine front, through the roller blood pump, up to a vertically mounted dialyzer on the side of the machine, and back through the venous drip chamber to the arm (arterial line red, venous line blue). A technician in NAVY scrubs with a clipboard observes. Five numbered callouts: the patient, the access, the lines, the machine, the record. Screen values indistinct.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: checks patient, access, lines, machine, and record on each round.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • 1 The patient
  • 2 The access: visible and dry
  • 3 The lines: no kinks
  • 4 The machine
  • 5 The record: real numbers, at the time
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
✗ No blanket covering the access
✗ No bloodlines entering the machine body without passing the blood pump and dialyzer
✗ No purple scrubs on the technician
✗ No readable numbers on the screen
✗ No needle close-up
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "1 The patient" present and spelled exactly — confirmed
□ Label "2 The access: visible and dry" present and spelled exactly — confirmed
□ Label "3 The lines: no kinks" present and spelled exactly — confirmed
□ Label "4 The machine" present and spelled exactly — confirmed
□ Label "5 The record: real numbers, at the time" present and spelled exactly — confirmed
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

### WATER-02-B — Reading the system drawing

**Save as:** `images/water-treatment-technician-02-system-drawing.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The drawing is a closed ring with no water source or treatment equipment, so the loop returns to nothing.

**Alt:** Simplified piping drawing of a dialysis water system with a symbol legend.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Reading the system drawing · academy/water-treatment-technician-02-source-water-system-design.html, section `drawing`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Clean engineering-style schematic on white, flow left to right: an inlet labeled by its symbol from a reverse osmosis unit (drawn as a simple box) feeds a pump, then a valve, a pressure gauge, and a sample port on the outgoing pipe; the loop runs right, turns, and comes back along the bottom as the loop return into the reverse osmosis box; a branch with an air gap leads down to a floor drain. A legend panel at top left explains each symbol.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: follows a simplified piping drawing and finds valves, gauges, and sample ports.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Legend
  • Valve
  • Pressure gauge
  • Sample port
  • Pump
  • Flow direction
  • Loop return
  • Drain
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
✗ No closed ring without a source
✗ No manufacturer title block
✗ No dimensions
✗ No dead-end branches
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Legend" present and spelled exactly — confirmed
□ Label "Valve" present and spelled exactly — confirmed
□ Label "Pressure gauge" present and spelled exactly — confirmed
□ Label "Sample port" present and spelled exactly — confirmed
□ Label "Pump" present and spelled exactly — confirmed
□ Label "Flow direction" present and spelled exactly — confirmed
□ Label "Loop return" present and spelled exactly — confirmed
□ Label "Drain" present and spelled exactly — confirmed
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

### WATER-04-A — Worker and polisher

**Save as:** `images/water-treatment-technician-04-worker-polisher.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The required label 'Chlorine-free water out' is missing, an invented label replaces it, and the chlorine dots that show removal are not drawn.

**Alt:** Two carbon tanks in series with a sample port after each.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Worker and polisher · academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `carbon`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two carbon tank cutaways in series, flow left to right. Many small green chlorine dots in the inlet pipe, a few dots between the tanks, none in the outlet pipe. Sample port 1 between the tanks, sample port 2 after tank 2.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: understands two tanks in series and where each sample port is.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Carbon tank 1: the worker
  • Carbon tank 2: the polisher
  • Sample port 1
  • Sample port 2
  • Chlorine and chloramine in
  • Chlorine-free water out
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
✗ No single-tank layout
✗ No parallel arrangement
✗ No label other than the verbatim list
✗ No numeric limits
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Carbon tank 1: the worker" present and spelled exactly — confirmed
□ Label "Carbon tank 2: the polisher" present and spelled exactly — confirmed
□ Label "Sample port 1" present and spelled exactly — confirmed
□ Label "Sample port 2" present and spelled exactly — confirmed
□ Label "Chlorine and chloramine in" present and spelled exactly — confirmed
□ Label "Chlorine-free water out" present and spelled exactly — confirmed
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

### WATER-04-C — Acting on the chlorine result

**Save as:** `images/water-treatment-technician-04-chlorine-decision.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** All four outcome labels differ from the plan, a reading at the limit is shown as a fail, and the tank 2 failure says HOLD rather than STOP.

**Alt:** Decision tree for total chlorine results after each carbon tank.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Acting on the chlorine result · academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `chlorine-test`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Decision tree, top to bottom, large readable type filling the canvas. Top box: test after tank 1. Two branches. Left (green): at or below the limit, record and release. Right (amber): above the limit, test after tank 2 now. From the amber box two branches: tank 2 within limit (amber), report, replace the worker, test more often; tank 2 above limit (red), STOP and report, no treatments start or continue.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: takes the correct action for each total chlorine result.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Test after tank 1
  • At or below the limit: record and release
  • Above the limit: test after tank 2 now
  • Tank 2 within limit: report, replace the worker, test more often
  • Tank 2 above limit: STOP and report
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
✗ No numeric limit printed
✗ No wording other than the verbatim labels
✗ No path that continues treatment after a tank 2 failure
✗ No small text
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Test after tank 1" present and spelled exactly — confirmed
□ Label "At or below the limit: record and release" present and spelled exactly — confirmed
□ Label "Above the limit: test after tank 2 now" present and spelled exactly — confirmed
□ Label "Tank 2 within limit: report, replace the worker, test more often" present and spelled exactly — confirmed
□ Label "Tank 2 above limit: STOP and report" present and spelled exactly — confirmed
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

### WATER-08-B — A log that can be trusted

**Save as:** `images/water-treatment-technician-08-good-log.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The two good-log rows give the same port and time, so one reading is recorded as both 60 psi and 'instrument unavailable'; the corrected value also reads '60 TA'.

**Alt:** Comparison of a weak water log entry with a complete one.

```text
Reference card · 1672 × 941, 16:9 landscape · A log that can be trusted · academy/water-treatment-technician-08-daily-monitoring-logs-trends.html, section `records`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Left: a weak log row with ticks, 'OK', and a blank cell, crossed out in amber. Right: two strong log rows. Row 1: 60, psi, filter inlet, 07:00, Tech A, with an earlier value struck through by one line and initialed. Row 2: instrument unavailable, N/A, filter outlet, 07:05, Tech A.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — A: writes entries with numbers, units, times, and names.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Ticks and OK: not evidence
  • Number, unit, port, time, name
  • Correct with one line and initials
  • No blanks: write why
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
✗ No real names
✗ No two rows with the same port and time
✗ No stray letters after a number
✗ No illegible handwriting
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Ticks and OK: not evidence" present and spelled exactly — confirmed
□ Label "Number, unit, port, time, name" present and spelled exactly — confirmed
□ Label "Correct with one line and initials" present and spelled exactly — confirmed
□ Label "No blanks: write why" present and spelled exactly — confirmed
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

### WATER-09-B — Where to sample

**Save as:** `images/water-treatment-technician-09-sample-points.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** Two required labels are missing, an invented banner replaces them, and the loop is not connected to the reverse osmosis unit or tank.

**Alt:** System outline marking the usual microbiological sample points.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Where to sample · academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `points`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
System outline: reverse osmosis unit and storage tank at left; the loop leaves the reverse osmosis unit, passes three dialysis machines, and returns to the reverse osmosis unit or tank. Map pins: loop start (just after reverse osmosis), loop return (last pipe before re-entry, pin drawn larger), tank outlet, and machines in rotation. A banner: sample before disinfection, not after.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: knows the usual sample points and why the loop return matters most.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Loop start
  • Loop return: usually highest
  • Tank outlet
  • Machines in rotation
  • Sample before disinfection, not after
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
✗ No frequency numbers
✗ No loop drawn as a closed ring without a source
✗ No text other than the verbatim labels
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Loop start" present and spelled exactly — confirmed
□ Label "Loop return: usually highest" present and spelled exactly — confirmed
□ Label "Tank outlet" present and spelled exactly — confirmed
□ Label "Machines in rotation" present and spelled exactly — confirmed
□ Label "Sample before disinfection, not after" present and spelled exactly — confirmed
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

### WATER-11-A — The maintenance calendar

**Save as:** `images/water-treatment-technician-11-maintenance-calendar.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The planner grid is empty, so the figure teaches no schedule.

**Alt:** Planner showing recurring maintenance tasks by interval.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · The maintenance calendar · academy/water-treatment-technician-11-maintenance-replacement-validation.html, section `schedule`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Wall-planner graphic: six component rows (filters, softener, carbon, reverse osmosis, loop disinfection, lamps and ultrafilters) and four columns (daily, weekly, monthly, yearly). Each row has generic check markers in the columns where routine work typically falls: filters daily and monthly; softener daily and monthly; carbon daily and yearly; reverse osmosis daily and monthly; loop disinfection monthly; lamps and ultrafilters yearly. A technician holds a clipboard beside it.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees maintenance as recurring tasks at different intervals.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Daily
  • Weekly
  • Monthly
  • Yearly
  • Filters
  • Softener
  • Carbon
  • Reverse osmosis
  • Loop disinfection
  • Lamps and ultrafilters
  • Follow the manufacturer's intervals
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
✗ No dates
✗ No numbers in cells
✗ No empty grid
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Daily" present and spelled exactly — confirmed
□ Label "Weekly" present and spelled exactly — confirmed
□ Label "Monthly" present and spelled exactly — confirmed
□ Label "Yearly" present and spelled exactly — confirmed
□ Label "Filters" present and spelled exactly — confirmed
□ Label "Softener" present and spelled exactly — confirmed
□ Label "Carbon" present and spelled exactly — confirmed
□ Label "Reverse osmosis" present and spelled exactly — confirmed
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

### BIOMED-04-A — Mixing and checking dialysate

**Save as:** `images/dialysis-biomedical-technician-04-proportioning.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The dialyzer has red caps at both ends, and dialysate enters at the top and leaves at the bottom, which is co-current with blood entering at the top.

**Alt:** Schematic of proportioning with control and protective conductivity cells.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Mixing and checking dialysate · academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `mix`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Generic, unbranded hemodialysis machine shown in cutaway. Treated water enters; acid pump and bicarbonate pump add concentrate; mixing chamber; control conductivity cell; independent protective conductivity cell; then the dialysate line goes to the dialyzer. The dialyzer is vertical with a red cap at the top (blood in) and a blue cap at the bottom (blood out); fresh dialysate enters the LOWER side port and used dialysate leaves the UPPER side port, so dialysate flows upward against the downward blood flow.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: follows three streams to a checked mix.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Treated water
  • Acid pump
  • Bicarbonate pump
  • Mixing
  • Control conductivity cell
  • Protective conductivity cell
  • To dialyzer
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
✗ No ratios
✗ No millisiemens values
✗ No brand
✗ No dialysate entering the top side port
✗ No red caps on both ends
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Treated water" present and spelled exactly — confirmed
□ Label "Acid pump" present and spelled exactly — confirmed
□ Label "Bicarbonate pump" present and spelled exactly — confirmed
□ Label "Mixing" present and spelled exactly — confirmed
□ Label "Control conductivity cell" present and spelled exactly — confirmed
□ Label "Protective conductivity cell" present and spelled exactly — confirmed
□ Label "To dialyzer" present and spelled exactly — confirmed
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

### BIOMED-04-C — The total, not the recipe

**Save as:** `images/dialysis-biomedical-technician-04-total-not-recipe.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The core label reads 'Conductivity reflects dissolved ions' instead of 'Conductivity = total salts', and the two meters show no matching value.

**Alt:** Two different concentrates producing the same conductivity reading.

```text
Reference card · 1672 × 941, 16:9 landscape · The total, not the recipe · academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `mix`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Two concentrate containers with clearly different labels (different recipes) each feeding a small beaker; two identical handheld conductivity meters show the SAME generic reading drawn as three identical bars or an identical icon, not digits. A caption tile states the point. Below: a technician reading a container label, and a reference meter checked against the machine sensor.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A compact reference card with a few illustrated tiles. Large, legible type; generous spacing.
Learning purpose — U: understands the limit of conductivity.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Different recipes
  • Same reading
  • Conductivity = total salts
  • Read the label
  • Verify the sensor against a reference meter
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
✗ No formulas or numbers on labels or meter screens
✗ No label other than the verbatim list
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Different recipes" present and spelled exactly — confirmed
□ Label "Same reading" present and spelled exactly — confirmed
□ Label "Conductivity = total salts" present and spelled exactly — confirmed
□ Label "Read the label" present and spelled exactly — confirmed
□ Label "Verify the sensor against a reference meter" present and spelled exactly — confirmed
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

### BIOMED-05-C — Checking ultrafiltration accuracy

**Save as:** `images/dialysis-biomedical-technician-05-uf-check.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The device is a benchtop box, and the cylinder is filled from a standalone tap instead of the machine's ultrafiltration or drain outlet.

**Alt:** Four steps of a volumetric ultrafiltration accuracy check.

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Checking ultrafiltration accuracy · academy/dialysis-biomedical-technician-05-fluid-balance-ultrafiltration.html, section `balance`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Four or five steps with the same generic, unbranded hemodialysis machine in each: technician sets up following a manual; the machine's ultrafiltration or drain line empties into a glass measuring cylinder on a level surface; the technician compares the cylinder volume with the machine display; out of tolerance, she adjusts and repeats; she records as found and as left.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order.
Learning purpose — A: outlines the volumetric check.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Set up by the manual
  • Collect in a measuring cylinder
  • Compare with the display
  • Outside tolerance: correct and repeat
  • Record as found and as left
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
✗ No tolerance figures
✗ No benchtop box in place of a dialysis machine
✗ No water tap filling the cylinder
✗ No readable screen values
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Set up by the manual" present and spelled exactly — confirmed
□ Label "Collect in a measuring cylinder" present and spelled exactly — confirmed
□ Label "Compare with the display" present and spelled exactly — confirmed
□ Label "Outside tolerance: correct and repeat" present and spelled exactly — confirmed
□ Label "Record as found and as left" present and spelled exactly — confirmed
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

### BIOMED-08-B — A staggered year

**Save as:** `images/dialysis-biomedical-technician-08-staggered-year.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The two visits per machine are not evenly spread (gaps vary from four to eight months), and one month has no visits at all.

**Alt:** Year grid showing staggered maintenance visits for twelve machines.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · A staggered year · academy/dialysis-biomedical-technician-08-preventive-maintenance-program.html, section `program`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Twelve-month grid (columns 1 to 12) for twelve generic machines (rows). Each machine has exactly two visits exactly six months apart, and the first visits are staggered one machine per month: machine 1 in months 1 and 7, machine 2 in months 2 and 8, through machine 6 in months 6 and 12, then machine 7 in months 1 and 7 again, continuing so every month has exactly two visits. Completed visits shown with a green check, upcoming ones with a purple calendar icon, and one overdue visit with a red exclamation mark.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — U: sees visits spread so few machines are out at once.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Machines 1 to 12
  • Months
  • Scheduled visit
  • Done
  • Overdue: report it
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
✗ No calendar year
✗ No dates
✗ No machine with gaps other than six months
✗ No month without a visit
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Machines 1 to 12" present and spelled exactly — confirmed
□ Label "Months" present and spelled exactly — confirmed
□ Label "Scheduled visit" present and spelled exactly — confirmed
□ Label "Done" present and spelled exactly — confirmed
□ Label "Overdue: report it" present and spelled exactly — confirmed
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

### BIOMED-12-B — One machine or several

**Save as:** `images/dialysis-biomedical-technician-12-shared-causes.png` (replaces the published image) · **Canvas:** 1672 × 941, 16:9 landscape

**Why it is being redone:** The highlighted concentrate branch feeding the alarming machines starts from an open pipe end and is not connected to the shared concentrate main.

**Alt:** Several machines alarming on one shared concentrate line.

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · One machine or several · academy/dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone.html, section `method`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Row of six generic machines fed from above by three continuous horizontal mains: shared water (blue), shared concentrate (orange), shared power (gray conduit). Each machine has a drop from each main. A tee on the concentrate main feeds a highlighted orange sub-branch that serves machines 4, 5, and 6, which show red alarm lights. A technician looks along the lines.
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
1672 × 941, 16:9 landscape. Reading order left to right, top to bottom. White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art.
Learning purpose — A: looks for a shared cause when several machines alarm.
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
  • Shared water
  • Shared concentrate
  • Shared power
  • Several alarms at once: check what they share
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
✗ No pipe that starts or ends in mid-air
✗ No sensor replacement shown
✗ No label spelled differently from the verbatim list
✗ No extra panels, steps, or tiles beyond those described
✗ No arrows pointing against the described direction of flow or sequence
✗ No crowded layout: every label has clear space around it

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `© renalcarematters.com`, bottom right, small, navy, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Label "Shared water" present and spelled exactly — confirmed
□ Label "Shared concentrate" present and spelled exactly — confirmed
□ Label "Shared power" present and spelled exactly — confirmed
□ Label "Several alarms at once: check what they share" present and spelled exactly — confirmed
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

# Part 2 — Optional edits (37)

| ID | File | Edit request |
|---|---|---|
| HD-01-A | `images/hemodialysis-technician-01-unit-map.png` | Start the red used-item route at the treatment stations and end it at a labeled waste holding room, with its label on the red line. |
| HD-02-A | `images/hemodialysis-technician-02-kidneys-kidney-failure-teaching-diagram.png` | End the nephron at the urine label and remove the bladder, or move it into a small separate inset. |
| HD-02-C | `images/hemodialysis-technician-02-weight-trend.png` | Have the technician report to the dialysis nurse in purple scrubs, not to a physician in a white coat. |
| HD-03-A | `images/hemodialysis-technician-03-treatment-options-living-with-kidney-failure-teaching-diagram.png` | Show a dialyzer and bloodlines connected on both hemodialysis panels. |
| HD-03-C | `images/hemodialysis-technician-03-home-equipment.png` | Place the peritoneal dialysis drain bag on the floor, clearly below the patient's abdomen. |
| HD-05-A | `images/hemodialysis-technician-05-infection-prevention-waste-management-teaching-diagram.png` | Show a running countdown instead of a pause icon in step 4, and wipe the machine as well as the chair in step 3. |
| HD-06-A | `images/hemodialysis-technician-06-machines-dialyzers-extracorporeal-circuit-teaching-diagram.png` | Make the diffusion arrows run only from the fibers into the surrounding dialysate. |
| HD-07-B | `images/hemodialysis-technician-07-which-test.png` | Change the conductivity question to 'Is the reverse osmosis membrane separating salts?' |
| HD-07-C | `images/hemodialysis-technician-07-making-dialysate.png` | End the bypass line at a floor drain with an air gap, not a faucet over a sink. |
| HD-08-A | `images/hemodialysis-technician-08-vascular-access-recognition-protection-teaching-diagram.png` | Add a closed clamp on each catheter limb. |
| HD-09-A | `images/hemodialysis-technician-09-the-hemodialysis-session-teaching-diagram.png` | Add the caption 'Evaluate completion and stability' to the nurse's after-treatment panel. |
| HD-09-C | `images/hemodialysis-technician-09-unexpected-weight.png` | Put the bag or wheelchair on the scale in 'Anything extra?', and show the patient hands-free on the repeat weight. |
| HD-10-B | `images/hemodialysis-technician-10-red-flags.png` | Draw the collapse tile as slumped and unresponsive, not calmly asleep. |
| HD-10-C | `images/hemodialysis-technician-10-utility-failure.png` | Make the last tile a sign-off or all-clear handover so it differs from step 3. |
| HD-12-A | `images/hemodialysis-technician-12-integrated-practice-competency-assessment-teaching-diagram.png` | Add one assessor with a checklist in a different uniform at a station. |
| HD-12-B | `images/hemodialysis-technician-12-six-habits.png` | Close the steps into a loop and give 'Release: designated person only' its own color. |
| HD-12-C | `images/hemodialysis-technician-12-three-levels.png` | Re-render the header so the word 'competent' has no smudge. |
| WATER-01-B | `images/water-treatment-technician-01-contaminant-groups.png` | Rename the third column 'Living contaminants' and caption which barrier serves each column. |
| WATER-03-C | `images/water-treatment-technician-03-brine-tank.png` | Show the two brine tanks as separate side-by-side cutaways, not both plumbed to one softener. |
| WATER-05-C | `images/water-treatment-technician-05-ro-trends.png` | Caption the 'Flow falling' photo as the prefilter, or show a fouled membrane instead. |
| WATER-06-A | `images/water-treatment-technician-06-loop-layout.png` | Move 'Sample port: return' to the last pipe before the loop re-enters the reverse osmosis unit. |
| WATER-06-B | `images/water-treatment-technician-06-dead-legs.png` | Make the capped dead-leg branch clearly long and the correct branch clearly short. |
| WATER-07-C | `images/water-treatment-technician-07-central-delivery.png` | Attach a hose to the red connector in the technician's hand. |
| WATER-09-C | `images/water-treatment-technician-09-action-level.png` | Use the lesson wording: 'Above: hold and report', 'Between: act now', 'Below: continue'. |
| WATER-10-B | `images/water-treatment-technician-10-disinfection-cycle.png` | Remove the flow arrows from the Dwell panel and add a timer icon. |
| WATER-11-C | `images/water-treatment-technician-11-service-handover.png` | Re-lay out the steps to fill the canvas with larger text. |
| WATER-12-B | `images/water-treatment-technician-12-four-failures.png` | Show dark carbon tanks and the sample taken after tank 2 in the chlorine breakthrough tile. |
| BIOMED-02-B | `images/dialysis-biomedical-technician-02-power-path.png` | Add a small legend: 'Colors show role, not your local wiring code.' |
| BIOMED-02-C | `images/dialysis-biomedical-technician-02-multimeter.png` | Show one-hand probing with the other probe clipped in the 'Test on a known source' panel. |
| BIOMED-03-A | `images/dialysis-biomedical-technician-03-inlet-heat-degas.png` | End the heat exchanger's orange pipes at a labeled 'used dialysate to drain' stub. |
| BIOMED-04-B | `images/dialysis-biomedical-technician-04-bypass.png` | Supply dialysate from inside the machine and send it to a closed drain line, not an open reservoir and beaker. |
| BIOMED-05-A | `images/dialysis-biomedical-technician-05-balancing-chamber.png` | Replace the arrows through the membrane with a membrane-displacement cue. |
| BIOMED-05-B | `images/dialysis-biomedical-technician-05-silent-errors.png` | Draw the ultrafiltration pump as a generic pump body, not a fan. |
| BIOMED-06-C | `images/dialysis-biomedical-technician-06-pressures.png` | Optional: use the lesson's verbatim label wording. |
| BIOMED-07-B | `images/dialysis-biomedical-technician-07-blood-leak-detector.png` | Route the used dialysate line to the detector from the dialyzer's upper outlet consistently, and remove the orphan line. |
| BIOMED-11-A | `images/dialysis-biomedical-technician-11-earth-path.png` | Draw Philippine-style grounded outlets (Type B), not UK sockets, and show the fuse visibly open. |
| BIOMED-11-C | `images/dialysis-biomedical-technician-11-station-utilities.png` | Add a small 'Outlet grounding verified' tag at the grounded outlet. |
