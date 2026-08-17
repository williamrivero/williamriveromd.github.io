---
name: williamriveromd-hero-vignette
description: >-
  Produces a single copy-paste ChatGPT Image Generator prompt for a guide HERO
  graphic designed to sit inside the circular vignette beside the hero title on
  renalcarematters.com. v3 spec: 2048×2048 canvas, circle occupies 85–90% of the
  diameter with a visible white margin (NOT full-bleed), a 20–25% reserved
  title-safe zone, mandatory people-variation rules, rotating composition
  archetypes, and camera-angle rotation across guides. Use whenever creating
  or regenerating the hero image for a guide whose hero uses the circular-
  vignette layout (copy on the left, a round photo/illustration on the right
  — e.g. epilepsy-seizures-ckd, igan-guide, prostate-cancer-ckd, hivan,
  first-nephrology-visit-guide, natural-supplements). For full-width editorial
  poster heroes or OG cards (NOT the circular vignette), use
  williamriveromd-infographic-skill. For in-body figures/algorithms use
  williamriveromd-simple-figure.
---

# WILLIAM RIVERO MD — HERO VIGNETTE GENERATOR v3

## PURPOSE

Generate ONE production-ready image prompt for a **guide hero graphic displayed
inside a circular vignette** (the `.hero-vignette` disc) beside the hero title.

This is fundamentally different from the older full-width editorial hero / OG
card: the image is masked into a **circle**, then given a soft edge vignette by
CSS. Any title text, watermark band, logo lockup, or infographic content baked
into the image will be **clipped by the circle and/or duplicate the HTML title**
— so it must not exist in the image.

## WHEN TO USE

Use this skill when:
- A guide's hero uses the **circular vignette** layout (`hero-grid` → `hero-copy`
  + `figure.hero-figure > .hero-vignette > img`).
- You are **regenerating** an existing hero so it crops cleanly into the circle.
- You want a clean, single-subject editorial **photo**, **still-life**, or **calm
  3D anatomy** — with no embedded words.

Use a DIFFERENT skill when:
- The hero is a **full-width infographic/poster** (dense panels, stats, numbered
  steps, baked title) → `williamriveromd-infographic-skill`.
- You need an **OG / social share card** (1200×630 with title text) →
  `williamriveromd-infographic-skill`.
- You need an **in-body figure, algorithm, or comparison** →
  `williamriveromd-simple-figure`.

> Rule of thumb: if the deliverable contains *words*, it is not a vignette hero.
> The vignette hero is purely a picture; the guide's `<h1>` sits beside it.

---

## UNIVERSAL CIRCULAR VIGNETTE HERO STRUCTURE (v3)

### CANVAS
- Compose on a **square canvas (2048 × 2048 recommended)**.
- The circular vignette should occupy **85–90% of the canvas diameter**.
- Leave a **visible white border around the entire circle**.
- The circle must be **fully visible and never cropped**.

### PRIMARY DESIGN GOAL
- This is a **hero image, not a complete infographic**.
- The artwork should communicate **one central idea at a glance**.
- Favor **simplicity, elegance, and visual impact** over information density.
- **Large, clean imagery is preferred over many small details.**

### TITLE SAFE ZONE (VERY IMPORTANT)
- Reserve approximately **20–25% of the circle as clean negative space** for
  the guide title and subtitle.
- This reserved area should contain:
  - soft gradients
  - subtle textures
  - blurred background
  - open sky
  - clean walls
  - uncluttered landscape
- **Avoid placing inside the title safe zone**:
  - faces
  - anatomy
  - icons
  - labels
  - food
  - objects
  - callouts
- The title should be able to occupy several lines using large typography
  without covering important artwork.

### VISUAL SIMPLICITY
Use only:
- **ONE dominant hero subject**
- **TWO to FOUR supporting visual elements**
- **ZERO to FOUR small supporting icons** if appropriate

Do NOT fill every empty space. Large areas of elegant negative space are
encouraged. **Think like the cover of a premium medical textbook.**

### COMPOSITION ARCHETYPES
Choose ONE composition archetype not recently used. Commit fully to that
archetype. Do not mix multiple archetypes.

| Code | Name | Recipe |
|---|---|---|
| **A** | Editorial Portrait | One large subject + 2–3 supporting scenes |
| **B** | Journey | One visual pathway + max 3 milestones |
| **C** | Radial | One central object + 4–6 surrounding elements |
| **D** | Panorama | Landscape dominates + one primary focal point |
| **E** | Lifestyle | 2–4 lifestyle scenes, minimal overlays |
| **F** | Anatomy | Large anatomical illustration + 2–3 supporting concepts |
| **G** | Infographic | One dominant diagram + max 5 supporting callouts |
| **H** | Clinical | One consultation scene, minimal supporting imagery |
| **I** | Object Hero | One large object occupies most of the circle, small environmental details only |
| **J** | Environmental Storytelling | One cohesive scene, no floating panels |

### VISUAL HIERARCHY
- **60–70% hero subject**
- **20–30% supporting context**
- **10–20% reserved whitespace**
- The viewer should immediately know what the hero subject is.
- Avoid visual clutter.

### HUMAN VARIATION (MANDATORY — DO NOT IGNORE)
If this guide includes people, they MUST NOT resemble people from previous
generations. Treat every guide as if it were photographed with an entirely
different cast. It is **unacceptable to reuse the same stock-model appearance**.

RANDOMIZE ALL OF THE FOLLOWING:
- age
- biological sex
- gender presentation
- facial proportions
- face shape
- jawline
- nose
- lips
- eye shape
- eyebrow shape
- hairstyle
- hair color
- hair length
- body habitus
- height impression
- skin tone within Filipino diversity
- clothing style
- clothing colors
- accessories
- posture
- hand position
- facial expression
- activity
- environment
- camera distance
- camera angle

**At least 12 of these characteristics should visibly differ from the previous
guide.**

### NEVER REUSE THESE ARCHETYPES
Avoid repeatedly generating:
- smiling older Filipino man eating
- smiling older Filipino woman eating
- middle-aged couple at dining table
- identical kitchen scene
- identical dining room
- identical wooden table
- identical teal polo shirt
- identical beige blouse
- identical white plate with grilled salmon and vegetables
- identical three-quarter seated pose
- identical window lighting

If a newly generated person could reasonably be mistaken for someone from
another guide, **generate a different individual instead**.

### PEOPLE VARIETY
Across the entire website, intentionally rotate between:
- no people
- one woman
- one man
- teenager
- young adult
- elderly adult
- clinician only
- patient only
- caregiver
- married couple
- siblings
- family
- unrelated community members
- chef
- market vendor
- farmer
- dialysis nurse
- dietitian
- office worker
- athlete

**Do not repeat the same people arrangement in consecutive guides.**

### CAMERA VARIETY
Rotate between:
- close portrait
- environmental portrait
- overhead
- top-down
- side profile
- wide-angle
- over-the-shoulder
- macro food scene
- hands-only composition
- silhouette
- rear three-quarter view

**Never use the same framing twice in succession.**

### OPTIONAL — NON-PEOPLE HEROES
Whenever appropriate, intentionally choose one of the following instead of
using a person:
- beautifully plated kidney-friendly meal
- premium ingredient still life
- anatomical illustration
- clinical consultation room
- grocery basket
- cooking scene
- kitchen countertop
- nutrition objects
- dialysis equipment
- medical illustration
- infographic object hero

**A human is not required unless it clearly strengthens the educational message.**

---

## HOUSE STYLE CONSTITUTION

### Subject & tone
- Warm, authentic, **Filipino clinical context** where people are shown.
- Calm, reassuring, documentary-realistic — not stocky, not staged-cheesy, not
  dark or clinical-cold. Soft natural daylight.
- For non-people topics: a single clean **still-life** or a calm **semi-photoreal
  3D anatomy** on a soft, uncluttered surface.

### Colour & light
- Bright, light, airy. Soft daylight, gentle depth of field, shallow background
  blur.
- Palette harmonizes with the pastel hero: clinical teal `#1a6b72`, navy
  `#0f1e2e`, renal green `#1f7a4d`, warm neutrals. Avoid heavy saturation, HDR,
  or neon.
- Backgrounds: light interiors, soft teal-tinted or warm neutral surfaces.
  **Never a dark/charcoal/black scene.**

### Realism
- Anatomically and clinically plausible. Correct hands, faces, equipment.
- Skin tones and features reflect Filipino patients/clinicians.

---

## CANONICAL SIZE

| Use | Dimensions | Ratio |
|---|---|---|
| **Circular vignette hero (v3 default)** | **2048 × 2048** | 1:1 |
| Compact option (older guides) | 1536 × 1536 | 1:1 |
| Minimum | 1024 × 1024 | 1:1 |

Always **square**. Never landscape/portrait for a vignette hero (those get badly
cropped). v3 prefers the larger canvas so the 85–90% inscribed circle still
delivers a hi-res rendered disc.

---

## NEGATIVE PROMPT (always include)

Avoid:
- busy layouts
- collage overload
- more than four supporting scenes
- dozens of icons
- tiny unreadable labels
- infographic clutter
- duplicated people
- repeated compositions
- cropped circle
- cropped objects
- cropped anatomy
- edge clipping
- objects touching the circular border
- important content inside the title safe zone
- baked-in text, titles, captions, logos, watermarks
- rectangular borders, frames, banners
- dark / charcoal / black backgrounds
- cartoon style, neon, HDR, over-saturation
- distorted hands or faces, implausible anatomy

---

## EXECUTION INSTRUCTIONS

When this skill is invoked:

1. **Identify the guide** (slug) and its subject. Decide the subject archetype
   using the **People variety** / **Camera variety** / **Composition archetype**
   matrices above. Pick combinations that haven't been used in adjacent guides.
2. **Pick ONE composition archetype** (A–J) and one camera framing.
3. **Pick ONE scaffold** (Clinical People / Still-Life / Anatomy) and fill in
   the specifics, weaving in the chosen archetype and camera.
4. **Output exactly ONE prompt block** in the OUTPUT FORMAT — nothing else.

### Scaffold A — Clinical People Scene (2048 × 2048)
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed
to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas
diameter with a visible WHITE BORDER around the full circle (the circle must
never touch the canvas edges). Composition archetype: [A–J chosen]. Camera:
[chosen framing — e.g. environmental portrait, over-the-shoulder, side profile].

Subject: a Filipino [age/sex/profession with explicit randomized traits — see
HUMAN VARIATION list; ≥12 traits must visibly differ from the last guide in
the same library] [doing/discussing TOPIC] in a clean, bright modern Philippine
[clinic / kitchen / market / home / community setting], with soft natural
daylight and gentle shallow depth of field.

Visual hierarchy: hero subject occupies 60–70% of the circle; 2–4 supporting
context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient /
clean wall / open sky / blurred background (no faces, anatomy, icons, food, or
callouts inside that zone) so the HTML title can sit beside the disc without
covering important artwork.

Calm, reassuring, documentary-realistic colour grade harmonizing with clinical
teal #1a6b72 and navy #0f1e2e on a light background. Edge falloff toward a
slightly deeper neutral at the rim. Full-bleed within the inscribed circle,
no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or
renalcarematters.com watermark.
```

### Scaffold B — Single Still-Life / Object (2048 × 2048)
```
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be
displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter
with a visible WHITE BORDER around the full circle. Composition archetype:
[I Object Hero / C Radial / G Infographic — chosen]. Camera: [top-down /
macro / side / overhead — chosen].

Subject: a single clean arrangement of [OBJECT(S): e.g. fresh low-sodium
Filipino foods / a supplement bottle and capsules / a blister pack and water
glass / a labeled blood tube / a blood-pressure cuff / a stethoscope and lab
slip] centered on a soft, uncluttered light [teal-tinted / warm neutral]
surface with gentle daylight and shallow depth of field.

Visual hierarchy: hero object 60–70% of the circle; 2–4 small supporting
elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of empty surface or soft
gradient (no objects, labels, icons inside that zone). Soft edge falloff
toward a slightly deeper neutral at the rim. Light, calm, appetizing-but-
clinical colour grade.

Absolutely NO readable text or labels on the objects (no packaging copy you
can read), no titles, no logos, no watermark. Full-bleed within the inscribed
circle, no rectangular borders.
```

### Scaffold C — Calm 3D Anatomy / Illustration (2048 × 2048)
```
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas,
composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the
canvas diameter with a visible WHITE BORDER around the full circle.
Composition archetype: [F Anatomy / I Object Hero — chosen]. Camera:
[three-quarter / cross-section / macro — chosen].

Subject: a single clean render of [ANATOMY: e.g. a pair of human kidneys /
one nephron / a glomerulus / a blood vessel cross-section / a stylised
mitochondrion] floating on a soft, uncluttered light [teal-tinted / off-
white] background, centered with gentle studio lighting and soft shadow.
Anatomically accurate, restrained clinical colour (renal reds, teal accents),
not garish.

Visual hierarchy: the anatomical structure occupies 60–70% of the circle;
2–3 supporting structures or subtle context cues 20–30%; reserve a 20–25%
TITLE SAFE ZONE of empty soft background (no anatomy, leader lines, labels,
or callouts in that zone). Soft falloff at the rim.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or
watermark — clean render only. Full-bleed within the inscribed circle, no
rectangular borders.
```

5. **Output ONE prompt block** in this exact format:

```
FILE NAME: [guide-slug]-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — [Scaffold A people / B still-life / C anatomy]
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: [A–J letter + name]
CAMERA: [framing]
HUMAN VARIATION (vs. previous guide): [list ≥12 traits that differ — or "no people"]
AUDIENCE: [patients / clinicians / mixed]
VISUAL GOAL: [one sentence — what the picture conveys at a glance]

PROMPT:
[filled-in scaffold, fully expanded with the guide's specifics]

NEGATIVE INSTRUCTIONS:
[paste the canonical NEGATIVE PROMPT block above]

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin —
never cropped. ONE dominant hero subject occupying 60–70% of the circle, 2–4
supporting elements, 20–25% empty title-safe zone reserved (soft gradient, sky,
wall, or blurred background — no faces, anatomy, icons, food, or callouts
inside). Filipino clinical context where people are shown, with ≥12 traits
visibly different from the last guide in the library. Camera framing not
repeated from the previous guide. Crops cleanly inside the circle with no
text or subject lost at the edges.
```

---

## TWO-STAGE PIPELINE & PLACEMENT

This skill is **Stage 1** (prompt authoring). To stage the file and folder
structure, hand the prompt to `williamriveromd-local-image-generator` as usual,
OR place the final asset manually:

- Save as `images/<guide-slug>-vignette-hero.png` **and** a WebP twin
  `images/<guide-slug>-vignette-hero.webp`.
- The guide's hero references these via
  `<picture><source srcset="../images/<slug>-vignette-hero.webp"><img
  src="../images/<slug>-vignette-hero.png" ...></picture>` inside
  `figure.hero-figure > .hero-vignette`.
- The CSS handles the circle clip, centering, ring, and edge vignette. The
  v3 spec's own 85–90% white-bordered circle adds a second margin inside the
  CSS circle for an extra-clean, "framed-portrait" feel — that's intentional.
- Keep the square `width`/`height` attributes (e.g. `width="2048"
  height="2048"`) — the CSS scales the picture to its `.hero-vignette` slot.

## REMINDERS

- **One subject per hero.** If the topic suggests two scenes, pick the stronger one.
- **Square only.** Never deliver a landscape banner for a vignette hero.
- **The picture carries the mood; the words live in the HTML.** Keep the image wordless.
- **Rotate everything**: archetype, people composition, camera, environment.
  If a newly generated image could be mistaken for the last one — regenerate.
