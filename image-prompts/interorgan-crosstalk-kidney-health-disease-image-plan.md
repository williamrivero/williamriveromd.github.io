# Image Plan Blueprint — Interorgan Crosstalk in Kidney Health and Disease

**Guide:** `guides/interorgan-crosstalk-kidney-health-disease.html` · **Companion calculators:** `guides/calc-post-aki-followup.html`, `guides/calc-vexus-grading.html`
**Version:** 2.0 · November 22, 2026 (replaces v1.0, which had 12 prompts; prompts 001 to 012 are unchanged)
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` · `williamriveromd-organ-crosstalk-sigil-graphic` · `williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure` · Stage 2 schema from `williamriveromd-local-image-generator`
**Local folder (Stage 2):** `~/Downloads/interorgan-crosstalk-kidney-health-disease/`

**How to use this file.** Paste one `PROMPT` block at a time into the Image Generator GPT, with its `NEGATIVE INSTRUCTIONS`. Check the result against its `QUALITY CHECK`. Save it under the exact `FILE NAME`. Produce in the order given in A.6.

---

## Part A — Blueprint

### A.1 The aim: one set of pictures, four kinds of reader

The guide is read by people who cannot read English well, by patients who read at about a grade 6 level, by families and students who want the reasoning, and by clinicians who want the mechanism and its evidence. Each image is built in layers so that every one of them takes something away.

| Layer | Who it serves | What carries the meaning | Rule in the prompts |
|---|---|---|---|
| 1 · Picture | A reader who does not read the labels | Shape, position, color and arrows alone | The image must pass the cover-the-words test: hide every label and the main idea is still visible |
| 2 · Label | Grade 6 reader, any of the four site languages | Labels of 1 to 5 plain English words | No sentence on an image is longer than 12 words; no abbreviation on a patient image |
| 3 · Caption | Families, students, health workers | The four-language `fig-desc` caption and `fig-abbrevs` in the guide | Captions live in HTML, never baked into the image |
| 4 · Detail | Clinicians | Callouts, evidence coding, magnified insets | Clinician figures only; still one idea per image |

Three tests are applied to every finished image before it is accepted:

1. **Cover-the-words test.** Hide the text. Can a family member still say what the picture is about?
2. **Ten-second phone test.** At 390 px wide, is the main idea readable in 10 seconds without zooming?
3. **Truth test.** Does any arrow, size or color claim more than the guide's text claims? Experimental links must look experimental.

### A.2 Why these images, in this order

Understanding comes first from recognition, then from a model, then from proof. The set follows that order.

| Stage of understanding | Reader's question | Images |
|---|---|---|
| Recognition | "Is this about me?" | 001 hero, 014 family visit, 020 medicine bag |
| A model to hold | "How do I picture this?" | 013 barangay of organs, 003 organ hub, 015 partner cards |
| Why it matters | "What could go wrong, and when do I act?" | 019 warning signs, 016 same number two stories, 004 post-AKI timeline |
| What I can do | "What do I check and what protects me?" | 017 tests as windows, 018 one habit many organs |
| Mechanism | "What exactly is happening?" | 005, 006, 007, 008, 010, 023, 024, 025 |
| Proof and its limits | "How sure are we?" | 021 three questions of proof, 009 evidence-coded loop, 026 shared therapy, 022 time definitions |
| Applying it | "What do I do at the bedside?" | 027 VExUS card, 028 three cases |

### A.3 Visual grammar (identical in every prompt that uses it)

- **Kidneys:** always a matched pair, soft renal red-brown with a teal (#1a6b72) outline accent, at the center or on the left.
- **Solid teal arrow:** established physiology or evidence from human trials.
- **Dashed purple (#6c3d8e) arrow with a small flask icon:** experimental evidence from animals or cells.
- **Small two-person icon:** evidence from studies in people.
- **Warm red:** arterial blood and "act now". **Muted blue:** venous blood. **Amber (#b8860b):** caution. **Green (#1f7a4d):** safe or protective.
- **Color is never the only signal.** Every color-coded item also has a shape, icon or line style, so the figure works for color-blind readers and in grayscale print.
- **People:** Filipino adults, calm expressions, bright natural light, everyday clothing. No celebrity likeness, no identifiable real person, no clinic or drug branding.

### A.4 Appreciation: what makes a reader want to keep looking

- **Familiar settings.** The analogy picture (013) is a Philippine barangay street. The family scene (014) is a small clinic room, not a stock corporate office.
- **Dignity.** Patients are shown as capable adults asking questions and holding their own records, never as frightened or passive.
- **Craft.** Organs are soft semi-3D with gentle studio light, matching the site's illustrated look. Flat clip-art is excluded in every prompt except the two sigils, which are line art by design.
- **Calm.** White space is part of the teaching. No prompt allows more than eight labeled elements on a patient image.

### A.5 What stays code-native (do not generate)

Effect sizes, confidence intervals, trial names and denominators stay in the guide's HTML tables and Evidence Scorecard, because image generators garble digits. The only digits allowed on any image are listed in each prompt's quality check: "3 months" (004), step numbers (005, 008, 021), "7 days" and "90 days" (022), and the VExUS thresholds (027). Proofread those characters one by one.

### A.6 Image inventory, placement and production tiers

**Tier P1 (publish-blocking, 10 images):** 001, 002, 003, 004, 013, 016, 019, 005, 006, 025.
**Tier P2 (strongly recommended, 11 images):** 014, 015, 017, 018, 007, 008, 009, 010, 021, 022, 023.
**Tier P3 (enrichment, 7 images):** 020, 024, 026, 027, 028, 011, 012.

| # | File (PNG + WebP twin), prefix `interorgan-crosstalk-kidney-health-disease-` | Section | Audience | Skill / archetype | Size | Wired in guide? |
|---|---|---|---|---|---|---|
| 001 | `vignette-hero` | Hero | Mixed | Hero vignette v3, Scaffold C anatomy | 2048×2048 | Yes |
| 002 | `og` | `<head>` | Mixed | OG / social share card | 1200×630 | Yes |
| 003 | `01-organ-crosstalk-hub` | `#p-start` | Patients | Organ crosstalk sigil, labeled | 1536×1536 | Yes |
| 004 | `02-post-aki-timeline` | `#p-change` | Mixed | Simple figure, Scaffold C | 1792×1024 | Yes |
| 005 | `03-five-channels` | `#md-physio` | Clinicians | Simple figure, Scaffold D | 1792×1024 | Yes |
| 006 | `04-cardiorenal-congestion-forward-flow` | `#md-heart` | Clinicians | Biomedical mechanism figure | 1792×1024 | Yes |
| 007 | `05-hepatorenal-hemodynamics` | `#md-liver` | Clinicians | Biomedical mechanism figure | 1792×1024 | Yes |
| 008 | `06-gut-liver-kidney-solutes` | `#md-gut` | Clinicians | Simple figure, Scaffold C | 1792×1024 | Yes |
| 009 | `07-bone-kidney-heart-fgf23-loop` | `#md-bone` | Clinicians | Organ crosstalk sigil, evidence-coded | 1536×1536 | Yes |
| 010 | `08-epo-hepcidin-iron` | `#md-marrow` | Clinicians | Biomedical mechanism figure | 1792×1024 | Yes |
| 011 | `calc-post-aki-followup-og` (no prefix) | Calculator page | Clinicians | OG card | 1200×630 | Optional |
| 012 | `calc-vexus-grading-og` (no prefix) | Calculator page | Clinicians | OG card | 1200×630 | Optional |
| 013 | `09-barangay-of-organs` | `#p-start`, before 003 | Patients | Simple figure, Scaffold B (analogy beside anatomy) | 1792×1024 | New |
| 014 | `10-family-clinic-visit` | `#p-visit` | Patients | Infographic skill, archetype 1 photorealistic editorial | 1792×1024 | New |
| 015 | `11-eight-partner-cards` | `#p-organs`, above the table | Patients | Infographic skill, archetype 4 multi-panel | 1792×1024 | New |
| 016 | `12-same-number-two-stories` | `#p-change`, first figure | Patients | Simple figure, Scaffold B | 1792×1024 | New |
| 017 | `13-tests-as-windows` | `#p-tests` | Patients | Simple figure, Scaffold E quick-look | 1536×1152 | New |
| 018 | `14-one-habit-many-organs` | `#p-protect` | Patients | Infographic skill, archetype 8 circular | 1024×1024 | New |
| 019 | `15-warning-signs` | After the red urgent-care alert | Patients | Simple figure, Scaffold E quick-look | 1792×1024 | New |
| 020 | `16-medicine-bag-check` | `#p-protect`, beside "Do this" | Patients | Infographic skill, archetype 1 photorealistic editorial | 1792×1024 | New |
| 021 | `17-three-questions-of-proof` | `#md-answer` | Mixed | Simple figure, Scaffold C | 1792×1024 | New |
| 022 | `18-aki-akd-ckd-time-axis` | `#md-timeline` | Clinicians | Simple figure, Scaffold C | 1792×1024 | New |
| 023 | `19-lung-kidney-two-edemas` | `#md-lung` | Clinicians | Biomedical mechanism figure, two-panel | 1792×1024 | New |
| 024 | `20-brain-kidney-nerve-loop` | `#md-brain` | Clinicians | Organ crosstalk sigil, evidence-coded | 1536×1536 | New |
| 025 | `21-muscle-creatinine-trap` | `#md-muscle` (also suits `#p-organs`) | Mixed | Simple figure, Scaffold B | 1792×1024 | New |
| 026 | `22-one-prescription-several-organs` | `#md-shared` | Mixed | Simple figure, Scaffold D | 1792×1024 | New |
| 027 | `23-vexus-grading-card` | `#md-heart` and `calc-vexus-grading.html` | Clinicians | Simple figure, Scaffold E reference card | 1536×1152 | New |
| 028 | `24-three-cases` | `#md-cases` | Clinicians | Infographic skill, archetype 7 case snapshot | 1792×1024 | New |

"New" images are not yet referenced in the guide. Each needs a `<figure>` block with `width`, `height`, `alt`, a `fig-desc` caption (four languages for patient figures) and `fig-abbrevs` where an abbreviation appears. Suggested English captions are in Part C.

### A.7 Medical accuracy locks (do not let the generator change these)

- Kidneys: bean-shaped pair, hilum facing the midline, ureters leaving downward. Never one kidney, never three.
- Arterial inflow enters at the hilum; the renal vein leaves at the hilum toward the inferior vena cava. In 006 congestion backs up **in the vein**.
- Liver: right upper abdomen, larger than either kidney. Cirrhotic liver (007) is nodular and smaller.
- Parathyroid (009): one small gland icon at the neck, not on the kidney.
- Experimental links stay dashed purple with a flask: bone to heart (009), cytokine permeability edema (023), neuroinflammation (024).
- 016: both panels show the **same** rising creatinine. The difference is the body's fluid state, not the number.
- 025: both figures have the **same** kidney filtration. Only muscle mass and creatinine differ.
- 019: symptoms only. No instruction other than "Go to the emergency room".
- 020 and 026: no brand names, no readable drug names, no doses.
- 027: thresholds must read exactly "2 cm", "30%", "50%", and grades "0, 1, 2, 3". If any digit is wrong, discard the image and keep the HTML table.

---

## Part B — Prompt blocks

### 001 · Hero vignette

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C anatomy
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C — Radial
CAMERA: soft three-quarter view, slightly above
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: mixed
VISUAL GOAL: One glance shows the kidneys at the center of a ring of partner organs that work together.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be
displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE
BORDER around the full circle. Composition archetype: C Radial. Camera: soft three-quarter view
from slightly above.

Subject: a single clean render of a pair of human kidneys at the center, anatomically accurate,
in restrained renal red-brown with a subtle teal rim light. Arranged in a loose ring around them,
smaller and softer, four supporting organs: a heart (upper left), a pair of lungs (upper right),
a liver (lower right) and a short length of long bone (lower left). Thin, softly glowing teal
threads of light arc between the kidneys and each organ, suggesting two-way communication. All
organs float on a soft, uncluttered light teal-tinted (#eef6f7) background with gentle studio
lighting and soft shadows.

Visual hierarchy: the kidneys occupy about 40% of the circle and the four supporting organs
together about 25%; reserve a 20–25% TITLE SAFE ZONE of empty soft background on the left side
of the circle (no anatomy, threads, labels or callouts in that zone). Soft falloff at the rim.
Calm, premium medical textbook cover feeling. Color grade harmonizes with clinical teal #1a6b72
and navy #0f1e2e on a light background.

Absolutely NO text, labels, leader lines, callouts, titles, logos or watermark — clean render
only. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting organs, dozens of icons, tiny
labels, cropped circle, cropped anatomy, objects touching the circular border, important content
inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular
frames, dark or charcoal backgrounds, cartoon style, neon, HDR, over-saturation, implausible
anatomy, a single kidney, people or faces.

QUALITY CHECK:
Two kidneys, correctly shaped; four supporting organs recognizable at thumbnail size; left-side
title zone empty; circle fully visible with a white margin; no words anywhere.
```

### 002 · OG / social share card

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
AUDIENCE: mixed
VISUAL GOAL: A share card that says "the kidneys talk to every organ" in one glance, with the guide title readable on a phone.

PROMPT:
Social share card, 1200 × 630, off-white (#fafafa) background. Left 55%: title text in bold
navy (#0f1e2e) Inter, three lines: "Interorgan Crosstalk" / "in Kidney Health" / "and Disease".
Below it, one line in clinical teal (#1a6b72) Inter, smaller: "How the kidneys talk to the heart,
lungs, liver, gut, bone, blood, brain and muscle". Right 45%: a soft semi-3D illustration of a
pair of kidneys at the center with six small organ icons around them (heart, lungs, liver,
intestine, bone, brain), joined to the kidneys by thin two-way teal arrows. Generous margins,
calm and uncluttered. A thin teal rule under the title block. Bottom-right: "renalcarematters.com"
in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy,
HDR, excessive saturation. NEVER use dark, navy, charcoal or black backgrounds. Use ONLY Inter.
No author name on the card. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200 × 630. Title spelled exactly as written. No author suffix. Light background.
Attribution visible bottom-right.
```

### 003 · Organ crosstalk hub (patient)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-01-organ-crosstalk-hub.png
IMAGE TYPE: Organ crosstalk sigil, labeled
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1536 × 1536
AUDIENCE: patients and families
VISUAL GOAL: The kidneys sit at the center of a two-way network with eight partner organs.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring:

ORGANS:
- a pair of kidneys (center)
- heart, lungs, liver, intestine, a long bone, a cluster of red blood cells, brain, and a flexed
  arm muscle (eight icons in an evenly spaced ring around the kidneys)

RELATIONSHIP:
Show two-way communication between the kidneys and each of the eight organs using dotted curved
arrows with an arrowhead at BOTH ends, one arrow per organ, all meeting the central kidneys.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette (teal #1a6b72, muted
blue, slate, pale gray), white background, clean rounded organ shapes, balanced radial sigil-like
composition, generous whitespace, no photorealism, no 3D. Add ONE short label under each organ in
Inter, navy (#0f1e2e), sentence case: "Heart", "Lungs", "Liver", "Gut", "Bones", "Blood", "Brain",
"Muscles", and "Kidneys" under the center pair. No other text.

COMPOSITION:
Place the kidneys at the exact center, slightly larger than the surrounding icons. Arrange the
eight organs like the hours on a clock face. Keep every arrow the same weight and the same dotted
pattern so no organ looks more important than another.

OUTPUT:
Square image, clean margins, high resolution, publication-grade medical icon aesthetic. Include a
small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner, not
obscuring the sigil.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, extra labels, dark background, neon colors, crowded
or crossing arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic lighting. One-way
arrows are wrong: every arrow has two heads. Use only Inter. Never omit the attribution.

QUALITY CHECK:
Nine labels, all spelled correctly. Two kidneys. Eight double-headed arrows. Light background.
```

### 004 · Post-AKI timeline (both tabs)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-02-post-aki-timeline.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: After a sudden kidney injury there is a 3-month recovery window that ends with a kidney check.

PROMPT:
Medical step-sequence infographic, AJKD/NEJM graphical abstract style, soft semi-3D illustrated
(not flat clip-art). White (#ffffff) background. Title at top in bold navy (#0f1e2e) Inter:
"After a sudden kidney injury". Subtitle in clinical teal (#1a6b72): "The first 3 months".

One horizontal timeline arrow runs left to right across the middle. Three stations along it, each
a rounded card on soft gray (#f3f4f6) with a small illustration above:
1. Left card, labeled "Hospital stay": a hospital bed icon beside a kidney shown slightly inflamed
   in muted red. Small caption: "Sudden kidney injury".
2. Middle card, labeled "Recovery window": a kidney fading from muted red to healthy red-brown,
   with a small calendar icon. Small caption: "Healing can continue for weeks".
3. Right card, labeled "3-month kidney check": a healthy kidney with a teal flag planted beside
   it, a blood sample tube and a urine sample cup. Small caption: "Blood test + urine albumin test".
Above the right-hand third of the arrow, an amber (#b8860b) rounded tag: "Go sooner if advised".

Bottom strip in navy text on light teal tint (#eef6f7): "A check-up shows whether the kidneys have
recovered or need continued care." Ample negative space, mobile-readable labels.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy,
overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal or black backgrounds.
Use ONLY Inter. No percentages or statistics. Never omit the attribution.

QUALITY CHECK:
Three stations only. The number "3" appears only in "3 months" and "3-month". Light background.
Attribution bottom-right.
```

### 005 · Five channels and the five-step template (clinician)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-03-five-channels.png
IMAGE TYPE: Simple figure — Scaffold D single mechanism / one-panel poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Kidney-organ signals travel through five channels, and each pathway can be written in five steps.

PROMPT:
Medical pathophysiology infographic, AJKD/NEJM graphical abstract style, soft semi-3D rendering.
White (#ffffff) background. Title at top in bold navy (#0f1e2e) Inter: "Five channels of
kidney-organ crosstalk". Subtitle in clinical teal (#1a6b72): "One template for every pathway".

Upper two-thirds: a semi-photorealistic kidney on the left and a soft gray silhouette labeled
"Distant organ" on the right. Between them, five parallel horizontal bands, each a different soft
color with a two-headed arrow and a small icon, labeled top to bottom:
"Pressure and flow" (warm red band, small pressure-gauge icon),
"Hormones" (teal band, small droplet icon),
"Nerves" (amber band, small nerve-fiber icon),
"Metabolite handling" (green band, small filter icon),
"Immune signals" (purple band, small white-cell icon).

Lower third: a five-box horizontal strip on soft gray (#f3f4f6) joined by small teal arrows,
numbered 1 to 5: "1 Source tissue" → "2 Route or mediator" → "3 Target" → "4 Response" →
"5 Feedback", with a thin curved arrow returning from box 5 to box 1.

Ample negative space, no clutter, mobile-readable labels.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy,
HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Do not add molecule names,
statistics or extra bands. Never omit the attribution.

QUALITY CHECK:
Exactly five bands and five numbered boxes, labels spelled as written. Light background.
```

### 006 · Cardiorenal: forward flow versus congestion (clinician)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-04-cardiorenal-congestion-forward-flow.png
IMAGE TYPE: Biomedical mechanism figure, two-panel comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A failing heart lowers kidney filtration by two different routes that need different treatment.

PROMPT:
Create a publication-grade biomedical mechanism schematic about:

Topic: How heart failure lowers kidney filtration
Disease context: Heart failure with worsening kidney function
Central mechanism: Filtration depends on the pressure difference across the kidney; it falls when
inflow drops or when outflow pressure rises.

Layout: two side-by-side panels separated by a thin dashed vertical line, review-article style,
flat vector anatomy with soft semi-3D shading, white background, Inter typography.

Left panel, header "Low forward flow": a heart with a weak, small output arrow in red leading
through the aorta and renal artery to a kidney. The renal artery is drawn thin and pale. Inside a
dashed magnified inset, one glomerulus with a narrow afferent arteriole. Callouts: "↓ Cardiac
output", "↓ Renal perfusion", "↓ Filtration pressure".

Right panel, header "Venous congestion": a heart with a dilated right side; the inferior vena cava
and renal vein are drawn wide and deep blue with small arrows pushing back toward the kidney. The
kidney looks slightly swollen within its capsule. Inside a dashed magnified inset, one glomerulus
with a distended efferent side and compressed tubules. Callouts: "↑ Central venous pressure",
"↑ Renal venous and interstitial pressure", "↓ Filtration gradient".

Bottom summary flow across both panels: left pale pink box "Both lower filtration and raise
creatinine" → center box "Read with congestion, perfusion, urine output and time course" → right
pale blue box "Different pathway, different next step".

Use a white background, muted clinical colors (red for arterial, blue for venous, light gray-blue
anatomy), thin dashed connector lines, and a review-article figure style.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, gibberish text. Do not
show congestion in the artery. No numeric pressures, no drug names. Use ONLY Inter.

QUALITY CHECK:
Arterial problem on the left, venous problem on the right. Renal vein drains toward the vena
cava. Callout arrows point the correct way. Light background. Attribution bottom-right.
```

### 007 · Hepatorenal hemodynamics (clinician)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-05-hepatorenal-hemodynamics.png
IMAGE TYPE: Biomedical mechanism figure
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: In advanced cirrhosis, gut vasodilation triggers vasoconstrictor systems that narrow the kidney arterioles.

PROMPT:
Create a publication-grade biomedical mechanism schematic about:

Topic: Hemodynamic basis of hepatorenal syndrome
Disease context: Advanced cirrhosis with ascites
Central mechanism: Splanchnic vasodilation lowers effective arterial volume; compensating
vasoconstrictor systems reduce renal perfusion.

Organ-level panel (left): a small, nodular cirrhotic liver with a congested portal vein, and
below it widened, relaxed gut (splanchnic) arteries drawn in soft red. A pale blue pool under the
liver labeled "Ascites". Disease label: "Cirrhosis with portal hypertension". A dashed connector
box points to the magnified panel.

Magnified mechanism panel (center/right, dashed border): a kidney in cross-section with one
enlarged afferent arteriole shown tightly narrowed, highlighted in pale yellow. Concise callouts:
- "↓ Effective arterial volume"
- "↑ Renin-angiotensin-aldosterone system"
- "↑ Sympathetic tone and vasopressin"
- "Renal vasoconstriction → ↓ Filtration"

Bottom summary flow: left pale pink box "Drivers: splanchnic vasodilation, inflammation, infection"
→ center box "Bridge: vasoconstrictor activation" → right pale blue box "Consequence: sodium
retention, falling filtration".

Small corner note in gray: "Tubular injury and congestion can coexist".

Use a white background, muted clinical colors, clean sans-serif labels set in Inter, thin dashed
connector lines, review-article figure style, soft semi-3D shading.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, gibberish text. No drug
names, no doses, no laboratory thresholds. Use ONLY Inter.

QUALITY CHECK:
Liver nodular and smaller than normal; gut vessels wide, kidney arteriole narrow. All four
callouts present and spelled correctly. Light background.
```

### 008 · Gut, liver, kidney: three steps for a retained solute (clinician)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-06-gut-liver-kidney-solutes.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A gut-derived solute is generated, processed and cleared in three organs, and each step is a separate target.

PROMPT:
Medical step-sequence infographic, AJKD/NEJM graphical abstract style, soft semi-3D illustrated.
White (#ffffff) background. Title at top in bold navy (#0f1e2e) Inter: "Gut-derived solutes: three
steps, three targets". Subtitle in clinical teal (#1a6b72): "Generation, processing, clearance".

Three large stations left to right joined by teal arrows, each with a semi-3D organ above a
rounded card on soft gray (#f3f4f6):
1. "1 Generation — gut": a segment of colon with small rod-shaped bacteria. Card text: "Bacteria
   convert dietary amino acids to indole and p-cresol".
2. "2 Processing — liver": a liver. Card text: "Liver adds sulfate: indoxyl sulfate, p-cresyl
   sulfate".
3. "3 Clearance — kidney": a kidney with one magnified proximal tubule. Card text: "Tubular
   secretion into urine".
Under station 3, a second, paler kidney with a dimmed tubule and an amber (#b8860b) tag: "CKD:
secretion falls, blood levels rise".

Bottom strip, navy text on light teal tint (#eef6f7): "Trials aimed at each step changed solute
levels; none has improved patient outcomes." A small two-person icon sits beside the sentence to
mark human evidence.

Ample negative space, mobile-readable labels.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, chemical structures,
unrealistic anatomy, HDR. NEVER use dark backgrounds. Use ONLY Inter. No statistics or trial names.

QUALITY CHECK:
Three numbered stations in the order gut, liver, kidney. "p-cresyl sulfate" and "indoxyl sulfate"
spelled correctly. Light background. Attribution bottom-right.
```

### 009 · Bone, parathyroid, kidney, heart: evidence-coded FGF23 loop (clinician)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-07-bone-kidney-heart-fgf23-loop.png
IMAGE TYPE: Organ crosstalk sigil, evidence-coded
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1536 × 1536
AUDIENCE: clinicians
VISUAL GOAL: The mineral loop between bone, parathyroid and kidney is established; the link from bone to heart is experimental.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring:

ORGANS:
- a long bone (top)
- a pair of kidneys (lower left)
- a small parathyroid gland icon beside a thyroid outline (lower right)
- a heart (center, slightly smaller)

RELATIONSHIP:
Three SOLID teal (#1a6b72) dotted-loop arrows form a triangle between bone, kidneys and
parathyroid: bone → kidneys labeled "FGF23", kidneys → parathyroid labeled "Calcitriol",
parathyroid → bone labeled "PTH". One DASHED purple (#6c3d8e) arrow runs from the bone to the
heart, labeled "FGF23 → hypertrophy", with a small flask icon beside it.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette with one purple accent,
white background, clean rounded organ shapes, balanced composition, generous whitespace, no
photorealism, no 3D. All labels in Inter, navy (#0f1e2e). Under the diagram, a two-item legend in
small type: a solid teal line "Established physiology" and a dashed purple line with a flask
"Experimental; human association only".

COMPOSITION:
Triangle of bone (top), kidneys (lower left) and parathyroid (lower right) with the heart at the
center. The dashed arrow is visibly different from the three solid arrows.

OUTPUT:
Square image, clean margins, high resolution. Small, semi-transparent "renalcarematters.com"
attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, dark background, neon colors, crowded arrows, thick cartoon
outlines, 3D rendering. The bone-to-heart arrow must NOT be solid. No statistics. Use only Inter.

QUALITY CHECK:
Three solid arrows, one dashed arrow, flask icon present, legend present, four labels spelled as
written. Parathyroid drawn at the neck, not on the kidney.
```

### 010 · Erythropoietin, hepcidin and iron (clinician)

```
FILE NAME: interorgan-crosstalk-kidney-health-disease-08-epo-hepcidin-iron.png
IMAGE TYPE: Biomedical mechanism figure
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Red cell production in kidney disease depends on two signals: erythropoietin drives it and hepcidin restricts its iron supply.

PROMPT:
Create a publication-grade biomedical mechanism schematic about:

Topic: Why chronic kidney disease causes anemia
Disease context: Chronic kidney disease
Central mechanism: Less erythropoietin from the kidney, and iron restricted by hepcidin from the
liver.

Organ-level panel (left): a kidney releasing a few small teal capsules labeled "Erythropoietin"
into a blood vessel, with a label "↓ in CKD". Below it, a liver releasing small amber capsules
labeled "Hepcidin", with a label "↑ with inflammation, ↓ renal clearance".

Magnified mechanism panel (center/right, dashed border): a cross-section of bone marrow with
erythroid precursor cells maturing into red cells from left to right. Above the marrow, a
macrophage (storage cell) holding iron as small rust-colored dots behind a closed gate labeled
"Ferroportin blocked". A thin, reduced stream of iron dots reaches the marrow. Concise callouts:
- "↓ Erythropoietin signal"
- "↑ Hepcidin → iron trapped in storage"
- "↓ Iron delivered to marrow"
- "↓ Red cell production"

Bottom summary flow: left pale pink box "Drivers: reduced kidney oxygen-sensing output,
inflammation, blood loss" → center box "Check hemoglobin with ferritin and TSAT" → right pale blue
box "Treat the limiting step".

Use a white background, muted clinical colors, clean sans-serif labels set in Inter, thin dashed
connector lines, review-article figure style with soft semi-3D shading.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, gibberish text. No drug
names, no doses, no laboratory thresholds. Use ONLY Inter.

QUALITY CHECK:
Erythropoietin comes from the kidney and hepcidin from the liver, never reversed. "Ferroportin"
and "Hepcidin" spelled correctly. Light background. Attribution bottom-right.
```

### 011 and 012 · Calculator OG cards (optional)

```
FILE NAME: calc-post-aki-followup-og.png  /  calc-vexus-grading-og.png
IMAGE TYPE: OG / social share card
PIXEL DIMENSIONS: 1200 × 630 (fixed)
AUDIENCE: clinicians

PROMPT (011):
Social share card, 1200 × 630, off-white (#fafafa) background. Left 60%: title in bold navy
(#0f1e2e) Inter, two lines: "Post-AKI Follow-Up" / "Planner". One teal (#1a6b72) line below:
"The 3-month kidney check, dated". Right 40%: a soft semi-3D kidney beside a desk calendar with
one day circled in teal and a small checklist card with four tick boxes. Bottom-right:
"renalcarematters.com" in small semi-transparent navy text.

PROMPT (012):
Social share card, 1200 × 630, off-white (#fafafa) background. Left 60%: title in bold navy
(#0f1e2e) Inter, two lines: "VExUS Grading" / "Worksheet". One teal (#1a6b72) line below: "Venous
congestion, documented". Right 40%: a soft semi-3D handheld ultrasound probe beside three small
stylized Doppler waveform tiles in teal, blue and amber. Bottom-right: "renalcarematters.com" in
small semi-transparent navy text.

NEGATIVE INSTRUCTIONS (both):
NEVER use dark backgrounds. Use ONLY Inter. No statistics. No author name. Exactly 1200 × 630.
```

### 013 · The barangay of organs (patient analogy, walked back to anatomy)

```
IMAGE NUMBER: 013
SECTION PLACEMENT: #p-start, first figure, before the organ hub
FILE NAME: interorgan-crosstalk-kidney-health-disease-09-barangay-of-organs.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side (analogy beside real anatomy)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
PICTURE-ONLY MESSAGE: Neighbors who depend on each other; organs that depend on each other.
VISUAL GOAL: The body works like a neighborhood where every household relies on the others, and the kidneys are one of those households.

PROMPT:
Medical education comparison infographic, soft semi-3D illustrated style (not flat clip-art, not
cartoon). White (#ffffff) background. Title centered at top in bold navy (#0f1e2e) Inter: "Your
organs are neighbors". A soft dashed vertical divider splits the canvas into two equal panels.

Left panel, labeled in clinical teal (#1a6b72): "A neighborhood". A warm, tidy Philippine barangay
street seen from slightly above: five small houses with tin roofs and potted plants, a shared water
pump at the center, and thin dotted footpaths linking every house to the others. Each house has a
simple sign icon above its door (a heart, a pair of lungs, a liver, a bone, and a pair of kidneys on
the house beside the water pump). No people.

Right panel, labeled in clinical teal: "Your body". The same five organs drawn as soft semi-3D
anatomy in the same positions as the houses, with the pair of kidneys in the same place as the
water-pump house, and thin dotted two-way teal arrows linking every organ, matching the footpaths.

One wide, pale teal curved arrow at the bottom runs from the left panel to the right panel with the
words "Same idea".

Bottom strip, navy text on light teal tint (#eef6f7): "When one neighbor struggles, the others feel
it." Ample negative space, large labels.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon characters, organs with faces, talking organs, clutter, tiny labels, AI gibberish
text, poverty imagery, dark or moody lighting, HDR. NEVER use dark backgrounds. Use ONLY Inter.
No more than five houses and five organs. Never omit the attribution.

QUALITY CHECK:
Cover the words: the two panels still mirror each other. Kidneys are a pair. House positions match
organ positions. Three text items only, spelled as written. Light background.
```

### 014 · Family at the clinic visit (patient)

```
IMAGE NUMBER: 014
SECTION PLACEMENT: #p-visit
FILE NAME: interorgan-crosstalk-kidney-health-disease-10-family-clinic-visit.png
ARCHETYPE: Infographic skill — 1. Photorealistic editorial hero
VISUAL MIX: photorealistic models: yes · 2D infographic: none · 3D components: none · algorithm: none
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
PICTURE-ONLY MESSAGE: Bring your questions and your family; the doctor listens.
VISUAL GOAL: Make asking questions at a kidney visit feel normal and welcome.

PROMPT:
Photorealistic medical editorial image for a nephrology education guide. A Filipino woman
nephrologist in her forties, white coat over a plain blouse, sits beside (not behind) a small desk
in a bright, modest clinic room, leaning slightly toward a Filipino man in his late sixties and his
adult daughter. The older man holds a small notebook with handwritten lines and is pointing to one
of them; the daughter holds a clear folder of laboratory papers. The doctor is listening, pen down.
On the desk: a simple anatomical model of a kidney and a blood pressure cuff. Soft daylight from a
window on the left, white walls, a potted plant. Premium healthcare publication aesthetic, natural
skin texture, calm and attentive expressions, shallow depth of field, navy and teal accents in
clothing and furnishings, clean uncluttered background, mobile-safe crop with the three faces in
the central two-thirds of the frame.
No readable text anywhere in the scene. Bottom-right: "renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid generic stock-photo look, staged smiles at the camera, cartoon style, dark or moody lighting,
HDR, excessive saturation, distorted hands, extra fingers, readable brand names, logos, drug names,
hospital branding, celebrity likeness. No text overlays except the attribution.

QUALITY CHECK:
Three people, five-fingered hands, doctor at eye level with the patient, notebook visible. Bright
room. No legible writing. Attribution present.
```

### 015 · Eight partners of the kidneys (patient)

```
IMAGE NUMBER: 015
SECTION PLACEMENT: #p-organs, above the organ table
FILE NAME: interorgan-crosstalk-kidney-health-disease-11-eight-partner-cards.png
ARCHETYPE: Infographic skill — 4. Multi-panel educational infographic
VISUAL MIX: photorealistic models: none · 2D infographic: cards and icons · 3D components: organs · algorithm: none
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
PICTURE-ONLY MESSAGE: Eight organs, each sharing one job with the kidneys.
VISUAL GOAL: A picture index of the organ table: what each partner shares with the kidneys.

PROMPT:
Patient education infographic poster, landscape 16:9, modern nephrology clinic aesthetic, soft
semi-3D illustrated. Clean white (#ffffff) background. Top header in bold navy (#0f1e2e) Inter:
"Eight partners of your kidneys".

Below it, eight equal rounded cards in two rows of four on soft gray (#f3f4f6), each with a thin
teal (#1a6b72) top band. Every card shows a small pair of kidneys on the left, a two-way teal arrow,
and one partner organ in soft semi-3D on the right, with a bold one-word title and one short line:
1. "Heart" — "Blood flow and pressure"
2. "Lungs" — "Acid balance"
3. "Liver" — "Food and medicines"
4. "Gut" — "What bacteria make"
5. "Bones" — "Calcium and vitamin D"
6. "Blood" — "Red blood cells"
7. "Brain" — "Nerve signals"
8. "Muscles" — "Creatinine"

Bottom take-home strip, navy text on light teal tint (#eef6f7): "Each one helps the kidneys. The
kidneys help each one." Generous spacing, large labels readable on mobile.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, HDR,
excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Exactly eight cards. No extra
text, no statistics, no abbreviations. Never omit the attribution.

QUALITY CHECK:
Eight cards, eight titles and eight lines spelled as written. Every arrow has two heads. Kidneys
drawn as a pair in every card.
```

### 016 · Same number, two stories (patient)

```
IMAGE NUMBER: 016
SECTION PLACEMENT: #p-change, first figure
FILE NAME: interorgan-crosstalk-kidney-health-disease-12-same-number-two-stories.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
PICTURE-ONLY MESSAGE: Two people with the same test result need opposite treatment.
VISUAL GOAL: The same rising creatinine can come from too much fluid or too little, so the doctor looks at the whole person.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical abstract style, soft semi-3D
illustrated. White (#ffffff) background. Title centered at top in bold navy (#0f1e2e) Inter: "Same
test result, two different stories". Soft dashed vertical divider splitting the canvas into two
equal panels. At the very top center, straddling the divider, ONE shared laboratory slip icon with
an upward arrow and the words "Creatinine up", with thin lines dropping from it into both panels.

Left panel, header in muted blue: "Too much fluid". A simple, respectful semi-3D figure of an adult
Filipino man sitting upright, with visibly swollen lower legs and ankles shaded pale blue, a hand on
his chest, and pale blue shading at the base of both lungs. Three icon labels: "Swollen legs",
"Short of breath", "Weight going up". At the bottom of the panel, a teal (#1a6b72) rounded tag:
"Fluid needs to come off".

Right panel, header in amber (#b8860b): "Too little fluid". The same style of figure, an adult
Filipino woman standing and steadying herself on a chair, with dry lips and a slightly sunken look,
an empty water glass beside her. Three icon labels: "Dizzy on standing", "Dry mouth", "Very little
urine". At the bottom of the panel, a teal rounded tag: "Fluid needs to be given".

Bottom strip, navy text on light teal tint (#eef6f7): "Your doctor reads the number together with
your body." Rounded panel corners, ample negative space, large labels.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, frightening or undignified depictions, clutter, tiny labels, AI gibberish
text, any number or laboratory value, drug names, HDR. NEVER use dark backgrounds. Use ONLY Inter.
Do not make one panel "good" and the other "bad"; both are problems. Never omit the attribution.

QUALITY CHECK:
One shared lab slip feeding both panels. Swelling on the left only, dryness on the right only. No
digits anywhere. Two teal tags with opposite actions.
```

### 017 · Tests as windows (patient)

```
IMAGE NUMBER: 017
SECTION PLACEMENT: #p-tests
FILE NAME: interorgan-crosstalk-kidney-health-disease-13-tests-as-windows.png
IMAGE TYPE: Simple figure — Scaffold E quick-look card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
PICTURE-ONLY MESSAGE: Each test looks at a different organ partnership.
VISUAL GOAL: Six common tests, each shown as a window onto one kidney partnership.

PROMPT:
Clinical reference card for patients, publication-grade nephrology design, soft semi-3D
illustrated. White (#ffffff) background. Bold navy (#0f1e2e) title at top in Inter: "Six windows
into how your organs get along".

A grid of six rounded window-shaped cards, three across and two down, on soft gray (#f3f4f6). Each
card has a simple window frame in teal (#1a6b72); through the window we see a small semi-3D scene,
and under the window a bold label with one short line:
1. Through the window: a blood sample tube beside a kidney. Label "Creatinine and eGFR" — "How well
   the kidneys filter".
2. A urine sample cup beside a kidney. Label "Urine albumin" — "Protein leaking out".
3. A blood pressure cuff and a weighing scale beside a heart. Label "Blood pressure and weight" —
   "Fluid balance".
4. A heartbeat line beside a heart. Label "Potassium and bicarbonate" — "Heart rhythm and acid".
5. Red blood cells beside a bone cut to show marrow. Label "Hemoglobin and iron" — "Blood making".
6. A long bone beside a small gland in the neck. Label "Calcium, phosphate, PTH" — "Bone health".

Footer, navy on light teal tint (#eef6f7): "No single test shows the whole picture." Large labels,
not cluttered.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, any numeric value or
normal range, HDR. NEVER use dark backgrounds. Use ONLY Inter. Exactly six windows. Never omit the
attribution.

QUALITY CHECK:
Six windows with the six labels spelled as written. "eGFR" and "PTH" are the only abbreviations and
both are expanded in the guide's caption. No digits.
```

### 018 · One habit, many organs (patient)

```
IMAGE NUMBER: 018
SECTION PLACEMENT: #p-protect
FILE NAME: interorgan-crosstalk-kidney-health-disease-14-one-habit-many-organs.png
ARCHETYPE: Infographic skill — 8. Circular workflow / cycle
VISUAL MIX: photorealistic models: none · 2D infographic: ring of icons · 3D components: three organs · algorithm: none
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients and families
PICTURE-ONLY MESSAGE: Everyday habits on the outside protect three organs on the inside.
VISUAL GOAL: Six habits protect the kidneys, heart and brain at the same time.

PROMPT:
Circular patient education infographic, polished nephrology systems diagram, soft semi-3D
illustrated. White (#ffffff) background. Title at top in bold navy (#0f1e2e) Inter: "One habit
protects many organs".

Center: three semi-3D organs grouped closely inside a soft green (#1f7a4d) protective ring, a pair
of kidneys in front, a heart behind on the left, a brain behind on the right.

Around the ring, six evenly spaced round icon badges, each with a thin green arrow pointing inward
to the ring and a short label beneath:
"Control blood pressure" (cuff icon), "Control blood sugar" (glucose meter icon), "Less salt" (salt
shaker with a small downward arrow), "Stay active" (walking shoes icon), "No smoking" (cigarette
with a slash), "Vaccines up to date" (small vial and shield icon).

Clean labels, strong hierarchy, generous whitespace, readable on mobile.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, food brand imagery, drug
names, HDR, neon gradients. NEVER use dark backgrounds. Use ONLY Inter. Exactly six badges. Never
omit the attribution.

QUALITY CHECK:
Six badges, six labels spelled as written, all arrows pointing inward. Kidneys are a pair. No
digits.
```

### 019 · Warning signs: go to the emergency room (patient)

```
IMAGE NUMBER: 019
SECTION PLACEMENT: Directly after the red urgent-care alert at the top of the patient tab
FILE NAME: interorgan-crosstalk-kidney-health-disease-15-warning-signs.png
IMAGE TYPE: Simple figure — Scaffold E quick-look card
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families, including readers who do not read English
PICTURE-ONLY MESSAGE: These eight body signs mean go to the hospital now.
VISUAL GOAL: A reader who cannot read the alert text can still recognize the danger signs from pictures.

PROMPT:
Clinical safety quick-look card for patients, publication-grade nephrology design, soft semi-3D
illustrated pictograms. White (#ffffff) background. A red (#b91c1c) rounded header band at the top
with white bold Inter text: "Go to the emergency room now", and a small hospital cross-in-a-house
icon at its left.

Below, eight large, clear pictogram tiles in two rows of four on soft gray (#f3f4f6), each a simple
respectful human figure or body part showing ONE sign, with a short navy (#0f1e2e) label:
1. A person lying flat, hand on chest, struggling to breathe — "Hard to breathe lying down"
2. A person clutching the center of the chest — "Chest pain"
3. A nearly empty urine container — "Very little or no urine"
4. Two lower legs, visibly swollen — "Sudden swelling"
5. A person looking confused, with a small swirl beside the head — "Confusion or unusual sleepiness"
6. A person slumping, supported by a relative — "Fainting"
7. A toilet with a dark stool symbol and a small red drop — "Black stool or vomiting blood"
8. A heart with an uneven, rapid rhythm line — "Very fast or uneven heartbeat"

Thin red outline around each tile. Generous spacing, labels large enough for a phone.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid gore, graphic blood, frightening imagery, cartoon style, clutter, tiny labels, AI gibberish
text, any treatment advice, any drug name, any number. The only filled dark area is the red header
band; the canvas itself must stay white. Use ONLY Inter. Exactly eight tiles. Never omit the
attribution.

QUALITY CHECK:
Cover the labels: each of the eight signs is still recognizable. Header reads exactly "Go to the
emergency room now". No advice other than the header. No digits.
```

### 020 · The medicine bag check (patient)

```
IMAGE NUMBER: 020
SECTION PLACEMENT: #p-protect, beside the "Do this" alert
FILE NAME: interorgan-crosstalk-kidney-health-disease-16-medicine-bag-check.png
ARCHETYPE: Infographic skill — 1. Photorealistic editorial
VISUAL MIX: photorealistic models: hands only · 2D infographic: one small tag · 3D components: none · algorithm: none
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
PICTURE-ONLY MESSAGE: Bring everything you take, and ask before you take a pain reliever.
VISUAL GOAL: Show the habit of bringing every medicine and supplement to the visit.

PROMPT:
Photorealistic medical editorial image for a nephrology education guide, seen from above at a
gentle angle. On a clean light wooden clinic desk, an older Filipino patient's hands are emptying a
small woven bag: several plain white medicine boxes and blister packs with blank, unprinted
surfaces, one amber pill organizer, one plain bottle of herbal capsules, and one small sachet. A
clinician's hand opposite, with a pen, is checking them against a blank list. One blister pack of
round pain-reliever tablets is set slightly apart, and beside it sits a small amber (#b8860b) paper
tag with a question mark on it. Bright natural daylight, soft shadows, shallow depth of field,
calm and orderly mood, navy and teal accents (a teal folder edge, a navy pen).
No readable text on any package. Bottom-right: "renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
Avoid readable brand names, drug names, logos, doses or printed labels on any package. Avoid stock
photo blandness, clutter, dark or moody lighting, HDR, distorted hands, extra fingers, cartoon
style. No text overlays except the attribution and the single question mark.

QUALITY CHECK:
Every package is blank. Hands are anatomically correct. One blister pack is clearly separated with
the amber question-mark tag. Bright and uncluttered.
```

### 021 · Three questions of proof (both tabs)

```
IMAGE NUMBER: 021
SECTION PLACEMENT: #md-answer
FILE NAME: interorgan-crosstalk-kidney-health-disease-17-three-questions-of-proof.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
PICTURE-ONLY MESSAGE: Three stepping stones, from a clock to a laboratory to people.
VISUAL GOAL: A signal between organs counts as proven only after it passes three different tests.

PROMPT:
Clean clinical education infographic, soft semi-3D illustrated, white (#ffffff) background. Title
at top center in bold navy (#0f1e2e) Inter: "How we know one organ affects another". Subtitle in
clinical teal (#1a6b72): "Three questions, three kinds of proof".

Three rounded rectangular cards arranged horizontally in a single row on a very soft gray panel
(#f3f4f6), drawn as rising stepping stones from left to right and connected by bold navy
right-pointing arrows. Each card has a colored top accent band, an icon, a bold step label and one
line:
1. Amber band, clock-and-calendar icon. "1 Timing" — "What came first?"
2. Purple (#6c3d8e) band, laboratory flask icon. "2 Experiment" — "Does blocking the signal change
   the result in the laboratory?"
3. Green (#1f7a4d) band, two-person icon. "3 People" — "Does it happen in patients, and does
   treating it help them?"

Above the third card, a small green flag. Bottom strip, full-width soft gray, navy sentence:
"Finding a molecule in the blood does not show where it came from or whether treating it helps."
Generous whitespace, mobile-readable.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, statistics, trial names,
HDR. NEVER use dark backgrounds. Use ONLY Inter. Exactly three cards. Never omit the attribution.

QUALITY CHECK:
Cards numbered 1, 2, 3 and rising left to right. Flask on card 2 and two-person icon on card 3,
matching the icons used in figures 008, 009, 023 and 024. Text spelled as written.
```

### 022 · AKI, AKD and CKD on one time axis (clinician)

```
IMAGE NUMBER: 022
SECTION PLACEMENT: #md-timeline
FILE NAME: interorgan-crosstalk-kidney-health-disease-18-aki-akd-ckd-time-axis.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
PICTURE-ONLY MESSAGE: One line of time divided into three zones.
VISUAL GOAL: AKI, acute kidney disease and CKD are separated by time, and a shared insult can injure several organs at once.

PROMPT:
Clean clinical education infographic, soft semi-3D illustrated, white (#ffffff) background. Title
at top center in bold navy (#0f1e2e) Inter: "Three states separated by time".

One thick horizontal time axis across the middle with two vertical tick marks, labeled "7 days" and
"90 days". Three colored zones along the axis, each with a kidney above it:
- Left zone, amber (#b8860b) band, kidney shown acutely inflamed: "Acute kidney injury" — "Abrupt
  fall in function".
- Middle zone, teal (#1a6b72) band, kidney shown half-recovered with a small branching arrow above
  it splitting into "Recovery" (green, upward) and "Persistent dysfunction" (amber, level): "Acute
  kidney disease".
- Right zone, navy band, kidney shown smaller and paler: "Chronic kidney disease" — "Abnormality
  beyond 90 days".

At the far left, before the axis, a red (#b91c1c) starburst labeled "Insult" with three thin red
arrows fanning out to a small lung, a small heart and the first kidney, and a small gray note:
"A shared insult is not crosstalk".

Bottom strip, soft gray, navy sentence: "Reassess at 3 months: function, urine albumin, blood
pressure." Generous whitespace, mobile-readable.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, hazard ratios or any other
statistic, HDR. NEVER use dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
The only digits are "7 days", "90 days" (twice) and "3 months". Three zones in the order injury,
disease, chronic. The insult arrows reach three organs.
```

### 023 · Lung and kidney: two kinds of edema (clinician)

```
IMAGE NUMBER: 023
SECTION PLACEMENT: #md-lung
FILE NAME: interorgan-crosstalk-kidney-health-disease-19-lung-kidney-two-edemas.png
IMAGE TYPE: Biomedical mechanism figure, two-panel comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
PICTURE-ONLY MESSAGE: Water pushed into the air sacs by pressure on one side, leaking through damaged walls on the other.
VISUAL GOAL: Separate the established fluid route from kidney to lung from the experimental permeability route, and show the return path from ventilation to kidney.

PROMPT:
Create a publication-grade biomedical mechanism schematic about:

Topic: How kidney injury affects the lung, and how the lung affects the kidney
Disease context: Acute kidney injury in critical illness
Central mechanism: Positive fluid balance causes hydrostatic pulmonary edema; in animal models,
circulating cytokines also raise capillary permeability.

Layout: two side-by-side panels separated by a thin dashed vertical line, with a slim strip
underneath spanning both. Soft semi-3D shading, white background, Inter typography.

Left panel, header "Hydrostatic edema" with a small two-person icon: a kidney with a reduced urine
stream and a teal SOLID arrow labeled "Retained salt and water" leading to a lung. Dashed magnified
inset of one alveolus and its capillary: the capillary is distended, its wall intact, clear fluid
pushed into the air space. Callouts: "↑ Capillary pressure", "Intact barrier", "Fluid overload".

Right panel, header "Permeability edema" with a small flask icon: a kidney with a purple (#6c3d8e)
DASHED arrow labeled "Circulating cytokines" leading to a lung. Dashed magnified inset of one
alveolus: normal-width capillary with visible gaps in its wall, protein-rich fluid and a few white
cells in the air space. Callouts: "Leaky barrier", "↓ Alveolar fluid clearance", "Animal models".

Return strip under both panels: a ventilator icon and a lung on the left, a solid teal arrow to a
kidney on the right, labeled "Hypoxemia and positive-pressure ventilation → altered renal
perfusion and venous pressure".

Use a white background, muted clinical colors, thin dashed connector lines, review-article figure
style. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, gibberish text. The right
panel arrow must be dashed purple, never solid. No statistics, no drug names. Use ONLY Inter.

QUALITY CHECK:
Left arrow solid with two-person icon, right arrow dashed with flask icon. Barrier intact on the
left, gapped on the right. Return arrow runs lung to kidney.
```

### 024 · Brain and kidney: the nerve loop (clinician)

```
IMAGE NUMBER: 024
SECTION PLACEMENT: #md-brain
FILE NAME: interorgan-crosstalk-kidney-health-disease-20-brain-kidney-nerve-loop.png
IMAGE TYPE: Organ crosstalk sigil, evidence-coded
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1536 × 1536
AUDIENCE: clinicians
PICTURE-ONLY MESSAGE: A two-way wire between brain and kidney, plus one uncertain link.
VISUAL GOAL: Efferent and afferent renal nerves form an established loop; kidney-to-brain inflammation is experimental.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring:

ORGANS:
- a brain with a short brainstem (top)
- a pair of kidneys (bottom)

RELATIONSHIP:
Two SOLID teal (#1a6b72) dotted-loop arrows form a vertical loop on the left side: one running
down from the brainstem to the kidneys labeled "Efferent sympathetic nerves", and one running up
from the kidneys to the brainstem labeled "Afferent renal nerves". On the right side, one DASHED
purple (#6c3d8e) arrow runs up from the kidneys to the brain, labeled "Retained solutes and
inflammation", with a small flask icon beside it.

Beside the kidneys, three tiny line icons with one-word labels: a vessel "Tone", a droplet "Renin",
a salt crystal "Sodium".

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette with one purple accent,
white background, clean rounded organ shapes, balanced vertical composition, generous whitespace,
no photorealism, no 3D. All labels in Inter, navy (#0f1e2e). Under the diagram, a two-item legend
in small type: a solid teal line "Established physiology" and a dashed purple line with a flask
"Experimental".

OUTPUT:
Square image, clean margins, high resolution. Small, semi-transparent "renalcarematters.com"
attribution in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, dark background, neon colors, crowded arrows, thick cartoon outlines,
3D rendering. The right-hand arrow must NOT be solid. No statistics. Use only Inter.

QUALITY CHECK:
Two solid arrows in opposite directions, one dashed arrow with a flask, legend present. Kidneys are
a pair. Labels spelled as written.
```

### 025 · The creatinine trap: same filtration, different muscle (both tabs)

```
IMAGE NUMBER: 025
SECTION PLACEMENT: #md-muscle (also suitable for the Muscles row in #p-organs)
FILE NAME: interorgan-crosstalk-kidney-health-disease-21-muscle-creatinine-trap.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
PICTURE-ONLY MESSAGE: Two people with identical kidneys; the one with less muscle has a lower gauge reading.
VISUAL GOAL: Creatinine comes from muscle, so a person with little muscle can have a reassuring creatinine with the same reduced kidney function.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical abstract style, soft semi-3D
illustrated. White (#ffffff) background. Title centered at top in bold navy (#0f1e2e) Inter: "Same
kidney function, different creatinine". Soft dashed vertical divider splitting the canvas into two
equal panels.

Each panel shows, from top to bottom: a simple semi-3D adult figure, a thin arrow from the figure's
thigh muscle to a small pile of gray dots labeled "Creatinine made", a pair of kidneys, and a round
laboratory gauge.

Left panel, header in navy: "More muscle". A sturdy, muscular adult Filipino man. A LARGE pile of
gray dots. The kidneys are drawn with a small identical filter icon marked with two of four bars
filled. The gauge needle points high, labeled "Creatinine: higher".

Right panel, header in navy: "Less muscle". A thin, frail older Filipino woman with slender limbs.
A SMALL pile of gray dots. The kidneys and the two-of-four-bars filter icon are EXACTLY the same as
on the left. The gauge needle points low, labeled "Creatinine: lower".

A wide teal (#1a6b72) bracket joins the two identical kidney pairs across the divider, labeled
"Same filtration".

Bottom strip, navy text on light teal tint (#eef6f7): "A low creatinine does not always mean
healthy kidneys. Cystatin C depends less on muscle." Rounded corners, ample negative space.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, body-shaming or undignified depictions, clutter, tiny labels, AI gibberish
text, numeric laboratory values, HDR. NEVER use dark backgrounds. Use ONLY Inter. The two kidney
pairs must be identical. Never omit the attribution.

QUALITY CHECK:
Kidneys and filter icons identical in both panels. Dot piles clearly different in size. Gauge
high on the left, low on the right. No digits.
```

### 026 · One prescription, several organs (both tabs)

```
IMAGE NUMBER: 026
SECTION PLACEMENT: #md-shared
FILE NAME: interorgan-crosstalk-kidney-health-disease-22-one-prescription-several-organs.png
IMAGE TYPE: Simple figure — Scaffold D single mechanism / one-panel poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
PICTURE-ONLY MESSAGE: One tablet in the middle with protective arrows to the kidneys, heart and blood vessels.
VISUAL GOAL: The best-proven treatments in this field protect more than one organ, and that proof comes from trials in people.

PROMPT:
Medical education infographic, AJKD/NEJM graphical abstract style, soft semi-3D rendering. White
(#ffffff) background. Title at top in bold navy (#0f1e2e) Inter: "One prescription, several
organs". Subtitle in clinical teal (#1a6b72): "What trials in people have shown".

Center: a single plain, unbranded tablet resting on a small prescription pad with no writing.
Three SOLID green (#1f7a4d) arrows radiate from it to three semi-3D organs, each inside a soft
green shield outline with a rounded callout card:
- a pair of kidneys (left): "Slower loss of kidney function"
- a heart (upper right): "Fewer heart failure events"
- a short segment of artery (lower right): "Fewer cardiovascular deaths"

A small two-person icon sits beside each arrow to mark evidence from human trials.

Bottom strip, navy text on light teal tint (#eef6f7): "The benefit is proven. Which signal between
the organs explains it is still being worked out." Ample negative space, mobile-readable labels.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid brand names, drug names, molecule structures, logos, any readable writing on the tablet or
the pad, statistics, percentages, cartoon style, clutter, HDR. NEVER use dark backgrounds. Use ONLY
Inter. Never omit the attribution.

QUALITY CHECK:
Tablet and pad blank. Three solid arrows, three shields, three two-person icons. Callouts spelled
as written. No digits.
```

### 027 · VExUS grading card (clinician; proofread every digit)

```
IMAGE NUMBER: 027
SECTION PLACEMENT: #md-heart, and the Evidence section of calc-vexus-grading.html
FILE NAME: interorgan-crosstalk-kidney-health-disease-23-vexus-grading-card.png
IMAGE TYPE: Simple figure — Scaffold E reference table / quick-look card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
PICTURE-ONLY MESSAGE: One wide vein, then three waveforms that worsen from left to right.
VISUAL GOAL: Show the four inputs of the Venous Excess Ultrasound grade and how severe patterns add up.

PROMPT:
Clinical reference card, publication-grade nephrology design. White (#ffffff) background. Bold navy
(#0f1e2e) title at top in Inter: "VExUS grading at a glance".

Top row, one wide rounded card on soft gray (#f3f4f6): a simple side view of the inferior vena cava
entering the right atrium, with a caliper across it, and the text "Step 1: IVC diameter" and
"Under 2 cm = grade 0".

Below it, a compact grid with a header row and three body rows. Column headers in teal (#1a6b72):
"Vein", "Normal", "Mild", "Severe". Each body cell holds a small stylized Doppler waveform drawn as
a clean line above or below a baseline, plus a short caption:
- Row "Hepatic vein": "S larger than D" | "S smaller than D" | "S reversed"
- Row "Portal vein": "Pulsatility under 30%" | "30% to under 50%" | "50% or more"
- Row "Intrarenal vein": "Continuous" | "Two phases, interrupted" | "Diastolic only"
The "Severe" column has a pale red (#b91c1c at low opacity) tint and a thin red outline.

Bottom row, three rounded chips on soft gray: "No severe pattern = grade 1", "One severe pattern =
grade 2", "Two or more = grade 3".

Footer, small navy text: "Describes a congestion phenotype. Not an AKI probability." Alternating
soft row fills, not cluttered, mobile-readable.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, real ultrasound
screenshots, extra rows or columns, any other number. NEVER use dark backgrounds or black
ultrasound panels. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Read every character: "2 cm", "30%", "50%", grades "0", "1", "2", "3". Hepatic severe waveform
shows the S wave on the opposite side of the baseline. Three rows, four columns. If any digit or
caption is wrong, discard the image and rely on the HTML table in the calculator.
```

### 028 · Three cases: same numbers, different pathways (clinician)

```
IMAGE NUMBER: 028
SECTION PLACEMENT: #md-cases
FILE NAME: interorgan-crosstalk-kidney-health-disease-24-three-cases.png
ARCHETYPE: Infographic skill — 7. Case snapshot
VISUAL MIX: photorealistic models: none · 2D infographic: three case cards · 3D components: organ pairs · algorithm: none
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
PICTURE-ONLY MESSAGE: Three cards, each pairing the kidneys with a different organ and a question mark.
VISUAL GOAL: A visual index of the three teaching cases and the question each one turns on.

PROMPT:
Clinical case snapshot infographic, nephrology conference teaching style, soft semi-3D medical
objects. White (#ffffff) background. Title at top in bold navy (#0f1e2e) Inter: "Three cases, one
question: which pathway is active?".

Three modular case cards side by side on soft gray (#f3f4f6), each with a teal (#1a6b72) header
band, one visual component, and a teaching line:
1. Header "Case 1 · Heart failure". Visual: a heart and a pair of kidneys with a diuretic drip
   icon. Two small tags: green "Congestion improving" and amber "Perfusion falling". Teaching line:
   "Same creatinine. The bedside decides."
2. Header "Case 2 · Cirrhosis". Visual: a nodular liver, a pair of kidneys, and a thin, low-muscle
   arm outline. Tag in amber: "Creatinine understates the fall". Teaching line: "Exclude other
   causes. Check oxygen before a vasoconstrictor."
3. Header "Case 3 · After AKI, with anemia". Visual: a pair of kidneys, a bone showing marrow, and
   an iron storage icon. Tag in teal: "Stage only after chronicity". Teaching line: "Pair
   hemoglobin with iron tests."

Bold headings, concise text, clean icons, generous spacing, mobile-readable.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, laboratory values, drug
names, doses, patient faces, HDR. NEVER use dark backgrounds. Use ONLY Inter. Exactly three cards.
Never omit the attribution.

QUALITY CHECK:
Three cards in the order heart failure, cirrhosis, after AKI. The only digits are the case numbers
1, 2, 3. Text spelled as written.
```

---

## Part C — Wire-in manifest and suggested captions

**Already referenced in the guide:** 001 to 010. Save each PNG with a WebP twin in `images/`, then run `patch_responsive_images.py --guide interorgan-crosstalk-kidney-health-disease.html`, `patch_og_images.py --guide interorgan-crosstalk-kidney-health-disease.html` and `generate_latest_guides.py`.

**New in v2.0 (013 to 028):** each needs a `<figure>` block added to the section named in A.6. Suggested English captions follow; patient captions also need Tagalog, Cebuano and Kapampangan versions.

| # | Alt text (what the image shows) | Caption (`fig-desc`) | Abbreviations |
|---|---|---|---|
| 013 | Two matching panels: a neighborhood of five houses linked by footpaths, and five organs linked by arrows in the same positions | Your organs depend on each other the way neighbors do. When one struggles, the others feel it. | none |
| 014 | A doctor listening to an older man and his daughter, who are holding a notebook of questions and a folder of test results | Write your questions down and bring someone with you. A good visit is a conversation. | none |
| 015 | Eight cards, each showing the kidneys beside one partner organ with a two-way arrow | Each partner organ shares one job with the kidneys. The table below explains each one. | none |
| 016 | Two people under one shared lab slip: one swollen and breathless, one dry and dizzy | The same rising creatinine can mean too much fluid or too little. The treatment is opposite, so your doctor examines you as well as the number. | none |
| 017 | Six windows, each showing a test beside the organ it reports on | Each test looks at one partnership. Read together, they show how the organs are getting along. | eGFR, PTH |
| 018 | Kidneys, heart and brain inside a protective ring, with six habit icons pointing inward | Blood pressure, blood sugar, salt, activity, not smoking and vaccines protect several organs at once. | none |
| 019 | Eight pictograms of danger signs under a red banner | If you have kidney disease and notice any of these signs, go to the emergency room now. | none |
| 020 | Hands laying out medicine boxes and supplements on a clinic desk, with one pain reliever set aside | Bring every medicine and supplement to each visit, and ask before taking a pain reliever. | none |
| 021 | Three rising steps marked with a clock, a laboratory flask and two people | Timing, experiment and human studies answer different questions. A link between organs is proven only when it passes all three. | none |
| 022 | A time axis divided at 7 and 90 days into three zones, with one insult reaching three organs | Acute kidney injury, acute kidney disease and chronic kidney disease are separated by time. An insult that injures several organs at once is not evidence that one organ injured another. | AKI, AKD, CKD |
| 023 | Two alveoli compared: one flooded by pressure with an intact wall, one leaking through a damaged wall | Fluid overload is the established route from kidney to lung. Cytokine-driven permeability is shown in animal models and is not yet demonstrated in patients. | AKI |
| 024 | A brain and a pair of kidneys joined by two solid arrows and one dashed arrow | Efferent and afferent renal nerves form an established loop. Inflammatory injury from kidney to brain rests on experimental evidence. | none |
| 025 | Two people with identical kidneys: the muscular one has a high creatinine gauge, the frail one a low gauge | Creatinine is made by muscle. With the same kidney function, a person with less muscle has a lower creatinine, so the number can look better than the kidneys are. | none |
| 026 | One tablet with protective arrows to the kidneys, the heart and an artery | Some treatments protect the kidneys and the heart together. The benefit is proven in trials; the pathway that explains it is not. | none |
| 027 | A reference card with a vena cava measurement, a grid of nine Doppler waveforms and three grade chips | VExUS combines vena cava diameter with three venous Doppler patterns. The grade describes congestion; it is not a probability of kidney injury. | VExUS, IVC, AKI |
| 028 | Three case cards pairing the kidneys with the heart, the liver and the bone marrow | Three teaching cases in which the same laboratory value leads to different next steps. | AKI |

If a generated size differs from the size in A.6, use the real pixel size in the `<img>` `width` and `height` attributes.
