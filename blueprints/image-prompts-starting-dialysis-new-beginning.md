# Image Plan Blueprint — Why Starting Dialysis Is Not a Death Sentence, but a New Beginning

**Guide:** `guides/starting-dialysis-new-beginning.html` · **Companion calculator:** `guides/calc-starting-dialysis-planner.html`
**Version:** 2.0 · November 22, 2026 (replaces the 9-image v1 pack)
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/
**Skills used:** `williamriveromd-hero-vignette` (001) · `williamriveromd-infographic-skill` (002, 003, 007, 009, 012, 015, 021) · `williamriveromd-simple-figure` (004, 005, 006, 008, 010, 011, 013, 014, 016, 017, 020) · `williamriveromd-biomedical-mechanism-figure` (018) · `williamriveromd-algorithm-generator-skill` (019) · Stage 2 schema from `williamriveromd-local-image-generator` · attribution and anatomy rules from `williamriveromd-infographic-generator` (Constitution v1.0) · machine rule from `dialysis-circuit-schematic`
**Local folder (Stage 2):** `/Users/williamgregoryriveromd/Downloads/New Beginning/images/`

---

## Part A — Visual strategy

### A.1 The teaching problem the images must solve

The reader has just heard “it is time” and is afraid. Many carry a picture of a relative who started dialysis late and very sick. Words alone will not replace that picture; another picture can. The set therefore does two jobs in every patient image: it shows honestly what dialysis does and does not do, and it shows ordinary Filipino life continuing around it.

The guide's argument runs in six steps, and each step gets one image a person can understand without reading:

| Step in the guide | What the reader must come away with | Patient image | Clinician image |
|---|---|---|---|
| Her story | There is still a life to plan for; three things to carry | Hero (001), pocket card (003) | — |
| What dialysis does | Part of three jobs, a few hours at a time | Four jobs (004), 168 versus 12 hours (005) | Replaced versus not replaced (016) |
| Why now | Waiting has a physical cost | Acid, waste, fluid (006) | Composite judgment, not a number (017) |
| What to expect | The slide stops; climbing back takes more | Symptom line plus supports (007), first day (008) | EQUAL panels (018) |
| The plan | Ninety days with four stops; a week that still has a life in it | Roadmap (009), week planner (010) | Early-risk window (019 chart), pathway algorithm (020) |
| Choices, prognosis, safety, coverage | Options stay open; ask for three scenarios; know the red flags; know what is covered | Crossroads (011), three paths (012), warning signs (013), coverage card (014) | Trial design (015) |

### A.2 Designing for every educational level

Each patient image is built in three layers, so no reader is locked out:

1. **Picture layer (no reading needed).** The meaning must survive with every word covered. Run this “cover-the-words test” on each output before accepting it.
2. **Label layer (about grade 5).** At most eight labels per image, two to five words each, everyday words: “water,” “waste,” “ride,” “call today.” No acronyms on patient images except HD and PD where the guide has already taught them.
3. **Caption layer (four languages).** The `fig-desc` captions already in the guide carry the explanation in English, Tagalog, Cebuano, and Kapampangan. Bake no Tagalog, Cebuano, or Kapampangan into the images.

Other rules that serve low-literacy and anxious readers: one idea per image; left-to-right or top-to-bottom order only; color is never the only signal (red and amber panels also differ by icon and header words); familiar Philippine objects stand in for abstractions (a jeepney for transport, a covered plate for a ready meal, a parol for the season in the story); faces are calm, never frightened; no blood, no needles in skin.

Clinician images keep the same visual grammar and add precision: units, study names, and the limits of the data on the image itself.

### A.3 Style decision: illustrated, not flat

All figures request **soft semi-3D rendered illustration** or photorealistic editorial imagery, to match the site's GPT-rendered look. Flat vector clip-art is excluded. The two deliberate exceptions are the bar chart (019) and the flowchart (020), whose skills are chart and line-art by design.

### A.4 What stays code-native (do not generate)

Survival percentages, confidence intervals, hazard ratios, and the 90-day checklist text stay in HTML. Six prompts contain numbers and need a digit-by-digit proofread: 005 (168, 12), 014 (156; 6,350), 015 (445; 18%; 28%), 018 (13.3; 5.9; 13; 11), 019 (26.7; 16.9; 13.7; 120; 121–365), 020 (7, 30, 90).

### A.5 Image inventory and placement

All in-body files are already referenced in the guide with alt text and captions. Each needs a PNG and a WebP twin with the same base name, prefixed `starting-dialysis-new-beginning-`.

| # | File base name (after the prefix) | Section | Audience | Skill / archetype | Size | Priority |
|---|---|---|---|---|---|---|
| 001 | `vignette-hero` | Hero | Patients | Circular vignette hero v3 — Scaffold A people · Composition J (Environmental Storytelling) · camera: side profile, wide | 2048×2048 | **P1** |
| 002 | `og` | `<head>` | Mixed | OG / social share card | 1200×630 | **P1** |
| 003 | `12-three-things-pocket-card` | `#story` | Patients | Simple figure — single object | 1792×1024 | **P2** |
| 004 | `01-kidney-jobs-and-dialysis` | `#what-dialysis-does` | Patients | Simple figure — comparison | 1792×1024 | **P1** |
| 005 | `08-168-hours-versus-12` | `#what-dialysis-does` | Patients | Simple figure — two timelines | 1792×1024 | **P1** |
| 006 | `09-why-waiting-becomes-less-safe` | `#why-now` | Patients | Simple figure — cause and three effects | 1792×1024 | **P1** |
| 007 | `03-symptoms-before-after` | `#what-might-improve` | Patients | Patient infographic — one curve plus supports | 1792×1024 | **P1** |
| 008 | `10-first-treatment-day` | `#first-treatment` | Patients | Simple figure — three steps | 1792×1024 | **P1** |
| 009 | `02-first-90-days-roadmap` | `#your-first-90-days` | Patients | Patient infographic — four-stop path | 1792×1024 | **P1** |
| 010 | `11-a-week-with-dialysis` | `#daily-life` | Patients | Simple figure — week planner | 1792×1024 | **P1** |
| 011 | `04-options-remain-open` | `#options-remain-open` | Patients | Simple figure — crossroads | 1792×1024 | **P2** |
| 012 | `14-best-worst-most-likely` | `#how-long-can-i-live` | Patients | Photorealistic editorial scene with one drawn overlay | 1792×1024 | **P2** |
| 013 | `05-when-to-get-help` | `#when-to-get-help` | Patients | Reference card — two panels | 1792×1024 | **P1** |
| 014 | `13-coverage-and-backup-plan` | `#philippines` | Patients | Reference card — two halves | 1792×1024 | **P2** |
| 015 | `17-preparation-strategies-trial` | `#md-older` | Clinicians | Clinician reference — trial-design schematic | 1792×1024 | **P2** |
| 016 | `06-what-dialysis-replaces` | `#md-overview` | Clinicians | Simple figure — single mechanism poster | 1792×1024 | **P2** |
| 017 | `18-indication-not-threshold` | `#md-timing` | Clinicians | Simple figure — contrast | 1792×1024 | **P2** |
| 018 | `07-symptom-trajectory-evidence` | `#md-trajectory` | Clinicians | Biomedical figure — journal two-panel chart | 1792×1024 | **P2** |
| 019 | `15-early-risk-window` | `#md-first90` | Clinicians | Simple figure — bar chart | 1792×1024 | **P2** |
| 020 | `16-transition-pathway-algorithm` | `#md-practice` | Clinicians | Clinical algorithm — vertical flowchart | 1024×1536 | **P2** |
| 021 | `calc-starting-dialysis-planner-og` (no prefix) | Calculator `<head>` | Mixed | OG / social share card (optional) | 1200×630 | **P3** |

### A.6 Consistency anchors (repeat in every relevant prompt)

- Backgrounds white `#ffffff` or off-white `#fafafa`; cards `#f3f4f6` or `#eef6f7`. Never dark.
- Navy `#0f1e2e` text · teal `#1a6b72` headings and “dialysis helps” · green `#1f7a4d` safe · amber `#b8860b` caution · clinical red `#b91c1c` emergency · orange `#c55a11` “before dialysis” · purple `#4b3280` “medicines cover this.”
- Font: **Inter** on every image with text.
- Attribution `© renalcarematters.com`, small, semi-transparent navy, bottom-right (bottom-center on the portrait algorithm). The hero vignette carries no text at all.
- **Recurring visual grammar:** extra water = small blue drops; waste = small tan specks; potassium = a small banana-yellow “K” token; acid = a small orange “acid” token; dialysis days = teal dots; a ride = a jeepney or tricycle; a ready meal = a covered plate.
- **Cast.** Filipino adults of varied age, build, and skin tone. No face repeats across images, and none resembles the cast of the incremental-dialysis guide (a woman in her late thirties at a wall calendar). No real, identifiable person.
- **Dialysis machine rule.** Where a machine appears it is a background object: a closed, generic cabinet with a blank screen. No blood lines, blood pump, dialyzer, or needle sites. If a generator adds a dialyzer anyway, reject the image; a true circuit figure comes only from the `dialysis-circuit-schematic` skill (two end ports for blood, two side ports for dialysate, countercurrent flow).
- No trial names, guideline acronyms, or drug brand names on patient images.

---

## Part B — Copy-ready prompts

### 001 — Hero vignette

IMAGE NUMBER: 001
SECTION PLACEMENT: Hero — `figure.hero-figure.mode-patient > .hero-vignette` (already wired)
FILE NAME: starting-dialysis-new-beginning-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 — Scaffold A clinical people scene · Composition J (Environmental Storytelling) · camera: side profile, wide · skill: williamriveromd-hero-vignette
AUDIENCE: Patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX: photorealistic models: grandmother and adult son · 3D: none · 2D: none · algorithm: none
PURPOSE: Say “there is still a life to plan for” before a word is read, and echo the Christmas in the story.
KEY CONCEPTS: Dawn; a parol being hung; family at her side; ordinary life going on.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER
around the full circle (the circle never touches the canvas edges). Composition archetype: J,
Environmental Storytelling — one cohesive scene, no floating panels. Camera: side profile,
wide environmental framing, from across a small front yard.
Subject: a Filipino grandmother in her late sixties, short and sturdy build, medium-brown skin,
round face, silver hair pinned in a low bun, wearing a loose floral duster in soft coral and
rubber slippers. She stands on the tiled front porch of a modest provincial bungalow at early
morning, both arms raised to hang a handmade star-shaped parol lantern (capiz shell and
bamboo, cream and soft gold) on a hook under the eaves. Her son, in his early forties, tall and
lean, darker skin, short cropped hair, wearing a faded green T-shirt and work shorts, crouches
beside her steadying a low wooden stool with one hand and holding a coil of string in the
other, looking up at the lantern. Her expression is absorbed and quietly content; his is
attentive. Potted santan and a clay water jar sit by the porch steps.
Visual hierarchy: the two figures and the parol occupy 60–70% of the circle, placed in the
right two-thirds; porch and plants are supporting context. Reserve the LEFT 20–25% of the
circle as a TITLE SAFE ZONE: open pale dawn sky and a softly blurred cream-colored wall, with
no faces, objects, plants, or details inside it.
Bright, airy first light with a gentle warm rim on the lantern; calm, reassuring,
documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a
light background; edge falloff toward a slightly deeper neutral at the rim.
Absolutely NO text of any kind: no title, caption, label, logo, or watermark.
NEGATIVE: no medical equipment, dialysis machine, hospital, bandage, visible fistula or
catheter; no kitchen or dining table, no wall calendar, no meal scene; no sad or frightened
faces; no busy layout, collage, floating icons, or more than two people; no cropped circle,
no objects touching the circular border, nothing in the title safe zone; no rectangular
frames or banners; no dark or moody lighting; no cartoon style, neon, HDR, or
over-saturation; no distorted hands or faces.
```

### 002 — Open Graph share card

IMAGE NUMBER: 002
SECTION PLACEMENT: `<head>` og:image and twitter:image
FILE NAME: starting-dialysis-new-beginning-og.png
ARCHETYPE: OG / social share card · skill: williamriveromd-infographic-skill
AUDIENCE: Mixed
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
VISUAL MIX: photorealistic models: same pair as 001 · 2D: title typography
PURPOSE: A link preview that a frightened patient or a relative will tap.
KEY CONCEPTS: Title; warmth; no clinical imagery.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Social share card, exactly 1200 × 630 px, off-white (#fafafa) background with a very light
teal tint (#eef6f7) panel on the left. RIGHT 45%: photorealistic editorial image, rounded
rectangle with a soft edge, of a Filipino grandmother in her late sixties in a coral floral
duster hanging a cream-and-gold star-shaped parol lantern on a porch at early morning while
her adult son steadies a stool beside her; bright, airy dawn light. LEFT 55%: title in bold
Inter, navy (#0f1e2e), three lines: "Why Starting Dialysis" / "Is Not a Death Sentence," /
"but a New Beginning" — the third line in amber (#b8860b). Beneath it, one line in teal
(#1a6b72), regular weight: "What to expect, the first 90 days, and when to get help". Bottom-
right: "© renalcarematters.com" in small semi-transparent navy text. All text inside a 60 px
safe margin.
NEGATIVE: no other words, no author name, no logos; no medical equipment, needles, or
hospital scene; no dark or navy background; no serif, decorative, or handwritten fonts; no
misspellings; no clutter; no HDR.
QUALITY CHECK: spell-check every word; title readable at 400 px wide; attribution reads
exactly "© renalcarematters.com".
```

### 003 — Three things to take with you (patient)

IMAGE NUMBER: 003
SECTION PLACEMENT: `#story`, after the “Three things to take with you today” callout (wired as figure 12)
FILE NAME: starting-dialysis-new-beginning-12-three-things-pocket-card.png
ARCHETYPE: Simple figure — single object · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: photorealistic: a hand · 3D: card · 2D: three icon rows
PURPOSE: Turn the guide's first ask into an object the reader can copy onto paper.
KEY CONCEPTS: Why dialysis; who to call; what to protect.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education illustration on a white (#ffffff) background, soft semi-3D rendering, Inter
font. A realistic adult Filipino hand, medium-brown skin, holds up a wallet-size card that
fills most of the frame, slightly tilted. The card is off-white with a teal (#1a6b72) top
band reading "My dialysis card". Three wide rows, each with a large round icon on the left, a
short bold navy (#0f1e2e) label, and an empty ruled line to write on: Row 1, teal question-
mark icon — "Why I need dialysis"; Row 2, green (#1f7a4d) telephone icon — "Number to call";
Row 3, orange (#c55a11) heart icon — "One thing I want to keep doing". A ballpoint pen rests
beside the card. Generous whitespace. Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.
NEGATIVE: no filled-in handwriting, no phone numbers, no names, no extra rows or icons; no
cartoon style, no flat clip-art, no dark background, no tiny labels, no gibberish text, no
serif fonts; never omit the attribution.
QUALITY CHECK: exactly three rows; three labels spelled exactly as given; lines left blank;
attribution visible.
```

### 004 — Four kidney jobs, three covered in part (patient)

IMAGE NUMBER: 004
SECTION PLACEMENT: `#what-dialysis-does` (wired as figure 01)
FILE NAME: starting-dialysis-new-beginning-01-kidney-jobs-and-dialysis.png
ARCHETYPE: Simple figure — side-by-side comparison · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 3D: kidneys, medicine tray · 2D: four cards · illustrated person: one man
PURPOSE: Show that dialysis takes over part of three jobs and medicines cover the fourth.
KEY CONCEPTS: Water; waste; potassium and acid; hormones.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic, soft semi-3D illustration on a white (#ffffff) background, Inter
font. Title at top in bold navy (#0f1e2e): "What dialysis does, and what it does not do".
LEFT third: a pair of healthy kidneys in correct anatomy (bean-shaped, the indented hilum
facing the midline, renal vein blue in front, artery red behind it, ureter pale yellow leaving
downward) with a small clock badge reading "All day, all night". CENTER: four stacked rounded
cards on soft gray (#f3f4f6), each with one icon and a short label: (1) blue water drops —
"Removes extra water"; (2) tan specks being swept — "Clears waste"; (3) a small balance scale
with a yellow K token and an orange acid token — "Balances potassium and acid"; (4) a red
blood cell beside a bone — "Makes hormones". RIGHT third: a heavyset Filipino man in his
fifties with a mustache, in a striped polo shirt, resting in a recliner; behind him a closed,
generic dialysis cabinet with a blank screen. Teal (#1a6b72) check-mark ribbons run from cards
1, 2, and 3 to the right side under the tag "Dialysis helps, in part". From card 4 a purple
(#4b3280) ribbon runs instead to a small tray holding an injection pen and a strip of tablets,
tagged "Medicines cover this". Bottom strip in soft gray, navy text: "Dialysis does part of
the work. Medicines, food, and fluid do the rest." Bottom-right: "© renalcarematters.com" in
small semi-transparent navy text.
NEGATIVE: no blood lines, blood pump, dialyzer, tubing, or needles; no kidneys drawn inside or
over the man's body; no mirrored kidney anatomy, no hilum on the outer border; no cartoon
style, no flat clip-art, no dark background, no tiny labels, no gibberish text, no serif
fonts; never omit the attribution.
QUALITY CHECK: four cards, exactly three teal ribbons and one purple; labels spelled exactly
as given; kidney anatomy plausible; man relaxed; attribution visible.
```

### 005 — 168 hours versus 12 (patient)

IMAGE NUMBER: 005
SECTION PLACEMENT: `#what-dialysis-does`, after the table (wired as figure 08)
FILE NAME: starting-dialysis-new-beginning-08-168-hours-versus-12.png
ARCHETYPE: Simple figure — two timelines · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 2D: two week strips · 3D: small kidney and machine icons, drops and tokens
PURPOSE: Make “why do I still limit salt and fluid?” obvious at a glance.
KEY CONCEPTS: Continuous versus intermittent; build-up in the gaps.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic on a white (#ffffff) background, soft semi-3D style, Inter font.
Title at top in bold navy (#0f1e2e): "Why food and fluid still matter". Two long horizontal
week strips, one above the other, each divided into seven equal day boxes labeled Mon, Tue,
Wed, Thu, Fri, Sat, Sun. UPPER strip: a small pair of kidneys at the left end; every day box
filled solid teal (#1a6b72); large label at the right end: "168 hours a week". LOWER strip: a
small closed dialysis cabinet icon at the left end; the boxes are pale gray, with one short
teal block in Mon, one in Wed, and one in Fri; large label at the right end: "About 12 hours a
week". In the gray gaps of the lower strip, small blue water drops, tan waste specks, a yellow
K token, and an orange acid token pile up gradually toward the next teal block, then clear
after it. A thin bracket over the longest gap, Fri to Mon, is tagged "Longest gap". Bottom
strip in soft gray, navy text: "Between treatments, water, potassium, and acid build up
again." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: use only the numbers 168 and 12; no other numbers, clocks, or percentages; no blood
lines, dialyzer, or needles; no cartoon style, no flat clip-art, no dark background, no tiny
labels, no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: seven boxes per strip in Mon-to-Sun order; exactly three teal blocks on the
lower strip; "168" and "12" correct; build-up visibly grows across each gap; attribution
visible.
```

### 006 — Why waiting becomes less safe (patient)

IMAGE NUMBER: 006
SECTION PLACEMENT: `#why-now` (wired as figure 09)
FILE NAME: starting-dialysis-new-beginning-09-why-waiting-becomes-less-safe.png
ARCHETYPE: Simple figure — one cause, three effects · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 3D: kidney, body details · 2D: three effect cards and a lower band
PURPOSE: Give the body's reason for “now,” so the recommendation is not just a lab number.
KEY CONCEPTS: Acid and muscle; waste and appetite and itch; fluid and heart and lungs.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic on a white (#ffffff) background, soft semi-3D illustration, Inter
font. Title at top in bold navy (#0f1e2e): "When waiting becomes less safe". LEFT: one kidney
drawn smaller and paler than normal, in correct anatomy with the hilum facing right toward the
midline, labeled "Kidneys can no longer keep up". Three thick arrows fan out to the RIGHT into
three rounded cards on soft gray (#f3f4f6). Card 1, orange (#c55a11) top band, "Acid builds
up": an upper arm shown twice, a fuller arm fading to a thinner one, with the note "The body
breaks down muscle". Card 2, amber (#b8860b) top band, "Waste builds up": a plate of rice and
fish pushed away by a hand, and a second small scene of a hand scratching a forearm, with the
note "Poor appetite, nausea, itching". Card 3, clinical red (#b91c1c) top band, "Fluid builds
up": swollen ankles in slippers and a simple chest outline with heart and lungs, with the note
"Strain on heart and lungs". LOWER band, left to right: a tablet strip and a bowl of
vegetables under "Medicines and diet hold this back, often for years", then an arrow to a
teal (#1a6b72) rounded box reading "When they no longer can: dialysis". Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: no numbers or lab values; no frightening, wasted, or distressed patient imagery; no
dialysis machine, blood, or needles; no mirrored kidney anatomy; no cartoon style, no flat
clip-art, no dark background, no tiny labels, no gibberish text, no serif fonts; never omit
the attribution.
QUALITY CHECK: exactly three effect cards in the order acid, waste, fluid; all labels spelled
as given; lower band reads left to right and ends in the teal box; attribution visible.
```

### 007 — Symptoms before and after the start (patient)

IMAGE NUMBER: 007
SECTION PLACEMENT: `#what-might-improve` (wired as figure 03)
FILE NAME: starting-dialysis-new-beginning-03-symptoms-before-after.png
ARCHETYPE: Patient infographic — one curve plus supports · skill: williamriveromd-infographic-skill
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 2D: one line chart without numbers, five cards · 3D: small icons
PURPOSE: Set an honest expectation: dialysis usually stops the slide; climbing back takes the rest of the care.
KEY CONCEPTS: Rising before; leveling after; five supports.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic on a white (#ffffff) background, soft semi-3D style, Inter font.
Title at top in bold navy (#0f1e2e): "Dialysis usually stops the slide". LEFT 60%: a simple
chart with no numbers. Horizontal timeline with three labels: "1 year before", "Dialysis
starts" (a vertical teal dashed line in the middle), "1 year after". One vertical label,
"Symptoms", with a small upward arrow. A thick orange (#c55a11) line climbs steadily from the
left up to the dashed line, then continues as a thick teal (#1a6b72) line that levels off and
dips slightly toward the right. A small callout at the turn reads "Levels off". RIGHT 40%:
heading "What helps you climb back" above five rounded cards in a column, each with one icon
and a short label: a bowl of fish and vegetables — "Good nutrition"; a red blood cell —
"Anemia care"; a walking figure — "Movement"; a crescent moon — "Sleep"; two speech bubbles —
"Mood and support". Bottom strip in soft gray (#f3f4f6), navy text: "From studies of older
adults in Europe. Your own course may differ." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.
NEGATIVE: no numbers, percentages, gridline values, or data points; do not draw the line
returning to its starting level; no second line; no cartoon style, no dark background, no
tiny labels, no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: one line only, orange before and teal after; it levels and dips slightly; five
cards; attribution visible.
```

### 008 — Your first hemodialysis day (patient)

IMAGE NUMBER: 008
SECTION PLACEMENT: `#first-treatment` (wired as figure 10)
FILE NAME: starting-dialysis-new-beginning-10-first-treatment-day.png
ARCHETYPE: Simple figure — three sequential steps · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: illustrated people: patient, nurse, family member · 2D: three step cards
PURPOSE: Replace the imagined first session with an ordinary, survivable one.
KEY CONCEPTS: Before: weigh and check; during: rest and speak up; after: weigh out and ride home.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic on a white (#ffffff) background, warm soft semi-3D illustration,
Inter font. Title at top in bold navy (#0f1e2e): "Your first hemodialysis day". Three large
rounded step cards in a row, left to right, each with a numbered circle and a colored top
band. Card 1, teal (#1a6b72) band, "Before": a young Filipino woman in her late twenties with
shoulder-length hair, wearing a yellow T-shirt and jeans, stands on a clinic scale while a
male nurse in light blue scrubs reads a blood-pressure cuff on her arm; two short bullets:
"Weight and blood pressure" and "Access check". Card 2, green (#1f7a4d) band, "During": the
same woman rests in a recliner under a light blanket reading a paperback, a closed generic
dialysis cabinet with a blank screen behind her, the nurse standing nearby; two bullets:
"Rest, read, or sleep" and "Tell the nurse if you feel unwell". Card 3, amber (#b8860b) band,
"After": she steps off the scale and walks toward the door with her father, a man in his
sixties in a checked shirt, a tricycle waiting outside; two bullets: "Weighed again" and
"Ride home, then rest". Thin arrows link the cards. Bottom strip in soft gray (#f3f4f6), navy
text: "First sessions are often shorter and gentler on purpose." Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: no needles, blood, blood lines, blood pump, dialyzer, or tubing attached to the
patient; no visible fistula, graft, or catheter; no frightened or pained faces; no numbers
other than the step numbers 1, 2, 3; no cartoon style, no flat clip-art, no dark background,
no tiny labels, no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: same woman recognizable in all three cards; six bullets spelled as given;
machine is a closed cabinet only; attribution visible.
```

### 009 — The first 90 days roadmap (patient)

IMAGE NUMBER: 009
SECTION PLACEMENT: `#your-first-90-days` (wired as figure 02)
FILE NAME: starting-dialysis-new-beginning-02-first-90-days-roadmap.png
ARCHETYPE: Patient infographic — four-stop pathway · skill: williamriveromd-infographic-skill
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: illustrated people: small scenes · 2D: path and four markers
PURPOSE: Make three months look like a path with four clear stops, not an open-ended ordeal.
KEY CONCEPTS: Know your plan; report and record; review what changed; check your goal.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education illustration on a white (#ffffff) background, soft semi-3D style, Inter
font. Title at top in bold navy (#0f1e2e): "Your first 90 days". A gently winding path runs
left to right across a soft green-and-cream provincial landscape with coconut palms far in
the background. Four round milestone markers sit on the path, each with a small scene above
and a short label below. Marker 1, teal (#1a6b72), label "Know your plan": a hand writing on a
small card beside a mobile phone. Marker 2, orange (#c55a11), label "First week: report and
record": an open notebook with a pencil and a small clock. Marker 3, purple (#4b3280), label
"Day 30: review what changed": a Filipino man in his forties and his wife seated across a
desk from a woman doctor, all three in side view, talking. Marker 4, navy (#0f1e2e), label
"Day 90: check your goal": an older Filipino man in a white sando and shorts walking to a
house gate holding a small grandchild's hand. Small footprints link the markers. Bottom strip
in soft gray (#f3f4f6), navy text: "Your team can move these dates. Hospital instructions
come first." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: no numbers other than 90 in the title and 30 and 90 in the labels; no calendar
dates; no medical equipment, needles, or hospital beds; no cartoon style, no flat clip-art,
no dark background, no tiny labels, no gibberish text, no serif fonts; never omit the
attribution.
QUALITY CHECK: exactly four markers in left-to-right order; "Day 30" and "Day 90" correct;
calm faces; attribution visible.
```

### 010 — A week with dialysis in it (patient)

IMAGE NUMBER: 010
SECTION PLACEMENT: `#daily-life` (wired as figure 11)
FILE NAME: starting-dialysis-new-beginning-11-a-week-with-dialysis.png
ARCHETYPE: Simple figure — week planner · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 3D: small scene icons · 2D: seven-column board
PURPOSE: Show that the week still holds work, movement, and family around three treatment days.
KEY CONCEPTS: Dialysis day = ride + ready meal + rest; other days = life.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education illustration on a white (#ffffff) background, soft semi-3D style, Inter
font. Title at top in bold navy (#0f1e2e): "A week with dialysis in it". A household
corkboard week planner fills the frame: seven equal columns headed Mon, Tue, Wed, Thu, Fri,
Sat, Sun. Mon, Wed, and Fri each carry a large teal (#1a6b72) dot labeled "Dialysis" and,
stacked beneath it, three small illustrated tiles: a jeepney labeled "Ride", a covered plate
labeled "Meal ready", and a pillow labeled "Rest". Tue shows a pair of walking shoes on a
path, labeled "Short walk". Thu shows a desk with a laptop and an ID lanyard, labeled "Work".
Sat shows a woven bayong bag of vegetables, labeled "Market". Sun shows a family table with
several plates, labeled "Family lunch". Pinned at the lower left corner, a small paper note
with a telephone icon: "Backup ride: ________". Bottom strip in soft gray (#f3f4f6), navy
text: "Start with one thing you want to protect." Bottom-right: "© renalcarematters.com" in
small semi-transparent navy text.
NEGATIVE: no clock times, dates, or numbers; no dialysis machine, needles, or hospital
imagery; no people's faces needed; no cartoon style, no flat clip-art, no dark background,
no tiny labels, no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: seven columns in Mon-to-Sun order; teal dots only on Mon, Wed, Fri; all labels
spelled as given; backup-ride line left blank; attribution visible.
```

### 011 — Your options remain open (patient)

IMAGE NUMBER: 011
SECTION PLACEMENT: `#options-remain-open` (wired as figure 04)
FILE NAME: starting-dialysis-new-beginning-04-options-remain-open.png
ARCHETYPE: Simple figure — crossroads · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: illustrated people: patient, spouse, doctor · 2D: five scene cards, two-way arrows
PURPOSE: Show five connected paths and that a first choice can be reviewed.
KEY CONCEPTS: In-center hemodialysis; home peritoneal dialysis; home hemodialysis; transplant; conservative kidney management.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education illustration on a white (#ffffff) background, soft semi-3D style, Inter
font. Title at top in bold navy (#0f1e2e): "Your options remain open". CENTER: a Filipino
woman in her forties with a short bob and eyeglasses, her husband in a blue barong-style
shirt, and a male nephrologist in a white coat stand beside a wooden signpost. Five paths fan
out from the signpost, each ending in a rounded scene card with a label below it: "In-center
hemodialysis" (a recliner beside a closed generic machine cabinet); "Peritoneal dialysis at
home" (a tidy bedroom corner with a fluid bag hanging on a stand and stacked supply boxes);
"Home hemodialysis" (a living-room armchair beside a small closed machine cabinet); "Kidney
transplant" (one healthy kidney cradled in two open hands); "Conservative kidney management"
(an older man in an armchair at home with a visiting nurse seated beside him holding a
notebook). Curved two-way teal (#1a6b72) arrows link neighboring paths. All five cards are the
same size and brightness. Bottom strip in soft gray (#f3f4f6), navy text: "A choice made in a
hurry can be reviewed once you are stable." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.
NEGATIVE: no blood lines, pumps, dialyzers, tubing connected to a person, needles, or surgery;
no ranking, stars, medals, or "best" badges; no path drawn larger or brighter than the
others; no numbers; no cartoon style, no flat clip-art, no dark background, no tiny labels,
no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: exactly five labeled paths spelled as given; two-way arrows present; no option
looks favored; attribution visible.
```

### 012 — Best case, worst case, most likely (patient)

IMAGE NUMBER: 012
SECTION PLACEMENT: `#how-long-can-i-live` (wired as figure 14)
FILE NAME: starting-dialysis-new-beginning-14-best-worst-most-likely.png
ARCHETYPE: Photorealistic editorial scene with one drawn overlay · skill: williamriveromd-infographic-skill
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: photorealistic models: patient, daughter, doctor · 2D: three hand-drawn paths
PURPOSE: Replace “how many years?” with a question the team can actually answer.
KEY CONCEPTS: Three scenarios; everyday endpoints, not numbers.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Photorealistic medical editorial image, bright and airy clinic consultation room with white
walls and soft daylight, Inter font for overlay text. A Filipino man in his early seventies,
thin, bald, wearing a short-sleeved checked polo, sits beside his adult daughter in her
thirties, who has long hair tied back and holds a small notebook. Across a light wooden desk,
a woman nephrologist in her fifties with gray-streaked hair and a white coat leans forward,
drawing on a sheet of paper with a marker. All three are seen in a wide side view; expressions
are serious but calm and engaged. A clean illustrated overlay enlarges the paper in the upper
right of the frame: three simple paths starting from one point — an upper green (#1f7a4d)
path labeled "Best case" ending at a small icon of a man walking with a child; a wide middle
teal (#1a6b72) path labeled "Most likely" ending at an icon of a family meal; a lower amber
(#b8860b) path labeled "Worst case" ending at an icon of a man resting in a chair with a
caregiver beside him. Title at top left in bold navy (#0f1e2e): "Ask for three scenarios".
Bottom strip in soft gray (#f3f4f6), navy text: "What will my days look like in each?"
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: no numbers, percentages, years, charts, or survival curves; no grim or tearful
faces; no medical equipment; no dark or moody lighting; no cartoon people; no tiny labels,
no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: three paths only, labeled exactly "Best case", "Most likely", "Worst case";
the middle path widest; no digits anywhere; attribution visible.
```

### 013 — When to get help (patient)

IMAGE NUMBER: 013
SECTION PLACEMENT: `#when-to-get-help` (wired as figure 05)
FILE NAME: starting-dialysis-new-beginning-05-when-to-get-help.png
ARCHETYPE: Reference card — two panels · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 3D: eight icon tiles · 2D: two-panel card
PURPOSE: Separate “emergency now” from “call the unit today” for a reader who cannot read the labels.
KEY CONCEPTS: Four emergency signs; four same-day signs; press on access bleeding.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clinical safety reference card on a white (#ffffff) background, clean soft semi-3D icons,
Inter font. Title at top in bold navy (#0f1e2e): "When to get help". Two equal panels side by
side. LEFT panel: clinical red (#b91c1c) header bar with an ambulance icon and the words
"Emergency room now"; four large icon tiles with labels beneath — a person leaning forward
struggling to breathe: "Severe trouble breathing"; a hand pressed to the chest: "Chest
pain"; a person slumped in a chair: "Fainting or new confusion"; a forearm with a second hand
pressing a folded white gauze pad firmly on it: "Bleeding that will not stop — press
firmly". RIGHT panel: amber (#b8860b) header bar with a telephone icon and the words "Call
your dialysis team today"; four large icon tiles with labels — a thermometer: "Fever or
chills"; a simple chest-wall catheter exit site with a reddened ring around it: "Redness or
drainage at the access"; two fingertips resting on a forearm with small vibration lines
crossed out: "Fistula or graft buzz is missing"; a clear drain bag holding cloudy fluid:
"Cloudy PD fluid or new belly pain". Bottom strip in soft gray (#f3f4f6), navy text: "Cannot
come to a session? Call your unit early." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.
NEGATIVE: no visible blood, wounds, or needles; no graphic or frightening imagery; no numbers;
no cartoon style, no dark background, no tiny labels, no gibberish text, no serif fonts;
never omit the attribution.
QUALITY CHECK: four tiles per panel; red with ambulance on the left, amber with telephone on
the right; every label spelled as given; gauze pressure shown without blood; attribution
visible.
```

### 014 — Coverage and a backup plan (patient)

IMAGE NUMBER: 014
SECTION PLACEMENT: `#philippines` (wired as figure 13)
FILE NAME: starting-dialysis-new-beginning-13-coverage-and-backup-plan.png
ARCHETYPE: Reference card — two halves · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 3D: card, calendar, checklist icons · 2D: two-half layout
PURPOSE: Answer the family's memory of rationed dialysis with what is covered now, and name what they must still arrange.
KEY CONCEPTS: 156 sessions; ₱6,350 per session; four things to arrange.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient reference card on a white (#ffffff) background, soft semi-3D style, Inter font. Title
at top in bold navy (#0f1e2e): "What is covered, and what to arrange". LEFT half, teal
(#1a6b72) header "PhilHealth hemodialysis benefit": a generic green-and-white health
insurance membership card with no real logo, beside a wall calendar page showing one week
with three teal dots. Two large stat tiles beneath: "156" with the caption "sessions a
year" and "₱6,350" with the caption "per session". Small note: "For registered members with
stage 5 kidney disease". RIGHT half, amber (#b8860b) header "Arrange these yourself": a
checklist of four rows, each with an empty checkbox, an icon, and a short label — an ID card:
"Check your registration"; a sheet of paper with a peso sign: "Ask for a written quote"; a
jeepney and coins: "Count fares and food"; a second jeepney and a storm cloud: "Backup ride
and backup unit". Bottom strip in soft gray (#f3f4f6), navy text: "Rules change. Confirm with
your unit." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: use only the numbers 156, 6,350, and 5; no other amounts, totals, dates, or
percentages; no real PhilHealth logo or seal, no real card numbers or names; no cartoon
style, no flat clip-art, no dark background, no tiny labels, no gibberish text, no serif
fonts; never omit the attribution.
QUALITY CHECK: proofread "156" and "₱6,350" with the peso sign and comma; four checklist rows
spelled as given; no official logo; attribution visible.
```

### 015 — Prepare for Kidney Care: what was compared (clinician)

IMAGE NUMBER: 015
SECTION PLACEMENT: `#md-older` (wired as figure 17)
FILE NAME: starting-dialysis-new-beginning-17-preparation-strategies-trial.png
ARCHETYPE: Clinician reference card — trial-design schematic · skill: williamriveromd-infographic-skill
AUDIENCE: Clinicians
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 2D: flow schematic, icon arrays · 3D: none
PURPOSE: Prevent the commonest misreading: this trial compared preparation strategies, not dialysis versus no dialysis.
KEY CONCEPTS: 445 randomized; two pathways; 18% and 28% started dialysis; no clear difference in quality-adjusted life-years.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clinical reference infographic, publication-grade nephrology design on a white (#ffffff)
background, clean schematic with soft shading, Inter font. Title at top in bold navy
(#0f1e2e): "Prepare for Kidney Care: what was compared". TOP center: a rounded box, "445
older adults with frailty or multimorbidity, eGFR below 15", with a small "Randomized" tag
and two arrows splitting downward. LEFT arm, teal (#1a6b72) box: "Prepare for responsive
management (conservative care)". RIGHT arm, navy box outline on white: "Prepare for
dialysis". Under each arm, a row of ten small person icons: on the left, about two of ten
filled teal with the caption "18% started dialysis"; on the right, about three of ten filled
navy with the caption "28% started dialysis". Both arms then converge on one wide outcome box
at the bottom containing a level balance scale and the words "No clear difference in
quality-adjusted life-years". Two small side notes in soft gray (#f3f4f6) cards: "Compares
preparation strategies, not dialysis versus no dialysis" and "Not equivalence; does not cover
emergency starts". Bottom-right: "© renalcarematters.com" in small semi-transparent navy
text.
NEGATIVE: use only the numbers 445, 15, 18%, and 28%; no confidence intervals, hazard ratios,
p-values, or other figures; no photographs of people; no dark background, no tiny labels, no
gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: proofread "445", "18%", "28%"; balance scale level; both side notes present and
spelled as given; attribution visible.
```

### 016 — What hemodialysis replaces (clinician)

IMAGE NUMBER: 016
SECTION PLACEMENT: `#md-overview` (wired as figure 06)
FILE NAME: starting-dialysis-new-beginning-06-what-dialysis-replaces.png
ARCHETYPE: Simple figure — single mechanism poster (Scaffold D) · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 3D: one kidney in coronal section · 2D: two week bars, seven cards
PURPOSE: Tie which symptoms respond early to which functions are replaced.
KEY CONCEPTS: Continuous versus intermittent; replaced in part versus not replaced.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Medical pathophysiology infographic, AJKD/NEJM graphical-abstract style, white (#ffffff)
background, Inter font. Title at top in bold navy (#0f1e2e): "What hemodialysis replaces, and
what it does not". FAR LEFT: one semi-photorealistic 3D kidney in coronal section — cortex on
the outside, medullary pyramids with apices pointing inward to the calyces, renal pelvis at
the medial hilum, hilum facing right. TOP band: two week-long horizontal bars, Mon to Sun.
Upper bar, labeled "Native kidneys", solid teal (#1a6b72) end to end, tag "continuous". Lower
bar, labeled "Hemodialysis, three sessions", pale gray with three short navy blocks spaced
across the week, tag "intermittent". BOTTOM band: two columns of rounded cards. Left column,
teal header "Replaced in part": "Volume", "Potassium", "Acid", "Small solutes (urea)"; a
bracket beneath leads to the phrase "Respond early: congestion, nausea, poor appetite". Right
column, orange (#c55a11) header "Not replaced": "Erythropoietin", "Vitamin D activation",
"Tubular secretion of protein-bound solutes"; a bracket beneath leads to the phrase "Need
separate treatment: fatigue, itch, poor sleep". Bottom-right: "© renalcarematters.com" in
small semi-transparent navy text.
NEGATIVE: no numbers anywhere; no dialysis circuit, pump, dialyzer, or tubing; no mirrored or
cartoon kidney, no calyces pointing outward, no pelvis floating in the center; no dark
background, no tiny labels, no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: upper bar solid, lower bar exactly three blocks; four cards left, three right;
every term spelled as given; kidney anatomy correct; attribution visible.
```

### 017 — Indication, not threshold (clinician)

IMAGE NUMBER: 017
SECTION PLACEMENT: `#md-timing` (wired as figure 18)
FILE NAME: starting-dialysis-new-beginning-18-indication-not-threshold.png
ARCHETYPE: Simple figure — side-by-side contrast (Scaffold B) · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 3D: one gauge, five input icons · 2D: two panels
PURPOSE: Fix the guideline position in one glance: a composite judgment, with kidney function as one input.
KEY CONCEPTS: Symptoms and signs; volume and blood pressure; acid–base and potassium; nutrition; preference.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clinical comparison infographic on a white (#ffffff) background, soft semi-3D style, Inter
font. Title at top in bold navy (#0f1e2e): "Timing dialysis: indication, not threshold". Two
panels side by side. LEFT panel, pale gray (#f3f4f6), header "A single number": one large
round gauge labeled "eGFR" with its needle near the low end and a thin amber (#b8860b)
diagonal line across the panel; caption beneath: "Not a trigger by itself". RIGHT panel, very
light teal (#eef6f7), header in teal (#1a6b72) "A composite judgment": six rounded input cards
arranged around a central circle labeled "Start when the balance tips" — a person holding the
stomach: "Symptoms and signs"; water drops and a cuff: "Volume and blood pressure"; a small
scale with K and acid tokens: "Acid–base and potassium"; a plate and a downward weight arrow:
"Nutritional trajectory"; a small gauge: "eGFR and labs"; two speech bubbles: "Patient
preference and quality of life". Thin arrows run from each card to the center. Bottom strip
in soft gray, navy text: "Kidney function is one input among six." Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: no numeric values, units, or thresholds on the gauges; no trial or guideline names;
no photographs; no dark background, no tiny labels, no gibberish text, no serif fonts; never
omit the attribution.
QUALITY CHECK: exactly six input cards on the right, spelled as given; no digits anywhere;
left panel visibly de-emphasized, not alarming; attribution visible.
```

### 018 — Symptoms and quality of life around the start (clinician)

IMAGE NUMBER: 018
SECTION PLACEMENT: `#md-trajectory` (wired as figure 07)
FILE NAME: starting-dialysis-new-beginning-07-symptom-trajectory-evidence.png
ARCHETYPE: Biomedical figure — journal two-panel chart · skill: williamriveromd-biomedical-mechanism-figure (text and palette rules)
AUDIENCE: Clinicians
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 2D: two aligned line panels with uncertainty bands
PURPOSE: Show decline before the start and stabilization after, with honest uncertainty.
KEY CONCEPTS: +13.3 then −5.9 on the symptom index; −13 and −11 then flat on quality of life; no untreated comparator.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Publication-grade scientific review-article figure on a white (#ffffff) background, precise
chart elements with soft shading, Inter font. Title at top in bold navy (#0f1e2e): "Before
and after starting dialysis: adults aged 65 or older". Two stacked panels sharing one
horizontal axis with three ticks: "−12 months", "Dialysis start" (a vertical teal dashed line
through both panels), "+12 months". UPPER panel, y-axis label "Symptom burden (DSI, 0–150)":
one orange (#c55a11) line rising from the left to the dashed line, annotated "+13.3 points";
then one teal (#1a6b72) line sloping slightly downward to the right, annotated "−5.9 points";
a light shaded band around each segment, clearly wider on the right. LOWER panel, y-axis
label "Quality of life (SF-36 summary scores)": two lines, navy labeled "Mental" and purple
(#4b3280) labeled "Physical", both falling from the left to the dashed line, annotated "−13"
and "−11", then running roughly flat to the right inside wide shaded bands. A pale blue
footnote box at the bottom: "Observational cohort (EQUAL). No untreated comparator. Change
after the start is consistent with stabilization." Bottom-right: "© renalcarematters.com" in
small semi-transparent navy text.
NEGATIVE: use only these numbers: 13.3, 5.9, 13, 11, 12, 65, 0, 150, 36; no gridline values,
p-values, or sample sizes; do not draw any line returning to its starting level; no 3D chart
effects, no dark background, no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: proofread "+13.3", "−5.9", "−13", "−11"; upper line orange then teal; lower
panel two lines; bands wider after the start; footnote present; attribution visible.
```

### 019 — The early-risk window (clinician)

IMAGE NUMBER: 019
SECTION PLACEMENT: `#md-first90` (wired as figure 15)
FILE NAME: starting-dialysis-new-beginning-15-early-risk-window.png
ARCHETYPE: Simple figure — reference chart (Scaffold E) · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians
ASPECT RATIO: 7:4
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX: 2D: three-bar chart with one callout
PURPOSE: Justify concentrating follow-up in the first months.
KEY CONCEPTS: 26.7, 16.9, 13.7 deaths per 100 patient-years; observational.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clinical reference chart, publication-grade nephrology design on a white (#ffffff)
background, Inter font. Title at top in bold navy (#0f1e2e): "Mortality by time since
starting hemodialysis". Subtitle in teal (#1a6b72): "Deaths per 100 patient-years, DOPPS,
11 countries". A clean vertical bar chart with three wide bars, left to right, each with its
value printed above it in large navy digits and its period printed below: first bar, tallest,
clinical red (#b91c1c), value "26.7", period "First 120 days"; second bar, amber (#b8860b),
value "16.9", period "Days 121–365"; third bar, shortest, teal, value "13.7", period "After
1 year". Bar heights are in true proportion to the values. A rounded callout pointing to the
first bar: "The window for closer follow-up". A pale gray (#f3f4f6) footnote box: "Observational.
Early excess reflects unplanned starts, catheters, and acute illness as well as time on
dialysis." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.
NEGATIVE: use only the numbers 26.7, 16.9, 13.7, 120, 121, 365, 1, 100, 11; no gridline
values, confidence intervals, or extra bars; no 3D bar effects; no dark background, no tiny
labels, no gibberish text, no serif fonts; never omit the attribution.
QUALITY CHECK: proofread "26.7", "16.9", "13.7", "120", "121–365"; first bar roughly twice the
height of the third; footnote spelled as given; attribution visible.
```

### 020 — From recommendation to day 90 (clinician algorithm)

IMAGE NUMBER: 020
SECTION PLACEMENT: `#md-practice` (wired as figure 16)
FILE NAME: starting-dialysis-new-beginning-16-transition-pathway-algorithm.png
ARCHETYPE: Clinical algorithm — vertical flowchart · skill: williamriveromd-algorithm-generator-skill
AUDIENCE: Clinicians
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX: algorithm/flowchart only
PURPOSE: One page a unit can post: the transition as a pathway with owners and review points.
KEY CONCEPTS: Indication; diagnosis; safety net; goal; reviews at week 1, day 30, day 90; recovery branch.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a polished medical guideline algorithm flowchart, portrait 1024 × 1536, white
background, clean sans-serif typography set in Inter, thin dark-gray arrows, generous
margins, strict alignment and consistent node spacing. Title at top center in bold navy:
"Starting dialysis: from recommendation to day 90".
Use these visual conventions: peach rounded boxes for initial assessment steps; a pink
diamond for the one decision question; green rounded boxes for safety and supportive steps;
blue rounded boxes for scheduled review steps; a gray capsule for the side pathway.
Content to render, top to bottom down the center:
1. Peach box: "Name the indication in one plain sentence"
2. Pink diamond: "Which diagnosis?" with three short exits labeled "Chronic kidney failure",
   "Acute kidney injury", "Uncertain"
3. Right-hand side branch from "Acute kidney injury" and "Uncertain" to a gray capsule:
   "Recovery pathway: named clinician, review date, urine output and pre-dialysis labs",
   with a return arrow rejoining the main line
4. Green box: "Give the after-hours number and the red flags"
5. Green box: "Ask for one patient goal"
6. Blue box: "First week: symptoms, access, recovery time"
7. Blue box: "Day 30: access plan, modality, transplant referral, caregiver"
8. Blue box: "Day 90: goal, function, admissions, missed sessions"
9. Final peach box: "Record one change, its owner, and the next review date"
Design requirements: no decorative icons, no photos, no 3D elements, no dark background, no
heavy shadows; short readable text inside boxes only. Include a small professional footer
reading "© renalcarematters.com" at the bottom-right corner in subtle gray
medical-publication styling.
NEGATIVE: no extra nodes, no numbers other than 30 and 90 and the word "week"; no drug names,
doses, or thresholds; no crossing arrows; no gibberish text; no serif fonts.
QUALITY CHECK: nine nodes in the stated order; one diamond with three exits; side branch
returns to the main line; "Day 30" and "Day 90" correct; footer present.
```

### 021 — Planner share card (calculator, optional)

IMAGE NUMBER: 021
SECTION PLACEMENT: Calculator `<head>` og:image (not yet wired; the page uses the dialysis category image)
FILE NAME: calc-starting-dialysis-planner-og.png
ARCHETYPE: OG / social share card · skill: williamriveromd-infographic-skill
AUDIENCE: Mixed
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
VISUAL MIX: 2D: title · 3D: three tool icons
PURPOSE: A recognizable preview when the planner link is shared in a patient group chat.
KEY CONCEPTS: Time and transport; recovery log; goal dates.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Social share card, exactly 1200 × 630 px, off-white (#fafafa) background, Inter font. LEFT
55%: title in bold navy (#0f1e2e), two lines: "Starting Dialysis" / "Planner"; beneath it,
one line in teal (#1a6b72): "Time and rides · Recovery log · Goal dates". RIGHT 45%: three
soft semi-3D icons in a row on rounded light-teal (#eef6f7) tiles — a jeepney beside a small
clock; an open notebook with a pencil; a calendar page with a small flag. Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text. All text inside a 60 px safe
margin.
NEGATIVE: no other words or numbers, no people, no medical equipment; no dark background, no
serif or decorative fonts, no misspellings, no clutter.
QUALITY CHECK: title and subtitle spelled exactly; three icons only; attribution reads
"© renalcarematters.com".
```

---

## Part C — Production and wiring checklist

1. **Generate** in priority order: all P1 first (001, 002, 004, 005, 006, 007, 008, 009, 010, 013), then P2, then 021. Save each output as PNG at the stated size into the local folder.
2. **Run the cover-the-words test** on every patient image (A.2). If the meaning is lost with the labels hidden, regenerate.
3. **Proofread** every text-bearing image. Reject any image with a misspelled word, an extra word, a real logo, or a wrong number. Check 005, 014, 015, 018, 019, and 020 digit by digit against A.4.
4. **Check the machine rule** on 004, 008, and 011: a closed cabinet only. Reject any image that shows blood lines, a dialyzer, or needles.
5. **Check the cast:** no face repeats across the set, and the hero pair does not resemble the incremental-dialysis hero.
6. **Convert** each PNG to a WebP twin (quality about 82) and place both in `images/` with the exact file names in A.5.
7. **Already wired:** the hero, the OG image, and figures 01 to 18 are referenced in the guide with alt text, a `fig-desc` (four languages on patient figures), and `fig-abbrevs` where needed. Once the files exist, the alt-text placeholders clear. If a generated image adds an acronym that is not in its `fig-abbrevs`, add it there and to the glossary, then rerun `audit_acronym_expansion.py --guide starting-dialysis-new-beginning.html`.
8. **After upload,** from the repo root: `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, `patch_image_lightbox.py`, `patch_og_images.py`, and `patch_responsive_images.py`, each with `--guide starting-dialysis-new-beginning.html`; then `generate_rg_thumbs.py` and `generate_latest_guides.py`. For 021, point the calculator's `og:image` and `twitter:image` at the new file, then run `generate_latest_calculators.py`.

## Part D — Stage 2 manifest rows (`image-manifest.csv`)

```
image_number,section_placement,file_name,archetype,audience,aspect_ratio,width,height,status,alt_text
001,"Hero",starting-dialysis-new-beginning-vignette-hero.png,"Circular vignette hero v3 — Scaffold A people · Composition J · camera: side profile, wide","Patients and families",1:1,2048,2048,prompted,"A Filipino grandmother on her front porch at early morning hanging a star-shaped parol lantern while her grown son steadies the stool beside her."
002,"<head>",starting-dialysis-new-beginning-og.png,"OG / social share card","Mixed",1.91:1,1200,630,prompted,"Share card titled 'Why Starting Dialysis Is Not a Death Sentence, but a New Beginning' with a grandmother hanging a parol at dawn."
003,"#story",starting-dialysis-new-beginning-12-three-things-pocket-card.png,"Simple figure — single object","Patients and families",7:4,1792,1024,prompted,"A hand holding a pocket card with three rows to fill in: why I need dialysis, number to call, one thing I want to keep doing."
004,"#what-dialysis-does",starting-dialysis-new-beginning-01-kidney-jobs-and-dialysis.png,"Simple figure — comparison","Patients and families",7:4,1792,1024,prompted,"Four kidney jobs as cards; dialysis helps with three in part and medicines cover the hormone job."
005,"#what-dialysis-does",starting-dialysis-new-beginning-08-168-hours-versus-12.png,"Simple figure — two timelines","Patients and families",7:4,1792,1024,prompted,"Two week strips: healthy kidneys working 168 hours and three hemodialysis sessions totaling about 12 hours, with build-up in the gaps."
006,"#why-now",starting-dialysis-new-beginning-09-why-waiting-becomes-less-safe.png,"Simple figure — cause and three effects","Patients and families",7:4,1792,1024,prompted,"A failing kidney leading to acid, waste, and fluid build-up, with their effects on muscle, appetite, and the heart and lungs."
007,"#what-might-improve",starting-dialysis-new-beginning-03-symptoms-before-after.png,"Patient infographic — one curve plus supports","Patients and families",7:4,1792,1024,prompted,"A symptom line rising before dialysis and leveling after, beside five supports for recovery."
008,"#first-treatment",starting-dialysis-new-beginning-10-first-treatment-day.png,"Simple figure — three steps","Patients and families",7:4,1792,1024,prompted,"Three panels of a first hemodialysis day: checks before, rest during, weigh-out and ride home after."
009,"#your-first-90-days",starting-dialysis-new-beginning-02-first-90-days-roadmap.png,"Patient infographic — four-stop path","Patients and families",7:4,1792,1024,prompted,"A winding path with four milestones across the first 90 days on dialysis."
010,"#daily-life",starting-dialysis-new-beginning-11-a-week-with-dialysis.png,"Simple figure — week planner","Patients and families",7:4,1792,1024,prompted,"A household week planner with three dialysis days and the rest of the week kept for walks, work, market, and family lunch."
011,"#options-remain-open",starting-dialysis-new-beginning-04-options-remain-open.png,"Simple figure — crossroads","Patients and families",7:4,1792,1024,prompted,"A crossroads signpost with five connected kidney failure care paths."
012,"#how-long-can-i-live",starting-dialysis-new-beginning-14-best-worst-most-likely.png,"Photorealistic editorial scene with drawn overlay","Patients and families",7:4,1792,1024,prompted,"A nephrologist sketching best case, worst case, and most likely paths for a patient and his daughter."
013,"#when-to-get-help",starting-dialysis-new-beginning-05-when-to-get-help.png,"Reference card — two panels","Patients and families",7:4,1792,1024,prompted,"Red panel of emergency signs and amber panel of same-day call signs for people on dialysis."
014,"#philippines",starting-dialysis-new-beginning-13-coverage-and-backup-plan.png,"Reference card — two halves","Patients and families",7:4,1792,1024,prompted,"PhilHealth hemodialysis coverage of 156 sessions a year at 6,350 pesos per session beside a four-item checklist of things to arrange."
015,"#md-older",starting-dialysis-new-beginning-17-preparation-strategies-trial.png,"Clinician reference — trial-design schematic","Clinicians",7:4,1792,1024,prompted,"Trial-design schematic of Prepare for Kidney Care showing two preparation pathways and the share who started dialysis in each."
016,"#md-overview",starting-dialysis-new-beginning-06-what-dialysis-replaces.png,"Simple figure — single mechanism poster","Clinicians",7:4,1792,1024,prompted,"Continuous native kidney clearance versus intermittent hemodialysis, with functions replaced in part and not replaced."
017,"#md-timing",starting-dialysis-new-beginning-18-indication-not-threshold.png,"Simple figure — contrast","Clinicians",7:4,1792,1024,prompted,"A single eGFR gauge contrasted with a six-input composite judgment for timing dialysis."
018,"#md-trajectory",starting-dialysis-new-beginning-07-symptom-trajectory-evidence.png,"Biomedical figure — two-panel chart","Clinicians",7:4,1792,1024,prompted,"Two aligned panels of symptom burden and quality of life before and after dialysis initiation in older adults."
019,"#md-first90",starting-dialysis-new-beginning-15-early-risk-window.png,"Simple figure — bar chart","Clinicians",7:4,1792,1024,prompted,"Bar chart of mortality per 100 patient-years by time since starting hemodialysis: 26.7, 16.9, and 13.7."
020,"#md-practice",starting-dialysis-new-beginning-16-transition-pathway-algorithm.png,"Clinical algorithm — vertical flowchart","Clinicians",2:3,1024,1536,prompted,"Vertical flowchart from the dialysis recommendation through reviews at the first week, day 30, and day 90."
021,"Calculator <head>",calc-starting-dialysis-planner-og.png,"OG / social share card","Mixed",1.91:1,1200,630,prompted,"Share card for the Starting Dialysis Planner with icons for rides, a recovery log, and goal dates."
```
