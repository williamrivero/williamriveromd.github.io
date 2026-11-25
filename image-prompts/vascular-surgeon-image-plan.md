# Vascular Surgeon track: image plan blueprint and GPT prompt book

Renal Care Academy → Renal Care Physicians Track → Vascular Surgeon. Prepared November 25, 2026. American English throughout.

## 1. Why these images

Every picture in this track has one job: make a decision easier to understand, apply, or remember. The plan follows the track’s teaching sequence (intuition → physiology → evidence → practice), so each module gets:

| Image | Purpose in learning | Where it appears | Count |
| --- | --- | --- | --- |
| **Circular vignette hero** | Sets the scene and the emotional stakes (appreciation): who is involved, where, and what is at risk | Top of each module page and the course home; source of the page’s share image if no OG card exists | 21 |
| **Teaching figure A** | Mechanism or anatomy (understanding): why the decision makes physiologic sense | After the first paragraph of the physiology/mechanism section | 20 |
| **Teaching figure B** | Decision tool, evidence picture or checklist (application): what to do, and how strong the evidence is | After the first paragraph of the evidence or practice section | 20 |
| **Course tile** | Recognition on the syllabus and Academy landing (navigation) | Module cards on the course home; the course card | 21 |
| **OG share card** | A share preview that names the module and its idea (reach) | `og:image` on Facebook, Viber, Messenger, X, LinkedIn | 21 |
| **Track share-card art** | Background art for the Academy’s composited track card | `images/academy/og-art/vascular-surgeon.webp`, text added by `build_academy_og.py` | 1 |
| **Landing tile** | The Vascular Surgeon card on `academy/index.html` | `images/academy/landing/vascular-surgeon.webp` | (made from the course tile) |

**Total: 104 prompts** (21 heroes, 40 teaching figures, 21 tiles, 21 OG cards, 1 track art).

## 2. Rules that apply to every image

- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c, purple #6c3d8e.
- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). No serif or decorative type. American English spelling on every label.
- **Attribution:** teaching figures and OG cards carry `renalcarematters.com` bottom-right (bottom-center for portrait). Heroes and tiles carry no text at all.
- **Safety for a surgical track:** no visible blood, open wounds, needles in skin, or operative step sequences. Anatomy is drawn as a schematic and the caption says so. No figure carries a dose, diameter, pressure or threshold that is not written in its prompt; every number in a prompt is already in the module and verified against its source.
- **People:** Filipino patients and clinicians, a different cast in every image (age, sex, face, hair, clothing, posture, camera).
- **Skills used:** `williamriveromd-hero-vignette` (heroes), `williamriveromd-simple-figure`, `williamriveromd-algorithm-generator-skill`, `williamriveromd-biomedical-mechanism-figure`, `williamriveromd-organ-crosstalk-sigil-graphic` and `williamriveromd-infographic-skill` (teaching figures, tiles, OG cards).

## 3. Production workflow

1. Generate each prompt below in ChatGPT Image Generator. Save the PNG with the exact FILE NAME stem shown into `images/incoming/vascular-surgeon/` in the repo.
2. Run `python3 tools/techcourses/vs/prep_images.py`. It converts and places every file: heroes to `images/<slug>-vignette-hero.png` + `.webp`; teaching figures to `images/<file>.webp` (+ `.png`); tiles to 640 × 360 WebP; the landing tile to 960 × 540; OG cards to 1200 × 630 JPEG ≤ 300 KB in `images/og/`; the track art to `images/academy/og-art/vascular-surgeon.webp`.
3. Rebuild: `python3 generate_tech_courses.py --course vs --patch`, then `python3 build_academy_og.py --art images/academy/og-art --only vascular-surgeon --patch`, `python3 generate_rg_thumbs.py`, `python3 patch_rg_card_thumbs.py`, `python3 patch_responsive_images.py`.
4. Check one module in light and dark mode, and paste one module URL into the Facebook Sharing Debugger.

Figures are already wired into the modules (`tools/techcourses/vs/figs.py` and `{{fig:…}}` macros), so a page shows each figure as soon as its file exists.

## 4. Image map by module

| Module | Hero idea | Figure A (understand) | Figure B (apply) |
| --- | --- | --- | --- |
| 1. The surgeon in the kidney care team | A referral is a phone call that must end with an owner. | Three authorities, one patient | Where does this access referral go? |
| 2. The lifetime access plan | Access planning is a family conversation about a whole life. | One plan, three answers | What the access-type data can and cannot say |
| 3. Examine and preserve the vessels | Examine both arms; compare before you cut. | How old lines close future outflow | Examine both arms in four steps |
| 4. Mapping and choosing an access | The map is drawn for construction and for needles. | What a vessel map shows, and what it cannot | Distal first: a trade, not a rule |
| 5. Make the patient ready for surgery | Readiness is checked on the day. | Why potassium stops an operation | Day-of-surgery readiness |
| 6. Plan and create an autogenous fistula | A fistula is a vein remodeled by flow. | Maturation is a race | A drug moved the surrogate, not the outcome |
| 7. Grafts and alternative configurations | A graft trades maturation for maintenance. | Why grafts narrow at the venous end | Fistula or graft: choosing with the patient |
| 8. Dialysis catheters and central veins | Catheters are bridges that wear the riverbanks. | Where a catheter goes, and what it can cost | Poor flow after insertion: when to stop |
| 9. Maturation and the first cannulation | Patent is not the same as usable. | Ultrasound and readiness: what the numbers showed | A thrill is not a usable fistula |
| 10. Recognize a failing access | Read the access against its own baseline. | Reading the access: where is the narrowing? | Fixing stenosis before it causes trouble |
| 11. Stenosis and endovascular choices | Choose the device that protects the next site. | Why stenoses come back, and how devices respond | Landing zone: protect the next site |
| 12. Thrombosis and urgent dialysis | Dialysis safety and salvage run in parallel. | A clotted access: two jobs at once | Clues to why the access clotted |
| 13. Hand ischemia and neurologic injury | A thrill reassures about the access, never the hand. | Hand ischemia is a pressure problem | Grade the threatened hand |
| 14. Aneurysm and life threatening bleeding | Two-finger pressure and a call for help. | Read the skin over an aneurysm | Stopping an access bleed at home |
| 15. Access infection and sepsis | Sepsis first, then source control. | Why foreign material keeps the infection | Source control by access type |
| 16. High flow and central venous obstruction | State the mechanism before the operation. | The access and the heart | Breathless with an access: find the mechanism |
| 17. The difficult access and changing modality | Reconstruct the history before the next attempt. | Reconstruct the history before the next attempt | When access is hard: the paths to discuss |
| 18. Kidney care beyond the access | Notice the problem the referral did not name. | Not the access? Route it | Investigate without harming the kidneys |
| 19. Philippine documentation and quality | Honest measures make improvement possible. | Three kinds of patency | A code is not a payment |
| 20. The integrated vascular access service | Every transition needs an owner. | Every handoff needs an owner | Capstone: how the plan is judged |

## 5. Track-level images

### Course home hero

```
FILE NAME: images/vascular-surgeon-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: environmental portrait, eye level
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: The surgeon’s work continues in the dialysis chair.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: environmental portrait, eye level. Subject: a Filipino vascular surgeon in his early 50s with a broad square face, salt-and-pepper close-cropped hair and rimless glasses, navy scrubs under an open white coat, gently supporting the forearm of a seated patient in a dialysis chair while a dialysis nurse looks on; a bright modern Philippine hemodialysis unit softly blurred behind, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

### Course tile and Academy landing tile

Make one master; the prep script writes both `images/vascular-surgeon-card.webp` (640 × 360) and `images/academy/landing/vascular-surgeon.webp` (960 × 540).

```
FILE NAME: images/vascular-surgeon-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a dialysis access surgeon’s hands in gloves resting beside a schematic arm model with a highlighted fistula, a stethoscope and a clipboard on a pale teal surface. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

### Course home OG card

```
FILE NAME: images/og/vascular-surgeon-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Vascular Surgeon". Subtitle in teal: "20 modules · referral to rescue". Right 45%: a clean photorealistic still-life on a light surface: a dialysis access surgeon’s hands in gloves resting beside a schematic arm model with a highlighted fistula, a stethoscope and a clipboard on a pale teal surface, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Track share-card art (Academy composited card)

```
FILE NAME: images/academy/og-art/vascular-surgeon.png (prep script writes .webp)
IMAGE TYPE: Background art for build_academy_og.py
PIXEL DIMENSIONS: 1536 × 1024

PROMPT:
16:9-like 3:2 landscape photorealistic editorial still-life on a light background: a dialysis access surgeon’s hands in gloves resting beside a schematic arm model with a highlighted fistula, a stethoscope and a clipboard on a pale teal surface. Keep the LEFT 45% as clean, light, empty negative space (the builder places the track title, group label and stats there). Soft daylight, gentle depth of field, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Absolutely NO text, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid text, faces, clutter, dark backgrounds, visible blood, needles in skin.

QUALITY CHECK:
Left 45% empty and light; subject on the right; no text.
```

## 6. Module prompts

### Module 1: The surgeon in the kidney care team

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-01-the-surgeon-in-the-kidney-care-team-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: H Clinical
CAMERA: over-the-shoulder, slightly high
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: A referral is a phone call that must end with an owner.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: over-the-shoulder, slightly high. Subject: a Filipina surgeon in her late 30s with a long oval face, hair in a low bun, pearl stud earrings and light-blue scrubs, on a corridor phone call while writing on a clipboard; through a glass window behind her a lit dialysis unit with two nurses is softly blurred, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Three authorities, one patient**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `roles`

```
FILE NAME: images/vascular-surgeon-01-who-owns-what.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Three authorities, one patient.

PROMPT:
Title at top: "Three authorities, one patient". A reference card with three stacked columns joined at the bottom by one patient icon. Column 1 header "Dialysis facility" (teal): "Licensed by the DOH", "Staff, records, referral arrangements". Column 2 header "Attending nephrologist" (navy): "Kidney plan and dialysis prescription", "Coordinates access with the surgeon (PSN 2024, §1.2 b3)". Column 3 header "Surgeon" (purple): "Privileges from the operating hospital", "Creation, revision, salvage, ligation". A green band across the bottom where the columns meet: "The overlap is the access. Name an owner for every decision." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Three authorities, one patient. The facility is licensed by the Department of Health (DOH), the attending nephrologist owns the dialysis prescription and coordinates access under the Philippine Society of Nephrology (PSN) 2024 guidelines, and the surgeon’s authority comes from hospital privileges. Responsibility blurs where they overlap: the access.
*Alt text:* Card comparing the dialysis facility, the attending nephrologist and the surgeon: who authorizes each and what each decides.

**Figure B: Where does this access referral go?**  ·  skill `williamriveromd-algorithm-generator-skill`  ·  placed in section `triage`

```
FILE NAME: images/vascular-surgeon-01-referral-triage-tree.png
IMAGE TYPE: A Clinical algorithm
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Where an access referral goes.

PROMPT:
Title at top: "Where does this access referral go?". A top-to-bottom algorithm. Start node (navy): "Access referral received". Decision 1 (teal): "Threat now? Bleeding, cold or weak hand, fever or low blood pressure, breathlessness" → YES → red node "Emergency pathway today: named receiving clinician and hospital". NO → Decision 2 (teal): "Last session missed or failed?" → YES → amber node "Attending nephrologist decides on dialysis now, in parallel with the access plan". NO → green node "Dated clinic or imaging slot, with instructions if it worsens". All three end nodes flow into one final navy node: "Close the loop: owner, time, read-back, fallback, record". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Where an access referral goes. Threats go to the emergency pathway the same day; a missed session goes to the attending nephrologist in parallel; everything else gets a dated slot. Every branch ends with a closed loop.
*Alt text:* Decision tree that sends an access referral to the emergency pathway, to a parallel dialysis decision, or to a dated clinic slot.

**Course tile**

```
FILE NAME: images/vascular-surgeon-01-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: a desk phone, a referral slip with no readable text and a clipboard arranged around a small toy relay baton on a pale teal surface. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-01-the-surgeon-in-the-kidney-care-team-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "The surgeon in the kidney care team". Subtitle in teal: "Vascular Surgeon · Module 1 of 20". Right 45%: a clean photorealistic still-life on a light surface: a desk phone, a referral slip with no readable text and a clipboard arranged around a small toy relay baton on a pale teal surface, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 2: The lifetime access plan

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-02-the-lifetime-access-plan-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: E Lifestyle
CAMERA: wide-angle, table level
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Access planning is a family conversation about a whole life.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: E Lifestyle. Camera: wide-angle, table level. Subject: an 80-year-old Filipina grandmother with short white permed hair and a floral duster, her cane hooked on the chair, and her daughter in her 40s with a ponytail and office blouse, seated across a small clinic table from a male nephrologist; a simple hand-drawn arm sketch on paper lies between them, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: One plan, three answers**  ·  skill `williamriveromd-infographic-skill`  ·  placed in section `lifeplan`

```
FILE NAME: images/vascular-surgeon-02-present-contingency-successor.png
IMAGE TYPE: Journey (horizontal pathway)
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: The Life-Plan in one picture.

PROMPT:
Title at top: "One plan, three answers". A horizontal journey along a gently curving path drawn over a faint schematic left-arm silhouette (labeled "schematic"). Three milestones as large rounded cards: 1 green "Present access: what works now", 2 amber "Contingency: what if it fails", 3 teal "Successor: what comes after, and what to protect". Beside the path, two small side branches leaving the arm: "Peritoneal dialysis" and "Transplant" with simple icons. A small shield icon over the right arm labeled "Protect for later". Footer strip: "KDOQI 2019 ESKD Life-Plan: write the second and third plans before you need them." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* The Life-Plan in one picture. The Kidney Disease Outcomes Quality Initiative (KDOQI) end-stage kidney disease (ESKD) Life-Plan asks three questions in advance: what works now, what happens if it fails, and what comes after.
*Alt text:* Pathway showing a present access, a contingency and a successor, with peritoneal dialysis and transplant as side branches.

**Figure B: What the access-type data can and cannot say**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `evidence`

```
FILE NAME: images/vascular-surgeon-02-association-not-causation.png
IMAGE TYPE: B Side-by-side comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Association, not proof.

PROMPT:
Title at top: "What the access-type data can and cannot say". Two equal panels. Left panel, green header "What 62 cohorts found": three horizontal bars comparing catheter users with fistula users, labeled exactly "Death: risk ratio 1.53", "Fatal infection: risk ratio 2.12", "Cardiovascular events: risk ratio 1.38". Under it a small note "586,337 people, observational". Right panel, amber header "Why it is not the whole story": three icon rows: "Sicker patients more often get catheters", "Unplanned starts begin with catheters", "Exhausted sites leave only catheters". Footer: "Prefer a working fistula. Never promise that a fistula will work, or that it will prolong life." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Association, not proof. In a systematic review of 62 cohorts (586,337 people), catheter users had higher risks of death, fatal infection and cardiovascular events than fistula users, but sicker patients and unplanned starts explain part of the gap.
*Alt text:* Two panels: the higher risks seen with catheters in cohort studies, and the confounders that explain part of that difference.

**Course tile**

```
FILE NAME: images/vascular-surgeon-02-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: three small path markers (green, amber, teal) placed along a curving ribbon on a white surface, with a tiny kidney model at the end. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-02-the-lifetime-access-plan-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "The lifetime access plan". Subtitle in teal: "Vascular Surgeon · Module 2 of 20". Right 45%: a clean photorealistic still-life on a light surface: three small path markers (green, amber, teal) placed along a curving ribbon on a white surface, with a tiny kidney model at the end, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 3: Examine and preserve the vessels

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-03-examine-and-preserve-the-vessels-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: close-up, hands-only, side light
HUMAN VARIATION: Hands only; skin tone, age and hand position differ from the previous image
AUDIENCE: Clinicians
VISUAL GOAL: Examine both arms; compare before you cut.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: close-up, hands-only, side light. Subject: the two bare forearms of a Filipino man in his late 50s resting palms-up on a white examination pillow, one slightly fuller than the other, with a surgeon’s gloved fingers lightly palpating the wrist; a pocket Doppler probe and a soft tape measure lie beside, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: How old lines close future outflow**  ·  skill `williamriveromd-biomedical-mechanism-figure`  ·  placed in section `history`

```
FILE NAME: images/vascular-surgeon-03-catheter-to-central-stenosis.png
IMAGE TYPE: Organ → inset → injury/benefit
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: How old lines close future outflow.

PROMPT:
Title at top: "How old lines close future outflow". Left panel: simplified upper torso (schematic) with the right internal jugular, subclavian and brachiocephalic veins and the superior vena cava in soft blue; a dialysis catheter and a pacemaker lead drawn in gray; a dashed connector to the inset. Center inset (dashed box): magnified vein wall where the catheter rubs, labels "Endothelial injury", "Platelets and fibrin", "Smooth muscle growth", "Narrowed lumen". Right small panel: an arm with a new fistula and swelling, label "Arterial flow meets a blocked outflow". Bottom row: pink box "Catheters, device leads, PICCs injure veins" → blue box "Ask about every line and device; image the central veins when at risk" → blue box "The fistula is placed where it can drain". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* How old lines close future outflow. Wall contact by catheters and device leads injures the endothelium; healing narrows the vein, and a fistula on that side later swells the arm. Schematic, not to scale.
*Alt text:* Schematic of a catheter and pacemaker lead injuring a central vein, narrowing it, and later causing arm swelling after a fistula.

**Figure B: Examine both arms in four steps**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `exam`

```
FILE NAME: images/vascular-surgeon-03-four-part-arm-exam.png
IMAGE TYPE: C Horizontal step sequence
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Examine both arms in four steps.

PROMPT:
Title at top: "Examine both arms in four steps". Four rounded cards in a row joined by arrows, each with a simple line icon of an arm. Card 1 teal "Inflow": "Pulses", "Pressure in both arms", "Palmar arch". Card 2 green "Superficial veins": "Light tourniquet", "Continuity and depth", "Straight segment". Card 3 amber "Outflow warning signs": "Edema", "Chest-wall collaterals", "Device on that side". Card 4 purple "Hand baseline": "Color and refill", "Sensation", "Grip and pinch". Footer strip: "Record the hand before you touch it." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Examine both arms in four steps. The baseline hand examination is what lets you recognize a new deficit after surgery.
*Alt text:* Four-step arm examination: inflow, superficial veins, outflow warning signs and a recorded hand baseline.

**Course tile**

```
FILE NAME: images/vascular-surgeon-03-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: two plaster forearm models side by side on a white cloth, a pocket Doppler probe and a soft tape measure between them. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-03-examine-and-preserve-the-vessels-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Examine and preserve the vessels". Subtitle in teal: "Vascular Surgeon · Module 3 of 20". Right 45%: a clean photorealistic still-life on a light surface: two plaster forearm models side by side on a white cloth, a pocket Doppler probe and a soft tape measure between them, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 4: Mapping and choosing an access

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-04-mapping-and-choosing-an-access-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: side profile, medium distance
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: The map is drawn for construction and for needles.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: side profile, medium distance. Subject: a Filipino sonographer in his late 20s with a buzz cut and slim build scanning the inner upper arm of a seated woman in her late 40s with shoulder-length wavy hair, the ultrasound screen glowing with a vein image, while a surgeon marks the skin with a skin marker, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: What a vessel map shows, and what it cannot**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `reading`

```
FILE NAME: images/vascular-surgeon-04-what-the-map-shows.png
IMAGE TYPE: D Single mechanism poster
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: What a vessel map shows, and what it cannot.

PROMPT:
Title at top: "What a vessel map shows, and what it cannot". A central schematic left arm (labeled "schematic") with radial and brachial arteries in red and cephalic vein in blue. Callout cards with green ticks: "Arterial diameter and calcification", "Vein continuity, depth, branches", "Straight segment for two needles". Callout cards with amber question marks: "How the artery will dilate", "Wall quality and remodeling", "Skill of the cannulator". A faded zone behind the clavicle marked with a red outline and the label "Central veins: not seen on arm duplex". Bottom strip: "Never declare an access usable from diameter alone." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* What a vessel map shows, and what it cannot. Diameter stands in for how a vessel will respond to flow; read it with depth, length and central outflow in mind.
*Alt text:* Annotated arm schematic: what duplex mapping shows, what it cannot predict, and the central veins it cannot see.

**Figure B: Distal first: a trade, not a rule**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `evidence`

```
FILE NAME: images/vascular-surgeon-04-distal-first-tradeoff.png
IMAGE TYPE: B Side-by-side comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Distal first is a trade.

PROMPT:
Title at top: "Distal first: a trade, not a rule". Two panels with a balance-scale icon between them. Left panel teal "Distal (forearm) first": "Keeps upper-arm sites for later", "Fails primarily more often", "Needs time to mature". Right panel purple "Proximal (upper arm) now": "More likely to mature", "Uses a site the future may need", "More hand ischemia with brachial inflow". Footer: "UKKA 2025, statement 3.2 (1B): favor distal sites when anatomy and preference allow. Time to dialysis tips the balance." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Distal first is a trade. The UK Kidney Association (UKKA) 2025 guideline favors distal sites first (grade 1B); with little time before dialysis, the balance shifts upward.
*Alt text:* Balance comparing a distal-first fistula with an upper-arm fistula: what each preserves and what each risks.

**Course tile**

```
FILE NAME: images/vascular-surgeon-04-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: a compact ultrasound probe on a folded towel beside a printed vein-map silhouette with no readable text and a skin marker. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-04-mapping-and-choosing-an-access-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Mapping and choosing an access". Subtitle in teal: "Vascular Surgeon · Module 4 of 20". Right 45%: a clean photorealistic still-life on a light surface: a compact ultrasound probe on a folded towel beside a printed vein-map silhouette with no readable text and a skin marker, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 5: Make the patient ready for surgery

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-05-make-the-patient-ready-for-surgery-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: H Clinical
CAMERA: environmental portrait, low angle
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Readiness is checked on the day.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: environmental portrait, low angle. Subject: a pre-operative bay where a Filipina anesthesiologist in her mid 40s with a short bob and teal cap, a young male surgeon with curly hair and a nurse review a printed lab sheet beside a man in his 60s lying on a trolley with a nasal oxygen cannula, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Why potassium stops an operation**  ·  skill `williamriveromd-biomedical-mechanism-figure`  ·  placed in section `threats`

```
FILE NAME: images/vascular-surgeon-05-potassium-and-the-heart.png
IMAGE TYPE: Organ → inset → injury/benefit
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Why potassium stops an operation.

PROMPT:
Title at top: "Why potassium stops an operation". Left panel: a heart with an electrocardiogram strip showing tall peaked T waves. Inset (dashed box): one cardiac cell membrane with potassium ions outside rising, labels "Higher outside potassium", "Membrane partly depolarized", "Slower conduction". Inflow arrows into the potassium pool from four labeled sources: "No kidney excretion", "Acidosis shifts potassium out of cells", "Tissue injury releases it", "Some anesthetic drugs raise it". Bottom row: pink "Missed dialysis, high potassium, peaked T waves" → blue "Treat with the nephrologist and anesthesiologist; postpone elective surgery" → blue "Operate when the threat is fixed". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Why potassium stops an operation. Rising outside potassium partly depolarizes heart cells and slows conduction; peaked T waves are the warning. An elective access benefit never outweighs this threat.
*Alt text:* Mechanism of hyperkalemia: four sources of potassium, a depolarized heart cell, peaked T waves, and the decision to postpone.

**Figure B: Day-of-surgery readiness**  ·  skill `williamriveromd-algorithm-generator-skill`  ·  placed in section `anesthesia`

```
FILE NAME: images/vascular-surgeon-05-day-of-surgery-readiness.png
IMAGE TYPE: A Clinical algorithm
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Readiness is checked on the day.

PROMPT:
Title at top: "Day-of-surgery readiness". Top-to-bottom checklist algorithm with four teal decision diamonds in sequence: "Potassium and ECG acceptable?", "Can lie flat, no new breathlessness?", "No fever or bacteremia?", "Anticoagulant plan agreed?". Every YES continues down; every NO branches right to an amber node "Postpone. Name the owner of the fix" with small owner tags: "Nephrologist", "Nephrologist", "Treating team", "Prescriber with anesthesia". Final green node: "Proceed; huddle confirms anesthesia plan". Bottom note: "Readiness is checked on the day, not at the clinic visit." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Readiness is checked on the day. Each reason to postpone has a named owner, so the access plan survives the delay.
*Alt text:* Four-question readiness algorithm on the day of access surgery, with an owner for each reason to postpone.

**Course tile**

```
FILE NAME: images/vascular-surgeon-05-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a pre-operative checklist board with four empty check boxes, an ECG strip with tall T waves and an anesthesia mask on a light tray. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-05-make-the-patient-ready-for-surgery-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Make the patient ready for surgery". Subtitle in teal: "Vascular Surgeon · Module 5 of 20". Right 45%: a clean photorealistic still-life on a light surface: a pre-operative checklist board with four empty check boxes, an ECG strip with tall T waves and an anesthesia mask on a light tray, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 6: Plan and create an autogenous fistula

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-06-plan-and-create-an-autogenous-fistula-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold C anatomy)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: F Anatomy
CAMERA: three-quarter, studio
HUMAN VARIATION: No people, or hands only
AUDIENCE: Clinicians
VISUAL GOAL: A fistula is a vein remodeled by flow.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Anatomy. Camera: three-quarter, studio. Subject: a clean schematic forearm with a radial artery joined to a dilated cephalic vein, the vein visibly enlarged and thick-walled downstream of the anastomosis, rendered in renal reds and soft blues on an off-white background; no operative field, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Maturation is a race**  ·  skill `williamriveromd-biomedical-mechanism-figure`  ·  placed in section `maturation`

```
FILE NAME: images/vascular-surgeon-06-maturation-race.png
IMAGE TYPE: Organ → inset → injury/benefit
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Maturation is a race between outward remodeling and neointimal hyperplasia.

PROMPT:
Title at top: "Maturation is a race". Left panel: a forearm with a radiocephalic fistula (schematic). Center inset (dashed box): the vein beyond the anastomosis split into two halves. Upper half in blue, label "High flow → shear stress → nitric oxide → outward remodeling, thicker wall". Lower half at the swing segment in red, label "Injury → neointimal hyperplasia → narrowed lumen". A finish-line icon reading "Usable for two needles". Bottom row of four small failure cards: "Inflow: small or calcified artery", "Juxta-anastomotic stenosis", "Deep or branched vein", "Outflow stenosis". Footer: "Median 115 days to maturation in the HFM study." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Maturation is a race between outward remodeling and neointimal hyperplasia. In the Hemodialysis Fistula Maturation (HFM) study, median time to maturation was 115 days.
*Alt text:* Mechanism of fistula maturation: outward remodeling from shear stress racing against neointimal hyperplasia, with four failure routes.

**Figure B: A drug moved the surrogate, not the outcome**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `drugs`

```
FILE NAME: images/vascular-surgeon-06-surrogate-versus-function.png
IMAGE TYPE: B Side-by-side comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: A surrogate is not the outcome.

PROMPT:
Title at top: "A drug moved the surrogate, not the outcome". Two panels, each with a pair of simple vertical bars (placebo gray, clopidogrel teal), exact labels on bars. Left panel title "Early thrombosis (surrogate)": placebo "19.5%", clopidogrel "12.2%", a green check. Right panel title "Never suitable for dialysis (what matters)": placebo "59.5%", clopidogrel "61.8%", an amber equals sign. Caption under panels: "DAC trial, 877 patients, randomized". Footer: "Judge a fistula by use, not by patency." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* A surrogate is not the outcome. In the Dialysis Access Consortium (DAC) trial, clopidogrel reduced early fistula thrombosis but did not increase the number of fistulas suitable for dialysis.
*Alt text:* Bar pairs from the clopidogrel trial: less early thrombosis, but no more fistulas suitable for dialysis.

**Course tile**

```
FILE NAME: images/vascular-surgeon-06-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a clear acrylic model of a forearm with a red artery joined to a widening blue vein, studio light on white. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-06-plan-and-create-an-autogenous-fistula-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Plan and create an autogenous fistula". Subtitle in teal: "Vascular Surgeon · Module 6 of 20". Right 45%: a clean photorealistic still-life on a light surface: a clear acrylic model of a forearm with a red artery joined to a widening blue vein, studio light on white, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 7: Grafts and alternative configurations

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-07-grafts-and-alternative-configurations-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: overhead, macro
HUMAN VARIATION: No people, or hands only
AUDIENCE: Clinicians
VISUAL GOAL: A graft trades maturation for maintenance.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: overhead, macro. Subject: a coiled soft white synthetic vascular graft resting on a sterile pale-teal drape beside a surgical skin marker and a folded forearm diagram card with no readable writing, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the lower-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Why grafts narrow at the venous end**  ·  skill `williamriveromd-biomedical-mechanism-figure`  ·  placed in section `why`

```
FILE NAME: images/vascular-surgeon-07-graft-venous-anastomosis.png
IMAGE TYPE: Organ → inset → injury/benefit
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Why grafts narrow at the venous end.

PROMPT:
Title at top: "Why grafts narrow at the venous end". Left panel: a forearm loop graft (schematic) with the arterial end and the venous end labeled. Dashed inset at the venous end: a stiff graft joined to a soft vein, swirl arrows labeled "Turbulence and vibration", a stiffness gradient labeled "Compliance mismatch", and growing tissue inside the vein labeled "Neointimal hyperplasia". Bottom row: pink "Venous anastomotic stenosis → falling flow → clot" → blue "Watch the venous end; treat lesions that cause dysfunction" → blue "A graft trades a maturation problem for a maintenance problem". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Why grafts narrow at the venous end. Turbulence and the mismatch between a stiff graft and a soft vein drive hyperplasia that slowly lowers flow until the graft clots.
*Alt text:* Schematic of a loop graft and its venous anastomosis, where turbulence and compliance mismatch drive narrowing.

**Figure B: Fistula or graft: choosing with the patient**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `when`

```
FILE NAME: images/vascular-surgeon-07-fistula-versus-graft-card.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Fistula or graft.

PROMPT:
Title at top: "Fistula or graft: choosing with the patient". A two-column comparison table with teal headers "Fistula" and "Graft" and five rows: "Time to use": "Usually 3 to 6 months" | "Usually 2 to 4 weeks; early-cannulation grafts within days"; "Primary failure": "Common, about 1 in 4" | "Uncommon"; "Procedures to maintain": "Fewer once mature" | "More"; "Infection": "Lowest" | "Higher"; "Hand ischemia": "Usually later" | "More often early". Footer: "UKKA 3.4 (1C): a graft may be considered when early use is needed or anatomy is unfavorable." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Fistula or graft. A graft is a reasoned first choice when early use is needed or conventional anatomy is unfavorable (UKKA 2025, statement 3.4, grade 1C).
*Alt text:* Table comparing fistula and graft for time to use, primary failure, maintenance, infection and timing of hand ischemia.

**Course tile**

```
FILE NAME: images/vascular-surgeon-07-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a coiled white synthetic vascular graft on a pale teal sterile drape, macro view. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-07-grafts-and-alternative-configurations-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Grafts and alternative configurations". Subtitle in teal: "Vascular Surgeon · Module 7 of 20". Right 45%: a clean photorealistic still-life on a light surface: a coiled white synthetic vascular graft on a pale teal sterile drape, macro view, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 8: Dialysis catheters and central veins

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-08-dialysis-catheters-and-central-veins-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold C anatomy)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: F Anatomy
CAMERA: frontal, slight three-quarter
HUMAN VARIATION: No people, or hands only
AUDIENCE: Clinicians
VISUAL GOAL: Catheters are bridges that wear the riverbanks.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: F Anatomy. Camera: frontal, slight three-quarter. Subject: a translucent upper torso showing the right internal jugular vein, brachiocephalic veins and superior vena cava with a tunneled dual-lumen catheter tip in the right atrium, central veins highlighted in soft blue, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Where a catheter goes, and what it can cost**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `injury`

```
FILE NAME: images/vascular-surgeon-08-central-veins-and-catheter-sites.png
IMAGE TYPE: D Single mechanism poster
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Where a catheter goes, and what it can cost.

PROMPT:
Title at top: "Where a catheter goes, and what it can cost". A clean frontal schematic of the neck and upper chest veins (labeled "schematic"): right and left internal jugular, subclavian and brachiocephalic veins, superior vena cava, right atrium. A tunneled catheter in the right internal jugular marked with a green badge "First choice (UKKA 5.1)". The subclavian route crossed out in red with "Avoid when other veins exist (UKKA 5.2)". Red injury markers at the bends where veins pass under the clavicle labeled "Wall injury → stenosis". A faint arm on each side labeled "Future access drains here". Bottom strip: "Every catheter: why now, where, how checked, until when." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Where a catheter goes, and what it can cost. The UK Kidney Association (UKKA) favors the right internal jugular vein and avoiding the subclavian route, because injured central veins drain future arm access.
*Alt text:* Schematic of central veins showing the preferred right internal jugular site, the avoided subclavian route and stenosis sites.

**Figure B: Poor flow after insertion: when to stop**  ·  skill `williamriveromd-algorithm-generator-skill`  ·  placed in section `complications`

```
FILE NAME: images/vascular-surgeon-08-stop-troubleshooting.png
IMAGE TYPE: A Clinical algorithm
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: When to stop troubleshooting.

PROMPT:
Title at top: "Poor flow after insertion: when to stop". Top node navy "Poor catheter flow after insertion or exchange". Decision teal "Is the patient deteriorating? breathless, hypotensive, hypoxic, chest pain". YES → red node "Stop using the catheter. Airway, breathing, circulation. Image the chest. Call senior and emergency team" → red node "Do not reverse lines or keep dialyzing until position is confirmed". NO → amber node "Systematic dysfunction work-up" → amber "Thrombolytic lock (UKKA 6.2)" → purple "Exchange where fibrin sheath disruption is available (UKKA 6.3)". Footer: "Resistance is information. The problem is the patient, not the flow rate." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* When to stop troubleshooting. A deteriorating patient after a catheter procedure turns a flow problem into an emergency.
*Alt text:* Algorithm for poor catheter flow: stop and escalate if the patient deteriorates; otherwise lock, then exchange.

**Course tile**

```
FILE NAME: images/vascular-surgeon-08-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a tunneled dual-lumen dialysis catheter laid in a gentle curve on a white tray beside a small anatomical heart model. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-08-dialysis-catheters-and-central-veins-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Dialysis catheters and central veins". Subtitle in teal: "Vascular Surgeon · Module 8 of 20". Right 45%: a clean photorealistic still-life on a light surface: a tunneled dual-lumen dialysis catheter laid in a gentle curve on a white tray beside a small anatomical heart model, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 9: Maturation and the first cannulation

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-09-maturation-and-the-first-cannulation-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: close portrait, eye level
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Patent is not the same as usable.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: close portrait, eye level. Subject: a senior Filipino dialysis nurse in his 50s with a thin mustache, rounded face and white uniform marking a straight segment on a young woman’s forearm fistula with a skin pen while a female surgeon in her 30s with braided hair watches, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Ultrasound and readiness: what the numbers showed**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `readiness`

```
FILE NAME: images/vascular-surgeon-09-robbin-criteria.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Ultrasound and readiness.

PROMPT:
Title at top: "Ultrasound and readiness: what the numbers showed". A clean card with three horizontal bars showing the share of fistulas adequate for dialysis: green bar "Both: vein at least 4 mm and flow at least 500 mL/min → 95% (19 of 20)"; amber bar "Vein at least 4 mm (either flow) → 89% (24 of 27)" and amber bar "Flow at least 500 mL/min (either diameter) → 84% (26 of 31)"; red bar "Neither → 33% (5 of 15)". Small source line: "Robbin 2002, 54 fistulas with known outcome". Footer: "Surrogates for usability. Add depth and a straight segment, judged together." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Ultrasound and readiness. In Robbin’s study, 95% of fistulas meeting both diameter and flow criteria were adequate for dialysis, against 33% meeting neither. Depth and a usable straight segment still decide first use.
*Alt text:* Bar card of the Robbin criteria: share of fistulas adequate for dialysis when both, one, or neither ultrasound criterion was met.

**Figure B: A thrill is not a usable fistula**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `timing`

```
FILE NAME: images/vascular-surgeon-09-patent-is-not-usable.png
IMAGE TYPE: D Single mechanism poster
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: A thrill is not a usable fistula.

PROMPT:
Title at top: "A thrill is not a usable fistula". A central forearm fistula schematic with a glowing "thrill" icon near the anastomosis and four numbered problem callouts along it: 1 "Vein too deep to needle" (cross-section showing depth below skin), 2 "Large side branch steals flow", 3 "Narrowing beside the anastomosis", 4 "Segment too short or tortuous". Each callout has a small green fix chip: "Superficialization", "Branch ligation", "Imaging and angioplasty or revision", "Discuss another site". Footer: "Silence is not permission to cannulate." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* A thrill is not a usable fistula. Depth, a diverting side branch, a juxta-anastomotic narrowing or a short segment can each block first use; each has a usual fix.
*Alt text:* Fistula schematic with a thrill but four reasons it cannot yet be needled, each paired with its usual fix.

**Course tile**

```
FILE NAME: images/vascular-surgeon-09-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a skin pen and a strip of medical tape marking a straight line on a plaster forearm model with a soft glow over the vein. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-09-maturation-and-the-first-cannulation-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Maturation and the first cannulation". Subtitle in teal: "Vascular Surgeon · Module 9 of 20". Right 45%: a clean photorealistic still-life on a light surface: a skin pen and a strip of medical tape marking a straight line on a plaster forearm model with a soft glow over the vein, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 10: Recognize a failing access

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-10-recognize-a-failing-access-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: rear three-quarter
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Read the access against its own baseline.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: rear three-quarter. Subject: a Filipino man in his late 50s in a gray polo seated in a dialysis chair raising his access arm while a surgeon observes the fistula; a dialysis machine display glows softly blurred beside them, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Reading the access: where is the narrowing?**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `physiology`

```
FILE NAME: images/vascular-surgeon-10-where-is-the-stenosis.png
IMAGE TYPE: B Side-by-side comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Where is the narrowing? Outflow lesions trap pressure; inflow lesions starve the access.

PROMPT:
Title at top: "Reading the access: where is the narrowing?". Two panels, each with a garden-hose-style access drawn over a forearm. Left panel red header "Outflow stenosis": the pinch near the outflow, the segment before it swollen; labels "Pulsatile, firm", "Does not collapse when the arm is raised", "Needle sites bleed longer", "High venous pressure", "Arm swelling". Right panel amber header "Inflow stenosis": the pinch near the artery, the access flat; labels "Soft and flat", "Collapses when the arm is raised", "Poor blood flow", "More negative arterial pressure". Footer: "Compare with the patient’s own baseline." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Where is the narrowing? Outflow lesions trap pressure; inflow lesions starve the access. Compare every sign with the patient’s own baseline.
*Alt text:* Two panels: the bedside signs of an outflow stenosis versus an inflow stenosis.

**Figure B: Fixing stenosis before it causes trouble**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `evidence`

```
FILE NAME: images/vascular-surgeon-10-preemptive-correction-forest.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Fixing stenosis early.

PROMPT:
Title at top: "Fixing stenosis before it causes trouble". A simple forest-plot style card with a vertical line at 1.0 labeled "No effect". Row 1 "Access loss": point at 0.81 with a horizontal line from 0.65 to 1.02 crossing the 1.0 line, label "RR 0.81 (0.65 to 1.02): not significant". Row 2 "Thrombosis": point at 0.79 with a line from 0.65 to 0.97, label "RR 0.79 (0.65 to 0.97)". Header: "14 randomized trials, 1,390 people". Footer: "A scan finding in a working access is not, by itself, a reason to treat." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Fixing stenosis early. Across 14 randomized trials, preemptive correction reduced thrombosis but not access loss; treat the patient’s problem, not the scan.
*Alt text:* Forest-plot card: preemptive stenosis correction reduced thrombosis but did not significantly reduce access loss.

**Course tile**

```
FILE NAME: images/vascular-surgeon-10-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: a garden hose with a gentle pinch near its end on a white surface, a small pressure gauge beside it. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-10-recognize-a-failing-access-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Recognize a failing access". Subtitle in teal: "Vascular Surgeon · Module 10 of 20". Right 45%: a clean photorealistic still-life on a light surface: a garden hose with a gentle pinch near its end on a white surface, a small pressure gauge beside it, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 11: Stenosis and endovascular choices

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-11-stenosis-and-endovascular-choices-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: H Clinical
CAMERA: wide-angle, high angle
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Choose the device that protects the next site.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: wide-angle, high angle. Subject: an angiography suite with a fistulogram on a large monitor showing a narrowing, two clinicians in lead aprons (a stocky interventional radiologist in his 40s and a lean female surgeon in her 50s with short gray hair) discussing the image, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the lower-right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Why stenoses come back, and how devices respond**  ·  skill `williamriveromd-biomedical-mechanism-figure`  ·  placed in section `mechanism`

```
FILE NAME: images/vascular-surgeon-11-why-restenosis.png
IMAGE TYPE: Organ → inset → injury/benefit
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Why stenoses return.

PROMPT:
Title at top: "Why stenoses come back, and how devices respond". Left panel: an upper-arm access with a narrowed segment (schematic). Center inset (dashed box) in three small frames: "Balloon stretches and tears the wall" → "Recoil" → "New neointimal hyperplasia". Two therapy callouts: blue "Drug-coated balloon: paclitaxel slows the cells that drive scar", blue "Stent graft: holds the lumen and walls off healing tissue". Bottom row: pink "Injury restarts the healing that caused the lesion" → blue "Choose the device for the lesion and the next site" → blue "Judge success by reliable dialysis". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Why stenoses return. Balloon injury restarts neointimal hyperplasia; drug-coated balloons slow it and stent grafts wall it off, each with trade-offs.
*Alt text:* Mechanism of restenosis after balloon angioplasty, with how drug-coated balloons and stent grafts aim to delay it.

**Figure B: Landing zone: protect the next site**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `future`

```
FILE NAME: images/vascular-surgeon-11-landing-zone.png
IMAGE TYPE: B Side-by-side comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Landing zone.

PROMPT:
Title at top: "Landing zone: protect the next site". Two panels of the same upper-arm venous anatomy (schematic): graft-vein anastomosis, basilic vein, axillary vein junction. Left panel green "Protects the contingency": a stent graft ending before the junction, the axillary vein open and labeled "Next access possible". Right panel red "Consumes the contingency": a stent graft crossing the junction into the axillary vein, label "Future site covered". Footer: "Agree the landing zone with the access team before deployment." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Landing zone. A convenient deployment across a venous junction can consume the patient’s next access; agree where the device may land.
*Alt text:* Two diagrams: a stent graft ending before a venous junction versus one crossing it and covering the next access site.

**Course tile**

```
FILE NAME: images/vascular-surgeon-11-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a deflated angioplasty balloon catheter and a short covered stent graft on a sterile blue-green drape, macro view, no blood. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-11-stenosis-and-endovascular-choices-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Stenosis and endovascular choices". Subtitle in teal: "Vascular Surgeon · Module 11 of 20". Right 45%: a clean photorealistic still-life on a light surface: a deflated angioplasty balloon catheter and a short covered stent graft on a sterile blue-green drape, macro view, no blood, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 12: Thrombosis and urgent dialysis

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-12-thrombosis-and-urgent-dialysis-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: J Environmental Storytelling
CAMERA: over-the-shoulder
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Dialysis safety and salvage run in parallel.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: J Environmental Storytelling. Camera: over-the-shoulder. Subject: an emergency bay where a breathless Filipino man in his late 60s sits upright with nasal oxygen, a nephrologist checks a monitor showing an ECG trace, and a surgeon feels his upper-arm graft, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: A clotted access: two jobs at once**  ·  skill `williamriveromd-infographic-skill`  ·  placed in section `two`

```
FILE NAME: images/vascular-surgeon-12-two-lanes.png
IMAGE TYPE: Two-lane workflow
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: A clotted access means two jobs at once.

PROMPT:
Title at top: "A clotted access: two jobs at once". Two parallel horizontal lanes that merge on the right. Upper lane red header "Dialysis safety (nephrologist and emergency team)": steps "Potassium and ECG", "Oxygen and volume", "Emergency treatment", "Dialysis, bridge catheter if needed". Lower lane teal header "Access salvage (surgeon or interventionist)": steps "How long silent?", "Surgical or endovascular", "Find the culprit lesion", "Confirm flow". Both lanes merge into a green node "Next session booked and confirmed". Small note on the bridge catheter: "Site chosen to protect the access arm". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* A clotted access means two jobs at once. Dialysis safety and salvage run in parallel, with a bridge catheter placed to protect the access arm.
*Alt text:* Two-lane workflow: dialysis safety and access salvage run in parallel and meet at a confirmed next session.

**Figure B: Clues to why the access clotted**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `why`

```
FILE NAME: images/vascular-surgeon-12-why-accesses-clot.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Why the access clotted.

PROMPT:
Title at top: "Clues to why the access clotted". A reference table with teal headers "Clue before the clot", "Likely cause", "At salvage" and four rows: "Rising venous pressure, prolonged bleeding" | "Outflow stenosis" | "Image and treat the outflow"; "Weak, flat access in prior weeks" | "Inflow or juxta-anastomotic stenosis" | "Image the arterial side"; "Clot after a hypotensive session or diarrhea" | "Low flow from low pressure" | "Review target weight and drugs"; "Repeated clots, no lesion" | "Hypercoagulability or compression" | "Consider testing and teaching". Footer: "Remove the clot, then fix the reason it formed." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Why the access clotted. Removing the clot without treating the culprit leads to another clot.
*Alt text:* Table linking clues before an access clot to the likely cause and what to do at salvage.

**Course tile**

```
FILE NAME: images/vascular-surgeon-12-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: two parallel ribbons, one red and one teal, merging into one green ribbon on a white surface. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-12-thrombosis-and-urgent-dialysis-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Thrombosis and urgent dialysis". Subtitle in teal: "Vascular Surgeon · Module 12 of 20". Right 45%: a clean photorealistic still-life on a light surface: two parallel ribbons, one red and one teal, merging into one green ribbon on a white surface, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 13: Hand ischemia and neurologic injury

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-13-hand-ischemia-and-neurologic-injury-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: macro, hands-only
HUMAN VARIATION: Hands only; skin tone, age and hand position differ from the previous image
AUDIENCE: Clinicians
VISUAL GOAL: A thrill reassures about the access, never the hand.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: macro, hands-only. Subject: two hands of a Filipina woman in her 70s side by side on a white sheet, one slightly paler and cooler-toned, a clinician’s fingers testing fingertip sensation with a cotton wisp, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Hand ischemia is a pressure problem**  ·  skill `williamriveromd-biomedical-mechanism-figure`  ·  placed in section `mechanism`

```
FILE NAME: images/vascular-surgeon-13-pressure-not-steal.png
IMAGE TYPE: Organ → inset → injury/benefit
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Hand ischemia is a pressure problem.

PROMPT:
Title at top: "Hand ischemia is a pressure problem". Left panel: an arm with a brachial-based fistula (schematic) and a color gradient of perfusion pressure along the forearm arteries from teal near the elbow to pale red at the fingers, label "Pressure falls toward the fingers". Inset (dashed box): the artery beyond the anastomosis with a small reversed-flow arrow labeled "Reversed flow: common, often harmless". Risk chips: "Diabetes", "Coronary disease", "Female", "Brachial inflow". Bottom row: pink "Arteries cannot enlarge; the access draws off pressure" → blue "Grade it; find inflow stenosis or high flow" → blue "Restore hand perfusion; the hand outranks the access". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Hand ischemia is a pressure problem. Reversed flow beyond the access is common; symptoms come when perfusion pressure in the hand falls too low.
*Alt text:* Mechanism of access-related hand ischemia: falling perfusion pressure toward the fingers, with reversed flow shown as often harmless.

**Figure B: Grade the threatened hand**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `grading`

```
FILE NAME: images/vascular-surgeon-13-steal-grading-card.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Grade the threatened hand.

PROMPT:
Title at top: "Grade the threatened hand". A four-row reference card with colored left bars. Row 1 green "Grade 1, mild: pale or cool, no pain → no treatment; document and review". Row 2 amber "Grade 2, moderate: pain on exercise or during dialysis → treatment often needed; may be planned". Row 3 red "Grade 3, severe: rest pain, ulcer or necrosis → prompt treatment". Row 4 dark red with an alert icon "Any grade with new weakness or numbness → immediate surgical assessment". Footer: "A thrill reassures you about the access, never about the hand. (UKKA 2025)" Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Grade the threatened hand. The UK Kidney Association (UKKA) grade links symptoms to urgency; new weakness or numbness needs immediate surgical assessment.
*Alt text:* Card grading access-related hand ischemia from mild to severe, with new neurologic deficit as an immediate emergency.

**Course tile**

```
FILE NAME: images/vascular-surgeon-13-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: two hands resting side by side on a white sheet, one paler, a cotton wisp touching a fingertip. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-13-hand-ischemia-and-neurologic-injury-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Hand ischemia and neurologic injury". Subtitle in teal: "Vascular Surgeon · Module 13 of 20". Right 45%: a clean photorealistic still-life on a light surface: two hands resting side by side on a white sheet, one paler, a cotton wisp touching a fingertip, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 14: Aneurysm and life threatening bleeding

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-14-aneurysm-and-life-threatening-bleeding-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: close-up, side light
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Mixed
VISUAL GOAL: Two-finger pressure and a call for help.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: close-up, side light. Subject: a gloved hand pressing two fingers firmly on a gauze pad over an upper-arm fistula of a Filipino man in his 50s, a nurse calling for help softly blurred in the background; no visible blood, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Read the skin over an aneurysm**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `why`

```
FILE NAME: images/vascular-surgeon-14-skin-threat-ladder.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Read the skin over an aneurysm.

PROMPT:
Title at top: "Read the skin over an aneurysm". A vertical ladder of four illustrated skin swatches over an access bulge (clean illustration, no blood), from bottom to top: green "Thick healthy skin: rotate sites, review"; amber "Rapid growth, rising venous pressure: image and treat the outflow"; red "Thin, shiny or discolored skin: do not cannulate; urgent review"; dark red "Ulcer, scab or recent bleed: do not cannulate; same-day surgical assessment". Footer: "A small bleed from threatened skin is a warning, not a resolved problem." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Read the skin over an aneurysm. Thin, shiny, ulcerated or scabbed skin means the barrier has almost gone; never needle it.
*Alt text:* Ladder of skin changes over an access aneurysm, from healthy to impending rupture, with the action for each.

**Figure B: Stopping an access bleed at home**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `teaching`

```
FILE NAME: images/vascular-surgeon-14-two-finger-pressure.png
IMAGE TYPE: B Do / Don’t comparison
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Stopping an access bleed.

PROMPT:
Title at top: "Stopping an access bleed at home". Two clean illustrated panels of a hand over an upper-arm access (no blood, no wound shown). Left panel green check "Do": two fingertips pressing firmly on one point, labels "Press firmly on the spot", "Keep pressing", "Call for emergency help". Right panel red cross "Don’t": a bulky towel spread loosely, labels "Bulky dressing spreads the pressure", "Do not lift to look". Footer: "Teach every patient and household. Most fatal access bleeds happen at home." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Stopping an access bleed. In a forensic series of 100 deaths, 81% of fatal access hemorrhages occurred at home, so every household should know focused two-finger pressure.
*Alt text:* Do and don’t panels: two-finger focused pressure versus a loose bulky dressing for an access bleed.

**Course tile**

```
FILE NAME: images/vascular-surgeon-14-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a folded gauze pad under two gloved fingertips pressing on a plaster arm model, no blood. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-14-aneurysm-and-life-threatening-bleeding-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Aneurysm and life threatening bleeding". Subtitle in teal: "Vascular Surgeon · Module 14 of 20". Right 45%: a clean photorealistic still-life on a light surface: a folded gauze pad under two gloved fingertips pressing on a plaster arm model, no blood, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 15: Access infection and sepsis

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-15-access-infection-and-sepsis-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: H Clinical
CAMERA: environmental portrait, eye level
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Sepsis first, then source control.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: environmental portrait, eye level. Subject: a Filipina woman in her 60s with short curly hair on an emergency trolley with an IV line, blood culture bottles on a tray, a young female nurse with glasses preparing the bottles and a surgeon examining a reddened forearm, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Why foreign material keeps the infection**  ·  skill `williamriveromd-biomedical-mechanism-figure`  ·  placed in section `biology`

```
FILE NAME: images/vascular-surgeon-15-biofilm-versus-living-wall.png
IMAGE TYPE: Organ → inset → injury/benefit
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Why foreign material keeps the infection.

PROMPT:
Title at top: "Why foreign material keeps the infection". Two magnified dashed insets side by side. Left inset "Catheter or graft surface": bacteria in a gel-like biofilm matrix on a gray synthetic surface, antibiotic molecules bouncing off, labels "Biofilm forms within days", "Shielded from antibiotics and white cells", "Sheds into the blood". Right inset "Living fistula wall": vessel wall with capillaries and immune cells reaching bacteria, label "Perfused, defended tissue". Bottom row: pink "Same organism returns after treatment" → blue "Sepsis care first, then source control" → blue "Remove infected synthetic material when indicated". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Why foreign material keeps the infection. Biofilm shields bacteria on synthetic surfaces; a living fistula wall can often clear infection with antibiotics.
*Alt text:* Comparison of biofilm on a catheter or graft surface with a perfused, defended fistula wall.

**Figure B: Source control by access type**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `sepsis`

```
FILE NAME: images/vascular-surgeon-15-source-control-matrix.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Source control by access type, after sepsis care has started..

PROMPT:
Title at top: "Source control by access type". Reference table with teal headers "Access", "Why it matters", "Usual source control" and four rows: "Catheter" | "Biofilm on the surface" | "Exchange or removal for severe, recurrent or S. aureus infection"; "Graft, localized" | "Infected segment of synthetic material" | "Partial excision and bypass"; "Graft, extensive or with sepsis" | "Material cannot be sterilized" | "Total or near-total removal"; "Fistula" | "Living wall" | "Often antibiotics; surgery for abscess or bleeding". A red banner above the table: "Hypotension with an infected access = sepsis first". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Source control by access type, after sepsis care has started.
*Alt text:* Table of usual source control for an infected catheter, graft or fistula, under a sepsis-first banner.

**Course tile**

```
FILE NAME: images/vascular-surgeon-15-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: two blood culture bottles and a petri dish with a faint biofilm sheen on a light lab bench. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-15-access-infection-and-sepsis-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Access infection and sepsis". Subtitle in teal: "Vascular Surgeon · Module 15 of 20". Right 45%: a clean photorealistic still-life on a light surface: two blood culture bottles and a petri dish with a faint biofilm sheen on a light lab bench, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 16: High flow and central venous obstruction

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-16-high-flow-and-central-venous-obstruction-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: H Clinical
CAMERA: wide-angle, table level
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: State the mechanism before the operation.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: H Clinical. Camera: wide-angle, table level. Subject: a small multidisciplinary meeting room where a cardiologist in her 40s wearing a hijab, a nephrologist in his 60s with a gray beard and a surgeon review an echocardiogram and a duplex flow study on two screens, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: The access and the heart**  ·  skill `williamriveromd-organ-crosstalk-sigil-graphic`  ·  placed in section `physiology`

```
FILE NAME: images/vascular-surgeon-16-access-heart-crosstalk.png
IMAGE TYPE: Organ crosstalk sigil
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: The access and the heart.

PROMPT:
Title at top: "The access and the heart". Minimal monoline organ sigils on white: an arm with an access on the left, a heart in the center, lungs on the right, connected by dotted teal flow lines. Labels along the lines: "Low resistance shunt" (arm), "Venous return rises" (arm to heart), "Cardiac output rises" (heart), "Most adapt without symptoms" (green note), "High flow in some: breathlessness" (amber note toward lungs). A small caption chip: "Access flow of 2.0 L/min or more: investigate, do not assume (small study)". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* The access and the heart. An access lowers resistance and raises cardiac output; most patients adapt, and high flow prompts investigation rather than a diagnosis.
*Alt text:* Minimal sigil diagram linking an arm access, the heart and the lungs through rising venous return and cardiac output.

**Figure B: Breathless with an access: find the mechanism**  ·  skill `williamriveromd-algorithm-generator-skill`  ·  placed in section `options`

```
FILE NAME: images/vascular-surgeon-16-breathlessness-tree.png
IMAGE TYPE: A Clinical algorithm
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Find the mechanism.

PROMPT:
Title at top: "Breathless with an access: find the mechanism". Top node navy "Breathless patient with an upper-arm access". Five parallel teal test branches: "Volume: weight trend, edema, response to fluid removal", "Access: flow and cardiac output", "Heart: ischemia, valves", "Anemia: hemoglobin", "Lungs and pulmonary pressure". A purple node below "Brief access compression: do heart rate and output fall?" → YES green "Access contributes: discuss flow reduction (banding) with the team"; NO amber "Look elsewhere; keep the access". Footer: "State the mechanism before the operation." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Find the mechanism. A fall in heart rate and output with brief access compression supports an access contribution; otherwise keep the access and look elsewhere.
*Alt text:* Algorithm for breathlessness in a patient with an access: test competing causes, then use brief compression before flow reduction.

**Course tile**

```
FILE NAME: images/vascular-surgeon-16-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: an anatomical heart model and a schematic arm model connected by a soft dotted teal line on white. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-16-high-flow-and-central-venous-obstruction-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "High flow and central venous obstruction". Subtitle in teal: "Vascular Surgeon · Module 16 of 20". Right 45%: a clean photorealistic still-life on a light surface: an anatomical heart model and a schematic arm model connected by a soft dotted teal line on white, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 17: The difficult access and changing modality

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-17-the-difficult-access-and-changing-modality-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: E Lifestyle
CAMERA: top-down over a table
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Reconstruct the history before the next attempt.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: E Lifestyle. Camera: top-down over a table. Subject: a conference table seen from above with old venogram films, a hand-drawn timeline of operations on paper with no readable words, a peritoneal dialysis bag and a transplant information folder, the hands of three clinicians and a patient pointing, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the lower-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Reconstruct the history before the next attempt**  ·  skill `williamriveromd-infographic-skill`  ·  placed in section `history`

```
FILE NAME: images/vascular-surgeon-17-access-chronology.png
IMAGE TYPE: Timeline
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Reconstruct the history before the next attempt.

PROMPT:
Title at top: "Reconstruct the history before the next attempt". A horizontal timeline on soft gray with year ticks labeled only "Year 1" to "Year 7". Above the line, access icons with outcome chips: "Left forearm fistula: never matured", "Right forearm fistula: thrombosed", "Left upper-arm graft: repeated stenosis". Below the line, intervention dots "Angioplasty" and "Thrombectomy" and catheter bars "Jugular catheter". At the right end a panel "What remains" with chips "Central veins: image first", "Peritoneal dialysis", "Transplant", "Supportive care". Footer: "Every failure had a cause. Write it down." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Reconstruct the history before the next attempt. A dated chronology with the reason each route failed prevents repeating a known mistake.
*Alt text:* Timeline of a patient’s accesses, interventions and catheters over seven years, ending with the options that remain.

**Figure B: When access is hard: the paths to discuss**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `conference`

```
FILE NAME: images/vascular-surgeon-17-paths-when-access-is-hard.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: When access is hard, discuss every path with the patient at a complex access conference..

PROMPT:
Title at top: "When access is hard: the paths to discuss". Five horizontal cards stacked, each with an icon: "Further upper-limb access: needs patent outflow; lower odds"; "Lower-limb or complex reconstruction: needs expertise and rescue capacity"; "Peritoneal dialysis: spares the veins; daily self-care"; "Transplant: fitness and a donor"; "Long-term catheter or conservative care: an informed choice". A people icon at the top: "Complex access conference with the patient". Footer: "No modality is a punishment for difficult vessels." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* When access is hard, discuss every path with the patient at a complex access conference.
*Alt text:* Five paths for a patient with difficult access, from further upper-limb access to conservative care.

**Course tile**

```
FILE NAME: images/vascular-surgeon-17-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: old X-ray films fanned on a table beside a hand-drawn timeline with no readable words and a peritoneal dialysis bag. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-17-the-difficult-access-and-changing-modality-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "The difficult access and changing modality". Subtitle in teal: "Vascular Surgeon · Module 17 of 20". Right 45%: a clean photorealistic still-life on a light surface: old X-ray films fanned on a table beside a hand-drawn timeline with no readable words and a peritoneal dialysis bag, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 18: Kidney care beyond the access

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-18-kidney-care-beyond-the-access-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: A Editorial Portrait
CAMERA: low angle, kneeling perspective
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Notice the problem the referral did not name.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: A Editorial Portrait. Camera: low angle, kneeling perspective. Subject: a Filipino surgeon in his 40s with a lean face and short side-parted hair kneeling to examine the bare foot of an older man with diabetes seated on a clinic chair, his fistula arm resting on the armrest, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Not the access? Route it**  ·  skill `williamriveromd-algorithm-generator-skill`  ·  placed in section `interfaces`

```
FILE NAME: images/vascular-surgeon-18-routing-map.png
IMAGE TYPE: A Clinical algorithm
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Not the access? Route it.

PROMPT:
Title at top: "Not the access? Route it". Top node navy "Access patient with another vascular problem". Four branches to colored destination nodes: "Rest pain, toe wound, gangrene" → red "Urgent vascular service"; "Sudden cold, painful, pale limb" → dark red "Emergency vascular surgery"; "Transplant recipient: new hypertension or graft dysfunction" → purple "Transplant team"; "Resistant hypertension, flash pulmonary edema" → teal "Nephrologist with vascular input". Final node: "Warm handoff: call, findings, urgency, confirmed acceptance". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Not the access? Route it. Recognizing a problem and handing it to the right team is part of good access care.
*Alt text:* Routing algorithm for non-access vascular problems in dialysis patients, each to its own service.

**Figure B: Investigate without harming the kidneys**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `kidney`

```
FILE NAME: images/vascular-surgeon-18-protect-residual-function.png
IMAGE TYPE: C Horizontal step sequence
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Investigate without harming the kidneys.

PROMPT:
Title at top: "Investigate without harming the kidneys". Four cards in a row with arrows. 1 teal "Ask what result you need". 2 green "Duplex first when it answers the question". 3 amber "If angiography: lowest effective contrast". 4 purple "Plan timing and fluids with the renal team". Above the row a kidney icon with a water drop labeled "Residual kidney function: worth protecting". Footer: "Contrast-associated AKI is the usual worry." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Investigate without harming the kidneys. Residual function helps control fluid and potassium; choose the least harmful test that answers the question. AKI: acute kidney injury.
*Alt text:* Four steps to investigate a dialysis or late chronic kidney disease patient while protecting residual kidney function.

**Course tile**

```
FILE NAME: images/vascular-surgeon-18-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic still-life for a course tile that is shown as small as 320 × 180 px. Subject: a clinician’s gloved hands examining a foot model with a small toe dressing, a fistula arm model in the background. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-18-kidney-care-beyond-the-access-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Kidney care beyond the access". Subtitle in teal: "Vascular Surgeon · Module 18 of 20". Right 45%: a clean photorealistic still-life on a light surface: a clinician’s gloved hands examining a foot model with a small toe dressing, a fistula arm model in the background, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 19: Philippine documentation and quality

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-19-philippine-documentation-and-quality-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold B still-life)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: I Object Hero
CAMERA: overhead
HUMAN VARIATION: No people, or hands only
AUDIENCE: Clinicians
VISUAL GOAL: Honest measures make improvement possible.

PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: I Object Hero. Camera: overhead. Subject: a laptop on a light table showing an unlabeled run chart, beside a stack of folders, a pen and a coffee cup, viewed from above; no readable text on the screen or paper, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the upper-left side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Three kinds of patency**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `measures`

```
FILE NAME: images/vascular-surgeon-19-patency-definitions.png
IMAGE TYPE: D Single mechanism poster
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Three kinds of patency, as defined by the Society for Vascular Surgery (SVS) reporting standards.

PROMPT:
Title at top: "Three kinds of patency". A horizontal timeline from "Creation" with event markers: "Intervention to keep it open", "Thrombosis", "Thrombectomy", "Abandonment". Three colored bars run from Creation: teal bar "Primary patency" ends at the first intervention or thrombosis; green bar "Assisted primary patency" passes through interventions and ends at thrombosis or abandonment; purple bar "Secondary patency" passes through interventions and thrombectomy and ends at abandonment. A separate gold bar "Functional use" labeled "Actually used for dialysis". Footer: "SVS reporting standards. Patency is a surrogate; report use too." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Three kinds of patency, as defined by the Society for Vascular Surgery (SVS) reporting standards. Patency is a surrogate; report functional use beside it.
*Alt text:* Timeline showing where primary, assisted primary and secondary patency end, with functional use shown separately.

**Figure B: A code is not a payment**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `record`

```
FILE NAME: images/vascular-surgeon-19-code-is-not-payment.png
IMAGE TYPE: C Horizontal step sequence
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1792 × 1024 (generate at 1536 × 1024 if 1792 is unavailable)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: A code is not a payment.

PROMPT:
Title at top: "A code is not a payment". Four separate cards with gaps between them (no arrows implying one follows from the other), each with a small check box: "Procedure code: what was done", "Payer classification: how it is grouped", "Eligibility: patient, provider, accreditation", "Payable amount: rules on the date of service". Under each card a small label "Check separately". Footer: "Confirm current PhilHealth circulars with the claims lead. Never teach a fixed amount." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* A code is not a payment. Each of the four questions is verified on its own, against the rules in force on the date of service.
*Alt text:* Four separate checks: procedure code, payer classification, eligibility and payable amount.

**Course tile**

```
FILE NAME: images/vascular-surgeon-19-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: an overhead laptop showing an unlabeled run chart beside folders and a pen on a light desk. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-19-philippine-documentation-and-quality-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "Philippine documentation and quality". Subtitle in teal: "Vascular Surgeon · Module 19 of 20". Right 45%: a clean photorealistic still-life on a light surface: an overhead laptop showing an unlabeled run chart beside folders and a pen on a light desk, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

### Module 20: The integrated vascular access service

**Hero (circular vignette)**

```
FILE NAME: images/vascular-surgeon-20-the-integrated-vascular-access-service-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 (Scaffold A people)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048 (1024 × 1024 acceptable)
COMPOSITION ARCHETYPE: B Journey
CAMERA: side profile, wide
HUMAN VARIATION: Changed from the previous image: age, sex, face shape, hairstyle, hair length, clothing, colors, posture, hand position, expression, activity, setting, camera distance and angle
AUDIENCE: Clinicians
VISUAL GOAL: Every transition needs an owner.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: B Journey. Camera: side profile, wide. Subject: a young Filipina surgeon in her early 30s with a pixie cut presenting at a whiteboard showing a simple drawn pathway of connected circles with no words to a small panel of a nephrologist, a dialysis nurse and a quality lead, soft natural daylight, gentle shallow depth of field. Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the right side of soft gradient, clean wall or blurred background with no faces, anatomy, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, visible blood, open wounds, needles in skin, operative field.

QUALITY CHECK:
Circle 85–90% of canvas with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino clinical context; no text; no operative field or blood.
```

**Figure A: Every handoff needs an owner**  ·  skill `williamriveromd-infographic-skill`  ·  placed in section `pathway`

```
FILE NAME: images/vascular-surgeon-20-pathway-ring.png
IMAGE TYPE: Circular workflow
ASPECT RATIO: 1:1 square
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Every handoff needs an owner.

PROMPT:
Title at top: "Every handoff needs an owner". A circular ring of seven connected nodes with small owner badges: "Referral: accepting surgeon", "Planning: Life-Plan shared", "Creation: written handoff", "Maturation: assessed at 2 to 6 weeks", "First use: written plan", "Maintenance: clinical monitoring", "Rescue: emergency pathway". In the center a patient icon with a coordinator badge: "Pathway owner tracks and escalates". One node outlined in red dashes labeled "Orphaned step = no plan". Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Every handoff needs an owner. A pathway owner tracks the patient through each step and escalates delays; an orphaned step means there is no plan.
*Alt text:* Circular access pathway of seven steps, each with an owner, around a coordinator who tracks the patient.

**Figure B: Capstone: how the plan is judged**  ·  skill `williamriveromd-simple-figure`  ·  placed in section `capstone`

```
FILE NAME: images/vascular-surgeon-20-capstone-rubric.png
IMAGE TYPE: E Reference card
ASPECT RATIO: 4:3 card
PIXEL DIMENSIONS: 1536 × 1152 (generate at 1536 × 1024 and keep content inside the 4:3 center)
AUDIENCE: Clinicians (surgeons and trainees)
VISUAL GOAL: Capstone rubric.

PROMPT:
Title at top: "Capstone: how the plan is judged". A scoring card with five rows, each with three small boxes labeled 0, 1, 2: "Patient goals and alternatives", "Assessment and evidence", "Justified intervention and future options", "Safety and contingency", "Communication and improvement". A total box "Pass: 8 of 10, every emergency recognized and escalated". Footer: "A defensible alternative is welcome when it is explained." Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe/correct, amber #b8860b for caution, clinical red #b91c1c for danger, soft purple #6c3d8e for specialist steps. Typeface: Inter only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Generous whitespace. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text (about 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, unrealistic anatomy, overprocessed HDR, excessive saturation, photographs of real wounds, visible blood, needles in skin, and any operative step-by-step sequence. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans; no serif, decorative or handwritten typefaces. Do not invent numbers, doses, diameters, pressures or thresholds that are not written in this prompt. Use American English spelling on every label. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; clinically plausible and schematic (anatomy labeled as schematic, no dimensions); calm, publication-grade, white or soft light-gray background; renalcarematters.com visible bottom-right (bottom-center for portrait); one teaching idea only.
```

*On-page caption:* Capstone rubric. Five domains scored 0 to 2; a pass is 8 of 10 with every emergency recognized and escalated. Passing grants no privileges.
*Alt text:* Capstone rubric: five domains scored 0 to 2, with a pass mark of 8 of 10 and every emergency escalated.

**Course tile**

```
FILE NAME: images/vascular-surgeon-20-card.webp (generate PNG at 1536 × 1024, prep script crops and exports 640 × 360 WebP)
IMAGE TYPE: Course tile (16:9, no text)
PIXEL DIMENSIONS: master 1536 × 1024 → 640 × 360
VISUAL GOAL: Recognizable at thumbnail size; signals the module’s one idea.

PROMPT:
16:9 landscape photorealistic editorial still-life for a course tile that is shown as small as 320 × 180 px. Subject: a ring of seven small connected wooden tokens on a white table with a single central token, soft daylight. One bold, instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal #eef6f7), soft daylight, gentle shadow, high contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge for card cropping. Absolutely NO text, letters, numbers, logos or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, small details, people’s faces, text of any kind, dark backgrounds, visible blood, needles in skin, cartoon style, HDR.

QUALITY CHECK:
Readable at 320 px; one subject; light background; no text.
```

**OG share card**

```
FILE NAME: images/og/vascular-surgeon-20-the-integrated-vascular-access-service-og.jpg (generate PNG, prep script exports 1200 × 630 JPEG ≤ 300 KB)
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (final)
AUDIENCE: Clinicians
VISUAL GOAL: A share preview that names the module and shows its one idea.

PROMPT:
Social share card, final size exactly 1200 × 630 px (1.91:1). Design inside a 1.91:1 frame on a white (#ffffff) to pale teal (#eef6f7) background; generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1 without losing anything. Left 55%: text block in Inter. Small chip at top in teal #1a6b72 with white text "RENAL CARE ACADEMY · PHYSICIANS TRACK". Title in bold navy #0f1e2e, two lines at most: "The integrated vascular access service". Subtitle in teal: "Vascular Surgeon · Module 20 of 20". Right 45%: a clean photorealistic still-life on a light surface: a ring of seven small connected wooden tokens on a white table with a single central token, soft daylight, softly lit, no faces. A thin teal rule under the title. Bottom-right: "renalcarematters.com" in small semi-transparent navy text. Spell every word exactly as given, American English.

NEGATIVE INSTRUCTIONS:
Avoid extra words, misspellings, text in the outer bands that will be cropped, dark backgrounds, cluttered collage, people’s faces, visible blood, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.

QUALITY CHECK:
Title readable at 600 px wide; text only in the left 55%; nothing important outside the central 1.91:1 band; spelling exact.
```

## 7. Checklist before publishing

- [ ] Every label spelled exactly as in the prompt (GPT often misspells: compare letter by letter).
- [ ] No number appears on an image that is not in its prompt.
- [ ] Anatomy figures show "schematic" and no dimensions; no blood, wounds or needles in skin.
- [ ] `renalcarematters.com` visible on every teaching figure and OG card.
- [ ] Heroes: circle with white margin, empty title-safe zone, no text.
- [ ] Tiles readable at 320 px; OG titles readable at 600 px.
- [ ] Module pages checked in light and dark mode after the rebuild.
