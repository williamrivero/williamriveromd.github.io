# Image Plan — Eosinophilia and Kidney Disease (clinician guide)

**Guide:** `guides/eosinophilia-kidney-disease-clinician.html`
**Live path for assets:** `images/<file>.{webp,png}` (PNG + WebP twin for every asset)
**House system:** Constitution v1.0 (renalcarematters.com). Light backgrounds only.
Palette — white `#ffffff` / off-white `#fafafa`; navy `#0f1e2e` (text and accents, never a fill);
clinical teal `#1a6b72`; renal green `#1f7a4d`; caution amber `#b8860b`; clinical red `#b91c1c`.
Eosinophil granules: warm orange `#d9822b` (the one subject-specific accent).
Type: **Inter** only — never a serif. Every figure (not the vignette hero) carries a small
`© renalcarematters.com` mark, bottom-right, gray, ~70% opacity.

## Asset manifest

| # | File | Role | Skill | Canvas | Placement in guide |
|---|---|---|---|---|---|
| H | `eosinophilia-kidney-disease-clinician-vignette-hero` | Circular hero beside `<h1>` | hero-vignette v3 (Scaffold C) | 2048×2048 | hero |
| 1 | `eos-kidney-four-routes-mechanism` | Four routes from eosinophilia to kidney injury | biomedical-mechanism-figure | 1792×1024 | §Four Routes |
| 2 | `eos-kidney-decision-pathway` | Count → organ threat → sediment/timeline → branch | algorithm-generator, Mode C | 1024×1536 | §Diagnostic Pathway |
| 3 | `eos-kidney-strongyloides-safety-check` | Three-lane steroid safety workflow | algorithm-generator, Mode C | 1792×1024 | §Strongyloides Check |
| OG | `eosinophilia-kidney-disease-clinician-og` | Social share card | infographic-skill (OG) | 1200×630 | `og:image` / `twitter:image` |

All `<img>` width/height attributes in the guide already match these canvases. The `<figcaption>`
plain-language descriptions and abbreviation lists are written; no HTML changes are needed when the
files land — drop the PNG and WebP into `images/` and commit.

## Content guardrails for every figure

- Labels must match the guide text exactly; do not add thresholds, doses, or percentages that are
  not in the guide.
- The only numbers allowed in figures: AEC >500 cells/µL; HE ≥1,500 cells/µL; ivermectin
  200 µg/kg; "until stool/sputum negative 2 weeks".
- Mechanism figure: eosinophils are drawn as a *variable* participant in drug-induced AIN
  ("may be few or absent") — never as the defining cell.
- No patient faces anywhere in this guide's figures (the hero is anatomy, no people).
