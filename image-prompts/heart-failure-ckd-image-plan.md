# Image Plan — `heart-failure-ckd.html`
### Heart Failure & Chronic Kidney Disease — williamriveromd.com

**Stage 1 prompt pack.** Six figures, each authored with the correct house skill.
Generate in the [ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator),
save outputs to `images/`, then run Stage 2 (`williamriveromd-local-image-generator`)
for manifests + `og:image` wiring.

House rules applied to every prompt: **light background only**, navy/teal/green/amber/red
palette, mobile-readable labels, and the mandatory `williamriveromd.com` attribution
bottom-right (bottom-center for portrait).

---

## Plan overview

| # | Section | File | Skill | Type | Size | Status |
|---|---------|------|-------|------|------|--------|
| 1 | `#overview` (hero) | `heart-failure-ckd-hero.png` | infographic | Editorial/semi-3D hero | 1536×1024 | **referenced in HTML** (replaces hero `<figure>`) |
| 2 | `#common-soil` | `heart-failure-ckd-common-soil-mechanism.png` | mechanism-figure | Review-article mechanism | 1792×1024 | new figure |
| 3 | `#crs` | `heart-failure-ckd-cardiorenal-types.png` | simple-figure | Reference card (Scaffold E) | 1536×1152 | new figure |
| 4 | `#egfr-dip` | `heart-failure-ckd-egfr-dip.png` | simple-figure | Comparison (Scaffold B) | 1792×1024 | **fills existing placeholder (Figure 2)** |
| 5 | `#treatment` | `heart-failure-ckd-four-pillars.png` | infographic | Clinician reference / 4-panel | 1792×1024 | new figure |
| 6 | OG / social share | `heart-failure-ckd-og.png` | infographic | OG card | 1200×630 | recommended (replace hero as `og:image`) |

> Figures 1 and 4 already have slots in the HTML (the hero `<figure>` and the
> `img-placeholder` in the eGFR-dip section). Figures 2, 3, 5 are enhancements —
> drop them into their sections as `<figure>` blocks with a `<figcaption><p class="fig-desc">…`.

---

## 1 · Hero — the cardiorenal connection
*Skill: williamriveromd-infographic-skill · Archetype 1 (editorial hero, conceptual semi-3D)*

```
FILE NAME: heart-failure-ckd-hero.png
IMAGE TYPE: Semi-photorealistic 3D conceptual editorial hero
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024   (matches the guide's wired <img> + current og:image tags)
AUDIENCE: patients (mixed)
VISUAL MIX:
- photorealistic models: none (conceptual)
- 2D infographic: minimal (one subtle directional arrow motif)
- 3D component graphics: anatomical heart + kidney + connecting vessel
- algorithm/flowchart: none

PURPOSE: Convey at a glance that heart and kidney share one circulation — when one weakens it drags the other down (the two-way cardiorenal connection).
KEY CONCEPTS: shared circulation · bidirectional injury · cardiorenal connection
DIMENSIONS: 1536 × 1024

COPY-READY IMAGE GENERATOR GPT PROMPT:
Semi-photorealistic 3D medical editorial hero for a nephrology patient-education guide, on a clean white-to-very-light-teal (#eef6f7) gradient background. Show one anatomically accurate human heart on the left and one human kidney on the right, both rendered as soft, publication-grade semi-3D medical models with natural anatomical color (muted anatomical red heart, red-brown kidney). Connect the two organs with a SINGLE continuous looping blood vessel that leaves the heart as an artery, curves to the kidney, and returns as a vein — forming a smooth closed loop between them. Along the loop, add a restrained two-headed teal arrow to imply that each organ affects the other (bidirectional). Soft, bright, even clinical lighting; gentle shadows; calm and trustworthy mood. Preserve generous negative space in the upper-left for a title overlay. Restrained palette: anatomical reds, muted kidney brown, clinical teal (#1a6b72) accents, navy (#0f1e2e) only for the small label. Mobile-safe centered composition. Do NOT embed a headline; only render the small attribution "williamriveromd.com" in semi-transparent navy text in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, clinically plausible, visually calm, publication-grade, consistent with williamriveromd.com. Light background. Attribution visible bottom-right.
```

---

## 2 · "Common soil" mechanism — how both organs are injured together
*Skill: williamriveromd-biomedical-mechanism-figure*

```
FILE NAME: heart-failure-ckd-common-soil-mechanism.png
IMAGE TYPE: Publication-grade biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Show that shared cardiometabolic risk factors drive four overlapping mechanisms that injure BOTH heart and kidney — and where shared therapies interrupt the cycle.

COPY-READY PROMPT:
Create a publication-grade biomedical mechanism schematic in scientific review-article style on a pure white background, flat vector illustration with soft semi-3D shading, muted clinical palette, thin dashed connector boxes, clean sans-serif labels, generous whitespace.

Topic: The "common soil" of heart failure and chronic kidney disease.
Disease context: Coexisting HF + CKD (cardiorenal syndrome).
Central mechanism: Shared cardiometabolic risk factors generate inflammation, endothelial dysfunction, neurohormonal activation, and hemodynamic stress that injure both organs.

ORGAN-LEVEL PANEL (left):
Show a simplified human heart and a kidney side by side in light gray-blue, joined by the aorta and renal artery/vein. Label the pair "HF + CKD". Add a thin dashed connector box pointing to the magnified panel.

MAGNIFIED MECHANISM PANEL (center, inside a dashed border):
Show two stacked magnified units — (a) a blood-vessel wall / endothelium segment, and (b) a glomerulus with a nephron tubule. Highlight affected segments in pale yellow. Concise callouts:
- ↑ Inflammation · ↑ ROS / oxidative stress · immune-cell activation
- Endothelial dysfunction
- ↑ RAAS · ↑ SNS (neurohormonal activation)
- ↑ Venous congestion · ↑ central venous pressure · ↓ renal perfusion (hemodynamic)
Use red for injury/oxidative-stress arrows, blue for protective/therapeutic arrows.

BOTTOM SUMMARY FLOW (left → center → right, arrows between):
- Left pale-pink pathology box "SHARED DRIVERS": Obesity · Diabetes (insulin resistance) · Hypertension
- Center box "COMMON SOIL": inflammation · endothelial dysfunction · neurohormonal activation · hemodynamic stress → end-organ fibrosis in heart AND kidney
- Right pale-blue benefit box "SHARED THERAPIES INTERRUPT THE CYCLE": SGLT2 inhibitors · RAAS inhibitors / ARNI · finerenone · GLP-1 RA → ↓ inflammation, ↓ congestion, ↓ fibrosis → protect both organs

Use a white background, muted clinical colors, clean sans-serif labels, thin dashed connector lines, review-article figure style. Small semi-transparent navy "© williamriveromd.com" bottom-right. Avoid photorealism, dark backgrounds, decorative elements, and overcrowding.

NEGATIVE INSTRUCTIONS:
No photorealism, no dark/navy/black backgrounds, no decorative gradients or shadows, no cartoon styling, no gibberish text, no overcrowding. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Anatomically plausible, mechanistically accurate (no invented pathways), labels readable at slide size, calm muted palette, white background, attribution present.
```

---

## 3 · The five types of cardiorenal syndrome
*Skill: williamriveromd-simple-figure · Scaffold E (reference card)*

```
FILE NAME: heart-failure-ckd-cardiorenal-types.png
IMAGE TYPE: Scaffold E — Reference / quick-look card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: mixed
VISUAL GOAL: Summarise the five Ronco types of cardiorenal syndrome — which organ fails first, how fast, with a plain example.

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background. Bold navy (#0f1e2e) title at top: "Cardiorenal Syndrome — The Five Types". Compact, well-organized five-row table. Column headers in clinical teal (#1a6b72) on a soft gray (#f3f4f6) band: "Type", "What fails first", "Plain example". Rows, with a small colored left accent tab per row:
- Type 1 — Acute cardiorenal (teal tab): "Heart, suddenly" — a sudden heart attack or heart-failure flare triggers rapid acute kidney injury.
- Type 2 — Chronic cardiorenal (teal tab): "Heart, slowly" — a long-standing weak heart slowly grinds kidney function down.
- Type 3 — Acute renocardiac (amber tab): "Kidney, suddenly" — a sudden kidney injury overloads the heart, causing heart failure or dangerous potassium.
- Type 4 — Chronic renocardiac (amber tab): "Kidney, slowly" — long-standing CKD strains and thickens the heart, raising heart-attack and heart-failure risk.
- Type 5 — Secondary (soft purple #6c3d8e tab): "Both, from outside" — a whole-body illness (e.g. severe infection, diabetes) damages heart and kidney at once.
Alternating row fills (white / very soft gray). A small heart icon and kidney icon beside the relevant "what fails first" cell, with a subtle directional arrow (heart→kidney for types 1–2, kidney→heart for types 3–4, both for type 5). Footer takeaway in navy: "In real patients the types blur — what matters is that the damage runs both ways." Mobile-readable, not cluttered. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, clinically accurate type definitions, calm, publication-grade, white background, attribution bottom-right.
```

---

## 4 · The eGFR "dip" — safe vs concerning
*Skill: williamriveromd-simple-figure · Scaffold B (side-by-side comparison) — fills the existing Figure 2 placeholder*

```
FILE NAME: heart-failure-ckd-egfr-dip.png
IMAGE TYPE: Scaffold B — side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (mixed)
VISUAL GOAL: Distinguish the harmless, expected eGFR "dip" after starting a protective heart medicine from a true, ongoing decline.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white (#ffffff) background. Centered bold navy (#0f1e2e) title: "After Starting a Heart Medicine: Is the eGFR Dip OK?". A soft dashed vertical divider splits the canvas into two equal panels, each containing a small clean line-chart of eGFR (y-axis) over time (x-axis) with a vertical "medicine started" marker.
LEFT panel labeled in renal green (#1f7a4d): "EXPECTED DIP — usually safe". The line steps down by a small amount (≤30%) right after the marker, then flattens into a stable plateau. Caption bullets: "Small early drop (up to ~30%)", "Then stabilises", "A pressure change inside the filter — not damage", "➜ Continue the medicine; it protects heart & kidney".
RIGHT panel labeled in clinical red (#b91c1c): "ONGOING DECLINE — investigate". The line keeps falling steadily after the marker without recovering. Caption bullets: "Drop greater than ~30%, or keeps falling", "Red flags: high potassium, dehydration, very low BP", "➜ Don't stop on your own — call your doctor to look for another cause".
Rounded panel corners, ample negative space, mobile-readable labels ≥11pt, clean axis lines in navy. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic chart noise, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, clinically sound message (treat symptoms/volume not the creatinine number), calm, publication-grade, white background, attribution bottom-right.
```

---

## 5 · The four pillars of shared heart-kidney therapy
*Skill: williamriveromd-infographic-skill · Archetype 5 (clinician reference) / 4-panel*

```
FILE NAME: heart-failure-ckd-four-pillars.png
IMAGE TYPE: Clinician reference / multi-panel infographic ("four pillars" metaphor)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL MIX:
- photorealistic models: none
- 2D infographic: primary (four pillar columns + header)
- 3D component graphics: small heart + kidney models at top
- algorithm/flowchart: none

PURPOSE: Show the modern medicines that protect heart AND kidney together, with the eGFR level each can be started at and its landmark trial.
KEY CONCEPTS: SGLT2i · RAASi/ARNI · finerenone/MRA · GLP-1 RA · dual-organ protection · eGFR thresholds
DIMENSIONS: 1792 × 1024

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient-and-clinician education infographic, landscape 16:9, clean modern nephrology design, white (#ffffff) background. At the top center, a small semi-3D human heart and human kidney sit side by side beneath a bold navy (#0f1e2e) header: "Four Pillars That Protect Heart AND Kidney". Below them, four tall rounded "pillar" columns of equal height (a temple-pillar metaphor) visually supporting the two organs. Each pillar has a colored top cap, an icon, a bold name, a green "Heart + Kidney" dual badge, the eGFR level to start, and its key trial:
1. Teal pillar — "SGLT2 inhibitors" (dapagliflozin, empagliflozin) · start at eGFR ≥ 20 · ~25% fewer HF hospitalisations/CV deaths · trials: DAPA-HF, DELIVER, EMPEROR.
2. Navy pillar — "RAAS blockers: ACEi / ARB / ARNI" · continue even as eGFR falls · relax vessels, cut protein leak · watch potassium.
3. Amber pillar — "Finerenone (nsMRA)" · start at eGFR ≥ 25 · calms scarring hormone · trial: FINEARTS-HF, FIDELIO/FIGARO.
4. Green pillar — "GLP-1 agonists" (semaglutide) · helps weight, sugar, kidney · trial: FLOW (24% fewer kidney events).
Across the base of the four pillars, a soft gray (#f3f4f6) foundation strip labeled in navy: "Foundation: diuretics relieve fluid (symptoms) · beta-blocker for the weak-pump type · treat symptoms & volume, not the creatinine number." Color logic: teal/navy/amber/green per pillar, clinical red used only for a small caution note about potassium. Rounded cards, strong hierarchy, generous whitespace, mobile-readable labels. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, clinically accurate thresholds, visually calm, publication-grade, white background, attribution bottom-right.
```

---

## 6 · OG / social share card *(recommended)*
*Skill: williamriveromd-infographic-skill · OG card (fixed 1200×630)*

> Currently the guide reuses the hero as `og:image`. For best link previews,
> generate this dedicated 1200×630 card and update the meta tags to point to it
> (`og:image`, `og:image:width="1200"`, `og:image:height="630"`, `twitter:image`).

```
FILE NAME: heart-failure-ckd-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630   (fixed — non-negotiable for OG)
AUDIENCE: mixed
VISUAL GOAL: A crisp, legible social-share card for the guide.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Open-graph social share card, 1200×630, off-white (#fafafa) background. Left two-thirds: bold condensed navy (#0f1e2e) title "Heart Failure & Chronic Kidney Disease", with a clinical-teal (#1a6b72) subtitle "When two organs fail together — and the medicines that protect both." A thin teal rule under the title. Right third: a clean semi-3D human heart and kidney joined by a single looping vessel with a small two-headed teal arrow (echoing the hero). Small "W. G. M. Rivero, MD · williamriveromd.com" lockup in navy at the bottom-left. Lots of negative space, crisp at thumbnail size, no clutter. Attribution "williamriveromd.com" small semi-transparent navy, bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid clutter, tiny text, AI gibberish, dark/navy/black backgrounds (light only), excessive saturation. Never omit the williamriveromd.com attribution. Keep dimensions exactly 1200×630.

QUALITY CHECK:
Legible at small thumbnail size, light background, correct 1200×630, attribution present.
```

---

## After generating

1. Drop the PNGs (plus `.webp` copies) into `images/`.
2. Figures 2, 3, 5 — insert as `<figure>` blocks in their sections with a
   `<figcaption><p class="fig-desc">…</p></figcaption>` (the lightbox reads `.fig-desc`).
3. Re-run `python3 patch_hero_fetchpriority.py --guide heart-failure-ckd.html`,
   `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, `patch_image_lightbox.py`.
4. If using the dedicated OG card (#6), update the four `og:image`/`twitter:image`
   tags to `heart-failure-ckd-og.png` at 1200×630.
5. Optionally run Stage 2 — `williamriveromd-local-image-generator` — to build the
   manifest and verify the `og:image` wiring.

---
---

# Part B — Clinician Mode figures (English only)

Six figures for the **clinician (physician) mode** of the guide. These are denser,
publication-grade, English-only reference assets — but they still obey the house
**light-background rule** (navy is heading/accent only, never a fill). Each drops
into its `mode-physician` section as a `<figure>` with an English
`<figcaption><p class="fig-desc">…`.

| # | Clinician section | File | Skill | Type | Size |
|---|---|---|---|---|---|
| B1 | `#md-epi` | `heart-failure-ckd-md-risk-grid.png` | simple-figure | Heat-grid reference card (E) | 1536×1152 |
| B2 | `#md-pathophys` | `heart-failure-ckd-md-haemodynamics.png` | mechanism-figure | Review-article mechanism | 1792×1024 |
| B3 | `#md-dx` | `heart-failure-ckd-md-np-thresholds.png` | simple-figure | Reference card (E) | 1536×1152 |
| B4 | `#md-gdmt` | `heart-failure-ckd-md-gdmt-matrix.png` | infographic | Clinician reference matrix | 1792×1024 |
| B5 | `#md-decongest` | `heart-failure-ckd-md-diuretic-algorithm.png` | simple-figure | Algorithm flowchart (A) | 1024×1536 |
| B6 | `#md-trials` | `heart-failure-ckd-md-trials-matrix.png` | simple-figure | Evidence matrix (E) | 1792×1024 |

> `#md-advanced` is intentionally text-only (no figure). All Part B captions are
> English-only to match the clinician layer.

---

## B1 · eGFR × albuminuria — graded HF/CV risk grid
*Skill: williamriveromd-simple-figure · Scaffold E (reference card)*

```
FILE NAME: heart-failure-ckd-md-risk-grid.png
IMAGE TYPE: Scaffold E — heat-grid reference card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Show the graded, independent contribution of eGFR and albuminuria to heart-failure and cardiovascular risk (KDIGO-style heat map).

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background. Bold navy (#0f1e2e) title: "eGFR × Albuminuria — Graded Heart-Failure & CV Risk". A KDIGO-style risk heat-map grid. X-axis (columns), albuminuria categories with teal (#1a6b72) headers: "A1 <30 mg/g", "A2 30–300 mg/g", "A3 >300 mg/g". Y-axis (rows), eGFR categories top to bottom: "G1 ≥90", "G2 60–89", "G3a 45–59", "G3b 30–44", "G4 15–29", "G5 <15". Shade each cell on a calm clinical gradient from renal green (#1f7a4d, low) through amber (#b8860b, moderate) to clinical red (#b91c1c, high), with risk rising toward low eGFR and high albuminuria (bottom-right reddest). Keep cell fills soft/desaturated so any overlaid small labels stay legible. Right-side annotation card in navy text: "Lower eGFR and higher UACR are independent predictors of incident HF (especially HFpEF) and of worse outcomes in prevalent HF. UACR's predictive value for HF (re)hospitalisation is comparable to BNP." Footer takeaway in navy: "Measure BOTH eGFR and UACR — yet only ~1 in 5 at-risk patients get a UACR." Mobile-readable, clean axis labels, generous whitespace. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, KDIGO-accurate category boundaries, calm desaturated heat map, white background, attribution bottom-right.
```

---

## B2 · Haemodynamics of cardiorenal GFR decline
*Skill: williamriveromd-biomedical-mechanism-figure*

```
FILE NAME: heart-failure-ckd-md-haemodynamics.png
IMAGE TYPE: Publication-grade biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Explain how reduced cardiac output and elevated central venous pressure lower GFR via glomerular haemodynamics and tubular sodium avidity.

COPY-READY PROMPT:
Create a publication-grade biomedical mechanism schematic in scientific review-article style on a pure white background, flat vector illustration with soft semi-3D shading, muted clinical palette, thin dashed connector boxes, clean sans-serif labels, generous whitespace.

Topic: Haemodynamic mechanisms of GFR decline in the cardiorenal syndrome.
Disease context: Coexisting heart failure and CKD.
Central mechanism: ↓ cardiac output and ↑ central venous pressure reduce net renal perfusion pressure; neurohormonal activation drives efferent vasoconstriction, raising filtration fraction and proximal sodium reabsorption.

ORGAN-LEVEL PANEL (left):
Simplified heart and kidney in light gray-blue. Show the heart with a "↓ cardiac output / forward flow" label, and the kidney with an engorged, dilated renal vein labeled "↑ central venous pressure / venous congestion". Thin dashed connector box pointing to the magnified glomerulus.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single nephron's glomerulus with afferent and efferent arterioles and a proximal tubule. Highlight the efferent arteriole in pale yellow. Concise callouts (red arrows for injury/constriction, blue for protective):
- Efferent vasoconstriction (Angiotensin II) → ↑ filtration fraction
- ↑ renal venous/interstitial pressure → ↓ net filtration pressure
- ↑ proximal tubular Na⁺ reabsorption (Na⁺ avidity)
- ↓ renal blood flow

BOTTOM SUMMARY FLOW (left → center → right):
- Left pale-pink box "DRIVERS": ↓ cardiac index · ↑ central venous pressure · ↑ RAAS / ↑ SNS
- Center box "MECHANISM": ↓ renal perfusion + venous congestion → ↑ filtration fraction, ↑ Na⁺ avidity → ↓ eGFR (often haemodynamic, reversible)
- Right pale-blue box "INTERVENTION → BENEFIT": effective decongestion + GDMT (SGLT2i, RAASi/ARNI) → ↓ CVP, restored perfusion → eGFR stabilises; "treat volume & haemodynamics, not the creatinine value"

Use a white background, muted clinical colors, clean sans-serif labels, thin dashed connectors, review-article figure style. Small semi-transparent navy "© williamriveromd.com" bottom-right. Avoid photorealism, dark backgrounds, decorative elements, overcrowding.

NEGATIVE INSTRUCTIONS:
No photorealism, no dark/navy/black backgrounds, no decorative gradients/shadows, no cartoon styling, no gibberish text, no overcrowding. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Anatomically and mechanistically accurate (efferent vasoconstriction, filtration fraction, venous congestion), labels readable at slide size, muted palette, white background, attribution present.
```

---

## B3 · Diagnosing HF in CKD — natriuretic-peptide thresholds
*Skill: williamriveromd-simple-figure · Scaffold E (reference card)*

```
FILE NAME: heart-failure-ckd-md-np-thresholds.png
IMAGE TYPE: Scaffold E — reference card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Give the indication-specific BNP/NT-proBNP cut-points and the CKD caveats for interpreting them.

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background. Bold navy (#0f1e2e) title: "Natriuretic Peptides in CKD — Interpreting HF". Compact two-row table with teal (#1a6b72) headers on soft gray (#f3f4f6): columns "Setting", "BNP", "NT-proBNP". Rows: "Ambulatory / screening — rule-in HF risk → BNP ≥ 35 pg/mL · NT-proBNP ≥ 125 pg/mL"; "Acute / ED — decompensation → BNP ≥ 100 pg/mL · NT-proBNP ≥ 300 pg/mL". Below the table, three small rounded caveat cards: (amber #b8860b) "↑ with falling eGFR (reduced renal clearance) — no validated CKD-specific cut-points"; (amber) "↓ in obesity and frequently in HFpEF — may mask true HF"; (teal) "In G4/G5/G5D corroborate with echo (E/e′, IVC) or RHC; a NORMAL NP still helps exclude HF". Footer takeaway in navy: "Where feasible, record an individual ambulatory baseline NP and trend it; a fall with decongestion predicts better outcomes even if creatinine rises." Alternating soft row fills, mobile-readable, not cluttered. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, correct cut-points, accurate CKD caveats, white background, attribution bottom-right.
```

---

## B4 · GDMT across the eGFR spectrum — the framework matrix *(flagship)*
*Skill: williamriveromd-infographic-skill · Archetype 5 (clinician reference) / matrix poster*

```
FILE NAME: heart-failure-ckd-md-gdmt-matrix.png
IMAGE TYPE: Clinician reference matrix (conceptual GDMT framework)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL MIX:
- photorealistic models: none
- 2D infographic: primary (matrix grid + footnote band)
- 3D component graphics: small heart + kidney glyphs in the title lockup
- algorithm/flowchart: none

PURPOSE: One-look conceptual framework for medical management of HFrEF and HFpEF across eGFR strata (after the KDIGO HF&CKD conference, Figure 4).
KEY CONCEPTS: HFrEF vs HFpEF × eGFR bands · agent selection · initiation rules
DIMENSIONS: 1792 × 1024

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinician reference infographic, landscape 16:9, publication-grade nephrology/cardiology design, white (#ffffff) background. Bold navy (#0f1e2e) title with small heart + kidney glyphs: "Medical Management of HF + CKD — by Ejection Fraction & eGFR". A clean matrix with TWO row-bands and FOUR eGFR columns. Column headers in teal (#1a6b72): "eGFR ≥60", "eGFR 30–59", "eGFR 15–29", "eGFR <15". 
Row band 1 labeled in navy "HFrEF": 
- ≥60 → β-blocker · ARNI/ACEi/ARB · SGLT2i · steroidal MRA · vericiguat
- 30–59 → β-blocker · ARNI/ACEi/ARB · SGLT2i · sMRA · vericiguat
- 15–29 → β-blocker · SGLT2i (if eGFR >20) · vericiguat
- <15 → β-blocker · hydralazine/nitrates
Row band 2 labeled in navy "HFpEF":
- ≥60 → SGLT2i · nsMRA (finerenone) · ARNI if EF closer to 50%
- 30–59 → SGLT2i · nsMRA (eGFR ≥25) · ARNI if EF closer to 50%
- 15–29 → SGLT2i (if eGFR >20)
- <15 → individualised
Use soft teal/green cell tints (deeper where more agents apply), rounded cells, readable agent chips. Bottom full-width soft gray (#f3f4f6) footnote band in navy, four short rules: "ACEi/ARB for all CKD with diabetes or proteinuria, regardless of HF status" · "Initiate ACEi/ARB/MRA if K⁺ <5.0; use K-binders, SGLT2i & diet to maintain therapy" · "Diuretics irrespective of eGFR if volume-expanded (higher doses at low eGFR)" · "Never combine ARNI with ACEi/ARB". Generous whitespace, mobile-readable, no clutter. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, agent selection and thresholds accurate to the KDIGO HF&CKD framework, calm palette, white background, attribution bottom-right.
```

---

## B5 · Diuretic / decongestion algorithm
*Skill: williamriveromd-simple-figure · Scaffold A (clinical algorithm, portrait)*

```
FILE NAME: heart-failure-ckd-md-diuretic-algorithm.png
IMAGE TYPE: Scaffold A — clinical algorithm / flowchart
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: Stepwise decongestion with process-based response targets and escalation in HF + reduced kidney function.

PROMPT:
Clinical nephrology algorithm, KDIGO/ESC guideline flowchart aesthetic, single focused pathway for "Decongestion in HF with reduced kidney function". White (#ffffff) background. Bold navy (#0f1e2e) title at top. Top-to-bottom flow with rounded nodes:
1) Entry node (navy): "Congestion + volume overload; low eGFR or high UACR → expect diuretic resistance".
2) Action node (navy): "Initial IV loop diuretic ≥ 2.5× the oral home dose (consider torsemide/bumetanide)".
3) Decision node (teal #1a6b72): "Adequate response?" with the response targets listed beside it in a soft gray card: "1–2 h: spot urine Na >50–70 mEq/L · 6 h: urine output >100–150 mL/h · 24 h: weight ↓ 1–3 kg".
   - GREEN optimal branch (#1f7a4d) "Yes": "Continue to euvolemia → then resume/initiate GDMT".
   - AMBER caution branch (#b8860b) "No": "Double loop dose + sequential nephron blockade (thiazide/metolazone, acetazolamide, SGLT2i)".
4) From the amber branch, a re-check decision back to targets, then a RED escalation node (#b91c1c): "Refractory overload → ultrafiltration or peritoneal dialysis".
Bold connecting arrows, max 4 branching levels, no spaghetti, generous whitespace, mobile-readable labels. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, targets and escalation accurate (ESC/KDIGO), clean top-to-bottom flow, white background, attribution bottom-right.
```

---

## B6 · Key trials & the kidney-outcome discordance
*Skill: williamriveromd-simple-figure · Scaffold E (evidence matrix)*

```
FILE NAME: heart-failure-ckd-md-trials-matrix.png
IMAGE TYPE: Scaffold E — evidence reference matrix
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Summarise the practice-changing trials and explain why kidney-protective drugs underperform on kidney endpoints in HF trials.

PROMPT:
Clinical evidence reference card, publication-grade design, white (#ffffff) background. Bold navy (#0f1e2e) title: "HF + CKD — Practice-Changing Trials". A clean table with teal (#1a6b72) headers on soft gray (#f3f4f6): columns "Trial(s)", "Population", "Key signal". Rows:
- "DAPA-HF · DELIVER · EMPEROR-Reduced/Preserved" | "HF across the EF spectrum" | "HR ≈ 0.75 for CV death / HF hospitalisation; benefit regardless of EF or diabetes".
- "FINEARTS-HF" | "HF, LVEF ≥ 40%" | "↓ total worsening-HF events + CV death; first MRA to benefit HFmrEF/HFpEF".
- "FLOW" | "T2D + CKD" | "24% ↓ kidney events · 18% ↓ MACE · 20% ↓ all-cause death".
- "STEP-HFpEF" | "HFpEF + obesity" | "↑ KCCQ, exercise capacity, weight loss (semaglutide 2.4 mg)".
- "FIDELIO / FIGARO (FIDELITY)" | "T2D + CKD" | "↓ kidney progression and CV events (finerenone)".
Alternating soft row fills; highlight the headline percentages in amber (#b8860b). Below the table, a teal-bordered call-out box titled "Why kidney-protective drugs underperform on kidney endpoints in HF trials": bullets — "lower baseline CKD-progression risk in unselected, non-albuminuric HF populations" · "eGFR fluctuation is a weak surrogate" · "competing risks of death / worsening HF" · "HF-trial follow-up (~1.5–2.5 yr) too short for slow kidney endpoints". Mobile-readable, not cluttered. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, trial figures accurate, clean matrix + discordance call-out, white background, attribution bottom-right.
```

---

## After generating (clinician figures)

1. Drop the PNGs (+ `.webp`) into `images/`.
2. Insert each as a `<figure>` in its `mode-physician` section with an **English-only**
   `<figcaption><p class="fig-desc">…</p></figcaption>` (no `data-lang` spans — the
   clinician layer is English only).
3. Re-run `python3 patch_image_lightbox.py --guide heart-failure-ckd.html` (lightbox
   already present; safe/idempotent). The hero scripts only touch the first image, so
   they won't disturb these.
4. These figures live inside `mode-physician` blocks, so they are hidden in patient
   mode automatically — no extra wiring needed.
