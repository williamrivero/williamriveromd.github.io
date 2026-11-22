# Image Plan Blueprint — Microbiome-Directed Supplements for Kidney Health

**Guide:** `guides/microbiome-directed-supplements-for-kidney-health.html` · **Companion calculator:** `guides/calc-fiber-intake-tracker.html`
**Version:** 2.0 · November 22, 2026 (expands the 8-prompt starter set to 23 images: hero, share card, 20 in-guide figures and one calculator card)
**Production target:** ChatGPT image generation — https://chatgpt.com/ (current GPT image model)
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` · `williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure` (with Constitution v1.0 kidney rules) · `williamriveromd-algorithm-generator-skill` · `williamriveromd-organ-crosstalk-sigil-graphic` · Stage 2 schema from `williamriveromd-local-image-generator`. The skill used is named in each prompt’s ARCHETYPE line.
**Local folder (Stage 2):** `/Users/williamgregoryriveromd/Downloads/Microbiome/`

---

## Part A — Visual strategy

### A.1 The teaching problem the images must solve

Readers arrive with one question, “will this protect my kidneys?”, and a shelf of look-alike words. The images have three jobs: tell the products apart, show the real pathway from gut to kidney, and keep an in-between laboratory result visibly separate from an outcome that matters to a patient.

| Reader need | Patients & Families (all reading levels) | Clinicians (specialist precision) |
|---|---|---|
| “Where am I in this?” | Four situations, four short answers (003) | Gut–kidney sigil as a calm anchor (014) |
| “What are these products?” | Seven tiles, one object each (004) | Definitions stay in an HTML table |
| “How could the gut affect my kidneys?” | Plate → colon → liver → kidney, two tracks (005) | Mechanism schematic with tubular inset (015) |
| “Is there proof?” | Two goals, two kinds of proof (006) | Creatinine’s three inputs (016); outcome ladder (017) |
| “What about my situation?” | Dialysis: three checks (007); after AKI (008); antibiotics per 1,000 (010) | Dialysis evidence map (019); translocation in critical illness (020); baseline risk and NNT (021) |
| “What can I do today?” | Filipino fiber foods (009); label anatomy (011); visit checklist (012); who should ask first (013) | Constipation algorithm (018); live-organism triage (022) |

**Three reading levels in one image.** Each patient figure is built so that (1) the picture alone carries the idea for a reader who skips text, (2) the short English labels confirm it at about a grade 6 level, and (3) the four-language `fig-desc` caption under the figure, plus the lightbox abbreviation list, adds the precise wording for readers who want it. Clinician figures keep the same visual grammar and add mechanism and decision detail.

### A.2 Readability rules for every patient image

1. One idea per image, readable in about ten seconds on a phone.
2. On-image words are short English labels at about a grade 6 level; the four-language `fig-desc` captions in the guide carry the explanation, so no Tagalog, Cebuano or Kapampangan text is baked into images.
3. Every analogy sits beside the real organ (the “fermentation tank” is drawn as a colon, not a factory).
4. Laboratory-only results always carry the flask icon, so a picture never overstates the evidence.
5. No real brand, strain code or registration number appears anywhere; the label figure says “SAMPLE PRODUCT”.

### A.3 Style decision: illustrated, not flat

All figures request soft semi-3D rendered illustration, to match the site’s GPT-rendered aesthetic. The hero is a photoreal still life with no people: the two most recent supplement-themed heroes showed a person holding a bottle, and the hero skill’s rotation rules call for a different arrangement. People appear only once, in the dialysis card (007), as a patient and a nurse. Three deliberate exceptions to semi-3D follow their skills’ own design: the sigil (014, monoline) and the two algorithms (018, 022, flowchart).

### A.4 What stays code-native (do not generate)

Effect sizes, confidence intervals and event counts stay in the guide’s HTML tables, the Evidence Scorecard and the trial benefit explorer, because image generators garble digits. Four prompts contain numbers and must be **proofread digit by digit**: 010 (1,000 · 32 · 968 · 16 · 984), 011 (10 · 25 · 12/2027 · FR-0000000 · ABC-123), 018 (1 to 2 weeks · 2 to 4 weeks) and 021 (0.50 · 0.5% · 5 · 2.5 · 400 · 3.2% · 32 · 16 · 65 · 1,000). Every other image is number-free. No image shows a dialyzer or blood circuit, so the circuit-anatomy rules are met by exclusion; 003, 007 and 019 forbid circuit drawings explicitly.

### A.5 Image inventory and placement

| # | File (PNG + WebP twin) | Section | Audience | Size | Priority |
|---|---|---|---|---|---|
| 001 | `microbiome-directed-supplements-for-kidney-health-vignette-hero` | Hero — `figure.hero-figure.mode-patient > .hero-vignette` | Mixed | 1:1 · 2048 × 2048 | **P1** |
| 002 | `microbiome-directed-supplements-for-kidney-health-og` | `<head>` — `og:image` / `twitter:image` | Mixed (Facebook, Messenger, Viber previews) | 1.91:1 · 1200 × 630 | **P1** |
| 003 | `microbiome-directed-supplements-for-kidney-health-07-four-situations` | `#p-start` | Patients and families (all reading levels) | 3:2 · 1536 × 1024 | **P1** |
| 004 | `microbiome-directed-supplements-for-kidney-health-01-biotics-family` | `#p-products` | Patients and families (all reading levels) | 3:2 · 1536 × 1024 | **P1** |
| 005 | `microbiome-directed-supplements-for-kidney-health-02-gut-kidney-pathway` | `#p-gut` | Patients and families | 3:2 · 1536 × 1024 | **P1** |
| 006 | `microbiome-directed-supplements-for-kidney-health-03-two-goals` | `#p-ckd` | Patients and families | 3:2 · 1536 × 1024 | **P1** |
| 007 | `microbiome-directed-supplements-for-kidney-health-09-dialysis-three-checks` | `#p-dialysis` | Patients on hemodialysis or peritoneal dialysis, caregivers, dialysis nurses | 3:2 · 1536 × 1024 | **P1** |
| 008 | `microbiome-directed-supplements-for-kidney-health-10-after-aki-what-helps` | `#p-aki` | Patients and families after a hospital stay | 3:2 · 1536 × 1024 | **P1** |
| 009 | `microbiome-directed-supplements-for-kidney-health-11-fiber-foods-filipino` | `#p-nockd` | Patients, families, dietitians | 3:2 · 1536 × 1024 | **P1** |
| 010 | `microbiome-directed-supplements-for-kidney-health-12-antibiotics-per-1000` | `#p-nockd` | Patients and families (all reading levels) | 3:2 · 1536 × 1024 | **P1** |
| 011 | `microbiome-directed-supplements-for-kidney-health-04-label-anatomy` | `#p-label` | Patients, families, pharmacists | 3:2 · 1536 × 1024 | **P1** |
| 012 | `microbiome-directed-supplements-for-kidney-health-13-visit-checklist` | `#p-visit` | Patients and caregivers | 3:2 · 1536 × 1024 | **P2** |
| 013 | `microbiome-directed-supplements-for-kidney-health-08-ask-first` | `#p-faq` | Patients, families, pharmacists | 3:2 · 1536 × 1024 | **P1** |
| 014 | `microbiome-directed-supplements-for-kidney-health-14-gut-kidney-sigil` | `#md-answer` | Clinicians (also a calm emblem for any reader) | 1:1 · 1024 × 1024 | **P3** |
| 015 | `microbiome-directed-supplements-for-kidney-health-05-gut-kidney-axis-mechanism` | `#md-axis` | Clinicians | 3:2 · 1536 × 1024 | **P1** |
| 016 | `microbiome-directed-supplements-for-kidney-health-15-creatinine-gut-confounder` | `#md-ckd` | Clinicians | 3:2 · 1536 × 1024 | **P1** |
| 017 | `microbiome-directed-supplements-for-kidney-health-06-outcome-ladder` | `#md-ckd` | Clinicians and informed patients | 3:2 · 1536 × 1024 | **P2** |
| 018 | `microbiome-directed-supplements-for-kidney-health-16-constipation-ckd-algorithm` | `#md-fiber` | Clinicians, dialysis nurses, renal dietitians | 2:3 portrait · 1024 × 1536 | **P1** |
| 019 | `microbiome-directed-supplements-for-kidney-health-17-dialysis-evidence-map` | `#md-dialysis` | Clinicians and dialysis staff | 3:2 · 1536 × 1024 | **P2** |
| 020 | `microbiome-directed-supplements-for-kidney-health-18-translocation-critical-illness` | `#md-aki` | Clinicians, intensive care and dialysis staff | 3:2 · 1536 × 1024 | **P2** |
| 021 | `microbiome-directed-supplements-for-kidney-health-19-baseline-risk-nnt` | `#md-nockd` | Clinicians, pharmacists | 3:2 · 1536 × 1024 | **P1** |
| 022 | `microbiome-directed-supplements-for-kidney-health-20-probiotic-safety-triage` | `#md-safety` | Clinicians, pharmacists, dialysis nurses | 2:3 portrait · 1024 × 1536 | **P1** |
| 023 | `calc-fiber-intake-tracker-og` | `calc-fiber-intake-tracker.html` `<head>` — `og:image` | Mixed | 1.91:1 · 1200 × 630 | **P3** |

### A.6 Consistency anchors

Visual grammar (keep identical across the set): gut bacteria as small rounded rods and spheres in soft teal (#1a6b72) and renal green (#2e6b3e); fiber as pale wheat-colored strands; short-chain fatty acids as small green droplets; protein-derived waste compounds as small amber (#b8860b) hexagons; kidney in soft renal pink with the hilum facing the body midline; intermediate (laboratory) outcomes marked with a small flask icon and patient outcomes with a small two-person icon; established steps as solid teal arrows and unproven steps as dashed purple (#4b3280) arrows.

---

## Part B — Copy-ready prompts

Generate one image per prompt. Save each PNG with the exact file name shown, then make the WebP twin.

### 001 — Hero vignette

IMAGE NUMBER: 001
SECTION PLACEMENT: Hero — `figure.hero-figure.mode-patient > .hero-vignette` (already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 · Composition I (Object Hero) · camera: overhead top-down · non-people hero · skill: williamriveromd-hero-vignette
AUDIENCE: Mixed
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX: photorealistic models: none (non-people hero; the two most recent supplement-themed heroes used a person holding a bottle) · photoreal still life: yes · 2D: none · algorithm: none
PURPOSE: Say “gut-directed supplements, examined calmly” at a glance, without promising a cure and without repeating the person-with-a-bottle hero used on recent guides.
KEY CONCEPTS: An unbranded supplement beside the real foods that feed gut bacteria; a glass of water; a kidney-shaped dish as the only kidney cue.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Square 1:1 photorealistic editorial still life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: straight overhead, top-down.

Subject: on a pale, matte, warm-white stone surface in soft morning daylight, one small amber glass jar of plain capsules with a blank, unprinted cream label (no words, no logo), lid resting beside it, placed slightly right of center and low. Supporting elements, arranged loosely around it with generous space: a small shallow ceramic dish shaped subtly like a kidney bean, holding a spoonful of pale beige fiber powder with a wooden teaspoon; three unripe green saba bananas; a small handful of dry green mung beans (monggo) scattered naturally; and a clear glass of water casting a soft caustic shadow. Colors: warm neutrals with gentle teal (#1a6b72) and renal green accents from the produce. Shallow, soft shadows; calm and uncluttered, like the cover of a premium medical textbook.

Visual hierarchy: the jar and kidney-shaped dish together occupy about 60% of the circle; the bananas, beans and glass about 25%; reserve a 20–25% TITLE SAFE ZONE of empty pale stone surface in the upper-left of the circle — no objects, shadows, crumbs or reflections there. Soft falloff toward the rim.

Absolutely NO text, labels, numbers, leader lines, callouts, titles, logos, brand marks or watermark anywhere, including on the jar — clean photograph only. Full-bleed within the inscribed circle, no rectangular borders.
```
NEGATIVE INSTRUCTIONS: Any person, hand or face; readable or pseudo-text on the jar label; brand marks; pills spilling in a way that suggests overdose; more than five objects; cropped circle; objects touching the circular border; content inside the title-safe zone; rectangular frames; dark or moody lighting; HDR; neon; clutter.
QUALITY CHECK: Square 2048×2048; circle 85–90% with visible white margin; blank jar label; empty upper-left title zone; five objects or fewer; wordless; light, calm palette matching the pastel hero.
ALT TEXT: Overhead still life on a pale stone surface: an unlabeled amber jar of capsules, a small kidney-shaped dish of fiber powder with a wooden spoon, green saba bananas, scattered mung beans and a glass of water.
OG WIDTH: 2048
OG HEIGHT: 2048

---

### 002 — Open Graph share card

IMAGE NUMBER: 002
SECTION PLACEMENT: `<head>` — `og:image` / `twitter:image` (already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-og.png
ARCHETYPE: OG / social share card · skill: williamriveromd-infographic-skill
AUDIENCE: Mixed (Facebook, Messenger, Viber previews)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX: 2D title block · photoreal still life from the hero, smaller
PURPOSE: A readable link preview that asks the question patients are already asking and signals an evidence-based answer.
KEY CONCEPTS: The question; the three settings (CKD, dialysis, AKI); calm and non-promotional.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Social share card, 1200×630, light background (#f4f9f8) with a soft mint-to-white gradient. Left 58%: title in bold navy (#0f1e2e), Inter font, two lines: "Can a probiotic or fiber powder" / "protect your kidneys?". Under it, one line in teal (#1a6b72): "What the trials show in CKD, dialysis and AKI". Under that, three small rounded chips in a row with thin teal outlines: "Evidence", "Safety", "Reading the label".
Right 42%: a clean photorealistic still life cropped in a soft rounded rectangle: an amber glass jar of capsules with a completely blank cream label, a small kidney-shaped ceramic dish of pale fiber powder with a wooden spoon, two green saba bananas and a glass of water on pale stone, soft daylight.
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution.
QUALITY CHECK: Title spelled exactly, two lines; three chips spelled exactly; blank jar label; attribution present bottom-right; readable at thumbnail size.
ALT TEXT: Share card reading “Can a probiotic or fiber powder protect your kidneys? What the trials show in CKD, dialysis and AKI” beside a still life of an unlabeled supplement jar, fiber powder, green bananas and water.
OG WIDTH: 1200
OG HEIGHT: 630

---

### 003 — Four situations, four short answers (patient)

IMAGE NUMBER: 003
SECTION PLACEMENT: `#p-start`, end of section (figure 07, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-07-four-situations.png
ARCHETYPE: Patient infographic — 2×2 tile map · skill: williamriveromd-infographic-skill
AUDIENCE: Patients and families (all reading levels)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: four small scene objects · 2D labels
PURPOSE: Let every reader find themselves in one glance before reading further.
KEY CONCEPTS: Stable CKD; dialysis; AKI; no kidney disease; one honest line each.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic, soft semi-3D rendered illustration, white background. Title at top in bold navy (#0f1e2e): "Which one are you?". Subtitle in teal (#1a6b72): "Four situations, four short answers".
A two-by-two grid of large rounded tiles, each with a numbered teal circle, one small rendered object, a bold heading and one short line:
  1 (pale teal tile): one calm kidney beside a small calendar — "Kidney disease, not on dialysis" — "Fiber can help your bowels. Nothing is proven to delay dialysis."
  2 (pale blue tile): a plain dialysis chair and a measuring glass of water — "On dialysis" — "Ask your team first. Count the fluid."
  3 (pale rose tile): a hospital bed outline with a small kidney and a clock — "Kidney injury that came on fast" — "Do not start on your own. Follow your blood tests."
  4 (pale green tile): a bowl of vegetables and beans — "No kidney disease" — "Food first. Match any supplement to one clear goal."
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Any dialysis machine circuit or blood tubing.
QUALITY CHECK: Four tiles numbered 1 to 4; headings and lines spelled exactly; calm, non-frightening objects; attribution present.
ALT TEXT: Four tiles in a two-by-two grid: stable chronic kidney disease, dialysis, acute kidney injury, and no kidney disease, each with a small picture and a one-line answer.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 004 — Seven kinds of gut-directed products (patient)

IMAGE NUMBER: 004
SECTION PLACEMENT: `#p-products`, end of section (figure 01, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-01-biotics-family.png
ARCHETYPE: Patient infographic — tile grid · skill: williamriveromd-infographic-skill with simple-figure discipline
AUDIENCE: Patients and families (all reading levels)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: seven small objects · 2D labels
PURPOSE: Let a reader tell seven label words apart in ten seconds.
KEY CONCEPTS: Prebiotic = food for bacteria; probiotic = live microbes; synbiotic = both; postbiotic = inactive microbes; butyrate; fermented foods; fiber supplement.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic, clean graphical-abstract style with soft semi-3D rendered objects. White (#ffffff) background. Title at top in bold navy (#0f1e2e): "Seven products, seven different things". Subtitle in teal (#1a6b72): "Each one needs its own evidence".
A grid of seven rounded tiles on soft gray (#f3f4f6), four in the top row and three centered in the bottom row. Each tile has one small rendered object above a bold label and one short line:
  1. Wheat-colored fiber strands with tiny teal bacteria nibbling them — "Prebiotic" — "Food for your gut bacteria"
  2. An open capsule releasing living teal and green rod-shaped bacteria — "Probiotic" — "Live microbes"
  3. A capsule containing both bacteria and fiber strands — "Synbiotic" — "Microbes plus their food"
  4. Pale gray, still, inactive bacteria shapes in a capsule — "Postbiotic" — "Inactive microbes or their parts"
  5. Three small green droplets — "Butyrate" — "Made when bacteria ferment fiber"
  6. A small bowl of yogurt and a jar of pickled vegetables — "Fermented foods" — "Foods, not treatments"
  7. A spoon of pale husk powder beside a glass of water — "Fiber supplement" — "Adds bulk, holds water"
Visual grammar (keep identical across the set): gut bacteria as small rounded rods and spheres in soft teal (#1a6b72) and renal green (#2e6b3e); fiber as pale wheat-colored strands; short-chain fatty acids as small green droplets; protein-derived waste compounds as small amber (#b8860b) hexagons; kidney in soft renal pink with the hilum facing the body midline; intermediate (laboratory) outcomes marked with a small flask icon and patient outcomes with a small two-person icon; established steps as solid teal arrows and unproven steps as dashed purple (#4b3280) arrows. Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution.
QUALITY CHECK: Seven tiles; every label and line spelled exactly; live microbes colored, inactive microbes gray; attribution present.
ALT TEXT: Seven labeled tiles showing a prebiotic fiber, a probiotic capsule with live microbes, a synbiotic combining both, a postbiotic with inactive microbes, butyrate droplets, fermented foods, and a fiber supplement.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 005 — From plate to kidney (patient)

IMAGE NUMBER: 005
SECTION PLACEMENT: `#p-gut`, end of section (figure 02, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-02-gut-kidney-pathway.png
ARCHETYPE: Patient infographic — single left-to-right pathway · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: plate, large intestine, liver, kidney · 2D arrows and labels
PURPOSE: Give the core mental model: bacteria turn fiber into helpful compounds and leftover protein into waste the kidneys must clear.
KEY CONCEPTS: Two tracks through the same fermentation tank; liver conversion; kidney removal; an in-between result is not an outcome.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education diagram, soft semi-3D rendered illustration on a white background. Title at top in bold navy: "From your plate to your kidneys". Subtitle in teal: "What gut bacteria make from food".
One horizontal pathway with four stations, left to right, joined by wide arrows:
  Station 1 "Food": a plate with vegetables and beans on one half (tagged "Fiber") and a piece of fish on the other (tagged "Protein").
  Station 2 "Large intestine": a simplified, friendly section of colon drawn as a clean fermentation tank with teal and green bacteria inside. Two tracks leave it: an upper green track labeled "Short-chain fatty acids" with the note "feed the gut lining", and a lower amber track labeled "Indole and p-cresol".
  Station 3 "Liver": a small liver; the amber track passes through it and is relabeled "Indoxyl sulfate and p-cresyl sulfate".
  Station 4 "Kidneys": one kidney, convex border facing outward and hilum facing the body midline, with the amber hexagons leaving through the ureter as "Removed in urine".
Bottom strip on soft gray: left box with a flask icon "A lower blood level = an in-between result"; right box with a two-person icon "Fewer people needing dialysis = the result that matters", joined by a dashed purple arrow labeled "not yet shown".
Visual grammar (keep identical across the set): gut bacteria as small rounded rods and spheres in soft teal (#1a6b72) and renal green (#2e6b3e); fiber as pale wheat-colored strands; short-chain fatty acids as small green droplets; protein-derived waste compounds as small amber (#b8860b) hexagons; kidney in soft renal pink with the hilum facing the body midline; intermediate (laboratory) outcomes marked with a small flask icon and patient outcomes with a small two-person icon; established steps as solid teal arrows and unproven steps as dashed purple (#4b3280) arrows. Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Kidney with hilum on the outer convex border; renal pelvis drawn floating in the center; realistic stool.
QUALITY CHECK: Four stations in order; green and amber tracks distinct; kidney hilum medial; bottom strip wording exact; attribution present.
ALT TEXT: A left-to-right pathway: food reaches the large intestine, bacteria ferment fiber into short-chain fatty acids and leftover protein into indole and p-cresol, the liver converts them, and the kidneys remove them in urine.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 006 — Two goals, two kinds of proof (patient)

IMAGE NUMBER: 006
SECTION PLACEMENT: `#p-ckd`, end of section (figure 03, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-03-two-goals.png
ARCHETYPE: Simple figure — side-by-side comparison · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: diary, calendar, kidney · 2D labels
PURPOSE: Separate a goal a person can feel within weeks from a kidney goal that needs years of trials.
KEY CONCEPTS: Bowel comfort: judge in weeks. Kidney protection: needs long trials. Do not confuse them.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Side-by-side comparison figure, soft semi-3D illustration, white background. Title at top in bold navy: "Two goals, two kinds of proof".
Left panel on pale green (#eef7f0), heading "Bowel comfort": a small open diary with seven day-boxes, most ticked in green, beside a simple toilet-paper roll icon and a glass of water. Caption below: "You can judge this in weeks".
Right panel on pale lavender (#f3effa), heading "Kidney protection": a wall calendar showing several years as stacked pages, beside one calm kidney and a small dialysis-machine outline in gray. Caption below: "This needs trials that follow people for years".
Between the panels a vertical dotted divider with a small "≠" sign in navy.
Bottom line centered in teal: "Most supplements have evidence for the left side only".
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution.
QUALITY CHECK: Two panels; headings and captions spelled exactly; ≠ sign present; attribution present.
ALT TEXT: A split image: on the left a bowel diary showing regular days as a goal you can feel within weeks; on the right a calendar of years with a kidney and a dialysis machine as outcomes that still need long trials.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 007 — Three checks before a powder on dialysis (patient)

IMAGE NUMBER: 007
SECTION PLACEMENT: `#p-dialysis`, end of section (figure 09, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-09-dialysis-three-checks.png
ARCHETYPE: Reference card — three numbered panels · skill: williamriveromd-simple-figure
AUDIENCE: Patients on hemodialysis or peritoneal dialysis, caregivers, dialysis nurses
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Photorealistic models: one Filipino patient and one dialysis nurse in panel 3 only · 3D component graphics: measuring glass, pack · 2D labels
PURPOSE: Turn three safety habits into a picture a patient can remember at the store.
KEY CONCEPTS: Count the water; read the ingredients; show the label.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Three-panel reference card, soft semi-3D illustration with one warm photorealistic scene, white background. Title at top in bold navy: "On dialysis? Three checks before any powder or drink".
Panel 1 (pale blue), large numeral 1: a clear measuring glass of water with a spoon of powder being stirred in. Heading "Count the water". Line: "It is part of your daily fluid limit".
Panel 2 (pale amber), large numeral 2: a magnifying glass over a plain ingredient panel on an unbranded pack; three words are enlarged in the lens: "potassium", "sodium", "phos". Heading "Read the ingredients". Line: "Look for potassium, sodium and any word with phos".
Panel 3 (pale green), large numeral 3: a Filipino man in his forties with short graying hair, wearing a plain gray T-shirt, seated, holding out an unbranded pack to a Filipina dialysis nurse in navy scrubs with her hair tied back, who is reading it; bright clinic corridor softly blurred behind; no dialysis machine or tubing in view. Heading "Show the label". Line: "Before the first dose".
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Any dialysis circuit, dialyzer or blood tubing; visible needles; a brand on the pack.
QUALITY CHECK: Three numbered panels; the three magnified words spelled exactly; no dialysis equipment drawn; correct hands; attribution present.
ALT TEXT: Three numbered panels for people on dialysis: a measuring glass for counting the mixing water, a magnifying glass over an ingredient list, and a patient showing a label to a dialysis nurse.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 008 — After AKI: what helps, what can wait (patient)

IMAGE NUMBER: 008
SECTION PLACEMENT: `#p-aki`, end of section (figure 10, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-10-after-aki-what-helps.png
ARCHETYPE: Simple figure — two-column comparison · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families after a hospital stay
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: test tube, urine cup, clipboard, blood pressure cuff, jar · 2D labels
PURPOSE: Redirect attention from a supplement to the follow-up that protects recovery.
KEY CONCEPTS: Four follow-up actions first; supplement on pause until the doctor agrees.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Two-column comparison figure, soft semi-3D illustration, white background. Title at top in bold navy: "After a sudden kidney injury".
Left column on pale green (#eef7f0), wide (about two-thirds of the width), heading "What helps most": four evenly spaced objects in a row, each with a short label below — a blood test tube "Repeat creatinine", a urine sample cup "Urine test", a clipboard with a short list "Medicine review", a blood pressure cuff "Blood pressure check". A green check mark in the corner.
Right column on pale gray (#f3f4f6), narrow, heading "What can wait": one plain unlabeled supplement jar with a round pause symbol over it. Line below: "Start only if your doctor agrees".
Bottom line centered in teal: "Follow the trend of your tests, not one number".
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. A stop sign or skull; a frightened patient; a brand on the jar.
QUALITY CHECK: Four labeled objects on the left; pause symbol (not a prohibition sign) on the jar; wording exact; attribution present.
ALT TEXT: Two columns: on the left, what helps after acute kidney injury, shown as a blood test tube, a urine cup, a medicine list and a blood pressure cuff; on the right, a supplement jar with a pause symbol.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 009 — Food first: fiber from the Filipino table (patient)

IMAGE NUMBER: 009
SECTION PLACEMENT: `#p-nockd`, under “For general wellness” (figure 11, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-11-fiber-foods-filipino.png
ARCHETYPE: Food matrix — photoreal editorial still life with labels · skill: williamriveromd-infographic-skill
AUDIENCE: Patients, families, dietitians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Photorealistic food still life · 2D labels
PURPOSE: Make “food first” concrete and appetizing with market foods, while flagging the potassium question honestly.
KEY CONCEPTS: Eight familiar foods; fiber feeds your own bacteria; portions depend on the potassium plan.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Bright photorealistic overhead food photograph on a pale wooden table in soft daylight, arranged as a tidy two-row grid of eight small white dishes with generous space between them. Title above on a clean white band in bold navy: "Food first: fiber from the Filipino table". Each dish has a short navy label beneath it:
  Top row: a bowl of cooked mung beans "Monggo" · sliced green okra pods "Okra" · a bundle of water spinach "Kangkong" · cut yardlong beans "Sitaw"
  Bottom row: two saba bananas "Saba" · halved guava "Bayabas" · boiled orange sweet potato "Kamote" · a small mound of brown rice "Brown rice"
Bottom band on pale amber (#fff7e6): "Kidney disease? Ask your dietitian about portions. Some of these are high in potassium."
Natural colors, no garnish clutter, no sauces, no cutlery, no hands.
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Fried or processed foods; meat or fish; salt shaker; bagoong, patis or other sauces; foods not listed; more or fewer than eight dishes.
QUALITY CHECK: Exactly eight dishes; eight labels spelled exactly and matched to the right food; amber band wording exact; attribution present.
ALT TEXT: A bright overhead photograph of fiber-rich Filipino foods on a light table: cooked monggo, okra, kangkong, sitaw, saba bananas, guava, kamote and brown rice, with a note that portions depend on the potassium plan.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 010 — Antibiotics and probiotics: out of 1,000 people (patient)

IMAGE NUMBER: 010
SECTION PLACEMENT: `#p-nockd`, end of section (figure 12, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-12-antibiotics-per-1000.png
ARCHETYPE: Simple figure — side-by-side frequency comparison · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families (all reading levels)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 2D crowd illustration with highlighted clusters · large numerals
PURPOSE: Show a real but small benefit in natural frequencies, so it is neither dismissed nor oversold.
KEY CONCEPTS: 32 in 1,000 without; 16 in 1,000 with; most people do not get it either way; benefit is smaller when risk is low.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Side-by-side frequency figure, soft illustrated style, white background. Title at top in bold navy: "Diarrhea from the C. difficile germ during antibiotics". Subtitle in teal: "Out of 1,000 people".
Left panel, heading "Without a probiotic": a wide, dense crowd of small, simple gray person-shapes filling the panel; a small cluster at the lower left is colored amber. Large amber numeral beneath: "32". Line below: "968 did not get it".
Right panel, heading "With a probiotic": the same gray crowd; a visibly smaller amber cluster, about half the size. Large amber numeral beneath: "16". Line below: "984 did not get it".
Bottom strip on soft gray (#f3f4f6): "The benefit is smaller if your starting risk is low. Experts do not all agree."
The crowds suggest a large number; the person-shapes are not meant to be counted.
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Any numeral other than 1,000, 32, 968, 16 and 984; percentages; faces or distressed figures; toilets.
QUALITY CHECK: Numerals exactly 32, 968, 16, 984 and 1,000; right amber cluster about half the left; bottom strip wording exact; attribution present.
ALT TEXT: Two side-by-side crowds representing 1,000 people taking antibiotics: without a probiotic about 32 are highlighted as getting C. difficile diarrhea, with a probiotic about 16, with a note that the benefit is smaller when the starting risk is low.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 011 — Anatomy of a supplement label (patient)

IMAGE NUMBER: 011
SECTION PLACEMENT: `#p-label`, end of section (figure 04, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-04-label-anatomy.png
ARCHETYPE: Reference card — annotated object · skill: williamriveromd-simple-figure
AUDIENCE: Patients, families, pharmacists
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: one fictional box · 2D numbered callouts
PURPOSE: Show where to look on a Philippine food-supplement label, using a clearly fictional product.
KEY CONCEPTS: Full name with strain code; amount per serving; storage and expiry; other ingredients; registration number; registration is not proof of treatment.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Reference-card illustration, soft semi-3D, white background. Title at top in bold navy: "Where to look on a supplement label".
Center: one plain rectangular supplement box, cream with a teal band, turned three-quarters so the front and one side panel are visible. The box is FICTIONAL: the product name on it reads exactly "SAMPLE PRODUCT" and under it "Food Supplement". The side panel shows a simplified table of lines (no readable small print, just neat gray bars) except for these short readable lines: "Lactiplantibacillus plantarum ABC-123", "10 billion CFU per capsule", "Store below 25°C", "EXP 12/2027", "Other ingredients", "FR-0000000".
Six numbered navy circles with thin leader lines point to parts of the box, each with a short label card:
  1 "Full name and strain code"
  2 "Amount per serving"
  3 "Storage and expiry date"
  4 "Other ingredients: sugar, sodium, potassium, phosphate"
  5 "Registration number: check it online"
  6 "Not a medicine notice"
Bottom strip on pale amber (#fff7e6): "Registered means allowed for sale. It does not mean proven to treat disease."
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Any real product name, real registration number or real company; a strain code other than ABC-123.
QUALITY CHECK: Box reads SAMPLE PRODUCT; six callouts numbered and spelled exactly; digits 10, 25, 12/2027 and FR-0000000 proofread; attribution present.
ALT TEXT: A fictional unbranded supplement box with numbered callouts pointing to the full microbe name with strain code, the amount per serving, storage and expiry, other ingredients, and the registration number.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 012 — Four things to bring to your visit (patient)

IMAGE NUMBER: 012
SECTION PLACEMENT: `#p-visit`, end of section (figure 13, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-13-visit-checklist.png
ARCHETYPE: Reference card — checklist · skill: williamriveromd-simple-figure
AUDIENCE: Patients and caregivers
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: phone, note, list, diary, bag · 2D labels
PURPOSE: A friendly reminder of what makes the visit useful.
KEY CONCEPTS: Label photo; goal; medicine list; bowel diary.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Checklist card, soft semi-3D illustration, white background. Title at top in bold navy: "Bring these four things".
Left third: a simple woven market bag (bayong) standing open, in warm neutral tones.
Right two-thirds: four stacked rounded rows, each with a teal check box, a small object and a short line:
  a smartphone showing a photo of a plain pack — "A photo of every side of the label"
  a small note card with a pencil — "Your goal: what do you hope it will do?"
  a short printed list with pill icons — "All your medicines and supplements"
  a small diary with seven boxes — "A one-week bowel diary"
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution.
QUALITY CHECK: Four rows with check boxes; lines spelled exactly; no brand on the phone screen or pack; attribution present.
ALT TEXT: A checklist card with four items: a phone photo of a supplement label, a written goal, a list of medicines, and a one-week bowel diary, beside a market bag.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 013 — Who should ask a doctor first (patient)

IMAGE NUMBER: 013
SECTION PLACEMENT: `#p-faq`, end of section (figure 08, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-08-ask-first.png
ARCHETYPE: Reference card — four icons · skill: williamriveromd-simple-figure
AUDIENCE: Patients, families, pharmacists
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D icons, no photoreal people · 2D labels
PURPOSE: Make the four higher-risk groups recognizable without frightening anyone.
KEY CONCEPTS: Transplant or weak immunity; catheter or line in a large vein; in hospital or very ill; serious bowel disease.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Four-icon reference card, soft semi-3D illustration, white background. Title at top in bold navy: "Ask your doctor before any live-bacteria product if you have:".
Four rounded tiles in a row on pale rose (#fdf0f0), each with one calm, simple icon and a short label:
  a torso outline with one small transplanted kidney low in the pelvis on one side and a small shield with a gap in it — "A transplant or weak immunity"
  an upper-chest outline with a short soft catheter under the collarbone, capped, no blood shown — "A dialysis catheter or line in a large vein"
  a hospital bed with a small drip stand — "A hospital stay or serious illness"
  a simple intestine outline with one inflamed amber segment — "A serious bowel disease"
Bottom strip on pale amber: "Stop and get care for fever, chills, severe belly pain or blood in the stool."
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Blood, needles, open wounds; a transplanted kidney drawn in the flank instead of the lower pelvis; prohibition signs or skulls.
QUALITY CHECK: Four tiles; labels spelled exactly; transplant kidney low in the pelvis; catheter capped and bloodless; attribution present.
ALT TEXT: Four icons of people who should ask a doctor before taking a live-bacteria product: a kidney transplant recipient, a person with a dialysis catheter, a hospital patient, and a person with serious bowel disease.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 014 — Gut–kidney sigil (clinician)

IMAGE NUMBER: 014
SECTION PLACEMENT: `#md-answer`, end of section (figure 14, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-14-gut-kidney-sigil.png
ARCHETYPE: Organ crosstalk sigil · skill: williamriveromd-organ-crosstalk-sigil-graphic
AUDIENCE: Clinicians (also a calm emblem for any reader)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX: Monoline line art only (the one deliberate exception to the semi-3D style, by skill design)
PURPOSE: A quiet visual anchor for the axis before the detailed mechanism figure.
KEY CONCEPTS: Gut to kidney and kidney to gut: a two-way loop.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a simple medical organ-crosstalk sigil illustration featuring the intestine and the two kidneys.
RELATIONSHIP: show gut–kidney crosstalk using dotted curved arrows: one arc flowing down from the intestine to the kidneys and one returning upward, forming a calm two-way loop. A few tiny dots travel along the downward arc.
STYLE: minimal clinical line-art, thin monoline strokes, soft teal (#1a6b72) and slate palette, white background, clean rounded organ shapes, balanced sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels.
COMPOSITION: a simplified coiled large-intestine icon at top center; two bean-shaped kidneys symmetrically below, each with its concave hilum facing the midline. Connect them with dotted arrows forming a gentle bidirectional loop.
OUTPUT: square 1024×1024, clean margins, publication-grade medical icon aesthetic. Include a small, semi-transparent navy "© renalcarematters.com" in the bottom-right corner, not touching the sigil.
```
NEGATIVE INSTRUCTIONS: Photorealistic anatomy; surgical detail; any label other than the attribution; dark background; neon; thick cartoon outlines; 3D rendering; glossy icons; kidneys with the hilum facing outward.
QUALITY CHECK: Label-free except attribution; kidney hila face the midline; two-way dotted loop; thin even strokes.
ALT TEXT: Minimal line-art sigil: an intestine icon above two kidney icons, joined by dotted curved arrows forming a two-way loop.
OG WIDTH: 1024
OG HEIGHT: 1024

---

### 015 — Gut–kidney axis mechanism (clinician)

IMAGE NUMBER: 015
SECTION PLACEMENT: `#md-axis`, end of section (figure 05, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-05-gut-kidney-axis-mechanism.png
ARCHETYPE: Biomedical mechanism figure (organ-level panel → dashed magnified inset → bottom summary flow) · skill: williamriveromd-biomedical-mechanism-figure, with Constitution v1.0 kidney rules from williamriveromd-infographic-generator
AUDIENCE: Clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D anatomy: colon segment, liver, kidney, proximal tubule cell · 2D labels and arrows
PURPOSE: Trace the causal chain from colonic fermentation to tubular secretion, and mark where evidence stops.
KEY CONCEPTS: Saccharolytic vs proteolytic fermentation; hepatic conjugation; albumin binding; OAT-mediated proximal tubular secretion; intermediate vs patient-important outcomes.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Review-article biomedical mechanism schematic with soft semi-3D shading, white background, thin dashed boxes around magnified panels, muted clinical palette. Font: Inter. Title at top in navy: "The gut–kidney pathway".
LEFT PANEL (organ level): a short segment of colon in light gray-blue with two labeled lumen zones. Upper zone, green: "Saccharolytic fermentation" with fiber strands and bacteria, arrow out labeled "SCFA: acetate, propionate, butyrate" and a small note "fuel for colonocytes, barrier support". Lower zone, amber: "Proteolytic fermentation" with arrows out labeled "Tryptophan → indole" and "Tyrosine, phenylalanine → p-cresol". A small red upward arrow beside the lower zone labeled "↑ in CKD".
CENTER: a small liver with one arrow in and one arrow out, labeled "Hepatic conjugation → indoxyl sulfate (IS), p-cresyl sulfate (PCS)". Below it a small albumin shape carrying amber hexagons, labeled ">90% albumin-bound".
RIGHT PANEL: one kidney in coronal section, convex border lateral, hilum medial, renal pelvis at the hilum, calyces draining inward. A dashed connector leads to a DASHED MAGNIFIED INSET of a single proximal tubule cell: basolateral side facing a peritubular capillary, transporters drawn as teal channels labeled "OAT1 / OAT3", amber hexagons moving from blood through the cell into the tubular lumen, labeled "Proximal tubular secretion". A small red downward arrow labeled "↓ secretion in CKD".
BOTTOM SUMMARY FLOW, three boxes left to right joined by arrows:
  Pale pink box, flask icon: "Measured in trials: microbiota, urea, IS, PCS"
  Pale gray box, dashed purple arrow through it: "Unproven step"
  Pale blue box, two-person icon: "Needed: kidney failure, recovery, survival"
Visual grammar (keep identical across the set): gut bacteria as small rounded rods and spheres in soft teal (#1a6b72) and renal green (#2e6b3e); fiber as pale wheat-colored strands; short-chain fatty acids as small green droplets; protein-derived waste compounds as small amber (#b8860b) hexagons; kidney in soft renal pink with the hilum facing the body midline; intermediate (laboratory) outcomes marked with a small flask icon and patient outcomes with a small two-person icon; established steps as solid teal arrows and unproven steps as dashed purple (#4b3280) arrows. Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Hilum on the convex border; calyces pointing outward; renal pelvis floating centrally; glomerular filtration shown as the main clearance route for IS and PCS; transporters on the wrong (apical) membrane only; colon drawn inside the kidney.
QUALITY CHECK: Kidney orientation correct (convex lateral, hilum medial); calyces drain inward; OAT1/OAT3 on the basolateral membrane; SCFA track green and toxin track amber; three bottom boxes spelled exactly; attribution exact and unobstructed.
ALT TEXT: Mechanism schematic: colon with saccharolytic fermentation producing short-chain fatty acids and proteolytic fermentation producing indole and p-cresol; hepatic conjugation; albumin-bound transport; proximal tubular secretion in a magnified inset; and a bottom row separating intermediate from patient-important outcomes.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 016 — Creatinine and the gut: why confirmation matters (clinician)

IMAGE NUMBER: 016
SECTION PLACEMENT: `#md-ckd`, before “Other signals” (figure 15, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-15-creatinine-gut-confounder.png
ARCHETYPE: Simple figure — single mechanism with one hypothesis arrow · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D anatomy: muscle, kidney, colon segment, blood vessel · 2D labels
PURPOSE: Show why a gut-acting intervention can move serum creatinine without moving GFR, and what checks it.
KEY CONCEPTS: Production in muscle; renal filtration and tubular secretion; extrarenal gut degradation, larger in advanced CKD; hypothesis arrow; cystatin C as independent marker.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Scientific simple figure, soft semi-3D shading, white background, Inter font. Title at top in navy: "Serum creatinine has three inputs".
Center: a horizontal blood vessel segment labeled "Serum creatinine".
Left, feeding into the vessel with a solid teal arrow: a skeletal muscle belly labeled "Production: muscle mass, diet".
Right upper, leaving the vessel with a thick solid teal arrow: one kidney (convex border lateral, hilum medial) labeled "Kidney: filtration + tubular secretion".
Right lower, leaving the vessel with a thinner solid teal arrow: a short colon segment with teal bacteria labeled "Gut: bacterial degradation" and a small note "larger share in advanced CKD".
From a small unlabeled capsule drawn above the colon, a DASHED PURPLE arrow points at the gut route, labeled "Gut-acting product: effect on this route? (hypothesis)".
Bottom strip, two boxes: left pale amber "Creatinine eGFR and creatinine clearance share this dependence"; right pale blue "Independent check: cystatin C or measured GFR".
Visual grammar (keep identical across the set): gut bacteria as small rounded rods and spheres in soft teal (#1a6b72) and renal green (#2e6b3e); fiber as pale wheat-colored strands; short-chain fatty acids as small green droplets; protein-derived waste compounds as small amber (#b8860b) hexagons; kidney in soft renal pink with the hilum facing the body midline; intermediate (laboratory) outcomes marked with a small flask icon and patient outcomes with a small two-person icon; established steps as solid teal arrows and unproven steps as dashed purple (#4b3280) arrows. Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. The hypothesis arrow drawn solid; any claim that probiotics lower creatinine; hilum on the convex border; brand on the capsule.
QUALITY CHECK: Three routes present; only the capsule arrow is dashed purple and carries the word hypothesis; kidney orientation correct; bottom boxes spelled exactly; attribution present.
ALT TEXT: Schematic of creatinine handling: muscle produces creatinine, the kidney removes most of it, and a smaller share is degraded by gut bacteria; a dashed arrow marks the hypothesis that a gut-acting product could change the gut share, with cystatin C as an independent check.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 017 — Outcome ladder (clinician)

IMAGE NUMBER: 017
SECTION PLACEMENT: `#md-ckd`, end of section (figure 06, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-06-outcome-ladder.png
ARCHETYPE: Simple figure — four-rung ladder · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians and informed patients
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: ladder · 2D labels
PURPOSE: Show at a glance how far up the outcome hierarchy current trials reach.
KEY CONCEPTS: Microbiota composition → circulating solutes and urea → creatinine-based eGFR over months → sustained GFR loss, kidney failure, hospitalization, survival.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Simple figure, soft semi-3D illustration, white background. Title at top in bold navy: "How far have the trials climbed?".
A wide four-rung ladder leaning slightly right. Each rung has a label card to its right, bottom to top:
  Rung 1 (pale green card): "Stool microbiota composition"
  Rung 2 (pale green card): "Blood solutes and urea"
  Rung 3 (pale amber card): "Creatinine-based eGFR over months"
  Rung 4 (pale blue card, top): "Sustained GFR loss, kidney failure, hospitalization, survival"
Small flask icons beside rungs 1 to 3; a small two-person icon beside rung 4. A teal bracket spans rungs 1 to 3 with the note "Where current trials stop". A dashed purple arrow rises from rung 3 to rung 4 with the note "Not yet tested".
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution.
QUALITY CHECK: Four rungs in the stated order, bottom to top; notes spelled exactly; attribution present.
ALT TEXT: A four-rung ladder of outcomes: stool microbiota composition, blood solutes and urea, creatinine-based eGFR over months, and at the top sustained GFR loss, kidney failure, hospitalization and survival, with a bracket showing that current trials stop at the third rung.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 018 — Constipation in kidney disease algorithm (clinician)

IMAGE NUMBER: 018
SECTION PLACEMENT: `#md-fiber`, end of section (figure 16, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-16-constipation-ckd-algorithm.png
ARCHETYPE: Clinical algorithm, journal treatment-pathway style (Style B) · skill: williamriveromd-algorithm-generator-skill
AUDIENCE: Clinicians, dialysis nurses, renal dietitians
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX: Algorithm/flowchart only
PURPOSE: A one-page pathway that mirrors the seven-step HTML algorithm for wall or tablet use.
KEY CONCEPTS: Alarm features and medicines first; intake; food; psyllium in steps; product check; PEG or lactulose; avoid magnesium and phosphate; reassess.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Publication-grade clinical algorithm in the style of a journal treatment pathway. White background, centered top-to-bottom logic, rounded rectangles for actions, diamonds for decisions, thin navy arrows, muted pastel fills, consistent node size and spacing, generous margins, crisp navy sans-serif typography set in Inter. No photorealistic people, no cartoon styling, no decorative icons. Portrait layout. Title at top: "Constipation in kidney disease".
Top-to-bottom nodes, one per row, connected by single downward arrows:
  1. Diamond: "Alarm features? Weight loss, bleeding, vomiting, distension" — "Yes" branch to the right, pale red rounded box: "Evaluate first"
  2. Rounded box (pale gray): "Review medicines: opioids, calcium binders, oral iron, anticholinergics, potassium binders"
  3. Rounded box (pale teal): "Estimate current fiber intake"
  4. Rounded box (pale green): "Food first, within the potassium and phosphorus plan"
  5. Rounded box (pale green): "Add psyllium in small steps over 1 to 2 weeks"
  6. Rounded box (pale amber): "Check the product: potassium, phosphate, sodium, sugar, mixing fluid"
  7. Diamond: "Better at 2 to 4 weeks?" — "Yes" branch to the right, pale green box: "Continue and review"; "No" continues down
  8. Rounded box (pale blue): "Escalate: polyethylene glycol, or lactulose"
  9. Rounded box (pale red, at the bottom, full width): "Avoid at low GFR: magnesium laxatives, sodium phosphate preparations"
Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray (#6b7280) medical-publication styling, never inside a node or over an arrow. Spell every word exactly as given; add no other words or numbers.
```
NEGATIVE INSTRUCTIONS: Dark backgrounds; photorealistic people; cartoon styling; serif or decorative fonts; crossing or ambiguous arrows; nodes of uneven size; extra nodes, drug names, doses or numbers not listed; garbled text; missing or altered attribution.
QUALITY CHECK: Nine nodes in the stated order; two diamonds; numbers limited to "1 to 2 weeks" and "2 to 4 weeks"; no doses; attribution present.
ALT TEXT: Vertical clinical algorithm for constipation in kidney disease: exclude alarm features and review medicines, estimate fiber intake, food first, add psyllium in small steps, check product ingredients and fluid, escalate to polyethylene glycol or lactulose, avoid magnesium and phosphate laxatives.
OG WIDTH: 1024
OG HEIGHT: 1536

---

### 019 — Dialysis evidence map (clinician)

IMAGE NUMBER: 019
SECTION PLACEMENT: `#md-dialysis`, end of section (figure 17, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-17-dialysis-evidence-map.png
ARCHETYPE: Simple figure — two-column evidence map · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians and dialysis staff
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 2D grid with small header silhouettes
PURPOSE: Show the gap between measured and unmeasured outcomes, by modality, without implying numbers.
KEY CONCEPTS: Measured: solutes, inflammation, nutrition measures, phosphorus (HD); endotoxin, microbiota, uric acid (PD). Untested: residual function, adequacy, peritonitis, hospitalization, survival.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Evidence-map figure, soft clean style, white background, Inter font. Title at top in navy: "Dialysis: what trials measured, and what they did not".
Two columns with header chips: left "Hemodialysis" with a tiny, plain machine silhouette (a simple box on a stand, no circuit, no tubing); right "Peritoneal dialysis" with a tiny dialysate-bag silhouette.
Upper band across both columns, tinted pale green, row label at far left with a flask icon "Measured (small trials)":
  Hemodialysis cell, four chips: "Gut-derived solutes" · "Inflammatory markers" · "Skinfold and body mass index" · "Phosphorus (one trial)"
  Peritoneal dialysis cell, three chips: "Endotoxin and cytokines" · "Microbiota composition" · "Uric acid"
Lower band across both columns, white with a dashed purple outline, row label at far left with a two-person icon "Not yet tested":
  Hemodialysis cell, four empty-outline chips: "Residual kidney function" · "Dialysis adequacy" · "Hospitalization" · "Survival"
  Peritoneal dialysis cell, four empty-outline chips: "Residual kidney function" · "Peritonitis" · "Technique survival" · "Survival"
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Any dialyzer, blood tubing or circuit drawing; numbers or percentages; trial names.
QUALITY CHECK: Chips spelled exactly and in the right cells; upper band filled, lower band outline-only; no circuit drawn; attribution present.
ALT TEXT: Two-column evidence map for hemodialysis and peritoneal dialysis: a filled upper band lists what trials measured; an empty lower band lists what has not been tested, such as residual kidney function, peritonitis, hospitalization and survival.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 020 — Translocation in critical illness (clinician)

IMAGE NUMBER: 020
SECTION PLACEMENT: `#md-aki`, end of section (figure 18, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-18-translocation-critical-illness.png
ARCHETYPE: Biomedical mechanism figure — side-by-side barrier panels with dashed inset · skill: williamriveromd-biomedical-mechanism-figure
AUDIENCE: Clinicians, intensive care and dialysis staff
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D cellular anatomy: enterocytes, capillary, catheter hub · 2D labels
PURPOSE: Explain why a product that is benign in outpatients carries measurable risk in the ICU.
KEY CONCEPTS: Intact barrier vs compromised barrier; hypoperfusion; translocation; second route by catheter hub contamination.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Review-article biomedical mechanism schematic, soft semi-3D shading, white background, thin dashed boxes, muted clinical palette, Inter font. Title at top in navy: "Why critical illness changes probiotic safety".
LEFT PANEL in a dashed box, heading "Stable outpatient": a row of tall intestinal epithelial cells with tight junctions drawn as small closed teal clasps, a mucus layer above, teal rod-shaped organisms staying in the lumen, a calm capillary below. Label: "Intact barrier: organisms stay in the lumen".
RIGHT PANEL in a dashed box, heading "Critical illness": the same cell row with gaps between cells and open clasps, a thinned mucus layer, a paler capillary with a small red downward arrow "↓ gut perfusion", and two teal organisms crossing between cells into the capillary along a red arrow labeled "Translocation".
SMALL INSET at far right in a dashed box: the capped hub of a central venous catheter with one teal organism near the hub and a thin red arrow into the line, labeled "Second route: hub contamination during handling".
BOTTOM SUMMARY FLOW, three boxes joined by arrows: pale pink "Barrier injury + central access" → pale gray "Live organisms given" → pale red "Organism isolated from blood or sterile site".
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Gore; a full patient body; pus; monster-like bacteria; numbers or trial names.
QUALITY CHECK: Closed junctions on the left, open on the right; two entry routes shown; bottom boxes spelled exactly; calm palette; attribution present.
ALT TEXT: Mechanism schematic: a healthy gut barrier keeping probiotic organisms in the lumen, beside a critically ill gut with a leaky barrier where organisms cross into the bloodstream; a central venous catheter hub is shown as a second entry route.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 021 — Baseline risk and number needed to treat (clinician)

IMAGE NUMBER: 021
SECTION PLACEMENT: `#md-nockd`, end of section (figure 19, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-19-baseline-risk-nnt.png
ARCHETYPE: Simple figure — annotated risk scale with two worked points · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians, pharmacists
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 2D scale and cards
PURPOSE: Show why the same relative effect yields different absolute benefit, which is where the two guidelines part ways.
KEY CONCEPTS: Risk ratio 0.50 held constant; 3.2% → NNT about 65 (pooled trials); 0.5% → NNT about 400 (arithmetic).

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Annotated scale figure, clean soft style, white background, Inter font. Title at top in navy: "Same relative effect, different absolute benefit". Subtitle in teal: "C. difficile diarrhea during antibiotics, risk ratio 0.50".
A horizontal axis across the middle labeled "Baseline risk without a probiotic", with a soft gradient from pale green at the left ("lower risk") to pale amber at the right ("higher risk"). Two markers on the axis, each with a card above it:
  Left marker at "0.5%": card heading "Low-risk course (arithmetic)"; two lines "5 → 2.5 per 1,000" and "NNT about 400"
  Right marker at "3.2%": card heading "Pooled trials"; two lines "32 → 16 per 1,000" and "NNT about 65"
Under the axis, a thin bracket spanning both markers with the note "Know the baseline risk before deciding".
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution. Any numeral other than 0.50, 0.5%, 5, 2.5, 400, 3.2%, 32, 16, 65 and 1,000; guideline or trial names; a curve implying data between the two points.
QUALITY CHECK: All ten numerals exact; left card marked arithmetic, right card marked pooled trials; no extra data points; attribution present.
ALT TEXT: A horizontal baseline-risk scale with two worked points: at a control risk of 3.2 percent, 32 versus 16 cases per 1,000 and a number needed to treat of about 65; at 0.5 percent, 5 versus 2.5 per 1,000 and about 400.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 022 — Live-organism product triage (clinician)

IMAGE NUMBER: 022
SECTION PLACEMENT: `#md-safety`, end of section (figure 20, already wired)
FILE NAME: microbiome-directed-supplements-for-kidney-health-20-probiotic-safety-triage.png
ARCHETYPE: Clinical algorithm, journal treatment-pathway style (Style B) · skill: williamriveromd-algorithm-generator-skill
AUDIENCE: Clinicians, pharmacists, dialysis nurses
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX: Algorithm/flowchart only
PURPOSE: A quick screen to run before agreeing to any live-organism supplement.
KEY CONCEPTS: Do not start in critical illness or active AKI; review in immunosuppression, central access, severe bowel disease; unnamed strain not endorsed; mineral and fluid check; defined goal and stop date.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Publication-grade clinical algorithm in the style of a journal treatment pathway. White background, centered top-to-bottom logic, rounded rectangles for actions, diamonds for decisions, thin navy arrows, muted pastel fills, consistent node size and spacing, generous margins, crisp navy sans-serif typography set in Inter. No photorealistic people, no cartoon styling, no decorative icons. Portrait layout. Title at top: "Before a live-organism supplement".
Top-to-bottom decision spine with four diamonds; each "Yes" exits to the right into a rounded box, each "No" continues down:
  Diamond 1: "Critically ill, or acute kidney injury still evolving?" — Yes → pale red box "Do not start"
  Diamond 2: "Transplant, immunosuppression, central venous catheter, or severe bowel disease?" — Yes → pale amber box "Clinician review first"
  Diamond 3: "Strain not named on the label?" — Yes → pale amber box "Cannot be matched to evidence: do not endorse"
  Diamond 4: "Potassium, phosphate, sodium or fluid limit affected?" — Yes → pale amber box "Adjust, or choose another product"
Final rounded box at the bottom (pale green, full width): "Proceed for one defined goal. Set a review date and a stop date."
Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray (#6b7280) medical-publication styling, never inside a node or over an arrow. Spell every word exactly as given; add no other words or numbers.
```
NEGATIVE INSTRUCTIONS: Dark backgrounds; photorealistic people; cartoon styling; serif or decorative fonts; crossing or ambiguous arrows; nodes of uneven size; extra nodes, drug names, doses or numbers not listed; garbled text; missing or altered attribution.
QUALITY CHECK: Four diamonds in the stated order; four right-hand boxes with matching colors; final green box wording exact; no numbers; attribution present.
ALT TEXT: Vertical triage algorithm before a live-organism product: critical illness or active acute kidney injury leads to do not start; transplant, immunosuppression, central venous catheter or severe bowel disease lead to clinician review; an unnamed strain leads to do not endorse; otherwise check minerals and fluid, then proceed for a defined goal with a stop date.
OG WIDTH: 1024
OG HEIGHT: 1536

---

### 023 — Fiber tracker share card (calculator, optional)

IMAGE NUMBER: 023
SECTION PLACEMENT: `calc-fiber-intake-tracker.html` `<head>` — `og:image` (not wired; the page currently uses the nutrition category image)
FILE NAME: calc-fiber-intake-tracker-og.png
ARCHETYPE: OG / social share card · skill: williamriveromd-infographic-skill
AUDIENCE: Mixed
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX: 2D title block · semi-3D tablet and food objects
PURPOSE: A distinct link preview for the companion calculator.
KEY CONCEPTS: Fiber in grams; target from the care team; bowel diary.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Social share card, 1200×630, light background (#f4f9f8). Left 58%: title in bold navy, Inter font, two lines: "Fiber Intake" / "and Tolerance Tracker". Under it, one line in teal: "Add up your fiber. Keep a bowel diary."
Right 42%: a tablet at a slight angle showing a calm, simplified tracker screen (three plain rounded result tiles and a few neat gray rows; no readable small text), beside a small bowl of mung beans and a glass of water.
Large readable labels (minimum 22 px at full size), generous whitespace, soft semi-3D rendered illustration (not flat clip-art). Font: Inter. Bottom-right corner: small navy (#1F3864) text "© renalcarematters.com", exact lowercase string, clear of every panel, arrow and label. No journal names, trial names, drug or supplement brand names, logos or other watermarks. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; real brand names or logos; implausible anatomy; frightening or disgusting gut imagery; stool shown realistically; clutter; omitting or altering the renalcarematters.com attribution.
QUALITY CHECK: Title two lines, spelled exactly; no readable text on the tablet; attribution present.
ALT TEXT: Share card for the Fiber Intake and Tolerance Tracker showing a tablet with a simple tracker screen beside a bowl of mung beans and a glass of water.
OG WIDTH: 1200
OG HEIGHT: 630

---

## Part C — Production and wiring checklist

1. Generate P1 images first, then P2, then P3 (priorities are in the inventory table). The hero (001) and share card (002) unblock link previews.
2. Save PNGs to `Downloads/Microbiome/images/` with the exact file names, then copy to the repo `images/` folder with WebP twins.
3. Run `python3 patch_responsive_images.py --guide microbiome-directed-supplements-for-kidney-health.html` and `python3 patch_og_images.py --guide microbiome-directed-supplements-for-kidney-health.html`.
4. Confirm every figure’s `<figcaption>` still carries its `fig-desc` (already authored in four languages) and `fig-abbrevs` where the image shows an acronym.
5. Check the hero inside the circular vignette on desktop and phone: the upper-left title-safe zone must be empty.
6. Proofread 010, 011, 018 and 021 digit by digit; confirm no real brand or registration number appears on 011.
7. Confirm `© renalcarematters.com` is present, exact and unobstructed on 002–023. The hero (001) is wordless by design.
8. All 20 in-guide figures are already wired with four-language captions (patient) or English captions (clinician); only file names must match. The calculator share card (023) is optional and not wired.
