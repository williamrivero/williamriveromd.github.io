# Image-Prompts Pack — Dialysis Cramps & Stasis Pigmentation

**Guide:** `guides/dialysis-cramps-stasis-pigmentation.html`
**Target generator:** ChatGPT Image Generator GPT — <https://chatgpt.com/g/g-pmuQfob8d-image-generator>
**Skills used:** infographic-skill · hero-vignette · biomedical-mechanism-figure · simple-figure · organ-crosstalk-sigil · algorithm-generator

> Workflow: paste each `COPY-READY IMAGE GENERATOR GPT PROMPT` block into the GPT, save the output to `generated-images/` under the filename in `FILE NAME:`, then hand the folder to Stage 2 (`williamriveromd-local-image-generator`) for manifest + HTML wiring.

---

## 000 — OG / Social Share Card

```
IMAGE NUMBER: 000
SECTION PLACEMENT: <head> og:image / social share card (not inline on page)
FILE NAME: dialysis-cramps-stasis-pigmentation-og-card.png
ARCHETYPE: OG / Social Share Card (infographic-skill)
AUDIENCE: mixed — patients + clinicians; link-preview audience
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — title lockup, subtitle, two small calm calf motifs
- 3D component graphics: light semi-3D calf/dermal motif, restrained
- algorithm/flowchart: none
PURPOSE: A fixed-size social/link-preview card serving as the guide's og:image — instantly readable as a thumbnail on Facebook, X, LinkedIn, and iMessage; communicates the "paired phenotype on one leg" at a glance.
KEY CONCEPTS: paired cramp + pigment phenotype; spectrum framing; dual patient & clinician audience; premium nephrology editorial.

COPY-READY IMAGE GENERATOR GPT PROMPT:
A clean, premium social share card, landscape 1200 × 630, graphical-abstract aesthetic for a nephrology patient-and-clinician guide. White (#ffffff) / soft off-white (#fafafa) background — light only, never dark. Left two-thirds: a bold condensed sans-serif title in deep navy (#0f1e2e) set in Inter (or Manrope), reading on two lines "When Your Legs Cramp and Darken" with the words "Cramp" and "Darken" lightly tinted clinical-teal (#1a6b72); a smaller subtitle beneath in Nunito Sans, navy (#0f1e2e) at ~70% opacity, reading "Oxygen, Fluid, and the Dialysis Patient's Lower Limb — a patient & clinician spectrum guide". A thin teal rule and a small renal-green (#1f7a4d) tag dot beside the subtitle. Right third: a single tasteful, semi-photorealistic calm two-state lower-leg motif on a soft very-light teal tint panel — the top calf with a faint amber (#b8860b) lightning glyph indicating an acute cramp, the bottom calf with a soft brown (sienna-tinted) gaiter pigmentation in the supramalleolar gaiter area; both rendered with restrained clinical realism and ample negative space. No body, no faces, no full feet — just paired calves on a clean light background. Restrained navy / teal / amber / sienna accents, ample whitespace, strong visual hierarchy, mobile-thumbnail-legible. Bottom-right: small semi-transparent navy text "williamriveromd.com" at ~70% opacity. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif, decorative, or handwritten fonts. Never omit the williamriveromd.com attribution. Do not change the canvas size — it must be exactly 1200 × 630.

QUALITY CHECK:
Must be mobile-readable as a small link thumbnail, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com house style. Background must be white or soft light gray — never dark. Title legible at thumbnail scale. Both calf states (cramp + pigment) visible. Copyright attribution williamriveromd.com visible in the bottom-right corner. Canvas exactly 1200 × 630.

ALT TEXT: Cramp and brown gaiter pigmentation on a dialysis patient's calf — paired phenotype on a single leg, the cover card for the williamriveromd.com guide.
OG WIDTH: 1200
OG HEIGHT: 630
```

---

## 001 — Hero Vignette (patient-mode hero)

```
IMAGE NUMBER: 001
SECTION PLACEMENT: <figure class="hero-figure mode-patient"> → <div class="hero-vignette"> (top of guide)
FILE NAME: dialysis-cramps-stasis-pigmentation-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A (Clinical People) with Object-Hero framing on a single lower leg
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero (one large subject + small environmental details)
CAMERA: low-angle three-quarter from the patient's right side, framing the calf from knee to mid-foot with the chair/IV pole softly blurred behind
HUMAN VARIATION (vs. previous guide): older Filipino patient (different from post-dialysis-fatigue's middle-aged subject); ≥12 traits differ — male in mid-60s, weathered hands, short salt-and-pepper hair, plain grey-blue cotton trousers rolled to the knee, no glasses, simple wedding band, light-brown skin tone with subtle gaiter pigmentation above the ankle, calm focused expression, seated on a dialysis recliner with one foot slightly elevated on the chair's leg rest, a small folded face towel across the thigh, hands resting on the armrest, bright daylight from a wide clinic window on the left, soft pastel-mint hero accent in the background instead of the previous teal portrait.
AUDIENCE: patients / mixed
VISUAL GOAL: Convey the paired phenotype on one struggling leg — a calm, dignified Filipino HD patient mid-treatment with one calf in the foreground showing the early gaiter tint, the hand intuitively dorsiflexing the ankle to abort a cramp.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048 × 2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: I — Object Hero. Camera: low-angle three-quarter from the patient's right side, framing the calf from knee to mid-foot with the dialysis chair, IV pole, and bloodlines softly blurred in the background.

Subject: a Filipino man in his mid-60s seated in a dialysis recliner mid-session, with his right trouser leg rolled up to the knee, gently dorsiflexing his right ankle with one hand as a self-stretch — a soft, restrained calf cramp rescue. The calf is the hero of the frame: light-brown Filipino skin with a faint, anatomically subtle brown gaiter pigmentation in the supramalleolar gaiter region (early CEAP C4a), no open wounds. His other hand rests calmly on the recliner armrest. Wears plain grey-blue cotton trousers, a soft pastel-mint hospital blanket draped over the thigh, simple wedding band; no jewellery beyond that. Calm focused expression rather than pain; daylight from a wide clinic window on the left fills the scene; the room is a clean modern Philippine outpatient HD unit — soft mint and warm neutral walls, a glimpse of a teal recliner, blurred IV pole and bloodlines, no readable signage.

Visual hierarchy: the calf and the dorsiflexing hand occupy ~60–70% of the circle; the patient's relaxed upper body and the soft clinic backdrop fill the supporting 20–30%; a clean 20–25% TITLE SAFE ZONE of soft blurred mint-tinted clinic wall sits on the upper-left of the circle (no faces, anatomy, equipment, icons, or callouts inside that zone) so the HTML <h1> can sit beside the disc without covering important artwork.

Calm, reassuring, documentary-realistic colour grade harmonizing with the pastel mint patient-mode hero — clinical teal (#1a6b72) and navy (#0f1e2e) accents on a light background. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, journal name, guideline acronym, brand name, or williamriveromd.com watermark — the picture carries the mood; the words live in the HTML beside it.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text/titles/captions/logos/watermarks, rectangular borders/frames/banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope if any incidental text is unavoidable (it should not be) — never a serif, decorative, or handwritten face. No journal names, guideline acronyms, brand names, or watermarks.

QUALITY CHECK:
Square 2048 × 2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant hero subject (the calf and the dorsiflexing hand) at 60–70% of the circle; 2–4 supporting context elements; 20–25% empty title-safe zone reserved (soft mint wall / blurred clinic). Filipino clinical context with ≥12 traits visibly different from prior guides. Camera framing not repeated from the previous guide. Crops cleanly inside the circle with no text or subject lost at the edges. Anatomically correct calf and ankle, plausible early stasis pigmentation, calm dignified atmosphere.

ALT TEXT: An older Filipino hemodialysis patient gently dorsiflexes his ankle to abort a calf cramp at the dialysis chair, with subtle early brown gaiter pigmentation visible above the ankle — circular vignette hero for the williamriveromd.com guide.
OG WIDTH: 2048
OG HEIGHT: 2048
```

---

## 002 — SERCA / ATP Relaxation Pump (mechanism)

```
IMAGE NUMBER: 002
SECTION PLACEMENT: §pt-oxygen ("the oxygen budget"); also referenced from §md-pathophys
FILE NAME: dialysis-cramps-serca-relaxation-pump.png
ARCHETYPE: Biomedical Mechanism Figure (biomedical-mechanism-figure skill) — cell-level review-article schematic
AUDIENCE: mixed — patients + clinicians (mechanism literacy)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — multi-scale dashed-inset layout
- 3D component graphics: light semi-3D shading on the SERCA pump and SR membrane
- algorithm/flowchart: bottom injury → intervention → benefit summary
PURPOSE: Anchor the guide's central physiologic claim — muscle relaxation is the ATP-dependent step, and SERCA is the pump that fails when oxygen and cofactors run short.
KEY CONCEPTS: SERCA Ca²⁺ reuptake; 2 Ca²⁺ per ATP; sarcoplasmic reticulum; bioenergetic margin; relaxation failure = cramp.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade biomedical mechanism schematic in the style of an AJKD/NEJM review-article figure (without naming any journal). Canvas: landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif labels set in Inter (or Manrope or IBM Plex Sans); never a serif font.

LEFT PANEL — organ context: a simplified semi-photorealistic flat-vector calf muscle in cross-section, soft light-gray-blue anatomy, with a small dashed connector box pointing into the magnified central panel. A small label in deep navy (#0f1e2e) reads "Skeletal muscle, calf — intradialytic energy stress".

CENTER PANEL — magnified myocyte and sarcomere inside a thin dashed border. Show the sarcolemma, a single sarcomere with actin (light gray-blue) and myosin (muted teal), and the sarcoplasmic reticulum (SR) wrapping the sarcomere in soft pale yellow. Highlight a single SERCA pump on the SR membrane rendered with light semi-3D shading. Two stylized Ca²⁺ ions (small renal-green #1f7a4d circles labeled "Ca²⁺") move from cytosol into the SR through the pump; an arrow labeled "1 ATP → 2 Ca²⁺ in" runs alongside. Show a small ATP molecule docking and an ADP + Pi leaving. Concise mechanism callouts:
  • "↓ ATP" (red, #b91c1c) when O₂ + cofactors fall
  • "↑ cytosolic Ca²⁺" (red)
  • "Sustained actin–myosin engagement"
  • "= cramp (failure to relax)"

RIGHT INSET — a small dashed-bordered mini-panel showing the mitochondrion that feeds ATP: muted clinical colours, label "Mitochondrial ATP supply" with arrows from O₂ (sky-blue tag) and cofactors (small icons labeled "L-carnitine", "B-vitamins", "Mg²⁺", "CoQ10") feeding the ETC. A red dashed arrow downward labeled "↓ during UF stress".

BOTTOM SUMMARY FLOW (single horizontal row of three rounded boxes connected by teal arrows):
  LEFT (pale pink): "Pathology — ↓ ATP → SERCA fails → Ca²⁺ retained → sustained contracture"
  CENTER (pale blue): "Intervention — lower UFR, restore O₂ delivery, replete L-carnitine / B / Mg / CoQ10"
  RIGHT (pale green): "Benefit — Ca²⁺ reuptake restored, muscle relaxes, cramp aborts"

Restrained clinical palette throughout: light gray-blue anatomy, soft yellow SR, renal green Ca²⁺, red for injury/oxidative stress, blue for protective/therapeutic flow. Generous whitespace, mobile-readable labels (≥ 11pt equivalent). No photorealism, no dark backgrounds, no shadows beyond soft semi-3D. Bottom-right: "© williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid photorealism, avoid heavy shadows, avoid dark backgrounds, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif, decorative, or handwritten fonts. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically and biochemically plausible (correct SERCA stoichiometry, anatomically reasonable sarcomere, mitochondrion drawn at a plausible scale), visually calm, publication-grade, and consistent with williamriveromd.com house style. Background white. Bottom-right attribution visible.

ALT TEXT: A multi-scale review-article schematic of the SERCA Ca²⁺ ATPase pump on the sarcoplasmic reticulum, showing how falling ATP supply during dialysis ultrafiltration causes failure of muscle relaxation and a sustained cramp.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## 003 — The Five-Hit Cramp Mechanism

```
IMAGE NUMBER: 003
SECTION PLACEMENT: §pt-cramps (patient last-hour cramps) + §md-pathophys (clinician)
FILE NAME: dialysis-cramps-5hit-mechanism.png
ARCHETYPE: Biomedical Mechanism Figure (biomedical-mechanism-figure skill) — organ → inset → bottom flow
AUDIENCE: mixed — patients + clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — multi-panel review-article layout
- 3D component graphics: light semi-3D shading on the dialysis machine icon and calf
- algorithm/flowchart: bottom injury → intervention → benefit summary
PURPOSE: Show that five different upstream insults converge on a single end-point (SERCA-ATP failure → cramp) during the last hour of dialysis.
KEY CONCEPTS: hypoperfusion ischemia, contraction alkalosis, electrolyte/osmolar shift, cofactor-limited ATP, mechanical stretch + Golgi tendon organ unloading.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade biomedical mechanism schematic in the style of an AJKD/NEJM review-article figure (without naming any journal). Canvas: landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif labels set in Inter (or Manrope or IBM Plex Sans); never a serif font.

LEFT PANEL — organ-level context: a simplified semi-photorealistic flat-vector lower-limb silhouette from knee to mid-foot, soft light-gray-blue anatomy, with a clearly highlighted pale-yellow calf muscle. Above it, a small light-teal dialysis-machine icon with an arrow labeled "Ultrafiltration → plasma volume contraction" pointing into the limb. A small dashed connector box on the calf points into the central magnified panel.

CENTER PANEL — magnified myocyte cross-section in a thin dashed border. Show the sarcomere with sarcoplasmic reticulum (pale yellow), a single SERCA pump rendered semi-3D, and five inbound arrows converging on it, each labeled with one "hit":
  1. (red #b91c1c) "Hypoperfusion ischemia — ↓ O₂ delivery"
  2. (amber #b8860b) "Contraction alkalosis — ↑ HCO₃⁻, ↓ ionized Ca²⁺"
  3. (teal #1a6b72) "Osmolar / electrolyte shift — ↓ K⁺ Mg²⁺ Na⁺ osmolality"
  4. (purple #6b21a8) "Cofactor-limited ATP — ↓ L-carnitine, B-vitamins, CoQ10, Mg²⁺"
  5. (navy #0f1e2e) "Mechanical stretch + ↑ spindle / ↓ GTO afferents"

A small inset to the right of the SERCA pump shows the convergent result: "ATP insufficient → SERCA fails → Ca²⁺ retained → sustained contracture (cramp)" with a small red lightning glyph.

BOTTOM SUMMARY FLOW — single horizontal row of three rounded boxes connected by teal arrows:
  LEFT (pale pink, #fbe7e7): "Pathology drivers: high UFR, alkalotic dialysate, carnitine loss, shortened-fatigued calf in the chair"
  CENTER (pale blue, #e3edf9): "Intervention: lower UFR, individualize Na/HCO₃⁻ profile, cofactor replacement (L-carnitine + B + Mg + CoQ10), passive stretch + ankle pumps every 30 min"
  RIGHT (pale green, #e9f5ec): "Benefit: SERCA reactivates, cramp aborts, last-hour HD tolerated"

Use a small "73% of cramps in the final hour" annotation as a clinical anchor in the bottom strip.

Restrained clinical palette: light gray-blue anatomy, soft yellow SR, red for ischemia/injury, amber for alkalosis, teal for osmolar / dialysate, purple for cofactor depletion, navy for mechanical. Generous whitespace; mobile-readable labels. No photorealism; no dark backgrounds; soft semi-3D only. Bottom-right: "© williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, heavy shadows, dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable. Five hits visible and individually legible. Convergent geometry clear (all five arrows point at the SERCA pump / ATP node, not at five different targets). Anatomy plausible. Bottom three-box flow connected by visible teal arrows. Bottom-right attribution visible.

ALT TEXT: A review-article schematic showing five upstream insults — hypoperfusion ischemia, contraction alkalosis, osmolar and electrolyte shifts, cofactor-limited ATP, and mechanical stretch — converging on SERCA failure in a calf myocyte during the last hour of hemodialysis.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## 004 — Hemosiderin / Stasis Pigmentation Pathway

```
IMAGE NUMBER: 004
SECTION PLACEMENT: §pt-darken (patient) + §md-pigment (clinician)
FILE NAME: dialysis-cramps-hemosiderin-pathway.png
ARCHETYPE: Biomedical Mechanism Figure (biomedical-mechanism-figure skill) — organ → dermal-capillary inset → bottom flow
AUDIENCE: mixed — patients + clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — multi-scale schematic
- 3D component graphics: light semi-3D shading on dermal layers and capillary
- algorithm/flowchart: bottom injury → intervention → benefit summary
PURPOSE: Visualize how chronic venous hypertension drives RBC extravasation, hemosiderin deposition, MMP activation, and the spiral toward stasis dermatitis and ulceration.
KEY CONCEPTS: ambulatory venous hypertension, interendothelial gaps, RBC extravasation, hemoglobin → ferritin → hemosiderin, MMP-driven inflammation, lipodermatosclerosis, ulcer risk.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade biomedical mechanism schematic in the style of an AJKD/NEJM review-article figure (without naming any journal). Canvas: landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif labels set in Inter (or Manrope or IBM Plex Sans); never a serif font.

LEFT PANEL — organ-level context: a simplified semi-photorealistic flat-vector lower leg from knee to ankle in three-quarter view, soft light-gray-blue anatomy, with a subtle pale-sienna brown "gaiter" pigmentation band rendered around the supramalleolar region (anatomically plausible CEAP C4a). A small dashed connector box on the gaiter points into the magnified central panel; an upstream label reads "Chronic venous hypertension".

CENTER PANEL — magnified cross-section of the dermis inside a thin dashed border, three labeled vertical strata (epidermis at top, papillary + reticular dermis, hypodermis). Inside the papillary dermis, a single dilated post-capillary venule rendered semi-3D, with widened interendothelial junctions and several red blood cells visibly extravasating into the perivascular dermis. Show the iron cascade with concise labeled arrows:
  • Lysed RBC → "Hemoglobin"
  • Hemoglobin → "Ferritin"
  • Ferritin → "Hemosiderin" (soft sienna pigment granules in the dermis)
A separate red arrow shows extravasated iron activating "MMPs" with a small icon labeled "Matrix metalloproteinases" eating away at the surrounding extracellular matrix collagen fibers (the fibers drawn as muted gray-blue strands becoming frayed).
A subtle teal "fibrin cuff" wraps the capillary; a small annotation reads "Pericapillary fibrin cuff + leukocyte trapping → ↑ O₂ diffusion distance → chronic tissue hypoxia".

RIGHT INSET — small dashed mini-panel showing the downstream skin consequences as a vertical "consequence ladder":
  • "Hemosiderin pigmentation (brown gaiter)"
  • "Lipodermatosclerosis (skin hardening)"
  • "Stasis dermatitis"
  • "Venous stasis ulcer" (red)

BOTTOM SUMMARY FLOW — single horizontal row of three rounded boxes connected by teal arrows:
  LEFT (pale pink): "Pathology drivers: interdialytic volume overload, dependent leg, CKD microangiopathy, anemia"
  CENTER (pale blue): "Intervention: leg elevation, calf-pump activation, dry-weight discipline, ABI → TBI before compression, skin care"
  RIGHT (pale green): "Benefit: ↓ venous pressure, slowed pigment progression, reduced ulcer risk"

Restrained clinical palette: light gray-blue anatomy, sienna for pigment, red for injury/MMPs, teal for fibrin and protective flow, ample whitespace, mobile-readable labels. No photorealism; no dark backgrounds; soft semi-3D only. Bottom-right: "© williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, heavy shadows, dark backgrounds, overprocessed HDR, excessive saturation, gore. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable. Iron cascade (RBC → Hb → ferritin → hemosiderin) sequenced left-to-right and individually legible. Dermal strata anatomically plausible. Gaiter pigmentation rendered tastefully (no graphic wound). Bottom three-box flow connected by visible teal arrows. Bottom-right attribution visible.

ALT TEXT: A review-article schematic showing chronic venous hypertension widening dermal capillary junctions, with red blood cell extravasation, hemosiderin deposition, MMP-driven matrix damage, and the downstream ladder from gaiter pigmentation to lipodermatosclerosis and stasis ulcer.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## 005 — Two Axes, One Field (acute vs chronic comparison)

```
IMAGE NUMBER: 005
SECTION PLACEMENT: §pt-connection + §md-theory header
FILE NAME: dialysis-cramps-two-axes-one-field.png
ARCHETYPE: Side-by-side comparison (simple-figure skill, Scaffold B)
AUDIENCE: mixed — patients + clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — two-panel comparison + shared upstream cloud
- 3D component graphics: light semi-3D on the leg silhouette and the upstream "field" cloud
- algorithm/flowchart: none beyond the panel split
PURPOSE: Make the central teaching idea visible — two visible markers, one upstream hypoxic field.
KEY CONCEPTS: acute axis (cramp, minutes–hours) vs chronic axis (pigment, months–years); shared substrate.

COPY-READY IMAGE GENERATOR GPT PROMPT:
A clean medical education comparison infographic, AJKD/NEJM graphical-abstract style (without naming any journal). Landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif labels in Inter (or Manrope, IBM Plex Sans); never a serif font.

TITLE STRIP — top centered: bold navy "Two signals from one leg" with a smaller clinical-teal subtitle "Hypoxic Lower-Limb Spectrum — one upstream field, two outputs".

A single semi-3D simplified lower-leg silhouette in the upper-center, soft light gray-blue anatomy, with a soft pastel-teal "field" cloud above it labeled in small navy text: "Chronic volume overload · venous hypertension · CKD microangiopathy · anemia · autonomic dysfunction · cofactor depletion · mechanical stretch". From this single cloud, two arrows descend symmetrically into a soft dashed vertical divider that splits the lower canvas into two equal panels.

LEFT PANEL — header label in red (#b91c1c) "Acute axis · minutes–hours". A small red lightning glyph over the calf of a small semi-3D lower-leg illustration. Three concise bullet points in navy text (Manrope, ~14pt equivalent):
  • Ultrafiltration → plasma volume contraction
  • Hypoperfusion + alkalosis + cofactor-limited ATP
  • SERCA fails → muscle locks → cramp

RIGHT PANEL — header label in purple (#6b21a8) "Chronic axis · months–years". A small soft-sienna gaiter pigmentation band on a separate lower-leg illustration. Three concise bullet points:
  • Interdialytic volume overload + dependent leg
  • Venous hypertension → RBC extravasation
  • Hemosiderin → MMPs → lipodermatosclerosis → ulcer

A subtle baseline strip at the bottom in navy text: "Same upstream field — different time scale, same lever (volume, oxygen, stretching)."

Rounded panel corners, ample negative space, mobile-readable labels ≥ 11pt equivalent. Bottom-right: "williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable. Single shared cloud → split-arrow geometry is unmistakable. Acute vs chronic colour coding (red vs purple) consistent with the rest of the guide. Both panels balanced; baseline reinforces the unifying message. Bottom-right attribution visible.

ALT TEXT: A two-panel comparison showing the acute axis (intradialytic cramp) and chronic axis (brown gaiter pigmentation) descending from a single shared upstream field of lower-limb hypoxia — the "two axes, one field" teaching figure.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## 006 — Hypoxic Lower-Limb Sigil (organ-crosstalk style)

```
IMAGE NUMBER: 006
SECTION PLACEMENT: §md-theory header (next to the hypothesis box)
FILE NAME: dialysis-cramps-hypoxic-lower-limb-sigil.png
ARCHETYPE: Organ-crosstalk sigil (organ-crosstalk-sigil skill) — minimal monoline + dotted arrows
AUDIENCE: clinicians (header decoration)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: minimal — symbolic monoline only
- 3D component graphics: none
- algorithm/flowchart: dotted-loop crosstalk arrows
PURPOSE: A calm symbolic mark for the hypothesis — one upstream field connecting two outputs (cramp + pigment) on a single leg.
KEY CONCEPTS: monoline simplicity; symbolic crosstalk; restrained clinical palette.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a simple medical organ-crosstalk sigil illustration.

ORGANS:
- a single simplified lower leg (knee-to-ankle silhouette), monoline thin-stroke
- a small ultrafiltration / dialysis machine pictogram (a soft rectangle with a roller-pump curve)
- a small dermal-capillary motif (a thin curved tube with two micro-droplets)

RELATIONSHIP:
Show the Hypoxic Lower-Limb Spectrum as a calm dotted crosstalk loop: dotted curved arrows from the dialysis machine downward into the leg (acute axis — labelled in small monoline text "cramp"), and dotted curved arrows from a dermal-capillary motif beside the gaiter region pointing into the leg (chronic axis — labelled "pigment"); a central dotted ring labelled "lower-limb hypoxia" wraps both arrow groups in a gentle loop.

STYLE:
Minimal clinical line-art, thin monoline strokes (1.5–2 px equivalent), soft teal-blue palette (clinical teal #1a6b72 and navy #0f1e2e), white (#ffffff) background, clean rounded organ shapes, balanced sigil-like radial composition, generous whitespace, no photorealism, no 3D, no shadows. All type — including the labels "cramp", "pigment", and "lower-limb hypoxia" — set in a clean sans-serif: Inter (or Manrope, IBM Plex Sans) only, never a serif or decorative face.

COMPOSITION:
Place the lower-leg silhouette at the centre. Place the dialysis-machine pictogram at the upper-left and the dermal-capillary motif at the lower-right, in soft radial balance. Connect them with dotted curved arrows forming a gentle bidirectional loop, with the central dotted ring labeled "lower-limb hypoxia" running around the leg.

OUTPUT:
Square 1024 × 1024 canvas, clean margins, high-resolution, publication-grade medical icon aesthetic. Include a small, semi-transparent "williamriveromd.com" attribution in the bottom-right corner (≈70% opacity, navy text), not obscuring the sigil. No journal names, guideline acronyms, brand names, or watermarks beyond the attribution.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, excessive labels, dark background, neon colours, complex infographics, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic lighting, stock-photo style. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope for any text. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Reads as a calm symbolic mark at thumbnail scale. Monoline weights consistent. The single shared loop "lower-limb hypoxia" is unmistakable. Three pictograms (leg, dialysis machine, dermal capillary) easily identifiable. Bottom-right attribution visible.

ALT TEXT: A minimal monoline medical sigil of the Hypoxic Lower-Limb Spectrum — a single lower leg connected by dotted crosstalk arrows to a dialysis-machine pictogram (acute cramp axis) and a dermal-capillary motif (chronic pigment axis), with a central loop labeled "lower-limb hypoxia".
OG WIDTH: 1024
OG HEIGHT: 1024
```

---

## 007 — The Hypoxic Lower-Limb Spectrum Staircase (7 stages)

```
IMAGE NUMBER: 007
SECTION PLACEMENT: §pt-spectrum (top) + §md-spectrum (top)
FILE NAME: dialysis-cramps-spectrum-staircase.png
ARCHETYPE: Horizontal step sequence (simple-figure skill, Scaffold C — adapted to 7 stages)
AUDIENCE: mixed — patients + clinicians (master orienting figure)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — numbered rounded cards
- 3D component graphics: light semi-3D on the small lower-leg motif under each card
- algorithm/flowchart: implicit horizontal staircase
PURPOSE: One image that anchors the entire guide — a 7-stage colour-graded continuum that lets either audience locate themselves and see the next checkpoint.
KEY CONCEPTS: continuum, not binary; CEAP/Wagner mapping; diabetic acceleration; intervention checkpoints.

COPY-READY IMAGE GENERATOR GPT PROMPT:
A clean clinical-education infographic, landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif typography in Inter (or Manrope, IBM Plex Sans); never a serif font.

TITLE STRIP — top centered, bold navy: "The Hypoxic Lower-Limb Spectrum" with a smaller clinical-teal (#1a6b72) subtitle "Cramps → pigment → ulcer · one continuum, diabetes accelerates".

A single horizontal staircase of seven rounded rectangular cards, evenly spaced, connected by bold right-pointing arrows. Each card has a coloured top accent band, a stage number, a short title, a one-line marker, and a small monoline lower-leg motif underneath. Cards sit on a very soft gray panel (#f3f4f6) so the staircase reads as a unified ribbon.

Stage cards (left → right), each labeled "Stage 0" through "Stage 6", with these accent colours and content:

  Stage 0 — green (#1f7a4d) "Subclinical" · "No cramps, no skin change"
  Stage 1 — teal (#1a6b72) "Acute axis emerging" · "Last-hour cramps, legs visually normal"
  Stage 2 — amber (#b8860b) "Both axes engaged" · "Recurrent cramps + early hemosiderin tint"
  Stage 3 — amber-deep (#d97706) "Structural change" · "Established gaiter, lipodermatosclerosis"
  Stage 4 — red (#b91c1c) "Skin-barrier failure / pre-ulcer" · "Stasis dermatitis OR diabetic pre-ulcer"
  Stage 5 — purple (#6b21a8) "Open ulcer" · "Venous stasis ulcer or diabetic foot ulcer"
  Stage 6 — purple-deep (#4a1b78) "Critical limb threat" · "Rest pain · gangrene · non-healing"

Below the staircase, a single thin horizontal "DIABETES ACCELERATOR" rail drawn in soft sienna with a small DM glyph and an arrow, running diagonally so that for any given patient-time, a diabetic patient sits one stage further to the right. Below that rail, a small caption in navy: "Diabetes does not change the spectrum — it pushes patients along it faster (Lim et al., 2026)".

Above each card, a small monoline anatomical marker for the visible sign: a calf with a tiny lightning glyph (cramp) appears over Stages 1–2; a gradually deepening soft-sienna gaiter band appears over Stages 2–4; a small red wound dot appears over Stage 5; a small purple mark over Stage 6.

Generous whitespace. Mobile-readable labels (≥ 11pt equivalent). Strong left-to-right visual hierarchy. Bottom-right: "williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable. Seven discrete stage cards in a clear horizontal sequence, each colour-graded. Diabetes accelerator rail clearly subordinate and supportive. Spectrum reads as a single continuum, not seven separate diseases. Bottom-right attribution visible.

ALT TEXT: A horizontal staircase infographic of the seven-stage Hypoxic Lower-Limb Spectrum, from subclinical through critical limb-threatening ischemia, with a soft diabetes-accelerator rail showing how diabetes pushes dialysis patients forward along the continuum faster.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## 008 — 60-Second Cramp Rescue (4-step sequence)

```
IMAGE NUMBER: 008
SECTION PLACEMENT: §pt-rescue (60-second rescue at the chair)
FILE NAME: dialysis-cramps-rescue-steps.png
ARCHETYPE: Horizontal step sequence (simple-figure skill, Scaffold C — 4 steps)
AUDIENCE: patients + dialysis nursing
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — 4 rounded cards connected by arrows
- 3D component graphics: minimal — small monoline leg-in-each-position
- algorithm/flowchart: implicit horizontal sequence
PURPOSE: A bedside-ready visual the patient (or nurse) can glance at to abort a calf cramp.
KEY CONCEPTS: passive stretching reloads the Golgi tendon organ; tell the nurse; do not "tough it out".

COPY-READY IMAGE GENERATOR GPT PROMPT:
A clean clinical-education infographic, landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif typography in Inter (or Manrope, IBM Plex Sans); never a serif font.

TITLE STRIP — top centered, bold navy: "60-Second Cramp Rescue at the Dialysis Chair" with a smaller clinical-teal subtitle "Stretch the muscle the opposite way — reload the tendon brake".

Four rounded rectangular cards arranged horizontally in a single row, connected by bold navy right-pointing arrows. Each card has a coloured top accent band (steps coloured in sequence: teal → teal → green → amber), a step number (1–4) in a small Inter circle, a bold step label, a one-line action sentence, and a small monoline illustration of a seated patient's leg in that position. Cards sit on a very soft gray panel (#f3f4f6).

  Step 1 — teal (#1a6b72) "Straighten the knee"
    Action: "Push the heel of the cramping leg gently away from your hip."
    Illustration: seated patient in dialysis recliner, right leg extending, simple line-art.
  Step 2 — teal (#1a6b72) "Dorsiflex the ankle"
    Action: "Pull your toes up toward your shin (or have a family member do it). Hold steady 20–30 seconds."
    Illustration: same leg with the foot pulled toward the shin, a small arrow on the toes.
  Step 3 — green (#1f7a4d) "Repeat once"
    Action: "Release 5 seconds. Dorsiflex again. Most cramps end after 1–2 cycles."
    Illustration: leg returning to neutral, small loop arrow indicating one repetition.
  Step 4 — amber (#b8860b) "Tell your nurse"
    Action: "Your team can lower UF, reposition you, and — if needed — give a small saline bolus. Do not tough it out."
    Illustration: hand pressing a small call-button beside the recliner.

Bottom strip: full-width soft gray (#f3f4f6) panel, brief summary sentence in navy: "Stretching is mechanism-matched therapy — it reloads the Golgi tendon organ and aborts the discharge." Bottom-right: "williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable. Four discrete step cards clearly numbered and sequenced left-to-right. The "stretch the opposite way" mechanism is unmistakable from the leg illustrations. Step 4's "tell the nurse" call-button visible. Bottom strip summary sentence present. Bottom-right attribution visible.

ALT TEXT: A four-step horizontal sequence showing the at-the-chair calf-cramp rescue — straighten the knee, dorsiflex the ankle for 20 to 30 seconds, repeat once, then tell the nurse.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## 009 — ABI → TBI → TcPO₂ Safety-Gate Algorithm (clinician)

```
IMAGE NUMBER: 009
SECTION PLACEMENT: §md-workup (vascular assessment step) and §md-spectrum (operational take-home)
FILE NAME: dialysis-cramps-abi-tbi-algorithm.png
ARCHETYPE: Clinical algorithm (algorithm-generator skill, Mode C — williamriveromd.com house style)
AUDIENCE: clinicians
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — flat-flowchart with rounded rectangles and diamond decisions
- 3D component graphics: none
- algorithm/flowchart: yes — top-to-bottom clinical logic
PURPOSE: A bedside decision aid for the vascular safety gate before any compression therapy in DM-CKD — the ABI alone is unreliable; TBI is mandatory and TcPO₂ is added from stage 4 onward.
KEY CONCEPTS: ABI under-reads PAD in DM-CKD due to medial arterial calcification; TBI is the necessary adjunct; TcPO₂ for pre-ulcerative lesions; multidisciplinary referral threshold.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the williamriveromd.com house style. Portrait 1024 × 1536 canvas, white or very light off-white (#fafafa) background. Restrained navy (#0f1e2e) and teal (#1a6b72) typography in a clean sans-serif — Inter (or Manrope or IBM Plex Sans) only; never a serif font. Thin teal connector arrows. Top-to-bottom clinical logic, centered, symmetrical, generous margins.

TITLE (top): bold navy, "Vascular Safety Gate in the Cramp-and-Pigment DM-CKD Patient" with a smaller clinical-teal subtitle "ABI → TBI → TcPO₂ before any compression".

NODES (top → bottom, in this order):

1. Rounded rectangle (navy outline) — START
   "Adult HD patient with intradialytic cramps and/or lower-limb stasis pigmentation"
   ↓
2. Rounded rectangle (teal #1a6b72) — ASSESSMENT
   "Stage on the Hypoxic Lower-Limb Spectrum (0–6); document CEAP class; perform 10-g monofilament + 128-Hz tuning fork; inspect feet"
   ↓
3. Diamond (teal outline) — DECISION
   "Is the patient diabetic OR at spectrum stage ≥ 3?"
       ┌── No  ─── 4a. Rounded rectangle (green #1f7a4d) "ABI sufficient as safety gate — proceed per local PAD protocol"
       └── Yes ─── 5. Rounded rectangle (amber #b8860b)
                       "Measure ABI + TBI (always both); add TcPO₂ if CEAP ≥ C4 or any pre-ulcerative finding"
                       ↓
                   6. Diamond (teal outline)
                       "ABI ≥ 0.8 AND TBI ≥ 0.7?"
                           ┌── Yes ─── 7a. Rounded rectangle (green) "Adequate inflow — compression therapy permitted, supervised; revisit at 3 months"
                           └── No  ─── 7b. Rounded rectangle (red #b91c1c)
                                           "Critical or compressible-PAD signature — do NOT initiate compression; multidisciplinary referral (vascular + podiatry + wound care) within the week"
                                           ↓
                                       8. Rounded rectangle (purple #6b21a8)
                                           "Consider angiography for revascularization candidacy; optimize anemia, glycemia, volume in parallel"

Side notes (soft gray, off to the side at the relevant nodes):
  • Next to node 5: "Medial arterial calcification → ABI often falsely normal in DM-CKD (Wukich et al., 2015; Prasad et al., 2019)"
  • Next to node 6: "In heavily calcified vessels, prefer TBI threshold and TcPO₂ over ABI alone"
  • Next to node 7b: "Same-week pathway; cinacalcet / SGLT2i decisions deferred to vascular plan"

Rounded rectangles for actions and endpoints; diamonds for decisions. Consistent corner radius, consistent node widths, balanced left-right branching. No icons unless they materially clarify (none used here). No photorealistic people. No dark background. Generous whitespace, mobile-readable labels.

Bottom-right footer: "© williamriveromd.com" in small subtle gray (~#6b7280) medical-publication styling at ~70% opacity. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, dark backgrounds, overprocessed HDR, excessive saturation, decorative or handwritten typefaces. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the "© williamriveromd.com" footer attribution.

QUALITY CHECK:
Reads as a credible journal/guideline figure. Top-to-bottom logic unambiguous. Decision diamonds distinct from action rectangles. ABI / TBI / TcPO₂ trio explicit. Both branch outcomes (compression permitted vs not) clearly differentiated by colour. Bottom-right "© williamriveromd.com" visible.

ALT TEXT: A portrait clinical algorithm for the vascular safety gate in the cramp-and-pigment DM-CKD patient, sequencing ABI, TBI, and transcutaneous PO₂ before any compression therapy, with explicit ABI ≥ 0.8 and TBI ≥ 0.7 thresholds, multidisciplinary-referral routing for sub-threshold patients, and notes that ABI is falsely normal in medial arterial calcification.
OG WIDTH: 1024
OG HEIGHT: 1536
```

---

## 010 — Management 4-Tier Circular Workflow (clinician-only)

```
IMAGE NUMBER: 010
SECTION PLACEMENT: §md-management — opens the tiered management section
FILE NAME: dialysis-cramps-management-tiers-workflow.png
ARCHETYPE: Circular Workflow / Cycle (infographic-skill, Archetype 8)
AUDIENCE: clinicians
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
MODE SCOPING: clinician-only — embed inside <section class="section mode-physician" id="md-management">; must NOT render in patient mode.
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — circular workflow with central object
- 3D component graphics: light semi-3D on the central patient pictogram
- algorithm/flowchart: implicit cyclic flow with reassessment arrow
PURPOSE: A single circular diagram that anchors the four-tier management lever and makes the "reassess continuously" loop visible — one prescription, two axes, four levers.
KEY CONCEPTS: Tier 1 volume/Rx; Tier 2 acute rescue; Tier 3 bioenergetic; Tier 4 lower-limb venous axis; ABI/TBI safety gate; quarterly reassessment loop.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a polished circular clinical workflow infographic in the williamriveromd.com house style. Square 1024 × 1024 canvas, white (#ffffff) background. Clean sans-serif typography in Inter (or Manrope or IBM Plex Sans); never a serif font.

TITLE STRIP — top centered, bold navy (#0f1e2e): "Management — one prescription, two axes, four levers" with a smaller clinical-teal (#1a6b72) subtitle in Nunito Sans: "The cramp-and-pigment patient · reassess each tier each visit".

CENTER — a small, calm, semi-3D pictogram of a hemodialysis patient's lower leg (knee-to-mid-foot silhouette) on a soft pastel-teal disc, with a tiny stylised dialysis-machine icon beside it. A small navy label beneath the central disc reads "Patient".

FOUR-TIER WHEEL — four rounded quadrant cards arranged in a balanced compass around the central disc (12, 3, 6, 9 o'clock positions), connected to the centre by short teal arrows. Each card has a coloured top accent band, a Tier label, a one-line summary, and three short bullet points (Manrope, ~12pt equivalent):

  12 o'clock — green (#1f7a4d) "Tier 1 · Volume & Rx"
    • Dry weight ≤ 1–3 mo reassessment
    • IDWG ≤ 4–5% / UFR ≤ 10 mL/kg/h
    • Individualise dialysate (Na, HCO₃⁻, Mg)

  3 o'clock — teal (#1a6b72) "Tier 2 · Acute Rescue"
    • Passive stretching / dorsiflexion
    • Reposition out of shortened-calf seated posture
    • Saline bolus per protocol if hypotensive

  6 o'clock — amber (#b8860b) "Tier 3 · Bioenergetic"
    • L-carnitine — IV 1 g post-HD; oral 500–1000 mg PO BID where IV unavailable
    • Renal B-complex daily; CoQ10 in statin users
    • Magnesium mid-normal; consider Mg 0.75 mmol/L dialysate

  9 o'clock — purple (#6b21a8) "Tier 4 · Lower-Limb Venous Axis"
    • Leg elevation 2×/day, calf-pump activation
    • ABI + TBI before any compression; TcPO₂ at CEAP ≥ C4
    • Multidisciplinary referral at spectrum stage ≥ 3

A dotted teal circular arrow running outside the wheel (clockwise) labelled "Reassess each tier each visit" closes the loop and reads as the continuous-reassessment cycle. A small footer strip in navy below the wheel: "Volume + oxygen + stretching + footwear — same levers, both axes."

Restrained clinical palette throughout. Generous whitespace; mobile-readable labels. No photorealistic people; no dark backgrounds. Bottom-right: "© williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism of people, dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the © williamriveromd.com attribution. No journal/guideline/brand names.

QUALITY CHECK:
Reads as a calm, credible journal-quality circular workflow. Four tiers visually distinguishable by colour and clearly labelled. Central patient pictogram is small enough that the four quadrants dominate the wheel. Reassessment arrow continuous and unmistakable. Bottom-right attribution visible. Embeddable inside a clinician-mode-only section without competing with the patient-mode hero.

ALT TEXT: A clinician-mode circular workflow showing the four management levers — Tier 1 volume and Rx, Tier 2 acute rescue, Tier 3 bioenergetic, Tier 4 lower-limb venous axis — arranged around a small central patient pictogram, with a dotted outer "reassess each tier each visit" loop.
OG WIDTH: 1024
OG HEIGHT: 1024
```

---

## 011 — Pharmacology Quick-Reference Card (clinician-only)

```
IMAGE NUMBER: 011
SECTION PLACEMENT: §md-pharmacology — top of the section, above the HTML table
FILE NAME: dialysis-cramps-pharmacology-reference-card.png
ARCHETYPE: Clinician Reference Card (simple-figure skill, Scaffold E — adapted to landscape 4:3)
AUDIENCE: clinicians
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
MODE SCOPING: clinician-only — embed inside <section class="section mode-physician" id="md-pharmacology">; must NOT render in patient mode.
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — compact table-style reference card
- 3D component graphics: none
- algorithm/flowchart: minimal — a small spectrum-stage band at the top mapping each agent to its earliest indication
PURPOSE: A glance-able quick-reference for the 10 pharmacology + adjunct levers used across the Hypoxic-Lower-Limb Spectrum, with CKD-specific dosing and safety, including the Philippine-context oral L-carnitine alternative.
KEY CONCEPTS: agent × indication × dose × CKD safety; spectrum-stage anchor; PH-context oral L-carnitine; ABI/TBI safety gate for compression; denosumab for active Charcot in CKD.

COPY-READY IMAGE GENERATOR GPT PROMPT:
A clean clinician reference card, landscape 1536 × 1152 on a white (#ffffff) background. Publication-grade nephrology design. Clean sans-serif typography in Inter (or Manrope, IBM Plex Sans) for body and IBM Plex Sans for tabular numerals; never a serif font.

TITLE — top centered, bold navy (#0f1e2e): "Pharmacology & Adjuncts — Cramps + Stasis Pigmentation in CKD" with a smaller clinical-teal subtitle: "Doses · evidence · CKD-specific safety · spectrum-stage anchor".

SPECTRUM STAGE BAND — a thin horizontal band immediately under the title showing the 7 spectrum stages (0–6) as small colour-graded chips (green → teal → amber → red → purple), with each agent in the table below later labelled with its earliest indicated stage chip.

MAIN TABLE — four-column layout occupying most of the canvas; alternating row fills (white and very soft gray #f3f4f6). Column headers in teal (#1a6b72) on a soft gray header bar; column 1 narrow (agent), columns 2–4 wider:

| Agent | Earliest stage | Dose / regimen | CKD safety / note |
|---|---|---|---|
| L-carnitine — IV | 1 | 1 g IV post-HD × 12–24 wk (post-dialyzer line) | Evidence-grade route; reassess at 12 wk |
| L-carnitine — oral (PH alt) | 1 | 500–1000 mg PO BID × 12–24 wk | Where IV unavailable; pair with low red-meat / low egg-yolk diet (TMAO) |
| Renal B-complex | 0 | 1 tab PO daily, post-HD on dialysis days | Avoid non-renal multivitamins (vitamin A) |
| Magnesium dialysate | 1 | Consider 0.75 mmol/L vs ≤ 0.5 mmol/L | Dial-Mag pragmatic RCT in progress (Tangri 2025) |
| CoQ10 | 1 | 100–200 mg PO daily × 12 wk trial | Consider in statin co-prescribed patients |
| Saline bolus (acute) | 1 | 100–250 mL NS IV per protocol | Pair with UF reduction + passive stretch |
| Topical wound care | 3 | Emollient ± short-contact topical steroid | Gentle skin care; treat fissures early |
| Compression bandaging | 3 | Multilayer compression by trained team | Only after ABI ≥ 0.8 + TBI ≥ 0.7 |
| Pentoxifylline | 5 | 400 mg PO TID (renal-dose reduce in HD) | Adjunct to compression in C5–C6 VLU |
| Denosumab | 4 | 60 mg SC single dose | Active Charcot in CKD; replete 25-OH-D + Ca first |
| Cinacalcet / etelcalcetide review | any | Re-titrate or convert | Hypocalcemic cramping class effect |
| SGLT2i / GLP-1 RA in DM | any | Per KDIGO 2024–2026 | Baseline + quarterly foot exam mandatory |

Each "Earliest stage" cell carries the matching colour chip from the band (small filled chip + numeral). The "CKD safety / note" column uses concise navy text with a small amber-triangle icon in front of any safety-critical note (compression gate; Ca repletion before denosumab; foot exam mandate). Footer strip in navy: "Pharmacology is additive — fix volume / UF / dialysate first."

Restrained clinical palette throughout. No photorealistic people. No dark backgrounds. Bottom-right: "© williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks (within the figure itself — DOIs live in the HTML accordion).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the © williamriveromd.com attribution. No brand or journal names in the figure.

QUALITY CHECK:
Table legible at full resolution; column headers high-contrast on the header bar. The PH-context oral L-carnitine row is clearly visible directly under the IV row. Spectrum-stage chips visible per agent. Safety triangles visible in the safety column. Footer note present. Bottom-right attribution visible. Embeddable inside a clinician-mode-only section.

ALT TEXT: A clinician quick-reference card for the dialysis cramp / stasis pigmentation guide — an alphabetical pharmacology table covering L-carnitine IV and oral (Philippine alternative), dialysate magnesium, renal B-complex, CoQ10, saline bolus, topical wound care, compression, pentoxifylline, denosumab, calcimimetic review, and SGLT2i / GLP-1 foot-exam mandate, each anchored to the earliest spectrum stage of indication.
OG WIDTH: 1536
OG HEIGHT: 1152
```

---

## 012 — Diabetes Accelerator Mechanism (clinician-only)

```
IMAGE NUMBER: 012
SECTION PLACEMENT: §md-spectrum — under the "Why diabetes pushes patients forward" subsection
FILE NAME: dialysis-cramps-diabetes-accelerator-mechanism.png
ARCHETYPE: Biomedical Mechanism Figure (biomedical-mechanism-figure skill) — organ → inset → bottom flow
AUDIENCE: clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
MODE SCOPING: clinician-only — embed inside <section class="section mode-physician" id="md-spectrum">; must NOT render in patient mode.
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — multi-scale review-article layout
- 3D component graphics: light semi-3D on the foot cross-section and arterial wall
- algorithm/flowchart: bottom injury → intervention → benefit summary
PURPOSE: Diagram the five DM-specific accelerators that push patients further along the spectrum — and pin the ABI/TBI safety-gate failure mode to the calcified vessel.
KEY CONCEPTS: autonomic neuropathy → deeper IDH; sensory neuropathy → masked pre-ulcer; AGEs + glycation → mitochondrial impairment; medial arterial calcification (MAC) → false-normal ABI; impaired neutrophil + glycated matrix → delayed healing.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade biomedical mechanism schematic in the AJKD/NEJM review-article style (without naming any journal). Landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif labels in Inter (or Manrope, IBM Plex Sans); never a serif font.

TITLE — bold navy (#0f1e2e), top centred: "Diabetes accelerates every node of the Hypoxic-Lower-Limb Spectrum" with a smaller clinical-teal subtitle: "Five DM-specific levers · same upstream field".

LEFT PANEL — organ-level context: a simplified flat-vector diabetic neuropathic foot in lateral view (no gore), soft light gray-blue anatomy. Show a pale-sienna gaiter pigmentation band above the ankle, a small dotted area over the metatarsal pressure point labelled "pressure-point pre-ulcer / silent injury", and an outline glyph indicating monofilament insensitivity (a small monofilament tip with a question-mark glyph). A small dashed connector box on the calf vasculature points into the central inset.

CENTER PANEL — magnified arterial cross-section inside a thin dashed border. Show a small artery wall with three concentric layers: intima (thin teal), media (soft sienna with visible calcium granules — render medial arterial calcification as small irregular ivory/cream specks in the media), adventitia (gray-blue). A small label reads "Medial arterial calcification (MAC)". A dotted arrow points out of the inset with the note "→ ABI falsely normal; TBI required".

A second mini-inset above the artery shows a stylised mitochondrion with red dashed lines indicating "ETC impairment from AGEs / hyperglycemia → ↓ ATP".

A third mini-inset below the artery shows an autonomic nerve fibre with a faded synapse and the label "Autonomic neuropathy → blunted vasoconstrictor reflex → deeper IDH".

RIGHT PANEL — vertical "five-accelerator ladder", each row a soft pastel-amber rounded card with a one-line label in navy (Manrope, ~13pt equivalent), reading top to bottom:
  1. "Autonomic neuropathy → deeper IDH (hit 1 amplified)"
  2. "Sensory neuropathy → silent injury / Charcot risk"
  3. "AGEs + glycation → mitochondrial OXPHOS impairment (hit 4 amplified)"
  4. "Medial arterial calcification → ABI falsely normal → TBI/TcPO₂ mandatory"
  5. "Impaired neutrophils + glycated matrix → delayed healing → stage-5 ulcers"

BOTTOM SUMMARY FLOW — single horizontal row of three rounded boxes connected by teal arrows:
  LEFT (pale pink #fbe7e7): "Pathology drivers: same upstream field, amplified by DM at every node"
  CENTER (pale blue #e3edf9): "Intervention: ABI + TBI + TcPO₂; daily foot exam; SGLT2i / GLP-1 with foot-exam mandate; aggressive glycemic control without hypoglycemia; podiatry + vascular co-management"
  RIGHT (pale green #e9f5ec): "Benefit: spectrum progression slowed; ulceration delayed; amputation risk reduced"

Restrained clinical palette. Generous whitespace. Mobile-readable labels. No photorealism of people. No dark backgrounds. Bottom-right: "© williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism of feet or wounds (no gore), dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable. Five accelerators legible and individually labelled. Medial-arterial-calcification inset clearly shows the calcium in the media (not the intima) and the dotted "ABI falsely normal" caption. Bottom three-box flow connected by visible teal arrows. Bottom-right attribution visible. Reads as a clinician figure — never a patient hero.

ALT TEXT: A review-article schematic showing the five diabetes-specific accelerators that push patients forward along the Hypoxic-Lower-Limb Spectrum — autonomic neuropathy deepening intradialytic hypotension, sensory neuropathy masking pre-ulcerative injury, AGEs and glycation impairing mitochondrial ATP, medial arterial calcification rendering ABI falsely normal so TBI is mandatory, and impaired neutrophil function with a glycated matrix delaying wound healing.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## 013 — Clinic Audit Pipeline (clinician-only)

```
IMAGE NUMBER: 013
SECTION PLACEMENT: §md-audit — top of the testable-predictions section
FILE NAME: dialysis-cramps-clinic-audit-pipeline.png
ARCHETYPE: Horizontal step sequence (simple-figure skill, Scaffold C — 4 steps as an audit pipeline)
AUDIENCE: clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
MODE SCOPING: clinician-only — embed inside <section class="section mode-physician" id="md-audit">; must NOT render in patient mode.
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes — 4 rounded research-step cards connected by arrows
- 3D component graphics: none
- algorithm/flowchart: implicit research-pipeline sequence
PURPOSE: Turn the four testable predictions in §md-audit into a one-image clinic-audit pipeline a single nephrology unit can run on its own cohort.
KEY CONCEPTS: cross-sectional association; clustered phenotype; intervention coupling; tissue-oxygen signature; converting the hypothesis into local data.

COPY-READY IMAGE GENERATOR GPT PROMPT:
A clean clinical-research infographic, landscape 1792 × 1024 on a white (#ffffff) background. Clean sans-serif typography in Inter (or Manrope, IBM Plex Sans); never a serif font.

TITLE STRIP — top centred, bold navy: "Clinic Audit Pipeline — Test the Hypoxic Lower-Limb Hypothesis on Your Panel" with a smaller clinical-teal subtitle: "Four testable predictions, one season-long audit".

Four rounded rectangular cards arranged horizontally in a single row, connected by bold navy right-pointing arrows. Each card has a coloured top accent band (steps 1–4 coloured teal → teal-deep → amber → purple), a step number, a bold step label, and three short bullet points. Cards sit on a very soft gray panel (#f3f4f6).

  Step 1 — teal (#1a6b72) "Phenotype the cohort"
    • All maintenance HD patients in unit (n)
    • CEAP class for each lower limb (photo log)
    • Cramp Frequency–Severity score; intradialytic BP log

  Step 2 — teal-deep (#0e4a50) "Capture exposures"
    • IDWG, UFR, dry-weight gap (mean over 6 sessions)
    • Hgb, albumin, free carnitine (where available)
    • ABI + TBI for every diabetic / spectrum-stage-3+ patient

  Step 3 — amber (#b8860b) "Test predictions"
    • Cramps vs pigmentation cross-sectional χ² / OR
    • Clustering with UFR / Hgb / TBI (regression)
    • Pre-/post intervention bundle (volume + cofactor + venous axis)

  Step 4 — purple (#6b21a8) "Report + iterate"
    • Cramp-frequency delta, photo-log progression delta
    • Transcutaneous PO₂ trend at pigmented vs unpigmented limbs
    • Local audit memo + williamriveromd.com cohort contribution

Bottom strip: full-width soft gray (#f3f4f6) panel, brief summary sentence in navy: "Clinic data become the test — convert the hypothesis into local evidence and a teaching dataset." Bottom-right: "© williamriveromd.com" in small semi-transparent navy text. No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, dark backgrounds, overprocessed HDR, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the © williamriveromd.com attribution.

QUALITY CHECK:
Reads as a credible journal/audit figure. Four research-step cards clearly numbered and sequenced. Each step's three bullets legible at full resolution. Bottom summary sentence present. Bottom-right attribution visible. Embeddable inside a clinician-mode-only section.

ALT TEXT: A clinician-mode four-step clinic-audit pipeline for testing the Hypoxic-Lower-Limb hypothesis on a single nephrology unit's panel — phenotype the cohort, capture exposures (UFR, Hgb, ABI/TBI), test the four predictions with cross-sectional and intervention analyses, and report a local audit memo with cramp-frequency delta, photo-log progression, and transcutaneous PO₂ trends.
OG WIDTH: 1792
OG HEIGHT: 1024
```

---

## Production checklist (for the human running the GPT)

For each prompt above:
1. Open <https://chatgpt.com/g/g-pmuQfob8d-image-generator>.
2. Paste the `COPY-READY IMAGE GENERATOR GPT PROMPT` block (everything between that line and the `NEGATIVE INSTRUCTIONS:` block — but pasting both is also fine; the GPT respects the negative block).
3. Confirm the output matches `PIXEL DIMENSIONS` exactly (especially for #000 — 1200 × 630 is the OG sweet spot and must not be resized).
4. Save with the `FILE NAME:` shown above into `generated-images/` (under the local Stage-2 folder if you're following the standard pipeline).
5. Export a `.webp` twin of every `.png` so the guide's `<picture>` tags can pick the smaller asset first.
6. Hand the folder to Stage 2 (`williamriveromd-local-image-generator`) to validate the prompt-file schema, build `image-manifest.csv` / `image-manifest.json`, and wire the images back into `guides/dialysis-cramps-stasis-pigmentation.html`.
