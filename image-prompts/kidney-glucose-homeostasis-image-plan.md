# IMAGE PLAN — Your Kidneys and Blood Sugar (Kidney Glucose Homeostasis)

**Guide:** `guides/kidney-glucose-homeostasis.html`
**Live URL (after merge):** https://renalcarematters.com/guides/kidney-glucose-homeostasis.html
**Total images:** 13 (1 hero vignette · 1 OG card · 11 inline figures)
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Generated:** 30 August 2026

---

## Architecture of the plan

This guide's teaching problem is that the kidney's glucose jobs are invisible: readers already
have a mental model of the kidney as a filter, and every misunderstanding downstream — "sugar in
my urine means my diabetes got worse," "my eGFR dropped so the drug is hurting me," "this is a
diabetes pill so it can't help me" — traces back to that single missing model. Images are
allocated to the four places the model breaks, not evenly across sections.

| Reader failure the image prevents | Image | Skill used |
|---|---|---|
| "The kidney only filters" | 01 · Four glucose jobs | `williamriveromd-infographic-skill` (multi-panel) |
| "Sugar in urine = worse diabetes" | 02 · Nephron transport & threshold | `williamriveromd-biomedical-mechanism-figure` |
| "Only the liver makes sugar" | 03 · Renal gluconeogenesis & hypoglycemia | `williamriveromd-biomedical-mechanism-figure` |
| "High sugar just clogs the filter" | 04 · Maladaptive reabsorption loop | `williamriveromd-biomedical-mechanism-figure` |
| "The benefit is the sugar lowering" | 05 · SGLT2 reset | `williamriveromd-biomedical-mechanism-figure` |
| "My eGFR fell, so stop the drug" | 06 · Dip vs slope | `williamriveromd-infographic-skill` (schematic chart) |
| "I don't know which numbers matter" | 07 · Know your numbers card | `williamriveromd-infographic-skill` (reference card) |
| "I'll wait until my sugar is high to worry" | 08 · Sick-day stoplight | `williamriveromd-infographic-skill` (reference card) |
| "Pick one drug and move on" | 09 · Layered protection rings | `williamriveromd-infographic-skill` (circular workflow) |
| "All these trials say the same thing" | 10 · Trial landscape by phenotype | `williamriveromd-infographic-skill` (clinician ref card) |
| Trust / share identity | 00 · Editorial hero · HERO · OG | `williamriveromd-infographic-skill` · `williamriveromd-hero-vignette` |

### Deliberately NOT generated as raster images

- **The five-number table** (`#numbers`) and the **mechanism-to-evidence matrix**
  (`#md-pharmacology`) — both are accessible HTML tables with translated cells and certainty
  badges. Rasterizing them would break search, screen readers, and the language toggle.
- **The full 15-row outcome-trial table** (`#md-trials`) — image 10 is a *phenotype map*, not a
  duplicate of the table. The numbers stay in HTML where they can be corrected.
- **The two decision pathways** (`#md-pathways`) — already rendered as `.algo-card` step lists.

### House rules applied to every prompt below

- Light background only (white / off-white / soft gray / very light teal tint). Navy `#0f1e2e`
  and teal `#1a6b72` are typography and accent colors, never background fills.
- Sans-serif only — **Inter** is named explicitly in every prompt.
- `© renalcarematters.com` in the bottom-right corner (bottom-center for 1:1 cards), small,
  semi-transparent navy, never over clinical content.
- **No invented numbers.** Every figure that carries a value carries one that appears in the
  guide and is sourced in the References accordion. Image 06 is explicitly axis-free.
- Every inline figure already has a `<figcaption>` with `<p class="fig-desc">` and, where the
  image contains acronyms, a `<dl class="fig-abbrevs">` — the lightbox reads these, so the
  image itself does not need to spell out abbreviations twice.

---

## HERO · Circular vignette

```
FILE NAME: kidney-glucose-homeostasis-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C (calm 3D anatomy)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F — Anatomy
CAMERA: three-quarter, slightly above the horizon of the object
HUMAN VARIATION (vs. previous guide): no people — the previous guide in this
  category (sugar-control-kidney-disease) used a Filipino patient scene, so this
  one deliberately rotates to a wordless anatomy hero.
AUDIENCE: mixed
VISUAL GOAL: At a glance, the kidney is not a passive filter — it is actively
  pulling something valuable back out of the stream passing through it.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas,
composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas
diameter with a visible WHITE BORDER around the full circle (the circle must never
touch the canvas edges). Composition archetype: F Anatomy. Camera: three-quarter
view, slightly elevated.

Subject: a single clean render of one human nephron rendered as a translucent,
gently glowing tubule looping through soft focus, with its glomerulus as the
luminous focal point at the lower left of the circle. Fine suspended particles of
light travel with the fluid down the tubule and a visible proportion of them curve
back out through the tubule wall toward the surrounding capillary — the reclaiming
motion is the whole idea of the picture. Restrained clinical color: renal reds and
warm coral for the glomerular tuft, translucent pearl-grey for the tubule, teal
#1a6b72 accents on the returning particles, on a soft, uncluttered light teal-tinted
off-white background with gentle studio lighting and a soft contact shadow.
Anatomically plausible proportions, not garish, not neon.

Visual hierarchy: the nephron occupies 60–70% of the circle in the lower-left and
lower-center; 2–3 supporting cues (a suggestion of surrounding peritubular capillary,
a faint out-of-focus second nephron) occupy 20–30%; reserve the UPPER-RIGHT 20–25%
of the circle as a TITLE SAFE ZONE of empty soft gradient background — absolutely no
anatomy, leader lines, labels, or callouts in that zone. Soft falloff toward a
slightly deeper neutral at the rim.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark —
clean render only. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of
icons, tiny unreadable labels, infographic clutter, cropped circle, cropped anatomy,
edge clipping, objects touching the circular border, important content inside the
title safe zone, baked-in text/titles/captions/logos/watermarks, rectangular borders
or frames, dark / charcoal / black backgrounds, cartoon style, neon, HDR,
over-saturation, implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin —
never cropped. ONE dominant hero subject (the nephron) at 60–70% of the circle,
2–3 supporting elements, upper-right 20–25% empty for the HTML title. Wordless.
Crops cleanly inside the circle with nothing lost at the edges.
```

---

## OG · Social share card

```
FILE NAME: kidney-glucose-homeostasis-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630   (FIXED — never any other size)
AUDIENCE: mixed
VISUAL GOAL: Stop the scroll with the counter-intuitive claim, and make the four
  verbs legible at thumbnail size.

PROMPT:
Open Graph social share card, exactly 1200 × 630 px, premium nephrology education
design on a clean off-white #fafafa background. Left two-thirds: bold condensed
sans-serif typography set in Inter — a navy #0f1e2e headline reading
"Your Kidneys and Blood Sugar" on two lines, and beneath it a single teal #1a6b72
sub-line reading "Filter · Reclaim · Burn · Make". Below that sub-line, a slim
horizontal row of four small flat line icons in teal, evenly spaced and each sitting
directly under its word: a funnel, a curved return arrow, a small flame, and a plus
sign inside a circle. Right one-third: a clean semi-photorealistic 3D render of a
single translucent nephron with its glomerulus glowing warm coral, floating on the
same off-white background with a soft shadow, cropped generously so it reads at
thumbnail size. Generous whitespace, strong hierarchy, nothing smaller than
mobile-legible. Small semi-transparent navy text "© renalcarematters.com" in the
bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo
look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black
backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter — no serif,
decorative, or handwritten typefaces. Never omit the renalcarematters.com attribution.
No drug names, no brand names, no trial acronyms on the card.

QUALITY CHECK:
Exactly 1200 × 630. Headline legible at 300 px wide. Off-white background. Attribution
present bottom-right. Pair with og:image:width="1200" and og:image:height="630".
```

---

## 00 · Editorial hero — `#four-jobs`

```
FILE NAME: kidney-glucose-homeostasis-00-hero-editorial.png
IMAGE TYPE: Photorealistic editorial hero
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: patients
VISUAL GOAL: Ground the physiology in a real Philippine consultation before the
  reader meets a single transporter.

PROMPT:
Photorealistic medical editorial photograph for a nephrology education guide,
1536 × 1024. A Filipina woman in her early forties with a short bob, round wire-frame
glasses, a coral-red blouse and a slim silver watch sits at the patient side of a
clinic desk in a bright modern Philippine outpatient clinic, leaning forward with her
finger resting on a printed laboratory result sheet as she asks a question. Opposite
her, a Filipino nephrologist in his late fifties with close-cropped grey hair, a short
beard and a pale blue open-collar shirt under a white coat listens with his pen down
and his hands open on the desk — he is answering, not lecturing. Soft natural daylight
from a large window at camera left, bright airy white walls, shallow depth of field
with the background clinic softly blurred. Warm, calm, documentary-realistic color
grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e. Natural skin texture,
correct hands, calm engaged expressions, no exaggerated smiles. Small semi-transparent
navy text "© renalcarematters.com" in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid AI gibberish text, avoid readable text on the
lab sheet, avoid unrealistic anatomy, avoid distorted hands or faces, avoid overprocessed
HDR, avoid generic stock-photo blandness, avoid excessive saturation, avoid staged
thumbs-up or exaggerated grins. NEVER use dark, navy, charcoal, or black backgrounds.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Bright light clinic. Two clearly different Filipino faces, neither reused from another
guide. No legible text anywhere except the attribution. Mobile-readable at 600 px wide.
```

---

## 01 · The kidney's four glucose jobs — `#four-jobs`

```
FILE NAME: kidney-glucose-homeostasis-01-four-jobs.png
IMAGE TYPE: Multi-panel educational infographic
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: patients
VISUAL GOAL: Replace "the kidney is a filter" with a four-verb model in one glance.

PROMPT:
Patient education infographic, 1536 × 1024, modern nephrology clinic aesthetic on a
white #ffffff background with soft light-gray #f3f4f6 panel cards. A single row of
FOUR equal rounded cards, read left to right, each with a large numeral 01–04 in teal
#1a6b72, a bold navy #0f1e2e verb, one short sentence beneath it in dark gray, and one
clean semi-3D medical illustration:

01 FILTER — blood entering a glomerulus, small glucose spheres passing freely into the
tubule. Caption line: "About 180 g of glucose leaves the blood every day."
02 RECLAIM — a proximal tubule wall with pumps drawing nearly all the glucose spheres
back toward a neighbouring capillary; a small handful continue downstream. Caption line:
"Almost all of it is pulled straight back."
03 USE — the same tubule segment glowing faintly warm to signal high energy demand, with
a small stylised mitochondrion beside it. Caption line: "Doing that work burns fuel."
04 MAKE — a kidney cortex wedge with three small inbound substrate arrows and one
outbound glucose sphere. Caption line: "During fasting, the kidney builds new glucose."

All typography in Inter: card verbs at heading weight, captions mobile-readable and no
smaller than roughly 22 px at this canvas size. Generous whitespace between cards, thin
navy hairline rules, no drop shadows heavier than a soft 4 px. Small semi-transparent
navy text "© renalcarematters.com" in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
No dark backgrounds. Inter only. Do not add a fifth panel. Do not add any number that
is not one of the two given captions. Never omit the attribution.

QUALITY CHECK:
Four panels, four verbs, one sentence each. Only two numeric claims on the whole
figure (180 g, and none other). Readable at 600 px wide. Light background.
```

---

## 02 · Nephron transport and the glucose threshold — `#threshold`

Delegated to `williamriveromd-biomedical-mechanism-figure`.

```
FILE NAME: kidney-glucose-homeostasis-02-nephron-transport.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: mixed
VISUAL GOAL: Show that glucose reabsorption is segmental, sodium-coupled, and finite —
  which is why a threshold exists at all.

PROMPT:
Create a publication-grade biomedical mechanism schematic, 1536 × 1024, on a white
background in flat vector style with soft semi-3D shading, review-article figure
aesthetic, all labels in Inter.

Topic: segmental renal glucose reabsorption and the glucose threshold.
Disease context: normal physiology, shown as the baseline against which diabetes and
SGLT2 inhibition are later compared.

LEFT PANEL — organ-level context: a simplified light gray-blue kidney in section with
one nephron traced through cortex and medulla in pale yellow. A thin dashed connector
box points from the early proximal tubule to the magnified panel.

CENTER PANEL — magnified functional unit inside a thin dashed border: a longitudinal
cut of the proximal tubule divided into an S1/S2 segment and an S3 segment. In S1/S2,
label a lumen-side transporter "SGLT2 — ~90% of filtered glucose", with paired glucose
and sodium symbols moving together into the cell. In S3, label a second lumen-side
transporter "SGLT1 — most of the remainder". On the blood side of both cells, label an
exit channel "GLUT2 (S1/S2) · GLUT1 (S3)". On the basolateral membrane draw the
Na⁺/K⁺-ATPase and label it "Na⁺/K⁺-ATPase — sets the sodium gradient (ATP)". Add one
short annotation with an arrow pointing at the coupled glucose+sodium pair reading
"glucose rides the sodium gradient — blocking one loses the other".

RIGHT PANEL — a small clean line graph inside its own dashed box: filtered glucose load
on the x-axis, reabsorbed glucose on the y-axis, with a straight rising line that bends
over into a plateau. Label the plateau "TmG ≈ 375 mg/min", label the shoulder of the
bend "splay — nephrons saturate unevenly", and label the point where urine glucose
begins "threshold ≈ plasma glucose 180 mg/dL". Do not add any other numeric value and
do not put tick numbers on the axes.

BOTTOM SUMMARY FLOW, three boxes with arrows left to right:
Left pale-pink box — "Filtered load = plasma glucose × GFR"
Center box — "Segmental, sodium-coupled, saturable reabsorption"
Right pale-blue box — "Threshold is not a constant: rises with chronic hyperglycemia,
falls in pregnancy, congenitally low in familial renal glucosuria, lowered on purpose
by SGLT2 inhibition"

Muted clinical palette: light gray-blue anatomy, pale yellow highlighted tubule, red for
the lumen-side transporters, blue for the basolateral exit, pale pink and pale blue
summary boxes. Generous whitespace, thin dashed connectors, no photorealism, no dark
background. Small semi-transparent navy text "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
No photorealism, no dark backgrounds, no decorative effects, no cartoon styling, no
gibberish text, no excessive icons, no serif fonts. Do not invent axis values or any
numeric threshold beyond the three given (~90%, TmG ≈ 375 mg/min, threshold ≈ 180 mg/dL).
Do not place both transporters in the same segment. Never omit the attribution.

QUALITY CHECK:
S1/S2 and S3 are visually distinct segments with the correct transporter in each. Glucose
and sodium always move together on the lumen side. Only three numbers appear. Labels
readable at slide-viewing size.
```

---

## 03 · Renal gluconeogenesis and hypoglycemia risk — `#make-glucose`

Delegated to `williamriveromd-biomedical-mechanism-figure`.

```
FILE NAME: kidney-glucose-homeostasis-03-renal-gluconeogenesis.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: mixed
VISUAL GOAL: Establish the kidney as a glucose *producer*, then show why losing that
  producer makes hypoglycemia the under-recognized danger of advanced CKD.

PROMPT:
Create a publication-grade biomedical mechanism schematic, 1536 × 1024, white
background, flat vector with soft semi-3D shading, review-article style, Inter labels.

Topic: renal gluconeogenesis in the fasted state, and hypoglycemia in advanced kidney
disease.

LEFT PANEL — two simplified organs side by side in light gray-blue on a shared baseline:
a liver and a kidney, each with an outbound glucose arrow of the same visual weight
pointing into a shared vessel. Header above the pair: "After an overnight fast".
Beneath the liver: "glycogen breakdown + gluconeogenesis". Beneath the kidney: "almost
no glycogen store — gluconeogenesis only". A single caption bridging both: "Liver and
kidney release approximately equal amounts of glucose via gluconeogenesis."

CENTER PANEL — magnified functional unit in a thin dashed box: a proximal tubule cell of
the renal cortex highlighted in pale yellow, with three inbound substrate arrows labelled
"lactate", "glycerol", "glutamine" and one outbound arrow labelled "glucose → blood". A
small side branch off the glutamine arrow labelled "→ NH₄⁺ excretion (acid–base)" shows
the shared substrate. A small catecholamine icon with an upward arrow at the cell margin
labelled "catecholamines stimulate". Beneath the cell, a thin note: "renal glucose
utilization ≈ 10% of whole-body use; renal gluconeogenesis roughly doubles after a meal".

RIGHT PANEL — a vertical stack of four small pale-pink cards under the header "Why
hypoglycemia rises as eGFR falls":
"↓ renal insulin clearance — the same dose lasts longer"
"↓ renal gluconeogenesis — one rescue arm is gone"
"↑ drug accumulation — insulin, sulfonylureas and their active metabolites"
"↓ intake, ↑ illness, blunted awareness"

BOTTOM SUMMARY FLOW, three boxes left to right:
Left pale-pink box — "Recurrent or severe hypoglycemia in previously hard-to-control
diabetes"
Center box — "Read it as a signal of declining kidney function until proven otherwise"
Right pale-blue box — "Clinician-led medication review — never a self-adjustment and
never more sugar to cover a dose that has outgrown the kidney"

Muted clinical palette, thin dashed connectors, generous whitespace, no photorealism,
no dark background. Small semi-transparent navy "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
No photorealism, no dark background, no cartoon styling, no gibberish text, no serif
fonts. Do not add any numeric value beyond the single "≈ 10%" given. Do not depict the
kidney storing glycogen. Never omit the attribution.

QUALITY CHECK:
The liver and kidney glucose arrows are visually equal in weight — that equivalence is
the whole point of the left panel. Only one number on the figure. Four risk cards, no more.
```

---

## 04 · The maladaptive reabsorption loop — `#diabetes-loop`

Delegated to `williamriveromd-biomedical-mechanism-figure`.

```
FILE NAME: kidney-glucose-homeostasis-04-maladaptive-loop.png
IMAGE TYPE: Biomedical mechanism schematic — causal loop (review-article style)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: mixed
VISUAL GOAL: Show diabetic kidney injury as a self-reinforcing loop in which the
  kidney's own thrift is the problem — not as sugar "clogging" a filter.

PROMPT:
Create a publication-grade biomedical mechanism schematic, 1536 × 1024, white
background, flat vector with soft semi-3D shading, review-article style, Inter labels.

Topic: the maladaptive proximal-transport loop of diabetic kidney disease.

MAIN PANEL — one large closed causal loop occupying the upper two-thirds, drawn as a
clockwise ring of six numbered nodes connected by thick tapered arrows so the reading
order is unambiguous:
1 "Chronic hyperglycemia" → 2 "↑ filtered glucose load" → 3 "↑ SGLT2 / SGLT1 transport;
glucose AND sodium reclaimed early" → 4 "↓ NaCl delivery to the macula densa" →
5 "Tubuloglomerular feedback misreads it — afferent dilation, ↑ intraglomerular pressure"
→ 6 "↑ tubular workload and O₂ demand in an already tight cortex" → back to 1.

Anchor the ring on a simplified pale-yellow nephron drawn faintly behind it, with the
macula densa marked as a small distinct patch where the distal tubule touches its own
glomerulus, so nodes 4 and 5 sit anatomically where they belong.

RIGHT INSET in a thin dashed box, labelled "Downstream injury": a glomerular capillary
loop with podocyte foot processes effacing and detaching, red ROS marks over a
mitochondrion in a hypertrophied tubular cell, and a widening interstitial band of
fibrosis. Three short callouts: "podocyte stress → albuminuria", "cortical hypoxia →
oxidative stress", "tubular hypertrophy → inflammation → fibrosis".

BOTTOM SUMMARY FLOW, three boxes left to right:
Left pale-pink box — "Thrift becomes injury: the organ best placed to dump the surplus
hoards it instead"
Center box — "Loop, not a single arrow — hyperfiltration is neither necessary nor
sufficient, and the arteriolar mechanism differs between type 1 and type 2 diabetes"
Right pale-blue box — "Every therapeutic target in this guide interrupts one node of
this loop"

Color logic without relying on color alone: number every node, and use red for injury,
blue for the anatomy, pale yellow for the highlighted nephron. Muted clinical palette,
thin dashed connectors, generous whitespace, no photorealism, no dark background. Small
semi-transparent navy "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
No photorealism, no dark backgrounds, no cartoon styling, no gibberish text, no serif
fonts. Do NOT draw sugar crystals, shards, or granules damaging tissue — the metaphor is
pressure, workload and oxygen, never abrasion. Do not add numeric values of any kind. Do
not present afferent dilation as the universal mechanism. Never omit the attribution.

QUALITY CHECK:
Six numbered nodes forming one closed clockwise ring. The macula densa sits where the
distal tubule meets its own glomerulus. No crystals, no numbers, no red/green-only coding.
```

---

## 05 · What SGLT2 inhibition resets — `#sglt2-reset`

Delegated to `williamriveromd-biomedical-mechanism-figure`.

```
FILE NAME: kidney-glucose-homeostasis-05-sglt2-reset.png
IMAGE TYPE: Biomedical mechanism schematic — before/after (review-article style)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: mixed
VISUAL GOAL: Make it obvious that the drug's important action is hemodynamic and
  natriuretic, and that the glucose loss is a side of the same coin, not the point.

PROMPT:
Create a publication-grade biomedical mechanism schematic, 1536 × 1024, white
background, flat vector with soft semi-3D shading, review-article style, Inter labels.
Two mirrored panels side by side, each in its own thin dashed box, separated by a
vertical hairline rule.

LEFT PANEL header "Untreated": a nephron with the early proximal tubule highlighted in
pale yellow and heavily loaded with paired glucose+sodium symbols moving into the cell.
Downstream, a visibly sparse trickle of sodium reaching a marked macula densa. At the
glomerulus, a thick red pressure indicator and the label "↑ intraglomerular pressure".
Urine at the tubule outlet: clear, labelled "little or no glucose".

RIGHT PANEL header "On an SGLT2 inhibitor": the same nephron with the S1/S2 transporter
drawn blocked by a small blue inhibitor wedge. Paired glucose+sodium symbols now continue
downstream instead of crossing the cell. A visibly restored stream of sodium reaches the
macula densa, labelled "distal NaCl delivery restored → tubuloglomerular feedback
re-engages". At the glomerulus, a thinner blue pressure indicator and the label
"↓ intraglomerular pressure". Urine at the outlet: labelled "glucosuria + natriuresis —
the expected effect, not a failure of control".

BOTTOM SUMMARY FLOW, three boxes left to right:
Left pale-pink box — "Blocked early reabsorption"
Center box — "Restored distal sodium signal → lower filtration pressure; transient
osmotic diuresis; modest plasma-volume fall"
Right pale-blue box — "Established: lower CKD progression and heart-failure events.
Proposed, not proven: ketone fuel shift, improved cortical oxygenation, erythropoiesis,
direct anti-inflammatory effect"

Mark the right-hand box's second sentence with a small open-outline flag icon and the
word "proposed" so mechanism is never read as demonstrated mediation. Muted clinical
palette, thin dashed connectors, generous whitespace, no photorealism, no dark
background. Small semi-transparent navy "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
No photorealism, no dark backgrounds, no cartoon styling, no gibberish text, no serif
fonts. Do not add hazard ratios, percentages, or any numeric value. Do not imply the
proposed mechanisms are established. Do not draw the inhibitor acting on SGLT1 or on the
basolateral side. Never omit the attribution.

QUALITY CHECK:
The two panels are anatomically identical apart from the intervention. The blockade sits
on the lumen side of S1/S2 only. The "proposed" flag is visibly attached to the
hypothesis sentence. No numbers anywhere.
```

---

## 06 · The eGFR dip versus the eGFR slope — `#md-pharmacology`

```
FILE NAME: kidney-glucose-homeostasis-06-egfr-dip-slope.png
IMAGE TYPE: Schematic evidence chart
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Separate the acute hemodynamic dip from the chronic slope so a single
  worse creatinine does not end an organ-protective prescription.

PROMPT:
Clinician reference schematic, 1536 × 1024, on a white #ffffff background, publication-
grade nephrology design, all typography in Inter.

Center: a single clean line chart with two curves. The x-axis is labelled "Time from
initiation" and the y-axis "eGFR" — and NEITHER AXIS CARRIES ANY TICK NUMBERS OR UNITS.
A navy #0f1e2e dashed curve labelled "Untreated trajectory" declines steadily from left
to right. A teal #1a6b72 solid curve labelled "On hemodynamically active therapy" starts
at the same point, drops over the first short interval, flattens, and then declines more
slowly, crossing the navy curve and diverging above it toward the right edge. Shade the
early interval very lightly and label it "Acute hemodynamic dip — reduced intraglomerular
pressure, reversible". Label the long right-hand divergence "Chronic slope — the outcome
that matters". Add a small annotation at the crossing point: "curves cross, then diverge
in the patient's favor".

Beneath the chart, a single full-width amber-bordered #b8860b caution card with a bold
navy heading "Do not generalize the 30% creatinine rule" and one short line of body text:
"That threshold applies to RAS-inhibitor initiation and titration. No validated
percentage threshold exists for stopping an SGLT2 inhibitor after the expected dip —
assess magnitude, timing, trajectory, volume status, illness, NSAIDs, diuretics and other
AKI causes."

Beneath that, a slim caption line in gray: "Schematic of shape, not of magnitude. Axes
are intentionally unscaled."

Generous whitespace, thin navy hairline rules, rounded card corners, mobile-readable
labels. Small semi-transparent navy "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid overprocessed HDR, avoid excessive saturation. No dark backgrounds. Inter
only. DO NOT put any number on either axis, and do not add gridline values, percentages,
or a legend with numeric entries — the whole point is that this figure is unscaled.
Never omit the attribution.

QUALITY CHECK:
Two curves, one crossing, zero numbers on the axes. The only numeral anywhere on the
figure is the "30%" inside the caution card. Amber card is bordered, not filled dark.
```

---

## 07 · Know your numbers — printable visit card — `#numbers`

```
FILE NAME: kidney-glucose-homeostasis-07-know-your-numbers.png
IMAGE TYPE: Patient reference card (printable)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients
VISUAL GOAL: Give the patient a physical object to fill in and carry, including to
  emergency visits where the last eGFR and potassium change what is safe to give.

PROMPT:
Printable patient reference card, 1024 × 1024, on an off-white #fafafa background with
a thin teal #1a6b72 border inset from the edge. Publication-grade clinic design, all
typography in Inter.

Header: navy #0f1e2e title "My kidney and heart numbers" with a small teal kidney line
icon to its left, and a right-aligned blank ruled field labelled "Date".

Body: five equal horizontal rows, each a soft light-gray #f3f4f6 rounded band containing,
left to right: a small flat teal line icon, the label in bold navy, a one-line plain
explanation in dark gray, and a generous blank white write-in box on the right.
Row 1 — funnel icon — "eGFR" — "how much blood my kidneys filter"
Row 2 — droplet icon — "UACR" — "whether protein is leaking into my urine"
Row 3 — cuff icon — "Blood pressure" — "the pressure my filters live under"
Row 4 — chart icon — "HbA1c" — "my average blood sugar"
Row 5 — flask icon — "Potassium" — "the electrolyte that decides which drugs I can take"

Footer: a single-line field labelled "Next labs due" with a blank rule, and beneath it
one short gray line: "Bring this card to every visit, including the emergency room."

Deliberately leave every value blank — this is a form, not a result sheet. Generous
whitespace, high contrast, print-friendly (nothing depends on color alone; every row is
labelled in words). Small semi-transparent navy "© renalcarematters.com" centered at the
bottom.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid excessive saturation. No dark backgrounds. Inter only. DO NOT print any
example value, target range, reference interval, or number of any kind in the write-in
boxes — they must be empty. Never omit the attribution.

QUALITY CHECK:
Five rows, five blank boxes, zero numbers anywhere on the card. Prints legibly in
black and white. Attribution bottom-center.
```

---

## 08 · Sick-day stoplight — `#safety`

```
FILE NAME: kidney-glucose-homeostasis-08-sick-day-stoplight.png
IMAGE TYPE: Patient safety reference card
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients
VISUAL GOAL: Make the euglycemic-ketoacidosis red flags recognizable before the
  patient thinks to check a glucose meter.

PROMPT:
Patient safety reference card, 1024 × 1024, on a white #ffffff background, publication-
grade clinic design, all typography in Inter. Three stacked full-width bands, each a
rounded card with a thick left color rail, a bold word label, an icon, and body text —
so the card works in black and white and for color-blind readers.

BAND 1 — green #1f7a4d rail, check-circle icon, label "GREEN — WELL":
"Eating and drinking normally, no fever, no vomiting. Continue your medicines exactly as
prescribed."

BAND 2 — amber #b8860b rail, phone icon, label "AMBER — CALL TODAY":
"Vomiting, diarrhea, fever, poor intake, dehydration — or a planned fast, Ramadan, or a
scheduled procedure. Contact your care team for your written hold-and-restart plan."

BAND 3 — red #b91c1c rail, alert-triangle icon, label "RED — GO IN NOW":
"Nausea and vomiting, abdominal pain, unusual exhaustion, rapid or deep breathing,
confusion, or unable to keep fluids down. Tell them you take an SGLT2 inhibitor so
ketones are checked."

Beneath the three bands, a single navy-bordered emphasis strip in bold navy #0f1e2e:
"Your blood sugar can be normal and this can still be ketoacidosis. Do not wait for a
high reading." Beneath that, one short gray line: "Never stop insulin on your own."

Generous whitespace, high contrast, print-friendly. Small semi-transparent navy
"© renalcarematters.com" centered at the bottom.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid excessive saturation, avoid alarming imagery of distressed patients. No dark
backgrounds. Inter only. Do NOT use a literal traffic-light graphic. Do NOT add any
glucose value, ketone value, or medication dose. Do NOT list which specific medicines to
hold — that list is individual and must come from the patient's own clinician. Never
omit the attribution.

QUALITY CHECK:
Three bands, each labelled in WORDS as well as color. The "normal glucose" caveat is
visually the most prominent statement after the red band. No numbers, no drug hold list.
```

---

## 09 · Four layers of cardiorenal protection — `#md-pathways`

```
FILE NAME: kidney-glucose-homeostasis-09-layered-protection.png
IMAGE TYPE: Circular workflow / concentric rings
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show the four pillars as complementary layers rather than a numbered
  ladder, so nobody reads it as a mandatory sequence.

PROMPT:
Clinician systems diagram, 1024 × 1024, on an off-white #fafafa background,
publication-grade nephrology design, all typography in Inter. FOUR concentric rings —
not a flowchart, not a numbered staircase.

CENTER DISC, teal #1a6b72 fill with white text, label "FOUNDATION" and beneath it in
smaller text: "education · smoking cessation · activity · nutrition · weight · blood
pressure · lipids · individualized glycemia · vaccination · avoid nephrotoxins".

RING 2, pale teal fill with navy text: "RAS BLOCKADE — ACE inhibitor or ARB for indicated
hypertension with albuminuria, titrated as tolerated. Never combine the two."

RING 3, pale blue fill with navy text: "SGLT2 INHIBITOR — kidney and cardiovascular
protection in eligible CKD and heart-failure phenotypes, independent of HbA1c and of
diabetes status."

RING 4 (outermost), pale amber fill with navy text, split into two labelled arcs:
left arc "GLP-1 RECEPTOR AGONIST — demonstrated kidney and cardiovascular benefit";
right arc "FINERENONE — eligible albuminuric type 2 diabetes, with potassium monitoring".

Place a short caption directly beneath the rings in gray: "Complementary layers, not a
fixed order. Choice depends on eGFR, albuminuria, potassium, volume status, blood
pressure, hypoglycemia risk, weight goals, pregnancy potential, adverse-effect history,
cost and patient preference."

No arrows around the rings and no step numbers anywhere — the absence of sequencing is
the point. Thin navy hairline separating each ring. Generous whitespace, mobile-readable
labels. Small semi-transparent navy "© renalcarematters.com" centered at the bottom.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid excessive saturation. No dark backgrounds. Inter only. DO NOT number the
rings, DO NOT add directional arrows between rings, and DO NOT draw this as a ladder,
staircase, pyramid, or numbered flow — any of those would contradict the caption. Do not
add brand names or doses. Never omit the attribution.

QUALITY CHECK:
Four concentric rings, no numbers, no arrows. Foundation is at the center. The caption
about individualization is legible. Off-white background.
```

---

## 10 · Trial landscape by phenotype — `#md-trials`

```
FILE NAME: kidney-glucose-homeostasis-10-trial-landscape.png
IMAGE TYPE: Clinician reference matrix
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show at a glance which phenotypes are directly supported by a dedicated
  trial and which rest on extrapolation — including which trials enrolled people
  without diabetes.

PROMPT:
Clinician reference matrix, 1536 × 1024, on a white #ffffff background, publication-grade
nephrology design, all typography in Inter. A clean grid, not a chart.

COLUMNS (four), headed in navy #0f1e2e: "Dedicated CKD outcome", "Heart failure",
"Type 2 diabetes CV outcome", "Enrolled participants WITHOUT diabetes".

ROWS (nine), each a trial name in bold navy in the leftmost label column: CREDENCE,
DAPA-CKD, EMPA-KIDNEY, FLOW, DAPA-HF, EMPEROR-Reduced, EMPEROR-Preserved, DELIVER,
EMPA-REG OUTCOME.

CELLS: where a trial covers a column, place a solid teal #1a6b72 filled rounded square
containing a white check mark. Where it does not, leave the cell empty with a faint gray
dot. Do not use color alone — every filled cell carries the check glyph.

Fill pattern, exactly as follows and no other:
CREDENCE — dedicated CKD ✓
DAPA-CKD — dedicated CKD ✓, without diabetes ✓
EMPA-KIDNEY — dedicated CKD ✓, without diabetes ✓
FLOW — dedicated CKD ✓
DAPA-HF — heart failure ✓, without diabetes ✓
EMPEROR-Reduced — heart failure ✓, without diabetes ✓
EMPEROR-Preserved — heart failure ✓, without diabetes ✓
DELIVER — heart failure ✓, without diabetes ✓
EMPA-REG OUTCOME — type 2 diabetes CV outcome ✓

Add a right-hand annotation column headed "Agent class" with one short word per row:
SGLT2i for all rows except FLOW, which reads GLP-1 RA.

Beneath the grid, a single gray caption line: "Coverage map only — composite endpoint
definitions differ between trials and are not interchangeable. Effect sizes and
limitations are in the guide's evidence table."

Generous whitespace, thin navy hairline rules between rows, alternating very light gray
row banding, mobile-readable labels. Small semi-transparent navy
"© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid excessive saturation. No dark backgrounds. Inter only. DO NOT print hazard
ratios, confidence intervals, sample sizes, percentages, or follow-up durations anywhere
on this figure — this is a coverage map, and the numbers live in the HTML table where
they can be corrected. Do not invent additional trials or additional checks beyond the
fill pattern given. Never omit the attribution.

QUALITY CHECK:
Nine rows, four coverage columns plus one class column. Every filled cell carries a check
glyph, not color alone. Zero numeric values on the entire figure. The fill pattern
matches the list exactly.
```

---

## Stage 2 handoff

Hand this pack to `williamriveromd-local-image-generator` to build
`/Users/williamgregoryriveromd/Downloads/kidney-glucose-homeostasis/`, write
`image-manifest.csv` / `.json`, and generate `README-image-generation.md`.

Once the PNGs are returned, place them as:

```
images/kidney-glucose-homeostasis-vignette-hero.{png,webp}   2048 × 2048
images/kidney-glucose-homeostasis-og.png                     1200 × 630
images/kidney-glucose-homeostasis-00-hero-editorial.{png,webp}    1536 × 1024
images/kidney-glucose-homeostasis-01-four-jobs.{png,webp}         1536 × 1024
images/kidney-glucose-homeostasis-02-nephron-transport.{png,webp} 1536 × 1024
images/kidney-glucose-homeostasis-03-renal-gluconeogenesis.{png,webp} 1536 × 1024
images/kidney-glucose-homeostasis-04-maladaptive-loop.{png,webp}  1536 × 1024
images/kidney-glucose-homeostasis-05-sglt2-reset.{png,webp}       1536 × 1024
images/kidney-glucose-homeostasis-06-egfr-dip-slope.{png,webp}    1536 × 1024
images/kidney-glucose-homeostasis-07-know-your-numbers.{png,webp} 1024 × 1024
images/kidney-glucose-homeostasis-08-sick-day-stoplight.{png,webp} 1024 × 1024
images/kidney-glucose-homeostasis-09-layered-protection.{png,webp} 1024 × 1024
images/kidney-glucose-homeostasis-10-trial-landscape.{png,webp}   1536 × 1024
```

The guide already references every one of these paths with matching `width`/`height`
attributes, `loading="lazy"` (except the hero, which is `fetchpriority="high"
loading="eager"`), and a structured `<figcaption>` — so no HTML edits are needed once the
files land, other than generating the `-rg-thumb.webp` via `generate_rg_thumbs.py`.
