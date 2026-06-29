# Biomedical Mechanism Figure — Prompt Pack (Tier 3: Atlas Gaps + NSAID restyle)

Generated with the **`williamriveromd-biomedical-mechanism-figure`** skill.

Six publication-grade review-article mechanism schematics that fill the remaining
gaps in the nephrology visual atlas (`guides/nephrology-atlas.html`) plus one
restyle. Same house style as `biomedical-mechanism-figures.md`:
**organ-level panel → magnified functional-unit inset (dashed) → bottom
injury → intervention → benefit flow.**

**Shared style (applies to every prompt below):**
Flat vector illustration with soft semi-3D shading, white background, generous
whitespace, clean sans-serif labels, thin dashed connector lines separating
magnified panels. Muted clinical palette — light gray-blue anatomy, soft yellow
for highlighted/affected segments, red for arteries/injury/ROS/immune deposits,
blue for veins/protective/therapeutic effects, pale pink pathology summary box,
pale blue benefit summary box. No photorealism, no shadows, no dark background,
no cartoonish styling, no excessive icons, no gibberish text. 16:9 aspect ratio,
labels readable at slide-viewing size. Always flag non-standard/experimental
therapies as "proposed / experimental." **Every figure carries small
semi-transparent navy text "© williamriveromd.com" in the bottom-right corner,
not obscuring the figure.**

**Atlas wiring (after generation):** each new figure becomes a `Mechanism`-render
item. Suggested atlas placement and next ids (current highest: c24 / al12):
| Figure | Atlas section | Suggested id |
|---|---|---|
| Lupus nephritis | Glomerular disease | c25 |
| FSGS | Glomerular disease | c26 |
| Membranous nephropathy | Glomerular disease | c27 |
| Sepsis-associated AKI | Acute kidney injury | c28 |
| RAAS pathway | Renal physiology (`a` prefix) | a23 |
| NSAID AKI (restyle) | replaces existing **c23** image | — |

---

## 1. Lupus Nephritis
**Atlas:** Glomerular disease · **Guide:** `guides/lupus-nephritis.html`
**Suggested file:** `lupus-nephritis-mechanism.png`
*(Note: a `lupus-nephritis-immune-cascade.png` already exists in the guide — this
new figure is the atlas-style review-article mechanism; keep both or supersede.)*

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for immune
complexes/injury, blue for therapy, pale pink pathology box, pale blue benefit
box. No photorealism, no dark background, no clutter. 16:9. Bottom-right corner:
small semi-transparent navy "© williamriveromd.com", not obscuring the figure.

TOPIC: How systemic lupus erythematosus injures the kidney (lupus nephritis).
DISEASE CONTEXT: Lupus nephritis (ISN/RPS classes).
CENTRAL MECHANISM: Anti-dsDNA and other autoantibodies form immune complexes
that deposit in the glomerulus and activate complement, causing immune-mediated
glomerular injury.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "Lupus nephritis."
Dashed connector to the magnified glomerulus.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single glomerulus with mesangium, subendothelial and subepithelial spaces.
Highlight affected regions pale yellow with red immune-complex deposits. Callouts:
  • "Anti-dsDNA / nucleosome autoantibodies → circulating immune complexes"
  • "Mesangial + subendothelial deposits (wire-loop lesions)"
  • "Complement activation (↓C3, ↓C4, C1q) → inflammation"
  • "Endocapillary proliferation / crescents → haematuria + proteinuria"
Small note: "ISN/RPS Class I–VI determines treatment & prognosis."

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): Autoantibody immune complexes · complement
    activation · proliferative glomerular injury · **Nephritic/nephrotic injury, CKD**
  Intervention box (center): Hydroxychloroquine backbone · induction
    immunosuppression (MMF or low-dose cyclophosphamide + steroids) · add-on
    belimumab or voclosporin · RAAS blockade
  Benefit box (pale blue): Complete renal response · ↓proteinuria · preserved
    eGFR · fewer flares
```

---

## 2. Focal Segmental Glomerulosclerosis (FSGS)
**Atlas:** Glomerular disease · **Guide:** `guides/glomerulonephritis.html` (general)
**Suggested file:** `fsgs-mechanism.png`

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for injury, blue
for therapy, pale pink pathology box, pale blue benefit box. No photorealism, no
dark background, no clutter. 16:9. Bottom-right corner: small semi-transparent
navy "© williamriveromd.com", not obscuring the figure.

TOPIC: How podocyte injury causes focal segmental glomerulosclerosis.
DISEASE CONTEXT: FSGS (primary, genetic/APOL1, and secondary/adaptive).
CENTRAL MECHANISM: Podocyte depletion and foot-process effacement lead to
segmental scarring of the glomerular tuft and nephrotic-range proteinuria.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "FSGS." Dashed
connector to the magnified glomerulus.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single glomerulus with podocytes lining the capillary loops; show one segment
sclerosed (highlighted pale yellow), the rest preserved. Callouts:
  • "Podocyte injury — circulating permeability factor / genetic / APOL1 /
    adaptive hyperfiltration"
  • "Foot-process effacement → loss of slit diaphragm → heavy proteinuria"
  • "Podocyte detachment/depletion (cannot regenerate)"
  • "Segmental sclerosis + hyalinosis → progressive glomerular scarring"

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): Podocyte depletion · foot-process effacement ·
    segmental sclerosis · **Nephrotic proteinuria → CKD/ESKD**
  Intervention box (center): Identify cause (primary vs secondary/genetic) ·
    immunosuppression (corticosteroids ± calcineurin inhibitors) for primary ·
    RAAS blockade + SGLT2 inhibitors · treat secondary drivers
  Benefit box (pale blue): ↓proteinuria · partial/complete remission ·
    slower eGFR decline
```

---

## 3. Membranous Nephropathy
**Atlas:** Glomerular disease · **Guide:** `guides/glomerulonephritis.html` (general)
**Suggested file:** `membranous-nephropathy-mechanism.png`

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for immune
deposits/injury, blue for therapy, pale pink pathology box, pale blue benefit
box. No photorealism, no dark background, no clutter. 16:9. Bottom-right corner:
small semi-transparent navy "© williamriveromd.com", not obscuring the figure.

TOPIC: How membranous nephropathy causes nephrotic syndrome.
DISEASE CONTEXT: Primary (anti-PLA2R / anti-THSD7A) membranous nephropathy.
CENTRAL MECHANISM: Autoantibodies against podocyte antigens form subepithelial
immune deposits that activate complement and injure the filtration barrier.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "Membranous
nephropathy." Dashed connector to a magnified glomerular capillary loop.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A single glomerular capillary loop cross-section: endothelium, GBM, podocyte.
Show subepithelial immune deposits (red) with "spike-and-dome" GBM reaction
(highlighted pale yellow). Callouts:
  • "Anti-PLA2R / anti-THSD7A IgG4 binds podocyte antigen"
  • "Subepithelial immune-complex deposits"
  • "Complement (C5b-9 / MAC) → podocyte injury"
  • "GBM 'spikes' (basement-membrane reaction) → heavy proteinuria"
Small note: "Serum anti-PLA2R titre tracks disease activity."

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): Anti-PLA2R IgG4 · subepithelial deposits · C5b-9
    podocyte injury · **Nephrotic syndrome**
  Intervention box (center): Supportive (RAAS blockade, diuretics,
    anticoagulation if high VTE risk) · immunosuppression for high risk —
    rituximab (anti-CD20), or cyclophosphamide + steroids, or CNI
  Benefit box (pale blue): Immunologic remission (falling anti-PLA2R) →
    ↓proteinuria · preserved eGFR · lower thrombosis risk
```

---

## 4. Sepsis-Associated Acute Kidney Injury
**Atlas:** Acute kidney injury · **Guide:** general (no dedicated guide)
**Suggested file:** `sepsis-aki-mechanism.png`

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for
injury/inflammation, blue for therapy, pale pink pathology box, pale blue
benefit box. No photorealism, no dark background, no clutter. 16:9. Bottom-right
corner: small semi-transparent navy "© williamriveromd.com", not obscuring the
figure.

TOPIC: How sepsis injures the kidney (sepsis-associated AKI).
DISEASE CONTEXT: Sepsis-associated AKI (SA-AKI) — the commonest AKI in the ICU.
CENTRAL MECHANISM: Inflammation, microcirculatory dysfunction, and tubular
metabolic reprogramming — not simply low blood pressure — drive injury.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "Sepsis-associated
AKI." Small systemic cue (bloodstream with bacteria/PAMPs). Dashed connector to
a magnified peritubular capillary + tubule unit.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
Peritubular capillary adjacent to a proximal tubule, both highlighted pale
yellow. Callouts:
  • "PAMPs/DAMPs + cytokines (TNF-α, IL-6) → endothelial activation"
  • "Glycocalyx shedding + microthrombi → microcirculatory dysfunction"
  • "Peritubular hypoperfusion + mitochondrial stress → tubular cell-cycle
    arrest (adaptive), not widespread necrosis"
  • "↓GFR with relatively preserved histology"

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): Inflammation · microvascular dysfunction +
    microthrombi · tubular metabolic reprogramming · **Sepsis-associated AKI**
  Intervention box (center): Early source control + antibiotics · balanced
    fluid resuscitation (avoid overload) · vasopressors to MAP target · avoid
    nephrotoxins · KRT for refractory complications
  Benefit box (pale blue): Restored perfusion · tubular recovery · ↓progression
    to CKD
```

---

## 5. RAAS Pathway in Kidney Disease
**Atlas:** Renal physiology (`a` prefix) · **Guide:** general physiology
**Suggested file:** `raas-pathway-mechanism.png`

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for
constriction/injury, blue for protective/therapeutic effects, pale pink
pathology box, pale blue benefit box. No photorealism, no dark background, no
clutter. 16:9. Bottom-right corner: small semi-transparent navy
"© williamriveromd.com", not obscuring the figure.

TOPIC: The renin–angiotensin–aldosterone system and why blocking it protects
the kidney.
DISEASE CONTEXT: RAAS activation in CKD / proteinuric kidney disease.
CENTRAL MECHANISM: Angiotensin II raises intraglomerular pressure and drives
fibrosis; ACEi/ARB (and MRA) blockade lowers pressure and is nephroprotective.

ORGAN-LEVEL PANEL (left):
Simplified kidney with a magnified juxtaglomerular apparatus inset (afferent
arteriole granular cells + macula densa), labeled "↓Perfusion / ↓NaCl → renin
release." Dashed connector to the cascade panel.

MAGNIFIED MECHANISM PANEL (center, dashed border):
Vertical cascade: "Renin → Angiotensinogen → Angiotensin I → (ACE) →
Angiotensin II → Aldosterone." Show a single glomerulus with the EFFERENT
arteriole constricted (red, highlighted pale yellow). Callouts:
  • "Ang II: efferent constriction → ↑intraglomerular pressure"
  • "Aldosterone: Na+/water retention → ↑BP"
  • "Ang II + aldosterone: inflammation & fibrosis (TGF-β)"

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): ↑Angiotensin II · efferent constriction ·
    ↑intraglomerular pressure · **Proteinuria + fibrosis**
  Intervention box (center): ACE inhibitor / ARB (block Ang II) · MRA /
    finerenone (block aldosterone) · often + SGLT2 inhibitor
  Benefit box (pale blue): Efferent dilation → ↓intraglomerular pressure ·
    ↓proteinuria · anti-fibrotic · slower eGFR decline
  Caution note (small, amber): "Expect a small early creatinine rise; monitor
    K⁺ — avoid dual ACEi+ARB."
```

---

## 6. NSAID-Induced AKI — RESTYLE (replace existing dark infographic)
**Atlas:** Acute kidney injury (already item **c23**, currently `Hybrid`)
**Guide:** `guides/nsaid-kidney-injury.html`
**Suggested file:** `nsaid-kidney-mechanisms.png` (**overwrite** — keeps the atlas
+ guide references; after replacing, flip atlas item c23 from `render:'Hybrid'`
to `render:'Mechanism'`).

```
Create a publication-grade biomedical mechanism schematic, scientific
review-article style. Flat vector, soft semi-3D shading, white background, clean
sans-serif labels, thin dashed connectors, generous whitespace. Muted clinical
palette: light gray-blue anatomy, soft yellow highlights, red for
constriction/injury, blue for therapy, pale pink pathology box, pale blue
benefit box. No photorealism, no dark background, no clutter. 16:9. Bottom-right
corner: small semi-transparent navy "© williamriveromd.com", not obscuring the
figure.

TOPIC: How NSAIDs damage the kidney.
DISEASE CONTEXT: NSAID-induced acute kidney injury.
CENTRAL MECHANISM: NSAIDs block COX-derived prostaglandins, removing the
afferent vasodilation the kidney relies on under stress, and can directly injure
tubules and the interstitium.

ORGAN-LEVEL PANEL (left):
Simplified kidney cross-section, light gray-blue, labeled "NSAID-induced AKI."
Dashed connector to a magnified glomerulus + tubule unit.

MAGNIFIED MECHANISM PANEL (center/right, dashed border):
A glomerulus with the AFFERENT arteriole constricted (red, highlighted pale
yellow) plus an adjacent tubule/interstitium. Callouts:
  • "NSAID → ↓COX-1/2 prostaglandins (PGE₂, PGI₂)"
  • "Loss of afferent vasodilation → ↓renal perfusion → ↓GFR (haemodynamic)"
  • "Direct tubular toxicity / acute interstitial nephritis (AIN)"
  • "Papillary necrosis (chronic/high-dose)"
Small note (amber): "Triple whammy: NSAID + ACEi/ARB + diuretic."

BOTTOM SUMMARY FLOW (left → center → right, arrows):
  Pathology box (pale pink): ↓Prostaglandins · afferent constriction ·
    tubulointerstitial injury · **Acute kidney injury**
  Intervention box (center): Stop the NSAID · restore volume · avoid in CKD,
    volume depletion, and the triple whammy · use safer analgesics
  Benefit box (pale blue): Restored afferent flow · recovered GFR · prevention
    in at-risk patients
```

---

### Post-generation checklist
1. Generate each prompt in the ChatGPT Image Generator (GPT-image / GPT-4o).
2. Save `<name>.png` to `images/`; generate matching `.webp` (Pillow q82) — see
   `build` note in `biomedical-mechanism-figures.md`.
3. Add each to `guides/nephrology-atlas.html` as a new item with
   `render:'Mechanism'` in the section above; bump the matching stat-pill count
   (Pathology for c-items, Anatomy for the RAAS `a`-item) and re-run the
   `node --check` validation on the TABS script.
4. For the NSAID restyle: overwrite `nsaid-kidney-mechanisms.png/.webp`, then
   change atlas item **c23** `render:'Hybrid'` → `render:'Mechanism'`.
5. Wire the disease figures into their guides where a guide exists
   (lupus-nephritis, glomerulonephritis, nsaid-kidney-injury) as
   `<figure class="illus-panel">` with WebP+PNG and a 4-language `<figcaption>`.
