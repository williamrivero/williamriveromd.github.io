# Image plan — `guides/personal-medical-journal-health-history.html`

The guide deliberately renders its explanatory visuals as HTML/CSS components rather
than raster art (the four-record cards, the weak-vs-useful comparison cards, the
source-certainty badges, and the digital folder map), matching the blueprint's own
asset plan — "HTML badges, not image text". Only two raster assets are required.

| # | File | Status |
|---|---|---|
| 1 | `images/personal-medical-journal-health-history-vignette-hero.png` + `.webp` | **Required — currently 404** |
| 2 | `images/personal-medical-journal-health-history-og.png` (1200×630) | **Required for social preview** |

---

## 1 — Circular vignette hero

```
FILE NAME: personal-medical-journal-health-history-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: overhead / top-down, slight tilt
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: patients and caregivers
VISUAL GOAL: scattered medical paperwork resolving into one calm, ordered set of records.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE
BORDER around the full circle (the circle must never touch the canvas edges).
Composition archetype: I Object Hero. Camera: overhead top-down with a slight tilt.

Subject: a single clean arrangement on a soft, uncluttered light warm-neutral wooden
table — a slim kraft document folder lying open with a neat stack of crisp white pages
squared inside it, a simple spiral notebook opened to a blank ruled page with a plain
ballpoint pen resting in the gutter, one blister strip of unbranded white tablets and a
small amber pill bottle with a blank label, and a home blood-pressure cuff coiled tidily
at the lower edge. Around the upper-left of the arrangement, three or four loose sheets
lie slightly askew and overlapping, as if just gathered — the visual contrast between
scattered paper and the squared stack is the whole idea. Soft natural daylight from the
upper left, gentle shallow depth of field, a soft shadow under the folder.

Visual hierarchy: the open folder with its squared stack is the hero object at 60–70% of
the circle; the notebook, medicines, cuff, and loose sheets together occupy 20–30%;
reserve a 20–25% TITLE SAFE ZONE of empty table surface in the upper-right quadrant
(no objects, papers, labels, or icons inside that zone). Soft edge falloff toward a
slightly deeper neutral at the rim. Light, calm, orderly, reassuring colour grade
harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background.

Absolutely NO readable text or labels on any paper, packaging, or pill bottle — the
sheets must read as blank or as illegible grey line-texture. No titles, no logos, no
watermark. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid: busy layouts; collage overload; more than four supporting scenes; dozens of icons;
tiny unreadable labels; infographic clutter; duplicated people; repeated compositions;
cropped circle; cropped objects; cropped anatomy; edge clipping; objects touching the
circular border; important content inside the title safe zone; baked-in text, titles,
captions, logos, watermarks; rectangular borders, frames, banners; dark / charcoal /
black backgrounds; cartoon style, neon, HDR, over-saturation; distorted hands or faces,
implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never
cropped. ONE dominant hero object (the open folder and its squared stack) at 60–70% of
the circle, 2–4 supporting elements, 20–25% empty title-safe zone reserved in the
upper-right (bare table surface only). No legible text anywhere. Crops cleanly inside
the circle with nothing lost at the edges.
```

Save the result as both `images/personal-medical-journal-health-history-vignette-hero.png`
and a WebP twin `…-vignette-hero.webp`. The guide's `<picture>` already points at both,
with `width="2048" height="2048"`.

---

## 2 — Open Graph share card (1200 × 630)

The head already declares `og:image`, `og:image:width`, `og:image:height`, and
`og:image:alt`. Generate with the `williamriveromd-infographic-skill` OG-card scaffold
using this brief:

> Landscape 1200×630 editorial share card. Left two-thirds: the same overhead still-life
> language as the hero — loose medical papers on the left resolving into one squared,
> ordered stack in an open folder on the right, on a light warm-neutral surface, soft
> daylight. Right third: clean negative space over a soft teal-to-white gradient for the
> title lockup. Palette: clinical teal `#1a6b72`, navy `#0f1e2e`, warm neutrals.
> No baked-in body copy; title text is added in the card template, not generated.

Alt text already set in the guide:
*"Scattered laboratory slips, prescriptions and hospital papers resolving into one clear
medical summary, timeline and folder."*
