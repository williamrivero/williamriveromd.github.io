# Image Plan Blueprint — Inflammation in Dialysis

**Guide:** `guides/inflammation-in-dialysis.html` · **Slug:** `inflammation-in-dialysis`
**Prepared:** November 2, 2026 · **Pipeline:** Stage 1 prompt pack → Stage 2 `williamriveromd-local-image-generator`
**Generator:** ChatGPT Image Generator GPT — https://chatgpt.com/
**Skills applied:** `williamriveromd-hero-vignette` (v3), `williamriveromd-infographic-skill` (v5), `williamriveromd-simple-figure`, `williamriveromd-biomedical-mechanism-figure`, `williamriveromd-algorithm-generator-skill` (Style Mode C), `williamriveromd-organ-crosstalk-sigil-graphic`

---

## 1. Visual strategy

**Editorial thesis to carry through every image:** a high CRP is a smoke alarm, not the fire. Inflammation is real and worth finding, but lowering a blood marker is not the same as helping the patient.

**One visual system, two audiences.**

| Audience | Visual register | Text on image | Motifs |
|---|---|---|---|
| Patients & Families | Calm 2D infographic cards, a few semi-photoreal 3D objects, one still-life hero | English only, short phrases, large type (the HTML carries the four-language text) | Smoke alarm and warning rings; dialysis blood lines; a fire hidden behind a door (the "source") |
| Clinicians | Review-article mechanism schematics, flat house-style algorithms, compact reference cards | Precise labels, trial names, effect sizes only where verified in the guide | NLRP3 → IL-1β → IL-6 → liver chain; evidence ladder; biomarker vs outcome split |

**House rules for every prompt (all skills):**
- Light backgrounds only (white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, light teal tint `#eef6f7`). Never navy, charcoal, or black fills.
- Palette: navy `#0f1e2e` (text and borders only), teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b`, clinical red `#b91c1c`, soft purple `#6c3d8e`.
- Fonts: Inter, Nunito Sans, IBM Plex Sans, or Manrope only. Each prompt names its font.
- Attribution `© renalcarematters.com` on every image except the text-free hero (bottom-right for landscape/square, bottom-center for portrait).
- No journal names, guideline acronyms, brand names, or watermarks. Generic drug names and trial acronyms are allowed where the guide uses them.
- Clinical guardrails: nothing on any image recommends an anti-cytokine drug, a CRP target, a colchicine regimen, or a supplement dose. ZEUS is always labeled "headline result; full results not yet published."

**Human variation.** This guide's hero uses no people (Object Hero, Scaffold B), which rotates away from the people-led heroes in adjacent guides. Patient figures 05 and 07 use small, simple people only where they add meaning; each must differ visibly from recent guide casts (age, sex, face shape, hair, clothing, setting).

**What already exists.** The guide currently ships original HTML-rendered placeholders for 001, 002, 008, 010, 013, and 017 (same filenames). Generating these prompts replaces them in place. Prompts 003–007, 009, 011, 012, and 014–016 are new figures; Stage 2 wires them into the sections listed.

---

## 2. Production manifest

| # | File name (.png + .webp) | Section | Skill / archetype | Size | Audience | Status |
|---|---|---|---|---|---|---|
| 001 | `inflammation-in-dialysis-vignette-hero.png` | Hero (patient) | Hero vignette v3 · Scaffold B · Object Hero | 2048 × 2048 | Patients | Replaces placeholder |
| 002 | `inflammation-in-dialysis-01-sources-map.png` | `#sources` | Infographic · Multi-panel educational | 1792 × 1024 | Patients | Replaces placeholder |
| 003 | `inflammation-in-dialysis-05-acute-vs-chronic.png` | `#what` | Simple figure · Scaffold B comparison | 1792 × 1024 | Patients | New |
| 004 | `inflammation-in-dialysis-06-crp-can-cannot.png` | `#tests` | Simple figure · Scaffold E quick-look card | 1024 × 1024 | Patients | New |
| 005 | `inflammation-in-dialysis-07-clue-checklist.png` | `#check` | Infographic · Multi-panel educational | 1792 × 1024 | Patients | New |
| 006 | `inflammation-in-dialysis-08-helps-vs-research.png` | `#treatments` | Simple figure · Scaffold B comparison | 1792 × 1024 | Patients | New |
| 007 | `inflammation-in-dialysis-09-warning-signs.png` | `#warning` | Simple figure · Scaffold E quick-look card | 1024 × 1024 | Patients | New |
| 008 | `inflammation-in-dialysis-02-il1-il6-pathway.png` | `#md-biology` | Biomedical mechanism figure | 1792 × 1024 | Clinicians | Replaces placeholder |
| 009 | `inflammation-in-dialysis-10-crosstalk-sigil.png` | `#md-outcomes` (opening) | Organ crosstalk sigil | 1024 × 1024 | Clinicians | New |
| 010 | `inflammation-in-dialysis-03-evidence-ladder.png` | `#md-outcomes` | Simple figure · Scaffold D single-panel poster | 1792 × 1024 | Clinicians | Replaces placeholder |
| 011 | `inflammation-in-dialysis-11-hepcidin-iron.png` | `#md-outcomes` (anemia paragraph) | Biomedical mechanism figure | 1792 × 1024 | Clinicians | New |
| 012 | `inflammation-in-dialysis-12-trial-timeline.png` | `#md-il6` (after ZEUS box) | Infographic · Clinician reference card (timeline) | 1792 × 1024 | Clinicians | New |
| 013 | `inflammation-in-dialysis-04-assessment-pathway.png` | `#md-pathway` | Algorithm · Style Mode C | 1024 × 1536 | Clinicians | Replaces placeholder |
| 014 | `inflammation-in-dialysis-13-symptom-matrix.png` | `#md-symptoms` | Infographic · Clinician reference card | 1536 × 1152 | Clinicians | New |
| 015 | `inflammation-in-dialysis-14-hd-vs-pd-sources.png` | `#md-pd` | Simple figure · Scaffold B comparison | 1792 × 1024 | Clinicians | New |
| 016 | `inflammation-in-dialysis-15-case-snapshots.png` | `#md-cases` | Infographic · Case snapshot | 1792 × 1024 | Clinicians | New |
| 017 | `inflammation-in-dialysis-og.png` | `<head>` og:image | Infographic · OG card | 1200 × 630 | Social | Replaces placeholder |

**Stage 2 notes.** Placeholders 002, 008, and 010 are currently 1600 × 1000; update the `width`/`height` attributes to 1792 × 1024 when swapping. Hero `<img>` keeps square attributes. Every new inline figure needs a `<figcaption>` with `<p class="fig-desc">` and a `<dl class="fig-abbrevs">` for any acronym on the image; in the abbreviation `<dd>`, write "Expansion (ACRONYM)" so `audit_acronym_expansion.py` stays at N/N. Re-run `patch_image_lightbox.py` and both audits after wiring.

---

## 3. Prompts

### IMAGE 001 — Hero vignette

```
FILE NAME: inflammation-in-dialysis-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B still-life
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero
CAMERA: low three-quarter view, looking slightly up at a ceiling-mounted object
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: patients and families (mixed)
VISUAL GOAL: A calm, glowing smoke alarm above dialysis blood lines says "this is an alarm, not the fire" at a glance.
```

**PROMPT:**
Square 1:1 semi-photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle; the circle never touches the canvas edges. Composition archetype: I Object Hero. Camera: low three-quarter view looking slightly up.

Subject: a single round white ceiling smoke alarm, matte finish with fine vent slots, its small indicator light glowing soft red. Three faint concentric warm-amber sound-wave rings radiate outward from it, fading as they expand. In the lower third of the circle, two softly curving dialysis blood lines (one deep red, one muted blue, translucent medical tubing) sweep across like a horizon, slightly out of focus. Background inside the circle is a soft daylight gradient from warm peach at the top right to pale clinical teal (#eef6f7) at the bottom left.

Visual hierarchy: the smoke alarm occupies 60–70% of the circle; the tubing and rings 20–30%; reserve a 20–25% TITLE SAFE ZONE of empty soft gradient in the upper-left of the circle (no objects, rings, or tubing there). Gentle studio daylight, soft shadow, shallow depth of field, calm and reassuring colour grade harmonizing with teal #1a6b72 and navy #0f1e2e. Soft edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, caption, label, logo, readable markings on the alarm, or watermark. No flames, smoke, or fire imagery.

**NEGATIVE INSTRUCTIONS:** Avoid busy layouts, collage overload, more than four supporting elements, tiny labels, infographic clutter, cropped circle, cropped objects, edge clipping, objects touching the circular border, anything inside the title-safe zone, baked-in text, logos, watermarks, rectangular borders, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation, flames, smoke, blood spatter, frightening imagery.

**QUALITY CHECK:** Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin, never cropped. One dominant subject (smoke alarm) at 60–70%; title-safe zone empty; tubing reads as dialysis blood lines; nothing readable on any surface.

**ALT TEXT:** Illustration of a smoke alarm sending out warning rings above red and blue dialysis blood lines, representing C-reactive protein as the body's inflammation alarm
**OG WIDTH / HEIGHT:** 2048 / 2048 (not used as OG)

---

### IMAGE 002 — Where inflammation comes from

```
IMAGE NUMBER: 002
SECTION PLACEMENT: Patient — #sources (replaces the current figure)
FILE NAME: inflammation-in-dialysis-01-sources-map.png
ARCHETYPE: Multi-panel educational infographic (radial)
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: six source cards
- 3D component graphics: central smoke alarm, small 3D icons per card
- algorithm/flowchart: radial arrows (solid and dashed)
PURPOSE: Show the six findable "fires" that set off the inflammation alarm.
KEY CONCEPTS: infection; vascular access; too little dialysis; fluid overload; nutrition and muscle; other illness; CRP as the alarm.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Patient education infographic poster, landscape 16:9, 1792 × 1024, white background (#ffffff) with a very light teal wash (#eef6f7) behind the center. Title top-left in Inter Bold, navy #0f1e2e: "Where inflammation on dialysis comes from". Subtitle in Inter Regular, slate gray: "Most sources can be found and treated — look for the fire before treating the alarm."

Center: a soft semi-photoreal 3D white smoke alarm with a small red light and three faint amber rings, sitting inside a pale peach circle. Under it, a rounded amber pill label in Inter SemiBold white text: "CRP = the alarm, not the fire". A short two-line caption beneath: "Immune cells release IL-6 → the liver makes C-reactive protein (CRP)".

Six rounded white cards arranged three on the left and three on the right, each with a thick colored left border, a small clean 3D icon, a bold title, and one short line:
1. Red #b91c1c — icon: dialysis catheter with a small bacterium — "Infection" — "Catheter, fistula or graft, teeth, skin, lungs, urine"
2. Amber #b8860b — icon: tunneled catheter in a neck vein — "Vascular access" — "A catheter in the blood; an old clotted graft"
3. Navy #0f1e2e — icon: dialysis machine with a clock — "Too little dialysis" — "Shortened or missed sessions"
4. Teal #1a6b72 — icon: water droplet over a swollen ankle — "Fluid overload" — "A congested gut can leak bacterial products"
5. Green #1f7a4d — icon: plate with fish, rice, vegetables and a flexed arm — "Nutrition and muscle" — "Low protein and muscle loss feed inflammation"
6. Purple #6c3d8e — icon: heart, joint, and liver mini-icons — "Other illness" — "Diabetes, heart failure, gout, liver disease"

Arrows from each card point to the central circle in the card's color: solid arrows for cards 1, 2, and 6 (well-established), dashed arrows for cards 3, 4, and 5 (plausible, less certain). A small centered legend at the bottom: solid line "well-established link", dashed line "plausible, less certain". All text in Inter, large and readable on mobile. Footer bottom-right, small semi-transparent navy text: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, flames or smoke, unrealistic anatomy, overprocessed HDR, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the renalcarematters.com attribution.

**QUALITY CHECK:** Six cards readable at phone width; solid vs dashed arrows correct; CRP shown as the alarm in the center; attribution visible bottom-right.

**ALT TEXT:** Diagram of the sources of inflammation in a person on dialysis: infection, vascular access, too little dialysis, fluid overload, nutrition, and other illnesses, all feeding a central inflammation alarm labeled CRP
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 003 — Healthy alarm vs stuck alarm

```
IMAGE NUMBER: 003
SECTION PLACEMENT: Patient — #what, after the second paragraph
FILE NAME: inflammation-in-dialysis-05-acute-vs-chronic.png
ARCHETYPE: Side-by-side comparison (Simple figure Scaffold B)
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two panels with timelines
- 3D component graphics: small hand with bandage; small smoke alarm
- algorithm/flowchart: none
PURPOSE: Contrast short, protective inflammation with low-grade inflammation that stays switched on.
KEY CONCEPTS: acute = switches on then off; chronic = stays on for months; linked to heart disease, poor appetite, muscle loss, tiredness, anemia.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Clean side-by-side comparison figure, landscape 1792 × 1024, white background. Title centered top in Nunito Sans Bold, navy #0f1e2e: "A helpful alarm vs. an alarm that stays on". Two equal rounded panels on soft gray (#f3f4f6), separated by a thin vertical rule.

Left panel, header in renal green #1f7a4d: "Short-term inflammation (helpful)". A small semi-photoreal 3D hand with a fresh bandage on a fingertip. Below it a simple line chart: a single green bump that rises over two days and falls back to baseline, x-axis labeled "Days", annotation "Switches on → heals → switches off". Three short bullets with green check icons: "Fights germs", "Repairs injury", "Turns off by itself".

Right panel, header in amber #b8860b: "Long-lasting inflammation on dialysis". A small 3D smoke alarm with its red light on. Below it a line chart that rises and stays high as a flat amber plateau across the x-axis labeled "Months", annotation "Stays switched on". Five small icons in a row with one-word captions: heart ("Heart"), plate ("Appetite"), arm muscle ("Muscle"), battery half-empty ("Energy"), red blood cell ("Anemia"). Under them a gray footnote in Nunito Sans Italic: "Linked with these problems — lowering the number alone has not been proven to fix them."

All type in Nunito Sans, large and mobile-readable. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** Avoid cartoon style, clutter, gore or open wounds, tiny labels, AI gibberish text, dark backgrounds, serif fonts. Never omit the attribution.

**QUALITY CHECK:** Two panels only; charts clearly differ (bump vs plateau); the footnote states association, not proven cause.

**ALT TEXT:** Two panels comparing short-term inflammation, which rises and settles after an injury, with long-lasting inflammation on dialysis, which stays high for months and is linked with heart disease, poor appetite, muscle loss, low energy, and anemia
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 004 — What a CRP test can and cannot tell you

```
IMAGE NUMBER: 004
SECTION PLACEMENT: Patient — #tests, after the first paragraph
FILE NAME: inflammation-in-dialysis-06-crp-can-cannot.png
ARCHETYPE: Square quick-look reference card (Simple figure Scaffold E)
AUDIENCE: Patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two-column card
- 3D component graphics: one blood tube
- algorithm/flowchart: none
PURPOSE: Set realistic expectations for a CRP result.
KEY CONCEPTS: CAN suggest the body is fighting something; CANNOT show where, cannot measure blood vessels, is not a treatment target; units mg/L vs mg/dL.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Square quick-look reference card, 1024 × 1024, white background, rounded outer card on light teal tint #eef6f7. Top: a small semi-photoreal 3D blood collection tube with a plain unlabeled cap beside the title in Manrope ExtraBold navy #0f1e2e: "Your CRP result". Two columns below.

Left column header in renal green #1f7a4d with a check icon: "It CAN tell you". Three short items: "The body is fighting something", "Whether it is staying high on repeat tests", "That it is worth looking for a cause".

Right column header in clinical red #b91c1c with an X icon: "It CANNOT tell you". Three short items: "Where the problem is", "What is happening inside your blood vessels", "Which medicine you need".

Bottom band in soft gray #f3f4f6 with a small ruler icon, Manrope SemiBold: "Units differ: 1 mg/dL = 10 mg/L. Compare results from the same laboratory."

All type in Manrope, minimum 22 px equivalent for body items. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** Avoid clutter, readable lab-tube labels, tiny text, cartoon style, dark backgrounds, serif fonts. Never omit the attribution.

**QUALITY CHECK:** Reads in 10 seconds on a phone; unit conversion correct (1 mg/dL = 10 mg/L).

**ALT TEXT:** Reference card: a CRP result can show the body is fighting something and that a cause is worth looking for, but cannot show where the problem is, what is happening in the blood vessels, or which medicine is needed; 1 mg/dL equals 10 mg/L
**OG WIDTH / HEIGHT:** 1024 / 1024

---

### IMAGE 005 — Inflammation clues at a glance

```
IMAGE NUMBER: 005
SECTION PLACEMENT: Patient — #check, above the clue checker
FILE NAME: inflammation-in-dialysis-07-clue-checklist.png
ARCHETYPE: Multi-panel educational infographic (three tiers)
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: one small hands-only inset (a nurse's gloved hand checking a fistula arm)
- 2D infographic: three tier columns
- 3D component graphics: small icons
- algorithm/flowchart: none
PURPOSE: Visual companion to the interactive checker: warning signs, body clues, lab clues.
KEY CONCEPTS: red = go today; amber = clues to tell your team this week; teal = lab clues.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Patient education infographic, landscape 1792 × 1024, white background. Title in Inter Bold navy #0f1e2e: "Clues that inflammation may be present". Subtitle in Inter Regular gray: "No single clue proves it — together they tell your team where to look."

Three tall rounded columns:

Column 1, red header band #b91c1c with white text "Go today — warning signs". Icons with short labels: thermometer "Fever or shaking chills on dialysis"; arm with fistula showing redness "Red, swollen, painful, or pus at your access"; cloudy fluid bag "Peritoneal dialysis: cloudy fluid or belly pain"; chest outline "Chest pain or new breathlessness". A small hands-only photoreal inset at the bottom of this column: a gloved nurse's hand gently examining a fistula arm, bright clinic light, no faces.

Column 2, amber header band #b8860b with white text "Tell your team this week — body clues". Icons: plate with fork "Poor appetite or weight loss"; battery "Unusual tiredness"; tooth "Toothache or swollen gums"; foot with small sore "A sore that will not heal"; joint "Hot, swollen joint"; calendar with missed day "Missed or shortened sessions"; catheter "Dialyzing through a catheter".

Column 3, teal header band #1a6b72 with white text "Lab clues — ask for your results". Icons: blood tube "CRP above the lab's normal limit"; protein drop "Albumin below 3.8 g/dL"; iron atom "High ferritin with low TSAT"; red blood cell with down arrow "Hemoglobin falling despite the same EPO dose"; white cell "White cell count above 11".

Bottom band in soft gray: "Do not self-treat with antibiotics, pain relievers, or supplements. Bring these clues to your nephrologist." All type in Inter, mobile-readable. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** Avoid gore, pus close-ups, frightening imagery, tiny labels, clutter, cartoon style, dark backgrounds, serif fonts. Never omit the attribution.

**QUALITY CHECK:** Thresholds match the guide's checker exactly (albumin < 3.8 g/dL; ferritin > 500 ng/mL with TSAT < 20% summarized as "high ferritin with low TSAT"; WBC > 11). Red column clearly says "go today."

**ALT TEXT:** Three-column chart of inflammation clues: warning signs that need same-day care, body clues to report this week, and laboratory clues such as high CRP, low albumin, high ferritin with low transferrin saturation, falling hemoglobin, and high white cell count
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 006 — What helps now vs what is still research

```
IMAGE NUMBER: 006
SECTION PLACEMENT: Patient — #treatments, after the first paragraph
FILE NAME: inflammation-in-dialysis-08-helps-vs-research.png
ARCHETYPE: Side-by-side comparison (Simple figure Scaffold B)
AUDIENCE: Patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two panels
- 3D component graphics: small objects (dialysis machine, fistula arm, plate, walking shoes, IV iron bag, syringe, capsule)
- algorithm/flowchart: none
PURPOSE: Separate everyday care that helps from investigational injections.
KEY CONCEPTS: proven everyday care; IL-6 drugs lower CRP but did not reduce heart events in ZEUS (headline; full results not yet published); fish-oil trial used a specific dose.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Clean comparison figure, landscape 1792 × 1024, white background. Title in IBM Plex Sans Bold navy #0f1e2e: "What helps now — and what is still being tested". Two rounded panels.

Left panel on light green tint, header in renal green #1f7a4d with a check badge: "Helps now (part of good dialysis care)". Six small 3D icons in a 2×3 grid, each with a short caption: fistula arm "Protect your access"; thermometer with magnifier "Find and treat infection early"; dialysis machine with full clock "Complete every session"; scale with water drop "Control fluid gains"; plate with fish and vegetables "Enough protein, with your dietitian"; walking shoes "Stay active".

Right panel on soft gray #f3f4f6, header in amber #b8860b with a flask badge: "Still in research". Two stacked cards. Card 1: a 3D syringe icon; text "Injections that block IL-1 or IL-6: lower CRP a lot, but a large 2026 trial (ZEUS) found no fewer heart attacks or strokes and more serious infections. Headline result only — full results not yet published. Available only in research studies." Card 2: a 3D fish-oil capsule icon; text "Fish oil: one hemodialysis trial used a specific high dose. Store capsules are different. Ask your nephrologist before starting."

All type in IBM Plex Sans, large and readable. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No product packaging or brand names, no doses beyond what is stated, no clutter, no cartoon style, no dark backgrounds, no serif fonts. Never omit the attribution.

**QUALITY CHECK:** ZEUS wording includes "full results not yet published"; no recommendation to take any injection or supplement.

**ALT TEXT:** Comparison: everyday dialysis care that helps now, including access protection, early infection treatment, full sessions, fluid control, nutrition, and activity, versus treatments still in research, including IL-1 and IL-6 blocking injections and high-dose fish oil
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 007 — Seek care today

```
IMAGE NUMBER: 007
SECTION PLACEMENT: Patient — #warning, beside the red alert
FILE NAME: inflammation-in-dialysis-09-warning-signs.png
ARCHETYPE: Square quick-look card (Simple figure Scaffold E)
AUDIENCE: Patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: icon grid
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: A screenshot-able red-flag card patients can save on their phone.
KEY CONCEPTS: fever or chills; access redness, pus, swelling, pain; cloudy PD fluid or belly pain; chest pain or breathlessness; confusion; sudden low blood pressure.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Square quick-look warning card, 1024 × 1024, white background, rounded card with a 6 px clinical red #b91c1c border. Title in Inter ExtraBold, red: "Call your dialysis unit or go to the ER today if you have:". A 2×3 grid of simple flat line icons in red and navy, each with a short label in Inter SemiBold navy #0f1e2e: thermometer "Fever or shaking chills"; arm with access site "Red, swollen, painful, or pus at your access"; drainage bag with cloudy fluid "Cloudy dialysis fluid or belly pain (PD)"; heart with lightning "Chest pain"; lungs "New shortness of breath"; head with question mark "Confusion or fainting". Bottom band in soft gray: "Do not wait for a blood test." Footer bottom-center, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** Avoid frightening imagery, gore, clutter, tiny labels, dark backgrounds, serif fonts. Never omit the attribution.

**QUALITY CHECK:** Six signs only; readable on a phone lock screen.

**ALT TEXT:** Warning card listing signs that need same-day care on dialysis: fever or chills, problems at the access, cloudy peritoneal dialysis fluid or belly pain, chest pain, new shortness of breath, and confusion or fainting
**OG WIDTH / HEIGHT:** 1024 / 1024

---

### IMAGE 008 — The NLRP3–IL-1β–IL-6 axis (mechanism)

```
IMAGE NUMBER: 008
SECTION PLACEMENT: Clinician — #md-biology (replaces the current figure)
FILE NAME: inflammation-in-dialysis-02-il1-il6-pathway.png
ARCHETYPE: Biomedical mechanism figure (organ panel → magnified inset → bottom flow)
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: review-article schematic
- 3D component graphics: soft semi-3D shading only
- algorithm/flowchart: left-to-right pathway
PURPOSE: Place CRP and hepcidin downstream of IL-6 and show where each drug acts.
KEY CONCEPTS: danger signals; NLRP3 inflammasome; caspase-1; IL-1β; IL-6; hepatocyte acute-phase response; hepcidin; drug targets.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Create a publication-grade biomedical mechanism schematic about:

Topic: the NLRP3 – IL-1β – IL-6 axis in kidney failure
Disease context: maintenance dialysis with persistent inflammation
Central mechanism: danger signals activate the NLRP3 inflammasome in macrophages; IL-1β induces IL-6; IL-6 drives hepatic CRP and hepcidin

Organ-level panel (left): simplified pair of failing kidneys and a dialysis blood line, labeled "Kidney failure: retained uremic solutes, oxidative stress, endotoxin, infection, urate and cholesterol crystals". A small dashed connector box points to the magnified panel.

Magnified mechanism panel (center, dashed border): a macrophage with a pale purple ring-shaped NLRP3 inflammasome highlighted in soft yellow; callouts "NLRP3 assembles → caspase-1 active", "pro-IL-1β → IL-1β", "IL-1β → IL-6 release". A thin arrow leads right to a simplified hepatocyte showing two outputs: "CRP, fibrinogen, serum amyloid A ↑ · albumin ↓" and "Hepcidin ↑ → ferroportin blocked".

Drug-target tags (small rounded pale-blue badges with thin leader lines): "Colchicine — upstream, indirect" near the inflammasome; "Canakinumab · anakinra · rilonacept — IL-1" at IL-1β; "Ziltivekimab · clazakizumab — IL-6 ligand" at IL-6.

Bottom summary flow:
Left pathology box (pale pink): "Persistent IL-6 signaling"
Center box (pale yellow): "CRP is a read-out, not the whole inflammatory state, and not plaque inflammation"
Right box (pale blue): "Blocking IL-6 lowers CRP by up to ~90% — outcome benefit in dialysis unproven"

Use a white background, muted clinical colors (gray-blue anatomy, soft yellow highlights, red for injury, blue for drug effects), clean labels set in IBM Plex Sans (never a serif font), thin dashed connector lines, and a review-article figure style. Include small semi-transparent navy text "© renalcarematters.com" in the bottom-right corner. Avoid photorealism, dark backgrounds, decorative elements, and overcrowding. No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No gibberish molecule names, no extra drugs, no serif fonts, no dark theme, no excessive icons.

**QUALITY CHECK:** CRP and hepcidin are downstream of IL-6; each drug badge sits at its correct target; colchicine labeled indirect; all labels spelled correctly.

**ALT TEXT:** Mechanism diagram: in kidney failure, danger signals activate the NLRP3 inflammasome in macrophages, producing IL-1 beta, which induces IL-6; IL-6 drives the liver to make CRP and hepcidin; drug targets marked for colchicine, IL-1 blockers, and IL-6 ligand antibodies
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 009 — IL-6 organ crosstalk sigil

```
IMAGE NUMBER: 009
SECTION PLACEMENT: Clinician — #md-outcomes, opening (small, right-floated or centered at 360 px)
FILE NAME: inflammation-in-dialysis-10-crosstalk-sigil.png
ARCHETYPE: Organ crosstalk sigil (label-free)
AUDIENCE: Clinicians (also usable as a social square)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: monoline sigil
- 3D component graphics: none
- algorithm/flowchart: dotted loop arrows
PURPOSE: Symbolize that inflammation in kidney failure is a multi-organ conversation, not one number.
KEY CONCEPTS: kidneys, liver, heart, bone marrow, gut, skeletal muscle connected in a loop.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Create a simple medical organ-crosstalk sigil illustration featuring:

ORGANS:
- kidneys (pair, center)
- liver
- heart
- bone marrow (stylized long-bone cross-section)
- gut (small loop of intestine)
- skeletal muscle (simple muscle bundle)

RELATIONSHIP:
Show inflammatory crosstalk in kidney failure: dotted curved arrows radiate from the kidneys to the gut and back (endotoxin), to the liver (acute-phase response), from the liver to the bone marrow (iron restriction), and to the heart and muscle (cardiovascular strain, wasting), forming one gentle circular loop around the kidneys.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette with a single warm amber accent dot at the center of the kidneys, white background, clean rounded organ shapes, balanced radial sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels.

COMPOSITION:
Place the kidneys at the center; arrange liver, heart, bone marrow, gut, and muscle evenly around them in a hexagonal ring. Connect them with dotted arrows forming a calm circular loop.

OUTPUT:
Square 1024 × 1024, clean margins, high-resolution, publication-grade medical icon aesthetic. Include a small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner, not obscuring the sigil. No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No labels, no complex anatomy, no 3D rendering, no heavy shadows, no clutter, no dark background.

**QUALITY CHECK:** Six organs recognizable as line icons; loop reads as one system; label-free except attribution.

**ALT TEXT:** Line-art sigil of the kidneys at the center linked by dotted arrows to the gut, liver, bone marrow, heart, and muscle, symbolizing inflammation as a conversation between organs in kidney failure
**OG WIDTH / HEIGHT:** 1024 / 1024

---

### IMAGE 010 — The evidence ladder

```
IMAGE NUMBER: 010
SECTION PLACEMENT: Clinician — #md-outcomes (replaces the current figure)
FILE NAME: inflammation-in-dialysis-03-evidence-ladder.png
ARCHETYPE: Single-panel poster (Simple figure Scaffold D)
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: six-rung staircase
- 3D component graphics: none
- algorithm/flowchart: upward arrow
PURPOSE: Teach that each endpoint level is a separate question.
KEY CONCEPTS: association; target engagement; physiology; anemia; patient-reported outcomes; events and survival; where each key study landed.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Single-panel educational poster, landscape 1792 × 1024, white background. Title in Inter Bold navy #0f1e2e: "The evidence ladder: each rung is a separate question". Subtitle in Inter Regular gray: "Success on a lower rung does not guarantee success above it."

A six-rung staircase rising from bottom-left to top-right, each rung a wide rounded bar with a colored number block on the left, the rung name and a short question in the middle, a study example, and a verdict pill on the right:
1 (slate gray) "Observational association — higher IL-6 and CRP go with more deaths" · "Hemodialysis cohorts" · pill "Associated, not causal"
2 (purple #6c3d8e) "Target engagement — drug lowers CRP or IL-6" · "Clazakizumab phase 2b: hsCRP −86 to −92%" · pill "Achieved"
3 (teal #1a6b72) "Physiologic endpoint — artery function" · "Rilonacept, CKD 3–4: flow-mediated dilation up, stiffness unchanged" · pill "Partial"
4 (green #1f7a4d) "Anemia endpoint — hemoglobin or ESA dose" · "RESCUE analysis: hemoglobin +0.6 to +1.0 g/dL" · pill "Surrogate signal"
5 (amber #b8860b) "Patient-reported outcomes — feel or function better" · "ACTION (anakinra, hemodialysis): no effect" · pill "Not shown"
6 (red #b91c1c) "Clinical events and survival" · "ZEUS (CKD): HR 0.99, headline only, full results not yet published · PISCES (hemodialysis, fish oil): HR 0.57" · pill "No anti-cytokine success yet"

A tall navy arrow along the left edge pointing up, labeled "Matters more to patients". All type in Inter. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No extra numbers beyond those listed, no clutter, no cartoon style, no dark background, no serif fonts. Never omit the attribution.

**QUALITY CHECK:** Numbers exactly as listed; ZEUS labeled headline-only; rungs ascend left-to-right.

**ALT TEXT:** Evidence ladder with six rungs from observational association, through biomarker target engagement, physiologic and anemia endpoints, and patient-reported outcomes, to clinical events and survival, each with an example study and verdict
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 011 — IL-6, hepcidin, and iron-restricted anemia (mechanism)

```
IMAGE NUMBER: 011
SECTION PLACEMENT: Clinician — #md-outcomes, after the anemia paragraph
FILE NAME: inflammation-in-dialysis-11-hepcidin-iron.png
ARCHETYPE: Biomedical mechanism figure
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: review-article schematic
- 3D component graphics: soft semi-3D shading
- algorithm/flowchart: bottom flow
PURPOSE: Explain why ferritin can be high while TSAT is low and ESA needs rise.
KEY CONCEPTS: IL-6 → hepatic hepcidin → ferroportin internalized in enterocytes and macrophages → iron trapped → low TSAT, high ferritin → iron-restricted erythropoiesis → ESA hyporesponsiveness; anemia remains multifactorial.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Create a publication-grade biomedical mechanism schematic about:

Topic: IL-6, hepcidin, and iron-restricted anemia in dialysis
Disease context: maintenance hemodialysis with persistent inflammation and ESA hyporesponsiveness
Central mechanism: IL-6 raises hepatic hepcidin, which blocks ferroportin and traps iron

Organ-level panel (left): simplified liver with a small inflamed macrophage cluster releasing IL-6; label "IL-6 → hepcidin ↑". A dashed connector leads to the magnified panel.

Magnified mechanism panel (center, dashed border, three mini-insets side by side): (a) duodenal enterocyte with ferroportin on its basolateral surface being internalized, label "Dietary iron absorption ↓"; (b) splenic macrophage holding iron in ferritin, ferroportin blocked, label "Recycled iron trapped → ferritin ↑"; (c) plasma transferrin with few iron atoms, label "TSAT ↓". Hepcidin drawn as small amber molecules binding ferroportin.

Right panel: bone marrow erythroblasts receiving little iron, label "Iron-restricted erythropoiesis".

Bottom summary flow:
Left pathology box (pale pink): "Inflammation, infection, uremia"
Center box (pale yellow): "High ferritin + low TSAT can mean iron is locked away, not absent"
Right box (pale blue): "Find the source; evaluate iron, bleeding, PTH, dialysis adequacy — anemia is multifactorial"

White background, muted clinical palette (gray-blue anatomy, soft yellow highlights, amber hepcidin, red for injury, blue for supportive actions), labels in Manrope (never a serif font), thin dashed connectors, review-article style. Small semi-transparent navy "© renalcarematters.com" bottom-right. Avoid photorealism, dark backgrounds, decorative elements, overcrowding. No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No drug doses, no iron product names, no gibberish labels, no serif fonts, no dark theme.

**QUALITY CHECK:** Ferroportin shown on enterocyte and macrophage; ferritin ↑ with TSAT ↓; bottom-right box keeps anemia multifactorial.

**ALT TEXT:** Mechanism diagram: IL-6 raises liver hepcidin, which blocks ferroportin in gut cells and macrophages, trapping iron so ferritin rises while transferrin saturation falls and the bone marrow becomes iron-restricted
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 012 — Trial timeline: biomarker results vs outcome results

```
IMAGE NUMBER: 012
SECTION PLACEMENT: Clinician — #md-il6, after the ZEUS teaching box
FILE NAME: inflammation-in-dialysis-12-trial-timeline.png
ARCHETYPE: Clinician reference card (horizontal timeline)
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two-lane timeline
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Show that biomarker wins and outcome results are different lanes, with publication status labeled.
KEY CONCEPTS: upper lane biomarker/pilot trials; lower lane outcome trials; status badges (peer-reviewed, headline only, ongoing).
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Clinician reference timeline, landscape 1792 × 1024, white background. Title in IBM Plex Sans Bold navy #0f1e2e: "Inflammation trials in kidney disease: biomarkers vs outcomes". A horizontal year axis from 2011 to 2029 across the middle, thin navy line with year ticks.

Upper lane, label on the left in purple #6c3d8e: "Biomarker and pilot trials". Rounded purple-outlined cards above their years: 2011 "IL-1ra pilot, hemodialysis (n=22): hsCRP ↓"; 2017 "Rilonacept, CKD 3–4: vascular function ↑"; 2021 "Ziltivekimab, hemodialysis anemia (n=61): ESA use ↓"; 2021 "RESCUE, CKD: hsCRP ↓ 77–92%"; 2022 "ACTION, hemodialysis (n=80): hsCRP difference not significant; no symptom benefit"; 2024 "Clazakizumab phase 2b, dialysis (n=127): hsCRP ↓ 86–92%".

Lower lane, label on the left in red #b91c1c: "Outcome trials". Cards below their years: 2017 "CANTOS (post-MI, not dialysis): MACE HR 0.85"; 2023 "CONVINCE (high-dose hemodiafiltration): death HR 0.77"; 2026 "PISCES (hemodialysis, fish oil): serious CV events HR 0.57"; 2026 "ZEUS (CKD, ziltivekimab): MACE HR 0.99"; 2029 dashed card "POSIBIL6ESKD (dialysis, clazakizumab): CV death or MI — ongoing".

Each card carries a small status badge: green "Peer-reviewed" for CANTOS, CONVINCE, PISCES and all upper-lane cards; amber "Headline only — full results not yet published" for ZEUS; gray "Ongoing" for POSIBIL6ESKD. Small legend bottom-left explaining the three badges. All type in IBM Plex Sans. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No invented numbers, no pooled effects, no arrows implying one trial caused another, no clutter, no dark background, no serif fonts.

**QUALITY CHECK:** ZEUS badge amber with "full results not yet published"; POSIBIL6ESKD dashed and ongoing; every number matches the guide.

**ALT TEXT:** Two-lane timeline from 2011 to 2029 separating biomarker and pilot trials, which lowered inflammatory markers, from outcome trials, with CANTOS, CONVINCE, and PISCES peer-reviewed, ZEUS a headline result awaiting full publication, and POSIBIL6ESKD ongoing
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 013 — Assessment pathway (algorithm)

```
IMAGE NUMBER: 013
SECTION PLACEMENT: Clinician — #md-pathway (replaces the current figure)
FILE NAME: inflammation-in-dialysis-04-assessment-pathway.png
ARCHETYPE: Clinical algorithm — Style Mode C (renalcarematters.com house style)
AUDIENCE: Clinicians and dialysis staff
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: primary
PURPOSE: Eight-step assessment with a red-flag exit, ending in patient reassessment, never an anti-cytokine prescription.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. Use a white background, restrained navy and teal typography set in Inter (never a serif font), thin teal connector arrows, and generous margins. The layout should be centered, top-to-bottom, and suitable for a clinician-facing nephrology education guide.

Color conventions: navy #0f1e2e for title and body text; teal #1a6b72 for decision nodes and arrows; green #1f7a4d for recommended actions; amber #b8860b for caution nodes; clinical red #b91c1c for the emergency exit only; soft gray for side notes.

Title: "Assessing the inflamed dialysis patient". Subtitle: "Treat the cause and the patient".

Content to render:
1. Rounded box (navy): "Clinical concern — persistent unexplained high CRP, rising ESA needs, worsening nutrition, or burdensome symptoms"
2. Teal diamond: "Red flags?" — branch right labeled "Yes" to a red-outlined box: "Fever or rigors on dialysis, access infection, sepsis, chest pain, instability, severe dyspnea → urgent pathway now. Do not wait for a repeat CRP." Branch down labeled "No".
3. Rounded box: "Context and trajectory — units, assay, recent illness, medicines, trend"
4. Rounded box: "Directed source search — access, teeth, feet, skin, chest, urinary tract, old grafts, tuberculosis risk"
5. Rounded box: "Access and dialysis delivery — catheter plan, delivered time and dose, volume; PD: exit site and peritonitis history"
6. Green box: "Anemia and iron together — hemoglobin, TSAT, ferritin, ESA trend, bleeding; correct reversible causes first"
7. Green box: "Nutrition, function, and the symptom the patient wants addressed first"
8. Green box: "Reassess the patient — symptoms, function, ESA needs, events; not a CRP target"
9. Gray dashed box: "Research discussion if appropriate — eligibility belongs to the trial team"
Side note (amber, dashed, beside steps 6–8): "Avoid empiric antibiotics, steroids, NSAIDs, colchicine, or cytokine blockers given only to lower CRP."

Design requirements: clear title, top-to-bottom logic, rounded rectangles for actions, one diamond for the red-flag decision, consistent spacing, no dark background, no clutter, no photorealistic people, no icons. Make the diagram vector-like with crisp typography, aligned nodes, and consistent arrow lengths. Include a small professional footer reading "© renalcarematters.com" at the bottom-center in subtle gray medical-publication styling. No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No drug doses, no eligibility calculator, no CRP target, no 3D, no gradients.

**QUALITY CHECK:** Red-flag exit before step 3; final action is reassessment; amber "avoid" note present.

**ALT TEXT:** Flowchart: clinical concern, red-flag check routing to urgent care, context review, directed source search, access and dialysis delivery review, anemia and iron evaluation, nutrition and symptom care, patient reassessment, and optional clinical-trial discussion
**OG WIDTH / HEIGHT:** 1024 / 1536

---

### IMAGE 014 — Symptom matrix (reference card)

```
IMAGE NUMBER: 014
SECTION PLACEMENT: Clinician — #md-symptoms, after the first two paragraphs
FILE NAME: inflammation-in-dialysis-13-symptom-matrix.png
ARCHETYPE: Clinician reference card
AUDIENCE: Clinicians, dialysis nurses
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none
- 2D infographic: compact table with icons
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: One-look symptom triage that keeps symptom relief independent of CRP.
KEY CONCEPTS: fatigue, pruritus, appetite, mood, pain, overall burden; assessment tool; competing causes; first steps.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Clinical reference card, 1536 × 1152, white background, rounded panels on soft gray #f3f4f6. Title in Inter Bold navy #0f1e2e: "Symptoms on dialysis: assess the symptom, not the CRP". A compact four-column table with teal header row (white text): "Symptom" · "How to assess" · "Common competing causes" · "First steps". Six rows, each starting with a small flat line icon:
- Fatigue and recovery time · "Ask recovery time; SONG-HD fatigue item" · "Anemia, low mood, poor sleep, intradialytic hypotension, high ultrafiltration" · "Review UF and BP, anemia, mood, sleep; graded activity"
- Itch · "Worst Itch NRS" · "Dry skin, phosphate, PTH, underdialysis, drugs" · "Emollients; mineral-bone review; specific antipruritic"
- Appetite and weight · "Dietitian assessment; SGA" · "Underdialysis, gastroparesis, dental disease, infection, low mood" · "Nutrition plan; source search"
- Mood · "Validated depression screen" · "Stressors, pain, insomnia" · "Psychosocial and psychiatric care"
- Pain · "0–10 rating and site" · "Access, neuropathy, bone, musculoskeletal" · "Cause-directed care; avoid NSAIDs"
- Overall burden · "Dialysis Symptom Index or KDQOL" · "Multiple" · "Ask which symptom matters most"
Bottom amber band: "A drug that lowered IL-6 did not make patients feel better (ACTION). Do not make symptom relief wait for CRP to fall." All type in Inter, minimum 18 px equivalent in table cells. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No drug doses, no tiny text, no clutter, no dark background, no serif fonts.

**QUALITY CHECK:** Six rows readable at full width; bottom band accurate to ACTION.

**ALT TEXT:** Reference table of six dialysis symptom domains with assessment tools, competing causes, and first management steps, emphasizing that symptom relief should not wait for CRP to fall
**OG WIDTH / HEIGHT:** 1536 / 1152

---

### IMAGE 015 — HD vs PD: different sources, different pathways

```
IMAGE NUMBER: 015
SECTION PLACEMENT: Clinician — #md-pd
FILE NAME: inflammation-in-dialysis-14-hd-vs-pd-sources.png
ARCHETYPE: Side-by-side comparison (Simple figure Scaffold B)
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two panels
- 3D component graphics: HD circuit and PD catheter/abdomen, accurate anatomy
- algorithm/flowchart: none
PURPOSE: Show why PD needs its own inflammation pathway.
KEY CONCEPTS: HD — catheter/fistula/graft infection, circuit, delivered dose, volume; PD — peritonitis, exit-site/tunnel infection, membrane exposure to glucose, peritoneal protein loss lowering albumin; peritonitis targets ≤0.40 episodes/patient-year at risk and >80% peritonitis-free per year.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Clean comparison figure, landscape 1792 × 1024, white background. Title in Nunito Sans Bold navy #0f1e2e: "Inflammation sources: hemodialysis vs peritoneal dialysis". Two equal rounded panels.

Left panel (teal #1a6b72 header): "Hemodialysis". A clean semi-3D diagram of an arm with an arteriovenous fistula connected to two needles and blood lines leading to a simplified dialyzer (a vertical cylinder with blood entering the top header and leaving the bottom header, dialysate flowing countercurrent through side ports), plus a small inset of a tunneled neck catheter. Four short callouts: "Catheter, fistula, or graft infection", "Catheter dependence", "Delivered time and dose", "Volume overload".

Right panel (purple #6c3d8e header): "Peritoneal dialysis". A clean semi-3D torso cross-section showing the peritoneal cavity with dialysate and a coiled PD catheter exiting the abdominal wall through a subcutaneous tunnel. Four callouts: "Peritonitis — cloudy effluent", "Exit-site or tunnel infection", "Membrane exposure to glucose solutions", "Protein lost into dialysate lowers albumin".

Bottom gray band split in two: left "Use the hemodialysis access-infection pathway"; right "Use the peritoneal dialysis society pathway: overall peritonitis ≤0.40 episodes per patient-year; >80% of patients peritonitis-free per year". All type in Nunito Sans. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** Dialyzer must have blood headers top and bottom with dialysate side ports, flowing countercurrent; no anatomical errors; no clutter; no dark background; no serif fonts.

**QUALITY CHECK:** Hemofilter anatomy correct; PD catheter exits through a tunnel; peritonitis targets exactly as stated.

**ALT TEXT:** Side-by-side diagram comparing inflammation sources in hemodialysis, such as access infection and delivered dose, with peritoneal dialysis, such as peritonitis, exit-site infection, membrane exposure, and protein loss that lowers albumin
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 016 — Five teaching cases

```
IMAGE NUMBER: 016
SECTION PLACEMENT: Clinician — #md-cases, above the case accordions
FILE NAME: inflammation-in-dialysis-15-case-snapshots.png
ARCHETYPE: Case snapshot
AUDIENCE: Clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: five case cards
- 3D component graphics: one small object per card
- algorithm/flowchart: none
PURPOSE: Preview the five cases as decision cards.
KEY CONCEPTS: A infection, B iron restriction, C fatigue, D IL-6 antibody request, E fish oil question.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Clinical case snapshot infographic, nephrology teaching style, landscape 1792 × 1024, white background. Title in Inter Bold navy #0f1e2e: "Five cases: the decision is rarely about CRP". Five equal rounded cards in a row on soft gray, each with a letter badge, one small semi-3D object, a two-line scenario, and a teal "Decision" line:
A — tunneled catheter icon — "hsCRP 38 mg/L, rigors on dialysis" — Decision: "Infection pathway: cultures, source control"
B — iron atom and blood tube — "Rising ESA dose, ferritin 900, TSAT 16%" — Decision: "Look for the source; iron locked away, not absent"
C — battery half-empty — "Disabling fatigue, normal hsCRP" — Decision: "Assess recovery time, BP, anemia, sleep, mood"
D — syringe — "Patient asks for an IL-6 antibody" — Decision: "Biomarker ≠ outcome; registered trial only"
E — fish-oil capsule — "Patient asks whether to buy fish oil" — Decision: "Trial used a specific high dose; review bleeding risk"
All type in Inter. Footer bottom-right, small semi-transparent navy: "© renalcarematters.com". No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No patient faces, no doses, no product brands, no clutter, no dark background, no serif fonts.

**QUALITY CHECK:** Values match the guide's cases; no card recommends an anti-cytokine drug.

**ALT TEXT:** Five teaching case cards: catheter infection, iron-restricted anemia, fatigue with normal CRP, a request for an IL-6 antibody, and a question about fish oil, each with its key decision
**OG WIDTH / HEIGHT:** 1792 / 1024

---

### IMAGE 017 — Open Graph share card

```
IMAGE NUMBER: 017
SECTION PLACEMENT: <head> og:image / twitter:image (replaces the current card)
FILE NAME: inflammation-in-dialysis-og.png
ARCHETYPE: OG / social share card
AUDIENCE: General / social
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title card
- 3D component graphics: smoke alarm at right
- algorithm/flowchart: none
PURPOSE: Facebook and X link preview.
```

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
Social share card exactly 1200 × 630, white to off-white background (#fafafa) with a faint peach wash on the right. Right third: a soft semi-photoreal 3D white smoke alarm with a small red light and three faint amber sound-wave rings. Left two-thirds, left-aligned text in Inter: a small teal #1a6b72 pill label with white text "Dialysis & Critical Nephrology"; a large bold navy #0f1e2e title "Inflammation in Dialysis"; a teal subtitle "A high CRP is a smoke alarm, not the fire"; a smaller gray line "Where it comes from · why IL-6 drugs lowered CRP but not heart events · what helps now". Bottom-left in bold navy: "renalcarematters.com". Bottom-right, small semi-transparent navy: "© renalcarematters.com". Keep at least 40 px of margin on every edge. No journal names, guideline acronyms, brand names, or watermarks.

**NEGATIVE INSTRUCTIONS:** No dark background, no flames, no people, no clutter, no serif fonts, no other size.

**QUALITY CHECK:** Exactly 1200 × 630; text legible at 600 px wide; nothing clipped.

**ALT TEXT:** Inflammation in Dialysis: From Biology to Bedside Decisions — renalcarematters.com
**OG WIDTH / HEIGHT:** 1200 / 630

---

## 4. Production checklist (Stage 2)

1. Paste each prompt into the Image Generator GPT; save outputs to `generated-images/` with the file names above.
2. Convert each PNG to a WebP twin; place both in `images/`.
3. Replace placeholders 001, 002, 008, 010, 013, 017 in place; update `width`/`height` where sizes changed (002, 008, 010 → 1792 × 1024).
4. Wire new figures 003–007, 009, 011, 012, 014–016 into the listed sections with `<picture>` (webp + png), descriptive `alt`, `<p class="fig-desc">`, and `<dl class="fig-abbrevs">` using "Expansion (ACRONYM)" in each `<dd>`.
5. Confirm og:image meta still points to `inflammation-in-dialysis-og.webp` at 1200 × 630.
6. Run `patch_image_lightbox.py`, `audit_acronym_expansion.py`, and `audit_apa_references.py` for the guide; check light and dark mode.
7. When the full ZEUS report is published, regenerate 010 and 012 with updated wording and status badges.
