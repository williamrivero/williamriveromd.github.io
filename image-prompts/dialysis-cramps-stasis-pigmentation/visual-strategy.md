# Visual Strategy — Dialysis Cramps & Stasis Pigmentation

**Guide slug:** `dialysis-cramps-stasis-pigmentation`
**Guide file:** `guides/dialysis-cramps-stasis-pigmentation.html`
**Audience:** dual-mode (patients + clinicians); patient track multilingual EN/TL/CEB/KAP, clinician track English-only
**Pipeline stage:** Stage 1 (prompt authoring) → feeds Stage 2 (`williamriveromd-local-image-generator`)
**Target generator:** ChatGPT Image Generator GPT — <https://chatgpt.com/g/g-pmuQfob8d-image-generator>

---

## 1. Guide purpose (what each image must support)

This dual patient/clinician guide frames intradialytic muscle cramps and lower-limb stasis (hemosiderin) pigmentation as **two visible markers on a single, slow-moving spectrum of lower-limb tissue hypoxia** — the **Hypoxic Lower-Limb Spectrum**. The same upstream substrate (chronic volume overload, microvascular compromise, dependent congestion, ATP-cofactor depletion, mechanical stretch) produces:

- an **acute axis** (the last-hour cramp) when ultrafiltration transiently violates the muscle's oxygen-and-cofactor margin, and
- a **chronic axis** (the brown gaiter, then dermatitis, then ulceration) when years of standing venous hypertension and microvascular hypoxia accumulate.

Diabetes does not change the spectrum — it accelerates progression along it and changes the type of wound that eventually appears (diabetic foot ulcer vs venous stasis ulcer), with the **ABI safety gate failing** in the calcified DM-CKD vasculature so a **TBI / TcPO₂ pathway** is required.

Every image must serve **one** of three jobs:

1. Make the **paired phenotype** visible (cramp + pigment, same leg).
2. Make the **spectrum** legible at a glance (a continuum, not a binary).
3. Equip **clinicians** with diagrammatic anchors for SERCA-ATP physiology, the hemosiderin/MMP pathway, the multi-hit cramp model, the ABI→TBI safety gate, and the diabetic-foot accelerator.

---

## 2. House style (non-negotiable across every prompt)

- **Light backgrounds only** — white `#ffffff`, off-white `#fafafa`, or very-light teal tint `#eef6f7`. **Never** navy, charcoal, or black as a fill.
- **Color tokens:**
  - Navy `#0f1e2e` — text, headers, structural lines
  - Clinical teal `#1a6b72` — accents, primary flow
  - Renal green `#1f7a4d` — safe / normal states
  - Amber/gold `#b8860b` — caution / intermediate
  - Clinical red `#b91c1c` — danger / cramp / hypoperfusion
  - Soft purple `#6b21a8` — hypothesis / chronic axis / advanced spectrum
- **Typography (mandatory):** all on-image type must use **Inter**, **Nunito Sans**, **IBM Plex Sans**, or **Manrope** only — never a serif, decorative, or handwritten face. The chosen font is named explicitly in every prompt.
- **Mandatory attribution** on every image: `williamriveromd.com` (and on mechanism schematics, `© williamriveromd.com`) — small, semi-transparent navy/dark-teal text, bottom-right for landscape/square, bottom-center for portrait.
- **Prompt closing line on every image:** "No journal names, guideline acronyms, brand names, or watermarks."
- **Filipino clinical context** wherever people appear — natural skin tones, modest realistic clothing, daylight clinical or home settings.

---

## 3. Image inventory (14 assets — 10 base + 4 clinician extensions)

The guide is **dual-mode** (patient + clinician toggle), so every asset is explicitly scoped to one of three audiences in the table below:

- **PT** = renders only when the patient tab is active (`.mode-patient` containers, or no mode scoping).
- **MD** = renders only when the clinician tab is active (`.mode-physician` containers).
- **Both** = shared figures placed inside both a `.mode-patient` and a `.mode-physician` section so each audience sees them in context.

| # | File | Skill used | Archetype / Scaffold | Dimensions | Mode | Placement in guide |
|---|------|-----------|----------------------|-----------:|:----:|----|
| 000 | `dialysis-cramps-stasis-pigmentation-og-card.png` | Infographic | OG / Social Share Card | 1200 × 630 | — | `<head>` `og:image`; link previews on FB/X/LinkedIn/iMessage |
| 001 | `dialysis-cramps-stasis-pigmentation-vignette-hero.png` | Hero Vignette v3 | Scaffold A — Clinical People | 2048 × 2048 | **PT** | `figure.hero-figure.mode-patient > .hero-vignette` — hidden in clinician mode |
| 002 | `dialysis-cramps-serca-relaxation-pump.png` | Biomedical Mechanism | Multi-scale schematic (cell → SERCA pump) | 1792 × 1024 | **Both** | §pt-oxygen + §md-pathophys |
| 003 | `dialysis-cramps-5hit-mechanism.png` | Biomedical Mechanism | Organ → inset → injury/intervention/benefit | 1792 × 1024 | **Both** | §pt-cramps + §md-pathophys |
| 004 | `dialysis-cramps-hemosiderin-pathway.png` | Biomedical Mechanism | Organ → dermal-capillary inset → MMP/inflammation flow | 1792 × 1024 | **Both** | §pt-darken + §md-pigment |
| 005 | `dialysis-cramps-two-axes-one-field.png` | Simple Figure | Scaffold B — Side-by-Side Comparison | 1792 × 1024 | **Both** | §pt-connection + §md-theory |
| 006 | `dialysis-cramps-hypoxic-lower-limb-sigil.png` | Organ-Crosstalk Sigil | Minimal monoline + dotted arrows | 1024 × 1024 | **MD** | §md-theory header |
| 007 | `dialysis-cramps-spectrum-staircase.png` | Simple Figure | Scaffold C — Horizontal Step Sequence (7 stages) | 1792 × 1024 | **Both** | §pt-spectrum + §md-spectrum (top of section) |
| 008 | `dialysis-cramps-rescue-steps.png` | Simple Figure | Scaffold C — Step Sequence (4 steps) | 1792 × 1024 | **PT** | §pt-rescue (60-second rescue) |
| 009 | `dialysis-cramps-abi-tbi-algorithm.png` | Algorithm Generator | Mode C — house-style clinical algorithm | 1024 × 1536 | **MD** | §md-workup + §md-spectrum |
| 010 | `dialysis-cramps-management-tiers-workflow.png` | Infographic | Archetype 8 — Circular Workflow | 1024 × 1024 | **MD** | §md-management (opens the tiered section) |
| 011 | `dialysis-cramps-pharmacology-reference-card.png` | Simple Figure | Scaffold E — Clinician Reference Card (4:3) | 1536 × 1152 | **MD** | §md-pharmacology (top, above the HTML table) |
| 012 | `dialysis-cramps-diabetes-accelerator-mechanism.png` | Biomedical Mechanism | Organ → inset → bottom flow | 1792 × 1024 | **MD** | §md-spectrum (DM amplification subsection) |
| 013 | `dialysis-cramps-clinic-audit-pipeline.png` | Simple Figure | Scaffold C — Step Sequence (4 steps) | 1792 × 1024 | **MD** | §md-audit (top of the testable-predictions section) |

**Clinician-only inventory (6 dedicated images):** 006 (sigil), 009 (ABI/TBI algorithm), 010 (management workflow), 011 (pharmacology card), 012 (DM accelerator mechanism), 013 (audit pipeline). Together they anchor every clinician section (pathophys, pigment, theory, workup, management, pharmacology, spectrum, audit) — with §md-pearls deliberately left visual-free (its content is short alert callouts).

**Coverage map.** Every Stage 1 skill is exercised at least once:

- **Infographic skill** → #000 (OG card), #010 (management workflow).
- **Hero vignette skill** → #001.
- **Biomedical mechanism figure skill** → #002, #003, #004, #012 (the four big mechanism schematics that anchor the science).
- **Simple figure skill** → #005, #007, #008, #011, #013 (single-concept teaching figures and reference cards).
- **Organ-crosstalk sigil skill** → #006 (the hypothesis sigil).
- **Algorithm generator skill** → #009 (the ABI/TBI safety gate).

---

## 4. Variety, repeatability, and Filipino context

- Only **one** image features people (#001, the hero vignette). To avoid repetition across the wider library, this hero rotates to **Composition Archetype I (Object Hero)** centered on a single Filipino HD patient's lower leg in mid-stretch at the dialysis chair (rather than a face-forward portrait), preserving a 20–25% title-safe zone of soft blurred clinic interior on the left.
- The **OG card (#000)** is text-forward; no people. It carries the title + subtitle + a calm two-state lower-leg motif (cramp lightning on one calf, faint gaiter pigmentation on the other) so the link preview communicates the "paired phenotype" instantly.
- All mechanism schematics (#002–#004) use the dashed-inset, muted-clinical-palette house style — they are deliberately **wordless beyond short scientific labels** so they read identically across the patient and clinician tracks.
- The spectrum staircase (#007) uses a color-graded sequence (green → teal → amber → red → purple) so it functions as a quick mental map for both audiences without translation.

---

## 5. Output (what this folder ships)

```
image-prompts/dialysis-cramps-stasis-pigmentation/
├── visual-strategy.md           ← this file (blueprint)
├── image-prompts.md             ← consolidated paste-ready prompts for the ChatGPT Image Generator GPT
└── README-image-generation.md   ← how to use the prompts and save the outputs
```

Both files are versioned with the guide. Stage 2 (`williamriveromd-local-image-generator`) consumes them to build the local `/Users/williamgregoryrivero/Downloads/dialysis-cramps-stasis-pigmentation/` folder, manifest CSV/JSON, and wire the generated images back into the guide HTML.
