# GPT image prompts — replacements after the November 24, 2026 audit

Two of the thirteen Module 13 and hub images failed the audit and were **not** placed. Regenerate each from the corrected prompt below, save it under the same file name (PNG master plus same-size WebP) in `Nephrology Nursing/images`, and the next install run will place it. The other eleven passed and are live.

| ID | File | Why it failed | Fix |
|---|---|---|---|
| 13-D | `nephrology-nursing-13-cvvhdf-citrate-circuit.png` | Several labels are crossed by lines and become hard to read: “Blood out” and “Effluent out” are cut by the effluent and return lines; “Access pressure” is crossed by the citrate line; “Post” sits on the replacement line; the catheter drawing runs through “dialysis catheter” inside the patient box. The circuit topology itself was correct (citrate before the blood pump, pre and post tees, venous pressure then air detector last before the patient, dialysate countercurrent, calcium on a separate line). | Keep the topology exactly as drawn. Move every label so that no line, tee, or marker passes through any letter: put labels above or below their line with a short leader, and keep a clear margin of white space around each label. Draw the dual-lumen catheter outside the patient box so it never crosses the box text. |
| 13-K | `nephrology-nursing-13-hdf-trials.png` | A template placeholder leaked into the picture: the lower panel heading renders as “WHY-RESULTS-DIFFERED” (capitals with hyphens). All trial numbers matched the module text. | Render that heading exactly as “Why the results differed” in sentence case, the same style as the other headings. Change nothing else. |

## 13-D — CVVHDF circuit with regional citrate and calcium — replacement

**Audit finding:** Several labels are crossed by lines and become hard to read: “Blood out” and “Effluent out” are cut by the effluent and return lines; “Access pressure” is crossed by the citrate line; “Post” sits on the replacement line; the catheter drawing runs through “dialysis catheter” inside the patient box. The circuit topology itself was correct (citrate before the blood pump, pre and post tees, venous pressure then air detector last before the patient, dialysate countercurrent, calcium on a separate line).

**What to change:** Keep the topology exactly as drawn. Move every label so that no line, tee, or marker passes through any letter: put labels above or below their line with a short leader, and keep a clear margin of white space around each label. Draw the dual-lumen catheter outside the patient box so it never crosses the box text.

- **File:** images/nephrology-nursing-13-cvvhdf-citrate-circuit.png
- **Placement:** Module 13, section `crrt-anticoag` (Keeping the circuit open: no anticoagulant, heparin, or regional citrate); also supports `crrt-circuit` (The circuit: priming, pressures, filter life, and alarms)
- **Job:** U — the learner can trace blood, dialysate, replacement fluid, citrate, and calcium through a CVVHDF circuit and say where each pressure and sample is taken.
- **Governing skill:** dialysis-circuit-schematic (locked topology; modality CVVHDF: countercurrent dialysate PLUS replacement)
- **Canvas:** 1672 × 941, 16:9
- **Alt text:** CVVHDF circuit from a jugular dialysis catheter: citrate enters the red access line, dialysate runs countercurrent, replacement fluid joins one blood line, calcium returns separately.
- **Caption:** Citrate enters the blood line just after it leaves the patient and binds calcium so the circuit cannot clot; much of it leaves in the effluent, and calcium is replaced into the patient by a separate infusion. Dialysate runs outside the fibers against the blood; replacement fluid joins the blood line itself.
- **Source of truth:** m13_x.py `crrt-modes`: CVVHDF = both dialysate and replacement fluid, diffusion plus convection; building blocks: blood pump, filter, effluent pump, dialysate pump, one or two replacement pumps, syringe or infusion pumps for anticoagulant; integrated scales; usually a non-tunneled dialysis central venous catheter. `crrt-prescription`: replacement site pre-filter, post-filter, or split. `crrt-anticoag` citrate steps: (1) citrate infused into the blood line just after it leaves the patient, binds ionized calcium; (2) in the filter much of the citrate–calcium complex passes into the effluent and is discarded; (3) calcium replaced by a separate calcium infusion into the patient, either through the return line or a separate central line, according to the machine and protocol; (4) citrate reaching the patient is metabolized (liver, muscle) to bicarbonate. Post-filter ionized calcium sampled from the circuit after the filter (circuit anticoagulated enough? guides citrate rate); patient ionized calcium from an arterial line or the patient's own vein (patient safe? guides calcium infusion); label every sample with site and time; never run calcium through the same line as citrate. `crrt-circuit` pressure table: access (between catheter and blood pump, normally negative), pre-filter (after pump, before filter, positive), return/venous (after filter, before re-entry, positive), effluent pressure (fluid side of the filter), transmembrane pressure (calculated across the membrane), air trap; air detector and blood leak detector (red cells in the effluent). m13.py `physiology`: convection, solvent drag. Topology, port rules, colors, catheter course from the dialysis-circuit-schematic skill.
- **Reviewer flags:** (1) Calcium site: the text allows the return line OR a separate central line; the figure draws a separate purple line to a separate central venous line, labeled "per protocol", and notes the alternative. Confirm. (2) Citrate site: the text says "just after it leaves the patient"; the figure places the citrate tee on the red line after the access-pressure point and before the blood pump (simple-figure skill order). Confirm against the ICU's machine. (3) Post-filter sample site placed on the blue line between the filter outlet and the post-dilution tee; the text says only "from the circuit after the filter". Confirm. (4) Removed from the circuit-skill template because the module does not state them: KDIGO dose 20–25 mL/kg/h on the circuit, "about 15%" pre-dilution clearance loss, filtration fraction 20–25%, IHD 500 mL/min, five-modality legend, and blood pump "mL/min" label. (5) Catheter in the right internal jugular with the tip at the SVC–right atrial junction is a circuit-skill anatomy rule; the module says only "non-tunneled dialysis central venous catheter". (6) Amber #C9A84C (citrate) and purple #4B3280 (calcium) are additions to the circuit palette, declared in the legend.
- **Attach when generating:** /root/.claude/skills/synced/e7f3cdd9-a361-44a3-a710-a92e74c17604_d5a9b0e0-f0c3-4377-8b81-f15e9ba9cc14/dialysis-circuit-schematic/assets/catheter-hub-connection-reference.png (the same file is provided as /mnt/user-data/outputs/nursing/image-plan/catheter-hub-connection-reference.png; attach it to the ChatGPT message together with the prompt)

```text
Flat 2D medical schematic, 1672 × 941 landscape (16:9) — CVVHDF (continuous venovenous hemodiafiltration) circuit with regional citrate anticoagulation and a separate calcium infusion. Two panels: (L) whole-circuit map of blood, dialysate, replacement, effluent, citrate, and calcium paths; (R) hollow-fiber cutaway showing countercurrent diffusion PLUS solvent drag. White #ffffff background. An attached reference image shows correct versus wrong catheter hub connections; follow the CORRECT example.

════════════════════════════════════
LAYER A — CIRCUIT TRUTH BLOCK (supreme override)
- MODALITY IS CVVHDF: BOTH a dialysate bag AND a replacement-fluid bag. Both panels teach diffusion plus convection.
- RED #C00000 = blood leaving the patient (arterial/access). BLUE #1F6FC0 = blood returning (venous/return). Red and blue are used for blood only.
- DIALYSATE (TEAL #1A6B72): dialysate bag → dialysate pump → filter's UPPER SIDE PORT (near the blood outlet). Flows DOWN outside the fibers, countercurrent to blood, and leaves with the effluent at the LOWER SIDE PORT.
- REPLACEMENT FLUID (GREEN #2E6B3E): bag → replacement pump → THREE-WAY SELECTOR → EITHER the pre-dilution tee (red line, between blood pump and filter inlet) OR the post-dilution tee (blue line, after the filter outlet). ONE ROUTE AT A TIME. Badge the selector "OR — select one route"; both branches equal visual weight. Replacement NEVER enters a side port.
- EFFLUENT (TEAL #1A6B72): filter's LOWER SIDE PORT → effluent pressure point → blood leak detector → effluent pump → waste bag. Effluent = spent dialysate + ultrafiltrate (with the citrate–calcium complex).
- CITRATE (AMBER #C9A84C): citrate bag → small citrate pump → SHORT STUB tee into the RED line just after it leaves the patient: AFTER the access pressure point, BEFORE the blood pump.
- CALCIUM (PURPLE #4B3280): calcium bag → small calcium pump → its OWN separate line to a separate small central venous line in the patient's upper chest. It never joins the citrate line, never joins the red line, and never enters the filter.
- AN INFUSION JOINS A LINE, IT NEVER REROUTES OR RECOLORS IT. Green and amber branches end at their tees as SHORT STUBS. The red line stays red and unbroken from the red hub to the filter's bottom cap; the blue line stays blue and unbroken from the filter's top cap to the blue hub.
- ENDS ARE FOR BLOOD, SIDES ARE FOR FLUID. Bottom END CAP (red) = blood inlet; top END CAP (blue) = blood outlet. Side ports carry dialysate and effluent only. The red line approaches the bottom cap FROM BELOW along the filter axis; the blue line leaves the top cap UPWARD along the same axis.
- CATHETER: temporary, non-tunneled, dual-lumen, right internal jugular — ONE catheter bifurcating into TWO limbs, each ending in a luer hub with a colored terminal cap (one RED, one BLUE), a clamp on each limb. Translucent course: internal jugular → brachiocephalic vein → superior vena cava, tip at the SVC–right atrial junction. Only bifurcation and hubs outside the skin.
- Lines connect END-TO-END at the hub tips: one continuous tube of constant width, no gap, no side attachment, NO ARROWHEAD STANDING IN FOR A CONNECTION. No hub-tip zoom inset.
- HUB HEIGHTS MATCH LINE HEIGHTS: BLUE hub HIGH, level with the venous line along the top; RED hub LOW, level with the arterial line along the bottom.
- FLIPPED LAYOUT: red half along the BOTTOM, blue half along the TOP; blood ascends the filter.
- Blood path order (mandatory): patient (RED hub, low) → ACCESS PRESSURE (negative) → CITRATE TEE (amber) → BLOOD PUMP (roller) → PRE-DILUTION TEE → PRE-FILTER PRESSURE → FILTER bottom cap → up inside fibers → top cap → POST-FILTER SAMPLE SITE → POST-DILUTION TEE → VENOUS PRESSURE → AIR TRAP AND AIR DETECTOR → patient (BLUE hub, high).
- Anchor to landmarks: the venous pressure gauge sits just after the post-dilution tee; the air detector sits immediately beside the patient's BLUE hub, the last thing blood passes. Nothing between the air detector and the blue hub.
- Blood pump on the RED side only. Pre-filter pressure INLINE between pump and filter inlet.
- Arrows: red arrows patient → machine; blue arrows machine → patient; teal dialysate arrows run downward outside the fibers.

════════════════════════════════════
LAYER B — SPATIAL ORIENTATION
- Left panel (about 64% width): patient head, neck, upper chest at far left in light-gray outline; catheter in the right neck, limbs splayed (blue hub high, red hub low); a separate small purple central line in the upper chest. Red line along the bottom to a vertical filter at the panel's right; blue line returns along the top. Bags hang along the right edge, each drawn sitting on a small scale cradle: dialysate (teal) and replacement (green) upper right; effluent waste bag lower right. Citrate (amber) and calcium (purple) small bags and pumps lower left, near the patient.
- Right panel (about 36% width): standalone vertical filter cutaway, blood bottom → top.

════════════════════════════════════
LAYER C — RENDER SPECIFICATIONS
Panel heading, top left: "CVVHDF circuit with regional citrate". Component labels, verbatim:
- "Dialysis catheter, internal jugular (temporary)"
- "Access pressure (suction, normally negative)"
- "Citrate in: binds calcium, circuit can't clot"
- "Blood pump"
- "Pre-filter pressure"
- "Filter"
- "Blood in" (bottom cap) and "Blood out" (top cap)
- "Dialysate in" (upper side port) and "Effluent out" (lower side port)
- "Transmembrane pressure (calculated)" as a thin double-headed annotation across the filter wall, not a flow arrow
- "Post-filter sample: is the circuit anticoagulated?"
- "Venous (return) pressure"
- "Air trap and air detector: never override"
- "Dialysate pump" · "Replacement pump" · "Effluent pump"
- "Replacement fluid" · "Dialysate" · "Effluent bag"
- "OR — select one route"
- "Pre-dilution: longer filter life"
- "Post-dilution: more clearance per liter"
- "Effluent pressure"
- "Blood leak detector"
- "Integrated scales: hands off"
- "Citrate per protocol"
- "Calcium per protocol: separate line"
Small gray note under the calcium label: "Or via return line, per machine and protocol".
Small note box near the patient, teal outline: "Patient sample: arterial line or vein. Is the patient safe?"
Right panel cutaway, title: "Inside the filter: diffusion plus convection". Labels:
- "Blood rises inside the fibers"
- "Dialysate flows the opposite way"
- "Water drags solutes across"
- "Citrate–calcium complex leaves in effluent"
- "Cells and albumin stay in the blood"
Cutaway: teal dialysate enters at the upper side port and flows DOWN outside the fibers; small arrows also cross the wall outward (solvent drag); effluent leaves the lower side port.
Legend box (small, lower right of left panel): red "Blood out of patient"; blue "Blood back to patient"; teal "Dialysate and effluent"; green "Replacement fluid"; amber "Citrate"; purple "Calcium".
Typeface: Inter for all text. Leader lines thin navy. Text navy #0f1e2e.
Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all structures and labels.

════════════════════════════════════
LAYER D — IMAGING PHYSICS
Not applicable — schematic.

════════════════════════════════════
LAYER E — NEGATIVE CONSTRAINTS
✗ No line, tee, arrow, or marker passing through any letter of any label (check “Blood out”, “Effluent out”, “Access pressure”, “Post”, “TMP”, and the patient box)
✗ No catheter drawing overlapping the text inside the patient box
✗ No missing dialysate bag or replacement bag — CVVHDF shows both.
✗ No dialysate entering the blood line; no replacement fluid entering a side port.
✗ No cocurrent dialysate; dialysate enters near the blood OUTLET (upper) and leaves near the INLET (lower).
✗ No permanently forked green line feeding both tees; no selector without the "OR — select one route" badge.
✗ No green or amber segment replacing any stretch of blood line; no infusion color continuing past its tee.
✗ No citrate tee on the blue line, after the blood pump, or on the filter.
✗ No calcium line joining the citrate line, the red line, or the filter; calcium and citrate never share a line.
✗ No blood line touching the side of the filter; no fluid line on an end cap.
✗ No air detector before the venous pressure gauge; nothing between the detector and the blue hub.
✗ No blood pump on the return side; no pre-filter gauge on a side branch.
✗ No filter with blood descending.
✗ No line attached to the side of a hub; no arrowhead in place of a connection; no hub-tip zoom inset; no both hubs at mid-height.
✗ No catheter tip in the neck, mid-SVC, or ventricle; no two dialysis catheters.
✗ No numbers anywhere: no flow rates, doses, mL/kg/h, percentages, calcium targets, pressures, or alarm limits.
✗ No modality legend listing other therapies; no heparin line.
✗ No kidney drawn in the circuit; no red or blue on anything but blood.
✗ No dark background, no 3D render, no DM Sans, no serif font, no cartoon style, no garbled or placeholder text, no prompt text in the image.
✗ No missing or altered footer.

════════════════════════════════════
LAYER F — STYLE REFERENCE
Flat vector schematic, white background, leader-line labels, colors exactly as in Layers A and C, card fill #f3f4f6, Inter.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Header, bags, and cutaway agree: CVVHDF, both a dialysate bag and a replacement bag, countercurrent stream plus outward solvent-drag arrows
□ Dialysate (teal) enters the UPPER side port and flows down; effluent (teal) leaves the LOWER side port
□ Replacement (green) reaches the blood line only, through the selector badged "OR — select one route"; both branches equal weight; short stub at the tee
□ Citrate (amber) is a short stub on the RED line, after access pressure and before the blood pump
□ Calcium (purple) runs on its own line to a separate central line; it never meets the citrate line, the red line, or the filter; "Or via return line, per machine and protocol" note present
□ Post-filter sample site on the blue line after the filter; patient-sample note near the patient
□ Exactly four filter connections: two end caps (blood), two side ports (fluid); no blood line on a side wall
□ Red line enters the bottom cap from below; blue leaves the top cap upward; blood ascends
□ Blood path order: access pressure → citrate tee → blood pump → pre-dilution tee → pre-filter pressure → filter → post-filter sample → post-dilution tee → venous pressure → air trap and detector → blue hub
□ Air detector is the last component before the patient
□ Effluent line carries effluent pressure point and blood leak detector before the effluent pump
□ Transmembrane pressure drawn as an annotation across the wall, not a flow arrow
□ Blue hub high, red hub low; trace each line hub to filter with no gap or arrowhead substitute
□ Catheter: one dual-lumen catheter in the internal jugular, red and blue terminal caps, clamps, tip at the SVC–right atrial junction
□ Legend shows all six colors, including amber citrate and purple calcium
□ No numbers anywhere (no rates, doses, targets, pressures, percentages)
□ Label spelling correct throughout ("hemodiafiltration", "anticoagulated", "Transmembrane"); American spelling; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

**QA after regeneration (in addition to the checklist above):**
□ No line, tee, arrow, or marker passing through any letter of any label (check “Blood out”, “Effluent out”, “Access pressure”, “Post”, “TMP”, and the patient box)
□ No catheter drawing overlapping the text inside the patient box


## 13-K — The HDF trials at a glance — replacement

**Audit finding:** A template placeholder leaked into the picture: the lower panel heading renders as “WHY-RESULTS-DIFFERED” (capitals with hyphens). All trial numbers matched the module text.

**What to change:** Render that heading exactly as “Why the results differed” in sentence case, the same style as the other headings. Change nothing else.

- **File:** images/nephrology-nursing-13-hdf-trials.png
- **Placement:** Module 13 page, section `hdf-evidence` (What the trials show, and what they do not)
- **Job:** U/P — the learner sees why early trials looked neutral, why CONVINCE was different, and which findings are associations.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Six HDF studies compared: CONTRAST, Turkish, ESHOL, CONVINCE, and two pooled analyses, with patients, comparator, and result; volume link shown as association.
- **Caption:** The trials that delivered lower convection volumes found no overall survival difference; CONVINCE randomized only patients able to receive high volumes and found lower mortality. The link between higher achieved volume and better survival is an association, not proof.
- **Source of truth:** m13_x2.py `hdf-evidence` table and text. CONTRAST (2012): 714 patients; post-dilution online HDF versus low-flux HD; all-cause death no significant difference (hazard ratio 0.95; 95% CI 0.75 to 1.20); on-treatment: higher volumes, lower mortality; "required confirmation". Turkish online HDF study (2013): 782; versus high-flux HD; composite of death and nonfatal cardiovascular events no significant difference (event-free survival 77.6% versus 74.8%); mean filtration volume about 17.2 liters; post hoc above 17.4 liters better survival. ESHOL (2013): 906; high-efficiency post-dilution online HDF versus continued HD; all-cause death 30% lower (HR 0.70; 95% CI 0.53 to 0.92). CONVINCE (2023): 1,360 on high-flux HD for at least 3 months, all judged able to receive at least 23 liters; high-volume HDF versus continued high-flux HD; all-cause death 17.3% (118 of 683) versus 21.9% (148 of 677), median 30 months, HR 0.77 (95% CI 0.65 to 0.93); mean delivered 25.3 liters. Pooled 2016 (peters2016): four trials, 2,793 participants; 14% lower all-cause death, 23% lower cardiovascular death; largest benefit above 23 liters per 1.73 m². Pooled 2024 (vernooij2024): five trials, 4,153 patients; all-cause death 23.3% HDF versus 27.0% HD, median 30 months, HR 0.84 (95% CI 0.74 to 0.95); lower risk with higher convection volume in a graded pattern. Text: post hoc and on-treatment analyses "show an association, not proof"; dose–response "drawn from volumes that patients achieved rather than volumes assigned at random, so it supports, but does not prove"; CONVINCE "addressed this directly by enrolling only patients able to receive high volumes and randomizing them".
- **Values left out (leanest version):** CONVINCE event counts (118 of 683, 148 of 677); Turkish 17.4-liter post hoc threshold; ESHOL secondary findings (fewer hypotensive sessions, fewer hospitalizations); CONVINCE quality-of-life results; the "required confirmation" wording.
- **Reviewer flags:** (1) Dense: six rows × four columns plus a footer band. If the hazard ratios or intervals come back garbled after two tries, use an HTML table (the page already has this table in HTML) and keep the image to the "Why results differed" band only. (2) The ESHOL comparator is "continued HD" (the text does not say low-flux or high-flux); the figure keeps that wording. (3) Pooled 2016 has no hazard ratio in the text, so only the percentages are shown.

```text
Clinical evidence reference card, 1536 × 1152 (4:3). Subject: randomized trials and pooled analyses comparing online hemodiafiltration (HDF) with hemodialysis (HD). Publication-grade table, white #ffffff background, flat design, no illustrations except tiny icons. Font: Inter throughout (never serif). Short lines; large enough to read on a phone.

TITLE BLOCK (top left):
- Title, bold navy #0f1e2e: "HDF versus HD: what the trials found"
- Subtitle, teal #1a6b72: "Outcome: death, unless stated"

TABLE (full width, rounded outer border, column headers in teal #1a6b72 on soft gray #f3f4f6, alternating white and very soft gray rows). Four columns: "Study" · "Patients and comparator" · "Result" · "Convection volume". Six rows:

Row 1: "CONTRAST (2012)" | "714 · vs low-flux HD" | "No significant difference" / "HR 0.95 (0.75–1.20)" | "Higher volume, lower mortality (on-treatment)"
Row 2: "Turkish online HDF study (2013)" | "782 · vs high-flux HD" | "Death or nonfatal cardiovascular event: no significant difference" / "Event-free 77.6% vs 74.8%" | "Mean about 17.2 L"
Row 3: "ESHOL (2013)" | "906 · vs continued HD" | "30% lower" / "HR 0.70 (0.53–0.92)" | "High-efficiency HDF"
Row 4 (highlighted with a thin teal left bar): "CONVINCE (2023)" | "1,360 · vs high-flux HD" / "All able to receive at least 23 L" | "17.3% vs 21.9% over median 30 months" / "HR 0.77 (0.65–0.93)" | "Mean 25.3 L delivered"
Row 5 (separated by a thin divider labeled "Pooled analyses"): "Pooled, 2016" | "4 trials · 2,793" | "14% lower death" / "23% lower cardiovascular death" | "Largest benefit above 23 L per 1.73 m²"
Row 6: "Pooled, 2024" | "5 trials · 4,153" | "23.3% vs 27.0% over median 30 months" / "HR 0.84 (0.74–0.95)" | "Graded: higher volume, lower risk"

Result cell styling: "No significant difference" cells in neutral gray-blue text #43536a; cells showing lower mortality in teal #1a6b72 bold. Percentages always written "HDF vs HD" order; add tiny gray header note above the Result column: "HDF vs HD".

LEGEND LINE (small gray, under the table): "HR = hazard ratio (95% confidence interval)"

Why the results differed BAND (full width, light teal fill #eef6f7, three boxes joined by navy arrows, small icons):
Box 1: "Neutral trials delivered lower volumes"
Box 2 (amber outline #b8860b, small "association" tag): "Higher achieved volume, better survival: an association, not proof"
Box 3 (teal outline): "CONVINCE randomized patients able to reach high volumes"
Under the band, one bold navy line: "Benefit shown for high-volume HDF, not for every patient or any volume"

FOOTER: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, outside the table.

DO NOT:
✗ No numbers other than those in quotation marks above; do not round, recompute, or convert any value.
✗ No word "proves", "proven", or "cause" applied to the volume finding.
✗ No "HDF benefits all patients" or "HD is unsafe" wording.
✗ No quality-of-life, hospitalization, or cost claims.
✗ No p-values, numbers needed to treat, or forest-plot drawing.
✗ No journal names, author names, or logos.
✗ Do not change comparators: CONTRAST is low-flux HD; Turkish and CONVINCE are high-flux HD; ESHOL is "continued HD".
✗ No country flags or maps.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render every label exactly as written in quotation marks above, spelled correctly, in Inter, including the en dash in each interval and "m²" with a superscript 2. Add no other text.

REPLACEMENT CONSTRAINTS
✗ No hyphenated slugs, code-style identifiers, or all-capital placeholder text anywhere; the lower heading reads exactly “Why the results differed”
```

**QA after generation:**
□ Six rows in order: CONTRAST, Turkish, ESHOL, CONVINCE, Pooled 2016, Pooled 2024
□ Sample sizes exact: 714, 782, 906, 1,360, 2,793, 4,153
□ Hazard ratios and intervals exact: 0.95 (0.75–1.20), 0.70 (0.53–0.92), 0.77 (0.65–0.93), 0.84 (0.74–0.95)
□ Percentages exact: 77.6 vs 74.8; 17.3 vs 21.9; 23.3 vs 27.0; 30%; 14%; 23%
□ Volumes exact: about 17.2 L; at least 23 L; 25.3 L; above 23 L per 1.73 m²
□ Comparators correct: low-flux (CONTRAST), high-flux (Turkish, CONVINCE), continued HD (ESHOL)
□ Volume–survival box says "an association, not proof"
□ No invented numbers, no QoL or hospitalization claims
□ Label spelling: hemodiafiltration abbreviations, cardiovascular, CONVINCE, ESHOL
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

**QA after regeneration (in addition to the checklist above):**
□ No hyphenated slugs, code-style identifiers, or all-capital placeholder text anywhere; the lower heading reads exactly “Why the results differed”

