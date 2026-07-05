---
name: williamriveromd-local-image-generator
description: >-
  Stage 2 of the WilliamRiveroMD two-stage image pipeline. Consumes the
  image-prompts/ pack produced by any Stage 1 prompt-authoring skill
  (williamriveromd-infographic-skill, williamriveromd-simple-figure, or
  williamriveromd-biomedical-mechanism-figure), validates
  every prompt against the required schema, builds the local guide folder
  structure under /Users/williamgregoryrivero/Downloads/[guide-folder]/,
  writes image-manifest.csv, image-manifest.json, and
  README-image-generation.md, then hands the prompts to the user for
  generation in the ChatGPT Image Generator GPT. Also appends the correct
  og:image / og:image:width / og:image:height / og:image:alt tags to the
  guide HTML once images are confirmed received.
---

# WILLIAMRIVEROMD LOCAL IMAGE GENERATOR — Stage 2

## Role in the pipeline

Stage 1 creates the prompts and saves them into `image-prompts/`. Stage 1 is any
of the prompt-authoring skills:
- `williamriveromd-infographic-skill` — multi-panel posters, heroes, OG cards,
  reference cards, food matrices, workflows
- `williamriveromd-simple-figure` — a single focused figure
- `williamriveromd-biomedical-mechanism-figure` — review-article biomedical
  mechanism schematics (organ-level panel → magnified functional-unit inset →
  injury → intervention → benefit flow)

This skill (Stage 2) operationalizes prompts from **any** of those skills
identically: it does not re-author the prompt, only validates, organizes, and
wires it. When validating, accept the mechanism skill's template fields
(organ-level panel, magnified inset, bottom injury/intervention/benefit flow) as
a complete prompt. Confirm every prompt — regardless of authoring skill — carries
the shared `© williamriveromd.com` attribution before building manifests. Also
confirm every prompt that renders on-image text names an approved sans-serif font
(Inter, Nunito Sans, IBM Plex Sans, or Manrope); flag any text-bearing prompt that
omits the font or specifies a serif/decorative typeface. Text-free photorealistic
prompts (e.g. "no text embedded" heroes) are exempt.

Stage 2 (this skill) operationalizes those prompts locally:
- validates prompt completeness
- builds the local folder structure
- finalizes manifests
- presents prompts to the user for paste-in to the Image Generator GPT
- wires generated images into the guide HTML
- appends OG image tags

The actual image rendering still happens inside the ChatGPT Image Generator
GPT (https://chatgpt.com/g/g-pmuQfob8d-image-generator). This skill does not
call that API directly.

---

## Local base path

/Users/williamgregoryrivero/Downloads

## Standard guide folder structure

```
/Users/williamgregoryrivero/Downloads/[guide-slug]/
├── image-plan/
│   └── visual-strategy.md          ← written by Stage 1
├── image-prompts/
│   ├── 001-[desc].md               ← written by Stage 1
│   ├── 002-[desc].md
│   └── ...
├── generated-images/               ← user saves ChatGPT outputs here
├── image-manifest.csv              ← written/updated by Stage 2
├── image-manifest.json             ← written/updated by Stage 2
└── README-image-generation.md      ← written by Stage 2
```

---

## Required prompt file schema

Every file in `image-prompts/` must contain all of these fields:

```
IMAGE NUMBER:
SECTION PLACEMENT:
FILE NAME:
ARCHETYPE:
AUDIENCE:
ASPECT RATIO:
PIXEL DIMENSIONS:
VISUAL MIX:
- photorealistic models:
- 2D infographic:
- 3D component graphics:
- algorithm/flowchart:
PURPOSE:
KEY CONCEPTS:
COPY-READY IMAGE GENERATOR GPT PROMPT:
NEGATIVE INSTRUCTIONS:
QUALITY CHECK:
ALT TEXT:
OG WIDTH:
OG HEIGHT:
```

Missing fields must be flagged before proceeding.

---

## Archetype → dimension reference

| Archetype                        |    W |    H |
|----------------------------------|-----:|-----:|
| Photorealistic Editorial Hero    | 1792 | 1024 |
| Pathophysiology Mechanism Poster | 1792 | 1024 |
| Dense Mechanism Poster           | 1536 | 1152 |
| Clinical Algorithm               | 1024 | 1536 |
| Long Clinical Algorithm          | 1024 | 1792 |
| Wide Clinical Algorithm          | 1536 | 1152 |
| Multi-panel Educational          | 1792 | 1024 |
| Clinician Reference Card         | 1024 | 1536 |
| Compact Reference Card           | 1536 | 1152 |
| Food Matrix                      | 1536 | 1152 |
| Case Snapshot                    | 1792 | 1024 |
| Circular Workflow                | 1024 | 1024 |
| Access / Procedural Education    | 1792 | 1024 |

---

## Stage 2 execution steps

1. **Scan** `image-prompts/` for all `.md` files.
2. **Validate** each file has all required schema fields. Report missing fields.
3. **Create folders** `generated-images/` if absent.
4. **Write / update** `image-manifest.csv` and `image-manifest.json` from
   prompt file data. Template files are in `examples/`.
5. **Write** `README-image-generation.md` listing every prompt with:
   - numbered filename
   - archetype
   - pixel dimensions
   - paste URL: https://chatgpt.com/g/g-pmuQfob8d-image-generator
   - save destination: `generated-images/[filename]`
6. **Present** each prompt to the user one at a time (or as a batch if
   requested), clearly labelled with image number and file name.
7. **After** the user uploads generated images to this thread:
   - rename to convention: `[guide-slug]-[desc]-infographic.png/.webp`
     (heroes: `[guide-slug]-hero-[desc].png/.webp`)
   - place both `.png` and `.webp` in `images/` in the repo
   - wire `<img>` into the guide using the site frame pattern (see below)
   - append OG image tags to the guide `<head>` (see below)
   - commit and push to `main`

---

## Site frame pattern for inserting images

Patient / general section:
```html
<div class="illus-wrap illus-wrap-light">
  <picture>
    <source srcset="/images/[filename].webp" type="image/webp">
    <img src="/images/[filename].png" alt="[alt text]" loading="lazy" width="[W]" height="[H]">
  </picture>
</div>
```

Clinician section or figure with caption:
```html
<figure>
  <picture>
    <source srcset="/images/[filename].webp" type="image/webp">
    <img src="/images/[filename].png" alt="[alt text]" loading="lazy" width="[W]" height="[H]">
  </picture>
</figure>
```

---

## OG image tag block (new guides)

Append immediately after the existing `og:description` meta tag in `<head>`.
Use the PRIMARY image (first image / hero) for the guide.

```html
<meta property="og:image"        content="https://renalcarematters.com/images/[filename].webp"/>
<meta property="og:image:width"  content="[OG WIDTH from prompt file]"/>
<meta property="og:image:height" content="[OG HEIGHT from prompt file]"/>
<meta property="og:image:alt"    content="[Guide title] — williamriveromd.com"/>
```

Dimensions come from the `OG WIDTH` / `OG HEIGHT` fields in the prompt file,
which in turn come from the archetype dimension table above.

### Canonical OG / social share image size

**1200 × 630 px (1.91:1 ratio)** is the correct size for any image intended
as an Open Graph / social share card.

- Facebook treats anything ≥ 600 px wide at 1.91:1 as a "large" link preview
- 1200 × 630 is the retina sweet spot — sharp without being downscaled oddly
- Always declare `og:image:width` and `og:image:height` explicitly so the
  scraper does not have to guess dimensions
- Square (1:1) images work for Instagram-first assets but will be letterboxed
  on Facebook/X link previews — prefer 1200 × 630 for guide OG images
- Guide hero images used **inline on the page** can be any archetype dimension;
  the **OG image** should be a separate 1200 × 630 card when social sharing
  is a priority

---

## Naming convention

- General images: `[guide-slug]-[desc]-infographic.png` + `.webp`
- Hero images:    `[guide-slug]-hero-[desc].png` + `.webp`
- Always ship both `.png` and `.webp` as a pair.
- Prompt files:   `NNN-[desc].md` (zero-padded three-digit number)

---

## Hard rules inherited from pipeline

- NEVER put journal/guideline/brand names (AJKD, NEJM, KDIGO, Harrison's)
  in a prompt. End every prompt with:
  "No journal names, guideline acronyms, brand names, or watermarks."
- Clinician algorithms use the conservative flat-flowchart style:
  white background, boxes, diamond decisions, minimal color, no 3D/icons.
- All on-image typography uses one of the four approved sans-serif fonts only —
  Inter, Nunito Sans, IBM Plex Sans, or Manrope. No serif or decorative fonts.
- OG image always points to the `.webp` version of the primary image.
- Commit directly to `main`. No PRs.
