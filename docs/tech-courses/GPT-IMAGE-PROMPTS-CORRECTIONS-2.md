# GPT image prompts — corrections, round 2

**Site:** renalcarematters.com · **Prepared:** November 23, 2026 · **Source:** `~/Documents/HD Technicians/Corrected images` (14 regenerated figures)

## Audit of the corrected images

| ID | Result | Finding |
|---|---|---|
| HD-05-C | Pass | Neutral gray bins, no color code asserted; labels verbatim. |
| HD-07-A | Pass | Correct train order; station fed from a drop off the loop; loop returns to the reverse osmosis outlet junction. |
| HD-09-B | Pass | Technician in navy; access and lines uncovered; lines leave the frame, so no impossible equipment. The machine appears as a separate screen inset. |
| WATER-02-B | Pass | Reverse osmosis unit feeds the loop; pump, valve, gauge, and sample port in order; drain with an air gap; loop returns to the source. |
| WATER-04-A | Pass (note) | Chlorine dots now dense, sparse, then none. The label 'Chlorine-free water out' is still replaced by 'Test total chlorine at the outlet', which is accurate. |
| WATER-04-C | Fail | Labels were rephrased again: 'action point' instead of 'limit', a reading exactly at the limit counts as a fail (the lesson passes it), and 'replace the worker, test more often' is missing. |
| WATER-08-B | Pass | Rows now differ by port and time; the correction reads as 62 struck through, initialed TA, corrected to 60. |
| WATER-09-B | Fail | Loop now connects to the reverse osmosis unit, but 'Loop return: usually highest' and 'Sample before disinfection, not after' are still missing, and an invented banner appears again. |
| WATER-11-A | Pass | Planner now carries markers in the expected columns. |
| BIOMED-04-A | Pass | Red cap at the top and blue at the bottom; dialysate enters the lower port and leaves the upper port (countercurrent). |
| BIOMED-04-C | Fail | The key label still reads 'Conductivity reflects dissolved ions' instead of 'Conductivity = total salts'. |
| BIOMED-05-C | Pass | Generic dialysis machine; the cylinder fills from the machine's outlet line. |
| BIOMED-08-B | Pass | Every machine has two visits six months apart; each month has two visits; one overdue mark. |
| BIOMED-12-B | Pass | Highlighted branch now tees off the shared concentrate main. |

**11 passed and are published. 3 failed again**, each because the generator reworded a required label. The failed images were still published, because each is better than the version it replaced, but they should be regenerated. The prompts below add a wording lock and spell out each box's text.

## Regenerate (3)

| # | ID | Figure | Save as |
|---|---|---|---|
| 1 | WATER-04-C | Acting on the chlorine result | `water-treatment-technician-04-chlorine-decision.png` |
| 2 | WATER-09-B | Where to sample | `water-treatment-technician-09-sample-points.png` |
| 3 | BIOMED-04-C | The total, not the recipe | `dialysis-biomedical-technician-04-total-not-recipe.png` |

Save each new PNG (with its WebP) into `~/Documents/HD Technicians/Corrected images` under the same filename, then ask for the folder to be processed and pushed.

### WATER-04-C — Acting on the chlorine result

**Save as:** `water-treatment-technician-04-chlorine-decision.png` · **Canvas:** 1672 × 941, 16:9 landscape

**Why it failed again:** Labels were rephrased again: 'action point' instead of 'limit', a reading exactly at the limit counts as a fail (the lesson passes it), and 'replace the worker, test more often' is missing.

**Tip:** after generating, compare every word with the label list. If one label is reworded, reply in the same chat: *Change the text "…" to exactly "…" and change nothing else.*

```text
Process or decision figure · 1672 × 941, 16:9 landscape · Acting on the chlorine result · academy/water-treatment-technician-04-carbon-tanks-chlorine-control.html, section `chlorine-test`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
WORDING LOCK: every text element in the image must be copied character for character from the label list below. Do not paraphrase, shorten, translate, or 'improve' any label. Do not add any title, banner, caption, or sentence that is not in the list. If a label does not fit, make the box larger, not the wording different.
The four outcome boxes carry exactly these words and no others: 'At or below the limit: record and release' (green); 'Above the limit: test after tank 2 now' (amber); 'Tank 2 within limit: report, replace the worker, test more often' (amber); 'Tank 2 above limit: STOP and report' (red). Never use the words 'action point', 'protocol', or 'procedure'.
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
✗ No reworded label
✗ No invented banner or caption
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

### WATER-09-B — Where to sample

**Save as:** `water-treatment-technician-09-sample-points.png` · **Canvas:** 1672 × 941, 16:9 landscape

**Why it failed again:** Loop now connects to the reverse osmosis unit, but 'Loop return: usually highest' and 'Sample before disinfection, not after' are still missing, and an invented banner appears again.

**Tip:** after generating, compare every word with the label list. If one label is reworded, reply in the same chat: *Change the text "…" to exactly "…" and change nothing else.*

```text
Atlas visual aid · 1672 × 941, 16:9 landscape · Where to sample · academy/water-treatment-technician-09-chemical-microbiological-sampling.html, section `points`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
WORDING LOCK: every text element in the image must be copied character for character from the label list below. Do not paraphrase, shorten, translate, or 'improve' any label. Do not add any title, banner, caption, or sentence that is not in the list. If a label does not fit, make the box larger, not the wording different.
The loop return pin carries the full label 'Loop return: usually highest'. Across the top, a single banner carries exactly 'Sample before disinfection, not after'. There is no other banner and no mention of sampling plans.
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
✗ No reworded label
✗ No invented banner or caption
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

### BIOMED-04-C — The total, not the recipe

**Save as:** `dialysis-biomedical-technician-04-total-not-recipe.png` · **Canvas:** 1672 × 941, 16:9 landscape

**Why it failed again:** The key label still reads 'Conductivity reflects dissolved ions' instead of 'Conductivity = total salts'.

**Tip:** after generating, compare every word with the label list. If one label is reworded, reply in the same chat: *Change the text "…" to exactly "…" and change nothing else.*

```text
Reference card · 1672 × 941, 16:9 landscape · The total, not the recipe · academy/dialysis-biomedical-technician-04-proportioning-conductivity-bypass.html, section `mix`

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
WORDING LOCK: every text element in the image must be copied character for character from the label list below. Do not paraphrase, shorten, translate, or 'improve' any label. Do not add any title, banner, caption, or sentence that is not in the list. If a label does not fit, make the box larger, not the wording different.
The large caption tile carries exactly 'Conductivity = total salts', with the equals sign. Never write 'reflects', 'dissolved', or 'ions'.
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
✗ No reworded label
✗ No invented banner or caption
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
