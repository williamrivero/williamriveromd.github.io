# Replacement image prompts · Dialysis Clinical Head track

Audit of the November 24, 2026 image batch for the Dialysis Clinical Head track (48 figures, 15 heroes, 15 cards). 44 of 48 figures, all 15 heroes, and all 15 cards passed and are placed on renalcarematters.com. Four figures failed and are held back; their pages show nothing in their place until a replacement passes audit. One placed figure carries a style advisory.

**Status, November 24, 2026:** all five replacements passed audit and are placed on the site. This file is kept as the record of what failed and how the prompts were corrected.

**How to use:** paste one fenced block per generation into the Image Generator GPT. Generate at 1672 × 941. Save the PNG master and the WebP under the exact filename shown, drop both in `Documents/Dialysis Clinical Head/images`, and ask for an audit-and-place pass. The page slot is already wired; the figure appears as soon as the file is placed.

| # | File | Status | Defect in one line |
|---|---|---|---|
| 1 | `dialysis-clinical-head-00-track-map.webp` | Failed, held | Modules 06 and 12 drawn in the wrong part color |
| 2 | `dialysis-clinical-head-04-week-sawtooth.webp` | Failed, held | Friday both completed and missed; chart stops before the Monday peak |
| 3 | `dialysis-clinical-head-06-hierarchy-of-fixes.webp` | Failed, held | Strongest tier illustrated with a weak, memory-based fix |
| 4 | `dialysis-clinical-head-09-competence-matched-staffing.webp` | Failed, held | Float nurse assigned catheter patients she is not validated for |
| 5 | `dialysis-clinical-head-14-30-60-90.webp` | Advisory, placed | Comic style and cast off-model for the track |

## DCH-F01 (replacement) · `dialysis-clinical-head-00-track-map.webp`

**Audit finding:** Two milestones sit in the wrong part. Milestone 06 (the cheese slice, risk and quality) is on the orange Part 3 road with an orange badge; it belongs to Part 2 (teal). Milestone 12 (the dark screen, downtime and privacy) is on the purple Part 4 road; it belongs to Part 5 (green). A learner reading the map would place Modules 6 and 12 in the wrong part of the track.

**Function:** Appreciate · **Priority:** P1 · **Placement:** Hub, below the opening cards

**Why this image:** Learners see fourteen titles, not a journey; they cannot see how authority, safety, continuity, people, and change build on each other.

**Caption on page:** The track at a glance: authority, safety, continuity, people and money, then high-stakes events and change.

```
Illustrated teaching infographic, landscape 1672 × 941 px (16:9), white or very light background.
Renal Care Academy · Dialysis Clinical Head track · audience: physician unit heads and their leadership team, readable by nurses and administrators.
Summary: A winding road in five colored stretches with fourteen numbered milestones; each stretch holds exactly its own modules (navy 01–03, teal 04–06, orange 07–08, purple 09–11, green 12–14), ending at a lit dialysis unit marked Capstone.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL AND CLINICAL TRUTH BLOCK
• Hemodialysis equipment, where shown: upright machine console with blood pump; arterial bloodline RED leaving the patient, venous bloodline BLUE returning; dialyzer mounted vertically.
• Vascular access, where shown: forearm arteriovenous fistula as a raised vein under intact skin; tunneled catheter exits the upper chest under a clean dressing.
• No anatomy visible through skin; no organs drawn on bodies. A kidney, if ever shown, appears only as a small inset (12% of the panel or less) labeled NOT TO SCALE.
• Infographic objects are illustrated with soft shading and depth (GPT-rendered look), never flat clip-art or vector icons.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
• Read left to right, top to bottom. Main subject in the central 70%; labels in clear space with thin leader lines.
• Keep a clear margin of at least 60 px on every edge; nothing touches the frame.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
• A winding road across a light landscape in five colored stretches, left to right along the road. Each stretch carries ONLY its own milestones, and the color changes exactly between the milestones listed:
• Stretch 1, NAVY #1F3864: milestones 01, 02, 03 (signed letter, clipboard, claim form). Color changes to teal after 03.
• Stretch 2, TEAL #1A6B72: milestones 04, 05, 06 (huddle, water drop, cheese slice). The cheese slice 06 sits on TEAL road, never orange. Color changes to orange after 06.
• Stretch 3, ORANGE #C55A11: milestones 07, 08 (typhoon cloud, funnel). Only two milestones on orange. Color changes to purple after 08.
• Stretch 4, PURPLE #4B3280: milestones 09, 10, 11 (group of staff, open door, peso coin). Color changes to green after 11.
• Stretch 5, GREEN #2E6B3E: milestones 12, 13, 14 (dark computer screen, family, staircase). The dark screen 12 sits on GREEN road, never purple.
• Each milestone number badge is filled with the SAME color as the road stretch under it.
• The road ends at a modest dialysis unit with lights on and a flag reading Capstone.
• A small legend card at top left listing the five parts with their colors. Put the part labels only in the legend, not along the road.
• Labels, spelled exactly, American English, DM Sans, sentence case: "Part 1 Authority and accountability"; "Part 2 Clinical and technical safety"; "Part 3 Continuity and capacity"; "Part 4 People, patients, and money"; "Part 5 High-stakes events and change"; "01"; "02"; "03"; "04"; "05"; "06"; "07"; "08"; "09"; "10"; "11"; "12"; "13"; "14"; "Capstone"
• Color meaning: NAVY #1F3864 titles and structure · TEAL #1A6B72 safe, approved, agreed · ORANGE #C55A11 caution, pending, gap · RED #C00000 stop, hold, error · GREEN #2E6B3E verified, complete · PURPLE #4B3280 sampling, measurement, personnel.
• Attribution footer: "© renalcarematters.com" in the bottom-right corner, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content and labels.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
• No medical imaging in this figure. Any monitor or screen shows simple abstract shapes, never a CT, ultrasound, ECG, or readable values.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No cartoon style, flat vector, or clip-art icons
✗ No garbled, misspelled, or extra text
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer; it reads exactly "© renalcarematters.com"
✗ No altered attribution: no www, no https://, no capitals, no other domain
✗ No attribution overlapping content, centered, enlarged, or in any color but navy #1F3864
✗ No anatomy visible through skin; no organs on bodies
✗ No real people, brand names, logos, or facility names
✗ No real patient names, numbers, or identifiable records
✗ No graphic injury, blood pooling, or frightening imagery
✗ No module titles spelled out beside milestones (numbers only)
✗ No people on the road
✗ No arrows that loop back
✗ No cars or vehicles
✗ No milestone 06 on orange road or with an orange badge (06 is teal)
✗ No milestone 12 on purple road or with a purple badge (12 is green)
✗ No color boundary placed between two milestones of the same part
✗ No part labels repeated along the road (legend only)
✗ No decorative icons that carry no meaning
✗ No labels beyond those listed in Layer C
✗ No arrows without a stated meaning
✗ No perspective distortion that bends or hides text
✗ No numbers or percentages other than those listed
✗ No official DOH or PhilHealth seals or logos
✗ No British spellings in any label

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
• References: Brenner & Rector's The Kidney (clinical accuracy); CDC dialysis safety materials (setting realism); KDIGO and NEJM visual abstracts (clarity of numbers).
• Palette NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C; white or very light background.
• Typography: DM Sans for labels, DM Mono for numbers.
• Attribution footer "© renalcarematters.com", bottom right, small, navy, exact lowercase.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Five road segments in the listed colors and order — confirmed
□ Fourteen milestones numbered 01 to 14 in order — confirmed
□ Capstone at the end of the road — confirmed
□ Milestones 04–06 on teal road with teal badges (06 included) — confirmed
□ Milestones 07–08 only on orange road — confirmed
□ Milestones 12–14 on green road with green badges (12 included) — confirmed
□ Every badge color matches the road color under it — confirmed
□ Every label spelled exactly as listed, American English — confirmed
□ Color meanings follow Layer C — confirmed
□ Illustrated, shaded style on a light background, not flat vector — confirmed
□ Bloodlines, if visible: arterial RED, venous BLUE — confirmed
□ No real names, logos, or identifiable records — confirmed
□ No anatomy visible through patient skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## Module 01 · Before You Sign: Authority and Appointment

## DCH-F11 (replacement) · `dialysis-clinical-head-04-week-sawtooth.webp`

**Audit finding:** The figure contradicts itself and misses the point it was built to teach. Friday is drawn as a completed dialysis session (both lines drop inside the Friday bar), and then a "Missed Friday" dashed line rises from the post-dialysis low, so the missed session and the completed session appear together. The chart also ends on Sunday, so the highest pre-Monday peak after the two-day gap never appears; the only "Two-day gap" label points at the first Monday, with no gap drawn before it. The legend adds unrequested text. Redrawn as two stacked panels so the usual week and the missed-Friday week cannot be confused.

**Function:** Understand · **Priority:** P1 · **Placement:** M04 · Who is at risk, after the first paragraph

**Why this image:** Why Monday and missed sessions are dangerous is physiology; a sawtooth curve of potassium and fluid across the week makes it visible.

**Caption on page:** Why Monday and missed sessions carry the risk. Illustrative, not to scale.

```
Illustrated teaching infographic, landscape 1672 × 941 px (16:9), white or very light background.
Renal Care Academy · Dialysis Clinical Head track · audience: physician unit heads and their leadership team, readable by nurses and administrators.
Summary: Two stacked line charts sharing one x-axis from Monday to the next Monday. Top: the usual week, potassium and body fluid fall during the Monday, Wednesday, and Friday sessions and rise between them, with the highest point just before the next Monday. Bottom: the same week with Friday missed, both lines keep rising from Wednesday into a danger band before Monday.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL AND CLINICAL TRUTH BLOCK
• Hemodialysis equipment, where shown: upright machine console with blood pump; arterial bloodline RED leaving the patient, venous bloodline BLUE returning; dialyzer mounted vertically.
• Vascular access, where shown: forearm arteriovenous fistula as a raised vein under intact skin; tunneled catheter exits the upper chest under a clean dressing.
• No anatomy visible through skin; no organs drawn on bodies. A kidney, if ever shown, appears only as a small inset (12% of the panel or less) labeled NOT TO SCALE.
• Infographic objects are illustrated with soft shading and depth (GPT-rendered look), never flat clip-art or vector icons.
• Lines fall during each dialysis bar and rise between bars; the peak just before the next Monday is the highest of the week.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
• Read left to right, top to bottom. Main subject in the central 70%; labels in clear space with thin leader lines.
• Keep a clear margin of at least 60 px on every edge; nothing touches the frame.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
• Two stacked panels, same width, same x-axis: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday (eight day ticks, the last Monday at the right edge).
• TOP PANEL, titled "Usual week": shaded vertical bars labeled "Dialysis" on Monday, Wednesday, Friday, and the next Monday. Two smooth sawtooth lines, potassium (ORANGE) and body fluid (TEAL): each drops steeply inside every dialysis bar and rises steadily between bars. The rise from Friday to the next Monday is the longest and ends at the HIGHEST point of the week, just before the next Monday bar. A bracket under Saturday and Sunday labeled "Two-day gap".
• BOTTOM PANEL, titled "Missed Friday": the same lines and bars for Monday and Wednesday only. The Friday position shows an empty dashed outline bar with no label inside it and NO drop in either line. From Wednesday onward both lines are dashed and rise without interruption through Friday, Saturday, and Sunday, entering a pale red band at the top labeled "Danger zone" by Sunday.
• The red "Danger zone" band appears ONLY in the bottom panel; the top panel lines stay below it.
• A small legend with exactly two entries: "Potassium" (orange line) and "Body fluid" (teal line). No extra words in the legend.
• A small "Illustrative, not to scale" note at bottom left. No numbers on the y-axis.
• Labels, spelled exactly, American English, DM Sans, sentence case: "Usual week"; "Missed Friday"; "Potassium"; "Body fluid"; "Dialysis"; "Two-day gap"; "Danger zone"; "Monday"; "Tuesday"; "Wednesday"; "Thursday"; "Friday"; "Saturday"; "Sunday"; "Illustrative, not to scale"
• Color meaning: NAVY #1F3864 titles and structure · TEAL #1A6B72 safe, approved, agreed · ORANGE #C55A11 caution, pending, gap · RED #C00000 stop, hold, error · GREEN #2E6B3E verified, complete · PURPLE #4B3280 sampling, measurement, personnel.
• Attribution footer: "© renalcarematters.com" in the bottom-right corner, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content and labels.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
• No medical imaging in this figure. Any monitor or screen shows simple abstract shapes, never a CT, ultrasound, ECG, or readable values.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No cartoon style, flat vector, or clip-art icons
✗ No garbled, misspelled, or extra text
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer; it reads exactly "© renalcarematters.com"
✗ No altered attribution: no www, no https://, no capitals, no other domain
✗ No attribution overlapping content, centered, enlarged, or in any color but navy #1F3864
✗ No anatomy visible through skin; no organs on bodies
✗ No real people, brand names, logos, or facility names
✗ No real patient names, numbers, or identifiable records
✗ No graphic injury, blood pooling, or frightening imagery
✗ No numeric axis values for potassium or fluid
✗ No line falling between sessions
✗ No Friday dialysis drop in the bottom (missed Friday) panel
✗ No Friday dialysis bar shown as completed in the bottom panel
✗ No missed-Friday line that starts after a completed Friday session
✗ No danger band in the top panel
✗ No chart that ends on Sunday; the axis ends at the next Monday
✗ No extra legend text such as "builds up between dialysis"
✗ No decorative icons that carry no meaning
✗ No labels beyond those listed in Layer C
✗ No arrows without a stated meaning
✗ No perspective distortion that bends or hides text
✗ No dialysis on Sunday
✗ No numbers or percentages other than those listed
✗ No official DOH or PhilHealth seals or logos
✗ No British spellings in any label

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
• References: Brenner & Rector's The Kidney (clinical accuracy); CDC dialysis safety materials (setting realism); KDIGO and NEJM visual abstracts (clarity of numbers).
• Palette NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C; white or very light background.
• Typography: DM Sans for labels, DM Mono for numbers.
• Attribution footer "© renalcarematters.com", bottom right, small, navy, exact lowercase.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ 'Illustrative, not to scale' present — confirmed
□ Axis runs Monday to the next Monday in both panels — confirmed
□ Top panel: four dialysis bars (Mon, Wed, Fri, next Mon) and the highest peak just before the next Monday — confirmed
□ Bottom panel: no drop at Friday; dashed lines rise from Wednesday into the danger zone by Sunday — confirmed
□ Danger zone only in the bottom panel — confirmed
□ Every label spelled exactly as listed, American English — confirmed
□ Color meanings follow Layer C — confirmed
□ Illustrated, shaded style on a light background, not flat vector — confirmed
□ Bloodlines, if visible: arterial RED, venous BLUE — confirmed
□ No real names, logos, or identifiable records — confirmed
□ No anatomy visible through patient skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## DCH-F20 (replacement) · `dialysis-clinical-head-06-hierarchy-of-fixes.webp`

**Audit finding:** The top tier teaches the wrong lesson. "Remove or force" is illustrated by "keep look-alike bicarbonate concentrates on different shifts", which is a scheduling workaround that depends on people remembering, not a forcing function, so the strongest tier is shown with a weak fix. The original prompt left the examples open ("separate similar names across shifts"), which invited this; the replacement fixes all four example texts word for word and makes the top tier a physical barrier (connectors that fit only the right concentrate).

**Function:** Apply · **Priority:** P1 · **Placement:** M06 · Investigating, before the flow

**Why this image:** Readers default to retraining; an inverted pyramid ranks fixes by strength with dialysis examples.

**Caption on page:** The hierarchy of fixes. Training supports a stronger fix; on its own it fades.

```
Illustrated teaching infographic, landscape 1672 × 941 px (16:9), white or very light background.
Renal Care Academy · Dialysis Clinical Head track · audience: physician unit heads and their leadership team, readable by nurses and administrators.
Summary: An inverted pyramid with four tiers, strongest at the wide top: remove or force, standardize and simplify, check and alert, train and remind. Each tier has one exact dialysis example on a tag at right.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL AND CLINICAL TRUTH BLOCK
• Hemodialysis equipment, where shown: upright machine console with blood pump; arterial bloodline RED leaving the patient, venous bloodline BLUE returning; dialyzer mounted vertically.
• Vascular access, where shown: forearm arteriovenous fistula as a raised vein under intact skin; tunneled catheter exits the upper chest under a clean dressing.
• No anatomy visible through skin; no organs drawn on bodies. A kidney, if ever shown, appears only as a small inset (12% of the panel or less) labeled NOT TO SCALE.
• Infographic objects are illustrated with soft shading and depth (GPT-rendered look), never flat clip-art or vector icons.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
• Read left to right, top to bottom. Main subject in the central 70%; labels in clear space with thin leader lines.
• Keep a clear margin of at least 60 px on every edge; nothing touches the frame.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
• An inverted pyramid of four tiers, widest at top, narrowest at bottom. A thick teal arrow on the left labeled "Stronger" points UP.
• Tier 1 (top, widest), TEAL: title "Remove or force". Inside, an illustrated pair of concentrate jugs whose connectors are physically different shapes, so the acid connector cannot fit the bicarbonate port. Tag at right reads exactly: "Dialysis example: connectors that fit only the right concentrate".
• Tier 2, ORANGE: title "Standardize and simplify". Inside, a machine screen with three boxes joined by arrows. Tag reads exactly: "Dialysis example: one programming sequence on every machine".
• Tier 3, PURPLE: title "Check and alert". Inside, a clipboard with one ticked box. Tag reads exactly: "Dialysis example: a second check of the dialysate prescription before start".
• Tier 4 (bottom, narrowest), GREEN: title "Train and remind". Inside, a memo pad. Tag reads exactly: "Dialysis example: a memo and a staff briefing".
• The tier titles and tag texts are the ONLY words besides "Stronger"; the generator must not write its own examples.
• Labels, spelled exactly, American English, DM Sans, sentence case: "Stronger"; "Remove or force"; "Standardize and simplify"; "Check and alert"; "Train and remind"; "Dialysis example: connectors that fit only the right concentrate"; "Dialysis example: one programming sequence on every machine"; "Dialysis example: a second check of the dialysate prescription before start"; "Dialysis example: a memo and a staff briefing"
• Color meaning: NAVY #1F3864 titles and structure · TEAL #1A6B72 safe, approved, agreed · ORANGE #C55A11 caution, pending, gap · RED #C00000 stop, hold, error · GREEN #2E6B3E verified, complete · PURPLE #4B3280 sampling, measurement, personnel.
• Attribution footer: "© renalcarematters.com" in the bottom-right corner, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content and labels.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
• No medical imaging in this figure. Any monitor or screen shows simple abstract shapes, never a CT, ultrasound, ECG, or readable values.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No cartoon style, flat vector, or clip-art icons
✗ No garbled, misspelled, or extra text
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer; it reads exactly "© renalcarematters.com"
✗ No altered attribution: no www, no https://, no capitals, no other domain
✗ No attribution overlapping content, centered, enlarged, or in any color but navy #1F3864
✗ No anatomy visible through skin; no organs on bodies
✗ No real people, brand names, logos, or facility names
✗ No real patient names, numbers, or identifiable records
✗ No graphic injury, blood pooling, or frightening imagery
✗ No upright pyramid
✗ No tiers out of order
✗ No top-tier example that relies on people remembering (shift separation, signs, or reminders are not forcing functions)
✗ No examples other than the four listed, word for word
✗ No wording about "different shifts" anywhere
✗ No decorative icons that carry no meaning
✗ No labels beyond those listed in Layer C
✗ No arrows without a stated meaning
✗ No perspective distortion that bends or hides text
✗ No numbers or percentages other than those listed
✗ No official DOH or PhilHealth seals or logos
✗ No British spellings in any label

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
• References: Brenner & Rector's The Kidney (clinical accuracy); CDC dialysis safety materials (setting realism); KDIGO and NEJM visual abstracts (clarity of numbers).
• Palette NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C; white or very light background.
• Typography: DM Sans for labels, DM Mono for numbers.
• Attribution footer "© renalcarematters.com", bottom right, small, navy, exact lowercase.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Inverted with Remove or force at top — confirmed
□ Stronger arrow pointing up — confirmed
□ Top tier shows a physical forcing function (connectors that cannot be swapped) — confirmed
□ Each tag text matches Layer C word for word — confirmed
□ Every label spelled exactly as listed, American English — confirmed
□ Color meanings follow Layer C — confirmed
□ Illustrated, shaded style on a light background, not flat vector — confirmed
□ Bloodlines, if visible: arterial RED, venous BLUE — confirmed
□ No real names, logos, or identifiable records — confirmed
□ No anatomy visible through patient skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## DCH-F30 (replacement) · `dialysis-clinical-head-09-competence-matched-staffing.webp`

**Audit finding:** The figure shows the opposite of its lesson. Under the float nurse, whose card correctly shows catheter care not validated, the board places two two-lumen catheter magnets, so the float nurse is assigned exactly the patients she is not cleared for. The callouts are also wrong: a "Fistula care" label points at a catheter magnet, and "Float nurse" appears twice. The replacement prints "Fistula" or "Catheter" on every magnet and fixes the placement column by column.

**Function:** Apply · **Priority:** P1 · **Placement:** M09 · Big picture, after the plain-language box

**Why this image:** 'Count competencies, not bodies' is a slogan until the board shows a float nurse's card missing the skill.

**Caption on page:** Count competencies, not bodies. A nurse counts toward the assignments she has been validated to do.

```
Illustrated teaching infographic, landscape 1672 × 941 px (16:9), white or very light background.
Renal Care Academy · Dialysis Clinical Head track · audience: physician unit heads and their leadership team, readable by nurses and administrators.
Summary: An assignment board with three nurse columns. Two validated nurses carry both fistula and catheter patients; the float nurse, whose card shows catheter care not yet validated, carries fistula patients only.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL AND CLINICAL TRUTH BLOCK
• Hemodialysis equipment, where shown: upright machine console with blood pump; arterial bloodline RED leaving the patient, venous bloodline BLUE returning; dialyzer mounted vertically.
• Vascular access, where shown: forearm arteriovenous fistula as a raised vein under intact skin; tunneled catheter exits the upper chest under a clean dressing.
• No anatomy visible through skin; no organs drawn on bodies. A kidney, if ever shown, appears only as a small inset (12% of the panel or less) labeled NOT TO SCALE.
• Infographic objects are illustrated with soft shading and depth (GPT-rendered look), never flat clip-art or vector icons.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
• Read left to right, top to bottom. Main subject in the central 70%; labels in clear space with thin leader lines.
• Keep a clear margin of at least 60 px on every edge; nothing touches the frame.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
• A whiteboard assignment board with three columns. At the top of each column, a nurse card with a head-and-shoulders portrait (fictional Filipino nurse in purple scrubs) and two competency rows: "Fistula care" and "Catheter care".
• Column 1 and column 2: both rows ticked with TEAL check boxes; a green outline around each card; a small tag "Validated" beside column 1 only.
• Column 3: a band across the card reads "Float nurse". "Fistula care" ticked; "Catheter care" shows an EMPTY ORANGE box. An orange outline around this card; a single callout "Not yet validated" points ONLY to the empty catheter care box.
• Below each card, rectangular patient magnets. Each magnet shows a small illustrated access icon AND a printed word: a fistula magnet shows a single looped arm-access line and the word "Fistula"; a catheter magnet shows a two-lumen catheter with one RED and one BLUE cap and the word "Catheter".
• Exact magnet placement: column 1 = one "Fistula" magnet and one "Catheter" magnet; column 2 = two "Catheter" magnets; column 3 (float nurse) = two "Fistula" magnets and NO catheter magnets.
• No other callouts on the board. No leader lines from labels to magnets.
• Labels, spelled exactly, American English, DM Sans, sentence case: "Validated"; "Not yet validated"; "Float nurse"; "Fistula care"; "Catheter care"; "Fistula"; "Catheter"
• Color meaning: NAVY #1F3864 titles and structure · TEAL #1A6B72 safe, approved, agreed · ORANGE #C55A11 caution, pending, gap · RED #C00000 stop, hold, error · GREEN #2E6B3E verified, complete · PURPLE #4B3280 sampling, measurement, personnel.
• Attribution footer: "© renalcarematters.com" in the bottom-right corner, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content and labels.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
• No medical imaging in this figure. Any monitor or screen shows simple abstract shapes, never a CT, ultrasound, ECG, or readable values.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No cartoon style, flat vector, or clip-art icons
✗ No garbled, misspelled, or extra text
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer; it reads exactly "© renalcarematters.com"
✗ No altered attribution: no www, no https://, no capitals, no other domain
✗ No attribution overlapping content, centered, enlarged, or in any color but navy #1F3864
✗ No anatomy visible through skin; no organs on bodies
✗ No real people, brand names, logos, or facility names
✗ No real patient names, numbers, or identifiable records
✗ No graphic injury, blood pooling, or frightening imagery
✗ No real staff names
✗ No catheter patient assigned to the float nurse
✗ No catheter magnet (two-lumen, red and blue caps) anywhere in the float nurse column
✗ No callout labels outside the board pointing at magnets
✗ No duplicated "Float nurse" label
✗ No magnet without its printed word "Fistula" or "Catheter"
✗ No decorative icons that carry no meaning
✗ No labels beyond those listed in Layer C
✗ No arrows without a stated meaning
✗ No perspective distortion that bends or hides text
✗ No numbers or percentages other than those listed
✗ No official DOH or PhilHealth seals or logos
✗ No British spellings in any label

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
• References: Brenner & Rector's The Kidney (clinical accuracy); CDC dialysis safety materials (setting realism); KDIGO and NEJM visual abstracts (clarity of numbers).
• Palette NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C; white or very light background.
• Typography: DM Sans for labels, DM Mono for numbers.
• Attribution footer "© renalcarematters.com", bottom right, small, navy, exact lowercase.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Float card lacks catheter tick — confirmed
□ Catheter patients under validated nurses — confirmed
□ Float nurse column holds only "Fistula" magnets — confirmed
□ Columns 1 and 2 together hold all three "Catheter" magnets — confirmed
□ Only one callout, "Not yet validated", pointing at the empty catheter care box — confirmed
□ Every label spelled exactly as listed, American English — confirmed
□ Color meanings follow Layer C — confirmed
□ Illustrated, shaded style on a light background, not flat vector — confirmed
□ Bloodlines, if visible: arterial RED, venous BLUE — confirmed
□ No real names, logos, or identifiable records — confirmed
□ No anatomy visible through patient skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## DCH-F48 (replacement) · `dialysis-clinical-head-14-30-60-90.webp`

**Audit finding:** ADVISORY, placed for now. Content is correct, but the style departs from the track: thick-outline comic panels, six scenes instead of three, a cast that does not read as Filipino unit staff, and a CPR scene the module does not teach. Regenerate when convenient so Module 14 matches the other 43 figures; the current file stays live until a replacement passes audit.

**Function:** Apply · **Priority:** P2 · **Placement:** M14 · Your first 90 days, after the handover paragraph

**Why this image:** New leaders plan the future first; three columns sequence containment before improvement.

**Caption on page:** Your first 90 days. Find the work people are already waiting for before you plan the future.

```
Illustrated teaching infographic, landscape 1672 × 941 px (16:9), white or very light background.
Renal Care Academy · Dialysis Clinical Head track · audience: physician unit heads and their leadership team, readable by nurses and administrators.
Summary: Three tall illustrated columns for days 30, 60, and 90, each showing the same Filipino clinical head with his team at a Philippine dialysis unit: reconcile and walk, test and review, present and commit.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL AND CLINICAL TRUTH BLOCK
• Hemodialysis equipment, where shown: upright machine console with blood pump; arterial bloodline RED leaving the patient, venous bloodline BLUE returning; dialyzer mounted vertically.
• Vascular access, where shown: forearm arteriovenous fistula as a raised vein under intact skin; tunneled catheter exits the upper chest under a clean dressing.
• No anatomy visible through skin; no organs drawn on bodies. A kidney, if ever shown, appears only as a small inset (12% of the panel or less) labeled NOT TO SCALE.
• Infographic objects are illustrated with soft shading and depth (GPT-rendered look), never flat clip-art or vector icons.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
• Read left to right, top to bottom. Main subject in the central 70%; labels in clear space with thin leader lines.
• Keep a clear margin of at least 60 px on every edge; nothing touches the frame.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
• Three tall columns like pillars, each with a header badge and one illustrated scene beneath, in the same soft-shaded illustrated style as the rest of the track (no thick comic outlines, no flat cel shading).
• Cast: the same fictional Filipino physician clinical head in every column, with Filipino nurses and staff in purple or teal scrubs; a Philippine hemodialysis unit setting (blue chairs, upright machines, tropical light).
• Day 30: the physician and head nurse walking the floor, a binder of records under his arm. Day 60: a tabletop drill at a nurses’ station with a printed run chart. Day 90: the physician presenting a one-page plan to two owners at a small table.
• Labels, spelled exactly, American English, DM Sans, sentence case: "Day 30: reconcile and walk"; "Day 60: test and review"; "Day 90: present and commit"
• Color meaning: NAVY #1F3864 titles and structure · TEAL #1A6B72 safe, approved, agreed · ORANGE #C55A11 caution, pending, gap · RED #C00000 stop, hold, error · GREEN #2E6B3E verified, complete · PURPLE #4B3280 sampling, measurement, personnel.
• Attribution footer: "© renalcarematters.com" in the bottom-right corner, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content and labels.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
• No medical imaging in this figure. Any monitor or screen shows simple abstract shapes, never a CT, ultrasound, ECG, or readable values.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No cartoon style, flat vector, or clip-art icons
✗ No garbled, misspelled, or extra text
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer; it reads exactly "© renalcarematters.com"
✗ No altered attribution: no www, no https://, no capitals, no other domain
✗ No attribution overlapping content, centered, enlarged, or in any color but navy #1F3864
✗ No anatomy visible through skin; no organs on bodies
✗ No real people, brand names, logos, or facility names
✗ No real patient names, numbers, or identifiable records
✗ No graphic injury, blood pooling, or frightening imagery
✗ No real dates
✗ No more than three columns
✗ No comic-book or graphic-novel style, thick black outlines, or flat cel shading
✗ No cast that does not read as Filipino staff and owners
✗ No CPR or resuscitation scene
✗ No more than one scene per column
✗ No decorative icons that carry no meaning
✗ No labels beyond those listed in Layer C
✗ No arrows without a stated meaning
✗ No perspective distortion that bends or hides text
✗ No numbers or percentages other than those listed
✗ No official DOH or PhilHealth seals or logos
✗ No British spellings in any label

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
• References: Brenner & Rector's The Kidney (clinical accuracy); CDC dialysis safety materials (setting realism); KDIGO and NEJM visual abstracts (clarity of numbers).
• Palette NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C; white or very light background.
• Typography: DM Sans for labels, DM Mono for numbers.
• Attribution footer "© renalcarematters.com", bottom right, small, navy, exact lowercase.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Three columns in order — confirmed
□ Same clinical head appears in all three columns — confirmed
□ Style matches the rest of the track (soft shading, light background) — confirmed
□ Every label spelled exactly as listed, American English — confirmed
□ Color meanings follow Layer C — confirmed
□ Illustrated, shaded style on a light background, not flat vector — confirmed
□ Bloodlines, if visible: arterial RED, venous BLUE — confirmed
□ No real names, logos, or identifiable records — confirmed
□ No anatomy visible through patient skin — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## Heroes and cards

## Acceptance checks for every replacement

- The exact filename, 1672 × 941, PNG master plus WebP.
- Every Layer G box confirmed by eye, with particular attention to the defect named in the audit finding.
- Every label spelled exactly as listed, in American English, with no extra words.
- The footer reads exactly "© renalcarematters.com", bottom right, small, navy.
