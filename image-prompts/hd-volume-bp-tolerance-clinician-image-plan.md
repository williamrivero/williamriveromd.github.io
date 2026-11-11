# Image Plan Blueprint — `hd-volume-bp-tolerance-clinician`

**Guide:** `guides/hd-volume-bp-tolerance-clinician.html`
**Title:** Volume, Blood Pressure & Hemodynamic Tolerance in Maintenance HD — A Clinician's Guide
**Audience:** Clinicians only (nephrologists, fellows, dialysis nurses, renal pharmacists, dietitians)
**Prepared:** 2 November 2026 (Asia/Manila)
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/
**Stage 2 handoff:** `williamriveromd-local-image-generator` (validation, manifests, og:image wiring)

---

## 1. Design brief

### What the images must do
This is a clinician reference whose core message is **"congestion and UF tolerance are two different problems — don't let one number stand in for the other."** Every image should either (a) make a physiologic mechanism visible, (b) turn a review pathway into something scannable on a ward round, or (c) show evidence at its true strength. No image should look like a prescription.

### Rules carried into every prompt
| Rule | Why |
|---|---|
| Light backgrounds only (white / `#fafafa` / `#f3f4f6` / `#eef6f7`) | House style |
| Fonts: **Inter** only in this set (one face across the guide for consistency) | Approved-font rule; visual unity |
| Attribution `renalcarematters.com` (algorithms: `© renalcarematters.com`), bottom-right | House style |
| Palette: navy `#0f1e2e`, teal `#1a6b72`, green `#1f7a4d`, amber `#b8860b`, red `#b91c1c` | House style |
| **Green never means "safe UFR."** Green = recommended review action or reassessment only | Clinical blueprint: no false safety states |
| **No numeric value that is not in the guide.** No dialysate concentrations, drug doses, saline volumes or UFR "limits" | Medical-accuracy rule |
| Every guideline statement shows its issuer and its own grade (UKKA 2B, KDIGO = ungraded consensus) | Teaching standard: never convert grades |
| American English spelling in all on-image text (hemodialysis, hemodiafiltration, edema, center) | CLAUDE.md |
| No people in any image | Clinician reference; avoids decorative photography |

### Skill routing
| Skill | Used for |
|---|---|
| `williamriveromd-hero-vignette` | #00 hero |
| `williamriveromd-infographic-skill` | #00b OG card, #12 tool reference card, #15 symptom cycle, #17 unit review cycle |
| `williamriveromd-biomedical-mechanism-figure` | #04 circulatory-stress mechanism |
| `williamriveromd-organ-crosstalk-sigil-graphic` | #05 multiorgan sigil |
| `williamriveromd-algorithm-generator-skill` | #07 P01, #08 P02 (Mode C house style), #13 incremental HD (Mode B journal) |
| `williamriveromd-simple-figure` | #06, #09, #10, #11, #14, #16 |

---

## 2. Image inventory and placement map

Existing vector figures **01–03 stay as SVG** (they carry dense, exact clinical labels that image generators garble). New raster figures are numbered from **04**.

| # | File name | Skill / archetype | Size | Section (`id`) | Insert after… | Priority |
|---|---|---|---|---|---|---|
| 00 | `…-vignette-hero.png` | Hero vignette · Scaffold C anatomy | 2048×2048 | hero | replaces interim | **P0** |
| 00b | `…-og.png` | OG share card | 1200×630 | `<head>` meta | replaces interim | **P0** |
| 01 | `…-01-compartments.svg` | (existing SVG) | — | `#physiology` | — | done |
| 02 | `…-02-review-matrix.svg` | (existing SVG) | — | `#review-lens` | — | done |
| 03 | `…-03-evidence-ladder.svg` | (existing SVG) | — | `#start-here` | — | done |
| 04 | `…-04-circulatory-stress-mechanism.png` | Biomedical mechanism | 1792×1024 | `#physiology` §4 | "…does not by itself prove that any single intervention improves survival" paragraph | **P0** |
| 05 | `…-05-multiorgan-sigil.png` | Organ-crosstalk sigil | 1024×1024 | `#physiology` §4 | directly after #04 (small, centered, max-width 420px) | P2 |
| 06 | `…-06-bp-measurement-roles.png` | Simple figure · Scaffold E card | 1536×1152 | `#bp-targets` | first paragraph, before the table | **P0** |
| 07 | `…-07-p01-recurrent-idh.png` | Algorithm Mode C | 1024×1536 | `#pathways` | after P01 algo-card | P1 |
| 08 | `…-08-p02-congested-intolerant.png` | Algorithm Mode C | 1024×1536 | `#pathways` | after P02 algo-card | **P0** |
| 09 | `…-09-time-lowers-ufr.png` | Simple figure · Scaffold B comparison | 1792×1024 | `#ufr-time` | first paragraph | **P0** |
| 10 | `…-10-sodium-thirst-cycle.png` | Simple figure · Scaffold C sequence | 1792×1024 | `#sodium` | first paragraph | P1 |
| 11 | `…-11-cooling-policy-vs-patient.png` | Simple figure · Scaffold B comparison | 1792×1024 | `#levers` | "Cooling" paragraph | P1 |
| 12 | `…-12-mra-evidence-timeline.png` | Simple figure · Scaffold E card | 1536×1152 | `#medications` | MRA paragraph | **P0** |
| 13 | `…-13-what-each-tool-sees.png` | Infographic · Clinician reference card | 1536×1152 | `#tools` | before the tool table | P1 |
| 14 | `…-14-incremental-hd-selection.png` | Algorithm Mode B journal | 1024×1536 | `#rkf` | after the study table | P1 |
| 15 | `…-15-convection-vs-net-uf.png` | Simple figure · Scaffold D mechanism | 1792×1024 | `#hdf` | first paragraph | P2 |
| 16 | `…-16-symptom-cycle-map.png` | Infographic · Circular workflow | 1024×1024 | `#symptoms` | end of section | P2 |
| 17 | `…-17-simulation-vs-trial.png` | Simple figure · Scaffold B comparison | 1792×1024 | `#frontier` | adaptive UF paragraph | P2 |
| 18 | `…-18-unit-review-cycle.png` | Infographic · Circular workflow | 1024×1024 | `#implementation` | first paragraph | P2 |

`…` = `hd-volume-bp-tolerance-clinician`. Produce PNG from GPT, then a WebP twin (`convert X.png -quality 82 X.webp`).

**Suggested production order:** P0 (00, 00b, 04, 06, 08, 09, 12) → P1 → P2.

---

## 3. Prompts

Each block is copy-ready for the Image Generator GPT. Paste **only** the text inside the fenced block.

---

### #00 — Circular vignette hero (P0)

```
FILE NAME: hd-volume-bp-tolerance-clinician-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C anatomy
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F — Anatomy
CAMERA: macro cross-section, slightly elevated three-quarter view
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: clinicians
VISUAL GOAL: At a glance, fluid moving from waterlogged tissue back into one blood capillary — the plasma-refill idea behind "congested but hypotensive."

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Anatomy. Camera: macro cross-section, slightly elevated three-quarter view.

Subject: one gently curving blood capillary crossing the lower-middle of the circle from left to right, its wall semi-translucent so a few biconcave red blood cells are visible inside. Below and around the vessel, a soft, slightly swollen interstitial tissue bed of rounded pale-pink cells with glistening fluid between them. Small, clear, teal-tinted fluid droplets drift upward from the tissue spaces through the capillary wall into the bloodstream, suggesting plasma refill. Anatomically plausible proportions, restrained clinical colors (muted renal reds, soft pinks, clinical teal #1a6b72 accents), gentle studio lighting, soft shadows, shallow depth of field.

Visual hierarchy: the capillary and refilling droplets occupy 60–70% of the circle; the tissue bed gives 20–30% supporting context; reserve the upper 20–25% of the circle as a TITLE SAFE ZONE of empty, softly graded very light teal-white background (#eef6f7 fading to off-white) with no anatomy, droplets, leader lines, labels or callouts. Soft falloff toward a slightly deeper neutral at the rim.

Absolutely NO text, labels, arrows with words, leader lines, callouts, titles, logos or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, dozens of icons, tiny labels, infographic clutter, cropped circle, cropped anatomy, edge clipping, objects touching the circular border, content inside the title safe zone, baked-in text, logos, watermarks, rectangular frames, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted anatomy, gore, people.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. One dominant subject (capillary + refill), 2–4 supporting elements, 20–25% empty title-safe zone at the top. No people. No text anywhere.
```

**Alt text (update in HTML):** "Circular vignette hero: a semi-translucent blood capillary crossing above swollen tissue cells, with small teal droplets rising from the tissue into the bloodstream, representing plasma refill during ultrafiltration."

---

### #00b — OG / social share card (P0)

```
FILE NAME: hd-volume-bp-tolerance-clinician-og.png
IMAGE TYPE: OG social share card (editorial, typographic + anatomy disc)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: clinicians
VISUAL GOAL: A calm, premium share card that reads "volume vs tolerance in hemodialysis — clinician guide" at thumbnail size.

PROMPT:
Clean 1200×630 social share card on a pure white (#ffffff) background, all typography in Inter. A thin navy (#1f3864) vertical accent bar runs down the far-left edge. Left 58% of the card: a small uppercase teal (#1a6b72) kicker "CLINICIAN GUIDE · MAINTENANCE HD"; below it a large bold navy (#0f1e2e) title on three lines — "Volume, Blood Pressure &" — then, in teal (#1a6b72), "Hemodynamic Tolerance"; below the title one line of navy body text: "Congested, hypotensive — or both?". Right 42%: a circular disc, fully inside the card with comfortable margin, containing a semi-photorealistic render of a blood capillary crossing above pale-pink tissue cells with small teal droplets rising into the vessel, on a very light teal (#eef6f7) background with a soft shadow. Generous whitespace, no other icons or graphics. "renalcarematters.com" in small navy text at 70% opacity in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, stock-photo look, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter — no serif, decorative or handwritten typefaces. Spell every word exactly as given (American English: "Hemodynamic"). Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200 × 630. White background. Title legible at thumbnail size. Disc not cropped. Attribution visible bottom-right.
```

**After generating:** replace `images/…-og.png/.webp`, then `python3 generate_rg_thumbs.py --guide hd-volume-bp-tolerance-clinician.html --force` and `python3 generate_latest_guides.py`.

---

### #04 — HD-induced circulatory stress mechanism (P0)

```
FILE NAME: hd-volume-bp-tolerance-clinician-04-circulatory-stress-mechanism.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show how ultrafiltration that outpaces plasma refill becomes intradialytic hypotension and organ hypoperfusion, and which levers act on each step.

PROMPT:
Create a publication-grade biomedical mechanism schematic in scientific review-article style on a pure white background. Flat vector illustration with soft semi-3D shading, thin dashed boxes for magnified panels, muted clinical palette, and clean sans-serif labels set in Inter. Title at top-left in bold navy (#0f1e2e): "When UF outpaces refill: HD-associated circulatory stress".

Topic: hemodialysis-associated circulatory stress. Disease context: adults on maintenance hemodialysis. Central mechanism: ultrafiltration removes water only from plasma; when the UF rate exceeds plasma refill from the interstitium, circulating volume and cardiac filling fall, and blood pressure depends on cardiac reserve and vascular compensation.

Organ-level panel (left third): a simplified torso outline in light gray-blue showing the heart, major vessels, and a hemodialysis circuit leaving and returning to the arm. Label the patient "Maintenance HD." A small dashed connector box points from a capillary bed in the forearm to the magnified panel.

Magnified mechanism panel (center, inside a dashed rounded border): a single capillary with surrounding interstitial tissue. Blue arrows labeled "Plasma refill" move from the tissue into the capillary; a red arrow labeled "UF rate" leaves the capillary toward a small dialyzer icon. Three concise callouts:
- "UF rate > refill → ↓ plasma volume"
- "↓ venous return → ↓ cardiac filling"
- "Stiff, hypertrophied LV: small ↓ filling → large ↓ stroke volume"
A thin side callout in gray: "Refill depends on: interstitial excess, albumin, capillary permeability, time."

Right panel (smaller, dashed box): four small simplified organ icons — heart, brain, gut, kidney — each with a small red downward arrow and the label "↓ perfusion". Caption under them in gray italics: "Proposed mechanism; outcome benefit of specific fixes not proven by this pathway."

Bottom summary flow (three boxes connected left → right by arrows):
Left pale-pink pathology box: "High UF rate (short time, high IDWG) · Warm dialysate → venous pooling · LVH / diastolic stiffness · Autonomic dysfunction · Drugs, arrhythmia, infection" — final bold line "Intradialytic hypotension".
Center neutral box: "Mechanistic bridge: plasma volume falls faster than tissue refills".
Right pale-blue box titled "Levers to review (not a sequence)": "Longer or more frequent sessions · Lower IDWG via sodium · Cooler dialysate in selected patients · BP-drug timing review" — small gray footnote "Evidence strength differs by lever — see guide."

Use a white background, muted clinical colors (light gray-blue anatomy, red for injury, blue for refill/protective effects, pale pink pathology box, pale blue lever box), thin dashed connector lines. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, gibberish text, invented numeric thresholds (no UF-rate numbers, no BP cutoffs, no temperatures), any word "safe," cartoon styling, heavy shadows. Use ONLY Inter — no serif fonts. Draw the dialyzer only as a small simple cylinder icon (no ports required). Never omit the attribution.

QUALITY CHECK:
1792×1024, white background, three-panel top + three-box bottom flow, all labels legible at slide size, no numbers anywhere on the image, attribution visible bottom-right.
```

**fig-desc:** "Fluid removal drains the blood faster than the tissues can refill it. When that happens, the heart fills less, and a stiff heart pumps much less, so blood pressure and blood flow to the heart, brain, gut and kidneys can fall. The bottom row shows the main drivers and the levers worth reviewing."
**fig-abbrevs:** HD — Hemodialysis · UF — Ultrafiltration · IDWG — Interdialytic weight gain · LV — Left ventricle · LVH — Left ventricular hypertrophy · BP — Blood pressure

---

### #05 — Multiorgan circulatory-stress sigil (P2)

```
FILE NAME: hd-volume-bp-tolerance-clinician-05-multiorgan-sigil.png
IMAGE TYPE: Organ-crosstalk sigil
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A calm symbolic mark showing that one dialysis session's circulatory stress reaches several organs at once.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring the heart at the center, with the brain above, the intestine lower left, and a single kidney lower right.

Relationship: show hemodialysis-associated circulatory stress radiating from the heart to the three other organs using thin dotted curved arrows, with a soft dotted circular loop connecting all four organs to suggest recurrent, session-after-session stress.

Style: minimal clinical line-art, thin monoline strokes, soft teal-blue palette (#1a6b72, muted slate, pale gray), white background, clean rounded organ shapes, balanced radial sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels.

Composition: heart centered; brain top center; intestine lower left; kidney lower right; dotted arrows outward from the heart and a gentle dotted ring linking all four. Square image, clean margins, high-resolution, publication-grade medical icon aesthetic. Include a small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner, not obscuring the sigil.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, labels, dark background, neon colors, complex infographics, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic lighting. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
1024×1024, white background, four simple monoline organs, dotted links, no text other than the attribution.
```

**fig-desc:** "A symbol for the idea that repeated drops in blood flow during dialysis can affect the heart, brain, gut and kidneys together."

---

### #06 — Which BP reading answers which question (P0)

```
FILE NAME: hd-volume-bp-tolerance-clinician-06-bp-measurement-roles.png
IMAGE TYPE: Simple figure — Scaffold E reference card (three-column)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Make it instantly clear that ABPM, home/standardized readings and routine unit readings answer different clinical questions.

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "Three BP questions in hemodialysis — three different measurements". Teal (#1a6b72) subtitle: "UK Kidney Association 2025 guideline (grades as published)".

Three equal rounded columns on soft gray (#f3f4f6) cards, each with a simple flat line icon at the top and a teal header band:
Column 1 header: "Does this patient have hypertension?" Icon: a small ambulatory BP monitor with cuff. Body: "Interdialytic ambulatory BP monitoring (ABPM)" — grade chip "Recommend · 1C".
Column 2 header: "Is treatment working?" Icon: a home BP monitor on a table. Body: "Home BP or standardized out-of-unit clinic BP" — grade chip "Suggest · 2C".
Column 3 header: "Is it safe to run this session?" Icon: a dialysis chair with an automated cuff. Body: "Routine pre-, intra- and postdialysis unit readings" — grade chip "Suggest · 2C" — small amber note "Not for hypertension management decisions".

Bottom full-width strip in light teal (#eef6f7), navy text: "Never average home and unit readings into one number. KDIGO 2021's intensive target is for CKD not on dialysis." Small gray footnote: "UKKA evidence search: Jan 2000 – Dec 2022."

Grade chips are small rounded pills: navy outline, navy text. Generous whitespace, mobile-readable labels ≥11pt. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, people or faces, any numeric BP target, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter — no serif, decorative or handwritten typefaces. Spell exactly as given. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
1536×1152, three balanced columns, grades exactly "1C", "2C", "2C", no BP numbers, attribution bottom-right.
```

**fig-desc:** "Each blood pressure measurement answers a different question: a 24–48-hour monitor diagnoses high blood pressure, home or standardized readings track treatment, and readings taken in the dialysis unit mainly tell the team whether the session is safe to run."
**fig-abbrevs:** ABPM — Ambulatory blood pressure monitoring · BP — Blood pressure · CKD — Chronic kidney disease · KDIGO — Kidney Disease: Improving Global Outcomes · UKKA — UK Kidney Association

---

### #07 — P01 Recurrent intradialytic hypotension review (P1)

```
FILE NAME: hd-volume-bp-tolerance-clinician-07-p01-recurrent-idh.png
IMAGE TYPE: Clinical algorithm — Style Mode C (renalcarematters.com house style)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: A ward-round version of pathway P01 that cannot be mistaken for a treatment protocol.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. White background, restrained navy and teal typography set in Inter (never a serif font), thin teal connector arrows, generous margins, centered and symmetrical.

Color conventions: navy #0f1e2e for title and body text; teal #1a6b72 for decision diamonds and arrows; green #1f7a4d for review/reassessment endpoints; amber #b8860b for caution nodes; clinical red #b91c1c for the single acute-interrupt node; soft gray for side notes.

Title: "P01 · Recurrent intradialytic hypotension — review pathway". Subtitle in gray: "A review structure, not a treatment protocol".

Content to render (top to bottom):
1. Red rounded box at top-right as a side exit: "Acute instability or severe new symptoms → bedside assessment under LOCAL emergency protocol".
2. Teal diamond: "Recurrent, stable pattern?" — "No" arrow to the red box; "Yes" arrow down.
3. Navy rounded box: "Characterize: symptoms, timing in session, nadir, rescue used, early stops".
4. Navy rounded box: "Check delivery: planned vs delivered time and UF · actual post-weights · intradialytic fluids".
5. Teal diamond: "Congestion present?"
   - Left branch "Yes" → amber box: "Congested AND intolerant → go to P02".
   - Right branch "No / uncertain" → navy box: "Target too low? Lean-mass loss? Non-volume causes: cardiac, rhythm, ischemia, infection, bleeding, drugs, autonomic".
6. Both branches converge into a wide navy box: "Options to review (not a sequence): longer or extra sessions · target rationale · BP-drug timing · cooler dialysate (selected) · dialysate sodium trade-off · HDF if available · volume tool as adjunct".
7. Green endpoint box: "Reassess BOTH: IDH frequency and congestion · named owner · review date".

Gray side note at bottom-left: "KDIGO 2020: symptomatic fall or nadir systolic <90 mmHg should prompt reassessment (consensus, ungraded)."

Design requirements: rounded rectangles for actions and endpoints, diamonds for decisions, consistent spacing and alignment, no clutter, no icons, no people, no dark background. Include a small professional footer reading "© renalcarematters.com" at the bottom-right in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No drug names with doses, no fluid volumes, no UF-rate numbers, no word "safe", no serif fonts, no dark backgrounds, no spaghetti arrows, no gibberish text.

QUALITY CHECK:
1024×1536 portrait, ≤10 nodes, one red node only, green only at the reassessment endpoint, the only number on the image is "<90 mmHg" in the gray KDIGO side note, footer visible.
```

**fig-desc:** "A step-by-step review for repeated low blood pressure during dialysis: rule out an emergency, describe the pattern, check what was actually delivered, decide whether the patient is also fluid-overloaded, then review options and plan a follow-up that watches both low blood pressure and congestion."
**fig-abbrevs:** IDH — Intradialytic hypotension · UF — Ultrafiltration · BP — Blood pressure · HDF — Hemodiafiltration · KDIGO — Kidney Disease: Improving Global Outcomes · P01/P02 — Review pathways in this guide

---

### #08 — P02 Congested AND UF-intolerant (P0)

```
FILE NAME: hd-volume-bp-tolerance-clinician-08-p02-congested-intolerant.png
IMAGE TYPE: Clinical algorithm — Style Mode C (renalcarematters.com house style) with a two-harm balance motif
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: Show the hardest state in the guide and that the answer is to change the delivery burden, not to force UF or accept overload.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. White background, navy and teal typography set in Inter (never a serif font), thin teal connector arrows, generous margins, centered.

Color conventions: navy #0f1e2e text; teal #1a6b72 decisions and arrows; green #1f7a4d review endpoint; amber #b8860b caution; clinical red #b91c1c for the two "harm" boxes only; soft gray side notes.

Title: "P02 · Congested AND poorly tolerating ultrafiltration". Subtitle (gray): "The hardest cell — review the delivery burden".

Top: a horizontal balance graphic drawn as a simple thin navy beam on a small triangle fulcrum. Left pan: red outline box "Force removal in one session → ischemic circulatory stress, IDH". Right pan: red outline box "Accept chronic overload → hypertension, LVH, heart-failure admissions". Beam is level.

Below the balance, top-to-bottom flow:
1. Teal diamond: "Both findings confirmed?" — "Data conflict" arrow right to gray box "Reconcile timing and method → P07"; "Yes" arrow down.
2. Navy box: "Look for a reversible driver: acute illness · new cardiac dysfunction · arrhythmia · drug change · missed or shortened sessions".
3. Navy box (wide, bold): "Change the delivery burden: same volume over more time or more sessions · reduce sodium-driven gains".
4. Amber box: "Record which risk the plan accepts, and for how long".
5. Green endpoint box: "Reassess with balancing measures: IDH episodes · cramps · early stops · congestion signs · recovery time".

Gray side note bottom-left: "UKKA 2025: consider extended hours for poor BP control or IDH on thrice-weekly HD, if resources allow (2A)."

Rounded rectangles, one diamond, consistent spacing, no icons except the balance, no people, no dark background. Footer "© renalcarematters.com" small gray at bottom-right.

NEGATIVE INSTRUCTIONS:
No numbers of minutes, liters, mL/kg/h or mmHg; no drug names; no word "safe"; no serif fonts; no dark backgrounds; no gibberish; balance beam must be level (neither harm favored).

QUALITY CHECK:
1024×1536 portrait, level balance at top, five-step flow, grade "2A" exactly in the side note, footer visible.
```

**fig-desc:** "When a patient is both fluid-overloaded and cannot tolerate fluid removal, both extremes cause harm. The safer path is usually to spread removal over more time or more sessions and cut the salt that drives fluid gain, while tracking both sides."
**fig-abbrevs:** IDH — Intradialytic hypotension · LVH — Left ventricular hypertrophy · BP — Blood pressure · HD — Hemodialysis · UKKA — UK Kidney Association · P07 — Discordant-measurements pathway

---

### #09 — Same volume, more time, lower rate (P0)

```
FILE NAME: hd-volume-bp-tolerance-clinician-09-time-lowers-ufr.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Make the arithmetic of time vs UF rate visible, and show that 13 mL/kg/h is a reference point, not a line between safe and unsafe.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) centered title: "Same fluid, more time, lower rate". Teal (#1a6b72) subtitle: "Example: 3.5 L removed from a 70 kg patient".

Soft dashed vertical divider splits the canvas into two equal rounded panels on very soft gray (#f3f4f6).
Left panel header in navy: "4 hours". A simple horizontal clock-bar graphic 4 segments long; beneath it a large navy number "12.5 mL/kg/h".
Right panel header in navy: "4.5 hours". A clock-bar 4.5 segments long; beneath it a large navy number "11.1 mL/kg/h".
Between panels at the bottom, a thin horizontal gradient scale (pale gray to pale amber, NO green and NO red) with a small neutral tick labeled "13 mL/kg/h — observational reference (HEMO cohort), not a safety line". Both values sit as small navy dots on the scale.

Bottom full-width light teal (#eef6f7) strip, navy text: "Rate = volume ÷ time. Higher rates are associated with mortality in cohorts; no randomized trial has shown that lowering the rate improves outcomes."

Mobile-readable labels ≥11pt, rounded corners, ample negative space. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Do NOT color either side green or red. Do not use the words "safe", "unsafe", "danger" or "limit". No numbers other than: 3.5 L, 70 kg, 4 hours, 4.5 hours, 12.5, 11.1, 13. No people, no cartoon, no clutter, no dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
1792×1024, two equal panels, numbers exactly 12.5 and 11.1, neutral reference tick at 13 with its caption, attribution bottom-right.
```

**fig-desc:** "Removing the same 3.5 liters over 4.5 hours instead of 4 hours lowers the rate of removal from 12.5 to 11.1 mL per kg per hour. The 13 mark is a reference from an observational study, not a line between safe and unsafe."
**fig-abbrevs:** UF — Ultrafiltration · HEMO — Hemodialysis Study (US randomized trial whose data were later analyzed for UF rate)

---

### #10 — Sodium drives thirst drives weight gain (P1)

```
FILE NAME: hd-volume-bp-tolerance-clinician-10-sodium-thirst-cycle.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (and dietitians)
VISUAL GOAL: Show why interdialytic weight gain is mostly a sodium problem, and where dialysate sodium enters the loop.

PROMPT:
Clean clinical education infographic, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top center: "Water follows sodium". Teal subtitle: "Why fluid restriction alone tends to fail".

Five rounded rectangular cards in a single horizontal row on a very soft gray panel (#f3f4f6), connected by bold navy right-pointing arrows. Each card has a thin colored top accent band, a small flat line icon, a bold label and one short line:
1. Teal band — icon salt shaker — "Sodium intake" — "Diet, sauces, processed food".
2. Teal band — icon droplet with "Na" symbol — "↑ Plasma osmolality".
3. Amber band — icon glass of water — "Thirst → drinking".
4. Amber band — icon bathroom scale — "↑ Interdialytic weight gain".
5. Navy band — icon dialyzer cylinder — "Higher UF need next session".

Above card 3, a second smaller input arrow from a box labeled "Dialysate sodium above plasma → diffusive sodium gain during HD" feeding into card 2.

Bottom strip, full-width soft gray, navy text: "UKKA 2025: dietary salt ≤5 g/day (1B) — about 2 g of sodium." Small gray right-aligned note: "Low dialysate sodium lowers IDWG but probably increases IDH and cramps (Cochrane 2024)."

Generous whitespace, mobile-readable. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No dialysate sodium concentrations in mmol/L, no fluid-allowance numbers, no people, no food brand logos, no cartoon, no clutter, no dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
1792×1024, five cards in one row, one side input from dialysate, only numbers "5 g", "2 g", "1B", "2024", attribution visible.
```

**fig-desc:** "Salt raises the concentration of the blood, which causes thirst; the water a patient drinks is held until the next session, so the weight gain between sessions is mostly driven by salt. Dialysate with more sodium than the blood can add salt during the session too."
**fig-abbrevs:** Na — Sodium · HD — Hemodialysis · UF — Ultrafiltration · IDWG — Interdialytic weight gain · IDH — Intradialytic hypotension · UKKA — UK Kidney Association

---

### #11 — Cooling: center-wide policy vs selected patient (P1)

```
FILE NAME: hd-volume-bp-tolerance-clinician-11-cooling-policy-vs-patient.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Separate the question MyTEMP answered from the question UKKA addresses, so neither is over-read.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white (#ffffff) background, all text in Inter. Bold navy title centered: "Cooler dialysate: two different questions".

Dashed vertical divider, two equal rounded panels on soft gray (#f3f4f6). Both panel headers in navy (do NOT use green vs red).
Left panel header: "Question 1 — Cool everyone? (center-wide policy)". Small flat icon of a dialysis unit floor with many chairs. Text lines:
"MyTEMP · 84 centers · 15,413 patients"
"Achieved 35.8 vs 36.4 °C"
"CV death or CV hospitalization: HR 1.00 (96% CI 0.89–1.11)"
Verdict chip (navy outline): "No CV benefit from a universal policy".
Right panel header: "Question 2 — Cool this hypotension-prone patient?". Small flat icon of one dialysis chair with a thermometer.
Text lines:
"UKKA 2025: lowering dialysate temperature can reduce IDH in prone patients — Suggest (2A)"
"Physiology: less skin and splanchnic vasodilation → better preload"
Verdict chip (navy outline): "Reasonable targeted trial; watch thermal discomfort".

Bottom light teal strip, navy text: "MyTEMP argues against cooling everyone for cardiovascular protection. It does not settle targeted cooling for a symptomatic individual."

Mobile-readable, generous whitespace. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No recommended temperature setting, no people's faces, no green/red good-vs-bad coding, no cartoon, no dark backgrounds, no gibberish. Use ONLY Inter. Spell "center" and "hospitalization" in American English. Never omit the attribution.

QUALITY CHECK:
1792×1024, numbers exactly as given (84; 15,413; 35.8; 36.4; 1.00; 96%; 0.89–1.11; 2A), attribution visible.
```

**fig-desc:** "A large trial found that cooling the dialysate for everyone in a unit did not reduce heart events. That is a different question from cooling the dialysate for one patient whose blood pressure keeps dropping, which the UK guideline suggests can help."
**fig-abbrevs:** CV — Cardiovascular · HR — Hazard ratio · CI — Confidence interval · IDH — Intradialytic hypotension · UKKA — UK Kidney Association

---

### #12 — Spironolactone in dialysis: guideline vs newer trials (P0)

```
FILE NAME: hd-volume-bp-tolerance-clinician-12-mra-evidence-timeline.png
IMAGE TYPE: Simple figure — Scaffold E reference card (timeline layout)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Show that the 2025 outcome trials post-date the UKKA evidence search, and separate BP lowering from cardiovascular protection.

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background, all text in Inter. Bold navy title: "Mineralocorticoid receptor antagonists in dialysis — read by date and by indication".

A clean horizontal timeline across the upper half, thin navy line with year ticks 2022, 2023, 2024, 2025. A shaded soft-gray band from the left edge to 2022 labeled "UKKA 2025 evidence search ends Dec 2022". Two teal markers at 2025: "ACHIEVE" and "ALCHEMIST", both outside the shaded band.

Lower half: a three-row table with teal (#1a6b72) column headers on soft gray (#f3f4f6): "Source", "Question", "Result".
Row 1: "UKKA 2025, Rec 29 (2B)" | "Difficult-to-control BP" | "MRA may be considered, with careful potassium monitoring".
Row 2: "ACHIEVE (2025)" | "CV protection" | "2,538 randomized after run-in · CV death or HF admission HR 0.92 (0.78–1.09) · stopped for futility".
Row 3: "ALCHEMIST (2025)" | "CV protection" | "644 randomized · CV composite HR 1.00 (0.73–1.36) · stopped when funding ended (not futility)".

Footer sentence in navy on light teal: "Do not start spironolactone for cardiovascular protection in dialysis. Resistant hypertension is a separate, narrower question — with a potassium cost."

Alternating white/soft-gray rows, key phrases "stopped for futility" and "not futility" in amber. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No doses, no drug packaging, no people, no green check marks, no red crosses, no cartoon, no dark backgrounds, no gibberish. Use ONLY Inter. Numbers exactly as given. Never omit the attribution.

QUALITY CHECK:
1536×1152, timeline + 3-row table, all numbers match the prompt, attribution visible.
```

**fig-desc:** "The UK guideline's evidence search stopped at the end of 2022, before two large 2025 trials showed that spironolactone does not protect the heart in people on dialysis. The guideline's narrower suggestion — considering it for hard-to-control blood pressure — is a separate question."
**fig-abbrevs:** MRA — Mineralocorticoid receptor antagonist · UKKA — UK Kidney Association · BP — Blood pressure · CV — Cardiovascular · HF — Heart failure · HR — Hazard ratio

---

### #13 — What each volume tool sees (P1)

```
FILE NAME: hd-volume-bp-tolerance-clinician-13-what-each-tool-sees.png
IMAGE TYPE: Infographic — Clinician reference card (archetype 5)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Map each volume-assessment tool to the compartment it actually measures, so no single reading is treated as "liters to remove."

PROMPT:
Clinical reference infographic card for clinicians, publication-grade nephrology design, white background, all text in Inter. Bold navy title: "Each tool sees one compartment, at one moment". Teal subtitle: "None returns 'liters to remove'".

Center: a simple semi-3D schematic of three nested compartments drawn as translucent rounded shapes — outermost "Interstitial fluid" (pale teal), inner "Plasma" (pale red), and a separate small "Lungs" shape (pale blue) above, with a small "Heart" icon. Thin leader lines connect six small modular cards around the schematic:
1. "Lung ultrasound — extravascular lung water" → Lungs.
2. "Bioimpedance spectroscopy — extra- vs intracellular water (model-based)" → Interstitial fluid.
3. "Relative blood volume — % change during the session" → Plasma.
4. "Absolute blood volume — estimated circulating volume (device-specific)" → Plasma.
5. "IVC / point-of-care ultrasound — venous filling at one moment" → a small vena cava drawn beside the heart.
6. "Natriuretic peptides — myocardial wall stress (raised by kidney failure itself)" → Heart.
Each card has one amber caveat line in smaller text: timing in the cycle · model assumptions · no absolute baseline · limited outcome data · operator and breathing · not volume-specific.

Bottom strip, navy text on light teal: "UKKA 2025: inadequate evidence that any one technology beats another or clinical assessment (2C)."

Rounded cards, compact, no clutter, mobile-readable. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No device brand names or logos, no numeric cutoffs (no B-line counts, no OH values, no RBV percentages), no people, no cartoon, no dark backgrounds, no gibberish. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
1536×1152, six cards each linked to the correct compartment, one caveat per card, grade "2C" exactly, attribution visible.
```

**fig-desc:** "Each volume test looks at a different part of the body's fluid — lung water, total body water, the blood itself, the large vein near the heart, or heart strain — at one point in time. None of them tells you exactly how much fluid to remove."
**fig-abbrevs:** IVC — Inferior vena cava · RBV — Relative blood volume · OH — Overhydration (bioimpedance estimate) · UKKA — UK Kidney Association

---

### #14 — Incremental HD: selection and escalation (P1)

```
FILE NAME: hd-volume-bp-tolerance-clinician-14-incremental-hd-selection.png
IMAGE TYPE: Clinical algorithm — Style Mode B (journal / nephrology treatment algorithm)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: Show that urine volume alone cannot select a twice-weekly schedule, and that escalation triggers are agreed before starting.

PROMPT:
Create a clean academic medical journal treatment algorithm flowchart on a white background, resembling a nephrology review figure: minimal, centered, symmetrical, publication-ready. Typography clean, black and journal-like, set in Inter (never a serif font).

Visual conventions: beige rounded rectangles for patient category; pale blue rounded rectangles for assessment steps; pale green rounded rectangles for the agreed plan and monitoring; thin muted teal arrows; balanced left-right branching; consistent box widths.

Title: "Incremental hemodialysis — selection and escalation".

Content to render:
1. Beige: "Incident HD patient with residual urine output".
2. Pale blue: "Is residual function MEASURED? (dated timed collection with urea clearance, Kru)".
   - Left branch "Urine volume only / unknown" → pale blue: "Collect timed urine · track potassium, fluid, nutrition" → arrow back up to step 2 (thin dashed).
   - Right branch "Measured" → pale blue: "Nephrologist-led review: solute and potassium control · fluid control · nutrition · intercurrent illness · monitoring capacity · patient preference".
3. Pale green: "Agree escalation triggers as a LOCAL protocol before starting".
4. Pale green: "Scheduled re-measurement of residual function".
Small gray footnote under the chart: "Evidence: mostly observational (meta-analysis 2024); small RCTs with diet co-intervention or HDF-only populations (2025)."

Design requirements: concise text, centered alignment, wide margins, no icons, no dark background. Include a small professional footer reading "© renalcarematters.com" positioned at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No numeric clearance or urine-volume cutoffs, no "twice weekly" recommendation node, no diet prescription, no serif fonts, no dark backgrounds, no gibberish.

QUALITY CHECK:
1024×1536, two branches from the measurement diamond/box, dashed return loop on the "urine only" branch, footer visible.
```

**fig-desc:** "Before starting dialysis less often, the team should measure how much the kidneys still clear with a timed urine collection — urine volume alone is not enough — and agree in advance what changes would trigger more frequent dialysis."
**fig-abbrevs:** HD — Hemodialysis · Kru — Residual urea clearance · RCT — Randomized controlled trial · HDF — Hemodiafiltration

---

### #15 — Convection volume is not net fluid removal (P2)

```
FILE NAME: hd-volume-bp-tolerance-clinician-15-convection-vs-net-uf.png
IMAGE TYPE: Simple figure — Scaffold D single mechanism (hemodiafiltration circuit, post-dilution)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show that in HDF most of the large filtered volume is returned as replacement fluid, so convection volume ≠ the patient's net fluid loss.

PROMPT:
Medical pathophysiology infographic, AJKD/NEJM graphical-abstract style, white (#ffffff) background, all text in Inter. Title in bold navy: "Hemodiafiltration: big convection, small net loss". Teal subtitle: "Convection volume is not net fluid removal".

Center: a horizontal hollow-fiber hemodiafilter drawn as a clean semi-3D cylinder with fine parallel lines for the fiber bundle. Anatomy MUST be: two END ports on the blood path — left end "Arterial port · blood IN", right end "Venous port · blood OUT"; two SIDE ports on the shell — "Dialysate IN" near the RIGHT (venous, blood-out) end and "Effluent OUT" near the LEFT (arterial, blood-in) end, so dialysate flows right-to-left, countercurrent to blood. A single arterial line comes from a simple arm icon at far left to the arterial port; a single venous line returns from the venous port to the arm.

A thick teal arrow labeled "Large convective filtration across the membrane" points from the fibers into the shell space toward the effluent port. On the VENOUS line, after the filter, a separate small bag labeled "Replacement fluid (post-dilution)" infuses into the blood line — NOT into the filter's shell port.

Right side, two stacked rounded cards:
Card 1 (navy): "Convection volume = filtered volume (mostly replaced)".
Card 2 (teal): "Net fluid removal = filtered volume − replacement volume".

Bottom strip, navy text on light teal: "CONVINCE (2023): high-dose HDF lowered all-cause mortality in selected candidates (HR 0.77). It was not a trial of UF intolerance."

Ample negative space, mobile-readable. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Do NOT merge dialysate and replacement fluid into one input. Do NOT place dialysate and effluent ports at the same end or swap them. Do NOT draw replacement fluid entering the filter shell. Draw exactly one arterial and one venous line. No numeric volumes in liters, no pressure values, no people, no cartoon, no dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
1792×1024; port topology exactly as specified (end ports = blood, side ports = dialysate in near venous end, effluent out near arterial end, countercurrent); replacement fluid joins the venous blood line; only number "0.77" and "2023"; attribution visible.
```

**fig-desc:** "In hemodiafiltration a lot of fluid is filtered out of the blood to clear waste, but most of it is put back as clean replacement fluid. Only the difference is actually removed from the patient."
**fig-abbrevs:** HDF — Hemodiafiltration · UF — Ultrafiltration · HR — Hazard ratio

---

### #16 — Symptom map across the dialysis cycle (P2)

```
FILE NAME: hd-volume-bp-tolerance-clinician-16-symptom-cycle-map.png
IMAGE TYPE: Infographic — Circular workflow / cycle (archetype 8)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Map symptoms to the phase of the dialysis cycle so clinicians capture both congestion and tolerance signals.

PROMPT:
Circular clinical workflow infographic, polished nephrology systems diagram, white background, all text in Inter. Center object: a simple semi-3D dialysis machine icon on a soft teal (#eef6f7) disc. Around it, a ring divided into four equal arcs with thin teal arrows running clockwise:
Arc 1 "Before session" (amber accent): "Dyspnea · orthopnea · edema — after the long interval".
Arc 2 "During session" (red accent): "Cramps · dizziness · nausea · chest discomfort".
Arc 3 "After session" (navy accent): "Post-dialysis fatigue · recovery time".
Arc 4 "Between sessions" (teal accent): "Thirst · daily function".
Outer caption ring in small gray text: "Track one benefit AND one balancing measure".
Title at top in bold navy: "Symptoms across the dialysis cycle".

Clean labels, strong hierarchy, mobile-readable, no clutter. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No people or faces, no symptom scores or numbers, no named questionnaires, no cartoon, no dark backgrounds, no gibberish. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
1024×1024, four equal arcs in clockwise order, center icon, no numbers, attribution visible.
```

**fig-desc:** "Different symptoms point to different problems depending on when they happen: breathlessness before a session suggests fluid overload, cramps and dizziness during it suggest poor tolerance, and fatigue afterward affects recovery."

---

### #17 — Simulation vs prospective trial (P2)

```
FILE NAME: hd-volume-bp-tolerance-clinician-17-simulation-vs-trial.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Prevent the "90% of patients improved" statistic from being read as 90% time in target or as a clinical benefit.

PROMPT:
Medical education comparison infographic, white background, all text in Inter. Bold navy title centered: "Reading an adaptive-UF headline". Teal subtitle: "In silico study, 2026 — 119,472 historical treatments, 11,246 patients".

Dashed vertical divider, two equal rounded panels on soft gray (#f3f4f6), both headers in navy.
Left panel header: "What the simulation showed". A simple horizontal bar pair: "Historical 36.3%" (short gray bar) and "Simulated 56.4%" (longer teal bar), labeled "Mean time in RBV target region". Below: "Improved in 90.0% of patients".
Right panel header: "What it did NOT show". Three amber-outlined chips stacked:
"90% of patients improved ≠ 90% time in target"
"Surrogate RBV metric ≠ patient outcome"
"Replayed past data ≠ prospective trial"
Small gray note: "Several authors reported industry affiliations."

Bottom light teal strip, navy text: "Rung 7 on the evidence ladder — watch list, not practice."

Mobile-readable, generous whitespace. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No device brand names or logos, no green checkmarks, no red X marks, no people, no cartoon, no dark backgrounds, no gibberish. Use ONLY Inter. Numbers exactly as given. Never omit the attribution.

QUALITY CHECK:
1792×1024, bars labeled 36.3% and 56.4%, "90.0%" shown once as a patient proportion, three "≠" chips, attribution visible.
```

**fig-desc:** "A computer simulation increased the share of each session spent in a target blood-volume range from about 36% to 56%, and that improved for 90% of patients. That does not mean 90% of the session was in range, and it has not yet been shown to help patients."
**fig-abbrevs:** UF — Ultrafiltration · RBV — Relative blood volume

---

### #18 — Monthly unit review cycle (P2)

```
FILE NAME: hd-volume-bp-tolerance-clinician-18-unit-review-cycle.png
IMAGE TYPE: Infographic — Circular workflow / cycle (archetype 8)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians, dialysis unit leads
VISUAL GOAL: Show how a unit can run a monthly multidisciplinary volume review without turning it into protocol medicine.

PROMPT:
Circular clinical workflow infographic, polished nephrology systems diagram, white background, all text in Inter. Title at top in bold navy: "Monthly volume & BP review — unit cycle".

Center object: a simple flat clipboard icon on a soft teal disc labeled "Multidisciplinary review: nephrologist · charge nurse · dietitian · pharmacist".
Five steps around it, connected clockwise by thin teal arrows, each in a small rounded card:
1. "Flag: recurrent IDH · high UFR on delivered time · missed targets · out-of-unit hypertension".
2. "Record the 3 axes: congestion · UF tolerance · residual function".
3. "Name the data gaps".
4. "Plan + owner + review date".
5. "Measure: process AND balancing measures".
Small gray note under the cycle: "No mortality claim; no unadjusted unit benchmarking."

Navy/teal/gold accents, strong hierarchy, mobile-readable, no clutter. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
No people or faces, no performance scores, no traffic-light compliance colors, no numbers, no cartoon, no dark backgrounds, no gibberish. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
1024×1024, five steps clockwise around a central icon, no numbers other than "3", attribution visible.
```

**fig-desc:** "A monthly team review flags patients with recurring problems, records what is known and unknown about their fluid and blood pressure, sets a plan with an owner and a date, and tracks both benefits and side effects."
**fig-abbrevs:** BP — Blood pressure · IDH — Intradialytic hypotension · UFR — Ultrafiltration rate · UF — Ultrafiltration

---

## 4. HTML insertion template

Use this shape for every new figure (lightbox-ready, CLAUDE.md rule 11):

```html
<figure style="margin:28px 0;">
<picture>
<source srcset="../images/hd-volume-bp-tolerance-clinician-NN-name.webp" type="image/webp">
<img loading="lazy" src="../images/hd-volume-bp-tolerance-clinician-NN-name.png" alt="[descriptive alt]" width="W" height="H" style="width:100%;height:auto;">
</picture>
<figcaption style="font-size:13px;color:var(--text-muted);text-align:center;margin:10px auto 0;max-width:600px;line-height:1.55;"><p class="fig-desc" style="margin:0;">[fig-desc from this plan]</p>
<dl class="fig-abbrevs">
<dt>XX</dt><dd>Expansion</dd>
</dl>
</figcaption>
</figure>
```

After inserting figures, re-run:
`python3 audit_acronym_expansion.py --guide hd-volume-bp-tolerance-clinician.html` — a figure `<dl>` placed *before* an acronym's first body use will fail the audit; move the figure later or expand the acronym in prose above it. Add any new acronym (for example `OH`, `HEMO`) to the guide's Glossary.

---

## 5. Production checklist (per image)

- [ ] Light background; no dark fills
- [ ] Inter only; no serif text
- [ ] Attribution present bottom-right (bottom-center for portrait if it collides)
- [ ] Every number on the image appears in the guide text (spot-check against §2 inventory)
- [ ] No "safe/unsafe" language; no green on a UFR value
- [ ] Grades exactly as the issuer published them (UKKA 1B/1C/2A/2B/2C/2D; KDIGO 2020 = ungraded)
- [ ] American English spelling (hemodialysis, hemodiafiltration, center, hospitalization)
- [ ] Hemodiafilter anatomy (image #15) matches the port rules exactly
- [ ] PNG + WebP saved to `images/`; figure inserted with fig-desc + fig-abbrevs
- [ ] Hero/OG replaced → update hero alt, regenerate rg-thumb and Latest guides strip
