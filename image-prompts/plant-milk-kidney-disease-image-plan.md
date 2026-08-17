# Image Plan — `plant-milk-kidney-disease.html`

**Guide:** *Plant Milk & Your Kidneys: The Additive Problem No Label Warns You About*
**Audience:** Dual (patient-facing + clinician evidence layer) · **Category:** Nutrition
**Production target:** ChatGPT Image Generator GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
**House rules (all images):** light backgrounds only; sans-serif type only (Inter / Nunito Sans / IBM Plex Sans / Manrope); `renalcarematters.com` attribution bottom-right (bottom-center for portrait) — **except the wordless circular vignette hero, which carries no text at all.**

---

## Blueprint at a glance

| # | File | Type / Skill | Size | Placement in guide | Status |
|---|---|---|---|---|---|
| 1 | `plant-milk-kidney-disease-vignette-hero.png` | Circular vignette hero (still-life) · *hero-vignette* | 2048×2048 | Hero disc (already wired) | **wired** |
| 2 | `plant-milk-kidney-disease-og.png` | OG / social share card · *infographic* | 1200×630 | `og:image` / Twitter (already referenced) | **wired** |
| 3 | `plant-milk-kidney-disease-00-hero-editorial.png` | Photoreal editorial opener · *infographic* | 1536×1024 | §The Myth (`#myth`) — already wired | **wired** |
| 4 | `plant-milk-kidney-disease-01-phosphorus-bioavailability.png` | Comparison panel · *simple-figure* | 1792×1024 | §The Real Test (`#two-numbers`) | new figure |
| 5 | `plant-milk-kidney-disease-02-milk-comparison-matrix.png` | Food matrix · *infographic* | 1536×1152 | §Milk by Milk (`#compare`) | new figure |
| 6 | `plant-milk-kidney-disease-03-read-the-label.png` | Annotated one-panel · *simple-figure* | 1792×1024 | §Read the Carton (`#red-flags`) | new figure |
| 7 | `plant-milk-kidney-disease-04-gut-kidney-axis.png` | Organ-crosstalk sigil · *organ-crosstalk* | 1024×1024 | §Evidence by Variable (clinician `#md-evidence`) | new figure |

> Images 1–3 are already referenced by the HTML; generate and drop them in.
> Images 4–7 are new in-body figures — generate them, then wire a `<figure>` (with a
> `<figcaption class="fig-desc">` + `<dl class="fig-abbrevs">`) into the mapped section.
> Each `<figure>` also needs `patch_hero_fetchpriority.py` skipped (only the hero is LCP);
> run `patch_image_lightbox.py` is already satisfied (script tag present).

---

## 1 — Circular vignette hero

```
FILE NAME: plant-milk-kidney-disease-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: slightly elevated three-quarter still-life
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: patients
VISUAL GOAL: At a glance — "the truth about this milk is on the back of the carton, not the front."

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE
BORDER around the full circle (the circle must never touch the canvas edges). Composition
archetype: Object Hero. Camera: slightly elevated three-quarter still-life.

Subject: a single clean arrangement of three or four plain, unbranded non-dairy milk
cartons (oat, almond, soy, coconut — different pastel carton heights, NO readable brand
text) standing on a soft, uncluttered light teal-tinted surface, with one carton turned
to reveal a blank nutrition/ingredient panel and a simple magnifying glass resting against
it, its lens gently enlarging the blank panel. A couple of loose almonds and two oat grains
sit as small supporting props near the base; a faint, tasteful pale-teal silhouette of a
pair of kidneys is suggested as soft out-of-focus background texture on the lower right.

Visual hierarchy: the carton cluster + magnifier occupy 60–70% of the circle; 2–4 small
supporting props (almonds, oats, soft kidney silhouette) 20–30%; reserve a 20–25% TITLE
SAFE ZONE of empty soft-gradient surface across the upper-left (no objects, labels, or
icons in that zone) so the HTML title can sit beside the disc. Soft edge falloff toward a
slightly deeper neutral at the rim. Light, calm, clean editorial colour grade harmonizing
with clinical teal #1a6b72 and renal green #1f7a4d on a bright background; soft daylight,
gentle shallow depth of field.

Absolutely NO readable text or labels on the cartons or panel (no packaging copy you can
read), no titles, no logos, no watermark. Full-bleed within the inscribed circle, no
rectangular borders, frames, or banners.

NEGATIVE INSTRUCTIONS:
Avoid: busy layouts; collage overload; more than four supporting scenes; dozens of icons;
tiny unreadable labels; infographic clutter; duplicated people; repeated compositions;
cropped circle; cropped objects; edge clipping; objects touching the circular border;
important content inside the title safe zone; baked-in text, titles, captions, logos,
watermarks; rectangular borders, frames, banners; dark / charcoal / black backgrounds;
cartoon style, neon, HDR, over-saturation; distorted or implausible objects.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never
cropped. ONE dominant subject (carton cluster + magnifier) at 60–70% of the circle, 2–4
supporting props, 20–25% empty title-safe zone reserved (soft gradient, no objects). No
readable packaging text anywhere. Crops cleanly inside the circle with nothing lost at the
edges. Wordless.
```

---

## 2 — OG / social share card

```
FILE NAME: plant-milk-kidney-disease-og.png
IMAGE TYPE: OG / social share card (Photorealistic editorial hero + title)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed (social share)
VISUAL GOAL: Stop the scroll with the core thesis — "dairy-free" is not "kidney-safe"; the risk is in the ingredient list.

PROMPT:
Photorealistic medical editorial OG share card, 1200×630, bright airy studio-lit still-life
on a clean off-white (#fafafa) background. LEFT 55%: a neat row of three or four plain,
unbranded pastel non-dairy milk cartons (oat, almond, soy, coconut) with one carton turned
to show its back panel, and a realistic magnifying glass held over that panel — inside the
lens, a few short ingredient lines are subtly legible with the fragment "…phosphate…"
faintly highlighted in clinical red (#b91c1c). A soft, tasteful pale-teal 3D silhouette of
a pair of kidneys floats as a light background motif behind the cartons.

RIGHT 45%: clean typographic block on the light background. Title in bold navy (#0f1e2e)
Inter: "Plant Milk & Your Kidneys". Beneath it, a thinner navy/teal subtitle in Inter:
"The additive problem no label warns you about." A short clinical-teal (#1a6b72) rule
separates title and subtitle. One small amber (#b8860b) pill reads "READ THE INGREDIENTS,
NOT THE PANEL".

Premium nephrology-education aesthetic, restrained, generous negative space, mobile-legible
type, navy/teal/green/amber accents only. Bottom-right: "renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use
dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif
fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative
typefaces. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Title/subtitle spelled correctly and mobile-readable. Light background.
Only the intended words render (no gibberish). renalcarematters.com bottom-right.
```

---

## 3 — In-body editorial opener (§The Myth)

```
FILE NAME: plant-milk-kidney-disease-00-hero-editorial.png
IMAGE TYPE: Photorealistic editorial opener (still-life / lifestyle)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: patients
VISUAL GOAL: "The front of the carton sells a story; the back tells the truth" — a shopper checking the ingredient list.

PROMPT:
Photorealistic editorial photograph for a nephrology nutrition guide, bright and airy,
1536×1024, on a clean light supermarket-aisle or kitchen-counter setting with soft natural
daylight and gentle shallow depth of field. A neat row of four plain, unbranded pastel
non-dairy milk cartons (oat, almond, soy, coconut) stands on a light shelf. A Filipino
adult's hands (natural skin texture, realistic) hold one carton turned to its back and a
simple magnifying glass over the ingredient panel; the person is softly out of focus behind
the cartons — the hands and cartons are the subject. Two loose almonds and a small heap of
oats sit as props. Colour grade calm and trustworthy, harmonizing with clinical teal
#1a6b72 and renal green #1f7a4d on a bright background.

No readable brand names or packaging copy anywhere (blank/blurred panels). No embedded
title text. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid unrealistic anatomy or distorted hands, avoid overprocessed HDR, avoid excessive
saturation, avoid stock-photo blandness. NEVER use dark, navy, charcoal, or black
backgrounds — light backgrounds only. Sans-serif only if any text appears. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
3:2 1536×1024. Realistic hands, plausible cartons, no readable brand text. Bright light
setting. renalcarematters.com bottom-right.

FIGCAPTION (for the HTML, once generated):
  fig-desc: "A shopper turns the carton over to read the ingredient list — where the real
  kidney story is told, not on the marketing front."
```

---

## 4 — Phosphorus bioavailability comparison (§The Real Test)

```
FILE NAME: plant-milk-kidney-disease-01-phosphorus-bioavailability.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison (three-tier + callout)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patient-friendly, clinician-accurate)
VISUAL GOAL: Not all phosphorus is equal — the ADDED (inorganic) kind is nearly fully absorbed, and it makes additive plant milks rival cow's milk.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white
(#ffffff) background, 1792×1024. Title centered at top in bold navy (#0f1e2e) Inter:
"Not all phosphorus is absorbed the same way". Subtitle in clinical teal (#1a6b72):
"How much your gut absorbs depends on the source".

MAIN ROW — three rounded cards left to right, each with a simple horizontal fill bar showing
the absorbed fraction (bar length = %):
  • Card 1 (clinical red #b91c1c), bar ~95%: "Inorganic phosphate ADDITIVES" — small caption
    "tricalcium phosphate, phosphoric acid, potassium phosphate" — big value "~90–100% absorbed".
  • Card 2 (amber #b8860b), bar ~50%: "Animal-protein-bound (dairy, meat)" — big value "~40–60%".
  • Card 3 (renal green #1f7a4d), bar ~30%: "Plant phytate-bound (nuts, grains)" — big value "~20–40%".

BOTTOM STRIP — soft gray (#f3f4f6) panel with two small opposed bars comparing measured
phosphorus in plant milks: a tall red bar labeled "WITH phosphate additive — 58.5 mg P/100g"
next to a short green bar labeled "Additive-free — 7.4 mg P/100g", and a short navy caption:
"Some fortified plant milks deliver MORE absorbed phosphorus than cow's milk."

Clean modular cards, generous whitespace, mobile-readable labels in Inter, navy/teal/green/
amber/red palette. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use
dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter, Nunito
Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9 1792×1024. Bar lengths match the stated percentages. Numbers spelled exactly
(90–100%, 40–60%, 20–40%, 58.5, 7.4). Light background, mobile-readable. renalcarematters.com
bottom-right.

FIGCAPTION (for the HTML):
  fig-desc: "Phosphorus from added (inorganic) phosphate is almost fully absorbed, unlike the
  phosphorus naturally locked in plants — which is why a fortified plant milk can carry a
  bigger absorbed phosphorus load than cow's milk."
  fig-abbrevs: P = phosphorus.
```

---

## 5 — Milk-by-milk comparison matrix (§Milk by Milk)

```
FILE NAME: plant-milk-kidney-disease-02-milk-comparison-matrix.png
IMAGE TYPE: Food matrix / nutrition infographic (archetype 6)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients
VISUAL GOAL: One scannable grid of the eight common plant milks across the parameters CKD cares about.

PROMPT:
CKD nutrition infographic, clean educational food matrix, white (#ffffff) background,
1536×1152. Title at top in bold navy (#0f1e2e) Inter: "Plant milks, side by side".
Subtitle in clinical teal (#1a6b72): "Categories, not brands — always confirm the carton".

A tidy 8-row table with a small realistic glass/carton thumbnail per row and four columns.
Column headers in teal on soft-gray (#f3f4f6): "Protein / cup", "Oxalate", "Phosphate-additive
risk", "Best fit". Rows (top to bottom): Soy, Oat, Macadamia, Coconut, Almond, Cashew, Hemp,
Rice. Fill the cells with short chips:
  • Soy — "7–8 g" (green), "Moderate", "Only if fortified", chip "Best all-round" (green).
  • Oat — "1–3 g", "Low", "Common", chip "Good if additive-free" (teal).
  • Macadamia — "1 g", "Low", "Variable", chip "Good if additive-free" (teal).
  • Coconut — "0–1 g", "Very low", "Variable", chip "Portion matters" (amber).
  • Almond — "1 g", "Highest" (red), "Common", chip "Caution: stones" (amber).
  • Cashew — "1 g", "High" (red), "Common", chip "Caution: stones" (amber).
  • Hemp — "2–3 g", "Low", "Variable", chip "Reasonable" (teal).
  • Rice — "0–1 g", "Low", "Common", chip "Not for young children" (red).

Alternating white / very-soft-gray row fills, rounded corners, mobile-readable Inter labels,
navy/teal/green/amber/red palette, generous whitespace. Bottom strip navy caption: "Unsweetened
soy is the only plant milk that matches dairy's protein." Bottom-right: "renalcarematters.com"
in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid brand logos or readable brand names, avoid overprocessed HDR, avoid excessive
saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
4:3 1536×1152. Eight rows, four columns, values match exactly. No brand names. Light
background, mobile-readable. renalcarematters.com bottom-right.

FIGCAPTION (for the HTML):
  fig-desc: "The eight common plant milks compared on protein, oxalate, phosphate-additive
  risk, and best-fit — a generic guide to read alongside any carton's ingredient list."
```

---

## 6 — Read-the-label scan (§Read the Carton)

```
FILE NAME: plant-milk-kidney-disease-03-read-the-label.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side (clean list vs flagged list)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients
VISUAL GOAL: Teach the 10-second shelf check — scan the ingredient list for "phos" and "carrageenan".

PROMPT:
Medical education comparison infographic, white (#ffffff) background, 1792×1024. Title
centered at top in bold navy (#0f1e2e) Inter: "Read the ingredient list, not the panel".
A soft dashed vertical divider splits the canvas into two equal ingredient-panel mockups,
each drawn as a simple rounded carton back-label card with a short bulleted ingredient list
in clean Inter.

LEFT panel, header in renal green (#1f7a4d): "CLEANER CHOICE" — ingredient list reads:
"Water · Soybeans · Calcium carbonate" with a green check badge.
RIGHT panel, header in clinical red (#b91c1c): "PUT IT BACK" — ingredient list reads:
"Water · Oats · Dipotassium phosphate · Tricalcium phosphate · Sugar · Carrageenan", with
a simple magnifying-glass graphic hovering and the words "dipotassium phosphate",
"tricalcium phosphate" and "carrageenan" circled/highlighted in red.

Small bottom strip in soft gray (#f3f4f6): navy caption "Scan for any word with 'phos' —
and for 'carrageenan'." Rounded panels, ample negative space, mobile-readable ≥11pt labels,
navy/teal/green/red palette. Bottom-right: "renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid brand logos or readable brand names, avoid overprocessed HDR, avoid excessive
saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
16:9 1792×1024. Both ingredient lists spelled exactly as given; the flagged words are the
ones highlighted in red. Light background, mobile-readable. renalcarematters.com bottom-right.

FIGCAPTION (for the HTML):
  fig-desc: "A clean plant-milk ingredient list (water, soybeans, calcium carbonate) beside a
  flagged one — showing the 'phos' words and carrageenan to scan for and avoid."
  fig-abbrevs: (none)
```

---

## 7 — Gut–kidney axis sigil (clinician §Evidence by Variable)

```
FILE NAME: plant-milk-kidney-disease-04-gut-kidney-axis.png
IMAGE TYPE: Organ-crosstalk sigil (monoline, labelled)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians
VISUAL GOAL: The mechanistically-coherent (but CKD-unproven) additive → gut barrier → uremic-toxin → vascular-inflammation pathway, hedged as such.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration on a white background, 1024×1024.

ORGANS (minimal monoline line-art, thin clean strokes, soft teal-blue palette):
- a simplified intestine/gut coil at the upper center
- a pair of kidneys at the lower left
- a heart-with-vessel-segment icon at the lower right

RELATIONSHIP:
Show a downward/around dotted-arrow pathway: from a small "plant-milk carton + additive"
mark feeding INTO the gut, then dotted arrows from the gut to the kidneys and to the
heart/vessel, forming a gentle triangular loop. Along the arrows, place four short
sans-serif (Inter) labels in muted navy: near the gut "barrier disruption · dysbiosis
(carrageenan)"; along the gut→kidney arrow "gut-derived uremic toxins — indoxyl sulfate,
p-cresyl sulfate"; near the heart/vessel "vascular inflammation"; and a small amber tag on
the whole loop reading "mechanistic — not yet proven in CKD".

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette on white
background, clean rounded organ shapes, balanced sigil-like triangular composition, generous
whitespace, no photorealism, no 3D, no heavy shadows. All labels in Inter (sans-serif only).

COMPOSITION:
Gut at top center; kidneys lower-left, heart/vessel lower-right; dotted curved arrows form a
calm triangular loop with the additive input entering the gut from above. Symbolic,
educational, publication-grade medical-icon aesthetic. Include a small, semi-transparent
"renalcarematters.com" attribution in the bottom-right corner, not obscuring the sigil.

NEGATIVE INSTRUCTIONS:
Avoid: photorealistic anatomy, surgical detail, excessive labels, dark background, neon
colors, complex infographics, crowded arrows, thick cartoon outlines, 3D rendering, glossy
icons, dramatic lighting, stock-photo style. Serif or decorative fonts forbidden — Inter,
Nunito Sans, IBM Plex Sans, or Manrope only. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
1:1 1024×1024. Three organ icons + additive input, dotted triangular loop, four short
correctly-spelled labels, the amber "not yet proven in CKD" hedge present. White background,
monoline aesthetic. renalcarematters.com bottom-right.

FIGCAPTION (for the HTML):
  fig-desc: "A schematic of the gut–kidney axis: plant-milk additives such as carrageenan may
  disrupt the intestinal barrier and shift the microbiome, raising gut-derived uremic toxins
  that drive vascular inflammation — a mechanistically coherent but not-yet-CKD-proven pathway."
  fig-abbrevs: (spell out indoxyl sulfate / p-cresyl sulfate in the caption; both are gut-derived uremic toxins.)
```

---

## Production notes

- **Order of generation:** 1 (hero) → 2 (OG) → 3 (opener) first, since the HTML already
  points at them; then 4–7.
- **After generating each file:** save a `.png` and a `.webp` twin into `images/` using the
  exact file names above.
- **Wiring the new figures (4–7):** insert a `<figure>` with `<picture>` (webp source + png
  img, explicit `width`/`height`, descriptive `alt`) and the `<figcaption class="fig-desc">`
  text supplied per prompt; add a `<dl class="fig-abbrevs">` where noted. The lightbox script
  (`assets/image-lightbox.js`) is already loaded, so a structured figcaption lights up the
  caption panel automatically.
- **Text-accuracy risk:** prompts 4–6 embed exact numbers/words — regenerate if the model
  garbles any digit or ingredient name; the figures are only useful if the values are correct.
- **Consistency:** every panel keeps the shared light background, sans-serif type, and
  `renalcarematters.com` mark so the set reads as one system.
