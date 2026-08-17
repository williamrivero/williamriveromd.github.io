# Image Plan — *Magnesium Supplements and Kidney Disease* (`magnesium-supplements-ckd.html`)

**Guide:** What the different magnesium forms really do — single-mode patient guide (EN/TL/CEB/KAP), 14 sections
**Companion tool:** `calc-magnesium-replacement.html` (elemental conversion across 17 salts)
**Prepared:** 2026-08-16 · **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the
ChatGPT **Image Generator** GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` ·
`williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure` ·
`williamriveromd-algorithm-generator-skill` · `williamriveromd-organ-crosstalk-sigil-graphic`

---

## House rules baked into every prompt
- **Light backgrounds only** (white `#ffffff` / off-white `#fafafa` / soft gray `#f3f4f6` / pale teal `#eef6f7`).
  Never navy / charcoal / black.
- **Fonts:** on-image type is one of **Inter · Nunito Sans · IBM Plex Sans · Manrope** — no serif, no decorative.
- **Palette:** navy `#0f1e2e` (text/accents), clinical teal `#1a6b72`, renal green `#1f7a4d` (supported/safe),
  amber `#b8860b` (partly supported/caution), red `#b91c1c` (danger/urgent), slate `#6b7684` (not established) —
  used *only* as text and accents on light fills.
- **Attribution:** small semi-transparent navy `renalcarematters.com` bottom-right (bottom-centre on portrait) on
  every image **except the wordless vignette hero**, which carries no text at all.
- **Save each asset** as `.png` **and** a matching `.webp` twin under `images/`, using the exact FILE NAME below.

### Clinical guardrails for THIS guide — non-negotiable, and stricter than usual
This guide exists to *dismantle* a marketing chart. A graphic that accidentally rebuilds that chart defeats the
whole page. Every prompt below therefore forbids the following, and the negative-instruction blocks repeat it:

- **No dose recommendation, anywhere.** Never render "take 200–400 mg," a daily target, a split morning/night
  schedule, or a per-stage dose. The **only** numbers permitted on any asset are: elemental percentages (pure
  chemistry), the `1,500 mg → 240 mg` label example, the `350 mg` adult upper limit **always** labelled
  *supplements and medicines only · generally healthy adults*, the antibiotic/bisphosphonate spacing hours, and
  the `~2 mmHg` blood-pressure effect size.
- **No CKD-stage dosing table.** Not as a grid, not as a ladder, not as a traffic light by stage. The guide
  deliberately refuses to publish one; no image may smuggle it back in.
- **No "best form" winner.** No trophy, crown, podium, gold star, or #1 badge on any salt. No green check beside
  glycinate-for-sleep, taurate-for-heart, or threonate-for-brain. **The only permitted ranking of forms is by
  elemental magnesium percentage, which is molecular weight, not merit.**
- **No one-form-to-one-organ map.** Never draw a salt with an arrow pointing at a brain, heart, or sleeping
  figure. That diagram *is* the misinformation this guide corrects.
- **Exactly three evidence labels**, never more, never reworded: **Supported · Partly supported · Not established.**
  Never "doesn't work," never "debunked," never "myth" as a verdict on an unstudied claim.
- **Marketing claim and evidence must be visually distinct** — the claim always in a muted gray/italic card, the
  evidence always in navy/teal on white. They must never share one voice.
- **No product branding or shopping cues.** No readable brand names, no real bottle designs, no price tags, no
  shopping carts, no "buy" affordances, no supplement-aisle glamour lighting.
- **The kidney is the exit door.** Any physiology asset must show renal excretion as the rate-limiting step, and
  must show accumulation — not deficiency — as the failure mode when clearance drops.
- **Epsom salt / topical is never shown working.** No glowing skin, no magnesium particles crossing skin, no
  absorption arrows through a dermis into blood.
- **No fear imagery in people scenes** — but the hypermagnesemia red-flag block must read as genuinely urgent
  (red, unambiguous). Calm ≠ soft-pedalling a real danger.

## Asset roster

| # | File (`images/…`) | Guide section | Governing skill | Size |
|---|---|---|---|---|
| 1 | `magnesium-supplements-ckd-vignette-hero.png` | hero disc (replaces `hero-cat-electrolytes`) | hero-vignette | 2048×2048 |
| 2 | `magnesium-supplements-ckd-og.png` | `og:image` (replaces `hero-cat-electrolytes`) | infographic | 1200×630 |
| 3 | `magnesium-supplements-ckd-01-gut-kidney-bone-sigil.png` | §3 Why kidney function changes the answer | organ-crosstalk-sigil | 1024×1024 |
| 4 | `magnesium-supplements-ckd-02-renal-handling-mechanism.png` | §3 (clinician depth) | biomedical-mechanism-figure | 1792×1024 |
| 5 | `magnesium-supplements-ckd-03-hidden-sources.png` | §3 Hidden magnesium | infographic | 1792×1024 |
| 6 | `magnesium-supplements-ckd-04-elemental-ladder.png` | §6 The forms | simple-figure (Scaffold E) | 1024×1536 |
| 7 | `magnesium-supplements-ckd-05-claim-check.png` | §7 Claim check | simple-figure (Scaffold B) | 1792×1024 |
| 8 | `magnesium-supplements-ckd-06-label-explainer.png` | §8 Reading the label | simple-figure (Scaffold B) | 1792×1024 |
| 9 | `magnesium-supplements-ckd-07-interaction-spacing.png` | §10 Interactions | simple-figure (Scaffold E) | 1536×1152 |
| 10 | `magnesium-supplements-ckd-08-decision-pathway.png` | §11 Decision pathway | algorithm-generator (Style C) | 1024×1536 |

**Currently in the guide:** the hero and `og:image` both point at the shared category image
`images/hero-cat-electrolytes.{webp,png}` (1254×1254). Assets 1 and 2 replace those; assets 3–10 are new inline
figures that do not yet exist in the HTML. See the **Production checklist** at the end for the exact wiring.

---

## 1 · Circular vignette hero *(replaces the category-hero placeholder)*

> **Skill:** `williamriveromd-hero-vignette` · Scaffold B (still-life) · Archetype **I — Object Hero**
> **Rotation note:** the two nearest library neighbours (`natural-supplements-kidney`, `vitamin-d-philippines-kidney-disease`)
> both used people scenes. This one deliberately goes **no-people, top-down still-life** so consecutive supplement
> guides do not repeat a cast or a framing.

```
FILE NAME: magnesium-supplements-ckd-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B single still-life / object
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero (one dominant arrangement, small environmental detail only)
CAMERA: top-down flat-lay, very slight tilt, soft shallow depth of field at the rim
HUMAN VARIATION (vs. previous guide): no people — deliberate rotation away from the consecutive people-led
  supplement heroes (natural-supplements-kidney, vitamin-d-philippines-kidney-disease)
AUDIENCE: patients and families
VISUAL GOAL: "Many different forms, all going to the same place" — a calm, honest still-life of varied magnesium
  presentations beside a plain glass of water, with no brand, no promise, and no winner.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette
occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never
touch the canvas edges). Composition archetype: Object Hero. Camera: top-down flat-lay with a very slight tilt,
gentle daylight from the upper left, soft shallow depth of field falling off toward the rim.

Subject: a single calm arrangement on a soft, uncluttered pale teal-tinted stone surface — four or five visibly
DIFFERENT magnesium presentations grouped loosely together: a few plain white oval tablets, two clear amber
capsules showing pale powder inside, a small heap of fine white crystalline powder, a single larger chalky
white tablet, and a shallow unlabeled glass dish holding coarse bath-salt crystals set slightly apart from the
others. Beside them, a plain clear glass of water. All containers and tablets are completely UNBRANDED and
UNMARKED — no printed text, no logos, no pill imprints, no packaging, no blister foil, no bottle labels.

Visual hierarchy: the grouped magnesium forms and the glass occupy 60–70% of the circle; 2–3 quiet supporting
details (the soft shadow of the glass, a faint water ring, the stone texture) fill 20–30%; reserve a 20–25%
TITLE SAFE ZONE of empty smooth surface and soft gradient in the upper-left quadrant — no objects, crystals,
tablets, glass, labels, or icons inside that zone — so the HTML title can sit beside the disc without covering
anything. Light, calm, clinical-but-warm colour grade harmonising with clinical teal #1a6b72 and navy #0f1e2e;
soft edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no
rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, brand name, logo, or renalcarematters.com
watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, dozens of icons, tiny unreadable labels,
infographic clutter, repeated compositions, cropped circle, cropped objects, edge clipping, objects touching the
circular border, important content inside the title-safe zone, baked-in text/titles/captions/logos/watermarks,
rectangular borders/frames/banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation.
NO branded packaging, NO readable label text, NO pill imprints, NO price tags, NO shopping or supplement-aisle
styling, NO glamour or "wellness advertisement" lighting, NO glowing or sparkling particles, NO anatomy or organ
imagery, NO one-form-to-one-organ arrows.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant
subject (the grouped magnesium forms) at 60–70% of the circle, 2–3 supporting details, 20–25% empty upper-left
title-safe zone. Every object unbranded and textless. Reads as honest and clinical, not as an advertisement.
No form is visually favoured over another. Crops cleanly inside the circle. Completely wordless.
```

---

## 2 · OG / social share card *(replaces the category-hero `og:image`)*

> **Skill:** `williamriveromd-infographic-skill` · Archetype 1 adapted to a titled OG card
> **Size is fixed at 1200 × 630** — non-negotiable per the skill's OG rule.

```
FILE NAME: magnesium-supplements-ckd-og.png
IMAGE TYPE: Editorial OG / social share card with baked title text
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630  (FIXED — never any other size for an OG card)
AUDIENCE: mixed (patients, families, clinicians)
VISUAL GOAL: One glance says "the tidy form-to-benefit chart is not real, and kidneys change the question" —
  without ranking a single product.

PROMPT:
Photorealistic-plus-vector medical editorial OG / social share card, exactly 1200×630 px, for a nephrology
patient-education guide, on a clean WHITE background. Split composition.

LEFT ~48%: a bright, softly lit top-down photorealistic still-life of several visibly different UNBRANDED
magnesium presentations — plain white tablets, two clear capsules, a small heap of white powder — grouped on a
pale teal-tinted surface beside a plain glass of water. No packaging, no readable label text, no logos, no
pill imprints.

RIGHT ~52%: a clean off-white panel carrying the title text and, beneath it, a simple flat vector motif of a
neat four-cell grid whose tidy connecting lines dissolve into soft dashes and fade out on the right-hand side —
reading visually as "the neat chart does not hold up." Draw the grid and dashes in clinical teal #1a6b72 and
slate #6b7684 only. The grid cells are EMPTY — no organ icons, no brain, no heart, no sleeping figure, no
salt names inside them.

Title text, bold Inter, navy #0f1e2e, large and mobile-legible:
  "Magnesium: what the forms really do"
Sub-line, medium weight, clinical teal #1a6b72:
  "The evidence is less tidy than the label. Kidney function changes what is safe."

Strong hierarchy, generous negative space, rounded soft panel edges, publication-grade nephrology editorial look.
Small semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI-gibberish text, unrealistic anatomy, overprocessed HDR,
generic stock-photo look, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use
ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope — no serif, no decorative type. NO dose numbers of any kind, NO
milligram figures, NO CKD stages, NO brand names or packaging, NO trophy/crown/podium/#1 badge, NO green check
on any single form, NO organ icons inside the grid cells, NO arrow from a salt to a body part. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Mobile-legible two-line title. Light background. The dissolving-grid motif reads as "this
chart is not real" without naming or ranking any product. No dose figures anywhere. No form is favoured.
renalcarematters.com visible bottom-right. Pair with og:image:width="1200" og:image:height="630".
```

---

## 3 · Gut–kidney–bone magnesium sigil *(add — § 3, opening the physiology)*

> **Skill:** `williamriveromd-organ-crosstalk-sigil-graphic` · monoline sigil, minimal labels
> **Why a sigil here:** the single idea the reader must carry out of §3 is a *route* — in through the gut, stored
> in bone, out through the kidney. A symbolic three-organ loop states that faster than a detailed poster.

```
FILE NAME: magnesium-supplements-ckd-01-gut-kidney-bone-sigil.png
IMAGE TYPE: Organ-crosstalk sigil — three-organ magnesium route
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients and families
VISUAL GOAL: "In through the gut, held in bone, out through the kidney — and the exit is the part that fails."

PROMPT:
Create a simple medical organ-crosstalk sigil illustration on a clean white background.

ORGANS (simplified monoline line-art icons, evenly weighted strokes, rounded organic line quality):
- a simplified intestine / gut coil at the TOP LEFT
- a pair of kidneys at the BOTTOM CENTRE, drawn slightly larger than the other two organs
- a simplified long bone (femur, cross-sectioned to suggest storage) at the TOP RIGHT

RELATIONSHIP:
Show the magnesium route using thin dotted curved arrows. One dotted arrow travels from the gut DOWN toward the
kidneys (absorption entering the circulation). A slim BIDIRECTIONAL dotted arc connects the bone and the
circulation path (storage in and release out). A single, clearly thicker and more prominent dotted arrow leaves
the kidneys and exits DOWNWARD out of the composition — this exit arrow is the visual emphasis of the whole
sigil and should read as the busiest, most important channel. Draw a small open gate or narrowing constriction
symbol partway along that exit arrow, drawn in muted clinical red #b91c1c, to suggest the route can narrow.
Every other line is soft teal-blue.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal #1a6b72 and slate-blue palette with the single red
constriction accent, white background, clean rounded organ shapes, balanced sigil-like composition, generous
whitespace, no photorealism, no 3D, no shading, no heavy shadows.

LABELS (the only text permitted, set in clean sans-serif Inter, small, navy #0f1e2e):
  "IN" beside the gut arrow · "STORED" beside the bone arc · "OUT" beside the kidney exit arrow
No other words, no organ names, no numbers, no dose figures.

OUTPUT:
Square image, clean margins, high-resolution, publication-grade medical icon aesthetic. Include a small,
semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner, not obscuring the sigil.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, excessive labels, dark backgrounds, neon colours, complex
infographics, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic lighting, stock-photo
style. NO dose numbers, NO milligram figures, NO CKD stages, NO supplement or tablet imagery, NO brain/heart/
sleep icons, NO one-form-to-one-organ mapping. If text is present, never use serif or decorative fonts — Inter,
Nunito Sans, IBM Plex Sans, or Manrope only. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Three organs only, monoline, generous whitespace. The kidney exit arrow is unmistakably the most prominent
channel and carries the red narrowing symbol. Exactly three words on the image (IN / STORED / OUT). Reads in
under three seconds on a phone. renalcarematters.com bottom-right.
```

---

## 4 · Renal magnesium handling — mechanism figure *(add — § 3, clinician depth)*

> **Skill:** `williamriveromd-biomedical-mechanism-figure` · full organ → magnified inset → bottom summary flow
> **Accuracy note for the generator:** the loop of Henle's **thick ascending limb** is the dominant site of
> magnesium reabsorption (paracellular, driven by the lumen-positive voltage), with **fine regulation distally**.
> Excretion is the adaptive lever. Do not invent transporter names beyond those listed.

```
FILE NAME: magnesium-supplements-ckd-02-renal-handling-mechanism.png
IMAGE TYPE: Biomedical mechanism schematic — organ panel → magnified nephron inset → summary flow
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians and motivated patients
VISUAL GOAL: "Healthy kidneys adapt magnesium excretion across a wide range; when that adaptation is lost,
  ordinary over-the-counter magnesium accumulates."

PROMPT:
Create a publication-grade biomedical mechanism schematic in a scientific review-article style, flat vector
illustration with soft semi-3D shading, on a WHITE background, 1792×1024.

TOPIC: renal handling of magnesium and its failure in reduced kidney function.

LEFT PANEL — organ-level context:
Show a simplified light gray-blue kidney in longitudinal cross-section with cortex, medulla, and the renal
artery and vein indicated. Label the panel "REDUCED KIDNEY FUNCTION". A thin dashed connector box points from
the kidney to the magnified panel on the right.

CENTRE / RIGHT PANEL — magnified functional unit, inside a thin dashed border:
Show a clean schematic nephron — glomerulus, proximal tubule, loop of Henle, distal convoluted tubule,
collecting duct — with the segments highlighted in pale yellow where magnesium is handled. Add concise
callouts with directional arrows:
  · at the proximal tubule:            "Modest reabsorption"
  · at the thick ascending limb (label it as the dominant site, drawn largest):  "Bulk paracellular reabsorption"
  · at the distal convoluted tubule:   "Fine regulation"
  · at the collecting duct outflow:    "↑ Excretion when intake rises  ·  ↓ Excretion when intake falls"
Draw a wide double-headed adaptation arrow spanning the outflow labelled "ADAPTIVE RANGE", and beside it a
second, visibly COMPRESSED version of the same arrow drawn in muted red #b91c1c labelled "NARROWED IN CKD".
The contrast between the wide arrow and the compressed arrow is the central teaching point of the figure.

BOTTOM SUMMARY FLOW — three boxes, left to right, joined by arrows:
  LEFT (pale pink pathology box):     "Reduced filtration and reduced adaptive excretion"
  CENTRE (neutral bridge box):        "Ordinary magnesium load — supplement, laxative, antacid, bowel prep"
  RIGHT (pale blue outcome box):      "↑ Serum magnesium  ·  Nausea, flushing, weakness  ·  ↓ Blood pressure
                                       ·  ↓ Respiratory drive  ·  Arrhythmia"
The right-hand box must read as a clinical hazard, not a benefit.

Muted clinical palette: light gray-blue anatomy, pale yellow highlighted segments, red #b91c1c for the narrowed
arrow and pathology accents, blue for the outcome box, pale pink for the pathology box. Thin dashed connector
lines. Clean sans-serif typography set in Inter throughout. Generous whitespace, labels legible at slide-viewing
size. Small semi-transparent navy "© renalcarematters.com" in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative effects, drop shadows, cartoonish styling, gibberish text,
excessive icons, overcrowding. NO invented transporter or channel names beyond those written above. NO numeric
thresholds of any kind — no serum magnesium cut-offs, no eGFR numbers, no CKD stage numbers, no doses in
milligrams. NO supplement bottles or tablets. NO one-form-to-one-organ mapping. Use ONLY Inter/Nunito Sans/
IBM Plex Sans/Manrope — never a serif font.

QUALITY CHECK:
Organ panel → dashed magnified nephron inset → bottom injury/bridge/outcome flow, in that order. The thick
ascending limb is drawn as the dominant reabsorption site. The wide "ADAPTIVE RANGE" arrow versus the compressed
red "NARROWED IN CKD" arrow is the clearest contrast on the page. Anatomically plausible nephron. No numbers
anywhere. © renalcarematters.com bottom-right.
```

---

## 5 · Hidden magnesium — the sources nobody declares *(add — § 3)*

> **Skill:** `williamriveromd-infographic-skill` · Archetype 4 (multi-panel educational)
> **Teaching point:** patients truthfully report "no magnesium supplement" while taking two products containing it.

```
FILE NAME: magnesium-supplements-ckd-03-hidden-sources.png
IMAGE TYPE: Multi-panel educational infographic — hidden sources
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients, families, and pharmacists
VISUAL GOAL: "You may already be taking magnesium without knowing it — and it all counts the same."

PROMPT:
Patient-education infographic poster, landscape 16:9, modern nephrology clinic aesthetic, on a clean WHITE
background, 1792×1024.

TOP HEADER, bold Inter, navy #0f1e2e:  "Magnesium hides in ordinary products"
Sub-line, clinical teal #1a6b72:       "Every one of these counts toward your total. Tell your kidney team about all of them."

MAIN BODY: six evenly sized rounded cards in a single tidy row of six (or two rows of three), each on a very
soft gray #f3f4f6 fill with a thin teal top accent band. Each card holds one simple flat vector icon in
teal #1a6b72 plus a short bold navy label and one short plain line beneath it:

  1. Icon: a bottle tipping into a spoon      Label: "Milk of magnesia"        Line: "A magnesium laxative."
  2. Icon: a chewable tablet with a flame     Label: "Antacids"                Line: "Often magnesium-based."
  3. Icon: a large drink jug                  Label: "Bowel preparation"       Line: "A very large load, quickly."
  4. Icon: a sachet with a crescent moon      Label: "Sleep & 'calm' powders"  Line: "Usually magnesium plus extras."
  5. Icon: a sports sachet in water           Label: "Electrolyte mixes"       Line: "May add sodium and potassium."
  6. Icon: a multivitamin tablet              Label: "Multivitamins"           Line: "Small, but it stacks."

All product depictions are generic and UNBRANDED — no readable brand names, no real packaging designs, no logos.

BOTTOM STRIP: a full-width soft gray band with one centred take-home line in navy Inter:
  "If it contains magnesium, it counts — even if nobody calls it a supplement."

Clean modular layout, rounded cards, generous whitespace, mobile-readable labels, publication-grade design.
Small semi-transparent navy "renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI-gibberish text, overprocessed HDR, generic stock-photo
look, excessive saturation. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito Sans/
IBM Plex Sans/Manrope. NO brand names, NO real packaging, NO price tags, NO shopping carts. NO milligram figures,
NO dose numbers, NO CKD stages. NO red X or "forbidden" symbols over the products — these are ordinary items the
reader may legitimately be using; the message is *declare them*, not *they are bad*. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Exactly six cards, evenly weighted, none singled out as worse. Icons unbranded and generic. Mobile-readable at
thumbnail size. Tone is "tell your team," not "stop taking these." Light background. renalcarematters.com
bottom-right.
```

---

## 6 · The elemental ladder — 17 forms by magnesium content *(add — § 6)*

> **Skill:** `williamriveromd-simple-figure` · Scaffold E (reference table / quick-look card), portrait
> **This is the anchor figure of the guide** and the visual twin of `calc-magnesium-replacement.html`.
> Percentages below are computed from molecular weight and are verified — reproduce them exactly.

```
FILE NAME: magnesium-supplements-ckd-04-elemental-ladder.png
IMAGE TYPE: Reference card — elemental magnesium content by salt form
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: patients, clinicians, pharmacists
VISUAL GOAL: "The percentage is chemistry, not merit — this ladder ranks magnesium content and nothing else."

PROMPT:
Clinical reference card, publication-grade nephrology design, on a WHITE #ffffff background, portrait 1024×1536.

TITLE, bold Inter, navy #0f1e2e:  "How much magnesium is actually in it?"
SUB-LINE, clinical teal #1a6b72:  "Elemental magnesium by weight. This ranks chemistry, not benefit."

MAIN BODY: a clean two-column horizontal bar chart, one row per magnesium salt, sorted from highest elemental
percentage at the top to lowest at the bottom. Left column: the salt name in bold navy. Right column: a
horizontal bar in clinical teal #1a6b72 whose length is proportional to the percentage, with the percentage
printed at the bar's end in bold navy. Alternate very soft gray #f3f4f6 row fills for readability. Render
these seventeen rows with exactly these values:

  Magnesium oxide                         60.3%
  Magnesium hydroxide                     41.7%
  Magnesium carbonate                     28.8%
  Magnesium chloride (anhydrous)          25.5%
  Magnesium sulfate (anhydrous)           20.2%
  Trimagnesium dicitrate                  16.2%
  Magnesium malate                        15.5%
  Magnesium bisglycinate                  13.9%
  Magnesium lactate                       12.0%
  Magnesium chloride hexahydrate          12.0%
  Magnesium citrate (1:1)                 11.3%
  Magnesium sulfate heptahydrate (Epsom)   9.9%
  Magnesium taurate                        8.9%
  Magnesium aspartate                      8.4%
  Magnesium L-threonate                    8.3%
  Magnesium orotate                        7.3%
  Magnesium gluconate                      5.9%

Every bar is the SAME teal colour — no bar is green, gold, highlighted, starred, or otherwise marked as better.

FOOTER BAND, soft gray, two short lines in navy Inter:
  "Higher percentage means more magnesium per gram — it does not mean better absorbed, safer, or more effective."
  "Hydrated salts carry water weight, which is why Epsom salt looks weak per gram."

Compact, well-organised, mobile-readable, not cluttered. Small semi-transparent navy "renalcarematters.com"
attribution at the bottom-centre (portrait format).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI-gibberish text, overprocessed HDR, excessive saturation.
NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope — no
serif. Do NOT alter, round differently, reorder, or invent any of the seventeen percentage values. NO trophy,
crown, podium, gold star, #1 badge, or green check on any row. NO colour-coding rows by benefit. NO dose
recommendation, NO milligram-per-day figure, NO CKD stages. NO organ icons beside any salt. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Seventeen rows, values exactly as listed, sorted high to low. All bars identical in colour — no row visually
favoured. Footer explicitly separates "more magnesium per gram" from "better." Legible on a phone.
renalcarematters.com bottom-centre.
```

---

## 7 · Claim check — marketing against evidence *(add — § 7)*

> **Skill:** `williamriveromd-simple-figure` · Scaffold B (side-by-side comparison), landscape
> **The single most guardrail-sensitive asset in the set.** The three evidence labels are fixed wording.

```
FILE NAME: magnesium-supplements-ckd-05-claim-check.png
IMAGE TYPE: Side-by-side comparison — claim versus evidence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: "Six popular claims, each graded honestly — and only one of them is actually supported."

PROMPT:
Medical education comparison infographic, graphical-abstract style, on a WHITE #ffffff background, 1792×1024.

TITLE centred at top, bold Inter, navy #0f1e2e:  "What the claims say, and what the evidence shows"

MAIN BODY: six horizontal rows. Each row is split by a soft dashed vertical divider into two unequal panels.

  LEFT PANEL (~40%), on a muted soft gray #f3f4f6 fill, text in ITALIC slate gray #6b7684, small quotation
  marks — deliberately quieter and less authoritative than the right panel. This is the marketing claim.

  RIGHT PANEL (~60%), on white, text in navy #0f1e2e — the evidence. Each right panel begins with a small
  rounded evidence badge, then one short plain-language line.

Use EXACTLY these three badge labels and no others — "Supported" (renal green #1f7a4d fill, white text),
"Partly supported" (amber #b8860b fill, white text), "Not established" (slate #6b7684 outline, slate text):

  Row 1  Claim: "Best for sleep"                 → Badge: Not established  · "Three small trials, low certainty."
  Row 2  Claim: "Calms anxiety"                  → Badge: Not established  · "Trials too small and too mixed."
  Row 3  Claim: "Stops muscle cramps"            → Badge: Not established  · "Cramps do not prove deficiency."
  Row 4  Claim: "Sharpens memory"                → Badge: Not established  · "Animal and early human data only."
  Row 5  Claim: "Lowers blood pressure"          → Badge: Partly supported · "Real but small — about 2 mmHg."
  Row 6  Claim: "Relieves constipation"          → Badge: Supported        · "A genuine laxative effect."

Beneath row 6, a full-width soft gray footer band with one line in navy Inter:
  "'Not established' means the evidence is insufficient — not that it has been disproved."

Rounded panel corners, ample negative space, mobile-readable labels, clean modular layout. Small semi-transparent
navy "renalcarematters.com" attribution bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI-gibberish text, overprocessed HDR, excessive saturation.
NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope — no
serif. Use ONLY the three badge labels "Supported", "Partly supported", "Not established" — never "debunked",
"myth", "false", "doesn't work", "proven", or any fourth label. NO red X marks, NO crossed-out claims, NO
thumbs-down. NO salt or form names anywhere on this figure — it grades claims, not products. NO dose numbers,
NO CKD stages. The left claim panel must never look more authoritative than the right evidence panel.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Six rows, claim left in muted italic gray, evidence right in confident navy. Exactly three badge labels used,
worded exactly as specified. The footer sentence distinguishing "not established" from "disproved" is present
and legible. No product or salt named. renalcarematters.com bottom-right.
```

---

## 8 · The label that lies by omission *(add — § 8)*

> **Skill:** `williamriveromd-simple-figure` · Scaffold B (side-by-side comparison)
> Reproduces the guide's worked example exactly. Verified against the calculator: 1,500 mg trimagnesium
> dicitrate × 16.2% ≈ **242 mg** elemental, which the guide rounds to the label-typical 240 mg.

```
FILE NAME: magnesium-supplements-ckd-06-label-explainer.png
IMAGE TYPE: Side-by-side comparison — front of bottle versus Supplement Facts panel
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients, families, pharmacists
VISUAL GOAL: "The big number on the front is the salt. The small number on the back is the magnesium."

PROMPT:
Medical education comparison infographic on a WHITE #ffffff background, 1792×1024, clean and highly legible.

TITLE centred at top, bold Inter, navy #0f1e2e:  "The number on the front is not the dose"

MAIN BODY: two large rounded panels side by side, separated by a bold navy right-pointing arrow in the centre
gutter.

LEFT PANEL, labelled in slate gray #6b7684 above it: "WHAT THE FRONT SAYS"
  A clean generic UNBRANDED supplement bottle rendered as a simple flat vector shape in soft gray, with one
  large bold line of text across it in navy:  "Magnesium citrate 1,500 mg"
  Beneath the bottle, in italic slate gray:   "The weight of the whole compound"

RIGHT PANEL, labelled in clinical teal #1a6b72 above it: "WHAT THE PANEL SAYS"
  A clean simplified Supplement Facts table rendered as a white card with thin navy rules — a header row reading
  "Supplement Facts", then one highlighted data row on a pale amber #fdf6e3 fill reading:
    "Magnesium        240 mg"
  Beneath the table, in navy:                 "The dose that actually matters"

BOTTOM STRIP: a full-width soft gray band carrying one bold centred line in navy Inter:
  "Same bottle. 1,500 mg of salt — 240 mg of magnesium."

Generous negative space, rounded corners, mobile-readable type at ≥11pt equivalent, publication-grade layout.
Small semi-transparent navy "renalcarematters.com" attribution bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI-gibberish text, overprocessed HDR, excessive saturation.
NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope — no
serif. The bottle must be generic and UNBRANDED — no real brand name, no logo, no trade dress. Print ONLY the
two figures 1,500 mg and 240 mg — no daily dose, no "take X per day", no tablet count, no CKD stage, no other
milligram value. NO red X, NO "scam" or "warning" framing — the label is not deceptive, it is simply misread.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Two panels, clear left-to-right arrow. Exactly two numbers on the whole image: 1,500 mg and 240 mg. Bottle is
unbranded. The bottom line lands the contrast in one sentence. Legible at phone width. renalcarematters.com
bottom-right.
```

---

## 9 · Medication spacing quick card *(add — § 10)*

> **Skill:** `williamriveromd-simple-figure` · Scaffold E (reference table), 4:3
> Spacing figures are the NIH Office of Dietary Supplements values cited in the guide — reproduce exactly.

```
FILE NAME: magnesium-supplements-ckd-07-interaction-spacing.png
IMAGE TYPE: Clinician/patient reference card — magnesium drug interactions and spacing
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients, families, pharmacists
VISUAL GOAL: "Two interactions need clock spacing; the rest need a conversation."

PROMPT:
Clinical reference card, publication-grade nephrology design, on a WHITE #ffffff background, 1536×1152.

TITLE, bold Inter, navy #0f1e2e:  "Magnesium and your other medicines"
SUB-LINE, clinical teal #1a6b72:  "Bring your full medication list to a pharmacist."

MAIN BODY: a compact clean table with three columns — "Medicine", "What happens", "What to do" — with column
headers in white on a clinical teal #1a6b72 header bar, alternating white and very soft gray #f3f4f6 row fills,
and thin navy rules. Seven rows:

  1. "Tetracycline & quinolone antibiotics" | "Magnesium binds the antibiotic and less is absorbed"
     | "Antibiotic at least 2 hours before, or 4–6 hours after"   ← print this cell in bold amber #b8860b
  2. "Oral bisphosphonates"                 | "Absorption reduced"
     | "Separate by at least 2 hours"                             ← print this cell in bold amber #b8860b
  3. "Loop & thiazide diuretics"            | "Increase urinary magnesium loss"        | "Monitor — not automatic supplementation"
  4. "Potassium-sparing diuretics"          | "Reduce urinary magnesium loss"          | "Monitor"
  5. "Proton pump inhibitors"               | "Long-term use can lower magnesium"      | "Mention it if you have taken one for years"
  6. "Magnesium antacids & laxatives"       | "Add to your total magnesium exposure"   | "Count them — they are the commonest hidden source"
  7. "Calcium supplements"                  | "Routine blocking is overstated"         | "Follow product instructions; ask if doses are high"

BOTTOM BAND, soft gray, one centred line in navy Inter:
  "Only the first two rows need clock spacing. The rest need a conversation, not a stopwatch."

Compact, well-organised, mobile-readable, not cluttered. Small semi-transparent navy "renalcarematters.com"
attribution bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI-gibberish text, overprocessed HDR, excessive saturation.
NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope — no
serif. Do NOT invent additional interactions, drug names, or spacing intervals beyond the seven rows written
above. NO magnesium dose figures, NO CKD stages, NO drug dosages. Do NOT render rows 3–7 with clock icons or
hour figures — only rows 1 and 2 involve timed spacing. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Seven rows, three columns, wording exactly as specified. Only rows 1 and 2 carry amber timing emphasis. No
invented interactions or intervals. Bottom line prevents over-generalising the spacing rule. Legible on a
phone. renalcarematters.com bottom-right.
```

---

## 10 · Safer decision pathway *(add — § 11)*

> **Skill:** `williamriveromd-algorithm-generator-skill` · **Style Mode C — renalcarematters.com house style**
> (branded, patient-facing; not the AHA emergency style, not the journal treatment style)

```
FILE NAME: magnesium-supplements-ckd-08-decision-pathway.png
IMAGE TYPE: Clinical algorithm flowchart — house style (Style Mode C)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: patients and families
VISUAL GOAL: "The first question can end the process — and for many readers of this page, it should."

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style, portrait
1024×1536, on a white or very light off-white background. Restrained navy and teal typography set in Inter,
thin teal connector arrows, generous margins, centred and symmetrical, suitable for a patient-facing nephrology
education guide.

TITLE at top, bold navy #0f1e2e:  "Should I be taking magnesium at all?"

Top-to-bottom flow, five numbered decision points. Use rounded rectangles for questions and endpoints and a
diamond for the single true branch point at step 1.

  STEP 1 — teal #1a6b72 diamond decision node:
    "Do you have kidney disease, dialysis, a transplant, a reduced eGFR, a past high magnesium result —
     or simply not know?"
    → A prominent branch labelled "YES or NOT SURE" in bold red #b91c1c leads immediately to a RED-bordered
      terminal endpoint box, drawn LARGER and more visually dominant than any other node on the page:
        "STOP. Do not self-start. Ask your kidney team or pharmacist."
      This endpoint is the visual anchor of the whole chart.
    → A quieter branch labelled "NO" continues downward to step 2.

  STEP 2 — navy action node:
    "Are you trying to treat a symptom?"
    with a small teal side-note box: "Then look for the symptom's common causes first — not a deficiency."

  STEP 3 — navy action node:
    "Is deficiency actually plausible or documented?"
    with a small teal side-note box: "Diarrhea, malabsorption, diabetes, alcohol, certain medicines."

  STEP 4 — navy action node:
    "Has a clinician recommended a product?"
    with a small teal side-note box: "Then compare elemental magnesium, bowel effects, and interactions."

  STEP 5 — red #b91c1c bordered safety endpoint at the bottom:
    "New weakness, vomiting, marked sleepiness, low blood pressure, slow breathing, or irregular heartbeat?
     Stop the product and seek urgent medical advice."

Consistent node widths, consistent vertical spacing, no spaghetti routing, maximum three branching levels,
strong use of negative space. Include a small professional footer reading "© renalcarematters.com" at the
bottom-right in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid decorative icons, photographs, 3D elements, dark backgrounds, heavy shadows, cartoon styling, clutter, and
photorealistic people. Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope — never a serif font. NO dose numbers,
NO milligram figures, NO daily targets, NO CKD stage numbers, NO eGFR threshold values, NO serum magnesium
cut-offs. NO branch that ends in "so take magnesium" — no node on this chart may recommend starting a
supplement. NO product or salt names. Never omit the © renalcarematters.com footer.

QUALITY CHECK:
Five steps, top-to-bottom, one true branch at step 1. The red STOP endpoint at step 1 is the largest and most
prominent node on the page. No node recommends starting magnesium. No numeric thresholds anywhere. Reads
cleanly at thumbnail size. © renalcarematters.com bottom-right.
```

---

## Production checklist (after generating in GPT)

1. **Generate** each prompt in the ChatGPT Image Generator GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
2. **Save** every asset under `images/` as **both** `.png` and a `.webp` twin, using the exact FILE NAME above.
3. **Swap the hero and OG card.** Both currently point at the shared category placeholder. In
   `guides/magnesium-supplements-ckd.html` replace `hero-cat-electrolytes` with the new hero in the
   `figure.hero-figure` block, and update the four social tags in `<head>`:
   ```
   og:image        → https://renalcarematters.com/images/magnesium-supplements-ckd-og.png
   og:image:width  → 1200
   og:image:height → 630
   twitter:image   → https://renalcarematters.com/images/magnesium-supplements-ckd-og.png
   ```
   Do the same swap in `guides/calc-magnesium-replacement.html`, which shares the placeholder.
4. **Wire assets 3–10 inline.** Each goes inside its section as a `<figure>` with a `<picture>` (webp `<source>`
   + png `<img>`), a descriptive `alt`, and — **required by CLAUDE.md rule 11** — a `<figcaption>` containing a
   `<p class="fig-desc">` plain-language description. Assets 4, 6, 7 and 9 contain acronyms or abbreviations and
   therefore also need a `<dl class="fig-abbrevs">` block so the lightbox can render the abbreviation panel.
   Mirror each `fig-desc` into TL/CEB/KAP sibling spans — this guide is four-language throughout.
5. **Re-run the pipeline** after wiring, in this order:
   ```bash
   python3 patch_hero_fetchpriority.py --guide magnesium-supplements-ckd.html
   python3 patch_hero_fullwidth.py     --guide magnesium-supplements-ckd.html
   python3 patch_hero_maxwidth.py      --guide magnesium-supplements-ckd.html
   python3 patch_image_lightbox.py     --guide magnesium-supplements-ckd.html
   python3 patch_reading_time.py       --guide magnesium-supplements-ckd.html
   python3 audit_acronym_expansion.py  --guide magnesium-supplements-ckd.html
   python3 generate_latest_guides.py
   ```
6. **Check dark mode.** Every asset has a light background by house rule, so each needs a container that does not
   strand it on a dark surface — use `.illus-wrap illus-wrap-light`, which master CSS already remaps for dark mode.

## Verify-before-ship (clinical, per `medical-teaching-standard`)

- [ ] **No image recommends a magnesium dose**, a daily target, or a per-stage amount. Check every asset again
      specifically for this — it is the guide's central editorial commitment.
- [ ] **No image ranks forms by benefit.** Asset 6 ranks by elemental percentage only, all bars one colour, and
      its footer explicitly separates "more per gram" from "better."
- [ ] **The seventeen percentages in asset 6 match the calculator exactly.** Cross-check against `MG_FORMS` in
      `guides/calc-magnesium-replacement.html`; regenerate if the model altered, reordered, or rounded any value.
- [ ] **Asset 7 uses exactly three badge labels**, worded *Supported · Partly supported · Not established*, and
      carries the "insufficient, not disproved" footer.
- [ ] **Asset 4 invents no transporter names and prints no numeric thresholds**; the thick ascending limb is the
      dominant reabsorption site; the narrowed-adaptation contrast is the clearest thing on the figure.
- [ ] **Asset 9's spacing intervals match the guide text** (antibiotics ≥2 h before or 4–6 h after;
      bisphosphonates ≥2 h) and no additional interactions were invented.
- [ ] **Asset 10 contains no branch that ends in "take magnesium"**, and its step-1 STOP endpoint is the most
      prominent node.
- [ ] **No brand names, packaging, price tags, or shopping cues** on any asset.
- [ ] **Every asset carries `renalcarematters.com`** bottom-right (bottom-centre for the two portrait assets),
      except the wordless vignette hero.
- [ ] **All on-image type is Inter / Nunito Sans / IBM Plex Sans / Manrope.** No serif anywhere.
