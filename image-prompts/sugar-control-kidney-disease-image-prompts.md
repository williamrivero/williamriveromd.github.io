# Image Plan — `sugar-control-kidney-disease.html`
### "Blood Sugar and Your Kidneys: Breaking the Glycemic-Renal Cycle"

Stage-1 prompt pack for the **ChatGPT Image Generator GPT**
(<https://chatgpt.com/g/g-pmuQfob8d-image-generator>). Every prompt below is
copy-paste ready. Generated with the renalcarematters.com graphic skills
(hero-vignette v3, simple-figure, biomedical-mechanism-figure, algorithm-generator,
infographic v5).

---

## 1 · Blueprint overview

| # | Asset | File base | Skill used | Placement in guide | Size | Wiring |
|---|-------|-----------|-----------|--------------------|------|--------|
| 1 | Circular hero (metaphor) | `sugar-control-kidney-disease-vignette-hero` | hero-vignette v3 (Scaffold C anatomy) | Hero disc (patient hero) | 2048×2048 | ✅ referenced |
| 2 | Syrup-in-the-filter comparison | `sugar-control-kidney-disease-01-syrup-filter` | simple-figure (Scaffold B) | Patient §"Why Sugar Matters" | 1792×1024 | ✅ referenced |
| 3 | Glycemic-renal-CV cascade | `sugar-control-kidney-disease-02-cascade` | biomedical-mechanism-figure | Clinician §Pathophysiology | 1792×1024 | ✅ referenced |
| 4 | eGFR-stratified Rx decision tree | `sugar-control-kidney-disease-03-pharmacotherapy-tree` | algorithm-generator (Mode C) | Clinician §Pharmacotherapy | 1024×1536 | ✅ wired |
| 5 | HbA1c reliability by CKD stage | `sugar-control-kidney-disease-04-hba1c-reliability` | simple-figure (Scaffold E) | Clinician §Diagnostic Nuance | 1448×1086 | ✅ wired |
| 6 | OG / social share card | `sugar-control-kidney-disease-og` | infographic v5 (Archetype 1) | `og:image` / `twitter:image` | 1200×630 | ✅ referenced |

**Blueprint coverage (Section 7):** cascade diagram → #3; eGFR pharmacotherapy
decision tree → #4; patient "syrup in the filter" analogy → #2; HbA1c
reliability-by-stage chart → #5. Hero (#1) and OG card (#6) round out the set.

**Wiring note.** All six assets are now live in the guide: #1/#2/#3/#6 were
already referenced, and #4/#5 were wired into the clinician Pharmacotherapy and
Diagnostic-Nuance sections (with `fig-desc` + `fig-abbrevs` for the lightbox).
Delivered files are PNG at native resolution plus WebP twins; the OG card was
normalized to its declared 1200×630.

## 2 · Production checklist (every asset)

1. Paste the `PROMPT` block into the Image Generator GPT; render at the stated
   **PIXEL DIMENSIONS**.
2. Save the PNG as `images/<file-base>.png`.
3. Make a **WebP twin**: `cwebp -q 82 images/<file-base>.png -o images/<file-base>.webp`
   (the guide's `<picture>` blocks load the `.webp` with a `.png` fallback).
4. The OG card (#6) is **exactly 1200×630** — the `<head>` already declares
   `og:image:width=1200` / `og:image:height=630`.
5. After dropping the files in, run `python3 patch_hero_fetchpriority.py --guide
   sugar-control-kidney-disease.html` (already done, idempotent) so the hero ships
   `fetchpriority="high"`.
6. All in-body figures already carry a plain-language `figcaption` — the image
   lightbox reads it, so the rendered art needs **no baked caption**.

---

## 3 · Prompts

### IMAGE 1 — Circular vignette hero

```
FILE NAME: sugar-control-kidney-disease-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C (calm 3D anatomy)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F — Anatomy
CAMERA: three-quarter cross-section, gentle studio lighting
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: the "syrup in the filter" metaphor at a glance — a translucent kidney whose delicate filter is being coated and thickened by a warm amber glucose sheen.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: F Anatomy. Camera: three-quarter cross-section, macro, soft studio lighting.

Subject: a single clean render of one human kidney gently sectioned to reveal a translucent glomerulus and a few nephron tubules, floating on a soft teal-tinted off-white background. A warm amber–gold, honey-like translucent sheen ("syrup") clings to and thickens the fine filtering membrane of the glomerulus, contrasting with the healthy clear filtrate — a quiet visual metaphor for high blood sugar clogging the kidney's filter. Restrained clinical colour: renal reds and soft pink tissue, translucent teal accents, warm amber glucose sheen; anatomically accurate, calm, premium-medical-textbook feel, not garish.

Visual hierarchy: the kidney + glomerulus occupies 60–70% of the circle; 2–3 supporting cues (a couple of tiny suspended glucose particles, a faint clear-vs-thickened filtrate contrast) 20–30%; reserve a 20–25% TITLE SAFE ZONE in the upper-left as empty soft gradient background (no anatomy, particles, leader lines, or callouts in that zone) so the HTML title can sit beside the disc. Soft edge falloff toward a slightly deeper neutral at the rim.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders, no dark/charcoal/black background.

NEGATIVE INSTRUCTIONS:
Avoid: busy layouts; collage overload; more than four supporting scenes; dozens of icons; tiny unreadable labels; infographic clutter; duplicated people; repeated compositions; cropped circle; cropped objects; cropped anatomy; edge clipping; objects touching the circular border; important content inside the title safe zone; baked-in text, titles, captions, logos, watermarks; rectangular borders, frames, banners; dark / charcoal / black backgrounds; cartoon style, neon, HDR, over-saturation; distorted or implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant hero subject (the kidney/glomerulus) at 60–70%, 2–3 supporting cues, a clean 20–25% upper-left title-safe zone. Wordless. Light teal-tinted background, restrained clinical palette. Crops cleanly inside the circle with nothing lost at the edges.
```

---

### IMAGE 2 — Syrup-in-the-filter comparison (patient)

```
FILE NAME: sugar-control-kidney-disease-01-syrup-filter.png
IMAGE TYPE: Simple figure — Scaffold B (side-by-side comparison)
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients
VISUAL GOAL: contrast a healthy kidney filter passing clear fluid against a sugar-coated, stiffened filter leaking protein — the earliest painless sign of diabetic kidney damage.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, on a white (#ffffff) background. Clean sans-serif typography in Inter throughout. Title centered at top in bold navy (#0f1e2e): "Syrup in the Filter". A soft dashed vertical divider splits the canvas into two equal panels with rounded corners.

LEFT panel labeled in renal green (#1f7a4d): "Healthy filter". Show a simplified semi-3D kidney glomerular filter (a looped capillary tuft with a clean membrane) passing CLEAR fluid downward into a tubule; small blue droplets of clear filtrate flow through smoothly; the retained protein (a few larger amber-gold spheres labeled "protein / albumin") stays inside the blood side. A short caption line in navy: "Clear fluid passes · protein stays in".

RIGHT panel labeled in clinical red (#b91c1c): "Sugar-coated filter (years of high sugar)". Show the same filter now coated and stiffened by a warm amber–gold, honey-like glaze; the membrane looks thickened and sticky; a few amber protein spheres now LEAK through the coated membrane into the tubule/urine below. A short caption in navy: "Sugar stiffens the filter · protein (albumin) leaks into the urine".

Bottom full-width soft gray (#f3f4f6) strip with a single navy takeaway line: "A simple urine test (UACR — urine albumin-to-creatinine ratio) catches this leak years before you feel anything." Include a small caption note: "CKD = chronic kidney disease".

Rounded panel corners, ample negative space, mobile-readable labels ≥11pt. Bottom-right: "renalcarematters.com" in small semi-transparent navy text (~70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative typefaces. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable, clinically plausible, calm, publication-grade. White background. Two panels only (green healthy vs red sugar-coated). The single clear idea — clear fluid vs leaking protein — must read in under 10 seconds. renalcarematters.com visible bottom-right.
```

---

### IMAGE 3 — Glycemic-renal-cardiovascular cascade (clinician)

```
FILE NAME: sugar-control-kidney-disease-02-cascade.png
IMAGE TYPE: Biomedical mechanism figure — review-article schematic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: distinguish the hemodynamic from the glucotoxic path from hyperglycemia to diabetic kidney injury, and end on the injury → intervention → benefit flow.

PROMPT:
Create a publication-grade biomedical mechanism schematic in a scientific review-article style (flat vector illustration with soft semi-3D shading, white background, thin dashed connector boxes, minimal clutter, muted clinical palette). Clean sans-serif labels in Inter (never a serif font). Title top-left in bold navy: "The Glycemic–Renal–Cardiovascular Cascade".

ORGAN-LEVEL PANEL (left): a simplified light gray-blue kidney with major vessels, labeled "Diabetic kidney disease". A thin dashed connector box points from the kidney cortex to the magnified panel.

MAGNIFIED FUNCTIONAL-UNIT PANEL (center, inside a dashed border): a glomerulus + single nephron schematic. Highlight the afferent arteriole and glomerular tuft in pale yellow. Two clearly separated mechanism tracks:
  • HEMODYNAMIC track (red arrows): "Hyperglycemia" → "SGLT2-mediated Na⁺–glucose reabsorption (proximal tubule)" → "↓ distal Na⁺ to macula densa" → "blunted tubuloglomerular feedback (TGF)" → "afferent vasodilation → glomerular HYPERFILTRATION" → "↑ intraglomerular pressure" → "albuminuria".
  • GLUCOTOXIC track (muted amber arrows): "AGE cross-linking" + "RAAS activation (↑ proximal angiotensinogen; efferent constriction)" → "mesangial expansion, GBM thickening, tubulointerstitial fibrosis".
  Small side note in soft gray: both tracks "converge with the lipid / cardiovascular axis on endothelial dysfunction".

BOTTOM SUMMARY FLOW (three boxes, left→right arrows):
  • LEFT pale-pink pathology box "INJURY": hyperfiltration · intraglomerular hypertension · AGE/RAAS-driven fibrosis · endothelial dysfunction.
  • CENTER box "INTERVENTION": SGLT2 inhibitor (restores TGF, lowers intraglomerular pressure) · RAAS inhibitor · GLP-1 receptor agonist · finerenone (nsMRA) · statin.
  • RIGHT pale-blue benefit box "BENEFIT": slowed eGFR decline · reduced albuminuria · cardiovascular protection.

Muted clinical colours: light gray-blue anatomy, pale yellow highlighted segments, red for the hemodynamic/injury arrows, blue for protective/therapeutic effects, pale pink pathology box, pale blue benefit box. Generous whitespace, legible at slide-viewing size, no photorealism, no dark background, no decorative icons.

Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No gibberish text, no excessive icons, no dark theme, no photorealism, no cartoon styling, no overcrowding, no invented numeric thresholds. Use only the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — never serif. Keep the © renalcarematters.com attribution.

QUALITY CHECK:
Reads as an NEJM/AJKD review figure. Hemodynamic and glucotoxic tracks visibly separated. Bottom injury → intervention → benefit flow present and correctly ordered. Anatomy plausible, labels medically precise, white background, mobile/slide-readable, attribution bottom-right.
```

---

### IMAGE 4 — eGFR-stratified pharmacotherapy decision tree (clinician)

```
FILE NAME: sugar-control-kidney-disease-03-pharmacotherapy-tree.png
IMAGE TYPE: Clinical algorithm — algorithm-generator Style Mode C (renalcarematters.com house style)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: a clean top-down decision tree for glycemic pharmacotherapy in T2DM + CKD, stratified by eGFR and anchored to KDIGO 2022/2024 and ADA 2026.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. White / very light off-white background, restrained navy and teal typography set in Inter (never a serif font), thin teal connector arrows, generous margins, centered symmetrical top-to-bottom layout, suitable for a clinician-facing nephrology guide. Rounded rectangles for actions/endpoints, diamonds for decision points.

Colour conventions: navy #0f1e2e for title, structural text, and body; teal #1a6b72 for decision nodes and connector accents; green #1f7a4d for recommended/foundation actions and endpoints; amber #b8860b for caution nodes; soft gray for side-note "pearl" boxes; clinical red #b91c1c reserved for the euglycemic-DKA safety pearl.

Title (navy): "Glycemic Pharmacotherapy in T2DM + CKD". Subtitle (teal): "eGFR-stratified · KDIGO 2022/2024 · ADA 2026".

Content to render (top → bottom):
1. START node (teal): "Confirmed type 2 diabetes with CKD (albuminuria and/or reduced eGFR; stage with the KDIGO G×A heat map)."
2. FOUNDATION node (green): "Metformin — full dose if eGFR ≥45 · reduce if eGFR 30–45 · individualize risk–benefit if <30 (not a hard stop)."
3. PARALLEL foundation node (green): "Add an SGLT2 inhibitor for renal/CV protection — IRRESPECTIVE of A1C. Initiate down to eGFR ~20 and continue below."
4. DECISION diamond (teal): "A1C above the individualized target? (KDIGO 2022: 6.5–8.0%, not a default)."
   → YES branch (green action): "Add a GLP-1 receptor agonist (usable across the eGFR range; watch GI tolerance)."
   → NO branch (soft gray): "Maintain protective regimen; do not intensify glucose lowering for its own sake."
5. DECISION diamond (teal): "Residual albuminuria on RAAS inhibitor + SGLT2i?"
   → YES (green): "Add finerenone (nsMRA) — monitor serum K⁺."
6. DECISION diamond (teal): "Advancing CKD / insulin deficiency?"
   → YES (green): "Insulin — proactively DOWN-titrate as eGFR falls (clearance declines)."
7. CAUTION node (amber, off to the side): "Deprioritize sulfonylureas — high hypoglycemia risk in CKD."

Two boxed 'pearl' side-notes:
  • Red pearl box: "Euglycemic DKA — a NORMAL glucose does not exclude DKA on an SGLT2 inhibitor. HOLD the SGLT2i on sick days and peri-operatively."
  • Soft-gray pearl box: "HbA1c unreliable in G4–G5/dialysis — trust CGM-derived time-in-range / GMI."

Make it publication-grade and vector-like: crisp typography, aligned nodes, consistent arrow lengths, balanced branches, generous margins, legible at full and thumbnail size. No dark background, no clutter, no photorealistic people, no cartoon styling. Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No dark/navy/charcoal/black background; no spaghetti arrows; no clutter; no cartoon or decorative styling; no invented drug doses or numeric thresholds beyond those stated. Use only Inter, Nunito Sans, IBM Plex Sans, or Manrope — never serif. Keep the © renalcarematters.com footer.

QUALITY CHECK:
Clear top-to-bottom clinical logic, decision diamonds visually distinct from action rectangles, foundation therapy (metformin + SGLT2i) reads as parallel and A1C-independent, the two safety pearls stand out, portrait 1024×1536, attribution bottom-right.
```

---

### IMAGE 5 — HbA1c reliability by CKD stage (clinician)

```
FILE NAME: sugar-control-kidney-disease-04-hba1c-reliability.png
IMAGE TYPE: Simple figure — Scaffold E (reference / quick-look card)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: at-a-glance guide to when HbA1c can be trusted across CKD stages and what to use instead in advanced CKD/dialysis.

PROMPT:
Clinical reference card, publication-grade nephrology design, on a white (#ffffff) background. Clean sans-serif typography in Inter. Bold navy (#0f1e2e) title at top: "How Reliable Is HbA1c Across CKD Stages?" Small teal subtitle: "And what to trust when it fails".

A compact, well-organized 4-column table. Column headers in teal (#1a6b72) on a soft gray (#f3f4f6) background: "CKD stage" · "HbA1c reliability" · "Why" · "What to trust". Alternating row fills (white / very soft gray). Use a small colored status chip in the reliability column (green = reliable, amber = caution, red = unreliable).

Rows:
1. "G1–G2 (eGFR ≥60)" · GREEN "Reliable" · "Normal red-cell survival" · "HbA1c every 3–6 months".
2. "G3a–G3b (eGFR 30–59)" · AMBER "Mostly reliable" · "Early anemia/iron effects begin" · "HbA1c + trend; corroborate if anemic".
3. "G4–G5 non-dialysis (eGFR <30)" · RED "Unreliable — biased LOW" · "Shortened RBC lifespan, iron therapy, ESA use, uremic carbamylation" · "CGM time-in-range (TIR) / GMI; structured SMBG".
4. "Dialysis (G5D)" · RED "Unreliable — biased LOW" · "RBC turnover + intradialytic glucose/insulin shifts" · "CGM (TIR/GMI); interpret a 'good' HbA1c as possibly falsely low".

Footer takeaway line in navy: "In advanced CKD a reassuring HbA1c can HIDE true hyperglycemia — do not titrate to HbA1c alone." Small caption note: "ESA = erythropoiesis-stimulating agent · CGM = continuous glucose monitor · GMI = glucose management indicator · TIR = time in range · SMBG = self-monitored blood glucose".

Mobile-readable, not cluttered, generous whitespace. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic content, overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Reads as a clean clinician quick-look card. Reliability trend green → amber → red → red is obvious. The "biased LOW in advanced CKD" message is unmistakable. White background, 4:3, attribution bottom-right.
```

---

### IMAGE 6 — OG / social share card

```
FILE NAME: sugar-control-kidney-disease-og.png
IMAGE TYPE: Infographic v5 — Archetype 1 (editorial share card)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630  (fixed — never change for an OG card)
AUDIENCE: mixed (social share)
VISUAL GOAL: a premium, calm share card that states the title and the syrup-in-the-filter promise, brand-consistent with renalcarematters.com.

PROMPT:
Premium editorial social share card (Open Graph) for a nephrology education guide, 1200×630, on a clean off-white (#fafafa) background with a subtle light teal-tinted (#eef6f7) panel. Clean sans-serif typography in Inter. Calm, publication-grade, uncluttered, mobile-thumbnail-legible.

LEFT two-thirds — text block, left-aligned:
  • A small teal (#1a6b72) eyebrow label: "RENALCAREMATTERS.COM · NEPHROLOGY GUIDE".
  • Large bold navy (#0f1e2e) title on two lines: "Blood Sugar & Your Kidneys".
  • Amber-gold (#b8860b) italic-weight subtitle: "Breaking the Glycemic-Renal Cycle".
  • A short navy supporting line: "Individualized targets · Filipino food · medicines that protect both".

RIGHT third — a single clean semi-3D vignette: a translucent human kidney with a warm amber–gold honey/"syrup" droplet descending toward and coating its glomerular filter, on the soft teal-tinted panel; a couple of small glucose particles suspended nearby. Restrained clinical palette (renal reds, teal accents, warm amber), gentle soft shadow, no clutter.

Strong visual hierarchy, generous negative space, everything readable as a small thumbnail. Bottom-right: "renalcarematters.com" in small semi-transparent navy text (~70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, generic stock-photo look, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative typefaces. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Title and subtitle legible at Facebook/X/LinkedIn thumbnail size. Light background, teal/navy/amber palette, one clean kidney+syrup vignette on the right, calm and premium. Attribution bottom-right.
```

---

## 4 · After rendering

All six assets are live (PNG + WebP twins in `images/`, OG normalized to
1200×630, figures #4/#5 wired). Dimension attributes were updated to the real
files, and the APA + acronym audits still pass at N/N. To regenerate any asset,
re-render its prompt above and drop the file into `images/` (remake the WebP twin
with `cwebp -q 82` or Pillow).
