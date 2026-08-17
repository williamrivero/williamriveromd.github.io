---
name: williamriveromd-organ-crosstalk-sigil-graphic
description: >-
  Generate clean, minimal medical "organ sigil" image prompts for
  renalcarematters.com nephrology patient-education guides — simple line-art organ
  icons connected by dotted arrows or flow lines to show organ crosstalk,
  physiology, feedback loops, or systemic relationships (e.g. neuro-renal,
  cardiorenal, gut-kidney, hepatorenal, muscle-kidney axes). Use when the user
  wants a symbolic, monoline "sigil"-style crosstalk diagram rather than a
  detailed infographic, photorealistic hero, algorithm flowchart, or
  review-article mechanism schematic. Outputs a single copy-paste ChatGPT Image
  Generator prompt in the renalcarematters.com house style.
---

# williamriveromd-organ-crosstalk-sigil-graphic

## Purpose
Generate clean, minimal, medical "organ sigil" image prompts: simple line-art organ icons connected by dotted arrows or flow lines to show organ crosstalk, physiology, feedback loops, or systemic relationships.

Use this skill when the request is a **symbolic monoline crosstalk diagram** — two or
more simplified organ icons linked by dotted loop arrows. For a detailed multi-panel
poster use `williamriveromd-infographic-skill`; for a decision flowchart use
`williamriveromd-algorithm-generator-skill` or `williamriveromd-simple-figure`; for an
organ→inset→injury/intervention/benefit review-article schematic use
`williamriveromd-biomedical-mechanism-figure`.

## Visual Style
- Minimal medical line-art illustration
- White or transparent background
- Thin clean monoline strokes
- Soft clinical palette: teal, cyan, slate, muted blue, pale gray
- Rounded organic line quality
- Light paper/grid texture optional
- No photorealism
- No complex anatomy
- No 3D rendering
- No clutter
- No heavy shadows
- No labels unless requested

## Typography (when labels ARE requested)
- **Approved fonts (MANDATORY): use only a clean sans-serif typeface — Inter,
  Nunito Sans, IBM Plex Sans, or Manrope. No other fonts, and never a serif font.**
  Name the chosen font explicitly in the generated prompt whenever any text label
  appears. The sigil default is label-free; this rule applies the moment a label,
  caption, or organ name is added.

## Attribution (MANDATORY, house convention)
Even though the sigil is otherwise label-free, every generated image must carry the
shared renalcarematters.com mark:
- Text: `renalcarematters.com`
- Placement: bottom-right corner (square/landscape); bottom-center (portrait)
- Style: small, semi-transparent navy or dark-teal text, ~10–11px, ~70% opacity
- Never omit. Never obscure the sigil. This is the only mark permitted — no other
  watermarks.

## Core Composition
Create a central "sigil-like" diagram using:
1. Two or more simplified organ icons
2. Dotted curved arrows or circular flow paths
3. Balanced vertical or radial symmetry
4. Generous whitespace
5. A calm clinical educational tone

## Prompt Template

Create a simple medical organ-crosstalk sigil illustration featuring:

ORGANS:
- [organ 1]
- [organ 2]
- [organ 3, optional]

RELATIONSHIP:
Show [physiologic relationship / feedback loop / disease pathway] using dotted curved arrows or subtle flow lines.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette, white background, clean rounded organ shapes, balanced sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels unless specified. If any label is included, set all type in a clean sans-serif font — Inter, Nunito Sans, IBM Plex Sans, or Manrope only (never a serif font).

COMPOSITION:
Place [primary organ] at the top/center and [secondary organ/s] below or around it. Connect them with dotted arrows forming a gentle circular or bidirectional loop. Keep the design simple, symbolic, and suitable for a patient-education medical website.

OUTPUT:
Square or vertical image, clean margins, high-resolution, publication-grade medical icon aesthetic. Include a small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner (bottom-center for portrait), not obscuring the sigil.

## Example Prompt

Create a simple medical organ-crosstalk sigil illustration featuring the brain and kidneys.

Show brain–kidney communication using subtle dotted curved arrows flowing downward from the brain to both kidneys and returning upward in a soft circular loop.

Minimal clinical line-art, thin monoline strokes, soft teal-blue palette, white background, clean rounded organ shapes, balanced sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels.

Place the brain at the top center and the two kidneys symmetrically below. Connect them with dotted arrows forming a calm bidirectional loop. The image should feel like a symbolic medical sigil for neuro-renal crosstalk, suitable for a patient-education nephrology website. Add a small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner.

## Variants

### Heart–Kidney Sigil
Use heart at top, kidneys below. Dotted loop arrows showing cardiorenal crosstalk.

### Gut–Kidney Sigil
Use intestine at top or center, kidneys below. Dotted arrows showing gut microbiome–kidney axis.

### Liver–Kidney Sigil
Use liver above, kidneys below. Flow lines showing hepatorenal physiology.

### Muscle–Kidney Sigil
Use skeletal muscle icon and kidneys connected by dotted metabolic arrows.

### Brain–Gut–Kidney Sigil
Triangular composition with brain top, gut lower left, kidney lower right, circular dotted arrows.

## Negative Prompt
Avoid: photorealistic anatomy, surgical detail, excessive labels, dark background, neon colors, complex infographics, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic lighting, stock-photo style. If text is present, never use serif or decorative fonts — Inter, Nunito Sans, IBM Plex Sans, or Manrope only. Never omit the renalcarematters.com attribution.
