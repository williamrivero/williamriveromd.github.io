# Renal Dietitian track: replacement image prompts

Audit of the November 24, 2026 batch (`~/Documents/Renal Dietitians/Images`): 41 of 45 images passed and were placed. The four below were held back; their pages show nothing in their place until a replacement passes audit.
Save each replacement under the same file name (PNG, 1672 × 941) in `~/Documents/Renal Dietitians/Images/Corrected`. Each prompt is the original Constitution v1.0 prompt with a correction block at the top and matching items added to Layers E and G.

| File | Why it was held back |
|---|---|
| `renal-dietitian-03-nutrition-focused-exam.png` | The thigh marker (6) sits on the knee and the calf marker (7) sits on the front of the shin. |
| `renal-dietitian-04-protein-ladder.png` | The word "kidney" in the top rung renders as a garbled glyph ("(‹idney"). |
| `renal-dietitian-10-cloudy-effluent.png` | Both drain bags hang high on an IV pole, which reads as fluid being infused rather than drained. |
| `renal-dietitian-14-supplement-bag-review.png` | Star fruit is labeled "Foods to discuss with the kidney team"; the module says to avoid it completely. The trays are empty. |

## `renal-dietitian-03-nutrition-focused-exam.png`

**Held back:** The thigh marker (6) sits on the knee and the calf marker (7) sits on the front of the shin.

### rd03_nfpe

**Alt:** An adult figure showing sites to check for muscle loss, fat loss, and edema, with a grip dynamometer.
**Caption:** Nutrition-focused physical examination sites, and grip strength on the arm without the fistula.

```
CORRECTION (supersedes anything below that conflicts):
- Marker 6 (thigh, quadriceps) sits on the FRONT of the mid-thigh, halfway between hip and knee, never on the knee
- Marker 7 (calf, gastrocnemius) sits on the BACK of the lower leg; show it on the back view (posterior), never on the shin
- Marker 9 (triceps) sits on the BACK of the upper arm; show it on the back view

Visual aid, landscape 16:9, 1672 x 941 px, dual audience (renal dietitians and patients/families). Renal Care Academy, Renal Dietitian track.
Subject: Nutrition-focused physical examination sites, and grip strength on the arm without the fistula.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
- Human figures: Filipino adults, realistic proportions, respectful clothing; no anatomy visible through opaque skin
- Food: Philippine dishes drawn accurately (rice, fish, tokwa, monggo, tinola, sinigang, calamansi); realistic household portions
- Numbers shown in the image must match the module text exactly

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Landscape 16:9; reading order left to right, top to bottom
- Anterior view conventions for any body figure: patient's right = image left
- Keep a clear 4% margin; bottom-right corner reserved for the attribution footer

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Front and back views of a clothed, seated older Filipino man (respectful, realistic). Numbered teal dots: temples, collarbone, shoulder, scapula, interosseous hand, thigh, calf (muscle); orange dots: triceps, under-eye (fat); blue dots: ankle, sacrum (edema). Inset: hand gripping a dynamometer on the non-access arm; the other forearm shows an arteriovenous fistula with a small 'Do not use this arm' note. Legend panel right.
- Label format: Medical term (plain English) wherever a technical term appears
- Attribution footer: "© renalcarematters.com" bottom-right, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable (no imaging modality shown). If any scan is added later, apply Constitution v1.0 Layer D rules.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy
✗ No flat vector or clip-art style; painterly editorial illustration with soft natural light (house style)
✗ No cartoon faces or mascots
✗ No garbled or unreadable text; every label in clean DM Sans / DM Mono
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer: © renalcarematters.com appears on every image
✗ No altered attribution text: not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, rendered large, centered, or in any color other than navy #1F3864
✗ No real brand names, logos, or identifiable real people
✗ No British spellings in labels (use American English: hemodialysis, color, liter)
✗ No anatomy visible through skin
✗ Fistula only on the arm not used for grip
✗ No nudity; patient wears simple clothing
✗ No muscle-site marker on a joint (knee, elbow) or on bone (shin)
✗ Calf and triceps markers not on the front view

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Brenner & Rector's The Kidney (concepts); KDOQI/KDIGO visual summaries; Netter (any anatomy)
- Painterly editorial illustration, warm natural light, white or very light background
- Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C
- Typography: DM Sans (plain English labels) · DM Mono (numbers, units, medical terms)
- Attribution footer: "© renalcarematters.com" — bottom right, small, navy #1F3864, DM Sans, exact lowercase string

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Style is illustrated (painterly), not flat vector — confirmed
□ All labels legible and spelled in American English — confirmed
□ Medical term paired with a plain-English label throughout — confirmed
□ No prompt text visible in the generated image — confirmed
□ Three color groups with legend — confirmed
□ Grip on the non-access arm — confirmed
□ Edema at ankle and sacrum — confirmed
□ Marker 6 on the anterior mid-thigh — confirmed
□ Markers 7 and 9 on the posterior view — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## `renal-dietitian-04-protein-ladder.png`

**Held back:** The word "kidney" in the top rung renders as a garbled glyph ("(‹idney").

### rd04_protein_ladder

**Alt:** A ladder of protein targets in g/kg/day from very low-protein with ketoanalogues to post-transplant and ICU levels, with the guideline for each.
**Caption:** Protein targets differ by stage, treatment, and illness. Know which rung your patient is on.

```
CORRECTION (supersedes anything below that conflicts):
- Top rung text exactly: "Critical illness or kidney replacement therapy (KRT), e.g., dialysis in the ICU"
- Keep all six rungs, numbers, and gram values exactly as in Layer C

Visual aid, landscape 16:9, 1672 x 941 px, dual audience (renal dietitians and patients/families). Renal Care Academy, Renal Dietitian track.
Subject: Protein targets differ by stage, treatment, and illness. Know which rung your patient is on.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
- Human figures: Filipino adults, realistic proportions, respectful clothing; no anatomy visible through opaque skin
- Food: Philippine dishes drawn accurately (rice, fish, tokwa, monggo, tinola, sinigang, calamansi); realistic household portions
- Numbers shown in the image must match the module text exactly

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Landscape 16:9; reading order left to right, top to bottom
- Anterior view conventions for any body figure: patient's right = image left
- Keep a clear 4% margin; bottom-right corner reserved for the attribution footer

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Vertical ladder graphic, bottom to top: 0.28–0.43 (VLPD + ketoanalogues, KDOQI, supervised); 0.55–0.60 (LPD, KDOQI, stable, no diabetes); 0.6–0.8 (diabetes, KDOQI opinion); 0.8 (KDIGO 2024 / ADA 2026, CKD G3–G5); 1.0–1.2 (HD and PD, KDOQI); 1.3–1.7 (critical illness / KRT, ESPEN). Side callouts: 'Frail older adult: consider higher (KDIGO)' and 'Metabolically unstable: do not restrict'. Small food icons per rung showing approximate plate for a 60 kg person.
- Label format: Medical term (plain English) wherever a technical term appears
- Attribution footer: "© renalcarematters.com" bottom-right, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable (no imaging modality shown). If any scan is added later, apply Constitution v1.0 Layer D rules.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy
✗ No flat vector or clip-art style; painterly editorial illustration with soft natural light (house style)
✗ No cartoon faces or mascots
✗ No garbled or unreadable text; every label in clean DM Sans / DM Mono
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer: © renalcarematters.com appears on every image
✗ No altered attribution text: not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, rendered large, centered, or in any color other than navy #1F3864
✗ No real brand names, logos, or identifiable real people
✗ No British spellings in labels (use American English: hemodialysis, color, liter)
✗ No rung numbers different from specified
✗ No implication that lower is always better
✗ No brand names
✗ No malformed letters; re-check every word in all six rungs

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Brenner & Rector's The Kidney (concepts); KDOQI/KDIGO visual summaries; Netter (any anatomy)
- Painterly editorial illustration, warm natural light, white or very light background
- Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C
- Typography: DM Sans (plain English labels) · DM Mono (numbers, units, medical terms)
- Attribution footer: "© renalcarematters.com" — bottom right, small, navy #1F3864, DM Sans, exact lowercase string

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Style is illustrated (painterly), not flat vector — confirmed
□ All labels legible and spelled in American English — confirmed
□ Medical term paired with a plain-English label throughout — confirmed
□ No prompt text visible in the generated image — confirmed
□ Six rungs in correct order — confirmed
□ Guideline label on each rung — confirmed
□ Two side callouts present — confirmed
□ Top rung reads "kidney replacement therapy" with every letter intact — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## `renal-dietitian-10-cloudy-effluent.png`

**Held back:** Both drain bags hang high on an IV pole, which reads as fluid being infused rather than drained.

### rd10_cloudy

**Alt:** Two peritoneal dialysis drain bags side by side, one clear and one cloudy, with a stop sign and a phone.
**Caption:** Cloudy fluid means call the PD team now. Keep the bag.

```
CORRECTION (supersedes anything below that conflicts):
- Drained effluent bags lie flat on a clean towel on the FLOOR or a low stool, BELOW the level of the patient's abdomen
- No IV pole in the scene
- Clear bag: newspaper print visible through it but not legible; cloudy bag: milky, opaque

Visual aid, landscape 16:9, 1672 x 941 px, dual audience (renal dietitians and patients/families). Renal Care Academy, Renal Dietitian track.
Subject: Cloudy fluid means call the PD team now. Keep the bag.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
- Human figures: Filipino adults, realistic proportions, respectful clothing; no anatomy visible through opaque skin
- Food: Philippine dishes drawn accurately (rice, fish, tokwa, monggo, tinola, sinigang, calamansi); realistic household portions
- Numbers shown in the image must match the module text exactly

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Landscape 16:9; reading order left to right, top to bottom
- Anterior view conventions for any body figure: patient's right = image left
- Keep a clear 4% margin; bottom-right corner reserved for the attribution footer

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Two drain bags hanging, left clear (newspaper text visible through it, unreadable), right cloudy. Red stop panel: 'Cloudy fluid, belly pain, or fever: call the PD team now. Keep the bag.' Phone icon. Small text: 'Nutrition can wait'.
- Label format: Medical term (plain English) wherever a technical term appears
- Attribution footer: "© renalcarematters.com" bottom-right, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable (no imaging modality shown). If any scan is added later, apply Constitution v1.0 Layer D rules.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy
✗ No flat vector or clip-art style; painterly editorial illustration with soft natural light (house style)
✗ No cartoon faces or mascots
✗ No garbled or unreadable text; every label in clean DM Sans / DM Mono
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer: © renalcarematters.com appears on every image
✗ No altered attribution text: not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, rendered large, centered, or in any color other than navy #1F3864
✗ No real brand names, logos, or identifiable real people
✗ No British spellings in labels (use American English: hemodialysis, color, liter)
✗ No legible newspaper text
✗ No blood-colored fluid
✗ No dramatic gore
✗ No PD bag hanging above the patient
✗ No IV pole
✗ No tubing connecting a cloudy bag to the patient

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Brenner & Rector's The Kidney (concepts); KDOQI/KDIGO visual summaries; Netter (any anatomy)
- Painterly editorial illustration, warm natural light, white or very light background
- Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C
- Typography: DM Sans (plain English labels) · DM Mono (numbers, units, medical terms)
- Attribution footer: "© renalcarematters.com" — bottom right, small, navy #1F3864, DM Sans, exact lowercase string

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Style is illustrated (painterly), not flat vector — confirmed
□ All labels legible and spelled in American English — confirmed
□ Medical term paired with a plain-English label throughout — confirmed
□ No prompt text visible in the generated image — confirmed
□ Clear vs cloudy contrast — confirmed
□ Stop panel with keep-the-bag instruction — confirmed
□ Phone icon — confirmed
□ Both drain bags below abdomen level, on floor or low stool — confirmed
□ No IV pole — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

## `renal-dietitian-14-supplement-bag-review.png`

**Held back:** Star fruit is labeled "Foods to discuss with the kidney team"; the module says to avoid it completely. The trays are empty.

### rd14_bag

**Alt:** Supplements sorted into four trays: needed, harmless, duplicate, and risky, with star fruit and kamias in a red danger box.
**Caption:** Review the bag item by item. Star fruit and kamias are dangerous in kidney disease.

```
CORRECTION (supersedes anything below that conflicts):
- Danger box heading exactly: "AVOID: star fruit and kamias"
- Sub-labels: "Balimbing (star fruit): oxalate and a nerve toxin"; "Kamias (bilimbi): oxalate"
- Products sorted INTO the trays: Needed (green): one generic "Renal vitamin" bottle; Duplicate (amber): two calcium bottles; Higher risk (red): Vitamin A 5,000 IU, Vitamin C 1,000 mg, Magnesium, Noni juice, Detox tea

Visual aid, landscape 16:9, 1672 x 941 px, dual audience (renal dietitians and patients/families). Renal Care Academy, Renal Dietitian track.
Subject: Review the bag item by item. Star fruit and kamias are dangerous in kidney disease.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
- Human figures: Filipino adults, realistic proportions, respectful clothing; no anatomy visible through opaque skin
- Food: Philippine dishes drawn accurately (rice, fish, tokwa, monggo, tinola, sinigang, calamansi); realistic household portions
- Numbers shown in the image must match the module text exactly

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Landscape 16:9; reading order left to right, top to bottom
- Anterior view conventions for any body figure: patient's right = image left
- Keep a clear 4% margin; bottom-right corner reserved for the attribution footer

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Four trays labeled Needed (green), Harmless (gray), Duplicate (amber), Risky (red). Risky tray: vitamin A 5,000 IU bottle, vitamin C 1,000 mg, magnesium, noni juice, 'detox' tea (generic labels). Separate red box: star fruit (balimbing) and kamias with 'Avoid: oxalate and nerve toxin'. Magnifier over one label.
- Label format: Medical term (plain English) wherever a technical term appears
- Attribution footer: "© renalcarematters.com" bottom-right, small (10–12 px at final size), navy #1F3864, DM Sans, clear of all content

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable (no imaging modality shown). If any scan is added later, apply Constitution v1.0 Layer D rules.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No mirrored anatomy
✗ No flat vector or clip-art style; painterly editorial illustration with soft natural light (house style)
✗ No cartoon faces or mascots
✗ No garbled or unreadable text; every label in clean DM Sans / DM Mono
✗ No prompt text or metadata visible in the image
✗ No missing attribution footer: © renalcarematters.com appears on every image
✗ No altered attribution text: not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping content, rendered large, centered, or in any color other than navy #1F3864
✗ No real brand names, logos, or identifiable real people
✗ No British spellings in labels (use American English: hemodialysis, color, liter)
✗ No real brand names
✗ Star fruit drawn accurately (five ridges, star cross-section)
✗ No skull imagery
✗ No softened wording such as "discuss" or "limit" for star fruit
✗ No empty trays

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Brenner & Rector's The Kidney (concepts); KDOQI/KDIGO visual summaries; Netter (any anatomy)
- Painterly editorial illustration, warm natural light, white or very light background
- Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C
- Typography: DM Sans (plain English labels) · DM Mono (numbers, units, medical terms)
- Attribution footer: "© renalcarematters.com" — bottom right, small, navy #1F3864, DM Sans, exact lowercase string

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Style is illustrated (painterly), not flat vector — confirmed
□ All labels legible and spelled in American English — confirmed
□ Medical term paired with a plain-English label throughout — confirmed
□ No prompt text visible in the generated image — confirmed
□ Four trays colored — confirmed
□ Star fruit and kamias in danger box — confirmed
□ Generic labels only — confirmed
□ Danger heading reads "AVOID" — confirmed
□ Each product sits in its tray — confirmed
□ Attribution footer present in bottom-right corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```
