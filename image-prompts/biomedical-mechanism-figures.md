# Biomedical Mechanism Figure — Prompt Pack

Generated with the **`williamriveromd-biomedical-mechanism-figure`** skill.

These are publication-grade biomedical mechanism schematics in the review-article style:
**organ-level panel → magnified functional-unit inset (dashed) → bottom injury → intervention → benefit flow.**

**Shared style (applies to every prompt below):**
Flat vector illustration with soft semi-3D shading, white background, generous
whitespace, clean sans-serif labels, thin dashed connector lines separating
magnified panels. Muted clinical palette — light gray-blue anatomy, soft yellow
for highlighted tubular/affected segments, red for arteries/injury/ROS, blue for
veins/protective/therapeutic effects, pale pink pathology summary box, pale blue
benefit summary box. No photorealism, no shadows, no dark background, no
cartoonish styling, no excessive icons, no gibberish text. 16:9 aspect ratio,
labels readable at slide-viewing size. Always flag non-standard therapies as
"proposed / experimental."

**Workflow:** paste a block into the ChatGPT Image Generator (GPT-image / GPT-4o).
Suggested output filenames follow each guide's existing naming convention so the
new figure drops straight into the guide.

---

## 1. Diabetes & Your Kidneys
**Guide:** `guides/diabetes-kidneys.html` · **Suggested file:** `dkd-pat-02-mechanism.png`
**Placement:** after the overview infographic, before the staging figure.

```
Create a publication-grade biomedical mechanism schematic in a scientific
review-article style. Flat vector illustration, soft semi-3D shading, white
background, clean sans-serif labels, thin dashed connector lines, generous
whitespace. Muted clinical palette: light gray-blue anatomy, soft yellow for
highlighted glomerular/tubular structures, red for injury/ROS, blue for
therapeutic effects, pale pink pathology box, pale blue benefit box. No
photorealism, no dark background, no shadows, no clutter. 16:9.

TOPIC: How high blood sugar damages the kidney in diabetic kidney disease.
DISEASE CONTEXT: Type 2 diabetes / diabetic kidney disease (DKD).
CENTRAL MECHANISM: Chronic hyperglycemia → glomerular hyperfiltration and
podocyte injury → albuminuria → progressive nephron loss; modern therapy
relieves intraglomerular pressure.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section in light gray-blue with renal artery (red) and
renal vein (blue), labeled "Diabetic kidney disease." Small dashed connector
box pointing to the magnified glomerulus.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single glomerulus with afferent and efferent arterioles, plus an attached
proximal tubule. Highlight the affected structures in pale yellow. Concise
callouts:
  • Afferent arteriole dilated / efferent constricted → "Glomerular
    hyperfiltration, ↑ intraglomerular pressure"
  • Podocytes (foot-process effacement) → "Podocyte injury → albuminuria"
  • Mesangium → "Mesangial expansion, ↑ ROS, basement-membrane thickening"
  • Tubulointerstitium → "Tubular stress → interstitial fibrosis"

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): ↑ Intraglomerular pressure · ↑ ROS / AGEs ·
    Podocyte loss · **Progressive nephron loss & proteinuria**
  Intervention box (center): SGLT2 inhibitors (afferent constriction, lower
    intraglomerular pressure) · RAAS blockade (ACEi/ARB, efferent dilation) ·
    glycemic & BP control
  Benefit box (pale blue): ↓ Intraglomerular pressure · ↓ Albuminuria ·
    Slower eGFR decline · Cardiorenal protection
```

---

## 2. CKD–Mineral & Bone Disorder (CKD-MBD)
**Guide:** `guides/ckd-mbd.html` · **Suggested file:** `ckd-mbd-mechanism-infographic.png`
**Placement:** after the "what is CKD-MBD" infographic.

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for injury, blue
for therapy, pale pink pathology box, pale blue benefit box. No photorealism, no
dark background, no clutter. 16:9.

TOPIC: The mineral and bone cascade of chronic kidney disease.
DISEASE CONTEXT: CKD-MBD (mineral and bone disorder of CKD).
CENTRAL MECHANISM: Failing kidneys retain phosphate and underproduce active
vitamin D → secondary hyperparathyroidism → bone disease and vascular
calcification.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "CKD (↓ function)."
Callouts: "↓ Phosphate excretion → ↑ serum phosphate" and "↓ 1-alpha-
hydroxylase → ↓ active vitamin D (calcitriol)." Dashed connector to the
magnified panel.

MAGNIFIED MECHANISM PANEL (center, dashed border):
Three linked units in sequence —
  • Parathyroid gland cell (highlighted pale yellow): "↑ PTH secretion
    (secondary hyperparathyroidism), ↑ FGF23"
  • Bone with osteoclasts/osteoblasts: "↑ Bone turnover → renal osteodystrophy,
    fracture risk"
  • Artery wall cross-section: "Calcium-phosphate deposition → vascular
    calcification, arterial stiffness"
Connect them with thin arrows showing the cascade.

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): ↑ Phosphate · ↓ Active vitamin D · ↑ PTH / FGF23 ·
    **Bone disease + vascular calcification**
  Intervention box (center): Dietary phosphate restriction · phosphate binders ·
    active vitamin D analogues · calcimimetics
  Benefit box (pale blue): Normalized phosphate & PTH · ↓ Vascular calcification ·
    Stronger bone · ↓ Fracture & cardiovascular risk
```

---

## 3. Metabolic Acidosis in CKD
**Guide:** `guides/metabolic-acidosis-ckd.html` · **Suggested file:** `metabolic-acidosis-mechanism.png`
**Placement:** before the consequences diagram.

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for injury, blue
for therapy, pale pink pathology box, pale blue benefit box. No photorealism, no
dark background, no clutter. 16:9.

TOPIC: How chronic kidney disease causes metabolic acidosis and how it harms the
body.
DISEASE CONTEXT: Metabolic acidosis of CKD.
CENTRAL MECHANISM: Reduced nephron mass → impaired acid excretion and
bicarbonate regeneration → chronic low serum bicarbonate → muscle, bone and
kidney injury.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "CKD: reduced nephron
mass." Dashed connector to the magnified nephron.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single nephron with proximal and distal segments highlighted pale yellow.
Callouts:
  • Proximal tubule: "↓ Bicarbonate reabsorption / regeneration"
  • Distal tubule / collecting duct: "↓ Ammonium (NH4+) and titratable acid
    excretion → H+ retention"
  • Result label near tubule: "↓ Serum bicarbonate (chronic acid retention)"

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): H+ retention · ↓ Serum bicarbonate · Muscle
    protein breakdown · bone buffering · **Faster CKD progression**
  Intervention box (center): Oral alkali (sodium bicarbonate) · base-producing
    fruit & vegetable diet · treat underlying CKD
  Benefit box (pale blue): Normalized bicarbonate · Preserved muscle & bone ·
    Slower eGFR decline
```

---

## 4. Anemia Management in CKD
**Guide:** `guides/anemia-management.html` · **Replaces/augments:** `anemia-ckd-mechanism.png`
**Placement:** swap in for the existing simplified box diagram.

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for injury, blue
for therapy, pale pink pathology box, pale blue benefit box. No photorealism, no
dark background, no clutter. 16:9.

TOPIC: Why chronic kidney disease causes anemia (the erythropoietin axis).
DISEASE CONTEXT: Anemia of CKD.
CENTRAL MECHANISM: Damaged kidneys make too little erythropoietin (EPO), and
inflammation raises hepcidin and limits iron → reduced red-cell production.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "CKD." Magnified inset
of a peritubular interstitial fibroblast highlighted pale yellow: "↓ EPO
production from interstitial fibroblasts." Dashed connector to the bone marrow
panel.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
Bone marrow with erythroid precursors maturing into red blood cells. Callouts:
  • "↓ EPO signal → ↓ erythroid proliferation"
  • "↑ Hepcidin (inflammation) → functional iron deficiency"
  • Output: "↓ Red blood cell production → anemia"

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): ↓ Erythropoietin · ↑ Hepcidin / iron sequestration ·
    Shortened RBC survival · **Anemia of CKD**
  Intervention box (center): Iron repletion (oral/IV) · erythropoiesis-
    stimulating agents (ESA) · HIF-PH inhibitors · treat inflammation
  Benefit box (pale blue): Restored erythropoiesis · ↑ Hemoglobin · ↑ Energy &
    quality of life · fewer transfusions
```

---

## 5. IgA Nephropathy
**Guide:** `guides/igan-guide.html` · **Suggested file:** `igan-mechanism.png`
**Placement:** between the diagnosis and treatment patient-pathway figures.

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for injury/
immune-complex deposition, blue for therapy, pale pink pathology box, pale blue
benefit box. No photorealism, no dark background, no clutter. 16:9.

TOPIC: How IgA nephropathy injures the glomerulus (the four-hit model).
DISEASE CONTEXT: IgA nephropathy (IgAN).
CENTRAL MECHANISM: Galactose-deficient IgA1 forms immune complexes that deposit
in the glomerular mesangium → complement activation → mesangial injury and
proteinuria.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "IgA nephropathy."
Dashed connector to the magnified glomerulus.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single glomerulus with the mesangium highlighted pale yellow. Show small
immune-complex deposits (red) in the mesangium. Callouts:
  • "Galactose-deficient IgA1 immune complexes deposit in mesangium"
  • "Complement activation (alternative & lectin pathways)"
  • "Mesangial cell proliferation & matrix → hematuria + proteinuria"
  • Optional small inset: gut-associated mucosal IgA1 source ("mucosal origin").

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): Gd-IgA1 immune complexes · complement activation ·
    mesangial proliferation · **Glomerular injury → proteinuria & CKD**
  Intervention box (center): RAAS blockade (ACEi/ARB) · SGLT2 inhibitors ·
    targeted-release budesonide (gut mucosal) · complement-pathway inhibitors
  Benefit box (pale blue): ↓ Proteinuria · ↓ Complement-mediated injury ·
    Slower eGFR decline
```

---

## 6. Hypertensive Kidney Disease
**Guide:** `guides/hypertensive-kidney-disease.html` · **Replaces/augments:** `hkd-mechanism-scarring.png`

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for arterial
injury, blue for therapy, pale pink pathology box, pale blue benefit box. No
photorealism, no dark background, no clutter. 16:9.

TOPIC: How chronic high blood pressure scars the kidney.
DISEASE CONTEXT: Hypertensive nephrosclerosis.
CENTRAL MECHANISM: Sustained high pressure damages small renal arteries and
glomeruli → ischemia and glomerulosclerosis → nephron loss → a self-reinforcing
pressure–damage cycle.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "Hypertensive kidney
disease." Dashed connector to the magnified nephron/arteriole.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single glomerulus with its afferent arteriole, wall thickened (highlighted
pale yellow, red injury accents). Callouts:
  • Arteriole: "Arteriolar wall thickening / hyalinosis → luminal narrowing"
  • Glomerulus: "Barotrauma + ischemia → glomerulosclerosis"
  • Tubulointerstitium: "Tubular atrophy & interstitial fibrosis → nephron loss"
  • A small curved arrow looping back: "Nephron loss → higher pressure on
    survivors (vicious cycle)."

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): Arteriolar narrowing · glomerulosclerosis ·
    interstitial fibrosis · **Progressive nephron loss**
  Intervention box (center): Blood-pressure control to target · RAAS blockade
    (ACEi/ARB) · sodium restriction · SGLT2 inhibitors
  Benefit box (pale blue): ↓ Intraglomerular pressure · ↓ Proteinuria ·
    Slower eGFR decline · ↓ Cardiovascular risk
```

---

## 7. Potassium & Hyperkalemia in CKD
**Guide:** `guides/potassium-hyperkalemia-ckd.html` · **Suggested file:** `potassium-hyperkalemia-mechanism.png`

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for injury/cardiac
risk, blue for therapy, pale pink pathology box, pale blue benefit box. No
photorealism, no dark background, no clutter. 16:9.

TOPIC: Why CKD causes high potassium and why it threatens the heart.
DISEASE CONTEXT: Hyperkalemia in CKD.
CENTRAL MECHANISM: Reduced kidney function and aldosterone resistance impair
distal potassium excretion → rising serum potassium → altered cardiac membrane
excitability.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "CKD." Dashed
connector to the magnified distal nephron.

MAGNIFIED MECHANISM PANEL (center, dashed border):
Distal tubule / collecting-duct principal cell highlighted pale yellow.
Callouts:
  • "↓ Distal K+ secretion (low flow, ↓ aldosterone effect, drugs: RAASi,
    K-sparing diuretics)"
  • "Result: ↑ Serum potassium (hyperkalemia)"

SECOND MAGNIFIED INSET (right, dashed border):
A cardiac myocyte with a small ECG tracing. Callouts:
  • "↑ Extracellular K+ → altered membrane potential"
  • "Peaked T waves → widened QRS → arrhythmia risk"

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): ↓ Renal K+ excretion · contributing medications ·
    ↑ Serum potassium · **Cardiac arrhythmia risk**
  Intervention box (center): Dietary potassium moderation · loop/thiazide
    diuretics · potassium binders · review of RAASi dosing (don't stop
    cardioprotective therapy unnecessarily)
  Benefit box (pale blue): Normalized serum potassium · Safer continuation of
    cardiorenal-protective drugs · ↓ Arrhythmia risk
```

---

## 8. Heart–Kidney Connection (Cardiorenal Syndrome)
**Guide:** `guides/heart-kidney-connection.html` · **Suggested file:** `heart-kidney-mechanism.png`

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for injury, blue
for therapy/venous, pale pink pathology box, pale blue benefit box. No
photorealism, no dark background, no clutter. 16:9.

TOPIC: How heart failure and kidney disease worsen each other (cardiorenal
syndrome).
DISEASE CONTEXT: Cardiorenal syndrome.
CENTRAL MECHANISM: Low cardiac output and venous congestion reduce kidney
perfusion → neurohormonal activation (RAAS, sympathetic) → sodium/water
retention → more congestion — a bidirectional spiral.

ORGAN-LEVEL PANEL (left):
Two simplified organs side by side — a heart and a kidney in light gray-blue,
joined by bidirectional arrows labeled "Cardiorenal syndrome." Heart callout:
"↓ Cardiac output + ↑ venous congestion." Dashed connector from the kidney to
the magnified nephron.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A glomerulus + tubule highlighted pale yellow. Callouts:
  • "↓ Renal perfusion + ↑ central venous pressure → ↓ effective filtration"
  • "RAAS & sympathetic activation → Na+/water retention"
  • "Tubular congestion/hypoxia → injury & fibrosis"
  • Curved feedback arrow: "Fluid retention → worsening cardiac congestion."

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): ↓ Cardiac output · venous congestion · RAAS /
    sympathetic activation · **Bidirectional heart–kidney decline**
  Intervention box (center): Decongestion (loop diuretics) · RAAS blockade ·
    SGLT2 inhibitors · guideline-directed heart-failure therapy
  Benefit box (pale blue): Relieved congestion · stabilized eGFR · ↓
    Hospitalizations · improved survival
```

---

### Post-generation checklist
Once images are received, for each guide:
1. Save the PNG into the guide's image folder with the suggested filename.
2. Insert as a `<figure>` with a descriptive multilingual `<figcaption>` (en/tl/ceb/kap) at the suggested placement.
3. Run `python3 patch_hero_fetchpriority.py --guide <file>` only if the new image becomes the hero (these are mid-body, so usually not).
4. Add `og:image` tags via the `williamriveromd-local-image-generator` skill if any becomes the guide's primary share image.
