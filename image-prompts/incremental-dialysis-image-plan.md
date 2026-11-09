# Image Plan: *Incremental Dialysis: Starting With the Kidney Function You Still Have* (`incremental-dialysis.html`)

**Guide:** Twice-weekly hemodialysis or lighter peritoneal dialysis (PD) when measured residual kidney function allows. Dual audience: Patients & Families (EN/TL/CEB/KAP) and Clinicians.
**Prepared:** 2026-11-09. **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the ChatGPT **Image Generator** GPT at https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` · `williamriveromd-simple-figure` · `williamriveromd-algorithm-generator-skill` (Mode C) · `williamriveromd-biomedical-mechanism-figure`

---

## Design intent: one idea per image, readable at every education level

The guide asks readers to grasp four ideas. Each image carries one of them, so a reader who only looks at the pictures still leaves with the core message.

| Idea the reader must get | Patient image | Clinician image |
|---|---|---|
| Your kidneys and dialysis **share** the work, and dialysis grows as the kidney share shrinks | #3 Shared work | #11 RKF physiology |
| The kidney share is **measured**, not guessed | #4 Urine collection | #8 Kru measurement |
| The plan is a **staircase** with checks and a ready third session | #5 Step-up staircase | #9 HD algorithm |
| HD and PD each have a lighter start, and each **steps up** | #6 HD and PD pathways | #10 PD schedules |
| Everyday habits **protect** what you still have | #7 Protect your kidneys | — |

**Readability rules used in every patient prompt:** no more than about 8 words on any label, plain words instead of jargon ("kidney share," not "Kru"), one icon per idea, and a strong left-to-right or bottom-to-top reading direction. Clinician prompts may use correct technical labels but keep each callout short.

## House rules baked into every prompt
- **Light backgrounds only** (white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, pale teal `#eef6f7`). Never navy, charcoal, or black fills.
- **Fonts:** on-image type is set in **Inter** (named in each prompt). Approved alternatives are Nunito Sans, IBM Plex Sans, and Manrope. No serif or decorative faces.
- **Palette:** navy `#0f1e2e` (text and accents only), clinical teal `#1a6b72` (dialysis and hemodialysis), renal green `#1f7a4d` (the patient's own kidneys and safe steps), amber `#b8860b` (caution and checks), red `#b91c1c` (urgent only), purple `#6c3d8e` (peritoneal dialysis accents, used sparingly).
- **Color logic is fixed across the set:** *green = your own kidneys*, *teal = dialysis*. Readers learn it once in #3 and reuse it in every later figure.
- **Attribution:** small, semi-transparent `renalcarematters.com` text, bottom-right (bottom-center on portrait), on every image **except the wordless vignette hero**.
- **American English** in all rendered text (hemodialysis, color, liter).
- **Save each asset** as `.png` **plus** a matching `.webp` twin in `images/`, using the exact FILE NAME given.

### Clinical guardrails for THIS guide (each must hold in every graphic)
1. **Stepping up is success, not failure.** Never show the third session or the added exchange as a red "warning" or a downward arrow. Use calm upward steps.
2. **No eligibility numbers in patient art.** Never print a Kru, urine-volume, or eGFR cutoff as a pass/fail gate. Clinician art may show numbers only where the prompt supplies them, always with units.
3. **Not a cost-saving picture.** No peso signs, wallets, or "save money" cues. Incremental dialysis is a medical plan built on measurement.
4. **Monitoring is always visible.** Any image of a twice-weekly schedule also shows a check (urine test, blood test, weight, or blood pressure).
5. **Respectful urine imagery.** Show only a closed, opaque collection container. No visible urine, no toilets in close-up.
6. **Dialysis equipment is accurate.** If a dialyzer or circuit appears, follow the house hemofilter anatomy (two end ports for blood, two side ports for dialysate with countercurrent flow). Prefer no circuit detail at all in patient images.
7. **Filipino clinical context** and calm, warm, daylight scenes. No distressed faces, no needles in the hero.

## Asset roster

| # | File (`images/…`) | Placement in guide | Skill | Size |
|---|---|---|---|---|
| 1 | `incremental-dialysis-vignette-hero.png` | Patient hero disc | hero-vignette (Scaffold A) | 2048×2048 |
| 2 | `incremental-dialysis-og.png` | `og:image` / social share | infographic (OG card) | 1200×630 |
| 3 | `incremental-dialysis-01-shared-work.png` | Patient §What it means | infographic (concept) | 1792×1024 |
| 4 | `incremental-dialysis-02-urine-collection.png` | Patient §Measuring | simple-figure (Scaffold C, steps) | 1792×1024 |
| 5 | `incremental-dialysis-03-step-up-staircase.png` | Patient §What we watch | infographic (journey) | 1792×1024 |
| 6 | `incremental-dialysis-04-hd-pd-pathways.png` | Patient §Stepping up | simple-figure (Scaffold B, comparison) | 1792×1024 |
| 7 | `incremental-dialysis-09-protect-kidneys.png` | Patient §Protect your kidneys | simple-figure (icon cards) | 1792×1024 |
| 8 | `incremental-dialysis-05-kru-measurement.png` | Clinician §Measuring Kru | simple-figure (Scaffold D) | 1792×1024 |
| 9 | `incremental-dialysis-06-incremental-hd-algorithm.png` | Clinician §HD workflow | algorithm (Mode C, house style) | 1024×1536 |
| 10 | `incremental-dialysis-07-pd-schedules.png` | Clinician §Incremental PD | simple-figure (Scaffold B/E) | 1792×1024 |
| 11 | `incremental-dialysis-08-rkf-physiology.png` | Clinician §Overview | biomedical-mechanism | 1792×1024 |

> **Wiring status.** All 11 `<figure>` / meta references are already in the guide HTML with matching file names, `width`/`height`, `alt` text, and lightbox captions (`.fig-desc` plus `.fig-abbrevs`). Until each file is committed, that figure shows its alt text. After saving the images, run `python3 patch_hero_fetchpriority.py --guide incremental-dialysis.html` and `python3 patch_image_lightbox.py --guide incremental-dialysis.html`.
>
> **Derived asset (no separate prompt):** `incremental-dialysis-rg-thumb.webp`, a 1:1 center crop of the OG card (#2), used by Related-guides cards on sibling guides.
>
> **Suggested generation order:** #1 and #2 first (they are visible on every share), then patient figures #3 to #7, then clinician figures #8 to #11.

---

## 1 · Circular vignette hero *(patient hero disc)*

```
FILE NAME: incremental-dialysis-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3, Scaffold A clinical people scene
ASPECT RATIO: 1:1 (square, displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J, Environmental Storytelling (one cohesive home scene, no floating panels)
CAMERA: over-the-shoulder / rear three-quarter view, eye level, shallow depth of field
HUMAN VARIATION (vs. previous guide, aki-icu-dialysis-decisions, a seated ICU family group with two clinicians):
  one person only (not a group); woman, late 30s (not a mixed-age family); standing (not seated);
  at home (not ICU); rear three-quarter view (not frontal environmental portrait); long dark hair
  in a low loose bun; slim build; medium-tan skin; small gold stud earring; mustard-yellow linen
  blouse with rolled sleeves; a slim wristwatch; her left hand lightly touching the calendar;
  calm, quietly hopeful profile expression; morning light (not ICU lighting).
AUDIENCE: patients and families
VISUAL GOAL: "My week can have room in it, and my plan is written on the calendar, ready to grow," wordless.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER
around the full circle (the circle must never touch the canvas edges). Composition archetype:
Environmental Storytelling. Camera: over-the-shoulder, rear three-quarter view at eye level,
gentle shallow depth of field.

Subject: a Filipino woman in her late thirties standing in the bright kitchen-dining corner of a
modest, tidy Philippine home on a weekday morning. She has long dark hair gathered in a low loose
bun, medium-tan skin, a slim build, a small gold stud earring, a mustard-yellow linen blouse with
rolled sleeves, and a slim wristwatch. Seen from behind her right shoulder, she lightly touches a
large paper wall calendar with her left hand. The calendar has NO readable words or numbers: it is
a clean grid of blank squares in which exactly two days of the same week carry a solid teal
(#1a6b72) dot, spaced apart, and one more day of that week is outlined with a dashed teal circle,
meaning "ready to add." Her face is visible in soft profile, calm and quietly hopeful. Supporting
context, softly out of focus: a small potted herb on the counter, a ceramic mug, a woven bayong
bag on a hook, and morning daylight from a window with capiz-shell panes.

Visual hierarchy: the woman and the calendar occupy 60–70% of the circle; 2–3 supporting context
cues fill 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft out-of-focus pale wall and window glow
in the upper-left of the circle (no faces, hands, objects, or calendar inside that zone).

Calm, warm, documentary-realistic color grade harmonizing with clinical teal #1a6b72, renal green
#1f7a4d, and warm neutrals on a light background. Slight edge falloff toward a soft neutral at the
rim. No dialysis machine, no needles, no hospital equipment, no medicine bottles in view.

Absolutely NO text of any kind: no title, subtitle, caption, label, numbers on the calendar, logo,
or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, dozens of icons, tiny
unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle,
cropped objects, edge clipping, objects touching the circular border, important content inside
the title safe zone, baked-in text, titles, captions, numbers, logos, watermarks, rectangular
borders, frames, banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR,
over-saturation, distorted hands or faces, peso signs or money imagery, hospital equipment.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin, never cropped.
One dominant subject (woman + calendar) at 60–70% of the circle; 20–25% empty title-safe zone
upper-left. Exactly two solid teal dots and one dashed circle on the calendar, with no readable
words or numbers. Filipino home context, morning daylight. No text anywhere.
```

---

## 2 · OG / social share card *(`og:image`)*

```
FILE NAME: incremental-dialysis-og.png
IMAGE TYPE: OG social share card, editorial split layout
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed, non-negotiable)
AUDIENCE: mixed (patients, families, clinicians)
VISUAL GOAL: In one glance on Facebook or Messenger: "Dialysis can start lighter when your own kidneys still help, and it steps up when needed."

PROMPT:
Social share card for a nephrology education guide, 1200×630 pixels, white (#ffffff) background
with a very soft pale-teal (#eef6f7) panel on the right 45% of the canvas. All typography set in
Inter.

LEFT SIDE (55%): a small teal (#1a6b72) uppercase eyebrow label "DIALYSIS · STARTING TREATMENT".
Below it, a large bold navy (#0f1e2e) headline on two lines: "Incremental Dialysis". Below that,
a medium-weight teal subline: "Starting with the kidney function you still have". Below that, a
single short navy line in regular weight: "2 sessions a week → 3 when needed". Generous left margin
and line spacing; nothing touches the edges.

RIGHT SIDE (45%, on the pale-teal panel): a clean semi-3D illustrated week strip of seven rounded
day tiles in a single row, with NO day names or numbers. Two non-adjacent tiles are filled solid
teal with a tiny simple dialysis-chair icon; one more tile is outlined with a dashed teal border
and a small "+" mark. Above the strip, a soft, semi-realistic pair of human kidneys tinted renal
green (#1f7a4d) with a gentle glow, connected by a thin dotted line down to the week strip,
meaning "your kidneys still contribute." Calm, uncluttered, plenty of negative space.

FOOTER: bottom-left, small navy text "W Rivero, MD · Nephrology". Bottom-right, small
semi-transparent (70% opacity) navy text "renalcarematters.com".

Style: premium medical-publication aesthetic, crisp edges, soft shadows only, no photographs of
people, no gradients darker than the pale-teal panel.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, misspelled words,
overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds;
light backgrounds only. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope); no serif,
decorative, or handwritten fonts. No peso signs or money imagery. No red or warning colors.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Headline readable at thumbnail size. The week strip shows two solid teal tiles
and one dashed "+" tile, with no day names or numbers. Kidneys are green, dialysis is teal.
All text spelled exactly as given. Attribution bottom-right.
```

---

## 3 · Shared work *(patient §What it means)*

```
FILE NAME: incremental-dialysis-01-shared-work.png
IMAGE TYPE: Patient concept infographic, three-stage comparison (infographic-skill archetype 4, simplified)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families (all literacy levels)
VISUAL GOAL: Show that the kidneys and dialysis share one job, and that dialysis grows as the kidney share shrinks.

PROMPT:
Clean patient-education infographic, white (#ffffff) background, all text in Inter. Title at top
center in bold navy (#0f1e2e): "Your kidneys and dialysis share the work". Small teal (#1a6b72)
subtitle: "When your kidneys do less, dialysis does more".

CENTER: three tall rounded columns standing side by side on a soft gray (#f3f4f6) base strip,
labeled underneath in navy: "At the start", "Months later", "Later on". Each column is the same
total height and represents one full week of blood-cleaning work. Each column is split into two
stacked colored parts with a soft semi-3D finish:
- the BOTTOM part is renal green (#1f7a4d) with a tiny simple kidney icon, labeled "Your kidneys";
- the TOP part is clinical teal (#1a6b72) with a tiny simple dialysis-chair icon, labeled "Dialysis".
In the first column, green fills roughly the lower third and teal the rest. In the second column,
green is smaller. In the third column, green is a thin band and teal fills almost the whole
column. Do NOT print any percentages or numbers on the columns.

Under the first column only, a small row of two teal calendar dots captioned "2 sessions a week";
under the third column, three teal calendar dots captioned "3 sessions a week". A gentle upward
navy arrow runs left to right beneath the columns, labeled "Checked with regular tests".

RIGHT MARGIN: a small rounded note card in pale teal (#eef6f7) with a magnifier icon and one line:
"Your team measures your kidney share with a timed urine test."

BOTTOM STRIP: full-width soft gray band with one navy sentence: "Starting lighter is a plan,
and the plan grows with you."

Generous whitespace, large labels readable on a phone, no clutter.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, percentages, numeric
thresholds, red warning colors, downward "decline" arrows, unrealistic anatomy, HDR, excessive
saturation. NEVER use dark backgrounds. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope).
No peso signs. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Three equal-height columns; green (kidneys) always at the bottom and shrinking left to right;
teal (dialysis) always on top and growing. No numbers on the columns. Labels ≤ 8 words.
Readable on mobile. Attribution bottom-right.
```

---

## 4 · Timed urine collection *(patient §Measuring)*

```
FILE NAME: incremental-dialysis-02-urine-collection.png
IMAGE TYPE: Simple figure, Scaffold C horizontal step sequence (4 steps)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and caregivers (low-literacy friendly)
VISUAL GOAL: Teach the four steps of a correct 24-hour urine collection so the result is accurate.

PROMPT:
Clean clinical education infographic, white (#ffffff) background, all text in Inter. Title at top
center in bold navy (#0f1e2e): "How to collect your urine for 24 hours". Teal (#1a6b72) subtitle:
"Every drop counts. Write down the times."

Four rounded rectangular cards arranged horizontally in a single row on a very soft gray
(#f3f4f6) panel, connected by bold navy right-pointing arrows. Each card has a colored top accent
band, a large numbered circle, a simple friendly semi-3D illustration, a bold step label, and one
short line of detail:

1. Teal band. Illustration: a simple wall clock beside a bathroom door, and a small notepad with a
   pencil. Label: "START". Detail: "Empty your bladder. Do not save it. Write the time."
2. Renal-green (#1f7a4d) band. Illustration: a large closed, opaque white collection jug with an
   orange screw cap, standing in a small cooler box. Label: "SAVE EVERY DROP". Detail: "Day and night,
   add all urine to the jug. Keep it cool."
3. Teal band. Illustration: the same wall clock showing the same time as card 1, and the notepad.
   Label: "FINISH". Detail: "At the end time, add one last urine. Write the time."
4. Navy band. Illustration: a Filipino patient handing the closed jug and the notepad to a smiling
   dialysis nurse in scrubs at a clinic counter. Label: "BRING IT IN". Detail: "Bring the jug and the
   times to your unit."

Below the row, a soft amber (#b8860b) outlined note with a small speech-bubble icon: "Missed some?
Tell the nurse. It is better to repeat the test."

Large labels readable on a phone, generous whitespace, calm and respectful.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid any visible urine, toilets in close-up, transparent containers showing contents, bodily
detail, cartoon style, clutter, tiny labels, AI gibberish text, clock faces with garbled numerals
(use a simple clock with hands and tick marks only), HDR, excessive saturation. NEVER use dark
backgrounds. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope). Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Exactly four cards in order START → SAVE EVERY DROP → FINISH → BRING IT IN. Jug is closed and
opaque. Clocks in cards 1 and 3 show the same time. Amber "Missed some?" note present. Text spelled
exactly as given. Attribution bottom-right.
```

---

## 5 · The step-up staircase *(patient §What we watch)*

```
FILE NAME: incremental-dialysis-03-step-up-staircase.png
IMAGE TYPE: Patient journey infographic (infographic-skill, journey pathway)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: The plan is a staircase with regular checks; stepping up to three sessions is expected and safe.

PROMPT:
Clean patient-education journey infographic, white (#ffffff) background, all text in Inter. Title
at top left in bold navy (#0f1e2e): "A plan that steps up with you". Teal (#1a6b72) subtitle:
"Regular checks tell your team when to add treatment".

MAIN VISUAL: a wide, gentle, semi-3D staircase of two broad steps rising from left to right, in
soft light-teal (#eef6f7) with crisp teal edges.
- LOWER STEP (left): a small calm illustrated Filipino man in his 50s seated in a dialysis chair,
  with a row of two solid teal calendar dots labeled "2 sessions a week".
- UPPER STEP (right): the same man, relaxed, with three solid teal calendar dots labeled
  "3 sessions a week".
- Between the steps, a soft green (#1f7a4d) upward arrow labeled "Step up on time".

ALONG THE LOWER STEP: four small round check icons in a row, each with a one-word label:
a urine jug "Urine test", a blood tube "Blood test", a bathroom scale "Weight",
a blood-pressure cuff "Blood pressure". Above them a thin dashed loop arrow labeled
"About every month".

A SMALL SIGNPOST at the riser between the steps, amber (#b8860b) outline, with three tiny icons
and labels: a smaller water drop "Less urine", a puffy ankle "More swelling",
a tired face "Feeling unwell". Caption under the signpost: "Signs it may be time".

BOTTOM STRIP: soft gray band, navy text: "Adding the third session means the plan is working."

Calm, reassuring, plenty of whitespace, mobile-readable labels.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid red alarm colors, downward arrows, distressed faces, needles, visible blood, cartoon style,
clutter, tiny labels, AI gibberish text, numeric thresholds, HDR, excessive saturation. NEVER use
dark backgrounds. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope). Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Two steps only, rising left to right. Same patient on both steps. Two dots on the lower step,
three on the upper. Four check icons present. Signpost is amber, not red. Attribution bottom-right.
```

---

## 6 · Hemodialysis and PD pathways *(patient §Stepping up)*

```
FILE NAME: incremental-dialysis-04-hd-pd-pathways.png
IMAGE TYPE: Simple figure, Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Show that both hemodialysis and home PD can start lighter, and both step up the same way.

PROMPT:
Medical education comparison infographic, white (#ffffff) background, all text in Inter. Title
centered at top in bold navy (#0f1e2e): "Two ways to start lighter". Soft dashed vertical divider
splitting the canvas into two equal rounded panels on very soft gray (#f3f4f6).

LEFT PANEL, header in clinical teal (#1a6b72): "Hemodialysis at the unit". Small semi-3D image of
a calm Filipino patient in a dialysis chair with a hemodialysis machine beside them, simple and
clean (no tubing detail). Below it, a "BEFORE → AFTER" pair:
- "Start": a week strip of seven blank rounded tiles with two solid teal tiles.
- green (#1f7a4d) arrow labeled "When needed".
- "Then": the same strip with three solid teal tiles.
Caption: "Two visits a week, then three."

RIGHT PANEL, header in soft purple (#6c3d8e): "Peritoneal dialysis at home". Small semi-3D image
of a Filipino patient at home beside a stand holding a PD solution bag (closed, no readable label),
in a bright tidy room. Below it, a "BEFORE → AFTER" pair:
- "Start": a single day shown as a row of three PD bag icons.
- green arrow labeled "When needed".
- "Then": a row of four PD bag icons, plus a small cycler-machine icon with a moon labeled
  "or more machine time at night".
Caption: "Fewer bag changes, then more."

BOTTOM STRIP across both panels: soft pale-teal (#eef6f7) band with a small magnifier icon and
navy text: "Both plans include regular tests and a ready plan to add more."

Rounded corners, ample negative space, labels readable on a phone.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid normal-versus-disease framing (both panels are equal, neither is "wrong"), red colors,
needles, visible blood, garbled machine labels, readable brand names on bags or machines, cartoon
style, clutter, tiny labels, AI gibberish text, HDR. NEVER use dark backgrounds. Use ONLY Inter
(or Nunito Sans, IBM Plex Sans, Manrope). Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Two equal panels. Left: two teal tiles → three teal tiles. Right: three bags → four bags (plus
night cycler option). Green "When needed" arrows on both sides. No brand names. Attribution
bottom-right.
```

---

## 7 · Protect your kidney function *(patient §Protect your kidneys)*

```
FILE NAME: incremental-dialysis-09-protect-kidneys.png
IMAGE TYPE: Simple figure, five icon cards (Scaffold C variant, no arrows)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and caregivers (low-literacy friendly)
VISUAL GOAL: Five everyday habits that protect remaining kidney function, recognizable from icons alone.

PROMPT:
Clean patient-education infographic, white (#ffffff) background, all text in Inter. Title at top
center in bold navy (#0f1e2e): "Protect the kidney function you still have". Small renal-green
(#1f7a4d) subtitle: "Five everyday habits". At top center, a small semi-3D pair of kidneys tinted
renal green inside a soft protective shield outline.

Five equal rounded cards in one row on a very soft gray (#f3f4f6) panel, each with a large
friendly semi-3D icon, a bold label of up to four words, and one short line:
1. Icon: a box of pain-reliever tablets with a red (#b91c1c) diagonal "no" stroke. Label:
   "Skip NSAID pain pills". Line: "Ask before ibuprofen or mefenamic acid."
2. Icon: a CT scanner ring with a small speech bubble. Label: "Tell before scans". Line: "Say you
   still have kidney function."
3. Icon: a glass of water beside a bright sun. Label: "Avoid dehydration". Line: "Vomiting,
   diarrhea, or heat? Call your team."
4. Icon: a weekly pill organizer. Label: "Take medicines as prescribed". Line: "Including your
   water pill."
5. Icon: a plate with rice, fish, and vegetables beside a dietitian's clipboard. Label: "Ask before
   changing diet". Line: "Your dietitian sets your protein."

Each card has a thin renal-green top accent band, except card 1, which has an amber (#b8860b)
band. Large icons, short words, generous spacing, readable on a phone.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid readable drug brand names, cartoon style, clutter, tiny labels, AI gibberish text,
misspellings of "ibuprofen" and "mefenamic", HDR, excessive saturation. NEVER use dark backgrounds.
Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope). Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
Exactly five cards in the given order. Only card 1 uses red, as a small "no" stroke. Drug names
spelled correctly. Kidneys in shield at top are green. Attribution bottom-right.
```

---

## 8 · Measuring Kru *(clinician §Measuring Kru)*

```
FILE NAME: incremental-dialysis-05-kru-measurement.png
IMAGE TYPE: Simple figure, Scaffold D single-mechanism schematic
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (nephrologists, dialysis nurses)
VISUAL GOAL: Show why Kru uses the time-averaged blood urea across the collection window, not the pre-dialysis peak.

PROMPT:
Publication-grade clinical schematic, AJKD graphical-abstract style, white (#ffffff) background,
all text in Inter. Title at top left in bold navy (#0f1e2e): "Measuring residual urea clearance
(Kru)". Teal (#1a6b72) subtitle: "Use the time-averaged blood urea across the collection window".

MAIN PANEL (upper two-thirds): a clean line chart on a light grid. X-axis: a 7-day week labeled
only "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun". Y-axis label: "Blood urea" (no numbers).
Draw a navy saw-tooth curve for a twice-weekly hemodialysis schedule: sharp drops on Mon and Thu
(small teal dialysis markers labeled "HD" at each drop), then steady rises between sessions.
Shade the interval from Tue to just before Thu in pale green (#1f7a4d at 15% opacity), labeled
"Urine collection window". Across that shaded window, draw a horizontal dashed green line labeled
"Time-averaged blood urea". At the right end of the window, mark the curve's peak just before
dialysis with a small amber (#b8860b) dot labeled "Pre-HD peak: overstates the average".

LOWER PANEL: a rounded pale-teal (#eef6f7) formula card, centered, in clean typography:
"Kru (mL/min) = (urine urea ÷ time-averaged blood urea) × urine volume (mL) ÷ collection minutes".
Under it, two small side notes in soft gray cards:
- left: "Same analyte and units in urine and blood"
- right: "Report absolute (mL/min) and indexed (mL/min/1.73 m²) separately"

Thin lines, restrained palette, generous whitespace, labels readable at slide size.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid numeric values on the y-axis, invented thresholds, extra dialysis sessions beyond Mon and
Thu, garbled formula characters, cartoon style, clutter, tiny labels, AI gibberish text, 3D
effects on the chart, HDR. NEVER use dark backgrounds. Use ONLY Inter (or Nunito Sans, IBM Plex
Sans, Manrope). Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Two HD drops only (Mon, Thu). Green shaded window between sessions with a dashed average line
lying BELOW the pre-HD peak. Formula reproduced exactly. Attribution bottom-right.
```

---

## 9 · Incremental HD algorithm *(clinician §HD workflow)*

```
FILE NAME: incremental-dialysis-06-incremental-hd-algorithm.png
IMAGE TYPE: Clinical algorithm, Style Mode C (renalcarematters.com house style)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: Incremental HD as a loop: measure, model, start twice weekly with support, monitor, escalate on defined triggers.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house
style. Use a white background, restrained navy (#0f1e2e) and teal (#1a6b72) typography set in
Inter, thin teal connector arrows, and generous margins. Portrait, centered, top-to-bottom.

Title: "Incremental hemodialysis: from selection to escalation". Subtitle (teal, smaller):
"Measure, model, monitor, step up".

Nodes, in order:
1. Navy-outlined rounded rectangle: "Planned start of maintenance HD".
2. Teal diamond: "Measured Kru and urine volume? Volume, K⁺, HCO₃⁻ controlled? Reliable follow-up
   and a backup chair?"
   - "No" branch → left → green rounded rectangle: "Start thrice weekly. Re-measure later if
     appropriate."
   - "Yes" branch → down.
3. Navy rounded rectangle: "Model weekly stdKt/V (dialytic + renal). Target 2.3, minimum 2.1"
   with a small soft-gray side note: "KDOQI 2015, Not Graded".
4. Teal rounded rectangle: "Start twice weekly + support: loop diuretic, NaHCO₃, K⁺ binder as
   needed".
5. Soft-gray rounded rectangle with a circular dashed loop arrow returning to itself: "Monitor:
   weight and BP every session · K⁺ and chemistry closely early · Kru about monthly (example
   cadence) · repeat sooner after illness".
6. Amber (#b8860b) diamond: "Escalation trigger? Falling Kru · total < 2.1 · K⁺/HCO₃⁻/PO₄ off
   target · congestion or high UFR after the long gap · uremic symptoms · unscheduled sessions"
   - "No" → curved arrow back up to node 5.
   - "Yes" → down.
7. Green (#1f7a4d) rounded rectangle (endpoint): "Add the third weekly session. Review dose and
   adjuncts."

A soft-gray footnote box at the bottom: "Study thresholds (e.g., Kru ≥ 2.5 mL/min; ≥ 3 mL/min/1.73
m²) describe trial populations, not eligibility rules."

Consistent node widths, aligned center trunk, short readable text, generous spacing.
Include a small professional footer reading "© renalcarematters.com" positioned at the bottom-center
in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No dark background, no photos, no people, no 3D, no clutter, no decorative icons, no serif fonts,
no garbled subscripts or symbols (render K⁺, HCO₃⁻, PO₄, NaHCO₃, stdKt/V exactly), no extra nodes
or invented thresholds. Never omit the attribution.

QUALITY CHECK:
Seven nodes plus one side endpoint and one footnote. Two loops back to monitoring are visible.
Numbers limited to 2.3, 2.1, 2.5, and 3 with units as written. Attribution bottom-center.
```

---

## 10 · Incremental PD schedules *(clinician §Incremental PD)*

```
FILE NAME: incremental-dialysis-07-pd-schedules.png
IMAGE TYPE: Simple figure, Scaffold B/E hybrid (schedule comparison + mini table)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians and PD nurses
VISUAL GOAL: Compare full-dose and incremental PD schedules by weekly fills and liters, and remind that clearance and UF change too.

PROMPT:
Publication-grade clinical comparison figure, white (#ffffff) background, all text in Inter.
Title at top left in bold navy (#0f1e2e): "Incremental PD: what changes in a week". Teal (#1a6b72)
subtitle: "Burden falls, and so may peritoneal clearance and ultrafiltration".

THREE equal rounded panels in a row on soft gray (#f3f4f6), each topped by a simple 24-hour clock
ring (tick marks only, no numerals) with colored arcs showing dwell periods:
1. Header (navy): "Full-dose CAPD". Clock with four evenly spaced exchange markers (small bag
   icons) and continuous dwell arcs. Stats below in large type: "4 × 2 L daily", "28 fills/week",
   "56 L/week".
2. Header (purple #6c3d8e): "Incremental CAPD". Clock with three exchange markers and continuous
   dwell arcs. Stats: "3 × 2 L daily", "21 fills/week", "42 L/week".
3. Header (purple): "Incremental APD". Clock with a night arc shaded as a cycler period (small
   cycler icon with a moon) and an empty, unshaded daytime arc labeled "No day dwell". Stats:
   "5 nights: 4 × 2 L + 1 L last fill", "25 fills/week", "45 L/week".

Below the panels, a full-width pale-teal (#eef6f7) strip with two short notes separated by a thin
divider:
- left (with a small kidney icon in green #1f7a4d): "Measure renal and peritoneal clearance separately"
- right (with a small water-drop icon in amber #b8860b): "Fewer exchanges can lower UF; watch volume"

Clean vector-like icons, restrained palette, generous whitespace, readable at slide size.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid clock numerals, brand names on bags or cyclers, extra statistics, invented Kt/V values,
garbled "×" or "L" symbols, cartoon style, clutter, tiny labels, AI gibberish text, HDR. NEVER use
dark backgrounds. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope). Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Panel stats exactly: 28 / 56, 21 / 42, 25 / 45. APD panel shows an unshaded day. Two notes in the
bottom strip. Attribution bottom-right.
```

---

## 11 · Why residual kidney function matters *(clinician §Overview)*

```
FILE NAME: incremental-dialysis-08-rkf-physiology.png
IMAGE TYPE: Biomedical mechanism figure (review-article schematic, organ → inset → summary flow)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Residual function works continuously and handles more than urea; intermittent HD works in bursts. Their sum is the patient's real clearance.

PROMPT:
Create a publication-grade biomedical mechanism schematic, review-article style, white background,
soft semi-3D shading on clean vector-like anatomy, all labels in Inter.

Topic: Residual kidney function (RKF) during incremental hemodialysis.
Disease context: kidney failure at the start of maintenance dialysis.
Central mechanism: continuous native clearance adds to intermittent dialytic clearance.

Title at top left in bold navy (#0f1e2e): "Why residual kidney function matters".

ORGAN-LEVEL PANEL (left): a simplified pair of kidneys in light gray-blue with renal artery (red)
and vein (blue), one kidney partly shaded in soft yellow to show remaining functioning nephrons.
Label: "Kidney failure with RKF". A thin dashed connector leads to the magnified panel.

MAGNIFIED PANEL (center, dashed border): a single nephron with the glomerulus and tubule; the
tubule is highlighted in pale yellow. A small round clock icon beside it labeled "24 h a day,
10,080 min a week". Concise callout arrows leaving the nephron into a collecting duct:
- "Urea and creatinine"
- "Sodium and water"
- "Potassium and phosphate"
- "Middle molecules (β₂-microglobulin)"
- small side callout: "Hormones: erythropoietin, active vitamin D"

RIGHT PANEL: a small clean line chart titled "Blood urea over one week" (no axis numbers): a navy
saw-tooth curve with two sharp drops labeled "HD" (twice weekly), and a second, flatter green
(#1f7a4d) curve labeled "With RKF: lower, flatter peaks", sitting below the navy curve between
sessions.

BOTTOM SUMMARY FLOW (three boxes with arrows left → right):
- Left pale-pink box: "Without RKF" · "Higher interdialytic peaks" · "More fluid and K⁺ between
  sessions" · "Dialysis must do all the work".
- Center neutral box with a kidney + dialysis-chair icon: "Incremental HD: credit measured Kru
  toward weekly stdKt/V".
- Right pale-blue box: "With measured RKF" · "Fewer sessions possible" · "Better volume and
  potassium control (association)" · "Re-measure as RKF declines".

Muted clinical palette, thin dashed connectors, generous whitespace, labels readable at slide size.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, invented numbers or
thresholds, survival claims stated as proven, garbled Greek letters (render β₂ exactly), serif
fonts, cartoon style. Use ONLY Inter (or Nunito Sans, IBM Plex Sans, Manrope). Never omit the
attribution.

QUALITY CHECK:
Organ panel → dashed nephron inset → week curve → three-box summary flow. Green curve lies below
the navy curve between sessions. The word "association" appears in the right box. No numbers
except "10,080 min" and "24 h". Attribution bottom-right.
```

---

## After generation: checklist

1. Save each PNG to `images/` with the exact file name, and export a `.webp` twin (quality about 82).
2. For #1, keep it square at 2048×2048 (the HTML already declares `width="2048" height="2048"`).
3. Export `incremental-dialysis-rg-thumb.webp` (1:1 center crop of #2, about 600×600).
4. Run `python3 patch_hero_fetchpriority.py --guide incremental-dialysis.html` and `python3 patch_image_lightbox.py --guide incremental-dialysis.html`.
5. Open the guide in light and dark mode: figures sit on light `.illus-wrap-light` cards in both themes, so no image should need a dark variant.
6. Commit the images to `main`.
