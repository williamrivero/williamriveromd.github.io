# Image Generation — Dialysis Cramps & Stasis Pigmentation

**Guide:** [`guides/dialysis-cramps-stasis-pigmentation.html`](../../guides/dialysis-cramps-stasis-pigmentation.html)
**Pack contents:** 14 production-ready prompts (1 OG card + 1 hero vignette + 4 biomedical mechanism schematics + 5 simple figures + 1 organ-crosstalk sigil + 1 clinical algorithm + 1 circular workflow). 6 of the 14 are **clinician-only** (mode-physician scoped); 1 is **patient-only**; 1 is the OG share card; the remaining 6 are **shared** across both tracks of the dual-mode guide.
**Target tool:** ChatGPT Image Generator GPT — <https://chatgpt.com/g/g-pmuQfob8d-image-generator>

---

## Files in this folder

| File | What it is |
|---|---|
| [`visual-strategy.md`](visual-strategy.md) | The image-plan blueprint: rationale, archetype mapping, house style, placement in the guide. |
| [`image-prompts.md`](image-prompts.md) | The consolidated, paste-ready master with all 10 prompts in order. |
| `README-image-generation.md` | This file — how to use the pack. |

---

## How to run the pack

1. Open the ChatGPT Image Generator GPT (link above).
2. Open `image-prompts.md`, scroll to the first prompt block.
3. Copy everything between the opening ```` ``` ```` and the closing ```` ``` ```` and paste it into the GPT.
4. Confirm the output matches the `PIXEL DIMENSIONS:` line on the prompt (especially for **000 — OG card**, which must be exactly **1200 × 630**).
5. Save the file with the exact `FILE NAME:` from the prompt into your local `generated-images/` folder.
6. Repeat for prompts **001 → 009**.

After all 10 are generated, hand the folder to **Stage 2** (`williamriveromd-local-image-generator`) which will:

- Validate every prompt file against the required schema.
- Build `image-manifest.csv` and `image-manifest.json`.
- Place the renamed `.png` + `.webp` twin into the repo's `/images/` directory.
- Append the `og:image / og:image:width / og:image:height / og:image:alt` tags into the guide HTML.

---

## Prompt index

| # | File name | Skill | Dimensions | Mode | Section in guide |
|---|-----------|-------|-----------:|:----:|---|
| 000 | `dialysis-cramps-stasis-pigmentation-og-card.png` | infographic | 1200 × 630 | — | `<head>` `og:image` |
| 001 | `dialysis-cramps-stasis-pigmentation-vignette-hero.png` | hero-vignette | 2048 × 2048 | **PT** | hero, scoped `mode-patient` |
| 002 | `dialysis-cramps-serca-relaxation-pump.png` | biomedical-mechanism-figure | 1792 × 1024 | **Both** | §pt-oxygen + §md-pathophys |
| 003 | `dialysis-cramps-5hit-mechanism.png` | biomedical-mechanism-figure | 1792 × 1024 | **Both** | §pt-cramps + §md-pathophys |
| 004 | `dialysis-cramps-hemosiderin-pathway.png` | biomedical-mechanism-figure | 1792 × 1024 | **Both** | §pt-darken + §md-pigment |
| 005 | `dialysis-cramps-two-axes-one-field.png` | simple-figure | 1792 × 1024 | **Both** | §pt-connection + §md-theory |
| 006 | `dialysis-cramps-hypoxic-lower-limb-sigil.png` | organ-crosstalk-sigil | 1024 × 1024 | **MD** | §md-theory header |
| 007 | `dialysis-cramps-spectrum-staircase.png` | simple-figure | 1792 × 1024 | **Both** | §pt-spectrum + §md-spectrum |
| 008 | `dialysis-cramps-rescue-steps.png` | simple-figure | 1792 × 1024 | **PT** | §pt-rescue |
| 009 | `dialysis-cramps-abi-tbi-algorithm.png` | algorithm-generator | 1024 × 1536 | **MD** | §md-workup + §md-spectrum |
| **010** | `dialysis-cramps-management-tiers-workflow.png` | infographic (circular workflow) | 1024 × 1024 | **MD** | §md-management |
| **011** | `dialysis-cramps-pharmacology-reference-card.png` | simple-figure (reference card) | 1536 × 1152 | **MD** | §md-pharmacology |
| **012** | `dialysis-cramps-diabetes-accelerator-mechanism.png` | biomedical-mechanism-figure | 1792 × 1024 | **MD** | §md-spectrum (DM subsection) |
| **013** | `dialysis-cramps-clinic-audit-pipeline.png` | simple-figure (step sequence) | 1792 × 1024 | **MD** | §md-audit |

**Mode legend:** **PT** = renders only in patient mode (`.mode-patient` container). **MD** = renders only in clinician mode (`.mode-physician` container). **Both** = the same image is embedded inside one patient-mode section AND one clinician-mode section so each audience sees it in their own context. "—" = the OG card, which never renders inline on the page; it serves the link-preview only.

**Wiring rule (dual-mode invariant):** any clinician-only image (006, 009, 010, 011, 012, 013) must be placed **inside** the corresponding `<section class="section mode-physician" id="...">` so the master CSS hides it in patient mode. Never wire a clinician-only image into a `.mode-patient` section or a mode-agnostic container — that would expose clinician content to patients and break the dual-mode contract.

---

## House-style invariants the GPT must obey

- **Light background only** — white `#ffffff`, off-white `#fafafa`, or very-light teal tint `#eef6f7`. Never dark.
- **Sans-serif only** — Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never a serif or decorative face.
- **Mandatory attribution** — every image carries `williamriveromd.com` (or `© williamriveromd.com` on mechanism schematics) in small semi-transparent navy text in the bottom-right corner.
- **No brand/journal names** — never embed AJKD, NEJM, KDIGO, or guideline acronyms into the image.
- **Filipino clinical context** for any image with people (only #001 in this pack).

If a generated image fails any invariant, regenerate it — do not paper over with post-processing.
