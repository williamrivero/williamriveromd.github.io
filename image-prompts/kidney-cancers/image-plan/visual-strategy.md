# Visual Strategy — Kidney Cancers

**Guide slug:** `kidney-cancers`
**Guide file:** `guides/kidney-cancers.html`
**Pipeline stage:** Stage 1 (prompt authoring) → this strategy feeds Stage 2 (`williamriveromd-local-image-generator`)

## Guide purpose

The "Kidney Cancers" guide is a patient-education resource for williamriveromd.com
covering renal cell carcinoma and related kidney tumors: how they are found
(often incidentally), the common subtypes and their underlying anatomy,
hereditary syndromes (notably VHL / HIF biology), the diagnostic workup,
TNM staging, treatment pathways, and the nephron-sparing surgery question.
It explains a frightening diagnosis in calm, accurate, plain language while
still giving enough clinical structure to be useful to referring clinicians.

## Audience

Dual-mode: written for **patients and their families** in the default reading
mode, with a **clinician mode** that surfaces staging, algorithm, and surgical
detail. Images must read clearly for a worried patient at a glance, yet stay
clinically accurate enough that a physician trusts them. Multilingual content
(English, Tagalog, Cebuano, Kapampangan) is text-only; images carry no
language-specific body copy beyond short universal labels.

## House style (mandatory)

- **Light backgrounds only** — clean white / very pale neutral. No dark posters.
- **Color tokens:**
  - Navy `#0f1e2e` — primary text, headers, structural lines
  - Teal `#1a6b72` — accents, anatomy highlights, primary flow
  - Green `#1f7a4d` — favorable / benign / lower-risk states
  - Amber `#b8860b` — caution / intermediate / surveillance states
  - Red `#b91c1c` — high-risk / malignant / urgent states
- **Mandatory attribution:** every image carries the `© williamriveromd.com`
  credit line.
- Clinician algorithms use the conservative flat-flowchart style (white
  background, boxes, diamond decisions, minimal color, no 3D, no icons).
- No journal names, guideline acronyms, brand names, or watermarks in any image.

## Why these images exist

The guide previously relied on inline SVGs for its diagrams. This pack replaces
those removed inline SVGs with a coherent set of 10 raster images (each shipped
as a `.png` + `.webp` pair), one keyed to each major section, giving a unified
house-style look and better fidelity than the hand-rolled SVGs allowed. The
guide HTML currently carries matching `<!-- IMAGE PLACEHOLDER -->` comments at
each section for Stage-2 wiring.

## Image plan

| # | FILE NAME (.png+.webp) | SECTION | SKILL | ARCHETYPE | DIMS |
|---|---|---|---|---|---|
| 001 | kidney-cancers-hero-overview | #overview | infographic | Photorealistic Editorial Hero | 1792×1024 |
| 002 | kidney-cancers-anatomy-subtypes-infographic | #types | infographic | Multi-panel/3D | 1792×1024 |
| 003 | kidney-cancers-bosniak-ladder-infographic | #incidental-mass | simple-figure | Step sequence | 1792×1024 |
| 004 | kidney-cancers-vhl-hif-mechanism-infographic | #hereditary | mechanism | Mechanism poster | 1792×1024 |
| 005 | kidney-cancers-how-found-infographic | #symptoms | simple-figure | Quick-look/bar | 1792×1024 |
| 006 | kidney-cancers-diagnostic-algorithm-infographic | #diagnosis | simple-figure | Clinical algorithm | 1024×1536 |
| 007 | kidney-cancers-tnm-staging-infographic | #staging | simple-figure | Step sequence | 1792×1024 |
| 008 | kidney-cancers-treatment-algorithm-infographic | #treatment | simple-figure | Clinical algorithm | 1024×1536 |
| 009 | kidney-cancers-partial-vs-radical-infographic | #nephron-sparing | simple-figure | Comparison | 1792×1024 |
| 010 | kidney-cancers-urinary-system-infographic | #urinary-tract | infographic | Multi-panel/3D | 1792×1024 |

## Per-image rationale and Stage-1 source

- **001 — Hero overview** (`#overview`, infographic skill): photorealistic
  editorial hero that sets a calm, authoritative tone and anchors the guide's
  opening. Replaces the old inline header SVG with a polished LCP-quality image.
- **002 — Anatomy & subtypes** (`#types`, infographic skill): multi-panel / 3D
  view of kidney anatomy mapped to the main renal cell carcinoma subtypes, so
  patients can see where tumors arise and how subtypes differ. Replaces the
  removed inline subtype-anatomy SVG.
- **003 — Bosniak ladder** (`#incidental-mass`, simple-figure skill): a step
  sequence climbing the cystic-mass risk ladder, clarifying why an incidentally
  found cyst may be watched or worked up. Replaces the inline risk-ladder SVG.
- **004 — VHL / HIF mechanism** (`#hereditary`, mechanism skill): review-article
  mechanism poster showing the VHL → HIF pathway behind hereditary clear-cell
  disease, organ-to-cellular. Replaces the inline pathway SVG.
- **005 — How it's found** (`#symptoms`, simple-figure skill): quick-look / bar
  figure showing how most kidney cancers are found incidentally vs. via the
  classic symptom triad. Replaces the inline presentation SVG.
- **006 — Diagnostic algorithm** (`#diagnosis`, simple-figure skill): portrait
  flat-flowchart algorithm walking a renal mass through imaging and biopsy
  decisions. Replaces the inline diagnostic-flow SVG.
- **007 — TNM staging** (`#staging`, simple-figure skill): step-sequence figure
  laying out tumor / node / metastasis staging tiers with risk coloring.
  Replaces the inline staging SVG.
- **008 — Treatment algorithm** (`#treatment`, simple-figure skill): portrait
  flat-flowchart mapping stage to treatment pathway (surgery, ablation,
  surveillance, systemic therapy). Replaces the inline treatment-flow SVG.
- **009 — Partial vs. radical** (`#nephron-sparing`, simple-figure skill):
  side-by-side comparison of partial (nephron-sparing) vs. radical nephrectomy
  and their trade-offs. Replaces the inline comparison SVG.
- **010 — Urinary system** (`#urinary-tract`, infographic skill): multi-panel /
  3D orientation of the full urinary tract so patients can place the kidneys in
  context. Replaces the inline urinary-tract SVG.
