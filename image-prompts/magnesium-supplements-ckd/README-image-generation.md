# Production run sheet — *Magnesium Supplements and Kidney Disease*

**Guide:** `guides/magnesium-supplements-ckd.html` · **Tool:** `guides/calc-magnesium-replacement.html`
**Prompts live in:** [`../magnesium-supplements-ckd-image-plan.md`](../magnesium-supplements-ckd-image-plan.md)
**Generate in:** ChatGPT Image Generator GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Save outputs to:** `generated-images/` in this folder, then copy the `.png` + `.webp` pair into `images/`.

Work top to bottom. Each row's `PROMPT` block in the plan is copy-paste ready — paste the whole block,
including the `NEGATIVE INSTRUCTIONS` and `QUALITY CHECK` sections.

| # | Paste this section of the plan | Size | Save as |
|---|---|---|---|
| 1 | § 1 Circular vignette hero | 2048 × 2048 | `magnesium-supplements-ckd-vignette-hero.png` |
| 2 | § 2 OG / social share card | **1200 × 630 (fixed)** | `magnesium-supplements-ckd-og.png` |
| 3 | § 3 Gut–kidney–bone sigil | 1024 × 1024 | `magnesium-supplements-ckd-01-gut-kidney-bone-sigil.png` |
| 4 | § 4 Renal handling mechanism | 1792 × 1024 | `magnesium-supplements-ckd-02-renal-handling-mechanism.png` |
| 5 | § 5 Hidden magnesium sources | 1792 × 1024 | `magnesium-supplements-ckd-03-hidden-sources.png` |
| 6 | § 6 Elemental ladder | 1024 × 1536 | `magnesium-supplements-ckd-04-elemental-ladder.png` |
| 7 | § 7 Claim check | 1792 × 1024 | `magnesium-supplements-ckd-05-claim-check.png` |
| 8 | § 8 Label explainer | 1792 × 1024 | `magnesium-supplements-ckd-06-label-explainer.png` |
| 9 | § 9 Interaction spacing card | 1536 × 1152 | `magnesium-supplements-ckd-07-interaction-spacing.png` |
| 10 | § 10 Decision pathway | 1024 × 1536 | `magnesium-supplements-ckd-08-decision-pathway.png` |

## Reject-and-regenerate triggers

Text-heavy assets are where image models drift. Regenerate rather than accept if any of these appear —
each one breaks a commitment the guide makes in prose:

- **Any milligram-per-day figure, daily target, or split morning/night schedule** on any asset.
- **Any CKD stage number paired with a dose.**
- **A trophy, crown, podium, gold star, #1 badge, or green check** on a single magnesium form.
- **An arrow from a salt to a brain, heart, or sleeping figure** — that diagram is the misinformation the guide corrects.
- **A fourth evidence label** on asset 7, or the words "debunked," "myth," "false," or "doesn't work."
- **Altered, reordered, or re-rounded percentages** on asset 6 — verify against `MG_FORMS` in the calculator.
- **Invented drug interactions or spacing intervals** on asset 9, or clock icons on rows 3–7.
- **Any branch on asset 10 that ends in "so take magnesium."**
- **Readable brand names, real packaging, or price tags** on any asset.
- **A serif font**, or a dark background, anywhere.
- **A missing `renalcarematters.com` mark** — required on every asset except the wordless hero.

## After the images land

1. Copy each `.png` and its `.webp` twin into `images/`.
2. Swap the hero and the four social tags in both the guide and the calculator — both currently point at the
   shared `hero-cat-electrolytes` placeholder. Exact tag values are in the plan's Production checklist.
3. Wire assets 3–10 as `<figure>` blocks with `<picture>`, `alt`, and a `<figcaption><p class="fig-desc">`
   description (CLAUDE.md rule 11). Assets 4, 6, 7 and 9 also need `<dl class="fig-abbrevs">` — the
   abbreviation strings are pre-written in `image-manifest.csv`.
4. Mirror every `fig-desc` into TL/CEB/KAP sibling spans. This guide is four-language throughout.
5. Re-run the patch pipeline and the acronym audit (commands in the plan's Production checklist).

`image-manifest.csv` / `image-manifest.json` carry the alt text and abbreviation strings for step 3, so the
HTML wiring does not need to be re-authored from scratch.
