---
name: williamriveromd-hero-vignette
description: >-
  Produces a single copy-paste ChatGPT Image Generator prompt for a guide HERO
  graphic designed to sit inside the new circular vignette beside the hero title
  on williamriveromd.com. Use whenever creating or regenerating the hero image
  for a guide whose hero uses the circular-vignette layout (copy on the left, a
  round photo/illustration on the right — e.g. epilepsy-seizures-ckd, igan-guide,
  prostate-cancer-ckd, hivan, first-nephrology-visit-guide, natural-supplements).
  The defining constraints: SQUARE 1:1, a single subject centered inside the
  inscribed circle's safe zone, and NO baked-in title/heading/logo text (the page
  renders the title in HTML next to the circle). For full-width editorial poster
  heroes or OG cards (NOT the circular vignette), use williamriveromd-infographic-skill
  instead. For in-body figures/algorithms use williamriveromd-simple-figure.
---

# WILLIAM RIVERO MD — HERO VIGNETTE GENERATOR v1

## PURPOSE

Generate ONE production-ready image prompt for a **guide hero graphic that will be
displayed cropped to a circle** (the `.hero-vignette` disc) beside the hero title.

This is fundamentally different from the older full-width editorial hero / OG card:
the image is masked into a **circle**, centered with `object-fit: cover` and a focal
point near `object-position: 50% 42%`, then given a soft edge vignette by CSS. Any
title text, watermark band, logo lockup, or infographic content baked into the image
will be **clipped by the circle and/or duplicate the HTML title** — so it must not
exist in the image.

## WHEN TO USE

Use this skill when:
- A guide's hero uses the **circular vignette** layout (`hero-grid` → `hero-copy` +
  `figure.hero-figure > .hero-vignette > img`).
- You are **regenerating** an existing hero photo so it crops cleanly into the circle.
- You want a clean, single-subject clinical **photo**, **still-life**, or **calm
  editorial illustration** — with no embedded words.

Use a DIFFERENT skill when:
- The hero is a **full-width infographic/poster** (dense panels, stats, numbered
  steps, baked title) → `williamriveromd-infographic-skill`. These are intentionally
  kept full-width and are NOT circle-cropped.
- You need an **OG / social share card** (1200×630 with title text) →
  `williamriveromd-infographic-skill`.
- You need an **in-body figure, algorithm, or comparison** →
  `williamriveromd-simple-figure`.

> Rule of thumb: if the deliverable contains *words*, it is not a vignette hero.
> The vignette hero is purely a picture; the guide's `<h1>` sits beside it.

---

## VIGNETTE TECHNICAL CONSTRAINTS (non-negotiable)

1. **Square canvas, 1:1.** The circle is inscribed in a square frame.
2. **Safe zone = the inscribed circle.** Everything important (faces, hands, the key
   object) must sit within the centered circle whose diameter ≈ the square's width.
   **The four corners WILL be cut off** — keep them empty / soft background only.
3. **Focal point slightly high.** The display focal point is ~42% from the top, so
   compose the main subject's faces/key detail around the **upper-middle** (about
   38–48% down), not dead-center and never near the bottom edge.
4. **NO baked-in text of any kind** — no title, no subtitle, no captions, no numbered
   callouts, no logo, no "williamriveromd.com" watermark. (Attribution lives in the
   page footer; a baked watermark would be clipped by the circle anyway.)
5. **No hard rectangular borders, frames, or banners** — the CSS adds the round mask,
   border ring, and edge vignette. Deliver a full-bleed image.
6. **Edge-friendly background.** Let the scene fall off into a soft, slightly deeper
   tone toward the edges so it blends with the CSS vignette; avoid bright busy detail
   right at the rim.

---

## HOUSE STYLE CONSTITUTION

### Subject & tone
- Warm, authentic, **Filipino clinical context** where people are shown: a Filipino
  nephrologist (mid-career, approachable, white coat / scrubs, stethoscope) with a
  Filipino patient and/or family, in a clean modern Philippine clinic or dialysis unit.
- Calm, reassuring, documentary-realistic — not stocky, not staged-cheesy, not dark
  or clinical-cold. Soft natural daylight.
- For non-people topics: a single clean **still-life** (e.g. supplements, food, lab
  tube, BP cuff, medication) or a calm **semi-photoreal 3D anatomy** (kidney, nephron)
  on a soft, uncluttered surface.

### Color & light
- Bright, light, airy. Soft daylight, gentle depth of field, shallow background blur.
- Palette harmonizes with the pastel hero: clinical teal `#1a6b72`, navy `#0f1e2e`,
  renal green `#1f7a4d`, warm neutrals. Avoid heavy saturation, HDR, or neon.
- Backgrounds: light clinic interiors, soft teal-tinted or warm neutral surfaces.
  Never a dark/charcoal/black scene.

### Realism
- Anatomically and clinically plausible. Correct hands, faces, equipment.
- Skin tones and features reflect Filipino patients/clinicians.

---

## CANONICAL SIZE

| Use | Dimensions | Ratio |
|---|---|---|
| Circular vignette hero (default) | **1024 × 1024** | 1:1 |
| Higher-res option | 1536 × 1536 | 1:1 |

Always **square**. Never landscape/portrait for a vignette hero (those get badly cropped).

---

## EXECUTION INSTRUCTIONS

When this skill is invoked:

1. **Identify the guide** (slug) and its subject. Decide the subject archetype:
   - **People scene** (clinician + patient/family discussing the condition) — default
     for most patient guides.
   - **Still-life / object** (food, supplement, medication, device, lab sample).
   - **Calm 3D anatomy / illustration** (kidney, nephron, vessel) on a soft surface.
2. **Pick ONE scaffold** below and fill in the specifics.
3. **Output exactly ONE prompt block** in the OUTPUT FORMAT — nothing else.

### Scaffold A — Clinical People Scene (default, 1024 × 1024)
```
Square 1:1 photorealistic editorial photograph for a medical hero image, composed to be
cropped into a CIRCLE. A Filipino nephrologist ([describe: e.g. warm mid-career doctor in
white coat with stethoscope]) [interacting] with a Filipino [patient / older patient /
patient and family member] about [TOPIC], in a clean, bright modern Philippine clinic.
Soft natural daylight, gentle shallow depth of field, calm reassuring documentary mood.
Compose the faces and hands in the UPPER-MIDDLE of the frame, fully inside a centered
circular safe zone — keep all four corners empty soft background, since the image will be
masked to a circle. Background falls off into a soft, slightly deeper light-teal/neutral
tone toward the edges. Light, airy, professional color grade harmonizing with teal #1a6b72
and navy #0f1e2e. Absolutely NO text, NO title, NO captions, NO logo, NO watermark,
NO graphic overlays — a clean photograph only. Full-bleed, no borders or frames.
```

### Scaffold B — Single Still-Life / Object (1024 × 1024)
```
Square 1:1 photorealistic still-life for a medical hero image, composed to be cropped into
a CIRCLE. A single clean arrangement of [OBJECT(S): e.g. fresh low-sodium Filipino foods /
a supplement bottle and capsules / a blister pack and water glass / a labeled blood tube /
a blood-pressure cuff] centered on a soft, uncluttered light [teal-tinted / warm neutral]
surface with gentle daylight and shallow depth of field. Keep the hero object within a
centered circular safe zone with empty soft background in the corners (the image is masked
to a circle). Soft edge falloff toward a slightly deeper tone at the rim. Light, calm,
appetizing-but-clinical color grade. Absolutely NO text, labels, packaging copy you can
read, titles, logos, or watermark — a clean photograph only. Full-bleed, no borders.
```

### Scaffold C — Calm 3D Anatomy / Illustration (1024 × 1024)
```
Square 1:1 semi-photorealistic 3D medical illustration for a hero image, composed to be
cropped into a CIRCLE. A single clean render of [ANATOMY: e.g. a pair of human kidneys /
one nephron / a glomerulus / a blood vessel cross-section] floating on a soft, uncluttered
light [teal-tinted / off-white] background, centered in the frame with gentle studio
lighting and soft shadow. Anatomically accurate, restrained clinical color (renal reds,
teal accents), not garish. Keep the structure within a centered circular safe zone, corners
empty soft background (masked to a circle), soft falloff at the rim. Absolutely NO text,
labels, leader lines, callouts, titles, logos, or watermark — clean render only.
Full-bleed, no borders or frames.
```

4. **Output ONE prompt block** in this exact format:

```
FILE NAME: [guide-slug]-hero.png
IMAGE TYPE: Circular vignette hero — [Scaffold A people / B still-life / C anatomy]
ASPECT RATIO: 1:1 (square — displayed circle-cropped)
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: [patients / clinicians / mixed]
VISUAL GOAL: [one sentence — what the picture conveys at a glance]

PROMPT:
[filled-in scaffold, fully expanded with the guide's specifics]

NEGATIVE INSTRUCTIONS:
No text of any kind (no title, subtitle, captions, numbers, labels, logo, or
williamriveromd.com watermark). No rectangular borders, frames, banners, or UI.
No important content in the corners (they get clipped by the circle). No dark, navy,
charcoal, or black background. Avoid cartoon style, clutter, over-saturation, HDR,
distorted hands/faces, implausible anatomy, or stocky staged poses.

QUALITY CHECK:
Square 1:1. Single clear subject centered in the circular safe zone with empty soft
corners. Faces/key detail in the upper-middle (~42% from top). Light, calm, Filipino
clinical context, publication-grade. Crops cleanly to a circle with no text or subject
lost at the edges.
```

---

## TWO-STAGE PIPELINE & PLACEMENT

This skill is **Stage 1** (prompt authoring). To stage the file and folder structure,
hand the prompt to `williamriveromd-local-image-generator` as usual, OR place the final
asset manually:

- Save as `images/<guide-slug>-hero.png` **and** a WebP twin `images/<guide-slug>-hero.webp`.
- The guide's hero already references these via
  `<picture><source srcset="../images/<slug>-hero.webp"><img src="../images/<slug>-hero.png" ...></picture>`
  inside `figure.hero-figure > .hero-vignette`. No markup change is needed when
  regenerating — just replace the image files (keep the same `width`/`height` square
  attributes, e.g. `width="1024" height="1024"`).
- The CSS handles the circle, centering, ring, and edge vignette. If a particular image
  still shows a baked-in title or watermark at the top, add the `zoom` class to that
  guide's `<div class="hero-vignette zoom">` to crop past it (as done for
  epilepsy-seizures-ckd) — but the goal of a regenerated image is that no such crop is
  needed.

## REMINDERS

- One subject per hero. If the topic suggests two scenes, pick the stronger one.
- Square only. Never deliver a landscape banner for a vignette hero.
- The picture carries the mood; the words live in the HTML. Keep the image wordless.
