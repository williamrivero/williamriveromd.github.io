# Your Kidneys: The Master Regulators — Biomedical Mechanism Figure Prompt Pack

**Guide:** `guides/kidney-functions.html`
Generated with the **`williamriveromd-biomedical-mechanism-figure`** skill (Stage 1).

These are publication-grade biomedical mechanism schematics in the review-article style:
**organ-level panel → magnified functional-unit inset (dashed) → bottom three-box flow.**
Because this guide describes *normal* kidney physiology, the bottom flow is adapted to:
**normal mechanism → what fails in CKD (pathology box) → why it matters / protection (benefit box).**

**Shared style (applies to every prompt below):**
Flat vector illustration with soft semi-3D shading, white background, generous
whitespace, clean sans-serif labels, thin dashed connector lines separating
magnified panels. Muted clinical palette — light gray-blue anatomy, soft yellow
for highlighted tubular/affected segments, red for arteries/injury/ROS, blue for
veins/protective/therapeutic effects, pale pink pathology summary box, pale blue
benefit summary box. No photorealism, no shadows, no dark background, no
cartoonish styling, no excessive icons, no gibberish text. Labels readable at
slide-viewing size. **Every figure carries a small semi-transparent navy
attribution "© williamriveromd.com" in the bottom-right corner (bottom-center for
the portrait/landscape OG image), not obscuring any figure element.**

**Workflow:** paste a block into the ChatGPT Image Generator (GPT-image / GPT-4o),
generate, then save under `images/` with the suggested filename so it drops straight
into the guide. Stage 2 (`williamriveromd-local-image-generator`) can validate and
wire any additional in-page `<figure>` placements.

> **OG image status:** the social-share tags are already wired in the guide head —
> `og:image` → `https://www.williamriveromd.com/images/kidney-functions-og.png`
> (1200×630), with matching `og:image:width`, `og:image:height`, and `og:image:alt`.
> Generate **Figure 1** below at 1200×630 and save it exactly as
> `images/kidney-functions-og.png` to satisfy that tag.

---

## 1. OG / Master Hero — The Kidney as Master Regulator
**Suggested file:** `kidney-functions-og.png` · **Size:** 1200 × 630 (landscape, social-share + hero)
**Placement:** OG/Twitter share image (already tagged in head); optionally as the guide's first in-page figure.

```
Create a publication-grade biomedical "master regulator" schematic in a scientific
review-article style, landscape 1200x630. Flat vector illustration, soft semi-3D
shading, white background, clean sans-serif labels, thin dashed connector lines,
generous whitespace. Muted clinical palette: light gray-blue anatomy, soft yellow
highlights, red for arteries, blue for veins/protective signals, pale pink and pale
blue accent boxes. No photorealism, no dark background, no shadows, no clutter.
Bottom-center: small semi-transparent navy text "© williamriveromd.com", not
obscuring the figure.

TITLE (top, bold navy sans-serif): "Your Kidneys: The Master Regulators"

CENTER PANEL:
One simplified kidney cross-section in light gray-blue with renal artery (red) and
renal vein (blue), and a small dashed inset showing a single nephron. From the
kidney, draw clean thin arrows radiating outward to eight labeled regulatory roles,
each a small icon + short label:
  • Water & fluid balance (water-drop)
  • Sodium & blood pressure (gauge)
  • Potassium & heartbeat (heart with ECG line)
  • Acid–base balance (pH scale)
  • Red blood cell production — erythropoietin (red cells)
  • Vitamin D & bone strength (bone)
  • Phosphate / Klotho–FGF23 (vessel)
  • Waste & toxin removal (filter)

BOTTOM STRIP (one line, three pale-blue chips with arrows between):
  "Filters ~180 L plasma/day"  →  "Regulates blood chemistry, BP, hormones"  →
  "Protects heart, bone & whole-body homeostasis"

Keep it clean and editorial — this doubles as a social-share banner. No injury
imagery; emphasize the kidney as an intelligent, central regulator.
```

---

## 2. The Nephron Function Map
**Suggested file:** `kidney-functions-nephron-map.png` · **Size:** 16:9
**Placement:** `#nephron` — "The Nephron: The Functional Unit of the Kidney."

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow for highlighted segments, red for arterioles, blue for
the venous/peritubular side. No photorealism, no dark background, no clutter.
Bottom-right: small semi-transparent navy text "© williamriveromd.com".

TOPIC: One nephron, with each segment labeled by the body-wide job it performs.
DISEASE CONTEXT: Normal kidney physiology (foundational anatomy).

ORGAN-LEVEL PANEL (left): simplified kidney cross-section (cortex + medulla) in light
gray-blue, labeled "~1 million nephrons per kidney," with a dashed connector box to the
magnified nephron.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a single anatomically plausible
nephron — glomerulus with afferent (red) and efferent (red) arterioles, proximal tubule,
loop of Henle (descending + thick ascending limb), distal convoluted tubule, collecting
duct, juxtaglomerular apparatus, and surrounding interstitium with peritubular capillaries.
Highlight each segment in pale yellow with a concise callout:
  • Glomerulus → "Filtration barrier — 180 L/day"
  • Proximal tubule → "Bulk reabsorption · gluconeogenesis · ammoniagenesis"
  • Loop of Henle → "Countercurrent multiplication → medullary gradient"
  • Distal convoluted tubule → "Fine-tuning Na⁺ / Ca²⁺ / Mg²⁺ (NCC)"
  • Collecting duct → "ADH/aquaporins · K⁺ · acid–base · final urine"
  • Juxtaglomerular apparatus → "Renin · tubuloglomerular feedback"
  • Interstitium → "Erythropoietin · oxygen sensing"

BOTTOM SUMMARY (one pale-blue band): "Every regulatory function in this guide is performed
by these specialized nephron segments working together."
```

---

## 3. Sodium & Long-Term Blood Pressure — The RAAS Mechanism
**Suggested file:** `kidney-functions-raas-bp.png` · **Size:** 16:9
**Placement:** `#fn-bp` (also supports `#fn-sodium` / `#fn-renin`).

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow highlights, red for injury/high pressure, blue for
therapeutic/lowering effects, pale pink pathology box, pale blue benefit box. No
photorealism, no dark background, no clutter. Bottom-right: small semi-transparent
navy text "© williamriveromd.com".

TOPIC: How the kidney sets long-term blood pressure through sodium handling and RAAS.
DISEASE CONTEXT: Hypertension and CKD.
CENTRAL MECHANISM: Low perfusion / low distal NaCl / sympathetic tone → renin →
angiotensin II → aldosterone → ENaC sodium retention; pressure natriuresis and
tubuloglomerular feedback provide counter-regulation.

ORGAN-LEVEL PANEL (left): kidney in light gray-blue with renal artery (red), labeled
"Long-term BP control," dashed connector to the juxtaglomerular apparatus.

MAGNIFIED MECHANISM PANEL (center, dashed border): juxtaglomerular apparatus at the
glomerulus with afferent arteriole and macula densa, plus a short cascade arrow chain:
  Renin → Angiotensinogen → Angiotensin I → (ACE) Angiotensin II → Aldosterone → ENaC (collecting duct)
Callouts:
  • Macula densa → "Senses ↓ NaCl delivery"
  • Afferent arteriole → "Senses ↓ stretch/pressure"
  • Angiotensin II → "Vasoconstriction"
  • Aldosterone/ENaC → "↑ Na⁺ & water reabsorption"
Add a small labeled loop: "Pressure natriuresis: ↑ BP → ↑ Na⁺ excretion → ↓ volume."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Sodium retention · RAAS overactivation · **Resistant
    hypertension, fluid overload, heart failure**
  Intervention box (center): RAAS blockade (ACEi/ARB) · MRA/finerenone · dietary salt
    reduction · SGLT2 inhibitors
  Benefit box (pale blue): ↓ Volume & BP · ↓ Proteinuria · cardiorenal protection
```

---

## 4. Acid–Base Balance — Bicarbonate Reclamation & Ammoniagenesis
**Suggested file:** `kidney-functions-acid-base.png` · **Size:** 16:9
**Placement:** `#fn-acidbase`.

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow tubular highlights, red for acid/H⁺, blue for
bicarbonate/protective, pale pink pathology box, pale blue benefit box. No
photorealism, no dark background, no clutter. Bottom-right: small semi-transparent
navy text "© williamriveromd.com".

TOPIC: How the kidney removes the body's daily metabolic acid.
DISEASE CONTEXT: Metabolic acidosis of CKD.
CENTRAL MECHANISM: Proximal bicarbonate reclamation + new bicarbonate via glutamine
ammoniagenesis + acid excretion as ammonium and titratable acid.

ORGAN-LEVEL PANEL (left): kidney in light gray-blue labeled "Acid–base balance," dashed
connector to a proximal tubule cell.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a proximal tubule epithelial cell
between lumen (left) and blood (right), with two stacked sub-panels:
  (1) Bicarbonate reclamation: lumen H⁺ secreted via NHE3 and H⁺-ATPase →
      H⁺ + HCO₃⁻ → H₂CO₃ → (carbonic anhydrase) CO₂ + H₂O → CO₂ enters cell →
      intracellular CA reforms HCO₃⁻ → exits to blood. Label arrows clearly.
  (2) Ammoniagenesis: "Glutamine → NH₄⁺ (excreted) + new HCO₃⁻ (to blood)";
      note "Acidosis ↑ glutamine uptake." Add a collecting-duct inset: "Titratable
      acid — H⁺ buffered by phosphate."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): ↓ Acid excretion · ↓ New HCO₃⁻ · **Metabolic acidosis →
    muscle wasting, bone loss, faster CKD progression**
  Intervention box (center): Oral alkali (sodium bicarbonate) · reduce dietary acid load ·
    treat underlying CKD
  Benefit box (pale blue): Restored serum bicarbonate · preserved muscle & bone ·
    slower eGFR decline
```

---

## 5. Erythropoietin & Oxygen Sensing — The HIF Pathway
**Suggested file:** `kidney-functions-epo-hif.png` · **Size:** 16:9
**Placement:** `#fn-epo` (also supports `#fn-oxygen`).

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow highlights, red for hypoxia/injury, blue for oxygen/
protective, pale pink pathology box, pale blue benefit box. No photorealism, no dark
background, no clutter. Bottom-right: small semi-transparent navy text
"© williamriveromd.com".

TOPIC: How the kidney senses oxygen and signals the marrow to make red blood cells.
DISEASE CONTEXT: Anemia of CKD.
CENTRAL MECHANISM: Low O₂ → prolyl-hydroxylase inhibition → HIF stabilization → EPO
transcription → bone-marrow erythropoiesis.

ORGAN-LEVEL PANEL (left): kidney in light gray-blue labeled "Oxygen sensor," dashed
connector to a peritubular interstitial fibroblast-like cell in the cortex/outer medulla.

MAGNIFIED MECHANISM PANEL (center, dashed border): the interstitial cell with an oxygen
gauge. Callout chain:
  ↓ O₂ → "Prolyl hydroxylase inhibited" → "HIF stabilized" → "EPO gene transcription" →
  EPO released into blood (arrow to a small bone-marrow inset showing red-cell progenitors
  maturing into red blood cells).
Label: "Tubular transport is energy-intensive → cortex/medulla sit near a delicate O₂ balance."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Loss of EPO-producing cells · fibrosis · capillary rarefaction ·
    **Normocytic anemia of CKD → fatigue, dyspnea, LVH**
  Intervention box (center): ESAs (erythropoiesis-stimulating agents) · HIF-PH inhibitors
    (proposed/oral) · iron repletion
  Benefit box (pale blue): ↑ Hemoglobin · ↑ exercise tolerance · ↓ cardiac strain
```

---

## 6. Bone & Mineral Axis — Calcium · Phosphate · PTH · Vitamin D · FGF23 · Klotho
**Suggested file:** `kidney-functions-bone-mineral-axis.png` · **Size:** 16:9
**Placement:** `#fn-bone` (also supports `#fn-mineral`, `#fn-vitd`, `#fn-klotho`).

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow highlights, red for injury, blue for protective signals,
pale pink pathology box, pale blue benefit box. No photorealism, no dark background, no
clutter. Bottom-right: small semi-transparent navy text "© williamriveromd.com".

TOPIC: The kidney-run mineral-and-hormone axis that keeps bones strong and arteries flexible.
DISEASE CONTEXT: CKD-mineral and bone disorder (CKD-MBD).
CENTRAL MECHANISM: Kidney activates vitamin D (1-alpha hydroxylase → calcitriol), excretes
phosphate (NaPi-IIa/IIc, suppressed by PTH & FGF23), and produces Klotho (FGF23 co-receptor).

ORGAN-LEVEL PANEL (left): kidney (proximal tubule highlighted) in light gray-blue labeled
"Mineral & bone regulator," dashed connectors to a small ring of organs: bone, parathyroid
gland, gut.

MAGNIFIED MECHANISM PANEL (center, dashed border): a hub-and-spoke axis with labeled arrows:
  • Kidney → "25-OH vitamin D → (1-alpha hydroxylase) calcitriol" → gut "↑ Ca²⁺ absorption"
  • Kidney proximal tubule → "Phosphate excretion via NaPi-IIa/IIc"
  • Parathyroid → "PTH ↑ Ca²⁺ reabsorption, ↑ phosphate excretion"
  • Bone → "FGF23 → ↑ phosphate wasting, ↓ calcitriol" (with Klotho as co-receptor at the kidney)
  • Kidney → "Klotho (membrane + soluble) — vascular protection"

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): ↓ Calcitriol · phosphate retention · ↑ PTH · ↓ Klotho ·
    **Renal osteodystrophy + vascular calcification**
  Intervention box (center): Phosphate binders · active vitamin D analogs · calcimimetics ·
    dietary phosphate control
  Benefit box (pale blue): Balanced Ca²⁺/PO₄ · stronger bones · flexible, less-calcified arteries
```

---

## 7. Water Balance & Urine Concentration — Countercurrent Multiplication
**Suggested file:** `kidney-functions-urine-concentration.png` · **Size:** 16:9
**Placement:** `#fn-urine` (also supports `#fn-water`).

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow highlights, gradient blue shading for the medullary
osmotic gradient, pale pink pathology box, pale blue benefit box. No photorealism, no
dark background, no clutter. Bottom-right: small semi-transparent navy text
"© williamriveromd.com".

TOPIC: How the kidney concentrates or dilutes urine to manage body water.
DISEASE CONTEXT: Polyuria/nocturia and hyponatremia risk in CKD.
CENTRAL MECHANISM: Thick ascending limb (NKCC2, water-impermeable) builds a medullary
gradient via countercurrent multiplication; urea recycling deepens it; ADH opens AQP2 in
the collecting duct so water follows the gradient back to blood.

ORGAN-LEVEL PANEL (left): kidney with cortex-to-medulla shading (light at cortex → deep at
papilla) labeled "Water manager," dashed connector to a loop of Henle + collecting duct.

MAGNIFIED MECHANISM PANEL (center, dashed border): a loop of Henle beside a collecting duct,
with a vertical osmolality scale (≈300 mOsm cortex → ≈1200 mOsm papilla). Callouts:
  • Thick ascending limb → "NKCC2 pumps NaCl out; water-impermeable"
  • Descending limb → "Water-permeable"
  • Inner medullary collecting duct → "Urea recycling strengthens gradient"
  • Collecting duct principal cell → "ADH → AQP2 inserted → water reabsorbed"
Add a small toggle note: "Low ADH → duct stays water-impermeable → dilute urine."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Impaired concentration → polyuria/nocturia/dehydration ·
    Impaired dilution → **hyponatremia risk**
  Intervention box (center): Match fluid intake to need · treat the cause · monitor sodium
  Benefit box (pale blue): Stable blood volume & sodium across hydration states
```

---

## 8. Renal Gluconeogenesis — Glucose & the Acid-Base Link
**Suggested file:** `kidney-functions-gluconeogenesis.png` · **Size:** 16:9
**Placement:** `#fn-glucose`.

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow proximal-tubule highlight, blue for glucose/protective,
pale pink pathology box, pale blue benefit box. No photorealism, no dark background, no
clutter. Bottom-right: small semi-transparent navy text "© williamriveromd.com".

TOPIC: The kidney as the body's second glucose-producing organ during fasting.
DISEASE CONTEXT: Hypoglycemia risk in advanced CKD (especially diabetics on insulin/sulfonylureas).
CENTRAL MECHANISM: Cortical proximal tubule converts lactate, glutamine, glycerol, and alanine
into glucose; glutamine metabolism simultaneously makes bicarbonate and removes acid.

ORGAN-LEVEL PANEL (left): kidney with cortex highlighted, labeled "Fasting glucose source
(~25% of total)," dashed connector to a cortical proximal tubule cell.

MAGNIFIED MECHANISM PANEL (center, dashed border): a proximal tubule cell with a compact
gluconeogenic pathway. Inputs (left): lactate, glutamine, glycerol, alanine. Key enzymes
labeled along the path: pyruvate carboxylase → PEPCK → fructose-1,6-bisphosphatase →
glucose-6-phosphatase → "free glucose released to blood." Side note off glutamine:
"Glutamine → glucose + NH₄⁺ + new HCO₃⁻ — links glucose production to acid removal
(↑ during acidosis)."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Advanced CKD → ↓ renal gluconeogenesis + ↓ insulin clearance ·
    **↑ hypoglycemia risk (insulin / sulfonylureas)**
  Intervention box (center): Adjust glucose-lowering drugs · monitor fasting/overnight glucose
  Benefit box (pale blue): Safer glucose control · fewer hypoglycemic events
```

---

## 9. Cardiovascular Protection — The Kidney–Heart–Bone–Blood Axis
**Suggested file:** `kidney-functions-cardiorenal-axis.png` · **Size:** 16:9
**Placement:** `#fn-heart`.

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow highlights, red for injury, blue for protective effects,
pale pink pathology box, pale blue benefit box. No photorealism, no dark background, no
clutter. Bottom-right: small semi-transparent navy text "© williamriveromd.com".

TOPIC: The many ways healthy kidneys protect the heart and blood vessels.
DISEASE CONTEXT: Cardiorenal disease — "kidney disease is cardiovascular disease."
CENTRAL MECHANISM: Kidney controls volume, sodium, potassium, BP, acid-base, EPO, and the
mineral/Klotho axis — together limiting LVH, heart failure, arrhythmia, and calcification.

ORGAN-LEVEL PANEL (left): a kidney and a heart connected by red artery and blue vein,
labeled "Cardiorenal axis," dashed connector to the central hub.

MAGNIFIED MECHANISM PANEL (center, dashed border): the kidney at a hub with six labeled
protective spokes pointing to a heart + vessel wall:
  • Volume & sodium control → "Prevents fluid overload / hypertension"
  • Potassium regulation → "Prevents arrhythmia"
  • Acid–base balance → "Stable myocardial function"
  • Erythropoietin → "Prevents anemia → less cardiac strain"
  • Phosphate / FGF23 / Klotho → "Limits vascular calcification"
  • Blood-pressure control → "Less LVH"

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD → fluid overload · hyperkalemia · anemia · calcification ·
    **Heart failure, LVH, arrhythmia, MI, stroke**
  Intervention box (center): BP & volume control · K⁺ management · anemia & mineral therapy ·
    SGLT2 inhibitors / RAAS blockade
  Benefit box (pale blue): ↓ Cardiovascular events · preserved heart & vessel function
```

---

## 10. CKD Complication Cascade — When the Regulator Fails
**Suggested file:** `kidney-functions-ckd-cascade.png` · **Size:** 16:9
**Placement:** `#ckd-failure` — "What Happens When Kidney Function Falls?"

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow highlights, red for injury/loss, pale pink pathology
boxes, pale blue benefit box. No photorealism, no dark background, no clutter.
Bottom-right: small semi-transparent navy text "© williamriveromd.com".

TOPIC: How progressive nephron loss cascades into multi-system failure across CKD stages.
DISEASE CONTEXT: CKD stages 1–5.
CENTRAL MECHANISM: Nephron loss → simultaneous failure of filtration, endocrine, metabolic,
and homeostatic functions.

ORGAN-LEVEL PANEL (left): a row of four kidneys getting progressively smaller/scarred,
labeled "Stage 1–2 (silent)," "Stage 3 (decline begins)," "Stage 4 (multi-system)," and
"Stage 5 (failure)," with a downward eGFR arrow beneath.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): from a shrinking nephron, fan out
labeled red arrows to the functions progressively lost:
  • ↓ Waste removal → uremia
  • ↓ Water & sodium control → edema, hypertension
  • ↓ Potassium regulation → hyperkalemia
  • ↓ Acid excretion → metabolic acidosis
  • ↓ EPO → anemia
  • ↓ Vitamin D activation + ↑ phosphate → CKD-MBD
  • ↓ Cardiovascular protection → heart failure, calcification

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Progressive loss of filtration + endocrine + metabolic +
    homeostatic functions · **Whole-body regulatory failure**
  Intervention box (center): Early detection · slow progression (BP/glucose/SGLT2/RAAS) ·
    treat each complication · plan kidney replacement therapy
  Benefit box (pale blue): Preserved function · fewer complications · better survival & quality of life
```

---

### Suggested in-page placement summary

| # | File | Section anchor |
|---|------|----------------|
| 1 | `kidney-functions-og.png` (1200×630) | OG share image (tagged) + optional hero |
| 2 | `kidney-functions-nephron-map.png` | `#nephron` |
| 3 | `kidney-functions-raas-bp.png` | `#fn-bp` |
| 4 | `kidney-functions-acid-base.png` | `#fn-acidbase` |
| 5 | `kidney-functions-epo-hif.png` | `#fn-epo` |
| 6 | `kidney-functions-bone-mineral-axis.png` | `#fn-bone` |
| 7 | `kidney-functions-urine-concentration.png` | `#fn-urine` |
| 8 | `kidney-functions-gluconeogenesis.png` | `#fn-glucose` |
| 9 | `kidney-functions-cardiorenal-axis.png` | `#fn-heart` |
| 10 | `kidney-functions-ckd-cascade.png` | `#ckd-failure` |
