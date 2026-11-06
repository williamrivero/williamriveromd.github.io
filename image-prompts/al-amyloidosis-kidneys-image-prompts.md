# AL Amyloidosis and Your Kidneys — image prompt pack

Guide: `guides/al-amyloidosis-kidneys.html` · Attribution: `© renalcarematters.com` (public atlas set) · American English in every label.

## Asset status

| ID | File (images/) | Size | Status | Source |
|---|---|---|---|---|
| 001 | `al-amyloidosis-kidneys-vignette-hero.{png,webp}` | 2048 × 2048 | **Interim** code-native illustration shipped; replace with the generated raster below | `al-amyloidosis-kidneys-svg/…-vignette-hero.svg` |
| 002 | `…-02-three-parts.{png,webp}` | 1792 × 1024 | Final, code-native (primary teaching graphic) | SVG in `al-amyloidosis-kidneys-svg/` |
| 003 | `…-03-diagnosis-typing.{png,webp}` | 1792 × 1024 | Final, code-native | SVG |
| 004 | `…-04-follow-up-domains.{png,webp}` | 1792 × 1024 | Final, code-native | SVG |
| 005 | `…-05-discordant-pathway.{png,webp}` | 1024 × 1536 | Final, code-native | SVG |
| 006 | `…-og.{png,webp}` + `…-rg-thumb.webp` | 1200 × 630 | Final, code-native | SVG |
| — | Cohort bar chart | responsive SVG | Drawn in-page from the static table | `assets/al-amyloidosis-evidence-data.json` |

Labeled diagrams (002–006) are deliberately code-native: labels stay editable and translatable, and no
generated image can misstate a clinical detail. The cohort chart is never a raster and never copies the
journal figure. No asset depicts histology; do not generate a "biopsy photograph".

To regenerate the code-native set: `python3 image-prompts/al-amyloidosis-kidneys-svg/make_figs.py .` from the repo root, which writes
SVG sources here and PNG masters + WebP twins into `images/`.

---

## 001 — Circular vignette hero (replace the interim illustration)

```
FILE NAME: al-amyloidosis-kidneys-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: overhead, slightly angled top-down (about 70 degrees)
HUMAN VARIATION (vs. previous guide): no people (previous guide, Born Small, used a family scene)
AUDIENCE: mixed (patients and clinicians)
VISUAL GOAL: Calm, organized follow-up: one kidney-shaped focal object surrounded by the quiet tools of keeping track over time.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR
vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the
circle must never touch the canvas edges). Composition archetype: I Object Hero. Camera: overhead, slightly
angled top-down.

Subject: a single smooth, matte ceramic sculpture of a human kidney in soft rose-coral glaze, resting on a
pale teal-tinted linen surface. Beside it, small supporting elements only: a closed pale-gray clinic folder
with two blank tabbed dividers, a clear empty urine specimen cup with a white lid, and a slim navy pen
resting diagonally. A faint soft shadow from window daylight falls from the upper left. Gentle shallow depth
of field; the kidney is sharp, the folder edge softly blurred.

Visual hierarchy: the ceramic kidney occupies 60–70% of the circle, positioned center-right and lower;
supporting objects 20–30% along the lower right; reserve a 20–25% TITLE SAFE ZONE in the upper-left of the
circle as plain, softly lit linen with no objects, labels, or shadows of objects. Soft edge falloff toward a
slightly deeper teal-gray at the rim. Light, calm, clinical colour grade harmonizing with clinical teal
#1a6b72 and navy #0f1e2e.

Absolutely NO readable text or labels on any object (folder, tabs, cup, and pen are blank), no titles, no
logos, no watermark. No pills, syringes, blood, or medical-procedure imagery. Full-bleed within the inscribed
circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid: busy layouts; collage overload; more than four supporting scenes; dozens of icons; tiny unreadable
labels; infographic clutter; duplicated people; repeated compositions; cropped circle; cropped objects;
cropped anatomy; edge clipping; objects touching the circular border; important content inside the title
safe zone; baked-in text, titles, captions, logos, watermarks; rectangular borders, frames, banners; dark /
charcoal / black backgrounds; cartoon style, neon, HDR, over-saturation; distorted hands or faces,
implausible anatomy; microscope slides or anything resembling a biopsy image.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant
hero subject occupying 60–70% of the circle, 2–4 supporting elements, 20–25% empty title-safe zone in the
upper-left. No people. Camera framing differs from the previous guide. Crops cleanly inside the circle with
no text or subject lost at the edges.
```

After generation: save the PNG master and a WebP twin at exactly 2048 × 2048 over the interim files (same
names), keep `alt=""` (decorative; the H1 carries the meaning).

---

## 002 — Three parts of recovery (optional raster restyle; the SVG is the source of truth)

Use only if a painterly version is wanted for social posts. Delegated style: `williamriveromd-biomedical-mechanism-figure`.

```
Create a publication-grade biomedical mechanism schematic, 1792×1024 (16:9 landscape), white background,
flat vector with soft semi-3D shading, clean sans-serif labels set in Inter (never a serif font).
Topic: Three parts of recovery in light-chain (AL) amyloidosis.
Left dashed panel: a bone-marrow plasma cell (pale gray-blue) releasing small Y-shaped light chains (muted
red); label "1 · Light-chain production"; caption "Measured in blood: free light chains, immunofixation";
pill "Weeks to months".
Center dashed panel: a glomerulus (pale pink capillary loops) with short amber fibril bundles along the loop
walls and one small pale-green macrophage at the edge; label "2 · Deposits already in the kidney"; caption
"Cleared slowly; mechanisms not fully understood"; pill "Months to years".
Right dashed panel: a simplified kidney with two small dial gauges labeled "Protein held in" and "Filtering
out"; label "3 · Kidney function"; caption "Urine protein and eGFR, read together"; pill "Months to years;
scar may remain".
Bottom flow, left to right with teal arrows: pale-pink box "Treatment stops new light chains" → pale-amber
box "Deposits shrink slowly, if at all" → pale-green box "Function may recover, often partly".
Small gray note bottom-left: "Schematic for teaching; not drawn from measured data."
Footer: small semi-transparent navy "© renalcarematters.com" bottom-right.
Avoid: photorealism, histology images, numbers, timelines with dates, dark backgrounds, clutter, extra text.
```

## 003 — Diagnosis and typing (optional raster restyle)

Style: `williamriveromd-algorithm-generator-skill`, Mode C (house style).

```
Create a clean publication-ready clinical algorithm in the renalcarematters.com house style, 1792×1024,
white background, navy #0f1e2e and teal #1a6b72 typography set in Inter, thin teal arrows, generous margins.
Title: "Confirming AL amyloidosis: three separate answers". Subtitle: "A monoclonal protein answers only the
third question".
Three equal rounded columns:
(1) "Is there amyloid in tissue?" Test: Congo red stain; apple-green birefringence under polarized light.
Why: fat pad + bone marrow in most people; organ biopsy when needed.
(2) "Which protein is it?" Test: typing by laser-capture mass spectrometry (preferred) or expert
immunostaining. Why: separates AL from AA, ATTR, LECT2, fibrinogen, and other forms.
(3) "Is there a plasma-cell clone?" Test: serum + urine immunofixation; serum free light chains;
bone-marrow examination. Why: finds the source that treatment will target.
Arrows converge on a green endpoint box: "AL amyloidosis is confirmed only when all three agree".
Gray footnote: "Bone scintigraphy is not used to diagnose AL cardiac amyloidosis when a monoclonal protein is
present (ASH 2026)."
Include a small professional footer reading "© renalcarematters.com" at the bottom-right in subtle gray.
No icons of microscopes or slides, no histology, no dark background.
```

## 004 — Follow-up domains (optional raster restyle)

```
Clean flat-vector educational panel, 1792×1024, white background, Inter typography.
Title: "Five things to follow, five different questions"; subtitle "Keep each one comparable over time and
report them separately". Five equal pastel cards in a row, each with one simple line icon in a circle:
Blood (plasma cell icon; "Free light chains, immunofixation"; Asks "Is the clone still active?"),
Urine (glomerulus icon; "24-hour protein or UPCR / UACR"; Asks "How leaky is the filter?"),
Filtration (kidney icon; "eGFR, same equation, stable, adult"; Asks "How much filtering power?"),
Heart (heart icon; "NT-proBNP, troponin, echocardiography"; Asks "How strained is the heart?"),
Daily life (clipboard icon; "Weight, blood pressure, swelling, energy"; Asks "How is treatment tolerated?").
Bottom banner: "A better blood result does not prove kidney recovery; a lower urine protein with a falling
eGFR needs review." Footer "© renalcarematters.com" bottom-right, small gray.
No numbers, no thresholds, no dark background.
```

## 005 — Discordant-results pathway (optional raster restyle)

Style: algorithm generator Mode C, portrait 1024×1536.

```
Clean clinical algorithm, portrait 1024×1536, white background, Inter typography, thin teal arrows,
six stacked rounded boxes with numbered circles, color-coded but muted:
Title "When blood, urine, and eGFR disagree"; subtitle "Clinician assessment workflow (practice proposal)".
1 Confirm comparability — same test, units, complete collection, same eGFR equation, steady state.
2 Exclude reversible causes — over-diuresis, new RAAS or SGLT2 drugs, hypotension, NSAIDs, contrast, sepsis.
3 Re-examine the clone — rising dFLC or new immunofixation: hematology review.
4 Assess the heart — NT-proBNP and troponin trends with eGFR; echocardiography.
5 Reconsider the kidney diagnosis — drug toxicity, renal vein thrombosis, obstruction, second process.
6 Report each domain separately — hematologic, renal, cardiac status with dates in the letter.
Red footnote: "Falling urine protein with falling eGFR can mean nephron loss, not repair."
Footer "© renalcarematters.com" bottom-center, small gray. No numeric thresholds, no icons, no dark background.
```

## 006 — Social share card

Code-native card shipped (1200 × 630, mint background, title, subtitle, glomerulus motif, renalcarematters.com).
If restyled, keep: title "AL Amyloidosis and Your Kidneys", subtitle "Why blood remission is only part of
recovery", attribution `renalcarematters.com`, no clinical numbers, no histology.

## Alt text and captions (as wired in the guide)

| ID | Alt text | Caption (EN) |
|---|---|---|
| 001 | `""` (decorative) | — |
| 002 | Three-panel teaching figure: light-chain production in the marrow, deposits in the kidney, and kidney function, each recovering on a different timeline. | Three parts of recovery: treatment lowers light-chain production first; existing deposits clear slowly; kidney function improves later and may stay partly scarred. |
| 003 | Diagram of the three diagnostic questions: amyloid in tissue, protein type, and plasma-cell clone, each with its test. | The three diagnostic questions and the test that answers each. |
| 004 | Five follow-up domains in AL amyloidosis: blood light chains, urine protein, filtration, heart, and symptoms. | The five things followed in AL amyloidosis, each answering a different question. |
| 005 | Clinician workflow for discordant blood, urine-protein, and eGFR trends. | A stepwise check when hematologic, urine-protein, and filtration trends move differently. |
