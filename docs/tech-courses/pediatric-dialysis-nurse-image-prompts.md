# Pediatric Dialysis Nurse track: image plan blueprint and GPT prompt pack

Renal Care Academy → Nephrology Nursing Track → By Specialization → Pediatric Dialysis Nurse. Prepared November 27, 2026. American English throughout. Stage 1 of the two-stage image pipeline: generate in ChatGPT image generation, then run the prep script (Stage 2).

## 1. Why these images

Every image has one job: make a pediatric dialysis decision easier to understand, apply, or appreciate. This track turns on size: small bodies, small volumes, small margins. So the teaching figures show proportions (circuit to blood volume, fill volume to body surface area), worked arithmetic, and decision paths, while the heroes show children and families as people first, cared for at eye level.

| Image | Learning purpose | Where it appears | Count |
| --- | --- | --- | --- |
| **Circular vignette hero** | Appreciation: who is involved, where, and what is at stake | Top of the course home and each module | 21 |
| **Teaching figure** | Understanding (the central idea) and application (a check, flow or card to use on shift) | Already wired into the module text through `figs.py`; each image appears as soon as it is placed | 41 |
| **Course tile** | Navigation: recognition on the syllabus cards and module tiles | Course home module cards; Related Guides thumbnails | 21 |
| **OG share card** | Reach: a share preview that names the page | `og:image` for the course home and each module (`images/og/<slug>-og.jpg`) | 21 |
| **Toolkit OG card** | Reach for the calculator page | `og:image` of `guides/calc-pediatric-dialysis-nurse-toolkit.html` | 1 |
| **Track share-card art** | Background for the Academy composited track card (text set by `build_academy_og.py`) | `images/academy/og-art/pediatric-dialysis-nurse.webp` | 1 |
| **Landing tile** | The Pediatric Dialysis Nurse card on `academy/index.html` | `images/academy/landing/pediatric-dialysis-nurse.webp` | made from the course tile |

**Total: 106 prompts.**

## 2. Rules for every image

- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c, purple #6c3d8e; the Nephrology Nursing track accent is teal #1a6b72.
- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). American English spelling on every label.
- **Attribution:** teaching figures and OG cards carry `© renalcarematters.com` bottom-right (public Academy pages, not patient documents). Heroes and tiles carry no text.
- **Children:** fictional Filipino children only, calm, fully clothed, treated with dignity; no crying or frightened close-ups; no needles in a child’s skin; child-sized equipment; a PD exit site shown only with the shirt raised just enough.
- **Numbers:** an image carries only the numbers written in its prompt, each already in the module and verified (10% rule; 800 and 1,400 mL/m²; 3.3 → 0.8; 0.63 → 0.42; 0.4 benchmark; 300 mL ÷ 3 h ÷ 20 kg; 3.8 − 1.3 L ÷ 25 kg). No drug names or doses on any image.
- **Tunneled catheters:** every image that shows one follows the tunneled-dialysis-catheter-path lock (right internal jugular route, exit on the right upper chest, cuff inside the tunnel, red arterial and blue venous clamps). Heroes show only the chest dressing.
- **People:** a different cast, camera and setting in each hero (hero-vignette v3 human-variation rule).
- **Skills used:** `williamriveromd-hero-vignette` v3 (heroes), `williamriveromd-infographic-skill` v5 (figures, tiles, OG cards), `williamriveromd-simple-figure` (single-idea figures), `williamriveromd-algorithm-generator-skill` (decision paths), `tunneled-dialysis-catheter-path` (catheter anatomy).

## 3. Production workflow

1. Generate each prompt in ChatGPT image generation. Save each PNG with the exact FILE NAME stem into `images/incoming/pediatric-dialysis-nurse/` in the repo (track art in a subfolder `og-art/`), or first into the working folder `~/Downloads/Pedia Dialysis Nurse/images/` for audit.
2. Run `python3 tools/techcourses/pdn/prep_images.py` (`--report` lists what is still missing). It writes heroes to `images/<slug>-vignette-hero.png` + `.webp`, figures to `images/<stem>.webp` + `.png`, tiles to 640 × 360 WebP (the course tile also to `images/academy/landing/pediatric-dialysis-nurse.webp` 960 × 540), OG cards to 1200 × 630 JPEG ≤ 300 KB in `images/og/`, and the track art to `images/academy/og-art/pediatric-dialysis-nurse.webp`.
3. Rebuild: `python3 generate_tech_courses.py --course pdn --patch`; `python3 tools/techcourses/pdn/expand_acronyms.py`; `python3 build_academy_og.py --art images/academy/og-art --only pediatric-dialysis-nurse --patch` and `--only academy-index`; `python3 generate_rg_thumbs.py`; `python3 patch_rg_card_thumbs.py`.
4. Audit each image against its QUALITY CHECK, check one module in light and dark mode, and paste one module URL into the Facebook Sharing Debugger. Write corrected prompts for any failures in a new MD file in the working folder.

## 4. Image map by module

| Module | Hero idea | Teaching figures (section) |
| --- | --- | --- |
| Course home | A child on dialysis is still a child; the nurse meets her at her level. | Small body, small margins (Module 1, big picture) |
| 1. The Pediatric Dialysis Nurse: Role, Scope and the Child’s Journey | Know your authorization before your first shift. | Four separate authorizations (`separate-authorizations`); The child’s kidney journey (`the-childs-journey`) |
| 2. Why Children’s Kidneys Fail, and How a Modality Is Chosen | Why this child’s kidneys failed shapes everything that follows. | Causes change with age and region (`causes-by-age`); Choosing a modality with the family (`choosing-a-modality`) |
| 3. Development, Assent, Consent and Safeguarding | Speak to the child first, at her eye level, and ask for her agreement. | Talking with a child at each age (`talking-by-age`); Assent beside consent (`assent-and-consent`) |
| 4. Assessment, Fluid Balance and Weight-Based Arithmetic | Small bodies leave small margins; measure carefully. | Every route counts (`every-route-counts`); Arithmetic with units (`arithmetic-with-units`) |
| 5. Infection Prevention and Access Protection | Hands and hubs are the main gates; keep them clean. | How organisms reach the child (`chain-of-transmission`); Bundles that lowered infection (`bundles-that-work`) |
| 6. Medication Safety in Children on Dialysis | Every pediatric dose is a calculation; check it twice. | The ten-fold error (`ten-fold-errors`); The independent double check (`the-checked-dose`) |
| 7. PD in Children: Physiology, Readiness and the Prescription | PD in children lets therapy happen at home while they sleep. | Fill volume is scaled to body surface area (`fill-volume-and-pressure`); Reading a pediatric PD order (`reading-the-order`) |
| 8. The PD Catheter, Exit Site and Mechanical Problems | Protect the exit site and you protect the catheter. | Catheter design and exit site (`catheter-design`); When it will not drain (`when-it-will-not-drain`) |
| 9. CAPD: A Supervised Exchange in a Small Body | Connection and disconnection deserve full attention. | The exchange in a small body (`the-exchange`); Dry versus wet contamination (`contamination`) |
| 10. APD: Cycler Setup, Alarms and Home Monitoring | The cycler follows the order exactly; check the order first. | Cycling small volumes (`small-volume-cycling`); Alarms as clinical signals (`alarms-as-signals`) |
| 11. PD Peritonitis and Exit-Site Infection: The First Hour | A cloudy bag starts the clock; the first hour matters. | Two of four (`recognizing-peritonitis`); The first hour (`the-first-hour`) |
| 12. Pediatric Hemodialysis: Prescription Logic and Vascular Access | Every vein a child keeps today is an access for tomorrow. | Access for a lifetime (`access-for-a-lifetime`); The catheter care bundle (`catheter-care`) |
| 13. The Small Circuit: Blood Volume, Priming, Water and Preparation | The circuit must be small compared with the child. | The 10% rule (`blood-volume-and-the-circuit`); The priming decision (`priming-decisions`) |
| 14. The Hemodialysis Session: Initiation, Monitoring and Completion | Watch the child, not only the numbers. | First sessions and disequilibrium (`first-sessions-and-disequilibrium`); Monitoring during the session (`fluid-removal-in-children`) |
| 15. Emergencies and Pediatric Resuscitation Readiness | Know your role before the emergency. | Early warning in children (`recognize-early`); Air in the venous line (`dialysis-emergencies`) |
| 16. AKI, Acute PD and Continuous Kidney Replacement Therapy | Acute PD can save a child where machines are scarce. | Percent fluid overload (`fluid-overload`); Acute PD where machines are scarce (`acute-pd`) |
| 17. Growth, Nutrition, Anemia and Bone | Growth is an outcome; measure it every time. | Growth is an outcome (`growth-is-an-outcome`); The feeding team (`feeding-the-child`) |
| 18. Teaching Caregivers, Home Support and Disaster Planning | Readiness is shown, not counted. | Readiness by return demonstration (`readiness-by-demonstration`); Typhoon and outage plan (`home-and-disaster-plans`) |
| 19. Adolescence, School, Transplant and Transition | Treat the adolescent as a partner; transition is a process. | Transition is a process (`transition`); Preparing for transplant (`transplant-preparation`) |
| 20. Philippine Requirements, Records, Quality and Capstone | Know who governs what, count honestly, and improve one thing at a time. | Who governs what (`who-governs-what`); Infection-rate arithmetic (`measuring-quality`) |

## 5. Track-level images

### Course home hero

```
FILE NAME: images/pediatric-dialysis-nurse-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: eye level, medium-wide
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: A child on dialysis is still a child; the nurse meets her at her level.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: eye level, medium-wide. Subject: a Filipina pediatric dialysis nurse in her late 30s with a round face, a low bun of black hair and teal scrubs with a small cartoon-free lanyard, kneeling at eye level beside a seven-year-old girl in a child-sized dialysis chair; the girl wears a yellow T-shirt and holds a picture book on her lap while her mother sits close holding her hand; a softly blurred child-sized hemodialysis machine and colorful but uncluttered wall in a bright pediatric dialysis room, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

### Track figure: Small body, small margins (Module 1 big picture)

```
FILE NAME: images/pediatric-dialysis-nurse-00-small-body-small-margins.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Comparison infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Small body, small margins". Two side-by-side panels. Left: a semi-photoreal Filipino adult silhouette labeled "Adult 70 kg" with a tall bar labeled "Blood volume about 5,600 mL" and a small teal slice labeled "200 mL circuit = about 4%". Right: a toddler silhouette labeled "Child 10 kg" with a short bar labeled "Blood volume about 800 mL" and a large amber slice labeled "200 mL circuit = 25%". Footer: "Teaching estimate: 80 mL/kg". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Small body, small margins. The same 200 mL outside the body is about 4% of an adult’s blood volume and a quarter of a 10-kilogram child’s (teaching estimate of 80 mL/kg).
*Alt text:* Side-by-side silhouettes of a 70-kilogram adult and a 10-kilogram toddler, each with a bar showing estimated blood volume (about 5,600 mL and 800 mL) and the same 200 mL circuit shaded: about 4% of the adult's blood volume and 25% of the child's.

### Course tile and Academy landing tile

```
FILE NAME: images/pediatric-dialysis-nurse-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP; the course tile also writes images/academy/landing/pediatric-dialysis-nurse.webp 960 × 540)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the track’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a small child-sized dialysis chair with a folded yellow blanket and a soft teddy bear sitting on it, in a bright clean room. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

### Course home OG card

```
FILE NAME: images/og/pediatric-dialysis-nurse-og.png (prep script exports images/og/pediatric-dialysis-nurse-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Pediatric Dialysis Nurse". Subtitle in teal #1a6b72: "20 modules · PD and hemodialysis for infants, children and teens". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a small child-sized dialysis chair with a folded yellow blanket and a soft teddy bear sitting on it, in a bright clean room, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Toolkit OG card

```
FILE NAME: images/og/pediatric-dialysis-nurse-toolkit.png (prep script exports images/og/pediatric-dialysis-nurse-toolkit.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Pediatric Dialysis Nurse Toolkit". Subtitle in teal #1a6b72: "6 tools · fill volume · circuit volume · fluid · infection rates". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a calculator, a pediatric scale, a small PD bag and a clipboard with a blurred grid, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Track share-card art (Academy composited card)

```
FILE NAME: images/incoming/pediatric-dialysis-nurse/og-art/pediatric-dialysis-nurse.png (prep script writes images/academy/og-art/pediatric-dialysis-nurse.webp)
SKILL: williamriveromd-infographic-skill v5 (background art)
IMAGE TYPE: Background art for build_academy_og.py (the script sets every word)
PIXEL DIMENSIONS: 1536 × 1024

PROMPT:
3:2 landscape photorealistic editorial photograph on a light background: in a bright Philippine pediatric dialysis room, a Filipina nurse in her late 30s with a low bun and teal scrubs kneels at eye level beside a seven-year-old girl in a child-sized dialysis chair; the girl holds a picture book and her mother sits close. Place the people in the RIGHT 55%; keep the LEFT 45% as clean, light, empty negative space (soft wall and window light) where the builder sets the track title, group label and stats. Soft daylight, gentle depth of field, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Absolutely NO text, logos or watermark; no legible screens or papers.

NEGATIVE INSTRUCTIONS:
Avoid text, clutter, dark backgrounds, distressed or crying children, needles in skin, legible documents, people in the left 45%.

QUALITY CHECK:
Left 45% empty and light; subjects on the right; child calm; no text.
```

## 6. Module prompts

### Module 1: The Pediatric Dialysis Nurse: Role, Scope and the Child’s Journey

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-01-role-scope-and-the-childs-journey-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder, slightly high
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Nurses
VISUAL GOAL: Know your authorization before your first shift.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder, slightly high. Subject: a young Filipino nurse in his early 30s with short wavy hair, rimless glasses and navy scrubs speaking with a senior Filipina nurse educator in her 50s with short gray-streaked hair and a white cardigan, both looking at a closed binder at a nurses’ station outside a pediatric dialysis room; a child’s drawing taped to the glass behind them (blurred), soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Four separate authorizations**  ·  skill `infographic-skill`  ·  placed in section `separate-authorizations`  ·  key `pdn01_a`

```
FILE NAME: images/pediatric-dialysis-nurse-01-four-separate-authorizations.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Stacked card infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Four separate authorizations". Four stacked rounded cards with icons, top to bottom: "1 License — PRC", "2 Modality training", "3 Facility authorization — modality, device, age and size band" (teal highlight), "4 Clinical privileges". An arrow leads to a nurse beside a child-sized dialysis chair. Footer chip in amber: "No course certificate replaces any of them." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Four separate authorizations. Each answers a different question; no course certificate replaces any of them.
*Alt text:* Four stacked cards labeled license, modality training, facility authorization by modality and age band, and clinical privileges, each with a small icon, leading to a nurse at a pediatric dialysis chair.

**Figure B: The child’s kidney journey**  ·  skill `simple-figure`  ·  placed in section `the-childs-journey`  ·  key `pdn01_b`

```
FILE NAME: images/pediatric-dialysis-nurse-01-the-childs-kidney-journey.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Journey path illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The child’s kidney journey". A gentle winding path left to right with five stops: "CKD care", "Preparation", "PD or hemodialysis", "Transplant", "Transition to adult care". The same child grows older along the path (toddler, school child, teen, young adult). A small nurse icon stands at every stop. A thin dashed loop from "Transplant" back to "PD or hemodialysis" labeled "If a transplant fails". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The child’s kidney journey. Dialysis is one stage of a path that usually leads to transplant and, later, adult care.
*Alt text:* A winding path from diagnosis through CKD care, preparation, PD or hemodialysis, transplant and transition to adult care, with a child growing older along the path and the nurse appearing at each stage.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-01-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a nurse’s lanyard with a blank badge resting on a closed binder beside a child’s crayon. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-01-role-scope-and-the-childs-journey-og.png (prep script exports images/og/pediatric-dialysis-nurse-01-role-scope-and-the-childs-journey-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "The Pediatric Dialysis Nurse: Role, Scope and the Child’s Journey". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 1 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a nurse’s lanyard with a blank badge resting on a closed binder beside a child’s crayon, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 2: Why Children’s Kidneys Fail, and How a Modality Is Chosen

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-02-pediatric-kidney-failure-and-modality-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: side profile, medium distance
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Why this child’s kidneys failed shapes everything that follows.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: side profile, medium distance. Subject: a Filipina mother in her late 20s with a ponytail and a floral blouse holding her three-year-old son on her lap in a clinic room while a nurse in light-blue scrubs shows them a simple model of a kidney; the toddler reaches for the model, curious, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Causes change with age and region**  ·  skill `simple-figure`  ·  placed in section `causes-by-age`  ·  key `pdn02_a`

```
FILE NAME: images/pediatric-dialysis-nurse-02-causes-change-with-age.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Age band chart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Causes change with age and region". A horizontal age band from "Infant" to "Adolescent". Above the young end, a large teal block "CAKUT and hereditary disease"; above the older end, a purple block rising "Immune-mediated glomerular disease". A small map chip of Southeast Asia: "Southeast Asia: immune-mediated glomerular disease most common". A gray chip: "Cause unknown in 14% worldwide". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Causes change with age and region. Congenital and hereditary diseases lead in young children; immune-mediated glomerular disease is the most common cause in Southeast Asia.
*Alt text:* A horizontal age band from infant to adolescent: congenital anomalies and hereditary disease dominate the younger end; immune-mediated glomerular disease rises toward adolescence, with a note that it is the most common cause in Southeast Asia.

**Figure B: Choosing a modality with the family**  ·  skill `infographic-skill`  ·  placed in section `choosing-a-modality`  ·  key `pdn02_b`

```
FILE NAME: images/pediatric-dialysis-nurse-02-choosing-a-modality-with-the-family.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Decision illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Choosing a modality with the family". A Filipino family (mother, father, school-age child) at a round table with a nurse and a pediatric nephrologist. Three cards on the table: "PD at home", "Hemodialysis in a center", "Transplant before dialysis". Around them, five small icons with labels: "Age and size", "Home and caregivers", "Distance", "Abdomen and access", "School". Footer: "The best modality is the one this family can do safely." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Choosing a modality with the family. Age and size, the home, school, distance and who can provide care all shape the choice.
*Alt text:* A family seated with a nurse and pediatric nephrologist around a table with three cards for PD at home, hemodialysis in a center, and preemptive transplant, surrounded by small icons for age and size, school, distance, caregivers and vascular access.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-02-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a simple anatomical kidney model beside a toddler’s wooden toy block. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-02-pediatric-kidney-failure-and-modality-og.png (prep script exports images/og/pediatric-dialysis-nurse-02-pediatric-kidney-failure-and-modality-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Why Children’s Kidneys Fail, and How a Modality Is Chosen". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 2 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a simple anatomical kidney model beside a toddler’s wooden toy block, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 3: Development, Assent, Consent and Safeguarding

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-03-development-assent-consent-and-safeguarding-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F Human Connection
CAMERA: low angle at child’s eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Speak to the child first, at her eye level, and ask for her agreement.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Human Connection. Camera: low angle at child’s eye level. Subject: a Filipina nurse in her 40s with a short bob and a lavender scrub top crouched beside a nine-year-old girl in a dialysis chair, both looking at a small picture card the girl holds; the girl’s father stands slightly behind, one hand on the chair, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Talking with a child at each age**  ·  skill `simple-figure`  ·  placed in section `talking-by-age`  ·  key `pdn03_a`

```
FILE NAME: images/pediatric-dialysis-nurse-03-talking-with-a-child-at-each-age.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Four-panel infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Talking with a child at each age". Four panels left to right, each with a semi-photoreal scene and one short tip: "Infant — comfort and the parent close"; "Toddler — short honest words just before"; "School age — reasons and real choices"; "Adolescent — privacy and a say". The nurse is at eye level in every panel. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Talking with a child at each age. Match words, tools and privacy to the stage, not only to the age in years.
*Alt text:* Four panels: an infant held by a parent, a toddler with a toy, a school-age child looking at a picture of a kidney, and a teenager speaking privately with the nurse, each with one short communication tip.

**Figure B: Assent beside consent**  ·  skill `algorithm-generator-skill`  ·  placed in section `assent-and-consent`  ·  key `pdn03_b`

```
FILE NAME: images/pediatric-dialysis-nurse-03-assent-and-consent.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Two-track flow
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Assent beside consent". Two parallel lanes: top lane "Parent or guardian: informed consent"; bottom lane "Child: assent in words that fit the age". Both meet at "Shared plan". From the child lane, a branch "Child says no" leads to three steps: "Pause if safe", "Find the fear", "Change what you can". A small amber note: "Urgent care: least restrictive approach, document". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Assent beside consent. Parents consent; children are asked, in their own terms, and their answer is taken seriously.
*Alt text:* Two parallel tracks: the parent or guardian giving informed consent and the child giving assent in words that fit their age, joining at a shared decision, with a branch for what to do when the child says no.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-03-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two chairs of different heights facing each other, one child-sized, with a picture card on the small one. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-03-development-assent-consent-and-safeguarding-og.png (prep script exports images/og/pediatric-dialysis-nurse-03-development-assent-consent-and-safeguarding-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Development, Assent, Consent and Safeguarding". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 3 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two chairs of different heights facing each other, one child-sized, with a picture card on the small one, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 4: Assessment, Fluid Balance and Weight-Based Arithmetic

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-04-assessment-fluid-and-calculations-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C Still-Life
CAMERA: top-down flat lay
HUMAN VARIATION: No people
AUDIENCE: Nurses
VISUAL GOAL: Small bodies leave small margins; measure carefully.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Still-Life. Camera: top-down flat lay. Subject: a pediatric digital scale, a small blood pressure cuff in a child size beside a larger one, a measuring tape, a calculator and a clipboard with a blurred chart arranged neatly on a clean white treatment table, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Every route counts**  ·  skill `simple-figure`  ·  placed in section `every-route-counts`  ·  key `pdn04_a`

```
FILE NAME: images/pediatric-dialysis-nurse-04-every-route-counts.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Fluid balance diagram
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Every route counts". A child at the center of a balance scale. Left pan labeled "In" with icons: "Feeds", "Drinks", "IV fluids", "Flushes", "Medicines". Right pan labeled "Out": "Urine", "Stool", "Drains", "Dialysis removal". A teal callout on the flushes: "10 flushes × 5 mL = 50 mL". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Every route counts. Flushes and medicines can be a large share of a small child’s daily intake.
*Alt text:* A 24-hour fluid chart around a child: feeds, drinks, intravenous fluids, flushes and medicines on the intake side; urine, stool, drains and dialysis removal on the output side, with a balance at the center.

**Figure B: Arithmetic with units**  ·  skill `simple-figure`  ·  placed in section `arithmetic-with-units`  ·  key `pdn04_b`

```
FILE NAME: images/pediatric-dialysis-nurse-04-arithmetic-with-units.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Worked example card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Arithmetic with units". A clean card with three lines: "300 mL ÷ 3 h = 100 mL/h", "100 mL/h ÷ 20 kg = 5 mL/kg/h", and a crossed-out worksheet stub in red: "300 mL/h ✗". A green footer: "Units at every step. A second person calculates without seeing your answer." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Arithmetic with units. Write the units at every step, then have a second person check without seeing your answer.
*Alt text:* A worked example card: 300 mL over 3 hours equals 100 mL per hour; divided by 20 kilograms equals 5 mL/kg per hour; a red cross over a worksheet that says 300 mL per hour.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-04-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a pediatric digital scale with a small blood pressure cuff resting on it. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-04-assessment-fluid-and-calculations-og.png (prep script exports images/og/pediatric-dialysis-nurse-04-assessment-fluid-and-calculations-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Assessment, Fluid Balance and Weight-Based Arithmetic". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 4 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a pediatric digital scale with a small blood pressure cuff resting on it, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 5: Infection Prevention and Access Protection

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-05-infection-prevention-and-access-protection-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: close-up of hands, slightly angled
HUMAN VARIATION: Hands only; skin tone and hand position differ from the previous image
AUDIENCE: Nurses
VISUAL GOAL: Hands and hubs are the main gates; keep them clean.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: close-up of hands, slightly angled. Subject: hands only: a nurse’s gloved hands scrubbing a catheter hub with an antiseptic pad above a clean sterile field on a small tray, a child’s sleeve and a stuffed toy just visible at the frame edge, blurred, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: How organisms reach the child**  ·  skill `infographic-skill`  ·  placed in section `chain-of-transmission`  ·  key `pdn05_a`

```
FILE NAME: images/pediatric-dialysis-nurse-05-how-organisms-reach-the-child.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Annotated illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "How organisms reach the child". A semi-photoreal clothed school-age child with a PD catheter (abdomen, dressing only) and a dressing on the right upper chest. Five labeled arrows toward the child: "Hands", "Catheter hubs", "Exit site", "Diapers", "Gastrostomy". Beside each arrow a green shield with the protection: "Hand hygiene", "Scrub the hub", "Clean, dry dressing", "Exit away from the diaper", "Plan with the team". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* How organisms reach the child. Hands and hubs are the main gates; diapers and gastrostomies add routes unique to children.
*Alt text:* A child with a PD catheter and a central line, with arrows showing hands, catheter hubs, the exit site, diapers and a gastrostomy as routes for organisms, each with a protective action beside it.

**Figure B: Bundles that lowered infection**  ·  skill `simple-figure`  ·  placed in section `bundles-that-work`  ·  key `pdn05_b`

```
FILE NAME: images/pediatric-dialysis-nurse-05-bundles-that-lowered-infection.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Before-and-after bar chart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Bundles that lowered infection". Two pairs of bars. Pair 1 labeled "Hemodialysis catheter infections per 100 patient-months": amber bar "Before 3.3", green bar "After 48 months 0.8". Pair 2 labeled "PD peritonitis per patient-year": amber "Before 0.63", green "After 36 months 0.42". Footnote: "SCOPE collaborative; before-and-after comparisons". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Bundles that lowered infection. Standardized care in the SCOPE collaborative was followed by fewer infections (pre–post comparisons, not randomized).
*Alt text:* Two simple before-and-after bar pairs from the SCOPE collaborative: hemodialysis catheter bloodstream infections 3.3 to 0.8 per 100 patient-months, and PD peritonitis 0.63 to 0.42 episodes per patient-year.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-05-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: an antiseptic pad packet and a capped catheter hub on a sterile blue drape. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-05-infection-prevention-and-access-protection-og.png (prep script exports images/og/pediatric-dialysis-nurse-05-infection-prevention-and-access-protection-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Infection Prevention and Access Protection". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 5 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: an antiseptic pad packet and a capped catheter hub on a sterile blue drape, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 6: Medication Safety in Children on Dialysis

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-06-medication-safety-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C Still-Life
CAMERA: 45-degree tabletop
HUMAN VARIATION: No people
AUDIENCE: Nurses
VISUAL GOAL: Every pediatric dose is a calculation; check it twice.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Still-Life. Camera: 45-degree tabletop. Subject: two oral syringes of different sizes, a small amber medicine bottle without a readable label, a pill organizer and a pediatric dosing cup on a light counter, with soft daylight, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The ten-fold error**  ·  skill `simple-figure`  ·  placed in section `ten-fold-errors`  ·  key `pdn06_a`

```
FILE NAME: images/pediatric-dialysis-nurse-06-the-ten-fold-error.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Single-idea illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The ten-fold error". Two oral syringes side by side: left filled to a small mark labeled "0.5 mL" (green check), right filled to a large mark labeled "5 mL" (red cross). Above, a large order card reading ".5 mL" with the missing leading zero circled in red. Footer: "Leading zero always. Trailing zero never." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The ten-fold error. Weight-based doses create decimals, and decimals create ten-fold errors.
*Alt text:* A syringe and an order card showing 0.5 mL and 5 mL side by side, with the misplaced decimal point highlighted and a note that a ten-fold error in an adult dose can be the entire dose for a child.

**Figure B: The independent double check**  ·  skill `algorithm-generator-skill`  ·  placed in section `the-checked-dose`  ·  key `pdn06_b`

```
FILE NAME: images/pediatric-dialysis-nurse-06-the-independent-double-check.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Four-step flow
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The independent double check". Four rounded steps left to right: "1 Nurse A calculates", "2 Nurse B calculates separately", "3 Compare with the order and today’s weight", "4 Match → give". From step 3, a red branch: "Mismatch → stop, ask the prescriber or pharmacist". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The independent double check. Two people calculating separately catch what one person checking another’s work misses.
*Alt text:* A flow of four steps: first nurse calculates, second nurse calculates without seeing the first answer, both compare to the order and the weight, any mismatch stops the dose and goes to the prescriber or pharmacist.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-06-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: two oral syringes of different sizes beside a small amber bottle with no label. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-06-medication-safety-og.png (prep script exports images/og/pediatric-dialysis-nurse-06-medication-safety-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Medication Safety in Children on Dialysis". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 6 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: two oral syringes of different sizes beside a small amber bottle with no label, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 7: PD in Children: Physiology, Readiness and the Prescription

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-07-pd-physiology-and-prescription-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide, eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: PD in children lets therapy happen at home while they sleep.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide, eye level. Subject: a Filipino father in his 30s with a crew cut and a gray polo sitting on a bed beside his five-year-old son, who is asleep under a light blanket next to a home PD cycler on a clean bedside table, warm lamp light in a tidy modest bedroom, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Fill volume is scaled to body surface area**  ·  skill `infographic-skill`  ·  placed in section `fill-volume-and-pressure`  ·  key `pdn07_a`

```
FILE NAME: images/pediatric-dialysis-nurse-07-fill-volume-scaled-to-body-surface-area.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Annotated scale illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Fill volume is scaled to body surface area". Left: a child silhouette with a label "Body surface area (m²) = √(height × weight ÷ 3,600)". Right: a vertical scale in mL/m² with an amber band at "about 800 mL/m² — often the upper limit under age 2" and a teal band rising to "about 1,400 mL/m² — recruitment plateau from age 2". A note: "Tolerance decides". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Fill volume is scaled to body surface area. Under age 2 tolerance limits the volume; from age 2 the membrane recruits up to about 1,400 mL/m².
*Alt text:* A child silhouette with a body surface area label and a scale bar for fill volume in mL per square meter: about 800 mL/m² often used as an upper limit under age 2, and recruitment rising toward about 1,400 mL/m² from age 2, with a note that tolerance decides.

**Figure B: Reading a pediatric PD order**  ·  skill `simple-figure`  ·  placed in section `reading-the-order`  ·  key `pdn07_b`

```
FILE NAME: images/pediatric-dialysis-nurse-07-reading-a-pediatric-pd-order.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Annotated order card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Reading a pediatric PD order". A mock PD order card with blurred handwriting and five highlighted fields, each with a check box and a label: "Weight, height, BSA", "Fill volume in mL and mL/m²", "Dextrose strength", "Dwell time and cycles", "Last fill". Footer: "Check every field against today’s size." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Reading a pediatric PD order. Check each element against the child’s current weight and body surface area.
*Alt text:* A mock pediatric PD order with five highlighted fields: weight and body surface area, fill volume in mL and mL/m², dextrose strength, dwell time and number of cycles, and the last fill, each with a check mark.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-07-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a small PD solution bag beside a child’s night-light on a bedside table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-07-pd-physiology-and-prescription-og.png (prep script exports images/og/pediatric-dialysis-nurse-07-pd-physiology-and-prescription-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "PD in Children: Physiology, Readiness and the Prescription". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 7 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a small PD solution bag beside a child’s night-light on a bedside table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 8: The PD Catheter, Exit Site and Mechanical Problems

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-08-pd-catheter-and-exit-site-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: close, slightly from above
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Protect the exit site and you protect the catheter.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: close, slightly from above. Subject: a nurse with dark brown skin tone and short natural hair, in white scrubs, gently checking a PD catheter exit site on the lower abdomen of a calm six-year-old boy lying on an exam couch in a T-shirt pulled up just enough, his mother holding a toy car nearby; the dressing area is clean and the image is respectful and modest, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Catheter design and exit site**  ·  skill `infographic-skill`  ·  placed in section `catheter-design`  ·  key `pdn08_a`

```
FILE NAME: images/pediatric-dialysis-nurse-08-catheter-design-and-exit-site.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Cross-section illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Catheter design and exit site". A schematic cross-section of a child’s abdominal wall showing a PD catheter with two cream-colored cuffs (labeled "Deep cuff" and "Superficial cuff") inside the tunnel and the exit site pointing downward. Small icons mark "Diaper line" and "Gastrostomy" with arrows showing the exit placed away from both. Footer chip: "Double cuff, downward or lateral exit (ISPD 2024, 2D)". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Catheter design and exit site. The 2024 pediatric guideline suggests a double-cuff catheter with a downward or lateral exit.
*Alt text:* A cross-section of a child’s abdominal wall with a double-cuff PD catheter, the exit site pointing downward or sideways, placed away from the diaper line and a gastrostomy.

**Figure B: When it will not drain**  ·  skill `algorithm-generator-skill`  ·  placed in section `when-it-will-not-drain`  ·  key `pdn08_b`

```
FILE NAME: images/pediatric-dialysis-nurse-08-when-it-will-not-drain.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Decision path
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "When it will not drain". A vertical path of five rounded steps: "Clamps and kinks", "Bag below the abdomen", "Change position", "Bowels and bladder", "Fibrin strands", ending in "Still slow? Call the PD team". A red stop box on the side: "Pain, fever or cloudy fluid → call now". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* When it will not drain. Work from simple external causes inward, and stop if the child has pain, fever or cloudy fluid.
*Alt text:* A decision path for poor drainage: check clamps and kinks, position, constipation and bladder, fibrin, then call; a red stop box for pain, fever or cloudy fluid.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-08-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a coiled PD catheter with two cuffs on a white tray. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-08-pd-catheter-and-exit-site-og.png (prep script exports images/og/pediatric-dialysis-nurse-08-pd-catheter-and-exit-site-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "The PD Catheter, Exit Site and Mechanical Problems". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 8 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a coiled PD catheter with two cuffs on a white tray, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 9: CAPD: A Supervised Exchange in a Small Body

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-09-capd-supervised-exchange-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F Human Connection
CAMERA: medium, eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Connection and disconnection deserve full attention.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Human Connection. Camera: medium, eye level. Subject: a Filipina grandmother in her 60s with gray hair in a bun and reading glasses, wearing a mask, carefully connecting a PD bag on a clean table while a nurse in a teal scrub top watches with a checklist; a four-year-old grandson sits on a parent’s lap nearby watching a tablet (screen blurred), soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The exchange in a small body**  ·  skill `simple-figure`  ·  placed in section `the-exchange`  ·  key `pdn09_a`

```
FILE NAME: images/pediatric-dialysis-nurse-09-the-exchange-in-a-small-body.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Step sequence
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The exchange in a small body". Six numbered tiles with small semi-photoreal scenes: "1 Prepare room and child", "2 Mask and hand hygiene", "3 Check bag and order", "4 Drain", "5 Flush before fill", "6 Fill the ordered volume". Tiles 1 and 6 outlined in teal; a small amber label on tile 6: "Small volume — measure carefully". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The exchange in a small body. The steps match adult CAPD; the volumes and the child’s cooperation do not.
*Alt text:* Six numbered steps of a manual exchange for a child: prepare the room and the child, hand hygiene and mask, check the bag and order, drain, flush, fill, with the small fill volume highlighted.

**Figure B: Dry versus wet contamination**  ·  skill `simple-figure`  ·  placed in section `contamination`  ·  key `pdn09_b`

```
FILE NAME: images/pediatric-dialysis-nurse-09-dry-versus-wet-contamination.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Comparison panels
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Dry versus wet contamination". Two panels. Left "Dry": a clamped transfer set, a touched connector, no fluid flowing; steps "Clamp, cover, replace, report". Right "Wet": an open transfer set with fluid flowing; steps "Clamp now, cover, call the PD team" and an amber chip "Prophylaxis decision by the team". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Dry versus wet contamination. A wet contamination needs the team’s prophylaxis decision; the 2024 guideline suggests antibiotics after it.
*Alt text:* Two panels: a dry contamination with the system clamped and nothing infused, and a wet contamination where fluid ran after a break, with arrows to the different next steps.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-09-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a PD drainage bag and a mask on a clean table with a small stuffed animal. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-09-capd-supervised-exchange-og.png (prep script exports images/og/pediatric-dialysis-nurse-09-capd-supervised-exchange-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "CAPD: A Supervised Exchange in a Small Body". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 9 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a PD drainage bag and a mask on a clean table with a small stuffed animal, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 10: APD: Cycler Setup, Alarms and Home Monitoring

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-10-apd-cycler-and-home-monitoring-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C Still-Life
CAMERA: low angle, soft night light
HUMAN VARIATION: No people
AUDIENCE: Mixed
VISUAL GOAL: The cycler follows the order exactly; check the order first.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Still-Life. Camera: low angle, soft night light. Subject: a home PD cycler on a bedside table at night with neatly arranged tubing, a small night-light, a folded child’s blanket with a simple star pattern and a closed notebook, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Cycling small volumes**  ·  skill `simple-figure`  ·  placed in section `small-volume-cycling`  ·  key `pdn10_a`

```
FILE NAME: images/pediatric-dialysis-nurse-10-cycling-small-volumes.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Scene with chart
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Cycling small volumes". Left: a home cycler beside a child’s bed at night. Right: a simple line chart across the night with repeated small fill and drain steps labeled "Fill", "Dwell", "Drain"; one drain step dips short and is marked with an amber alarm icon labeled "Low drain". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Cycling small volumes. Small fills and short dwells make the cycler sensitive to position and drain problems.
*Alt text:* A cycler beside a child’s bed at night with a small fill volume, short dwells and a drain line, and a graph of fill and drain volumes across the night.

**Figure B: Alarms as clinical signals**  ·  skill `infographic-skill`  ·  placed in section `alarms-as-signals`  ·  key `pdn10_b`

```
FILE NAME: images/pediatric-dialysis-nurse-10-alarms-as-clinical-signals.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Three-row reference card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Alarms as clinical signals". Three rows, each with an alarm icon, "What it may mean" and "First response": "Low drain — position, constipation, catheter tip — check lines and position"; "Line occlusion — clamp closed or kinked line — check clamps and line path"; "Fill problem — bag clamp or empty bag — check bags". Red footer: "Pain, cloudy fluid or fever: stop and call". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Alarms as clinical signals. Every repeated alarm is information about the child, not only about the machine.
*Alt text:* Three common cycler alarm types (low drain, line occlusion, fill problem) each paired with what it may mean in the child and what the caregiver does first.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-10-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a home PD cycler with neat tubing on a child’s bedside table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-10-apd-cycler-and-home-monitoring-og.png (prep script exports images/og/pediatric-dialysis-nurse-10-apd-cycler-and-home-monitoring-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "APD: Cycler Setup, Alarms and Home Monitoring". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 10 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a home PD cycler with neat tubing on a child’s bedside table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 11: PD Peritonitis and Exit-Site Infection: The First Hour

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-11-pd-peritonitis-and-exit-site-infection-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder at a phone
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Nurses
VISUAL GOAL: A cloudy bag starts the clock; the first hour matters.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder at a phone. Subject: a Filipina PD nurse in her 30s with shoulder-length hair and a headset at a quiet hotline desk, holding a clear empty effluent bag up to the light while speaking on the phone, a small clock on the wall (no readable time), soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Two of four**  ·  skill `simple-figure`  ·  placed in section `recognizing-peritonitis`  ·  key `pdn11_a`

```
FILE NAME: images/pediatric-dialysis-nurse-11-diagnosing-peritonitis-two-of-four.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Four-tile criteria card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Two of four". Four tiles: "Effluent white cells above 100/mm³", "50% or more neutrophils", "Pain or fever", "Positive culture". A teal banner across: "Any two = empiric diagnosis". A small amber note: "Dry day? Instill and wait at least 2 hours before sampling". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Two of four. The 2024 pediatric guideline makes an empiric diagnosis when at least two are present (not graded).
*Alt text:* Four tiles: effluent white cells above 100 per mm³, at least 50% neutrophils, clinical signs such as pain or fever, and a positive culture; any two make an empiric diagnosis.

**Figure B: The first hour**  ·  skill `algorithm-generator-skill`  ·  placed in section `the-first-hour`  ·  key `pdn11_b`

```
FILE NAME: images/pediatric-dialysis-nurse-11-the-first-hour.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Timeline
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The first hour". A horizontal timeline from a cloudy bag icon: "0 min Sepsis screen", "Keep the bag", "Call the PD team (SBAR)", "Sample correctly", "Antibiotics as ordered, without delay". A red branch at the start: "Drowsy, fast breathing, cold hands → emergency now". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The first hour. Antibiotics start as soon as possible after the specimens are taken.
*Alt text:* A timeline for a cloudy bag at home: screen for sepsis, keep the bag, call the PD team, sample after an adequate dwell, start antibiotics as ordered as soon as specimens are taken.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-11-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a clear PD effluent bag held up to window light. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-11-pd-peritonitis-and-exit-site-infection-og.png (prep script exports images/og/pediatric-dialysis-nurse-11-pd-peritonitis-and-exit-site-infection-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "PD Peritonitis and Exit-Site Infection: The First Hour". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 11 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a clear PD effluent bag held up to window light, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 12: Pediatric Hemodialysis: Prescription Logic and Vascular Access

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-12-hd-prescription-and-vascular-access-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: three-quarter view
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Every vein a child keeps today is an access for tomorrow.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: three-quarter view. Subject: a thirteen-year-old Filipino boy in a school uniform shirt sitting in a dialysis chair reading a book, with a tunneled catheter dressing visible as a neat white square on the right upper chest under an open collar; a nurse in navy scrubs adjusts the machine behind him, blurred, soft natural daylight, gentle shallow depth of field. Show the tunneled catheter only as a neat white dressing on the patient’s right upper chest, below the clavicle, with a short capped dual limb (red and blue clamps) emerging below it; no tube in the neck. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Access for a lifetime**  ·  skill `infographic-skill`  ·  placed in section `access-for-a-lifetime`  ·  key `pdn12_a`

```
FILE NAME: images/pediatric-dialysis-nurse-12-access-for-a-lifetime.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Anatomy and timeline illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Access for a lifetime". Left: a schematic child’s upper body (glass-like translucent, no face) with a tunneled catheter on the right upper chest following the locked path, and the left forearm marked with a teal band labeled "Protected for a fistula — no needles". Right: a timeline "Age 8 → 18 → 40" with a vein icon at each point. Footer: "Every vein is a future access." ANATOMY LOCK — CATHETER PATH (follow exactly; overrides style): Anterior view, so the patient’s RIGHT side is on the IMAGE LEFT. The whole catheter is on the patient’s right (image left) and never crosses the midline. 1. EXIT SITE: right upper anterior chest wall, below the clavicle, a few finger-breadths lateral to the sternum, above the nipple line; below it a hub splits into two short external limbs hanging downward, RED clamp and cap (arterial) and BLUE clamp and cap (venous). 2. CUFF: a small textured cream-white Dacron cuff band INSIDE the subcutaneous tunnel just above the exit site, under the skin. 3. TUNNEL: from the cuff the catheter runs UPWARD beneath the skin of the anterior chest wall, passing OVER (in front of) the medial clavicle, never beneath it. 4. VENOTOMY AND LOOP: just above the clavicle it makes ONE smooth gentle U-shaped turn and enters the LOW right internal jugular vein, lateral to the common carotid artery. 5. INTRAVASCULAR COURSE: straight down the right internal jugular vein, right brachiocephalic vein, superior vena cava, RIGHT ATRIUM. 6. TIP: upper-to-mid right atrium. Child-sized proportions throughout. Never: mirrored anatomy, catheter under the clavicle or in the subclavian vein, crossing the midline, exit site in the neck or on the abdomen, external cuff, sharp kink or double loop, tip in the right ventricle or high superior vena cava, red/blue clamps swapped. Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.

CATHETER QA:
□ Chest-wall exit → cuff inside tunnel → tunnel over clavicle → one smooth loop into the low right internal jugular vein → superior vena cava → tip in right atrium □ Entirely on the image left; never crosses midline □ Red = arterial, blue = venous
```

*On-page caption:* Access for a lifetime. Every vein used today is one a child may need as an adult; protect them all.
*Alt text:* A child’s arm and neck veins with a central line, a fistula and protected veins marked, and a timeline showing that a child may need vascular access for decades.

**Figure B: The catheter care bundle**  ·  skill `simple-figure`  ·  placed in section `catheter-care`  ·  key `pdn12_b`

```
FILE NAME: images/pediatric-dialysis-nurse-12-catheter-care-bundle.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Checklist board
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The catheter care bundle". A clean checklist board with six icon rows and green check boxes: "Hand hygiene", "Mask", "Scrub the hub", "Exit-site care", "Clean dry dressing", "Aseptic connect and disconnect". Header chip: "Every step, every time". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The catheter care bundle. Every step, every time, observed and recorded.
*Alt text:* A checklist board for a tunneled hemodialysis catheter: hand hygiene, mask, scrub the hub, exit-site care, dressing, and connecting and disconnecting, each with an icon.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-12-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a dual-lumen tunneled catheter with red and blue clamps and a visible cuff on a sterile drape. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-12-hd-prescription-and-vascular-access-og.png (prep script exports images/og/pediatric-dialysis-nurse-12-hd-prescription-and-vascular-access-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Pediatric Hemodialysis: Prescription Logic and Vascular Access". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 12 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a dual-lumen tunneled catheter with red and blue clamps and a visible cuff on a sterile drape, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 13: The Small Circuit: Blood Volume, Priming, Water and Preparation

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-13-hd-circuit-water-and-preparation-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C Still-Life
CAMERA: 45-degree, studio-bright
HUMAN VARIATION: No people
AUDIENCE: Nurses
VISUAL GOAL: The circuit must be small compared with the child.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Still-Life. Camera: 45-degree, studio-bright. Subject: a small pediatric dialyzer and neatly coiled pediatric blood lines beside a larger adult dialyzer for comparison on a clean steel trolley, a sealed priming bag in the background, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: The 10% rule**  ·  skill `simple-figure`  ·  placed in section `blood-volume-and-the-circuit`  ·  key `pdn13_a`

```
FILE NAME: images/pediatric-dialysis-nurse-13-the-ten-percent-rule.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Proportion illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The 10% rule". A child silhouette with a vertical bar labeled "Estimated blood volume" and a horizontal teal line at "10%". Beside it, a small dialyzer and lines with their combined volume shaded. Two examples: "10 kg child: circuit 8.5% — below 10%" (green) and "3.5 kg newborn: circuit 23% — priming plan needed" (amber). Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The 10% rule. Total extracorporeal volume should stay below about 10% of the child’s blood volume.
*Alt text:* A child with an estimated blood volume bar and a hemodialysis circuit whose volume is shaded; when the circuit exceeds 10% of blood volume, a flag shows priming with albumin or blood may be needed.

**Figure B: The priming decision**  ·  skill `algorithm-generator-skill`  ·  placed in section `priming-decisions`  ·  key `pdn13_b`

```
FILE NAME: images/pediatric-dialysis-nurse-13-the-priming-decision.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Decision path
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The priming decision". Four steps: "Estimate blood volume", "Add lines + dialyzer volume", "Compare with 10%", then two branches: "Below 10% → saline prime per order" and "Above 10% → albumin or blood prime per written order". A purple chip: "The prescriber decides the prime". A small note: "Plan whether the circuit is returned at the end". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The priming decision. The nurse calculates and confirms; the prescriber decides the prime.
*Alt text:* A decision path: calculate blood volume, add lines and dialyzer volume, compare with 10%, then saline prime, or albumin or blood prime per the written order, with a note on returning blood at the end.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-13-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a small pediatric dialyzer with neatly coiled blood lines. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-13-hd-circuit-water-and-preparation-og.png (prep script exports images/og/pediatric-dialysis-nurse-13-hd-circuit-water-and-preparation-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "The Small Circuit: Blood Volume, Priming, Water and Preparation". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 13 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a small pediatric dialyzer with neatly coiled blood lines, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 14: The Hemodialysis Session: Initiation, Monitoring and Completion

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-14-hd-session-monitoring-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide, eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Watch the child, not only the numbers.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide, eye level. Subject: an eleven-year-old Filipina girl lying back in a dialysis chair with a light blanket, holding a handheld game, as a male nurse in his 40s with a goatee and blue scrubs checks her blood pressure with a child-sized cuff; her mother reads a magazine in a chair nearby, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: First sessions and disequilibrium**  ·  skill `simple-figure`  ·  placed in section `first-sessions-and-disequilibrium`  ·  key `pdn14_a`

```
FILE NAME: images/pediatric-dialysis-nurse-14-first-sessions-and-disequilibrium.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Single-scene illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "First sessions and disequilibrium". A child in a dialysis chair at a first session with a slowly turning blood pump icon labeled "Slow" and a short clock labeled "Short". Three amber warning chips around: "Headache", "Vomiting", "Restlessness or confusion". Footer: "Gentle start so urea falls slowly." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* First sessions and disequilibrium. Early sessions are short and gentle so urea falls slowly.
*Alt text:* A child in a dialysis chair at a first session, with a slow blood flow pump, a short clock and warning symbols for headache, vomiting and confusion.

**Figure B: Monitoring during the session**  ·  skill `simple-figure`  ·  placed in section `fluid-removal-in-children`  ·  key `pdn14_b`

```
FILE NAME: images/pediatric-dialysis-nurse-14-monitoring-during-the-session.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Monitoring timeline
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Monitoring during the session". A horizontal session timeline with check icons at intervals: "Behavior", "Heart rate trend", "Blood pressure", "Color and comfort", "Access and pressures", "Fluid removed". Near the end of the timeline an amber zone labeled "Near target weight: watch closely". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Monitoring during the session. Children often show distress late; watch trends, not only single values.
*Alt text:* A session timeline with checks every set interval: blood pressure, heart rate, symptoms, access and line pressures, fluid removed, and the child’s comfort and activity.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-14-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a child-sized blood pressure cuff draped over the arm of a dialysis chair. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-14-hd-session-monitoring-og.png (prep script exports images/og/pediatric-dialysis-nurse-14-hd-session-monitoring-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "The Hemodialysis Session: Initiation, Monitoring and Completion". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 14 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a child-sized blood pressure cuff draped over the arm of a dialysis chair, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 15: Emergencies and Pediatric Resuscitation Readiness

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-15-emergencies-and-resuscitation-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H Clinical
CAMERA: dynamic, slightly high
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Nurses
VISUAL GOAL: Know your role before the emergency.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: dynamic, slightly high. Subject: a small team of three Filipino nurses and a pediatrician gathered calmly around a dialysis chair with a pediatric emergency cart beside it, one nurse holding a clipboard, a teenage patient sitting up and being spoken to reassuringly; the scene is a drill, organized and calm, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Early warning in children**  ·  skill `infographic-skill`  ·  placed in section `recognize-early`  ·  key `pdn15_a`

```
FILE NAME: images/pediatric-dialysis-nurse-15-early-warning-in-children.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Annotated illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Early warning in children". A calm semi-photoreal school-age child in a dialysis chair with six small labeled icons around: "Quiet or irritable", "Heart rate rising", "Slow capillary refill", "Cool hands", "Fast breathing", "Yawning". A small gray chip at the bottom: "Low blood pressure comes late". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Early warning in children. Compensation hides shock until it fails; behavior and heart rate change first.
*Alt text:* A child on dialysis with early warning signs around them: change in behavior, color, breathing, heart rate, capillary refill, yawning or restlessness, each with a small icon.

**Figure B: Air in the venous line**  ·  skill `algorithm-generator-skill`  ·  placed in section `dialysis-emergencies`  ·  key `pdn15_b`

```
FILE NAME: images/pediatric-dialysis-nurse-15-air-in-the-venous-line.png
SKILL: williamriveromd-algorithm-generator-skill
IMAGE TYPE: Three-step emergency card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Air in the venous line". Three large rounded steps in red outline with icons: "1 Stop the pump", "2 Clamp the venous line", "3 Call and position as trained". Above, an air detector alarm icon on a venous line with small bubbles. Footer: "Then follow the unit emergency procedure." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Air in the venous line. Stop, clamp, call; then follow the unit’s emergency procedure.
*Alt text:* Three large steps: stop the pump, clamp the venous line, call for help and position the child as trained, with the air detector alarm shown.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-15-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a pediatric emergency cart with closed drawers and a small bag-valve mask on top. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-15-emergencies-and-resuscitation-og.png (prep script exports images/og/pediatric-dialysis-nurse-15-emergencies-and-resuscitation-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Emergencies and Pediatric Resuscitation Readiness". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 15 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a pediatric emergency cart with closed drawers and a small bag-valve mask on top, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 16: AKI, Acute PD and Continuous Kidney Replacement Therapy

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-16-aki-acute-pd-and-ckrt-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: wide, eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Acute PD can save a child where machines are scarce.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: wide, eye level. Subject: a provincial pediatric ward bed with a nine-year-old boy resting under a blanket, an acute PD setup with bags hanging on a stand, and a Filipina nurse in her 30s with a ponytail writing on a clipboard at the bedside; rain visible softly through a window, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Percent fluid overload**  ·  skill `simple-figure`  ·  placed in section `fluid-overload`  ·  key `pdn16_a`

```
FILE NAME: images/pediatric-dialysis-nurse-16-percent-fluid-overload.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Formula card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Percent fluid overload". A formula card: "%FO = (fluid in − fluid out) ÷ admission weight × 100". Worked example: "(3.8 L − 1.3 L) ÷ 25 kg × 100 = 10%". Below, three small bars labeled "Under 10%", "10–20%", "20% or more" with a gray note: "Registry: higher overload, higher mortality (association)". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Percent fluid overload. In the prospective pediatric CRRT registry, 20% or more was associated with higher mortality (observational).
*Alt text:* A formula card: fluid in minus fluid out, divided by admission weight, times 100, with a worked example and a small registry note that 20% or more was associated with higher mortality.

**Figure B: Acute PD where machines are scarce**  ·  skill `simple-figure`  ·  placed in section `acute-pd`  ·  key `pdn16_b`

```
FILE NAME: images/pediatric-dialysis-nurse-16-acute-pd-where-machines-are-scarce.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Scene illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Acute PD where machines are scarce". A bright provincial pediatric ward with a nine-year-old boy resting in bed, PD bags on a stand with a Y-shaped closed tubing set, and a nurse writing on an hourly fluid sheet. A teal chip: "PD suitable for pediatric AKI (ISPD 2020, 1C)". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Acute PD where machines are scarce. The 2020 ISPD pediatric guideline grades PD as suitable for AKI in children (1C).
*Alt text:* A provincial pediatric ward after a flood with a child on acute PD, a nurse at the bedside with an hourly fluid sheet, and a note that PD is suitable for pediatric AKI.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-16-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: PD bags on an IV stand beside a hospital bed window with rain. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-16-aki-acute-pd-and-ckrt-og.png (prep script exports images/og/pediatric-dialysis-nurse-16-aki-acute-pd-and-ckrt-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "AKI, Acute PD and Continuous Kidney Replacement Therapy". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 16 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: PD bags on an IV stand beside a hospital bed window with rain, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 17: Growth, Nutrition, Anemia and Bone

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-17-growth-nutrition-anemia-and-bone-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: side view, eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Growth is an outcome; measure it every time.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: side view, eye level. Subject: a seven-year-old Filipino boy standing straight against a wall stadiometer, shoes off, while a nurse with a short pixie cut in a green scrub top lowers the head piece gently; his mother watches smiling, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Growth is an outcome**  ·  skill `simple-figure`  ·  placed in section `growth-is-an-outcome`  ·  key `pdn17_a`

```
FILE NAME: images/pediatric-dialysis-nurse-17-growth-is-an-outcome.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Growth chart illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Growth is an outcome". A clean growth chart with percentile curves and a child’s plotted height line flattening below the "3rd percentile" curve, an amber callout "Height velocity below the 25th percentile". Beside it, a nurse measuring a child on a stadiometer. Footer: "Measure, plot, refer." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Growth is an outcome. Measure accurately, plot every time, and refer when the line falls away.
*Alt text:* A growth chart with a child’s height falling below the 3rd percentile and height velocity below the 25th, alongside a nurse measuring height with a stadiometer.

**Figure B: The feeding team**  ·  skill `infographic-skill`  ·  placed in section `feeding-the-child`  ·  key `pdn17_b`

```
FILE NAME: images/pediatric-dialysis-nurse-17-the-feeding-team.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Team circle infographic
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "The feeding team". A child at the center with four people around: "Renal dietitian — writes the plan" (purple), "Nurse — measures and reports" (teal), "Parents — feed and record", "Pediatric nephrologist — medical plan". Small icons at the edge: "Breast milk or formula", "Food", "Tube feeding", "Protein lost in PD fluid". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* The feeding team. The renal dietitian writes the plan; the nurse measures, reinforces and reports.
*Alt text:* A child at the center with the renal dietitian, nurse, parents and pediatric nephrologist, and icons for breast milk or formula, food, tube feeding and dialysate protein losses.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-17-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a wall stadiometer with a child’s small shoes placed neatly below it. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-17-growth-nutrition-anemia-and-bone-og.png (prep script exports images/og/pediatric-dialysis-nurse-17-growth-nutrition-anemia-and-bone-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Growth, Nutrition, Anemia and Bone". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 17 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a wall stadiometer with a child’s small shoes placed neatly below it, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 18: Teaching Caregivers, Home Support and Disaster Planning

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-18-caregiver-teaching-and-home-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F Human Connection
CAMERA: medium, eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Readiness is shown, not counted.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Human Connection. Camera: medium, eye level. Subject: a Filipina nurse in her 50s with silver-streaked hair and a white blouse sitting at a kitchen table in a modest home with a Filipina grandmother in her late 60s, practicing on a PD training model while a six-year-old girl draws at the end of the table; picture cards spread on the table, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-left side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Readiness by return demonstration**  ·  skill `simple-figure`  ·  placed in section `readiness-by-demonstration`  ·  key `pdn18_a`

```
FILE NAME: images/pediatric-dialysis-nurse-18-readiness-by-return-demonstration.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Scene illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Readiness by return demonstration". A Filipina grandmother performing a PD exchange on a training model while a nurse watches with a checklist; two speech bubbles: nurse "Tell me what you do if the bag is cloudy." and grandmother "Keep the bag and call the team." A green chip: "Shown, not counted". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Readiness by return demonstration. Caregivers are ready when they show it safely, not when the hours are done.
*Alt text:* A grandmother performing a PD exchange on a training model while a nurse observes with a checklist, with teach-back speech bubbles.

**Figure B: Typhoon and outage plan**  ·  skill `infographic-skill`  ·  placed in section `home-and-disaster-plans`  ·  key `pdn18_b`

```
FILE NAME: images/pediatric-dialysis-nurse-18-typhoon-and-outage-plan.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Home plan board
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Typhoon and outage plan". A home emergency plan board with five tiles and icons: "Supplies above flood level", "Charged phone and power bank", "PD unit hotline", "Manual exchange backup if trained and ordered", "Route to a hospital that treats children". A small rain-cloud icon in the corner. Footer: "Make the plan before the storm." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Typhoon and outage plan. Agree on the plan in good weather, and check it before every storm season.
*Alt text:* A home emergency plan board: supplies for several days, a charged phone, the PD unit hotline, a backup power plan, and the route to the nearest facility that can treat children.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-18-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a PD training model and picture cards on a kitchen table. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-18-caregiver-teaching-and-home-og.png (prep script exports images/og/pediatric-dialysis-nurse-18-caregiver-teaching-and-home-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Teaching Caregivers, Home Support and Disaster Planning". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 18 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a PD training model and picture cards on a kitchen table, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 19: Adolescence, School, Transplant and Transition

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-19-adolescence-school-transplant-transition-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: three-quarter, eye level
HUMAN VARIATION: Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Treat the adolescent as a partner; transition is a process.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: three-quarter, eye level. Subject: a sixteen-year-old Filipina with long straight hair and a denim jacket talking privately with a nurse in his late 20s in a quiet consultation room, both seated, the teen holding a phone face-down and a small notebook; a window with daylight behind, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Transition is a process**  ·  skill `simple-figure`  ·  placed in section `transition`  ·  key `pdn19_a`

```
FILE NAME: images/pediatric-dialysis-nurse-19-transition-is-a-process.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Stepped path
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Transition is a process". Four rising steps with an adolescent climbing: "Parent-led", "Shared", "Self-managed", "Adult clinic". Under each step two short skills: "Names condition and medicines"; "Books appointments, speaks alone"; "Decides with the team"; "First adult visit confirmed". Footer: "Skills, not birthdays." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Transition is a process. It starts years before the transfer and is judged by skills, not birthdays.
*Alt text:* A stepped path for an adolescent from parent-led care to shared care to self-managed care, ending at an adult kidney clinic, with skills listed at each step.

**Figure B: Preparing for transplant**  ·  skill `simple-figure`  ·  placed in section `transplant-preparation`  ·  key `pdn19_b`

```
FILE NAME: images/pediatric-dialysis-nurse-19-preparing-for-transplant.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Checklist illustration
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Preparing for transplant". An adolescent holding a clipboard with five checked items: "Vaccinations", "Growth and nutrition", "Veins protected", "School and mental health", "Family and donor evaluation". A small kidney icon at the end of a path. Footer: "Built on dialysis, months before the call." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Preparing for transplant. Most of the work happens on dialysis, months before the call.
*Alt text:* An adolescent with a checklist toward transplant: vaccinations, growth and nutrition, dialysis access preserved, school and mental health, family and donor evaluation.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-19-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a school backpack leaning against a dialysis chair. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-19-adolescence-school-transplant-transition-og.png (prep script exports images/og/pediatric-dialysis-nurse-19-adolescence-school-transplant-transition-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Adolescence, School, Transplant and Transition". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 19 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a school backpack leaning against a dialysis chair, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

### Module 20: Philippine Requirements, Records, Quality and Capstone

**Hero (circular vignette)**

```
FILE NAME: images/pediatric-dialysis-nurse-20-philippine-practice-quality-capstone-vignette-hero.png
SKILL: williamriveromd-hero-vignette v3
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: C Still-Life
CAMERA: top-down flat lay
HUMAN VARIATION: No people
AUDIENCE: Nurses
VISUAL GOAL: Know who governs what, count honestly, and improve one thing at a time.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: C Still-Life. Camera: top-down flat lay. Subject: a neat portfolio folder, a printed run chart with dots and a dashed line (no numbers), a pen, a small calendar and a stethoscope on a light desk, soft natural daylight, gentle shallow depth of field. Children appear calm, comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child.

QUALITY CHECK:
Square 2048×2048; circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the upper-right side; Filipino setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.
```

**Figure A: Who governs what**  ·  skill `infographic-skill`  ·  placed in section `who-governs-what`  ·  key `pdn20_a`

```
FILE NAME: images/pediatric-dialysis-nurse-20-who-governs-what.png
SKILL: williamriveromd-infographic-skill
IMAGE TYPE: Card array
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Who governs what". Five cards on a desk, each with a small calendar icon labeled "Date": "PRC — the nurse", "DOH — the facility", "PSN — professional guidelines", "PhilHealth — benefits", "Hospital — privileges and procedures". Footer: "Read every rule for its issuer, scope and date." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Who governs what. Read every rule for its issuer, its scope and its date.
*Alt text:* Five labeled cards: PRC (the nurse), DOH (the facility license), PSN (professional guidelines), PhilHealth (benefits) and the hospital (privileges and procedures), each with a small date stamp.

**Figure B: Infection-rate arithmetic**  ·  skill `simple-figure`  ·  placed in section `measuring-quality`  ·  key `pdn20_b`

```
FILE NAME: images/pediatric-dialysis-nurse-20-infection-rate-arithmetic.png
SKILL: williamriveromd-simple-figure
IMAGE TYPE: Worked example card
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)
AUDIENCE: Pediatric dialysis nurses and families

PROMPT:
Title at top in bold navy: "Infection-rate arithmetic". A card: "3 episodes ÷ (96 patient-months ÷ 12) = 3 ÷ 8 = 0.375 per patient-year". A small gauge beside it with a green zone "0.4 or fewer (ISPD 2024 pediatric benchmark)" and the needle just inside. Footer: "Count, divide by time at risk, investigate every episode." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber #b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous whitespace. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No drug names or doses. No visible blood spills, needles in a child’s skin, crying or frightened close-ups, or partially dressed children. American English on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; © renalcarematters.com visible bottom-right.
```

*On-page caption:* Infection-rate arithmetic. Count episodes, divide by time at risk in years, and compare with the benchmark of 0.4 or fewer.
*Alt text:* A worked example card: 3 peritonitis episodes over 96 patient-months at risk equals 8 patient-years, so 0.375 episodes per patient-year, beside the ISPD 2024 pediatric benchmark of 0.4 or fewer.

**Course tile**

```
FILE NAME: images/pediatric-dialysis-nurse-20-card.png (generate at 1536 × 1024; prep script exports 640 × 360 WebP)
SKILL: williamriveromd-infographic-skill v5 (tile)
IMAGE TYPE: Course tile (16:9, no text)
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: a portfolio folder and a printed run chart (dots and a dashed line, no numbers) on a desk. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, faces, children’s faces, text of any kind, dark backgrounds, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/pediatric-dialysis-nurse-20-philippine-practice-quality-capstone-og.png (prep script exports images/og/pediatric-dialysis-nurse-20-philippine-practice-quality-capstone-og.jpg 1200 × 630 JPEG ≤ 300 KB)
SKILL: williamriveromd-infographic-skill v5 (OG card)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Pediatric dialysis nurses and kidney care teams
VISUAL GOAL: A share preview that names the page and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: text block in Inter. Small chip at top in clinical teal #1a6b72 with white text "RENAL CARE ACADEMY · NEPHROLOGY NURSING TRACK". Title in bold navy #0f1e2e, three lines at most: "Philippine Requirements, Records, Quality and Capstone". Subtitle in teal #1a6b72: "Pediatric Dialysis Nurse · Module 20 of 20". A thin teal rule under the title. Right 45%: a clean photorealistic still-life on a light surface: a portfolio folder and a printed run chart (dots and a dashed line, no numbers) on a desk, softly lit, no faces. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; spelling exact; light background.
```

## 7. Audit checklist before publishing

- [ ] Every label spelled exactly as in the prompt (compare letter by letter; GPT often misspells).
- [ ] No number on an image that is not in its prompt; no drug names or doses anywhere.
- [ ] Children calm, clothed and dignified; no needles in skin; no crying close-ups; child-sized equipment.
- [ ] Tunneled catheter images follow the path lock (right upper chest exit, cuff inside, over the clavicle, right internal jugular, right atrium; red arterial, blue venous).
- [ ] Heroes: circle with white margin, title-safe zone empty, a different cast from the previous hero, no text.
- [ ] Figures and OG cards: light background, Inter, © renalcarematters.com bottom-right.
- [ ] OG cards: text only in the left 55%, nothing important outside the 1.91:1 band.
- [ ] Any image that fails: note why, and write a corrected prompt in a new MD file in the working folder.
