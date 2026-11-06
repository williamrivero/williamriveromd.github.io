# Cancer Treatment and Your Kidneys — Image Plan and GPT Prompt Pack

**Guide:** `guides/onconephrology-chemotherapy-kidney.html` · **Production target:** ChatGPT Image Generator GPT · **Prepared:** November 6, 2026
**House rules applied to every prompt:** light backgrounds only · fonts Inter / Nunito Sans / IBM Plex Sans / Manrope only · American English · attribution `© renalcarematters.com` (public guide set) · `.png` masters + `.webp` twins at exact pixel size · no histology photographs, no invented numbers, no copied journal figures (ADQI 34 Figures 1–3 are redrawn as original schematics only).

---

## Part 1 — Image plan

### 1.1 Visual narrative

The guide teaches one idea: **the kidney is both the exit door and a target for cancer medicines**, so kidney-safe cancer care means measuring kidney function correctly, preventing injury drug by drug, and dosing together. Patient-tab images use plain words; clinician-tab images use standard abbreviations, each defined in the figure's `fig-abbrevs` list.

### 1.2 Asset register

Every asset below already ships as a **code-native interim** rendered from `image-prompts/onconephrology-chemotherapy-kidney-svg/make_figs.py` (SVG → PNG → WebP). Replace an interim only after the generated version passes QC.

| ID | File (`images/`) | Size | Skill | Placement | Tab | Status |
|---|---|---|---|---|---|---|
| 001 | `onconephrology-chemotherapy-kidney-vignette-hero.png` | 2048 × 2048 | hero-vignette v3 | Hero disc | Patient | Replace interim illustration |
| 002 | `onconephrology-chemotherapy-kidney-02-exit-door-target.png` | 1792 × 1024 | biomedical-mechanism-figure | `#why-kidneys` | Patient | Replace interim after QC |
| 003 | `onconephrology-chemotherapy-kidney-03-injury-pattern-map.png` | 1792 × 1024 | biomedical-mechanism-figure | `#md-drugs` | Clinician | Replace interim after QC |
| 004 | `onconephrology-chemotherapy-kidney-04-before-cisplatin-checklist.png` | 1792 × 1024 | algorithm-generator, Mode C | `#md-drugs` (cisplatin) | Clinician | Replace interim after QC |
| 005 | `onconephrology-chemotherapy-kidney-05-gfr-for-dosing.png` | 1792 × 1024 | algorithm-generator, Mode C | `#md-kidney-function` | Clinician | Replace interim after QC |
| 006 | `onconephrology-chemotherapy-kidney-og.png` | 1200 × 630 | infographic (OG card) | `og:image`, Latest strip | — | Replace interim card after QC |

### 1.3 Rules for the whole set

- **Words are exact.** Every on-image label is quoted in the prompt. Reject renders with misspelled, extra, or invented words; regenerate rather than edit pixels.
- **Numbers:** only those quoted in a prompt (the de-indexing formula, Calvert formula, and 125 mL/min cap in 005). No other percentages, doses, or thresholds.
- **No drug packaging, brands, or real likenesses.**
- **Attribution** bottom-right, small gray, ≥70% opacity.

---

## Part 2 — Prompts

### 001 — Hero vignette

```
FILE NAME: onconephrology-chemotherapy-kidney-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A people
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H — Clinical (one consultation scene, minimal supporting imagery)
CAMERA: wide environmental view from a slightly elevated over-the-shoulder angle behind the clinicians
HUMAN VARIATION (vs. previous guide): previous guide (AL amyloidosis) had no people (object hero, overhead). This hero introduces three people with deliberately different traits: a woman in her early 40s as the patient (slim build, short wavy black bob, warm medium-brown skin, oval face, light lavender knit cardigan, small pearl studs, seated reclined, calm attentive expression), a male nephrologist in his late 50s (stocky build, close-cropped graying hair, rectangular glasses, square jaw, navy scrub top under an open white coat, standing, holding a tablet), and a female oncologist in her early 30s (tall, long straight hair in a low ponytail, deeper tan skin, angular face, teal blouse, white coat, pointing to the tablet). Different age, sex mix, hairstyles, builds, clothing colors, posture, activity, environment, and camera angle from every recent hero.
AUDIENCE: mixed (patients and clinicians)
VISUAL GOAL: Two specialists planning together beside a calm patient in a chemotherapy chair — kidney-safe cancer care is a team plan.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H — Clinical. Camera: wide environmental view from a slightly elevated over-the-shoulder angle behind the two clinicians.

Subject: a bright, modern Philippine outpatient chemotherapy infusion suite. A Filipino woman in her early 40s (slim, short wavy black bob, warm medium-brown skin, oval face, light lavender knit cardigan, small pearl studs) sits reclined in a pale gray infusion chair with an IV line taped to her forearm, connected to a plain unlabeled IV bag on a pole; her expression is calm and attentive. In the foreground, seen partly from behind, a Filipino male nephrologist in his late 50s (stocky, close-cropped graying hair, rectangular glasses, navy scrub top under an open white coat) holds a tablet whose screen shows only an abstract soft-colored line chart with no readable text, while a Filipino female oncologist in her early 30s (tall, long straight hair in a low ponytail, deeper tan skin, teal blouse, white coat) points to it; both turn slightly toward the patient as if including her in the conversation. Soft natural daylight from a large window, gentle shallow depth of field, a small potted plant and a water tumbler on a side table.

Visual hierarchy: the three-person consultation occupies 60–70% of the circle (lower and right portions); 2–3 supporting elements (IV pole, side table with water, window light) 20–30%; reserve a 20–25% TITLE SAFE ZONE in the upper-left of the circle of soft, out-of-focus pale wall and window glow — no faces, hands, equipment, or objects inside that zone.

Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, readable screen text, drug names, logo, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, readable drug labels, rectangular borders, frames, banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible needles piercing skin, distressed or ill-appearing patient, hair loss caricature.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant consultation scene occupying 60–70% of the circle, 2–3 supporting elements, 20–25% empty title-safe zone upper-left. Filipino clinical context with three people whose traits differ from earlier heroes. Wide over-the-shoulder framing not used by the previous guide. No text anywhere, including the tablet screen and IV bag.
```

### 002 — The kidney is both the exit door and a target (patient)

```
Create a publication-grade biomedical mechanism schematic, 1792 × 1024 px (16:9), white background, review-article style, flat vector with soft semi-3D shading, clean sans-serif labels set in Inter (never a serif font).

Topic: How cisplatin injures the proximal tubule. Disease context: chemotherapy-associated kidney injury. Central mechanism: uptake faster than efflux causes intracellular accumulation, mitochondrial injury, and electrolyte wasting.

Title (top-left, navy #0f1e2e, bold): "The kidney is both the exit door and a target"
Subtitle (gray): "How cisplatin builds up inside a proximal tubule cell"

Organ-level panel (left, small): a simplified kidney in gray-blue with one nephron highlighted in pale yellow; a thin dashed connector box leads to the magnified panel. Label: "Kidney".

Magnified mechanism panel (center-right, dashed border): one large proximal tubule epithelial cell drawn as a rounded rectangle. Left edge = basolateral membrane facing a pale pink band labeled "Blood side"; right edge = brush-border (apical) membrane with short microvilli facing a pale yellow band labeled "Urine side".
- On the basolateral membrane, a wide teal channel labeled "Entry door (OCT2)" with a bold teal arrow carrying small teal dots (drug) into the cell.
- On the apical membrane, a narrow amber pump labeled "Exit pump (MATE1)" with a thin arrow and the small word "slower".
- Inside the cell, a cluster of teal dots labeled "Drug builds up".
- Two mitochondria drawn in soft red-orange with a small red jagged injury mark, labeled "Energy factories (mitochondria) injured".
- A red arrow from the cell toward the urine side carrying three small circles each marked "Mg", labeled "Magnesium, potassium, salt leak".

Bottom summary flow (three rounded boxes left to right with arrows):
Left pale-pink box: "Fast in, slow out"
Center pale-pink box: "Injury and electrolyte wasting"
Right pale-blue box: "Protection: fluids, magnesium, no NSAIDs"

Use only these words. Muted clinical palette: gray-blue anatomy, pale yellow tubule highlight, red for injury, teal for drug transport, blue for protective box. Generous whitespace, labels readable at slide size, thin dashed connectors. No photorealism, no dark background, no extra icons, no invented pathways or numbers. Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray.
```

### 003 — Where chemotherapy injures the nephron (clinician)

```
Create a publication-grade biomedical mechanism schematic, 1792 × 1024 px (16:9), white background, review-article style, flat vector, clean sans-serif labels set in Inter (never a serif font). This is an ORIGINAL schematic; do not reproduce any journal figure layout.

Title (top-left, navy, bold): "Where chemotherapy injures the nephron"
Subtitle (gray): "Lesion pattern predicts the clinical picture"

Main drawing: one simplified nephron running left to right — a glomerulus (circle of capillary loops, labeled "Glomerulus") on the left, then a curving tubule (pale yellow lumen with gray-blue wall) ending at the right edge with the label "to urine". Small amber diamond-shaped crystals sit inside the distal portion of the tubule lumen. Small purple dots sit in the interstitial space below the tubule.

Four callout boxes, each joined to its site by a thin dashed line of the same color:
1. Red box near the glomerular capillaries — header "Vessel lining (TMA)"; lines: "Gemcitabine, mitomycin C" / "Hypertension, hematuria," / "proteinuria, hemolysis"
2. Teal box above the proximal tubule — header "Proximal tubule (ATI)"; lines: "Cisplatin, ifosfamide," / "melphalan, pemetrexed" / "Creatinine rise, Mg and K" / "wasting, Fanconi syndrome"
3. Purple box below the interstitial dots — header "Interstitium"; lines: "MTX, pemetrexed: nephritis" / "Pemetrexed: chronic fibrosis"
4. Amber box near the crystals — header "Tubular lumen (crystals)"; lines: "High-dose MTX" / "Nonoliguric AKI," / "delayed drug clearance"

Small neutral gray note box at top-right: "Not covered by ADQI 34: checkpoint inhibitors (interstitial nephritis) and VEGF inhibitors (TMA, proteinuria)"
Small gray caption bottom-left: "Original schematic based on the pattern categories in ADQI 34 (Lentini et al., Kidney International 2026)."

Use only these words. No crossing connector lines, no text overlapping lines. Muted palette, generous whitespace. No histology, no photorealism, no dark background, no numbers. Footer "© renalcarematters.com" bottom-right in subtle gray.
```

### 004 — Before a nephrotoxic chemotherapy cycle (clinician)

```
Create a clean publication-ready clinical algorithm in the renalcarematters.com house style, 1792 × 1024 px landscape, white background, typography set in Inter (never a serif font), navy #0f1e2e text, thin teal #1a6b72 connector arrows, generous margins.

Title (top-left, navy, bold): "Before a nephrotoxic chemotherapy cycle"
Subtitle (gray): "Five checks, every cycle"

Five equal rounded-rectangle columns left to right, each with a numbered circle at top and a short header, joined by small right-pointing arrows:
1 (teal) "Kidney function method": "Stable? Start with eGFR" / "Low muscle: add cystatin C" / "High stakes: measure GFR" / "Dose on mL/min (de-index)"
2 (green #1f7a4d) "Magnesium and potassium": "Check and correct" / "before the dose" / "IV magnesium with" / "cisplatin hydration"
3 (blue) "Hydration plan": "IV fluid before and after" / "Alkaline urine for HD-MTX" / "Respect heart failure" / "and dialysis fluid limits"
4 (amber #b8860b) "Nephrotoxin review": "Stop NSAIDs" / "Review PPI, TMP-SMX," / "penicillins, contrast," / "aminoglycosides, herbals"
5 (purple) "Monitoring schedule": "Creatinine, electrolytes," / "urine every cycle" / "MTX levels for HD-MTX" / "BP, hemolysis for TMA drugs"

Full-width soft-gray rounded bar beneath the columns, centered navy text in two lines: "If creatinine rises: look for dehydration, obstruction, and other drugs first;" / "then delay, reduce, substitute, or rescue, as a shared oncology–nephrology decision."

Use only these words; all text must fit inside its box with padding. No icons, no doses, no other numbers. Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling.
```

### 005 — Choosing a kidney-function number for dosing (clinician)

```
Create a clean publication-ready clinical algorithm in the renalcarematters.com house style, 1792 × 1024 px landscape, white background, typography set in Inter (never a serif font), navy #0f1e2e text, thin teal connector arrows, generous margins.

Title (top-left, navy, bold): "Choosing a kidney-function number for anticancer dosing"
Subtitle (gray): "Aligned with KDIGO 2024 and ADDIKD 2025"

Row of four rounded boxes left to right joined by arrows:
1 (pale red border) header "Is kidney function stable?"; lines "Yes: continue to the right" / "No (evolving AKI): use kinetic" / "eGFR and clinical judgment"
2 (teal) header "Start: CKD-EPI eGFR"; lines "From creatinine" / "(not Cockcroft-Gault CrCl" / "for new assessments)"
3 (amber) header "Creatinine unreliable?"; lines "Low muscle, amputation," / "cachexia: add cystatin C" / "(eGFRcr-cys)"
4 (purple) header "High-stakes dose?"; lines "HD-MTX, high-dose cisplatin," / "curative carboplatin, extremes" / "of body size: measure GFR"

Full-width white box with navy border below the row:
"Then convert for dosing (de-index):"
Large teal formula line: "Absolute GFR (mL/min) = eGFR (mL/min/1.73 m²) × BSA ÷ 1.73"
Gray line: "Carboplatin (Calvert): dose = target AUC × (GFR + 25); cap estimated GFR at 125 mL/min"

Soft-gray bar at the bottom, centered navy text: "Cystatin C-based eGFR can read falsely low with cancer, inflammation, and steroids;" / "when creatinine and cystatin C disagree and the decision matters, measure GFR."

Reproduce the formulas character for character (superscript ², ×, ÷). No other numbers, no icons. Footer "© renalcarematters.com" bottom-right in subtle gray.
```

### 006 — OG card

```
Create a 1200 × 630 px social share card on a very light mint background (#f3f8f7), typography in Inter (never a serif font), renalcarematters.com house style.

Left two-thirds, left-aligned:
- small teal (#1a6b72) uppercase eyebrow: "ONCONEPHROLOGY"
- large bold navy (#0f1e2e) title on two lines: "Cancer Treatment" / "and Your Kidneys"
- slate subtitle on two lines: "Kidney-safe chemotherapy: risks, prevention," / "and dosing with CKD or dialysis"
- white rounded pill with teal outline and teal text: "Patients & Clinicians · EN TL CEB KAP"
- small gray byline: "W Rivero, MD · renalcarematters.com"

Right third: a soft pale-teal circle containing a calm, semi-flat illustration of a single kidney beside a plain IV drip bag (no labels) and one small water droplet, conveying protection rather than danger.

Use only these words. No photos of people, no drug names on the bag, no dark background, no extra icons. Keep all text inside a 60 px safe margin.
```

---

## Part 3 — After generation

1. Save PNG masters to `images/` with the exact file names, then create WebP twins (quality ~86).
2. Compare each against its interim and the QC rules above; keep the interim if the render has any text error.
3. No HTML changes are needed: the guide already references every file name and size listed in 1.2.
