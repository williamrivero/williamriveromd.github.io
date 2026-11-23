# GPT image production brief — Nephrology Nursing & Hemodialysis (12 module heroes)

**For:** a GPT image-generation session. This file is complete on its own; you do not need the website repository or any earlier conversation.
**Site:** Renal Care Matters (renalcarematters.com), a free kidney-health education library for Filipino patients and clinicians.
**What you are making:** one hero picture for each of 12 nursing-education modules. Each picture sits inside a circular frame beside the page title.
**What you are not making:** diagrams, infographics, labels, or anything with words. Two modules also need instructional diagrams; those are specified separately at the end and are **not** to be produced by free image generation.

## 1. Art direction (applies to every prompt)

Paste this block before each module prompt, or keep it as the session's standing instruction.

```
ART DIRECTION — RENAL CARE MATTERS NURSING SERIES

Format: square 1:1, 2048 x 2048 px. The scene is composed to be shown inside a CIRCLE that
fills 85-90% of the canvas, with a visible plain white margin all the way around. The circle
never touches the canvas edge and nothing important touches the circle's edge.

Style: realistic documentary-style editorial illustration with the look of a natural-light
photograph. Calm, warm, unstaged. Soft daylight, gentle depth of field. Bright and airy;
never dark, never high-contrast, never neon or HDR. Colors harmonize with clinical teal
#1a6b72, navy #1f3864, renal green #2e6b3e and warm neutrals. One consistent color grade
across all 12 images so they read as a set.

Setting and people: contemporary Philippine renal-care settings (ward, clinic, dialysis unit,
home). Filipino staff and patients with realistic, varied faces, ages, builds and skin tones.
Staff wear plain scrubs or uniforms with no logos; closed shoes; hair tied back; no jewelry on
hands except a plain watch or ring where stated. Patients are dressed modestly and shown with
dignity. Every image uses a different cast: no person may look like a person in another image.

Composition: one clear focal point that still reads when the picture is cropped to a small
circle on a phone. Hero subject 60-70% of the circle, supporting context 20-30%. Reserve
20-25% of the circle, on the LEFT side, as calm negative space (plain wall, soft blur, window
light) with no faces, hands or equipment in it.

Clinical accuracy: correct hands (five fingers), plausible anatomy, plausible equipment.
Equipment is generic and unbranded. If you are unsure how a device looks, keep it soft-focus
in the background rather than inventing detail.

Never include: any text, letters, numbers, labels, captions, watermarks, logos or brand names;
readable screens, monitors, charts, forms, name bands or medicine labels; needles entering
skin, blood, open wounds, or resuscitation maneuvers; real or recognizable individuals;
cartoon or flat-vector style; borders, frames or banners; a cropped circle.
```

## 2. Delivery

| Item | Specification |
|---|---|
| Master | 2048 x 2048 px PNG, sRGB, no transparency, white outside the circle |
| File name | exactly as given in each prompt (site convention `<page-slug>-vignette-hero.png`) |
| Where it goes | `images/` in the site repository |
| Derivatives | made by the site's own scripts after intake: WebP copy, 800 px phone copy, 1200 x 630 share card, 220 x 160 related-card thumbnail. Do not produce these. |
| Text in image | none (this differs from the atlas figures, which carry a footer; hero vignettes carry no text) |
| Language | any wording you write back to the team is in American English |

After intake, the site maintainer runs: `python3 generate_nursing_course.py --patch`, then `patch_responsive_images.py`, `patch_og_images.py` and `generate_rg_thumbs.py`. A module page shows no hero picture until its file exists, so images can arrive in any order.

## 3. Review before publication

Each image has a named reviewer type. Regenerate, do not retouch, if any of these appear: an impossible hand or limb; equipment that could not work or that implies a wrong technique (for example a blood-pressure cuff over clothing, a needle or tubing where the prompt forbids it, a catheter being handled without gloves or mask); readable or pseudo-readable text; a face that resembles a real public figure; a person repeated from another image; a patient shown in distress or undressed.

## 4. Module prompts

### Module 1 — Kidney Function and Renal Assessment

- **Module ID:** 01 (work ID `renal-nursing-01-renal-assessment`)
- **Final file name:** `nephrology-nursing-01-kidney-function-renal-assessment-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-01-kidney-function-renal-assessment`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show the two anchor measurements of renal assessment, weight and blood pressure, as calm, routine nursing work.
- **Alt text (already set on the page):** Nurse checks weight and blood pressure during a focused renal assessment.
- **Review:** Renal nurse educator

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: H (Clinical). Camera: environmental portrait at seated eye level, subject group left of center.

Scene: A Filipino registered nurse in plain teal scrubs wraps a blood-pressure cuff on the upper arm of a seated adult man in his sixties in a hospital ward bay. A column-type bedside weighing scale stands beside the chair.

Cast (unique to this image): Nurse: woman, late 20s, short bob, light-brown skin, teal scrubs. Patient: man, 60s, gray crew cut, medium-brown skin, loose plaid shirt.

Framing and focal point: The nurse’s hands positioning the cuff at heart level on the supported arm; the scale visible behind. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Bright Philippine hospital medical ward, curtain partition, daylight from a jalousie window.

Clinically significant details to get right: Cuff on bare upper arm, arm supported at heart level, patient seated with back supported and feet flat. Scale platform clear.

Do not show: No readable numbers on the monitor or scale, no intravenous pump displays, no name bands with text, no logos. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-01-kidney-function-renal-assessment-vignette-hero.png
```

### Module 2 — CKD Identification, Staging, and Progression

- **Module ID:** 02 (work ID `renal-nursing-02-ckd-staging`)
- **Final file name:** `nephrology-nursing-02-ckd-identification-staging-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-02-ckd-identification-staging`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show trend review as a shared activity between nurse and patient.
- **Alt text (already set on the page):** Nurse reviews kidney function and urine albumin trends with a patient.
- **Review:** Renal nurse educator

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: H (Clinical). Camera: over-the-shoulder view from behind the patient, looking toward the nurse and the shared page.

Scene: A Filipina nurse in her forties sits beside, not across from, a woman in her late fifties at an outpatient desk. The nurse points with a pen to a printed sheet of laboratory results lying between them; two small medicine boxes sit near the patient’s hand.

Cast (unique to this image): Nurse: woman, 40s, hair in a low bun, glasses, maroon scrub top. Patient: woman, late 50s, shoulder-length wavy hair, floral blouse.

Framing and focal point: The shared sheet and the two faces turned toward it. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Small Philippine outpatient clinic room, electric fan, wall calendar without readable text.

Clinically significant details to get right: Printed results shown as soft, unreadable rows; plain unbranded medicine boxes.

Do not show: No readable values, names, brand names, or hospital logos; no computer screen content. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-02-ckd-identification-staging-vignette-hero.png
```

### Module 3 — CKD Complications, Nutrition, and Medicines

- **Module ID:** 03 (work ID `renal-nursing-03-nutrition-counseling`)
- **Final file name:** `nephrology-nursing-03-ckd-complications-nutrition-medicines-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-03-ckd-complications-nutrition-medicines`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Present renal nutrition as individualized counseling built on familiar food.
- **Alt text (already set on the page):** Nurse and dietitian review a meal during renal nutrition counseling.
- **Review:** Renal dietitian and renal nurse educator

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: E (Lifestyle). Camera: three-quarter overhead view of the table, faces partly in frame.

Scene: A male Filipino renal nurse and a female dietitian sit with an older Filipino man at a small table. On the table is one ordinary home-style plate: a modest portion of rice, grilled fish, and sautéed vegetables. The dietitian gestures toward the plate with an open hand.

Cast (unique to this image): Nurse: man, 30s, stocky, navy scrubs. Dietitian: woman, 30s, long ponytail, white coat over a green top. Patient: man, 60s, thin, balding, light polo shirt.

Framing and focal point: The plate at the center with three people leaning in. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Counseling corner of a dialysis center or clinic, warm natural light.

Clinically significant details to get right: Realistic portion sizes; a glass of water; no food shown as forbidden or crossed out.

Do not show: No text, no red X marks, no food pyramid graphics, no branded packaging. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-03-ckd-complications-nutrition-medicines-vignette-hero.png
```

### Module 4 — AKI and Acute Kidney Support

- **Module ID:** 04 (work ID `renal-nursing-04-aki-escalation`)
- **Final file name:** `nephrology-nursing-04-aki-acute-kidney-support-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-04-aki-acute-kidney-support`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show escalation as a calm, practiced two-person action.
- **Alt text (already set on the page):** Hospital nurses assess a patient and make an urgent clinical handoff.
- **Review:** Critical care nurse and nephrologist

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: J (Environmental storytelling). Camera: wide-angle interior, sharp foreground figure, soft background action.

Scene: In an ICU bay, one Filipina nurse in the foreground speaks on a wall-mounted telephone while reading from a clipboard. Behind her, slightly out of focus, a male nurse leans over an older male patient in bed, hand on the patient’s wrist.

Cast (unique to this image): Foreground nurse: woman, 30s, tall, hair clipped up, light-blue scrubs. Background nurse: man, 40s, broad build. Patient: man, 70s, mostly out of focus.

Framing and focal point: The nurse on the phone, face composed and attentive. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Philippine tertiary hospital ICU, bedside monitor and infusion stands in soft focus.

Clinically significant details to get right: Monitor screen blurred to indistinct colored traces; urinary drainage bag hanging below bed level.

Do not show: No legible monitor values or waveforms, no drug labels, no visible distress or resuscitation maneuvers. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-04-aki-acute-kidney-support-vignette-hero.png
```

### Module 5 — Kidney Failure, Treatment Choices, and Conservative Care

- **Module ID:** 05 (work ID `renal-nursing-05-treatment-choices`)
- **Final file name:** `nephrology-nursing-05-kidney-failure-treatment-choices-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-05-kidney-failure-treatment-choices`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show an unhurried, eye-level conversation in which the family is included.
- **Alt text (already set on the page):** Patient and family discuss kidney failure treatment options with a nurse.
- **Review:** Renal nurse educator

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: H (Clinical). Camera: eye-level side profile of the three seated people.

Scene: An older Filipina woman sits beside her adult daughter on a bench-style sofa. A male nurse in his thirties sits on a low stool facing them at the same eye level, hands open and relaxed, with a closed folder on his lap.

Cast (unique to this image): Patient: woman, early 70s, silver hair in a bun, dark-brown skin, house dress and cardigan. Daughter: woman, 40s, market apron folded on her lap. Nurse: man, 30s, slim, gray scrubs.

Framing and focal point: The patient’s face as she speaks; the nurse listening. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Private consultation room in a Philippine provincial hospital, window with soft afternoon light, a potted plant.

Clinically significant details to get right: No one standing over the patient; daughter’s hand resting on her mother’s arm.

Do not show: No dialysis machines, no posters with text, no documents with readable content. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-05-kidney-failure-treatment-choices-vignette-hero.png
```

### Module 6 — HD Principles, Prescription, and Adequacy

- **Module ID:** 06 (work ID `renal-nursing-06-prescription-check`)
- **Final file name:** `nephrology-nursing-06-hd-principles-prescription-adequacy-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-06-hd-principles-prescription-adequacy`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show verification as a deliberate pause before treatment.
- **Alt text (already set on the page):** Nurse compares the dialysis prescription with a training machine before treatment.
- **Review:** Hemodialysis nurse educator and biomedical technician

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: H (Clinical). Camera: rear three-quarter view of the nurse, machine in soft focus beyond.

Scene: A Filipina nurse in navy scrubs stands at a hemodialysis machine in a training room, holding a clipboard in one hand and touching the edge of the machine with the other while her eyes move from paper to machine. The bloodlines hang neatly coiled and unconnected; the chair beside the machine is empty.

Cast (unique to this image): Nurse: woman, 50s, short graying hair, navy scrubs, seen from behind and to the side.

Framing and focal point: The nurse’s gaze moving between clipboard and machine. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Clean training bay of a Philippine dialysis center; daylight.

Clinically significant details to get right: Generic machine with a blank or softly glowing screen; dialyzer mounted but dry.

Do not show: No patient connected, no blood in lines, no readable screen values, labels, or manufacturer logos. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-06-hd-principles-prescription-adequacy-vignette-hero.png
```

> Diagram note for this module: A membrane or circuit diagram, if wanted, must be a clinician-approved vector layout with correct flow direction; use the house dialysis-circuit-schematic skill, not free image generation.

### Module 7 — HD Vascular Access and Infection Prevention

- **Module ID:** 07 (work ID `renal-nursing-07-fistula-assessment`)
- **Final file name:** `nephrology-nursing-07-hd-vascular-access-infection-prevention-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-07-hd-vascular-access-infection-prevention`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show the thirty-second examination that precedes every cannulation.
- **Alt text (already set on the page):** Nurse palpates a forearm fistula to check for a thrill.
- **Review:** Vascular access nurse and nephrologist

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: I (Object hero). Camera: macro, hands-only composition; no faces.

Scene: Close view of a nurse’s gloved fingertips resting lightly on the inner forearm of an adult patient, over a visibly enlarged vein. The patient’s arm rests palm-up on a chair armrest covered with a clean disposable sheet.

Cast (unique to this image): Nurse's hands in light-blue nitrile gloves; patient's forearm, medium-brown skin, adult man. No faces.

Framing and focal point: Fingertips on the forearm; skin intact and clean. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Dialysis chair, soft background blur.

Clinically significant details to get right: Bare forearm with a gently prominent, straight vein and two small healed needle marks; nurse’s other hand steadying the wrist.

Do not show: No needles, no tubing, no blood, no catheter, no tourniquet, no exaggerated aneurysm, no faces required. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-07-hd-vascular-access-infection-prevention-vignette-hero.png
```

### Module 8 — HD Equipment, Water, and Dialysate Safety

- **Module ID:** 08 (work ID `renal-nursing-08-water-room-log`)
- **Final file name:** `nephrology-nursing-08-hd-equipment-water-dialysate-safety-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-08-hd-equipment-water-dialysate-safety`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show the release step: a person reading the log before the day begins.
- **Alt text (already set on the page):** Dialysis staff member reviews the water-system monitoring log before treatment.
- **Review:** Dialysis water technician or biomedical engineer, and nephrologist

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: J (Environmental storytelling). Camera: wide-angle interior from the doorway, single figure at one-third.

Scene: A Filipino dialysis technician or nurse in scrubs stands in a compact water-treatment room holding an open logbook, pen poised, looking from the page toward a row of tall cylindrical tanks and a wall-mounted panel of gauges.

Cast (unique to this image): Technician: man, 20s, lean, cap worn backward, dark-green scrub top, rubber shoes.

Framing and focal point: The person and the open logbook; tanks behind. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Tiled water room in a Philippine dialysis center, pipes along the wall, a small sampling tap.

Clinically significant details to get right: Two matching tall tanks side by side suggesting carbon tanks in series; a small test kit on a shelf.

Do not show: No readable log entries, gauge numbers, or labels; no brand names; do not attempt to depict a technically complete treatment train. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-08-hd-equipment-water-dialysate-safety-vignette-hero.png
```

> Diagram note for this module: A treatment-train diagram must be built as reviewed site-native markup or a verified vector graphic; topology and sampling points require technical review.

### Module 9 — The Complete HD Session and Complication Response

- **Module ID:** 09 (work ID `renal-nursing-09-emergency-simulation`)
- **Final file name:** `nephrology-nursing-09-hd-session-complication-response-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-09-hd-session-complication-response`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show that emergency response is learned by rehearsal, as a team.
- **Alt text (already set on the page):** Dialysis nurses rehearse an urgent response at a simulation station.
- **Review:** Hemodialysis nurse educator and ACLS-certified nephrologist

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: J (Environmental storytelling). Camera: wide environmental shot from slightly above, team arranged in an arc.

Scene: Three Filipino dialysis nurses of different ages gather around a training mannequin reclined in a dialysis chair. One kneels at the mannequin’s side, one stands at an unpowered dialysis machine, and one holds a clipboard as the trainer, observing.

Cast (unique to this image): Three nurses: woman in her 20s with a braid, man in his 40s with glasses, woman in her 50s as trainer; mixed scrub colors.

Framing and focal point: The team’s coordinated posture around the mannequin. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Simulation bay or quiet corner of a dialysis unit after hours; an emergency cart visible in the background.

Clinically significant details to get right: Mannequin clearly artificial; machine screen dark; lines unconnected.

Do not show: No real patient, no blood, no depiction of chest compressions or other specific maneuvers, no readable text on the cart or clipboard. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-09-hd-session-complication-response-vignette-hero.png
```

### Module 10 — PD and Home Dialysis Nursing

- **Module ID:** 10 (work ID `renal-nursing-10-pd-home-teaching`)
- **Final file name:** `nephrology-nursing-10-pd-home-dialysis-nursing-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-10-pd-home-dialysis-nursing`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show PD as home-based care that depends on a prepared space and patient teaching.
- **Alt text (already set on the page):** Nurse teaches a patient to prepare a clean space for home peritoneal dialysis.
- **Review:** Peritoneal dialysis nurse

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: E (Lifestyle). Camera: environmental portrait from the doorway of the room.

Scene: In a modest Filipino home, a female nurse and a middle-aged male patient stand at a small wiped-down table near a window. Sealed, unopened dialysis solution bags in plain packaging and a box of supplies sit on the table; the nurse gestures toward the cleared surface while the patient looks on, hands clasped.

Cast (unique to this image): Nurse: woman, 30s, curly hair tied back, white community-nurse uniform. Patient: man, mid-60s, heavyset, sleeveless undershirt under an open short-sleeved shirt.

Framing and focal point: The clean table surface and the two people facing it. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Bedroom or sala corner with wooden furniture, a wall hook, a closed window with light curtains; cardboard supply boxes stacked on a low shelf off the floor.

Clinically significant details to get right: All supplies sealed; a bottle of hand rub; a face mask on the table.

Do not show: No catheter visible, no open bags or tubing, no exchange in progress, no brand names or readable labels, no pets. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-10-pd-home-dialysis-nursing-vignette-hero.png
```

### Module 11 — Transplantation and Special Populations

- **Module ID:** 11 (work ID `renal-nursing-11-transplant-followup`)
- **Final file name:** `nephrology-nursing-11-transplantation-special-populations-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-11-transplantation-special-populations`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show medicine teaching as the core of long-term transplant nursing.
- **Alt text (already set on the page):** Transplant nurse reviews the medication schedule with a patient.
- **Review:** Transplant nurse coordinator

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: H (Clinical). Camera: overhead, hands-and-table composition; faces out of frame or cropped at the chin.

Scene: A Filipina transplant nurse and a man in his forties sit at a clinic desk. Between them is a weekly pill organizer with compartments and a plain printed schedule grid; the nurse indicates one compartment while the patient holds a small notebook.

Cast (unique to this image): Nurse's hands (woman, no gloves, plain watch) and patient's hands (man, 40s, wedding ring). Faces not shown.

Framing and focal point: The pill organizer and the two pairs of hands. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Outpatient transplant clinic room, calm and uncluttered.

Clinically significant details to get right: Pill organizer with generic tablets; schedule shown as an unreadable grid.

Do not show: No drug names, brand packaging, readable schedule text, or laboratory values. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-11-transplantation-special-populations-vignette-hero.png
```

### Module 12 — Philippine Practice, Quality Improvement, and Capstone

- **Module ID:** 12 (work ID `renal-nursing-12-quality-huddle`)
- **Final file name:** `nephrology-nursing-12-philippine-practice-quality-capstone-vignette-hero.png`
- **Placement:** hero circular vignette on `/guides/nephrology-nursing-12-philippine-practice-quality-capstone`, to the right of the title on desktop, above it on phones
- **Learning purpose:** Show quality improvement as a routine team conversation.
- **Alt text (already set on the page):** A dialysis team reviews a unit quality audit during a staff huddle.
- **Review:** Head nurse or quality officer

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: J (Environmental storytelling). Camera: side profile of a standing group, speaker facing left.

Scene: Five members of a Philippine dialysis team (nurses, a technician, a physician) stand in a loose half-circle at the nurses’ station. One nurse holds a clipboard and speaks; behind them a whiteboard shows a simple hand-drawn line chart with no legible labels.

Cast (unique to this image): Five staff: head nurse (woman, 50s), two staff nurses (man 20s, woman 30s), technician (man, 40s), physician (woman, 40s, white coat).

Framing and focal point: The speaking nurse and the attentive group. The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: Nurses’ station of a dialysis unit before the first shift; chairs and machines idle in the background.

Clinically significant details to get right: Mixed ages and sexes; relaxed, attentive posture; chart drawn as abstract rising dots.

Do not show: No readable chart values, names, patient information, logos, or patients. Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: nephrology-nursing-12-philippine-practice-quality-capstone-vignette-hero.png
```

## Asset manifest (summary)

The machine-readable version is `image-manifest.json` beside this file.

| Module | Final file name | Alt text | Reviewer |
|---|---|---|---|
| 1 | `nephrology-nursing-01-kidney-function-renal-assessment-vignette-hero.png` | Nurse checks weight and blood pressure during a focused renal assessment. | Renal nurse educator |
| 2 | `nephrology-nursing-02-ckd-identification-staging-vignette-hero.png` | Nurse reviews kidney function and urine albumin trends with a patient. | Renal nurse educator |
| 3 | `nephrology-nursing-03-ckd-complications-nutrition-medicines-vignette-hero.png` | Nurse and dietitian review a meal during renal nutrition counseling. | Renal dietitian and renal nurse educator |
| 4 | `nephrology-nursing-04-aki-acute-kidney-support-vignette-hero.png` | Hospital nurses assess a patient and make an urgent clinical handoff. | Critical care nurse and nephrologist |
| 5 | `nephrology-nursing-05-kidney-failure-treatment-choices-vignette-hero.png` | Patient and family discuss kidney failure treatment options with a nurse. | Renal nurse educator |
| 6 | `nephrology-nursing-06-hd-principles-prescription-adequacy-vignette-hero.png` | Nurse compares the dialysis prescription with a training machine before treatment. | Hemodialysis nurse educator and biomedical technician |
| 7 | `nephrology-nursing-07-hd-vascular-access-infection-prevention-vignette-hero.png` | Nurse palpates a forearm fistula to check for a thrill. | Vascular access nurse and nephrologist |
| 8 | `nephrology-nursing-08-hd-equipment-water-dialysate-safety-vignette-hero.png` | Dialysis staff member reviews the water-system monitoring log before treatment. | Dialysis water technician or biomedical engineer, and nephrologist |
| 9 | `nephrology-nursing-09-hd-session-complication-response-vignette-hero.png` | Dialysis nurses rehearse an urgent response at a simulation station. | Hemodialysis nurse educator and ACLS-certified nephrologist |
| 10 | `nephrology-nursing-10-pd-home-dialysis-nursing-vignette-hero.png` | Nurse teaches a patient to prepare a clean space for home peritoneal dialysis. | Peritoneal dialysis nurse |
| 11 | `nephrology-nursing-11-transplantation-special-populations-vignette-hero.png` | Transplant nurse reviews the medication schedule with a patient. | Transplant nurse coordinator |
| 12 | `nephrology-nursing-12-philippine-practice-quality-capstone-vignette-hero.png` | A dialysis team reviews a unit quality audit during a staff huddle. | Head nurse or quality officer |


## 5. Instructional diagrams (separate track — do not generate freely)

These are teaching diagrams whose labels, directions and numbers must be correct. They are built as reviewed vector graphics or site-native HTML, with every label authored as real text on the page. An image generator must not be asked to render machine settings, numeric values, labels or procedural steps.

| Module | Diagram | How it is produced | Must be verified by |
|---|---|---|---|
| 6 | Dialyzer transport: blood and dialysate in countercurrent flow; diffusion of urea and potassium out and bicarbonate in; ultrafiltration of water by pressure | The house `dialysis-circuit-schematic` skill, which fixes port colors, flow directions and pressure points; labels in HTML beside the figure | Hemodialysis nurse educator and nephrologist |
| 6 | Extracorporeal circuit overview: arterial needle, blood pump, dialyzer, venous chamber and air detector, venous needle | Same skill; no numeric settings in the image | Hemodialysis nurse educator and biomedical technician |
| 8 | Water treatment train: feed water, sediment filter, softener, two carbon tanks in series, reverse osmosis, distribution loop, machine; with the total-chlorine sampling point after the carbon tanks | Site-native markup (an ordered flow built in HTML and CSS) or a verified vector; topology and sampling points must match the unit being taught, and the caption must say it is an example layout | Dialysis water technician or biomedical engineer, and nephrologist |

The tables of limits, schedules and first actions in Modules 2, 4, 6, 8 and 9 already exist as accessible HTML on the pages and must stay as HTML.
