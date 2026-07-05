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
> `og:image` → `https://renalcarematters.com/images/kidney-functions-og.png`
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

---

## 11. Glomerular Filtration Barrier — Size & Charge Selectivity
**Suggested file:** `kidney-functions-filtration-barrier.png` · **Size:** 16:9
**Placement:** `#fn-waste`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow for highlighted segments, red for arteries/injury,
blue for protective/filtered flow, pale pink pathology box, pale blue benefit box.
No photorealism, no dark background, no clutter. Bottom-right: small semi-transparent
navy text "© williamriveromd.com".

TOPIC: The three-layer glomerular filtration barrier that selectively passes small
solutes while retaining blood cells and albumin.
DISEASE CONTEXT: Glomerular disease, proteinuria, CKD with falling GFR.
CENTRAL MECHANISM: The fenestrated endothelium, glomerular basement membrane (GBM),
and podocyte foot processes + slit diaphragm form a size-and-charge-selective barrier
allowing ~180 L plasma/day to filter while retaining proteins and cells.

ORGAN-LEVEL PANEL (left): simplified kidney cross-section (light gray-blue) labeled
"~180 L plasma filtered/day," with renal artery (red) entering the glomerulus. A dashed
connector box points from the glomerular tuft to the magnified mechanism panel.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): cross-sectional view of the
filtration barrier spanning from capillary lumen to Bowman's space. Show three distinct
layers from left (blood side) to right (filtrate side), each highlighted in soft yellow:
  Layer 1 — Fenestrated endothelium: label "Fenestrae (~70–100 nm pores) — blocks blood
    cells; negatively charged glycocalyx repels albumin."
  Layer 2 — Glomerular basement membrane (GBM): label "Type IV collagen + laminin + heparan
    sulfate proteoglycans — size and charge barrier."
  Layer 3 — Podocyte foot processes + slit diaphragm: label "Nephrin / podocin slit
    diaphragm (~40 nm) — final selectivity filter."
Draw small labeled icons passing rightward through all three layers: H₂O (water drop),
urea, creatinine, uric acid — labeled "freely filtered." Draw red blood cells and albumin
blocked at the endothelium/GBM, with a red ✗ or blockade arrow, labeled "retained in blood."
Add a concise callout: "Normal: <30 mg albumin/day in urine."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Barrier damage (diabetes, immune injury, hypertension) →
    foot-process effacement · nephrin loss · ↑ permeability · **Proteinuria, falling GFR,
    uremic solute retention**
  Intervention box (center): RAAS blockade (ACEi/ARB) · SGLT2 inhibitors · immunosuppression
    (selected glomerulopathies) · BP and glycemic control
  Benefit box (pale blue): ↓ Proteinuria · preserved GFR · clean blood maintained
```

---

## 12. Tubular Secretion of Drugs & Toxins
**Suggested file:** `kidney-functions-tubular-secretion.png` · **Size:** 16:9
**Placement:** `#fn-toxins`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow proximal-tubule highlight, red for toxin accumulation/
injury, blue for active secretion/clearance, pale pink pathology box, pale blue benefit
box. No photorealism, no dark background, no clutter. Bottom-right: small semi-transparent
navy text "© williamriveromd.com".

TOPIC: Active tubular secretion as the kidney's second drug-elimination mechanism beyond
filtration.
DISEASE CONTEXT: Drug accumulation and toxicity in CKD; need for dose adjustment.
CENTRAL MECHANISM: Proximal tubule epithelial cells actively transport organic anions and
cations from peritubular blood into the tubular lumen via basolateral uptake transporters
(OAT1/3, OCT2) and apical efflux pumps (MRP2/4, P-glycoprotein), clearing drugs even
when filtration alone is insufficient.

ORGAN-LEVEL PANEL (left): kidney in light gray-blue labeled "Drug & toxin elimination,"
with the proximal tubule highlighted (soft yellow), dashed connector to the magnified cell.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a single proximal tubule
epithelial cell oriented between blood/peritubular space (left, labeled "Basolateral")
and tubular lumen (right, labeled "Apical/Lumen"). Show active transport in two steps:
  Basolateral uptake (blood → cell):
    • OAT1/OAT3 (organic anion transporters): import penicillins, diuretics (furosemide),
      uric acid, NSAIDs — label each substrate in a small bubble
    • OCT2 (organic cation transporter): imports metformin, creatinine
  Apical efflux (cell → lumen):
    • MRP2/MRP4: export organic anions
    • P-glycoprotein (P-gp): export digoxin, select drugs
    • MATE1/2: export metformin (coupled to H⁺ gradient)
  Arrow from lumen rightward: "→ excreted in urine."
Add callout: "Secretion clears drugs even when plasma protein binding limits filtration."
Second callout: "OAT/OCT compete — drug interactions at shared transporters."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD → ↓ OAT/OCT expression + ↓ GFR · ↑ uremic toxin
    competition · **↓ drug clearance → accumulation, toxicity (metformin lactic acidosis,
    digoxin toxicity)**
  Intervention box (center): Dose adjustment for eGFR · avoid nephrotoxic drug combos ·
    monitor drug levels in advanced CKD
  Benefit box (pale blue): Safe, effective drug elimination · reduced adverse drug events
```

---

## 13. Potassium Secretion — Protecting the Heartbeat
**Suggested file:** `kidney-functions-potassium-secretion.png` · **Size:** 16:9
**Placement:** `#fn-potassium`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow for highlighted tubular segments, red for
hyperkalemia/arrhythmia injury, blue for protective K⁺ homeostasis, pale pink
pathology box, pale blue benefit box. No photorealism, no dark background, no
clutter. Bottom-right: small semi-transparent navy text "© williamriveromd.com".

TOPIC: How the kidney fine-tunes potassium secretion in the collecting duct to
maintain the narrow serum K⁺ range essential for cardiac rhythm.
DISEASE CONTEXT: Hyperkalemia and hypokalemia in CKD, diuretic use, and heart disease.
CENTRAL MECHANISM: Cortical collecting duct principal cells secrete K⁺ via ROMK and
BK channels driven by the basolateral Na⁺/K⁺-ATPase; aldosterone, distal Na⁺ delivery,
tubular flow rate, and serum K⁺ regulate the process; type A intercalated cells
reabsorb K⁺ via H⁺/K⁺-ATPase during depletion.

ORGAN-LEVEL PANEL (left): kidney in light gray-blue with the cortical collecting duct
highlighted (soft yellow), labeled "K⁺ guardian — normal serum K⁺ 3.5–5.0 mEq/L,"
dashed connector to the magnified cell pair.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): show two adjacent cells side
by side:
  Principal cell (left cell, soft yellow):
    • Basolateral: Na⁺/K⁺-ATPase pumps Na⁺ out, K⁺ in (energy-driven)
    • Apical: ROMK (small conductance K⁺ channel) — basal constitutive secretion
    • Apical: BK channel (flow-activated) — secretes K⁺ during high flow/volume
    • Regulators in callout bubbles: ↑ Aldosterone → more ROMK/ENaC → ↑ K⁺ secretion;
      ↑ Distal Na⁺ delivery → ↑ lumen electronegativity → ↑ K⁺ secretion;
      ↑ Serum K⁺ → directly stimulates secretion
    • Arrow from apical surface to lumen: "K⁺ secreted → urine"
  Type A intercalated cell (right cell, pale blue):
    • Apical: H⁺/K⁺-ATPase — reabsorbs K⁺ in exchange for H⁺
    • Callout: "Active during K⁺ depletion — conserves K⁺, excretes H⁺"
Add a small ECG strip inset with label: "Normal K⁺ → normal cardiac conduction."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD + ACEi/ARB/MRA → ↓ aldosterone signaling · ↓ distal
    Na⁺ delivery · **Hyperkalemia → peaked T waves, arrhythmia, cardiac arrest;
    Hypokalemia (loop diuretics) → muscle weakness, U waves, arrhythmia**
  Intervention box (center): Dietary K⁺ restriction · patiromer / sodium zirconium
    cyclosilicate (K⁺ binders) · loop/thiazide diuretics for depletion · optimize
    RAAS dosing · treat metabolic acidosis
  Benefit box (pale blue): Stable serum K⁺ 3.5–5.0 mEq/L · protected cardiac rhythm
```

---

## 14. Magnesium Handling — TAL Paracellular & DCT TRPM6
**Suggested file:** `kidney-functions-magnesium.png` · **Size:** 16:9
**Placement:** `#fn-magnesium`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow for highlighted tubular segments, red for
hypermagnesemia/toxicity, blue for reabsorption/protective effects, pale pink pathology
box, pale blue benefit box. No photorealism, no dark background, no clutter. Bottom-right:
small semi-transparent navy text "© williamriveromd.com".

TOPIC: The kidney's two-stage magnesium reabsorption system that balances blood Mg²⁺
for nerve, muscle, and cardiac function.
DISEASE CONTEXT: Hypermagnesemia in advanced CKD; hypomagnesemia with diuretics or
tubular disorders.
CENTRAL MECHANISM: ~60–70% of filtered Mg²⁺ is passively reabsorbed via paracellular
claudin-16/19 channels in the thick ascending limb (TAL), driven by the lumen-positive
voltage that NKCC2 generates; the remaining fine-tuning occurs in the distal convoluted
tubule (DCT) via active transcellular uptake through the TRPM6 channel.

ORGAN-LEVEL PANEL (left): kidney in light gray-blue with the thick ascending limb (TAL)
and distal convoluted tubule (DCT) both highlighted in soft yellow, labeled "Mg²⁺
homeostasis — normal serum 0.7–1.1 mmol/L," dashed connector to the magnified dual-panel.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): two stacked sub-panels:
  Sub-panel A — TAL (Thick Ascending Limb):
    • Show a TAL epithelial cell between the tubular lumen (top) and interstitium (bottom).
    • Label apical NKCC2 transporter reabsorbing Na⁺, K⁺, 2Cl⁻ into cell → generating
      lumen-positive transepithelial voltage (+8 mV).
    • Between two adjacent TAL cells: paracellular tight junction with claudin-16 and
      claudin-19 labeled; arrow from lumen to interstitium: "Passive Mg²⁺ reabsorption
      driven by lumen-positive voltage — ~60–70% of filtered load."
    • Callout: "NKCC2 inhibition (loop diuretics) → abolishes voltage → ↓ Mg²⁺
      reabsorption → hypomagnesemia."
  Sub-panel B — DCT (Distal Convoluted Tubule):
    • Show a DCT epithelial cell.
    • Apical membrane: TRPM6 channel imports Mg²⁺ from lumen into cell.
    • Basolateral: Mg²⁺ exits to interstitium (via SLC41A3 exchanger, labeled).
    • Callout: "TRPM6 is the regulated fine-tuning step — sensitive to Mg²⁺ status,
      epidermal growth factor, estrogen."
    • Second callout: "NCC (thiazide target) activity drives DCT Na⁺ uptake → affects
      TRPM6 activity."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Advanced CKD → GFR-dependent Mg²⁺ retention + Mg-rich
    antacids/laxatives · **Hypermagnesemia → areflexia, hypotension, respiratory
    depression;** Loop/thiazide diuretics · PPI use · tubular disorders → TRPM6
    downregulation · **Hypomagnesemia → cramps, arrhythmia, refractory hypokalemia
    and hypocalcemia**
  Intervention box (center): Restrict Mg-containing antacids/laxatives in CKD ·
    Mg supplementation (glycinate/oxide) for depletion · review diuretic class
    and PPI necessity · IV Mg for severe depletion
  Benefit box (pale blue): Balanced Mg²⁺ for nerve conduction, muscle contraction,
    cardiac rhythm, and enzymatic function (>300 Mg-dependent enzymes)
```

---

## 15. Klotho–FGF23 Axis — Phosphate & Vascular Protection
**Suggested file:** `kidney-functions-klotho-fgf23.png` · **Size:** 16:9
**Placement:** `#fn-klotho`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow for highlighted kidney tubule, red for phosphate
retention/vascular injury, blue for Klotho-mediated protection, pale pink pathology
box, pale blue benefit box. No photorealism, no dark background, no clutter. Bottom-right:
small semi-transparent navy text "© williamriveromd.com".

TOPIC: The Klotho–FGF23 signaling axis that regulates phosphate excretion and provides
direct vascular and anti-aging protection.
DISEASE CONTEXT: CKD-mineral bone disorder (CKD-MBD), vascular calcification, accelerated
cardiovascular aging.
CENTRAL MECHANISM: Bone-derived FGF23 requires membrane-bound Klotho (produced in the
kidney tubule) as a co-receptor to signal phosphaturia and calcitriol suppression; soluble
Klotho shed from the tubule exerts independent anti-fibrotic, anti-inflammatory, and
anti-calcification effects on vessels; CKD causes Klotho deficiency and FGF23 resistance.

ORGAN-LEVEL PANEL (left): simplified figure showing bone (small icon, labeled "osteocyte")
linked by a red dashed arrow to the kidney (light gray-blue, labeled "Klotho-producing
tubule"), which in turn links blue arrows to a blood vessel (labeled "endothelium"). Dashed
connector box from the kidney tubule to the magnified mechanism panel.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a proximal/distal tubule
epithelial cell with two labeled domains:
  Membrane-bound Klotho (apical/basolateral surface):
    • Klotho protein anchored in membrane, associated with FGFR1c
    • FGF23 (labeled with bone-origin arrow) binds FGF23–Klotho–FGFR1c complex
    • Downstream signaling (small arrows): ↓ NaPi-IIa / NaPi-IIc expression →
      "↓ Phosphate reabsorption → ↑ urinary phosphate excretion"
    • Second downstream arrow: "↓ CYP27B1 activity → ↓ calcitriol synthesis"
  Soluble Klotho (shed into blood/urine by ADAM10/17):
    • Arrow from the cell: "Soluble Klotho → bloodstream → vessels"
    • At a small vessel wall inset: labels "↓ TGF-β / Wnt signaling → anti-fibrotic;
      ↓ NF-κB → anti-inflammatory; inhibits phosphate-induced calcification → anti-calcification"
    • Label: "Acts as a circulating anti-aging factor."
Add a callout: "CKD → ↓ Klotho expression → FGF23 resistance → compensatory FGF23 ↑↑↑
(10–100× normal) → independent cardiac harm (LVH)."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD → ↓ Klotho · FGF23 resistance · ↑↑ FGF23 (cardiac toxin) ·
    phosphate retention · ↓ calcitriol · **Vascular calcification, arterial stiffness,
    accelerated cardiovascular aging, CKD-MBD**
  Intervention box (center): Dietary phosphate restriction · phosphate binders · active
    vitamin D analogs · calcimimetics · emerging: Klotho supplementation (proposed/experimental)
  Benefit box (pale blue): ↓ Phosphate · balanced FGF23–Klotho axis · flexible, less-calcified
    vessels · protected cardiac function
```

---

## 16. Renal Immune Signaling — The Kidney as an Immune Modulator
**Suggested file:** `kidney-functions-immune.png` · **Size:** 16:9
**Placement:** `#fn-immune`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow for highlighted tubular cells, red for inflammation/
infection/injury signals, blue for calcitriol/Klotho protective immune modulation,
pale pink pathology box, pale blue benefit box. No photorealism, no dark background,
no clutter. Bottom-right: small semi-transparent navy text "© williamriveromd.com".

TOPIC: The kidney's active roles in immune defense — producing calcitriol (immune
modulator), calcitriol-driven antimicrobial peptides, and Klotho (inflammation suppressor)
— and how CKD dismantles these defenses.
DISEASE CONTEXT: Chronic low-grade inflammation, increased infection susceptibility, and
accelerated vascular disease in CKD.
CENTRAL MECHANISM: Tubular epithelial cells sense danger signals (PAMPs, DAMPs, uremic
toxins) and produce cytokines (IL-6, IL-8, MCP-1), chemokines, and TLR-triggered innate
immune signals; the kidney's calcitriol (1,25-OH₂ vitamin D) modulates macrophage
polarization (→ M2 anti-inflammatory), T-cell differentiation (↓ Th17, ↑ Treg), and
dendritic cell function, as well as inducing beta-defensin antimicrobial peptides; soluble
Klotho suppresses NF-κB and TGF-β inflammatory signaling in immune cells and vessels.

ORGAN-LEVEL PANEL (left): kidney in light gray-blue with the tubular interstitium
highlighted, labeled "Immune-active organ," with small red immune-cell icons (macrophage,
T cell) in the interstitium during injury. Dashed connector to magnified cell panel.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a tubular epithelial cell at
the center with bidirectional signaling:
  Innate immune activation (red arrows, top):
    • TLR2/TLR4 on tubular cell surface sensing uremic toxins, PAMPs
    • → NF-κB activation → "↑ IL-6, IL-8, MCP-1, TNF-α" (red bubbles)
    • → Chemotaxis of macrophages and neutrophils into interstitium (small cell icons)
    • Label: "Persistent activation in CKD → chronic tubulointerstitial inflammation"
  Calcitriol immune axis (blue arrows, center):
    • Tubular cell produces calcitriol (1-alpha hydroxylase)
    • Calcitriol acts on macrophages: "↑ phagocytosis · M2 polarization · ↓ IL-12"
    • Calcitriol acts on T cells: "↓ Th17 / ↑ Treg → controlled adaptive immunity"
    • Calcitriol on epithelial cells: "↑ beta-defensin-2 → antimicrobial peptide defense"
  Klotho immune axis (blue arrows, bottom):
    • Soluble Klotho arrow from tubular cell → immune cells
    • Label: "↓ NF-κB · ↓ TGF-β1 · ↓ NLRP3 inflammasome → anti-inflammatory"
    • Callout: "CKD → ↓ calcitriol + ↓ Klotho → loss of immune brake"

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD → ↓ calcitriol · ↓ Klotho · ↑ uremic toxins · persistent
    NF-κB activation · **Chronic low-grade inflammation ("inflammaging") → higher infection
    risk (pneumonia, sepsis, peritonitis), accelerated vascular disease, protein-energy
    wasting, worsened anemia**
  Intervention box (center): Active vitamin D analogs (calcitriol/paricalcitol) · adequate
    dialysis (reduce uremic toxins) · vaccinations · nutrition support · anti-inflammatory
    therapies under study (proposed/experimental)
  Benefit box (pale blue): ↓ Systemic inflammation · balanced adaptive immunity ·
    controlled infection risk · reduced cardiovascular burden
```

---

## 17. Homeostasis — The Kidney as the Body's Master Integration Hub
**Suggested file:** `kidney-functions-homeostasis.png` · **Size:** 16:9
**Placement:** `#fn-homeostasis`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector, soft semi-3D shading, white background, clean sans-serif
labels, thin dashed connectors, generous whitespace. Muted clinical palette: light
gray-blue anatomy, soft yellow for the nephron hub, red for failure/drift signals,
blue for regulated/stable outputs, pale pink pathology box, pale blue benefit box.
No photorealism, no dark background, no clutter. Bottom-right: small semi-transparent
navy text "© williamriveromd.com".

TOPIC: The nephron as a real-time integrator receiving multiple simultaneous physiologic
inputs and producing continuous multi-axis regulatory outputs to maintain whole-body
homeostasis.
DISEASE CONTEXT: Progressive CKD leading to simultaneous failure of all regulated
systems and whole-body dysregulation.
CENTRAL MECHANISM: The nephron continuously monitors and adjusts ten interdependent
variables every second — water, sodium, potassium, acid/bicarbonate, phosphate, calcium,
magnesium, oxygen tension, blood pressure, and red cell mass — using a combination of
filtration, selective reabsorption, active secretion, and hormone production to keep each
parameter within a narrow physiologic range despite large variations in diet and activity.

ORGAN-LEVEL PANEL (left): a compact kidney cross-section (light gray-blue) labeled "~1
million nephrons — continuous integration 24/7," with a small ECG line, bone, and heart
icon flanking it to hint at the multiple systems it protects. A single thick dashed
connector leads to the central nephron hub.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): the nephron drawn as a clean
anatomical arc (glomerulus → proximal tubule → loop of Henle → distal tubule →
collecting duct) occupying the center of the panel, highlighted in soft yellow. Around
the nephron, arrange ten labeled input/output spoke-pairs in a radial layout — left
spokes are inputs (arriving signals/stimuli, small red or gray arrowheads pointing
inward), right spokes are outputs (regulated variables, small blue arrowheads pointing
outward):
  1. Input: "Osmoreceptors / ADH" → Output: "Water balance — dilute or concentrate urine"
  2. Input: "Blood pressure sensors / RAAS / ANP" → Output: "Sodium balance — long-term BP set point"
  3. Input: "Serum K⁺ / aldosterone / flow rate" → Output: "Potassium secretion — stable heartbeat"
  4. Input: "CO₂ / pH / ammoniagenesis signals" → Output: "Acid excretion — serum HCO₃⁻ 22–26 mEq/L"
  5. Input: "Serum HCO₃⁻ / pCO₂" → Output: "Bicarbonate reclamation — pH 7.35–7.45"
  6. Input: "PTH / FGF23 / serum phosphate" → Output: "Phosphate excretion — bone & vessel protection"
  7. Input: "Renal oxygen tension / HIF" → Output: "EPO production — red cell mass / O₂ delivery"
  8. Input: "Blood pressure afferents / myogenic stretch" → Output: "Autoregulation — stable GFR"
  9. Input: "Serum Ca²⁺ / PTH / vitamin D" → Output: "Calcium reabsorption — bone mineralization"
  10. Input: "Serum Mg²⁺ / flow / NKCC2 voltage" → Output: "Magnesium balance — nerve & cardiac function"
Add a small bold callout box inside the nephron arc: "Filters, reabsorbs, secretes,
and signals — simultaneously."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Progressive nephron loss → all ten regulated variables drift
    simultaneously: ↑ uremic toxins · Na⁺ + water excess · hyperkalemia · metabolic acidosis ·
    hyperphosphatemia · anemia · hypertension · **Whole-body regulatory failure — every organ
    system affected**
  Intervention box (center): Early CKD detection · SGLT2 inhibitors + RAAS blockade to slow
    nephron loss · proactive management of each individual complication · timely planning of
    kidney replacement therapy
  Benefit box (pale blue): Stable internal environment despite changing diet, activity, and
    illness · protected heart, bones, nerves, and vessels · extended years of preserved function
```

---

### Suggested in-page placement summary

This pack now covers **every function** in the guide. Generate all at 16:9 except
the OG image (1200×630). Save each under `images/` with the suggested filename.

| # | File | Section anchor | Function(s) shown |
|---|------|----------------|-------------------|
| 1 | `kidney-functions-og.png` (1200×630) | OG share image (tagged) + optional hero | Master regulator overview |
| 2 | `kidney-functions-nephron-map.png` | `#nephron` | Nephron anatomy (all segments) |
| 11 | `kidney-functions-filtration-barrier.png` | `#fn-waste` | 1 · Waste removal |
| 12 | `kidney-functions-tubular-secretion.png` | `#fn-toxins` | 2 · Drugs & toxins |
| 7 | `kidney-functions-urine-concentration.png` | `#fn-urine` / `#fn-water` | 3 · Water · 14 · Urine concentration |
| 3 | `kidney-functions-raas-bp.png` | `#fn-bp` / `#fn-sodium` / `#fn-renin` | 4 · Sodium · 8 · BP · 10 · Renin |
| 13 | `kidney-functions-potassium-secretion.png` | `#fn-potassium` | 5 · Potassium |
| 6 | `kidney-functions-bone-mineral-axis.png` | `#fn-bone` / `#fn-mineral` / `#fn-vitd` | 6 · Ca/PO₄ · 11 · Vitamin D · 13 · Bone |
| 14 | `kidney-functions-magnesium.png` | `#fn-magnesium` | 7 · Magnesium |
| 4 | `kidney-functions-acid-base.png` | `#fn-acidbase` | 9 · Acid–base |
| 5 | `kidney-functions-epo-hif.png` | `#fn-epo` / `#fn-oxygen` | 12 · EPO · 17 · Oxygen sensing |
| 15 | `kidney-functions-klotho-fgf23.png` | `#fn-klotho` | 12 · Klotho |
| 8 | `kidney-functions-gluconeogenesis.png` | `#fn-glucose` | 15 · Gluconeogenesis |
| 16 | `kidney-functions-immune.png` | `#fn-immune` | 16 · Immune support |
| 9 | `kidney-functions-cardiorenal-axis.png` | `#fn-heart` | 18 · Cardiovascular protection |
| 17 | `kidney-functions-homeostasis.png` | `#fn-homeostasis` | 19 · Homeostasis |
| 10 | `kidney-functions-ckd-cascade.png` | `#ckd-failure` | When function fails (CKD) |

> Figure numbers above match the prompt-block headings in this file (1–17). The
> table is ordered by where each figure appears in the guide.

