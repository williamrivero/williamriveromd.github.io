# Image Plan — Unlocking Urine Electrolytes (clinician guide)

**Guide:** `guides/unlocking-urine-electrolytes-clinician.html`
**Live path for assets:** `images/unlocking-urine-electrolytes-clinician-*.{webp,png}`
**House system:** Constitution v1.0 (renalcarematters.com). Light backgrounds only.
Palette — background `#ffffff` / off-white `#fafafa`; **navy `#0f1e2e` (text & accents only, never a fill)**;
clinical teal `#1a6b72`; renal green `#1f7a4d`; caution amber/gold `#b8860b`; clinical red `#b91c1c`.
Type: **Inter** (or Nunito Sans / IBM Plex Sans / Manrope) — never a serif.
Every asset carries a small `© renalcarematters.com` mark, bottom-right, ~60–70% opacity.

## Two prompt packs (same 10 assets, two engines)

- **`PROMPTS-nanobanana.md`** — Gemini / Nano Banana. Conversational, scene-first prompts; explicit
  aspect ratio + "render every label crisply, spelled exactly as written." Nano Banana renders text
  well, so labels are stated verbatim.
- **`PROMPTS-gpt.md`** — ChatGPT Image Generator (GPT-image / GPT-4o), Constitution v1.0 layered format.
  Use both, compare, keep the stronger render per figure.

## Asset manifest

| # | Slug (`…-clinician-`) | Role | Skill mapping | Canvas | Embedded in guide? |
|---|---|---|---|---|---|
| H | `vignette-hero` | Circular hero (beside `<h1>`) | hero-vignette v3 | 2048×2048 (1:1) | ✅ hero |
| 1 | `01-serum-problem-urine-response` | Central mechanism (blood→nephron→urine, 4 verbs) | simple-figure | 1659×948 (~16:9) | ✅ §Mental Model |
| 2 | `02-interpretation-loop` | Five-question loop | algorithm-generator | 1200×1200 (1:1) | ⭘ optional companion |
| 3 | `03-concentration-deceives` | Two cups, identical total Na | simple-figure | 1200×900 (4:3) | ✅ §Specimen |
| 4 | `04-urine-chloride-locator` | Two-pathway branch + gray-zone band | algorithm-generator | 1659×948 | ✅ §Chloride |
| 5 | `05-hyponatremia-pathway` | Diagnostic flowchart, emergency banner separate | algorithm-generator | 1200×1400 (portrait) | ✅ §Hyponatremia |
| 6 | `06-hypokalemia-matrix` | 2×2 matrix + BP/urine-Cl refiners | simple-figure | 1200×1000 | ✅ §Hypokalemia |
| 7 | `07-formula-toolbox-stopsigns` | Five formula cards, each 1 assumption + 1 failure | simple-figure / reference card | 1659×948 | ✅ §FENa/FEUrea |
| 8 | `08-case-resolution` | Linear cascade of the opening case | algorithm-generator | 1659×948 | ✅ §Cases |
| OG | `og` | Social share card (title baked) | infographic-skill | 1200×630 | og:image |

**Production notes**
- Export each as **both** `.webp` (primary) and `.png` (fallback) at the listed pixel size; the guide's
  `<picture>` blocks already reference both.
- The hero is a **pure picture — no baked words** (the HTML `<h1>` sits beside it). Keep a 20–25%
  calm title-safe zone even though the CSS circle masks it.
- Only the **OG card** (and, lightly, the in-body figures) carry text; the hero never does.
- After images are confirmed, append `og:image` dims/alt if they change (currently 1200×630).
- Medical-accuracy guardrails (Constitution): do not invent numeric thresholds beyond the guide's
  stated approximate cutoffs (urine Cl ~15–20 mmol/L, urine Na ~30 mmol/L, UOsm ~100 mOsm/kg,
  K/Cr ~1.5 mmol/mmol, FENa 1–2%); render thresholds as gray-zone bands, never hard walls.
