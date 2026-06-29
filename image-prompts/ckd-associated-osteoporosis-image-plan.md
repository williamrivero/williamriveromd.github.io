# Image Plan — `ckd-associated-osteoporosis.html`
### CKD-Associated Osteoporosis — Bringing Skeletal Fragility & CKD-MBD Under One Clinical Umbrella · williamriveromd.com

**Stage 1 prompt pack** for the new clinician-mode guide *"CKD-Associated
Osteoporosis."* Each prompt below was authored with the correct house image
skill (`/williamriveromd-hero-vignette`,
`/williamriveromd-infographic-skill`,
`/williamriveromd-biomedical-mechanism-figure`,
`/williamriveromd-algorithm-generator-skill`) and is ready to paste into the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator).

Generate each at the stated size, save the PNG **and** a `.webp` twin to
`images/`, then optionally run Stage 2 (`williamriveromd-local-image-generator`)
for manifests and og:image wiring.

House rules applied to every prompt:

- **Light background only** (white / off-white / soft gray / light teal tint).
  Navy `#0f1e2e` / teal `#1a6b72` are typography and accent, never a fill.
- **Approved fonts only** — Inter, Nunito Sans, IBM Plex Sans, or Manrope.
  Never a serif font.
- **Attribution mandatory** — small semi-transparent
  `© williamriveromd.com` in the bottom-right (bottom-center for portrait
  algorithms) of every figure *except* the circular hero vignette (which is
  masked by CSS and cannot carry corner text).
- **English-only on-image text.** The guide is single-mode clinician (no
  multilingual toggle) — no Tagalog / Cebuano / Kapampangan strings inside
  any figure.

> **Central thesis carried by every figure:** CKD-associated osteoporosis is
> a single, individualized problem — not two competing diagnoses. Name the
> dominant lesion, sequence CKD-MBD before bone-targeting, and weigh every
> drug on both the skeletal *and* vascular ledgers.

---

## Plan overview

| # | Placement | File (PNG + WebP twin) | Skill | Type | Size | Priority |
|---|-----------|------------------------|-------|------|------|----------|
| Hero | `.hero-vignette` (circular) | `ckd-associated-osteoporosis-hero.png` | hero-vignette | Circular anatomy still — umbrella + nephron + vertebra | 1024 × 1024 | **Core** |
| OG | head `og:image` (social share card) | `ckd-associated-osteoporosis-og.png` | infographic | 1.91:1 share card, navy + teal on white | 1200 × 630 | **Core** |
| 1 | §1 *The Treatment Gap* | `ckd-associated-osteoporosis-01-treatment-gap.png` | infographic | Bar chart + KPI callout (fracture vs prescribing) | 1792 × 1024 | **Core** |
| 2 | §2 *Nosology* | `ckd-associated-osteoporosis-02-umbrella-tmv.png` | infographic | Conceptual umbrella schematic + TMV axes | 1792 × 1024 | **Core** |
| 3 | §3 *Pathophysiology* | `ckd-associated-osteoporosis-03-fgf23-axis.png` | biomedical-mechanism-figure | Organ → osteocyte/nephron inset → injury / intervention / benefit | 1792 × 1024 | **Core** (signature mechanism) |
| 4 | §4 *Workup* | `ckd-associated-osteoporosis-04-workup-algorithm.png` | algorithm-generator | Vertical journal-style diagnostic algorithm | 1024 × 1536 | **Core** |
| 5 | §6 *Therapeutics* | `ckd-associated-osteoporosis-05-master-algorithm.png` | algorithm-generator | House-style master treatment decision tree (eGFR × turnover) | 1024 × 1536 | **Core** |

Insert each finished figure as a `<figure class="illus-wrap illus-wrap-light">`
with a `<figcaption class="illus-caption">` (already present in the guide
body — just replace the placeholder PNG/WebP files in `images/`). The first
inline figure on the page is already wired with `fetchpriority="high"`.

---

## Hero — `/williamriveromd-hero-vignette`

```
FILE NAME: ckd-associated-osteoporosis-hero.png
IMAGE TYPE: Circular vignette hero — Scaffold C calm 3D anatomy / illustration
ASPECT RATIO: 1:1 (square — displayed circle-cropped)
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: clinicians (nephrology · IM · endocrinology · bone specialists)
VISUAL GOAL: visualise the "one umbrella" thesis — a single canopy sheltering
both kidney and skeleton — at a glance, with no embedded text.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration for a hero image,
composed to be cropped into a CIRCLE. A single clean render of a stylised
slender umbrella canopy floating above and gently sheltering a pair of human
kidneys (rendered in restrained renal red, anatomically plausible) and a
single human lumbar vertebra (rendered in soft ivory bone tone with subtle
trabecular detail), the two organs arranged side-by-side beneath the canopy
on a soft, uncluttered light teal-tinted background. The umbrella is a calm
muted clinical teal, the canopy slightly translucent so soft daylight passes
through. Gentle studio lighting from upper-left, soft drop shadow. Compose
the umbrella tip and the two organs in the UPPER-MIDDLE of the frame
(roughly 38–48% down), fully inside a centered circular safe zone — keep
all four corners empty soft background. The background falls off into a
slightly deeper light-teal tone toward the rim. Light, airy, publication-
grade color grade harmonising with teal #1a6b72 and navy #0f1e2e.
Absolutely NO text, NO title, NO captions, NO numbers, NO leader lines, NO
labels, NO logos, NO watermark — a clean illustration only. Full-bleed, no
borders or frames. Clean sans-serif label conventions are forbidden — there
are no labels in this image. Anatomy is restrained, not gory; tone is
reassuring and editorial.

NEGATIVE INSTRUCTIONS:
No text of any kind (no title, subtitle, captions, numbers, labels, logo,
or williamriveromd.com watermark). No rectangular borders, frames, banners,
or UI. No important content in the corners (they get clipped by the circle).
No dark, navy, charcoal, or black background. Avoid cartoon style, clutter,
over-saturation, HDR, distorted anatomy, garish renal red, implausible
vertebra detail, or photorealistic faces / hands (no people).

QUALITY CHECK:
Square 1:1. Single clear subject (umbrella + kidneys + vertebra) centered in
the circular safe zone with empty soft corners. Key detail in the upper-
middle (~42% from top). Light, calm, publication-grade. Crops cleanly to a
circle with no text or anatomy lost at the edges.
```

---

## OG / Social Share Card — `/williamriveromd-infographic-skill`

```
FILE NAME: ckd-associated-osteoporosis-og.png
IMAGE TYPE: OG / social share card (editorial split layout)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630  (NON-NEGOTIABLE)
AUDIENCE: clinicians (nephrology · IM · endocrinology · bone specialists)
VISUAL GOAL: A social-share card that conveys "one umbrella, one patient"
in two seconds — title left, clean 3D pair of organs (kidney + vertebra)
under a calm teal umbrella icon on the right.

PROMPT:
Editorial Open Graph share card on a clean white background, 1200 × 630
landscape. Left two-thirds: a strong navy headline set in Inter (#0f1e2e),
"CKD-Associated Osteoporosis", with a clinical-teal subtitle set in Manrope
(#1a6b72), "One umbrella for skeletal fragility & CKD-MBD." A small
uppercase eyebrow label in soft gray reads "CLINICIAN REFERENCE ·
williamriveromd.com". Right one-third: a calm semi-photorealistic 3D
illustration of a stylised clinical-teal umbrella canopy sheltering a
single human kidney and a single lumbar vertebra side by side, on a soft
off-white surface with gentle daylight and shallow depth of field. Restrained
clinical color (renal reds, teal accent, ivory bone). Generous whitespace,
no clutter, mobile-readable at thumbnail size. Use ONLY Inter / Manrope /
Nunito Sans typefaces — never a serif font. Footer line in soft gray
typography "© williamriveromd.com" in the lower-right at ~11 px equivalent.
House palette: navy #0f1e2e, teal #1a6b72, soft gray #6b7280, off-white
background #fafafa.

NEGATIVE INSTRUCTIONS:
No dark backgrounds (no navy, charcoal, or black fills). No cartoon style.
No clutter. No tiny unreadable labels. No AI gibberish text. No serif
fonts. No decorative or handwritten typefaces. No stocky stock-photo look.
Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1200 × 630. Headline readable at 600 px wide. Light background.
House palette respected. Attribution visible bottom-right.
```

---

## Figure 1 — Treatment-gap KPI bar chart — `/williamriveromd-infographic-skill`

```
FILE NAME: ckd-associated-osteoporosis-01-treatment-gap.png
IMAGE TYPE: Multi-panel educational infographic — bar chart + KPI callout
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (mixed nephrology + IM + endocrinology)
VISUAL GOAL: Anchor §1 with the visual KPI of the treatment gap —
fracture incidence rises with falling eGFR while bone-targeted prescribing
falls; pin the 2.3% / 2.6% prescribing statistic.

PROMPT:
Clinician-facing patient-education infographic poster, landscape 16:9, on a
clean white background with soft gray section dividers. Title at top-left in
navy Inter 700: "The CKD Treatment Gap". A short subtitle in dark-teal
Manrope 500: "Fracture risk rises with falling eGFR while bone-targeted
prescribing falls."

Center-left panel — a clean grouped bar chart comparing two stratified
populations across four eGFR bins (G1–G2 ≥60, G3 30–59, G4 15–29, G5/G5D
<15 mL/min/1.73m²) on the x-axis. For each bin, two grouped bars:
(a) age-adjusted hip-fracture incidence per 1,000 person-years (taller bars
for lower eGFR, color: navy #0f1e2e) and (b) population-matched non-CKD
control incidence (color: muted clinical teal #1a6b72). Y-axis in Inter
Regular, gridlines soft gray #e5e7eb. Bars rounded at the top, clean and
uncluttered.

Right panel — a vertical KPI callout card on a very pale red background
(#fff0f0) with a red left border (#b91c1c). Large numerals in Inter 800:
"2.3% / 2.6%". Below in small navy Manrope: "Dialysis-population denosumab
and oral-bisphosphonate prescribing — Titan et al. 2020; Bird et al. 2024."
A second smaller line below in soft red: "The KPI of therapeutic
nihilism."

Bottom-strip key takeaways in three modular cards (white card on soft-gray
background), one short line each in dark navy Manrope: "Coexistence is the
rule." · "Fracture risk multiplies with declining eGFR." · "Bone specialist
defers — nephrologist defers — patient fractures."

House palette: navy #0f1e2e, clinical teal #1a6b72, soft red #b91c1c, soft
gray #e5e7eb. Typography ONLY in Inter (headings) and Manrope (body) —
never a serif font. Subtle "© williamriveromd.com" attribution in soft
navy at 70% opacity, bottom-right corner at ~11 px equivalent.

NEGATIVE INSTRUCTIONS:
No dark backgrounds. No cartoon style. No 3D bar art, no glossy bars, no
neon. No tiny unreadable labels. No AI gibberish numbers. No serif fonts.
Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1792 × 1024. Bars mobile-readable. KPI numeral huge and dominant.
Attribution visible bottom-right. House palette respected.
```

---

## Figure 2 — Umbrella convergence + TMV schematic — `/williamriveromd-infographic-skill`

```
FILE NAME: ckd-associated-osteoporosis-02-umbrella-tmv.png
IMAGE TYPE: Conceptual schematic — convergence + small inset
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: The unifying umbrella — two distinct diagnostic trees
(hormone-driven osteoporosis vs mineral-homeostasis–driven CKD-MBD) meet
under one canopy labelled "CKD-associated osteoporosis", with downstream
arrows pointing to fragility fracture and cardiovascular events.

PROMPT:
Clinician educational schematic, landscape 16:9, on a clean white
background. Title at top in navy Inter 700: "The Unifying Umbrella".
Subtitle below in dark-teal Manrope: "Two biologically distinct disorders.
Two converging outcomes."

Center composition — a large stylised translucent teal umbrella canopy
(#1a6b72 at low opacity) labelled with a small uppercase Inter eyebrow
"CKD-ASSOCIATED OSTEOPOROSIS" running along its inside arc. Beneath the
canopy, two diagnostic trees enter from the left and right and merge under
the canopy:

- Left tree (label "OSTEOPOROSIS — hormone-driven"): three small navy
  rounded cards stacked diagonally — "Menopausal estrogen loss",
  "Senescence", "Glucocorticoids / immobility".
- Right tree (label "CKD-MBD — mineral-homeostasis driven"): three small
  navy rounded cards stacked diagonally — "FGF-23 ↑ early", "Hyper-Pi /
  Hypocalcemia", "Secondary HPT".

Two thin teal arrows leave the bottom of the umbrella and point to two
outcome capsules — left capsule (red border, pale red fill): "FRAGILITY
FRACTURE" in red Inter 700; right capsule (amber border, pale amber fill):
"CARDIOVASCULAR EVENTS" in amber Inter 700.

Right-margin inset (small, dashed-border) — a clean 3-axis schematic of the
TMV bone-biopsy classification: three labelled orthogonal axes "TURNOVER"
(vertical), "MINERALIZATION" (horizontal), "VOLUME" (depth) with four small
markers placed in the quadrants for high-turnover, low-turnover/adynamic,
osteomalacia, and mixed uremic patterns. Restrained labels in Inter 600.

House palette: navy #0f1e2e, clinical teal #1a6b72, soft red #b91c1c,
amber #b8860b, soft gray #e5e7eb. Typography ONLY in Inter (titles +
labels) and Manrope (subtitles + body). Subtle
"© williamriveromd.com" attribution in soft navy at 70% opacity bottom-
right at ~11 px equivalent.

NEGATIVE INSTRUCTIONS:
No dark backgrounds. No cartoon umbrellas. No emoji. No tiny unreadable
labels. No 3D umbrella art (kept vector-stylised). No serif fonts.
Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1792 × 1024. Trees clearly enter from both sides and converge.
Outcome capsules clearly downstream of canopy. TMV inset legible at
publication size.
```

---

## Figure 3 — FGF-23 / Klotho / PTH biomedical mechanism — `/williamriveromd-biomedical-mechanism-figure`

```
FILE NAME: ckd-associated-osteoporosis-03-fgf23-axis.png
IMAGE TYPE: Biomedical mechanism schematic (review-article)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A publication-grade review-article mechanism schematic that
shows how the FGF-23 / Klotho / PTH / vitamin-D axis evolves across CKD
stages, with a parallel bone-vascular crosstalk inset; bottom flow pins
the dual-benefit modifiable targets.

PROMPT:
Create a publication-grade biomedical mechanism schematic about:

**Topic:** The mineral-bone axis in CKD and its bone-vascular crosstalk.

**Disease context:** CKD G1–G5D / CKD-MBD.

**Central mechanism:** FGF-23 rises first → Klotho falls →
1,25(OH)₂D suppressed → PTH hysteresis then secondary
hyperparathyroidism, with skeletal PTH hyporesponsiveness; vascular smooth
muscle cells transdifferentiate to osteoblast-like phenotype while bone
loses mineral.

**Organ-level panel (left):**
Show a simplified pair of human kidneys in light gray-blue, declining
function shown by a stage banner along the bottom edge reading
"G1 → G2 → G3 → G4 → G5/G5D" (small Inter 600). A small dashed connector
box on the right edge points to the magnified mechanism panel.

**Magnified mechanism panel (center):**
A dashed-bordered inset showing an osteocyte (top) connected by a thin line
to a nephron tubule (below). Highlight the osteocyte in pale yellow. Add
concise callouts:
- Osteocyte: ↑ FGF-23 (earliest signal)
- Klotho expression: ↓
- Renal 1α-hydroxylase: ↓ 1,25(OH)₂D
- Parathyroid: PTH ↑ (after hysteresis), skeletal PTH hyporesponsiveness
  (variable response)

**Parallel inset panel (right):**
A dashed-bordered inset of a small artery cross-section. Show a vascular
smooth muscle cell transdifferentiating to an osteoblast-like cell, with
hydroxyapatite deposits beginning to form in the media. Highlight the
transitioning cell in pale yellow. Callouts:
- VSMC → osteoblast-like phenotype
- Hyper-Pi, inflammation, oxidative stress drive
- "Calcification paradox" — bone loses mineral, vessel gains it

**Bottom summary flow:**
Left pathology box (pale pink):
- Hyperphosphatemia
- Chronic inflammation
- Oxidative stress
- Uremic toxins
- **Skeletal + vascular injury (one biology, two compartments)**

Center intervention/mechanism box (gray):
- Phosphate control (diet · binders)
- Anti-inflammatory levers
- Oxidative-stress modulation
- Stage-matched vitamin D repletion
- (experimental) Intermittent PTH early in CKD

Right benefit/outcome box (pale blue):
- ↓ Bone resorption mismatch
- ↓ Vascular calcification progression
- Preserved bone quality
- Plausible CV-risk attenuation (open research question)

Arrow flow from injury → intervention → benefit.

Use a white background, muted clinical colors (light gray-blue anatomy,
pale yellow highlights, red for arteries / injury, blue for veins /
protective effects, pale pink injury box, pale blue benefit box), clean
sans-serif labels set in Inter or Nunito Sans (never a serif font), thin
dashed connector lines, and a review-article figure style. Avoid
photorealism, dark backgrounds, decorative elements, and overcrowding.

Include a small "© williamriveromd.com" footer in the bottom-right corner,
medium gray (~#6b7280), professional and unobtrusive.

NEGATIVE INSTRUCTIONS:
No photorealism. No dark backgrounds. No cartoon styling. No invented
pathways. No anatomically implausible structures. No serif fonts. No
gibberish labels. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1792 × 1024. Organ-level panel left, magnified inset center,
parallel vascular inset right, bottom summary flow with three colored
boxes. Mechanism faithful to current consensus. Attribution visible
bottom-right.
```

---

## Figure 4 — Diagnostic workup flowchart — `/williamriveromd-algorithm-generator-skill` (Style Mode B — journal)

```
FILE NAME: ckd-associated-osteoporosis-04-workup-algorithm.png
IMAGE TYPE: Clinical algorithm flowchart (journal nephrology style)
ASPECT RATIO: 2:3 (portrait)
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: A diagnostic algorithm that takes the clinician from "CKD G3–
G5D + suspected fragility" through biochemistry → BTMs → DXA / TBS → biopsy
trigger, terminating in one of four turnover phenotypes that drive the
§6 master algorithm.

PROMPT:
Create a clean academic medical journal treatment algorithm flowchart on a
white background. The design should resemble a nephrology review figure:
minimal, centered, symmetrical, and publication-ready.

Use these visual conventions:
- Beige rounded rectangles for diagnosis, disease category, or severity
  classification
- Pale blue rounded rectangles for assessment phases or treatment stages
- Pale green rounded rectangles for therapeutic options, maintenance,
  disease control, and remission outcomes (here used for the four turnover
  phenotypes that exit the algorithm)
- Pale amber rounded rectangle for the biopsy-trigger node (caution)
- Thin muted blue/teal arrows
- Top-down flow with balanced left-right branching
- Consistent rounded corners, box widths, and vertical spacing
- No icons, no decorative graphics, no dark background
- Typography should be clean, black, and journal-like, set in Inter or
  Nunito Sans (never a serif font)

Content to render:

Title at the top in navy Inter 700:
"Diagnostic Workup — CKD-Associated Osteoporosis"

Subtitle in soft-gray Manrope:
"Establish turnover before choosing drug class."

Top entry node (beige):
"Patient with CKD G3–G5D + suspected fragility / low-trauma fracture / DXA
T-score ≤ −2.0"

Three parallel assessment branches (pale blue) descend from the entry:
1. "Biochemistry panel
   Ca · Pi · iPTH · 25(OH)D
   ± albumin / ionised Ca"
2. "Bone turnover markers (non-renally cleared)
   BSAP · P1NP · TRAP-5b
   pair formation + resorption"
3. "Imaging
   DXA + TBS
   ± HR-pQCT (research)"

All three branches merge into a single central decision diamond (pale blue
diamond):
"Concordant turnover phenotype?"

From the diamond:
- Branch LEFT — "Concordantly high turnover" → pale green endpoint:
  "HIGH-TURNOVER + OSTEOPOROSIS phenotype → §6 high-turnover pathway"
- Branch CENTER — "Concordantly low turnover" → pale green endpoint:
  "LOW-TURNOVER / ADYNAMIC phenotype → §6 anabolic pathway"
- Branch RIGHT — "Discordant / unexplained / pre-antiresorptive in
  advanced CKD" → pale amber rounded rectangle (biopsy trigger):
  "BIOPSY REFERRAL
   • Unexplained Ca / Pi
   • Suspected osteomalacia
   • Pre-long-term antiresorptive when adynamic plausible
   • Atypical fracture
   • Pre-transplant"

A thin dashed arrow returns from the biopsy node to a fourth pale green
endpoint:
"MIXED / OSTEOMALACIA phenotype → §6 mineralization / mixed pathway"

Design requirements:
- Keep all text concise
- Preserve clinical hierarchy
- Use centered alignment
- Maintain wide margins
- Avoid clutter
- Make the final image look like a medical journal figure
- Include a small professional footer reading "© williamriveromd.com"
  positioned at the bottom-right corner in subtle gray medical-publication
  styling

NEGATIVE INSTRUCTIONS:
No dark backgrounds. No cartoon icons. No 3D shadowed boxes. No serif
fonts. No tiny unreadable labels. No gibberish. Never omit the
williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1024 × 1536 (portrait). Top-down flow. Three parallel assessment
branches merge into a single decision diamond. Four distinct exit
phenotypes. Attribution visible bottom-right.
```

---

## Figure 5 — Master treatment decision tree — `/williamriveromd-algorithm-generator-skill` (Style Mode C — house style)

```
FILE NAME: ckd-associated-osteoporosis-05-master-algorithm.png
IMAGE TYPE: Clinical algorithm flowchart (williamriveromd.com house style)
ASPECT RATIO: 2:3 (portrait)
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: The master algorithm — eGFR × turnover → drug class. The
single image clinicians screenshot from the guide.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the
williamriveromd.com house style. Use a white or very light off-white
background, restrained navy and teal typography set in Inter or Manrope
(never a serif font), thin teal connector arrows, and generous margins.
The layout should be centered, symmetrical, and suitable for a clinician-
facing nephrology education guide.

Use these color conventions:
- Navy #0f1e2e for title, body text, and structural emphasis
- Teal #1a6b72 for decision nodes and connector accents
- Green #1f7a4d for final recommended actions or qualifying endpoints
- Amber #b8860b for caution nodes (boxed-warning drugs)
- Red #b91c1c for contraindicated nodes
- Soft gray for explanatory side notes

Content to render:

Title at top in navy Inter 700:
"CKD-Associated Osteoporosis — Master Treatment Algorithm"

Subtitle in soft-gray Manrope:
"CKD-MBD first → stratify by turnover → pick drug class."

Top entry node (teal rounded rectangle):
"Patient with CKD G1–G5D + fragility / fracture / DXA T ≤ −2.5"

Step 1 (navy rounded rectangle):
"Stage CKD (eGFR) + establish turnover (BTMs ± biopsy)."

Step 2 (navy rounded rectangle):
"Foundation moves (every patient):
• Exercise (weight-bearing + resistance)
• Falls / culprit-med review
• Ca 800–1000 mg/d (do not exceed ~1500)
• Vitamin D repletion"

Step 3 (navy rounded rectangle):
"Correct mineral metabolism & SHPT first
(phosphate control, PTH suppression, calcimimetic if HD)."

Decision diamond 1 (teal diamond):
"eGFR ≥ 30 mL/min?"

- LEFT branch (YES):
  Decision diamond 2a (teal): "Turnover?"
  - High-turnover → green rounded rect: "Suppress turnover, then ORAL
    BISPHOSPHONATE (alendronate / risedronate)."
  - Low-turnover / adynamic → amber rounded rect: "AVOID potent
    antiresorptive. Consider TERIPARATIDE off-label after biopsy
    confirmation."
  - Postmenopausal HD-naïve woman, VTE-low → green rounded rect:
    "RALOXIFENE second-line."

- RIGHT branch (NO — eGFR < 30 mL/min):
  Decision diamond 2b (teal): "Turnover?"
  - High-turnover + osteoporosis → amber rounded rect with red border:
    "DENOSUMAB with §6c safety bundle
    • Correct CKD-MBD first
    • Ca + active vitamin D cover
    • Ca check day 3 / 7 / 10 post-dose
    • Follow-on antiresorptive planned at INITIATION
    (FDA boxed warning Jan 2024)"
  - Low-turnover / adynamic → red rounded rect: "AVOID denosumab and
    bisphosphonates. Consider TERIPARATIDE off-label after biopsy."
  - Selected — postmenopausal HD, VC-low burden → amber rounded rect with
    red border: "ROMOSOZUMAB
    • FDA boxed warning: MI / stroke / CV death
    • 12-month course → mandatory follow-on antiresorptive"

Tail node (navy rounded rectangle):
"Plan EXIT at initiation: every denosumab / romosozumab course needs a
documented follow-on antiresorptive (rebound vertebral-fracture risk)."

Side note (soft gray, right margin):
"Weigh every choice on the vascular ledger.
Calcium-containing binders → minimise in established VC."

Design requirements:
- Clear title and subtitle
- Top-to-bottom clinical logic
- Rounded rectangles for actions and endpoints
- Diamonds for decision points
- Consistent spacing and alignment
- No dark background
- No clutter
- No photorealistic people
- Include a small professional footer reading "© williamriveromd.com"
  positioned at the bottom-right corner in subtle gray medical-publication
  styling

NEGATIVE INSTRUCTIONS:
No dark backgrounds. No cartoon icons. No 3D shadowed boxes. No serif
fonts. No tiny unreadable labels. No gibberish. Never omit the
williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1024 × 1536 (portrait). Top-down flow. Branches by eGFR (≥30 vs
<30) and then by turnover. Color logic: green = recommended, amber =
caution / boxed warning, red = contraindicated. Attribution visible
bottom-right.
```

---

## Stage 2 hand-off (optional)

After generating the six files above (PNG **and** WebP twins) into
`images/`, invoke
`/williamriveromd-local-image-generator` to:

1. Validate every prompt's schema (filename, size, archetype).
2. Build `/Users/williamgregoryrivero/Downloads/ckd-associated-osteoporosis/`
   with manifest CSV + JSON + README-image-generation.md.
3. Confirm the og:image / og:image:width / og:image:height / og:image:alt
   tags are correctly wired in `ckd-associated-osteoporosis.html` (they are
   already authored — only need re-confirmation after the OG card is
   produced).

No HTML changes are required when replacing images — the guide already
references the correct paths inside `<picture>` / `<figure>` blocks and the
hero `<picture>`. Drop the new PNGs into `images/` and the page picks them
up.
