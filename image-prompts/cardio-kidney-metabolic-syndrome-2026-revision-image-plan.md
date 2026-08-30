# Image plan — CKM hub 2026 revision + HF-in-CKD gap

Six new figures for the sections added in the 2026 KDIGO revision. Everything else
in both guides reuses existing artwork (`ckm-triad-overview…`, `ckm-staging-ladder…`,
`ckm-common-soil-engine…`, `ckm-biomarker-panel…`, `ckm-egfr-dip-therapy…`,
`ckm-three-pillars…`, `ckm-fluid-congestion…`, `ckm-sglt2i-pleiotropy…`), whose
figcaptions were upgraded to the v2.0 `fig-desc` + `fig-abbrevs` structure.

Deliberately **not** illustrated: the indication-based pharmacotherapy matrix and the
multidisciplinary care table. Both are dense reference content that a real HTML table
renders more legibly, more accessibly, and more maintainably than a raster image.

House style: `williamriveromd-simple-figure` v1 — light backgrounds only, sans-serif
only (Inter / Nunito Sans / IBM Plex Sans / Manrope), `renalcarematters.com`
attribution mandatory.

| # | File | Guide · section | Scaffold | Size |
|---|---|---|---|---|
| 1 | `ckm-egfr-uacr-two-tests.png` | CKM · `#measuring` | B — comparison | 1792 × 1024 |
| 2 | `ckm-kidney-in-the-middle.png` | CKM · `#kidney-middle` | D — mechanism | 1792 × 1024 |
| 3 | `ckm-risk-tools-prevent-kfre.png` | CKM · `#md-risk` | E — reference card | 1536 × 1152 |
| 4 | `ckm-when-cause-needs-a-look.png` | CKM · `#whats-the-cause` / `#md-etiology` | A — algorithm | 1024 × 1536 |
| 5 | `ckm-obesity-kidney-masld.png` | CKM · `#weight-liver` / `#md-obesity` | D — mechanism | 1792 × 1024 |
| 6 | `heart-failure-ckd-potassium-ladder.png` | HF · `#md-potassium` | C — step sequence | 1792 × 1024 |

---

## 1

```
FILE NAME: ckm-egfr-uacr-two-tests.png
IMAGE TYPE: Scaffold B — side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients and clinicians)
VISUAL GOAL: Show that eGFR and UACR answer two different questions, so ordering only one leaves half the kidney unassessed.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical abstract style. White
(#ffffff) background. Title centered at top in bold navy (#0f1e2e), Inter typeface:
"Two tests, two different questions". Subtitle beneath in clinical teal (#1a6b72):
"Creatinine alone answers only half".
A soft dashed vertical divider splits the canvas into two equal panels.
LEFT panel header in clinical teal (#1a6b72): "eGFR — from blood". Beneath it a clean
semi-photorealistic cutaway of a single glomerulus with blood flowing through the
capillary tuft and filtrate leaving into the tubule, with a small teal flow-rate gauge
icon. Three short bullet labels in navy: "How FAST the kidney filters", "Falls late —
damage can precede it", "Distorted by muscle mass and rapid weight change". A small
amber (#b8860b) caution chip beneath reads: "A HIGH eGFR can mean hyperfiltration, not
health".
RIGHT panel header in soft purple (#6c3d8e): "UACR — from urine". Beneath it a clean
semi-photorealistic cutaway of the same glomerular filtration barrier shown damaged,
with small albumin protein spheres slipping across the barrier into the tubule and a
specimen cup icon. Three short bullet labels in navy: "WHETHER protein is leaking",
"The earlier and more sensitive signal", "Predicts heart events as well as kidney ones".
A small clinical red (#b91c1c) chip beneath reads: "The test most often skipped".
A single horizontal bottom strip on soft gray (#f3f4f6) spanning the full width, navy
text, centered: "Order both. Either can be abnormal while the other still looks normal.
Confirm an unexpected result before calling it chronic kidney disease."
Rounded panel corners, ample negative space, mobile-readable labels at 11pt minimum.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
Do NOT draw a whole kidney bean shape in either panel — both panels are glomerular-scale.
Do NOT imply one test replaces the other or label either panel "better".
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and
consistent with renalcarematters.com house style. Background must be white or soft light
gray — never dark. Copyright attribution renalcarematters.com must be visible in the
bottom-right corner.
```

## 2

```
FILE NAME: ckm-kidney-in-the-middle.png
IMAGE TYPE: Scaffold D — single mechanism / one-panel poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: Show that a damaged kidney stops being only a victim of CKM syndrome and becomes a driver of cardiac injury through six named pathways.

PROMPT:
Medical pathophysiology infographic, AJKD/NEJM graphical abstract style. White (#ffffff)
background. Title at top in bold navy (#0f1e2e), Inter typeface: "The kidney in the
middle". Subtitle in clinical teal (#1a6b72): "Once damaged, the kidney drives cardiac
injury — it is not only a bystander".
Centre-left: a semi-photorealistic 3D anatomical kidney rendered in muted clinical
colours, subtly shaded to suggest scarring. Centre-right: a semi-photorealistic 3D
anatomical human heart, its left ventricle wall drawn visibly thickened.
Six labelled rounded cards on soft gray (#f3f4f6) arranged in an arc between and around
the two organs, each with a small icon, a bold navy label and one short line of detail,
each connected to the heart by a colour-coded arrow flowing kidney → heart:
1. "Sodium and water retention" — more volume for the heart to move (teal #1a6b72 arrow)
2. "Anemia" — less erythropoietin, so the heart beats faster for the same oxygen (teal)
3. "Mineral and bone disorder" — calcium and phosphate stiffen artery walls (amber #b8860b)
4. "Retained uremic metabolites" — some are directly toxic to myocardium (amber)
5. "Inflammation and oxidative stress" — accelerates atherosclerosis (red #b91c1c)
6. "Neurohormonal activation and fibrosis" — remodelling of the ventricle (red)
A single thin looping arrow returns from the heart back to the kidney, labelled in navy:
"and the failing heart reduces kidney perfusion in turn".
Bottom strip, full width, soft gray, navy text centered: "Protecting the kidney IS heart
protection — lower eGFR and higher albuminuria are each independently associated with
death, myocardial infarction, stroke and heart failure."
Ample negative space, no clutter, mobile-readable labels at 11pt minimum.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
Do NOT draw more than six pathway cards. Do NOT use causal wording on the bottom strip
beyond "associated with" — the underlying evidence is observational.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and
consistent with renalcarematters.com house style. Background must be white or soft light
gray — never dark. Copyright attribution renalcarematters.com must be visible in the
bottom-right corner.
```

## 3

```
FILE NAME: ckm-risk-tools-prevent-kfre.png
IMAGE TYPE: Scaffold E — reference / quick-look card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians
VISUAL GOAL: Stop the common error of using PREVENT as a kidney-failure calculator by putting the three instruments side by side with their actual scope.

PROMPT:
Clinical reference card, publication-grade nephrology design. White (#ffffff) background.
Bold navy (#0f1e2e) title at top, Inter typeface: "Cardiovascular risk and kidney-failure
risk are different questions". Subtitle in clinical teal (#1a6b72): "Three instruments,
three scopes — none substitutes for another".
A compact three-column table below, column headers in white on clinical teal (#1a6b72)
bands: "PREVENT", "KFRE", "KDIGO GFR–albuminuria heat map". Four labelled rows down the
left in navy on soft gray (#f3f4f6): "Predicts", "Population", "Inputs", "Does NOT do".
Cell content, concise:
- Predicts: "10- and 30-year total CVD, ASCVD and heart failure" | "2- and 5-year risk of
  kidney failure needing kidney replacement therapy" | "Relative risk across ten outcomes
  simultaneously"
- Population: "General adults" | "CKD G3–G5 (KDIGO 1A)" | "Any CKD assessment"
- Inputs: "eGFR in the base model; UACR and HbA1c optional" | "Age, sex, eGFR, UACR" |
  "GFR category × albuminuria category"
- Does NOT do: highlighted in clinical red (#b91c1c) — "estimate kidney failure" |
  "estimate total cardiovascular risk" | "give an absolute individual risk"
A single amber (#b8860b) footnote bar spanning the width beneath the table, navy text:
"The published heat map omits the eGFR ≥105 band — creatinine-based eGFR is J-shaped at
the high end, and hyperfiltration is common in obesity and early diabetic kidney disease."
Alternating row fills, white and very soft gray. Mobile-readable, uncluttered.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid invented numeric risk values, avoid overprocessed HDR, avoid excessive saturation.
Do NOT render example percentages or a sample patient — this is a scope comparison only.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and
consistent with renalcarematters.com house style. Background must be white or soft light
gray — never dark. Copyright attribution renalcarematters.com must be visible in the
bottom-right corner.
```

## 4

```
FILE NAME: ckm-when-cause-needs-a-look.png
IMAGE TYPE: Scaffold A — clinical algorithm / flowchart
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians (readable by informed patients)
VISUAL GOAL: Give a short decision path for when reduced kidney function in a metabolic patient should not simply be attributed to diabetes or hypertension.

PROMPT:
Clinical nephrology algorithm, KDIGO guideline flowchart aesthetic. Single focused
pathway for establishing the cause of chronic kidney disease in a patient with metabolic
disease. White (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter typeface:
"Do not assume diabetes or hypertension caused it". Rounded rectangular nodes, bold
connecting arrows, top-to-bottom flow, maximum three branching levels.
Entry node in navy: "Reduced eGFR and/or raised UACR in a patient with diabetes,
hypertension or obesity".
Decision node in clinical teal (#1a6b72): "Does the story fit diabetic kidney disease?
— adequate diabetes duration · albuminuria preceding GFR decline · gradual progression
· retinopathy often present".
Left branch, labelled "Fits" in renal green (#1f7a4d), leading to a green action node:
"Classify by cause, GFR and albuminuria · estimate kidney-failure and cardiovascular
risk separately · treat by indication · monitor".
Right branch, labelled "Does not fit" in amber (#b8860b), leading to an amber node
titled "Look further — any one of these" containing a compact two-column list in navy:
"Persistent hematuria · eGFR falling faster than explained · nephrotic-range proteinuria
· active urinary sediment · CKD at a young age · strong family history · rash, arthritis
or unexplained fever · structural abnormality on imaging · tubular or electrolyte
derangement out of proportion to GFR · no retinopathy".
From the amber node, a red (#b91c1c) escalation node: "Nephrology referral — repeat urine
studies, imaging, serology; kidney biopsy where the histology would change management
(KDIGO 2D)".
A small teal note box at the bottom, navy text: "A common cause in the room is not proof
of the cause in front of you. Some alternative diagnoses have specific treatment."
Generous whitespace, no spaghetti routing, mobile-readable labels at 11pt minimum.
Bottom-center: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid overprocessed HDR, avoid excessive saturation, avoid more than three branch levels.
Do NOT use alarming imagery — this figure prompts evaluation, not fear.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and
consistent with renalcarematters.com house style. Background must be white or soft light
gray — never dark. Copyright attribution renalcarematters.com must be visible in the
bottom-center.
```

## 5

```
FILE NAME: ckm-obesity-kidney-masld.png
IMAGE TYPE: Scaffold D — single mechanism / one-panel poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: Trace visceral and ectopic fat through hyperfiltration and albuminuria to CKD, with MASLD as the parallel liver track, and show where treatment enters.

PROMPT:
Medical pathophysiology infographic, AJKD/NEJM graphical abstract style. White (#ffffff)
background. Title at top in bold navy (#0f1e2e), Inter typeface: "Where CKM usually
begins — adipose tissue, the kidney and the liver". Subtitle in clinical teal (#1a6b72):
"Not just how much fat, but what kind and where".
Left third: a clean semi-photorealistic cross-section of the abdomen showing visceral
adipose tissue around the organs, clearly distinguished from a thin subcutaneous layer,
with small labelled arrows for released adipokines and cytokines.
Centre: two parallel colour-coded tracks flowing left to right from the adipose panel.
UPPER track in clinical teal, labelled "Kidney", drawn as four connected rounded cards:
"Insulin resistance and neurohormonal activation" → "Glomerular hyperfiltration —
surviving filters forced to overwork" → "Albuminuria appears first" → "Glomerulosclerosis
and progressive CKD". A semi-photorealistic glomerulus sits beside the hyperfiltration
card with an amber (#b8860b) chip: "eGFR can look normal or HIGH here".
LOWER track in soft purple (#6c3d8e), labelled "Liver", drawn as three connected cards:
"Ectopic fat deposition" → "MASLD" → "Amplifies both cardiovascular and kidney risk",
with a semi-photorealistic liver beside the middle card.
Right edge: a vertical renal-green (#1f7a4d) intervention rail with a downward arrow
touching both tracks, headed "Where treatment enters", listing: "Diet, activity and
behaviour", "GLP-1 receptor agonists", "Metabolic and bariatric surgery".
Bottom strip, full width, soft gray (#f3f4f6), navy text: "Duration matters — long-term,
early-onset obesity carries the highest risk of later CKD. Asian populations reach the
same risk at a lower BMI and waist. In advanced CKD, target fat mass, not body mass."
Ample negative space, mobile-readable labels at 11pt minimum.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
Do NOT depict a stigmatising or caricatured human body — use anatomical cross-section only.
Do NOT show weight or BMI numbers on a scale or a person.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and
consistent with renalcarematters.com house style. Background must be white or soft light
gray — never dark. Copyright attribution renalcarematters.com must be visible in the
bottom-right corner.
```

## 6

```
FILE NAME: heart-failure-ckd-potassium-ladder.png
IMAGE TYPE: Scaffold C — horizontal step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Make stopping guideline-directed therapy the last step rather than the first when potassium rises.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top center in
bold navy (#0f1e2e), Inter typeface: "Hyperkalemia on guideline-directed therapy — work
down the ladder before you stop the drug". Subtitle in clinical teal (#1a6b72): "Heart
failure with chronic kidney disease".
Seven rounded rectangular cards arranged horizontally in a single row, connected by bold
navy right-pointing arrows, sitting on a very soft gray panel (#f3f4f6). Each card has a
colored top accent band, a small icon, a bold navy step label and two short detail lines:
1. Teal (#1a6b72) — "CONFIRM": "Exclude pseudohyperkalemia", "Hemolysis · fist clenching
   · tourniquet · high platelets"
2. Teal — "REVIEW THE LIST": "NSAIDs, trimethoprim, heparin, calcineurin inhibitors",
   "Potassium-containing salt substitutes"
3. Teal — "CORRECT ACIDOSIS": "Shifts potassium back intracellularly", "Independently
   reasonable in CKD"
4. Renal green (#1f7a4d) — "USE THE DIURETIC": "Increases distal potassium secretion",
   "Treats congestion at the same time"
5. Green — "MODERATE THE DIET": "Moderate, do not eliminate", "Blanket restriction costs
   fruit, vegetables and fiber"
6. Amber (#b8860b) — "BIND": "Patiromer or sodium zirconium cyclosilicate", "Enables
   continued therapy — surrogate endpoint, not mortality"
7. Clinical red (#b91c1c) — "ONLY THEN REDUCE": "Stopping is the last step, not the
   first", "Document a rechallenge plan and date"
Bottom strip, full width, soft gray, navy text centered: "People with CKD whose RASi is
down-titrated or stopped fare worse than matched people who continue — an association,
not a randomized comparison, but enough to shift the default."
Generous whitespace, mobile-readable labels at 11pt minimum.
Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid overprocessed HDR, avoid excessive saturation.
Do NOT print specific potassium threshold values — thresholds vary by guideline and setting.
Do NOT imply potassium binders reduce mortality.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and
consistent with renalcarematters.com house style. Background must be white or soft light
gray — never dark. Copyright attribution renalcarematters.com must be visible in the
bottom-right corner.
```

---

## After generation

Save each as `images/<file-name>` plus a matching `.webp`, then wire into the guide with
the v2.0 figure structure — `<picture>` with a WebP `<source>`, explicit `width`/`height`,
`loading="lazy"`, and a `<figcaption>` carrying `<p class="fig-desc">` and, where the image
contains acronyms, `<dl class="fig-abbrevs">`. Then re-run
`audit_acronym_expansion.py --guide <file>`: a new `fig-abbrevs` entry adds that acronym to
the guide's tracked set and can move an acronym's first use earlier in the document.
