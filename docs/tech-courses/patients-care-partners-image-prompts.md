# Renal Patients and Care Partners: image plan blueprint and GPT prompt pack (version 2)

Renal Care Academy → Renal Patients and Care Partners. Prepared November 28, 2026 (evening). American English throughout. Stage 1 of the two-stage image pipeline: generate in ChatGPT image generation, then run the prep step (Stage 2). **This pack replaces `IMAGE_PLAN_AND_GPT_PROMPTS.md`.**

## 1. What changed, and why

The first plan gave the course one hero per pathway, in a painted style, with dark share cards and square tiles. It did not match the other Academy tracks, and most figures illustrated an analogy rather than the module’s own lesson. This version uses the same house style and file conventions as the Social Worker, Pediatric Dialysis Nurse and other tracks, and it is built from the modules themselves:

- **Every hero shows that module’s own real situation** (Mang Ramon’s tricycle and his daughter’s phone, Aling Cora’s report, Kuya Jun’s swollen ankle, Ate Grace’s dressing in the rain, Paolo’s 2 a.m. call, Rosa in the Bicol storm, and so on). Each prompt quotes the situation it is built from (GROUNDED IN).
- **Every figure label comes from the lesson text**, and each prompt names the module section it is placed in and quotes that lesson. Numbers on figures are only the ones the module states (156 sessions; 14.5% → 9.2% and 16.9% → 13.1%; published November 21, effective December 6, 2026 expected; one in four with depression).
- **House style:** square photographic circular heroes, crisp white-background figures in Inter with the Academy palette, 16:9 photographic still-life tiles, and light share cards with the teal Academy chip.
- **Anatomy:** Constitution v1.0 anatomy locks and anatomy QA (from `williamriveromd-infographic-generator`) on every figure that shows a kidney, nephron, fistula, PD catheter, transplant or tunneled catheter; the catheter path lock on both catheter images.

### The 62 images made this morning

| Group | Decision |
| --- | --- |
| Heroes (9, rpcp-hero-*) | Replace. Landscape 1536 × 1024 painted illustrations, one per pathway; the Academy uses a square 2048 × 2048 photographic hero for every page. |
| Share cards (11, rpcp-og-*) | Replace. Dark, saturated color backgrounds break the Academy light-background rule; Academy cards are white to pale teal with a teal chip. |
| Tiles (10, rpcp-tile-*) | Replace. Square painted illustrations; Academy tiles are 16:9 photographic still-lifes, one per module. |
| Figures (32, rpcp-<code>-*) | Interim only. Content was checked and they read well, but the painted look differs from the crisp white Academy figures and several illustrate the analogy rather than the lesson. The pages use them until the new figure for that module is placed, then drop them. |

## 2. Inventory

| Image | Learning purpose | Where it appears | Count |
| --- | --- | --- | --- |
| **Circular vignette hero** | Appreciation: the module’s own person and moment | Top of the course home and every module | 33 |
| **Teaching figure** | Understanding (the mechanism) and application (an action path, card or checklist) | In the named lesson section of its module | 42 |
| **Course and module tiles** | Navigation: recognition on the module cards and Related Guides thumbnails | Course home cards; landing page tile | 34 |
| **OG share card** | Reach: a share preview naming the page | `images/og/<page>-og.jpg` for the course home, 32 modules, urgent help, worksheets, final check and toolkit | 37 |
| **Track share-card art** | Background for the Academy composite card | `images/academy/og-art/patients-care-partners.webp` | 1 |

**Total: 147 prompts.** Suggested order: heroes and figures for the shared foundations (C01–C12) first, then the pathways, then tiles and share cards.

## 3. Rules for every image

- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c (emergency only), purple #6c3d8e.
- **Photographic, not painted:** heroes and tiles are real-photograph style; figures are crisp semi-photoreal infographics like the other Academy figures. No watercolor, no warm sepia.
- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). American English spelling on every label.
- **Attribution:** figures and share cards carry `© renalcarematters.com` bottom-right; heroes and tiles carry no text.
- **No individual clinical targets on any image:** no fluid amounts, potassium or phosphorus values, blood pressure targets, doses, machine settings or phone numbers.
- **People:** fictional Filipinos, calm, fully clothed, dignified; a different cast, camera and setting in each hero; no needles in skin, blood or wounds.
- **Skills used:** `williamriveromd-hero-vignette` v3, `williamriveromd-infographic-skill` v5, `williamriveromd-simple-figure`, `williamriveromd-algorithm-generator-skill`, `williamriveromd-infographic-generator` (Constitution v1.0 anatomy locks), `tunneled-dialysis-catheter-path`.

## 4. Production workflow

1. Generate each prompt in ChatGPT image generation. Save each PNG with the exact FILE NAME stem into `~/Downloads/Renal Patients & Care Partners/images-v2/` (track art in `images-v2/og-art/`).
2. Tell me when a batch is ready. I audit each image against its QUALITY CHECK and anatomy QA, place it (heroes `images/<page>-vignette-hero.png` + `.webp`; figures `images/<stem>.webp` + `.png`; tiles 640 × 360 WebP, the course tile also `images/academy/landing/patients-care-partners.webp`; share cards 1200 × 630 JPEG ≤ 300 KB in `images/og/`), rebuild with `python3 generate_patients_care_partners.py --patch`, and write corrected prompts for any failures in a new MD file.
3. Nothing is pushed until you say so.

## 5. Image map by module

| Module | Hero (the module’s situation) | Figures (section) |
| --- | --- | --- |
| Course home | Kidney care is learned together: the patient, the person they choose, and the team. | — |
| C01. Start with your goals and care team | Mang Ramon finds his stop: Find your stop: one goal, one supporter, one care team. | Who helps with what (`lesson-2`) |
| C02. Understand kidney disease and your test results | Aling Cora's "normal" result: Read both numbers: how much the kidneys clean, and whether they leak. | Two tests, two stories (`lesson-2`); One result is a snapshot; the trend is the story (`lesson-3`) |
| C03. Choose treatment through shared decisions | Two neighbors, two right answers: The same facts can lead to different, well-informed choices. | Options worth discussing (`lesson-1`) |
| C04. Make medicines easier and safer | The pain reliever from the sari-sari store: Ask before you take it: weak kidneys clear some medicines more slowly. | Why the same dose can build up (`picture`); Ask before adding a product (`lesson-2`) |
| C05. Build a food plan that fits your life | Aling Nena gives up vegetables: Do not cut out whole food groups on a rumor; build the plan with your dietitian. | Use the meals you already eat (`lesson-2`); When a food list becomes too strict (`lesson-3`) |
| C06. Follow your own fluid and monitoring plan | Kuya Jun's birthday weekend: With little urine, every glass stays until the next treatment. | The closing drain (`picture`) |
| C07. Prevent infection and protect your access | Ate Grace's damp dressing: Report redness the same day; do not wait for the next session. | Know your doorway (`lesson-2`); Clean hands protect your doorway (`lesson-1`) |
| C08. Recognize urgent problems and get help | The 30-second call: In an emergency, call: location, what happened, kidney treatment, bleeding. | Get emergency help now (`lesson-1`); The 30-second call (`lesson-2`) |
| C09. Manage tiredness, emotions and daily activity | Manong Ben stops going out: Tiredness and low mood are information; several causes can be treated. | Tired is information (`lesson-1`) |
| C10. Understand Philippine benefits and treatment costs | The rate in the news: Ask what you are signing; a benefit is paid to the facility, not to you. | A benefit, not cash (`lesson-1`) |
| C11. Plan for travel, typhoons and interrupted care | Signal No. 3 in Bicol: Plan while services are open: go early, keep a portable folder. | The spare tire plan (`lesson-2`) |
| C12. Speak up, protect privacy and review your plan | Nodding in the clinic: Explain it back: teach-back catches mistakes before they happen. | Ask until the plan is clear (`lesson-1`) |
| K01. Protect kidney health before dialysis | Sir Arnel's stomach flu: A written sick-day plan turns an emergency into a phone call. | Many small drips (`picture`); When you are sick (`lesson-3`) |
| K02. Prepare for changing kidney care needs | Two ways to start dialysis: Planning ahead gives you a ready access and a treatment you chose. | Two ways to start dialysis (`picture`) |
| K03. The heart, kidney and sugar connection, and kidney-protecting medicines | Ma'am Lyn's worrying dip: A small early dip can mean the medicine is working; ask before stopping. | The heart, kidney and sugar connection (`picture`); A small early dip, then slower decline (`lesson-3`) |
| H01. Navigate a hemodialysis treatment day | Tatay Lito's quiet cramps: Report cramps and dizziness early; it is part of the treatment. | Inside the dialyzer (`picture`) |
| H02. Protect fistulas, grafts and dialysis catheters | The silent fistula: Feel the buzz morning and evening; if it weakens or stops, contact your unit promptly. | Know and protect your access (`lesson-1`); If a needle site bleeds at home (`lesson-3`) |
| H03. Use dialysis reviews to improve daily life | Ate Joy leaves early: Your review is numbers plus your experience; solve the barrier together. | A review looks beyond one number (`lesson-1`) |
| H04. Potassium, phosphorus and fluid between sessions: why the rules exist | Christmas Eve and the long gap: Plan the food and fluid before the longest gap between sessions. | Rising behind the dam (`picture`); Why binders go with meals (`lesson-2`) |
| P01. Prepare for supervised peritoneal dialysis training | Learning from a cousin's video: Only supervised training makes you ready for home PD. | How peritoneal dialysis works (`picture`) |
| P02. Recognize PD infection and contamination concerns | Cloudy on a Saturday night: A cloudy bag is an urgent call, even at night. | Clear or cloudy (`picture`); If a connection may be contaminated (`lesson-2`) |
| P03. Organize home dialysis routines and reassessment | A new helper, an old habit: A new helper or a long gap means a new skills check. | A safe home routine (`lesson-2`) |
| T01. Prepare for a kidney transplant evaluation | Ana and her brother: A living donor has their own team and can say no at any time. | Where a new kidney goes (`picture`) |
| T02. Build a safe routine after transplantation | Rico's empty bottle: Every anti-rejection dose matters; plan refills before you run out. | The steady guard (`picture`) |
| T03. Navigate transplant benefits across policy dates | Two dates, one surgery: Coverage depends on which policy applies, and from what date. | Published is not the same as effective (`lesson-2`) |
| S01. Understand conservative kidney management | Lola Iska's priority: Conservative care is active care, focused on comfort and what matters. | Conservative care is active care (`lesson-1`) |
| S02. Plan for comfort and future care conversations | Manang Elsa's kitchen-table talk: Talking about future care is a gift to the people who may decide for you. | Talking about future care (`lesson-2`) |
| A01. Support someone while protecting their choices | Who answers the doctor?: Support without taking over: the patient speaks first. | A co-pilot, not the driver (`picture`) |
| A02. Organize appointments, records and practical support | The family group chat: A shared plan, a backup for every task, and private channels for medical details. | Make tasks visible, share carefully (`lesson-1`) |
| A03. Prevent care partner burnout and arrange backup | Ate Rowena's breaking point: An empty cup cannot pour; ask for specific help. | An empty cup cannot pour (`picture`) |
| F01. Support children, teens and growing independence | JM turns seventeen: Hand over responsibility step by step, with a safety net. | Growing independence, step by step (`lesson-3`) |
| F02. Recover after hospital care and rebuild your plan | Two lists, one patient: After a hospital stay, reconcile one clear plan. | Two lists, one plan (`lesson-1`) |

## 6. Track-level images

### Course home hero

```
FILE NAME: images/patients-care-partners-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: eye level, medium-wide
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Kidney care is learned together: the patient, the person they choose, and the team.
GROUNDED IN: Course home: the track serves patients, care partners and educators together.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: eye level, medium-wide. Subject: in a bright, modern Philippine dialysis unit lounge, a Filipino man in his early 60s with a round face, close-cropped gray hair and a striped polo sits with his adult daughter, who holds a small notebook, while a nurse educator in teal scrubs with a short bob shows them a printed booklet (pages blurred); other patients and chairs softly blurred behind, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

### Course tile and Academy landing tile

```
FILE NAME: images/patients-care-partners-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP; the course tile also writes images/academy/landing/patients-care-partners.webp 960 × 540)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the track’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a teal notebook and a pen resting on a small printed booklet (pages blurred) beside a folded light blanket on the armrest of a dialysis chair, bright clinic window light. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

### Course home OG card

```
FILE NAME: images/og/patients-care-partners-og.png (prep exports images/og/patients-care-partners-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Renal Patients and Care Partners". Subtitle in teal #1a6b72: "32 short modules · 9 pathways · free, no account". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a teal notebook and a pen resting on a small printed booklet (pages blurred) beside a folded light blanket on the armrest of a dialysis chair, bright clinic window light, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Track share-card art (Academy composite card)

```
FILE NAME: images/incoming/patients-care-partners/og-art/patients-care-partners.png (prep writes images/academy/og-art/patients-care-partners.webp)
SKILL: williamriveromd-infographic-skill v5 (background art)
IMAGE TYPE: Background art for build_academy_og.py (the script sets every word)
PIXEL DIMENSIONS: 1536 × 1024

PROMPT:
3:2 landscape photorealistic editorial photograph on a light background: in a bright, modern Philippine dialysis unit lounge, a Filipino man in his early 60s and his adult daughter sit with a nurse educator in teal scrubs who shows them a printed booklet (pages blurred). Place the people in the RIGHT 55%; keep the LEFT 45% as clean, light, empty negative space (soft wall and window light) where the builder sets the track title and stats. Soft daylight, gentle depth of field, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Absolutely NO text, logos or watermark; no legible screens or papers.

NEGATIVE INSTRUCTIONS:
Avoid text, clutter, dark backgrounds, painterly style, people in the left 45%.

QUALITY CHECK:
Left 45% empty and light; subjects on the right; photographic; no text.
```

### Urgent help page OG card

```
FILE NAME: images/og/patients-care-partners-urgent-help-og.png (prep exports images/og/patients-care-partners-urgent-help-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "When to Get Urgent Help". Subtitle in teal #1a6b72: "Know the signs. Make the call.". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a refrigerator door with a magnet holding a folded contact card and a medicine list (unreadable), softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Worksheets page OG card

```
FILE NAME: images/og/patients-care-partners-worksheets-og.png (prep exports images/og/patients-care-partners-worksheets-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Printable Patient Worksheets". Subtitle in teal #1a6b72: "23 blank forms for your visits". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a clipboard with blank lined worksheet pages, a pencil and a calculator on a light wooden table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Final knowledge check page OG card

```
FILE NAME: images/og/patients-care-partners-final-check-og.png (prep exports images/og/patients-care-partners-final-check-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Final Knowledge Check". Subtitle in teal #1a6b72: "Built from the modules on your path". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a printed medicine schedule (unreadable) with a pen and a small padlock on a desk, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Toolkit page OG card

```
FILE NAME: images/og/calc-patient-care-partner-toolkit-og.png (prep exports images/og/calc-patient-care-partner-toolkit-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Patient and Care Partner Toolkit". Subtitle in teal #1a6b72: "6 tools · results trend · label sodium · fluid · weight gain · sessions · medicine clock". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a clipboard with blank lined worksheet pages, a pencil and a calculator on a light wooden table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Toolkit tile

```
FILE NAME: images/patients-care-partners-toolkit-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a clipboard with blank lined worksheet pages, a pencil and a calculator on a light wooden table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

## 7. Module prompts

### Module C01 (1 of 32): Start with your goals and care team

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-01-start-with-your-goals-and-care-team-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder, slightly high
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Find your stop: one goal, one supporter, one care team.
GROUNDED IN: Module C01 real situation "Mang Ramon finds his stop": Mang Ramon, 58, drives a tricycle in Malolos and was told at a barangay screening that his kidneys were "weak." His daughter Liza, a call-center agent, opens the course on her phone. They argue: Ramon thinks he must read every module tonight, and Liza wants to start with dialysis because a neighbor is on it.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder, slightly high. Subject: Mang Ramon, a Filipino tricycle driver in his late 50s with a weathered tan face, short salt-and-pepper hair and a faded cap in his hand, sits beside his daughter Liza, late 20s, long straight hair, office lanyard, who holds a phone showing a course page (screen blurred); a barangay health worker in a white blouse hands them a blank care-team card at a simple community health station, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Who helps with what**  ·  skill `infographic-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-01-care-team-map.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Role map infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C01, section "lesson-2"
GROUNDED IN: Module C01, Lesson 2 "People who can help": Kidney care is a team sport. Your nephrologist (kidney doctor) leads the medical plan. Nurses teach, assess and watch for problems. A pharmacist can untangle medicine lists. A dietitian turns food advice into meals you actually eat. A social worker or benefits coordinator helps with costs, PhilHealth paperwork and transport. A care partner is someone you choose to help you: a spouse, child, sibling, friend or paid helper. Choosing a care partner does not hand them your decisions. You decide what they help with and what they may know. Ask your unit or clinic for a contact card that says who answers medicine, food, treatment and money questions, and how to reach them after hours.

PROMPT:
Title at top in bold navy: "Who helps with what". A center circle with a seated Filipino patient and the care partner they chose beside them. Around it six rounded cards, each with a small semi-photoreal portrait and one line: "Kidney doctor (nephrologist): the medical plan", "Nurse: teaches and watches for problems", "Pharmacist: untangles medicine lists", "Dietitian: meals you actually eat", "Social worker or benefits officer: costs, PhilHealth, transport", "Care partner: the person you choose". Right side: a blank card titled "My care team card" with four empty lines labeled "Medicines", "Food", "Treatment", "Money" and a fifth "After hours". Footer chip: "You decide what your care partner helps with." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-01-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a blank care-team contact card and a pen on a clinic counter beside a tricycle key on a keychain. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-01-start-with-your-goals-and-care-team-og.png (prep exports images/og/patients-care-partners-01-start-with-your-goals-and-care-team-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Start with your goals and care team". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C01 · 1 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a blank care-team contact card and a pen on a clinic counter beside a tricycle key on a keychain, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C02 (2 of 32): Understand kidney disease and your test results

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-02-understand-kidney-disease-and-your-test-results-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: close portrait, three-quarter
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Read both numbers: how much the kidneys clean, and whether they leak.
GROUNDED IN: Module C02 real situation "Aling Cora's "normal" result": Aling Cora, 52, has had diabetes for ten years. Her eGFR came back in the normal range, so she skipped her follow-up visit. Months later her doctor points to another line on the same report: urine albumin, clearly raised, and higher than the year before.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: close portrait, three-quarter. Subject: Aling Cora, a Filipina in her early 50s with diabetes, shoulder-length wavy hair with a clip and reading glasses, sits at a clinic desk looking closely at a printed laboratory report (text blurred) while a woman doctor in a white coat points to a second line further down the page; soft window light, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Two tests, two stories**  ·  skill `simple-figure`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-02-two-tests.png
SKILL: williamriveromd-simple-figure + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Two-panel comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C02, section "lesson-2"
GROUNDED IN: Module C02, Lesson 2 "Two tests that tell different stories": eGFR (estimated glomerular filtration rate) estimates how much blood your filters clean each minute. It is calculated from a blood test, creatinine, together with your age and sex. Think of it as how much water the plant can process. Urine albumin, usually reported as a urine albumin-to-creatinine ratio (uACR), measures a protein that should mostly stay in the blood. Albumin leaking into urine means the filters are damaged, like a strainer whose holes are stretching. A person can have a normal eGFR but leaking albumin, or a low eGFR with little leak. International guidelines use both numbers together to judge risk, because together they predict what happens next far better than either alone.

PROMPT:
Title at top in bold navy: "Two tests, two stories". Left panel titled "eGFR: how much your filters clean": an enlarged single nephron (glomerulus and tubule) with blood entering and filtrate leaving, and a gauge. Right panel titled "Urine albumin (uACR): is the filter leaking?": a magnified filter wall with small gold albumin dots crossing into urine, and a strainer icon labeled "holes stretching". Bottom band: "Normal eGFR can still leak albumin. Both together show risk." Small kidney orientation inset labeled "NOT TO SCALE". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK (overrides style): any whole kidney is bean-shaped with the convex border LATERAL and the hilum MEDIAL; the renal pelvis exits at the medial hilum only; calyces drain INWARD toward the pelvis; renal vein anterior, artery middle, ureter posterior (VAU). A nephron is drawn as a standalone enlarged diagram, never inside a full-size kidney; the whole kidney appears only as a small orientation inset (12% of the panel or less) labeled "NOT TO SCALE". Glomerulus: a capillary tuft inside Bowman’s capsule, afferent arteriole in, efferent arteriole out, filtrate into the proximal tubule. Arteries have a thick muscular wall and round lumen; veins are thin-walled. Anatomy is never drawn through clothing or skin except inside a labeled inset.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ Nephron standalone; whole kidney only in a small NOT TO SCALE inset — confirmed
□ Afferent arteriole in, efferent out; filtrate into tubule — confirmed
□ Kidney convex border lateral, hilum medial, calyces drain inward — confirmed
```

**Figure B: One result is a snapshot; the trend is the story**  ·  skill `simple-figure`  ·  placed in `lesson-3`

```
FILE NAME: images/patients-care-partners-02-trend.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Annotated line chart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C02, section "lesson-3"
GROUNDED IN: Module C02, Lesson 3 "Use results without guessing treatment": Keep a dated list of your results with the units printed on the report, because laboratories do not all use the same units. One result is a snapshot; the trend is the story. Creatinine can rise a little after a big meal of meat, heavy exercise, dehydration or certain medicines, so your team looks at the pattern and repeats tests before drawing conclusions. Ask: "How does this compare with last time? What would make you worried? Which change should make me call before my next visit?" Do not change medicines or diet on your own because of one number.

PROMPT:
Title at top in bold navy: "One result is a snapshot; the trend is the story". A simple line chart with five dated dots (no numbers on the axes) and a gentle line through them. Three callouts: "Same units every time", "One high dot after a big meat meal or dehydration" pointing to a single outlier, and "Ask: is the trend stable, improving or getting worse?" A small clipboard icon labeled "Keep a dated list". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-02-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a printed laboratory report (text blurred) under a pair of reading glasses, with a urine sample cup with a blank label. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-02-understand-kidney-disease-and-your-test-results-og.png (prep exports images/og/patients-care-partners-02-understand-kidney-disease-and-your-test-results-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Understand kidney disease and your test results". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C02 · 2 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a printed laboratory report (text blurred) under a pair of reading glasses, with a urine sample cup with a blank label, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C03 (3 of 32): Choose treatment through shared decisions

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-03-choose-treatment-through-shared-decisions-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: The same facts can lead to different, well-informed choices.
GROUNDED IN: Module C03 real situation "Two neighbors, two right answers": Two men in the same barangay reach kidney failure in the same month. Mang Tonio, 45, works as a security guard on rotating shifts and has a wife who is a nurse. Lolo Pedring, 84, has heart failure and memory problems and says his wish is to stay home with his apo.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide, eye level. Subject: a small barangay hall in late afternoon: Mang Tonio, mid-40s, security-guard uniform shirt, short hair, sits with his wife, a nurse in civilian clothes; across the room an 84-year-old grandfather, Lolo Pedring, in a cane chair with his grandchild leaning on his arm; a kidney doctor in a polo stands between them, talking warmly, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Options worth discussing**  ·  skill `infographic-skill`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-03-options.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Option cards
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C03, section "lesson-1"
GROUNDED IN: Module C03, Lesson 1 "Options worth discussing": Depending on your condition, the options may include protecting the kidneys you have for as long as possible; hemodialysis, where a machine cleans your blood, usually in a unit about three times a week; peritoneal dialysis, where fluid placed in your belly cleans the blood using your own abdominal lining, usually at home; kidney transplantation from a living or deceased donor; and conservative kidney management, which is active care focused on comfort and quality of life without dialysis. Not every option suits every person, and local availability varies. Learning about an option never commits you to it.

PROMPT:
Title at top in bold navy: "Options worth discussing". Five equal cards in a row, each with a semi-photoreal scene and a short label: "Protect the kidneys you have", "Hemodialysis in a unit, about three times a week", "Peritoneal dialysis at home", "Kidney transplant", "Conservative kidney management: comfort and quality of life". Above the row two overlapping cards: "What is medically suitable" (held by a doctor) and "What matters to me" (held by a patient). A circular arrow under the row: "A decision can be revisited". All five cards the same size and brightness. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-03-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: five small blank cards fanned out on a table beside a clinician’s stethoscope. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-03-choose-treatment-through-shared-decisions-og.png (prep exports images/og/patients-care-partners-03-choose-treatment-through-shared-decisions-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Choose treatment through shared decisions". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C03 · 3 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: five small blank cards fanned out on a table beside a clinician’s stethoscope, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C04 (4 of 32): Make medicines easier and safer

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-04-make-medicines-easier-and-safer-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: 45-degree tabletop
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Ask before you take it: weak kidneys clear some medicines more slowly.
GROUNDED IN: Module C04 real situation "The pain reliever from the sari-sari store": Tito Boy, 63, has CKD and high blood pressure. After helping move furniture for a fiesta, his back aches, so he buys mefenamic acid from the corner store and takes it three times a day for a week. It is hot, he drinks little water, and his legs begin to swell. His next blood test shows his kidney function has dropped.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: 45-degree tabletop. Subject: a pharmacist’s hands at a neighborhood pharmacy counter holding a blister pack and turning a small box so its side label (blurred) faces a Filipino man in his 60s, Tito Boy, whose hand rests on his lower back; a handwritten medicine list on the counter (unreadable), soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Why the same dose can build up**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-04-two-exits.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Analogy diagram
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C04, section "picture"
GROUNDED IN: Module C04, The everyday picture: Most medicines leave the body through the liver, the kidneys or both. Picture a busy road with two exits. When the kidney exit narrows, cars that normally leave that way start to pile up. A dose that was perfect for healthy kidneys can build up to a harmful level when the kidneys are weak. That is why the same tablet can be safe for your neighbor and risky for you, and why the dose on the box is not always your dose.

PROMPT:
Title at top in bold navy: "Why the same dose can build up". A highway with capsule-shaped cars (medicines) and two exits: one to a liver icon, one to a kidney icon. Left half "Healthy kidneys": both exits flowing. Right half "Weak kidneys": the kidney exit narrowed to one lane and cars queuing, label "Medicine builds up". A thin dashed divider separates the analogy from a small real kidney icon. Footer: "A dose that was right for healthy kidneys may need changing." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Figure B: Ask before adding a product**  ·  skill `infographic-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-04-ask-first.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Three-card action figure
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C04, section "lesson-2"
GROUNDED IN: Module C04, Lesson 2 "Ask before adding a product": Some everyday products are hard on kidneys. Pain relievers called NSAIDs (non-steroidal anti-inflammatory drugs, such as ibuprofen, mefenamic acid and naproxen) reduce blood flow into the kidney's filters and can cause sudden kidney injury, especially when you are dehydrated. Many herbal "kidney cleansers," detox teas and imported supplements are not tested for people with kidney disease; some contain potassium, heavy metals or hidden drugs. Before taking anything new, show the label to your pharmacist or kidney team and say: "I have kidney disease and I am on [your treatment]. Is this safe for me?"

PROMPT:
Title at top in bold navy: "Ask before adding a product". Three cards left to right with generic, unbranded products: "Pain relievers called NSAIDs (ibuprofen, mefenamic acid, naproxen) reduce blood flow into the filters"; "Herbal ‘kidney cleansers’ and detox teas are not tested for kidney disease"; "Imported supplements may hide potassium, metals or drugs". Below, a pharmacist and patient at a counter with a speech bubble: "I have kidney disease. Is this safe for me?" Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-04-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: an unbranded blister pack, a small box and a handwritten medicine list (unreadable) on a pharmacy counter. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-04-make-medicines-easier-and-safer-og.png (prep exports images/og/patients-care-partners-04-make-medicines-easier-and-safer-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Make medicines easier and safer". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C04 · 4 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: an unbranded blister pack, a small box and a handwritten medicine list (unreadable) on a pharmacy counter, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C05 (5 of 32): Build a food plan that fits your life

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-05-build-a-food-plan-that-fits-your-life-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F Human Connection
CAMERA: three-quarter, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Do not cut out whole food groups on a rumor; build the plan with your dietitian.
GROUNDED IN: Module C05 real situation "Aling Nena gives up vegetables": Aling Nena, 67, read in a group chat that "kidney patients must avoid vegetables and fruit." For three months she eats rice, eggs and canned meat loaf. She feels weak, is constipated, and her blood pressure is higher, not lower.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Human Connection. Camera: three-quarter, eye level. Subject: Aling Nena, 67, petite, short gray hair with a side part, cotton duster dress, at her kitchen table with a renal dietitian in a white polo who shows her a bowl of tinola with green papaya and malunggay and a small plate of fruit; a can of meat loaf and a plate of plain rice and egg pushed to the side; daylight from a jalousie window, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Use the meals you already eat**  ·  skill `infographic-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-05-less-salt.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Three-panel food figure
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C05, section "lesson-2"
GROUNDED IN: Module C05, Lesson 2 "Use the meals you already eat": Bring real examples to your dietitian: sinigang, tinola, adobo, pancit, rice with fried fish, champorado. Most can be adapted. Season with calamansi, garlic, onion, ginger, pepper and herbs instead of extra patis, toyo, bagoong and seasoning cubes. On packaged foods, find sodium per serving on the nutrition label, then count how many servings you actually eat; one pack of instant noodles is often two servings. Ask how cooking methods, such as boiling vegetables and discarding the water, change what is in the food, and what affordable substitutes are available at your market.

PROMPT:
Title at top in bold navy: "Use the meals you already eat". Panel 1 "Same dish, less salt": sinigang, tinola, rice and fried fish, with patis, toyo, bagoong and a seasoning cube fading out and calamansi, garlic, onion, ginger and pepper coming in. Panel 2 "Read the label": a generic nutrition label with "Sodium per serving" highlighted and the note "1 pack of instant noodles is often 2 servings". Panel 3 "Ask your dietitian": a dietitian and an older patient with a notebook "My plan". Footer: "There is no single kidney food list that fits everyone." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Figure B: When a food list becomes too strict**  ·  skill `simple-figure`  ·  placed in `lesson-3`

```
FILE NAME: images/patients-care-partners-05-too-strict.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Before-and-after comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C05, section "lesson-3"
GROUNDED IN: Module C05, Lesson 3 "Avoid making the plan too restrictive": Cutting whole food groups because another patient was told to can cause poor nutrition, muscle loss and constipation, and muscle loss itself worsens outcomes in kidney disease. Report poor appetite, unplanned weight loss, or a diet so strict you have stopped enjoying meals. A dietitian can loosen what is safe to loosen. Your plan should change when your treatment changes: what was right before dialysis is often wrong after it.

PROMPT:
Title at top in bold navy: "When a food list becomes too strict". Left panel "Three months on a rumor": a plate of plain rice, egg and canned meat loaf; an older Filipina looking tired, with three amber chips "Weak", "Constipated", "Blood pressure higher". Right panel "A plan made with a dietitian": the same woman at the same table with tinola, vegetables, a small portion of fruit and rice, and green chips "Salt cut first", "Other limits only if your results call for them", "Plan changes when treatment changes". Footer: "Report poor appetite, weight loss, or a diet so strict you stopped enjoying meals." No potassium or phosphorus numbers. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-05-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a bowl of sinigang with calamansi halves and garlic beside it on a woven placemat. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-05-build-a-food-plan-that-fits-your-life-og.png (prep exports images/og/patients-care-partners-05-build-a-food-plan-that-fits-your-life-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Build a food plan that fits your life". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C05 · 5 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a bowl of sinigang with calamansi halves and garlic beside it on a woven placemat, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C06 (6 of 32): Follow your own fluid and monitoring plan

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-06-follow-your-own-fluid-and-monitoring-plan-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: side profile, medium
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: With little urine, every glass stays until the next treatment.
GROUNDED IN: Module C06 real situation "Kuya Jun's birthday weekend": Kuya Jun, 41, has been on hemodialysis for two years and passes very little urine. Over a long weekend he attends two parties with plenty of soup, soft drinks and ice. On Monday morning his ankles are swollen, and he feels short of breath when he lies down.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: side profile, medium. Subject: Kuya Jun, early 40s, slim build, short spiky hair, birthday-party shirt, sits on the edge of a bed in the morning, gently pressing his swollen ankle with a thumb; a bathroom scale on the floor and a small glass of water on the side table, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The closing drain**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-06-closing-drain.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Three-step analogy
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C06, section "picture"
GROUNDED IN: Module C06, The everyday picture: Healthy kidneys work like a smart overflow drain: drink more and they release more, drink less and they hold on. As kidney function falls, especially on dialysis when urine output drops, the drain slows or closes. Water you drink stays in the body until the next treatment removes it. Extra fluid first collects in the legs and around the eyes, then in the lungs, where it makes breathing hard. That is why some people need a fluid limit and others do not, and why the limit is personal.

PROMPT:
Title at top in bold navy: "The closing drain". Three panels, each a sink above a seated person. "Kidneys working": drain open, water flowing out. "Less urine": drain half closed, water rising, light blue shading at the ankles labeled "swelling". "Very little urine, on dialysis": drain nearly closed, water high, a small inset of the lungs labeled "fluid can reach the lungs". Bottom band: a measuring cup labeled "Your amount, if any, comes from your team" and a red chip "Can’t breathe lying flat? Get help now." No numbers. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-06-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a bathroom scale on a tiled floor beside a small glass of water. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-06-follow-your-own-fluid-and-monitoring-plan-og.png (prep exports images/og/patients-care-partners-06-follow-your-own-fluid-and-monitoring-plan-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Follow your own fluid and monitoring plan". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C06 · 6 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a bathroom scale on a tiled floor beside a small glass of water, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C07 (7 of 32): Prevent infection and protect your access

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-07-prevent-infection-and-protect-your-access-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: close, slightly angled
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Report redness the same day; do not wait for the next session.
GROUNDED IN: Module C07 real situation "Ate Grace's damp dressing": Ate Grace, 36, has a tunneled catheter while her fistula matures. During the rainy season she bathes with a dipper and the dressing gets wet. She notices a little redness at the exit site but decides to wait for Thursday's session. On Wednesday night she has shaking chills.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: close, slightly angled. Subject: Ate Grace, 36, hair tied up, loose button-front blouse open at the collar, sitting on a dialysis unit bed on a rainy day while a dialysis nurse in navy scrubs and a mask examines the clean white dressing on her right upper chest below the collarbone (only the dressing and the red and blue capped limbs visible, no tube in the neck); a folded umbrella dripping by the chair, rain on the window, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

CATHETER LOCK FOR THIS HERO (tunneled-dialysis-catheter-path skill, vignette rules): the patient faces the camera, so her RIGHT side is on the IMAGE LEFT. Only the outside is visible: a clean white dressing on her right upper chest wall below the collarbone, a few finger-breadths from the breastbone and above the nipple line, with a hub and two short limbs hanging DOWNWARD below it, RED clamp and cap (arterial) and BLUE clamp and cap (venous). No tube in the neck, no catheter crossing the midline, no exit site on the neck or abdomen, no internal path, no inset, no labels; the body is never mirrored.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Know your doorway**  ·  skill `infographic-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-07-doorways.png
SKILL: williamriveromd-infographic-skill + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Four-column comparison with anatomy insets
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C07, section "lesson-2"
GROUNDED IN: Module C07, Lesson 2 "Know your doorway": Ask which access you have and how to care for it daily. A fistula joins an artery directly to a vein in your arm; a graft uses a soft tube to connect them; a hemodialysis catheter is a tube placed in a large neck or chest vein; a PD catheter enters the belly. Keep catheter dressings clean and dry as taught, and never open a catheter cap, flush it, or remove a dressing to look at a problem yourself; that is how germs get a direct route into the bloodstream. Wash a fistula or graft arm with soap and water before every session.

PROMPT:
Title at top in bold navy: "Know your doorway". Four columns with a short label each: "Fistula: your artery joined to a vein" (left forearm), "Graft: a soft tube joins artery and vein" (forearm with looped tube), "Hemodialysis catheter: a tube in a large vein" (clothed upper right chest with dressing and red and blue clamps; internal path only in a NOT TO SCALE inset), "PD catheter: a tube into the belly" (lower abdomen with a dressing, tube pointing down). Under the first three columns a bar labeled "Hemodialysis bloodstream infection risk (CDC)" running from "Lowest: fistula" to "Highest: catheter". Footer: "Never open a cap or remove a dressing yourself. Report redness, pus, fever or chills the same day." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK — FISTULA (overrides style): left forearm radiocephalic fistula, the cephalic vein joined end-to-side to the radial artery near the wrist; the arterialized vein is visibly enlarged and runs up the forearm under the skin. When needles are shown, the arterial needle (red) sits nearer the joining point and the venous needle (blue) is further up the arm and points AWAY from the joining point, toward the heart. A graft, if shown, is a separate soft tube looping under the forearm skin.

ANATOMY LOCK — CATHETER PATH (tunneled-dialysis-catheter-path skill; follow exactly; overrides style): Anterior view, so the patient’s RIGHT side is on the IMAGE LEFT. The whole catheter is on the patient’s right (image left) and never crosses the midline. 1. EXIT SITE: right upper anterior chest wall, below the clavicle, a few finger-breadths lateral to the sternum, above the nipple line; below it a hub splits into two short external limbs hanging downward, RED clamp and cap (arterial) and BLUE clamp and cap (venous). 2. CUFF: a small textured cream-white Dacron cuff INSIDE the subcutaneous tunnel just above the exit site, under the skin. 3. TUNNEL: upward beneath the skin, passing OVER (in front of) the medial clavicle, never beneath it. 4. VENOTOMY AND LOOP: just above the clavicle ONE smooth gentle U-shaped turn into the LOW right internal jugular vein, lateral to the common carotid artery. 5. COURSE: straight down the right internal jugular vein, right brachiocephalic vein, superior vena cava. 6. TIP: upper-to-mid right atrium. Internal path only inside an inset labeled "NOT TO SCALE". Never: catheter under the clavicle or in the subclavian vein, crossing the midline, exit site in the neck or on the abdomen, external cuff, sharp kink or double loop, tip in the right ventricle or high superior vena cava, red/blue clamps swapped.

CONSTITUTION v1.0 ANATOMY LOCK — PD CATHETER (overrides style): soft silicone Tenckhoff catheter entering the LOWER abdominal wall off the midline; exit site points DOWNWARD; deep cuff preperitoneal, superficial cuff about 2 cm inside the exit site; the tip lies low in the pelvis, never in the bladder or bowel. The peritoneum is a thin glossy membrane lining the abdominal wall and covering the bowel, rich in tiny capillaries. Internal anatomy only inside a labeled cutaway inset marked "NOT TO SCALE".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ Fistula on the left forearm near the wrist; vein enlarged up the forearm — confirmed
□ If needles shown: red nearer the joining point, blue further up pointing toward the heart — confirmed
□ Path: chest-wall exit → cuff inside tunnel → over the clavicle → one loop into the low right internal jugular vein → superior vena cava → right atrium — confirmed
□ Entirely on the image left; never crosses the midline — confirmed
□ Red = arterial, blue = venous limbs below the hub — confirmed
□ PD exit site on the lower abdomen pointing downward — confirmed
□ Catheter tip low in the pelvis, not in bladder or bowel — confirmed
□ Anatomy only in a NOT TO SCALE inset — confirmed
```

**Figure B: Clean hands protect your doorway**  ·  skill `simple-figure`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-07-hands.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Four-moment icon strip
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C07, section "lesson-1"
GROUNDED IN: Module C07, Lesson 1 "Hands and shared spaces": Most germs that reach an access travel on hands. Clean your hands with soap and water or an alcohol hand rub before touching your access, dressing or supplies, after using the toilet, and after handling pets or garbage. Ask your educator to show you the exact method your unit uses and watch you do it once. Tell staff before your session if you have a fever, cough, diarrhea or a skin wound, so they can protect you and other patients. Wearing a mask when you have a cough protects the people sitting next to you in the unit.

PROMPT:
Title at top in bold navy: "Clean hands protect your doorway". Four rounded tiles, each with a soap-and-water or alcohol hand-rub icon and a label: "Before touching your access", "Before handling your dressing or supplies", "After the toilet", "After pets or garbage". Below, two chips: "Mask when you have a cough" and "Tell staff about fever, cough, diarrhea or a skin wound before your session". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-07-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a hand-rub bottle and a sealed sterile dressing packet on a clean blue tray. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-07-prevent-infection-and-protect-your-access-og.png (prep exports images/og/patients-care-partners-07-prevent-infection-and-protect-your-access-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Prevent infection and protect your access". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C07 · 7 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a hand-rub bottle and a sealed sterile dressing packet on a clean blue tray, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C08 (8 of 32): Recognize urgent problems and get help

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-08-recognize-urgent-problems-and-get-help-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: medium, low light
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: In an emergency, call: location, what happened, kidney treatment, bleeding.
GROUNDED IN: Module C08 real situation "The 30-second call": At 2 a.m., Lola Fe, 74, on hemodialysis, wakes gasping and cannot lie down. Her grandson Paolo, 19, panics and starts typing her symptoms into a search engine.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: medium, low light. Subject: a small home at night: Paolo, 19, lanky, messy hair, T-shirt, speaking urgently but calmly on his phone while his grandmother Lola Fe, 70s, sits upright on the edge of her bed propped by pillows; a contact card and medicine list held by a magnet on the refrigerator in the background (unreadable), soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Get emergency help now**  ·  skill `algorithm-generator-skill`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-08-help-now.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Action card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C08, section "lesson-1"
GROUNDED IN: Module C08, Lesson 1 "Act on severe symptoms": Get emergency help immediately for: severe or worsening breathlessness, or being unable to lie flat; chest pain or pressure; fainting or collapse; new confusion, severe drowsiness, or difficulty speaking; new weakness of the face, arm or leg; heavy or spurting bleeding from an access; and a seizure. Severe muscle weakness or a very slow or irregular heartbeat in someone who has missed dialysis can be a sign of dangerous potassium. In the dialysis unit, call staff at once. Outside the unit, use your local emergency service or go to the nearest emergency department.

PROMPT:
Title at top in bold navy: "Get emergency help now". A red header "Get emergency help now". Seven rows with simple icons: "Severe breathlessness or can’t lie flat", "Chest pain or pressure", "Fainting or collapse", "New confusion or trouble speaking", "New weakness of face, arm or leg", "Heavy or spurting bleeding from an access", "Seizure". Right side: two boxes "In the dialysis unit: call staff at once" and "At home: local emergency service or nearest emergency department". Footer in red: "No website or chat is watched in real time." No phone numbers. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Figure B: The 30-second call**  ·  skill `simple-figure`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-08-the-call.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Four-box script
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C08, section "lesson-2"
GROUNDED IN: Module C08, Lesson 2 "Say the important details": Responders work faster with clear facts. Practice saying: where you are (with a landmark), what is happening, when it started, that the person has kidney disease and which treatment (hemodialysis, PD or transplant), and whether there is active bleeding. If you can, bring the medicine and allergy list and the dialysis or transplant contact card. Tell emergency staff the arm with a fistula or graft should not be used for blood pressure or drips. Do not delay urgent care to finish a form or wait for a reply to a message.

PROMPT:
Title at top in bold navy: "The 30-second call". A phone at the center with four numbered speech boxes around it: "1 Where you are, with a landmark", "2 What is happening and when it started", "3 Kidney treatment: hemodialysis, PD or transplant", "4 Is there bleeding?". Below: a refrigerator magnet holding a contact card and medicine list, with the note "Tell staff: no blood pressure or drips on the fistula arm." No phone numbers. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-08-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a refrigerator door with a magnet holding a folded contact card and a medicine list (unreadable). One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-08-recognize-urgent-problems-and-get-help-og.png (prep exports images/og/patients-care-partners-08-recognize-urgent-problems-and-get-help-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Recognize urgent problems and get help". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C08 · 8 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a refrigerator door with a magnet holding a folded contact card and a medicine list (unreadable), softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C09 (9 of 32): Manage tiredness, emotions and daily activity

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-09-manage-tiredness-emotions-and-daily-activity-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: E Lifestyle
CAMERA: environmental portrait, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Tiredness and low mood are information; several causes can be treated.
GROUNDED IN: Module C09 real situation "Manong Ben stops going out": Manong Ben, 66, a retired teacher on hemodialysis, used to lead the parish choir. Over six months he stops attending, sleeps most afternoons, and tells his wife there is no point. He has never mentioned any of this at the unit because "everyone there is tired."

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: E Lifestyle. Camera: environmental portrait, eye level. Subject: Manong Ben, 66, a retired teacher with thick glasses, a cardigan and neatly combed white hair, walking slowly across a town plaza toward the parish church with his wife holding his arm and a choir folder under his other arm; morning light, church facade softly blurred, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Tired is information**  ·  skill `infographic-skill`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-09-tired.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Cause-and-action figure
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C09, section "lesson-1"
GROUNDED IN: Module C09, Lesson 1 "Describe the effect on your day": Use plain words and concrete examples. Instead of "I'm tired," try "I can no longer climb the stairs to my apartment without stopping twice" or "After dialysis I sleep until evening and miss my grandchildren's visit." Say when the symptom happens, how long it lasts and what it stops you doing. Ask which symptoms need tests. Tiredness can come from anemia, the low red blood cell count that is common in kidney disease, and that is treatable.

PROMPT:
Title at top in bold navy: "Tired is information". Left: an older Filipino man on a porch with a thought bubble "I can no longer climb the stairs without stopping." Center: four cards of causes the team can look for: "Anemia (low red blood cells)", "Poor sleep", "Depression", "Dialysis that needs review". Right: three action tiles: "Describe how it affects your day", "Start small with walking, with your team’s OK", "Ask for a counselor or social worker". Footer chip: "About one in four people with kidney disease has depression; it is treatable." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-09-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a pair of walking shoes beside a park bench in a town plaza in morning light. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-09-manage-tiredness-emotions-and-daily-activity-og.png (prep exports images/og/patients-care-partners-09-manage-tiredness-emotions-and-daily-activity-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Manage tiredness, emotions and daily activity". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C09 · 9 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a pair of walking shoes beside a park bench in a town plaza in morning light, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C10 (10 of 32): Understand Philippine benefits and treatment costs

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-10-understand-philippine-benefits-and-treatment-costs-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder at a desk
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Ask what you are signing; a benefit is paid to the facility, not to you.
GROUNDED IN: Module C10 real situation "The rate in the news": Mang Celso, 55, hears on the radio that PhilHealth "gives P6,350 per dialysis." He expects nothing to pay and is upset when the unit asks him to sign a form and mentions a charge for a medicine given during dialysis.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder at a desk. Subject: Mang Celso, 55, heavyset, basketball jersey, a bucket hat in his lap, at the reception desk of a dialysis unit while a benefits officer with short hair and a lanyard explains a form (unreadable) before he signs, the pen resting on the desk; a small transistor radio peeks out of his shoulder bag, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: A benefit, not cash**  ·  skill `simple-figure`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-10-benefit-flow.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Flow diagram
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C10, section "lesson-1"
GROUNDED IN: Module C10, Lesson 1 "Know the benefit category": Under PhilHealth Circular 2024-0023, eligible members with stage 5 chronic kidney disease who are registered in the PhilHealth Dialysis Database can receive coverage for up to 156 hemodialysis sessions per calendar year, at a package rate of PHP 6,350 per session, paid to the accredited facility. That is roughly three sessions a week for a year. These are payments to the provider for covered treatment, not cash given to you. Ask the facility to confirm your registration, eligibility and how many sessions remain.

PROMPT:
Title at top in bold navy: "A benefit, not cash". Left: a plain building icon labeled "PhilHealth" (text only, no logo). Arrow "pays for covered services" to the center: "Accredited facility". Arrow to the right: a patient receiving treatment and holding "Itemized bill" and "Copies of documents". A crossed-out dashed arrow from PhilHealth to a wallet: "Not cash to you". Bottom band: "Up to 156 hemodialysis sessions per calendar year for eligible, registered members (PhilHealth Circular 2024-0023, checked November 28, 2026)". No peso amounts. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-10-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a clear document folder with an itemized statement (unreadable) and a pen on a hospital counter. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-10-understand-philippine-benefits-and-treatment-costs-og.png (prep exports images/og/patients-care-partners-10-understand-philippine-benefits-and-treatment-costs-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Understand Philippine benefits and treatment costs". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C10 · 10 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a clear document folder with an itemized statement (unreadable) and a pen on a hospital counter, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C11 (11 of 32): Plan for travel, typhoons and interrupted care

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-11-plan-for-travel-typhoons-and-interrupted-care-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: D Panorama
CAMERA: wide, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Plan while services are open: go early, keep a portable folder.
GROUNDED IN: Module C11 real situation "Signal No. 3 in Bicol": Aling Rosa, 59, dialyzes Mondays, Wednesdays and Fridays in Legazpi. A typhoon is forecast to make landfall on a Wednesday. On Monday, the unit announces it will add Tuesday sessions for patients whose routes may flood.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: D Panorama. Camera: wide, eye level. Subject: Aling Rosa, 59, slim, gray-streaked bun, rain jacket, leaving her house in Legazpi under heavy gray skies for the extra Tuesday session her unit added before the typhoon, holding a sealed waterproof folder and a power bank; a relative waits by a tricycle; wet road, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The spare tire plan**  ·  skill `infographic-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-11-spare-tire.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Flat-lay plus timeline
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C11, section "lesson-2"
GROUNDED IN: Module C11, Lesson 2 "Prepare a portable folder": Keep a waterproof folder or sealed plastic bag with: your treatment summary and prescription, medicine and allergy list, latest laboratory results, PhilHealth details, the contact card for your unit and a backup unit, and a few days of medicines. Keep a phone power bank charged. PD patients should store supplies off the floor, away from floodwater, and ask what emergency stock is right for them. Ask your team whether you need any written emergency diet instructions for days when dialysis is delayed.

PROMPT:
Title at top in bold navy: "The spare tire plan". Left: a top-down photo of a sealed waterproof folder holding "Treatment summary", "Medicine and allergy list", "Latest results", "PhilHealth details", "Unit and backup unit card", a few days of medicines and a charged power bank. Right: a four-step vertical timeline with rain icons: "Storm signal raised" → "Unit announces schedule change" → "Go early, or to the backup unit" → "Can’t reach anyone? Follow your written plan; emergency if severe symptoms". A PD supply box on a shelf above a floodwater line. No logos. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-11-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a sealed waterproof pouch with folded papers and a power bank on a windowsill with rain outside. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-11-plan-for-travel-typhoons-and-interrupted-care-og.png (prep exports images/og/patients-care-partners-11-plan-for-travel-typhoons-and-interrupted-care-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Plan for travel, typhoons and interrupted care". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C11 · 11 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a sealed waterproof pouch with folded papers and a power bank on a windowsill with rain outside, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module C12 (12 of 32): Speak up, protect privacy and review your plan

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-12-speak-up-protect-privacy-and-review-your-plan-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: three-quarter, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Explain it back: teach-back catches mistakes before they happen.
GROUNDED IN: Module C12 real situation "Nodding in the clinic": Ate Mylene, 48, a market vendor, is told her medicines will change. She nods, but at home she cannot remember which tablet to stop. Her cousin, who came along, tells the rest of the family about her diagnosis without asking her.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: three-quarter, eye level. Subject: Ate Mylene, late 40s, market vendor with a ponytail and an apron folded on her lap, explaining something back to a nurse in teal scrubs who listens and holds a pen over a printed medicine schedule (unreadable); a consultation room with a closed door, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Ask until the plan is clear**  ·  skill `simple-figure`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-12-teach-back.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Loop plus privacy card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module C12, section "lesson-1"
GROUNDED IN: Module C12, Lesson 1 "Ask until the plan is clear": Try these phrases: "Please show me." "Can you write that down?" "Let me explain it back so you can check I understood." If you use a language other than the one being spoken, ask for an interpreter or bring someone you trust. You can raise concerns about your care respectfully, and you can ask for a second opinion. A good team will not be offended.

PROMPT:
Title at top in bold navy: "Ask until the plan is clear". Left: a four-step loop with small scenes: "Nurse explains" → "You explain it back" → "Nurse corrects one detail" → "Written plan". Three speech chips: "Please show me.", "Can you write that down?", "Let me explain it back." Right: a card "Who may know about my health" with three checkboxes (no names) and a padlock: "Health information is sensitive personal information (Data Privacy Act)." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-12-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a printed medicine schedule (unreadable) with a pen and a small padlock on a desk. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-12-speak-up-protect-privacy-and-review-your-plan-og.png (prep exports images/og/patients-care-partners-12-speak-up-protect-privacy-and-review-your-plan-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Speak up, protect privacy and review your plan". Subtitle in teal #1a6b72: "Patients & Care Partners · Module C12 · 12 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a printed medicine schedule (unreadable) with a pen and a small padlock on a desk, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module K01 (13 of 32): Protect kidney health before dialysis

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-13-protect-kidney-health-before-dialysis-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: medium, slightly low
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: A written sick-day plan turns an emergency into a phone call.
GROUNDED IN: Module K01 real situation "Sir Arnel's stomach flu": Sir Arnel, 50, a public school teacher with CKD and diabetes, catches stomach flu during exam week. He keeps taking all his medicines while barely eating or drinking for two days and feels dizzy when standing.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: medium, slightly low. Subject: Sir Arnel, a public school teacher around 50 with a mustache and a barong-style polo, sits at his kitchen table pale and tired with a glass of oral rehydration fluid, reading a small written sick-day card from his clinic (text blurred); a stack of exam papers beside him, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Many small drips**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-13-drips.png
SKILL: williamriveromd-simple-figure + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Analogy with real inset
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module K01, section "picture"
GROUNDED IN: Module K01, The everyday picture: Picture the kidney filters as clay pots under a dripping roof. High blood pressure is water hitting the pots too hard; high blood sugar is water that is sticky and corrosive; smoking narrows the pipes that feed them. Each drip does a little damage, and lost filters do not grow back. But fix the roof early and the remaining pots can last for decades. Kidney protection is less about one big treatment and more about stopping many small drips.

PROMPT:
Title at top in bold navy: "Many small drips". A row of clay pots (palayok) labeled "kidney filters" under a nipa roof with five drips labeled "High blood pressure", "High blood sugar", "Smoking", "Some pain relievers", "Dehydration"; a person repairing the roof labeled "Treatment and daily habits". A dashed inset shows a real glomerulus with arrows "pressure inside the filter". Footer: "Lost filters do not grow back; protect the ones you have." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK (overrides style): any whole kidney is bean-shaped with the convex border LATERAL and the hilum MEDIAL; the renal pelvis exits at the medial hilum only; calyces drain INWARD toward the pelvis; renal vein anterior, artery middle, ureter posterior (VAU). A nephron is drawn as a standalone enlarged diagram, never inside a full-size kidney; the whole kidney appears only as a small orientation inset (12% of the panel or less) labeled "NOT TO SCALE". Glomerulus: a capillary tuft inside Bowman’s capsule, afferent arteriole in, efferent arteriole out, filtrate into the proximal tubule. Arteries have a thick muscular wall and round lumen; veins are thin-walled. Anatomy is never drawn through clothing or skin except inside a labeled inset.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ Nephron standalone; whole kidney only in a small NOT TO SCALE inset — confirmed
□ Afferent arteriole in, efferent out; filtrate into tubule — confirmed
□ Kidney convex border lateral, hilum medial, calyces drain inward — confirmed
```

**Figure B: When you are sick**  ·  skill `algorithm-generator-skill`  ·  placed in `lesson-3`

```
FILE NAME: images/patients-care-partners-13-sick-day.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Simple decision path
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module K01, section "lesson-3"
GROUNDED IN: Module K01, Lesson 3 "Prepare for illness": Vomiting, diarrhea, fever and not eating can dry you out and cause a sudden drop in kidney function, called acute kidney injury (AKI). Some medicines, including certain blood pressure and diabetes medicines, may need to be paused during such illness and restarted afterward, but the right list is individual. Ask your clinician for written sick-day instructions that name your own medicines, and whom to call. Do not stop or restart a medicine based on a generic online list.

PROMPT:
Title at top in bold navy: "When you are sick". Start box "Vomiting, diarrhea, fever or not eating" → "Find your written sick-day card from your clinician" → two branches: "Medicines the card says to pause" and "Medicines the card says to keep" → "Call your clinic" → "Restart as the card says when you are eating and drinking". Red side box: "Do not use a generic online list." No medicine names. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-13-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a home blood pressure monitor and a small written card (unreadable) on a kitchen table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-13-protect-kidney-health-before-dialysis-og.png (prep exports images/og/patients-care-partners-13-protect-kidney-health-before-dialysis-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Protect kidney health before dialysis". Subtitle in teal #1a6b72: "Patients & Care Partners · Module K01 · 13 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a home blood pressure monitor and a small written card (unreadable) on a kitchen table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module K02 (14 of 32): Prepare for changing kidney care needs

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-14-prepare-for-changing-kidney-care-needs-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: B Journey
CAMERA: wide, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Planning ahead gives you a ready access and a treatment you chose.
GROUNDED IN: Module K02 real situation "Two ways to start dialysis": Nanay Lourdes and Tatay Rodel both reach kidney failure in the same year. Lourdes had met a PD nurse and had a fistula created six months earlier. Rodel had skipped visits because he felt fine, and arrives at the emergency department breathless.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: B Journey. Camera: wide, eye level. Subject: Nanay Lourdes, early 60s, short permed hair, floral blouse, walking out of a modern dialysis unit entrance in daylight with her husband carrying her bag; she glances at the healed fistula on her left forearm, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Two ways to start dialysis**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-14-two-starts.png
SKILL: williamriveromd-simple-figure + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Two timelines
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module K02, section "picture"
GROUNDED IN: Module K02, The everyday picture: Starting dialysis in an emergency is like moving house during a flood: everything is rushed, and the choices are made for you. People who plan ahead are more likely to start with a ready access, a chosen treatment and a family that knows what to expect. Planning is not giving up hope. It is packing the bag early so that, if the day comes, you walk out the door instead of being carried.

PROMPT:
Title at top in bold navy: "Two ways to start dialysis". Top timeline "Planned start": "Clinic visits" → "Meets the PD nurse, visits a unit" → "Fistula made months before" (forearm icon) → "Planned first session, home the same day". Bottom timeline "Crisis start": "Skipped visits" → "Emergency department, breathless" → "Urgent catheter" (clothed right upper chest with a dressing and red and blue capped limbs only) → "Hospital stay". Footer: "People who plan ahead are more likely to start with a ready access and a treatment they chose." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

ANATOMY LOCK — CATHETER PATH (tunneled-dialysis-catheter-path skill; follow exactly; overrides style): Anterior view, so the patient’s RIGHT side is on the IMAGE LEFT. The whole catheter is on the patient’s right (image left) and never crosses the midline. 1. EXIT SITE: right upper anterior chest wall, below the clavicle, a few finger-breadths lateral to the sternum, above the nipple line; below it a hub splits into two short external limbs hanging downward, RED clamp and cap (arterial) and BLUE clamp and cap (venous). 2. CUFF: a small textured cream-white Dacron cuff INSIDE the subcutaneous tunnel just above the exit site, under the skin. 3. TUNNEL: upward beneath the skin, passing OVER (in front of) the medial clavicle, never beneath it. 4. VENOTOMY AND LOOP: just above the clavicle ONE smooth gentle U-shaped turn into the LOW right internal jugular vein, lateral to the common carotid artery. 5. COURSE: straight down the right internal jugular vein, right brachiocephalic vein, superior vena cava. 6. TIP: upper-to-mid right atrium. Internal path only inside an inset labeled "NOT TO SCALE". Never: catheter under the clavicle or in the subclavian vein, crossing the midline, exit site in the neck or on the abdomen, external cuff, sharp kink or double loop, tip in the right ventricle or high superior vena cava, red/blue clamps swapped.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ Path: chest-wall exit → cuff inside tunnel → over the clavicle → one loop into the low right internal jugular vein → superior vena cava → right atrium — confirmed
□ Entirely on the image left; never crosses the midline — confirmed
□ Red = arterial, blue = venous limbs below the hub — confirmed
```

**Module tile**

```
FILE NAME: images/patients-care-partners-14-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a calendar page with an appointment circled (no readable text) beside a walking cane. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-14-prepare-for-changing-kidney-care-needs-og.png (prep exports images/og/patients-care-partners-14-prepare-for-changing-kidney-care-needs-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Prepare for changing kidney care needs". Subtitle in teal #1a6b72: "Patients & Care Partners · Module K02 · 14 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a calendar page with an appointment circled (no readable text) beside a walking cane, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module K03 (15 of 32): The heart, kidney and sugar connection, and kidney-protecting medicines

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-15-heart-kidney-sugar-connection-and-protective-medicines-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder at a desk
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: A small early dip can mean the medicine is working; ask before stopping.
GROUNDED IN: Module K03 real situation "Ma'am Lyn's worrying dip": Ma'am Lyn, 57, an accountant with diabetes and CKD, starts an SGLT2 inhibitor. Four weeks later her eGFR is a little lower. A friend says the medicine is "killing her kidneys," and she considers stopping it.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder at a desk. Subject: Ma’am Lyn, an accountant in her late 50s with a short layered haircut, pearl earrings and a blazer, on a video call with her nephrologist on a laptop (screen softly blurred) while holding her printed laboratory results; a cup of coffee and a pill organizer nearby, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The heart, kidney and sugar connection**  ·  skill `infographic-skill`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-15-three-gears.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Mechanism analogy
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module K03, section "picture"
GROUNDED IN: Module K03, The everyday picture: The heart, the kidneys and the body's sugar and fat handling are linked like three gears in one clock. When one gear slips, the others strain: diabetes damages kidney filters, failing kidneys raise blood pressure and stiffen arteries, and a weak heart starves the kidneys of blood flow. Doctors now call this the cardiovascular-kidney-metabolic (CKM) connection. The good news is that some medicines turn all three gears in the right direction at once.

PROMPT:
Title at top in bold navy: "The heart, kidney and sugar connection". Three interlocking gears labeled "Heart", "Kidneys", "Sugar and fat handling", with arrows showing strain passing between them. Four hands steady the gears, tagged "ACE inhibitor or ARB", "SGLT2 inhibitor", "Finerenone", "GLP-1 medicine (for some)". Caption chip: "Ask: is one right for me?" No doses, no brand names. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Figure B: A small early dip, then slower decline**  ·  skill `simple-figure`  ·  placed in `lesson-3`

```
FILE NAME: images/patients-care-partners-15-early-dip.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Annotated line chart with trial bars
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module K03, section "lesson-3"
GROUNDED IN: Module K03, Lesson 3 "A small early dip can be expected": Because these medicines lower the pressure inside the filters, eGFR often dips slightly in the first weeks, like easing off the accelerator to save the engine. Your team will check blood tests after starting and decide whether the dip is the expected kind. Do not stop the medicine yourself because of one result. Also ask about sick-day pauses, low blood pressure symptoms and, for SGLT2 inhibitors, keeping the genital area clean, since sugar in the urine can encourage yeast infections.

PROMPT:
Title at top in bold navy: "A small early dip, then slower decline". Left: a schematic line chart (no axis numbers) with two lines: "Without protection" declining steadily and "With protection" dipping slightly at the start then declining more slowly; a callout on the dip: "Expected early dip: lower pressure inside the filter. Your team checks it." Right: two small bar pairs from trials: "DAPA-CKD: 14.5% → 9.2% over about 2.4 years" and "EMPA-KIDNEY: 16.9% → 13.1% over 2 years", captioned "Kidney decline, kidney failure or death from kidney or heart causes". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-15-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: three interlocking brass gears on a clean white surface. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-15-heart-kidney-sugar-connection-and-protective-medicines-og.png (prep exports images/og/patients-care-partners-15-heart-kidney-sugar-connection-and-protective-medicines-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "The heart, kidney and sugar connection, and kidney-protecting medicines". Subtitle in teal #1a6b72: "Patients & Care Partners · Module K03 · 15 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: three interlocking brass gears on a clean white surface, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module H01 (16 of 32): Navigate a hemodialysis treatment day

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-16-navigate-a-hemodialysis-treatment-day-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: eye level, medium
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Report cramps and dizziness early; it is part of the treatment.
GROUNDED IN: Module H01 real situation "Tatay Lito's quiet cramps": Tatay Lito, 70, gets leg cramps in the last hour of every session but says nothing, not wanting to bother the busy nurses. One day he feels faint, and his blood pressure drops sharply.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: eye level, medium. Subject: Tatay Lito, about 70, thin, white mustache, in a dialysis chair with a light blanket, raising his hand to signal while a dialysis nurse with braided hair in teal scrubs turns toward him; the machine and lines softly blurred; his left forearm rests on a pillow, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Inside the dialyzer**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-16-dialyzer.png
SKILL: williamriveromd-simple-figure + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Circuit and cutaway
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module H01, section "picture"
GROUNDED IN: Module H01, The everyday picture: During hemodialysis, your blood travels out through a needle or catheter, through a filter called a dialyzer, and back again. The dialyzer is a bundle of thousands of hair-thin hollow fibers. Blood flows inside the fibers, cleaning fluid called dialysate flows around them in the opposite direction, and waste and extra minerals cross the fiber walls from the side with more to the side with less. At the same time the machine gently pulls off extra water. Removing two or three days' worth of fluid in about four hours is why some people feel cramps or dizziness, and why reporting early helps.

PROMPT:
Title at top in bold navy: "Inside the dialyzer". Left: a seated, clothed patient with a left forearm fistula and two needles, red line to a blood pump, a vertical dialyzer, blue line back to the arm. Blood enters the dialyzer at the TOP and leaves at the BOTTOM; dialysate enters at the BOTTOM and leaves at the TOP (opposite directions). Right: a magnified cutaway of three hollow fibers: blood inside, dialysate outside, small waste dots crossing out, and a water drop labeled "extra fluid removed". Bottom: "Cramps or dizziness? Tell the nurse early." No machine numbers or brand. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK — FISTULA (overrides style): left forearm radiocephalic fistula, the cephalic vein joined end-to-side to the radial artery near the wrist; the arterialized vein is visibly enlarged and runs up the forearm under the skin. When needles are shown, the arterial needle (red) sits nearer the joining point and the venous needle (blue) is further up the arm and points AWAY from the joining point, toward the heart. A graft, if shown, is a separate soft tube looping under the forearm skin.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ Fistula on the left forearm near the wrist; vein enlarged up the forearm — confirmed
□ If needles shown: red nearer the joining point, blue further up pointing toward the heart — confirmed
```

**Module tile**

```
FILE NAME: images/patients-care-partners-16-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: an empty reclining dialysis chair with a folded blanket and a pillow, softly lit. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-16-navigate-a-hemodialysis-treatment-day-og.png (prep exports images/og/patients-care-partners-16-navigate-a-hemodialysis-treatment-day-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Navigate a hemodialysis treatment day". Subtitle in teal #1a6b72: "Patients & Care Partners · Module H01 · 16 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: an empty reclining dialysis chair with a folded blanket and a pillow, softly lit, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module H02 (17 of 32): Protect fistulas, grafts and dialysis catheters

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-17-protect-fistulas-grafts-and-dialysis-catheters-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: close, hands only
HUMAN VARIATION: Hands only
AUDIENCE: Patients and care partners
VISUAL GOAL: Feel the buzz morning and evening; if it weakens or stops, contact your unit promptly.
GROUNDED IN: Module H02 real situation "The silent fistula": On a Sunday morning, Kuya Dodong, 49, notices he cannot feel the usual buzz in his fistula. His next session is Monday, and he decides to wait.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: close, hands only. Subject: hands only: Kuya Dodong’s right fingertips resting lightly on the inside of his left forearm near the wrist, checking his fistula on a Sunday morning, his other hand reaching for a phone (screen blurred) on a wooden table beside a cup of coffee, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Know and protect your access**  ·  skill `infographic-skill`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-17-daily-check.png
SKILL: williamriveromd-infographic-skill + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Three-panel access care
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module H02, section "lesson-1"
GROUNDED IN: Module H02, Lesson 1 "Name your access": Ask your team to show you which access you have: a fistula (artery joined to vein), a graft (a soft tube joining them), or a catheter (a tube in a large vein in the neck or chest, with two colored caps outside the skin). If you have a fistula or graft, learn to feel the thrill with your fingertips every morning and evening, and to listen if you were taught. If the buzz becomes weak, changes to a pulse-like beat, or disappears, contact your unit promptly; clots are often easier to clear when treated early.

PROMPT:
Title at top in bold navy: "Know and protect your access". Panel 1 "Feel the thrill": fingertips on a left forearm fistula with soft vibration lines; ear icon "listen if taught". Panel 2 "Protect this arm": four crossed icons "No blood pressure, blood draws or drips on this arm", "No tight sleeves, watches or bracelets", "Do not sleep on it", "No heavy bags hanging from it". Panel 3 "Catheter": clothed right upper chest with a clean dry dressing and red and blue capped limbs; "Keep dry and covered", "Never open the caps"; internal path only in a NOT TO SCALE inset. Red banner: "Buzz weak, pulse-like or gone? Contact your unit promptly; clots are easier to clear early." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK — FISTULA (overrides style): left forearm radiocephalic fistula, the cephalic vein joined end-to-side to the radial artery near the wrist; the arterialized vein is visibly enlarged and runs up the forearm under the skin. When needles are shown, the arterial needle (red) sits nearer the joining point and the venous needle (blue) is further up the arm and points AWAY from the joining point, toward the heart. A graft, if shown, is a separate soft tube looping under the forearm skin.

ANATOMY LOCK — CATHETER PATH (tunneled-dialysis-catheter-path skill; follow exactly; overrides style): Anterior view, so the patient’s RIGHT side is on the IMAGE LEFT. The whole catheter is on the patient’s right (image left) and never crosses the midline. 1. EXIT SITE: right upper anterior chest wall, below the clavicle, a few finger-breadths lateral to the sternum, above the nipple line; below it a hub splits into two short external limbs hanging downward, RED clamp and cap (arterial) and BLUE clamp and cap (venous). 2. CUFF: a small textured cream-white Dacron cuff INSIDE the subcutaneous tunnel just above the exit site, under the skin. 3. TUNNEL: upward beneath the skin, passing OVER (in front of) the medial clavicle, never beneath it. 4. VENOTOMY AND LOOP: just above the clavicle ONE smooth gentle U-shaped turn into the LOW right internal jugular vein, lateral to the common carotid artery. 5. COURSE: straight down the right internal jugular vein, right brachiocephalic vein, superior vena cava. 6. TIP: upper-to-mid right atrium. Internal path only inside an inset labeled "NOT TO SCALE". Never: catheter under the clavicle or in the subclavian vein, crossing the midline, exit site in the neck or on the abdomen, external cuff, sharp kink or double loop, tip in the right ventricle or high superior vena cava, red/blue clamps swapped.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ Fistula on the left forearm near the wrist; vein enlarged up the forearm — confirmed
□ If needles shown: red nearer the joining point, blue further up pointing toward the heart — confirmed
□ Path: chest-wall exit → cuff inside tunnel → over the clavicle → one loop into the low right internal jugular vein → superior vena cava → right atrium — confirmed
□ Entirely on the image left; never crosses the midline — confirmed
□ Red = arterial, blue = venous limbs below the hub — confirmed
```

**Figure B: If a needle site bleeds at home**  ·  skill `algorithm-generator-skill`  ·  placed in `lesson-3`

```
FILE NAME: images/patients-care-partners-17-bleeding.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Action path
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module H02, section "lesson-3"
GROUNDED IN: Module H02, Lesson 3 "Have a bleeding plan": Bleeding from a needle site after dialysis is usually stopped with firm, steady pressure. Ask your nurse to show you exactly where and how to press, with clean gauze, and for how long before checking. Heavy or spurting bleeding that does not stop with pressure needs emergency help immediately: keep pressing while someone calls. Keep clean gauze and your contact card where you can find them quickly.

PROMPT:
Title at top in bold navy: "If a needle site bleeds at home". Start "Needle site bleeding" → "Press firmly with clean gauze, as your nurse showed you" → "Stopped?" Yes → "Keep watching; tell the unit at your next contact". No, heavy or spurting → red box "Keep pressing. Someone calls emergency help now." Side note: "Keep clean gauze and your contact card where you can find them." No times or numbers. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-17-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a left forearm resting on a pillow with two fingers gently on the inner wrist (hands only), clean and bright. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-17-protect-fistulas-grafts-and-dialysis-catheters-og.png (prep exports images/og/patients-care-partners-17-protect-fistulas-grafts-and-dialysis-catheters-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Protect fistulas, grafts and dialysis catheters". Subtitle in teal #1a6b72: "Patients & Care Partners · Module H02 · 17 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a left forearm resting on a pillow with two fingers gently on the inner wrist (hands only), clean and bright, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module H03 (18 of 32): Use dialysis reviews to improve daily life

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-18-use-dialysis-reviews-to-improve-daily-life-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: three-quarter
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Your review is numbers plus your experience; solve the barrier together.
GROUNDED IN: Module H03 real situation "Ate Joy leaves early": Ate Joy, 44, a single mother, ends her sessions 30 minutes early twice a week to pick up her children from school. Her waste removal results begin to fall, and she feels more tired.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: three-quarter. Subject: Ate Joy, mid-40s, single mother with a short pixie cut and a school-pickup tote bag, talking with a head nurse at a small review table in a dialysis unit; a printed monthly results sheet between them (unreadable), soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: A review looks beyond one number**  ·  skill `infographic-skill`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-18-review.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Dashboard figure
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module H03, section "lesson-1"
GROUNDED IN: Module H03, Lesson 1 "A review looks beyond one number": Ask how your team measures whether dialysis is working: tests of how much waste is removed (such as Kt/V or URR, the urea reduction ratio), hemoglobin for anemia, potassium, phosphorus, calcium and parathyroid hormone for bones and heart, albumin for nutrition, and your blood pressure and weight. Then tell them what the numbers cannot: how long you need to recover after a session, whether you sleep, eat and itch, and which activities you are struggling to keep.

PROMPT:
Title at top in bold navy: "A review looks beyond one number". Left: a clipboard with six unnumbered dials: "Waste removal (Kt/V, URR)", "Hemoglobin", "Potassium", "Phosphorus and calcium", "Albumin", "Blood pressure and weight". Right: three dials labeled "Only you can tell us": "Recovery time after a session", "Sleep, appetite and itch", "Activities I miss". Bottom: a session bar divided into four hours with waste removed steadily, the last part shaded with scissors: "Leaving early removes less." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-18-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a clipboard with a blurred results sheet beside a dialysis chair armrest. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-18-use-dialysis-reviews-to-improve-daily-life-og.png (prep exports images/og/patients-care-partners-18-use-dialysis-reviews-to-improve-daily-life-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Use dialysis reviews to improve daily life". Subtitle in teal #1a6b72: "Patients & Care Partners · Module H03 · 18 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a clipboard with a blurred results sheet beside a dialysis chair armrest, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module H04 (19 of 32): Potassium, phosphorus and fluid between sessions: why the rules exist

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-19-potassium-phosphorus-and-fluid-between-sessions-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C Radial
CAMERA: 45-degree tabletop
HUMAN VARIATION: No people
AUDIENCE: Patients and care partners
VISUAL GOAL: Plan the food and fluid before the longest gap between sessions.
GROUNDED IN: Module H04 real situation "Christmas Eve and the long gap": Tito Ernie, 62, dialyzes Monday, Wednesday and Friday. After his Friday session before Christmas, he enjoys Noche Buena: ham, fruit salad, buko juice and soft drinks. By Monday morning he feels weak and his legs feel heavy.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Radial. Camera: 45-degree tabletop. Subject: a Noche Buena table seen from the side: a sliced ham, a bowl of fruit salad, a young coconut with a straw and a soft drink, with a small medicine cup of phosphate binder tablets placed beside the plate and a wall calendar softly blurred behind, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Rising behind the dam**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-19-long-gap.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Weekly sawtooth chart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module H04, section "picture"
GROUNDED IN: Module H04, The everyday picture: Between dialysis sessions, things you eat and drink build up in the blood like water rising behind a dam. On a three-times-a-week schedule, the gaps are not equal: the weekend gap is a full day longer, so the water rises highest just before the first session of the week. That is when potassium and fluid are most likely to reach dangerous levels, and when planning matters most.

PROMPT:
Title at top in bold navy: "Rising behind the dam". A week strip Monday to Sunday with dialysis on Monday, Wednesday and Friday. Above it a sawtooth line rising between sessions and dropping on dialysis days, highest before Monday, labeled "Longest gap: plan ahead". Two icons riding the line: "Potassium" and "Fluid". Footer: "Never skip the session after a long gap." No values. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Figure B: Why binders go with meals**  ·  skill `simple-figure`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-19-binders.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Mechanism figure
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module H04, section "lesson-2"
GROUNDED IN: Module H04, Lesson 2 "Phosphorus, binders and bones": Phosphorus is found in protein foods, dairy and especially in processed foods with phosphate additives, such as some processed meats, instant noodles and soft drinks. Dialysis removes only part of it. High phosphorus pulls calcium from bones and can deposit calcium in blood vessels and the heart, making them stiff. Phosphate binders are medicines that grab phosphorus in the food inside your gut, which is why they must be taken with meals, not on an empty stomach. Ask how to time yours with your actual meals and snacks.

PROMPT:
Title at top in bold navy: "Why binders go with meals". Left: a plate with rice, fish and a soft drink, with small orange dots labeled "phosphorus (also in processed foods and some soft drinks)". Center: a schematic stomach and small intestine (dashed inset) where binder particles catch phosphorus dots so they leave in the stool. Right: two small panels "Too much phosphorus pulls calcium from bones" (bone icon) and "and stiffens blood vessels" (vessel icon). Footer: "Take binders with meals, as your team instructs." No doses. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-19-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a young coconut with a straw beside a small medicine cup of tablets and a plate. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-19-potassium-phosphorus-and-fluid-between-sessions-og.png (prep exports images/og/patients-care-partners-19-potassium-phosphorus-and-fluid-between-sessions-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Potassium, phosphorus and fluid between sessions: why the rules exist". Subtitle in teal #1a6b72: "Patients & Care Partners · Module H04 · 19 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a young coconut with a straw beside a small medicine cup of tablets and a plate, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module P01 (20 of 32): Prepare for supervised peritoneal dialysis training

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-20-prepare-for-supervised-peritoneal-dialysis-training-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F Human Connection
CAMERA: medium, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Only supervised training makes you ready for home PD.
GROUNDED IN: Module P01 real situation "Learning from a cousin's video": Bong, 38, a jeepney dispatcher, is scheduled for PD training next week. His cousin, also on PD, sends him videos and offers to teach him at home so he can "skip the training."

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Human Connection. Camera: medium, eye level. Subject: Bong, late 30s, jeepney dispatcher with a buzz cut and a reflective vest folded on his chair, practicing a PD exchange on a training model at a clean table, masked, while a PD nurse in white scrubs watches with a checklist; his wife sits beside him taking notes, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: How peritoneal dialysis works**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-20-fill-dwell-drain.png
SKILL: williamriveromd-simple-figure + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Three-step cutaway
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module P01, section "picture"
GROUNDED IN: Module P01, The everyday picture: Your abdomen is lined by a thin, living membrane called the peritoneum, rich in tiny blood vessels. In peritoneal dialysis, a sterile fluid is drained into your belly through a soft tube. Waste moves from the blood vessels into the fluid, and a sugar in the fluid draws out extra water, the way salt draws water out of cucumbers when you make atchara. After some hours, the used fluid is drained out and replaced. The membrane does the filtering; your job, after training, is to keep every connection clean.

PROMPT:
Title at top in bold navy: "How peritoneal dialysis works". Three steps, each a clothed person with a NOT TO SCALE abdominal cutaway inset: "Fill" (sterile fluid flows in through the catheter), "Dwell" (magnified circle: capillaries in the peritoneum with waste and water moving into the fluid; note "sugar in the fluid draws out water"), "Drain" (used fluid flows into a drain bag). Bottom: two icons "CAPD: exchanges by day" and "APD: a cycler at night", and a trainer watching a patient practice: "Only supervised training makes you ready." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK — PD CATHETER (overrides style): soft silicone Tenckhoff catheter entering the LOWER abdominal wall off the midline; exit site points DOWNWARD; deep cuff preperitoneal, superficial cuff about 2 cm inside the exit site; the tip lies low in the pelvis, never in the bladder or bowel. The peritoneum is a thin glossy membrane lining the abdominal wall and covering the bowel, rich in tiny capillaries. Internal anatomy only inside a labeled cutaway inset marked "NOT TO SCALE".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ PD exit site on the lower abdomen pointing downward — confirmed
□ Catheter tip low in the pelvis, not in bladder or bowel — confirmed
□ Anatomy only in a NOT TO SCALE inset — confirmed
```

**Module tile**

```
FILE NAME: images/patients-care-partners-20-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a PD training model and a mask on a clean table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-20-prepare-for-supervised-peritoneal-dialysis-training-og.png (prep exports images/og/patients-care-partners-20-prepare-for-supervised-peritoneal-dialysis-training-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Prepare for supervised peritoneal dialysis training". Subtitle in teal #1a6b72: "Patients & Care Partners · Module P01 · 20 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a PD training model and a mask on a clean table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module P02 (21 of 32): Recognize PD infection and contamination concerns

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-21-recognize-pd-infection-and-contamination-concerns-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: medium, warm lamp light at night
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: A cloudy bag is an urgent call, even at night.
GROUNDED IN: Module P02 real situation "Cloudy on a Saturday night": Aling Merly, 61, on CAPD in Pampanga, sees a slightly cloudy bag at 10 p.m. on Saturday. Her belly feels only mildly sore, and she does not want to disturb the nurse on a weekend.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: medium, warm lamp light at night. Subject: Aling Merly, early 60s, short curly gray hair, house dress, sits at her home exchange table at night holding up a drained PD bag to the lamp light while her daughter, mid-30s, dials a phone beside her; the bag looks faintly cloudy, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Clear or cloudy**  ·  skill `infographic-skill`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-21-cloudy.png
SKILL: williamriveromd-infographic-skill + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Comparison plus actions
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module P02, section "picture"
GROUNDED IN: Module P02, The everyday picture: Used PD fluid should look clear enough that you could read a newspaper through the bag. When germs reach the peritoneum, white blood cells rush in to fight them, and the fluid turns cloudy, sometimes before pain or fever appear. That is why cloudy fluid is the earliest alarm of peritonitis, an infection of the abdominal lining. Treated early, most episodes clear with antibiotics; delayed, they can damage the membrane or end PD.

PROMPT:
Title at top in bold navy: "Clear or cloudy". Left: two drained PD bags held in front of a printed newspaper page (generic text): print readable through the clear bag, unreadable through the cloudy bag; a magnified circle of white blood cells. Right: three action steps "Call your PD team now, day or night", "Keep the cloudy bag", "If you can’t reach them, go to the emergency department with the bag". A small exit-site close-up with labels "redness", "swelling", "crust or pus", "pain". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK — PD CATHETER (overrides style): soft silicone Tenckhoff catheter entering the LOWER abdominal wall off the midline; exit site points DOWNWARD; deep cuff preperitoneal, superficial cuff about 2 cm inside the exit site; the tip lies low in the pelvis, never in the bladder or bowel. The peritoneum is a thin glossy membrane lining the abdominal wall and covering the bowel, rich in tiny capillaries. Internal anatomy only inside a labeled cutaway inset marked "NOT TO SCALE".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ PD exit site on the lower abdomen pointing downward — confirmed
□ Catheter tip low in the pelvis, not in bladder or bowel — confirmed
□ Anatomy only in a NOT TO SCALE inset — confirmed
```

**Figure B: If a connection may be contaminated**  ·  skill `algorithm-generator-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-21-contamination.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Action path
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module P02, section "lesson-2"
GROUNDED IN: Module P02, Lesson 2 "Report a break in clean technique": If a connection touches something unclean, a cap falls off, a line cracks, or you are unsure whether a step was sterile, follow the response your trainer taught, and call the PD team promptly. Contamination does not always lead to infection, but reporting it lets the team decide whether you need preventive treatment. Never improvise a repair, and never add antibiotics or other medicines to a bag on your own.

PROMPT:
Title at top in bold navy: "If a connection may be contaminated". Start "A tip touched something, a cap fell off, or a line cracked" → "Stop. Follow the step your trainer taught you" → "Call the PD team promptly" → "The team decides about preventive treatment". Red side box: "Never repair it yourself. Never add medicine to a bag." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-21-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a clear PD drainage bag held up to window light. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-21-recognize-pd-infection-and-contamination-concerns-og.png (prep exports images/og/patients-care-partners-21-recognize-pd-infection-and-contamination-concerns-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Recognize PD infection and contamination concerns". Subtitle in teal #1a6b72: "Patients & Care Partners · Module P02 · 21 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a clear PD drainage bag held up to window light, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module P03 (22 of 32): Organize home dialysis routines and reassessment

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-22-organize-home-dialysis-routines-and-reassessment-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: medium, slightly high
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: A new helper or a long gap means a new skills check.
GROUNDED IN: Module P03 real situation "A new helper, an old habit": Tatay Nestor, 72, has done PD for three years with his wife's help. She is hospitalized, and his grandson Kevin, 22, offers to help after watching a few exchanges.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: medium, slightly high. Subject: Tatay Nestor, early 70s, bald with a gray goatee, and his grandson Kevin, 22, with a fade haircut and glasses, both masked at a clean home table while a PD nurse watches Kevin practice a connection on a training set; boxes stored on a shelf off the floor, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: A safe home routine**  ·  skill `infographic-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-22-home-station.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Room illustration with ring of triggers
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module P03, section "lesson-2"
GROUNDED IN: Module P03, Lesson 2 "Make supplies manageable": Store boxes off the floor in a clean, dry, cool place, use the oldest stock first, and check bags for damage and expiry before use. Plan deliveries around holidays and typhoon season, and tell the team early about travel. Follow the unit's waste disposal instructions. Ask how to report damaged or questionable supplies, and never use a bag that looks wrong.

PROMPT:
Title at top in bold navy: "A safe home routine". A modest Filipino home corner: a clean, well-lit table with a mask and hand rub, PD boxes on a raised shelf in a dry, cool corner labeled "Off the floor" and "Oldest first", a hand checking a bag labeled "Check for damage and expiry", and a wall record sheet with blank columns labeled "Records help the home team". Around it six skills-review triggers: "After an infection", "After a hospital stay", "New helper", "New equipment", "Eyesight, hands or memory changed", "Feeling unsure". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-22-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: stacked PD supply boxes on a raised shelf, off the floor, in a tidy room. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-22-organize-home-dialysis-routines-and-reassessment-og.png (prep exports images/og/patients-care-partners-22-organize-home-dialysis-routines-and-reassessment-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Organize home dialysis routines and reassessment". Subtitle in teal #1a6b72: "Patients & Care Partners · Module P03 · 22 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: stacked PD supply boxes on a raised shelf, off the floor, in a tidy room, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module T01 (23 of 32): Prepare for a kidney transplant evaluation

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-23-prepare-for-a-kidney-transplant-evaluation-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: three-quarter
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: A living donor has their own team and can say no at any time.
GROUNDED IN: Module T01 real situation "Ana and her brother": Ana, 31, on dialysis for a year, learns her brother Paolo wants to donate. Their mother pushes him hard, and Paolo privately feels unsure because he just got married.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: three-quarter. Subject: Paolo, late 20s, Ana’s brother, newly married, with a neat side part and a wedding ring, in a private consultation room with a transplant donor coordinator, a woman in her 40s with glasses; the door is closed, both seated, a water glass on the table, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Where a new kidney goes**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-23-where-it-goes.png
SKILL: williamriveromd-simple-figure + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)
IMAGE TYPE: Anatomy schematic plus two cards
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module T01, section "picture"
GROUNDED IN: Module T01, The everyday picture: A kidney transplant places a healthy kidney from a donor into the lower abdomen, where it is connected to blood vessels and the bladder; the old kidneys usually stay in place. The new kidney can do what dialysis cannot fully do: work all day, every day, including making hormones. But the body's immune system sees it as a stranger and will try to reject it unless medicines hold it back for as long as the kidney works. Evaluation is the process of checking whether the benefits outweigh those risks for you.

PROMPT:
Title at top in bold navy: "Where a new kidney goes". Left: an anterior translucent schematic of the abdomen and pelvis (cropped torso, no face): native kidneys in place; donor kidney in the right lower abdomen with labels "New kidney", "Artery", "Vein", "Ureter to bladder", "Your own kidneys usually stay". Right: two cards "Anti-rejection medicines keep the immune system calm for as long as the kidney works" and "A living donor has their own team and can say no at any time". A small gray chip: "Buying or selling organs is illegal." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

CONSTITUTION v1.0 ANATOMY LOCK — TRANSPLANT (overrides style): anterior view, patient’s RIGHT on the IMAGE LEFT. Native kidneys stay in their usual place (right slightly lower than left). The donor kidney sits in the RIGHT iliac fossa (image left, lower abdomen): its renal artery joins the external iliac artery (red, thick-walled), its renal vein joins the external iliac vein (blue, thin-walled), and its ureter enters the bladder dome. Never in the native kidney position, never joined to bowel, never mirrored.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.

ANATOMY QA (Constitution v1.0, Layer G):
□ Donor kidney in the right iliac fossa (image left) — confirmed
□ Artery to external iliac artery, vein to external iliac vein, ureter to bladder — confirmed
□ Native kidneys still present — confirmed
```

**Module tile**

```
FILE NAME: images/patients-care-partners-23-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two chairs facing each other in a quiet consultation room with a closed door and a glass of water. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-23-prepare-for-a-kidney-transplant-evaluation-og.png (prep exports images/og/patients-care-partners-23-prepare-for-a-kidney-transplant-evaluation-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Prepare for a kidney transplant evaluation". Subtitle in teal #1a6b72: "Patients & Care Partners · Module T01 · 23 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two chairs facing each other in a quiet consultation room with a closed door and a glass of water, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module T02 (24 of 32): Build a safe routine after transplantation

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-24-build-a-safe-routine-after-transplantation-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: close, 45-degree
HUMAN VARIATION: No people
AUDIENCE: Patients and care partners
VISUAL GOAL: Every anti-rejection dose matters; plan refills before you run out.
GROUNDED IN: Module T02 real situation "Rico's empty bottle": Rico, 27, two years after transplant, runs out of one anti-rejection medicine during a long weekend in Baguio. Feeling fine, he decides to wait until Tuesday to refill.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: close, 45-degree. Subject: a weekly pill organizer with morning and evening compartments next to a phone alarm screen (blurred) and a travel pouch with a spare three-day supply, on a pine table in a Baguio guesthouse with a misty window, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The steady guard**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-24-steady-guard.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Schematic level chart plus habits
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module T02, section "picture"
GROUNDED IN: Module T02, The everyday picture: Anti-rejection medicines work like a guard who keeps the immune system calm around the new kidney. The guard needs a steady level in the blood. Missed or late doses let the level fall, and the immune system can begin attacking quietly, often with no symptoms until damage shows in a blood test. Too much medicine, on the other hand, can harm the kidney and lower defenses against infection. That is why timing, consistency and blood level checks matter so much.

PROMPT:
Title at top in bold navy: "The steady guard". Left: a line staying inside a soft green band labeled "steady medicine level" over seven days; on day 4 a missed dose dips below into a pale orange zone where small immune-cell icons approach a kidney icon: "Rejection can start quietly". Right: three habit tiles "Alarms at the same times", "Weekly pill organizer", "Refill two weeks early", and a card "Ask before pomelo, grapefruit or herbal products". No drug names or level numbers. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-24-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a weekly pill organizer with morning and evening compartments beside a phone. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-24-build-a-safe-routine-after-transplantation-og.png (prep exports images/og/patients-care-partners-24-build-a-safe-routine-after-transplantation-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Build a safe routine after transplantation". Subtitle in teal #1a6b72: "Patients & Care Partners · Module T02 · 24 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a weekly pill organizer with morning and evening compartments beside a phone, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module T03 (25 of 32): Navigate transplant benefits across policy dates

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-25-navigate-transplant-benefits-across-policy-dates-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Coverage depends on which policy applies, and from what date.
GROUNDED IN: Module T03 real situation "Two dates, one surgery": Mrs. Dela Cruz's living-donor transplant was pre-authorized in early November 2026, with surgery planned for mid-December. Her son reads online that "the new package starts December" and assumes the new rules apply.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder. Subject: Mrs. Dela Cruz, mid-40s, with long hair in a low ponytail, and her adult son in a university shirt, sitting with a hospital benefits coordinator who holds a dated written estimate (unreadable) and a wall calendar softly blurred behind, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Published is not the same as effective**  ·  skill `simple-figure`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-25-dates.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Timeline
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module T03, section "lesson-2"
GROUNDED IN: Module T03, Lesson 2 "Check the transition": PhilHealth published Circular 2026-0019, revising the transplant package, on November 21, 2026. Its effectivity clause gives an expected effective date of December 6, 2026, fifteen days after publication; this date was calculated from the clause, not confirmed operationally. The circular also keeps the earlier rules for procedures pre-authorized and performed under the previous policy. Ask the coordinator which policy applies to your case and from what date.

PROMPT:
Title at top in bold navy: "Published is not the same as effective". Three chapter cards: "Evaluation", "Surgery (recipient and donor)", "Life after transplant (follow-up and medicines)". Below, a calendar strip: "Published November 21, 2026" and "Expected effective December 6, 2026 (calculated, not yet confirmed)" with a bracket "fifteen days". A chip: "Pre-authorized under the earlier rules? Ask which policy applies." Right: a hand holding "Dated written estimate". No peso amounts, no logos. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-25-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a wall calendar with two days circled (no readable text) beside a folder. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-25-navigate-transplant-benefits-across-policy-dates-og.png (prep exports images/og/patients-care-partners-25-navigate-transplant-benefits-across-policy-dates-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Navigate transplant benefits across policy dates". Subtitle in teal #1a6b72: "Patients & Care Partners · Module T03 · 25 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a wall calendar with two days circled (no readable text) beside a folder, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module S01 (26 of 32): Understand conservative kidney management

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-26-understand-conservative-kidney-management-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Conservative care is active care, focused on comfort and what matters.
GROUNDED IN: Module S01 real situation "Lola Iska's priority": Lola Iska, 86, with dementia and heart failure, has kidney function at about one-tenth of normal. Her children disagree: one wants dialysis "to do everything," another fears it would mean spending her last months in hospital.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide, eye level. Subject: Lola Iska, 86, small and frail, white hair in a bun, wrapped in a shawl in a cane chair on a shaded porch, holding her daughter’s hand while a home-visit nurse kneels beside her with a small medical bag; potted plants and afternoon light, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Conservative care is active care**  ·  skill `infographic-skill`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-26-active-care.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Care wheel
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module S01, section "lesson-1"
GROUNDED IN: Module S01, Lesson 1 "Care continues": CKM includes protecting remaining kidney function with medicines and diet, treating anemia, controlling fluid and blood pressure, and managing symptoms such as itch, breathlessness, poor sleep, nausea and pain. It includes emotional, spiritual and family support, and planning for the future. Ask your kidney team how they would address your own needs and who would coordinate your care.

PROMPT:
Title at top in bold navy: "Conservative care is active care". Center: an older Filipina at home in a garden chair with family near. A ring of six labeled care segments: "Symptom relief (itch, breathlessness, sleep)", "Protect remaining kidney function", "Anemia and fluid care", "Emotional and spiritual support", "Family meetings", "Plan for the future". A visiting nurse with a bag: "Your team stays with you." Warm but clinical, light background. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-26-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a cane chair with a shawl on a shaded porch beside potted plants. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-26-understand-conservative-kidney-management-og.png (prep exports images/og/patients-care-partners-26-understand-conservative-kidney-management-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Understand conservative kidney management". Subtitle in teal #1a6b72: "Patients & Care Partners · Module S01 · 26 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a cane chair with a shawl on a shaded porch beside potted plants, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module S02 (27 of 32): Plan for comfort and future care conversations

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-27-plan-for-comfort-and-future-care-conversations-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Talking about future care is a gift to the people who may decide for you.
GROUNDED IN: Module S02 real situation "Manang Elsa's kitchen-table talk": Manang Elsa, 78, on dialysis for six years, tells her nurse she is tired of hospital stays and worries her children will fight if she can no longer speak.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide, eye level. Subject: Manang Elsa, late 70s, silver hair cut short, glasses on a chain, speaking at a kitchen table to her three adult children while a nephrologist and a nurse listen; a rosary and a cup of tea on the table, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Talking about future care**  ·  skill `infographic-skill`  ·  placed in `lesson-2`

```
FILE NAME: images/patients-care-partners-27-future-care.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Scene plus card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module S02, section "lesson-2"
GROUNDED IN: Module S02, Lesson 2 "Talk about future situations": If you wish, discuss who should speak for you if you cannot communicate, what you would want if you became very ill, and what matters most: being at home, being free of pain, being with family, or trying every treatment. Ask a clinician how these preferences can be documented in your setting, since forms and legal recognition vary.

PROMPT:
Title at top in bold navy: "Talking about future care". A family around a kitchen table, the older woman speaking, a doctor and nurse listening. On the table a card "What matters to me" with icons "Being at home", "Free of pain", "With family", "Trying every treatment" and a line "Who should speak for me if I cannot: ________". Footer ribbon: "Ask your clinician how to record it; formal documents need your care team." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-27-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a kitchen table with a cup of tea, a rosary and a blank card. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-27-plan-for-comfort-and-future-care-conversations-og.png (prep exports images/og/patients-care-partners-27-plan-for-comfort-and-future-care-conversations-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Plan for comfort and future care conversations". Subtitle in teal #1a6b72: "Patients & Care Partners · Module S02 · 27 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a kitchen table with a cup of tea, a rosary and a blank card, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module A01 (28 of 32): Support someone while protecting their choices

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-28-support-someone-while-protecting-their-choices-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: side profile, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Support without taking over: the patient speaks first.
GROUNDED IN: Module A01 real situation "Who answers the doctor?": At every visit, Marites answers all the doctor's questions for her father, Mang Andoy, 70, who is fully able to speak for himself. He grows quiet and stops mentioning his own worries.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: side profile, eye level. Subject: Mang Andoy, about 70, tall and lean with a cap, speaking to a doctor across a clinic desk while his daughter Marites, mid-40s, in a work blouse, sits slightly behind him taking notes and smiling, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: A co-pilot, not the driver**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-28-co-pilot.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Analogy plus clinic inset
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module A01, section "picture"
GROUNDED IN: Module A01, The everyday picture: Filipino families care deeply, and that love sometimes turns into taking over: answering for the patient, deciding meals, hiding bad news. Good support is more like being a co-pilot than a driver. The co-pilot reads the map, watches the road and offers help, but the driver, if able, keeps the wheel. People who keep control over their own care tend to stay more engaged in it.

PROMPT:
Title at top in bold navy: "A co-pilot, not the driver". A jeepney with an older Filipino man driving and his adult daughter in the front seat holding a map, pointing. Three labels: "He keeps the wheel", "She reads the map", "They agree on the route". Inset: the same pair in a clinic, the father speaking first and the daughter taking notes. No plate numbers or operator names. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-28-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two pairs of hands on a clinic desk, an older man’s hand resting near a notebook held by a younger woman’s hand. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-28-support-someone-while-protecting-their-choices-og.png (prep exports images/og/patients-care-partners-28-support-someone-while-protecting-their-choices-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Support someone while protecting their choices". Subtitle in teal #1a6b72: "Patients & Care Partners · Module A01 · 28 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two pairs of hands on a clinic desk, an older man’s hand resting near a notebook held by a younger woman’s hand, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module A02 (29 of 32): Organize appointments, records and practical support

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-29-organize-appointments-records-and-practical-support-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: straight-on, eye level
HUMAN VARIATION: No people
AUDIENCE: Patients and care partners
VISUAL GOAL: A shared plan, a backup for every task, and private channels for medical details.
GROUNDED IN: Module A02 real situation "The family group chat": The Santos family coordinates Lolo Ben's dialysis in a 60-member group chat, where someone posts his laboratory results and PhilHealth details. Meanwhile, nobody is sure who is driving him on Friday.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: straight-on, eye level. Subject: a refrigerator door with a hand-drawn weekly roster on paper (columns and small avatar stickers, no readable names), a clean magnet holding a folded contact card, and a phone on the counter showing a small private chat (blurred), soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Make tasks visible, share carefully**  ·  skill `infographic-skill`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-29-roster.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Two-panel figure
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module A02, section "lesson-1"
GROUNDED IN: Module A02, Lesson 1 "Make tasks visible": Agree who helps with appointments, transport, meals, refills and paperwork. Use a simple shared calendar, on paper on the refrigerator or on a phone, and name a backup for each key task. Avoid assuming one person can be available all the time; overseas relatives can help with scheduling, reminders or costs even from afar.

PROMPT:
Title at top in bold navy: "Make tasks visible, share carefully". Left: a weekly roster on a refrigerator, columns Monday to Sunday, rows "Transport", "Meals", "Refills", "Paperwork", filled with avatar circles and a "Backup" badge on each row. Right: two phones: a large family group chat crossed out, labeled "Not for records, prescriptions or PhilHealth numbers", and a small private chat with four avatars labeled "Helpers only". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-29-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a refrigerator door with a hand-drawn weekly roster made of colored stickers, no readable names. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-29-organize-appointments-records-and-practical-support-og.png (prep exports images/og/patients-care-partners-29-organize-appointments-records-and-practical-support-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Organize appointments, records and practical support". Subtitle in teal #1a6b72: "Patients & Care Partners · Module A02 · 29 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a refrigerator door with a hand-drawn weekly roster made of colored stickers, no readable names, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module A03 (30 of 32): Prevent care partner burnout and arrange backup

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-30-prevent-care-partner-burnout-and-arrange-backup-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: environmental portrait
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: An empty cup cannot pour; ask for specific help.
GROUNDED IN: Module A03 real situation "Ate Rowena's breaking point": Ate Rowena, 46, has cared alone for her husband on PD for two years while working part-time. She has stopped seeing friends, sleeps four hours a night, and one morning forgets a step during an exchange.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: environmental portrait. Subject: Ate Rowena, mid-40s, tired but smiling, hair loosely tied, sitting on a bench outside a parish hall with a cup of coffee, a support-group member in her 60s sitting beside her with a hand on her shoulder, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: An empty cup cannot pour**  ·  skill `simple-figure`  ·  placed in `picture`

```
FILE NAME: images/patients-care-partners-30-empty-cup.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Analogy figure
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module A03, section "picture"
GROUNDED IN: Module A03, The everyday picture: Caring for someone with kidney failure is often a marathon run at sprint speed. Many care partners, especially wives and daughters, keep going until their own health breaks. An empty cup cannot pour. Looking after yourself is not selfish; it keeps the care going.

PROMPT:
Title at top in bold navy: "An empty cup cannot pour". A Filipina care partner holding a cup being refilled by four labeled streams: "Sleep", "Shared tasks", "Support group", "Time for myself". Side card: "‘Can you drive Tatay to dialysis every Wednesday this month?’ works better than ‘Can someone help?’" Badge: "Backup helpers need training for clinical tasks." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-30-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a ceramic mug being filled with coffee on a bench outside a church hall. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-30-prevent-care-partner-burnout-and-arrange-backup-og.png (prep exports images/og/patients-care-partners-30-prevent-care-partner-burnout-and-arrange-backup-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Prevent care partner burnout and arrange backup". Subtitle in teal #1a6b72: "Patients & Care Partners · Module A03 · 30 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a ceramic mug being filled with coffee on a bench outside a church hall, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module F01 (31 of 32): Support children, teens and growing independence

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-31-support-children-teens-and-growing-independence-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: three-quarter, eye level
HUMAN VARIATION: Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Patients and care partners
VISUAL GOAL: Hand over responsibility step by step, with a safety net.
GROUNDED IN: Module F01 real situation "JM turns seventeen": JM, 17, received a kidney transplant at 12. His mother has always managed his medicines. Now in senior high school, he wants freedom, stays out late, and sometimes skips evening doses.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: three-quarter, eye level. Subject: JM, 17, a Filipino teenager with a curtain haircut and a hoodie, filling his own weekly pill organizer at a clinic table while his mother watches from a chair behind him and a pediatric nurse in printed scrubs gives a thumbs-up, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Growing independence, step by step**  ·  skill `simple-figure`  ·  placed in `lesson-3`

```
FILE NAME: images/patients-care-partners-31-steps.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Staircase
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module F01, section "lesson-3"
GROUNDED IN: Module F01, Lesson 3 "Prepare for growing independence": Start gradually in early adolescence: letting the teen speak first in visits, learn their medicines, and book a refill. Ask who coordinates the move to adult services, what skills will be practiced, and when the first joint visit will be. This module is family orientation, not a complete pediatric curriculum.

PROMPT:
Title at top in bold navy: "Growing independence, step by step". A staircase of four steps, the same young person growing older on each: "Learns the names of his medicines", "Speaks first in visits", "Books his own refill; parent checks", "First joint visit with adult services". A pediatric nurse walks alongside. Caption: "Children are not small adults." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-31-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a school backpack beside a weekly pill organizer on a clinic table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-31-support-children-teens-and-growing-independence-og.png (prep exports images/og/patients-care-partners-31-support-children-teens-and-growing-independence-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Support children, teens and growing independence". Subtitle in teal #1a6b72: "Patients & Care Partners · Module F01 · 31 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a school backpack beside a weekly pill organizer on a clinic table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

### Module F02 (32 of 32): Recover after hospital care and rebuild your plan

**Hero (circular vignette)**

```
FILE NAME: images/patients-care-partners-32-recover-after-hospital-care-and-rebuild-your-plan-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C Radial
CAMERA: top-down flat lay
HUMAN VARIATION: No people
AUDIENCE: Patients and care partners
VISUAL GOAL: After a hospital stay, reconcile one clear plan.
GROUNDED IN: Module F02 real situation "Two lists, one patient": Mang Jose, 68, on hemodialysis, is discharged after pneumonia with a new list. At home his old box still holds a blood pressure medicine the ward had stopped because his pressure was low, and a new brand that is actually the same drug as one he already takes.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Radial. Camera: top-down flat lay. Subject: a hospital discharge folder, two printed medicine lists side by side with two lines circled (unreadable), a medicine box with blister packs and a highlighter on a dialysis unit counter, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or watermark; papers, screens and cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Two lists, one plan**  ·  skill `simple-figure`  ·  placed in `lesson-1`

```
FILE NAME: images/patients-care-partners-32-reconcile.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Merge diagram
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Patients and care partners (plain words), and the nurses who teach them
PLACED IN: Module F02, section "lesson-1"
GROUNDED IN: Module F02, Lesson 1 "Check what changed": Before leaving, ask the ward team to go through every medicine: what is new, what stopped, what changed dose, and why. At home, compare the discharge list with your old list and your actual medicine box. Bring both lists to your kidney team or pharmacist so differences are resolved. Do not combine conflicting instructions on your own.

PROMPT:
Title at top in bold navy: "Two lists, one plan". Left: two lists "Hospital discharge list" and "My home list" with placeholder bars (no drug names), two lines highlighted: "stopped in hospital" and "same medicine, different name". Arrow to a single "Reconciled list" held by a pharmacist and a patient’s daughter, with arrows to "Dialysis unit", "Kidney doctor", "Primary care doctor". Footer: "Bring both lists and your medicine box." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.
```

**Module tile**

```
FILE NAME: images/patients-care-partners-32-card.png (generate at 1536 × 1024; prep exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the page’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two printed lists side by side with a highlighter and a medicine box. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or watercolor style, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; photographic; no text.
```

**OG share card**

```
FILE NAME: images/og/patients-care-partners-32-recover-after-hospital-care-and-rebuild-your-plan-og.png (prep exports images/og/patients-care-partners-32-recover-after-hospital-care-and-rebuild-your-plan-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Patients, care partners and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · PATIENTS & CARE PARTNERS". Title in bold navy #0f1e2e, three lines at most: "Recover after hospital care and rebuild your plan". Subtitle in teal #1a6b72: "Patients & Care Partners · Module F02 · 32 of 32". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two printed lists side by side with a highlighter and a medicine box, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Light background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.
```

## 8. Audit checklist before publishing

- [ ] Every label spelled exactly as in the prompt (compare letter by letter).
- [ ] No number on an image that is not in its prompt; no doses, fluid amounts, targets or phone numbers.
- [ ] Heroes: square photograph, circle with white margin, empty title-safe zone, the module’s own situation, a different cast from the previous hero, no text.
- [ ] Figures: white background, Inter, crisp (not painted), © renalcarematters.com bottom-right; anatomy QA ticked where present.
- [ ] Catheter images follow the path lock (right upper chest exit, cuff inside, over the clavicle, low right internal jugular, right atrium; red arterial, blue venous).
- [ ] Tiles: 16:9 photographic still-life, readable at 320 px, no text.
- [ ] Share cards: light background, teal chip, text only in the left 55%, nothing important outside the 1.91:1 band.
- [ ] Any image that fails: note why, and write a corrected prompt in a new MD file in the working folder.
