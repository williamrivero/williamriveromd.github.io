# Image prompts — Why Home Hemodialysis Is Difficult to Run in the Philippines

Guide: `guides/home-hemodialysis-philippines.html`
Stage 1 output (prompt authoring). Paste each PROMPT block into the ChatGPT Image
Generator GPT: https://chatgpt.com/g/g-pmuQfob8d-image-generator

Save each result as **both** `.png` and a `.webp` twin in `images/`.

The three analytical visuals required by the blueprint (barrier system map,
"where responsibility moves", evidence map) are **built as accessible inline
HTML/SVG inside the guide**, not as generated images — they carry text
equivalents in the DOM, reflow at 320 px, survive printing, and stay editable
when policy changes. Only the two photographic assets below are generated.

---

## IMAGE 1 — Circular vignette hero

```
FILE NAME: home-hemodialysis-philippines-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B (still-life / object hero, no people)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling
CAMERA: Wide-angle environmental, slightly low eye level, from the doorway
HUMAN VARIATION (vs. previous guide): No people — deliberate rotation away from the
  previous two guides in this library, which both featured Filipino human subjects
  (a nephrologist portrait collage and a family meal scene). An empty, waiting room
  is the point: the machine has arrived, the system around it has not.
AUDIENCE: Mixed (patients, families, clinicians, policymakers)
VISUAL GOAL: A hospital-grade dialysis machine standing alone in an ordinary Filipino
  living room — clinical technology dropped into domestic space, with nobody yet
  trained to run it.

PROMPT:
Square 1:1 photorealistic editorial still-life on a 2048×2048 canvas, composed to be
displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a
visible WHITE BORDER around the full circle (the circle must never touch the canvas
edges). Composition archetype: J, Environmental Storytelling — one cohesive scene, no
floating panels or collage tiles. Camera: wide-angle environmental view from the
doorway, slightly below eye level.

Subject: a single modern hemodialysis machine on castors — a tall white-and-grey
clinical console with a hollow-fibre dialyzer mounted vertically on its front, coiled
clear blood tubing, and a small dark screen that is switched off — standing on the
tiled floor of an ordinary, modest Filipino living room. Beside it, one empty reclining
chair with a folded clean towel on the armrest. Supporting environmental details, small
and quiet: morning light falling through jalousie windows, a plain painted wall, a
single household electrical outlet low on the wall with the machine's cable running to
it, and a short length of drainage tubing disappearing toward a doorway. Everything is
clean, ordinary and domestic — a family home, not a clinic.

Visual hierarchy: the dialysis machine and chair occupy 60–70% of the circle, placed
right of centre; 2–4 supporting environmental elements (window light, wall outlet,
drainage line, tiled floor) occupy 20–30%; reserve the UPPER-LEFT 20–25% of the circle
as a TITLE SAFE ZONE of softly lit blank wall and diffuse window glow, containing no
objects, equipment, cables, furniture, faces or callouts, so the HTML title can sit
beside the disc without covering important artwork.

Bright, airy, calm documentary colour grade harmonizing with clinical teal #1a6b72 and
navy #0f1e2e against a light background of warm white wall and pale floor tile. Gentle
shallow depth of field, soft natural daylight, no dramatic shadows. Soft edge falloff
toward a slightly deeper warm neutral at the rim. Full-bleed within the inscribed
circle, no rectangular borders, frames or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, machine screen
readout, readable equipment branding, logo, or williamriveromd.com watermark. The
machine's display is dark and blank.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons,
tiny unreadable labels, infographic clutter, duplicated people, any people at all,
repeated compositions, cropped circle, cropped objects, cropped anatomy, edge clipping,
objects touching the circular border, important content inside the title safe zone,
baked-in text, titles, captions, logos, watermarks, readable branding on the machine,
rectangular borders, frames, banners, dark / charcoal / black backgrounds, hospital-ward
or ICU look, cartoon style, neon, HDR, over-saturation, distorted or implausible
equipment anatomy, tangled or physically impossible tubing.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never
cropped. ONE dominant hero subject (the machine + chair) occupying 60–70% of the circle,
2–4 supporting environmental elements, upper-left 20–25% title-safe zone left as soft
lit wall. Domestic Philippine interior, unmistakably a home rather than a clinic. No
people, no text anywhere. Dialyzer mounted plausibly on the console with tubing that
traces a physically coherent path. Crops cleanly inside the circle with nothing lost at
the edges.
```

---

## IMAGE 2 — OG / social share card, also used as the inline lead figure

```
FILE NAME: home-hemodialysis-philippines-og.png
IMAGE TYPE: Photorealistic editorial hero + light diagrammatic overlay (Archetype 1)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: Mixed (patients, families, clinicians, policymakers, health journalists)
VISUAL GOAL: The article's whole argument in one frame — everything a licensed clinic
  supplies as a *building* has to be rebuilt as a *service* that reaches one living room.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Photorealistic medical editorial share card for a nephrology policy article, landscape
1200 × 630, split composition on a bright light background.

LEFT HALF (approximately 45% of the frame): a bright, busy, licensed Philippine
hemodialysis clinic photographed in clean natural daylight — an orderly row of four or
five hemodialysis machines beside reclining chairs, a Filipino dialysis nurse in scrubs
standing attentively mid-frame checking a machine, a glimpse through an interior window
of a water-treatment room with vertical reverse-osmosis columns and blue pressure
vessels, and a wall-mounted emergency light. Institutional, staffed, supervised.

RIGHT HALF (approximately 45% of the frame): the same lighting and colour grade, but a
single modest Filipino living room — one hemodialysis machine beside one reclining
chair, one older Filipino woman seated calmly with a light blanket over her lap, and one
adult daughter standing beside her looking at the machine. Domestic tiled floor, plain
painted wall, jalousie window, a small stack of supply boxes in the corner. Quiet,
ordinary, unsupervised.

CONNECTING THE TWO HALVES: five or six thin dashed teal (#1a6b72) lines arcing from the
clinic side across the seam into the living room, each carrying one short label set in
small clean sans-serif navy (#0f1e2e) capitals: TRAINING · TECHNICAL SERVICE · TREATED
WATER · SUPPLIES · 24/7 SUPPORT · BACKUP CARE. Keep these labels sparse, legible on
mobile, and clearly secondary to the photography — they are annotation, not an
infographic.

TITLE: across the upper portion of the frame, in bold navy (#0f1e2e) Inter, two lines,
generously letterspaced and mobile-readable: "HOME HEMODIALYSIS" / "IS A PROGRAM, NOT AN
APPLIANCE". Beneath it, one smaller line in clinical teal (#1a6b72) Inter medium: "Why
the Philippines has no clear pathway yet". Reserve clean, uncluttered light space behind
all typography so it reads cleanly.

Overall: premium healthcare publication aesthetic, restrained and calm, natural Filipino
skin texture, realistic equipment, bright airy daylight throughout, white to off-white
(#fafafa) base with soft grey (#f3f4f6) section separation, navy and teal accents only.
No red, no alarm imagery, no distressed or frightened expressions — the tone is
analytical, not fearful.

Include the copyright attribution rendered exactly as williamriveromd.com in small,
semi-transparent (70% opacity) navy (#0f1e2e) sans-serif text in the bottom-right corner,
not obscuring clinical content.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look,
avoid excessive saturation. Avoid needles in skin, blood, distress, or fear imagery.
Avoid more than six dashed connector labels. Avoid a hard vertical dividing line or
picture-frame border between the two halves — the seam should be a soft gradient.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY
the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no
serif fonts, no decorative or handwritten typefaces. Never omit the williamriveromd.com
attribution.

QUALITY CHECK:
Exactly 1200 × 630. Must be mobile-readable, clinically plausible, visually calm,
publication-grade, and consistent with williamriveromd.com. Both halves share one
lighting scheme and one colour grade so the frame reads as a single image, not a collage.
Machines, dialyzers and tubing are anatomically and mechanically plausible. Background is
white / off-white / soft light grey — never dark. Title occupies clean negative space.
Copyright attribution williamriveromd.com visible in the bottom-right corner.
```

---

## After the images are received

1. Save `home-hemodialysis-philippines-vignette-hero.png` + `.webp` and
   `home-hemodialysis-philippines-og.png` + `.webp` into `images/`.
2. Run `python3 patch_hero_fetchpriority.py --guide home-hemodialysis-philippines.html`
   and `python3 patch_img_dimensions.py` to confirm the intrinsic dimensions match.
3. The guide already carries the correct `og:image`, `og:image:width` (1200) and
   `og:image:height` (630) meta tags — no meta edits needed.
