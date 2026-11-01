# hd-volume-bp-tolerance-clinician — image plan

Guide: `guides/hd-volume-bp-tolerance-clinician.html` (clinician-only, single-mode).

## Status of assets

| File | Status | Source |
|---|---|---|
| `images/hd-volume-bp-tolerance-clinician-01-compartments.svg` | Final | Hand-authored vector figure (accurate labels, light background, © renalcarematters.com) |
| `images/hd-volume-bp-tolerance-clinician-02-review-matrix.svg` | Final | Hand-authored vector figure |
| `images/hd-volume-bp-tolerance-clinician-03-evidence-ladder.svg` | Final | Hand-authored vector figure |
| `images/hd-volume-bp-tolerance-clinician-vignette-hero.{png,webp}` | **Interim** — replace | Flat vector placeholder rendered from SVG so the hero is never broken |
| `images/hd-volume-bp-tolerance-clinician-og.{png,webp}` | **Interim** — replace if desired | HTML-rendered 1200×630 card using the interim hero |

The three in-body figures were drawn as SVG on purpose: they carry precise clinical labels (UF, RBV, refill determinants, the 3×3 review grid, evidence rungs) that image generators tend to garble. Keep them as SVG.

When the final hero is generated, also update the hero `<img alt>` in the guide to describe the new picture, and regenerate the OG card (prompt 2) and `images/hd-volume-bp-tolerance-clinician-rg-thumb.webp` (`python3 generate_rg_thumbs.py --guide hd-volume-bp-tolerance-clinician.html --force`).

---

## Prompt 1 — Circular vignette hero (williamriveromd-hero-vignette v3)

```
FILE NAME: hd-volume-bp-tolerance-clinician-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C anatomy
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F — Anatomy
CAMERA: macro cross-section, slightly elevated three-quarter view
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: clinicians
VISUAL GOAL: At a glance, fluid moving from waterlogged tissue back into a single blood capillary — the plasma-refill idea at the heart of "congested but hypotensive."

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Anatomy. Camera: macro cross-section, slightly elevated three-quarter view.

Subject: a single clean render of one gently curving blood capillary crossing the lower-middle of the circle from left to right, its wall semi-translucent so a few biconcave red blood cells are visible inside. Below and around the vessel, a soft, slightly swollen interstitial tissue bed of rounded pale-pink cells with glistening fluid between them. Small, clear, teal-tinted fluid droplets drift upward from the tissue spaces through the capillary wall into the bloodstream, suggesting plasma refill. Anatomically plausible proportions, restrained clinical colors (muted renal reds, soft pinks, clinical teal #1a6b72 accents), gentle studio lighting with soft shadows, shallow depth of field.

Visual hierarchy: the capillary and the refilling droplets occupy 60–70% of the circle; the tissue bed provides 20–30% supporting context; reserve the upper 20–25% of the circle as a TITLE SAFE ZONE of empty, softly graded very light teal-white background (#eef6f7 fading to off-white) with no anatomy, droplets, leader lines, labels or callouts inside it. Soft falloff toward a slightly deeper neutral at the rim.

Absolutely NO text, labels, arrows with words, leader lines, callouts, titles, logos or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted anatomy, gore.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant subject (capillary + refill) occupying 60–70% of the circle, 2–4 supporting elements, 20–25% empty title-safe zone at the top. No people. Crops cleanly inside the circle with nothing lost at the edges. No text anywhere.
```

---

## Prompt 2 — OG / social share card (williamriveromd-infographic-skill)

```
FILE NAME: hd-volume-bp-tolerance-clinician-og.png
IMAGE TYPE: Photorealistic editorial hero — OG social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: clinicians (nephrologists, dialysis nurses, renal pharmacists, dietitians)
VISUAL GOAL: A calm, premium share card that says "volume vs tolerance in hemodialysis — clinician guide."

PROMPT:
Clean 1200×630 social share card on a pure white (#ffffff) background. Left 60%: typography in Inter. Small uppercase teal (#1a6b72) kicker "CLINICIAN GUIDE · MAINTENANCE HD". Large bold navy (#0f1e2e) title on three lines: "Volume, Blood Pressure &" then, in teal (#1a6b72), "Hemodynamic Tolerance". Below, one line of navy body text: "Congested, hypotensive — or both?" A thin navy (#1f3864) vertical accent bar on the far left edge. Right 40%: a circular disc containing the semi-photorealistic capillary-and-tissue refill render from the hero (blood capillary crossing the disc, pale tissue cells below, teal-tinted droplets rising into the vessel), on a very light teal (#eef6f7) background, with soft shadow, fully inside the card. Generous whitespace, no clutter, no other icons. Copyright attribution "renalcarematters.com" in small navy text at 70% opacity in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter — no serif, decorative or handwritten typefaces. Never omit the renalcarematters.com attribution. Spell every word exactly as given.

QUALITY CHECK:
Exactly 1200 × 630. White background. Title legible at thumbnail size. Attribution renalcarematters.com visible bottom-right. American English spelling ("Hemodynamic").
```
