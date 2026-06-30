# Image Plan — `ai-in-nephrology-practice.html`
### Artificial Intelligence in Nephrology Practice — A Clinician's Perspective · williamriveromd.com

**Stage 1 prompt pack** for the 12 raster assets that illustrate this guide. Each
prompt is authored with the matching williamriveromd graphic skill, ready to
paste into the [ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator).
Save the PNG (+ `.webp` twin) outputs into `images/`, then optionally hand the
pack to Stage 2 (`williamriveromd-local-image-generator`) for manifests + `og:image` wiring.

**The guide is currently single-mode clinician.** This pack covers visuals that
work in clinician mode today *and* a small patient-mode subset that would let
the guide be promoted to dual-mode later (or be reused as social/explainer
collateral). The audience is called out on every prompt.

**House rules applied to every prompt:** light backgrounds only (navy / teal are
typography + accent, never a fill), the navy / teal / green / amber / red /
purple palette, sans-serif type (Inter / Nunito Sans / IBM Plex Sans / Manrope —
named explicitly in every prompt), mobile-readable labels, and the mandatory
`williamriveromd.com` attribution bottom-right (bottom-center for portrait).

> **On-image text is English only** — consistent with every other Perspectives
> guide. The hero-meta labels translate via HTML; the raster images do not.

---

## Plan overview

| # | Section / use | File | Skill | Type | Size | Audience |
|---|---|---|---|---|---|---|
|  1 | Hero circular vignette (beside `<h1>`) | `ai-in-nephrology-practice-vignette-hero.png` | hero-vignette | Scaffold A — clinician people scene | 1024 × 1024 (1:1) | Clinician |
|  2 | OG / share card | `ai-in-nephrology-practice-og.png` | infographic | OG editorial poster | **1200 × 630 (fixed)** | Mixed |
|  3 | §M1 Foundations — AI / ML / DL / LLM taxonomy ladder | `ai-in-nephrology-practice-01-taxonomy-ladder.png` | simple-figure | Single mechanism / one-panel (D) | 1792 × 1024 (16:9) | Mixed |
|  4 | §M3 AKI — alert → action bundle algorithm | `ai-in-nephrology-practice-02-aki-alert-bundle.png` | algorithm-generator | Style Mode C — house style | 1024 × 1536 (2:3) | Clinician |
|  5 | §M4 Pathology — oculo-renal axis mechanism | `ai-in-nephrology-practice-03-oculo-renal-axis.png` | biomedical-mechanism-figure | Review-article schematic | 1792 × 1024 (16:9) | Clinician |
|  6 | §M7 LLMs — RAG architecture for clinical use | `ai-in-nephrology-practice-04-rag-architecture.png` | simple-figure | Horizontal step sequence (C) | 1792 × 1024 (16:9) | Clinician |
|  7 | §M8 Governance — eGFR race-coefficient reclassification | `ai-in-nephrology-practice-05-egfr-reclassification.png` | simple-figure | Side-by-side comparison (B) | 1792 × 1024 (16:9) | Mixed |
|  8 | §M8 Governance — model lifecycle loop | `ai-in-nephrology-practice-06-governance-loop.png` | simple-figure | Single mechanism / circular (D) | 1024 × 1024 (1:1) | Clinician |
|  9 | §10 The 7-point appraisal checklist clinician card | `ai-in-nephrology-practice-07-appraisal-checklist-card.png` | simple-figure | Reference card (E) | 1536 × 1152 (4:3) | Clinician |
| 10 | §11 Kidney–CV–Metabolic crosstalk sigil | `ai-in-nephrology-practice-08-kidney-cv-metabolic-sigil.png` | organ-crosstalk-sigil | Triangular sigil | 1024 × 1024 (1:1) | Mixed |
| 11 | Patient-mode — "AI helps draft. Your doctor decides." | `ai-in-nephrology-practice-09-patient-llm-safety.png` | simple-figure | Horizontal step sequence (C) | 1792 × 1024 (16:9) | Patient |
| 12 | Patient-mode — "What AI is doing in your kidney care" | `ai-in-nephrology-practice-10-patient-overview.png` | simple-figure | Single mechanism / one-panel (D) | 1792 × 1024 (16:9) | Patient |

> The guide HTML already references `ai-in-nephrology-practice-vignette-hero.{webp,png}`
> at `width="1254" height="1254"`. When you save the 1024 × 1024 hero, either bump
> the markup to `1024 1024` or keep the markup square — the CSS round-mask works
> with both.

---

## 1 · Hero vignette — Filipino nephrologist with subtle AI overlay
*Skill: williamriveromd-hero-vignette · Scaffold A — Filipino clinical people scene*

> Square, masked into the round hero disc. Faces and key detail in the
> **upper-middle (~42% from top)** so the CSS circle crop never loses them. No
> baked-in titles, logos, or watermarks — the page renders the `<h1>` next to
> the circle.

```
FILE NAME: ai-in-nephrology-practice-vignette-hero.png
IMAGE TYPE: Circular vignette hero — Scaffold A (clinical people scene)
ASPECT RATIO: 1:1 (square — displayed circle-cropped)
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: Clinicians
VISUAL GOAL: Convey the editorial thesis in one frame — a thoughtful Filipino nephrologist at the bedside, working with (not replaced by) a translucent AI decision-support overlay.

PROMPT:
Square 1:1 photorealistic editorial photograph for a medical hero image, composed to be cropped into a CIRCLE. A warm, mid-career Filipino nephrologist in a clean white coat with a stethoscope around the neck, standing at a hospital bedside reviewing a tablet or wall-mounted clinical display. On the display, a soft translucent overlay shows a kidney silhouette, an EHR-style sparkline of labs, and a small confidence-band curve — clearly illustrative, never realistic enough to be a real chart, never readable as words. A Filipino patient is visible in soft focus in the lower foreground (back of the head and shoulder only — no face) suggesting the bedside context without distracting from the physician. Clean, bright, modern Philippine hospital interior. Soft natural daylight from a window left, gentle shallow depth of field, calm reassuring documentary mood. Compose the nephrologist's face and the tablet in the UPPER-MIDDLE of the frame, fully inside a centered circular safe zone — keep all four corners empty soft background, since the image will be masked to a circle. Background falls off into a soft, slightly deeper light-teal/neutral tone toward the edges. Light, airy, professional color grade harmonizing with teal #1a6b72 and navy #0f1e2e. Absolutely NO text, NO title, NO captions, NO logo, NO watermark, NO readable letters or numbers anywhere — a clean photograph only. Full-bleed, no borders or frames.

NEGATIVE INSTRUCTIONS:
No text of any kind (no title, subtitle, captions, numbers, labels, logo, or williamriveromd.com watermark). No rectangular borders, frames, banners, or UI chrome on the screen. No important content in the corners (they get clipped by the circle). No dark, navy, charcoal, or black background. Avoid cartoon style, clutter, over-saturation, HDR, distorted hands/faces, implausible anatomy, or stocky staged poses. Avoid sci-fi neon, hologram cliches, or "robot doctor" imagery — the AI overlay is restrained and quiet.

QUALITY CHECK:
Square 1:1. Single clear subject (nephrologist + tablet) centered in the circular safe zone with empty soft corners. Face and tablet in the upper-middle (~42% from top). Light, calm, Filipino clinical context, publication-grade. Crops cleanly to a circle with no text or subject lost at the edges.
```

---

## 2 · OG / share card — editorial poster
*Skill: williamriveromd-infographic-skill · OG / social share card*

> Fixed **1200 × 630** for Facebook / X / LinkedIn / iMessage. Title, tagline,
> author credit; no decorative clutter; light background.

```
FILE NAME: ai-in-nephrology-practice-og.png
IMAGE TYPE: OG / social share card — editorial poster
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: Mixed (clinicians and informed patients)
VISUAL GOAL: A scannable share card that names the editorial — AI in nephrology, written by a practicing nephrologist, framed as perspective rather than hype.

PROMPT:
Editorial OG share card, 1200 × 630, for a clinician-facing nephrology perspective titled "Artificial Intelligence in Nephrology Practice". Light off-white background (#fafafa) with a very faint soft gray panel band on the right third (#f3f4f6). Left two-thirds: bold sans-serif title in navy (#0f1e2e) set in Inter, two lines maximum — "Artificial Intelligence in Nephrology Practice" with the word "Nephrology" emphasized in clinical teal (#1a6b72). Below it, a one-line tagline in medium-weight navy at ~28pt equivalent: "A practicing nephrologist's perspective — 8 modules + a 7-point appraisal checklist." Below that, a small author chip with a thin teal underline: "W. Rivero, MD · FPCP · DPSN · williamriveromd.com". Right third: a small, calm semi-photorealistic 3D vignette — a stylized kidney silhouette in muted renal red overlapping a subtle EHR-style sparkline and a single small circular "AI" node with three thin teal connector lines (no glowing neon, no hologram look). All on the off-white field, edges soft. Generous whitespace, strong type hierarchy, mobile-readable at thumbnail. Bottom-right: "williamriveromd.com" in small semi-transparent navy text, ~10–11px equivalent, ~70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No glowing neon "AI" cliches, no robot-doctor imagery, no hologram brain. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1200 × 630. Title legible at Facebook/X thumbnail size. Light background. Single clean right-side vignette (kidney + spark + AI node), not a multi-panel collage. williamriveromd.com attribution visible bottom-right.
```

---

## 3 · §M1 Foundations — AI / ML / DL / LLM taxonomy ladder
*Skill: williamriveromd-simple-figure · Scaffold D — Single mechanism / one-panel poster*

> The "mental model without engineering jargon" figure: four nested concentric
> labels with one renal example per layer.

```
FILE NAME: ai-in-nephrology-practice-01-taxonomy-ladder.png
IMAGE TYPE: Single mechanism / one-panel poster (Scaffold D)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Mixed (clinicians and informed patients)
VISUAL GOAL: Show that AI is a family of nested ideas — ML inside AI, DL inside ML, LLM inside DL — and ground each layer in a concrete nephrology use case.

PROMPT:
Medical-education taxonomy figure, AJKD / NEJM graphical-abstract style. White (#ffffff) background. Title at top in bold navy (#0f1e2e) set in Inter: "Artificial Intelligence in Nephrology — a Nested Mental Model". Subtitle in clinical teal (#1a6b72), medium weight: "AI ⊃ ML ⊃ DL ⊃ LLM — each layer with a concrete renal task." Center the canvas on four concentric rounded rectangles, left-aligned vertically, slightly nested like Russian dolls (largest at left, smaller stacked inward to the right). Layer 1 (outermost, light teal tint #eef6f7): label "ARTIFICIAL INTELLIGENCE" in navy; subtext: "Software that performs tasks normally requiring human judgement." Layer 2 (light gray #f3f4f6): label "MACHINE LEARNING" in navy; subtext: "Patterns learned from data, not hand-coded rules." Layer 3 (very light renal-green tint): label "DEEP LEARNING" in navy; subtext: "Multilayer neural networks for images and sequences." Layer 4 (innermost, very light amber tint): label "LARGE LANGUAGE MODELS" in navy; subtext: "Next-token prediction over text — ChatGPT-class tools." On the right side of the figure, four small rounded cards aligned with each layer, each tagged "Renal example": (1) "AI: KDIGO-aligned clinical decision support." (2) "ML: KFRE-style CKD risk prediction." (3) "DL: Histopathologic segmentation of glomeruli, tubules, interstitium." (4) "LLM: Drafting a discharge summary or patient handout — with verification." Connect each layer to its example card with a thin navy line. Generous whitespace. Mobile-readable labels ≥12pt equivalent. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com house style. Background must be white or soft light gray — never dark. Four nested rectangles with the renal-example card aligned to each. williamriveromd.com attribution visible bottom-right.
```

---

## 4 · §M3 AKI — alert → action bundle algorithm
*Skill: williamriveromd-algorithm-generator-skill · Style Mode C — house style*

> Portrait clinical algorithm for the 5-step bundle the guide spells out as
> `.algo-card` in HTML. Mirror the bundle structure so the figure and the body
> copy reinforce each other.

```
FILE NAME: ai-in-nephrology-practice-02-aki-alert-bundle.png
IMAGE TYPE: Clinical algorithm — williamriveromd.com house style (Style Mode C)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Clinicians
VISUAL GOAL: Turn an AI AKI alert into a concrete, ordered five-step action bundle so the prediction routes to care rather than to documentation.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the williamriveromd.com house style. White (#ffffff) background. Bold navy (#0f1e2e) title at top in Inter: "AI AKI Alert → Action Bundle". Optional subtitle in clinical teal (#1a6b72): "Five steps that turn a 48-hour lead-time prediction into care." Centered, symmetric, top-to-bottom flow with thin teal connector arrows and generous margins. Restrained navy and teal typography set in Inter (never a serif font). Use these color conventions: navy #0f1e2e for title, body text, and structural emphasis; teal #1a6b72 for decision/action nodes and connector accents; renal green #1f7a4d for final recommended actions and reassessment endpoints; amber #b8860b for caution / drug-hold nodes; soft gray for explanatory side notes.

Content to render — five rounded rectangular action nodes in vertical sequence, each numbered and labeled:

1. (teal) "REASSESS PERFUSION & VOLUME" — bedside MAP, capillary refill, lactate, focused POCUS (IVC, VEXUS, lung B-lines, focused cardiac).
2. (amber) "REVIEW EVERY NEPHROTOXIN & CONTRAST PLAN" — aminoglycosides, NSAIDs, vancomycin troughs, planned iodinated/gadolinium contrast; defer, substitute, or dose-adjust.
3. (amber) "RECOMPUTE RENALLY-CLEARED DOSES" — antimicrobials, LMWH/DOACs, gabapentinoids. Estimate trajectory, not yesterday's creatinine.
4. (teal) "SET A FLUID PLAN WITH A STOP RULE" — resuscitate when indicated, with a pre-declared deresuscitation trigger (MAP > 65 sustained, lactate clearing, urine output recovering).
5. (green) "DOCUMENT A 4–6 H REASSESSMENT LOOP" — close the loop so the algorithm changes care, not the chart.

To the right of the column, a small soft-gray side panel runs full-height with a vertical title "Honest caveats" and three short bullets: "≈ 2 false alerts per true alert at threshold"; "Training cohort skew (e.g. ~94% male)"; "Audit local PPV before letting it touch order sets."

Design requirements: clear title at top; consistent rounded rectangle widths; consistent vertical spacing; thin teal arrows between numbered steps; balanced left-right margins; no clutter; no photorealistic people; no 3D elements; no dark background. Optional simple flat line icons (heart, capsule, drop, beaker, clock) only if useful, never touching node borders. Include a small professional footer reading "© williamriveromd.com" positioned at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No spaghetti arrows, no decorative chrome, no glowing neon "AI" iconography. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Portrait 2:3, five numbered nodes in clean vertical flow with a single side-panel of caveats. Color logic honored (teal action, amber caution, green endpoint). Title and every node label legible at full and thumbnail size. © williamriveromd.com footer visible bottom-right.
```

---

## 5 · §M4 Pathology — oculo-renal axis mechanism figure
*Skill: williamriveromd-biomedical-mechanism-figure · Review-article schematic*

> Organ panel (eye + kidney) → magnified inset (retinal microvasculature ↔
> glomerular microvasculature) → bottom injury → intervention → benefit flow.

```
FILE NAME: ai-in-nephrology-practice-03-oculo-renal-axis.png
IMAGE TYPE: Biomedical mechanism schematic — review-article style
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Clinicians
VISUAL GOAL: Anchor the oculo-renal axis mechanistically so deep learning on retinal images for diabetic kidney disease reads as biologically plausible (shared microvascular biology), not magic.

PROMPT:
Create a publication-grade biomedical mechanism schematic about:

**Topic:** The oculo-renal microvascular axis — why deep learning on retinal images can infer diabetic kidney disease.

**Disease context:** Diabetic kidney disease (DKD), considered as a microvascular complication that co-occurs with diabetic retinopathy.

**Central mechanism:** Hyperglycemia-driven endothelial injury affects the retinal and glomerular microcirculations in parallel; a deep-learning model trained on retinal photographs learns a non-invasive microvascular signature that tracks DKD risk.

**Organ-level panel (left):**
Show a simplified vector cross-section of a human eye on the upper left, labeled "Retina"; below it, a simplified vector cross-section of a kidney labeled "Kidney". Both organs muted clinical colors (light gray-blue anatomy, soft renal red for the kidney medulla). A small dashed connector box runs from each organ pointing to a single magnified panel in the center.

**Magnified mechanism panel (center, dashed inset):**
Inside the dashed inset, two side-by-side magnified vector schematics. LEFT half labeled "Retinal microvasculature" — show a retinal arteriole and venule with capillary network, microaneurysms as small red dots, and a thin label "Pericyte loss · BM thickening · ↑ permeability". RIGHT half labeled "Glomerular microvasculature" — show a glomerulus with afferent/efferent arterioles, mesangium, and podocytes, with a thin label "GBM thickening · Mesangial expansion · Podocyte loss · ↑ permeability". A thin dashed bidirectional arrow links the two halves, captioned "Shared hyperglycemic microvascular injury".

**Bottom summary flow (left → center → right):**
Left pink pathology box: "Hyperglycemia → endothelial dysfunction → microvascular injury → DKD."
Center pale blue intervention/mechanism box: "Deep-learning model trained on retinal images" with a small healthy-retina icon, plus a small italic flag: "Population-level screening — not biopsy substitution."
Right pale blue benefit/outcome box: "Non-invasive DKD screening signal · Earlier risk stratification · Useful where biopsy/UACR not feasible."

Use a white background, muted clinical colors (light gray-blue anatomy, soft yellow highlights, red for injury/arteries, blue for benefit boxes), clean sans-serif labels set in Inter (never a serif font), thin dashed connector lines, and a review-article figure style. Match anatomy to the mechanism — do not invent pathways. Flag the deep-learning step explicitly as a screening tool, not a routine clinical replacement for biopsy or UACR. Include a small, semi-transparent navy `© williamriveromd.com` attribution in the bottom-right corner, ~10–11px, not obscuring any figure element.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, and overcrowding. No cartoon styling, no 3D rendering, no glossy gradients. No invented anatomy. No implication that retinal AI replaces biopsy. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope — never a serif font. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Eye + kidney organ panel on left, dashed two-panel inset (retina vs glomerulus) in the center, three-box injury → intervention → benefit flow at the bottom. Restrained clinical palette. Labels readable at slide-viewing size. Attribution bottom-right.
```

---

## 6 · §M7 LLMs — Retrieval-Augmented Generation (RAG) architecture
*Skill: williamriveromd-simple-figure · Scaffold C — Horizontal step sequence*

> Five-card horizontal flow that explains why a RAG-grounded LLM is safer than a
> raw chatbot for clinical content.

```
FILE NAME: ai-in-nephrology-practice-04-rag-architecture.png
IMAGE TYPE: Horizontal step sequence (Scaffold C)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Clinicians
VISUAL GOAL: Show that a RAG-grounded LLM retrieves cited passages from a curated corpus before generating — the architecture that cuts hallucination for clinical use.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top center in bold navy (#0f1e2e) set in Inter: "Retrieval-Augmented Generation — the Safer LLM Architecture for Clinical Use". Subtitle in clinical teal (#1a6b72): "Retrieve → ground → generate → verify. The model paraphrases an audited source, not its training-time priors."

Five rounded rectangular cards arranged horizontally in a single row, connected by bold navy right-pointing arrows. Each card has a colored top accent band, a small flat icon, a bold step label in navy, and 2–3 short bullet details.

1. (teal accent · book icon) **CORPUS** — "KDIGO guidelines · ASN core curriculum · Institution order sets · This site's calculator scripts."
2. (teal accent · magnifier icon) **RETRIEVER** — "Embeds the question; pulls the top-k most relevant passages from the corpus."
3. (navy accent · brain icon) **LLM** — "Paraphrases the retrieved passages — does not generate citations from training-time priors."
4. (amber accent · stethoscope icon) **CITED ANSWER** — "Returns the answer plus a clickable source — auditable."
5. (renal-green accent · check icon) **PHYSICIAN VERIFIER** — "Clinician reads the source, signs the note. The model never owns the decision."

Cards sit on a very soft gray panel (#f3f4f6). Generous whitespace. Mobile-readable labels ≥12pt equivalent. Bottom strip: full-width soft gray, brief summary sentence in navy: "Hallucination drops because the model paraphrases an audited source, not its training-time priors." Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No glowing neon "AI" iconography, no holograms, no robot heads. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Five horizontal cards with arrows; corpus → retriever → LLM → cited answer → physician verifier. Bottom summary strip with the one-line takeaway. Light background. Attribution bottom-right.
```

---

## 7 · §M8 Governance — eGFR race-coefficient reclassification
*Skill: williamriveromd-simple-figure · Scaffold B — Side-by-side comparison*

> Two equal panels: old CKD-EPI-with-coefficient vs new race-free / cystatin C —
> showing how the same creatinine maps to a different CKD category and a
> different downstream decision.

```
FILE NAME: ai-in-nephrology-practice-05-egfr-reclassification.png
IMAGE TYPE: Side-by-side comparison (Scaffold B)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Mixed (clinicians and informed patients)
VISUAL GOAL: Make algorithmic bias concrete — show that removing the eGFR race coefficient reclassifies a meaningful share of patients, which then shifts referral, listing, and dosing decisions.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical abstract style. White (#ffffff) background. Title centered at top in bold navy (#0f1e2e) set in Inter: "Removing the eGFR Race Coefficient — What Actually Changes". Subtitle in clinical teal (#1a6b72): "Same creatinine. Different equation. Different category. Different decision."

Soft dashed vertical divider splitting the canvas into two equal panels.

LEFT panel labeled in soft gray with amber tag "PRIOR EQUATION (race-coefficient)": At the top, a small clean equation panel: "CKD-EPI 2009 — creatinine, with a higher multiplier applied if reported as Black." Below it, an example: a stylized patient silhouette labeled "Patient A · creatinine 1.6 mg/dL". Calculated eGFR badge: "≈ 56 mL/min/1.73m²". CKD-category strip below with rounded segments G1–G5; G3a highlighted in soft amber. Bottom of panel: a small "downstream" sub-card listing — "Referral threshold not yet met · KFRE risk reported as moderate · ACEi dose maintained · Transplant referral not triggered."

RIGHT panel labeled in soft gray with renal-green tag "RACE-FREE / CYSTATIN-C-BASED EQUATION": Same equation header for the new model: "CKD-EPI 2021 (race-free) or cystatin-C-based eGFR." Same patient silhouette and creatinine. Calculated eGFR badge: "≈ 48 mL/min/1.73m²". CKD-category strip with G3b highlighted in clinical red. Bottom of panel: same "downstream" sub-card with the shifted decisions — "Referral threshold met · Higher KFRE risk band · ACEi / SGLT2i intensification reviewed · Transplant referral conversation initiated."

Below both panels, a single full-width pale-purple summary band (using #faf5ff with #6b21a8 text) reading: "Removing the race coefficient is not cosmetic — it changes who is diagnosed, referred, dosed, and listed. The same logic applies to any AI model deployed in nephrology: inspect the embedded variables and the training population."

Rounded panel corners, ample negative space, mobile-readable labels ≥11pt. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid stigmatizing visual cues, avoid implying any race-based phenotype on the patient silhouettes (use a neutral, identical silhouette in both panels). NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Two equal panels with identical patient, identical creatinine, different equation, different eGFR, different CKD category, different downstream decisions. Pale-purple summary band beneath. Patient silhouettes neutral and identical between panels. Light background. Attribution bottom-right.
```

---

## 8 · §M8 Governance — model lifecycle loop
*Skill: williamriveromd-simple-figure · Scaffold D — Single mechanism / circular*

> Square circular loop diagram of the five governance phases. The guide treats
> these as the bare minimum for "ready to deploy": model → calibration in your
> population → monitoring → override path → accountability.

```
FILE NAME: ai-in-nephrology-practice-06-governance-loop.png
IMAGE TYPE: Single mechanism / circular workflow (Scaffold D, square)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: Clinicians
VISUAL GOAL: A printable square loop diagram a service lead can show at a governance committee: the five phases an AI tool has to live inside to be deployable in nephrology.

PROMPT:
Medical pathophysiology / systems infographic, AJKD/NEJM graphical abstract style — circular workflow variant. White (#ffffff) background. Title at top in bold navy (#0f1e2e) set in Inter: "The AI Governance Loop — What a Deployable Nephrology AI Has to Sit Inside". Subtitle in clinical teal (#1a6b72): "Model → calibration in your patients → monitoring → override → accountability. Then back to model."

Central circular workflow with five rounded-rectangle nodes arranged evenly around a small hub. Hub label in soft gray: "Named clinical owner". Connect the five nodes with thin navy clockwise arrows forming a continuous loop, plus a thin dashed feedback arrow from node 5 back to node 1.

Node 1 (top, teal accent · code icon) **MODEL** — "Intended use. Training population. Outcome definition. SaMD status if applicable."
Node 2 (upper-right, teal accent · chart icon) **CALIBRATION** — "Plot in your own patients before go-live. Not just the vendor's reference site."
Node 3 (lower-right, amber accent · gauge icon) **MONITORING** — "Discrimination, calibration, alert burden, subgroup performance — on a written cadence."
Node 4 (lower-left, renal-green accent · hand icon) **OVERRIDE** — "A documented path for the clinician to dissent. Audited."
Node 5 (upper-left, soft-purple accent · person icon) **ACCOUNTABILITY** — "Named clinical owner. Pre-declared kill-switch criterion. Pause authority."

Around the loop, a soft-gray outer ring with a single sentence in navy, broken into quadrants: "Adopt only tools that have all five." Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid HDR over-processing. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. No glowing neon, no holograms. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Square 1:1. Five labelled nodes in a clockwise loop with a named-clinical-owner hub. Color logic: teal (model/calibration), amber (monitoring), green (override), purple (accountability). Labels readable at slide-viewing size. Attribution bottom-right.
```

---

## 9 · §10 The 7-point appraisal checklist clinician card
*Skill: williamriveromd-simple-figure · Scaffold E — Reference / quick-look card*

> Printable clinician card mirroring the HTML checklist table in §10. Designed
> to be screenshotted, pinned, or printed on the back of a vendor demo handout.

```
FILE NAME: ai-in-nephrology-practice-07-appraisal-checklist-card.png
IMAGE TYPE: Clinician reference card (Scaffold E)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: Clinicians
VISUAL GOAL: A printable 7-question card the reader can apply to any AI claim — peer-reviewed paper, vendor demo, or institution pilot proposal.

PROMPT:
Clinical reference card, publication-grade nephrology design. White (#ffffff) background. Bold navy (#0f1e2e) title at top in Inter: "The 7-Point AI Appraisal Checklist". Subtitle in clinical teal (#1a6b72): "Run all seven, in order. A 'no' on any one is a question that must be answered before deployment, not after."

Below the title, a compact 7-row table on a soft gray background panel (#f3f4f6) with rounded corners. Column headers in teal on soft gray: "#", "Question", "Why it matters". Alternating row fills (white / very soft gray). Inter throughout. Rows:

1. **What exactly does it predict?** — Outcome definition and label quality drive everything downstream.
2. **In whom was it trained?** — Population mismatch (age, sex, race/ethnicity, comorbidity, region, care setting) breaks transportability.
3. **Externally validated?** — Internal-only performance overstates real-world accuracy. Require a population that did not contribute to training.
4. **Is it calibrated?** — Good discrimination with poor calibration misleads at the decision threshold.
5. **Does it arrive in time to act?** — Lead time and alert specificity decide whether the prediction can change care.
6. **Is it fair?** — Inspect subgroup performance and embedded variables (e.g., race coefficients).
7. **Who is accountable?** — Named owner. Override path. Monitoring cadence. Regulatory status.

Below the table, a single-row tier-badge strip with four small rounded badges:
- (renal-green) "Tier 1 — externally validated, calibrated, prospective"
- (teal) "Tier 2 — externally validated, retrospective"
- (amber) "Tier 3 — single-center, internal validation only"
- (soft purple) "Tier 4 — preprint / vendor claim, no peer review"

Footer line in navy: "Map every model to a tier. The tier should track how aggressively the model is allowed to touch a workflow." Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
4:3 reference card. Seven-row checklist table with clear question and rationale columns. Four-tier maturity strip below. Readable on mobile and on a printed handout. Light background. Attribution bottom-right.
```

---

## 10 · §11 Kidney–CV–Metabolic crosstalk sigil
*Skill: williamriveromd-organ-crosstalk-sigil-graphic · Triangular variant*

> The recurring cross-cutting thread is that every AI use case routes back to
> kidney–heart–metabolism integration. A monoline triangular sigil makes that
> thread legible as an icon.

```
FILE NAME: ai-in-nephrology-practice-08-kidney-cv-metabolic-sigil.png
IMAGE TYPE: Organ-crosstalk sigil — triangular variant
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: Mixed (clinicians and informed patients)
VISUAL GOAL: A symbolic crosstalk sigil that says "any AI use case in nephrology touches the kidney–CV–metabolic triangle" — usable as the §11 sidebar mark and as a small recurring motif.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring:

ORGANS:
- A pair of stylized kidneys (lower right)
- A stylized heart (lower left)
- A stylized pancreas / "metabolism" glyph — a small islet-of-Langerhans cell cluster or a calm pancreas silhouette (top center)

RELATIONSHIP:
Show the kidney–cardiovascular–metabolic axis using dotted curved arrows forming a continuous triangular loop between the three icons. The arrows should read as bidirectional (each pair connected by a soft dotted curve that gently reverses direction in the middle), conveying continuous crosstalk rather than one-way causation.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette with restrained accent renal-red for the kidneys and muted warm beige for the pancreas, white background, clean rounded organ shapes, balanced sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels.

COMPOSITION:
Place the pancreas/metabolism glyph at the top center, the heart at the lower left, and the kidneys at the lower right, forming an equilateral triangle. Connect them with dotted curved arrows forming a gentle triangular loop. Keep the design simple, symbolic, and suitable for a clinician-perspective nephrology guide on AI.

OUTPUT:
Square 1024 × 1024, clean margins, high-resolution, publication-grade medical icon aesthetic. Include a small, semi-transparent "williamriveromd.com" attribution in the bottom-right corner, ~10–11px, ~70% opacity, not obscuring the sigil.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, excessive labels, dark background, neon colors, complex infographics, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic lighting, stock-photo style. No text labels on the organs themselves. If any text is added, use only Inter, Nunito Sans, IBM Plex Sans, or Manrope — never a serif or decorative font. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Square 1:1. Three organs in equilateral triangle (pancreas top, heart lower-left, kidneys lower-right) with dotted bidirectional crosstalk arrows. Calm soft teal-blue palette, label-free, attribution bottom-right.
```

---

## 11 · Patient-mode — "AI helps draft. Your doctor decides."
*Skill: williamriveromd-simple-figure · Scaffold C — Horizontal step sequence (patient tone)*

> Patient-facing reassurance figure: shows the verification loop in plain
> language so a patient sees that an AI draft is always physician-reviewed.

```
FILE NAME: ai-in-nephrology-practice-09-patient-llm-safety.png
IMAGE TYPE: Horizontal step sequence (Scaffold C, patient tone)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients (and curious caregivers)
VISUAL GOAL: Reassure patients that when an AI tool is used in their care, a clinician always reviews and signs the result — the model never decides on its own.

PROMPT:
Clean clinical education infographic, white (#ffffff) background. Title at top center in bold navy (#0f1e2e) set in Inter: "AI Helps Draft. Your Doctor Decides." Subtitle in clinical teal (#1a6b72), medium weight, friendly tone: "Here's the loop your care always sits inside."

Four rounded rectangular cards arranged horizontally in a single row, connected by bold navy right-pointing arrows. Each card has a colored top accent band, a small friendly flat icon, a bold step label in navy, and one short patient-friendly sentence.

1. (teal accent · question icon) **YOUR QUESTION** — "A clinical question or a routine task — for example, a discharge summary, a lab explanation, or a risk estimate."
2. (teal accent · brain icon) **AI DRAFTS** — "An AI tool drafts a first pass, grounded in trusted clinical sources where possible."
3. (amber accent · stethoscope icon) **YOUR DOCTOR REVIEWS** — "Your physician reads the draft, checks the sources, and corrects anything wrong."
4. (renal-green accent · check icon) **YOU GET A SIGNED ANSWER** — "Only after your doctor signs does the answer reach your chart or your hand."

Cards sit on a very soft gray panel (#f3f4f6). Generous whitespace. Mobile-readable labels ≥12pt equivalent. Bottom strip: full-width soft gray, brief reassuring sentence in navy: "An AI tool never owns the decision. Your clinician does." Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid sci-fi neon, avoid robot-doctor imagery, avoid scary or alarming visual cues. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Four horizontal cards with arrows; question → AI drafts → doctor reviews → signed answer. Bottom reassurance strip. Warm, calm patient tone (no neon AI imagery). Light background. Attribution bottom-right.
```

---

## 12 · Patient-mode — "What AI is doing in your kidney care"
*Skill: williamriveromd-simple-figure · Scaffold D — Single mechanism / one-panel poster (patient tone)*

> Patient-facing overview: where AI actually shows up across the kidney journey,
> in plain language, with the boundary line ("everywhere here, your doctor still
> decides") made visible.

```
FILE NAME: ai-in-nephrology-practice-10-patient-overview.png
IMAGE TYPE: Single mechanism / one-panel poster (Scaffold D, patient tone)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients (and curious caregivers)
VISUAL GOAL: Show patients in one frame the five places AI typically shows up across kidney care — and the line that says "the clinician still decides".

PROMPT:
Patient education infographic poster, AJKD/NEJM graphical abstract style. White (#ffffff) background. Title at top center in bold navy (#0f1e2e) set in Inter: "Where AI Shows Up in Your Kidney Care". Subtitle in clinical teal (#1a6b72): "Five quiet places — and the line your clinician still owns."

Central layout: a horizontal soft-gray "patient journey" band running left-to-right across the middle of the canvas, labeled at the left "Diagnosis →" and at the right "Long-term care →". Above the band, five small rounded cards spaced evenly along the journey, each with a friendly flat icon, a bold short label in navy, and one short plain-language sentence.

1. (teal · risk gauge icon) **Risk estimate** — "A score that helps your doctor decide how often to see you and which treatments to start."
2. (amber · alarm-clock icon) **Early-warning alert** — "A heads-up in the hospital that your kidney function could drop — so the team can act before it does."
3. (renal-green · microscope icon) **Biopsy assistant** — "Software that helps the pathologist measure your kidney biopsy more reliably."
4. (teal · dialysis icon) **Dialysis decision support** — "A model that helps the dialysis team set safer fluid and dose targets."
5. (soft purple · document icon) **Clinic notes & education** — "An AI helper that drafts paperwork and patient handouts — your doctor checks and signs."

Below the journey band, a full-width pale-renal-green safety line with a single sentence in navy: "In every box, the AI is helping. Your nephrologist still decides." A small soft-gray sub-line below in navy/teal: "No AI tool sees your information without consent and physician oversight."

Generous whitespace, calm patient tone (no neon AI imagery, no robot-doctor icons). Mobile-readable labels ≥12pt equivalent. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid sci-fi neon, avoid robot-doctor imagery, avoid scary or alarming visual cues. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
16:9 patient-mode poster. Five small cards along a horizontal patient-journey band, with a pale-green safety line below. Plain-language tone. Light background. Attribution bottom-right.
```

---

## Post-generation wiring

After the assets are generated and saved into `images/`:

1. **Rename / keep the canonical slugs** so the HTML doesn't have to change.
   Each prompt's `FILE NAME` is the final slug.
2. **WebP twins.** Convert every PNG into a `.webp` of the same base name so
   the `<picture>` tags work.
3. **Hero `<img width/height>`.** Already `1254 × 1254` square in the HTML —
   compatible with the 1024 × 1024 hero. If you want the markup to match
   exactly, change to `1024 1024`.
4. **In-body figures.** For figures 3–12, drop a `<figure>` block into the
   matching section of `guides/ai-in-nephrology-practice.html` with a
   `<picture>` (webp + png), a descriptive `alt`, and a `<figcaption
   class="fig-desc">` plain description. The lightbox (`../assets/image-lightbox.js`)
   is already wired.
5. **OG card meta.** The HTML already references
   `https://www.williamriveromd.com/images/ai-in-nephrology-practice-og.png`
   with `og:image:width="1200"` and `og:image:height="630"` — drop the file in
   place and the share preview works.
6. **Patient-mode visuals (#11, #12).** The current guide is single-mode
   clinician, so these two assets are staged for a future dual-mode promotion
   or for use as standalone explainer pieces / Facebook share variants. Leave
   them in `images/` and they're ready when needed.

---

## Skill coverage summary

| Skill | Images authored |
|---|---|
| `williamriveromd-hero-vignette` | 1 (hero) |
| `williamriveromd-infographic-skill` | 1 (OG share card) |
| `williamriveromd-simple-figure` | 7 (taxonomy, RAG, eGFR reclassification, governance loop, appraisal checklist card, patient LLM-safety, patient overview) |
| `williamriveromd-algorithm-generator-skill` | 1 (AKI alert → action bundle) |
| `williamriveromd-biomedical-mechanism-figure` | 1 (oculo-renal axis) |
| `williamriveromd-organ-crosstalk-sigil-graphic` | 1 (kidney–CV–metabolic sigil) |
| **Total** | **12 prompts ready to paste** |
