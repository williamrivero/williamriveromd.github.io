# Image Plan Blueprint — Novel Regulators and Functions in Mineral Metabolism

**Guide:** `guides/novel-regulators-mineral-metabolism.html` · **Companion calculator:** `guides/calc-mineral-metabolism-workbench.html`
**Version:** 1.0 · November 11, 2026
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/
**Skills used:** `williamriveromd-hero-vignette` (001) · `williamriveromd-infographic-skill` (002, 003, 005, 007, 010, 020) · `williamriveromd-simple-figure` (004, 006, 008, 012, 016, 018, 019) · `williamriveromd-biomedical-mechanism-figure` (011, 013, 014, 015) · `williamriveromd-organ-crosstalk-sigil-graphic` (009) · `williamriveromd-algorithm-generator-skill` (017) · Stage 2 schema from `williamriveromd-local-image-generator`
**Local folder (Stage 2):** `/Users/williamgregoryrivero/Downloads/novel-regulators-mineral-metabolism/`

---

## Part A — Visual strategy

### A.1 The teaching problem the images must solve

Mineral metabolism is invisible: hormones nobody can see, ions measured in milligrams, and organs that seem unrelated (a neck gland, a bone, a kidney, an artery). Readers also need to keep two kinds of knowledge apart — what is **proven in people** and what was **seen in mice**. The plan uses one recurring visual language across both tabs, then changes only the level of detail.

| Layer | Patients & Families (all reading levels) | Clinicians (specialist precision) |
|---|---|---|
| The network | Four body parts passing glowing message capsules (003) | Evidence-coded physiology map: solid = established, dashed = experimental (010) and a calm sigil (009) |
| Compensation | “Normal number, hard work” comparison (004) | FGF23/PTH compensation narrated in text; mechanism figures 011–013 |
| New science | Six tiles, each badged **Lab** or **People** (005) | Rodent mechanisms drawn with a flask icon on every experimental arrow (011–015); evidence ladder (016) |
| Tests | Routine tubes vs a “research only” tray; trend over single value (006) | PTH ×ULN worked example (018); calcium: two measurements vs one estimate (019); low-phosphate algorithm (017) |
| Action | Filipino plate: additives vs fresh food (007); three medicine alerts (008) | Therapeutics and safety live in HTML tables (numbers stay code-native) |

**Recurring visual grammar** (written into every relevant prompt): Visual grammar (keep identical across the set): calcium shown as small pearl-white spheres, phosphate as small amber (#b8860b) spheres; hormone messengers as small glowing capsules — FGF23 teal (#1a6b72), PTH coral (#c55a11), active vitamin D sun-yellow; Klotho as a small purple (#6c3d8e) latch on a receptor; established pathways as solid teal arrows, experimental pathways as dashed purple arrows; a small flask icon marks laboratory or animal evidence and a small two-person icon marks human evidence.

### A.2 Readability rules for every patient image

1. One idea per image, readable in about 10 seconds on a phone.
2. On-image words are short English labels at roughly a grade 6 level; the four-language `fig-desc` captions already in the guide carry the explanation, so no Tagalog, Cebuano or Kapampangan text is baked into images.
3. Every analogy is shown next to the real organ (the “overtime” idea is drawn as extra hormone capsules from real bone and parathyroid, not as cartoon workers).
4. Laboratory-only ideas always carry the flask badge, so a picture never overstates the evidence.
5. This set uses no people: the hero and every figure are object- or anatomy-based (the hero skill’s non-people option), which also avoids repeating faces from earlier guides.

### A.3 Style decision: illustrated, not flat

All figures, including the mechanism figures, request **soft semi-3D rendered illustration** rather than flat vector clip-art, to match the site’s GPT-rendered aesthetic. The sigil (009) and the algorithm (017) are the two deliberate exceptions because their skills are line-art and flowchart by design.

### A.4 What stays code-native (do not generate)

Exact effect sizes, confidence intervals and trial denominators stay in the guide’s HTML tables and Evidence Scorecard, because image generators garble digits. Only two prompts contain numbers: 008 (calendar weeks 2–10) and 018 (540, 65, 88, 8.3, 6.1). **Proofread both digit by digit** before publishing.

### A.5 Image inventory and placement

| # | File (PNG + WebP twin) | Section | Audience | Skill / archetype | Size | Priority |
|---|---|---|---|---|---|---|
| 001 | `novel-regulators-mineral-metabolism-vignette-hero` | Hero | Mixed | Circular vignette hero v3 — Scaffold C anatomy · Composition C (Radial) · camera: soft three-quarter view, slightly above | 2048×2048 | **P1** |
| 002 | `novel-regulators-mineral-metabolism-og` | `<head>` | Mixed | OG / social share card | 1200×630 | **P1** |
| 003 | `novel-regulators-mineral-metabolism-01-four-organ-network` | `#p-what` | Patients and families | Patient infographic — single concept network | 1536×1024 | **P1** |
| 004 | `novel-regulators-mineral-metabolism-02-compensation-ckd` | `#p-ckd` | Patients and families | Simple figure — side-by-side comparison | 1536×1024 | **P1** |
| 005 | `novel-regulators-mineral-metabolism-03-new-discoveries-evidence` | `#p-new` | Patients and families | Patient infographic — 2×3 tile grid | 1536×1024 | **P1** |
| 006 | `novel-regulators-mineral-metabolism-05-blood-tests-card` | `#p-tests` | Patients and families | Reference card | 1536×1024 | **P2** |
| 007 | `novel-regulators-mineral-metabolism-04-phosphate-additives-plate` | `#p-help` | Patients, families, dietitians | Food matrix / photoreal editorial still life | 1536×1024 | **P1** |
| 008 | `novel-regulators-mineral-metabolism-06-medicine-safety-alerts` | `#p-safety` | Patients and families | Reference card — three columns | 1536×1024 | **P1** |
| 009 | `novel-regulators-mineral-metabolism-17-crosstalk-sigil` | `#md-overview` | Clinicians | Organ crosstalk sigil | 1024×1024 | **P3** |
| 010 | `novel-regulators-mineral-metabolism-07-physiology-map` | `#md-map` | Clinicians | Mechanism poster — organ network with evidence-coded arrows | 1536×1024 | **P1** |
| 011 | `novel-regulators-mineral-metabolism-08-kidney-phosphate-sensor-mechanism` | `#md-atlas` | Clinicians | Biomedical mechanism figure (organ → dashed inset → injury/bridge/benefit flow) | 1536×1024 | **P2** |
| 012 | `novel-regulators-mineral-metabolism-10-klotho-spatial` | `#md-atlas` | Clinicians | Simple figure — single mechanism along a nephron | 1536×1024 | **P2** |
| 013 | `novel-regulators-mineral-metabolism-09-osteoblast-gpat2-mechanism` | `#md-atlas` | Clinicians | Biomedical mechanism figure | 1536×1024 | **P2** |
| 014 | `novel-regulators-mineral-metabolism-11-calciprotein-particles` | `#md-atlas` | Clinicians | Biomedical mechanism figure (vessel inset) | 1536×1024 | **P2** |
| 015 | `novel-regulators-mineral-metabolism-12-iron-fgf23` | `#md-atlas` | Clinicians | Two-panel mechanism figure | 1536×1024 | **P2** |
| 016 | `novel-regulators-mineral-metabolism-14-evidence-ladder` | `#md-spotlight` | Mixed | Simple figure — vertical step sequence | 1024×1536 | **P2** |
| 017 | `novel-regulators-mineral-metabolism-13-phosphate-handling-algorithm` | `#md-bedside` | Clinicians | Clinical algorithm — journal style | 1024×1536 | **P1** |
| 018 | `novel-regulators-mineral-metabolism-15-pth-assay-standardization` | `#md-bedside` | Clinicians and dialysis staff | Simple figure — comparison | 1536×1024 | **P2** |
| 019 | `novel-regulators-mineral-metabolism-16-calcium-measurement` | `#md-bedside` | Clinicians | Simple figure — three-option comparison | 1536×1024 | **P2** |
| 020 | `calc-mineral-metabolism-workbench-og` | `guides/calc-mineral-metabolism-workbench.html` | Clinicians | OG / social share card | 1200×630 | **P3** |

**Production order:** 001 → 002 → 003 → 004 → 005 → 007 → 008 → 010 → 017 → then P2 (006, 011–016, 018, 019) → P3 (009, 020).

### A.6 Consistency anchors (repeat in every relevant prompt)

- Backgrounds white `#ffffff` / off-white `#fafafa`; cards `#f3f4f6` or `#eef6f7`. Never dark.
- Navy `#0f1e2e` text · teal `#1a6b72` established pathways and headings · green `#1f7a4d` safe/default · amber `#b8860b` caution and phosphate · clinical red `#b91c1c` danger · coral `#c55a11` PTH · purple `#6c3d8e` experimental evidence and Klotho.
- Font: **Inter** for every image with text.
- Attribution `© renalcarematters.com`, small, semi-transparent navy, bottom-right (bottom-center on portrait).
- No journal names, trial names, guideline acronyms, or drug brand names on any image (generic drug names only where essential: 015).

---

## Part B — Copy-ready prompts

> Paste the block under **COPY-READY IMAGE GENERATOR GPT PROMPT** into the GPT. Negative instructions and the quality check are part of the paste unless noted.

---

### 001 — Hero vignette

IMAGE NUMBER: 001
SECTION PLACEMENT: Hero — `figure.hero-figure.mode-patient > .hero-vignette` (already wired)
FILE NAME: novel-regulators-mineral-metabolism-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 — Scaffold C anatomy · Composition C (Radial) · camera: soft three-quarter view, slightly above · skill: williamriveromd-hero-vignette
AUDIENCE: Mixed
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX: photorealistic models: none (non-people hero) · 3D component graphics: kidney, bone segment, artery · 2D: none · algorithm: none
PURPOSE: Show at a glance that kidney, bone and blood vessels are one connected system, so the title reads as a story rather than jargon.
KEY CONCEPTS: Three organs; hormone messages traveling between them; minerals carried in the blood; calm, not frightening.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Radial. Camera: soft three-quarter view from slightly above.

Subject: a single healthy human kidney in soft renal pink, centered slightly right and low, floating on a calm light teal-tinted (#eef6f7) background with gentle studio lighting and a soft shadow. Around it, at a respectful distance, three supporting elements: a short cutaway segment of healthy long bone showing honeycomb trabeculae (upper right), a short translucent artery segment with a smooth inner wall (lower left), and a small hint of the paired parathyroid glands as four tiny pale-amber ovals (lower right). Thin glowing threads connect each element to the kidney; along the threads travel tiny teal and coral capsules (hormone messages) and a few pearl-white and amber micro-spheres (calcium and phosphate).

Visual hierarchy: the kidney occupies 60–70% of the circle; supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of empty soft teal gradient in the upper-left of the circle — no anatomy, threads, spheres, labels or callouts there. Soft falloff toward the rim.

Absolutely NO text, labels, leader lines, callouts, titles, logos or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders.
```
NEGATIVE INSTRUCTIONS: Busy layouts; collage; more than four supporting elements; icons; labels; cropped circle; objects touching the circular border; content inside the title-safe zone; baked-in text, logos or watermarks; rectangular frames; dark backgrounds; cartoon style; neon; HDR; gore; implausible anatomy.
QUALITY CHECK: Square 2048×2048; circle 85–90% with visible white margin; kidney dominant (60–70%); bone, artery and parathyroid read as supporting; empty upper-left title zone; wordless; calm palette matching the site.
ALT TEXT: Semi-realistic illustration of a kidney, a section of bone and a short artery floating in soft light, linked by thin glowing strands carrying tiny calcium and phosphate particles, suggesting hormone messages traveling between organs.
OG WIDTH: 2048
OG HEIGHT: 2048

---

### 002 — Open Graph share card

IMAGE NUMBER: 002
SECTION PLACEMENT: `<head>` — `og:image` / `twitter:image` (already wired)
FILE NAME: novel-regulators-mineral-metabolism-og.png
ARCHETYPE: OG / social share card · skill: williamriveromd-infographic-skill
AUDIENCE: Mixed (Facebook, Messenger, Viber previews)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX: 2D title block · 3D: the hero trio, smaller
PURPOSE: A readable, inviting link preview for patients and a signal of scientific depth for clinicians.
KEY CONCEPTS: Kidney–bone–vessel messages; “what is new and what helps.”

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean editorial social-share card, exactly 1200×630 pixels, white (#ffffff) background with a very soft light-teal (#eef6f7) panel filling the left 56%. All text in Inter.
Left side, stacked and left-aligned with generous margins:
  Small teal (#1a6b72) uppercase label: "CALCIUM · PHOSPHATE · BONE"
  Bold navy (#0f1e2e) title, two lines, large: "The Hidden Messengers of Kidney, Bone and Blood Vessels"
  Medium amber (#b8860b) subtitle: "What is new in mineral metabolism"
  Small navy line at 80% opacity: "What the science shows — and what actually helps"
Right side: the same semi-photorealistic trio as the hero — a kidney in soft renal pink, a cutaway bone segment and a short artery — linked by thin glowing threads carrying tiny teal and coral capsules and pearl-white and amber micro-spheres, floating on soft light with a gentle shadow.
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow.
Generous whitespace. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Dark backgrounds; serif or decorative fonts; misspelled or extra words; cluttered icons; neon; cartoon style; text crossing the illustration; cropped title.
QUALITY CHECK: Exactly 1200×630; title readable at 600 px wide; every word spelled as given; trio matches 001; attribution visible bottom-right.
ALT TEXT: Share card titled "The Hidden Messengers of Kidney, Bone and Blood Vessels" with an illustrated kidney, bone and artery linked by glowing hormone messages.
OG WIDTH: 1200
OG HEIGHT: 630

---

### 003 — Four organs, one balancing act (patient)

IMAGE NUMBER: 003
SECTION PLACEMENT: `#p-what`, end of section (figure 01, already wired)
FILE NAME: novel-regulators-mineral-metabolism-01-four-organ-network.png
ARCHETYPE: Patient infographic — single concept network · skill: williamriveromd-infographic-skill (multi-element) with simple-figure discipline
AUDIENCE: Patients and families (all reading levels)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D component graphics: gut, kidneys, skeleton, neck glands · 2D labels and arrows
PURPOSE: Give every reader the core mental model: four body parts share one job and talk through hormone messages.
KEY CONCEPTS: Gut absorbs; kidney keeps or releases and activates vitamin D; bone stores and sends FGF23; parathyroid glands sense calcium and send PTH.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education infographic, clean graphical-abstract style with soft semi-3D rendered organs (not flat clip-art). White (#ffffff) background. Title at top in bold navy (#0f1e2e), Inter font: "Four body parts keep calcium and phosphate balanced". Subtitle in teal (#1a6b72): "They talk through hormone messages in the blood".
Center: a calm, gender-neutral translucent human silhouette in very light gray. Inside it, rendered softly: the small intestine (lower abdomen), both kidneys (mid-back), a section of the skeleton (spine and pelvis visible), and four tiny parathyroid glands behind the thyroid in the neck.
Four rounded label cards around the figure, each with a thin leader line to its organ:
  Neck: "Parathyroid glands — sense calcium, send PTH"
  Kidneys: "Kidneys — keep or release minerals, switch on vitamin D"
  Bone: "Bones — store minerals, send FGF23"
  Gut: "Gut — absorbs calcium and phosphate from food"
Between the organs, curved solid teal arrows carry small glowing capsules: a coral capsule from neck to kidney, a teal capsule from bone to kidney, a sun-yellow capsule from kidney to gut. In the bloodstream, a few pearl-white spheres (calcium) and amber spheres (phosphate).
Small legend strip at the bottom on soft gray (#f3f4f6): pearl-white dot "Calcium", amber dot "Phosphate", coral capsule "PTH", teal capsule "FGF23", yellow capsule "Active vitamin D".
Visual grammar (keep identical across the set): calcium shown as small pearl-white spheres, phosphate as small amber (#b8860b) spheres; hormone messengers as small glowing capsules — FGF23 teal (#1a6b72), PTH coral (#c55a11), active vitamin D sun-yellow; Klotho as a small purple (#6c3d8e) latch on a receptor; established pathways as solid teal arrows, experimental pathways as dashed purple arrows; a small flask icon marks laboratory or animal evidence and a small two-person icon marks human evidence.
Large readable labels (minimum 22 px at full size), generous whitespace. Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Readable on a phone; four labels spelled exactly; arrows go neck→kidney, bone→kidney, kidney→gut; light background; attribution present.
ALT TEXT: Diagram of a human silhouette showing the gut, kidneys, bones and parathyroid glands, with arrows carrying PTH, FGF23 and active vitamin D between them and small calcium and phosphate spheres in the blood.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 004 — Compensation in early CKD (patient)

IMAGE NUMBER: 004
SECTION PLACEMENT: `#p-ckd`, end of section (figure 02)
FILE NAME: novel-regulators-mineral-metabolism-02-compensation-ckd.png
ARCHETYPE: Simple figure — side-by-side comparison · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D: kidneys, bone cell, neck glands, artery · 2D: panels, short labels
PURPOSE: Make “normal phosphate can hide strain” intuitive with the overtime metaphor walked back to real organs.
KEY CONCEPTS: Fewer nephrons; FGF23 and PTH work overtime; lab slip normal; early artery mineral flecks.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Single comparison figure for patients, soft semi-3D medical illustration, Inter font. White (#ffffff) background. Title in bold navy (#0f1e2e): "Normal phosphate can hide hard work". Two side-by-side panels with rounded borders.
Left panel header in green (#1f7a4d): "Healthy kidneys". Two healthy kidneys with many small glowing filtering units; a relaxed bone segment and calm neck glands; a lab slip icon reading "Phosphate: normal"; a smooth clean artery.
Right panel header in amber (#b8860b): "Early kidney disease". Kidneys with visibly fewer glowing filtering units; the bone segment releasing many teal capsules and the neck glands releasing many coral capsules toward the kidneys, with small motion lines suggesting effort; the same lab slip icon still reading "Phosphate: normal"; the artery shows a few tiny pale mineral flecks along its inner wall.
Under the right panel, one short line in navy: "Hormones work overtime to keep the number normal".
Visual grammar (keep identical across the set): calcium shown as small pearl-white spheres, phosphate as small amber (#b8860b) spheres; hormone messengers as small glowing capsules — FGF23 teal (#1a6b72), PTH coral (#c55a11), active vitamin D sun-yellow; Klotho as a small purple (#6c3d8e) latch on a receptor; established pathways as solid teal arrows, experimental pathways as dashed purple arrows; a small flask icon marks laboratory or animal evidence and a small two-person icon marks human evidence.
Large labels, generous whitespace. Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. Do not show faces, stress emojis, sweat drops or cartoon effort symbols.
QUALITY CHECK: The only words: title, two headers, two lab-slip lines, the caption line, attribution. Left vs right difference obvious within 5 seconds.
ALT TEXT: Side-by-side illustration: healthy kidneys with calm hormones and a normal phosphate result, versus early kidney disease with fewer filtering units, bone and parathyroid glands sending extra hormones, the same normal phosphate result, and early mineral flecks in an artery.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 005 — Six new discoveries, labeled by evidence (patient)

IMAGE NUMBER: 005
SECTION PLACEMENT: `#p-new`, after the purple alert (figure 03)
FILE NAME: novel-regulators-mineral-metabolism-03-new-discoveries-evidence.png
ARCHETYPE: Patient infographic — 2×3 tile grid · skill: williamriveromd-infographic-skill
AUDIENCE: Patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D micro-renders in each tile · 2D tile frames, icons
PURPOSE: Teach readers to separate “seen in the lab” from “seen in people” before they read the details.
KEY CONCEPTS: Phosphate sensor; bone fat-burning; Klotho zones; activin A; calcium cleanup crew; iron and FGF23.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient-education tile grid, soft semi-3D rendered micro-illustrations (not flat clip-art), Inter font, white (#ffffff) background. Title in bold navy (#0f1e2e): "New discoveries — and how sure we are". Six rounded tiles in two rows of three on soft gray (#f3f4f6), each with a short label under its picture and a small badge in its top-right corner:
1. A kidney with a tiny glowing sensor light; label "Kidney phosphate sensor"; purple flask badge "Lab".
2. A bone-building cell with a small fat droplet beside a glowing mitochondrion; label "Bone cells burn fat differently"; purple flask badge "Lab".
3. A short kidney tubule with two highlighted zones, one teal and one purple; label "Klotho works in two places"; purple flask badge "Lab".
4. A hemodialysis chair silhouette beside a small bone icon with a signal wave; label "Activin A: a bone signal"; green two-person badge "People".
5. A blood vessel cross-section with tiny round protein bubbles carrying minerals away; label "Calcium cleanup crew"; green two-person badge "People".
6. Red blood cells beside a small iron droplet and a teal capsule; label "Iron and FGF23"; green two-person badge "People".
Footer strip in purple (#6c3d8e) outline: "Lab discoveries explain disease. They are not treatments yet."
Visual grammar (keep identical across the set): calcium shown as small pearl-white spheres, phosphate as small amber (#b8860b) spheres; hormone messengers as small glowing capsules — FGF23 teal (#1a6b72), PTH coral (#c55a11), active vitamin D sun-yellow; Klotho as a small purple (#6c3d8e) latch on a receptor; established pathways as solid teal arrows, experimental pathways as dashed purple arrows; a small flask icon marks laboratory or animal evidence and a small two-person icon marks human evidence.
Large labels, generous whitespace. Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Exactly six tiles; badges: tiles 1–3 “Lab”, tiles 4–6 “People”; every label spelled as given.
ALT TEXT: Grid of six illustrated tiles showing recent discoveries in mineral metabolism, each tagged as laboratory evidence (flask) or human evidence (people).
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 006 — Your blood tests (patient)

IMAGE NUMBER: 006
SECTION PLACEMENT: `#p-tests`, after the teal alert (figure 05)
FILE NAME: novel-regulators-mineral-metabolism-05-blood-tests-card.png
ARCHETYPE: Reference card · skill: williamriveromd-simple-figure (reference card)
AUDIENCE: Patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 2D card, tube icons, simple trend line
PURPOSE: Show which tests guide care, that trends beat single results, and that research tests sit apart.
KEY CONCEPTS: Calcium, phosphate, PTH, ALP, vitamin D; trend over time; research tests separate.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean patient reference card, Inter font, white (#ffffff) background, soft semi-3D glass lab tubes (not flat icons). Title in bold navy (#0f1e2e): "Your mineral blood tests".
Top row: five upright lab tubes on a soft gray (#f3f4f6) shelf with short labels underneath: "Calcium", "Phosphate", "PTH", "ALP", "Vitamin D".
Middle: a simple, wide line graph with five gently rising-then-leveling dots over a time axis labeled only "Months" — caption beside it in teal (#1a6b72): "Follow the trend, not one result".
Bottom right: a separate, slightly faded tray of three tubes labeled "FGF23", "Klotho", "T50" with a purple (#6c3d8e) tag "Research only".
Bottom left small note in navy: "Compare PTH with your own lab’s range".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. No numbers on the graph axes or tubes.
QUALITY CHECK: Eight tube labels spelled exactly; no numerals anywhere; research tray clearly separated.
ALT TEXT: Reference card showing five routine tests — calcium, phosphate, PTH, ALP and vitamin D — a trend line labeled follow the trend, and a separate tray of research-only tests FGF23, Klotho and T50.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 007 — Phosphate additives on the Filipino plate (patient)

IMAGE NUMBER: 007
SECTION PLACEMENT: `#p-help`, end of the check-list (figure 04)
FILE NAME: novel-regulators-mineral-metabolism-04-phosphate-additives-plate.png
ARCHETYPE: Food matrix / photoreal editorial still life · skill: williamriveromd-infographic-skill (food matrix)
AUDIENCE: Patients, families, dietitians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Photorealistic food · 2D small tags
PURPOSE: Turn “limit additive phosphate” into a picture any reader recognizes from their own table.
KEY CONCEPTS: Processed foods with phosphate additives vs fresh home-cooked meal; protein kept.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Bright, naturally lit top-down food photograph style, white (#ffffff) table surface, two plates side by side, Inter font for the few labels.
Left plate on a pale amber (#fdf3e1) placemat, header above in amber (#b8860b): "Often high in added phosphate". On it: two sliced hotdogs, a small longganisa, a slice of luncheon meat, a small bowl of instant noodles, and beside the plate a glass of dark cola and a sachet of 3-in-1 coffee mix. Three or four tiny round tags reading "phos" sit next to items.
Right plate on a pale green (#e8f3ec) placemat, header in green (#1f7a4d): "Fresh, home-cooked". On it: steamed white rice, a piece of grilled fresh fish (bangus), sautéed green vegetables (kangkong), sliced tomato, and beside it a glass of water with a calamansi slice.
Bottom strip on soft gray (#f3f4f6), navy text: "Choose fresh food. Keep your protein. Ask your dietitian."
Bright, airy, realistic, appetizing; no people; no packaging logos or brand names visible.
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. Visible brand logos or packaging text; moody lighting; rotten or unappetizing food; people.
QUALITY CHECK: No brand logos; both headers and the bottom line spelled exactly; tags read “phos” only; fresh plate includes protein (fish).
ALT TEXT: Two Filipino plates: processed foods with phosphate additives such as hotdog, longganisa, luncheon meat, instant noodles and cola, beside a fresh home-cooked plate of rice, grilled fish, vegetables and calamansi water.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 008 — Three medicine alerts (patient)

IMAGE NUMBER: 008
SECTION PLACEMENT: `#p-safety`, end of section (figure 06)
FILE NAME: novel-regulators-mineral-metabolism-06-medicine-safety-alerts.png
ARCHETYPE: Reference card — three columns · skill: williamriveromd-simple-figure
AUDIENCE: Patients and families
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: 3D objects in each card · 2D frames
PURPOSE: Make the three safety messages memorable without numbers.
KEY CONCEPTS: Some IV iron lowers phosphate; denosumab needs calcium checks weeks 2–10 in advanced CKD; supplements have not reversed artery calcium.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Patient safety card, Inter font, white (#ffffff) background, three tall rounded cards side by side with soft semi-3D objects (not flat icons). Title in bold navy (#0f1e2e): "Three medicine alerts".
Card 1, amber (#b8860b) border, header "Some iron drips lower phosphate": an IV iron bag on a drip stand with a small downward amber arrow beside an amber sphere; footer "Report new weakness or bone pain".
Card 2, red (#b91c1c) border, header "Denosumab: check calcium": a prefilled injection pen beside a simple calendar with weeks 2 to 10 highlighted and a blood tube; footer "Do not stop it on your own".
Card 3, purple (#6c3d8e) border, header "Supplements are not artery cleaners": a supplement bottle beside an artery segment with a gentle crossed-out sparkle; footer "Ask before you start".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. Drug brand names on the pen or bag; syringes with needles pointing at people.
QUALITY CHECK: The only numerals are the highlighted calendar weeks 2–10; every header and footer spelled exactly; no brand names.
ALT TEXT: Three safety cards: an iron drip that can lower phosphate, a denosumab pen with a calendar highlighting weeks 2 to 10 for calcium checks, and a supplement bottle that does not clean arteries.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 009 — Mineral crosstalk sigil (clinician)

IMAGE NUMBER: 009
SECTION PLACEMENT: `#md-overview`, end of section (figure 17)
FILE NAME: novel-regulators-mineral-metabolism-17-crosstalk-sigil.png
ARCHETYPE: Organ crosstalk sigil · skill: williamriveromd-organ-crosstalk-sigil-graphic
AUDIENCE: Clinicians (also works for mixed)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX: Monoline line-art only
PURPOSE: A calm symbolic anchor for the clinician tab: the network is a loop, not a chain.
KEY CONCEPTS: Kidney center; bone, gut, parathyroid, marrow, artery around it; dotted loops.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a simple medical organ-crosstalk sigil illustration featuring the kidney at the center, a long bone above, the small intestine at the left, the parathyroid glands at the upper right, bone marrow red cells at the lower left and an artery segment at the lower right.
RELATIONSHIP: show two-way mineral-hormone signaling with dotted curved arrows looping from each organ to the kidney and back, forming a balanced radial pattern; two of the loops (bone↔kidney and marrow↔kidney) slightly brighter teal.
STYLE: minimal clinical line-art, thin monoline strokes, soft teal-blue and slate palette, white background, clean rounded organ shapes, generous whitespace, balanced sigil-like composition, no photorealism, no 3D, no text labels.
OUTPUT: square, clean margins, high resolution. Include a small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner, not obscuring the sigil.
```
NEGATIVE INSTRUCTIONS: Photorealistic anatomy, surgical detail, labels, dark background, neon colors, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, serif fonts; never omit the attribution.
QUALITY CHECK: Six recognizable organ icons; dotted loops symmetrical; no words except the attribution.
ALT TEXT: Monoline sigil with the kidney at the center linked by dotted loops to bone, gut, parathyroid glands, bone marrow and an artery.
OG WIDTH: 1024
OG HEIGHT: 1024

---

### 010 — Physiology map (clinician)

IMAGE NUMBER: 010
SECTION PLACEMENT: `#md-map`, after the first paragraph (figure 07)
FILE NAME: novel-regulators-mineral-metabolism-07-physiology-map.png
ARCHETYPE: Mechanism poster — organ network with evidence-coded arrows · skill: williamriveromd-infographic-skill (pathophysiology poster)
AUDIENCE: Clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Soft semi-3D organs · 2D arrows, short labels, legend
PURPOSE: One map that shows every connection and whether it is established (solid) or experimental (dashed), with the static table beneath as the text equivalent.
KEY CONCEPTS: PTH→kidney; FGF23–Klotho→kidney; calcitriol→gut; kidney G-3-P→bone (dashed); osteoblast GPAT2 (dashed); PTH–SIK (dashed); erythroid FGF23 (dashed); CPP in vessel; PPi.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Publication-grade clinician mechanism map, soft semi-3D rendered organs with restrained shading (not flat vector), white (#ffffff) background, Inter font, generous whitespace. Title top-left in bold navy (#0f1e2e): "Mineral metabolism network".
Layout: kidney large at center; parathyroid glands above; bone with an inset osteocyte and bone marrow at left; small intestine below; an artery wall cross-section at right.
SOLID teal (#1a6b72) arrows with short labels:
  parathyroid → kidney: "PTH"
  bone → kidney: "FGF23 + Klotho"
  kidney → intestine: "Calcitriol"
  intestine → blood: "Calcium, phosphate"
DASHED purple (#6c3d8e) arrows with short labels and a tiny flask icon on each:
  kidney → bone: "G-3-P signal"
  inside bone: "GPAT2"
  inside kidney near PTH arrival: "PTH–SIK"
  marrow → red cells: "Erythroid FGF23"
In the artery panel: pale protein bubbles labeled "CPP" next to a small label "PPi" at the vessel wall.
Legend box bottom-left on soft gray (#f3f4f6): solid teal line "Established in humans"; dashed purple line "Experimental (animal models)"; flask icon "Lab evidence"; two-person icon "Human evidence".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Proofread every label: PTH, FGF23 + Klotho, Calcitriol, Calcium, phosphate, G-3-P signal, GPAT2, PTH–SIK, Erythroid FGF23, CPP, PPi; solid vs dashed exactly as specified.
ALT TEXT: Map of kidney, parathyroid, bone, marrow, gut and artery wall: solid arrows for established PTH, FGF23 with Klotho and calcitriol pathways, and dashed arrows for experimental G-3-P, GPAT2, PTH–SIK and erythroid FGF23 pathways.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 011 — Kidney phosphate sensor (clinician)

IMAGE NUMBER: 011
SECTION PLACEMENT: `#md-atlas`, after the atlas cards (figure 08)
FILE NAME: novel-regulators-mineral-metabolism-08-kidney-phosphate-sensor-mechanism.png
ARCHETYPE: Biomedical mechanism figure (organ → dashed inset → injury/bridge/benefit flow) · skill: williamriveromd-biomedical-mechanism-figure
AUDIENCE: Clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D organ and cell · 2D callouts and bottom flow
PURPOSE: Show the 2023–2026 rodent kidney-to-bone loop precisely, with experimental status visible without hovering.
KEY CONCEPTS: NPT2a uptake; glycolysis; Gpd1 → G-3-P; NAD⁺ recycling; G-3-P to bone; osteocyte FGF23; phosphaturia; rodent only.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Publication-grade biomedical mechanism figure in scientific review-article style with soft semi-3D shading (not flat clip-art). White background, Inter font, muted clinical palette, thin dashed connector lines.
Left organ panel: a kidney cross-section in light gray-blue labeled "Phosphate load"; a small dashed box on the cortex connects to the main panel.
Center magnified panel in a dashed border: one proximal tubule cell, brush border on top. Callouts: "NPT2a: phosphate uptake", "↑ Glycolysis", "Gpd1 → G-3-P", "NAD⁺ recycling". An arrow carries small purple G-3-P dots out of the basolateral side into a capillary.
Right panel: a bone segment with an inset osteocyte releasing teal FGF23 capsules, labeled "Osteocyte → FGF23"; a dashed purple return arrow to the kidney labeled "↑ Phosphate excretion".
Bottom flow of three boxes with arrows: pale-pink box "Phosphate load" → pale-lavender box "Kidney-to-bone signal (mouse, rat)" with a flask icon → pale-blue box "Phosphaturia; limits hyperphosphatemia".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. Do not imply a clinical test or drug.
QUALITY CHECK: Labels exactly: Phosphate load, NPT2a: phosphate uptake, ↑ Glycolysis, Gpd1 → G-3-P, NAD⁺ recycling, Osteocyte → FGF23, ↑ Phosphate excretion, Kidney-to-bone signal (mouse, rat), Phosphaturia; limits hyperphosphatemia.
ALT TEXT: Mechanism figure: phosphate entering a proximal tubule cell increases glycolysis and glycerol-3-phosphate production, which travels to bone and triggers osteocyte FGF23 release, increasing phosphate excretion; marked as rodent evidence.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 012 — Spatial Klotho (clinician)

IMAGE NUMBER: 012
SECTION PLACEMENT: `#md-atlas`, after figure 08 (figure 10)
FILE NAME: novel-regulators-mineral-metabolism-10-klotho-spatial.png
ARCHETYPE: Simple figure — single mechanism along a nephron · skill: williamriveromd-simple-figure (defers style to the mechanism skill)
AUDIENCE: Clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D nephron · 2D zone labels
PURPOSE: Make “proximal Klotho for phosphate, distal Klotho for calcium” visible at once.
KEY CONCEPTS: Proximal tubule zone; DCT/CNT zone; TRPV5 calcium reabsorption; urinary soluble Klotho; mouse evidence.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean clinician figure of one nephron in soft semi-3D rendering on white (#ffffff), Inter font. Title in bold navy (#0f1e2e): "Klotho has two jobs along the nephron".
The nephron runs left to right: glomerulus, proximal tubule highlighted in teal (#1a6b72), loop, then the distal convoluted tubule and connecting tubule highlighted in purple (#6c3d8e), then the collecting duct.
Teal zone callout: "Proximal Klotho: phosphate control"; small amber spheres leaving into the tubular fluid.
Purple zone callout: "Distal Klotho: calcium reabsorption (TRPV5)"; small pearl-white spheres moving back into a capillary through channel shapes; second callout "Source of urinary Klotho" with small purple fragments flowing into the urine.
Bottom note on soft gray (#f3f4f6) with a flask icon: "Mouse studies, 2026 — no human Klotho test cutoff".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Anatomical order correct; labels exactly as given; flask icon present.
ALT TEXT: Nephron illustration with the proximal tubule highlighted for Klotho-dependent phosphate control and the distal convoluted and connecting tubules highlighted for calcium reabsorption through TRPV5 and the release of urinary Klotho, based on mouse studies.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 013 — Osteoblast GPAT2 (clinician)

IMAGE NUMBER: 013
SECTION PLACEMENT: `#md-atlas`, after figure 10 (figure 09)
FILE NAME: novel-regulators-mineral-metabolism-09-osteoblast-gpat2-mechanism.png
ARCHETYPE: Biomedical mechanism figure · skill: williamriveromd-biomedical-mechanism-figure
AUDIENCE: Clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D bone and osteoblast · 2D callouts and bottom flow
PURPOSE: Explain the September 2026 GPAT2 finding as a fuel-routing switch, flagged as preclinical.
KEY CONCEPTS: Fatty acids → GPAT2 → LPA → FGF23; less β-oxidation; less phosphate into bone; bone-targeted inhibitor in mice.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Publication-grade biomedical mechanism figure, review-article style with soft semi-3D shading, white background, Inter font, thin dashed connectors.
Left organ panel: a long bone in light gray-blue labeled "CKD bone"; a dashed box on its surface connects to the main panel.
Center magnified panel in a dashed border: one osteoblast. Fatty acid droplets enter. A fork: one branch toward glowing mitochondria labeled "↓ Fatty acid oxidation"; the main branch through an enzyme shape labeled "GPAT2 ↑" toward "LPA" and then teal FGF23 capsules leaving the cell labeled "↑ FGF23". Beside the cell, mineralizing matrix with fewer amber spheres labeled "↓ Phosphate into bone".
Bottom flow: pale-pink box "CKD: GPAT2 rises in osteoblasts" → pale-lavender box "Bone-targeted GPAT inhibitor (experimental, mouse)" with a flask icon → pale-blue box "Better bone mineral; less vascular calcification and cardiac hypertrophy in models".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. No dosing, no human patient, no pill bottle.
QUALITY CHECK: Labels exactly as given; “experimental, mouse” visible; no numbers.
ALT TEXT: Mechanism figure: in CKD models, osteoblast GPAT2 diverts fatty acids from mitochondrial oxidation toward lysophosphatidic acid and FGF23, reducing phosphate incorporation into bone; an experimental bone-targeted inhibitor improved bone and cardiovascular features in mice.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 014 — Calciprotein particles and T50 (clinician)

IMAGE NUMBER: 014
SECTION PLACEMENT: `#md-atlas`, after figure 09 (figure 11)
FILE NAME: novel-regulators-mineral-metabolism-11-calciprotein-particles.png
ARCHETYPE: Biomedical mechanism figure (vessel inset) · skill: williamriveromd-biomedical-mechanism-figure
AUDIENCE: Clinicians (also usable for advanced patients)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D vessel, particles · 2D callouts, test-tube inset
PURPOSE: Show buffering versus injury and make clear that T50 is a test-tube assay.
KEY CONCEPTS: Fetuin-A → CPM → CPP1 cleared; CPP2 crystalline, pro-inflammatory; T50 ex vivo.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Publication-grade biomedical mechanism figure, review-article style with soft semi-3D shading, white background, Inter font.
Main panel: a large blood vessel cut in cross-section. In the lumen, from left to right: fetuin-A proteins (small blue globules) wrapping pearl-white and amber ions into tiny round particles labeled "CPM", then soft round clusters labeled "CPP1 (amorphous)" with a curved arrow toward a liver-shaped silhouette labeled "Cleared in minutes"; then larger angular crystalline clusters labeled "CPP2 (crystalline)" attached to an inflamed, slightly reddened inner wall with early mineral flecks, labeled "Inflammation, calcification".
Inset box upper right, dashed border: a test tube of serum with a small timer icon labeled "T50: serum calcification propensity (test tube)" and a small note "Not a CT calcium score".
Bottom flow: pale-blue box "Buffering" → pale-pink box "Buffer overwhelmed in CKD" → pale-lavender box "Therapies: research stage".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Labels exactly as given; CPP1 shown being cleared; CPP2 at the inflamed wall; inset says test tube and not a CT score.
ALT TEXT: Blood vessel illustration: fetuin-A packages excess calcium and phosphate into calciprotein monomers and soft primary particles that are cleared, while crystalline secondary particles adhere to an inflamed vessel wall; an inset explains that T50 is a test-tube measure, not a calcium scan.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 015 — Iron and FGF23 (clinician)

IMAGE NUMBER: 015
SECTION PLACEMENT: `#md-atlas`, after figure 11 (figure 12)
FILE NAME: novel-regulators-mineral-metabolism-12-iron-fgf23.png
ARCHETYPE: Two-panel mechanism figure · skill: williamriveromd-biomedical-mechanism-figure
AUDIENCE: Clinicians
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D marrow, osteocyte, IV bag, kidney · 2D labels
PURPOSE: Link the mouse erythroid biology to the human IV iron problem while keeping the evidence labels separate.
KEY CONCEPTS: Furin cleavage; intact vs C-terminal FGF23; erythroid FGFR1; FCM → FGF23 → phosphaturia.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Two-panel clinician figure with soft semi-3D shading, white background, Inter font, thin divider line between panels.
Left panel header with a flask icon: "Marrow and bone (mouse)". An osteocyte and a cluster of erythroid precursors both release teal FGF23 capsules; small scissors labeled "Furin" cut some capsules into two fragments labeled "C-terminal fragments"; an intact capsule docks on a receptor on a red cell precursor labeled "Intact FGF23 → FGFR1 → slower red cell production".
Right panel header with a two-person icon: "Iron infusion (people)". An IV bag labeled "Ferric carboxymaltose" with an arrow to more intact teal capsules, then to a kidney losing amber spheres into urine labeled "Renal phosphate loss", and a small gauge with the needle in a low zone labeled "Serum phosphate".
Footer note on soft gray (#f3f4f6): "Intact and C-terminal FGF23 tests measure different things".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. No brand names; no numbers on the gauge.
QUALITY CHECK: Panel headers and evidence icons correct; labels spelled exactly; the drug label is the generic name only.
ALT TEXT: Two panels: in mice, osteocytes and erythroid precursors make FGF23, furin cleaves some of it, and intact FGF23 slows red cell production through FGFR1; in people, ferric carboxymaltose increases intact FGF23 activity and renal phosphate loss.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 016 — Evidence ladder (mixed)

IMAGE NUMBER: 016
SECTION PLACEMENT: `#md-spotlight`, after the table (figure 14)
FILE NAME: novel-regulators-mineral-metabolism-14-evidence-ladder.png
ARCHETYPE: Simple figure — vertical step sequence · skill: williamriveromd-simple-figure
AUDIENCE: Mixed (clinicians; also teaches patients)
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX: 2D ladder with soft semi-3D icons
PURPOSE: One picture of why a strong mouse study can still be “research only.”
KEY CONCEPTS: Lab → human association → surrogate trial → outcome trial → graded guideline; readiness rises alongside.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Vertical evidence ladder, portrait, white (#ffffff) background, Inter font, soft semi-3D icons on each rung. Title at top in bold navy (#0f1e2e): "How a discovery reaches the bedside".
Five rungs from bottom to top, each a rounded bar with an icon at left:
  1 (purple #6c3d8e): flask icon — "Cell and animal studies"
  2 (amber #b8860b): two people with a link icon — "Human association"
  3 (teal #1a6b72): scan icon — "Trial: lab or imaging change"
  4 (green #1f7a4d): heart-and-person icon — "Trial: outcomes patients feel"
  5 (navy #0f1e2e): open book icon — "Graded guideline"
A slim arrow along the right side rising from bottom to top labeled "Clinical readiness".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Five rungs in the stated order; labels exactly as given; portrait 1024×1536; attribution bottom-center.
ALT TEXT: Five-rung ladder from cell and animal studies, to human association, to trials of laboratory or imaging change, to trials of outcomes patients feel, to graded guidelines, with clinical readiness rising alongside.
OG WIDTH: 1024
OG HEIGHT: 1536

---

### 017 — Low phosphate algorithm (clinician)

IMAGE NUMBER: 017
SECTION PLACEMENT: `#md-bedside`, after the first two paragraphs (figure 13)
FILE NAME: novel-regulators-mineral-metabolism-13-phosphate-handling-algorithm.png
ARCHETYPE: Clinical algorithm — journal style · skill: williamriveromd-algorithm-generator-skill
AUDIENCE: Clinicians
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX: 2D flowchart only
PURPOSE: A bedside path from confirmed hypophosphatemia to renal versus non-renal causes, with applicability limits beside it.
KEY CONCEPTS: Confirm; shift / intake-GI / renal; paired fasting sample; FEPO4, TRP, TmP/GFR; low TmP/GFR → FGF23-mediated vs non-FGF23 causes.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Create a clean journal-style clinical algorithm flowchart, portrait 1024×1536, white background, centered top-to-bottom logic, rounded rectangles for actions, diamonds for decisions, thin navy arrows, muted pastel fills (teal, lavender, pale amber, pale green), crisp navy text in Inter only, consistent node sizes, generous margins.
Nodes in order:
1 (rectangle, teal): "Low serum phosphate — confirmed on repeat"
2 (diamond): "Shift? (refeeding, insulin, alkalosis)" — Yes branch to a side node "Treat the cause; recheck"
3 (diamond): "Low intake or gut loss?" — Yes branch to a side node "Nutrition and gut review"
4 (rectangle, lavender): "Paired fasting serum + urine: phosphate, creatinine"
5 (rectangle, lavender): "Calculate FEPO4, TRP, TmP/GFR"
6 (diamond): "TmP/GFR low for an adult?"
  Yes → 7a (rectangle, pale amber): "Renal phosphate loss" → two small boxes side by side: "FGF23-mediated: recent ferric carboxymaltose, XLH, TIO" and "Not FGF23: PTH excess, proximal tubulopathy"
  No → 7b (rectangle, pale green): "Kidney conserving — revisit shift and intake"
Side note box (pale gray, right margin, not connected): "Not interpretable: dialysis, anuria. Unstable: AKI, non-paired or non-fasting samples, recent replacement."
Include a small professional footer reading "© renalcarematters.com" at the bottom center in subtle gray.
```
NEGATIVE INSTRUCTIONS: Photorealistic people, cartoon styling, dark background, serif fonts, overlapping arrows, numbers or thresholds not listed, misspelled abbreviations, decorative icons.
QUALITY CHECK: Proofread every node; abbreviations exactly FEPO4, TRP, TmP/GFR, XLH, TIO, PTH, AKI; no numeric cutoffs anywhere.
ALT TEXT: Algorithm for low phosphate: confirm, exclude shift and intake or gut loss, collect a paired fasting sample, calculate FEPO4, TRP and TmP/GFR, then separate renal phosphate loss (FGF23-mediated or not) from appropriate conservation, with interpretation limits listed.
OG WIDTH: 1024
OG HEIGHT: 1536

---

### 018 — PTH assay standardization (clinician)

IMAGE NUMBER: 018
SECTION PLACEMENT: `#md-bedside`, after puzzle 2 (figure 15)
FILE NAME: novel-regulators-mineral-metabolism-15-pth-assay-standardization.png
ARCHETYPE: Simple figure — comparison · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians and dialysis staff
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D analyzers and tube · 2D ratio bars and trend line
PURPOSE: Make the ×ULN idea and the trend break obvious with one worked example.
KEY CONCEPTS: Same sample, two assays; 540 pg/mL; ULN 65 vs 88; 8.3 vs 6.1 × ULN; break the line at an assay change.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clinician comparison figure, white (#ffffff) background, soft semi-3D laboratory analyzers (not flat icons), Inter font. Title in bold navy (#0f1e2e): "Read PTH against its own assay".
Top: one blood tube splits by two arrows into two analyzers labeled "Assay A" and "Assay B". Under each, a small result card:
  Assay A card: "PTH 540 pg/mL", "Upper limit 65", and a teal bar labeled "8.3 × ULN".
  Assay B card: "PTH 540 pg/mL", "Upper limit 88", and a teal bar labeled "6.1 × ULN".
Bottom: a simple trend line of dots over time that stops, leaves a visible gap with a small amber label "Assay changed", and restarts at a different level.
Footer line in navy: "Same number, different meaning — record the assay and break the trend line".
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Numbers exactly: 540, 65, 88, 8.3, 6.1 — no others; ULN spelled as given; visible gap in the trend line.
ALT TEXT: Two laboratory analyzers give the same PTH value of 540 pg/mL, which equals 8.3 times the upper limit on an assay with an upper limit of 65 but 6.1 times on an assay with an upper limit of 88; a trend line breaks where the assay changes.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 019 — Three ways to report calcium (clinician)

IMAGE NUMBER: 019
SECTION PLACEMENT: `#md-bedside`, after puzzle 4 (figure 16)
FILE NAME: novel-regulators-mineral-metabolism-16-calcium-measurement.png
ARCHETYPE: Simple figure — three-option comparison · skill: williamriveromd-simple-figure
AUDIENCE: Clinicians (also useful for nurses)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX: Semi-3D tubes and syringe · 2D labels, albumin carriers
PURPOSE: Separate two measurements from one estimate, and show why the estimate fails in hypoalbuminemia.
KEY CONCEPTS: Measured total calcium; albumin-adjusted estimate; ionized calcium measured directly; albumin carrying calcium.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clinician comparison figure, white (#ffffff) background, soft semi-3D objects, Inter font. Title in bold navy (#0f1e2e): "Calcium: two measurements and one estimate".
Three columns:
  1. A serum blood tube with a green (#1f7a4d) check badge, label "Measured total calcium", sub-label "Default result".
  2. A calculator icon over a faded tube with an amber (#b8860b) caution triangle, label "Albumin-adjusted estimate", sub-label "Least reliable when albumin is low".
  3. A blood-gas syringe with a green check badge, label "Ionized calcium, measured directly", sub-label "Use when a decision depends on it".
Background behind the columns: soft illustration of albumin proteins (pale blue globules) each carrying a few pearl-white calcium spheres, with a few free pearl-white spheres floating between them.
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution. No numbers or formulas.
QUALITY CHECK: Three labels and sub-labels exactly as given; caution only on the adjusted estimate; no numerals.
ALT TEXT: Three options for reporting calcium: measured total calcium as the default, an albumin-adjusted estimate marked with caution because it is least reliable when albumin is low, and ionized calcium measured directly.
OG WIDTH: 1536
OG HEIGHT: 1024

---

### 020 — Workbench share card (calculator, optional)

IMAGE NUMBER: 020
SECTION PLACEMENT: `guides/calc-mineral-metabolism-workbench.html` — replace the fallback `hero-cat-ckd-risk.png` in og:image/twitter:image after generation
FILE NAME: calc-mineral-metabolism-workbench-og.png
ARCHETYPE: OG / social share card · skill: williamriveromd-infographic-skill
AUDIENCE: Clinicians
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX: 2D title block · semi-3D tablet with a clean chart
PURPOSE: Give the new calculator its own recognizable thumbnail in the Latest Calculators carousel.
KEY CONCEPTS: Phosphate handling, PTH trends, calcium ledger.

COPY-READY IMAGE GENERATOR GPT PROMPT:
```
Clean editorial share card, exactly 1200×630, white (#ffffff) background with a light-teal (#eef6f7) panel on the left 56%. Inter font.
Left, stacked: small teal (#1a6b72) uppercase label "CLINICAL CALCULATOR"; bold navy (#0f1e2e) title "Mineral Metabolism Workbench"; medium amber (#b8860b) subtitle "Phosphate handling · PTH trends · Calcium ledger".
Right: a semi-3D tablet on a soft shadow showing a calm dashboard with three small line charts and a few pearl-white and amber spheres floating beside it; no numbers on the screen.
Bottom-right corner: small semi-transparent navy text "© renalcarematters.com" (bottom-center on portrait), never inside a panel or arrow. No journal names, trial names, guideline acronyms, drug brand names, or watermarks other than the renalcarematters.com attribution. Spell every word exactly as given; add no other words.
```
NEGATIVE INSTRUCTIONS: Flat clip-art or plain vector look; cartoon style; dark, navy, charcoal or black backgrounds; neon, HDR or over-saturation; serif or decorative fonts (Inter only); tiny unreadable labels; AI gibberish text; misspelled or extra words; numbers not listed in the prompt; implausible anatomy; gore; clutter; omitting the renalcarematters.com attribution.
QUALITY CHECK: Exactly 1200×630; three text lines spelled exactly; no numerals on the tablet.
ALT TEXT: Share card for the Mineral Metabolism Workbench calculator showing a tablet with a calm dashboard of trend charts.
OG WIDTH: 1200
OG HEIGHT: 630

---

## Part C — Production and wiring checklist

1. **Generate** in the order in A.5. Save each output as `generated-images/NNN-[file-name].png` in the local folder.
2. **Proofread** every text-bearing image. Reject any image with a misspelled word, an extra word, a brand name, or a wrong number. Prompts 010, 011, 013, 015, 017 and 018 need a label-by-label check against the guide.
3. **Convert** each PNG to a WebP twin (quality ~82) and place both in `images/` using the exact file names above.
4. **Already wired:** every figure (01–17), the hero vignette and the OG image are referenced in the guide with alt text, a four-language `fig-desc` (patient figures) and a `fig-abbrevs` list. Once files exist, the current missing-image placeholders clear. If a generated image adds an acronym not in its `fig-abbrevs`, add it there and to the glossary, then rerun `audit_acronym_expansion.py --guide novel-regulators-mineral-metabolism.html`.
5. **After upload:** run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py` and `patch_image_lightbox.py` for the guide, then `generate_latest_guides.py` (the strip uses the OG image). For 020, change the calculator’s `og:image` and `twitter:image` to `calc-mineral-metabolism-workbench-og.png`, then run `generate_latest_calculators.py`.

## Part D — Stage 2 manifest rows (`image-manifest.csv`)

```
image_number,section_placement,file_name,archetype,audience,aspect_ratio,width,height,status,alt_text
001,"Hero",novel-regulators-mineral-metabolism-vignette-hero.png,"Circular vignette hero v3 — Scaffold C anatomy · Composition C (Radial) · camera: soft three-quarter view, slightly above","Mixed",1:1,2048,2048,prompted,"Semi-realistic illustration of a kidney, a section of bone and a short artery floating in soft light, linked by thin glowing strands carrying tiny calcium and phosphate particles, suggesting hormone messages traveling between organs."
002,"<head>",novel-regulators-mineral-metabolism-og.png,"OG / social share card","Mixed",1.91:1,1200,630,prompted,"Share card titled 'The Hidden Messengers of Kidney, Bone and Blood Vessels' with an illustrated kidney, bone and artery linked by glowing hormone messages."
003,"#p-what",novel-regulators-mineral-metabolism-01-four-organ-network.png,"Patient infographic — single concept network","Patients and families",3:2,1536,1024,prompted,"Diagram of a human silhouette showing the gut, kidneys, bones and parathyroid glands, with arrows carrying PTH, FGF23 and active vitamin D between them and small calcium and phosphate spheres in the blood."
004,"#p-ckd",novel-regulators-mineral-metabolism-02-compensation-ckd.png,"Simple figure — side-by-side comparison","Patients and families",3:2,1536,1024,prompted,"Side-by-side illustration: healthy kidneys with calm hormones and a normal phosphate result, versus early kidney disease with fewer filtering units, bone and parathyroid glands sending extra hormones, the same normal phosphate result, and early mineral flecks in an artery."
005,"#p-new",novel-regulators-mineral-metabolism-03-new-discoveries-evidence.png,"Patient infographic — 2×3 tile grid","Patients and families",3:2,1536,1024,prompted,"Grid of six illustrated tiles showing recent discoveries in mineral metabolism, each tagged as laboratory evidence (flask) or human evidence (people)."
006,"#p-tests",novel-regulators-mineral-metabolism-05-blood-tests-card.png,"Reference card","Patients and families",3:2,1536,1024,prompted,"Reference card showing five routine tests — calcium, phosphate, PTH, ALP and vitamin D — a trend line labeled follow the trend, and a separate tray of research-only tests FGF23, Klotho and T50."
007,"#p-help",novel-regulators-mineral-metabolism-04-phosphate-additives-plate.png,"Food matrix / photoreal editorial still life","Patients, families, dietitians",3:2,1536,1024,prompted,"Two Filipino plates: processed foods with phosphate additives such as hotdog, longganisa, luncheon meat, instant noodles and cola, beside a fresh home-cooked plate of rice, grilled fish, vegetables and calamansi water."
008,"#p-safety",novel-regulators-mineral-metabolism-06-medicine-safety-alerts.png,"Reference card — three columns","Patients and families",3:2,1536,1024,prompted,"Three safety cards: an iron drip that can lower phosphate, a denosumab pen with a calendar highlighting weeks 2 to 10 for calcium checks, and a supplement bottle that does not clean arteries."
009,"#md-overview",novel-regulators-mineral-metabolism-17-crosstalk-sigil.png,"Organ crosstalk sigil","Clinicians",1:1,1024,1024,prompted,"Monoline sigil with the kidney at the center linked by dotted loops to bone, gut, parathyroid glands, bone marrow and an artery."
010,"#md-map",novel-regulators-mineral-metabolism-07-physiology-map.png,"Mechanism poster — organ network with evidence-coded arrows","Clinicians",3:2,1536,1024,prompted,"Map of kidney, parathyroid, bone, marrow, gut and artery wall: solid arrows for established PTH, FGF23 with Klotho and calcitriol pathways, and dashed arrows for experimental G-3-P, GPAT2, PTH–SIK and erythroid FGF23 pathways."
011,"#md-atlas",novel-regulators-mineral-metabolism-08-kidney-phosphate-sensor-mechanism.png,"Biomedical mechanism figure (organ → dashed inset → injury/bridge/benefit flow)","Clinicians",3:2,1536,1024,prompted,"Mechanism figure: phosphate entering a proximal tubule cell increases glycolysis and glycerol-3-phosphate production, which travels to bone and triggers osteocyte FGF23 release, increasing phosphate excretion; marked as rodent evidence."
012,"#md-atlas",novel-regulators-mineral-metabolism-10-klotho-spatial.png,"Simple figure — single mechanism along a nephron","Clinicians",3:2,1536,1024,prompted,"Nephron illustration with the proximal tubule highlighted for Klotho-dependent phosphate control and the distal convoluted and connecting tubules highlighted for calcium reabsorption through TRPV5 and the release of urinary Klotho, based on mouse studies."
013,"#md-atlas",novel-regulators-mineral-metabolism-09-osteoblast-gpat2-mechanism.png,"Biomedical mechanism figure","Clinicians",3:2,1536,1024,prompted,"Mechanism figure: in CKD models, osteoblast GPAT2 diverts fatty acids from mitochondrial oxidation toward lysophosphatidic acid and FGF23, reducing phosphate incorporation into bone; an experimental bone-targeted inhibitor improved bone and cardiovascular features in mice."
014,"#md-atlas",novel-regulators-mineral-metabolism-11-calciprotein-particles.png,"Biomedical mechanism figure (vessel inset)","Clinicians",3:2,1536,1024,prompted,"Blood vessel illustration: fetuin-A packages excess calcium and phosphate into calciprotein monomers and soft primary particles that are cleared, while crystalline secondary particles adhere to an inflamed vessel wall; an inset explains that T50 is a test-tube measure, not a calcium scan."
015,"#md-atlas",novel-regulators-mineral-metabolism-12-iron-fgf23.png,"Two-panel mechanism figure","Clinicians",3:2,1536,1024,prompted,"Two panels: in mice, osteocytes and erythroid precursors make FGF23, furin cleaves some of it, and intact FGF23 slows red cell production through FGFR1; in people, ferric carboxymaltose increases intact FGF23 activity and renal phosphate loss."
016,"#md-spotlight",novel-regulators-mineral-metabolism-14-evidence-ladder.png,"Simple figure — vertical step sequence","Mixed",2:3,1024,1536,prompted,"Five-rung ladder from cell and animal studies, to human association, to trials of laboratory or imaging change, to trials of outcomes patients feel, to graded guidelines, with clinical readiness rising alongside."
017,"#md-bedside",novel-regulators-mineral-metabolism-13-phosphate-handling-algorithm.png,"Clinical algorithm — journal style","Clinicians",2:3,1024,1536,prompted,"Algorithm for low phosphate: confirm, exclude shift and intake or gut loss, collect a paired fasting sample, calculate FEPO4, TRP and TmP/GFR, then separate renal phosphate loss (FGF23-mediated or not) from appropriate conservation, with interpretation limits listed."
018,"#md-bedside",novel-regulators-mineral-metabolism-15-pth-assay-standardization.png,"Simple figure — comparison","Clinicians and dialysis staff",3:2,1536,1024,prompted,"Two laboratory analyzers give the same PTH value of 540 pg/mL, which equals 8.3 times the upper limit on an assay with an upper limit of 65 but 6.1 times on an assay with an upper limit of 88; a trend line breaks where the assay changes."
019,"#md-bedside",novel-regulators-mineral-metabolism-16-calcium-measurement.png,"Simple figure — three-option comparison","Clinicians",3:2,1536,1024,prompted,"Three options for reporting calcium: measured total calcium as the default, an albumin-adjusted estimate marked with caution because it is least reliable when albumin is low, and ionized calcium measured directly."
020,"guides/calc-mineral-metabolism-workbench.html",calc-mineral-metabolism-workbench-og.png,"OG / social share card","Clinicians",1.91:1,1200,630,prompted,"Share card for the Mineral Metabolism Workbench calculator showing a tablet with a calm dashboard of trend charts."
```
