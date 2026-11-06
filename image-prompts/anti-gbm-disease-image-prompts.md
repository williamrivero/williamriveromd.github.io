# Image prompt pack: Anti-GBM Disease (Goodpasture Disease)

Stage 1 output for `guides/anti-gbm-disease.html`. The guide already ships with **code-native interim figures** (source: `image-prompts/anti-gbm-disease-svg/make_figs.py` → `images/anti-gbm-disease-*.png/.webp`), so nothing is broken while these are generated. Paste each COPY-READY prompt into the ChatGPT Image Generator GPT, then save the result over the same filename (PNG master + WebP twin). Hand to `williamriveromd-local-image-generator` (Stage 2) for manifests if wanted.

House rules applied: light background; on-image text in Inter only; `renalcarematters.com` attribution bottom-right (except the wordless hero); no journal names, brand names, or invented numbers. Figure 05 (kidney-survival bar chart) is deliberately **not** in this pack: it carries study data (Floyd et al., 2023) and stays code-native so the numbers cannot drift.

---

## 001 — Vignette hero (patient mode only)

```
FILE NAME: anti-gbm-disease-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A people
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H — Clinical
CAMERA: over-the-shoulder (from behind the clinician, toward the patient)
HUMAN VARIATION (vs. previous guide: al-amyloidosis-kidneys used an anatomy still-life; born-small used no people): two people; young adult Filipino man (patient), late 20s, lean build, short undercut black hair, light stubble, oval face, medium-brown skin, wearing a pale-blue hospital gown, seated upright on an emergency-department stretcher with a nasal oxygen cannula, attentive worried-but-calm expression, one hand resting on a folded blanket; Filipina nephrologist seen from behind/three-quarter rear, mid-40s, shoulder-length wavy dark-brown hair tied low, white coat over a deep plum blouse, holding a tablet, slight forward lean; ≥12 traits differ from any prior hero
AUDIENCE: patients and families
VISUAL GOAL: A calm, urgent-but-reassuring emergency consultation: the doctor explaining why treatment is starting today.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder from behind the clinician.
Subject: a Filipino young adult man in his late 20s (lean build, short undercut black hair, light stubble, oval face, medium-brown skin, pale-blue hospital gown, nasal oxygen cannula) sitting upright on a clean emergency-department stretcher, listening attentively to a Filipina nephrologist in her mid-40s (shoulder-length wavy dark-brown hair tied low, white coat over a deep plum blouse) who is seen from behind at three-quarter rear and holds a tablet. In the soft-focus background, a plasma-exchange (apheresis) machine on a wheeled stand with neatly routed tubing and a blood-product bag on a pole, all unbranded. Bright, modern Philippine hospital emergency bay, soft daylight from a high window, gentle shallow depth of field.
Visual hierarchy: the patient's face and the doctor's shoulder form the hero subject at 60–70% of the circle; the apheresis machine and IV pole are small supporting context at 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft, blurred pale wall toward the upper-left of the circle with no faces, equipment, or icons inside it.
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Absolutely NO text of any kind: no title, subtitle, caption, label, screen text, logo, brand name on the machine, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, more than four supporting elements, readable screens or labels, cropped circle, faces cut by the circle edge, anything inside the title-safe zone, baked-in text, logos, brand names, watermarks, rectangular frames, dark or charcoal backgrounds, blood on the patient, coughing blood shown graphically, distressed or panicked expressions, cartoon style, neon, HDR, over-saturation, duplicated people, extra fingers, stock-photo smiling at camera.

QUALITY CHECK:
Square 2048×2048. Circle 85–90% of canvas with visible white margin, never cropped. One dominant subject at 60–70%, 2 supporting elements, 20–25% empty title-safe zone. No readable text anywhere. Filipino clinical context; ≥12 traits differ from previous guides; over-the-shoulder framing not used in the previous hero.

ALT TEXT: "" (decorative; the adjacent H1 carries the meaning).
```

---

## 002 — Mechanism figure (biomedical-mechanism-figure style)

```
IMAGE NUMBER: 002
SECTION PLACEMENT: #what-it-is (patient) and #md-pathophysiology (clinician)
FILE NAME: anti-gbm-disease-02-mechanism.png
ARCHETYPE: Review-article mechanism schematic — organ panel → magnified functional unit → molecular inset → injury → intervention → benefit
AUDIENCE: mixed (patients and clinicians)
ASPECT RATIO: 16:9 (1792 × 1024)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean, publication-grade flat-vector biomedical mechanism figure, 1792×1024, white background, muted clinical palette (renal pink, teal #1a6b72, navy #0f1e2e, soft purple for crescents, soft red for antibodies), thin consistent line weights, Inter sans-serif labels only.
LEFT PANEL (organ level): simple vector kidney and a pair of lungs side by side, each with a dashed magnification circle pointing right; small label "Kidney filters (glomeruli)" and "Lung air sacs (alveoli)".
CENTER-LEFT INSET (molecular): the collagen IV network drawn as a woven mesh; zoom on one NC1 hexamer made of six rounded subunits in teal/lavender/peach; a closed hexamer labeled "Target hidden" with small cross-link marks labeled "sulfilimine cross-links"; an arrow to an opened hexamer labeled "Hexamer opens" with two red dots labeled "α3 epitopes EA and EB"; Y-shaped IgG antibodies binding the red dots.
CENTER-RIGHT INSET (glomerulus): a glomerular capillary tuft with a thin teal ribbon lining the capillary walls labeled "Linear IgG"; an arrow to a second glomerulus where the capillary wall is ruptured, red cells and fibrin strands leak into Bowman space, and a lavender layered crescent of proliferating cells fills one side, labeled "Crescent"; small complement icons and two macrophage blobs.
RIGHT PANEL: three numbered green circles: "1 Remove antibodies — plasma exchange", "2 Stop new antibodies — cyclophosphamide, steroids", "3 Calm the injury — steroids, organ support".
BOTTOM FLOW (four rounded boxes with arrows): "Hidden α3 target exposed" → "Antibodies attack kidney ± lung" → "Crescents form within days" → "Early treatment saves filters".
Footer small gray text bottom-left: "Schematic for teaching." Bottom-right: "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No photorealism, no 3D gloss, no gradients heavier than subtle, no dark background, no journal or brand names, no numbers or percentages, no misspelled labels, no extra text beyond the labels listed, no cluttered icons, no cartoon faces.

QUALITY CHECK:
Every label above present and spelled exactly; Greek α rendered correctly; reading order left→right; bottom flow readable at 50% zoom; attribution present.

ALT TEXT: "Diagram: the hidden α3 target in the kidney and lung basement membrane is exposed, antibodies bind, inflammation forms a crescent, and treatment removes antibodies and stops new ones."
```

---

## 004 — First-24-hours algorithm (algorithm-generator style)

```
IMAGE NUMBER: 004
SECTION PLACEMENT: #md-treatment (clinician)
FILE NAME: anti-gbm-disease-04-first-24-hours.png
ARCHETYPE: AHA-style vertical clinical algorithm
AUDIENCE: clinicians
ASPECT RATIO: 8:9 (1600 × 1800)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean AHA-style clinical algorithm flowchart, 1600×1800, white background, seven full-width rounded rectangles stacked vertically and joined by short teal downward arrows, each with a large numbered colored circle on the left and an Inter bold heading plus two lines of regular body text. Title at top: "Suspected anti-GBM disease: the first 24 hours"; subtitle: "Do not let the biopsy schedule delay treatment".
Box 1 (red tint): "Suspect it" — "Rapidly rising creatinine with blood and protein in the urine, with or without coughing blood or new lung shadows".
Box 2 (teal tint): "Same-day tests" — "Anti-GBM antibody AND ANCA (MPO, PR3) together; urinalysis and sediment, creatinine, potassium, CBC; chest X-ray or CT".
Box 3 (amber tint): "High suspicion? Start now" — "Glucocorticoids; plasma exchange if it can start, even before results return (KDIGO Practice Point 11.2.1)".
Box 4 (teal tint): "Kidney biopsy, early" — "Linear IgG confirms; crescent count and normal glomeruli guide prognosis. Add 300–600 mL fresh plasma within 3 days of biopsy".
Box 5 (green tint): "Full course" — "Daily plasma exchange until antibody negative (about 14 days); oral cyclophosphamide 2–3 months; steroids about 6 months".
Box 6 (purple tint): "Decide on the edge cases" — "Dialysis-dependent + 100% crescents or >50% sclerosis + no lung bleeding: KDIGO exception; consider a short trial or supportive care".
Box 7 (navy tint): "Follow-up" — "Double-positive: maintenance as for ANCA vasculitis. No smoking. Transplant only after antibodies are negative for 6 months or more".
Footer: "Summary of KDIGO 2021 Chapter 11 and McAdoo & Pusey (2025). Individualize for each patient." Bottom-right: "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No icons inside boxes, no drug brand names, no additional doses or numbers beyond those listed, no dark background, no 3D, no shadows heavier than subtle, no misspellings.

QUALITY CHECK:
All seven boxes present in order with exact wording; arrows connect each box; text legible at mobile width.
```

---

## 003 — Variant map

Use `williamriveromd-simple-figure` Scaffold E (2 × 2 reference grid) with the exact wording rendered in the interim figure (`image-prompts/anti-gbm-disease-svg/anti-gbm-disease-03-variant-map.svg`). Keep the closing caption: "Associations with drugs and vaccines are reported cases; cause has not been proven."
