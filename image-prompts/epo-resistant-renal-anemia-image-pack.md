# EPO-Resistant Renal Anemia — Image Pack

Stage-1 prompt pack for `guides/epo-resistant-renal-anemia.html`. Each prompt below was authored with the matching `williamriveromd-*` graphic skill. Generate the images in ChatGPT Image Generator (GPT-4o native image generation), then save each as both `.png` and a `.webp` twin under `images/`. The guide's HTML already references the filenames below.

| # | Mode | Image (file) | Skill used |
|---|---|---|---|
| 1 | Patient | `epo-resistant-renal-anemia-vignette-hero.{png,webp}` | hero-vignette |
| 2 | Patient | `epo-resistant-renal-anemia-01-overview.{png,webp}` | infographic (Archetype 4) — also embeds the 8-reasons grid as its bottom-left quadrant |
| 3 | Patient | `epo-resistant-renal-anemia-03-fix-the-cause.{png,webp}` | simple-figure (Scaffold C) |
| 4 | Patient | `epo-resistant-renal-anemia-04-warning-signs.{png,webp}` | simple-figure (Scaffold E) |
| 5 | Clinician | `epo-resistant-renal-anemia-05-hepcidin-axis.{png,webp}` | biomedical-mechanism-figure |
| 6 | Clinician | `epo-resistant-renal-anemia-06-workup-algorithm.{png,webp}` | algorithm-generator (Mode A · AHA-style) |
| 7 | Clinician | `epo-resistant-renal-anemia-07-trials-targets.{png,webp}` | infographic (Archetype 5) |
| 8 | Clinician | `epo-resistant-renal-anemia-08-organ-crosstalk-sigil.{png,webp}` | organ-crosstalk-sigil |

---

## 8 — Clinician · §3 Organ-crosstalk sigil — the inflamed, iron-restricted phenotype  *(organ-crosstalk-sigil skill — labelled five-organ variant)*

```
FILE NAME: epo-resistant-renal-anemia-08-organ-crosstalk-sigil.png
IMAGE TYPE: Monoline organ-crosstalk sigil (labelled, five-organ variant)
ASPECT RATIO: 1:1 square
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A single calm, symbolic sigil that makes one point — ESA hyporesponse is a multi-organ inflammatory iron-restricted phenotype, not a single-axis EPO failure.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration showing the multi-organ
crosstalk that drives ESA hyporesponsiveness in chronic kidney disease.

ORGANS (five, arranged as a radial pentagon around a central labeled hub):
- KIDNEY — lower left (a paired-kidney silhouette)
- LIVER — top (single hepatic outline)
- BONE MARROW — lower right (a small femur cross-section with a faint marrow cavity)
- GUT — middle left (a simple looped intestine outline)
- PARATHYROID — middle right (four tiny ovals stacked behind a faint thyroid outline)

CENTRAL HUB:
A small soft-teal circle at the geometric center, with a single label inside in
Inter sans-serif (the only font used; no serifs anywhere): "Inflamed iron-
restricted erythron · ESA hyporesponse".

RELATIONSHIP:
Show the five-organ crosstalk using thin dotted curved arrows connecting each organ
to the central hub and to its two adjacent organs along the pentagon. Each arrow
carries a short Inter sans-serif label naming the actual mediator and its
direction:

  KIDNEY → hub:        "EPO ↓"
  KIDNEY → LIVER:      "indoxyl sulfate ↑ · 1,25-OH-D ↓"
  LIVER → hub:         "hepcidin ↑"
  LIVER → GUT:         "IL-6 → ↓ ferroportin"
  GUT → hub:           "iron absorption ↓"
  GUT → MARROW:        "iron transport ↓"
  MARROW → hub:        "progenitors ↓ · HIF blunted"
  PARATHYROID → hub:   "PTH ↑"
  PARATHYROID → MARROW: "marrow fibrosis"
  KIDNEY → PARATHYROID: "SHPT"

STYLE:
Minimal clinical line-art, thin monoline strokes (~1.5 pt), soft teal-blue palette
(#1a6b72 strokes on white #ffffff background; mediator labels in navy #0f1e2e
70% opacity; the central hub circle is a very pale teal tint #eef6f7 with a navy
border). Each dotted arrow uses a small chevron arrowhead at its terminus. Balanced
radial sigil-like composition; generous whitespace; no photorealism; no 3D; no
heavy shadows. Organ icons are simple rounded silhouettes — clinically recognizable
but not surgically detailed.

COMPOSITION:
Pentagon layout — LIVER at 12 o'clock (top), PARATHYROID at 2 o'clock (upper-right),
BONE MARROW at 5 o'clock (lower-right), KIDNEY at 7 o'clock (lower-left), GUT at
10 o'clock (upper-left). Central hub circle equidistant from all five. Outer
"hand-off" arrows along the pentagon edges; inner "to-hub" arrows along five
radial spokes. Generous outer margin.

OUTPUT:
Square 1024 × 1024, clean margins, high-resolution, publication-grade medical icon
aesthetic. Bottom-right corner: small semi-transparent navy (#0f1e2e) Inter text
"© williamriveromd.com" at ~11 px, 70% opacity, not obscuring the sigil.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, dark background, neon colors,
crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic
lighting, or stock-photo style. Use ONLY the sans-serif font Inter — no other
fonts, no serifs, no decorative or handwritten typefaces. Do not invent additional
mediators or arrows beyond the ten listed above; the sigil should feel sparse,
not exhaustive. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Reads at thumbnail size as a five-organ pentagon with a labelled central hub. Each
of the ten mediator labels is legible at slide-viewing size. The dotted-arrow loop
between adjacent organs is visually distinct from the radial spoke to the hub. The
visual point — that this is a multi-organ inflammatory iron-restricted phenotype,
not a single-axis EPO failure — is immediately legible. Background is white;
copyright attribution williamriveromd.com sits in the bottom-right corner.
```

---

## 7 — Clinician · §5 Landmark trials + KDIGO 2026 targets reference poster  *(infographic skill — Archetype 5 Clinician Reference Card)*

```
IMAGE NUMBER: 07
SECTION PLACEMENT: Clinician §5 "Targets & Trials"
FILE NAME: epo-resistant-renal-anemia-07-trials-targets.png
ARCHETYPE: Clinician Reference Card
AUDIENCE: clinicians (nephrology, internal medicine, dialysis units)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes (two-column reference card, modular rows)
- 3D component graphics: light (small Hb-range bar / single dialysis-icon accent)
- algorithm/flowchart: no

PURPOSE: One scannable evidence card that lets a clinician justify the dose ceiling
in EPO hyporesponse — five landmark trials in 5 rows on the left, KDIGO 2026 targets
in 5 tiles on the right, with the take-home line across the bottom.

KEY CONCEPTS: Besarab 1998 / CHOIR / CREATE / TREAT / PIVOTAL; KDIGO 2026 Hb
initiation thresholds; Hb ceiling (do not maintain > 11.5; do not intentionally
exceed 13); iron trial thresholds (TSAT ≤ 30%, ferritin ≤ 500); HIF-PHI
positioning (offer when ESA-intolerant / non-responder); KDIGO 2026 nomenclature.

DIMENSIONS: 1792 × 1024 (16:9)

ASPECT RATIO: 16:9

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical reference infographic card for clinicians, publication-grade nephrology
design. Landscape 1792 × 1024. White (#ffffff) background; thin soft-gray (#e2e6eb)
1-pt borders between modular sections; navy (#0f1e2e) primary text; clinical teal
(#1a6b72) headings; renal green (#1f7a4d) positive/recommended accents; amber
(#b8860b) caution accents; clinical red (#b91c1c) harm-signal accents. All
on-image typography uses the Inter sans-serif font family exclusively — no
serifs, no decorative faces. Generous whitespace; rounded card corners; no heavy
shadows or glow.

TITLE STRIP (full width, ~95 px tall):
Left-aligned bold navy Inter title: "Why we do not chase normal hemoglobin."
Right-aligned clinical-teal Inter regular subtitle, smaller: "Landmark trials &
KDIGO 2026 targets in ESA hyporesponse."

BODY (two columns, soft 1-pt vertical divider):

LEFT COLUMN — "The evidence ceiling" (~58% of canvas width).
Header row in clinical teal Inter bold: "Trial · Population / target · Key result ·
Lesson". Below it, five rounded rows on alternating white / very-soft-gray
(#fafafa) fills, each row ~80 px tall. Use Inter throughout; bold the trial name
and PMID, regular for the rest.

Row 1 — Normal Hematocrit · "Besarab 1998 · PMID 9718377"
  Population/target: 1,233 HD with cardiac disease; Hct 42% vs 30%
  Key result: Death/MI RR 1.3 (0.9–1.9); stopped early; ↑ access thrombosis
  Lesson (red Inter bold): "Normalizing Hct harms"

Row 2 — CHOIR · "Singh 2006 · PMID 17108343"
  Population/target: 1,432 NDD; Hb 13.5 vs 11.3 g/dL
  Key result: Composite HR 1.34 (1.03–1.74); no QoL benefit
  Lesson (red Inter bold): "Higher target = harm"

Row 3 — CREATE · "Drüeke 2006 · PMID 17108342"
  Population/target: 603 stage 3–4; Hb 13–15 vs 10.5–11.5
  Key result: CV HR 0.78 (0.53–1.14), NS; more dialysis in the high arm
  Lesson (amber Inter bold): "No CV benefit"

Row 4 — TREAT · "Pfeffer 2009 · PMID 19880844"
  Population/target: 4,038 T2DM NDD; darbepoetin to ~13 vs placebo
  Key result: Stroke HR 1.92 (1.38–2.68); no CV/renal benefit
  Lesson (red Inter bold): "The stroke signal"

Row 5 — PIVOTAL · "Macdougall 2019 · PMID 30365356"
  Population/target: 2,141 incident HD; proactive vs reactive IV iron
  Key result: Primary composite HR 0.85 (P=0.04); ESA-sparing (−7,539 IU/mo)
  Lesson (green Inter bold): "Proactive IV iron — safer ESA"

RIGHT COLUMN — "KDIGO 2026 at a glance" (~42% of canvas width).
Five compact tile rows on a very-soft-gray (#f3f4f6) panel, each a rounded white
card with a colored left accent bar:

Tile 1 (teal accent) — Hb INITIATION
  • NDD: 8.5–10.0 g/dL
  • Dialysis: 9.0–10.0 g/dL

Tile 2 (amber accent) — Hb CEILING
  • Do not maintain > 11.5 g/dL
  • Do not intentionally exceed 13 g/dL

Tile 3 (green accent) — IRON TRIAL
  • TSAT ≤ 30% AND ferritin ≤ 500 ng/mL
  • IV iron in HD (PIVOTAL); caution in NDD (REVOKE)

Tile 4 (soft purple accent #6c3d8e) — HIF-PHI POSITIONING
  • Offer to patients who CANNOT tolerate or do NOT respond to ESA
  • Oral advantage in NDD / PD / home-HD
  • Avoid in active malignancy, recent thrombosis, transplant, children

Tile 5 (navy accent) — KDIGO 2026 NOMENCLATURE
  • "Absolute iron deficiency" → systemic iron deficiency
  • "Functional iron deficiency" → iron-restricted erythropoiesis
  • Anemia: Hb < 12 (women), < 13 (men)

BOTTOM TAKE-HOME STRIP (full width, ~110 px tall, soft gray #f3f4f6 fill):
Centered bold navy Inter sentence: "The dose ceiling in hyporesponse is a safety
principle — not an admission of defeat."

ATTRIBUTION:
Bottom-right of the take-home strip: "williamriveromd.com" in small
semi-transparent navy (#0f1e2e) Inter text, ~11 px, 70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use
ONLY the sans-serif font Inter — no other fonts, no serifs, no decorative faces. Do
not invent trial values; reproduce the numbers above exactly. Never omit the
williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable at 600-px width, clinically plausible, visually calm,
publication-grade, and consistent with williamriveromd.com. Background must be
white or soft light gray — never dark. The five trial rows on the left and the
five KDIGO tiles on the right read as two parallel columns; the take-home strip
is the visual conclusion. PMIDs are legible at thumbnail size. Copyright
attribution williamriveromd.com must be visible in the bottom-right corner of
the take-home strip.
```

---

## 6 — Clinician · §4 EPO-hyporesponse workup algorithm  *(algorithm-generator skill — Style Mode A · AHA-style)*

```
FILE NAME: epo-resistant-renal-anemia-06-workup-algorithm.png
IMAGE TYPE: Style Mode A — AHA-style provider algorithm
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: A printable bedside / EHR pocket card that runs a clinician through the cause-directed workup before any ESA dose escalation, with the PRCA red-flag branch and the final dose-ceiling escalation node visible at a glance.

PROMPT:
Create a polished medical guideline algorithm flowchart in the style of an American
Heart Association provider algorithm. Use a white background, clean sans-serif
typography set in Inter (no serif font, no decorative or handwritten typeface),
thin black/dark-gray arrows, pastel rounded boxes, and pink decision diamonds.
Layout is portrait 1024 × 1536, centered, spacious, and easy to read.

Use these visual conventions:
- Green rounded boxes for safety, monitoring, or supportive care
- Peach/orange rounded boxes for initial assessment and activation steps
- Pink diamond boxes for decision questions
- Blue rounded boxes for active treatment steps
- Gray capsule boxes for transitional or escalation steps
- Red bold labels beside arrows for emergency / red-flag branch conditions
- A dashed horizontal divider may separate workup from escalation phase
- Maintain strict alignment, consistent spacing, and guideline-grade clarity
- Each step is a numbered node (1–10) in the AHA convention: a small navy circle
  containing the step number sits on the left edge of the node

Content to render:

TITLE (top, centered, bold navy Inter):
"EPO-hyporesponse workup — find the cause before climbing the dose"
SUBTITLE (clinical-teal Inter regular, one line):
"KDIGO 2026-aligned · before any ESA dose escalation"

ENTRY NODE (peach/orange rounded box, top center):
"Rising ERI at stable Hb — or — Hb stalled on appropriate weight-based ESA
   → launch the workup, do NOT escalate ESA yet"

Then a top-to-bottom numbered pathway. Each node is a wide rounded box with the
step number on the left:

1. Peach/orange — "Confirm & quantify"
   • Apply KDIGO dose-escalation criterion and/or ERI
   • Verify adherence, ESA cold-chain storage, injection technique

2. Blue — "Iron status FIRST"
   • TSAT and ferritin
   • Trial of iron if TSAT ≤ 30% AND ferritin ≤ 500 ng/mL
   • Distinguish absolute (systemic) vs iron-restricted erythropoiesis

3. Blue — "Inflammation / occult infection"
   • CRP / hsCRP ± IL-6
   • Hunt: access, retained catheter, failed graft, dental, foot

4. Blue — "Nutrition"
   • Albumin, Malnutrition-Inflammation Score
   • Treat protein-energy wasting

5. Blue — "CKD-MBD"
   • iPTH
   • Treat severe SHPT (especially > 800 pg/mL)

6. Blue — "Dialysis adequacy"
   • Kt/V
   • Reduce indoxyl-sulfate burden where possible

7. Blue — "Vitamins / cofactors"
   • B12, folate, 25-OH vitamin D
   • Consider vitamin C, L-carnitine in selected patients

8. Blue — "Blood loss / shortened RBC survival"
   • Reticulocytes, LDH, haptoglobin, peripheral smear
   • GI evaluation; review menstrual losses; dialysis-circuit losses

To the RIGHT of step 8 / 9, branching off with a red bold arrow labeled "RED FLAG":

9. Pink diamond — "Sudden Hb fall + reticulocytopenia on ESA?"
   YES branch (red arrow) → Blue rounded box, red bordered:
     "STOP ESA immediately
      → Anti-EPO antibody assay + marrow exam
      → Suspect anti-EPO–antibody PRCA
      → Immunosuppression ± HIF-PHI"
   NO branch → returns to the main vertical pathway.

Back on the main column:

10. Blue — "Medication & comorbidity review"
    • Malignancy, hemoglobinopathy, recent COVID-19
    • Do NOT reflexively stop RAS blockade (Saudan 2006)

DASHED HORIZONTAL DIVIDER across the column (labeled "If workup is unrevealing AND
iron / PTH already optimized").

FINAL ESCALATION NODE (gray capsule, full-width):
"Cap ESA at ~2× initial weight-based dose
 → Consider HIF-PHI (offered to patients who cannot tolerate or do not respond
   to ESA — KDIGO 2026 positioning)
 → Tolerate Hb 10–11.5 g/dL; avoid transfusion when possible
 → Continue to address inflammation / PEW / SHPT — these levers persist"

Design requirements:
- Title at top
- No decorative icons unless clinically necessary
- No photos
- No 3D elements
- No dark background
- No excessive shadows
- Use only short, readable text inside boxes
- Professional clinical-education style
- Make the diagram publication-grade and vector-like, with crisp typography,
  perfectly aligned nodes, consistent arrow lengths, balanced left-right branches,
  and generous margins
- Ensure all text is legible at full size and thumbnail size
- Include a small professional footer reading "© williamriveromd.com" positioned at
  the bottom-right corner in subtle gray (#6b7280) medical-publication styling, ~10–11
  px Inter, 70% opacity, never inside a node or overlapping arrows

NEGATIVE INSTRUCTIONS:
Avoid serif fonts, decorative or handwritten typefaces, cartoon styling, dark
backgrounds, photorealistic people, AI gibberish text, clutter, or any 3D effects.
Do not omit the PRCA red-flag branch — it is the only branch in the algorithm and
must be visually distinct (red label, separated). Do not omit the bottom escalation
node — it is the entire reason the workup exists.

QUALITY CHECK:
Portrait, AHA-style, ten numbered nodes plus the PRCA side-branch and the final
escalation node, all on a clean white background. Inter throughout. The eye moves
top → bottom on the main column; the PRCA branch peels off to the right and rejoins.
The "© williamriveromd.com" attribution is visible in the bottom-right corner.
```

---

## 5 — Clinician · §3 Hepcidin axis biomedical mechanism figure  *(biomedical-mechanism-figure skill — review-article schematic)*

```
FILE NAME: epo-resistant-renal-anemia-05-hepcidin-axis.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A single review-article-style figure that explains the central lesion of
ESA hyporesponsiveness — the IL-6 → hepcidin → ferroportin axis — at organ scale and
at macrophage scale, then maps it to injury → intervention → benefit.

PROMPT:
Create a publication-grade biomedical mechanism schematic in the AJKD / NEJM review-
article house style.

Topic: The IL-6 → hepcidin → ferroportin axis as the central lesion of
ESA hyporesponsiveness in chronic kidney disease.

Disease context: Anemia of chronic kidney disease with iron-restricted erythropoiesis
under hepcidin control.

Central mechanism: Pro-inflammatory IL-6 (from inflamed tissue, vascular access,
uremic milieu) drives hepatic HAMP transcription → circulating hepcidin binds and
internalizes ferroportin on macrophages and enterocytes → iron is trapped intracellularly
→ marrow erythron is starved of iron despite normal-to-high ferritin →
ESA hyporesponse.

ORGAN-LEVEL PANEL (left half of the canvas, ~55% width):
A simplified anatomical scene on a white (#ffffff) background, drawn in flat vector
with soft semi-3D shading, muted clinical colors. From left to right, gently
overlapping:
- An inflamed kidney (light gray-blue, with a small fibrosis stipple) labeled
  "CKD — uremic inflammation". A small flame icon and an IL-6 burst floats off it.
- A liver above and to the right (light gray-blue, hepatic outline) labeled
  "Liver / hepatocyte". An IL-6 arrow runs from the kidney/inflammation into the
  hepatocyte, with a small inset bubble: "IL-6 → JAK/STAT3 → HAMP transcription".
  A red dotted line emits from the hepatocyte labeled "hepcidin" and fans out into
  the circulation.
- A bone-marrow cross-section (femur with marrow cavity) to the right, labeled
  "Bone marrow erythron". A pale-yellow halo around the marrow indicates relative
  iron starvation; small erythroid progenitors are present but reduced.
- A circulating macrophage and an enterocyte (small cells under the marrow / next to
  the gut wall) — each shows iron stores (small brown dots) trapped inside, with
  red hepcidin molecules docked onto their surfaces.
A thin dashed connector box from the macrophage points to the magnified inset.

MAGNIFIED MECHANISM PANEL (right half, ~40% width, thin dashed border):
A close-up of a single macrophage in cross-section, on a soft pale-yellow tint to
indicate "affected region". Show:
- A membrane-spanning ferroportin channel — labeled "Ferroportin".
- A red hepcidin molecule binding the channel — labeled "Hepcidin → FPN binding".
- An arrow showing ubiquitination/endocytosis of the channel into the cell —
  labeled "Endocytosis & lysosomal degradation".
- Inside the cell, iron beads (brown) accumulate — labeled "Iron sequestered".
- A small outward arrow (Fe²⁺) shown crossed-out, labeled "↓ iron egress".
- A faint side note: "Inflammation also suppresses erythroid progenitors and blunts
  HIF response — triple hit on the erythron".
Use concise, high-yield labels in Inter sans-serif only.

BOTTOM SUMMARY FLOW (full width along the bottom ~22% of the canvas):
Three rounded boxes connected by bold arrows left → right, sitting on a very soft gray
(#f3f4f6) strip.

  Left box — pale pink fill, navy border, header "Injury":
    • Iron-restricted erythropoiesis (ferritin normal/high, TSAT low)
    • Suppressed erythroid progenitors
    • Blunted HIF / hypoxia response
    • Bottom line in bold: "ESA hyporesponse"

  Center box — light gray-blue fill, navy border, header "Intervention":
    • Treat inflammation & occult infection
    • Proactive IV iron (PIVOTAL — strongest in HD)
    • HIF-PHI: lowers hepcidin, raises transferrin / TIBC *(emerging — KDIGO 2026
      second-line)*
    • Anti-IL-6 (ziltivekimab) *(investigational — ZEUS trial)*

  Right box — pale blue fill, navy border, header "Benefit":
    • Iron reaches the marrow → erythropoiesis restored
    • ↓ ESA dose required → safer Hb 10–11.5 g/dL
    • ↓ MACE risk associated with high ESA exposure

Title strip above the figure: bold navy (#0f1e2e) Inter — "The central lesion of
ESA hyporesponsiveness: the IL-6 → hepcidin → ferroportin axis." Subtitle in
clinical teal (#1a6b72) Inter regular — "Why ferritin can look 'adequate' while the
marrow is starving of iron."

Use a white background, muted clinical colors (light gray-blue anatomy, soft yellow
highlight, red for hepcidin/injury, blue for therapy/benefit, pale pink for pathology
box, pale blue for benefit box), clean sans-serif Inter labels, thin dashed connector
lines, and a review-article figure style. Mark HIF-PHIs and ziltivekimab clearly as
"emerging" or "investigational" so the figure is not read as standard care.

Bottom-right corner: small semi-transparent navy "© williamriveromd.com" in Inter,
~10–11 px, 70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, decorative shadows, dark backgrounds, cartoon styling, AI
gibberish text, tiny unreadable labels, or invented pathways. Use ONLY the
sans-serif font Inter — no other fonts, no serifs, no decorative faces. Do not show
literal blood splatter or distressing imagery. Do not omit the experimental/emerging
flag on HIF-PHIs or anti-IL-6 agents. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must read as a single AJKD/NEJM-style schematic at slide-viewing size. Organ panel,
magnified macrophage inset, and bottom three-box flow are visually distinct but
clearly linked by arrows. Background must be white — never dark. Hepcidin and
ferroportin are anatomically correct (ferroportin shown on the cell membrane, not
inside the nucleus). Copyright attribution williamriveromd.com must be visible in the
bottom-right corner.
```

---

## 4 — Patient · §5 Warning-signs reference card  *(simple-figure skill — Scaffold E square reference card)*

```
FILE NAME: epo-resistant-renal-anemia-04-warning-signs.png
IMAGE TYPE: Scaffold E — Square Reference / Quick-Look Card
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients & families
VISUAL GOAL: A fridge- or phone-friendly red-flag card a Filipino dialysis patient or caregiver can scan in five seconds — six clinical-red warning signs and a calm "call the unit or go to the ER" footer.

PROMPT:
Clinical reference card, publication-grade nephrology design, square 1024 × 1024. White
(#ffffff) background. Bold navy (#0f1e2e) title at the top center in Inter typeface:
"Warning signs — call your kidney team." Short clinical-teal (#1a6b72) subtitle line
below in Inter regular: "When EPO-resistant anemia turns into an emergency."

Below the heading, a 3 × 2 grid of six rounded square tiles on a very soft gray panel
(#f3f4f6). Each tile is white with a thin navy border, a small clinical-red (#b91c1c)
solid dot in the top-left corner, a clean simple line icon in the upper-middle (no
literal emoji), and a short two-line label in Inter — bold first line, regular
descriptor second line.

Tile 1 — Icon: stylized droplet + downward arrow. Label: "Sudden energy drop / very
pale" → "after weeks of steady EPO injections."

Tile 2 — Icon: stomach/GI silhouette with droplet. Label: "Black, tarry or bloody
stools" → "or vomiting blood."

Tile 3 — Icon: calendar with droplet. Label: "Very heavy menstrual bleeding" →
"more than usual, soaks pads quickly."

Tile 4 — Icon: bandaged forearm fistula. Label: "Fever, chills, redness or pus" →
"at a dialysis catheter or fistula."

Tile 5 — Icon: tooth + foot silhouette. Label: "Severe dental pain or foot wound"
→ "or a new abscess anywhere."

Tile 6 — Icon: chest/heart with a small lightning-bolt brain. Label: "Chest pain or
stroke signs" → "one-sided weakness, slurred speech, vision loss."

Below the grid, a full-width clinical-red (#b91c1c) accent strip ~120 px tall with a
white-text Inter line in the middle, bold:
"Call your dialysis unit or go to the ER — don't wait for your next clinic visit."

Tiny soft-gray (#f3f4f6) bottom strip ~50 px with navy Inter regular: "EPO-resistant
anemia · patient safety card · williamriveromd.com" — the "williamriveromd.com"
portion is semi-transparent navy (#0f1e2e), ~11 px, 70% opacity, anchored to the
bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use
ONLY the sans-serif font Inter — no other fonts, no serifs, no decorative faces. Do
not depict literal blood pools, distressing wound close-ups, or any branded packaging.
The dental-pain and foot-wound icons must stay symbolic, not photographic. Never omit
the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable at 600-px width AND printable on a small fridge magnet,
clinically plausible, visually calm despite the red signals, publication-grade.
Background must be white or soft light gray — never dark. The six red-dotted tiles
read as a single scannable list; the bottom red strip is the clear "what to do"
action. Copyright attribution williamriveromd.com must be visible in the bottom-right
corner.
```

---

## 3 — Patient · §3 "Fix the cause, not the dose" — 6-step ladder figure  *(simple-figure skill — Scaffold C horizontal step sequence)*

```
FILE NAME: epo-resistant-renal-anemia-03-fix-the-cause.png
IMAGE TYPE: Scaffold C — Horizontal Step Sequence
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients & families
VISUAL GOAL: A calm one-glance step-ladder that shows the safer plan — six sequential things we do to make EPO work again — beside a small "DON'T just push the dose" counterpoint.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top center
in bold navy (#0f1e2e) Inter typeface: "Fix the cause — don't just push the dose." A
short clinical-teal (#1a6b72) subtitle line beneath in Inter regular:
"What we do when EPO stops working in kidney disease."

Six rounded rectangular cards arranged horizontally in a single row, connected by bold
navy right-pointing arrows. Each card has a colored top accent band, a small icon, a
bold step label in Inter, and 1–2 short bullet details. The cards sit on a very soft
gray panel (#f3f4f6). Generous whitespace.

Card 1 (top accent: clinical teal #1a6b72) — icon: simple magnifying-glass over a
heart/kidney symbol — "Find & fix the cause" — "Blood tests, history, exam."

Card 2 (top accent: renal green #1f7a4d) — icon: a stylized IV drip with an "Fe" tag
— "Replace iron" — "Often by IV in dialysis."

Card 3 (top accent: amber #b8860b) — icon: small flame / inflammation icon — "Hunt
hidden infection" — "Teeth, foot, dialysis access."

Card 4 (top accent: soft purple #6c3d8e) — icon: tiny bone with parathyroid dots —
"Balance PTH & minerals" — "Vitamin D, binders, calcimimetics."

Card 5 (top accent: clinical teal #1a6b72) — icon: stylized dialysis machine + plate
of food — "Optimize dialysis & nutrition" — "Full sessions, enough protein."

Card 6 (top accent: clinical teal #1a6b72) — icon: a simple capsule shape — "Add
HIF-PHI & adjuncts" — "When ESA alone is not enough."

To the right of card 6, set apart from the chain by a soft dashed vertical divider,
place a small red-tinted (#b91c1c) caution card occupying ~12% of the canvas width:
icon — a stop-circle — title in Inter bold red "DON'T just push the EPO dose" — one
short line "Higher dose = more stroke / heart risk, not more energy."

Bottom strip: full-width soft gray (#f3f4f6), height ~80 px, with a single brief
summary sentence centered in navy Inter:
"We aim for a steady, safer hemoglobin (10–11.5 g/dL) — not a 'perfect' number."

Bottom-right corner of the bottom strip: "williamriveromd.com" in small
semi-transparent navy (#0f1e2e) Inter text, ~11 px, 70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use
ONLY the sans-serif font Inter — no other fonts, no serifs, no decorative faces. Do
not depict literal needles entering skin, distressing imagery, or branded packaging.
Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable at 600-px width, clinically plausible, visually calm,
publication-grade, and consistent with williamriveromd.com house style. Background
must be white or soft light gray — never dark. The six-step ladder reads in one
horizontal glance; the red "DON'T push the dose" counterpoint sits clearly off to the
right side and does not compete with the ladder for the eye. Copyright attribution
williamriveromd.com must be visible in the bottom-right corner.
```

---

## 2 — Patient · §1 Overview poster — "Why EPO sometimes stops working"  *(infographic skill — Archetype 4 Multi-Panel Educational Infographic)*

```
IMAGE NUMBER: 02
SECTION PLACEMENT: Patient §1 "What it means" (top of body, just under hero)
FILE NAME: epo-resistant-renal-anemia-01-overview.png
ARCHETYPE: Multi-Panel Educational Infographic
AUDIENCE: patients & families
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes (modular cards, icons, arrows)
- 3D component graphics: yes (kidney, bone marrow, red blood cell, IL-6/hepcidin/iron motifs)
- algorithm/flowchart: light (a 4-step "the plan" strip at bottom)

PURPOSE: A single calm at-a-glance overview that lets a Filipino patient understand
(a) what EPO normally does, (b) why it can stop working, (c) the 8 common reasons,
and (d) what we do about it — before they read the long-form sections.

KEY CONCEPTS: healthy kidney makes EPO → marrow makes red cells (the "go" signal);
damaged kidney + inflammation + hepcidin → iron locked away (the "block"); 8 driver
icons; 4-step plan ladder (fix cause → iron → ESA ceiling → HIF-PHI → adjuncts).

DIMENSIONS: 1792 × 1024 (16:9)

ASPECT RATIO: 16:9

COPY-READY IMAGE GENERATOR GPT PROMPT:
A landscape 16:9 patient-education poster for a Filipino nephrology guide titled
"Why EPO sometimes stops working in kidney disease". Premium williamriveromd.com
publication aesthetic — clean, airy, modular, mobile-readable. Background pure white
#ffffff with subtle soft-gray section dividers; primary text in navy #0f1e2e, headings
in clinical teal #1a6b72, supportive accents in renal green #1f7a4d and amber #b8860b,
warning accents in clinical red #b91c1c. All on-image typography uses the Inter
sans-serif font family exclusively — no serifs, no decorative faces. Generous negative
space; rounded cards with soft 1-px borders, no heavy shadows or glow.

Compose four labeled quadrants of equal weight, separated by hairline dividers:

QUADRANT TOP-LEFT — "The normal signal."
A semi-photorealistic 3D anatomical mini-scene reading left → right: a healthy human
kidney (restrained renal red, anatomically accurate) emits a soft warm-gold flowing
ribbon labeled "EPO" that travels into a small cutaway of pelvic bone marrow, where
3–4 fresh red blood cells (biconcave discs) are blooming out. A small caption strip
below reads "Healthy kidneys make EPO. EPO tells the bone marrow to build red blood
cells." Use Inter, sentence case, mobile-readable.

QUADRANT TOP-RIGHT — "When the signal is blocked."
The same kidney, now visibly fibrotic and slightly shrunken, emits only a thin, dim
gold ribbon labeled "less EPO". Above it, a small inflammation cloud labeled "IL-6"
in soft amber, and a tiny liver icon emitting blue dots labeled "hepcidin". The
hepcidin dots dock onto a magnified macrophage holding iron beads — the iron is shown
trapped inside the cell behind a closed gate ("ferroportin closed"). A small caption:
"In CKD the kidney makes less EPO — and inflammation locks iron away from the marrow."

QUADRANT BOTTOM-LEFT — "Eight common reasons."
A neat 4×2 grid of small rounded icon cards, each ~150-px square, each with one
mobile-readable label in Inter:
  1. 🩸 "Low iron (or iron locked away)"
  2. 🔥 "Inflammation / hidden infection"
  3. 🦴 "Overactive parathyroid (high PTH)"
  4. 🍚 "Poor nutrition / weight loss"
  5. 💧 "Not enough dialysis"
  6. 🌿 "Low vitamin D, B12, folate"
  7. 🩸 "Hidden blood loss"
  8. ⛔ "Rare anti-EPO antibody reaction"
Use simple clean line icons, not emoji glyphs literally rendered — translate each
icon idea into a tasteful 2D pictogram in navy/teal.

QUADRANT BOTTOM-RIGHT — "The plan."
A horizontal 4-step ladder/arrow strip, each step a rounded teal-tinted card with a
short label in Inter:
  Step 1 — "Find and fix the cause"
  Step 2 — "Optimize iron (often IV)"
  Step 3 — "Hold ESA at a safe Hb 10–11.5"
  Step 4 — "Consider HIF-PHI + adjuncts"
A small green check at the end and a gentle arrow chain between the steps. Tiny
caption strip below: "We aim for a steady, safer hemoglobin — not a perfect number."

A discreet headline strip across the top (full width, ~80 px high): in Inter,
left-aligned navy "Why EPO sometimes stops working" with a short teal subheading
"A simple overview for kidney-disease patients". Right-aligned at the same height,
the small navy-teal "williamriveromd.com" attribution at ~10–11 px, 70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo
look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds
— light backgrounds only. Use ONLY the sans-serif font Inter — no other fonts, no
serifs, no decorative faces. Do not show literal emoji glyphs as image content; render
each icon as a flat 2D pictogram. Do not depict needles entering skin, blood loss, or
distressing imagery; the tone is calm and explanatory. Never omit the williamriveromd.com
attribution.

QUALITY CHECK:
Must be mobile-readable at 600-px width, clinically plausible, visually calm,
publication-grade, and consistent with williamriveromd.com. Background must be white,
off-white, or soft light gray — never dark. All text legible at thumbnail size; the
four quadrants read as a single coherent poster; the EPO-ribbon-to-marrow flow on the
top-left and the locked-iron/macrophage motif on the top-right are clearly the two
narrative anchors. Copyright attribution williamriveromd.com must be visible in the
top-right strip.
```

---

## 1 — Patient · Circular vignette hero  *(hero-vignette skill)*

```
FILE NAME: epo-resistant-renal-anemia-vignette-hero.png
IMAGE TYPE: Circular vignette hero — Scaffold A (Clinical People Scene)
ASPECT RATIO: 1:1 (square — displayed circle-cropped)
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients
VISUAL GOAL: A calm, reassuring Filipino hemodialysis bedside scene that conveys "we know your EPO isn't working — and we have a plan" without any baked text.

PROMPT:
Square 1:1 photorealistic editorial photograph for a medical hero image, composed to be
cropped into a CIRCLE. A Filipino patient in their 50s–60s — warm, dignified, slightly
tired but composed — is seated comfortably in a reclined hemodialysis chair in a clean,
bright modern Philippine dialysis unit. A Filipino nephrologist (mid-career, white coat
with stethoscope, kind expression) leans in gently from the right, listening, with a
hand resting reassuringly near the patient's forearm where the AV-fistula access lies
under a soft gauze. On a tidy bedside tray between them: a small clinic-style
erythropoietin prefilled syringe (capped, simple unbranded) and a labeled clinical vial,
arranged neatly — quietly suggesting the EPO injection that is being discussed. A soft
warm golden window light falls across the patient's chest and upper arm — a gentle
"signal" cue — that softens into the cool teal ambient room light at the edges, hinting
that the signal is muted before it can reach further. Compose the patient's face and the
doctor's hand in the UPPER-MIDDLE of the frame, fully inside a centered circular safe
zone. Keep all four corners empty soft background (light teal / warm neutral falloff)
since the image will be masked to a circle. Soft natural daylight, gentle shallow depth
of field, calm reassuring documentary mood. Light, airy, professional color grade
harmonizing with teal #1a6b72 and navy #0f1e2e, with one warm gold-amber accent on the
patient's lit side. Absolutely NO text, NO title, NO captions, NO logo, NO watermark,
NO graphic overlays — a clean photograph only. Full-bleed, no borders or frames.

NEGATIVE INSTRUCTIONS:
No text of any kind (no title, subtitle, captions, numbers, labels, logo, or
williamriveromd.com watermark). No rectangular borders, frames, banners, or UI.
No important content in the corners (they get clipped by the circle). No dark, navy,
charcoal, or black background. No literal "glowing aura" around the patient or a
fantasy energy effect — keep the warm-light cue subtle and photographic. Avoid cartoon
style, clutter, over-saturation, HDR, distorted hands/faces, implausible anatomy or
equipment, stocky staged poses, branded packaging.

QUALITY CHECK:
Square 1:1. Single clear two-person scene centered in the circular safe zone with empty
soft corners. Faces and the doctor's reassuring hand sit in the upper-middle (~42% from
top). Light, calm, Filipino dialysis-unit context, publication-grade. Crops cleanly to a
circle with no text or subject lost at the edges. The EPO syringe + vial read as quiet
narrative props, not the focal point — the human relationship is the focal point.
```

---
