# Image Plan Blueprint & Prompt Pack — Strengthening Kidney Resilience to AKI

**Guide:** `guides/strengthening-kidney-resilience-to-aki.html` · **Canonical:** https://renalcarematters.com/guides/strengthening-kidney-resilience-to-aki.html
**Version:** v2.1 (November 9, 2026). v2.1 adds a STYLE LOCK to every prompt: the first v2 render came out as flat vector diagrams that did not match the rest of the site, so those files were removed from the guide. Generate every image in the Image Generator GPT, not as SVG or code-drawn graphics.
**Pipeline:** Stage 1 (this file) → paste each prompt into the ChatGPT Image Generator GPT (https://chatgpt.com/) → Stage 2 `williamriveromd-local-image-generator` (validation, manifests, `og:image` tags).
**Skills used:** `williamriveromd-hero-vignette` v3 · `williamriveromd-infographic-skill` v5 · `williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure` · `williamriveromd-algorithm-generator-skill` (Mode C) · `williamriveromd-organ-crosstalk-sigil-graphic`.

**Number rule.** Every number that appears inside a prompt is taken from a source the guide cites and was checked for the guide: BigpAK-2 (Lancet 2025, Table 3 arm denominators), the 2012 international AKI guideline (timing windows), the 2020 ACR–NKF contrast consensus (eGFR bands), the 2020 UK follow-up appropriateness panel (review timing), and the guide's own synthetic teaching example (creatinine 1.00 / 2.10 / 1.40 mg/dL). Tell the generator not to add any other number, dose, fluid volume, drug brand, or name.

---

## Part 1 · Visual strategy

### 1.1 What the images must do
The guide asks readers to accept three ideas that words carry poorly:

1. **Resilience is invisible.** A normal creatinine does not show how much reserve is left. Images make the reserve visible as a concept (backup pumps, a gauge, a staircase), always labeled as a concept, never as a measurement.
2. **The same "hit" lands differently.** Two people, one illness, two outcomes. The difference is the starting reserve and the plan.
3. **Most protection is a habit, not a pill.** Four habits (know, avoid, act, finish) recur in every patient image as the same four icons, so a reader who cannot read English still recognizes the step.

Clinician images do a different job: compress a decision (escalation, contrast, perioperative care), show one trial honestly in absolute terms, and show how certain each claim is.

### 1.2 Design rules for readers of every education level

| Rule | Why it helps | How the prompts enforce it |
|---|---|---|
| **One idea per image** | Working memory is limited, more so when unwell or worried | Each prompt states one VISUAL GOAL; patient images cap at 6–8 short labels |
| **Concrete metaphor, then the real thing** | An everyday picture anchors a hidden process; walking it back prevents a false model | Backup pumps → nephrons; garden hose with two valves → glomerulus; each patient metaphor sits next to a caption naming the real structure |
| **Icon + 1–4 words, never icon alone** | Icons alone are ambiguous; words alone fail low literacy and non-English readers | Every patient icon carries a short English label; the label is redundant with the icon so TL/CEB/KAP readers still follow |
| **Numbers as people** | "22.3% vs 14.4%" means little to many readers; 100 figures with 8 fewer shaded is understood at a glance | Figure 10 uses two 10×10 icon arrays; the clinician version (22) keeps the percentages |
| **Show what to *do*, not only what goes wrong** | Fear without an action lowers engagement | Every patient image ends in a green action cue (call, bring, ask, keep the appointment) |
| **Filipino context** | Recognition builds trust | Mefenamic acid on the pain-reliever chart, the March–May hot season, wading after a typhoon, jeepney commute, narra-wood table |
| **Calm, not alarming** | Frightening images are avoided or skipped | No blood, needles, ICU drama, or distressed faces; red reserved for "go now" signs only |
| **Same picture, same meaning** | Consistency teaches faster than variety | Shared visual vocabulary (1.3) drawn identically in every image |
| **Text equivalent for every number image** | Accessibility and screen readers | Each figure's `fig-desc` in the guide restates the numbers in words |

### 1.3 Shared visual vocabulary (draw identically in every image)

| Element | Always drawn as |
|---|---|
| **Kidney** | One soft bean-shaped kidney, clinical teal #1a6b72 outline, light teal #eef6f7 fill |
| **Reserve (concept)** | A small vertical gauge beside the kidney: green when full, amber when low; always captioned "concept" — never a number |
| **Habit 1 · Know your starting point** | Compass, teal |
| **Habit 2 · Avoid the avoidable hits** | Shield, renal green #1f7a4d |
| **Habit 3 · Act early** | Stopwatch, amber #b8860b |
| **Habit 4 · Finish the recovery** | Seedling, teal |
| **A "hit" (illness, heat, medicine, surgery)** | Small amber lightning bolt |
| **Sick-day card** | Cream index card with blank lines and a tiny kidney in one corner; never readable drug names |
| **Go now / danger** | Clinical red #b91c1c with a simple exclamation triangle |
| **Do this / safe** | Renal green #1f7a4d with a check mark |
| **Review date** | Wall calendar with one day circled in teal |
| **Creatinine value** | Small lab-slip icon with a number in navy |
| **Text and structure** | Navy #0f1e2e; headings clinical teal #1a6b72 |

### 1.4 House constitution (applies to every prompt)
- **Rendering style:** rich, full-color, semi-3D illustrated infographics that match the existing guide figures (for example `aki-icu-dialysis-decisions-03-bridge-not-cure.png` and `aki-does-not-end-at-discharge-02-five-domains.png`). Never flat vector, SVG-style, or thin line art.
- Light backgrounds only (white #ffffff, off-white #fafafa, soft gray #f3f4f6, light teal #eef6f7, warm cream #f8f5f0). Never navy, charcoal, or black.
- Fonts: **Inter, Nunito Sans, IBM Plex Sans, or Manrope only**; each prompt names its font. Never serif.
- Attribution on every image except the wordless hero: `© renalcarematters.com`, small, ~70% opacity, bottom-right (bottom-center for portrait).
- No guideline or society acronyms, journal names, drug brand names, or device logos inside patient images. Clinician images may name a trial only where the trial is the data label (22, 25).
- American English spelling in every label.
- Output `.png`; save a `.webp` twin with the same stem in `images/`.
- Fixed sizes: hero 2048 × 2048; OG exactly 1200 × 630.

### 1.5 Language note
All on-image words are English and deliberately few. Because each label repeats what its icon shows, Tagalog, Cebuano, and Kapampangan readers can follow the picture while the surrounding guide text carries the translation. If localized image variants are wanted later, only figures 03, 05, 08, and 12 need relabeling; their label lists are short by design.

---

## Part 2 · Image inventory and placement

● = produce first (core teaching) · ○ = second wave (enrichment)

| # | Stem (`strengthening-kidney-resilience-to-aki-…`) | Section | Audience | Skill · archetype | Teaching job |
|---|---|---|---|---|---|
| 00 ● | `vignette-hero` | Hero | Patients | hero-vignette v3 · still-life | Preparation before illness |
| OG ● | `og` | Share card | Social | infographic · OG card | Recognizable preview |
| 01 ● | `01-backup-pumps` | `#resilience` | Patients | infographic · 2D/3D metaphor | Reserve made visible |
| 02 ● | `02-same-hit-two-kidneys` | `#resilience` | Patients | simple-figure B · comparison | Same illness, different outcome |
| 03 ● | `03-four-habits` | `#resilience` | Patients | simple-figure C · loop | The four habits |
| 04 ○ | `04-what-lowers-reserve` | `#starting-point` | Patients | simple-figure E · icon card | Who should make a plan |
| 05 ● | `05-carry-these-four` | `#starting-point` | Patients | simple-figure C · 4 cards | What to carry |
| 06 ● | `06-two-valves` | `#illness` | Patients | simple-figure D · metaphor | Why sick days and some medicines collide |
| 07 ● | `07-pain-reliever-check` | `#illness` | Patients | simple-figure B · comparison | Which pain relievers to review |
| 08 ● | `08-sick-day-card` | `#illness` | Patients | simple-figure C · 3 moments | How the card is used |
| 09 ● | `09-heat-and-floodwater` | `#illness` | Patients | infographic · 2-panel mixed media | Philippine hazards and what to do |
| 10 ● | `10-surgery-100-people` | `#procedures` | Patients | simple-figure B · icon arrays | Surgery plan benefit as people |
| 11 ○ | `11-contrast-balance` | `#procedures` | Patients | simple-figure D · metaphor | Contrast fear in proportion |
| 12 ● | `12-cause-decides-treatment` | `#hospital` | Patients | simple-figure · radial | Treatment depends on cause |
| 13 ● | `13-three-numbers` | `#recovery` | Patients | simple-figure D · line chart | "Better" is not "back to baseline" |
| 14 ○ | `14-recovery-road` | `#recovery` | Patients | simple-figure C · road | Follow-up milestones |
| 15 ● | `15-reserve-staircase` | `#next-risk` | Patients | simple-figure D · concept chart | Repeated hits add up; habits protect |
| 16 ○ | `16-three-stories` | `#stories` | Patients | infographic · case snapshot | The stories at a glance |
| 17 ● | `17-autoregulation-mechanism` | `#md-framework` | Clinicians | biomedical mechanism | Two-ended pressure defense |
| 18 ○ | `18-susceptibility-sigil` | `#md-framework` | Clinicians | organ-crosstalk sigil | Multiorgan susceptibility |
| 19 ● | `19-detect-escalate` | `#md-escalate` | Clinicians | algorithm Mode C | Detection to cause-directed care |
| 20 ○ | `20-sick-day-plan-fields` | `#md-stewardship` | Clinicians | infographic · reference card | Six fields of a usable plan |
| 21 ● | `21-periop-timeline` | `#md-periop` | Clinicians | simple-figure C · timeline | Before / during / after surgery |
| 22 ● | `22-bigpak2-absolute` | `#md-periop` | Clinicians | simple-figure B · bars | Trial in absolute terms |
| 23 ● | `23-contrast-pathway` | `#md-contrast` | Clinicians | algorithm Mode C | Risk-based contrast prophylaxis |
| 24 ● | `24-aki-akd-ckd-continuum` | `#md-transition` | Clinicians | simple-figure C · timeline | Windows and checkpoints |
| 25 ○ | `25-certainty-ladder` | `#md-ledger` | Clinicians | simple-figure E · ladder | How sure each claim is |

All 25 in-body figures and the hero are already placed in the guide with alt text, plain-language `fig-desc` captions, and abbreviation lists, so each image appears the moment its file lands in `images/`.

---

## Part 3 · Prompts

### 00 · Hero vignette ●

```
FILE NAME: strengthening-kidney-resilience-to-aki-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: overhead top-down
HUMAN VARIATION (vs. previous guide): no people (the previous AKI guide showed a family, nephrologist, and nurse at an ICU bedside, eye level)
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
softly lit wood grain fading to a gentle teal-tinted (#eef6f7) blur, with no objects or shadows inside it.

Bright, airy, soft diffused daylight from the upper left; gentle shadows; calm, reassuring colour grade
harmonizing with clinical teal #1a6b72 and navy #0f1e2e accents (the pill-organizer lids are pale teal).
Soft edge falloff toward a slightly deeper warm neutral at the rim. Full-bleed within the inscribed
circle, no rectangular borders.

Absolutely NO readable text anywhere: the card lines are blank, the monitor screen is dark and blank, the
pill organizer has no day letters, no packaging, no brand names, no title, no logo, no watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting objects, tiny labels, infographic
clutter, cropped circle, cropped objects, edge clipping, objects touching the circular border, anything
inside the title safe zone, baked-in text, titles, captions, logos, watermarks, readable drug names or
packaging, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style,
neon, HDR, over-saturation, hospital equipment, blood, needles.

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a visible white margin; one hero object (the blank card) ~60% of the
circle; four supporting objects; clean title-safe zone upper right; no people; overhead framing; no
readable text anywhere.
```

### OG · Social share card ●

```
FILE NAME: strengthening-kidney-resilience-to-aki-og.png
IMAGE TYPE: OG social card (infographic skill, light base)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
AUDIENCE: social feeds, Messenger and Viber link previews
VISUAL GOAL: A practical prevention guide, legible at thumbnail size.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Social share card, exactly 1200×630 landscape. Off-white (#fafafa) background with a very light teal
(#eef6f7) rounded panel filling the right 45%. Left side, set in Inter: title in bold navy (#0f1e2e), two
lines, large: "Strengthening Kidney" / "Resilience to AKI". Below in clinical teal (#1a6b72), Nunito Sans,
one line: "Protect your kidneys during illness, before procedures, and after an injury." Under it, small
gray text: "Patients & families · clinicians · 4 languages". Right panel: a calm semi-flat 3D
illustration of one teal-outlined kidney resting on a cream index card with blank lines; above it, four
small round badges in a gentle arc — a compass (teal), a shield (green #1f7a4d), a stopwatch (amber
#b8860b), and a seedling (teal) — no text on the badges. Thin teal vertical rule between the halves.
Bottom-left, small navy: "W Rivero, MD · renalcarematters.com". Bottom-right: "© renalcarematters.com" in
small gray at 70% opacity. All text crisp and correctly spelled; every element inside a 40-px safe margin.

NEGATIVE INSTRUCTIONS:
No dark background, no faces, no blood, no clutter, no serif fonts, no gibberish text, no drug names, no
guideline acronyms or journal names; the only mark is the © renalcarematters.com footer. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Exactly 1200 × 630; title legible at 300 px wide; "Resilience" spelled correctly.

ALT TEXT: Strengthening Kidney Resilience to AKI — protect your kidneys during illness, before procedures, and after acute kidney injury, a guide by W Rivero, MD
OG WIDTH: 1200
OG HEIGHT: 630
```

### 01 · Backup pumps: reserve made visible ● (patients, `#resilience`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-01-backup-pumps.png
IMAGE TYPE: Infographic — 2D/3D metaphor, two panels
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families (all literacy levels)
VISUAL GOAL: The kidney has backup capacity that switches on under stress, and that reserve cannot be seen on an ordinary blood test.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Patient education infographic, white (#ffffff) background, all text in Nunito Sans with the title in
Inter. Title at top center in bold navy (#0f1e2e): "Your kidneys have backup pumps". Two side-by-side
panels on soft gray (#f3f4f6) rounded cards.
Left panel heading in teal (#1a6b72): "An ordinary day". A clean semi-flat 3D village water station: a
row of six small teal pumps, only two running (soft blue water flowing from them), four resting with
little "off" switches. A small kidney icon in the corner of the panel. Caption under the panel: "Only
some pumps are working."
Right panel heading in amber (#b8860b): "A stress day — fever, diarrhea, heat, surgery". The same station
with a small amber lightning bolt above it; now five pumps running, water still flowing steadily.
Caption: "Backups switch on to keep things steady."
Below both panels, a full-width soft teal (#eef6f7) strip with a small lab-slip icon and navy text: "A
normal blood test shows the water is flowing today — not how many backups are left." At the far right of
the strip, a tiny line in gray: "Real kidneys: the 'pumps' are nephrons, tiny filters."
Ample whitespace, mobile-readable labels at least 11 pt. Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, faces, clutter, tiny labels, AI gibberish text, HDR, excessive saturation. NEVER dark
backgrounds. Use ONLY Nunito Sans and Inter. No numbers, no medical acronyms. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Two panels, same station drawn identically; 2 pumps running on the left, 5 on the right; captions exact;
light background; attribution bottom-right.
```

### 02 · Same hit, two kidneys ● (patients, `#resilience`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-02-same-hit-two-kidneys.png
IMAGE TYPE: Simple-figure Scaffold B — side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: The same illness can pass harmlessly in one person and injure the kidney in another; the difference is the starting reserve.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Medical education comparison infographic, white (#ffffff) background, text in Manrope with title in Inter.
Title at top center in bold navy (#0f1e2e): "Same illness, different kidneys". Under the title, one amber
(#b8860b) lightning bolt centered with the label "2 days of diarrhea", and two thin arrows splitting left
and right. Soft dashed vertical divider creating two equal panels.
Left panel, heading in renal green (#1f7a4d): "Plenty of reserve". A simple semi-flat illustration of a
Filipino woman in her thirties in a casual blouse, resting on a sofa with a glass of water; beside her a
kidney icon with a vertical reserve gauge mostly full and green. Below: a green check mark and the label
"Kidneys cope and recover".
Right panel, heading in amber: "Less reserve". A Filipino man in his seventies with gray hair and
reading glasses, seated with a blanket; beside him a kidney icon whose reserve gauge is low and amber,
and a small stack of three medicine bottles with no labels. Below: an amber exclamation and the label
"Higher chance of kidney injury". Under that, a small green action pill: "A plan made before illness
helps".
Footer strip in soft gray (#f3f4f6), navy text: "Things that lower reserve: older age, kidney disease, a
past kidney injury, heart failure, diabetes, many medicines." Tiny gray note at the right of the strip:
"Reserve gauge is a concept, not a test." Bottom-right: "© renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
No distressed faces, no hospital scene, no readable medicine labels, no numbers, no percentages, no
cartoon style, no clutter, no gibberish. NEVER dark backgrounds. Use ONLY Manrope and Inter. Never omit
the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
One shared "hit" at top; two clearly different people (age, sex, setting); gauge full-green versus
low-amber; the concept note is present; light background; attribution bottom-right.
```

### 03 · Four habits ● (patients, `#resilience`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-03-four-habits.png
IMAGE TYPE: Simple-figure Scaffold C — circular four-step loop
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients
VISUAL GOAL: Four everyday habits surround and protect the kidney.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clean clinical education infographic, white (#ffffff) background, set in Manrope with titles in Inter.
Title at top center in bold navy (#0f1e2e): "Four habits for a more resilient kidney". In the center, one
soft bean-shaped kidney with a teal (#1a6b72) outline and light teal (#eef6f7) fill. Around it, four
rounded cards at 12, 3, 6, and 9 o'clock, joined by a thin teal clockwise circular arrow.
Card 1 (top, teal accent band, compass icon): "Know your starting point" — "Usual creatinine · medicine
list". Card 2 (right, green #1f7a4d band, shield icon): "Avoid the avoidable hits" — "Sick-day plan ·
careful pain relievers · heat and floodwater". Card 3 (bottom, amber #b8860b band, stopwatch icon): "Act
early" — "Same-day check when ill · plan before surgery". Card 4 (left, teal band, seedling icon): "Finish
the recovery" — "Follow-up tests · review at about 3 months". Small amber lightning bolts outside the
circle, deflected by the cards. Generous whitespace; labels at least 11 pt. Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, gibberish text, HDR. NEVER dark backgrounds. Use ONLY Inter and
Manrope. No drug names, no numbers other than "3", no acronyms. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Four cards, one kidney, one clockwise loop; icons match the shared vocabulary; labels exact; light
background; attribution bottom-right.
```

### 04 · What lowers reserve ○ (patients, `#starting-point`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-04-what-lowers-reserve.png
IMAGE TYPE: Simple-figure Scaffold E — icon reference card
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients
VISUAL GOAL: A quick self-check — if any of these apply, ask your doctor for a written plan.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clinical reference card, white (#ffffff) background, text in Nunito Sans with title in Inter. Bold navy
(#0f1e2e) title: "Ask for a kidney plan if you have…". A 3×3 grid of soft gray (#f3f4f6) rounded tiles,
each with one simple teal line icon and a 1–4 word navy label: kidney with a small crack line — "Kidney
disease"; kidney with a small circular arrow — "Past kidney injury"; heart — "Heart failure"; liver —
"Liver cirrhosis"; blood-sugar meter with a blank screen — "Diabetes"; walking cane — "Age over 65";
three small pill bottles without labels — "Many daily medicines"; tiny newborn foot — "Born very small or
early"; urine cup with a small droplet — "Protein in the urine". Footer in teal: "Having one does not mean
injury will happen. It means a plan is worth making." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No faces, no readable labels on bottles or meters, no numbers except "65", no cartoon style, no clutter,
no gibberish. NEVER dark backgrounds. Use ONLY Nunito Sans and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Nine tiles, nine labels spelled exactly; icons simple and consistent line weight; footer present; light
background; attribution bottom-right.
```

### 05 · Carry these four ● (patients, `#starting-point`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-05-carry-these-four.png
IMAGE TYPE: Simple-figure Scaffold C — four-card row
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and caregivers
VISUAL GOAL: Four things to keep with you so any doctor can judge your kidneys quickly.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clean clinical education infographic, white (#ffffff) background, text in Manrope with title in Inter.
Title at top center in bold navy (#0f1e2e): "Keep these four with you". Four rounded cards in one
horizontal row on a soft gray (#f3f4f6) panel, each with a teal (#1a6b72) top accent band and a compass
icon in the band corner.
Card 1: a smartphone showing a photo of a lab slip (the slip's text blurred, only a large navy number
area visible as a blur) — label "Your usual creatinine" — sub-label "with the date".
Card 2: a folded paper list beside two plain blister packs and a small herbal-tea sachet with no
printing — label "Every medicine" — sub-label "including vitamins and herbal products".
Card 3: a cream card with a small kidney icon and a calendar mark — label "Your kidney history" — sub-label
"past injury, kidney stage".
Card 4: a phone contact icon with a stethoscope — label "Who to call" — sub-label "where family can find
it".
Bottom strip, full width, light teal (#eef6f7), navy text: "Bring these to every clinic visit, emergency
room, and surgery appointment." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No readable lab values, drug names, or packaging text; no faces; no cartoon style; no gibberish. NEVER dark
backgrounds. Use ONLY Manrope and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Four cards in order; labels exact; no readable medical specifics; light background; attribution
bottom-right.
```

### 06 · Two valves: why sick days and some medicines collide ● (patients, `#illness`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-06-two-valves.png
IMAGE TYPE: Simple-figure Scaffold D — single-mechanism metaphor
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: The kidney filter keeps its pressure with an inflow valve and an outflow valve; dehydration plus certain medicines can loosen both at once.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Medical education infographic, white (#ffffff) background, text in Nunito Sans with title in Inter.
Title at top in bold navy (#0f1e2e): "Why a sick day can strain the kidney"; subtitle in teal (#1a6b72):
"The filter keeps its pressure with two valves".
Center: a clean semi-flat illustration of a horizontal garden-hose-like pipe running left to right
through a round mesh filter (the filter drawn as a small teal sphere with a fine mesh). On the left pipe,
an "IN valve" drawn as a round green (#1f7a4d) valve wheel, wide open, labeled "Inflow kept open by the
body's own helpers". On the right pipe, an "OUT valve" drawn as a green valve wheel, partly tightened,
labeled "Outflow tightened to hold pressure". A small pressure dial above the filter reads in a green
zone (no numbers).
Below, three amber (#b8860b) cards with thin amber arrows pointing to what they affect:
"Dehydration and water pills" → arrow to the incoming water ("less water in the pipe");
"Pain relievers like ibuprofen or mefenamic acid" → arrow to the IN valve ("narrow the inflow");
"Some blood-pressure medicines (ACE inhibitors, ARBs)" → arrow to the OUT valve ("loosen the outflow").
Bottom strip in soft gray (#f3f4f6), navy text: "These medicines protect the heart and kidneys on normal
days. On a dehydrated day, follow the plan your own doctor wrote." Tiny gray note at the right: "Real
kidney: the filter is the glomerulus; the valves are small arteries." Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No brand names, no doses, no numbers on the dial, no anatomy realism, no cartoon faces, no clutter, no
gibberish. NEVER dark backgrounds. Use ONLY Nunito Sans and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
One pipe, one filter, two valves; three amber cards pointing to the correct part (water, IN valve, OUT
valve); reassurance strip present; light background; attribution bottom-right.
```

### 07 · Pain reliever check ● (patients, `#illness`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-07-pain-reliever-check.png
IMAGE TYPE: Simple-figure Scaffold B — side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (Philippine over-the-counter context)
VISUAL GOAL: Which common pain relievers to review with a doctor, and what is usually the kidney-safer first choice.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Medical education comparison infographic, white (#ffffff) background, text in Manrope with title in
Inter. Title in bold navy (#0f1e2e): "Pain relievers: check before you take". Soft dashed vertical divider,
two panels.
Left panel (wider, 60%), heading in amber (#b8860b) with an exclamation triangle: "Review with your
doctor — can strain the kidneys". Five plain unbranded tablet and capsule illustrations in a neat row,
each with a generic-name label below: "Ibuprofen", "Naproxen", "Mefenamic acid", "Diclofenac",
"Celecoxib". Below them, a sixth item: a plain cold-and-flu sachet with no printing, labeled "Cold and
flu mixes that contain these". A small note in navy: "Often bought for toothache, menstrual cramps, body
pain."
Right panel (40%), heading in renal green (#1f7a4d) with a check mark: "Usually kidney-safer first
choice". One plain white tablet labeled "Paracetamol", with a sub-label "at the label dose — ask what is
right for you, especially with liver disease".
Bottom strip, soft teal (#eef6f7), navy text with a small shopping-bag icon: "Bring every packet,
supplement, and herbal product to your visit." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No brand names, no packaging text, no doses or milligrams, no red "forbidden" symbols, no cartoon style,
no gibberish. NEVER dark backgrounds. Use ONLY Manrope and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Generic names spelled exactly; no brands; paracetamol caveat present; light background; attribution
bottom-right.
```

### 08 · The sick-day card in three moments ● (patients, `#illness`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-08-sick-day-card.png
IMAGE TYPE: Simple-figure Scaffold C — horizontal three-step sequence
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients
VISUAL GOAL: The card is written before illness, followed during illness, and closed by the team at restart.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clean clinical education infographic, white (#ffffff) background, text in Nunito Sans with titles in
Inter. Title at top center in bold navy (#0f1e2e): "Your sick-day card — three moments". Three rounded
cards in one horizontal row on a very soft gray panel (#f3f4f6), joined by bold navy right-pointing
arrows.
Card 1 (teal #1a6b72 band, compass icon): two pairs of hands — a doctor's in a white sleeve and a
patient's — filling in a cream index card with blank lines. Label: "Before you get sick". Bullets: "Fill
it in with your doctor" · "Say the plan back".
Card 2 (amber #b8860b band, stopwatch icon): the same cream card held next to a phone and a glass of
water; a small thermometer. Label: "When you get sick". Bullets: "Follow your card" · "Call early".
Card 3 (green #1f7a4d band, seedling icon): the cream card with a small green check mark and a wall
calendar with one day circled in teal. Label: "When you recover". Bullets: "Your team says when to
restart" · "Blood test on the planned date".
Bottom strip, full width, soft gray, navy text: "Your card records your own team's instructions — it is
not a list everyone should stop." Bottom-right: "© renalcarematters.com" in small semi-transparent navy
text.

NEGATIVE INSTRUCTIONS:
No readable drug names, doses, or fluid amounts on any card; hands only, no faces; no hospital beds; no
cartoon style, clutter, gibberish, HDR. NEVER dark backgrounds. Use ONLY Nunito Sans and Inter. Never omit
the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Exactly three cards, left-to-right arrows, labels exact, cards blank of medical specifics, light
background, attribution bottom-right.
```

### 09 · Heat and floodwater ● (patients, `#illness`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-09-heat-and-floodwater.png
IMAGE TYPE: Infographic — two-panel mixed media (photoreal scene + 2D action cards)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families in the Philippines
VISUAL GOAL: Two local hazards, their warning signs, and the one action for each.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Patient education infographic, landscape 16:9, white (#ffffff) background, text in Nunito Sans with
title in Inter. Title at top center in bold navy (#0f1e2e): "Two Philippine kidney hazards". Two equal
rounded panels.
Left panel, amber (#b8860b) heading with a sun icon: "Hot season (March–May)". Top half: a bright,
photorealistic editorial photo of a Filipino market vendor in her fifties, short curly hair, wide-brim
hat, wiping sweat under a canvas awning beside a stall of calamansi and vegetables, a reusable water
bottle in hand. Bottom half, three small 2D icon rows in navy: "Dizzy", "Stopped sweating", "Very little
dark urine". Green (#1f7a4d) action pill: "Rest in shade · call your team early".
Right panel, teal (#1a6b72) heading with a wave icon: "After floods". Top half: a calm photorealistic
photo of a Filipino teenage boy in a gray T-shirt and rubber boots stepping out of knee-deep brown
floodwater onto a dry concrete street after a typhoon, overcast but bright sky. Bottom half, four small
icon rows: "Fever", "Calf muscle pain", "Red eyes", "Less urine". Note in navy: "within about 2 weeks".
Green action pill: "Get seen and say: I waded in floodwater".
Footer strip in soft gray: "If you have a fluid limit or heart failure, ask for a hot-weather version of
your plan." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No dramatic disaster imagery, no injuries, no rescue scenes, no distressed faces, no dark storm skies,
no readable signs or brands, no numbers other than "2", no cartoon style, no gibberish. NEVER dark
backgrounds. Use ONLY Nunito Sans and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Two different people (adult woman vendor; teenage boy); warning-sign labels exact; action pills present;
calm tone; light background; attribution bottom-right.
```

### 10 · Surgery plan: 100 people ● (patients, `#procedures`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-10-surgery-100-people.png
IMAGE TYPE: Simple-figure Scaffold B — paired icon arrays
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families (numeracy-friendly)
VISUAL GOAL: Show the kidney-protection plan's benefit as people, not percentages.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Medical education comparison infographic, white (#ffffff) background, text in Manrope with title in
Inter. Title in bold navy (#0f1e2e): "A kidney-protection plan for major surgery". Subtitle in teal
(#1a6b72): "Out of every 100 high-risk adults, how many had moderate or severe kidney injury in the first 3
days?" Two side-by-side 10×10 grids of simple person icons (100 icons each), separated by a soft dashed
divider.
Left grid labeled "Usual care": 22 icons filled amber (#b8860b), 78 icons light gray. Big navy label
under it: "about 22".
Right grid labeled "With a kidney-protection plan": 14 icons filled amber, 86 light gray. Big navy label:
"about 14".
Between the grids, a green (#1f7a4d) rounded badge: "about 8 fewer in every 100".
Bottom strip in soft gray, navy text, with four tiny icons (blood-pressure cuff, water drop, crossed-out
pill, glucose meter): "The plan: careful blood pressure and fluids · avoid kidney-straining medicines ·
control blood sugar". Small gray note: "Selected high-risk adults in one 2025 trial." Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Icon counts must be exact (22 and 14 amber); no percentages, odds ratios, or other numbers; no trial
name; no faces on icons; no cartoon style; no gibberish. NEVER dark backgrounds. Use ONLY Manrope and
Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Count the amber icons: 22 left, 14 right; both grids 10×10; badge reads "about 8 fewer in every 100";
light background; attribution bottom-right.
```

### 11 · Contrast in proportion ○ (patients, `#procedures`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-11-contrast-balance.png
IMAGE TYPE: Simple-figure Scaffold D — single metaphor
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients
VISUAL GOAL: For a needed scan, the benefit of a timely diagnosis usually outweighs the small contrast risk; the team adds protection when kidney function is very low.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Medical education illustration, white (#ffffff) background, text in Nunito Sans with title in Inter.
Title in bold navy (#0f1e2e): "CT scan dye: keeping the risk in proportion". Center: a clean semi-flat
balance scale. The heavier, lower left pan holds a teal (#1a6b72) magnifying glass over a simple body
outline, labeled "Finding the problem on time". The lighter, higher right pan holds a small amber
(#b8860b) droplet labeled "Small risk from the dye".
Below the scale, two small cards. Amber card: "Risk matters most when kidney function is very low or a
kidney injury is already happening" with a small IV-bag icon and the words "your team may give IV fluid
first". Green (#1f7a4d) card with a stopwatch: "In an emergency, do not delay a needed scan".
Footer in soft gray: "Tell the team about any past kidney injury and your latest creatinine."
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No scanner brand, no needles, no numbers, no eGFR values, no fear imagery, no cartoon style, no gibberish.
NEVER dark backgrounds. Use ONLY Nunito Sans and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Scale clearly tipped toward diagnosis; both cards present; light background; attribution bottom-right.
```

### 12 · The cause decides the treatment ● (patients, `#hospital`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-12-cause-decides-treatment.png
IMAGE TYPE: Simple-figure — radial diagram
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Kidney injury in hospital is treated by finding its cause; more IV fluid is not always the answer.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clean medical education radial infographic, white (#ffffff) background, text in Manrope with title in
Inter. Title at top in bold navy (#0f1e2e): "In hospital, the cause decides the treatment". Center: a teal
(#1a6b72) kidney with a small amber lightning bolt, labeled "Kidney under stress". Five rounded cards
around it, each joined to the center by a thin navy line, each showing CAUSE in bold and FIX below:
1. Water-drop icon — "Too little fluid" → "Fluids".
2. Germ icon — "Infection" → "Treat the infection · support circulation".
3. Pill icon — "A medicine" → "Stop or change it".
4. Bladder icon with a small block — "Blocked urine flow" → "Relieve the blockage".
5. Magnifier over kidney — "Inflammation inside the kidney" → "Specialist tests".
At the bottom, an amber caution strip with a lungs icon: "Too much fluid can flood the lungs — fluids
help only when the body is truly low." Bottom-right: "© renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
No drug names, no procedures shown graphically, no catheters inserted, no numbers, no cartoon style, no
gibberish. NEVER dark backgrounds. Use ONLY Manrope and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Five cause→fix cards around one kidney; caution strip present; labels exact; light background;
attribution bottom-right.
```

### 13 · Three numbers to leave with ● (patients, `#recovery` and `#stories`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-13-three-numbers.png
IMAGE TYPE: Simple-figure Scaffold D — annotated line chart
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (uses the guide's synthetic example)
VISUAL GOAL: "Better" is not "back to baseline": discharge creatinine can still be above usual.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Patient education chart, white (#ffffff) background, text in Inter. Title in bold navy (#0f1e2e):
"Leave the hospital with three numbers". Subtitle in teal (#1a6b72): "Example — not a real patient".
A clean line chart, y-axis "Creatinine (mg/dL)" from 0 to 2.5 with light gridlines, x-axis with four
labeled points: "Usual", "Highest", "Going home", "Next checks".
Points: "Usual" at 1.00 (teal dot, label "1.00 usual"); "Highest" at 2.10 (amber dot, label "2.10
highest"); "Going home" at 1.40 (navy dot, label "1.40 going home"). A thin teal dashed horizontal line at
1.00 across the chart labeled "your usual level". A bracket between 1.00 and 1.40 at "Going home" labeled
"still 40% above usual". From "Going home" a dashed gray line continues to "Next checks" with two small
calendar icons: "blood test in about 2 weeks" and "3-month review".
Right-side panel, soft gray card with three lab-slip icons and labels: "Usual · Highest · Latest — with
dates". Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Plot exactly 1.00, 2.10, and 1.40 at the correct heights; draw no value at "Next checks"; no other
numbers; no stage labels; no cartoon style; no gibberish. NEVER dark backgrounds. Use ONLY Inter. Never
omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Three values at correct heights on a 0–2.5 axis; "40% above usual" bracket; no invented future value;
light background; attribution bottom-right.
```

### 14 · The recovery road ○ (patients, `#recovery`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-14-recovery-road.png
IMAGE TYPE: Simple-figure Scaffold C — road with milestones
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Recovery has milestones after discharge; keep every appointment even when you feel well.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clean clinical education infographic, white (#ffffff) background, text in Nunito Sans with title in
Inter. Title in bold navy (#0f1e2e): "The road after a kidney injury". A gently curving semi-flat road
from lower left to upper right on a soft teal (#eef6f7) landscape with low hills. Four milestone signposts
along the road, each with an icon and a short label:
1. Hospital door icon — "Before going home: three numbers, the cause, a medicine list".
2. Lab-tube icon — "First weeks: blood tests and medicine review (often 1–2 weeks to 1 month)".
3. Calendar with a circled day — "About 3 months: kidney function and urine albumin".
4. Seedling icon — "Every year: blood pressure, sugar, kidney tests".
A small walking figure of a Filipino woman in her forties with a backpack is at milestone 2, seen from
behind. Footer strip in soft gray: "Feeling well does not mean you can skip the checks." Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No other numbers; no hospital interior; no cartoon style; no gibberish. NEVER dark backgrounds. Use ONLY
Nunito Sans and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Four signposts in order; timing labels exact; light background; attribution bottom-right.
```

### 15 · The reserve staircase ● (patients, `#next-risk`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-15-reserve-staircase.png
IMAGE TYPE: Simple-figure Scaffold D — concept chart (no axis values)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Repeated kidney injuries can add up over the years; protective habits keep the line higher.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Patient education concept chart, white (#ffffff) background, text in Manrope with title in Inter. Title
in bold navy (#0f1e2e): "Each injury can leave a step down". Subtitle in teal (#1a6b72): "Concept drawing —
not anyone's real numbers".
Horizontal axis labeled only "Years", vertical axis labeled only "Kidney reserve" (no numbers). Two lines
start at the same high point on the left.
Amber (#b8860b) line: three sudden dips, each marked with a small amber lightning bolt labeled
"illness", "surgery", "dehydration"; after each dip the line recovers only part of the way, forming a
descending staircase that ends in a light purple (#6c3d8e) zone labeled "long-term kidney disease".
Green (#1f7a4d) line: the same three bolts but each blocked by a small shield; dips are shallow and the
line recovers nearly fully, staying high. Label at its end: "Fewer and smaller hits".
Under the chart, four small habit icons in a row (compass, shield, stopwatch, seedling) with the caption
"The four habits keep the green line". Bottom-right: "© renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
No axis numbers, no percentages, no stage labels, no medical acronyms, no cartoon style, no gibberish.
NEVER dark backgrounds. Use ONLY Manrope and Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Two lines from one starting point; amber staircase versus green near-flat line; "concept drawing" note
present; light background; attribution bottom-right.
```

### 16 · Three stories at a glance ○ (patients, `#stories`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-16-three-stories.png
IMAGE TYPE: Infographic — case snapshot, three cards
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Summarize the three made-up stories so readers remember the action in each.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Case snapshot infographic, white (#ffffff) background, text in Nunito Sans with title in Inter. Title in
bold navy (#0f1e2e): "Three stories, three right moves". Subtitle in gray: "Made-up examples". Three
rounded cards in a row, each with a small semi-flat portrait illustration at the top, a bold navy
heading, one green (#1f7a4d) action pill, and one icon.
Card 1: illustration of a Filipino man in his late sixties with a gray mustache, in a polo shirt, seated
with a basin nearby while his adult daughter makes a phone call. Heading "Sick at home". Green pill:
"Call the clinic the same day — bring the medicine bag and card". Icon: phone.
Card 2: illustration of a Filipino woman in her early sixties with a short bob haircut, holding a folder
at a pre-surgery desk. Heading "Before a hip operation". Green pill: "Ask who manages medicines and who
checks kidney tests after". Icon: clipboard.
Card 3: illustration of a Filipino man in his thirties with an undercut hairstyle and a backpack, walking
out of a hospital door holding a small card. Heading "Going home". Green pill: "Three numbers written
down: 1.00 · 2.10 · 1.40". Icon: calendar with a circled day.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No readable drug names, no hospital beds, no distress, no numbers other than 1.00, 2.10, 1.40; no cartoon
exaggeration; no gibberish. NEVER dark backgrounds. Use ONLY Nunito Sans and Inter. Never omit the
attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Three distinct people (different ages, sexes, hairstyles); action pills exact; light background;
attribution bottom-right.
```

### 17 · Two-ended defense of filtration pressure ● (clinicians, `#md-framework`) — biomedical mechanism

```
FILE NAME: strengthening-kidney-resilience-to-aki-17-autoregulation-mechanism.png
IMAGE TYPE: Biomedical mechanism schematic (organ → magnified inset → injury / intervention / benefit)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Glomerular pressure is defended at the afferent and efferent arterioles; volume depletion plus common drugs removes both defenses.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Create a publication-grade biomedical mechanism schematic. Topic: autoregulation of glomerular
filtration pressure and its failure during volume depletion. Disease context: acute kidney injury risk on
sick days. White background, flat vector with soft semi-3D shading, muted clinical palette, thin dashed
connector lines, review-article figure style. All labels in IBM Plex Sans.

Organ-level panel (left, about 25% width): a simplified kidney cross-section in light gray-blue with the
renal artery in red and renal vein in blue; label "Kidney during volume depletion". A small dashed square
on the cortex connects by a dashed line to the magnified panel.

Magnified mechanism panel (center-right, dashed border): one glomerulus inside Bowman's capsule, with the
afferent and efferent arterioles entering and leaving at the SAME vascular pole, splayed apart for
clarity; the efferent narrower than the afferent; the macula densa in soft yellow where the distal tubule
touches the pole. Callouts:
- Afferent arteriole: "Prostaglandins → dilation (blue protective arrow)"; "Myogenic tone".
- Efferent arteriole: "Angiotensin II → constriction (blue protective arrow)".
- Macula densa: "Tubuloglomerular feedback".
- Glomerular tuft: "Filtration pressure maintained → GFR".
Overlay four small red "removal" markers with thin red arrows: "Volume depletion / diuretics → ↓ renal
perfusion" (to the renal artery), "NSAID → ↓ afferent prostaglandins" (to afferent; its blue arrow
crossed out), "ACEi / ARB → ↓ efferent tone" (to efferent; its blue arrow crossed out). A small teal note
at the macula densa: "SGLT2 inhibitor → restores feedback, ↓ intraglomerular pressure (protective
long-term; expected early eGFR dip)".

Bottom summary flow, three boxes with arrows:
Left pale pink box (pathology drivers): "Volume depletion · sepsis · hypotension · NSAID + diuretic +
ACEi/ARB"
Center box (mechanistic bridge): "Loss of afferent dilation and efferent support → narrowed autoregulatory
margin"
Right pale blue box (protective response): "Individualized sick-day plan · avoid NSAIDs · restore volume
when depleted · planned restart with labs"

Avoid photorealism, dark backgrounds, decorative elements, overcrowding. Include small semi-transparent
navy "© renalcarematters.com" in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Do not place afferent and efferent arterioles at opposite poles; no numbers or thresholds; no drug brand
names; no gibberish; NEVER dark backgrounds. Use ONLY IBM Plex Sans. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Correct vascular-pole anatomy; efferent narrower; two blue defenses with the correct ones crossed out;
SGLT2 note present and framed as protective; bottom flow injury → bridge → response; attribution
bottom-right.
```

### 18 · Multiorgan susceptibility sigil ○ (clinicians, `#md-framework`) — organ-crosstalk sigil

```
FILE NAME: strengthening-kidney-resilience-to-aki-18-susceptibility-sigil.png
IMAGE TYPE: Organ-crosstalk sigil
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians (also calm enough for patients)
VISUAL GOAL: Kidney susceptibility is shaped by the heart, liver, and gut and by the environment; stresses flow in and congestion flows back.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Create a simple medical organ-crosstalk sigil illustration featuring the two kidneys at the center, the
heart at the top, the liver at the lower left, and the intestine at the lower right.

Show kidney susceptibility as dotted curved arrows flowing from each organ toward the kidneys
(low cardiac output from the heart; vasodilation and portal hypertension from the liver; fluid and salt
loss from the gut), and one returning dotted arrow from the kidneys back up to the heart representing
congestion and fluid overload, forming a calm loop. Outside the triangle, two tiny monoline symbols at
the edge of the composition: a small sun (heat) at upper right and a small wave (floodwater infection) at
upper left, each with a single short dotted arrow pointing toward the kidneys.

Render the organs as soft semi-3D anatomical illustrations (red-brown kidneys, red heart, brown liver, pink intestine) with
dotted teal arrows on a white background, balanced radial composition, generous whitespace. Small labels only, set in Inter, in slate gray: "heart",
"liver", "gut", "kidneys", "heat", "floodwater". No other text. Include a small semi-transparent
"© renalcarematters.com" attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, extra labels, dark background, neon colors, crowded arrows,
thick cartoon outlines, 3D rendering, glossy icons. Only Inter for the six labels. Never omit the
attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Four organs in a balanced triangle around the kidneys; one return arrow to the heart; two environmental
symbols; six labels exact; white background; attribution bottom-right.
```

### 19 · Detect and escalate ● (clinicians, `#md-escalate`) — algorithm Mode C

```
FILE NAME: strengthening-kidney-resilience-to-aki-19-detect-escalate.png
IMAGE TYPE: Clinical algorithm — renalcarematters.com house style (Mode C)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: From a creatinine or urine-output change to escalation, staging, and cause-directed care in parallel.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style.
White background, restrained navy and teal typography set in Inter, thin teal connector arrows, generous
margins, centered layout.

Color conventions: navy #0f1e2e for title and text; teal #1a6b72 for decision diamonds and arrows; green
#1f7a4d for recommended actions; amber #b8860b for caution nodes; red #b91c1c for escalation nodes; soft
gray for side notes.

Content to render:
Title: "Suspected AKI: detect, escalate, find the cause". Subtitle: "Adults; published 2012 criteria".
1. Start node (navy outline): "Creatinine rise or low measured urine output".
2. Decision diamond (teal): "Urgent threat?" Right branch labeled "Yes" to a red node: "Escalate now —
sepsis, obstruction, pulmonary edema, refractory potassium or acidosis, uremic complications → senior
review; KRT on clinical indications". Left/down branch labeled "No".
3. Action node (navy): "Compare with a credible baseline". Side note in soft gray: "Stable high creatinine
is not stage 3. A 48-hour pair can diagnose AKI without a baseline."
4. Two parallel green nodes side by side, joined by a bracket labeled "in parallel":
   a. "Stage it — highest supported stage; label 'at least' if data are missing".
   b. "Find the cause — history, examination, medicines, urinalysis, ultrasound".
5. Below the cause node, four small amber nodes in a row: "Volume depleted → fluid", "Congested →
decongest", "Septic → resuscitate and reassess", "Obstructed → decompress".
6. Bottom gray note: "Avoid low-dose dopamine. Loop diuretics only for fluid overload."

Design requirements: top-to-bottom logic, diamonds for decisions, rounded rectangles for actions, no
photorealistic people, no clutter. Include a small professional footer reading "© renalcarematters.com"
positioned at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No numeric thresholds other than those written; no drug doses; no dark background; no spaghetti arrows;
no gibberish. Use ONLY Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
One urgent-threat diamond; staging and cause nodes visibly parallel; four physiologic-state nodes;
footer present; text exact.
```

### 20 · Six fields of a usable sick-day plan ○ (clinicians, `#md-stewardship`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-20-sick-day-plan-fields.png
IMAGE TYPE: Clinician reference card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: A sick-day plan works only when six fields are completed and taught back.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clinical reference infographic card for clinicians, publication-grade nephrology design, white (#ffffff)
background, text in IBM Plex Sans. Bold navy (#0f1e2e) title: "Write a sick-day plan patients can use".
Teal (#1a6b72) subtitle: "Individualized, not generic". A 3×2 grid of soft gray (#f3f4f6) rounded
cards, each with a teal number, a simple line icon, a bold label, and one short line:
1. Calendar-with-thermometer icon — "Define the sick day" — "What illness counts for this patient".
2. Pill-list icon — "Drug-by-drug action" — "Continue, reduce, or hold, by generic name".
3. Play-button icon — "Restart condition" — "Eating and drinking normally, labs as planned".
4. Person-badge icon — "Restart owner" — "Who says when — named role".
5. Lab-tube icon — "Lab date" — "Creatinine and potassium when indicated".
6. Red triangle icon — "Red flags" — "When to go to emergency".
Bottom strip in light teal (#eef6f7) with a speech-bubble icon: "Teach-back: 'Who will tell me when to
restart?' · 'What will I do if I cannot drink?'" A small amber note at the right edge: "Avoid blanket holds
and fixed fluid targets." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No drug names, doses, or fluid volumes; no dark backgrounds; no clutter; no gibberish. Use ONLY IBM Plex
Sans. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Six numbered cards; teach-back strip; amber caution note; light background; attribution bottom-right.
```

### 21 · Perioperative kidney timeline ● (clinicians, `#md-periop`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-21-periop-timeline.png
IMAGE TYPE: Simple-figure Scaffold C — three-phase timeline
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (anesthesia, surgery, medicine)
VISUAL GOAL: Kidney protection is a sequence of actions before, during, and after surgery, each with an owner.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clean clinical education infographic, white (#ffffff) background, text in Inter. Title in bold navy
(#0f1e2e): "Kidney protection around major surgery". Subtitle in teal (#1a6b72): "Clinically high-risk
adults". Three wide rounded columns joined by navy arrows, each with a colored header band and a simple
icon:
Column 1, teal band, clipboard icon — "Before": "Credible baseline creatinine and urine albumin" ·
"Plan for ACE inhibitor/ARB, diuretics, SGLT2 inhibitor (ketosis risk), metformin" · "Non-NSAID pain plan"
· "Name who restarts each drug".
Column 2, amber (#b8860b) band, monitor icon — "During": "Avoid prolonged hypotension" · "Assess volume and
perfusion" · "Avoid nephrotoxins and unnecessary contrast" · "Control glucose".
Column 3, green (#1f7a4d) band, calendar icon — "After": "Daily creatinine for at least 48–72 hours" ·
"Measured urine output" · "Re-dose renally cleared drugs" · "Named weekend reviewer".
Bottom strip in soft gray, navy text: "Trial evidence supports this bundle in selected high-risk patients;
single components are untested." Bottom-right: "© renalcarematters.com" in small semi-transparent navy
text.

NEGATIVE INSTRUCTIONS:
No drug doses, no blood-pressure numbers, no trial or society names, no dark backgrounds, no clutter, no
gibberish. Use ONLY Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Three columns in order; bullets exact; the "48–72 hours" text correct; light background; attribution
bottom-right.
```

### 22 · BigpAK-2 in absolute terms ● (clinicians, `#md-periop`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-22-bigpak2-absolute.png
IMAGE TYPE: Simple-figure Scaffold B — paired bar comparison
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Show the short-term absolute benefit and the absent 90-day difference side by side.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Medical education comparison chart, publication style, white (#ffffff) background, all text in IBM Plex
Sans. Title in bold navy (#0f1e2e): "BigpAK-2: prevention bundle in high-risk major surgery". Subtitle in
teal (#1a6b72): "Selected adults at high risk by clinical factors and urine stress biomarkers".
Two panels separated by a soft dashed vertical divider.
Left panel heading: "Moderate or severe kidney injury within 72 hours". Two vertical bars on a light gray
gridline axis from 0% to 25%: "Usual care" bar in soft gray-navy reaching 22.3%, labeled "22.3%
(131/588)"; "Bundle" bar in teal reaching 14.4%, labeled "14.4% (84/584)". Between the bars, a small green
(#1f7a4d) bracket labeled "about 8 fewer per 100".
Right panel heading: "Major adverse kidney events at 90 days". Two bars on the same 0–25% axis: "Usual
care" 10.6% and "Bundle" 11.0%, both light gray with labels, and a small neutral note "no difference".
Bottom strip in soft gray, navy text: "Bundle = hemodynamic monitoring, volume optimization, avoiding
nephrotoxins and contrast, glucose control." Bottom-right: "© renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Bar heights proportional on a shared 0–25% axis; do not add odds ratios, confidence intervals, p-values,
or other numbers; no journal names; no 3D bars; NEVER dark backgrounds. Use ONLY IBM Plex Sans. Never
omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Four bars with exact values 22.3, 14.4, 10.6, 11.0; denominators 131/588 and 84/584; shared axis; light
background; attribution bottom-right.
```

### 23 · Intravenous contrast pathway ● (clinicians, `#md-contrast`) — algorithm Mode C

```
FILE NAME: strengthening-kidney-resilience-to-aki-23-contrast-pathway.png
IMAGE TYPE: Clinical algorithm — renalcarematters.com house style (Mode C)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: Risk-based intravenous saline prophylaxis for CT contrast, without delaying indicated imaging.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style.
White background, navy and teal typography set in Inter, thin teal connector arrows, generous margins,
centered layout. Colors: navy #0f1e2e text; teal #1a6b72 decision diamonds; green #1f7a4d recommended
actions; amber #b8860b caution; red #b91c1c for the emergency branch; soft gray side notes.

Content to render:
Title: "Intravenous contrast for CT: kidney decisions". Subtitle: "Contrast-associated is not the same as
contrast-induced".
1. Start: "Intravenous contrast CT is indicated".
2. Diamond: "Emergency?" — "Yes" → red node: "Scan without delay; manage kidney risk in parallel".
3. "No" → diamond: "AKI now, or eGFR below 30, and not on maintenance dialysis?" — "Yes" → green node:
"Intravenous normal saline prophylaxis, if volume status permits".
4. "No" → diamond: "eGFR 30–44?" — "Yes" → amber node: "Consider saline only in individual high-risk
circumstances".
5. "No (eGFR 45 or above)" → green node: "No routine prophylaxis".
6. Side gray notes: "Sodium bicarbonate is not better than saline; routine N-acetylcysteine does not
protect." and "Coronary angiography and PCI use separate risk models."
7. Bottom navy note: "Follow local radiology protocol."

Design requirements: top-to-bottom logic, diamonds for decisions, rounded rectangles for actions, no
photorealistic people, no clutter. Include a small professional footer reading "© renalcarematters.com"
positioned at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Only the eGFR thresholds 30, 44, and 45 written above; no fluid volumes or rates; no dark background; no
gibberish. Use ONLY Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Emergency branch first; thresholds exactly <30, 30–44, ≥45; dialysis exclusion present; two side notes;
footer present.
```

### 24 · AKI, AKD, CKD — one continuum ● (clinicians, `#md-transition`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-24-aki-akd-ckd-continuum.png
IMAGE TYPE: Simple-figure Scaffold C — horizontal timeline
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians (also readable by patients)
VISUAL GOAL: Show the time windows and the follow-up checkpoints that catch incomplete recovery.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clean clinical timeline infographic, white (#ffffff) background, labels in Inter. Title in bold navy
(#0f1e2e): "From injury to recovery — one continuum". A single horizontal arrow-shaped timeline divided
into three segments: left amber (#b8860b) "AKI" with "Day 0–7" beneath; middle soft purple (#6c3d8e) "AKD"
with "Day 7–90"; right navy-outlined light gray "CKD" with ">90 days". Above the timeline, three teal
(#1a6b72) checkpoint pins with icons: at the start of the middle segment, a hospital-door icon
"Discharge: baseline, peak, latest creatinine"; within the middle segment, a stethoscope icon "1–2 weeks
to 1 month: labs + medicine review"; at day 90, a calendar icon "About 3 months: creatinine/eGFR + urine
albumin". Below the timeline, a thin green (#1f7a4d) branch curving up and off before the CKD segment
labeled "Recovery". Bottom strip in soft gray, navy text: "Persistence past 90 days meets the time
criterion for CKD; chronicity and context still decide the diagnosis." Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No other numbers or thresholds; no guideline acronyms; no cartoon style; no gibberish. NEVER dark
backgrounds. Use ONLY Inter. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Three segments in order and color; checkpoint labels exact; "eGFR" lowercase e; light background;
attribution bottom-right.
```

### 25 · How certain is each claim? ○ (clinicians, `#md-ledger`)

```
FILE NAME: strengthening-kidney-resilience-to-aki-25-certainty-ladder.png
IMAGE TYPE: Simple-figure Scaffold E — evidence ladder card
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians (and curious patients)
VISUAL GOAL: Place the guide's main claims on a certainty ladder so readers see what is proven, suggested, associated, or unproven.

PROMPT:
STYLE LOCK — match the existing renalcarematters.com guide figures (reference look: the "Dialysis is a bridge, not a cure" and "five domains of recovery" figures): a rich, full-color, semi-3D illustrated infographic like a premium health-magazine explainer. Render organs as realistic 3D anatomy (textured red-brown kidneys with vessels), icons as glossy dimensional illustrations (droplets, pills, organs, people), and any scenery as soft painterly illustration. Very bold, heavy sans-serif headings in near-black navy; large readable labels; full-color rounded panels with solid colored header bands (renal green, amber, teal); thick colored card outlines; soft shadows and depth. This must NOT look like a flat vector diagram, SVG export, wireframe, or thin-stroke line art.

Clinical reference card, white (#ffffff) background, text in IBM Plex Sans. Bold navy (#0f1e2e) title:
"How sure are we?" Subtitle in teal (#1a6b72): "The guide's main claims by strength of evidence". A
vertical ladder of five rungs, top to bottom, each a rounded horizontal card with a colored left band and
a short label on the left and the claims on the right:
Rung 1, teal band — "How the body works": "Two-ended autoregulation of filtration pressure".
Rung 2, green (#1f7a4d) band — "Proven in randomized trials": "SGLT2 inhibitors lower AKI risk" · "Bundle
lowers short-term AKI in selected high-risk surgery" · "Bicarbonate and NAC do not prevent contrast
injury" · "Low-dose dopamine does not protect".
Rung 3, light green band — "Suggested by one large trial": "Amino acids lower AKI after cardiac surgery".
Rung 4, amber (#b8860b) band — "Associated, not proven to cause": "Urine albumin after AKI and later
decline" · "Extreme heat and AKI admissions" · "Born small and later AKI".
Rung 5, gray band — "Not proven / not offered": "Generic sick-day protocols preventing AKI" · "Any
'kidney resilience score'".
A thin navy arrow beside the ladder pointing up, labeled "more certain". Bottom-right:
"© renalcarematters.com" in small semi-transparent navy text (bottom-center acceptable for portrait).

NEGATIVE INSTRUCTIONS:
No numbers, effect sizes, or trial names; no dark backgrounds; no clutter; no gibberish. Use ONLY IBM
Plex Sans. Never omit the attribution. Do NOT produce a flat vector / SVG-style / thin line-art / wireframe diagram; render dimensional, illustrated, full-color artwork.

QUALITY CHECK:
Five rungs in order; claims placed on the correct rungs exactly as written; light background;
attribution visible.
```

---

## Part 4 · Production checklist

1. Generate the ● images first (16 items including hero and OG); the ○ images enrich but are not required for launch.
2. Save each PNG to `images/` with the exact stem and create a `.webp` twin.
3. Run Stage 2 (`williamriveromd-local-image-generator`) to validate and confirm `og:image` (1200 × 630 already declared in the guide head).
4. Spot-check before publishing — these are the renders most likely to go wrong:
   - **10**: count the amber icons (22 and 14).
   - **13**: plotted heights 1.00 / 2.10 / 1.40 on a 0–2.5 axis; no invented future value.
   - **17**: afferent and efferent arterioles at the same vascular pole; efferent narrower.
   - **22**: bar heights proportional; denominators exact.
   - **23**: thresholds <30, 30–44, ≥45 and the dialysis exclusion.
   - **07**: no brand names slipped in.
5. Reject and regenerate any image with gibberish text, a dark background, a serif font, or a missing `© renalcarematters.com` mark.
