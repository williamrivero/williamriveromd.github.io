# Kidney Physiology — Image Generation Pack

**Guide:** `guides/kidney-physiology.html` (immersive dark scrollytelling redo)
**Prompt style:** `williamriveromd-biomedical-mechanism-figure` (Stage 1)
**Total images to generate:** 16 (keep the existing `kidney-physiology-og.png` as-is)

---

## House style — apply to EVERY prompt below

> Publication-grade **biomedical mechanism schematic**, scientific review-article style.
> **Flat vector illustration with soft semi-3D shading on a WHITE background.**
> Muted clinical palette: light gray-blue anatomy · soft yellow for highlighted
> nephron/tubular segments · red for arteries/injury/oxidative stress · blue for
> veins/protective or therapeutic effects · pale-pink pathology boxes · pale-blue
> benefit/outcome boxes. Thin **dashed** boxes around magnified panels, with dashed
> connector lines. Clean sans-serif typography, medically precise, legible at
> slide size. Generous whitespace, minimal clutter. **No** photorealism, **no**
> dark/navy/black background, **no** decorative effects, **no** cartoon styling,
> **no** gibberish text. Small semi-transparent navy **`© williamriveromd.com`**
> in the bottom-right corner (bottom-center for portrait).

**Where these go on the page:** all figures are light-background "luminous cards"
that sit on the page's near-black canvas (a dark scrim is applied in-page for text
contrast). The 8 embryology frames (Section A) are used as a **scroll-synced
background that morphs from pronephros → mature kidney**, so they MUST share one
consistent framing/scale/viewpoint so they cross-fade cleanly (see Section A note).

**Generator:** paste each prompt into the ChatGPT Image Generator GPT
(https://chatgpt.com/g/g-pmuQfob8d-image-generator), one at a time. Output `.png`.

---

## SECTION A — Embryology scroll-background frames (8)

> **CONSISTENCY NOTE (critical for the scroll morph):** Generate all 8 at the same
> aspect ratio (**4:3, 1536 × 1152**), same centered composition, same illustration
> scale and viewpoint, same line weight and palette, so that when cross-faded in
> sequence they read as **one kidney developing**. Each frame = a labeled
> developmental stage; keep a small week-range label and stage title in the same
> corner across all 8.

### A1 — `kp-origin-1-pronephros.png` · 4:3 · 1536×1152
**Topic:** Pronephros (Stage E1), weeks 3–4.
**Organ-level panel:** simplified lateral human embryo, cervical (neck) region highlighted in soft yellow.
**Magnified panel (dashed inset):** ~7 pairs of primitive **pronephric tubules** in the cervical intermediate mesoderm; the **Wolffian (mesonephric) duct** beginning to grow caudally as a scaffold. Callouts: "non-functional," "regresses by week 5," "duct = scaffold for later stages."
**Bottom flow:** Left (pale pink): primitive, transient. → Center: forms the Wolffian duct. → Right (pale blue): template for all later kidney stages.
Label the figure "E1 · Pronephros · Wk 3–4." White background, muted clinical palette, dashed connectors, `© williamriveromd.com`.

### A2 — `kp-origin-2-mesonephros.png` · 4:3 · 1536×1152
**Topic:** Mesonephros (Stage E2), weeks 4–8.
**Organ-level panel:** same embryo viewpoint as A1; thoracolumbar region now highlighted.
**Magnified panel (dashed inset):** **mesonephric tubules** with small glomerular capsules draining into the **Wolffian duct**; adjacent gonadal ridge. Callouts: "intermediate kidney," "transiently functional."
**Bottom flow:** Left: transient excretory organ. → Center: Wolffian duct persists. → Right (pale blue): in males → epididymis, vas deferens, seminal vesicles; caudal duct → ureteric bud.
Label "E2 · Mesonephros · Wk 4–8." Same scale/framing as A1.

### A3 — `kp-origin-3-ureteric-bud-induction.png` · 4:3 · 1536×1152
**Topic:** Ureteric bud induction (Stage E3), weeks 5–6.
**Organ-level panel:** caudal embryo; pelvic region highlighted.
**Magnified panel (dashed inset):** the **ureteric bud** sprouting from the lower Wolffian duct and meeting the **metanephric mesenchyme**; reciprocal signaling drawn as labeled arrows: **GDNF → RET** (mesenchyme → bud tip) and **WNT9b → MET** (bud → mesenchyme).
**Bottom flow:** Left (pale pink): failed induction → renal agenesis; ectopic bud → duplex/ectopic ureter (Weigert–Meyer). → Center: reciprocal induction. → Right (pale blue): the definitive (metanephric) kidney begins.
Label "E3 · Ureteric Bud Induction · Wk 5–6."

### A4 — `kp-origin-4-branching-morphogenesis.png` · 4:3 · 1536×1152
**Topic:** Branching morphogenesis (Stage E4), weeks 6–10.
**Organ-level panel:** early kidney silhouette.
**Magnified panel (dashed inset):** **~15 rounds of dichotomous branching** of the ureteric tree forming the collecting system: renal pelvis → major calyces → minor calyces → papillary ducts → collecting ducts; a nephron seeded at each branch tip.
**Bottom flow / KEY FACT BANNER (emphasize, soft-yellow highlight):** "Nephrogenesis stops at ~36 weeks — final endowment ≈ **700,000–1.8 million nephrons per kidney** — none added after birth."
Label "E4 · Branching Morphogenesis · Wk 6–10."

### A5 — `kp-origin-5-nephrogenesis-met.png` · 4:3 · 1536×1152
**Topic:** Nephrogenesis, MET sequence (Stage E5), weeks 7–36.
**Magnified panel (dashed inset), left→right morphological series:** cap mesenchyme → **renal vesicle** → **comma-shaped body** → **S-shaped body** (label: proximal limb → Bowman's capsule + glomerulus; distal limb → connecting tubule) → **capillary-loop stage** (podocyte differentiation, glomerular vascularization) → **mature nephron**.
**Bottom flow:** Left: mesenchymal-to-epithelial transition. → Center: transcription factors WT1, PAX2, SIX2. → Right (pale blue): a functioning filtering nephron.
Label "E5 · Nephrogenesis (MET) · Wk 7–36."

### A6 — `kp-origin-6-ascent-rotation.png` · 4:3 · 1536×1152
**Topic:** Renal ascent & rotation (Stage E6), weeks 6–9.
**Organ-level panel:** posterior abdominal wall with vertebral landmarks; kidney shown migrating from **sacral (S1)** to **lumbar (L1–L2)** position with a **90° medial rotation** (hilum becomes anteromedial); arrows showing arterial supply migrating **sacral → iliac → aortic**.
**Bottom flow (pale pink):** arrested ascent → pelvic kidney; midline fusion → horseshoe kidney.
Label "E6 · Ascent & Rotation · Wk 6–9."

### A7 — `kp-origin-7-fetal-kidney.png` · 4:3 · 1536×1152
**Topic:** Mature fetal kidney (Stage E7), week 10 → birth.
**Organ-level panel:** fetal kidney with **normal fetal lobulation**; small fetus-in-amniotic-sac vignette showing **fetal urine → amniotic fluid** cycle.
**Magnified callouts:** "after ~36 wk growth is hypertrophic, not hyperplastic (no new nephrons)."
**Bottom flow (pale pink):** severe oligohydramnios from absent fetal urine → **Potter sequence** (pulmonary hypoplasia, limb/facial deformation).
Label "E7 · Mature Fetal Kidney · Wk 10–Birth."

### A8 — `kp-origin-8-anomaly-map.png` · 4:3 · 1536×1152
**Topic:** CAKUT failure-point map (Stage E8) + protection hook.
**Layout:** a clean horizontal developmental timeline; each disruption mapped to its anomaly with dashed connectors and color-coded nodes (light gray-blue = normal, soft yellow = caution, red = anomaly): bud fails → **agenesis**; mesenchyme absent → **multicystic dysplastic kidney / dysplasia**; ectopic bud → **duplex/ectopic ureter**; reduced branching → **oligonephropathy (low nephron endowment)**; arrested ascent → **pelvic kidney**; fusion → **horseshoe kidney**.
**Bottom benefit/realization box (pale blue):** "Prematurity / low birth weight → fewer nephrons for life → each works harder (**Brenner hyperfiltration**) → higher lifelong risk of high blood pressure & CKD. You can't grow new nephrons — **protect the ones you were born with.**"
Label "E8 · Where Development Can Fail (CAKUT)."

---

## SECTION B — Function figures (7) · 4:3 · 1536×1152 (B1 may be 1:1)

### B1 — `kp-nephron-unit.png` · 1:1 · 1254×1254
**Topic:** The nephron as the kidney's functional unit.
**Organ-level panel:** small kidney cross-section with a dashed connector to the magnified unit.
**Magnified panel (dashed inset):** a single labeled **nephron** — afferent/efferent arterioles, **glomerulus**, **Bowman's capsule**, **proximal tubule**, **loop of Henle**, **distal tubule**, **collecting duct**.
**Bottom caption strip:** "One of ~2,000,000 — working in parallel, in real time."
White background, muted palette, `© williamriveromd.com`.

### B2 — `kp-filtration-barrier.png` · 4:3 · 1536×1152
**Topic:** Glomerular filtration barrier.
**Magnified panel (dashed inset):** the three layers — **fenestrated endothelium → glomerular basement membrane → podocyte foot processes with slit diaphragm**. Show what PASSES (water, salts, glucose, small wastes — soft yellow) vs what STAYS (cells, albumin — red "retained").
**Bottom flow:** Left: ~180 L filtered/day. → Center: size- and charge-selective barrier. → Right (pale blue): protein-free ultrafiltrate.
Label "Glomerular filtration · 180 L/day."

### B3 — `kp-reabsorption.png` · 4:3 · 1536×1152
**Topic:** Tubular reabsorption.
**Magnified panel (dashed inset):** nephron segments (PCT, loop of Henle, DCT, collecting duct) with labeled recovery of **water, glucose, amino acids, bicarbonate, sodium** (soft-yellow highlighted segments; blue protective arrows back to blood).
**Bottom banner:** "**99% reclaimed · 1% released.**"
Label "Tubular reabsorption."

### B4 — `kp-electrolyte-balance.png` · 4:3 · 1536×1152
**Topic:** The kidney as a chemistry thermostat (electrolyte & acid–base balance).
**Center panel:** clean dial/gauge motif, each held within a narrow safe band: **sodium, potassium, calcium, phosphate, magnesium, acid–base (pH)**.
**Bottom caption (pale blue):** "Blood pH held within **±0.04** — every minute of your life."
Label "Electrolyte & acid–base homeostasis."

### B5 — `kp-endocrine-signals.png` · 4:3 · 1536×1152
**Topic:** The kidney as an endocrine organ and oxygen sensor.
**Organ-level panel:** kidney with labeled signaling arrows radiating to target organs: **erythropoietin → bone marrow (red cells)**; **calcitriol (active vitamin D) → calcium into bone**; **renin → RAAS → blood-pressure cascade**.
**Magnified inset (dashed):** an **O₂-sensing cell** with the **HIF–PHD** pathway responding to low oxygen → EPO.
**Bottom flow:** Left: low O₂ / low volume / low calcium signals. → Center: kidney as sensor + gland. → Right (pale blue): red cells, blood pressure, bone health.
Label "Endocrine roles + oxygen sensing."

### B6 — `kp-klotho-longevity.png` · 4:3 · 1536×1152
**Topic:** Klotho–FGF23 longevity axis.
**Magnified panel (dashed inset):** **kidney tubular cells** producing **membrane-bound Klotho** (co-receptor for bone-derived **FGF23**) and **soluble Klotho** released to the blood. Labeled effects: FGF23–Klotho → **phosphate excretion ↓ calcitriol**; soluble Klotho → **vascular-protective, anti-fibrotic, anti-calcification, anti-aging** (blue protective arrows).
**Bottom flow:** Left (pale pink): CKD → ↓ Klotho → phosphate retention, vascular aging. → Center: Klotho–FGF23 axis. → Right (pale blue): healthier vessels, slower aging.
Label "Klotho · the longevity protein."

### B7 — `kp-homeostasis.png` · 4:3 · 1536×1152
**Topic:** Whole-body homeostasis web.
**Center panel:** a central pair of kidneys connected by clean labeled lines to **heart, bone, marrow, brain, lungs, gut, blood vessels**, conveying coordination across the whole body.
**Bottom caption:** "The quiet center of the body's balance."
Label "Homeostasis · the body's set-point."

---

## SECTION C — Centerpiece poster (1)

### C1 — `kp-20-responsibilities.png` · 4:3 · 1536×1152
**Topic:** "20 Responsibilities of Healthy Kidneys" reference poster.
**Layout:** a clean, calm, premium grid of **20 numbered cells** (01–20), each with a tiny line-icon + short label, in the muted clinical palette on white. Strong title at top, mobile-readable labels, generous whitespace.
**The 20 cells:** 1 Waste removal · 2 Drug & toxin clearance · 3 Water balance · 4 Sodium · 5 Potassium · 6 Calcium & phosphate · 7 Magnesium · 8 Acid–base · 9 Blood pressure · 10 Erythropoietin · 11 Renin · 12 Vitamin D activation · 13 Klotho / longevity · 14 Bone protection · 15 Urine concentration · 16 Gluconeogenesis · 17 Immune support · 18 Oxygen sensing · 19 Cardiovascular protection · 20 Homeostasis.
Title "20 Responsibilities of Healthy Kidneys." `© williamriveromd.com` bottom-right.

---

## Generation checklist

- [ ] A1–A8 generated at **identical 4:3 framing/scale** (scroll morph depends on it)
- [ ] B1–B7 generated
- [ ] C1 generated
- [ ] All on **white** backgrounds, muted clinical palette, dashed insets
- [ ] Every figure carries `© williamriveromd.com` (bottom-right)
- [ ] Files saved to `images/` with the exact filenames above (`.png`)
- [ ] Keep existing `images/kidney-physiology-og.png` unchanged
