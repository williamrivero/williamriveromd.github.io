# Image Plan & Prompt Pack — Strengthening Kidney Resilience to AKI

**Guide:** `guides/strengthening-kidney-resilience-to-aki.html` · **Canonical:** https://renalcarematters.com/guides/strengthening-kidney-resilience-to-aki.html
**Pipeline:** Stage 1 (this file, written with the repo graphic skills) → generate in the ChatGPT Image Generator GPT (https://chatgpt.com/g/g-pmuQfob8d-image-generator) → Stage 2 `williamriveromd-local-image-generator` (validation, manifests, `og:image` tags).
**Prepared:** November 8, 2026. Every number inside a prompt comes from a source verified for the guide (BigpAK-2, Lancet 2025, Table 3 arm denominators; the 2012 international AKI guideline timing windows; the 2020 UK appropriateness panel for follow-up timing). Do not let the generator add numbers, drug doses, fluid volumes, or names that are not written in the prompt.

**Skills used:** `williamriveromd-hero-vignette` v3 (00) · `williamriveromd-simple-figure` Scaffold C (01, 03), Scaffold D (02), Scaffold C timeline variant (04), Scaffold B bar comparison (05) · OG card follows the house OG pattern from the infographic skill.

---

## Part 1 · Visual strategy

### 1.1 The goal
The guide's single idea is that kidney injury is usually a **vulnerable kidney meeting a hit**, and that four practical habits make that meeting less damaging. Images must make the levers concrete (a card, a checklist, a timeline), show *why* sick days matter physiologically (the two-ended glomerulus), and present the one strong trial in absolute terms. No image may imply a fixed fluid amount, a universal list of drugs to stop, or a "resilience score."

### 1.2 Shared visual vocabulary (draw identically in every image)

| Element | Always drawn as |
|---|---|
| **Kidney** | A single soft bean-shaped kidney icon in clinical teal #1a6b72 outline with a light teal fill |
| **The four levers** | Compass (starting point), shield (avoid hits), stopwatch (act early), seedling (finish recovery) |
| **Sick-day card** | A cream index card with blank write-in lines and a small kidney icon in the corner; never readable drug names |
| **Hit / stress** | A small amber (#b8860b) lightning bolt |
| **Safe / continue** | Renal green #1f7a4d + check mark |
| **Danger / urgent** | Clinical red #b91c1c |
| **Review date** | A wall calendar with one day circled in teal |
| **Structure / text** | Navy #0f1e2e; headings clinical teal #1a6b72 |

### 1.3 House constitution (applies to every prompt)
- Light backgrounds only (white #ffffff, off-white #fafafa, soft gray #f3f4f6, light teal #eef6f7). Never navy, charcoal, or black.
- Fonts: **Inter, Nunito Sans, IBM Plex Sans, or Manrope only**; each prompt names one. Never serif.
- Attribution on every image: `© renalcarematters.com` (bottom-right; bottom-center for portrait), small, ~70% opacity. The hero vignette is the only exception: it is wordless by the hero-vignette spec.
- No guideline or society acronyms, journal names, brand names, or device logos inside images. The trial name "BigpAK-2" appears only in clinician figure 05, where the trial *is* the data label.
- Output `.png`; save a `.webp` twin with the same stem in `images/`.

---

## Part 2 · Image inventory and placement

| # | File stem | Section | Audience | Skill |
|---|---|---|---|---|
| 00 | `strengthening-kidney-resilience-to-aki-vignette-hero` | Hero (patient tab) | Patients | hero-vignette v3 · Scaffold B |
| OG | `strengthening-kidney-resilience-to-aki-og` | `og:image` / `twitter:image` | Social | OG card pattern |
| 01 | `…-01-four-levers` | `#resilience` | Patients | simple-figure C |
| 02 | `…-02-autoregulation-reserve` | `#md-framework` | Clinicians | simple-figure D |
| 03 | `…-03-sick-day-card` | `#illness` | Patients | simple-figure C |
| 04 | `…-04-aki-akd-ckd-continuum` | `#md-transition` | Clinicians | simple-figure C (timeline) |
| 05 | `…-05-bigpak2-absolute` | `#md-periop` | Clinicians | simple-figure B (bar comparison) |

All six in-body `<figure>` tags and the hero `<picture>` already reference these stems in the guide.

---

## Part 3 · Prompts

### 00 · Hero vignette ● (patient hero)

```
FILE NAME: strengthening-kidney-resilience-to-aki-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: overhead top-down
HUMAN VARIATION (vs. previous guide): no people (previous AKI guide showed a family, nephrologist, and nurse at an ICU bedside)
AUDIENCE: patients and families
VISUAL GOAL: Preparation at home before illness — a calm kitchen table where the kidney plan is ready before the storm.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR
vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the
circle never touches the canvas edges). Composition archetype: Object Hero. Camera: overhead, straight
top-down.

Subject: a light narra-wood Filipino kitchen table seen from directly above. The hero object, slightly
left of center and occupying about 60% of the circle, is a cream index card with blank handwriting lines
and a small teal kidney outline in one corner, a pencil resting diagonally across it. Supporting elements
(20–30% of the circle), arranged loosely around the card: a clear seven-day pill organizer with a few
plain white and pale yellow tablets, a tall glass of water with soft caustic light, a compact home
blood-pressure monitor with its cuff neatly coiled, and a digital thermometer. In the lower-right edge of
the circle, a small out-of-focus corner of a window sill with raindrops on the glass suggests the rainy
season without showing a storm.

Reserve the upper-right quarter of the circle (about 20–25%) as a clean TITLE SAFE ZONE of plain,
softly lit wood grain fading to a gentle teal-tinted (#eef6f7) blur, with no objects, labels, or
shadows of objects inside it.

Bright, airy, soft diffused daylight from the upper left; gentle shadows; calm, reassuring colour grade
harmonizing with clinical teal #1a6b72 and navy #0f1e2e accents (the pill-organizer lids are pale teal).
Soft edge falloff toward a slightly deeper warm neutral at the rim of the circle. Full-bleed within the
inscribed circle, no rectangular borders.

Absolutely NO readable text anywhere: the card lines are blank, the monitor screen is dark and blank, the
pill organizer has no day letters, no packaging, no brand names, no title, no logo, no watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting objects, dozens of icons, tiny unreadable
labels, infographic clutter, cropped circle, cropped objects, edge clipping, objects touching the
circular border, anything inside the title safe zone, baked-in text, titles, captions, logos, watermarks,
readable drug names or packaging, rectangular borders, frames, banners, dark / charcoal / black
backgrounds, cartoon style, neon, HDR, over-saturation, hospital equipment, blood, needles.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE
dominant hero object (the blank card) occupying about 60% of the circle, four supporting objects, a clean
title-safe zone upper right. No people. Overhead framing differs from the previous AKI guide's eye-level
bedside scene. No readable text anywhere.
```

### OG · Social share card ●

```
IMAGE NUMBER: OG
SECTION PLACEMENT: <meta property="og:image"> and twitter:image (already in the guide head)
FILE NAME: strengthening-kidney-resilience-to-aki-og.png
ARCHETYPE: OG social card (light base)
AUDIENCE: social feeds, Messenger and Viber link previews
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
PURPOSE: Make the share preview read as a practical prevention guide, legible at thumbnail size.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Social share card, exactly 1200×630 landscape. Off-white (#fafafa) background with a very light teal
(#eef6f7) rounded panel filling the right 45%. Left side, set in Inter: title in bold navy (#0f1e2e),
two lines, large: "Strengthening Kidney" / "Resilience to AKI". Below in clinical teal (#1a6b72), Nunito
Sans, one line: "Protect your kidneys during illness, before procedures, and after an injury." Under it,
small gray text: "Patients & families · clinicians · 4 languages". Right panel: a calm semi-flat 3D
illustration of a single teal-outlined kidney resting on a cream index card with blank lines, with four
small round badges arranged in an arc above it — a compass, a shield, a stopwatch, and a seedling — each
in a soft circle of teal, green (#1f7a4d), amber (#b8860b), and teal respectively, no text on the badges.
Thin teal vertical rule between the halves. Bottom-left, small navy: "W Rivero, MD · renalcarematters.com".
Bottom-right: "© renalcarematters.com" in small gray at 70% opacity. All text crisp and correctly spelled;
keep every element inside a 40-px safe margin.

NEGATIVE INSTRUCTIONS:
No dark background, no faces, no blood, no clutter, no serif fonts, no gibberish text, no drug names, no
guideline acronyms or journal names; the only mark is the © renalcarematters.com footer.

QUALITY CHECK:
Title legible at 300 px wide; exact 1200 × 630; spelling of "Resilience" correct.

ALT TEXT: Strengthening Kidney Resilience to AKI — protect your kidneys during illness, before procedures, and after acute kidney injury, a guide by W Rivero, MD
OG WIDTH: 1200
OG HEIGHT: 630
```

### 01 · Four levers of kidney resilience ○ (patient, `#resilience`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-01-four-levers.png
IMAGE TYPE: Scaffold C — circular four-step sequence
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients
VISUAL GOAL: Four everyday habits surround and protect the kidney.

PROMPT:
Clean clinical education infographic, white (#ffffff) background, set in Manrope with titles in Inter.
Title at top center in bold navy (#0f1e2e): "Four steps to a more resilient kidney". In the center, one
soft bean-shaped kidney icon with a teal (#1a6b72) outline and light teal (#eef6f7) fill. Around it, four
rounded cards placed at 12, 3, 6, and 9 o'clock, joined by a thin teal circular arrow running clockwise.
Card 1 (top, teal accent band, compass icon): "Know your starting point" — "Usual creatinine · medicine
list". Card 2 (right, green #1f7a4d accent band, shield icon): "Avoid the avoidable hits" — "Sick-day plan
· careful pain relievers · heat and floodwater". Card 3 (bottom, amber #b8860b accent band, stopwatch
icon): "Act early" — "Same-day check when ill · plan before surgery". Card 4 (left, teal accent band,
seedling icon): "Finish the recovery" — "Follow-up tests · review at about 3 months". Small amber
lightning bolts drawn just outside the circle, deflected by the cards. Generous whitespace,
mobile-readable labels at least 11 pt. Bottom-right: "© renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, HDR,
excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY Inter and Manrope.
No drug names, no numbers other than "3", no guideline acronyms. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
Four cards, one kidney, one clockwise loop; every label spelled exactly as written; readable on mobile;
light background; attribution bottom-right.
```

### 02 · Why sick days strain the kidney ○ (clinician, `#md-framework`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-02-autoregulation-reserve.png
IMAGE TYPE: Scaffold D — single mechanism, one-panel
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Glomerular pressure is defended at both ends; volume depletion plus common drugs removes both defenses.

PROMPT:
Medical pathophysiology infographic, review-article graphical-abstract style, white (#ffffff) background,
labels in IBM Plex Sans. Title at top in bold navy (#0f1e2e): "Two-ended defense of filtration
pressure"; subtitle in clinical teal (#1a6b72): "and what removes it on a sick day". Center: a clean
semi-photorealistic 3D glomerulus (capillary tuft inside Bowman's capsule) with an afferent arteriole
entering from the left and a narrower efferent arteriole leaving to the right; a red-to-pink gradient
shows blood flow left to right, and a small pressure gauge icon sits over the tuft.
Left side callout card (renal green #1f7a4d header): "Afferent: prostaglandins dilate" with a small
green outward-arrow ring around the afferent vessel. Right side callout card (green header): "Efferent:
angiotensin II constricts" with a small green inward-arrow ring around the efferent vessel.
Below, a row of four small amber (#b8860b) "removal" chips, each with a thin amber arrow pointing to the
structure it affects: "Volume depletion" (arrow to the incoming blood), "NSAIDs" (arrow to the afferent
ring, which is crossed out), "ACE inhibitor / ARB" (arrow to the efferent ring, which is crossed out),
"Diuretics" (arrow to the incoming blood). A fifth small teal chip near the tubule: "SGLT2 inhibitor —
lowers glomerular pressure (protective long-term)".
Bottom strip in soft gray (#f3f4f6), navy text: "Each drug helps at steady state; combined with volume
depletion they narrow the autoregulatory margin." Ample negative space, no clutter, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, AI gibberish text, anatomically wrong glomerulus (efferent must
be narrower than afferent and both at the vascular pole on the same side of the capsule in reality —
draw them at the same pole, splayed for clarity), HDR, saturation. NEVER dark backgrounds. Use ONLY IBM
Plex Sans. No brand names, no doses, no guideline acronyms. Never omit the attribution.

QUALITY CHECK:
Afferent and efferent arise at the same vascular pole; two green defenses, four amber removals, one teal
SGLT2 note; spelling exact; light background; attribution bottom-right.
```

### 03 · The sick-day card in three moments ○ (patient, `#illness`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-03-sick-day-card.png
IMAGE TYPE: Scaffold C — horizontal three-step sequence
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients
VISUAL GOAL: The card is written before illness, followed during illness, and closed by the team at restart.

PROMPT:
Clean clinical education infographic, white (#ffffff) background, text in Nunito Sans with titles in
Inter. Title at top center in bold navy (#0f1e2e): "Your sick-day card — three moments". Three rounded
cards in one horizontal row on a very soft gray panel (#f3f4f6), joined by bold navy right-pointing
arrows.
Card 1 (teal #1a6b72 accent band): small illustration of two pairs of hands — a doctor's in a white
sleeve and a patient's — filling in a cream index card with blank lines. Label: "Before you get sick".
Bullets: "Fill it in with your doctor" · "Say the plan back".
Card 2 (amber #b8860b accent band): the same cream card held next to a phone and a glass of water;
a small thermometer. Label: "When you get sick". Bullets: "Follow your card" · "Call early".
Card 3 (green #1f7a4d accent band): the cream card with a small green check mark and a wall calendar with
one day circled in teal. Label: "When you recover". Bullets: "Your team says when to restart" · "Blood
test on the planned date".
Bottom strip, full width, soft gray, navy text: "Your card records your own team's instructions — it is
not a list everyone should stop." Bottom-right: "© renalcarematters.com" in small semi-transparent navy
text.

NEGATIVE INSTRUCTIONS:
No readable drug names, doses, or fluid amounts on any card; no faces required (hands only); no hospital
beds; no cartoon style, clutter, gibberish text, HDR. NEVER dark backgrounds. Use ONLY Nunito Sans and
Inter. Never omit the attribution.

QUALITY CHECK:
Exactly three cards, left-to-right arrows, every label exact, cards blank of medical specifics, light
background, attribution bottom-right.
```

### 04 · AKI, AKD, CKD — one continuum ○ (clinician, `#md-transition`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-04-aki-akd-ckd-continuum.png
IMAGE TYPE: Scaffold C — horizontal timeline
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians (also readable by patients)
VISUAL GOAL: Show the time windows and the follow-up checkpoints that catch incomplete recovery.

PROMPT:
Clean clinical timeline infographic, white (#ffffff) background, labels in Inter. Title in bold navy
(#0f1e2e): "From injury to recovery — one continuum". A single horizontal arrow-shaped timeline across
the canvas, divided into three colored segments: left segment amber (#b8860b) labeled "AKI" with "Day 0–7"
beneath; middle segment soft purple (#6c3d8e) labeled "AKD" with "Day 7–90"; right segment navy-outlined
light gray labeled "CKD" with ">90 days". Above the timeline, three teal (#1a6b72) checkpoint pins with
small icons: at the start of the middle segment, a hospital door icon "Discharge: baseline, peak, latest
creatinine"; within the middle segment, a stethoscope icon "1–2 weeks to 1 month: labs + medicine review";
at day 90, a calendar icon with one day circled "About 3 months: creatinine/eGFR + urine albumin". Below
the timeline, a thin green (#1f7a4d) branch curving up and off the timeline before the CKD segment labeled
"Recovery". Bottom strip in soft gray, navy text: "Persistence past 90 days meets the time criterion for
CKD; chronicity and context still decide the diagnosis." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No other numbers or thresholds; no guideline acronyms; no cartoon style, clutter, gibberish text. NEVER
dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Three segments in the correct order and colors; checkpoint labels exact; "eGFR" lowercase e; light
background; attribution bottom-right.
```

### 05 · BigpAK-2 in absolute terms ○ (clinician, `#md-periop`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-05-bigpak2-absolute.png
IMAGE TYPE: Scaffold B — side-by-side bar comparison
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Show the short-term absolute benefit and the absent 90-day difference side by side.

PROMPT:
Medical education comparison chart, publication style, white (#ffffff) background, all text in IBM Plex
Sans. Title in bold navy (#0f1e2e): "BigpAK-2: prevention bundle in high-risk major surgery". Subtitle in
teal (#1a6b72): "Selected adults at high risk by clinical factors and urine stress biomarkers".
Two panels separated by a soft dashed vertical divider.
Left panel heading: "Moderate or severe kidney injury within 72 hours". Two vertical bars on a light gray
gridline axis from 0% to 25%: "Usual care" bar in soft gray-navy reaching 22.3%, labeled "22.3% (131/588)";
"Bundle" bar in teal reaching 14.4%, labeled "14.4% (84/584)". Between the bars, a small green (#1f7a4d)
bracket labeled "about 8 fewer per 100".
Right panel heading: "Major adverse kidney events at 90 days". Two bars on the same 0–25% axis:
"Usual care" 10.6% and "Bundle" 11.0%, both in light gray with labels, and a small neutral note "no
difference".
Bottom strip in soft gray, navy text: "Bundle = hemodynamic monitoring, volume optimization, avoiding
nephrotoxins and contrast, glucose control." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Bar heights must be proportional to the stated percentages on a shared 0–25% axis; do not add odds
ratios, confidence intervals, p-values, or any other numbers; no journal names; no 3D bars; no cartoon
style; NEVER dark backgrounds. Use ONLY IBM Plex Sans. Never omit the attribution.

QUALITY CHECK:
Four bars with exact values 22.3, 14.4, 10.6, 11.0; denominators 131/588 and 84/584 exactly; both panels
share the same axis; light background; attribution bottom-right.
```

---

## Part 4 · After generation
1. Save each PNG to `images/` with the stem above and create a `.webp` twin.
2. Run Stage 2 (`williamriveromd-local-image-generator`) to validate and confirm the `og:image` tags (already present in the guide head with 1200 × 630).
3. Spot-check figure 05 bar heights and figure 02 vessel anatomy before publishing — these are the two most error-prone renders.
