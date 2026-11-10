# Image Plan & Prompt Pack — *Hold the Ketoanalogue Until You See a Nephrologist*

**Guide:** `guides/hold-ketoanalogue-until-nephrology-review.html`
**Slug:** `hold-ketoanalogue-until-nephrology-review`
**Prepared:** 11 November 2026 (Asia/Manila) · Stage 1 prompt pack for the ChatGPT Image Generator GPT
**Skills applied:** williamriveromd-hero-vignette (v3) · williamriveromd-infographic-skill (v5) · williamriveromd-simple-figure (v1) · williamriveromd-biomedical-mechanism-figure
**Attribution on every figure:** `© renalcarematters.com` (public guide set)

---

## Part 1 — Image plan blueprint

### 1.1 What the images must do

The guide carries one idea that is easy to state and easy to misread: *the food plan comes first, and the tablets do not cancel extra protein.* Readers range from a grandmother who cooks for a patient with CKD to a cardiologist deciding whether to write a prescription. The images therefore have three jobs:

1. **Make the invisible visible.** Protein in a shake, calcium in a tablet, and nitrogen in the blood cannot be seen. Each figure turns one hidden quantity into something a reader can count or compare.
2. **Carry the message without reading.** A reader with limited literacy should get the point from the picture alone: a plate, a can, a scale, a card resting on a tablet box. Words on images are short labels, never sentences.
3. **Stay honest.** No kidney "healing" imagery, no dialysis-countdown clocks, no tablets drawn as shields. Nothing may suggest the tablets reverse CKD or make extra protein safe.

### 1.2 Reader levels and the visual strategy for each

| Reader | What they need from a picture | Strategy used |
|---|---|---|
| Low literacy / older patient | One message, recognizable objects | Photoreal Filipino food and packaging; numbers in big type; one icon per idea |
| Caregiver who cooks | What to change in the kitchen | Real plate, real shake can, a simple tally card |
| Educated patient | Why the rule exists | The four-piece "one program" image; the two-errors comparison |
| Referring clinician | What to do and in what order | Portrait algorithm with color-coded nodes |
| Nephrologist / dietitian | The mechanism and its limits | Review-article mechanism figure with the nitrogen arithmetic |

### 1.3 Figure map

| # | File (PNG + WebP twin) | Section / tab | Skill & archetype | Size |
|---|---|---|---|---|
| H | `hold-ketoanalogue-until-nephrology-review-vignette-hero` | Hero (patient tab) | Hero vignette v3 · Scaffold B still-life · Archetype I Object Hero · top-down | 2048 × 2048 |
| OG | `hold-ketoanalogue-until-nephrology-review-og` | Social share card | Infographic v5 · OG card | **1200 × 630** |
| 01 | `…-01-one-program` | Patient · What They Are | Simple figure · Scaffold C step/assembly (4 pieces) | 1792 × 1024 |
| 02 | `…-02-protein-ledger` | Patient · Hidden Protein | Infographic v5 · Food matrix / photoreal + tally | 1792 × 1024 |
| 03 | `…-03-two-errors` | Patient · Cutting Too Much | Simple figure · Scaffold B comparison with center panel | 1792 × 1024 |
| 04 | `…-04-handoff-pathway` | Clinician · Handoff | Simple figure · Scaffold A algorithm | 1024 × 1536 |
| 05 | `…-05-nitrogen-mechanism` | Clinician · Physiology | Biomedical mechanism figure (illustrated, softly rendered) | 1792 × 1024 |
| 06 | `…-06-two-errors-clinician` | Clinician · Four Harms | Simple figure · Scaffold B comparison | 1792 × 1024 |
| RG | `…-rg-thumb.webp` | Related-guide cards on other pages | Crop of OG or hero | 600 × 600 (square crop) |

Figures 07 (patient, “Give the protein a job”) and 08 (clinician, “The anabolic sink”) were added later; their prompts are in the separate file `hold-ketoanalogue-until-nephrology-review-image-prompts-addendum-activity.md`.

All filenames are already wired into the guide HTML with matching `alt` text, `fig-desc`, and `fig-abbrevs`. Save each as `images/<file>.png` **and** `images/<file>.webp`.

### 1.4 Style decisions

- **Rendered, not flat.** Your guides use GPT-rendered illustration; flat SVG-style vectors look out of place. Every diagram prompt below asks for softly shaded, semi-3D illustrated objects on a light background. The mechanism figure keeps the review-article *layout* (organ panel, dashed inset, bottom flow) but with rendered, not flat-vector, objects.
- **Light backgrounds only.** White, off-white, or very light teal tint. Navy is for text and lines.
- **Fonts:** Inter for every on-image label (named in each prompt).
- **Color logic shared across all figures:** teal = the plan / coordinated care; amber = caution or "too much"; clinical red = danger or urgent; renal green = the balanced, supervised target; soft purple = honesty or uncertainty notes.
- **Recurring objects** (so the set reads as one family): the same plain white tablet box with no brand, the same unbranded shake can, the same handwritten meal-plan card, and the same planned plate of rice, vegetables, and a small piece of fish. No real brand names or logos anywhere.
- **People:** the hero has no person (Object Hero) to break the run of couple-at-table heroes. Figure 02 uses hands only. Figure 03 shows one household with no faces in close-up. This avoids repeating the stock older-Filipino-couple archetype.

### 1.5 Words on images — budget

| Figure | Max words (excluding attribution) | Language |
|---|---|---|
| Hero | 0 | — |
| OG | ≤ 14 | English |
| 01, 02, 03 | ≤ 25 each, short labels and numbers | English (captions are translated in the HTML) |
| 04 | ≤ 70, node labels only | English |
| 05, 06 | ≤ 60, labels and arrows | English |

### 1.6 Accuracy guardrails for the generator

- Numbers that may appear: 48 g, 25 g, 73 g, +25 g, 36 mg N per tablet, 50 mg calcium per tablet, 12 tablets = 432 mg N ≈ 2.7 g protein-equivalent, 25 g shake ≈ 4 g N. These come from the guide and the product information. **No other numbers.**
- Never show: a kidney regenerating or "turning pink again," a tablet acting as a shield, a dialysis-delay countdown, a pass/fail eligibility badge, a dose-by-weight chart, a crossed-out "STOP tablets" sign, or a crossed-out whole food group.
- The tablets are always shown *with* the plan, never alone as the solution.

---

## Part 2 — Copy-ready prompts

### H — Hero vignette

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: Top-down (overhead flat lay), slight 10° tilt for depth
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: mixed (patients, caregivers, clinicians)
VISUAL GOAL: At a glance, the written food plan sits on top of the tablets — the plan comes first.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I — Object Hero. Camera: top-down overhead flat lay with a slight 10-degree tilt for depth.

Subject: on a clean, light warm-cream Philippine kitchen countertop in soft morning daylight, a handwritten meal-plan card on lined paper (illegible soft pencil lines and simple sketched plate shapes, no readable words or numbers) rests squarely ON TOP of a closed, plain white unbranded box of tablets, as if the card is holding the box shut. Beside it, a small white plate shows a planned portion: a modest mound of steamed white rice, sautéed green vegetables (kangkong or pechay), and one small piece of grilled fish. At the outer edge of the arrangement, deliberately set apart, sits one unbranded matte protein-shake can with a plain label and no readable text. Supporting details only: a small glass of water and a wooden measuring spoon.

Visual hierarchy: the meal-plan card on the tablet box is the hero (60–70% of the circle, slightly below and left of center); the plate, the set-apart shake can, and the water glass are supporting context (20–30%). Reserve a 20–25% TITLE SAFE ZONE in the upper-right portion of the circle as clean, softly blurred countertop and gentle light gradient — no objects, food, labels, or shadows inside that zone.

Calm, reassuring, appetizing-but-clinical color grade: warm neutrals with subtle clinical teal #1a6b72 accents (a teal cloth napkin edge, a teal pencil on the card). Shallow depth of field, soft natural shadows, edge falloff toward a slightly deeper neutral at the rim of the circle. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO readable text or labels on any object, no brand names, no logos, no titles, no captions, no watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, dozens of icons, tiny unreadable labels, infographic clutter, duplicated objects, repeated compositions, cropped circle, cropped objects, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, readable packaging copy, real pharmaceutical brands, rectangular borders, frames, banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation, pills spilled dramatically, a kidney organ, medical shields or glowing effects.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant hero subject (meal-plan card on the closed tablet box) occupying 60–70% of the circle, 2–4 supporting elements, 20–25% empty title-safe zone at upper right. No people. Camera framing (top-down still-life) differs from the previous guide's hero. Crops cleanly inside the circle with no text or subject lost at the edges.
```

### OG — Social share card

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-og.png
IMAGE TYPE: OG / social share card (infographic v5)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed
VISUAL GOAL: In a Facebook or Viber preview, readers see "plan before the tablets" and the shake problem instantly.

PROMPT:
Social share card, 1200×630, white (#ffffff) background with a very light teal tint panel (#eef6f7) on the right 45%. Left 55%: title in bold Inter, navy #0f1e2e, three lines: "Hold the Ketoanalogue" / "until you see" / "a Nephrologist". Under it, one short line in clinical teal #1a6b72, Inter medium: "Food plan first. Tablets don't cancel extra protein." Right panel: a photorealistic top-down still-life on a light countertop — a handwritten meal-plan card (no readable words) resting on a closed plain white unbranded tablet box, a small planned plate of rice, green vegetables and a small piece of fish, and an unbranded protein-shake can set apart at the edge with a small amber (#b8860b) circular "+25 g" tag beside it. Soft daylight, shallow depth of field, calm color grade. Thin teal rule separating the panels. Generous whitespace, nothing near the edges. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy Inter text, 70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, generic stock-photo look, excessive saturation, real brand names or logos, kidney organ imagery, glowing shields, dialysis countdowns. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter — no serif, decorative, or handwritten typefaces for the title. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200 × 630. Title fully legible at thumbnail size. Background light. Attribution visible bottom-right. No more than 14 words of text besides the attribution.
```

### 01 — One program, not one pill (patient)

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-01-one-program.png
IMAGE TYPE: Simple figure — Scaffold C assembly sequence (4 pieces → 1 program)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: The tablets are one piece of a four-piece program; alone they are an incomplete puzzle.

PROMPT:
Clean patient-education figure on a white (#ffffff) background. Title at top center in bold Inter, navy #0f1e2e: "One program, not one pill". Center: four large rounded jigsaw-puzzle pieces, softly shaded semi-3D (not flat vector), fitting together into one square. Each piece holds one rendered object and a short Inter label beneath: (1) teal #1a6b72 piece — a handwritten meal-plan card, label "Written food plan"; (2) renal green #1f7a4d piece — a bowl of rice with vegetables and a small banana, label "Enough energy"; (3) soft gray piece — a plain white unbranded tablet box, label "Tablets"; (4) navy-outlined piece — a calendar page with one date circled and a small stethoscope, label "Follow-up". Small arrows show the pieces sliding together. Lower left: a separate small inset of the tablet piece alone, faded to 40% opacity with a dashed outline and the label "Tablet alone = incomplete" in amber #b8860b. Generous whitespace, soft shadows, light and calm. Bottom-right: "renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat clip-art, clutter, tiny unreadable labels, AI gibberish text, unrealistic objects, overprocessed HDR, excessive saturation, real brand names, kidney regeneration imagery, shields, countdown clocks. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter — no serif, decorative, or handwritten typefaces. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Readable on a phone in 10 seconds; four labels plus title only; tablets visually equal in size to the other three pieces, never dominant; light background; attribution bottom-right.
```

### 02 — The protein ledger (patient)

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-02-protein-ledger.png
IMAGE TYPE: Infographic v5 — food matrix with photoreal objects and a running tally
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients, caregivers, renal dietitians
VISUAL GOAL: A shake quietly adds 25 g to a 48 g plan; you can see it by reading the label and adding it up.

PROMPT:
Photorealistic-plus-infographic kitchen-counter scene on a light warm-cream surface, overhead three-quarter view, bright daylight. Left 40%: a white plate with a planned Filipino meal — steamed rice, sautéed pechay, one small piece of fish — with a small rounded teal (#1a6b72) tag "Meals 48 g". Center 25%: an unbranded matte protein-shake can held by one adult hand (hands only, Filipino skin tone, no face), the nutrition panel on the can shown as a simplified, legible inset magnifier with a single highlighted amber (#b8860b) line "Protein 25 g per serving" (all other panel lines blurred and illegible). Right 35%: a clean white tally card, softly shaded, with Inter text in navy #0f1e2e: "Meals 48 g" / "+ Shake 25 g" / bold divider / "Total 73 g" and below it a renal-green (#1f7a4d) dashed line labeled "Your plan: 48 g" with the 25 g excess shown as an amber bar segment labeled "+25 g". Small footnote under the card in Inter, teal: "Tablets are counted separately." Generous whitespace, calm, appetizing, clinical. Bottom-right: "renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, gibberish nutrition-panel text (blur all lines except the highlighted protein line), real brand names or logos, overprocessed HDR, excessive saturation, warning skulls or red X marks, kidney imagery, any percentage of kidney risk. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
The arithmetic reads 48 + 25 = 73 and +25 g exactly; no other numbers. Hands only, no face. Light background. Attribution bottom-right.
```

### 03 — Two opposite errors (patient)

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-03-two-errors.png
IMAGE TYPE: Simple figure — Scaffold B comparison with a center target panel
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Too much and too little are both mistakes; the planned plate in the middle is the goal.

PROMPT:
Medical-education comparison figure, white (#ffffff) background, softly rendered semi-3D photoreal objects (not flat vector). Title at top center in bold Inter, navy #0f1e2e: "Two errors, one goal". Three rounded panels on soft gray (#f3f4f6). LEFT panel, amber (#b8860b) header "Too much": a white plate with an oversized portion of fried pork and two eggs beside a large unbranded protein-shake glass. CENTER panel, slightly larger and raised, renal green (#1f7a4d) header "Planned plate": a balanced plate of rice, sautéed vegetables and a small piece of fish next to a handwritten meal-plan card (no readable words) and a plain white tablet box. RIGHT panel, amber header "Too little": a nearly empty plate with a few grains of rice and a glass of water, and beside it a belt loosened by one notch on the table to suggest weight loss. Thin dashed arrows from left and right panels point toward the center panel. Footer strip in Inter, teal #1a6b72: "Set the plate with your kidney team and dietitian." Generous whitespace. Bottom-right: "renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, crossed-out whole food groups, red X marks over food, frightening or sick-looking people, faces, real brand names, overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Both side panels use the same caution color (amber), not red — neither is shamed more than the other. Center panel visually dominant. No people's faces. Light background. Attribution bottom-right.
```

### 04 — Handoff pathway (clinician)

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-04-handoff-pathway.png
IMAGE TYPE: Simple figure — Scaffold A clinical algorithm (portrait)
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians (referring physicians, nephrologists, renal dietitians, pharmacists)
VISUAL GOAL: A referring clinician sees the order: goal → written food plan → reconciliation → monitoring owner; current users are reviewed, not stopped.

PROMPT:
Clinical nephrology algorithm, KDIGO-style guideline flowchart aesthetic, white (#ffffff) background, top-to-bottom flow, softly shaded rounded nodes with subtle depth (not flat). Title at top in bold Inter, navy #0f1e2e: "Before the first ketoanalogue tablet". Start node (navy outline): "Ketoanalogue being considered (non-dialysis adult CKD)". Decision node (teal #1a6b72): "Already on a prescribed regimen?" — YES branch to the right into a soft purple (#6c3d8e) side node: "Review the plan with the prescriber — do not stop abruptly"; NO branch continues down. Step 1 node (teal): "Document reason and patient goal; eGFR trend, ACR, weight trend". Step 2 node (renal green #1f7a4d): "Nephrology + renal dietitian: written protein g/day, energy kcal/day, reference weight and basis". Step 3 node (teal): "Reconcile every shake/supplement and all calcium sources". Step 4 node (renal green): "Name the monitoring owner, interval, and reassessment triggers". Caution node on the left (amber #b8860b): "Unstable, frail, poor intake, or losing weight → assess nutrition before any restriction". Red escalation node at the bottom left (#b91c1c): "Urgent symptoms → emergency care, not a nutrition appointment". A thin dashed teal bracket running down the full right margin labeled "Other kidney-protective care continues meanwhile". Maximum 9 nodes, generous whitespace, bold navy arrows, no crossing lines. Bottom-center: "renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, spaghetti arrows, clutter, tiny unreadable labels, AI gibberish text, eligibility scores, pass/fail badges, dose numbers, tablet counts, green "eligible" checkmarks, overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Node text matches the wording above exactly; no numeric doses or targets appear; the "do not stop abruptly" side branch is visible; light background; attribution bottom-center (portrait).
```

### 05 — Nitrogen mechanism (clinician)

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-05-nitrogen-mechanism.png
IMAGE TYPE: Biomedical mechanism figure — organ panel → magnified inset → bottom flow (illustrated, softly rendered)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians, renal dietitians
VISUAL GOAL: Ketoanalogues spare nitrogen only when dietary protein is low; their capacity is a small fraction of one protein shake.

PROMPT:
Create a publication-grade biomedical mechanism figure in the review-article layout, rendered as soft semi-3D medical illustration with gentle shading (not flat vector), white (#ffffff) background, muted clinical palette, all labels in Inter.

Topic: How ketoanalogues spare nitrogen — and why they cannot absorb extra protein.
Disease context: non-dialysis CKD on a low- or very-low-protein diet.

Organ-level panel (left, ~30%): a liver and a pair of kidneys in light gray-blue, connected by a bloodstream line. Dietary protein (a small plate icon) enters the gut → amino acids → liver, where a pale-red arrow labeled "Deamination → urea" flows to the kidneys labeled "CKD: ↓ clearance of urea, H⁺, phosphate". A small dashed connector box links the liver to the magnified panel.

Magnified mechanism panel (center-right, ~45%, inside a thin dashed border): a hepatocyte/muscle-cell schematic showing transamination. A keto-acid molecule (pale yellow hexagon, labeled "Ketoanalogue") receives an amino group (small blue "–NH₂" token) from a non-essential amino acid and becomes an "Essential amino acid" (blue hexagon) used for protein synthesis. Callouts: "Nitrogen reused, not added" and "Works only when intake is low and energy is adequate". A side gauge inside the panel compares two vertical bars on one scale: a short bar labeled "12 tablets accept ≈0.4 g N" and a tall amber (#b8860b) bar labeled "One 25 g shake ≈ 4 g N". Small note beneath the bars in Inter, soft purple: "Order-of-magnitude arithmetic, not a measured effect".

Bottom summary flow (full width): LEFT pale-pink box "Problem drivers": "Unrestricted or rising protein intake" · "Low energy → muscle breakdown" · "↑ urea, acid, phosphate". CENTER box with a small plain white tablet box and a meal-plan card: "Supervised program: written food plan + enough energy + ketoanalogues + follow-up". RIGHT pale-blue box "Intended effects (selected patients)": "↓ urea generation" · "Essential amino acids preserved" · "Nutrition monitored". Arrows flow left → center → right. Tiny Inter footnote in navy, right of the flow: "Benefit shown in selected, supervised trials; not with tablets alone."

Generous whitespace, thin dashed connectors, legible labels. Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid flat clip-art vector style, cartoon styling, photorealism of organs with gore, dark backgrounds, decorative effects, overcrowding, invented pathways, gibberish chemical structures, additional numbers beyond those specified, kidney regeneration imagery, tablets drawn as shields or filters that "remove" protein. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY the sans-serif font Inter. Never omit the attribution.

QUALITY CHECK:
Only the numbers "≈0.4 g N", "≈4 g N", "12 tablets", "25 g" appear; transamination drawn as amino-group transfer from a non-essential amino acid to the keto-acid; the uncertainty note is present; light background; attribution bottom-right.
```

### 06 — Two errors, clinician version

```
FILE NAME: hold-ketoanalogue-until-nephrology-review-06-two-errors-clinician.png
IMAGE TYPE: Simple figure — Scaffold B comparison (clinician)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Escalation and over-restriction are opposite errors with different evidence strength; the documented plan sits between them.

PROMPT:
Clinician comparison figure, AJKD graphical-abstract style, white (#ffffff) background, softly rendered semi-3D icons (not flat). Title in bold Inter, navy #0f1e2e: "Two errors around one prescription". Three columns on soft gray (#f3f4f6) rounded panels. LEFT, amber (#b8860b) header "Protein escalation": icons of an unbranded shake can with a magnified "25 g/serving" label line, an enlarged meat portion, and a supplement tub; evidence chip in soft purple (#6c3d8e): "Plausible — not measured; ask every visit". CENTER, teal (#1a6b72) header "Documented plan": a clipboard checklist with five short lines — "Protein g/day", "Energy kcal/day", "Reference weight + basis", "Renal dietitian", "Monitoring owner" — and a small plain tablet box beside it. RIGHT, amber header "Unsupervised restriction": icons of a small plate, a downward weight-trend line next to a body-weight scale with an edema droplet to signal fluid confounding, and a weakened grip dynamometer; evidence chip in soft purple: "Observational signal: weight loss on KA-VLPD". Thin dashed arrows from both sides into the center. Footer strip in Inter, teal: "Read weight with fluid status; albumin alone does not certify nutrition." Bottom-right: "renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat clip-art, clutter, tiny unreadable labels, AI gibberish text, red danger styling on either side, eligibility scores, dose tables, real brands, overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Evidence chips present on both sides and worded exactly; checklist lines exact; no numbers other than "25 g/serving"; light background; attribution bottom-right.
```

---

## Part 3 — Production checklist

1. Generate each prompt in the Image Generator GPT; regenerate any image whose text is misspelled, contains extra numbers, or shows a brand.
2. Save `images/<file>.png` and a WebP twin `images/<file>.webp` (quality ~82). Keep the exact filenames above; the guide already references them.
3. **Related-guide thumbnail:** export a square crop of the OG card's photo panel (or the hero) as `images/hold-ketoanalogue-until-nephrology-review-rg-thumb.webp` at 600 × 600. The calculator page's related card already points to it.
4. The OG meta tags are already set (`og:image`, width 1200, height 630, alt text). No HTML change needed after upload.
5. After upload, open the guide in light and dark mode on a phone and confirm the hero disc crops cleanly and figures 01–03 read in under 10 seconds.
6. Optional Stage 2: hand this file to `williamriveromd-local-image-generator` to create `image-manifest.csv/json` and the local folder.
