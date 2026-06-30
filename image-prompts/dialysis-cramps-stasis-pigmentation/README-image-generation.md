# Image Generation — Dialysis Cramps & Stasis Pigmentation

**Guide:** [`guides/dialysis-cramps-stasis-pigmentation.html`](../../guides/dialysis-cramps-stasis-pigmentation.html)
**Pack contents:** 10 production-ready prompts (1 OG card + 1 hero vignette + 3 biomedical mechanism schematics + 3 simple figures + 1 organ-crosstalk sigil + 1 clinical algorithm).
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

| # | File name | Skill | Dimensions | Section in guide |
|---|-----------|-------|-----------:|---|
| 000 | `dialysis-cramps-stasis-pigmentation-og-card.png` | infographic | 1200 × 630 | `<head>` `og:image` |
| 001 | `dialysis-cramps-stasis-pigmentation-vignette-hero.png` | hero-vignette | 2048 × 2048 | hero (patient-mode) |
| 002 | `dialysis-cramps-serca-relaxation-pump.png` | biomedical-mechanism-figure | 1792 × 1024 | §pt-oxygen + §md-pathophys |
| 003 | `dialysis-cramps-5hit-mechanism.png` | biomedical-mechanism-figure | 1792 × 1024 | §pt-cramps + §md-pathophys |
| 004 | `dialysis-cramps-hemosiderin-pathway.png` | biomedical-mechanism-figure | 1792 × 1024 | §pt-darken + §md-pigment |
| 005 | `dialysis-cramps-two-axes-one-field.png` | simple-figure | 1792 × 1024 | §pt-connection + §md-theory |
| 006 | `dialysis-cramps-hypoxic-lower-limb-sigil.png` | organ-crosstalk-sigil | 1024 × 1024 | §md-theory header |
| 007 | `dialysis-cramps-spectrum-staircase.png` | simple-figure | 1792 × 1024 | §pt-spectrum + §md-spectrum |
| 008 | `dialysis-cramps-rescue-steps.png` | simple-figure | 1792 × 1024 | §pt-rescue |
| 009 | `dialysis-cramps-abi-tbi-algorithm.png` | algorithm-generator | 1024 × 1536 | §md-workup + §md-spectrum |

---

## House-style invariants the GPT must obey

- **Light background only** — white `#ffffff`, off-white `#fafafa`, or very-light teal tint `#eef6f7`. Never dark.
- **Sans-serif only** — Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never a serif or decorative face.
- **Mandatory attribution** — every image carries `williamriveromd.com` (or `© williamriveromd.com` on mechanism schematics) in small semi-transparent navy text in the bottom-right corner.
- **No brand/journal names** — never embed AJKD, NEJM, KDIGO, or guideline acronyms into the image.
- **Filipino clinical context** for any image with people (only #001 in this pack).

If a generated image fails any invariant, regenerate it — do not paper over with post-processing.
