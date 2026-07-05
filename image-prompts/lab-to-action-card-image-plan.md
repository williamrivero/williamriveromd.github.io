# Image Plan — The Lab-to-Action Card
`guides/lab-to-action-card.html` · companion PDF: `downloads/wgmr-lab-to-action-guide.pdf`

Two images are needed. This guide currently ships with **no hero image** (it
was built with a text-only hero) and its `og:image` is a borrowed stopgap from
`understanding-lab-results.html`. Both prompts below are copy-paste ready for
the ChatGPT Image Generator GPT
(https://chatgpt.com/g/g-pmuQfob8d-image-generator). No images are needed
inside the companion PDF itself — it is a typography/table document with no
photographic figures.

After generating both PNGs, hand them to `williamriveromd-local-image-generator`
(or place manually per the instructions at the end of this file) and:
1. Add `single-mode` to `guides/lab-to-action-card.html`'s `<body>` class.
2. Wrap the vignette in `<figure class="hero-figure"><div class="hero-vignette">…</div></figure>`
   inside `.hero-grid`, right after `.hero-copy`.
3. Run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, and
   `patch_hero_maxwidth.py --guide lab-to-action-card.html` once the real hero
   `<img>` exists (running them today mis-targets the small doctor avatar —
   already reverted once in this guide; don't re-run until the hero image is in place).
4. Replace the `og:image` / `twitter:image` meta tags (currently pointing at
   `../images/labs-report-trends.png`) with the new OG card, and add
   `og:image:width="1200"` / `og:image:height="630"` / `og:image:alt`.

---

## 1 · Hero — Circular Vignette

FILE NAME: `lab-to-action-card-vignette-hero.png`
IMAGE TYPE: Circular vignette hero v3 — Scaffold A (Clinical People)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling (one cohesive scene, no floating panels)
CAMERA: Over-the-shoulder, looking down and across at the lab report and the patient's hands
HUMAN VARIATION (vs. previous guides): woman (not man), late-20s/early-30s (not elderly), rounder soft face shape, shoulder-length loose wavy hair worn down, warm medium-tan Filipino skin tone, soft yellow linen blouse (not teal polo/beige blouse), seated at a round rattan-and-glass table (not a wooden dining table), morning kitchen-nook setting (not a clinic or dining room), phone held in one hand hovering above the page rather than resting on the table, calm focused/thoughtful expression (not smiling), one hand resting flat on the paper, potted pothos plant softly blurred in the background, over-the-shoulder camera framing (not a frontal or three-quarter portrait)
AUDIENCE: patients and families
VISUAL GOAL: A calm, ordinary person quietly reading her own lab report at home and about to decide what to do next — the everyday moment this card exists to guide.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed
to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas
diameter with a visible WHITE BORDER around the full circle (the circle must
never touch the canvas edges). Composition archetype: J, Environmental
Storytelling — one cohesive scene, no floating panels or callouts. Camera:
over-the-shoulder, looking down and across at a printed lab report and the
subject's hands.

Subject: a Filipino woman in her late twenties or early thirties, rounder soft
face shape, warm medium-tan skin tone, shoulder-length loose wavy dark hair
worn down, wearing a soft yellow linen blouse, seated at a round rattan-and-glass
table in a bright kitchen nook at home. She is looking down at a printed lab
report resting on the table, one hand flat on the page, the other hand holding
a smartphone lifted just above it as if about to make a call. Her expression is
calm and thoughtful, not smiling — a quiet, ordinary moment of taking her own
health seriously. Soft morning daylight from a nearby window, a blurred potted
pothos plant in the background, gentle shallow depth of field.

Visual hierarchy: hero subject and lab report occupy 60–70% of the circle;
2–4 supporting context elements (phone, plant, warm tabletop light) 20–30%;
reserve a 20–25% TITLE SAFE ZONE of soft gradient / clean wall / open window
light in the upper portion of the circle (no faces, hands, paper, or objects
inside that zone) so the HTML title can sit beside the disc without covering
important artwork.

Calm, reassuring, documentary-realistic colour grade harmonizing with clinical
teal #1a6b72 and navy #0f1e2e worked subtly into the tabletop and background
tones, on an otherwise warm, bright, naturally lit home setting. Edge falloff
toward a slightly deeper neutral at the rim. Full-bleed within the inscribed
circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or
williamriveromd.com watermark. The lab report page itself should read as a
generic printed page with faint unreadable table lines — do not render legible
words, numbers, or a real lab-report layout on it.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens
of icons, tiny unreadable labels, infographic clutter, duplicated people,
repeated compositions, cropped circle, cropped objects, cropped anatomy, edge
clipping, objects touching the circular border, important content inside the
title safe zone, baked-in text, titles, captions, logos, watermarks,
rectangular borders, frames, banners, dark/charcoal/black backgrounds, cartoon
style, neon, HDR, over-saturation, distorted hands or faces, implausible
anatomy, legible text on the lab report prop.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin —
never cropped. ONE dominant hero subject (woman + report) occupying 60–70% of
the circle, 2–4 supporting elements, 20–25% empty title-safe zone reserved
(soft window light / clean wall — no faces, hands, paper, or objects inside).
Filipino home context, ≥12 traits visibly different from prior guides (sex,
age, face shape, hairstyle, clothing, setting, table type, camera framing,
prop interaction, expression, background object, lighting source, hand
position). Camera framing (over-the-shoulder) not repeated from the previous
guide. Crops cleanly inside the circle with no subject lost at the edges.

---

## 2 · OG / Social Share Card

FILE NAME: `lab-to-action-card-og.png`
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: patients and families (also the preview shown when clinicians share the link)
VISUAL GOAL: At thumbnail size on a social feed, instantly communicate "find your lab number, read the color, know what to do" — readable even at 300px wide.

PROMPT:
Clean 1200×630 OG social-share card, white background (#ffffff), premium
nephrology-education editorial design system for williamriveromd.com. Use only
the sans-serif font Inter for all typography — no other fonts, no serif fonts.

Layout: left 60% of the canvas holds text — a small teal (#1a6b72) uppercase
eyebrow label reading "PATIENT QUICK-REFERENCE," then a large bold navy
(#0f1e2e) headline in Inter set across two lines: "The Lab-to-Action Card,"
then a smaller navy/gray subtitle line below it: "Find your number. Read the
color. Know what to do." Right 40% of the canvas holds a simple, clean
flat-vector illustration of a rounded rectangular card/document shape, split
into three small horizontal bands colored clinical red (#b91c1c), amber
(#b8860b), and renal green (#1f7a4d) from top to bottom, each band paired with
a tiny simple rounded icon (a small circle, a small triangle, a small check —
abstract, not text) — representing red/amber/green triage at a glance, with
generous white space around it, no readable numbers or words on the card
illustration itself.

Background: white or very soft off-white (#fafafa), with a subtle very light
teal-tinted (#eef6f7) rounded panel behind the illustration on the right for
gentle visual separation. Rounded corners on all card/panel shapes. Clean,
calm, high contrast, mobile-thumbnail legible — the headline and eyebrow label
must remain crisp and readable even scaled down to roughly 300px wide.

Small semi-transparent (70% opacity) navy or dark teal attribution text
reading exactly "williamriveromd.com" in the bottom-right corner, small and
unobtrusive, not overlapping any other element.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text anywhere in the image (only the specified headline/eyebrow/
subtitle text should render, and it must be spelled exactly as given), avoid
unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look,
avoid excessive saturation. NEVER use dark, navy, charcoal, or black
backgrounds — light backgrounds only. Use ONLY Inter for all on-image text —
no other fonts, no serif fonts, no decorative or handwritten typefaces. Never
omit the williamriveromd.com attribution. Do not render any lab values,
numbers, or real medical text on the card illustration.

QUALITY CHECK:
Exactly 1200×630. Background white/off-white, never dark. Headline "The
Lab-to-Action Card" and eyebrow "PATIENT QUICK-REFERENCE" both legible and
correctly spelled in Inter. Red/amber/green triage motif reads clearly even at
thumbnail size. williamriveromd.com attribution visible bottom-right. No
clutter, no fabricated micro-text, no dark background.

---

## After generation — wiring checklist

- [ ] Save both files as `.png` in `images/`; also export a `.webp` twin of the
      hero (`lab-to-action-card-vignette-hero.webp`) for the `<picture><source>`.
- [ ] Add `single-mode` to `<body class="physician-mode single-mode">` →
      actually this guide has no physician mode, so just `<body class="single-mode">`.
- [ ] Insert the hero figure into `.hero-grid`, immediately after `.hero-copy`:
  ```html
  <figure class="hero-figure">
    <div class="hero-vignette">
      <picture>
        <source srcset="../images/lab-to-action-card-vignette-hero.webp" type="image/webp">
        <img src="../images/lab-to-action-card-vignette-hero.png"
             alt="A woman reviewing her printed lab report at home, phone in hand, deciding what to do next."
             width="2048" height="2048" fetchpriority="high" loading="eager" decoding="async">
      </picture>
    </div>
  </figure>
  ```
- [ ] Run, in order: `patch_hero_fetchpriority.py --guide lab-to-action-card.html`,
      `patch_hero_fullwidth.py --guide lab-to-action-card.html`,
      `patch_hero_maxwidth.py --guide lab-to-action-card.html`.
- [ ] Update head meta to point at the new OG card:
  ```html
  <meta property="og:image" content="https://renalcarematters.com/images/lab-to-action-card-og.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="The Lab-to-Action Card — find your lab number, read the color, know what to do.">
  <meta name="twitter:image" content="https://renalcarematters.com/images/lab-to-action-card-og.png">
  ```
- [ ] Re-run `patch_hero_meta.py --guide lab-to-action-card.html` if the hero
      structure changed enough to need re-sync (it shouldn't, since hero-meta
      is separate from hero-figure).
- [ ] Commit and push per the repo's direct-to-main workflow.
