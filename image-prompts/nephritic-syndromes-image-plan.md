# Image Plan: *Nephritic Syndrome: Recognize It, Act Fast, Find the Cause* (`nephritic-syndromes.html`)

**Guide:** Nephritic syndromes primer. Dual audience: Patients & Families (EN/TL/CEB/KAP) and Clinicians.
**Prepared:** 2026-11-10. **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the ChatGPT **Image Generator** GPT at https://chatgpt.com/
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` · `williamriveromd-biomedical-mechanism-figure` · `williamriveromd-algorithm-generator-skill` (Mode C) · `williamriveromd-local-image-generator` (schema and hand-off)

---

## Design intent: make an invisible leak visible, then make urgency obvious

Nephritic syndrome happens inside a structure no reader has ever seen: a filter one-tenth of a millimeter across. Most readers meet it as a frightening urine color or a lab number. The image set has three jobs, in order:

1. **Show the leak.** A healthy filter keeps red cells and protein in; an inflamed one lets red cells squeeze out bent and misshapen. Once a reader has seen that picture, "acanthocytes," "casts," and "glomerular bleeding" stop being jargon.
2. **Make urgency unmistakable for anyone who cannot read well.** One wordless-leaning pictogram card tells a patient, a grandparent, or a teenager when to go to the emergency room now.
3. **Give clinicians a map, not a rule.** The first-hours pathway, the cause map, and the biopsy panel organize reasoning without implying that complement or serology alone decides the diagnosis.

| Idea the reader must get | Patient image | Clinician image |
|---|---|---|
| The filter is inflamed, and red cells squeeze through and get bent | #3 Inflamed filter | #6 Mechanism |
| Nephritic (bleeding, high BP) is not nephrotic (heavy protein, heavy swelling) | #4 Two different leaks | — |
| **When to go to the ER now** | #5 Emergency pictograms | #7 First-hours algorithm (red branch) |
| One pattern has many causes; the cause decides treatment | #6 Many causes | #8 Cause map |
| What the lab sees under the microscope | #7 Urine clues | #8 / #9 |
| What helps while waiting for answers | #8 While you wait | — |
| Active lesions are treatable; scars are not | — | #9 Biopsy panel |

**Reading-level ladder.** Every patient image works at three levels at once:
1. **Picture level (no reading needed):** shape, color, and size carry the message (round cells stay in, bent cells squeeze out; a red-bordered card of four body pictograms means "go now").
2. **Label level (Grade 4–6 English):** no more than about 8 words per label, everyday words ("tiny filter," "blood leaks," "protein leaks"), no acronyms except IgA where unavoidable.
3. **Detail level:** the HTML caption and guide text carry the medical terms and numbers in four languages. Images carry English labels only, so one image serves EN/TL/CEB/KAP readers; the lightbox caption carries the translation.

Clinician images may use correct technical labels (GBM, ANCA, MPO, PR3, C3, C4, IFTA) but keep callouts short and every number traceable to the guide.

## House rules baked into every prompt
- **Light backgrounds only** (white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, pale teal `#eef6f7`). Never navy, charcoal, or black fills.
- **Font:** on-image type is set in **Inter** (named in each prompt). Approved alternatives: Nunito Sans, IBM Plex Sans, Manrope. No serif or decorative faces.
- **Palette:** navy `#0f1e2e` (text and accents only), clinical teal `#1a6b72` (filter, kidney, structure), renal green `#1f7a4d` (normal / safe / do this), orange `#c55a11` (inflammation and immune attack), purple `#6c3d8e` (protein / albumin), amber `#b8860b` (caution), red `#b91c1c` (emergency only).
- **Fixed color code across the set:** *soft red-pink discs = red blood cells* (round when healthy, bent and knobbed when they have squeezed through), *purple spheres = protein (albumin)*, *orange = inflammation and immune deposits*, *teal = the filter itself*. Readers learn it in #3 and reuse it in #4, #6, and #7.
- **Attribution:** small, semi-transparent `© renalcarematters.com`, bottom-right (bottom-center on portrait), on every image **except the wordless vignette hero**.
- **American English** in all rendered text (hemorrhage, edema, color, pediatric).
- **No journal names, guideline acronyms, drug brand names, or watermarks** in any rendered text.
- **Style:** illustrated and softly rendered (GPT-rendered editorial or semi-3D), not flat clip-art vector. Mechanism and biopsy figures follow the review-article schematic style with gentle shading.
- **Sizes:** in-body figures are declared **1536 × 1024** in the HTML (the Image Generator's native landscape size); the algorithm is **1024 × 1536** portrait; the hero is **2048 × 2048**; the OG card is **1200 × 630**.

### Clinical guardrails for THIS guide (each must hold in every graphic)
1. **No gore.** Urine is shown as tea- or cola-tinted liquid in a capped clear cup, never as bright red blood. No needles, no blood drops in the hero, no bleeding lungs drawn realistically (the coughing pictogram uses one small stylized droplet only).
2. **Red cells inside the filter are drawn correctly.** Healthy: smooth biconcave discs staying inside the capillary. Inflamed: discs squeezing through a small break in the wall and emerging **misshapen with small knob-like blebs** (acanthocytes); a cylinder-shaped **cast** forms downstream in the tubule, not inside the capillary.
3. **Complement is a clue, not an arrow to a diagnosis.** The cause map groups diseases under complement patterns in soft columns with a visible footer that these are clues; never draw a single arrow from "low C3" to one disease.
4. **No treatment selector.** No image tells the viewer which drug to use. Treatment appears only as generic categories (source control, immune treatment, plasma exchange, supportive care).
5. **Emergency card is unambiguous.** Exactly four symptoms, each a single large pictogram plus a 2–4 word label, a red border, and one destination: the emergency room. No numbers.
6. **No invented numbers.** No percentages, creatinine values, or titers unless written in the prompt.
7. **No brand names or readable packaging** on pills, kits, or devices.
8. **Filipino clinical context**, calm daylight, diverse cast that does not repeat the previous guide's people.

## Asset roster

| # | File (`images/…`) | Placement in guide | Skill | Size |
|---|---|---|---|---|
| 1 | `nephritic-syndromes-vignette-hero.png` | Patient hero disc | hero-vignette (Scaffold A, archetype J) | 2048×2048 |
| 2 | `nephritic-syndromes-og.png` | `og:image` / social share | infographic (OG card) | 1200×630 |
| 3 | `nephritic-syndromes-01-inflamed-filter.png` | Patient §What It Means | infographic (3D component, comparison) | 1536×1024 |
| 4 | `nephritic-syndromes-02-nephritic-vs-nephrotic.png` | Patient §Signs | infographic (split comparison) | 1536×1024 |
| 5 | `nephritic-syndromes-10-emergency-signs.png` | Patient §Signs (end) | infographic (pictogram warning card) | 1536×1024 |
| 6 | `nephritic-syndromes-08-many-causes.png` | Patient §Causes | infographic (radial, archetype C) | 1536×1024 |
| 7 | `nephritic-syndromes-03-urine-clues.png` | Patient §Tests | infographic (labeled microscopy schematic) | 1536×1024 |
| 8 | `nephritic-syndromes-09-while-you-wait.png` | Patient §What You Can Do | infographic (action tiles) | 1536×1024 |
| 9 | `nephritic-syndromes-04-mechanism.png` | Clinician §Overview | biomedical-mechanism | 1536×1024 |
| 10 | `nephritic-syndromes-05-first-hours-algorithm.png` | Clinician §First Hours | algorithm (Mode C, house style) | 1024×1536 |
| 11 | `nephritic-syndromes-06-cause-map.png` | Clinician §Tests | infographic (clinician reference card) | 1536×1024 |
| 12 | `nephritic-syndromes-07-biopsy-reading.png` | Clinician §Cause & Biopsy Map | biomedical-mechanism (pathology panel) | 1536×1024 |

> **Wiring status.** All 12 references already exist in the guide HTML with matching file names, `width`/`height`, `alt` text, and lightbox captions (`.fig-desc` plus `.fig-abbrevs`). Until each file is committed, that figure shows its alt text.
>
> **Derived asset (no separate prompt):** `nephritic-syndromes-rg-thumb.webp`, a 1:1 center crop of the OG card (#2), about 600 × 600, for Related-guides cards on sibling guides.

---

## 1 · Circular vignette hero *(patient hero disc)*

```
IMAGE NUMBER: 1
SECTION PLACEMENT: Patient hero (figure.hero-figure > .hero-vignette)
FILE NAME: nephritic-syndromes-vignette-hero.png
ARCHETYPE: Circular vignette hero v3, Scaffold A clinical people scene
AUDIENCE: patients and families
ASPECT RATIO: 1:1 (square, displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J, Environmental Storytelling (one cohesive consultation scene, no floating panels)
CAMERA: over-the-shoulder from behind the physician, looking across the desk at mother and son, eye level
HUMAN VARIATION (vs. previous guide, expanded-hemodialysis-hdx: a woman in her mid-60s in a dialysis
  chair with a male nurse in his early 30s, side profile): a mother in her early 30s (not mid-60s);
  her son about 9 years old is present (child in frame, not two adults); setting is an outpatient
  consultation room (not a dialysis unit); seated upright on chairs (not reclined); camera is
  over-the-shoulder (not side profile); clinician is a woman in her late 40s (not a man in his 30s)
  seen mostly from behind with only her shoulder, hands, and a sliver of her cheek; mother has long
  straight black hair in a low ponytail (not a short silver bob); slim build (not fuller); medium
  golden-tan skin (not deep warm-brown); no glasses; wears a sage-green short-sleeve blouse (not a
  lavender cardigan) and small gold stud earrings (not a jade bangle); the boy has a short buzz cut,
  a pale-yellow school polo, a small adhesive bandage on his knee; expressions are attentive and
  slightly worried but calm (not openly smiling); late-morning window light from the left (not
  afternoon).
VISUAL MIX:
- photorealistic models: mother, son, physician (from behind)
- 2D infographic: none
- 3D component graphics: none (a simple physical teaching model on the desk)
- algorithm/flowchart: none
PURPOSE: Wordless reassurance: a family being shown, calmly, what is happening in the kidney.
KEY CONCEPTS: urine sample, kidney model, a doctor explaining, a child as a possible patient (post-strep).

COPY-READY IMAGE GENERATOR GPT PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER
around the full circle (the circle must never touch the canvas edges). Composition archetype:
Environmental Storytelling — one cohesive scene, no floating panels. Camera: over-the-shoulder from
behind a physician's left shoulder at seated eye level, gentle shallow depth of field.

Subject: in a bright, clean, modern Philippine outpatient clinic room, a Filipina mother in her early
30s with long straight black hair in a low ponytail, medium golden-tan skin, a slim build, a
sage-green short-sleeve blouse, and small gold stud earrings sits upright beside her son, about 9
years old, with a short buzz cut, a pale-yellow school polo shirt, and a small adhesive bandage on one
knee. Both look attentively, a little worried but calm, toward the physician in the foreground. The
physician, a Filipina woman in her late 40s, is seen mostly from behind (white coat shoulder, a
sliver of cheek, dark hair in a neat bun); with one hand she holds up a capped clear urine sample cup
containing a light tea-colored liquid, and with the other she points to a simple, unlabeled,
cut-away teaching model of a kidney on the desk. Supporting context, softly out of focus: a window
with late-morning daylight on the left, a small potted plant, a pale wall.

Visual hierarchy: mother, son, and the cup-and-model gesture occupy 60–70% of the circle; 2–3
supporting context cues fill 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft, out-of-focus pale
wall and window glow in the upper-left of the circle (no faces, hands, objects, or equipment inside
that zone).

Calm, warm, documentary-realistic color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e
accents and warm neutrals on a light background. Slight edge falloff toward a soft neutral at the
rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, readable chart, poster
text, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, dozens of icons, tiny
unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle,
cropped objects, edge clipping, objects touching the circular border, important content inside the
title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames,
banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted
hands or faces, bright red urine, visible blood, needles, hospital beds, crying or distressed faces.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin, never cropped. One
dominant scene at 60–70%; 20–25% empty title-safe zone upper-left. Urine is light tea-colored in a
capped cup, not red. Kidney model has no labels. Mother, son, and physician differ in ≥12 traits from
the expanded-hemodialysis-hdx hero. No text anywhere.

ALT TEXT: A Filipino mother in her thirties sitting with her school-age son in a bright clinic as a kind physician holds up a clear urine sample cup and points to a simple kidney model on the desk, the family listening attentively.
OG WIDTH: n/a (hero; OG uses #2)
OG HEIGHT: n/a
```

---

## 2 · OG / social share card *(`og:image`)*

```
IMAGE NUMBER: 2
SECTION PLACEMENT: <head> og:image / twitter:image
FILE NAME: nephritic-syndromes-og.png
ARCHETYPE: OG / social share card (infographic skill, editorial + 3D component)
AUDIENCE: mixed (patients, families, clinicians on Facebook / Viber / LinkedIn)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX:
- photorealistic models: none
- 2D infographic: typography stack
- 3D component graphics: magnified glomerular capillary loop
- algorithm/flowchart: none
PURPOSE: In one glance: "inflamed kidney filters leak blood — know the warning signs."
KEY CONCEPTS: tea/cola urine, inflamed filter, act fast.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Social share card, exactly 1200×630 px, landscape, white (#ffffff) background with a very soft
pale-teal (#eef6f7) panel on the right 45%. LEFT 55%: typography stack set in Inter — small teal
(#1a6b72) uppercase eyebrow "KIDNEY HEALTH · NEW GUIDE"; bold navy (#0f1e2e) title on two lines
"Nephritic Syndrome"; teal subtitle "Recognize it. Act fast. Find the cause."; one short navy line
"Tea- or cola-colored urine · swelling · rising blood pressure". Generous left margin, nothing closer
than 60 px to any edge. RIGHT 45%: a semi-photorealistic 3D render of a single kidney filter
(glomerulus) as a soft teal tuft of looping capillaries inside a pale cup-shaped capsule, magnified,
with a gentle orange glow of inflammation on one loop where two or three soft red-pink red blood
cells squeeze through a small gap and emerge slightly misshapen; beside the render, a small capped
clear cup with a light tea-colored liquid. Soft studio light, gentle shadow, calm clinical look.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, bright red blood, gore,
brand names, unrealistic anatomy, HDR, excessive saturation, faces. NEVER use a dark, navy, charcoal,
or black background — light only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif
or decorative fonts. No journal names, guideline acronyms, brand names, or watermarks other than the
attribution. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Title readable at thumbnail size. Text spelled exactly as given, American English.
Urine light tea-colored, not red. Attribution bottom-right.

ALT TEXT: Nephritic syndrome: a magnified inflamed kidney filter leaking red blood cells beside a cup of tea-colored urine, a guide by W Rivero, MD.
OG WIDTH: 1200
OG HEIGHT: 630
```

---

## 3 · Healthy filter vs. inflamed filter *(patient §What It Means)*

```
IMAGE NUMBER: 3
SECTION PLACEMENT: Patient §What It Means (#what), after the "What inflammation does" paragraph
FILE NAME: nephritic-syndromes-01-inflamed-filter.png
ARCHETYPE: Patient education infographic — 3D component comparison (normal vs disease)
AUDIENCE: patients and families (any education level)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two-panel layout, short labels
- 3D component graphics: two magnified glomerular capillary walls
- algorithm/flowchart: none
PURPOSE: Make the leak visible: red cells and protein stay in a healthy filter and squeeze out, bent, through an inflamed one.
KEY CONCEPTS: filter wall as a sieve; inflammation makes gaps; red cells get bent; casts form downstream.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 3:2 patient-education illustration, white (#ffffff) background, all text set in Inter.
Title at top-left in bold navy (#0f1e2e): "A healthy filter vs. an inflamed filter". Two equal panels
side by side, each inside a soft rounded card on very pale teal (#eef6f7), separated by a thin gray
divider.
LEFT PANEL, header in green (#1f7a4d) "Healthy filter": a semi-photorealistic 3D cross-section of one
tiny blood vessel loop of the kidney filter. Inside the vessel, smooth round red-pink red blood cells
and soft purple spheres (protein) flow along and STAY INSIDE. Through the thin, intact three-layer
wall, only clear fluid with tiny pale dots passes outward into the urine space (pale blue arrows).
Label beside the wall: "Wall works like a fine sieve". Label beside the cells: "Blood cells and
protein stay in".
RIGHT PANEL, header in orange (#c55a11) "Inflamed filter": the same vessel loop, now with a swollen,
thickened wall tinted soft orange, two or three small round immune cells clustered on it, and one
small break in the wall. Two red-pink red blood cells squeeze through the break and come out BENT,
with small knob-like blebs; two or three purple protein spheres also slip through. Below the panel,
a short tube segment (the kidney's drainage pipe) shows a few red cells packed together into a
cylinder-shaped plug. Labels: "Swollen, leaky wall"; "Red cells squeeze out and get bent";
"Some protein leaks"; "Packed cells form a 'cast'".
Bottom strip across both panels, navy, centered: "Blood and protein in the urine come from the
filter, not the bladder." Calm, soft lighting, gentle shading, anatomically plausible, generous
whitespace. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, gore, bright pools of blood,
unrealistic anatomy, HDR, excessive saturation, numbers. NEVER use a dark, navy, charcoal, or black
background — light only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif fonts. No
journal names, guideline acronyms, brand names, or watermarks. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
Healthy side: nothing red or purple crosses the wall. Inflamed side: red cells exit through ONE
break and are visibly misshapen; the cast is in the tube below, not inside the vessel. Labels spelled
exactly as given. Mobile-readable at 390 px width. Attribution present.

ALT TEXT: Two side-by-side magnified kidney filters. On the left a healthy glomerulus keeps round red blood cells and albumin inside the blood vessels while clear fluid passes into the urine space. On the right an inflamed glomerulus with swollen walls and immune cells lets red blood cells squeeze through small gaps, coming out misshapen, with a few packed into a tube-shaped cast below.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 4 · Two different leaks: nephritic vs. nephrotic *(patient §Signs)*

```
IMAGE NUMBER: 4
SECTION PLACEMENT: Patient §Signs (#signs), after the comparison table
FILE NAME: nephritic-syndromes-02-nephritic-vs-nephrotic.png
ARCHETYPE: Multi-panel patient infographic — split comparison
AUDIENCE: patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: two softly illustrated figures (lower legs / face only)
- 2D infographic: two columns with four matched rows
- 3D component graphics: two small filter renders
- algorithm/flowchart: none
PURPOSE: Stop the common confusion between two similar-sounding words by showing two different leaks.
KEY CONCEPTS: nephritic = bleeding, inflamed, high BP; nephrotic = heavy protein, heavy swelling; some diseases show both.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 3:2 patient-education comparison infographic, white (#ffffff) background, all text set in
Inter. Title at top center in bold navy (#0f1e2e): "Two different leaks". Two columns of equal width
with four aligned rows, each row a soft rounded card.
LEFT COLUMN header, orange (#c55a11): "Nephritic — the filter bleeds". Row 1: a small 3D filter loop
with an orange inflamed patch and two red-pink red blood cells leaking out; label "Mostly blood leaks".
Row 2: a capped clear cup of tea-colored urine; label "Tea- or cola-colored urine". Row 3: a simple
blood-pressure cuff gauge with the needle in the upper zone, no numbers; label "Blood pressure often
high". Row 4: an illustrated pair of ankles with mild puffiness; label "Mild swelling".
RIGHT COLUMN header, purple (#6c3d8e): "Nephrotic — the filter leaks protein". Row 1: a small 3D
filter loop with many purple protein spheres streaming out and little inflammation; label "Lots of
protein leaks". Row 2: a capped clear cup of pale yellow urine with a thick layer of foam on top;
label "Very foamy urine". Row 3: the same gauge with the needle in the middle zone, no numbers; label
"Blood pressure normal or high". Row 4: illustrated legs with marked swelling and a puffy-eyelid
face icon; label "Marked swelling".
A thin teal (#1a6b72) banner across the bottom: "Some kidney diseases show both." Gentle shading,
calm palette, generous whitespace. Bottom-right: "© renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, numbers on gauges, AI gibberish text, bright red blood, unrealistic
anatomy, HDR, excessive saturation. NEVER use a dark, navy, charcoal, or black background — light only.
Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif fonts. No journal names, guideline
acronyms, brand names, or watermarks. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Rows align left to right. Orange = nephritic, purple = nephrotic throughout. No numbers. Urine on
the nephritic side is tea-colored, not red. Labels exactly as given. Attribution present.

ALT TEXT: Split-panel comparison. Left panel labeled nephritic: an inflamed glomerulus leaking red blood cells, a jar of tea-colored urine, a blood pressure cuff reading high, and mild ankle swelling. Right panel labeled nephrotic: a glomerulus leaking many protein particles with little inflammation, a jar of very foamy urine, and marked leg and eyelid swelling.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 5 · Go to the ER now: emergency pictograms *(patient §Signs, end)*

```
IMAGE NUMBER: 5
SECTION PLACEMENT: Patient §Signs (#signs), last figure in the section
FILE NAME: nephritic-syndromes-10-emergency-signs.png
ARCHETYPE: Patient warning card — pictogram infographic (low-literacy first)
AUDIENCE: patients, families, caregivers, community health workers
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none (simple illustrated figures)
- 2D infographic: four large pictograms with 2–4 word labels
- 3D component graphics: none
- algorithm/flowchart: one arrow to the emergency room
PURPOSE: A person who cannot read the guide should still know when to go to the emergency room.
KEY CONCEPTS: trouble breathing, coughing blood, almost no urine, severe headache with confusion or vision change.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 3:2 emergency warning card for patients, white (#ffffff) background with a 10 px rounded
clinical-red (#b91c1c) border inset from the edges. All text set in Inter. Top: a bold red title
"Go to the emergency room now". Below, a row of four large, equal, rounded pale-gray (#f3f4f6) tiles,
each containing ONE simple, friendly, softly shaded pictogram of a Filipino adult figure (neutral,
no facial distress beyond a slight frown) and a short navy label underneath:
Tile 1: a person with a hand on the chest and curved breath lines — "Hard to breathe".
Tile 2: a person coughing into a tissue with ONE small stylized red droplet — "Coughing up blood".
Tile 3: a clear urine cup that is almost empty with a downward arrow — "Almost no urine".
Tile 4: a person holding the head with soft swirl lines and a blurred eye icon — "Severe headache,
confusion, or blurry vision".
Under the row, a single thick teal (#1a6b72) arrow points right to a simple hospital building icon
with a plain red cross and the word "Emergency" on its sign. A small navy line at the bottom left:
"Blood in the urine with swelling or less urine: see a doctor today." Generous whitespace, very
high contrast, readable from a phone at arm's length. Bottom-right: "© renalcarematters.com" in
small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid gore, realistic blood, panicked faces, ambulances in motion, sirens, numbers, cartoon style,
clutter, tiny labels, AI gibberish text. NEVER use a dark, navy, charcoal, or black background —
light only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif fonts. No journal names,
guideline acronyms, brand names, or watermarks. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly four tiles, each understandable without reading. Only one small red droplet in the whole
image. Labels exactly as given. Red used only for the border, title, droplet, and cross.
Attribution present.

ALT TEXT: Four large simple pictograms in a row on a white card with a red border: a person short of breath holding their chest, a person coughing with a small red droplet, a urine cup almost empty, and a person holding their head with swirl lines for confusion and blurred vision. Below them a hospital emergency sign with an arrow.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 6 · One pattern, many causes *(patient §Causes)*

```
IMAGE NUMBER: 6
SECTION PLACEMENT: Patient §Causes (#causes), after the six cause cards
FILE NAME: nephritic-syndromes-08-many-causes.png
ARCHETYPE: Radial patient infographic (composition archetype C)
AUDIENCE: patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: six labeled satellite icons
- 3D component graphics: one central inflamed filter
- algorithm/flowchart: none (spokes only, no decision arrows)
PURPOSE: Show that many different illnesses produce the same filter picture, so the cause must be found.
KEY CONCEPTS: post-strep, IgA, lupus, vasculitis/anti-GBM, infected heart valve, complement/rare causes.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 3:2 radial patient-education infographic, white (#ffffff) background, all text set in
Inter. Title at top center in bold navy (#0f1e2e): "One pattern, many causes". CENTER: a medium-sized
semi-photorealistic 3D kidney filter (a teal tuft of capillary loops in a pale capsule) with a soft
orange inflamed glow and two tiny red-pink cells leaking out. Around it, evenly spaced on a gentle
circle, six rounded pale-teal (#eef6f7) badges, each with a simple softly shaded icon and a short
navy label, linked to the center by a thin dotted teal line (no arrowheads):
1 (top): a sore throat and a small skin sore — "After a throat or skin infection".
2 (upper right): a runny-nose tissue and a small Y-shaped antibody — "IgA nephropathy".
3 (lower right): a soft butterfly shape — "Lupus".
4 (bottom): a small blood vessel with two immune cells and a lung outline — "Vasculitis and anti-GBM".
5 (lower left): a heart with a small valve highlighted — "Infected heart valve".
6 (upper left): a short gene strand and a small protein chain — "Complement and rare causes".
Bottom banner in teal: "Finding the cause decides the treatment." Gentle shading, calm palette,
generous whitespace, all six badges the same size. Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid decision arrows pointing to one cause, drug names, numbers, gore, cartoon style, clutter, tiny
labels, AI gibberish text, glossy icons. NEVER use a dark, navy, charcoal, or black background —
light only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif fonts. No journal names,
guideline acronyms, brand names, or watermarks. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Six equal badges, spokes without arrowheads (no implied hierarchy). Labels exactly as given ("IgA"
and "anti-GBM" are the only abbreviations). Attribution present.

ALT TEXT: A single kidney filter drawn in the center of a white page, slightly inflamed, with six simple labeled pathways around it: a sore throat and skin sore, a runny nose with an IgA antibody shape, a butterfly for lupus, small blood vessels with immune cells for vasculitis, a heart valve for infection, and a gene strand for complement and rare causes.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 7 · What the lab sees: urine clues *(patient §Tests)*

```
IMAGE NUMBER: 7
SECTION PLACEMENT: Patient §Tests (#tests), after the "normal-looking test" callout
FILE NAME: nephritic-syndromes-03-urine-clues.png
ARCHETYPE: Labeled microscopy schematic (patient level, clinically exact)
AUDIENCE: patients, families, and clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three circular microscope fields with captions
- 3D component graphics: softly shaded cells
- algorithm/flowchart: none
PURPOSE: Show why a microscope check matters: bent cells and casts point to the filter.
KEY CONCEPTS: round red cells (could be anywhere), acanthocytes (filter), red cell cast (filter).

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 3:2 educational schematic, white (#ffffff) background, all text set in Inter. Title at top
left in bold navy (#0f1e2e): "What the lab sees under the microscope". Three equal circular
"microscope view" fields in a row, each with a thin gray ring and a very pale cream (#f8f5f0)
interior, drawn as clean schematic illustrations with soft shading (NOT a real photomicrograph):
FIELD 1: six or seven smooth, round, biconcave red-pink red blood cells, evenly shaped. Caption
below in navy: "Round red cells" and a smaller gray line "Can come from anywhere in the urinary
tract".
FIELD 2: five or six red-pink red blood cells that are irregular, with one or more small round
knob-like blebs on their edges (ring-shaped cells with blebs, i.e. acanthocytes). Caption: "Bent
cells with small knobs" and smaller gray line "Point to the kidney filters".
FIELD 3: one cylinder-shaped translucent cast with rounded ends, packed with red-pink red blood
cells. Caption: "Red cell cast" and smaller gray line "Points to the kidney filters".
Under fields 2 and 3, a thin teal (#1a6b72) bracket labeled "Signs of filter bleeding". Bottom navy
line: "Not finding them does not rule out kidney inflammation." Generous whitespace. Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid real photomicrographs, staining artifacts, crystals, bacteria, white cells, numbers, scale
bars, cartoon faces on cells, clutter, AI gibberish text. NEVER use a dark, navy, charcoal, or black
background — light only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif fonts. No
journal names, guideline acronyms, brand names, or watermarks. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
Field 1 cells all regular. Field 2 cells show knob-like blebs (not spiky crenation). Field 3 is a
single cylinder with cells inside. Labels exactly as given. Attribution present.

ALT TEXT: Labeled schematic of what the lab sees under the microscope: on the left, normal round red blood cells typical of bleeding from the bladder; in the center, misshapen red blood cells with small knob-like blebs called acanthocytes; on the right, a cylinder-shaped red blood cell cast. Each is captioned in plain words.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 8 · While you wait for answers *(patient §What You Can Do)*

```
IMAGE NUMBER: 8
SECTION PLACEMENT: Patient §What You Can Do (#home), after the checklist
FILE NAME: nephritic-syndromes-09-while-you-wait.png
ARCHETYPE: Multi-panel patient action infographic (five tiles)
AUDIENCE: patients, families, caregivers
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none (softly rendered still-life objects)
- 2D infographic: five action tiles
- 3D component graphics: objects (folder, blister pack, salt shaker, BP monitor, calendar)
- algorithm/flowchart: none
PURPOSE: Five concrete actions a family can take today.
KEY CONCEPTS: bring records, avoid NSAIDs, less salt, check BP, keep follow-up.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 3:2 patient action infographic, white (#ffffff) background, all text set in Inter. Title at
top left in bold navy (#0f1e2e): "While you wait for answers". Five equal rounded tiles in a single
row (or 3 + 2 if needed for legibility) on very pale teal (#eef6f7), each with one softly rendered
semi-realistic object and a short label; tiles 1, 3, 4, 5 carry a small green (#1f7a4d) check badge,
tile 2 carries a small amber (#b8860b) caution badge:
1: a manila folder with lab papers peeking out and a handwritten-looking medicine list with
unreadable lines — "Bring your lab results and medicine list".
2: a generic pain-reliever blister pack with a soft amber diagonal line over it (no brand, no
writing) — "Skip anti-inflammatory pain relievers".
3: a salt shaker with a small downward arrow — "Go easy on salt".
4: a home upper-arm blood pressure monitor with a blank screen — "Check your blood pressure".
5: a calendar page with one date circled and a check mark — "Keep every follow-up".
Bottom navy line: "Do not start leftover steroids or antibiotics on your own." Gentle daylight
shading, calm palette, generous whitespace. Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid readable packaging, drug brand names, numbers on the BP screen, cartoon style, clutter, tiny
labels, AI gibberish text, money imagery. NEVER use a dark, navy, charcoal, or black background —
light only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif fonts. No journal names,
guideline acronyms, brand names, or watermarks. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Five tiles, equal size. No brand or readable text on objects. BP screen blank. Labels exactly as
given. Attribution present.

ALT TEXT: Five simple illustrated action tiles on a white background: a folder of lab papers and a pill list labeled bring your records; a crossed-out pain-reliever blister pack; a salt shaker with a downward arrow; a home blood pressure monitor; and a calendar page with a check mark for follow-up.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 9 · Mechanism: from immune injury to crescents *(clinician §Overview)*

```
IMAGE NUMBER: 9
SECTION PLACEMENT: Clinician §Overview (#md-overview), after "From injury to bedside signs"
FILE NAME: nephritic-syndromes-04-mechanism.png
ARCHETYPE: Biomedical mechanism figure (review-article schematic)
AUDIENCE: clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: dashed inset, bottom three-box flow
- 3D component graphics: soft semi-3D shading on kidney and glomerulus
- algorithm/flowchart: injury → consequence → intervention targets
PURPOSE: Trace the causal chain from immune injury to the bedside signs and to the time-critical crescent.
KEY CONCEPTS: immune complexes / anti-GBM / ANCA-primed neutrophils; complement; capillary wall rupture; RBC deformation; casts; sodium retention; falling GFR; cellular → fibrous crescent.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade biomedical mechanism schematic in a scientific review-article style, white
background, flat vector illustration with soft semi-3D shading, all labels in clean sans-serif set in
Inter, landscape 3:2.

Topic: Nephritic syndrome — how glomerular inflammation produces hematuria, sodium retention, falling
GFR, and crescents.

ORGAN-LEVEL PANEL (left, about one quarter of width): a simplified kidney in light gray-blue with the
renal artery in red and vein in blue, one nephron outlined in soft yellow, labeled "Glomerulonephritis".
A thin dashed connector runs from one glomerulus to the magnified panel.

MAGNIFIED MECHANISM PANEL (center-right, inside a thin dashed rounded box): one glomerular capillary
loop in cross-section with its three-layer wall (fenestrated endothelium, glomerular basement membrane
labeled "GBM", podocyte foot processes) and Bowman's space beside it. Show, with short callouts:
- three small injury triggers converging on the wall, each a tiny icon with a label: "Immune complexes",
  "Anti-GBM antibody (linear)", "ANCA-primed neutrophils";
- a soft orange halo at the wall labeled "Complement activation · leukocyte influx";
- a small break in the GBM labeled "Capillary wall rupture";
- red-pink red blood cells passing through the break into Bowman's space and becoming knobbed,
  labeled "Dysmorphic RBCs";
- downstream, a short tubule segment containing a cylinder of packed cells labeled "RBC cast";
- on the far side of Bowman's space, a crescent-shaped layer of proliferating cells with fibrin strands,
  labeled "Cellular crescent", and a small arrow to a gray scarred version labeled "Fibrous crescent
  (weeks)".

BOTTOM SUMMARY FLOW (three boxes left to right with arrows):
Left, pale pink box "Injury": "Immune attack on the capillary wall" · "↓ Filtration surface → ↓ GFR" ·
"↑ Distal Na⁺ reabsorption → volume expansion" · bold "Hypertension · edema · hematuria".
Center, neutral box "Targets": "Source control (infection)" · "Immune treatment" · "Plasma exchange
(selected)" · "Supportive care: Na⁺, volume, BP".
Right, pale blue box "Goal": "Stop active inflammation" · "Preserve viable glomeruli" · bold "Act before
cellular crescents scar".

Muted clinical palette (gray-blue anatomy, soft yellow nephron, red arteries and injury, blue veins,
orange inflammation, pale pink pathology box, pale blue benefit box), thin dashed connectors,
generous whitespace, labels short and legible at slide size. Bottom-right: "© renalcarematters.com" in
small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, drug names, numeric thresholds,
gibberish text, serif fonts. No journal names, guideline acronyms, brand names, or watermarks other
than the attribution.

QUALITY CHECK:
Three triggers are visually distinct and none is drawn as the single cause. RBC casts appear in the
tubule, crescents in Bowman's space. "Fibrous crescent (weeks)" shown as later and gray. No drug names,
no numbers. Attribution present.

ALT TEXT: Review-article style mechanism figure. Top left: a kidney with one nephron highlighted. Dashed magnification panel: a glomerular capillary loop showing immune-complex deposits, complement activation, neutrophils, a break in the basement membrane, red cells squeezing into Bowman's space, and a cellular crescent forming. Bottom flow: injury, then consequences (hematuria, red cell casts, sodium retention, hypertension, falling GFR), then intervention targets (source control, immunosuppression, plasma exchange, supportive care).
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 10 · First hours in suspected nephritic syndrome *(clinician §First Hours)*

```
IMAGE NUMBER: 10
SECTION PLACEMENT: Clinician §First Hours (#md-first-hours), after the five-step algo card
FILE NAME: nephritic-syndromes-05-first-hours-algorithm.png
ARCHETYPE: Clinical algorithm — Style Mode C (renalcarematters.com house style), portrait
AUDIENCE: clinicians (emergency, internal medicine, nephrology)
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: top-down pathway with one red emergency branch and parallel action boxes
PURPOSE: Show that escalation and investigation run in parallel, and that no score or serology gates escalation.
KEY CONCEPTS: emergency features; confirm pattern; serology by tempo (anti-GBM + MPO/PR3 together); infection; biopsy; close the loop.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style,
portrait 2:3. White background, restrained navy and teal typography set in Inter, thin teal connector
arrows, generous margins, centered layout.

Color conventions: navy #0f1e2e for title and text; teal #1a6b72 for decision diamonds and connectors;
green #1f7a4d for recommended actions; amber #b8860b for caution notes; clinical red #b91c1c ONLY for the
emergency branch; soft gray for side notes.

Content to render (keep text exactly as written):
Title: "First hours in suspected nephritic syndrome"
Top rounded box (navy outline): "Glomerular hematuria ± proteinuria, hypertension, edema, or rising
creatinine"
Teal decision diamond: "Emergency features?"
→ Right branch, red label "Yes", to a red-outlined box: "Hypoxemia or suspected alveolar hemorrhage ·
Pulmonary edema · Hypertensive emergency · Severe hyperkalemia or acidosis · Near-anuria with
deterioration" → arrow to a solid red box with white text: "Emergency care + immediate nephrology ·
Transfer if dialysis, biopsy, or plasma exchange unavailable". From this red box, a thin dashed arrow
rejoins the main column with a small gray note: "Work-up continues in parallel".
→ Down branch, label "No / in parallel", to a horizontal row of four equal green rounded boxes, joined
by a bracket labeled "Do together":
 1 "Confirm the pattern: fresh urine microscopy · quantified proteinuria · creatinine vs dated baseline"
 2 "Serology by tempo: C3, C4 · if rapid or lung–kidney: anti-GBM + MPO/PR3-ANCA together"
 3 "Look for infection: blood cultures · echo if endocarditis possible"
 4 "Ultrasound · plan biopsy when it changes management"
Below the row, one teal box: "Rapid decline + glomerular sediment → same-day nephrology"
Final navy-outlined box: "Close the loop: who reviews pending results · when to repeat creatinine and
potassium · which symptoms bring the patient back sooner"
Amber side note at the bottom left, small: "Do not wait for a score, a percentage decline, or a
serology result to escalate."

Design requirements: top-to-bottom logic, rounded rectangles for actions, one diamond for the
decision, consistent spacing and alignment, no clutter, no icons, no photorealistic people, no dark
background. Include a small professional footer reading "© renalcarematters.com" positioned at the
bottom-center in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid spaghetti arrows, more than one decision diamond, drug names, numeric thresholds, invented
criteria, icons, 3D, gradients, dark background, serif fonts, gibberish text. No journal names,
guideline acronyms, brand names, or watermarks other than the attribution.

QUALITY CHECK:
Portrait 1024×1536. The emergency branch is the only red element. The four parallel boxes are visually
simultaneous (same row, bracketed). "anti-GBM + MPO/PR3-ANCA together" appears in one box. All text
matches the prompt exactly. Footer bottom-center.

ALT TEXT: Clinical algorithm flowchart titled First hours in suspected nephritic syndrome. Top box: glomerular hematuria with or without proteinuria, hypertension, edema, or rising creatinine. A red emergency branch lists hypoxemia or suspected alveolar hemorrhage, pulmonary edema, hypertensive emergency, severe hyperkalemia or acidosis, near-anuria, leading to emergency care and immediate nephrology. The main column shows parallel steps: confirm pattern with urine microscopy and quantified proteinuria; serology C3, C4 and, for rapid or lung-kidney presentations, anti-GBM plus MPO and PR3 ANCA together; infection screen; ultrasound; biopsy planning; and a closing box for follow-up ownership.
OG WIDTH: 1024
OG HEIGHT: 1536
```

---

## 11 · Narrowing the cause *(clinician §Tests)*

```
IMAGE NUMBER: 11
SECTION PLACEMENT: Clinician §Tests (#md-tests), after the test-interpretation table
FILE NAME: nephritic-syndromes-06-cause-map.png
ARCHETYPE: Clinician reference card (three-column map)
AUDIENCE: clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three columns of disease cards, an immunofluorescence strip, a footer caveat
- 3D component graphics: four tiny glomerulus thumbnails for IF patterns
- algorithm/flowchart: none (grouping, not branching)
PURPOSE: Organize the differential by complement pattern and immunofluorescence while stating plainly that these are clues.
KEY CONCEPTS: low C3/normal C4; low C3 and C4; normal complement; IF granular / linear / pauci-immune / C3-dominant.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical reference infographic card for clinicians, landscape 3:2, white (#ffffff) background, all
text set in Inter, publication-grade nephrology design with modular rounded cards. Title at top left
in bold navy (#0f1e2e): "Narrowing the cause of nephritic syndrome". Subtitle in teal (#1a6b72):
"Complement and immunofluorescence are clues — not verdicts".
THREE equal columns, each headed by a soft teal header chip:
Column 1 header "Low C3 · normal C4": two stacked cards — "Infection-related GN" (gray line:
"recent or ongoing infection; subepithelial humps") and "C3 glomerulopathy" (gray line: "C3-dominant
IF; exclude infection and monoclonal protein").
Column 2 header "Low C3 · low C4": two cards — "Lupus nephritis" (gray line: "SLE features; anti-dsDNA;
'full-house' IF") and "Cryoglobulinemic GN" (gray line: "very low C4; purpura; hepatitis C").
Column 3 header "Normal complement": four cards — "IgA nephropathy / IgA vasculitis" (gray line:
"hematuria with infections; IgA-dominant mesangial IF"), "ANCA-associated vasculitis" (gray line:
"MPO or PR3; pauci-immune"), "Anti-GBM disease" (gray line: "linear IgG; lungs may bleed"), and a
small amber-outlined card "Double-positive anti-GBM + ANCA".
Under the columns, a thin horizontal strip titled "Biopsy immunofluorescence" with four tiny
schematic glomerulus thumbnails and labels: "Granular (immune complex)", "Linear (anti-GBM)",
"Pauci-immune (ANCA)", "C3-dominant (C3G or infection)".
Footer band in pale amber (#f8f5f0 with amber text): "Endocarditis can lower complement and induce
ANCA · normal complement never excludes serious GN."
Generous whitespace, modular cards, no arrows between columns. Bottom-right: "© renalcarematters.com"
in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid arrows from a complement result to a single disease, drug names, numbers, photorealistic
micrographs, clutter, tiny unreadable labels, gibberish text. NEVER use a dark, navy, charcoal, or
black background — light only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope) — no serif
fonts. No journal names, guideline acronyms, brand names, or watermarks. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Three columns, no connecting arrows. Footer caveat visible. Abbreviations limited to C3, C4, GN, IF,
SLE, IgA, IgG, ANCA, MPO, PR3, GBM, anti-dsDNA, C3G. Attribution present.

ALT TEXT: Clinician reference map titled Narrowing the cause of nephritic syndrome. Columns for serum complement (low C3 normal C4; low C3 and low C4; normal), each listing candidate diseases with key clues: infection-related GN and C3 glomerulopathy; lupus nephritis and cryoglobulinemic GN; IgA nephropathy, IgA vasculitis, ANCA-associated vasculitis, and anti-GBM disease. Footer notes that complement patterns are clues, not diagnoses, and that biopsy immunofluorescence (granular, linear, pauci-immune, C3-dominant) confirms the category.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## 12 · What the biopsy shows *(clinician §Cause & Biopsy Map)*

```
IMAGE NUMBER: 12
SECTION PLACEMENT: Clinician §Cause & Biopsy Map (#md-differential), after "Reading the biopsy report"
FILE NAME: nephritic-syndromes-07-biopsy-reading.png
ARCHETYPE: Biomedical mechanism figure — pathology teaching panel
AUDIENCE: clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three glomeruli in a row with activity/chronicity labels; IF strip
- 3D component graphics: soft semi-3D shading
- algorithm/flowchart: a single left-to-right time arrow
PURPOSE: Make activity vs chronicity intuitive: treat what is active; scar cannot be recovered.
KEY CONCEPTS: normal glomerulus; necrosis + cellular crescent (active, potentially reversible); fibrous crescent + global sclerosis (chronic); IFTA.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade pathology teaching panel in a scientific review-article style, white
background, flat vector illustration with soft semi-3D shading, all labels in clean sans-serif set in
Inter, landscape 3:2. Title at top left in bold navy (#0f1e2e): "What the biopsy shows".
TOP ROW: three equal schematic glomeruli in round pale capsules, connected by a thin gray time arrow
running left to right labeled "Untreated: days → weeks":
1 "Normal glomerulus": open capillary loops, thin walls, empty Bowman's space; green (#1f7a4d) tag
"Viable".
2 "Active lesion": a segment of fibrinoid necrosis drawn as a bright pink-magenta smudge in one
loop, and a crescent of plump proliferating cells with fibrin strands filling part of Bowman's space;
orange (#c55a11) tag "Necrosis · cellular crescent — potentially reversible".
3 "Chronic lesion": the tuft collapsed and pale gray-blue, a thick acellular fibrous crescent, and a
globally sclerosed glomerulus beside it; gray tag "Fibrous crescent · global sclerosis — scar".
A small inset under glomerulus 3 shows a strip of tubules with interstitial fibrosis and atrophic
tubules, labeled "IFTA".
BOTTOM ROW, titled "Immunofluorescence pattern": four small round schematic glomeruli with
stylized fluorescent green staining on a light gray disc (NOT a dark field): "Granular — immune
complex", "Linear — anti-GBM", "Minimal — pauci-immune (ANCA)", "C3-dominant — C3G or infection".
Footer line in navy: "Treat the active; the scar tells you what cannot come back." Muted clinical
palette, thin dashed separators, generous whitespace. Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid real photomicrographs, dark-field black backgrounds for the IF panels, H&E photorealism, numbers,
percentages, drug names, clutter, gibberish text, serif fonts. No journal names, guideline acronyms,
brand names, or watermarks other than the attribution.

QUALITY CHECK:
Three glomeruli clearly progress normal → active → chronic. IF discs on light gray, not black. Only
the labels given. No numbers. Attribution present.

ALT TEXT: Clean teaching panel titled What the biopsy shows. Three glomeruli drawn side by side: a normal glomerulus; an active lesion with fibrinoid necrosis and a cellular crescent labeled potentially reversible; and a chronic lesion with a fibrous crescent and global sclerosis labeled scarred. Below, small immunofluorescence insets show granular, linear, pauci-immune, and C3-dominant staining patterns with their associated disease categories.
OG WIDTH: 1536
OG HEIGHT: 1024
```

---

## After generation: checklist

1. Save each PNG to `images/` with the exact file name, and export a `.webp` twin (quality about 82).
2. Keep #1 square at 2048×2048 and #10 portrait at 1024×1536 (both declared in the HTML). All other in-body figures are declared 1536×1024; if a render comes back at a different size, update that `<img>`'s `width`/`height`.
3. Export `nephritic-syndromes-rg-thumb.webp` (1:1 center crop of #2, about 600×600), then switch the Related-guides cards on `glomerulonephritis.html` and `hematuria-blood-in-urine.html` to `has-thumb` cards.
4. Run `python3 patch_hero_fetchpriority.py --guide nephritic-syndromes.html` and `python3 patch_image_lightbox.py --guide nephritic-syndromes.html`.
5. Spot-check every rendered label for spelling (American English) and for invented numbers, drug names, or a single arrow from a complement result to one disease; regenerate any image that breaks a guardrail.
6. Open the guide in light and dark mode: figures sit on light `.illus-wrap-light` cards in both themes, so no dark variant is needed.
7. Commit the images.
