# Image Prompt Pack — *Diabetes Is Not Always the Diagnosis*

**Guide:** `guides/diabetes-kidney-disease-not-always-diabetic.html`
**Slug:** `diabetes-kidney-disease-not-always-diabetic`
**Produced for:** ChatGPT Image Generator GPT → <https://chatgpt.com/g/g-pmuQfob8d-image-generator>
**Stage 1 authoring skills used:** `williamriveromd-hero-vignette` (IMG‑01), `williamriveromd-infographic-skill` (IMG‑02), `williamriveromd-biomedical-mechanism-figure` (IMG‑03), `williamriveromd-simple-figure` (IMG‑04)

---

## 1 · Architecture rationale (read first)

This guide is **evidence-heavy and number-heavy**. Blueprint §15 is explicit: *"Prefer SVG/code-native diagrams for exact process and quantitative visuals. Use generated raster imagery only for editorial illustration, not for charts or numbers."* So the image plan splits into two tiers:

| Asset | How it's produced | Why |
|---|---|---|
| Three-way diagnostic fork (in body) | **Code-native inline SVG** (already shipped) | Structural, must stay crisp/selectable |
| Caza breakdown **41.2 / 22.9 / 35.9 %** + the **58.8 %** bracket | **Code-native SVG/CSS** (already shipped) | Numbers — never raster (drift + a11y) |
| "Why the biopsy was done" indication bars (n, %, OR) | **Code-native SVG/CSS** (already shipped) | Numbers + selection-bias caption must be live text |
| Evidence timeline 2013 → 2026 | **Code-native SVG/CSS** (already shipped) | Structural, updates when guidance changes |
| Seven mismatch-signal cards / decision framework | **HTML cards** (already shipped) | Live, translatable, keyboard-accessible |
| **Hero vignette** (editorial) | **RASTER — generate (IMG‑01)** | Referenced placeholder; wordless editorial disc |
| **OG / social share card** | **RASTER — generate (IMG‑02)** | Referenced placeholder; needs baked title |
| **Mechanism: diabetes → nephron injury** | **RASTER — generate (IMG‑03)** | Editorial schematic, no numbers → raster-appropriate |
| **Pathology triptych LM / IF / EM** | **RASTER — generate (IMG‑04)** | Educational schematic, no numbers → raster-appropriate |

**Net: generate four raster images (IMG‑01…04).** Everything quantitative is already handled in-page as SVG/CSS and must **not** be re-created as a picture.

### Guardrails baked into every prompt
- **No "58.8 %" in the hero or OG** (blueprint: it would be decontextualized before selection bias is explained).
- **No fabricated pathology micrographs** — the triptych is a *labeled schematic*, not fake histology.
- **No invented numbers** in the mechanism figure; captions note that trajectories vary.
- Light background only; approved sans-serif only (Inter / Nunito Sans / IBM Plex Sans / Manrope); `renalcarematters.com` attribution on every figure that carries chrome (IMG‑02/03/04). The vignette hero (IMG‑01) stays **wordless** — no title, no watermark — because the CSS disc clips it and the HTML `<h1>` sits beside it.

### Placement map
| Image | Section anchor | Role |
|---|---|---|
| IMG‑01 | Hero (`figure.hero-figure > .hero-vignette`) | Circular editorial disc beside the `<h1>` |
| IMG‑02 | `<head>` `og:image` / `twitter:image` | Social share card (1200×630) |
| IMG‑03 | §2 `#mechanism` | Editorial upgrade of the "From diabetes to nephron injury" strip |
| IMG‑04 | §9 `#biopsy-adds` | Editorial upgrade of the LM/IF/EM triptych |

---

## 2 · IMG‑01 — Hero vignette (circular, wordless)

```
FILE NAME: diabetes-kidney-disease-not-always-diabetic-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C anatomy
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F — Anatomy (one large anatomical hero + 2–3 supporting concepts)
CAMERA: three-quarter macro, gentle studio light
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: A single calm idea — a kidney examined closely — signalling that diagnosis in diabetes deserves a second look, without any words.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas,
composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the
canvas diameter with a visible WHITE BORDER around the full circle (the circle
must never touch the canvas edges). Composition archetype: F Anatomy. Camera:
three-quarter macro with soft studio lighting and a gentle soft shadow.

Subject: a single anatomically accurate human kidney rendered in restrained
clinical colour (warm renal red-brown with subtle clinical-teal #1a6b72 rim
light), positioned in the lower-right of the circle, with a clean semi-
transparent magnifying-glass lens hovering over one pole of the kidney so that
the area beneath the lens looks subtly clearer and more detailed than the rest —
the visual metaphor of "look again, look closer." Two very soft, faded kidney
silhouettes sit far back in the blurred background at low opacity to hint that
not every kidney tells the same story, without cluttering the scene. Everything
floats on a soft, uncluttered light teal-tinted #eef6f7 background with gentle
depth of field.

Visual hierarchy: the kidney + magnifier occupy 60–70% of the circle; the two
faint background kidney silhouettes and the lens glow are the 20–30% supporting
context; reserve a clean 20–25% TITLE SAFE ZONE in the upper-left of the circle
as empty soft teal-to-white gradient (no anatomy, lens, leader lines, or
callouts in that zone) so the HTML title can sit beside the disc. Soft edge
falloff toward a slightly deeper neutral at the rim.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark —
clean render only. Full-bleed within the inscribed circle, no rectangular
borders or frames.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of
icons, tiny unreadable labels, infographic clutter, duplicated people, repeated
compositions, cropped circle, cropped objects, cropped anatomy, edge clipping,
objects touching the circular border, important content inside the title safe
zone, baked-in text/titles/captions/logos/watermarks, rectangular borders/frames/
banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-
saturation, distorted or implausible anatomy, fake pathology micrographs.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin —
never cropped. ONE dominant hero subject (kidney + magnifier) at 60–70% of the
circle, 2–3 faint supporting elements, a 20–25% empty title-safe zone reserved
in the upper-left (soft gradient, no anatomy/icons/callouts). Anatomically
plausible kidney, restrained clinical palette on a light teal background. No
text anywhere. Crops cleanly inside the circle with nothing lost at the edges.
```

---

## 3 · IMG‑02 — OG / social share card

```
FILE NAME: diabetes-kidney-disease-not-always-diabetic-og.png
IMAGE TYPE: Photorealistic/vector editorial OG social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: A share card that says diabetes is not the only cause of kidney disease, using a restrained three-way kidney diagnostic fork — no statistics.

PROMPT:
Landscape 1200×630 social share card (OG image) for a nephrology education guide,
clean AJKD/NEJM editorial aesthetic on an OFF-WHITE #fafafa background. Strong
modular hierarchy, generous negative space, mobile-thumbnail-legible.

Left 55% is a TEXT-SAFE ZONE containing, set in bold Inter:
  • a small clinical-teal #1a6b72 eyebrow line: "DIABETES & THE KIDNEY"
  • a large navy #0f1e2e headline (2–3 lines): "When Kidney Disease in Diabetes
    Is Not Diabetic Kidney Disease"
  • a smaller navy/teal subhead: "The clues nephrologists use to decide when the
    kidney story deserves a second look."

Right 45% shows a restrained THREE-WAY DIAGNOSTIC FORK as clean semi-
photorealistic 3D kidney icons on rounded light cards: one kidney labeled with a
tiny renal-green #1f7a4d tag "DN alone", one kidney with a small amber #b8860b
overlay tag "DN + another", and one kidney with a navy #1f3864 tag "another
cause". A soft branching connector (thin navy lines) splits from a single point
into the three cards to read as a fork. Keep the three kidneys visually equal in
weight — none dominant.

Palette: off-white canvas, navy #0f1e2e text, clinical teal #1a6b72 and renal
green #1f7a4d / amber #b8860b / navy #1f3864 accents only. Do NOT display any
percentage, statistic, or the number 58.8. Bottom-right corner: small semi-
transparent navy text "renalcarematters.com" at ~70% opacity, not obscuring
content.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic
stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or
black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter,
Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. Do NOT
render any statistic or percentage (no "58.8%"). Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Off-white background, navy/teal/green/amber accents only.
Headline legible as a small social thumbnail; three equal-weight kidneys in a
clean fork on the right; text-safe left column uncluttered. No statistics shown.
renalcarematters.com visible bottom-right. Approved sans-serif throughout.
```

> **Wiring after generation:** the guide already carries
> `og:image` / `twitter:image` → `…/images/diabetes-kidney-disease-not-always-diabetic-og.png`
> with `og:image:width="1200"` / `og:image:height="630"`. Just drop the PNG at
> `images/<slug>-og.png`. The related-guides thumbnail
> (`images/<slug>-rg-thumb.webp`) is **derived from this OG** via
> `python3 generate_rg_thumbs.py` — no separate prompt needed.

---

## 4 · IMG‑03 — Mechanism: diabetes → nephron injury

```
FILE NAME: diabetes-kidney-disease-not-always-diabetic-01-mechanism.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Show how diabetes injures the nephron in stages, while making clear the trajectory varies — no numbers, no intervention claim.

PROMPT:
Create a publication-grade biomedical mechanism schematic, scientific review-
article style, flat vector illustration with soft semi-3D shading on a WHITE
#ffffff background, clean sans-serif labels set in Inter, thin dashed connector
boxes, muted clinical palette, generous whitespace, 1792×1024.

Topic: How diabetic kidney disease injures the nephron.
Disease context: diabetes mellitus affecting the kidney.

ORGAN-LEVEL PANEL (left): a simplified light gray-blue kidney cross-section
labeled "Diabetic kidney disease", showing cortex, medulla, and a major vessel.
A thin dashed connector box points from the cortex to the magnified panel.

MAGNIFIED MECHANISM PANEL (center, inside a dashed inset): a single nephron
schematic — glomerulus + proximal tubule + loop + collecting segment. Highlight
the affected segments in pale yellow. Concise callouts arranged as five ordered
stages with small arrows:
  1. "Metabolic + hemodynamic stress" (red accent) on the glomerulus
  2. "↑ Glomerular basement membrane thickening + mesangial matrix" 
  3. "Podocyte stress → albumin leak" (arrow into the tubule)
  4. "Tubular protein reabsorption → inflammation + fibrosis signals"
  5. "Glomerulosclerosis + interstitial fibrosis/tubular atrophy → nephron loss"
A small italic note near the inset: "Trajectory varies — some lose function with
little albumin; some albumin regresses with treatment."

BOTTOM SUMMARY FLOW (three boxes, left → right, thin navy arrows):
  • Left pale-pink pathology box: "Injury drivers — hyperglycemia, intraglomerular
    hypertension, oxidative + inflammatory signaling"
  • Center box: "Filtration-barrier + tubulointerstitial injury"
  • Right pale-blue box: "Reduced nephron reserve → progressive CKD (variable pace)"

Do NOT print any numeric thresholds, percentages, eGFR values, or drug names —
this is a mechanism figure, not a treatment or data figure. Bottom-right corner:
small semi-transparent navy text "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text, avoid unrealistic anatomy, avoid photorealism, avoid HDR, avoid
excessive saturation, avoid decorative effects and shadows. NEVER use dark, navy,
charcoal, or black backgrounds — white/light only. Use ONLY Inter, Nunito Sans,
IBM Plex Sans, or Manrope — no serif fonts. Do NOT invent numbers, lab cutoffs,
or drug names. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
1792×1024, white background, muted clinical palette, one organ panel + one dashed
nephron inset + three-box bottom flow. Five ordered stage callouts anatomically
plausible and legible at slide size. "Trajectory varies" note present. No numbers
or drug names anywhere. renalcarematters.com bottom-right. Approved sans-serif.
```

---

## 5 · IMG‑04 — Pathology triptych: LM / IF / EM (labeled schematic)

```
FILE NAME: diabetes-kidney-disease-not-always-diabetic-02-pathology-triptych.png
IMAGE TYPE: Simple figure — three-panel labeled schematic (Scaffold C horizontal)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Explain the three complementary ways a kidney biopsy is read, as a clean educational schematic — not fake histology.

PROMPT:
Clean clinical education infographic, white #ffffff background, 1792×1024. Title
at top center in bold navy #0f1e2e (Inter): "Three views of one biopsy". Subtitle
in clinical teal #1a6b72: "Each answers a different question." Three equal rounded
cards arranged horizontally on a very soft gray #f3f4f6 panel, connected by thin
neutral dividers (a triptych, not a flow).

Card 1 — top accent band clinical teal #1a6b72, small microscope icon, bold label
"Light microscopy (LM)". Simple schematic: a stylized glomerulus + tubules +
vessels drawn as clean vector shapes with a few pale-yellow "scarred" segments.
Caption: "Architecture + how much is already scarred."

Card 2 — top accent band renal green #1f7a4d, small fluorescence icon, bold label
"Immunofluorescence (IF)". Simple schematic: a glomerular loop outline with soft
green glowing deposits along the capillary wall / mesangium. Caption: "Which
immune deposits — antibodies, complement, light chains."

Card 3 — top accent band navy #1f3864, small atom/particle icon, bold label
"Electron microscopy (EM)". Simple schematic: a magnified filtration barrier —
basement membrane band with podocyte foot processes on top and a couple of small
electron-dense deposits. Caption: "Ultrastructure — basement membrane, foot
processes, deposits."

Bottom full-width soft-gray strip, navy text: "Together they confirm diabetic
nephropathy, reveal a superimposed disease, or point to a different diagnosis."
Style everything as clean flat vector schematic — these are teaching diagrams,
NOT real photographic micrographs. Bottom-right corner: small semi-transparent
navy text "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text, avoid realistic/photographic pathology micrographs, avoid HDR,
avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds —
light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif
fonts. Do NOT fabricate real histology images or invent numeric values. Never
omit the renalcarematters.com attribution.

QUALITY CHECK:
1792×1024, white background, three equal cards (LM/IF/EM) with distinct accent
bands, each a clean vector schematic + one-line caption, plus a bottom take-home
strip. Reads as an educational triptych, not fake histology. Labels legible on
mobile. renalcarematters.com bottom-right. Approved sans-serif throughout.
```

---

## 6 · Production checklist (Stage 2)

1. Paste each `PROMPT` block into the Image Generator GPT, one at a time.
2. Save each output to `images/` with the exact `FILE NAME`, and make a **WebP twin** for the two page-embedded assets:
   - `images/diabetes-kidney-disease-not-always-diabetic-vignette-hero.{png,webp}`
   - `images/diabetes-kidney-disease-not-always-diabetic-og.png`
   - `images/diabetes-kidney-disease-not-always-diabetic-01-mechanism.{png,webp}` *(if you swap the CSS mechanism strip for the raster figure)*
   - `images/diabetes-kidney-disease-not-always-diabetic-02-pathology-triptych.{png,webp}` *(if you swap the CSS triptych)*
3. Hero + OG are already referenced in the guide `<head>`/hero — dropping the files in is enough.
4. IMG‑03 / IMG‑04 are **optional editorial upgrades**. If you use them, place each inside the existing `<figure>` (keep the current `<figcaption class="fig-desc">` for the lightbox) and re-run `python3 patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, `patch_image_lightbox.py` for that guide. Do **not** delete the SVG charts (Caza breakdown, indication bars, timeline) — those stay code-native.
5. Regenerate the related-guides thumbnail from the OG: `python3 generate_rg_thumbs.py`.
6. Optional folder-structure/manifest staging: hand this file to the `williamriveromd-local-image-generator` skill (Stage 2).
