# Image plan — `guides/personal-medical-journal-health-history.html`

**Guide:** How to Build Your Personal Medical Journal and Health History
**Mode:** dual (patient EN/TL/CEB/KAP · clinician EN)
**Skills used:** `williamriveromd-hero-vignette` (01) · `williamriveromd-infographic-skill` (02) ·
`williamriveromd-simple-figure` (03–09) · `williamriveromd-algorithm-generator-skill` (10)
**Target generator:** ChatGPT Image Generator (GPT-image)

---

## Why these ten, and not more

The guide already renders six explanatory visuals as HTML/CSS components — the four-record
cards, the weak-versus-useful comparison cards, the source-certainty badges, the folder map,
the algorithm cards, and the glossary. Those stay as markup, because the blueprint's own
asset plan calls for "HTML badges, not image text" and because text baked into a raster is
untranslatable, unsearchable, and unreadable to a screen reader.

The ten assets below are the ones that genuinely need pixels: a hero, a share card, and eight
figures that teach something the prose cannot show — a spatial relationship, a physical
technique, a sequence, or a comparison the reader must *see* to believe.

Every figure's teaching also exists in the running prose, so nothing is lost if an image
fails to load. That is a hard rule from the blueprint (§12): **do not embed key instructional
text only inside images.**

| # | File (`images/…`) | Placement | Skill | Size |
|---|---|---|---|---|
| 01 | `…-vignette-hero.png` / `.webp` | hero disc | hero-vignette | 2048×2048 |
| 02 | `…-og.png` | `og:image` | infographic | 1200×630 |
| 03 | `…-01-four-record-system.png` | `#four` | simple-figure | 1792×1024 |
| 04 | `…-02-three-medication-lists.png` | `#why` | simple-figure | 1792×1024 |
| 05 | `…-03-anatomy-of-a-summary.png` | `#summary` | simple-figure | 1536×1152 |
| 06 | `…-04-photograph-the-whole-page.png` | `#meds` | simple-figure | 1792×1024 |
| 07 | `…-05-symptom-entry-sequence.png` | `#symptoms` | simple-figure | 1792×1024 |
| 08 | `…-06-home-bp-technique.png` | `#measurements` | simple-figure | 1792×1024 |
| 09 | `…-07-md-transitions-information-loss.png` | `#md-evidence` | simple-figure | 1792×1024 |
| 10 | `…-08-md-bpmh-algorithm.png` | `#md-recon` | algorithm-generator (Mode C) | 1024×1536 |

**Fictional data rule.** Figures 05, 06, and 07 show mock records. Every name, date, value,
and medicine in them must be fictional and non-identifiable, and the figure must say so.
Use `Dela Cruz, Maria` / `1962` / generic drug names only.

---

## 01 — Circular vignette hero

```
FILE NAME: personal-medical-journal-health-history-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: overhead top-down, slight tilt
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: patients and caregivers
VISUAL GOAL: scattered medical paperwork resolving into one calm, ordered set of records.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE
BORDER around the full circle (the circle must never touch the canvas edges).
Composition archetype: I Object Hero. Camera: overhead top-down with a slight tilt.

Subject: a single clean arrangement on a soft, uncluttered light warm-neutral wooden
table — a slim kraft document folder lying open with a neat stack of crisp white pages
squared inside it, a simple spiral notebook opened to a blank ruled page with a plain
ballpoint pen resting in the gutter, one blister strip of unbranded white tablets and a
small amber pill bottle with a blank label, and a home blood-pressure cuff coiled tidily
at the lower edge. Around the upper-left of the arrangement, three or four loose sheets
lie slightly askew and overlapping, as if just gathered — the visual contrast between
scattered paper and the squared stack is the whole idea. Soft natural daylight from the
upper left, gentle shallow depth of field, a soft shadow under the folder.

Visual hierarchy: the open folder with its squared stack is the hero object at 60–70% of
the circle; the notebook, medicines, cuff, and loose sheets together occupy 20–30%;
reserve a 20–25% TITLE SAFE ZONE of empty table surface in the upper-right quadrant
(no objects, papers, labels, or icons inside that zone). Soft edge falloff toward a
slightly deeper neutral at the rim. Light, calm, orderly, reassuring colour grade
harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background.

Absolutely NO readable text or labels on any paper, packaging, or pill bottle — the
sheets must read as blank or as illegible grey line-texture. No titles, no logos, no
watermark. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid: busy layouts; collage overload; more than four supporting scenes; dozens of icons;
tiny unreadable labels; infographic clutter; duplicated people; repeated compositions;
cropped circle; cropped objects; edge clipping; objects touching the circular border;
important content inside the title safe zone; baked-in text, titles, captions, logos,
watermarks; rectangular borders, frames, banners; dark / charcoal / black backgrounds;
cartoon style, neon, HDR, over-saturation.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never
cropped. ONE dominant hero object at 60–70% of the circle, 2–4 supporting elements,
20–25% empty title-safe zone in the upper-right. No legible text anywhere.
```

> **Note on attribution:** the vignette hero is the *one* asset in this plan that carries
> **no** `renalcarematters.com` mark — the disc is a wordless picture by design and any text
> is clipped by the circle. Every other figure below must carry the attribution.

---

## 02 — Open Graph share card

```
FILE NAME: personal-medical-journal-health-history-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed
VISUAL GOAL: the fragmentation problem and its resolution, readable at thumbnail size.

PROMPT:
Landscape 1200×630 editorial share card, clean clinical publication aesthetic, on an
off-white (#fafafa) background. Left two-thirds: an overhead photorealistic still-life on
a light warm-neutral surface — a loose fan of medical papers, laboratory slips and a
blister strip scattered at the far left, progressively straightening across the frame into
one squared, ordered stack seated in an open kraft folder at centre-right. Soft natural
daylight from the upper left, gentle shallow depth of field. Right third: clean negative
space over a soft teal-to-white vertical gradient, reserved for a title lockup added later
in the card template — leave it empty. A thin clinical teal (#1a6b72) rule separates the
two zones. Palette restricted to clinical teal #1a6b72, navy #0f1e2e, and warm neutrals.
Small semi-transparent navy "renalcarematters.com" in the bottom-right corner.

Absolutely NO body copy, NO headline text, and NO readable text on any paper or packaging —
the sheets must read as blank or as illegible grey line-texture. No logos beyond the
attribution line. No people.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR,
excessive saturation, dark or navy backgrounds. Use ONLY the sans-serif fonts Inter, Nunito
Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Legible and recognisable at 300px wide. Right third genuinely empty for the title. Light
background. Attribution visible bottom-right.
```

Alt text already declared in the guide head:
*"Scattered laboratory slips, prescriptions and hospital papers resolving into one clear
medical summary, timeline and folder."*

---

## 03 — The four-record system

**Placement:** `#four`, immediately after the opening paragraph, before `.rec-grid`.

```
FILE NAME: personal-medical-journal-health-history-01-four-record-system.png
IMAGE TYPE: Scaffold C — horizontal step sequence (used as a four-part system map)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and caregivers
VISUAL GOAL: show that four short records, each answering one question, together cover
every situation — and that they point to one another rather than duplicating.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top centre in
bold navy (#0f1e2e): "Four records, four questions". Subtitle beneath in clinical teal
(#1a6b72): "Each one is short. Together they cover every situation."

Four rounded rectangular cards arranged horizontally in a single row on a very soft gray
panel (#f3f4f6), connected by bold navy right-pointing arrows. Each card has a coloured
top accent band, a simple flat line icon, a bold navy card title, one italic question line
in teal, and two short plain-language detail lines:

Card 1 — accent clinical red (#b91c1c), icon: a shield outline.
  Title "Emergency Health Summary". Question: "What must the team know immediately?"
  Details: "1–2 pages" · "Emergency, admission, referral"
Card 2 — accent clinical teal (#1a6b72), icon: a single document sheet.
  Title "Current Medical Summary". Question: "What is true now?"
  Details: "1–2 pages" · "Every consultation"
Card 3 — accent amber (#b8860b), icon: a simple line chart trending across time.
  Title "Medical Journal". Question: "What happened, and what changed?"
  Details: "Ongoing" · "Follow-up and complex illness"
Card 4 — accent renal green (#1f7a4d), icon: a folder outline.
  Title "Document Archive". Question: "Where is the original evidence?"
  Details: "As needed" · "Verification and detailed review"

Beneath the row, a single thin dashed teal arrow curves from Card 2, Card 3 and Card 1 back
down to Card 4, labelled in small navy text "every number traces back to an original".

Bottom strip: full-width soft gray band with the sentence in navy — "One summary for today,
one timeline for the past, one journal for what changed, one archive holding the proof."

Generous whitespace, mobile-readable labels at 11pt equivalent minimum, clean sans-serif
typography set in Inter. Bottom-right: "renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or
black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito
Sans, IBM Plex Sans, or Manrope — no serif, decorative, or handwritten typefaces.
Never omit the renalcarematters.com attribution. No photorealistic people.

QUALITY CHECK:
Four cards of identical width and height. Exactly one icon per card. All text legible at
thumbnail size. White background. Attribution visible bottom-right.
```

**Ready-to-paste figcaption:**
```html
<figcaption>
  <p class="fig-desc">The four records and the question each one answers: an emergency
  summary for what a team must know in seconds, a current summary for what is true today,
  a journal for what changed over time, and an archive holding the original reports that
  every number traces back to.</p>
</figcaption>
```

---

## 04 — Three medication lists, one patient

**Placement:** `#why`, immediately after the Aling Nena case paragraph, before the teal alert.

```
FILE NAME: personal-medical-journal-health-history-02-three-medication-lists.png
IMAGE TYPE: Scaffold B — side-by-side comparison, extended to three panels plus a resolution bar
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients, caregivers, and clinicians
VISUAL GOAL: three "correct" medication lists disagreeing, and the fourth column that
resolves them — the single idea the whole guide turns on.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white
(#ffffff) background. Title centred at top in bold navy (#0f1e2e): "Three lists, one
patient". Subtitle in clinical teal (#1a6b72): "Each one is correct where it was written.
Only the fourth is safe to prescribe from."

Three equal vertical panels separated by soft dashed grey dividers, each drawn as a simple
flat stylised document card with a coloured header band and a short list of generic
medicine rows rendered as small pill icons with short neutral placeholder labels:

Panel 1 — header amber (#b8860b), label "Hospital discharge summary · 2 months ago",
  eight pill rows.
Panel 2 — header amber (#b8860b), label "Health centre card · last updated a year ago",
  five pill rows.
Panel 3 — header clinical red (#b91c1c), label "What she actually swallows each morning",
  six pill rows, with three of them visually annotated by small flat icons and two-word
  captions: a halved tablet marked "half dose", a crossed-out tablet marked "stopped —
  dizzy", and a greyed tablet marked "never started".

Beneath all three, one full-width renal-green (#1f7a4d) resolution bar with white text:
"Record what is prescribed AND what is actually taken — the gap between them is the
information no chart contains."

All medicine names must be fictional and generic; use only neutral placeholder wording,
never a real brand. Rounded panel corners, ample negative space, mobile-readable labels
at 11pt equivalent minimum, clean sans-serif typography set in Inter. Bottom-right:
"renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid real brand names, avoid any identifiable patient information, avoid overprocessed
HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope.
Never omit the renalcarematters.com attribution. No photorealistic people.

QUALITY CHECK:
Three panels of identical width. Pill counts must read 8, 5, and 6 respectively. The green
resolution bar spans the full width. No real drug brand appears. Light background.
Attribution visible bottom-right.
```

**Ready-to-paste figcaption:**
```html
<figcaption>
  <p class="fig-desc">A fictional example: the same patient carries three medication lists
  that disagree — eight medicines on the hospital discharge summary, five on the health
  centre card, and six actually swallowed each morning, with one halved for dizziness, one
  stopped, and one never started because the pharmacy had no stock. Only a record that
  keeps "prescribed" and "actually taken" side by side exposes the difference.</p>
</figcaption>
```

---

## 05 — Anatomy of a one-page current summary

**Placement:** `#summary`, after the "What goes on the summary page" checklist.

```
FILE NAME: personal-medical-journal-health-history-03-anatomy-of-a-summary.png
IMAGE TYPE: Scaffold E — reference card, rendered as an annotated page mock-up
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and caregivers
VISUAL GOAL: show the information hierarchy of a good one-page summary — what sits at the
top, what a status word and a certainty label look like in place, and where the date goes.

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background.
Bold navy (#0f1e2e) title at top: "Anatomy of a one-page current summary". Small italic
grey subtitle: "Fictional example — not a real patient".

Centre of the canvas: a single clean stylised A4 page mock-up, drawn flat with a soft drop
shadow, tilted no more than 2 degrees, occupying about 60% of the canvas. Inside the page,
six stacked blocks with clear visual hierarchy:

  1. A header band in soft gray (#f3f4f6): "Dela Cruz, Maria · born 1962 · updated 14 Feb 2026"
  2. "My main concerns" — three short numbered lines
  3. "Active diagnoses" — three rows, each ending in a small coloured status pill:
     "Hypertension · 2011 — CONTROLLED" (green #1f7a4d),
     "Type 2 diabetes · 2015 — ACTIVE" (amber #b8860b),
     "Chronic kidney disease · 2022 — UNDER EVALUATION" (teal #1a6b72)
  4. "Medicines I actually take" — a compact two-column strip headed
     "Prescribed" and "How I take it"
  5. "Allergies" — one row reading "Penicillin — rash and facial swelling, 2009, severe"
  6. A footer line: "Reviewed 14 Feb 2026 · information from me and my clinic records"

Six thin teal (#1a6b72) leader lines run outward from these blocks to six small rounded
annotation cards arranged around the page margins, each with a bold navy label and one
short explanatory line:
  "Identity and date first — a page found alone must still be attributable"
  "Three to five concerns, most important first"
  "Every diagnosis carries a status word"
  "Two columns, always — prescribed and actual"
  "The reaction, not just the word allergic"
  "The review date tells the reader how much to trust it"

Annotation cards sit on very soft gray (#f3f4f6) with rounded corners and must not overlap
the page mock-up or each other. Generous margins, mobile-readable labels at 11pt equivalent
minimum, clean sans-serif typography set in Inter. Bottom-right: "renalcarematters.com" in
small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid crossing or tangled leader lines, avoid any real patient information, avoid real drug
brand names, avoid overprocessed HDR. NEVER use dark, navy, charcoal, or black backgrounds.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly six annotation cards, exactly six leader lines, none crossing. The page mock-up is
legible. "Fictional example" is stated. Light background. Attribution visible bottom-right.
```

**Ready-to-paste figcaption:**
```html
<figcaption>
  <p class="fig-desc">A fictional one-page current summary with its six load-bearing parts
  labelled: identity and date at the top, three to five concerns in order of importance,
  each diagnosis carrying a status word, medicines in two columns for prescribed and actual
  intake, allergies written with the real reaction, and a review date at the foot.</p>
</figcaption>
```

---

## 06 — Photograph the whole page

**Placement:** `#meds`, after the "Copy every name and strength from the box" paragraph.
Also cross-referenced from `#documents`.

```
FILE NAME: personal-medical-journal-health-history-04-photograph-the-whole-page.png
IMAGE TYPE: Scaffold B — side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and caregivers
VISUAL GOAL: the single most common avoidable record failure — a cropped photograph — shown
against the frame that actually works.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white
(#ffffff) background. Title centred at top in bold navy (#0f1e2e): "Photograph the whole
page". Subtitle in clinical teal (#1a6b72): "A cropped picture is the commonest reason a
test has to be repeated."

A soft dashed vertical divider splits the canvas into two equal panels.

LEFT panel, labelled in clinical red (#b91c1c): "Cropped — unusable". It contains two
stacked flat phone-screen frames drawn in simple line style. The upper frame shows a
laboratory report photographed so tightly that only one highlighted result row is visible,
with the patient name, the date, the unit, and the reference range all cut off outside the
frame edge — draw those missing zones as faded grey ghost text beyond a hard crop line.
The lower frame shows a loose white tablet photographed on a palm with no packaging at all.
Three small red cross markers annotate: "no name", "no date", "no unit or reference range".

RIGHT panel, labelled in renal green (#1f7a4d): "Whole page — usable". Two stacked flat
phone-screen frames. The upper frame shows the same laboratory report photographed
complete, flat, evenly lit, with the header block, the result row, the unit column and the
reference-range column all inside the frame. The lower frame shows a medicine blister strip
photographed with its full printed backing visible. Three small green check markers
annotate: "name and date visible", "unit and reference range visible", "generic name and
strength visible".

All text on the mock reports and packaging must be fictional, generic, and rendered as
short neutral placeholder wording — never a real brand, never a real patient name, never a
real laboratory result. Rounded panel corners, ample negative space, mobile-readable labels
at 11pt equivalent minimum, clean sans-serif typography set in Inter. Bottom-right:
"renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid real brand names, avoid identifiable patient data, avoid photorealistic hands with
distorted fingers, avoid overprocessed HDR. NEVER use dark, navy, charcoal, or black
backgrounds. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Two panels of identical width, two phone frames in each. Red crosses on the left only,
green checks on the right only. No real brand or patient name. Light background.
Attribution visible bottom-right.
```

**Ready-to-paste figcaption:**
```html
<figcaption>
  <p class="fig-desc">Left, the photographs that cannot be used: a laboratory result cropped
  so tightly that the name, date, unit and reference range fall outside the frame, and a
  loose tablet with no packaging. Right, the same two subjects photographed whole, so that
  every field a clinician needs is inside one frame.</p>
</figcaption>
```

---

## 07 — One symptom entry, in sequence

**Placement:** `#symptoms`, after the DATE–SYMPTOM algorithm card, before the comparison cards.

```
FILE NAME: personal-medical-journal-health-history-05-symptom-entry-sequence.png
IMAGE TYPE: Scaffold C — horizontal step sequence rendered as a timeline
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and caregivers
VISUAL GOAL: turn one worked symptom entry into a readable clock-time sequence — onset,
measurement, action, response — so the reader sees what "with dates" actually buys.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top centre in
bold navy (#0f1e2e): "One symptom, written so it can be used". Small italic grey subtitle:
"Fictional example — 24–25 August 2026".

A single bold horizontal navy timeline arrow runs left to right across the middle of the
canvas, with five evenly spaced circular time markers on it, each labelled beneath in navy
with a clock time. Above each marker sits a rounded rectangular card with a coloured top
accent band, a simple flat line icon, a bold short label, and one plain-language detail
line:

Marker 1 — "8:00 PM", accent clinical teal (#1a6b72), icon: a small onset spark.
  "Onset" · "Burning on urination began gradually"
Marker 2 — "8:00 PM – 6:00 AM", accent amber (#b8860b), icon: a simple counter.
  "Pattern" · "Passed urine seven times overnight, urgency, no visible blood"
Marker 3 — "9:30 PM", accent amber (#b8860b), icon: a thermometer outline.
  "Measurement" · "Temperature 37.8 °C"
Marker 4 — "10:00 PM", accent renal green (#1f7a4d), icon: a single tablet.
  "Action" · "Took paracetamol 500 mg"
Marker 5 — "Next morning", accent clinical red (#b91c1c), icon: a partial-response arrow.
  "Response" · "Temperature settled; burning continued. Slept poorly; still able to work"

Beneath the timeline, one full-width soft gray (#f3f4f6) strip with the sentence in navy:
"Same night, written as 'felt bad again, maybe a urine infection' — nothing above survives."

Generous whitespace, no card overlapping the timeline arrow, mobile-readable labels at 11pt
equivalent minimum, clean sans-serif typography set in Inter. Bottom-right:
"renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid real brand names, avoid identifiable patient data, avoid anatomical or clinical
imagery of the urinary tract, avoid overprocessed HDR. NEVER use dark, navy, charcoal, or
black backgrounds. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or
Manrope. Never omit the renalcarematters.com attribution. No photorealistic people.

QUALITY CHECK:
Exactly five markers and five cards, evenly spaced, none overlapping the arrow. Clock times
run forward left to right. "Fictional example" is stated. Light background. Attribution
visible bottom-right.
```

**Ready-to-paste figcaption:**
```html
<figcaption>
  <p class="fig-desc">A fictional symptom entry laid out as a timeline: onset at 8:00 PM,
  the overnight pattern, a measured temperature, the medicine taken and when, and the
  partial response by morning — including whether the person could still work. The same
  night recorded as "felt bad again" preserves none of it.</p>
</figcaption>
```

---

## 08 — How to take a home blood-pressure reading

**Placement:** `#measurements`, after the teal "A log only helps if somebody acts on it"
alert, before the calculator cards.

```
FILE NAME: personal-medical-journal-health-history-06-home-bp-technique.png
IMAGE TYPE: Scaffold D — single mechanism / one-panel technique poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and caregivers
VISUAL GOAL: the physical technique that makes a home reading worth recording, shown once,
correctly — posture is the part prose describes badly and a picture fixes instantly.

PROMPT:
Medical technique infographic, AJKD/NEJM graphical-abstract style, white (#ffffff)
background. Title at top in bold navy (#0f1e2e): "A reading worth writing down". Subtitle
in clinical teal (#1a6b72): "Five minutes of quiet first — then measure like this."

Centre-left: a clean semi-realistic side-profile medical illustration of a seated adult of
Filipino appearance, drawn in restrained flat-vector clinical style with muted natural skin
tone and simple neutral clothing, shown from the side at a plain chair and small table.
The figure is correctly positioned: back supported against the chair, both feet flat on the
floor and uncrossed, upper arm bare, forearm resting on the table with the cuff at the
level of the heart, and a small home blood-pressure monitor on the table.

Five thin teal (#1a6b72) leader lines run from the figure to five small rounded annotation
cards stacked down the right third of the canvas, each with a bold navy label and one short
line:
  "Back supported" · "Sit upright against the chair back"
  "Feet flat" · "Both feet on the floor, legs uncrossed"
  "Arm at heart level" · "Forearm resting on the table, not hanging"
  "Bare skin" · "Cuff on the bare upper arm, not over a sleeve"
  "Quiet first" · "Five minutes seated, no talking, no phone"

Bottom strip: full-width soft gray (#f3f4f6) band with the sentence in navy — "Write down
the reading you dislike as faithfully as the one you like."

Anatomically plausible proportions, correct hands, no distortion. Generous whitespace,
mobile-readable labels at 11pt equivalent minimum, clean sans-serif typography set in Inter.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid distorted hands or faces, avoid implausible anatomy, avoid displaying any specific
blood-pressure number on the monitor screen, avoid real device brand names, avoid
overprocessed HDR. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY the
sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly five annotation cards and five leader lines, none crossing. Posture is correct in
all five respects. The monitor screen shows no readable number. Light background.
Attribution visible bottom-right.
```

**Ready-to-paste figcaption:**
```html
<figcaption>
  <p class="fig-desc">Correct home blood-pressure technique: five quiet minutes seated
  first, back supported, both feet flat and uncrossed, the cuff on bare skin, and the
  forearm resting at heart level rather than hanging. A reading taken any other way is not
  worth entering in the log.</p>
</figcaption>
```

---

## 09 — Where information is lost across a transition

**Placement:** clinician section `#md-evidence`, after the "size and shape of the gap"
paragraphs, before the "What a patient-held record has actually been shown to do" heading.

```
FILE NAME: personal-medical-journal-health-history-07-md-transitions-information-loss.png
IMAGE TYPE: Scaffold C — horizontal step sequence used as a leak map
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: locate the documented losses at each handover point, so the reader sees the
patient-held record as a bridge across specific gaps rather than a general good idea.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top centre in
bold navy (#0f1e2e): "Where the information is lost". Subtitle in clinical teal (#1a6b72):
"Documented gaps at each handover — and the one record that crosses all of them."

Four rounded rectangular stage cards arranged horizontally on a very soft gray panel
(#f3f4f6), connected by bold navy right-pointing arrows, each with a navy header band and a
simple flat line icon:
  Stage 1 "Admission" · icon: hospital door
  Stage 2 "Inpatient stay" · icon: bed
  Stage 3 "Discharge" · icon: exit arrow
  Stage 4 "Follow-up clinic" · icon: outpatient chair

Below each stage card, a downward amber (#b8860b) "leak" arrow drops into a small rounded
caution card in amber-tinted fill, each holding one short finding line in navy:
  Under Admission — "53.6% of admissions carry at least one unintended medication discrepancy"
  Under Inpatient stay — "Omission of a regularly taken drug is the commonest single error"
  Under Discharge — "Direct hospitalist-to-primary-care contact in only 3–20% of discharges"
  Under Follow-up clinic — "Discharge summary available at the first visit in only 12–34%"

Running beneath all four stages, one continuous renal-green (#1f7a4d) horizontal bar
spanning the full width, with white text centred: "The patient-held record is the only
document present at all four points."

Small grey source line at the very bottom-left in 9pt: "Cornish 2005 · Tam 2005 ·
Kripalani 2007". Generous whitespace, mobile-readable labels at 11pt equivalent minimum,
clean sans-serif typography set in Inter. Bottom-right: "renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid inventing any statistic not listed above, avoid overprocessed HDR, avoid excessive
saturation. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY the sans-serif
fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope.
Never omit the renalcarematters.com attribution. No photorealistic people.

QUALITY CHECK:
Four stage cards of identical size, four leak arrows, four caption cards. Every number
matches the four supplied strings exactly — no invented figures. The green bar spans the
full width. Light background. Attribution visible bottom-right.
```

> **Verification note for production:** the four figures in this image are quoted from the
> guide's own cited sources (Cornish 2005; Tam 2005; Kripalani 2007). If the generator
> alters any digit, regenerate — do not retouch the number by hand and do not accept a
> plausible-looking substitute.

**Ready-to-paste figcaption** (clinician section, English only):
```html
<figcaption>
  <p class="fig-desc">The four handover points and the documented loss at each: unintended
  medication discrepancies at admission, omission of regularly taken drugs during the stay,
  absent hospitalist-to-primary-care contact at discharge, and a missing discharge summary
  at the first follow-up visit. The patient-held record is the only document present at all
  four.</p>
</figcaption>
```

---

## 10 — Best possible medication history: reconciliation algorithm

**Placement:** clinician section `#md-recon`, replacing or sitting beside the existing
six-step `.algo-card`.

Generated with `williamriveromd-algorithm-generator-skill`, **Style Mode C — house style**
(this is a branded renalcarematters.com guide asset, not an AHA emergency algorithm and not
a journal pharmacotherapy pathway).

```
FILE NAME: personal-medical-journal-health-history-08-md-bpmh-algorithm.png
IMAGE TYPE: Clinical algorithm — Style Mode C, renalcarematters.com house style
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: turn the six-step reconciliation into a decision pathway with the two
discrepancy branches made explicit.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com
house style. Use a white background, restrained navy and teal typography set in Inter
(never a serif font), thin teal connector arrows, and generous margins. The layout should
be centred, symmetrical, portrait, and suitable for a clinician-facing nephrology education
guide.

Title at top in navy #0f1e2e: "Building a best possible medication history". Subtitle in
teal #1a6b72: "With a patient-held record as source one — never as truth."

Use these colour conventions:
- Navy #0f1e2e for title, body text, and structural emphasis
- Teal #1a6b72 for decision nodes and connector accents
- Green #1f7a4d for final recommended actions and qualifying endpoints
- Amber #b8860b for caution nodes
- Soft gray for explanatory side notes

Content to render, top to bottom:

1. Rounded navy-outlined action node: "Take the patient's own list. Note its
   'last reviewed' date."
   — soft gray side note to the right: "A list reviewed last month behaves differently
     from one written 18 months ago."
2. Rounded action node: "Add a second independent source" with three short sub-lines:
   "Containers or full-label photographs" / "Dispensing pharmacy record" /
   "Last discharge summary or caregiver interview"
3. Rounded action node: "Ask the actual-intake question without judgement" with two short
   quoted sub-lines: "Which have been hardest to take?" / "Which did you never start, or
   stop on your own?"
4. Amber caution node: "Sweep the categories institutional lists omit" with sub-line:
   "OTC analgesics and NSAIDs · proton pump inhibitors · herbal and traditional
   preparations · topical and ophthalmic · inhalers · injectables given elsewhere ·
   as-needed medicines"
5. Teal DIAMOND decision node: "Discrepancy against current orders?"
   - Left branch labelled "No" in short navy text → green endpoint node: "Document the
     list as reconciled, with sources named."
   - Right branch labelled "Yes" → teal diamond: "Intentional?"
       - Branch "Yes" → amber node: "Intentional but undocumented — document the reason
         now. This is where most downstream error is generated."
       - Branch "No" → red-outlined node in #b91c1c: "Unintentional — correct the order
         and reconcile."
6. Both lower branches converge into one green endpoint node at the bottom:
   "Give the patient a corrected list with reasons. Ask them to update their own record
   before they leave."

Two small soft-gray footnote boxes at the bottom, side by side:
  "Always pass the stopped-drug list — a drug held for kidney injury, hyperkalaemia,
   bleeding or angio-oedema will otherwise be restarted."
  "Always pass the allergy field — replace bare labels with substance, reaction, severity
   and date."

Design requirements:
- Clear title and subtitle
- Top-to-bottom clinical logic with balanced left-right branching
- Rounded rectangles for actions and endpoints, diamonds for the two decision points
- Consistent spacing, alignment, node widths, and arrow lengths
- No dark background, no clutter, no photorealistic people, no decorative icons
- All text legible at full size and at thumbnail size
- Include a small professional footer reading "© renalcarematters.com" positioned at the
  bottom-right corner in subtle gray medical-publication styling

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid spaghetti connectors, avoid inventing extra steps or thresholds, avoid overprocessed
HDR. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY the sans-serif fonts
Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the attribution footer.

QUALITY CHECK:
Exactly two diamond decision nodes. Every branch is labelled. Both lower branches converge
on one endpoint. Node widths consistent. Light background. "© renalcarematters.com" visible
bottom-right.
```

**Ready-to-paste figcaption** (clinician section, English only):
```html
<figcaption>
  <p class="fig-desc">Reconciliation pathway: take the patient's own list as the first
  source rather than as truth, add a second independent source, ask the actual-intake
  question without judgement, sweep the categories institutional lists omit, then classify
  every discrepancy as intentional-and-documented, intentional-but-undocumented, or
  unintentional before closing the loop in writing.</p>
  <dl class="fig-abbrevs">
    <dt>BPMH</dt><dd>Best possible medication history</dd>
    <dt>NSAID</dt><dd>Nonsteroidal anti-inflammatory drug</dd>
    <dt>OTC</dt><dd>Over-the-counter</dd>
  </dl>
</figcaption>
```

---

## Production notes

**Not AI-generated.** The blueprint's asset #8, a *booklet preview montage* for the download
section, must be a genuine render of pages from
`downloads/personal-medical-journal-booklet.pdf` — three or four page thumbnails fanned on a
light background. Generating a fake booklet preview would misrepresent the actual download.

**Markup for every figure.** Each in-body figure ships as:

```html
<figure style="margin:28px 0;">
  <picture>
    <source srcset="../images/personal-medical-journal-health-history-NN-name.webp" type="image/webp">
    <img src="../images/personal-medical-journal-health-history-NN-name.png" loading="lazy"
         width="1792" height="1024" alt="[descriptive alt]"
         style="width:100%;height:auto;display:block;border-radius:10px;">
  </picture>
  <figcaption> … fig-desc … </figcaption>
</figure>
```

**Language.** Figures 03–08 sit in patient-mode sections, so their `<figcaption>` text needs
the four `data-lang` sibling spans (`en`, `tl`, `ceb`, `kap`). Figures 09 and 10 sit in
clinician-mode sections and stay English-only. The images themselves are English in all
cases — the caption carries the translation.

**After adding the figures, re-run:**

```bash
python3 patch_hero_fetchpriority.py --guide personal-medical-journal-health-history.html
python3 patch_hero_fullwidth.py --guide personal-medical-journal-health-history.html
python3 patch_hero_maxwidth.py --guide personal-medical-journal-health-history.html
python3 patch_image_lightbox.py --guide personal-medical-journal-health-history.html
python3 patch_img_dimensions.py --guide personal-medical-journal-health-history.html
python3 patch_reading_time.py --guide personal-medical-journal-health-history.html
```

**Accept/reject checklist for every generated image:**

- Light background — reject any dark, navy, or charcoal fill
- `renalcarematters.com` attribution present (01 is the sole exception)
- Sans-serif only: Inter, Nunito Sans, IBM Plex Sans, or Manrope
- No gibberish text, no real brand names, no identifiable patient data
- Every number matches the string supplied in the prompt — **regenerate rather than retouch**
- Legible at thumbnail width (300 px)
- WCAG AA contrast for any text rendered inside the image
- Save both `.png` and a `.webp` twin at the stated pixel dimensions
