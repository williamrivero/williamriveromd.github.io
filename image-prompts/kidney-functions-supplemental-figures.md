# Kidney Functions — Supplemental Mechanism Figures (7)

**Guide:** `guides/kidney-functions.html`
Generated with the **`williamriveromd-biomedical-mechanism-figure`** skill (Stage 1).

A companion to `kidney-functions-image-prompts.md`. These seven figures give a
dedicated pathway schematic to the sections that previously had **no image of their
own**, each deliberately differentiated from the shared figures in the main pack:

| File | Section | Distinct from |
|---|---|---|
| `kidney-functions-water-balance.png` | `#fn-water` | urine-concentration (gradient) → here: collecting-duct ADH/AQP2 switch |
| `kidney-functions-sodium-handling.png` | `#fn-sodium` | raas-bp (hormonal) → here: segmental transporter map + diuretic sites |
| `kidney-functions-renin.png` | `#fn-renin` | raas-bp (cascade) → here: JGA sensing/triggers |
| `kidney-functions-vitamin-d.png` | `#fn-vitd` | bone-mineral-axis → here: skin→liver→kidney 1-α-hydroxylase chain |
| `kidney-functions-bone-protection.png` | `#fn-bone` | bone-mineral-axis → here: skeleton/turnover + FGF23 conversation |
| `kidney-functions-oxygen-sensing.png` | `#fn-oxygen` | epo-hif (output) → here: PHD–HIF–VHL molecular switch |
| `kidney-functions-never-rest.png` | `#never-rest` | (new) "always-on" concept figure |

**Shared style (every prompt):** flat vector, soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connectors, muted clinical palette (light gray-blue
anatomy, soft yellow highlights, red for arteries/injury, blue for protective/therapeutic,
pale pink pathology box, pale blue benefit box); no photorealism, no dark background, no
clutter; 16:9; bottom-right semi-transparent navy `© williamriveromd.com`.

**Workflow:** paste each PROMPT into the ChatGPT Image Generator GPT, generate at 16:9,
save under `images/` with the exact filename; the in-page `<figure>` blocks can then be
wired at the listed anchors (Stage 2).

---

## 1. Water Balance — ADH & Aquaporins
**Suggested file:** `kidney-functions-water-balance.png` · **Size:** 16:9
**Placement:** `#fn-water`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector illustration with soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connector lines, generous whitespace. Muted
clinical palette — light gray-blue anatomy, soft yellow highlighted segments, red for
arteries/injury, blue for protective/therapeutic, pale pink pathology box, pale blue
benefit box; no photorealism, no dark background, no clutter. Bottom-right: small
semi-transparent navy "© williamriveromd.com".

TOPIC: How vasopressin (ADH) gates aquaporin-2 (AQP2) in collecting-duct principal
cells to control water reabsorption — the body's precision water switch.
DISEASE CONTEXT: SIADH (too little water excretion → edema, hyponatremia) vs.
central/nephrogenic diabetes insipidus (no ADH effect → polyuria, hypernatremia).
CENTRAL MECHANISM: Posterior pituitary releases ADH → ADH binds V2 receptor on
collecting-duct principal cell → cAMP cascade → intracellular AQP2 vesicles fuse with
apical membrane → luminal water flows into cell → exits basolaterally via AQP3/AQP4
into the hypertonic medullary interstitium → enters peritubular capillaries. Note that
the proximal tubule reabsorbs ~65–70% of filtered water isosmotically upstream (via
constitutive AQP1) — the collecting duct is the regulated switch, not the volume
workhorse.

ORGAN-LEVEL PANEL (left): kidney cross-section (light gray-blue) with cortex-to-medulla
shading, collecting duct highlighted in soft yellow, labeled "Collecting duct — the
regulated water switch." A small upstream note: "Proximal tubule: ~65–70% water
reabsorbed isosmotically (AQP1, constitutive — no ADH needed)." Dashed connector
from collecting duct to the magnified principal cell.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a single collecting-duct
principal cell oriented between tubular lumen (top) and hypertonic interstitium
(bottom). Show the pathway in two states side by side, separated by a thin vertical
dashed divider:
  LEFT STATE — "No ADH (water diuresis)":
    • Apical membrane: AQP2 vesicles stored in cytoplasm, not inserted
    • Label: "Membrane water-impermeable → dilute urine"
  RIGHT STATE — "ADH present (water retention)":
    • Hypothalamus/posterior pituitary small inset (top): "↓ Blood volume or ↑
      osmolality → ADH release"
    • ADH arrives at basolateral V2 receptor → Gs → adenylyl cyclase → ↑ cAMP →
      PKA activation (label each step with a small arrow chain)
    • AQP2 vesicles (labeled "AQP2") traffick to apical membrane and fuse
    • Luminal water arrow crossing apical AQP2 into cell
    • Basolateral membrane: AQP3 and AQP4 labeled — "constitutive basolateral exit"
    • Water arrow from cell into interstitium → peritubular capillary (blue)
    • Label: "Concentrated urine"
Add a concise callout: "ADH also ↑ AQP2 gene expression (long-term adaptation)."
Add a small osmolality scale on the right: "Urine: 50–1200 mOsm/kg depending on
ADH tone."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): ↑↑ ADH (SIADH, heart failure, cirrhosis) → excess water
    retention → dilutional hyponatremia, edema, pulmonary edema; ↓↓ ADH or V2/AQP2
    defect → nephrogenic/central diabetes insipidus → polyuria (>3 L/day), dehydration,
    hypernatremia
  Intervention box (center): Fluid restriction + V2 antagonists (tolvaptan) for SIADH
    · desmopressin (DDAVP) for central DI · treat nephrogenic DI: low-Na diet + thiazide
    diuretics + NSAIDs (reduce flow to collecting duct)
  Benefit box (pale blue): Stable blood volume · serum sodium 135–145 mEq/L ·
    appropriate urine output matched to hydration state
```

---

## 2. Sodium Handling — Segmental Transporter Map
**Suggested file:** `kidney-functions-sodium-handling.png` · **Size:** 16:9
**Placement:** `#fn-sodium`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector illustration with soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connector lines, generous whitespace. Muted
clinical palette — light gray-blue anatomy, soft yellow highlighted segments, red for
arteries/injury, blue for protective/therapeutic, pale pink pathology box, pale blue
benefit box; no photorealism, no dark background, no clutter. Bottom-right: small
semi-transparent navy "© williamriveromd.com".

TOPIC: The four major sodium transporters by nephron segment — where sodium is
reabsorbed and where key diuretics act.
DISEASE CONTEXT: Sodium retention → hypertension, edema, heart failure; salt-wasting
→ hypovolemia, hypotension.
CENTRAL MECHANISM: The nephron filters ~25,000 mEq Na⁺/day. Four sequentially active
transporters reclaim 99%+: NHE3 (± SGLT2) in the proximal tubule handles the bulk
(~65%); NKCC2 in the thick ascending limb (~25%); NCC in the distal convoluted tubule
(~5%); ENaC (aldosterone-driven) in the collecting duct (~3%) fine-tunes excretion.
Each transporter is the target of a major diuretic class — making this map the
pharmacologic framework for clinical diuretic selection.

ORGAN-LEVEL PANEL (left): kidney cross-section (light gray-blue), labeled "~25,000
mEq Na⁺ filtered/day — 99%+ reclaimed." Dashed connector to the magnified nephron.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a single anatomically
plausible nephron drawn as a vertical loop, with each segment color-coded by a soft
yellow band and labeled with its transporter, the approximate fraction of Na⁺
reabsorbed, and the diuretic that blocks it. Present as four stacked callout boxes
beside each segment:
  Segment 1 — Proximal tubule (largest segment, ~65%):
    • NHE3 (Na⁺/H⁺ exchanger 3) — apical; coupled to HCO₃⁻ reclamation
    • SGLT2 (Na⁺-glucose cotransporter 2) — apical; co-reabsorbs glucose
    • Callout: "~65% Na⁺ reabsorbed; isosmotic water follows"
    • Drug: SGLT2 inhibitors (empagliflozin, dapagliflozin) block SGLT2 → modest
      natriuresis + glycosuria; no direct NHE3 inhibitor in routine clinical use
  Segment 2 — Thick ascending limb of Henle (TAL, ~25%):
    • NKCC2 (Na⁺-K⁺-2Cl⁻ cotransporter 2) — apical; water-impermeable segment
    • Callout: "~25% Na⁺; builds medullary osmotic gradient"
    • Drug: Loop diuretics (furosemide, bumetanide, torsemide) — most potent
      natriuresis — highlighted in a small red-outlined pill icon
  Segment 3 — Distal convoluted tubule (DCT, ~5%):
    • NCC (Na⁺-Cl⁻ cotransporter) — apical
    • Callout: "~5% Na⁺; also reabsorbs Ca²⁺ and Mg²⁺"
    • Drug: Thiazide diuretics (hydrochlorothiazide, chlorthalidone) — moderate
      natriuresis; ↑ Ca²⁺ reabsorption (useful in hypercalciuria)
  Segment 4 — Collecting duct (ENaC, ~1–3%):
    • ENaC (epithelial Na⁺ channel) — apical; aldosterone-upregulated
    • Callout: "Fine-tuning; aldosterone drives ENaC + Na⁺/K⁺-ATPase"
    • Drugs: K-sparing diuretics — amiloride/triamterene block ENaC directly;
      spironolactone/eplerenone/finerenone block aldosterone receptor → ↓ ENaC
      expression; add small callout: "Spare K⁺ — useful with loop/thiazide"
Draw a thin horizontal bar at the bottom of the nephron showing cumulative Na⁺
remaining at each segment: 100% → 35% → 10% → 5% → <1% excreted.

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Excess aldosterone (primary hyperaldosteronism, heart
    failure, cirrhosis) · dysregulated RAAS · high dietary salt → ↑ NHE3/NKCC2/ENaC
    activity → sodium retention → hypertension, edema, ascites, heart failure
  Intervention box (center): Dietary Na⁺ restriction · RAAS blockade (ACEi/ARB/MRA) ·
    diuretics matched to site of action (loop > thiazide > K-sparing) · SGLT2 inhibitors
  Benefit box (pale blue): ↓ Volume overload · ↓ Blood pressure · cardiac and renal
    protection
```

---

## 3. Renin Release — The JGA Pressure Sensor
**Suggested file:** `kidney-functions-renin.png` · **Size:** 16:9
**Placement:** `#fn-renin`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector illustration with soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connector lines, generous whitespace. Muted
clinical palette — light gray-blue anatomy, soft yellow highlighted segments, red for
arteries/injury, blue for protective/therapeutic, pale pink pathology box, pale blue
benefit box; no photorealism, no dark background, no clutter. Bottom-right: small
semi-transparent navy "© williamriveromd.com".

TOPIC: The juxtaglomerular apparatus (JGA) as a multi-input pressure and NaCl sensor
that triggers renin release — the initiating step of the RAAS.
DISEASE CONTEXT: Excess renin → hypertension, proteinuric kidney disease, secondary
hyperaldosteronism; inadequate activation → hypotension, impaired perfusion.
CENTRAL MECHANISM: Three distinct signals converge on the JGA to release renin from
granular (juxtaglomerular) cells in the afferent arteriole wall: (1) decreased
afferent arteriolar wall stretch/pressure (baroreceptor mechanism); (2) decreased
NaCl concentration sensed by macula densa cells (tubuloglomerular feedback limb);
(3) increased β1-adrenergic sympathetic tone. Renin cleaves angiotensinogen →
angiotensin I (brief downstream note only — the full RAAS cascade is covered in the
RAAS figure).

ORGAN-LEVEL PANEL (left): kidney cross-section (light gray-blue) labeled "Blood
pressure and volume sensor," with the cortex highlighted. Dashed connector to the
magnified JGA.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a close-up of the
juxtaglomerular apparatus at the vascular pole of a glomerulus. Show three distinct
structures, each with its trigger:
  Structure 1 — Granular (JG) cells in the afferent arteriole wall (soft yellow):
    • Labeled "Baroreceptor / pressure sensor"
    • Trigger arrow: "↓ Afferent arteriolar stretch (↓ blood pressure / ↓ volume) →
      ↑ renin secretion"
    • Trigger arrow: "↑ Afferent arteriolar stretch → ↓ renin secretion (pressure
      natriuresis)"
    • Renin granules shown as small circles inside the cell
  Structure 2 — Macula densa cells (tubular epithelium, pale blue highlight):
    • Labeled "NaCl sensor (distal tubule end)"
    • Trigger arrow: "↓ NaCl delivery (↓ GFR or ↓ volume) → paracrine signal →
      ↑ renin release from JG cells"
    • Note: "NaCl sensed via NKCC2 at apical membrane"
    • Second note: "↑ NaCl → prostaglandin E2/NO counter-signal → ↓ renin"
  Structure 3 — Sympathetic nerve terminal (red nerve ending near afferent arteriole):
    • Labeled "β1 adrenergic input"
    • Trigger arrow: "↑ Sympathetic tone (stress, hypovolemia, upright posture) →
      β1 receptor → ↑ cAMP in JG cell → ↑ renin"
    • Drug note: "β-blockers (propranolol, carvedilol, metoprolol) → ↓ renin by
      blocking β1 input"
Draw a small converging arrow from all three structures to a single output: "Renin
released → angiotensinogen → angiotensin I → (ACE, in pulmonary capillaries) →
angiotensin II [see RAAS figure]." Keep this brief — the downstream cascade is
intentionally out of scope.
Add a callout box: "ACE inhibitors and ARBs raise renin levels via negative-feedback
loss (reactive hyperreninemia) — monitor accordingly."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): Renal artery stenosis · chronic volume depletion · high
    sympathetic tone → ↑↑ renin → secondary hypertension, proteinuria,
    hypokalemia (aldosterone excess); JG cell destruction in advanced CKD/tubulointerstitial
    fibrosis → inadequate renin → hypotension, impaired perfusion, type IV RTA
  Intervention box (center): RAAS blockade (ACEi/ARB) — reduce angiotensin II
    regardless of renin level · β-blockers — suppress sympathetic renin drive ·
    direct renin inhibitors (aliskiren — limited use) · treat renal artery stenosis
  Benefit box (pale blue): Defended perfusion pressure · controlled sodium balance ·
    protected BP set-point · cardiorenal protection
```

---

## 4. Vitamin D Activation — The Kidney as an Endocrine Factory
**Suggested file:** `kidney-functions-vitamin-d.png` · **Size:** 16:9
**Placement:** `#fn-vitd`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector illustration with soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connector lines, generous whitespace. Muted
clinical palette — light gray-blue anatomy, soft yellow highlighted segments, red for
arteries/injury, blue for protective/therapeutic, pale pink pathology box, pale blue
benefit box; no photorealism, no dark background, no clutter. Bottom-right: small
semi-transparent navy "© williamriveromd.com".

TOPIC: The three-organ vitamin D activation chain — skin/diet → liver → kidney →
active calcitriol — and the tight regulation of the renal 1-alpha hydroxylase step.
DISEASE CONTEXT: CKD → loss of 1-alpha hydroxylase → ↓ calcitriol → secondary
hyperparathyroidism, CKD-mineral and bone disorder (CKD-MBD).
CENTRAL MECHANISM: UV-B converts skin 7-dehydrocholesterol → vitamin D3 (cholecalciferol);
the liver hydroxylates it at C-25 (CYP2R1) → 25-hydroxyvitamin D (calcidiol, the
circulating storage form). The kidney proximal tubule performs the regulated final
hydroxylation at C-1 (CYP27B1 / 1-alpha hydroxylase) → 1,25-dihydroxyvitamin D
(calcitriol, the biologically active hormone). Regulation: 1-alpha hydroxylase is
stimulated by ↑ PTH, ↓ serum calcium, ↓ serum phosphate; suppressed by FGF23 and
↑ serum phosphate. Calcitriol feeds back to suppress PTH and stimulate FGF23.

ORGAN-LEVEL PANEL (left): a vertical three-organ chain (top to bottom):
  • Skin (small human silhouette + sun icon): "UV-B → Vitamin D3 (cholecalciferol)
    from 7-dehydrocholesterol" AND "Dietary sources: fatty fish, fortified milk"
  • Liver (brown lobe): "CYP2R1 → 25-hydroxyvitamin D (calcidiol) — storage form;
    normal range 30–80 ng/mL"
  • Kidney (light gray-blue, proximal tubule highlighted): "CYP27B1 (1-alpha
    hydroxylase) → 1,25-dihydroxyvitamin D (calcitriol) — ACTIVE hormone"
Each organ connected by a downward arrow labeled with the product. Dashed connector
from the kidney to the magnified proximal tubule cell.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a proximal tubule epithelial
cell centered in the panel. Show the 1-alpha hydroxylase enzyme inside the cell
(mitochondrial location, label "mitochondria"). Four regulatory arrows pointing to
the enzyme:
  Stimulators (blue arrows, pointing IN):
    ↑ PTH → "+ 1-alpha hydroxylase" (from parathyroid icon)
    ↓ Ca²⁺ → "+ 1-alpha hydroxylase"
    ↓ PO₄³⁻ → "+ 1-alpha hydroxylase"
  Inhibitors (red arrows, pointing IN):
    ↑ FGF23 → "− 1-alpha hydroxylase" (from bone icon)
    ↑ PO₄³⁻ → "− 1-alpha hydroxylase"
    Calcitriol itself → "− 1-alpha hydroxylase (short-loop negative feedback)"
From the cell, an arrow: "Calcitriol released → bloodstream." Then fan out to three
downstream targets with pale blue callouts:
  • Gut (intestine icon): "↑ Calbindin → ↑ Ca²⁺ absorption (duodenum/jejunum)"
  • Bone (bone icon): "↑ Osteoblast maturation → bone mineralization"
  • Parathyroid (gland icon): "↓ PTH synthesis (negative feedback loop)"

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD (GFR <45) → progressive loss of functioning proximal
    tubule mass → ↓ 1-alpha hydroxylase activity → ↓ calcitriol → ↓ gut Ca²⁺
    absorption → hypocalcemia → ↑↑ PTH (secondary hyperparathyroidism) → bone
    resorption, vascular calcification, CKD-MBD
  Intervention box (center): Active vitamin D analogs — calcitriol (1,25-OH₂ vitamin D)
    or paricalcitol/doxercalciferol (selective VDR agonists, lower hypercalcemia risk) ·
    25-OH vitamin D supplementation for deficiency · calcimimetics (cinacalcet) to
    suppress PTH · phosphate binders
  Benefit box (pale blue): ↑ Intestinal Ca²⁺ absorption · ↓ PTH · maintained bone
    mineralization · reduced fracture risk · slowed CKD-MBD progression
```

---

## 5. Bone Protection — The Skeleton–Kidney Conversation
**Suggested file:** `kidney-functions-bone-protection.png` · **Size:** 16:9
**Placement:** `#fn-bone`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector illustration with soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connector lines, generous whitespace. Muted
clinical palette — light gray-blue anatomy, soft yellow highlighted segments, red for
arteries/injury, blue for protective/therapeutic, pale pink pathology box, pale blue
benefit box; no photorealism, no dark background, no clutter. Bottom-right: small
semi-transparent navy "© williamriveromd.com".

TOPIC: The bone–kidney bi-directional conversation that maintains skeletal integrity —
bone signals the kidney (FGF23), the kidney signals the bone (calcitriol, Ca²⁺, PO₄)
— and how CKD disrupts the dialogue leading to renal osteodystrophy.
DISEASE CONTEXT: CKD-mineral and bone disorder (CKD-MBD) — abnormal bone turnover
(adynamic, osteoporosis, osteitis fibrosa cystica), fractures, bone pain, and
co-occurring vascular calcification.
CENTRAL MECHANISM: Normal bone remodeling balances osteoblast (formation) and
osteoclast (resorption) activity. The kidney supplies calcitriol (↑ osteoblast
maturation), Ca²⁺, and phosphate (mineralization substrates). Bone releases FGF23
(osteocyte-derived) → kidney phosphaturia and ↓ calcitriol. PTH (from parathyroid)
activates osteoclasts to free Ca²⁺ when serum Ca²⁺ is low. Klotho (kidney) amplifies
FGF23 signaling. Together, the Ca–PO₄–PTH–calcitriol–FGF23–Klotho loop keeps bone
turnover balanced and the skeleton mineralized.

ORGAN-LEVEL PANEL (left): a simplified long bone cross-section (femur, light
gray-blue cortex + yellow spongy core) labeled "Normal bone remodeling." Show two
cell icons side by side:
  Osteoblast (rounded, labeled "OB"): "Bone formation — lays new osteoid"
  Osteoclast (multinucleated, labeled "OC"): "Bone resorption — dissolves old matrix"
Between them: "Balanced remodeling → strong, mineralized bone."
Below the bone: small inset "Osteocyte in lacuna: secretes FGF23 → signals kidney."
Dashed connector from the bone to the magnified panel.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a circular hub-and-spoke
diagram with the bone–kidney axis at the center, showing the full Ca–PO₄–PTH–
calcitriol–FGF23–Klotho loop:
  BONE node (top): "Osteocyte → FGF23 ↑ when phosphate ↑"
    Arrow down-right to KIDNEY: "FGF23 → (via Klotho co-receptor) → kidney"
  KIDNEY node (right): "1-alpha hydroxylase → calcitriol; phosphaturia via ↓ NaPi-IIa"
    Arrow right to GUT: "Calcitriol → ↑ Ca²⁺ absorption"
    Arrow up-left to BONE: "Calcitriol → ↑ osteoblast maturation; PO₄ delivery"
    Arrow up to PARATHYROID: "↑ Ca²⁺ → ↓ PTH (negative feedback)"
  PARATHYROID node (left): "PTH ↑ when Ca²⁺ ↓"
    Arrow down to BONE: "PTH → ↑ RANKL → ↑ osteoclast activity → ↑ Ca²⁺ release"
    Arrow right to KIDNEY: "PTH → ↑ Ca²⁺ reabsorption, ↑ phosphate excretion,
      ↑ 1-alpha hydroxylase"
  GUT node (bottom): "↑ Ca²⁺ absorption → ↑ serum Ca²⁺ → ↓ PTH"
Add labels for Klotho: "Klotho (kidney tubule) — FGF23 co-receptor + soluble
anti-calcification factor." Mark the normal-physiology balance arrows in blue and
the CKD-disrupted arrows in red dashes.

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD → ↓ calcitriol · ↑ phosphate retention · ↓ Klotho
    · ↑↑ PTH (secondary HPT) → ↑ osteoclast overactivity · impaired osteoblast function →
    Osteitis fibrosa cystica (high-turnover) · adynamic bone disease (low-turnover) ·
    mixed uremic osteodystrophy; co-occurring vascular calcification from high Ca × PO₄
    product; fractures, bone pain, deformity
  Intervention box (center): Phosphate binders (sevelamer, calcium carbonate, lanthanum)
    · active vitamin D analogs (calcitriol/paricalcitol) · calcimimetics (cinacalcet) to
    suppress PTH · dietary phosphate restriction · denosumab or bisphosphonates for
    osteoporosis (use with caution in CKD)
  Benefit box (pale blue): Balanced osteoblast/osteoclast activity · normal bone
    turnover markers · mineralized, fracture-resistant skeleton · ↓ vascular calcification
```

---

## 6. Oxygen Sensing — The PHD–HIF Molecular Switch
**Suggested file:** `kidney-functions-oxygen-sensing.png` · **Size:** 16:9
**Placement:** `#fn-oxygen`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector illustration with soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connector lines, generous whitespace. Muted
clinical palette — light gray-blue anatomy, soft yellow highlighted segments, red for
arteries/injury, blue for protective/therapeutic, pale pink pathology box, pale blue
benefit box; no photorealism, no dark background, no clutter. Bottom-right: small
semi-transparent navy "© williamriveromd.com".

TOPIC: The molecular PHD–HIF oxygen-sensing switch in renal interstitial cells, and the
kidney's structural vulnerability to hypoxia from cortex to outer medulla.
DISEASE CONTEXT: CKD → capillary rarefaction, fibrosis, mitochondrial dysfunction →
chronic tubulointerstitial hypoxia → maladaptive HIF signaling → fibrosis and
progressive nephron loss.
CENTRAL MECHANISM: In normoxia, prolyl hydroxylase domain enzymes (PHD1/2/3) use O₂ +
α-ketoglutarate to hydroxylate two proline residues on HIF-α subunits → recognized by
von Hippel–Lindau (VHL) protein → polyubiquitination → proteasomal degradation (HIF-α
short half-life <5 minutes). In hypoxia, PHD activity drops (no O₂ substrate) → HIF-α
accumulates, translocates to nucleus, dimerizes with HIF-β (ARNT) → binds hypoxia-response
elements (HREs) → transcribes adaptive genes: EPO (erythropoiesis), VEGF (angiogenesis),
glucose transporters (GLUT1), glycolytic enzymes, and survival factors. In the kidney,
this is the primary mechanism for EPO production; the cortex/outer medulla sit near a
delicate O₂ balance because proximal tubular Na⁺ transport is energetically expensive.

ORGAN-LEVEL PANEL (left): kidney cross-section with a vertical O₂ gradient shading:
  Cortex (top, lighter blue): "PO₂ ~50 mmHg — high metabolic demand (proximal tubule
    oxidative phosphorylation)"
  Outer medulla (middle, medium gray): "PO₂ ~10–20 mmHg — near-hypoxic baseline
    (TAL active transport + countercurrent shunting)"
  Inner medulla/papilla (bottom, slightly darker): "PO₂ ~5–10 mmHg"
Labeled note: "The kidney is structurally poised near the hypoxic threshold — efficient
but fragile." Small red arrow: "CKD → capillary rarefaction → ↓ O₂ delivery → diffuse
tubulointerstitial hypoxia." Dashed connector to the magnified interstitial cell.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a peritubular interstitial
fibroblast-like cell (EPO-producing cell) shown in two states side by side:
  LEFT STATE — "NORMOXIA" (normal O₂):
    • PHD enzymes (labeled "PHD1/2/3") in cytoplasm, active
    • HIF-α being hydroxylated (small OH groups on proline residues)
    • VHL protein binds hydroxylated HIF-α → "Ubiquitin proteasome" degradation
      (show as a small funnel icon labeled "degraded")
    • Nucleus: HIF-α absent → "No HRE transcription"
    • Label: "HIF-α half-life <5 min"
  RIGHT STATE — "HYPOXIA" (↓ O₂):
    • PHD enzymes labeled "PHD — inhibited (no O₂ substrate)"
    • HIF-α: not hydroxylated → VHL cannot bind → escapes degradation
    • HIF-α translocates to nucleus → dimerizes with HIF-β (ARNT) → binds HRE
    • Gene transcription output arrows (blue):
      "EPO → erythropoiesis (→ bone marrow icon)"
      "VEGF → angiogenesis"
      "GLUT1 → glucose uptake ↑"
      "Glycolytic enzymes → anaerobic ATP"
      "Survival genes → ↓ apoptosis"
Add a small callout: "PHD also requires iron and ascorbate as co-factors — iron
deficiency may blunt the hypoxic response."
Add a drug note (pale blue box): "HIF-prolyl hydroxylase inhibitors (roxadustat,
daprodustat, vadadustat) — oral agents that inhibit PHD → stabilize HIF-α →
↑ EPO → treat anemia of CKD (approved/available in select regions)."

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink): CKD → peritubular capillary rarefaction · interstitial
    fibrosis → chronic tubulointerstitial hypoxia → maladaptive chronic HIF activation
    → VEGF-driven aberrant fibrosis, TGF-β upregulation, EMT of tubular cells →
    accelerated CKD progression; simultaneously, EPO-producing interstitial cells lost
    → anemia of CKD
  Intervention box (center): Optimize perfusion (BP control, RAAS blockade, SGLT2
    inhibitors → ↓ intraglomerular hypertension) · ESA therapy · HIF-PH inhibitors
    (proposed/approved in select indications) · anti-fibrotic agents (under study)
  Benefit box (pale blue): Restored EPO production · ↑ hemoglobin · adaptive
    angiogenesis · slowed tubulointerstitial fibrosis · preserved nephron mass
```

---

## 7. The Kidneys Never Truly Rest
**Suggested file:** `kidney-functions-never-rest.png` · **Size:** 16:9
**Placement:** `#never-rest`

```
Create a publication-grade biomedical mechanism schematic, scientific review-article
style, 16:9. Flat vector illustration with soft semi-3D shading, white background,
clean sans-serif labels, thin dashed connector lines, generous whitespace. Muted
clinical palette — light gray-blue anatomy, soft yellow highlighted segments, red for
arteries/injury, blue for protective/therapeutic, pale pink pathology box, pale blue
benefit box; no photorealism, no dark background, no clutter. Bottom-right: small
semi-transparent navy "© williamriveromd.com".

TOPIC: The kidney's continuous 24/7 operation — never fully resting, yet capable of
modulating workload; the concept of renal functional reserve and the closest the
kidney gets to "rest" through reduced hyperfiltration.
DISEASE CONTEXT: The paradox that the kidney cannot stop working, yet has built-in
reserve and circadian modulation — understanding this helps explain why nephron loss
is so consequential and why reducing intraglomerular pressure (RAAS blockade + SGLT2
inhibitors) is the best clinical approximation of protecting kidney longevity.
CENTRAL MECHANISM: The kidney continuously filters, reabsorbs, secretes, and produces
hormones — before birth, through sleep, under illness, until death. Yet it is not
always at full capacity: (1) Circadian biology: during sleep, renal blood flow ↓ ~10%,
GFR ↓ 10–20%, ADH ↑ → concentrated, low-volume nocturnal urine, mild sodium
retention. (2) Functional reserve: ~2 million nephrons normally operate below maximum
filtration capacity — GFR rises measurably after a high-protein meal or in pregnancy
(hyperfiltration), demonstrating reserve. (3) Maintenance: mitochondrial turnover,
autophagy, and DNA repair run continuously in tubular cells. The nearest clinical
equivalent to "lowering the engine's RPM" is reducing intraglomerular pressure with
RAAS blockers + SGLT2 inhibitors.

ORGAN-LEVEL PANEL (left): a kidney in light gray-blue with a subtle integrated
24/7/365 clock motif — a clean analog clock face overlaid lightly on the kidney
cortex, labeled "Continuously active — before birth until death." Below the kidney,
a small timeline bar: "Fetal life → childhood → adult → pregnancy → old age → end stage."
Dashed connector to the magnified nephron comparison panel.

MAGNIFIED MECHANISM PANEL (center/right, dashed border): a split-panel nephron
comparison with a vertical dashed divider:
  LEFT HALF — "AWAKE / ACTIVE STATE":
    • GFR: "↑ or baseline (90–120 mL/min/1.73m²)"
    • Renal blood flow: "Full" (solid renal artery arrow, red)
    • ADH: "Low to moderate → dilute-to-isosmotic urine"
    • Urine output: "Appropriate — 0.5–1 mL/min"
    • Na⁺ excretion: "Matched to intake"
    • Label: "High metabolic demand — proximal tubule O₂ consumption near maximum"
  RIGHT HALF — "SLEEP / REST STATE":
    • GFR: "↓ 10–20% (but never stops)"
    • Renal blood flow: "↓ ~10%" (thinner artery arrow, dashed)
    • ADH: "↑ markedly → concentrated nocturnal urine"
    • Urine output: "↓ — nocturia prevention"
    • Na⁺ excretion: "Mild transient retention (reverses by morning)"
    • Label: "Still filtering every minute of every night"
  Center note between the two halves: "No true 'off' switch — closest analogy: a
  factory that reduces its production line speed at night but never shuts down."

Three small inset boxes arranged along the bottom of the magnified panel (above the
summary flow):
  Inset A (soft yellow, "Functional Reserve"):
    "~2 million nephrons — normally < maximum capacity. GFR rises after high-protein
    meal (+20–40%) or in pregnancy (+50%) → reserve demonstrated. Nephron loss →
    survivors hyperfiltrate to compensate → accelerated injury."
  Inset B (soft blue, "Cellular Maintenance"):
    "Mitochondrial turnover (mitophagy) · autophagy · DNA mismatch repair — run
    continuously in proximal tubule and TAL cells even during 'reduced' nighttime
    workload."
  Inset C (pale gray, "Research Frontier"):
    "Hibernating animals (black bear, ground squirrel): GFR drops sharply during
    torpor yet uremia is avoided — novel adaptations studied for future AKI and
    CKD therapies (proposed/experimental)." Include tiny bear icon.

BOTTOM SUMMARY FLOW (arrows):
  Pathology box (pale pink, "The challenge"): No true resting state → continuous
    filtration, electrolyte balance, hormone production required every minute;
    nephron loss → surviving nephrons hyperfiltrate → intraglomerular hypertension →
    accelerated scarring → CKD progression spiral
  Intervention box (center): The closest clinical equivalent to 'lowering the RPM':
    RAAS blockade (ACEi/ARB) → efferent arteriole dilation → ↓ intraglomerular
    pressure; SGLT2 inhibitors → ↑ tubuloglomerular feedback via macula densa →
    afferent arteriole constriction → ↓ hyperfiltration; combined: fewer mechanical
    cycles per nephron per day → slowed structural injury
  Benefit box (pale blue, "Functional reserve protects"): 2 million nephrons provide
    buffer to meet extra demand and tolerate early nephron loss; ↓ intraglomerular
    pressure slows CKD progression; circadian GFR modulation spares kidneys nightly —
    sleep is the kidney's nearest thing to maintenance mode
```
