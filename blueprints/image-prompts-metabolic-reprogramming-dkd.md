# Image prompt pack — Metabolic Reprogramming in Diabetic Kidney Disease

**Guide:** `guides/metabolic-reprogramming-dkd.html`
**Status:** In-body figures 01–07 are already shipped as original code-native SVGs (`images/metabolic-reprogramming-dkd-0N-*.svg`), so the page is complete without generated art. This pack covers the two raster assets the page still references (hero vignette, OG card) plus two optional mechanism-figure upgrades.
**House rules:** American English in any rendered text. Public-site attribution `© renalcarematters.com` (never on the vignette hero, which must be wordless). Palette NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280.
**Pipeline:** Stage 1 prompts below → Stage 2 `williamriveromd-local-image-generator` (manifest, folders) → generate in ChatGPT Image Generator → save PNG + WebP twins to `images/`.

---

## 1. Hero vignette (required — currently 404)

```
FILE NAME: metabolic-reprogramming-dkd-vignette-hero.png  (+ .webp twin)
IMAGE TYPE: Circular vignette hero v3 — Scaffold C anatomy
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: Macro three-quarter view, slightly from above
HUMAN VARIATION (vs. previous guide): no people (previous inflammation-in-dialysis hero was an object/alarm illustration; this one is a cellular anatomy render)
AUDIENCE: mixed (patients and clinicians)
VISUAL GOAL: One kidney tubule cell whose healthy mitochondria glow like a clean engine while a few rust-colored patches creep along its outer membrane — fuel and "rust" in one glance.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas,
composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the
canvas diameter with a visible WHITE BORDER around the full circle (the circle
must never touch the canvas edges). Composition archetype: I Object Hero.
Camera: macro three-quarter view from slightly above.

Subject: a single cuboidal proximal tubule epithelial cell, cut away on one side
to reveal its interior, resting on a soft, uncluttered light teal-tinted
background. Inside, elongated mitochondria with visible cristae glow a warm amber,
suggesting clean fuel burning; a few small pale-yellow lipid droplets sit near
them. The apical brush border (fine microvilli) faces upper left. Along the
lower-right curve of the outer cell membrane, three or four small, irregular
rust-orange patches spread like early corrosion on metal, subtle and not gory.
Restrained clinical color: renal pinks and soft ivory cytoplasm, teal accents
(#1A6B72), amber mitochondria, rust patches in muted orange (#C55A11).
Gentle studio lighting with a soft shadow beneath the cell.

Visual hierarchy: the cell occupies 60–70% of the circle, centered slightly
right and low; 2–3 supporting cues (a faint capillary edge behind, a few floating
fatty-acid droplets entering from the left) occupy 20–30%; reserve a 20–25%
TITLE SAFE ZONE of empty soft teal gradient in the upper-left of the circle with
no anatomy, droplets, labels or callouts. Soft falloff toward a slightly deeper
neutral at the rim.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark —
clean render only. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
busy layouts; collage overload; more than four supporting elements; dozens of icons;
tiny unreadable labels; infographic clutter; cropped circle; cropped cell; edge
clipping; objects touching the circular border; important content inside the title
safe zone; baked-in text, titles, captions, logos, watermarks; rectangular borders,
frames, banners; dark, charcoal or black backgrounds; cartoon style, neon, HDR,
over-saturation; blood, gore, or a "dying cell" horror look; implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin —
never cropped. One dominant cell occupying 60–70% of the circle, 2–3 supporting
cues, 20–25% empty title-safe zone at upper left. Mitochondria read as "clean
engine," membrane patches read as "early rust," not as infection or blood.
Wordless. Crops cleanly inside the circle.
```

Placement: already wired in the hero as `../images/metabolic-reprogramming-dkd-vignette-hero.{webp,png}` with `width="2048" height="2048"`.

---

## 2. OG / social share card (required for link previews)

```
FILE NAME: metabolic-reprogramming-dkd-og.png  (+ .webp twin)
IMAGE TYPE: Editorial OG card (williamriveromd-infographic-skill style)
PIXEL DIMENSIONS: 1200 × 630 (1.91:1)

PROMPT:
A clean editorial social-share card, 1200×630, light ivory background with a soft
teal (#1A6B72) gradient band along the left 40%. Left side, large clean sans-serif
type in Inter, navy (#1F3864):
  Line 1 (bold, 54 px): "Metabolic Reprogramming in DKD"
  Line 2 (medium, 30 px, orange #C55A11): "From Fuel Selection to Ferroptosis"
  Line 3 (regular, 20 px, navy at 80%): "What the science shows — and what changes treatment"
Right side: a semi-photorealistic 3D cutaway of a single kidney tubule cell with
amber-glowing mitochondria and two or three small rust-orange patches on its outer
membrane, matching the hero vignette, floating on soft light. Bottom-right corner:
small semi-transparent navy text "© renalcarematters.com". Generous whitespace,
no other logos, no extra text, no dark background. All text spelled exactly as
given, American English.
```

After generation: confirm the existing `og:image` (webp), `og:image:width/height/alt`, and `twitter:image` (png) tags in the guide head already point to these filenames.

---

## 3. Optional upgrade — ferroptosis mechanism (replaces SVG 03 only if preferred)

Use `williamriveromd-biomedical-mechanism-figure`. Keep the shipped SVG unless the generated version is clearly better and text-accurate.

```
FILE NAME: metabolic-reprogramming-dkd-08-ferroptosis-mechanism.png (+ .webp)
ASPECT RATIO: 16:9 (1920 × 1080)
FONT: Inter (labels), sans-serif only

Create a publication-grade biomedical mechanism schematic.
Topic: Ferroptosis in the diabetic proximal tubule.
Disease context: diabetic kidney disease (experimental evidence).
Left panel (organ level): simplified kidney cross-section labeled "Diabetic kidney
disease", with a small dashed connector box pointing to a magnified proximal tubule
segment highlighted in soft yellow.
Center/right magnified panel (dashed border): one proximal tubule cell with:
  - membrane phospholipids containing PUFA chains; callout "ACSL4 / LPCAT3 → PUFA-PL"
  - red spark icons at the membrane labeled "Fe²⁺ + radicals → PL-OOH"
  - mitochondria with label "↑ ROS"
  - a blue defense track at the base: "SLC7A11 (cystine in) → GSH → GPX4 → PL-OH"
  - a parallel dashed blue track: "FSP1–CoQ"
Bottom summary flow:
  Left pale-pink box: "Substrate overload · ↑ ROS · impaired autophagy / ↓ AMPK · TGF-β1"
  Center box: "Phospholipid peroxidation exceeds repair"
  Right pale-blue box: "Membrane failure → tubular cell death (experimental models)"
Small grey footnote under the flow: "Mechanism from animal and cell studies; not a
validated clinical test." Bottom-right: small semi-transparent navy
"© renalcarematters.com". White background, muted clinical colors, thin dashed
connectors, no photorealism, no dark background, no extra text.
```

Required figcaption if placed: `.fig-desc` plus `dl.fig-abbrevs` for ACSL4, AMPK, CoQ, FSP1, GPX4, GSH, LPCAT3, PL-OH, PL-OOH, PUFA, ROS, SLC7A11, TGF-β1.

---

## 4. Optional upgrade — fuel switch overview (supplements SVG 02)

```
FILE NAME: metabolic-reprogramming-dkd-09-fuel-switch.png (+ .webp)
ASPECT RATIO: 16:9 (1920 × 1080)
FONT: Inter

Biomedical mechanism schematic. Topic: proximal tubule fuel use in diabetes.
Left panel: healthy proximal tubule cell — fatty acids entering via CPT1 into
mitochondria, "β-oxidation → TCA → OXPHOS → ATP", Na⁺/K⁺-ATPase at the basolateral
membrane, SGLT2 on the apical side moving glucose (label: "transport, not burning").
Right panel (dashed border): diabetic proximal tubule cell — more glucose and Na⁺
arriving (thicker arrows), lipid droplets accumulating, labels "↓ FAO genes (human
fibrosis)", "↑ glycolytic activity", "mitochondrial stress", "↑ mTORC1, ↓ AMPK".
A purple dashed box between panels: "States overlap — not a fixed timeline".
Bottom flow: pink "Substrate pressure + lost flexibility" → center "SGLT2 inhibition
lowers transport work (proposed metabolic effects)" → blue "Outcome benefit proven in
trials; metabolic mediators unproven". Bottom-right "© renalcarematters.com".
White background, muted colors, no dark background, no extra text.
```
