# Image Plan — *Green, Prepared and Resilient: Kidney Care in an Era of Climate Extremes* (`climate-extremes-kidney-care.html`)

**Guide:** Heat, typhoons, floods, power cuts, and smoke across CKD, dialysis, and transplant: dual patient/clinician, four languages
**Prepared:** 2026-11-10 · **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the
ChatGPT **Image Generator** GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` ·
`williamriveromd-biomedical-mechanism-figure` · `williamriveromd-algorithm-generator-skill` (house flowchart rules)

---

## Design intent: readable at every education level

Every figure in this guide has to work for three readers at once: a grandmother who reads little English, a caregiver skimming on a phone during a typhoon warning, and a nephrologist checking the physiology. To meet all three:

1. **Picture first, words second.** Each patient figure must make sense with the labels covered: a person, an action, an outcome. Labels confirm the picture; they never carry the message alone.
2. **One idea per figure.** No figure mixes heat physiology with storm logistics.
3. **Color means the same thing everywhere:** green = do this / safe; amber = prepare / caution; red = emergency / never; teal = information; gray = neutral infrastructure.
4. **Four to eight words per label, maximum.** Plain verbs ("Call your unit", "Cool down"), not nouns ("Communication protocol").
5. **Show Filipino life as it is:** sari-sari stores, tricycles, capiz windows, barangay halls, rain on GI-sheet roofs, but never disaster spectacle, injured people, or floodwater-swept victims.
6. **Clinician figures stay patient-safe.** No numbers that could be misread as personal targets.

## House rules baked into every prompt
- **Light backgrounds only** (white / off-white / soft gray / pale teal `#eef6f7`). Never navy / charcoal / black, even for storm scenes: render storms through *window views and gray clouds against a bright interior*.
- **Fonts:** on-image type is one of **Inter · Nunito Sans · IBM Plex Sans · Manrope**. No serif, no decorative.
- **Palette:** navy `#0f1e2e` (text/accents), clinical teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b`, red `#b91c1c`, used only as text/accents on light fills.
- **Rendering finish:** illustrated, softly shaded, semi-3D (rich editorial illustration). **Not flat clip-art or flat SVG vector**, and not cartoonish.
- **Attribution:** small semi-transparent `renalcarematters.com` bottom-right (bottom-center on portrait) on every image **except the wordless vignette hero**.
- **American English** in all on-image text.
- **Save each asset** as `.png` **and** a `.webp` twin under `images/`, using the exact FILE NAME below.

### Clinical guardrails for THIS guide (must hold in every graphic)
- **No fluid volumes, no water targets, no "drink X liters"**, and no glasses-of-water counts. Fluid plans are individual.
- **No "safe days without dialysis," no countdown clocks, no session-skipping imagery.**
- **No generic "clamp and cut" or disconnection steps**, no household water at a dialysis machine.
- **No heat-index numbers or PAGASA category colors** mapped to "safe/unsafe" activity.
- **No antibiotics** shown as flood prophylaxis.
- **No medicine-stopping imagery** (no crossed-out pills); medicine plans appear only as "written plan with your doctor."
- **Spent dialysate is never shown being reused.** RO reject reuse is drawn only for nonclinical uses (toilets, grounds).
- **Solar panels never imply backup power** unless a battery/generator is drawn and connected.
- **No real logos, brands, hospital names, or readable phone numbers.**

## Asset roster

| # | File (`images/…`) | Placement in guide | Skill | Size | Audience |
|---|---|---|---|---|---|
| 1 | `climate-extremes-kidney-care-vignette-hero.png` | Patient hero disc | hero-vignette (Scaffold A, archetype J) | 2048×2048 | Patients |
| 2 | `climate-extremes-kidney-care-og.png` | `og:image` share card | infographic (OG) | 1200×630 | Mixed |
| 3 | `climate-extremes-kidney-care-01-heat-kidney-pathway.png` | § Why It Matters | infographic (journey) | 1792×1024 | Patients |
| 4 | `climate-extremes-kidney-care-05-heat-exhaustion-vs-stroke.png` | § Hot Days | infographic (comparison) | 1792×1024 | Patients |
| 5 | `climate-extremes-kidney-care-04-modality-backup-plans.png` | § Storms & Outages | infographic (multi-panel) | 1792×1024 | Patients |
| 6 | `climate-extremes-kidney-care-02-continuity-chain.png` | § Your Unit | infographic (chain) | 1792×1024 | Mixed |
| 7 | `climate-extremes-kidney-care-03-heat-kidney-mechanism.png` | Clinician § Heat Physiology | biomedical-mechanism | 1792×1024 | Clinicians |
| 8 | `climate-extremes-kidney-care-07-disaster-roadmap.png` | Clinician § Unit Tabletop | algorithm / roadmap | 1024×1536 | Clinicians, unit staff |
| 9 | `climate-extremes-kidney-care-06-ro-water-flows.png` | Clinician § Stewardship | infographic (3D cutaway) | 1792×1024 | Clinicians, engineers |
| — | `climate-extremes-kidney-care-rg-thumb.webp` | Related-guide cards on 3 sibling guides | derived: 1:1 center crop of #2 or #1, export 220×160 | — | — |

> **Wiring status (2026-11-10).** All nine `<figure>`/hero/OG slots are already in the live HTML and point to these file names; until the files are committed, the alt text shows in place of each image. After adding files to `images/`, commit both `.png` and `.webp`. No HTML edit is needed unless dimensions change.

**Generation order (highest impact first):** 1 → 2 → 3 → 5 → 4 → 6 → 7 → 8 → 9.

---

## 1 · Circular vignette hero  *(patient hero disc)*

```
FILE NAME: climate-extremes-kidney-care-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A people
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling
CAMERA: slightly high-angle environmental portrait (three-quarter from above the table)
HUMAN VARIATION (vs. previous guide, incremental-dialysis: one woman in her late thirties, over-the-shoulder, wall calendar): two people instead of one; age 70s grandmother + 20s grandson instead of late-30s woman; male companion added; silver hair in a low bun vs. dark shoulder-length hair; round face with deep smile lines; grandson with a short undercut and thin-rimmed glasses; seated vs. standing; hands working together on a pouch vs. one hand on a calendar; faded floral duster and cardigan / gray hoodie vs. home blouse; frontal-high camera vs. over-the-shoulder; window and storm light vs. morning kitchen light; narra table vs. kitchen counter; calm focused expressions vs. reflective look
AUDIENCE: Patients and families
VISUAL GOAL: A calm family getting ready together before a storm, so preparation feels doable, not frightening.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: J, Environmental Storytelling — one cohesive scene, no floating panels. Camera: slightly high-angle environmental portrait looking down across the table.

Subject: a Filipino grandmother in her early seventies, slim, silver hair in a low bun, round face with deep smile lines, wearing a faded blue floral duster with a light cardigan, seated at a dark narra-wood table beside her grandson in his mid-twenties with a short undercut, thin-rimmed glasses, light-brown skin, and a soft gray hoodie. Together they are sliding a filled-in paper card (writing not legible) into a clear zip-lock waterproof pouch. On the table, small and secondary: a rechargeable desk fan, a small plastic medicine box with compartments, and a folded paper clinic document. Behind them, an open capiz-shell window shows soft gray rain clouds and a hint of swaying banana leaves; the room itself is BRIGHT, warm, and evenly lit by diffuse daylight, never dark. Expressions: calm, focused, quietly reassured, the grandson glancing at his grandmother.

Visual hierarchy: the two people and their hands with the pouch occupy 60–70% of the circle; the fan, medicine box, and window 20–30%; reserve a 20–25% TITLE SAFE ZONE in the upper-left of the circle as soft, out-of-focus pale wall and window light (no faces, objects, or details there).

Calm, documentary-realistic colour grade with soft teal #1a6b72 and warm neutral accents on a light background. Gentle edge falloff toward a slightly deeper warm neutral at the rim. Full-bleed within the inscribed circle; no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, readable writing on the card, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, moody storm lighting, floodwater in the room, fear or panic, cartoon style, neon, HDR, over-saturation, distorted hands or faces. No dialysis machine, no needles, no visible readable phone numbers.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. One dominant subject (two people preparing together), 2–4 supporting elements, 20–25% empty title-safe zone. Interior is bright even though the sky outside is cloudy. No legible text anywhere. Filipino home context; cast clearly different from the previous guide.
```

---

## 2 · Open Graph share card  *(og:image — FIXED 1200 × 630)*

```
FILE NAME: climate-extremes-kidney-care-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
AUDIENCE: Mixed (patients, families, clinicians on Facebook/Viber/X)
VISUAL GOAL: In one glance on a phone feed: heat + storm + kidney care + "be ready."

PROMPT:
Clean social share card for a kidney health education guide, 1200×630, white #ffffff background. Left 55%: typography in Inter. Small teal (#1a6b72) uppercase eyebrow "KIDNEY CARE · CLIMATE READY". Large bold navy (#0f1e2e) title on two lines: "Green, Prepared and Resilient". Below, in teal medium weight: "Heat, floods, power cuts and your kidneys". Under that, three small rounded pill chips in a row with simple line icons: a sun "Heat", a cloud with rain "Storms", a plug "Outages" (pills in very light teal #eef6f7 with navy text). Right 45%: a softly shaded semi-3D illustration (not flat clip-art) of a pair of healthy kidneys held gently in two cupped hands, with a thin protective teal shield arc over them; behind, a light sky split into a pale warm sun glow on one side and soft pale-gray rain clouds on the other, all on a white background with generous whitespace. Bottom-right corner: small semi-transparent navy text "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
Never a dark, navy, charcoal, or black background. No storm destruction, no flood victims, no thermometer showing a number, no heat-index values, no dialysis needles, no logos. No fonts other than Inter. No AI gibberish text; spell every word exactly as given. No cartoon style, no neon, no clutter.

QUALITY CHECK:
Exactly 1200×630. Title readable at thumbnail size. White background. Text spelled exactly. Attribution bottom-right. Calm, hopeful tone.
```

---

## 3 · Figure 01 — How heat reaches the kidneys  *(§ Why It Matters, patients)*

```
FILE NAME: climate-extremes-kidney-care-01-heat-kidney-pathway.png
IMAGE TYPE: Patient journey infographic (left-to-right pathway)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients and caregivers, any education level
VISUAL GOAL: Show, without jargon, the chain heat → sweat and skin blood flow → less blood to kidneys → kidney injury, and where cooling breaks the chain.

PROMPT:
Landscape patient-education pathway infographic, white #ffffff background, softly shaded semi-3D editorial illustration (not flat clip-art), Nunito Sans typography, large mobile-readable labels of 2–5 words.
Top title in navy Nunito Sans bold: "How heat reaches your kidneys".
A single left-to-right path of four large illustrated stops connected by thick soft teal arrows:
Stop 1 — a Filipino man in his fifties in a straw hat and work shirt under strong sun, sweat drops visible. Label: "Heat and hard work".
Stop 2 — a semi-transparent body silhouette showing blood vessels near the skin glowing warm red and widened, and sweat drops leaving. Label: "Blood moves to the skin. Water and salt are lost in sweat".
Stop 3 — a pair of kidneys with thinner incoming blood vessels and a small downward arrow beside them. Label: "Less blood reaches the kidneys".
Stop 4 — a kidney with a small amber warning triangle. Label: "Sudden kidney injury".
A thinner side branch from Stop 1 drops below to a small illustration of a tired arm muscle with tiny red particles flowing toward the kidney. Label: "Very hard work can break down muscle".
Along the bottom, a light-green rounded band labeled "Break the chain" with three icons and short labels in renal green #1f7a4d: a shaded tree "Shade and rest", a fan and cool cloth "Cool down", a phone "Call your kidney team early".
Bottom-right: small semi-transparent navy "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No water glasses or drink amounts, no liters, no numbers of any kind, no thermometer readings, no heat-index scale. No dark backgrounds. No serif fonts. No medical jargon on the image (no "perfusion", "GFR", "rhabdomyolysis"). No gore, no collapsed person in this figure. No AI gibberish text; spell labels exactly.

QUALITY CHECK:
A reader who covers all labels still understands sun → sweat → kidney → warning, and green means "what helps." Max 8 words per label. White background. Attribution present.
```

---

## 4 · Figure 05 — Heat exhaustion or heat stroke?  *(§ Hot Days, patients)*

```
FILE NAME: climate-extremes-kidney-care-05-heat-exhaustion-vs-stroke.png
IMAGE TYPE: Side-by-side comparison infographic
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients, caregivers, neighbors
VISUAL GOAL: Recognize the difference at a glance and know the one action for each side.

PROMPT:
Landscape two-column comparison infographic on an off-white #fafafa background, softly shaded semi-3D editorial illustration, Manrope typography, large readable labels.
Left column header in a renal-green #1f7a4d rounded banner: "Heat exhaustion". Illustration: a Filipino man in his late sixties with a short gray crew cut, sitting on a plastic monobloc chair in the shade of a sari-sari store awning, sweaty and tired but alert, a fan nearby and a damp towel on his neck. Three icon rows beneath with short labels: eye-open icon "Thinking clearly", sweat-drop icon "Sweaty, dizzy, tired", and an action row with three green icons: "Move to a cool place", "Rest and cool the skin", "Call your kidney team".
Right column header in a clinical-red #b91c1c rounded banner: "Heat stroke — emergency". Illustration: the same street setting; a different older man (thin, receding hairline, flushed skin) slumped and confused on a wooden bench while a woman neighbor in a yellow T-shirt calls on her phone and a teenage boy cools his arms and neck with a wet cloth. Icon rows: swirl icon "Confused or collapsing", flame-skin icon "Very hot skin", and an action row with three red icons: "Call emergency now", "Keep cooling while waiting", a glass with a red slash "No drinks if confused".
A thin vertical teal divider between columns. Bottom-right: small semi-transparent navy "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No temperatures or numbers. No ice baths, no IV lines, no ambulance branding or real hotline numbers. No dark backgrounds, no dramatic lighting, no fear imagery. No serif fonts. Spell labels exactly; no gibberish.

QUALITY CHECK:
The two sides read instantly by color (green vs red) and posture (resting vs collapsed). The "no drinks if confused" icon is clear. Attribution present.
```

---

## 5 · Figure 04 — Which backup plan is mine?  *(§ Storms & Outages, patients)*

```
FILE NAME: climate-extremes-kidney-care-04-modality-backup-plans.png
IMAGE TYPE: Multi-panel educational infographic (5 panels)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients on any kidney treatment, and families
VISUAL GOAL: Let each reader find "their" panel and see the one key backup action for it.

PROMPT:
Landscape patient-education infographic, white #ffffff background, five equal rounded cards in a single row (light teal #eef6f7 card fill, thin teal border), softly shaded semi-3D editorial illustration in each card, IBM Plex Sans typography. Top title in navy bold: "Which backup plan is mine?" Small subtitle in teal: "Find your card. Make the plan before the storm."
Card 1 — header "In-center hemodialysis": a Filipino woman in her forties with short wavy hair and a green raincoat stepping into a white van, holding a clear waterproof document folder; a small sign of a second dialysis center in the background. Label: "Backup unit + backup ride".
Card 2 — header "Home hemodialysis": a home dialysis machine (generic, no brand) in a bright room, a hand holding a phone with a call icon, and a water tap with a red slash beside it. Label: "Call your home program first".
Card 3 — header "Peritoneal dialysis": stacked plain PD supply boxes on a raised shelf, dry, above a floor with a small puddle; a small rain cloud icon. Label: "Supplies dry and off the floor".
Card 4 — header "Kidney transplant": a young Filipino man in his late twenties with a buzz cut holding a weekly pill organizer, standing by a generic pharmacy counter with a cross sign (no brand). Label: "Medicine refill plan".
Card 5 — header "CKD": an older Filipino woman with reading glasses and a doctor in a white coat looking together at a written plan on a clipboard (writing not legible). Label: "Written hot-day plan".
Bottom band across all cards in amber #b8860b text on very light cream: "If a treatment is at risk, call early. Do not wait for symptoms." Bottom-right: small semi-transparent navy "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No needles in arms, no blood lines, no disconnection or clamping steps, no household water near the machine, no numbers of days or supplies, no brand logos, no crossed-out pills. No dark backgrounds. No serif fonts. Spell all text exactly; no gibberish.

QUALITY CHECK:
Five cards equal in size and dignity. Each card readable on a phone when cropped alone. Bottom message reads clearly. Attribution present.
```

---

## 6 · Figure 02 — Six links that keep dialysis going  *(§ Your Unit, patients and staff)*

```
FILE NAME: climate-extremes-kidney-care-02-continuity-chain.png
IMAGE TYPE: Chain / process infographic
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients, families, dialysis staff
VISUAL GOAL: Make it obvious that dialysis stops if any single link fails, and that each link has an owner.

PROMPT:
Landscape infographic on a white #ffffff background, softly shaded semi-3D illustration, Inter typography. Title in navy bold: "Six links keep dialysis going in a disaster".
Across the center, a horizontal chain of six large interlocking rounded rings in clinical teal #1a6b72, each ring framing one illustrated icon with a short label beneath:
1 — a phone with an SMS bubble: "Patients contacted"
2 — a white van on a road: "Ride confirmed"
3 — a Filipino dialysis nurse in teal scrubs beside stacked supply boxes: "Staff and supplies"
4 — a lightning bolt and a water drop side by side: "Power and safe water"
5 — a generic dialysis machine: "Machines working"
6 — a calendar with a green check: "Sessions done, then follow-up"
Ring 4 is shown with a small crack and a tiny blue flood wave lapping at it, with an amber caption beside it: "One weak link stops the chain".
Below the chain, a light-gray rounded strip with three small owner tags in navy: "Patient outreach lead", "Clinical and facilities leads", "Incident lead". Bottom-right: small semi-transparent navy "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No numbers, no generator capacities, no water volumes, no specific hours. No storm destruction or injured people. No brand logos. No dark backgrounds, no serif fonts, no gibberish text.

QUALITY CHECK:
Six rings evenly spaced and legible; the cracked ring is noticeable but not alarming. Labels ≤ 6 words. Attribution present.
```

---

## 7 · Figure 03 — Heat to tubular injury (mechanism)  *(clinician § Heat Physiology)*

```
FILE NAME: climate-extremes-kidney-care-03-heat-kidney-mechanism.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Clinicians
VISUAL GOAL: Organ → nephron → injury/intervention/benefit, with established mechanisms visually separated from hypothesized ones.

PROMPT:
Create a publication-grade biomedical mechanism schematic on a white background, review-article figure style with soft semi-3D shading (refined illustration, not flat clip-art), muted clinical palette, thin dashed connector lines, IBM Plex Sans labels.
Topic: Heat stress and the kidney. Disease context: heat-related AKI and possible CKD progression.
Left organ-level panel: a simplified human torso outline with dilated, warm-red cutaneous vessels and sweat droplets at the skin; a small heart with an arrow labeled "↑ Cardiac output to skin"; below, kidneys with thinner renal arteries labeled "↓ Renal blood flow". A small leg-muscle inset shows fibers breaking apart labeled "Rhabdomyolysis → myoglobin". A dashed connector box points to the magnified panel.
Center/right magnified panel inside a dashed border: a nephron with the proximal tubule highlighted pale yellow. Callouts in solid boxes (established): "↓ GFR with volume depletion", "Proximal tubular hypoperfusion", "Myoglobin casts and tubular toxicity". Callouts in DASHED-OUTLINE boxes labeled with a small italic tag "proposed": "Hyperosmolality → ↑ vasopressin", "Polyol–fructokinase pathway", "↑ Uric acid". A small legend: solid box = established; dashed box = hypothesis.
Bottom summary flow with arrows:
Left pale-pink box: "Heat load + volume loss" / "Diuretics, RAAS blockade, SGLT2 inhibitors narrow reserve" / "Recurrent subclinical injury (hypothesis)" / **"Heat-related AKI"**.
Center box: "Cooling, shade, rest" / "Individualized fluid and medicine plan" / "Early assessment".
Right pale-blue box: "Restored perfusion" / "Fewer AKI episodes" / "Possible slower decline (unproven)".
Bottom-right: small semi-transparent navy "© renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No numeric thresholds, no heat-index values, no fluid volumes, no drug doses. Do not present vasopressin, fructokinase, or uric acid as proven causes. No photorealism, no dark backgrounds, no serif fonts, no decorative icons, no gibberish text.

QUALITY CHECK:
Organ → inset → bottom flow reads left-to-right. Established vs hypothesized visibly distinguished. Labels legible at slide size. Attribution present.
```

---

## 8 · Figure 07 — Prepare, respond, recover (roadmap)  *(clinician § Unit Tabletop)*

```
FILE NAME: climate-extremes-kidney-care-07-disaster-roadmap.png
IMAGE TYPE: Clinical algorithm / roadmap (vertical)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Nephrologists, dialysis unit managers, nurses
VISUAL GOAL: The ABCs → DIAL → ARC loop on one page a unit can pin to the wall.

PROMPT:
Vertical clinical roadmap infographic, KDIGO-style guideline flowchart aesthetic, white #ffffff background, Inter typography, rounded nodes, generous whitespace, mobile-readable.
Title in navy bold: "Kidney care disaster roadmap". Subtitle in teal: "Prepare · Respond · Recover".
Three stacked phase blocks connected by thick downward arrows:
PREPARE — teal #1a6b72 header "Before the season: the ABCs". Seven compact rounded nodes in a 2-column grid: "Assess risks and vulnerable patients", "Build a task force", "Capacity: staff, supplies, power, water", "Communication plan and offline roster", "Coach patients and staff", "Contingency and surge plan", "Strategic partner units".
RESPOND — amber #b8860b header "During the event: DIAL". Four nodes in a vertical sequence: "Damage and scope assessment", "Initiate the action plan", "Appraise regularly", "Liaise, engage, update".
RECOVER — renal green #1f7a4d header "After: the ARC". Three nodes: "Assess damage (water gate before restart)", "Return to the new norm", "Collect data to improve".
A curved thin teal arrow runs from RECOVER back up the right margin to PREPARE, labeled "Lessons feed the next plan".
Small footnote in gray: "Adapted from Sandal et al., JASN 2025". Bottom-center: small semi-transparent navy "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No spaghetti arrows, no more than 3 levels. No numbers, hours, or capacity values. No patient triage or ranking imagery. No dark backgrounds, no serif fonts, no gibberish text.

QUALITY CHECK:
Three phases instantly distinguishable by color. Every node ≤ 7 words. Readable on a phone in portrait. Attribution bottom-center.
```

---

## 9 · Figure 06 — Where dialysis water goes  *(clinician § Stewardship)*

```
FILE NAME: climate-extremes-kidney-care-06-ro-water-flows.png
IMAGE TYPE: 3D cutaway infographic (facility)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Clinicians, dialysis engineers, unit managers
VISUAL GOAL: Make the difference between RO permeate, RO reject, and spent dialysate unmistakable, and show where meters belong.

PROMPT:
Landscape semi-3D isometric cutaway of a small dialysis-unit water room on a white #ffffff background, clean engineering-illustration style with soft shading, Manrope typography, color-coded pipes.
Left: a "City water" inlet pipe enters a pretreatment train (sediment filter, softener, carbon tanks, drawn as generic cylinders) and then a reverse osmosis skid. Small round meter dials sit on three pipes, each with a tiny tag: "Feed meter", "Permeate meter", "Reject meter".
From the RO skid, a bright BLUE pipe labeled "Permeate → dialysis" runs right to two generic dialysis machines.
A separate GRAY pipe labeled "Reject (not dialysate)" runs down to a storage tank with a small check-valve icon labeled "Cross-connection protection", then on to a toilet and a garden tap, labeled "Approved nonclinical uses only".
From the dialysis machines, a BROWN pipe labeled "Spent dialysate" goes straight to a drain with a red stop sign and the label "Never reused".
Top title in navy bold: "Where dialysis water goes". A small teal note box top-right: "Reuse displaces fresh water elsewhere; it does not reduce RO feed."
Bottom-right: small semi-transparent navy "renalcarematters.com".

NEGATIVE INSTRUCTIONS:
No liters, percentages, or recovery numbers. No brand logos on equipment. Spent dialysate must never connect to the reuse tank. No solar panels. No dark backgrounds, no serif fonts, no gibberish text.

QUALITY CHECK:
Three water streams visually distinct by color and label; the dialysate-to-drain stop sign is unmissable. Meters on feed, permeate, and reject. Attribution present.
```

---

## Derived asset

- **`climate-extremes-kidney-care-rg-thumb.webp`** — 1:1 center-crop of the OG card's illustration side (#2) or of the hero (#1), exported at 220×160 for the related-guide cards on `typhoon-disaster-preparedness-dialysis`, `el-nino-heat-dialysis`, and `green-nephrology`.

## After generation (Stage 2 checklist)
1. Save each file to `images/` as `.png` + `.webp` twin with the exact names above.
2. Confirm the OG card is exactly 1200×630.
3. Re-run `python3 patch_hero_fetchpriority.py --guide climate-extremes-kidney-care.html` and `patch_image_lightbox.py` (idempotent).
4. Spot-check each figure against the clinical guardrails at the top. Reject any image that invents numbers, shows reuse of dialysate, or contains garbled text.
