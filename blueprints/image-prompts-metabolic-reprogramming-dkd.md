# Image Plan Blueprint — Metabolic Reprogramming in Diabetic Kidney Disease

**Guide:** `guides/metabolic-reprogramming-dkd.html` (live)
**Version:** 2.0 · 8 November 2026 (supersedes the v1 four-prompt pack)
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Skills used:** `williamriveromd-hero-vignette` (001) · `williamriveromd-infographic-skill` (002, 008, 009, 011, 017, 019, 020) · `williamriveromd-simple-figure` (003–007, 010, 016) · `williamriveromd-biomedical-mechanism-figure` (013–015) · `williamriveromd-organ-crosstalk-sigil-graphic` (012) · `williamriveromd-algorithm-generator-skill` (018) · Stage 2 schema from `williamriveromd-local-image-generator`
**Local folder (Stage 2):** `/Users/williamgregoryrivero/Downloads/metabolic-reprogramming-dkd/`

---

## Part A — Visual strategy

### A.1 The teaching problem images must solve

This guide asks readers to hold three abstract ideas: **fuel** (what kidney cells burn), **workload** (why diabetes overworks them), and **rust** (iron-driven damage to cell walls, called ferroptosis). It then asks them to keep two kinds of evidence apart: **proven outcomes** versus **laboratory mechanisms**. Text alone does this poorly for a reader with a grade-school education, and diagrams alone do it poorly for a specialist who wants precision. The plan therefore runs one visual metaphor through both tabs and then changes how detailed it gets.

| Layer | Patient tab (all reading levels) | Clinician tab (specialist precision) |
|---|---|---|
| Fuel | A busy **factory** with power plants burning clean fuel | Nephron fuel map: FAO, OXPHOS, glycolysis by segment |
| Workload | **Delivery trucks** piling sugar and salt at the gate | Two overlapping states: higher transport work, lost flexibility |
| Rust | **Rust on a gate** next to rust on a cell wall, with an "anti-rust crew" | Three-lane ferroptosis mechanism: substrate, oxidation, defense |
| Evidence | "Proven in people" badge vs. "seen in the lab" badge | Evidence ladder: outcome trials → surrogate trials → tissue → models |
| Action | Four shields around the kidney; Filipino plate; warning signs | Where each pillar acts; bedside algorithm; case; safety card |

The **visual grammar repeats** across images so a reader learns it once: amber-glowing mitochondria = healthy fuel use; rust-orange patches = ferroptosis; teal = protection/treatment; a small **flask icon** marks laboratory-only evidence and a small **people icon** marks human trial evidence.

### A.2 Readability rules applied to every patient image

1. One idea per image; a reader should get it in about 10 seconds on a phone.
2. On-image text is short English labels at about a grade 6 reading level. The guide's four-language captions (`fig-desc`) carry the explanation, so images need no Tagalog, Cebuano or Kapampangan text.
3. People shown are Filipino, varied in age, sex, body type and setting, and never look like the stock "smiling elder at a dining table."
4. Every laboratory-only idea carries a visible **"Seen in the lab"** tag so the picture never overstates the evidence.

### A.3 What must stay code-native (do not generate)

Images with exact numbers that clinicians will quote stay as the existing SVGs, because image generators garble digits:

- `metabolic-reprogramming-dkd-05-outcomes-forest.svg` (hazard ratios and CIs) — **keep, never regenerate**
- `metabolic-reprogramming-dkd-04-evidence-ladder.svg` — keep; prompt 016 adds a friendlier companion without numbers
- `metabolic-reprogramming-dkd-06-bedside-algorithm.svg` — keep as the source of truth; prompt 018 is an optional upgrade that **must be proofread number by number** before it replaces the SVG

Prompts 019 (case) and 020 (safety) contain a few numbers. Proofread each against the guide text before publishing.

### A.4 Image inventory and placement

| # | File (PNG + WebP twin) | Section | Audience | Skill / archetype | Size | Priority |
|---|---|---|---|---|---|---|
| 001 | `metabolic-reprogramming-dkd-vignette-hero` | Hero (patient) | Mixed | Hero vignette · Object Hero | 2048×2048 | **P1 — fixes current 404** |
| 002 | `metabolic-reprogramming-dkd-og` | `<head>` OG/Twitter | Mixed | OG card | 1200×630 | **P1** |
| 003 | `…-factory-engine-infographic` | `#p-engine` | Patients | Simple figure · single mechanism | 1792×1024 | P1 |
| 004 | `…-delivery-overload-infographic` | `#p-diabetes` | Patients | Simple figure · comparison | 1792×1024 | P1 |
| 005 | `…-rust-analogy-infographic` | `#p-rust` | Patients | Simple figure · comparison | 1792×1024 | P1 |
| 006 | `…-two-tests-infographic` | `#p-tests` | Patients | Simple figure · step sequence | 1792×1024 | P2 |
| 007 | `…-four-shields-infographic` | `#p-protect` | Patients | Simple figure · radial | 1024×1024 | P1 |
| 008 | `…-clinic-conversation-infographic` | `#p-protect` (above table) | Patients | Photoreal editorial scene | 1792×1024 | P2 |
| 009 | `…-filipino-plate-habits-infographic` | `#p-daily` | Patients | Food matrix | 1536×1152 | P1 |
| 010 | `…-supplement-myths-infographic` | `#p-daily` (beside amber alert) | Patients | Simple figure · comparison | 1536×1152 | P2 |
| 011 | `…-warning-signs-infographic` | `#p-warning` | Patients | Reference card | 1024×1536 | P1 |
| 012 | `…-fuel-crosstalk-sigil` | `#md-answer` | Clinicians | Organ crosstalk sigil | 1024×1024 | P3 |
| 013 | `…-nephron-fuel-map-infographic` | `#md-fuel` (replaces SVG 01 if accurate) | Clinicians | Biomedical mechanism | 1792×1024 | P2 |
| 014 | `…-flexibility-loss-infographic` | `#md-flex` (companion to SVG 02) | Clinicians | Biomedical mechanism | 1792×1024 | P3 |
| 015 | `…-ferroptosis-mechanism-infographic` | `#md-ferroptosis` (replaces SVG 03 if accurate) | Clinicians | Biomedical mechanism | 1792×1024 | P2 |
| 016 | `…-evidence-kinds-infographic` | `#md-studies` (above study cards) | Mixed | Simple figure · step sequence | 1792×1024 | P2 |
| 017 | `…-pillars-sites-infographic` | `#md-pillars` | Clinicians | Mechanism poster | 1792×1024 | P1 |
| 018 | `…-bedside-algorithm-infographic` | `#md-bedside` (optional SVG 06 upgrade) | Clinicians | Algorithm · house style C | 1024×1792 | P3 |
| 019 | `…-case-snapshot-infographic` | `#md-case` | Clinicians | Case snapshot | 1792×1024 | P2 |
| 020 | `…-sglt2-safety-card-infographic` | `#md-safety` | Clinicians | Reference card | 1536×1152 | P2 |

**Production order:** 001 → 002 → 003 → 004 → 005 → 007 → 009 → 011 → 017 → then P2 → P3.

### A.5 Consistency anchors (repeat in every relevant prompt)

- Background white `#ffffff` / off-white `#fafafa`; cards `#f3f4f6` or `#eef6f7`. Never dark.
- Navy `#0f1e2e` text · teal `#1a6b72` protection/headings · renal green `#1f7a4d` healthy/safe · amber `#b8860b` caution · clinical red `#b91c1c` danger · rust orange `#c55a11` ferroptosis · soft purple `#6c3d8e` "lab evidence."
- Font: **Inter** for every image with text (one face across the set).
- Attribution `renalcarematters.com`, small, semi-transparent navy, bottom-right (bottom-center on portrait).
- No journal names, guideline acronyms, trial names, or drug brand names on any image.

---

## Part B — Copy-ready prompts

> Paste the block under **COPY-READY IMAGE GENERATOR GPT PROMPT** into the GPT. The negative instructions and quality check are part of the paste unless noted.

---

### 001 — Hero vignette

IMAGE NUMBER: 001
SECTION PLACEMENT: Hero, `figure.hero-figure.mode-patient > .hero-vignette` (already wired; currently returns 404)
FILE NAME: metabolic-reprogramming-dkd-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 — Scaffold C anatomy · Composition I (Object Hero) · camera: macro three-quarter from slightly above
AUDIENCE: Mixed
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX:
- photorealistic models: none (no people; the previous guide's hero was an object illustration, and this one is a cellular render)
- 2D infographic: none
- 3D component graphics: one tubule cell cutaway
- algorithm/flowchart: none
PURPOSE: In one glance, show "clean fuel inside, early rust outside" so the title reads as a story, not jargon.
KEY CONCEPTS: Mitochondria as engines; membrane "rust" (ferroptosis); calm, not frightening.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition: one object hero. Camera: macro three-quarter view from slightly above.

Subject: a single cuboidal kidney proximal tubule cell, cut away on one side to reveal its interior, resting on a soft, uncluttered light teal-tinted background. Inside, elongated mitochondria with visible inner folds glow a warm amber, suggesting clean fuel burning; a few small pale-yellow fat droplets sit near them. A fine brush border of microvilli faces the upper left. Along the lower-right curve of the outer cell membrane, three or four small, irregular rust-orange patches spread like early corrosion on metal — subtle, never gory. Restrained clinical color: soft ivory cytoplasm, renal pink, teal accents (#1a6b72), amber mitochondria, rust patches in muted orange (#c55a11). Gentle studio lighting with a soft shadow beneath the cell.

Visual hierarchy: the cell occupies 60–70% of the circle, centered slightly right and low; two or three supporting cues (a faint capillary edge behind the cell, a few fat droplets drifting in from the left) take 20–30%; reserve a 20–25% TITLE SAFE ZONE of empty soft teal gradient in the upper-left of the circle with no anatomy, droplets, labels or callouts. Soft falloff toward a slightly deeper neutral at the rim.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders.
```
NEGATIVE INSTRUCTIONS: busy layouts; collage; more than four supporting elements; icons; labels; cropped circle; cropped cell; objects touching the circular border; content inside the title safe zone; baked-in text, logos or watermarks; rectangular frames; dark, charcoal or black backgrounds; cartoon style, neon, HDR, over-saturation; blood, gore, or a "dying cell" horror look; implausible anatomy.
QUALITY CHECK: Square 2048×2048; circle 85–90% of canvas with a visible white margin; one dominant cell (60–70%); empty upper-left title zone; mitochondria read as "clean engine," membrane patches as "early rust" (not infection or blood); wordless.
ALT TEXT: Three-dimensional illustration of a kidney tubule cell with glowing mitochondria inside and a few rust-colored patches on its outer membrane, representing healthy fuel use and early ferroptosis.
OG WIDTH: 2048
OG HEIGHT: 2048

---

### 002 — Open Graph share card

IMAGE NUMBER: 002
SECTION PLACEMENT: `<head>` — `og:image` (webp) and `twitter:image` (png); already wired
FILE NAME: metabolic-reprogramming-dkd-og.png
ARCHETYPE: OG / social share card
AUDIENCE: Mixed (Facebook, Messenger, Viber previews)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title block
- 3D component graphics: the hero cell, smaller
- algorithm/flowchart: none
PURPOSE: Make the link preview readable and inviting for patients scrolling Facebook while still signaling scientific depth to clinicians.
KEY CONCEPTS: Fuel to rust; "what the science shows and what helps."

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean editorial social-share card, exactly 1200×630 pixels, white (#ffffff) background with a very soft light-teal (#eef6f7) panel filling the left 55%. All text in Inter.
Left side, stacked and left-aligned with generous margins:
  Small teal (#1a6b72) uppercase label: "DIABETES & YOUR KIDNEYS"
  Bold navy (#0f1e2e) title, two lines, large: "When Diabetes Changes How Your Kidneys Burn Fuel"
  Medium rust-orange (#c55a11) subtitle: "From fuel selection to ferroptosis"
  Small navy line at 80% opacity: "What the science shows — and what actually protects the kidney"
Right side: a semi-photorealistic 3D cutaway of one kidney tubule cell with warm amber glowing mitochondria inside and two or three small rust-orange patches on its outer membrane, floating on soft light with a gentle shadow, matching a calm medical-illustration style.
Bottom-right corner: small semi-transparent navy text "renalcarematters.com".
Spell every word exactly as given. Generous whitespace. No other logos, no other text.
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: dark backgrounds of any kind; serif or decorative fonts (Inter only); misspelled or extra words; cluttered icons; neon; cartoon style; text crossing the cell; cropping of the title.
QUALITY CHECK: Exactly 1200×630; title readable at 600 px wide; all words spelled as given; cell matches 001; attribution visible bottom-right.
ALT TEXT: Share card titled "When Diabetes Changes How Your Kidneys Burn Fuel," with an illustrated kidney cell showing glowing mitochondria and early rust spots.
OG WIDTH: 1200
OG HEIGHT: 630

---

### 003 — The factory engine (patient)

IMAGE NUMBER: 003
SECTION PLACEMENT: `#p-engine`, after the first paragraph (the existing SVG 07 can move to `#p-diabetes` or be retired)
FILE NAME: metabolic-reprogramming-dkd-factory-engine-infographic.png
ARCHETYPE: Simple figure — Scaffold D single mechanism, three-step zoom
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: zoom panels, labels
- 3D component graphics: kidney, nephron, tubule cell
- algorithm/flowchart: none
PURPOSE: Give readers the mental model that the kidney is a working factory powered by fat-burning engines, before diabetes is mentioned.
KEY CONCEPTS: Filter, then take back salt, sugar and water; that takes energy; mitochondria burn fat.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Medical education infographic for patients, clean graphical-abstract style. White (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter font: "Your kidney is a busy factory". Subtitle in teal (#1a6b72): "It works hard to take back what your body needs".
Three panels from left to right, joined by thin dashed zoom lines:
Panel 1: a calm semi-photorealistic 3D human kidney, soft renal pink, label "Kidney".
Panel 2: one filtering unit (a small ball-shaped filter followed by a long coiled tube), the coiled tube highlighted in soft yellow, label "Filter + recycling tube".
Panel 3: a large cutaway of one tube cell. Inside, amber-glowing mitochondria drawn like small power plants with tiny fat droplets flowing into them. Small curved arrows show salt, sugar and water being carried back into a blood vessel at the cell's base. Labels: "Power plants (mitochondria)", "Main fuel: fat", "Takes back salt, sugar and water".
Bottom strip, soft gray (#f3f4f6), one sentence in navy: "Taking things back costs energy — so these cells need a steady, clean fuel supply."
Large readable labels, generous whitespace, calm colors, teal and amber accents.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, HDR, heavy saturation. Never use dark, navy, charcoal or black backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Readable on a phone; three panels clearly zoom from organ to cell; labels spelled exactly; fat shown as the fuel; light background; attribution bottom-right.
ALT TEXT: Three-step zoom from a kidney to a filtering unit to one tubule cell whose mitochondria burn fat to power the recycling of salt, sugar and water.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 004 — Delivery overload (patient)

IMAGE NUMBER: 004
SECTION PLACEMENT: `#p-diabetes`, after the paragraph
FILE NAME: metabolic-reprogramming-dkd-delivery-overload-infographic.png
ARCHETYPE: Simple figure — Scaffold B side-by-side comparison
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: comparison panels, simple delivery-truck icons
- 3D component graphics: two tubule cells
- algorithm/flowchart: none
PURPOSE: Turn "metabolic reprogramming" into something a reader can picture: too many deliveries, overtime, wrong fuel mix, fat piling up.
KEY CONCEPTS: High sugar → more sugar and salt delivered → overtime → fat-burning slows → fat piles up.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient education comparison infographic, clean graphical-abstract style. White (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter font: "What years of high blood sugar do to the factory". Soft dashed vertical divider splits the canvas into two equal panels with rounded corners.
LEFT panel, header in renal green (#1f7a4d): "Normal day". A semi-3D kidney tube cell with two small delivery trucks at its gate unloading a modest pile of sugar cubes and salt crystals. Inside, three amber-glowing mitochondria burning small fat droplets steadily. Labels: "Normal deliveries", "Fat burned cleanly".
RIGHT panel, header in amber (#b8860b): "Years of high sugar". The same cell with six delivery trucks crowding the gate and a large pile of sugar cubes and salt crystals. Inside, mitochondria look dimmer and slightly swollen; unused pale-yellow fat droplets pile up in the corners; a small clock icon shows overtime. Labels: "Too many deliveries", "Working overtime", "Fat piles up unused".
Bottom strip, soft gray (#f3f4f6), navy text: "Scientists call this shift metabolic reprogramming. It does not happen the same way in everyone."
Large readable labels, generous whitespace, calm colors; trucks are simple flat icons, not cartoons.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid cartoon faces on cells or trucks, clutter, tiny labels, AI gibberish text, gore, HDR. Never use dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Difference between panels is obvious in two seconds; fat accumulation visible on the right; no frightening imagery; labels exact.
ALT TEXT: Side-by-side cells: on a normal day a few deliveries arrive and fat burns cleanly; after years of high sugar, many deliveries crowd the cell, it works overtime, and unused fat piles up.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 005 — Rust analogy (patient)

IMAGE NUMBER: 005
SECTION PLACEMENT: `#p-rust`, after the first paragraph, before the purple honesty alert
FILE NAME: metabolic-reprogramming-dkd-rust-analogy-infographic.png
ARCHETYPE: Simple figure — Scaffold B comparison (analogy ↔ biology)
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: a photoreal rusting iron gate (no people)
- 2D infographic: labels, "lab" tag
- 3D component graphics: cell membrane close-up
- algorithm/flowchart: none
PURPOSE: Make ferroptosis memorable through a familiar Philippine image (a rusting gate in the rainy season) and show the "anti-rust crew" that normally protects the cell, while labeling it as laboratory knowledge.
KEY CONCEPTS: Iron + delicate fats + stress = chain reaction; glutathione and GPX4 stop it; if the crew runs out, the wall fails.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient education analogy infographic, clean graphical-abstract style. White (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter font: "Ferroptosis: when cell walls rust". Two panels with rounded corners separated by a soft dashed divider.
LEFT panel, header in teal (#1a6b72): "Rust on a gate". A photorealistic close-up of a painted metal gate of a Filipino home after the rainy season, light green paint with rust spreading from one bolt in an orange bloom. Bright daylight, clean background. Label: "Iron + water + air = rust that spreads".
RIGHT panel, header in rust orange (#c55a11): "Rust on a cell wall". A semi-3D close-up of a curved cell membrane made of small rounded lipid beads. Small iron spark icons touch a few beads that turn rust-orange, and the color spreads to neighbors like a chain. Below the membrane, three small friendly teal shield icons labeled "Anti-rust crew" stop part of the spread; a short label under them reads "Glutathione + GPX4". Labels: "Iron + delicate fats", "Chain reaction", "Crew runs short → wall breaks".
Top-right corner of the right panel: a small soft-purple (#6c3d8e) pill tag with a flask icon: "Seen in the lab".
Bottom strip, soft gray (#f3f4f6), navy text: "Doctors cannot yet measure this in patients, and no rust-blocking medicine is approved."
Large readable labels, generous whitespace.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid gore, blood, horror, cartoon faces, clutter, tiny labels, AI gibberish text, HDR. Never use dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Gate and membrane visually rhyme (same orange spread); "Seen in the lab" tag clearly visible; bottom sentence spelled exactly; light background.
ALT TEXT: A rusting metal gate beside a cell wall where iron and delicate fats start a rust-like chain reaction, with an anti-rust crew of glutathione and GPX4 holding part of it back; tagged as seen in the lab.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 006 — Your two tests (patient)

IMAGE NUMBER: 006
SECTION PLACEMENT: `#p-tests`, between the two paragraphs
FILE NAME: metabolic-reprogramming-dkd-two-tests-infographic.png
ARCHETYPE: Simple figure — Scaffold C horizontal sequence (two test cards + a timeline)
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: cards, timeline
- 3D component graphics: urine cup, small filter/sieve
- algorithm/flowchart: simple timeline
PURPOSE: Show what each test measures and set expectations: albumin falls within weeks; eGFR may dip slightly at first, and that dip is usually expected.
KEY CONCEPTS: UACR = the leak; eGFR = how much filtering; repeat tests; early small dip.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean patient education infographic, white (#ffffff) background. Title at top center in bold navy (#0f1e2e), Inter font: "The two tests that guide your treatment".
Upper half: two large rounded cards side by side on a soft gray (#f3f4f6) panel.
Card 1, teal (#1a6b72) top band, title "Urine albumin (UACR)": a 3D sieve with a few small protein drops slipping through into a urine cup. Short label: "How much protein leaks through the filter". Small note: "Repeat it — one test can be off".
Card 2, navy top band, title "eGFR (blood test)": a simple semicircular gauge from slow to fast with the needle in the middle zone. Short label: "How much filtering your kidneys do".
Lower half: a horizontal timeline with three markers labeled "Start medicine", "2–4 weeks", "Months to years".
Above the timeline, a teal line labeled "Urine albumin" drops early, in the first weeks.
Below the timeline, a navy line labeled "eGFR" dips slightly right after the start (small dip marked with an amber note "Small early dip — usually expected"), then runs flatter over time.
At the "2–4 weeks" marker, a small icon of a blood tube with the label "Check potassium and creatinine".
Large readable labels, generous whitespace, calm colors.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid numbers on the gauge or curves, clutter, tiny labels, AI gibberish text, cartoon style. Never use dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: No numeric axes; the albumin line drops early; the eGFR dip is small and labeled as expected; labels exact.
ALT TEXT: Two cards explain the urine albumin test as a filter leak and eGFR as filtering speed, above a timeline where albumin falls within weeks and eGFR dips slightly at first, with potassium and creatinine checked at two to four weeks.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 007 — Four shields (patient)

IMAGE NUMBER: 007
SECTION PLACEMENT: `#p-protect`, after the opening paragraph, before the medicine table
FILE NAME: metabolic-reprogramming-dkd-four-shields-infographic.png
ARCHETYPE: Simple figure — square radial (circular-workflow layout without a cycle)
AUDIENCE: Patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: four shield cards
- 3D component graphics: central kidney
- algorithm/flowchart: none
PURPOSE: Show the four proven medicine groups as complementary shields, each easing a different part of the workload, with a "proven in people" marker.
KEY CONCEPTS: ACE inhibitor/ARB, SGLT2 inhibitor, finerenone, GLP-1 medicine; not everyone needs all four.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Square patient education infographic, 1024×1024, white (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter font: "Four kinds of medicine that protect the kidney".
Center: a calm semi-photorealistic 3D kidney in soft renal pink.
Around it, four rounded shield-shaped cards at the corners, each in teal (#1a6b72) outline with a small icon and two short lines of text:
Top-left: "ACE inhibitor or ARB" — "Lowers pressure inside the filters" (icon: a gauge)
Top-right: "SGLT2 inhibitor" — "Fewer sugar and salt loads" (icon: a drop with a downward arrow)
Bottom-left: "Finerenone" — "Calms swelling and scarring signals" (icon: a calm wave)
Bottom-right: "GLP-1 medicine" — "Helps weight, sugar and blood vessels" (icon: a blood vessel)
Thin teal lines connect each shield to the kidney.
Under the title, a small renal-green (#1f7a4d) pill badge with a people icon: "Proven in large studies of people".
Footer line in navy: "Not everyone needs all four. Your doctor checks potassium and kidney tests."
Large readable labels, generous whitespace.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No pill brand names or packaging, no cartoon kidney faces, no clutter, no tiny labels, no AI gibberish text. Never use dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Four shields equally weighted; drug-class names spelled exactly; green "proven" badge present; footer present.
ALT TEXT: A kidney surrounded by four shields: ACE inhibitor or ARB, SGLT2 inhibitor, finerenone, and GLP-1 medicine, each easing a different part of the kidney's workload.
OG WIDTH: 1024
OG HEIGHT: 1024

---

### 008 — Clinic conversation (patient, photoreal)

IMAGE NUMBER: 008
SECTION PLACEMENT: `#p-protect`, after the final paragraph about starting medicines together
FILE NAME: metabolic-reprogramming-dkd-clinic-conversation-infographic.png
ARCHETYPE: Photorealistic editorial scene
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: Filipino patient, adult son, nephrologist
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Add warmth and trust: treatment decisions are a conversation using lab results, not a lecture.
KEY CONCEPTS: Shared decision-making; follow-up labs; family involvement.
HUMAN VARIATION: Patient is a woman in her early 50s, broad build, short permed salt-and-pepper hair, rectangular reading glasses, deep olive skin, wearing a mustard-yellow cardigan over a white blouse; her adult son in his 20s, slim, buzz cut, gray polo; the nephrologist is a woman in her late 30s, slim, straight shoulder-length black hair tied back, light-brown skin, white coat over a navy top. Setting: a bright outpatient clinic in Quezon City with a window and potted plant. Camera: over-the-shoulder from behind the physician toward the patient.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Photorealistic healthcare editorial photograph, 16:9, bright and airy. A Filipino nephrologist in her late 30s (slim, light-brown skin, straight shoulder-length black hair tied back, white coat over a navy top) sits across a small desk from a Filipino woman in her early 50s with type 2 diabetes (broad build, short permed salt-and-pepper hair, rectangular reading glasses, deep olive skin, mustard-yellow cardigan over a white blouse). The patient's adult son in his 20s (slim, buzz cut, gray polo shirt) sits beside her, leaning in. Camera is over the physician's shoulder, focused on the patient's face. The physician points with a pen to a printed lab sheet showing a simple downward trend line; a weekly pill organizer and a glass of water sit on the desk. Expressions: attentive, reassured, engaged. Setting: modern, clean outpatient clinic with soft daylight from a window, a small potted plant, light walls. Natural skin texture, shallow depth of field, calm teal and navy accents in the décor. The lab sheet has no readable text or numbers. No embedded text anywhere except a small semi-transparent navy "renalcarematters.com" in the bottom-right corner.
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid stock-photo look, smiling-at-camera poses, elderly couple at dining table, identical teal polo, readable labels on pill packs, dark or moody lighting, HDR, distorted hands or faces. Never use dark backgrounds. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Three distinct, natural-looking Filipino people; no readable brand or lab text; bright clinic; attribution visible.
ALT TEXT: A nephrologist reviews a simple lab trend with a woman who has type 2 diabetes and her adult son in a bright clinic, with a pill organizer on the desk.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 009 — Filipino plate and daily habits (patient)

IMAGE NUMBER: 009
SECTION PLACEMENT: `#p-daily`, after the first paragraph
FILE NAME: metabolic-reprogramming-dkd-filipino-plate-habits-infographic.png
ARCHETYPE: Food matrix / nutrition infographic
AUDIENCE: Patients and families
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none (food photography only)
- 2D infographic: matrix cards, icons
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Translate "steady blood sugar means fewer deliveries" into local, doable swaps.
KEY CONCEPTS: Rice portion, sugary drinks, processed and fried food, walking, sleep, no protein loading without advice.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean patient nutrition and lifestyle infographic, 4:3, white (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter font: "Fewer sugar deliveries: small daily swaps".
Top row: three "swap" cards with a soft gray (#f3f4f6) fill, each showing a realistic food photo on the left, a teal arrow, and a better choice on the right:
1. "A heaping mound of white rice" → "Half cup rice or part brown rice" (realistic Filipino plate with smaller rice portion, steamed fish, ginisang gulay)
2. "Soft drink, sweet iced tea, 3-in-1 coffee" → "Water or unsweetened drinks" (realistic glasses, no brand labels)
3. "Fried and processed meat (hotdog, longganisa)" → "Grilled or steamed fish or chicken"
Bottom row: three habit cards with simple teal line icons:
4. "Walk most days" (walking shoes icon)
5. "Sleep 7–8 hours" (moon icon)
6. "Ask before a high-protein diet" (amber caution icon, amber card border #b8860b)
Footer line in navy: "Steady sugar means less overtime for kidney cells."
Realistic, appetizing food photography with natural daylight; generous whitespace; large labels.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No brand logos on drinks or packages; avoid cluttered food piles; no tiny text; no AI gibberish; no dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Filipino foods are recognizable; swaps read left-to-right; no brands; footer exact.
ALT TEXT: Six cards of daily swaps: smaller rice portions, water instead of sweet drinks, grilled fish instead of processed meat, walking, enough sleep, and asking before a high-protein diet.
OG WIDTH: 1536
OG HEIGHT: 1152

---

### 010 — Supplement myths (patient)

IMAGE NUMBER: 010
SECTION PLACEMENT: `#p-daily`, immediately after the amber "Skip the anti-rust pills and herbs" alert
FILE NAME: metabolic-reprogramming-dkd-supplement-myths-infographic.png
ARCHETYPE: Simple figure — Scaffold B comparison (myth vs. what studies show)
AUDIENCE: Patients and families
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none
- 2D infographic: myth/fact rows
- 3D component graphics: unbranded capsule bottle, herb sprigs, iron tablet
- algorithm/flowchart: none
PURPOSE: Counter social-media claims kindly and clearly, and protect prescribed iron therapy.
KEY CONCEPTS: Anti-rust supplements unproven; one human study showed no benefit; some herbs harm the kidney and liver; keep prescribed iron.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient education myth-versus-fact infographic, 4:3, white (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter font: "Heard it online? Check before you buy". Three horizontal rows, each split into two rounded cards: left card with an amber (#b8860b) "You may hear" label, right card with a renal-green (#1f7a4d) "What studies show" label.
Row 1: left — an unbranded supplement bottle with capsules, text "Antioxidant pills stop kidney rust". Right — text "Only animal studies so far. A study in people with kidney disease found no gain."
Row 2: left — fresh herb sprigs in a small bowl, text "Herbal kidney detox is safe because it is natural". Right — red (#b91c1c) small warning icon, text "Some herbs can harm the liver and kidneys."
Row 3: left — a single iron tablet, text "Iron causes rust, so stop iron". Right — text "Keep iron your doctor prescribed. Treating low iron is still standard care."
Footer line in navy: "Bring any supplement to your next kidney visit."
Large readable labels, generous whitespace, unbranded objects.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No product brands or readable labels, no mocking tone, no skull or poison icons, no clutter, no tiny text, no dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Tone is respectful; every sentence spelled exactly; iron row clearly says keep prescribed iron.
ALT TEXT: Three myth-versus-fact rows: antioxidant pills are unproven in people, some herbal detox products can harm the liver and kidneys, and prescribed iron should not be stopped.
OG WIDTH: 1536
OG HEIGHT: 1152

---

### 011 — Warning signs card (patient)

IMAGE NUMBER: 011
SECTION PLACEMENT: `#p-warning`, after the red alert
FILE NAME: metabolic-reprogramming-dkd-warning-signs-infographic.png
ARCHETYPE: Clinician-style reference card adapted for patients (portrait, printable)
AUDIENCE: Patients and families
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three symptom blocks, action bar
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: A screenshot-and-save card families can keep on a phone or refrigerator.
KEY CONCEPTS: Ketoacidosis signs even with near-normal sugar; high potassium signs; low fluid and fainting; sick-day and surgery rule.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Portrait patient safety reference card, 1024×1536, white (#ffffff) background. Title at top in bold clinical red (#b91c1c), Inter font: "Get help the same day if…".
Three stacked rounded cards with simple line icons and large text:
Card 1, red left border: "On an SGLT2 inhibitor" — "Nausea or vomiting · belly pain · fast or deep breathing · unusual sleepiness" — small note "Even if your sugar looks normal".
Card 2, amber (#b8860b) left border: "Possible high potassium" — "Muscle weakness · pounding or irregular heartbeat".
Card 3, amber left border: "Too little fluid" — "Fainting · very little urine · vomiting or diarrhea that stops you eating or drinking".
Below the cards, a soft teal (#eef6f7) box with a calendar icon: "Can't eat or drink? Ask your doctor which medicines to pause. Planning surgery? Tell your surgeon you take an SGLT2 inhibitor, days before."
Bottom bar in red outline with a phone icon: "Go to the emergency room or call your doctor now".
Very large readable text, generous spacing, simple flat line icons.
Bottom-center: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No graphic body imagery, no cartoon faces, no tiny text, no AI gibberish, no dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Readable as a phone screenshot; red reserved for emergency; text spelled exactly; attribution bottom-center.
ALT TEXT: Printable card of same-day warning signs: ketoacidosis symptoms on an SGLT2 inhibitor even with normal sugar, signs of high potassium, and signs of too little fluid, with sick-day and surgery advice.
OG WIDTH: 1024
OG HEIGHT: 1536

---

### 012 — Fuel crosstalk sigil (clinician)

IMAGE NUMBER: 012
SECTION PLACEMENT: `#md-answer`, after the first paragraph
FILE NAME: metabolic-reprogramming-dkd-fuel-crosstalk-sigil.png
ARCHETYPE: Organ crosstalk sigil (labels requested)
AUDIENCE: Clinicians (also legible to patients)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: monoline organ icons
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Frame DKD as a whole-body fuel problem before zooming into the nephron.
KEY CONCEPTS: Adipose fatty acids, hepatic ketones and glucose, pancreatic insulin and hyperglycemia, muscle uptake, all converging on the kidney.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Simple medical organ-crosstalk sigil illustration, square 1024×1024, white background. Minimal clinical line-art, thin monoline strokes, soft teal-blue palette with a single warm amber accent, clean rounded organ shapes, balanced radial composition, generous whitespace, no photorealism, no 3D.
Place a pair of kidneys at the center. Around them, four smaller organ icons evenly spaced: liver (top-left), pancreas (top-right), skeletal muscle (bottom-left), and a cluster of fat cells (bottom-right). Dotted curved arrows flow from each organ toward the kidneys, and one dotted arrow from the kidneys returns toward the liver, forming a gentle loop.
Small labels in Inter, slate gray, beside each arrow: liver → "glucose, ketones"; pancreas → "insulin, high glucose"; fat cells → "fatty acids"; muscle → "glucose uptake"; kidneys → liver return arrow "glucose made by kidney". A small amber label under the kidneys: "Fuel arrives faster than it can be used cleanly".
Calm, symbolic, publication-grade medical icon aesthetic.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid photorealistic anatomy, surgical detail, crowded arrows, thick cartoon outlines, 3D, glossy icons, dark backgrounds, neon. Use only Inter for labels. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Kidneys clearly central; five short labels spelled exactly; balanced whitespace.
ALT TEXT: Line-art sigil of the liver, pancreas, muscle and fat cells sending glucose, ketones, insulin signals and fatty acids toward the kidneys, which return glucose to the circulation.
OG WIDTH: 1024
OG HEIGHT: 1024

---

### 013 — Nephron fuel map (clinician)

IMAGE NUMBER: 013
SECTION PLACEMENT: `#md-fuel` — replaces SVG 01 only if every label renders correctly; otherwise keep SVG 01 and skip
FILE NAME: metabolic-reprogramming-dkd-nephron-fuel-map-infographic.png
ARCHETYPE: Biomedical mechanism figure (organ panel → magnified nephron → summary flow)
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: callouts
- 3D component graphics: soft semi-3D nephron
- algorithm/flowchart: bottom flow
PURPOSE: Segment-specific fuel dependence without numbers, separating transport from oxidation.
KEY CONCEPTS: PT FAO/OXPHOS and gluconeogenesis; SGLT2/SGLT1 transport ≠ oxidation; TAL ATP demand with low outer-medullary oxygen; podocytes mixed.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a publication-grade biomedical mechanism schematic in a scientific review-article style. Font: Inter for all labels. White background, flat vector illustration with soft semi-3D shading, muted clinical palette, thin dashed connector lines, generous whitespace.
Topic: fuel use along the nephron in diabetic kidney disease.
Left organ-level panel: a simplified kidney cross-section in light gray-blue with cortex and medulla shaded, labeled "Diabetic kidney disease". A small dashed box on the cortex connects to the main panel.
Center/right magnified panel inside a dashed border: one nephron spanning cortex, outer medulla and inner medulla bands (outer medulla shaded slightly darker and labeled "low oxygen reserve"). Highlight the proximal tubule in soft yellow, the thick ascending limb in pale orange, and the glomerulus in pale pink. Callouts:
  Proximal tubule: "Fatty acid oxidation → OXPHOS → ATP", "Na⁺/K⁺-ATPase transport", "Gluconeogenesis", "SGLT2 / SGLT1 = glucose transport, not burning"
  Thick ascending limb: "High ATP demand", "Little oxygen margin"
  Glomerulus / podocyte: "Glycolysis + mitochondria", "Barrier against albumin leak"
Bottom summary flow:
  Left pale-pink box: "Diabetes: more filtered glucose and sodium · more transport work"
  Center box: "Injured tubules: ↓ oxidative capacity · glycolytic and lipid-handling shifts"
  Right pale-blue box: "Labels vary by cell state, disease stage and model"
Bottom-right: small semi-transparent navy text "© renalcarematters.com".
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, and any numeric values. No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No numbers, no invented pathways, no serif fonts, no dark backgrounds, no gibberish labels.
QUALITY CHECK: Proofread every label against SVG 01; anatomy order glomerulus → PT → loop → TAL → distal → collecting duct is plausible; no numbers.
ALT TEXT: Mechanism figure of a nephron showing the proximal tubule relying on fatty acid oxidation for transport, the thick ascending limb with high energy demand and low oxygen reserve, and podocytes using mixed pathways, with a summary of changes in diabetes.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 014 — Loss of metabolic flexibility (clinician)

IMAGE NUMBER: 014
SECTION PLACEMENT: `#md-flex`, immediately after SVG 02 as a visual companion (or replace SVG 02 if clearer)
FILE NAME: metabolic-reprogramming-dkd-flexibility-loss-infographic.png
ARCHETYPE: Biomedical mechanism figure (two-cell comparison + flow)
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: callouts, measurement-type chips
- 3D component graphics: two PT cells
- algorithm/flowchart: overlap box
PURPOSE: Show substrate pressure and lost oxidative capacity as overlapping states, labeled by the kind of measurement.
KEY CONCEPTS: CPT1 entry, β-oxidation, PPARα/PGC-1α; lipid droplets; mTORC1↑ AMPK↓; flux vs. gene expression vs. metabolite pool.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a publication-grade biomedical mechanism schematic, review-article style, Inter font, white background, flat vector with soft semi-3D shading, muted clinical palette, thin dashed connectors.
Topic: from higher transport work to loss of metabolic flexibility in the diabetic proximal tubule.
Left cell (teal outline, title "Higher workload state"): apical SGLT2 with thick arrows of glucose and Na⁺ entering; basolateral Na⁺/K⁺-ATPase; fatty acids entering mitochondria through "CPT1" → "β-oxidation" → "TCA" → "OXPHOS"; label "More substrate flux (mouse tracer data)" with a small chip "flux".
Right cell (muted red outline, title "Reduced flexibility state"): swollen mitochondria with fewer cristae, several pale-yellow lipid droplets, label "↓ PPARα / PGC-1α program (human fibrotic tubules)" with a chip "gene expression"; label "↑ glycolytic activity"; label "↑ mTORC1 · ↓ AMPK · ↓ autophagy".
Between the cells: a purple dashed box titled "States overlap — not a fixed timeline" with a circular two-arrow loop labeled "mitochondrial injury ⇄ lower oxidative capacity".
Bottom summary flow: left pale-pink box "Acylcarnitines can reflect entry, incomplete oxidation or clearance" → center box "Lipid droplets may buffer fatty acids; oxidizable membrane lipids feed ferroptosis" → right pale-blue box "Flux, gene expression and metabolite pools answer different questions".
Bottom-right: small semi-transparent navy text "© renalcarematters.com".
No numbers. No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid photorealism, dark backgrounds, overcrowding, invented pathways, serif fonts, garbled abbreviations.
QUALITY CHECK: Abbreviations (CPT1, TCA, OXPHOS, PPARα, PGC-1α, mTORC1, AMPK) spelled exactly; measurement chips present; overlap box between cells.
ALT TEXT: Two proximal tubule cells: one in a higher-workload state with more glucose, sodium and fatty acid flux, and one with reduced flexibility, swollen mitochondria, lipid droplets and lower oxidation genes, joined by an overlap loop between mitochondrial injury and lower oxidative capacity.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 015 — Ferroptosis mechanism (clinician)

IMAGE NUMBER: 015
SECTION PLACEMENT: `#md-ferroptosis` — replaces SVG 03 only if labels are exact; otherwise place after the purple evidence box as a companion
FILE NAME: metabolic-reprogramming-dkd-ferroptosis-mechanism-infographic.png
ARCHETYPE: Biomedical mechanism figure
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: lanes and callouts
- 3D component graphics: PT cell and membrane close-up
- algorithm/flowchart: bottom flow
PURPOSE: Visual anchor for the three-lane model with the experimental caveat built in.
KEY CONCEPTS: ACSL4/LPCAT3 → PUFA-PL; Fe²⁺ + radicals → PL-OOH; SLC7A11 → GSH → GPX4 → PL-OH; FSP1–CoQ; upstream stresses.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a publication-grade biomedical mechanism schematic, review-article style, Inter font, white background, flat vector with soft semi-3D shading, muted clinical palette, thin dashed connector lines.
Topic: ferroptosis in the diabetic proximal tubule (experimental evidence).
Left organ-level panel: simplified kidney cross-section labeled "Diabetic kidney disease", with a small dashed connector to a proximal tubule segment highlighted in soft yellow.
Center/right magnified panel inside a dashed border: one proximal tubule cell with an enlarged membrane strip along its top edge.
  Substrate (orange callout): "ACSL4 + LPCAT3 → PUFA in membrane phospholipids"
  Oxidation (red callout): small spark icons at the membrane, "Fe²⁺ + radicals → PL-OOH spreads"; mitochondria labeled "↑ ROS"
  Defense (blue track along the base): "SLC7A11 (cystine in) → GSH → GPX4 → PL-OH"
  Parallel dashed blue track: "FSP1–CoQ"
Bottom summary flow:
  Left pale-pink box: "Upstream stresses: substrate overload · ↑ ROS · impaired autophagy / ↓ AMPK · TGF-β1"
  Center box: "Phospholipid peroxidation outpaces repair"
  Right pale-blue box: "Membrane failure → tubular cell death (animal and cell studies)"
Small gray footnote under the flow: "Mechanism from laboratory models; not a validated clinical test."
Bottom-right: small semi-transparent navy text "© renalcarematters.com".
No numbers. No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid photorealism, gore, dark backgrounds, overcrowding, serif fonts, and any arrow from GPX4 to FSP1 (they act in parallel).
QUALITY CHECK: FSP1–CoQ shown parallel, not downstream; all abbreviations exact; laboratory caveat present.
ALT TEXT: Mechanism figure of ferroptosis in a kidney tubule cell: ACSL4 and LPCAT3 load polyunsaturated fats into the membrane, iron and radicals spread lipid peroxides, and SLC7A11, glutathione and GPX4 with a parallel FSP1–CoQ track defend it; based on laboratory models.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 016 — Kinds of evidence (mixed)

IMAGE NUMBER: 016
SECTION PLACEMENT: `#md-studies`, after the first paragraph (keeps SVG 04 lower in the section)
FILE NAME: metabolic-reprogramming-dkd-evidence-kinds-infographic.png
ARCHETYPE: Simple figure — Scaffold C horizontal step sequence (4 cards)
AUDIENCE: Mixed (clinicians, students, health-literate patients)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: cards and icons matching the guide's badge colors
- 3D component graphics: small objects (cell dish, mouse, slide, people group)
- algorithm/flowchart: left-to-right arrow of rising certainty
PURPOSE: Teach readers of any level to tell "seen in a dish" from "proven in people," matching the guide's evidence badges.
KEY CONCEPTS: Cells, animals, human tissue, randomized trials; only trials change prescribing.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean clinical education infographic, white (#ffffff) background. Title at top center in bold navy (#0f1e2e), Inter font: "Not all evidence is the same". Subtitle in teal (#1a6b72): "How far each kind of study can take us".
Four rounded cards in a single row on a soft gray (#f3f4f6) panel, joined by right-pointing navy arrows, with a long thin arrow underneath labeled "More certain →".
Card 1, orange (#c55a11) top band, small 3D petri dish with cells: "Cells in a dish" — "Shows a pathway can work".
Card 2, orange top band, small 3D laboratory mouse: "Animal studies" — "Tests cause and rescue in a model".
Card 3, navy top band with a small round dot badge, 3D microscope slide of kidney tissue: "Human tissue" — "Shows a signature, not the cause".
Card 4, renal green (#1f7a4d) top band with a small square badge, a simple group of six people silhouettes: "Randomized trials in people" — "Shows what prevents kidney failure".
Under cards 1–2, a soft purple (#6c3d8e) bracket labeled "Most ferroptosis evidence is here". Under card 4, a green bracket labeled "Where today's kidney medicines are proven".
Large readable labels, generous whitespace.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No cartoon mouse, no trial names, no numbers, no clutter, no dark backgrounds. Use only Inter. Never omit the renalcarematters.com attribution.
QUALITY CHECK: Four cards in rising certainty; two brackets clearly placed; badge shapes (dot, square) echo the guide's evidence badges.
ALT TEXT: Four kinds of evidence from cells in a dish and animal studies to human tissue and randomized trials in people, showing that most ferroptosis evidence is laboratory-based while kidney medicines are proven in trials.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 017 — Where each pillar acts (clinician)

IMAGE NUMBER: 017
SECTION PLACEMENT: `#md-pillars`, after the opening paragraph, before the table
FILE NAME: metabolic-reprogramming-dkd-pillars-sites-infographic.png
ARCHETYPE: Pathophysiology mechanism poster (infographic skill; mechanism-style left panel)
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: four callout cards with two-tier labels
- 3D component graphics: nephron with glomerulus and interstitium; small vessel and fat depot
- algorithm/flowchart: none
PURPOSE: Map each pillar to its site of action and separate "proven outcome" from "proposed metabolic mediator" in the same visual.
KEY CONCEPTS: RAS blockade (efferent/glomerular pressure); SGLT2i (proximal tubule load); finerenone (MR in interstitium, vessels, inflammation/fibrosis); semaglutide (vessels, weight, perirenal fat).

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Medical pathophysiology infographic poster, graphical-abstract style, Inter font, white (#ffffff) background. Title at top in bold navy (#0f1e2e): "Four pillars, four sites of action". Subtitle in teal (#1a6b72): "Outcomes are proven in trials; metabolic effects are proposed".
Center: a semi-photorealistic 3D nephron with glomerulus, afferent and efferent arterioles, proximal tubule (soft yellow), surrounding interstitium with a few fibroblasts, and a nearby small artery; to the right, a small perirenal fat depot.
Four numbered callout cards connect with thin lines to their sites:
1 (efferent arteriole/glomerulus) "ACE inhibitor or ARB" — top line in green: "Lowers glomerular pressure and albumin leak"; bottom line in soft purple italic: "May reduce protein-driven tubular stress"
2 (proximal tubule) "SGLT2 inhibitor" — green: "Restores tubuloglomerular feedback; less transport work"; purple: "Ketone shift, mTORC1 down, anti-ferroptosis in models"
3 (interstitium/vessel) "Finerenone" — green: "Blocks mineralocorticoid receptor overactivation"; purple: "Less inflammation and fibrosis in models"
4 (artery + perirenal fat) "Semaglutide" — green: "Weight, blood pressure, lower renal resistance"; purple: "Endothelial and anti-inflammatory programs"
Legend at bottom-left: green dot "Effect seen in people", purple dot "Proposed mechanism".
Bottom strip, soft gray, navy text: "Prescribe on outcome trials; read the purple lines as hypotheses."
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No numbers. No journal names, guideline acronyms, trial names, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: Avoid clutter, tiny labels, AI gibberish, dark backgrounds, serif fonts, pill packaging or brand names.
QUALITY CHECK: Four callouts point to anatomically correct sites; green vs. purple tiers consistent with the legend; text exact.
ALT TEXT: Nephron poster showing where ACE inhibitors or ARBs, SGLT2 inhibitors, finerenone and semaglutide act, with proven effects in green and proposed metabolic mechanisms in purple.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 018 — Bedside algorithm (clinician, optional upgrade)

IMAGE NUMBER: 018
SECTION PLACEMENT: `#md-bedside` — optional replacement for SVG 06; publish only after a number-by-number proofread against the guide table
FILE NAME: metabolic-reprogramming-dkd-bedside-algorithm-infographic.png
ARCHETYPE: Long clinical algorithm — Style Mode C (renalcarematters.com house style)
AUDIENCE: Clinicians
ASPECT RATIO: 4:7
PIXEL DIMENSIONS: 1024 × 1792
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: full
PURPOSE: A printable, slide-ready version of the bedside pathway.
KEY CONCEPTS: Confirm CKD → exclude non-DKD → foundation → SGLT2i → finerenone (T2D) → GLP-1 RA → monitor.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. White background, restrained navy (#0f1e2e) and teal (#1a6b72) typography set in Inter, thin teal connector arrows, generous margins, centered top-to-bottom layout, rounded rectangles for actions, diamonds for decisions. Green (#1f7a4d) for recommended actions, amber (#b8860b) for caution, soft gray for side notes. No photos, no 3D, no clutter.
Title: "Kidney protection in diabetes with CKD"
Content to render, top to bottom:
1. Box: "Confirm CKD: eGFR + UACR; albuminuria persistent if 2 of 3 samples abnormal over 3–6 months"
2. Diamond: "Red flags? Active sediment · abrupt eGFR fall · rapidly rising proteinuria · nephrotic syndrome" → right branch amber box: "Evaluate for another cause"
3. Box: "Foundation: individualized BP and glucose targets · nutrition · activity · no smoking · lipids"
4. Box: "ACE inhibitor or ARB at maximum tolerated dose if hypertension + albuminuria"
5. Green box: "SGLT2 inhibitor from eGFR ≥20; continue below 20 if tolerated"
6. Diamond: "Type 2 diabetes, UACR ≥30 mg/g, eGFR ≥25, potassium within label limits?" → yes: green box "Add finerenone (can start together with SGLT2 inhibitor when UACR ≥100 mg/g and eGFR 30–90)"
7. Green box: "GLP-1 receptor agonist with proven kidney or heart benefit"
8. Box: "Recheck potassium and creatinine at 2–4 weeks · creatinine rise ≤30% without volume depletion: usually continue · aim for ≥30% UACR fall when baseline UACR ≥300 mg/g"
Right-side soft gray note beside steps 5–6: "On SGLT2 inhibitor: nausea, vomiting, abdominal pain or fast breathing → urgent ketoacidosis check, even with near-normal glucose"
Include a small professional footer reading "© renalcarematters.com" positioned at the bottom-center in subtle gray medical-publication styling.
No journal names, guideline acronyms, trial names, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No icons, no shadows, no dark backgrounds, no serif fonts, no spaghetti arrows, no altered numbers.
QUALITY CHECK: Proofread every threshold (≥20, ≥30 mg/g, ≥25, ≥100 mg/g, 30–90, 2–4 weeks, ≤30%, ≥30%, ≥300 mg/g) against the guide; if any digit is wrong, keep SVG 06.
ALT TEXT: Top-to-bottom algorithm for kidney protection in diabetes with CKD: confirm CKD, check for other causes, foundation therapy, ACE inhibitor or ARB, SGLT2 inhibitor, finerenone in type 2 diabetes, GLP-1 receptor agonist, and monitoring at 2 to 4 weeks.
OG WIDTH: 1024
OG HEIGHT: 1792

---

### 019 — Case snapshot (clinician)

IMAGE NUMBER: 019
SECTION PLACEMENT: `#md-case`, after the vignette paragraph, before the algo card
FILE NAME: metabolic-reprogramming-dkd-case-snapshot-infographic.png
ARCHETYPE: Case snapshot
AUDIENCE: Clinicians and trainees
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none (avoid a patient face for a synthetic case)
- 2D infographic: two case cards and an arrow
- 3D component graphics: small lab tube and urine cup
- algorithm/flowchart: baseline → 4-week arrow
PURPOSE: Show the paired-baseline arithmetic and why a modest eGFR dip with a big UACR fall means continue.
KEY CONCEPTS: eGFR 45 → 40 (−11.1%); UACR 420 → 280 (−33.3%); potassium check; continue.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clinical case snapshot infographic, teaching-conference style, Inter font, white (#ffffff) background. Title at top in bold navy (#0f1e2e): "Case: reading the 4-week labs". Small gray tag at top-right: "Synthetic teaching case".
Left card (soft gray #f3f4f6), header "Baseline": small 3D lab tube and urine cup icons; rows: "Type 2 diabetes · on maximum ARB"; "eGFR 45"; "UACR 420 mg/g"; "Potassium 4.6 mEq/L"; footer chip in teal: "Start SGLT2 inhibitor + finerenone".
Center: a thick navy right-pointing arrow labeled "4 weeks".
Right card (soft gray), header "Follow-up": rows: "eGFR 40" with an amber (#b8860b) chip "−11.1% · expected dip"; "UACR 280 mg/g" with a green (#1f7a4d) chip "−33.3% · goal met"; "Check potassium" with a small tube icon.
Bottom strip, navy text: "Confirm volume status, repeat both tests, continue. New hematuria or rapid decline → look for another cause."
Large readable numbers, generous whitespace, clean tables.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No patient photographs, no extra numbers, no clutter, no dark backgrounds, no serif fonts.
QUALITY CHECK: Proofread every number exactly as given (45, 420, 4.6, 40, 280, −11.1%, −33.3%); "Synthetic teaching case" tag visible.
ALT TEXT: Case snapshot: baseline eGFR 45 and UACR 420 mg/g; four weeks after starting an SGLT2 inhibitor and finerenone, eGFR 40 (an expected 11.1% dip) and UACR 280 mg/g (a 33.3% fall), so treatment continues.
OG WIDTH: 1792
OG HEIGHT: 1024

---

### 020 — SGLT2 inhibitor safety card (clinician)

IMAGE NUMBER: 020
SECTION PLACEMENT: `#md-safety`, after the second paragraph
FILE NAME: metabolic-reprogramming-dkd-sglt2-safety-card-infographic.png
ARCHETYPE: Compact clinician reference card
AUDIENCE: Clinicians, nurses, pharmacists
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three-column card
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: A unit-ready card for ketoacidosis recognition and procedure holds.
KEY CONCEPTS: DKA criteria; red-flag symptoms; minimum hold intervals; restart conditions.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Compact clinical reference card for clinicians, 4:3, Inter font, white (#ffffff) background. Title at top in bold navy (#0f1e2e): "SGLT2 inhibitors: ketoacidosis and procedures". Three columns of rounded cards with teal (#1a6b72) headers on soft gray (#f3f4f6).
Column 1 header "Recognize": red (#b91c1c) icon; lines "Nausea · vomiting · abdominal pain · fast breathing", "Glucose may be near normal", "Check ketones and blood gas urgently".
Column 2 header "Diabetic ketoacidosis in adults (all three)": lines "Diabetes or glucose ≥200 mg/dL", "β-hydroxybutyrate ≥3.0 mmol/L or urine ketones ≥2+", "pH <7.3 and/or bicarbonate <18 mmol/L".
Column 3 header "Before elective procedures": lines "Canagliflozin, dapagliflozin, empagliflozin: hold ≥3 days", "Ertugliflozin: hold ≥4 days", amber (#b8860b) note "Unknown agent, emergency surgery or short hold → perioperative team".
Bottom strip in green (#1f7a4d) outline: "Restart when clinically stable, eating and drinking, and ketoacidosis risk has resolved."
Clean compact layout, large readable text, no clutter.
Bottom-right: small semi-transparent navy text "renalcarematters.com".
No journal names, guideline acronyms, brand names, or watermarks other than the renalcarematters.com attribution.
```
NEGATIVE INSTRUCTIONS: No brand names, no extra drugs, no altered numbers, no icons that crowd text, no dark backgrounds, no serif fonts.
QUALITY CHECK: Proofread numbers (≥200 mg/dL, ≥3.0 mmol/L, ≥2+, <7.3, <18 mmol/L, ≥3 days, ≥4 days) against the guide's safety section and the 2024 hyperglycemic-crises consensus.
ALT TEXT: Clinician card on SGLT2 inhibitor safety: symptoms of ketoacidosis even with near-normal glucose, the three adult diabetic ketoacidosis criteria, minimum hold of 3 days for canagliflozin, dapagliflozin and empagliflozin and 4 days for ertugliflozin before procedures, and restart conditions.
OG WIDTH: 1536
OG HEIGHT: 1152

---

## Part C — Production and wiring checklist

1. **Generate** in the order in A.4. Save each output as `generated-images/NNN-[file-name].png` in the local folder; upload to the guide thread when done.
2. **Proofread** every text-bearing image before upload. Reject and regenerate any image with a misspelled word, a wrong number, an extra word, or a brand name. Prompts 013, 015, 018, 019 and 020 need a line-by-line check against the guide.
3. **Convert** each PNG to a WebP twin (quality ~82) and place both in `images/`.
4. **Wire** with the guide's figure pattern:
   ```html
   <figure>
     <picture>
       <source srcset="../images/[file].webp" type="image/webp">
       <img src="../images/[file].png" alt="[ALT TEXT]" width="[W]" height="[H]" loading="lazy" style="width:100%;height:auto;border-radius:12px">
     </picture>
     <figcaption>
       <p class="fig-desc">[plain-language caption — EN/TL/CEB/KAP spans in patient sections]</p>
       <dl class="fig-abbrevs">[every acronym visible in the image]</dl>
     </figcaption>
   </figure>
   ```
   Patient figures (003–011) need the caption in all four languages. Clinician figures can stay English. Add any new acronym in an image (for example CPT1, PL-OH) to the glossary and expand it in prose before the figure, or the acronym audit will fail.
5. **Hero and OG:** 001 and 002 are already referenced; once the files exist, the 404 clears. Run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, `patch_image_lightbox.py` and `audit_acronym_expansion.py --guide metabolic-reprogramming-dkd.html`, then `generate_latest_guides.py` (the strip uses the OG image), and commit to `main`.
6. **Replacements:** only swap SVG 01, 03 or 06 for 013, 015 or 018 if the generated image is clearly better *and* text-perfect. Never replace SVG 05 (forest plot).
