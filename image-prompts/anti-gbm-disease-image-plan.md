# Image Plan Blueprint — Anti-GBM Disease (Goodpasture Disease)

**Guide:** `guides/anti-gbm-disease.html` · **Calculator:** `guides/calc-anti-gbm-renal-risk.html`
**Route:** https://renalcarematters.com/guides/anti-gbm-disease.html
**Paste target:** ChatGPT Image Generator GPT — https://chatgpt.com/
**Supersedes:** `image-prompts/anti-gbm-disease-image-prompts.md` (first-pass pack, retired)
**Skill provenance:** hero = `williamriveromd-hero-vignette` (v3) · OG cards, warning-signs poster, plasma-exchange procedural, life-after grid, regimen card = `williamriveromd-infographic-skill` (v5) · filter-mesh comparison, tests sequence, treatment timeline, time-saves-filters, biopsy triptych, variant map, double-positive table, Alport comparison, antibody spectrum, children/adults card = `williamriveromd-simple-figure` (v1) · kidney–lung sigil = `williamriveromd-organ-crosstalk-sigil-graphic` · clinician mechanism = `williamriveromd-biomedical-mechanism-figure` · first-24-hours, who-to-treat, Philippine pathway = `williamriveromd-algorithm-generator-skill` (Modes A, B, C).

---

## 1. Visual strategy — understandable at every educational level

The guide asks readers to grasp three things fast: **what breaks** (a hidden part of the filter mesh), **why hours matter** (crescents scar within days), and **what treatment does** (remove antibodies, stop new ones, protect). Every image serves one of those ideas.

| Principle | How it is applied |
|---|---|
| **One idea per image** | Each patient image answers one question a reader would ask ("What is it?", "What do I watch for?", "What happens in plasma exchange?"). No multi-topic posters on the patient side. |
| **Analogy first, then the real name** | The "fine mesh / sieve" analogy appears in pictures and is always labeled with the real term (basement membrane, crescent) so the analogy never replaces the physiology. |
| **Icon + word, never color alone** | Every color-coded state also has a shape or icon (check, warning triangle, clock) so color-blind and low-literacy readers read it the same way. |
| **Consistent color meaning across all 22 images** | Red `#b91c1c` = urgent/danger · Amber `#b8860b` = caution/decide · Green `#1f7a4d` = do this/protective · Teal `#1a6b72` = information/structure · Soft purple `#6c3d8e` = crescent/immune injury · Navy `#0f1e2e` = text only. |
| **Short on-image text** | Patient images: ≤ 8 words per label, everyday words ("pee less", not "oliguria"). Clinician images: concise technical labels; every acronym is defined in the guide's figure caption. |
| **Calm, not frightening** | No graphic blood, no "attacking" combat imagery, no distressed faces. Bleeding is shown as small red dots or a streak, never pooled blood. |
| **Numbers only when verified** | Patient images carry almost no statistics. Clinician images carry only figures already checked against the sources (Floyd 2023, Suhlrie 2026, McAdoo & Pusey 2025, Kuang 2026). The kidney-survival bar chart stays **code-native** so its data cannot drift. |
| **Filipino context** | People are Filipino patients, families, and clinicians in bright Philippine clinical or home settings; examples avoid foreign brands and use local cues (generic pain-reliever names used in the Philippines). |
| **Illustration, not fake tissue** | Biopsy and immunofluorescence panels are clearly stylized drawings, labeled as illustrations, never synthetic photomicrographs passed off as real. |

### House rules baked into every prompt
- Light backgrounds only: white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, light teal `#eef6f7`. Never navy/charcoal/black fills.
- On-image type: **Inter** only (approved set: Inter, Nunito Sans, IBM Plex Sans, Manrope; never serif). Named in every prompt.
- Attribution: small semi-transparent navy `© renalcarematters.com`, bottom-right (bottom-center for portrait). The wordless vignette hero carries no text by spec.
- **No journal names, guideline acronyms (no "KDIGO" on images), brand names, or other watermarks.**
- American English spelling in all on-image text.
- File format: `.png` master; save a `.webp` twin with the same name.

### How to produce (Stage 1 → Stage 2)
1. Open the Image Generator GPT. For each image, copy the **whole fenced block** (prompt + negatives) and paste it as one message.
2. Check the result against that image's **QUALITY CHECK** list (spelling of every label, numbers exactly as written, attribution present).
3. Save as `images/<FILE NAME>` (PNG) and export a `.webp` twin.
4. Hand back to Claude with `williamriveromd-local-image-generator` (Stage 2) to wire new images into the guide, swap the interim code-drawn figures, and refresh `og:image`.

### Production priority
- **Numbering:** the image number always equals the number in the file name (005 is the code-native chart and has no prompt; 022 and 023 are the share cards).
- **Tier 1 (do first; biggest gain in understanding):** 001 hero, 022 OG card, 006 filter mesh, 008 warning signs, 010 plasma exchange, 011 treatment timeline, 002 mechanism (clinician).
- **Tier 2:** 004 first-24-hours, 015 who-to-treat, 016 regimen card, 009 tests, 013 life after, 003 variant map.
- **Tier 3:** 007 sigil, 012 time-saves-filters, 014 biopsy pitfall, 017–021, 023 calculator card.

---

## 2. Asset map

| # | File name | Guide placement | Mode | Skill | Size | HTML status |
|---|---|---|---|---|---|---|
| 001 | `anti-gbm-disease-vignette-hero.png` | Hero disc `figure.hero-figure.mode-patient` | Patient | hero-vignette | 2048×2048 | referenced (interim drawing) |
| 022 | `anti-gbm-disease-og.png` | `og:image`, `twitter:image`, Latest-guides card | All | infographic | 1200×630 | referenced (interim) |
| 006 | `anti-gbm-disease-06-filter-mesh.png` | `#what-it-is` — replaces the patient use of figure 02 | Patient | simple-figure B | 1792×1024 | **new — wire in** |
| 007 | `anti-gbm-disease-07-kidney-lung-sigil.png` | `#what-it-is`, after the lung paragraph | Patient | organ sigil | 1024×1024 | **new — wire in** |
| 008 | `anti-gbm-disease-08-warning-signs.png` | `#warning-signs`, after the sign list | Patient | infographic (multi-panel) | 1792×1024 | **new — wire in** |
| 009 | `anti-gbm-disease-09-same-day-tests.png` | `#tests`, after the test list | Patient | simple-figure C | 1792×1024 | **new — wire in** |
| 010 | `anti-gbm-disease-10-plasma-exchange.png` | `#treatment`, under "1. Remove the antibodies" | Patient | infographic (procedural) | 1792×1024 | **new — wire in** |
| 011 | `anti-gbm-disease-11-treatment-timeline.png` | `#treatment`, end of section | Patient | simple-figure C (timeline) | 1792×1024 | **new — wire in** |
| 012 | `anti-gbm-disease-12-time-saves-filters.png` | `#recovery`, before the bar chart | Patient | simple-figure B | 1792×1024 | **new — wire in** |
| 013 | `anti-gbm-disease-13-life-after.png` | `#after`, after the action list | Patient | infographic (multi-panel) | 1792×1024 | **new — wire in** |
| 002 | `anti-gbm-disease-02-mechanism.png` | `#md-pathophysiology` | Clinician | biomedical-mechanism | 1792×1024 | referenced (interim) |
| 014 | `anti-gbm-disease-14-biopsy-pitfall.png` | `#md-diagnosis`, with the "disappearing glomeruli" paragraph | Clinician | simple-figure C (triptych) | 1792×1024 | **new — wire in** |
| 004 | `anti-gbm-disease-04-first-24-hours.png` | `#md-treatment` | Clinician | algorithm Mode A | 1024×1536 | referenced (interim) |
| 015 | `anti-gbm-disease-15-who-to-treat.png` | `#md-treatment`, "Who to treat" subsection | Clinician | algorithm Mode B | 1024×1536 | **new — wire in** |
| 016 | `anti-gbm-disease-16-regimen-card.png` | `#md-treatment`, after the regimen table | Clinician | infographic (reference card) | 1024×1536 | **new — wire in** |
| 003 | `anti-gbm-disease-03-variant-map.png` | `#md-variants` | Clinician | simple-figure E | 1792×1024 | referenced (interim) |
| 017 | `anti-gbm-disease-17-double-positive.png` | `#md-double-positive` | Clinician | simple-figure E | 1792×1024 | **new — wire in** |
| 018 | `anti-gbm-disease-18-alport-alloimmune.png` | `#md-alport-tx` | Clinician | simple-figure B | 1792×1024 | **new — wire in** |
| 019 | `anti-gbm-disease-19-antibody-spectrum.png` | `#md-pathophysiology`, after the IgG-subclass sentence | Clinician | simple-figure C | 1792×1024 | **new — wire in** |
| 020 | `anti-gbm-disease-20-children-adults.png` | `#md-children` | Clinician | simple-figure E | 1536×1152 | **new — wire in** |
| 021 | `anti-gbm-disease-21-philippine-pathway.png` | `#md-philippines` | Clinician | algorithm Mode C | 1024×1536 | **new — wire in** |
| 023 | `calc-anti-gbm-renal-risk-og.png` | Calculator `og:image` | Clinician | infographic (OG) | 1200×630 | **new — wire in** |
| 005 | `anti-gbm-disease-05-kidney-survival.png` | `#recovery`, `#md-prognosis` | Both | **code-native (no prompt)** | 1600×900 | keep as is (data figure) |

---

## 3. Patient-facing images

### 001 — Circular vignette hero

```
IMAGE NUMBER: 001
SECTION PLACEMENT: Hero, figure.hero-figure.mode-patient > .hero-vignette (patient mode only)
FILE NAME: anti-gbm-disease-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 — Scaffold A (clinical people); composition archetype H Clinical
AUDIENCE: patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX:
- photorealistic models: two (patient, nephrologist)
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Convey "urgent but in good hands": the doctor explaining why treatment starts today.
KEY CONCEPTS: emergency care, same-day treatment, plasma exchange, reassurance
CAMERA: over-the-shoulder from behind the clinician
HUMAN VARIATION: young adult Filipino man (late 20s, lean, short undercut black hair, light stubble, oval face, medium-brown skin, pale-blue gown, nasal oxygen cannula, attentive calm expression, hand on folded blanket); Filipina nephrologist (mid-40s, shoulder-length wavy dark-brown hair tied low, white coat over deep plum blouse, holding a tablet, seen three-quarter from behind). At least 12 traits differ from the previous guide hero.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder from behind the clinician.
Subject: a Filipino young man in his late 20s (lean build, short undercut black hair, light stubble, oval face, medium-brown skin, pale-blue hospital gown, thin nasal oxygen cannula) sitting upright on a clean emergency-department stretcher, listening attentively and calmly to a Filipina nephrologist in her mid-40s (shoulder-length wavy dark-brown hair tied low, white coat over a deep plum blouse) seen from behind at three-quarter rear, holding a tablet and leaning slightly forward. Soft-focus background: an unbranded plasma-exchange machine on a wheeled stand with neatly routed clear tubing, and an IV pole with a small straw-yellow fluid bag. Bright, modern Philippine hospital emergency bay, soft daylight from a high window, gentle shallow depth of field.
Visual hierarchy: the patient's face and the doctor's shoulder form the hero subject at 60–70% of the circle; the machine and IV pole are small supporting context at 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft blurred pale wall in the upper-left of the circle with no faces, equipment, or icons inside it.
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Absolutely NO text of any kind: no title, caption, label, readable screen, logo, brand name on the machine, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, more than four supporting elements, readable screens or labels, cropped circle, faces cut by the circle edge, anything inside the title-safe zone, baked-in text, logos, brand names, watermarks, rectangular frames, dark or charcoal backgrounds, visible blood on the patient, coughing blood, distressed or panicked expressions, cartoon style, neon, HDR, over-saturation, duplicated people, extra fingers, stock-photo smiling at the camera.
```
QUALITY CHECK: 2048×2048; circle 85–90% with white margin, never cropped; one dominant subject; empty title-safe zone upper-left; no readable text anywhere; calm expressions.
ALT TEXT: "" (decorative; the H1 beside it carries the meaning)
OG WIDTH: 2048 · OG HEIGHT: 2048

---

### 022 — Open Graph / social share card

```
IMAGE NUMBER: 022
SECTION PLACEMENT: og:image, twitter:image, Latest-guides strip card
FILE NAME: anti-gbm-disease-og.png
ARCHETYPE: OG / social share card
AUDIENCE: mixed (link-preview audience on Facebook, Messenger, Viber)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title block
- 3D component graphics: kidney, lungs, glomerulus
- algorithm/flowchart: none
PURPOSE: Make a reader stop scrolling and understand "kidney + lung emergency" from the thumbnail.
KEY CONCEPTS: anti-GBM disease, Goodpasture, kidney and lung, act within hours

COPY-READY IMAGE GENERATOR GPT PROMPT:
Open Graph social share card, exactly 1200 × 630 px, calm premium medical-editorial style on a clean off-white (#fafafa) background. LEFT 60%: bold title in navy (#0f1e2e), clean sans-serif Inter, two lines: "Anti-GBM Disease" and, in clinical teal (#1a6b72), "(Goodpasture Disease)". Below it, a navy Inter tagline on two lines: "A kidney and lung emergency." and "Why treatment must start within hours." A small rounded red (#b91c1c) pill badge with white Inter text "Act the same day" under the tagline. Generous negative space, strong hierarchy readable as a small thumbnail.
RIGHT 40%: a soft white circle containing a clean semi-3D illustration of a pair of pink lungs above two kidneys, linked by a thin dotted teal loop; beside the kidneys, a small glomerulus (rounded ball of capillary loops) with a thin teal ribbon lining its loops. A few tiny soft-red dots inside the lungs suggest bleeding gently, no pooled blood.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Never change the 1200 × 630 size. Avoid dark backgrounds, cartoon style, clutter, tiny text, AI gibberish text, graphic blood, combat or "attack" imagery, neon, HDR, serif or decorative fonts; use Inter only. Never omit the attribution.
```
QUALITY CHECK: exactly 1200×630; title legible at thumbnail size; spelling "Goodpasture"; light background; attribution bottom-right.
ALT TEXT: "Anti-GBM Disease (Goodpasture Disease): a kidney and lung emergency — renalcarematters.com"
OG WIDTH: 1200 · OG HEIGHT: 630

---

### 006 — What goes wrong: the filter mesh (analogy → real anatomy)

```
IMAGE NUMBER: 006
SECTION PLACEMENT: #what-it-is (patient), replacing the patient-section use of figure 02
FILE NAME: anti-gbm-disease-06-filter-mesh.png
ARCHETYPE: Simple figure — Scaffold B (side-by-side comparison)
AUDIENCE: patients and families (any reading level)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two comparison panels, callout chips
- 3D component graphics: soft semi-3D glomerulus and mesh close-up
- algorithm/flowchart: none
PURPOSE: Let a reader with no science background see what the disease does to one kidney filter.
KEY CONCEPTS: glomerulus as a tiny ball of vessels; basement membrane as a fine mesh; hidden part exposed; antibodies line the mesh; blood leaks; crescent forms within days

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient-education comparison illustration, clean medical-journal graphical-abstract style, clearly an educational illustration. White (#ffffff) background. Title centered at top in bold navy (#0f1e2e), clean sans-serif Inter: "What goes wrong in one kidney filter". Subtitle in clinical teal (#1a6b72), Inter: "Each kidney has about a million of these tiny filters".
A soft dashed vertical divider splits the canvas into two equal rounded panels.
LEFT panel, header with a green (#1f7a4d) check icon: "Healthy filter". A soft semi-3D glomerulus drawn as a small ball of looping pink capillaries wrapped in a fine, evenly woven teal mesh. A magnifying circle shows the mesh weave close up, with one small lock-shaped piece tucked neatly inside the weave, labeled "Hidden part of the mesh". Two simple arrows: a blue arrow labeled "Water and waste pass into urine" and a short curved arrow keeping small red blood cells and protein dots inside, labeled "Blood and protein stay in".
RIGHT panel, header with a red (#b91c1c) warning-triangle icon: "Anti-GBM disease". The same filter. In the magnifying circle the lock-shaped piece is now open and exposed. Small Y-shaped antibodies line up along the mesh in one smooth, straight line, labeled "Antibodies coat the mesh". A few small tears in the mesh with tiny red blood cells slipping through, labeled "Blood leaks into urine". A soft purple (#6c3d8e) crescent-shaped cap of piled-up cells hugs one side of the filter, labeled "Crescent: scar-forming cells". A small clock icon with the label "Can happen within days".
Bottom full-width soft-gray (#f3f4f6) strip with a navy Inter sentence: "The mesh is the kidney's basement membrane. Treatment works best before crescents turn into scar."
Labels short and large (mobile-readable, at least 11 pt equivalent), generous whitespace, calm restrained colors.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, cartoon faces, combat or weapon imagery, exploding or bleeding kidneys, pooled blood, clutter, more than eight labels, tiny text, AI gibberish text, serif fonts (Inter only), photorealistic tissue presented as real. Never omit the attribution.
```
QUALITY CHECK: two panels clearly different; lock "hidden" vs "exposed" reads instantly; every label spelled exactly; crescent drawn as a cap beside (not inside) the capillary ball; attribution present.
ALT TEXT: "Healthy kidney filter with an intact mesh beside a filter in anti-GBM disease, where antibodies coat the exposed mesh, blood leaks, and a crescent forms."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 007 — Kidney–lung sigil: two filters, one mesh

```
IMAGE NUMBER: 007
SECTION PLACEMENT: #what-it-is (patient), after the paragraph on the lungs
FILE NAME: anti-gbm-disease-07-kidney-lung-sigil.png
ARCHETYPE: Organ-crosstalk sigil (minimal monoline)
AUDIENCE: patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: monoline organ icons, dotted loop
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Give a memorable symbol for "the same target sits in the kidneys and the lungs".
KEY CONCEPTS: shared basement membrane; lungs and kidneys affected together

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring a pair of lungs and a pair of kidneys.
RELATIONSHIP: show that both organs share the same filter mesh, using a calm bidirectional dotted loop arrow that flows down from the lungs to both kidneys and back up, forming a soft circle. Inside the loop, at the center, place a tiny monoline woven-mesh icon (a small square of crisscross lines).
STYLE: minimal clinical line-art, thin monoline strokes, soft teal-blue palette (#1a6b72 and pale cyan), white background, clean rounded organ shapes, balanced symmetrical sigil composition, generous whitespace, no photorealism, no 3D, no shadows.
LABELS (three only, clean sans-serif Inter, navy #0f1e2e, small): "Lung air sacs" beside the lungs, "Kidney filters" beside the kidneys, and "Same mesh" under the central mesh icon.
COMPOSITION: lungs top-center, two kidneys symmetrically below, mesh icon in the middle of the loop.
OUTPUT: square, clean margins, publication-grade medical icon aesthetic. Small semi-transparent "© renalcarematters.com" in the bottom-right corner. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, more than three labels, dark background, neon colors, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: only three labels; loop clearly connects both organs both ways; attribution present.
ALT TEXT: "Line drawing linking the lungs and kidneys with a dotted loop and a small mesh icon labeled same mesh."
OG WIDTH: 1024 · OG HEIGHT: 1024

---

### 008 — Warning signs at a glance

```
IMAGE NUMBER: 008
SECTION PLACEMENT: #warning-signs (patient), after the list of signs
FILE NAME: anti-gbm-disease-08-warning-signs.png
ARCHETYPE: Multi-panel educational infographic (patient action poster)
AUDIENCE: patients, families, barangay health workers
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: six icon cards, urine color strip, action banner
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Let someone recognize the danger signs in seconds, even with limited reading.
KEY CONCEPTS: urine color change; less urine; swelling; coughing blood; breathlessness lying flat; tiredness; go today

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient-education warning-signs poster, landscape 16:9, clean modern Philippine clinic aesthetic, white (#ffffff) background. Title at top-left in bold navy (#0f1e2e), clean sans-serif Inter: "Warning signs of anti-GBM disease". Subtitle in clinical teal (#1a6b72), Inter: "Often starts like flu or a cough, then speeds up over days".
Six equal rounded cards in a 3 × 2 grid on a soft gray (#f3f4f6) panel, each with a simple flat line icon in teal at the top and a bold navy label of no more than six words beneath:
1. A horizontal strip of five urine-sample cup swatches from left to right: pale yellow with a small green check, then tea-brown, cola-dark brown, and red, each of the last three with a small red warning dot. Label: "Dark, tea, cola, or red urine".
2. A urine cup only one-quarter full with a small downward arrow. Label: "Peeing much less than usual".
3. Simple outline of lower legs and ankles with gentle puffiness lines and a fingertip leaving a small dent. Label: "Swollen face, legs, or ankles".
4. A folded tissue with a small thin red streak, no pooled blood. Label: "Coughing up blood".
5. A person resting propped up on two pillows with a small breath icon. Label: "Short of breath lying flat".
6. A tired person icon with a small low-battery symbol. Label: "Very tired, pale, no appetite".
Bottom full-width rounded banner in clinical red (#b91c1c) with white Inter text in two lines: "Blood in urine + swelling or less urine, or any coughing of blood:" and "Go to the emergency department TODAY." Under the banner, small navy Inter text: "Say: I may have kidney inflammation."
Icons flat, friendly, and clear; generous whitespace; text large enough to read on a phone.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, graphic blood or pooled blood, frightening faces, clutter, paragraph text, tiny labels, AI gibberish text, serif fonts (Inter only), cartoon mascots. Never omit the attribution.
```
QUALITY CHECK: exactly six cards; urine strip order pale yellow → tea → cola → red; red banner reads exactly as written; "TODAY" capitalized; attribution present.
ALT TEXT: "Six warning signs: dark or red urine, peeing less, swelling, coughing up blood, breathlessness lying flat, and tiredness, with a red banner saying go to the emergency department today."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 009 — The same-day tests

```
IMAGE NUMBER: 009
SECTION PLACEMENT: #tests (patient), after the list of tests
FILE NAME: anti-gbm-disease-09-same-day-tests.png
ARCHETYPE: Simple figure — Scaffold C (step sequence, 2 rows × 3 cards)
AUDIENCE: patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: six test cards, amber note strip
- 3D component graphics: small blood tube, urine cup, kidney, chest X-ray icon
- algorithm/flowchart: none
PURPOSE: Show what each test answers so the many tests on day one feel purposeful, not frightening.
KEY CONCEPTS: anti-GBM antibody; ANCA together; urine; creatinine and potassium; chest image; kidney biopsy ribbon pattern; treatment may start first

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean patient-education infographic, white (#ffffff) background. Title at top-center in bold navy (#0f1e2e), clean sans-serif Inter: "The tests, usually all on the same day". Six rounded cards in two rows of three on a very soft gray (#f3f4f6) panel; each card has a teal (#1a6b72) top accent band, one small clean semi-3D object, a bold navy title, and one short plain-language question in teal:
1. Small blood tube. Title: "Anti-GBM antibody test". Question: "Are the antibodies there?"
2. Small blood tube with a second tube beside it. Title: "ANCA test". Question: "Is a second antibody there too?" Small navy note: "About 1 in 3 have both".
3. Clear urine cup. Title: "Urine test". Question: "Is there blood and protein?"
4. Small kidney with a gauge dial. Title: "Creatinine and potassium". Question: "How much filtering is left?"
5. Simple chest X-ray outline of lungs. Title: "Chest X-ray or CT". Question: "Is there bleeding in the lungs?"
6. Small kidney with a thin biopsy needle and a round inset showing a filter whose loops are outlined by one smooth bright ribbon. Title: "Kidney biopsy". Question: "Confirms it and counts healthy filters".
Bottom full-width amber (#b8860b) soft-tint strip with a navy Inter sentence: "If doctors strongly suspect it, treatment starts right away, even before every result is back."
Generous whitespace, mobile-readable labels.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, needles shown piercing skin, blood spatter, clutter, tiny text, AI gibberish text, serif fonts (Inter only), real-looking pathology slides. Never omit the attribution.
```
QUALITY CHECK: six cards in the order listed; "ANCA" spelled correctly; amber strip text exact; no needle-in-skin imagery; attribution present.
ALT TEXT: "Six same-day tests: anti-GBM antibody, ANCA, urine, creatinine and potassium, chest X-ray or CT, and kidney biopsy, with a note that treatment may start before results return."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 010 — Plasma exchange, explained

```
IMAGE NUMBER: 010
SECTION PLACEMENT: #treatment (patient), under "1. Remove the antibodies already in the blood"
FILE NAME: anti-gbm-disease-10-plasma-exchange.png
ARCHETYPE: Access / procedural education infographic (mixed media)
AUDIENCE: patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: one Filipina patient and one nurse
- 2D infographic: four numbered step chips, three fact chips
- 3D component graphics: unbranded plasma-exchange machine, separation chamber, plasma bag
- algorithm/flowchart: simple left-to-right flow
PURPOSE: Remove fear of the machine by showing, step by step, what plasma exchange does and how long it takes.
KEY CONCEPTS: blood out; plasma separated; antibodies removed with the plasma; cells returned with albumin or donor plasma; 2–3 hours; daily until antibody test negative

COPY-READY IMAGE GENERATOR GPT PROMPT:
Mixed-media patient-education procedural infographic, landscape 16:9, bright white (#ffffff) background, calm Philippine hospital aesthetic. Title at top-left in bold navy (#0f1e2e), clean sans-serif Inter: "Plasma exchange: cleaning the antibodies out of the blood".
LEFT third: a soft photorealistic Filipina woman in her early 50s (short layered graying hair, round face, light-brown skin, reading glasses on her head, pale-green hospital gown) resting comfortably semi-upright in a hospital bed, with a neat white dressing over a catheter at the right side of her neck; a Filipino male nurse in his 30s (navy scrubs, short hair) checks the line beside her. Calm, relaxed expressions, bright daylight.
CENTER third: a clean semi-3D unbranded plasma-exchange machine with a clear separation chamber in which blood visibly divides into a dark-red cell layer below and a straw-yellow plasma layer above. Thin clear tubing connects the patient to the machine.
RIGHT third: a collection bag of straw-yellow plasma containing a few small Y-shaped antibody icons, labeled "Plasma with harmful antibodies: removed". A return line back to the patient labeled "Blood cells returned with albumin or donor plasma".
Across the top of the flow, four numbered teal (#1a6b72) step chips in Inter: "1 Blood flows out", "2 Machine separates the plasma", "3 Antibodies leave with the plasma", "4 Blood cells come back".
Along the bottom, three rounded soft-gray (#f3f4f6) fact chips with small icons, navy Inter text: a clock icon "About 2 to 3 hours", a calendar icon "Every day until the antibody test is negative (usually about 2 weeks)", a speech-bubble icon "Tingling lips? Tell the nurse".
Clean labels, generous whitespace, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, brand names or readable screens on the machine, visible blood outside the tubing, needles in skin, distressed expressions, tangled tubing, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Do not show a dialysis filter with dialysate ports. Never omit the attribution.
```
QUALITY CHECK: four steps in order; plasma drawn straw-yellow, cells dark red; antibodies only in the removed bag; fact chip wording exact ("usually about 2 weeks"); no brand names; attribution present.
ALT TEXT: "Plasma exchange: blood flows from a neck catheter to a machine that separates plasma, the plasma carrying antibodies is removed, and blood cells return with albumin or donor plasma."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 011 — Treatment timeline (the first six months)

```
IMAGE NUMBER: 011
SECTION PLACEMENT: #treatment (patient), end of section before the green "Before you start" box
FILE NAME: anti-gbm-disease-11-treatment-timeline.png
ARCHETYPE: Simple figure — Scaffold C variant (swim-lane timeline)
AUDIENCE: patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: five horizontal lanes on a time axis
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Answer "how long will this take?" with one picture: which treatment runs when, and when it stops.
KEY CONCEPTS: plasma exchange ~2 weeks; cyclophosphamide 2–3 months; steroids tapered over ~6 months; protection medicines; check-ups; usually no long-term medicine

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean patient-education timeline infographic, white (#ffffff) background. Title at top-left in bold navy (#0f1e2e), clean sans-serif Inter: "Your treatment, month by month". A horizontal time axis along the top with tick labels in navy Inter: "Day 1", "Week 2", "Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6".
Five horizontal rounded swim-lane bars, each with a small flat icon at the left and a bold navy label:
1. Teal (#1a6b72) bar from Day 1 to Week 2: "Plasma exchange, daily" with small text "until the antibody test is negative".
2. Purple (#6c3d8e) bar from Day 1 to Month 3: "Cyclophosphamide tablets" with small text "2 to 3 months".
3. Amber (#b8860b) bar from Day 1 to Month 6 that visibly tapers from thick to thin: "Steroid tablets" with small text "high dose, lowered step by step, then stopped".
4. Green (#1f7a4d) bar from Day 1 to Month 6: "Protection medicines" with small text "infection, stomach, and bone".
5. Light-gray dotted bar across the whole axis with small dot markers: "Check-ups" with small text "blood and urine tests".
Below the lanes, a slim soft-gray (#f3f4f6) dashed box: "Dialysis, if needed, supports the body while the kidneys recover."
Bottom full-width soft teal (#eef6f7) strip with navy Inter text: "Most people with classic disease need no long-term medicine after this. If ANCA is also positive, treatment lasts longer."
Generous whitespace, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, drug brand names, pill-bottle labels, dose numbers, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: plasma-exchange bar ends at Week 2; cyclophosphamide ends at Month 3; steroid bar tapers and ends at Month 6; bottom strip wording exact; no doses shown; attribution present.
ALT TEXT: "Timeline: daily plasma exchange for about two weeks, cyclophosphamide for two to three months, steroids tapered and stopped by six months, protection medicines, and regular check-ups."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 012 — Why hours matter: time saves filters

```
IMAGE NUMBER: 012
SECTION PLACEMENT: #recovery (patient), before the code-native kidney-survival chart
FILE NAME: anti-gbm-disease-12-time-saves-filters.png
ARCHETYPE: Simple figure — Scaffold B (comparison, icon array)
AUDIENCE: patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two rows of ten filter icons, clock, caption
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Make the link between speed of treatment and kidney recovery visible without statistics.
KEY CONCEPTS: healthy filters left; crescents scar; earlier treatment saves more filters; lungs usually respond well

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean patient-education comparison illustration, white (#ffffff) background. Title at top-center in bold navy (#0f1e2e), clean sans-serif Inter: "Why hours matter: every day saves filters".
Two horizontal rounded panels stacked vertically, each showing a row of exactly ten small round kidney-filter icons (simple balls of capillary loops):
TOP panel, header with a green (#1f7a4d) check: "Treated early". Seven icons are healthy (pink loops with a teal outline), three have a small purple (#6c3d8e) crescent cap. Small navy note at right: "More filters left to recover".
BOTTOM panel, header with an amber (#b8860b) clock: "Treated late". One icon is healthy; nine are flat gray scarred circles with a purple crescent fused into scar. Small navy note at right: "Fewer filters left".
Between the panels on the left, a simple clock-and-calendar icon with a downward arrow labeled "Days of delay".
Bottom soft-gray (#f3f4f6) strip with navy Inter text: "Doctors count healthy filters on the biopsy to estimate recovery. Lung bleeding usually stops with treatment." Under it, very small gray italic Inter text: "Illustration of the idea, not real patient data."
Generous whitespace, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, percentages or statistics, frightening imagery, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Each row must contain exactly ten icons. Never omit the attribution.
```
QUALITY CHECK: exactly 10 icons per row; 7 healthy top, 1 healthy bottom; disclaimer line present; no numbers other than icon counts; attribution present.
ALT TEXT: "Two rows of ten kidney filters: treated early leaves seven healthy filters; treated late leaves one, showing why fast treatment matters."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 013 — Life after anti-GBM disease

```
IMAGE NUMBER: 013
SECTION PLACEMENT: #after (patient), after the action list
FILE NAME: anti-gbm-disease-13-life-after.png
ARCHETYPE: Multi-panel educational infographic (action grid)
AUDIENCE: patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: one small header photo
- 2D infographic: eight action cards
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Turn the after-care advice into eight things a person can remember and do.
KEY CONCEPTS: no smoking or vaping; avoid fumes; follow-up tests; blood pressure; avoid NSAIDs; ask before herbals; vaccines and pregnancy planning; transplant after 6 months antibody-negative

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient-education action infographic, landscape 16:9, white (#ffffff) background. Header row: at left, a small soft photorealistic photo of a Filipino couple in their 40s walking together in a bright neighborhood park in the morning (man with short gray-flecked hair in a light polo, woman with a long ponytail in a mustard blouse), relaxed and healthy; at right of the photo, a bold navy (#0f1e2e) title in clean sans-serif Inter: "Life after anti-GBM disease" and a teal (#1a6b72) subtitle: "It usually happens once. Help keep it that way."
Below, eight equal rounded cards in a 4 × 2 grid on soft gray (#f3f4f6), each with one flat icon and a bold navy label (no more than eight words):
1. Red (#b91c1c) crossed-out cigarette and vape icon: "No smoking or vaping, ever".
2. Red crossed-out fuel can and paint-thinner can icon: "Avoid fuel, thinner, and solvent fumes".
3. Teal blood tube and urine cup with a calendar: "Keep every follow-up test".
4. Teal blood-pressure cuff: "Keep blood pressure controlled".
5. Amber (#b8860b) pill with a caution triangle: "Ask before ibuprofen or mefenamic acid".
6. Amber leaf with a question mark: "Ask before herbal products".
7. Green (#1f7a4d) syringe-and-shield plus a small heart: "Ask about vaccines; plan pregnancy".
8. Green kidney with a small calendar showing "6": "Transplant after 6 antibody-free months".
Generous whitespace, mobile-readable, friendly flat icons.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, brand names or packaging, people smoking, clutter, paragraph text, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: eight cards in the order listed; "mefenamic acid" spelled correctly; no brands; attribution present.
ALT TEXT: "Eight after-care actions: no smoking or vaping, avoid fumes, keep follow-up tests, control blood pressure, ask before pain relievers and herbals, ask about vaccines and pregnancy, and transplant after six antibody-free months."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

## 4. Clinician-facing images

### 002 — Mechanism: cryptic epitope to crescent (review-article schematic)

```
IMAGE NUMBER: 002
SECTION PLACEMENT: #md-pathophysiology (clinician); replaces interim figure 02
FILE NAME: anti-gbm-disease-02-mechanism.png
ARCHETYPE: Biomedical mechanism figure (organ panel → magnified unit → molecular inset → injury/intervention/benefit)
AUDIENCE: clinicians, residents, nephrology fellows
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: dashed insets, callouts, bottom summary boxes
- 3D component graphics: soft semi-3D vector anatomy
- algorithm/flowchart: injury → intervention → benefit flow
PURPOSE: Trace the causal chain from a hidden collagen epitope to crescent formation and lung hemorrhage, and show where each treatment acts.
KEY CONCEPTS: α3α4α5(IV) NC1 hexamer; sulfilimine cross-links; cryptic EA/EB epitopes; HLA-DR15 T cells; IgG1/IgG3; complement and C5a; GBM rupture; fibrin; parietal epithelial proliferation; crescent of uniform age; alveolar capillary permeability with smoking

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade biomedical mechanism schematic in a scientific review-article style.
Topic: anti-glomerular basement membrane disease. Disease context: rapidly progressive glomerulonephritis with or without alveolar hemorrhage. Central mechanism: exposure of a cryptic collagen IV epitope leads to antibody binding, complement activation, capillary-wall rupture, and crescent formation.
ORGAN-LEVEL PANEL (left): simplified gray-blue kidney cross-section labeled "Kidney: RPGN" and a simplified pair of lungs labeled "Lung: alveolar hemorrhage", each with a small dashed connector box pointing right.
MOLECULAR INSET (upper center, dashed box): the collagen IV network as a woven mesh; zoom on one NC1 hexamer of six rounded subunits labeled "α3", "α4", "α5". Left version labeled "Intact hexamer: epitopes hidden" with small cross-link marks labeled "sulfilimine cross-links (peroxidasin)". Arrow to right version labeled "Hexamer dissociates" with two red dots on α3 labeled "EA" and "EB". Small labels for possible triggers along the arrow: "smoking, hydrocarbons, infection". Beside it, a small antigen-presenting cell and CD4 T cell labeled "HLA-DR15 presentation".
MAGNIFIED GLOMERULUS (upper right, dashed box): left half shows capillary loops with a thin continuous teal ribbon along the GBM labeled "Linear IgG (IgG1, IgG3)", small complement icons labeled "C3, C5a", and neutrophils and macrophages. Right half shows a ruptured capillary wall with red cells and fibrin strands spilling into Bowman space, labeled "GBM rupture, fibrin", and a layered soft-purple crescent of proliferating parietal epithelial cells labeled "Cellular crescent → fibrous within weeks". Small note: "Crescents of uniform age".
LUNG INSET (lower center, small dashed box): alveolar capillary with continuous endothelium; a small "smoke" cue and the label "↑ permeability lets IgG reach the alveolar basement membrane".
BOTTOM SUMMARY FLOW (three boxes with arrows): pale-pink left box "Injury drivers": "Cryptic α3(IV)NC1 exposed • anti-GBM IgG • complement • neutrophils, macrophages". Center box "Interventions": "Plasma exchange removes circulating IgG • cyclophosphamide stops new antibody • glucocorticoids dampen inflammation". Pale-blue right box "Benefit": "Salvage of cellular (not fibrous) lesions • control of lung hemorrhage".
White background, flat vector with soft semi-3D shading, muted clinical palette (gray-blue anatomy, red for injury, blue for therapeutic effects, pale pink and pale blue summary boxes, soft purple crescent), thin dashed connectors, clean sans-serif labels set in Inter only, generous whitespace, labels readable at slide size.
Bottom-right: small semi-transparent navy "© renalcarematters.com". No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative effects, cartoon cells, combat imagery, invented pathways, numeric thresholds, misspelled Greek letters, more text than listed, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: α3/α4/α5, EA/EB, HLA-DR15, IgG1/IgG3 spelled exactly; crescent outside the tuft in Bowman space; interventions box lists exactly three agents; attribution present.
ALT TEXT: "Mechanism schematic: collagen IV hexamer dissociation exposes α3 epitopes, IgG binding with complement ruptures the capillary wall, a crescent forms, and plasma exchange, cyclophosphamide, and glucocorticoids act at different steps."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 014 — Reading the biopsy: linear IgG and the "disappearing glomeruli" pitfall

```
IMAGE NUMBER: 014
SECTION PLACEMENT: #md-diagnosis (clinician), with the "disappearing glomeruli" paragraph
FILE NAME: anti-gbm-disease-14-biopsy-pitfall.png
ARCHETYPE: Simple figure — Scaffold C (three-panel triptych)
AUDIENCE: clinicians, pathology-curious residents
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three stylized immunostain panels, bottom checklist
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Teach why a crescent-heavy biopsy can under-show linear IgG and how to avoid missing the diagnosis.
KEY CONCEPTS: linear IgG on intact glomeruli; loss of IgG in destroyed tufts; collagen IV α5 stain as structural correlate; mimics of linear IgG

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean clinical-education triptych, white (#ffffff) background, clearly STYLIZED ILLUSTRATIONS (not real photomicrographs). Title at top-center in bold navy (#0f1e2e), clean sans-serif Inter: "Reading the biopsy in anti-GBM disease". Subtitle in clinical teal (#1a6b72): "Linear IgG can disappear where the GBM is destroyed".
Three equal rounded cards on a soft gray (#f3f4f6) panel, each with a colored top accent band, a stylized circular immunostain panel drawn on a pale gray-green tile, a bold navy header, and one short teal line:
Card 1 — green (#1f7a4d) band, header "Intact glomerulus": a glomerulus whose capillary loops are outlined by one smooth, continuous bright-green ribbon. Line: "Strong linear IgG along the GBM".
Card 2 — purple (#6c3d8e) band, header "Crescentic glomerulus": a collapsed tuft surrounded by a layered purple crescent and fibrin strands, with NO green ribbon at all. Line: "IgG lost as the tuft is destroyed".
Card 3 — teal band, header "Collagen IV α5 stain": the crescentic glomerulus again, with staining absent in the tuft but preserved as a thin line along Bowman capsule. Line: "Confirms tissue loss, not absent antibody".
Thin navy arrows from card 1 to 2 to 3.
Bottom full-width soft teal (#eef6f7) strip with three short navy Inter checklist items with small check icons: "Report IgG on intact glomeruli", "Correlate with serology", "Exclude mimics: diabetic kidney disease, fibrillary GN, monoclonal deposition".
Generous whitespace, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark or black backgrounds (draw stain panels on pale tiles), photorealistic micrographs presented as real tissue, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: card 2 has no green ribbon; card 3 keeps Bowman capsule staining; "α5" rendered correctly; attribution present.
ALT TEXT: "Stylized immunostains: linear IgG on an intact glomerulus, loss of IgG in a crescentic glomerulus, and collagen IV alpha-5 staining confirming tissue loss."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 004 — Suspected anti-GBM disease: the first 24 hours (emergency algorithm)

```
IMAGE NUMBER: 004
SECTION PLACEMENT: #md-treatment (clinician); replaces interim figure 04
FILE NAME: anti-gbm-disease-04-first-24-hours.png
ARCHETYPE: Clinical algorithm — Style Mode A (AHA-style emergency algorithm)
AUDIENCE: emergency physicians, internists, nephrologists
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: full vertical algorithm with decision diamonds
PURPOSE: Give a one-glance emergency pathway that prevents the commonest error: waiting for results or the biopsy.
KEY CONCEPTS: suspect RPGN ± hemoptysis; same-day anti-GBM + ANCA; start before confirmation; early biopsy; plasma around the biopsy; full course; follow-up

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a polished medical guideline algorithm flowchart in the style of an emergency-care provider algorithm. White background, clean sans-serif typography set in Inter (never a serif font), thin black arrows, pastel rounded boxes, pink decision diamonds. Portrait, centered, spacious, easy to read. Title at top-left in bold black Inter: "Suspected anti-GBM disease: the first 24 hours".
Conventions: peach rounded boxes for assessment and activation; pink diamonds for decisions; blue rounded boxes for active treatment; green rounded boxes for monitoring and follow-up; gray capsules for timing steps; red bold labels beside urgent arrows.
Content, top to bottom:
1. Peach box: "Rapidly rising creatinine + blood and protein in urine ± coughing blood or new lung shadows".
2. Peach box: "Same-day tests: anti-GBM antibody AND ANCA (MPO, PR3) • urine sediment • creatinine, potassium, CBC • chest X-ray or CT".
3. Pink diamond: "High clinical suspicion?" Left branch labeled in red bold "YES" → Blue box: "Start now: glucocorticoids + plasma exchange as soon as available. Do not wait for results." Right branch "NO / uncertain" → Peach box: "Expedite results; re-assess within hours" with an arrow rejoining the main path.
4. Gray capsule: "As soon as safe".
5. Blue box: "Kidney biopsy: linear IgG, % crescents, % normal glomeruli. Add 300–600 mL fresh plasma to exchange within 3 days of biopsy".
6. Pink diamond: "Dialysis-dependent AND 100% crescents or >50% sclerosis AND no lung hemorrhage?" Branch "NO" (red bold label) → Blue box: "Full course: daily plasma exchange until antibody negative (~14 days) • oral cyclophosphamide 2–3 months • steroids tapered over ~6 months". Branch "YES" → Peach box: "Individualize: short trial vs supportive care (see next algorithm)".
7. Green box at the bottom: "Follow-up: if ANCA-positive, maintenance as for ANCA vasculitis • no smoking • transplant only after antibodies negative ≥6 months".
Optional dashed horizontal divider separating steps 1–3 (recognition) from steps 4–7 (confirmation and treatment). Strict alignment, consistent spacing, short text in every box.
Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
No photos, no 3D, no dark background, no decorative icons, no excessive shadows, no extra drug doses beyond those written, no serif fonts (Inter only), no AI gibberish text. Never omit the attribution.
```
QUALITY CHECK: decision 3 "YES" goes to start-now box; decision 6 wording exact including "AND"; doses exactly as written; footer present.
ALT TEXT: "Emergency algorithm: suspect anti-GBM disease, send anti-GBM and ANCA the same day, start treatment on high suspicion, biopsy early, then give the full course or individualize when dialysis-dependent with extensive crescents and no lung hemorrhage."
OG WIDTH: 1024 · OG HEIGHT: 1536

---

### 015 — Dialysis-dependent at presentation: who to treat

```
IMAGE NUMBER: 015
SECTION PLACEMENT: #md-treatment (clinician), "Who to treat, and the edge cases" subsection
FILE NAME: anti-gbm-disease-15-who-to-treat.png
ARCHETYPE: Clinical algorithm — Style Mode B (journal nephrology treatment algorithm)
AUDIENCE: nephrologists
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: symmetrical branching tree
PURPOSE: Make the futility decision explicit and humane: when intensive treatment is clearly indicated, and when a short trial or supportive care is reasonable.
KEY CONCEPTS: lung hemorrhage always treated; dialysis status; 100% crescents or >50% sclerosis; favorable features; 2–4 week trial; transplant planning

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a clean academic medical journal treatment algorithm flowchart on a white background, resembling a nephrology review figure: minimal, centered, symmetrical, publication-ready. Typography clean, black, journal-like, set in Inter (never a serif font). Beige rounded rectangles for diagnosis and severity classification, pale blue rounded rectangles for assessment steps, pale green rounded rectangles for treatment and outcome options. Thin muted teal arrows, top-down flow with balanced left-right branching, consistent box widths.
Title at top: "Anti-GBM disease: deciding how hard to treat".
Content:
Top beige box: "Confirmed or strongly suspected anti-GBM disease".
Pale blue box: "Pulmonary hemorrhage present?" Left arrow "Yes" → Pale green box: "Full treatment regardless of kidney findings (lung hemorrhage remits in 90–100%)". Right arrow "No" → next.
Pale blue box: "Dialysis needed at presentation?" Left arrow "No" → Pale green box: "Full treatment: plasma exchange + cyclophosphamide + glucocorticoids". Right arrow "Yes" → next.
Pale blue box: "Biopsy: 100% crescents or >50% global sclerosis?" Left arrow "No" → Pale green box: "Treat intensively; recovery is realistic". Right arrow "Yes" → next.
Beige box: "Any favorable feature? • dialysis started <72 h • non-oliguric • another cause for dialysis (e.g., acute tubular injury) • ANCA co-positive • younger, low treatment risk". Left arrow "Yes" → Pale green box: "Consider a short 2–4 week trial; taper if no kidney response". Right arrow "No" → Pale green box: "Supportive care and dialysis are reasonable; share the decision".
Bottom full-width pale gray note box: "Dialysis for more than 7 days before treatment: recovery very rare • Plan transplant only after antibodies are negative for at least 6 months".
Concise text, centered alignment, wide margins, no icons.
Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
No icons, no photos, no 3D, no dark background, no clutter, no additional numbers beyond those written, no serif fonts (Inter only), no AI gibberish text. Never omit the attribution.
```
QUALITY CHECK: lung-hemorrhage question comes first; numbers exactly "90–100%", "<72 h", "2–4 week", "7 days", "6 months"; footer present.
ALT TEXT: "Decision tree: treat fully with lung hemorrhage or without dialysis; when dialysis-dependent with 100% crescents or over 50% sclerosis, consider a short trial if favorable features exist, otherwise supportive care."
OG WIDTH: 1024 · OG HEIGHT: 1536

---

### 016 — Standard regimen reference card

```
IMAGE NUMBER: 016
SECTION PLACEMENT: #md-treatment (clinician), after the "Standard regimen" table
FILE NAME: anti-gbm-disease-16-regimen-card.png
ARCHETYPE: Clinician reference card (portrait)
AUDIENCE: nephrologists, internists, ward pharmacists
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: five stacked modular sections
- 3D component graphics: small icons only (bag, tablet, syringe, shield)
- algorithm/flowchart: none
PURPOSE: A ward-ready card summarizing doses, durations, and monitoring targets for the standard regimen.
KEY CONCEPTS: plasma exchange volume, replacement, endpoint, monitoring; cyclophosphamide dose and holds; prednisolone taper; rituximab alternative; prophylaxis

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical reference card for clinicians, publication-grade nephrology design, portrait. White (#ffffff) background. Bold navy (#0f1e2e) title at top in clean sans-serif Inter: "Anti-GBM disease: standard regimen". Teal (#1a6b72) subtitle: "Classic disease, adults".
Five stacked rounded modules, each with a teal header band, one small flat icon, and short navy Inter bullet lines (render every number exactly as written):
1. "Plasma exchange" (bag icon): "Daily, 40–60 mL/kg vs 5% albumin" • "Add 300–600 mL fresh plasma within 3 days of a procedure or with lung hemorrhage" • "Continue until antibody negative (~14 days); restart if titers rebound" • "Keep platelets >70 × 10⁹/L, fibrinogen >1 g/L, hemoglobin >90 g/L, corrected calcium normal".
2. "Cyclophosphamide, oral" (tablet icon): "2–3 mg/kg/day (ideal body weight), max 200 mg, for 2–3 months" • "Consider 50–100 mg/day if >55 years or on dialysis" • "Give after hemodialysis or plasma exchange" • "Hold if WBC <4 × 10⁹/L; restart at a lower dose".
3. "Glucocorticoids" (tablet icon): "Prednisolone 1 mg/kg/day, max 60 mg" • "Taper to 20 mg by week 6" • "Off by about 6 months".
4. "Rituximab (alternative or adjunct)" (syringe icon), purple (#6c3d8e) header band: "1 g on days 0 and 14, or 375 mg/m² weekly × 4" • "Delay plasma exchange 24–48 h after each dose" • "For cyclophosphamide contraindications or refractory disease".
5. "Prophylaxis" (shield icon), green (#1f7a4d) header band: "Cotrimoxazole (adjust for kidney function)" • "Antifungal, proton-pump inhibitor, calcium + vitamin D" • "Hepatitis B screen; antiviral if core antibody positive".
Footer line in small gray Inter: "Adjust for age, kidney function, and cytopenias; confirm against your local protocol."
Alternating very soft gray module fills, high readability, not cluttered.
Bottom-center: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, brand names, changed or rounded numbers, extra drugs not listed, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: verify every number character-by-character against this prompt (40–60 mL/kg; 300–600 mL; 3 days; ~14 days; >70 × 10⁹/L; >1 g/L; >90 g/L; 2–3 mg/kg/day; 200 mg; 50–100 mg/day; >55 years; <4 × 10⁹/L; 1 mg/kg/day; 60 mg; 20 mg; week 6; 6 months; 1 g days 0 and 14; 375 mg/m² × 4; 24–48 h); attribution bottom-center.
ALT TEXT: "Reference card of the standard anti-GBM regimen: plasma exchange dosing and targets, oral cyclophosphamide, prednisolone taper, rituximab as an alternative, and prophylaxis."
OG WIDTH: 1024 · OG HEIGHT: 1536

---

### 003 — Variant forms: four categories

```
IMAGE NUMBER: 003
SECTION PLACEMENT: #md-variants (clinician); replaces interim figure 03
FILE NAME: anti-gbm-disease-03-variant-map.png
ARCHETYPE: Simple figure — Scaffold E (2 × 2 reference grid)
AUDIENCE: clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: four category cards with management lines
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: One-glance map of the variant forms and what each changes in practice.
KEY CONCEPTS: overlap syndromes; immunologically distinct forms; clinical phenotype variants; medication/trigger-associated

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background. Bold navy (#0f1e2e) title at top-left in clean sans-serif Inter: "Variant forms of anti-GBM disease". Teal (#1a6b72) subtitle: "Four groups; each changes testing, treatment, or follow-up".
Four equal rounded cards in a 2 × 2 grid, each with a numbered colored circle, a bold navy header, four short body lines, a dashed divider, and a bold two-line practice note:
1. Teal (#1a6b72) card, light teal fill: header "Overlapping autoimmune disease". Lines: "With ANCA vasculitis (double-positive): about 1 in 3" • "With membranous nephropathy" • "With IgA nephropathy" • "Usually standard induction first". Practice note: "Double-positive: maintenance as for ANCA vasculitis".
2. Purple (#6c3d8e) card, light lavender fill: header "Immunologically distinct". Lines: "Alport syndrome after transplant: alloantibodies to α5" • "Seronegative or atypical: test negative, linear IgG on biopsy" • "Often milder, indolent course (atypical)" • "Check for a monoclonal protein". Practice note: "Standard blood tests can miss both".
3. Amber (#b8860b) card, light cream fill: header "Different clinical pattern". Lines: "Native-kidney relapse: rare, often lung bleeding, smokers" • "Older adults: more ANCA, worse survival" • "Normal kidney function: young, lung-first" • "IgG2/IgG4 antibodies in milder forms". Practice note: "Stop smoking; balance intensity vs infection".
4. Red (#b91c1c) card, light rose fill: header "Medication- or trigger-associated". Lines: "Alemtuzumab" • "Immune checkpoint inhibitors" • "Reported after infection epidemics" • "Reported after SARS-CoV-2 vaccination". Practice note: "Test anti-GBM promptly if kidney function falls".
Footer in small gray Inter: "Drug and vaccine links are reported associations; causation not proven."
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, drug brand names, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: four cards, numbered 1–4 in the listed colors; footer caveat present; "SARS-CoV-2" and "α5" rendered correctly; attribution present.
ALT TEXT: "Four variant categories of anti-GBM disease: overlap syndromes, immunologically distinct forms, different clinical patterns, and medication- or trigger-associated disease, each with a practice note."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 017 — Double-positive disease: a hybrid phenotype

```
IMAGE NUMBER: 017
SECTION PLACEMENT: #md-double-positive (clinician)
FILE NAME: anti-gbm-disease-17-double-positive.png
ARCHETYPE: Simple figure — Scaffold E (three-column comparison table)
AUDIENCE: clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: comparison table with a highlighted middle column
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Show at a glance why double-positive patients are induced like anti-GBM disease but maintained like ANCA vasculitis.
KEY CONCEPTS: hybrid phenotype; prodrome; chronicity; dialysis recovery tendency; relapse; maintenance

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background. Bold navy (#0f1e2e) title at top in clean sans-serif Inter: "Double-positive disease: two diseases in one". Teal (#1a6b72) subtitle: "Anti-GBM antibody + ANCA".
A clean comparison table with three columns and six rows. Column headers on soft gray (#f3f4f6): "Anti-GBM only" (teal text), "Double-positive" (purple #6c3d8e text, and the whole middle column has a soft lavender highlight), "ANCA vasculitis only" (amber #b8860b text). Row labels in bold navy on the left:
Row "Age": "Younger and older peaks" | "Older, like ANCA vasculitis" | "Older".
Row "Before diagnosis": "Short, abrupt" | "Longer prodrome" | "Longer prodrome".
Row "Biopsy": "Crescents of uniform age" | "More chronic damage" | "Lesions of mixed age".
Row "At presentation": "Severe: lung bleeding, dialysis" | "Severe, like anti-GBM" | "Variable".
Row "Relapse": "Rare" | "Like ANCA vasculitis" | "Common over years".
Row "After induction": "No maintenance needed" | "Maintenance as for ANCA vasculitis" | "Maintenance therapy".
Below the table, a full-width soft teal (#eef6f7) strip with bold navy Inter text: "Induce like anti-GBM disease. Maintain like ANCA vasculitis." Under it, small gray Inter text: "Double-positive patients also tended to recover from dialysis more often."
Alternating row fills, generous padding, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, added percentages, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: middle column highlighted; six rows exactly; summary strip exact; attribution present.
ALT TEXT: "Comparison table showing double-positive disease shares the severe presentation of anti-GBM disease and the age, chronicity, and relapse pattern of ANCA vasculitis."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 018 — Alport syndrome after transplant: alloimmune versus autoimmune

```
IMAGE NUMBER: 018
SECTION PLACEMENT: #md-alport-tx (clinician)
FILE NAME: anti-gbm-disease-18-alport-alloimmune.png
ARCHETYPE: Simple figure — Scaffold B (side-by-side comparison)
AUDIENCE: nephrologists, transplant teams
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two panels with molecular diagrams and practice chips
- 3D component graphics: soft semi-3D hexamers
- algorithm/flowchart: none
PURPOSE: Explain why routine assays can miss post-transplant anti-GBM disease in Alport syndrome.
KEY CONCEPTS: autoantibodies bind dissociated α3 epitopes; alloantibodies bind α5 EA on the intact hexamer; routine α3 assay may be negative; first year; graft loss

COPY-READY IMAGE GENERATOR GPT PROMPT:
Medical-education comparison figure, journal graphical-abstract style, white (#ffffff) background. Title centered at top in bold navy (#0f1e2e), clean sans-serif Inter: "Same name, different immune target". Soft dashed vertical divider splitting two equal rounded panels.
LEFT panel, teal (#1a6b72) header: "Classic anti-GBM disease (autoimmune)". A soft semi-3D NC1 hexamer of six subunits labeled "α3", "α4", "α5" shown splitting apart into separate subunits; small red Y-shaped autoantibodies bind exposed red dots on α3 labeled "α3 EA, α3 EB" (and one on α5 labeled "α5 EA"). Caption chip: "Binds only after the hexamer comes apart". Result chip with a green check: "Routine α3 antibody test: usually positive".
RIGHT panel, purple (#6c3d8e) header: "Alport syndrome after kidney transplant (alloimmune)". Two small kidney icons: a gray "Recipient: lacks normal α5" and a pink "Donor kidney: normal α3α4α5". The donor's hexamer stays fully intact; purple Y-shaped alloantibodies bind a dot on the intact α5 subunit labeled "α5 EA on intact hexamer". Result chip with an amber caution triangle: "Routine α3 test: may be negative". Two small navy chips: "Usually within the first year", "High risk of graft loss".
Bottom full-width soft teal (#eef6f7) strip with navy Inter text: "Know the genotype before transplant • tell the pathologist • a negative routine test does not exclude it".
Generous whitespace, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, photorealism, cartoon antibodies with faces, clutter, misrendered Greek letters, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: left hexamer split, right hexamer intact; α/EA/EB labels correct; amber caution on the right result; attribution present.
ALT TEXT: "Classic autoantibodies bind alpha-3 epitopes after the collagen hexamer comes apart, while Alport post-transplant alloantibodies bind alpha-5 on the intact hexamer and may be missed by routine tests."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 019 — Why severity varies: the antibody spectrum

```
IMAGE NUMBER: 019
SECTION PLACEMENT: #md-pathophysiology (clinician), after the sentence on narrower IgG2/IgG4 responses (also cross-link from #md-variants "Normal kidney function")
FILE NAME: anti-gbm-disease-19-antibody-spectrum.png
ARCHETYPE: Simple figure — Scaffold C (three-stage spectrum)
AUDIENCE: clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three stage cards on a gradient arrow
- 3D component graphics: small hexamer and antibody icons
- algorithm/flowchart: none
PURPOSE: Show how antigen breadth and IgG subclass relate to disease severity, from natural antibodies to aggressive disease.
KEY CONCEPTS: natural antibodies; epitope spreading; IgG subclass and complement activation

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean clinical-education infographic, white (#ffffff) background. Title at top-left in bold navy (#0f1e2e), clean sans-serif Inter: "Why severity varies: the antibody spectrum". Teal (#1a6b72) subtitle: "Broader targets and complement-fixing subclasses track worse disease".
A wide horizontal gradient arrow runs across the middle from pale teal (left) to deep red (#b91c1c, right), labeled above in navy Inter: "Epitope spreading and complement activation increase".
Three rounded cards sit on the arrow, each with a small row of five collagen-chain chips labeled "α1 α2 α3 α4 α5" in which targeted chains are filled and untargeted chains are outlined, a small row of IgG subclass chips, and a bold header:
Card 1, teal band, header "Healthy people": filled chips "α3, α4"; subclass chips "IgG2, IgG4"; line "Natural, low-activity antibodies; weak complement activation".
Card 2, amber (#b8860b) band, header "Normal kidney function form": filled chips "α3, α5"; subclass chips "IgG2, IgG4 (some IgG1)"; line "Mild lesions; often young smokers with lung bleeding".
Card 3, red band, header "Worsening kidney function": all five chips filled; subclass chips "IgG1 dominant + IgG3"; line "Strong complement activation; crescents".
Bottom soft-gray (#f3f4f6) strip with navy Inter text: "IgG1 and IgG3 activate complement best; IgG2 and IgG4 activate it weakly."
Generous whitespace, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, percentages, clutter, misrendered Greek letters, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: chip fills match each card (α3/α4; α3/α5; all five); subclass text exact; attribution present.
ALT TEXT: "Spectrum from natural antibodies targeting alpha-3 and alpha-4 with IgG2 and IgG4, to a mild form targeting alpha-3 and alpha-5, to severe disease targeting all five chains with IgG1 and IgG3."
OG WIDTH: 1792 · OG HEIGHT: 1024

---

### 020 — Children versus adults (2026 European cohort)

```
IMAGE NUMBER: 020
SECTION PLACEMENT: #md-children (clinician)
FILE NAME: anti-gbm-disease-20-children-adults.png
ARCHETYPE: Simple figure — Scaffold E (reference card, 4:3)
AUDIENCE: nephrologists, pediatric nephrologists
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two-column data card with paired values
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Summarize the pediatric-versus-adult comparison so the two key messages stand out: better function at diagnosis, and dialysis predicts outcome at any age.
KEY CONCEPTS: female predominance in children; eGFR at diagnosis; lung hemorrhage; cyclophosphamide-free regimens; final eGFR; dialysis as predictor

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical data card, publication-grade nephrology design, white (#ffffff) background. Bold navy (#0f1e2e) title at top-left in clean sans-serif Inter: "Children vs adults with anti-GBM disease". Teal (#1a6b72) subtitle: "European cohort, 2020–2024: 25 children, 47 adults".
A clean two-column comparison table with column headers on soft gray (#f3f4f6): "Children" (teal) and "Adults" (navy). Row labels in bold navy; render every value exactly:
"Median age": "14 years" | "61 years".
"Female": "80%" | "40%".
"eGFR at diagnosis (median)": "36" | "13".
"Dialysis at diagnosis": "46%" | "62%".
"Lung hemorrhage": "43%" | "21%".
"Cyclophosphamide-free regimen": "32%" | "9%".
"Final eGFR, off dialysis (median)": "71" | "32".
"Kidney failure at last visit": "24%" | "38%".
Small gray note under the table: "eGFR in mL/min/1.73 m². Dialysis, lung hemorrhage, and kidney-failure differences were not statistically significant."
Two bold callout boxes at the bottom: a teal box "Children had better kidney function at diagnosis and better final eGFR" and an amber (#b8860b) box "Dialysis at diagnosis predicted a worse kidney outcome at any age".
Alternating row fills, mobile-readable.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, photos of children, rounded or altered numbers, extra rows, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: verify all 16 values character-by-character (14/61; 80/40; 36/13; 46/62; 43/21; 32/9; 71/32; 24/38); non-significance note present; attribution present.
ALT TEXT: "Data card comparing 25 children and 47 adults: children were more often female, had higher eGFR at diagnosis and at follow-up, and dialysis at diagnosis predicted worse outcome at any age."
OG WIDTH: 1536 · OG HEIGHT: 1152

---

### 021 — Philippine practice pathway

```
IMAGE NUMBER: 021
SECTION PLACEMENT: #md-philippines (clinician)
FILE NAME: anti-gbm-disease-21-philippine-pathway.png
ARCHETYPE: Clinical algorithm — Style Mode C (renalcarematters.com house style)
AUDIENCE: Philippine internists, nephrologists, ER and ward teams
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: optional flat line icons
- 3D component graphics: none
- algorithm/flowchart: vertical seven-step pathway with one decision diamond
PURPOSE: Turn the local operational advice into a pathway a Philippine hospital team can follow on day 0.
KEY CONCEPTS: day-0 serology; don't wait for send-outs; exchange route options; replacement fluids; transfer; HBV and TB screening; documentation for coverage

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. White background, restrained navy (#0f1e2e) and teal (#1a6b72) typography set in Inter (never a serif font), thin teal connector arrows, generous margins. Centered, symmetrical, portrait.
Title: "Anti-GBM disease in a Philippine hospital: day 0". Subtitle in teal: "Get standard care delivered fast".
Steps (rounded rectangles, top to bottom, each with an optional small flat line icon that does not touch the border):
1. Teal-outlined box: "Send anti-GBM AND ANCA on the same draw; ask the lab for urgent processing and the expected turnaround".
2. Amber (#b8860b) box: "Do not wait for a send-out result: start glucocorticoids; arrange plasma exchange".
3. Teal diamond: "Plasma exchange available here?" Branch "Yes" → teal box: "Choose the route: blood-bank apheresis, or a plasma filter on a hemodialysis or continuous kidney replacement machine". Branch "No" → amber box: "Transfer early, especially if oxygen need is rising".
4. Teal box: "Secure replacement fluid on day 0: albumin, plus fresh plasma around the biopsy and with lung bleeding".
5. Teal box: "Screen before immunosuppression: hepatitis B (surface antigen, core antibody); assess tuberculosis exposure".
6. Green (#1f7a4d) box: "Document indication, antibody results, and biopsy for PhilHealth, HMO, and social-service claims; involve the social worker on admission".
Soft gray side note box: "Estimate exchange volume with a plasma-volume calculator".
Consistent spacing and alignment, no clutter, no photos.
Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
No dark background, no brand names of machines or drugs, no peso amounts or invented coverage figures, no photos, no clutter, no serif fonts (Inter only), no AI gibberish text. Never omit the attribution.
```
QUALITY CHECK: one decision diamond only; no peso figures; "PhilHealth" spelled correctly; footer present.
ALT TEXT: "Day-0 pathway for Philippine hospitals: send anti-GBM and ANCA together, start treatment without waiting, choose an exchange route or transfer, secure fluids, screen for hepatitis B and tuberculosis, and document for coverage."
OG WIDTH: 1024 · OG HEIGHT: 1536

---

### 023 — Calculator share card

```
IMAGE NUMBER: 023
SECTION PLACEMENT: calc-anti-gbm-renal-risk.html og:image and twitter:image (replaces the borrowed guide OG)
FILE NAME: calc-anti-gbm-renal-risk-og.png
ARCHETYPE: OG / social share card
AUDIENCE: clinicians
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title block and mini bar strip
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Identify the calculator in link previews and show what it estimates.
KEY CONCEPTS: four-group 36-month kidney survival; dialysis and normal glomeruli

COPY-READY IMAGE GENERATOR GPT PROMPT:
Open Graph social share card, exactly 1200 × 630 px, clean clinical-tool aesthetic on an off-white (#fafafa) background. LEFT 55%: small teal (#1a6b72) Inter eyebrow text "CLINICAL CALCULATOR"; bold navy (#0f1e2e) Inter title on two lines: "Anti-GBM Kidney" and "Outcome Risk"; navy Inter subtitle: "36-month kidney survival from dialysis status and normal glomeruli".
RIGHT 45%: a clean mini bar chart of four vertical rounded bars on a light grid with value labels above each bar exactly "96%", "74%", "42%", "14%", colored green (#1f7a4d), teal (#1a6b72), amber (#b8860b), red (#b91c1c); small two-line labels under each bar: "No dialysis / ≥10% normal", "No dialysis / <10% normal", "Dialysis / ≥10% normal", "Dialysis / <10% normal". Bars proportional to the values.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text. No journal names, guideline acronyms, brand names, or other watermarks.

NEGATIVE INSTRUCTIONS:
Never change the 1200 × 630 size. Avoid dark backgrounds, altered values, 3D bars, clutter, tiny text, AI gibberish text, serif fonts (Inter only). Never omit the attribution.
```
QUALITY CHECK: exactly 1200×630; values 96/74/42/14 in that order and proportional; attribution present.
ALT TEXT: "Anti-GBM Kidney Outcome Risk calculator — renalcarematters.com"
OG WIDTH: 1200 · OG HEIGHT: 630

---

## 5. Optional Tagalog on-image text sets (for low-English-literacy readers)

Generate a second version of 008 and 013 for printed clinic handouts by replacing the quoted English labels with these Tagalog labels (keep everything else identical; file names end in `-tl.png`).

**008 Warning signs (`anti-gbm-disease-08-warning-signs-tl.png`)**
- Title: "Mga babala ng anti-GBM disease" · Subtitle: "Madalas nagsisimula na parang trangkaso o ubo, saka bumibilis"
- Cards: "Maitim, kulay-tsaa, cola, o pulang ihi" · "Mas kaunting ihi kaysa karaniwan" · "Namamagang mukha, binti, o bukung-bukong" · "Pag-ubo ng dugo" · "Hinihingal kapag nakahiga" · "Pagod, maputla, walang gana"
- Red banner: "Dugo sa ihi + pamamaga o kaunting ihi, o anumang pag-ubo ng dugo:" / "Pumunta sa emergency department NGAYON."
- Under banner: "Sabihin: Baka may pamamaga ang aking bato."

**013 Life after (`anti-gbm-disease-13-life-after-tl.png`)**
- Title: "Buhay pagkatapos ng anti-GBM disease" · Subtitle: "Karaniwang isang beses lang ito. Tumulong na manatiling ganoon."
- Cards: "Bawal manigarilyo o mag-vape" · "Iwasan ang usok ng gasolina, thinner, solvent" · "Huwag laktawan ang follow-up test" · "Kontrolin ang presyon ng dugo" · "Magtanong bago mag-ibuprofen o mefenamic acid" · "Magtanong bago gumamit ng herbal" · "Magtanong sa bakuna; planuhin ang pagbubuntis" · "Transplant pagkatapos ng 6 buwang walang antibody"

> Tagalog strings match the guide's TL translation (draft, pending native-speaker review).

---

## 6. Stage 2 wiring checklist (after images are generated)

1. Save each PNG to `images/` and create a `.webp` twin (quality 88).
2. **Replace in place (same file name, no HTML change):** 001 (hero), 022 (OG card), 002 (`-02-mechanism`), 003 (`-03-variant-map`), 004 (`-04-first-24-hours`).
3. **New figures to insert** (each as `<figure class="ag-fig">` with `<picture>`, `p.fig-desc` plain-language description, and `dl.fig-abbrevs` for any acronym on the image): 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017, 018, 019, 020, 021. In `#what-it-is`, swap the patient-section `-02-mechanism` figure for `-06-filter-mesh`. Patient figure descriptions need EN/TL/CEB/KAP spans.
4. Calculator: point `og:image` / `twitter:image` to `calc-anti-gbm-renal-risk-og.webp` (1200 × 630).
5. Keep `-05-kidney-survival` code-native (data figure; regenerate only from `make_figs.py`).
6. Re-run: `patch_image_lightbox.py`, `audit_acronym_expansion.py` (new figure abbreviations), `generate_latest_guides.py`; commit to `main`.
