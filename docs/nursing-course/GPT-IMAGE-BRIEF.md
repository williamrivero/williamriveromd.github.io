# GPT image production brief — Nephrology Nursing & Hemodialysis (17 module heroes)

**For:** a GPT image-generation session. This file is complete on its own; you do not need the website repository or any earlier conversation.
**Site:** Renal Care Matters (renalcarematters.com), a free kidney-health education library for Filipino patients and clinicians.
**What you are making:** one hero picture for each of 17 nursing-education modules. Each picture sits inside a circular frame beside the page title.
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
across all images so they read as a set.

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

### Module 13 — Convective Therapies: CRRT and Hemodiafiltration

*(Scene: The ICU nurse and the hanging bags. Copied from GPT-IMAGE-PROMPTS-ADDENDUM-M13.md; keep the two in step.)*

- **File:** images/nephrology-nursing-13-convective-therapies-crrt-hdf-vignette-hero.png
- **Placement:** Module 13 hero circular vignette (`figure.hero-figure > .hero-vignette`)
- **Job:** P — the learner sees continuous therapy as calm, exacting bedside work: the bags the nurse checks are, in the module's words, an intravenous medicine.
- **Governing skill:** williamriveromd-hero-vignette v3 (Scaffold A, Clinical People Scene)
- **Canvas:** 2048 × 2048, 1:1
- **Alt text:** ICU nurse checks the hanging fluid bags on a continuous kidney therapy machine beside a sedated, ventilated patient.
- **Caption:** none (hero vignette; the page title sits beside it).
- **Source of truth:** ADDENDUM-PLAN.md 13-H0; m13.py `bedside` (replacement fluid is an intravenous medicine; check every bag; never lean on or touch the scales); m13_x.py `crrt-modes` (machines weigh each bag on integrated scales; runs around the clock in the ICU) and `crrt-fluid` (bags must hang freely); m13.py case (ICU, septic shock, night shift). docs/nursing-course/GPT-IMAGE-BRIEF.md casts and cameras checked so none is repeated. No clinical values.
- **Reviewer flags:** (1) m13.py `image.alt` currently reads "An ICU nurse checks a continuous therapy machine beside a patient while a dialysis nurse reviews a hemodiafiltration session" (two settings); this hero shows the ICU only, per the addendum plan, so the page alt text should be updated to the alt text above, or the hero re-briefed. (2) Confirm the cast differs from all 12 module heroes and the hub hero H-0 (Module 4 is already an ICU scene: tall woman in light-blue scrubs on a wall phone; this one is a different nurse, angle, and action). (3) Confirm no blood is visible in any line.

```text
Square 1:1 photorealistic documentary-style editorial photograph on a 2048 × 2048 canvas, composed to be displayed inside a CIRCULAR vignette that fills 85–90% of the canvas diameter, with a visible plain WHITE margin all the way around. The circle never touches the canvas edge, and nothing important touches the circle's edge. Composition archetype: I (Object Hero), with the nurse engaged with the object. Camera: low three-quarter angle from slightly below bag height, looking up past the hanging fluid bags toward the nurse's face in three-quarter profile. Shallow depth of field.

SCENE
Night shift in a bright, calm Philippine tertiary-hospital intensive care unit. A Filipino ICU nurse stands beside a generic, unbranded continuous kidney-therapy machine: a tall upright console on wheels with four large, clear, soft plastic fluid bags hanging freely from hooks on its lower sides, each bag resting in its own integrated weighing cradle. Clear fluid lines run from the bags into the console. The nurse holds a small printed order sheet (unreadable, soft rows only) in one hand and, with the other, steadies nothing: her fingertip points at one bag's label area without touching the bag or the scale, as she compares the bag against the order. Her expression is calm, focused, unhurried. In the soft-focus background lies a sedated adult patient on a ventilator: a woman in her late fifties, eyes closed, sheet folded neatly at the chest, a ventilator tube at the mouth, peaceful and dignified, mostly out of focus.

CAST (unique to this image; must not resemble any other image in the series)
- ICU nurse (hero subject): woman, mid-40s, full-figured build, round face with high cheekbones, light olive-brown skin, black hair braided into a neat crown under a pale-blue disposable bouffant cap, thick straight eyebrows, small reading glasses pushed up onto the cap, royal-blue scrub top over a long-sleeved white undershirt, sleeves pushed to the forearm, plain black wristwatch, surgical mask lowered under the chin.
- Patient (background, soft focus): woman, late 50s, short graying hair against the pillow, medium-brown skin.
Closed shoes; no logos on clothing.

SETTING
ICU bed space with a glass sliding door, pale walls, soft indirect ceiling light mixed with cool dawn light from a window. A bedside monitor and an infusion pump stand in soft background blur; their screens are dark or an indistinct soft glow with nothing readable. The machine's own screen faces away from the camera.

VISUAL HIERARCHY
The hanging bags, the machine's side, and the nurse's face and pointing hand occupy 60–70% of the circle, right of center. The sedated patient and ICU background form 20–30%. Reserve the LEFT 20–25% of the circle as a calm TITLE-SAFE ZONE of soft-focus pale wall and window light, with no faces, hands, equipment, or objects in it.

STYLE
Bright, airy, natural light; gentle color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, renal green #1f7a4d, and warm neutrals; one consistent grade with the other module heroes. Correct hands with five fingers; plausible, generic equipment.

ABSOLUTELY NO TEXT: no title, caption, label, logo, watermark, brand name, readable screen, readable bag label, readable order sheet, readable name badge, or any letters or numbers anywhere.

NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermark of any kind (including no renalcarematters.com mark)
✗ No readable machine screen, monitor, pump display, bag label, or order sheet
✗ No blood visible in any line, no red or dark tubing in the foreground, no needles, no open wounds
✗ No nurse touching, leaning on, or holding a bag or scale (the scales must hang free)
✗ No telephone, no clipboard-and-phone pose, no wide ICU escalation scene (another image already shows this)
✗ No resuscitation, no distress, no alarms, no crowd of staff; exactly one nurse and one patient
✗ No patient face in sharp focus; no exposed body; patient covered to the chest
✗ No dark, moody, charcoal, or high-contrast lighting; no HDR, neon, or oversaturation
✗ No cartoon or flat-vector style; no rectangular border, frame, or banner
✗ No cropped circle; no subject touching or crossing the circle's edge
✗ No faces, hands, or objects inside the left title-safe zone
✗ No distorted hands or faces; no branded or real-model equipment

Render no text of any kind; the image must be completely wordless.
```

**QA after generation:**
□ Square 2048 × 2048; circle fills 85–90% with an even white margin; circle not cropped
□ Absolutely no text, letters, numbers, logos, or watermark anywhere (heroes carry no footer)
□ Hanging bags and the nurse's face are the clear focal point, right of center; left 20–25% is empty soft wall or window light
□ Bags hang freely in their cradles; the nurse's hand does not touch a bag or a scale
□ Nurse is a full-figured woman in her mid-40s in royal-blue scrubs with braided crown and bouffant cap; she resembles no person in the 12 module heroes or H-0 (compare side by side)
□ Patient is sedated and ventilated, calm, covered, soft-focus; exactly two people
□ No blood visible; no needles; no telephone or escalation scene
□ Machine screen faces away; monitor and pump screens unreadable; order sheet unreadable
□ Hands have five fingers; equipment generic and unbranded
□ Light, bright color grade consistent with the module heroes; no dark background

---

### Module 14 — Living Well on Hemodialysis: Mind, Behavior, and Longevity

*(Scene: Listening at the chair. Copied from GPT-IMAGE-PROMPTS-ADDENDUM-2.md; keep the two in step.)*

- **File:** images/nephrology-nursing-14-living-well-hemodialysis-vignette-hero.png
- **Placement:** Module 14 hero circular vignette (`figure.hero-figure > .hero-vignette`)
- **Job:** P — the learner sees mental health care in the dialysis unit as attentive, private, unhurried conversation at the chair.
- **Governing skill:** williamriveromd-hero-vignette v3 (Scaffold A, Clinical People Scene)
- **Canvas:** 2048 × 2048, 1:1
- **Alt text:** A dialysis nurse sits at eye level beside a middle-aged Filipino patient during treatment, listening attentively while a family member sits nearby.
- **Caption:** none (hero vignette; the page title sits beside it).
- **Source of truth:** m14.py `image` (work ID `renal-nursing-14-living-well`; alt and purpose used verbatim); m14.py `bedside` (ask in private, lower your voice, choose a quiet moment early in the session, listen without hurrying to reassure; involve the family with consent). No clinical values.
- **Reviewer flags:** (1) The Module 16 hero brief is similar (nurse at eye level, family nearby); this hero is told apart by a male nurse, a middle-aged male patient, a seated-forward listening pose with no touch, and a side camera; 16-H0 uses an older woman, hand-holding, and a frontal camera. Compare the two side by side. (2) Confirm the cast differs from the 13 earlier heroes and H-0. (3) Confirm no needles or blood are visible at the access arm.
- **Attach when generating:** not applicable

```text
Square 1:1 photorealistic documentary-style editorial photograph on a 2048 × 2048 canvas, composed to be displayed inside a CIRCULAR vignette that fills 85–90% of the canvas diameter, with a visible plain WHITE margin all the way around. The circle never touches the canvas edge, and nothing important touches the circle's edge. Composition archetype: H (Clinical, conversation). Camera: side view at seated eye level, slightly behind the patient's shoulder, so both faces are seen in three-quarter profile. Shallow depth of field.

SCENE
Mid-morning in a bright, calm Philippine outpatient hemodialysis unit. A Filipino dialysis nurse has pulled a low stool beside a reclining dialysis chair and sits at the patient's eye level, leaning slightly forward, forearms resting on his knees, hands loosely clasped, listening. The patient, a middle-aged man in the reclining chair, is mid-sentence, looking at the nurse; his expression is thoughtful and a little tired, not distressed. His left forearm rests on a pillow, covered from wrist to elbow by a folded light blanket, so no access, needle, or tubing is visible. A generic dialysis machine stands behind the chair in soft focus, its screen turned away. A privacy curtain is half drawn on the far side. Sitting on a plastic chair at the foot of the reclining chair, slightly out of focus, his wife listens quietly with her hands folded on a small cloth bag.

CAST (unique to this image; must not resemble any other image in the series)
- Nurse (hero subject): man, early 40s, lean build, close-cropped black hair with a light beard shadow, warm medium-brown skin, plum-colored scrub top over a white long-sleeved undershirt, plain black wristwatch, no mask.
- Patient: man, early 50s, medium build, short black hair graying at the temples, a thin mustache, dark-brown skin, gray zip-up jacket over a plain dark T-shirt.
- Wife (soft focus): woman, late 40s, round face, light-brown skin, hair held back in a clip, pale-yellow blouse.
Closed shoes; no logos on clothing.

SETTING
Pale walls, a wide window with soft daylight behind the curtain, other chairs in deep background blur with no faces in focus. The machine screen and any monitor face away or show only an indistinct soft glow.

VISUAL HIERARCHY
The nurse's attentive face and clasped hands and the patient's face occupy 60–70% of the circle, right of center. The wife and unit background form 20–30%. Reserve the LEFT 20–25% of the circle as a calm TITLE-SAFE ZONE of soft-focus window light and pale wall, with no faces, hands, equipment, or objects in it.

STYLE
Bright, airy, natural light; gentle color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, renal green #1f7a4d, and warm neutrals; one consistent grade with the other module heroes. Correct hands with five fingers; plausible, generic equipment.

ABSOLUTELY NO TEXT: no title, caption, label, logo, watermark, brand name, readable screen, readable chart, readable name badge, or any letters or numbers anywhere.

NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermark of any kind (including no renalcarematters.com mark)
✗ No needles, no visible blood, no visible tubing at the patient's arm, no open wounds
✗ No nurse standing over the patient, writing on a clipboard, or looking at a screen; the nurse is listening
✗ No crying, despair, anger, or distress on any face; no clinical emergency
✗ No touching between nurse and patient (that pose belongs to another image)
✗ No crowd of staff; exactly three people in focus range
✗ No dark, moody, or high-contrast lighting; no HDR, neon, or oversaturation
✗ No cartoon or flat-vector style; no rectangular border, frame, or banner
✗ No cropped circle; no subject touching or crossing the circle's edge
✗ No faces, hands, or objects inside the left title-safe zone
✗ No distorted hands or faces; no branded or real-model equipment

Render no text of any kind; the image must be completely wordless.
```

**QA after generation:**
□ Square 2048 × 2048; circle fills 85–90% with an even white margin; circle not cropped
□ Absolutely no text, letters, numbers, logos, or watermark anywhere (heroes carry no footer)
□ Nurse seated at the patient's eye level, leaning in, listening; faces of nurse and patient are the focal point, right of center
□ Left 20–25% of the circle is empty soft window light or wall
□ No needles, tubing, or blood visible at the covered forearm
□ Nurse is a lean man in his early 40s in a plum scrub top; patient a man in his early 50s with a mustache and gray jacket; wife in soft focus; none resembles a person in the other heroes (compare side by side, especially with 16-H0)
□ Calm, unhurried mood; no distress
□ Machine screen faces away; nothing readable
□ Hands have five fingers; equipment generic and unbranded
□ Light, bright color grade consistent with the module heroes; no dark background

---

### Module 15 — Glomerular and Systemic Kidney Diseases

*(Scene: The morning weight. Copied from GPT-IMAGE-PROMPTS-ADDENDUM-2.md; keep the two in step.)*

- **File:** images/nephrology-nursing-15-glomerular-systemic-kidney-disease-vignette-hero.png
- **Placement:** Module 15 hero circular vignette (`figure.hero-figure > .hero-vignette`)
- **Job:** P — the learner sees the routine checks that track a leaking or inflamed glomerulus (daily weight, edema, urine testing, careful charting) as calm, skilled nursing.
- **Governing skill:** williamriveromd-hero-vignette v3 (Scaffold A, Clinical People Scene)
- **Canvas:** 2048 × 2048, 1:1
- **Alt text:** A ward nurse weighs a patient with swollen legs on a bedside scale at the start of the morning, with a urine dipstick and a chart on the trolley beside her.
- **Caption:** none (hero vignette; the page title sits beside it).
- **Source of truth:** m15.py `image` (work ID `renal-nursing-15-glomerular`; alt and purpose verbatim); m15.py `bedside` (daily weight: same scale, same time in the morning after voiding and before breakfast, same clothing; edema check; urine dipstick read at the stated time). No clinical values.
- **Reviewer flags:** (1) Module 1's hero also shows a weighing scale (column scale beside a seated man having his blood pressure taken); this hero differs in action (patient standing on the scale), ward, camera, and cast. Confirm they read as different scenes. (2) Edema must be visible but not grotesque.
- **Attach when generating:** not applicable

```text
Square 1:1 photorealistic documentary-style editorial photograph on a 2048 × 2048 canvas, composed to be displayed inside a CIRCULAR vignette that fills 85–90% of the canvas diameter, with a visible plain WHITE margin all the way around. The circle never touches the canvas edge, and nothing important touches the circle's edge. Composition archetype: H (Clinical). Camera: low three-quarter angle at about knee-to-waist height, looking slightly up, so the scale platform, the patient's swollen ankles, and the nurse's face are all in frame. Shallow depth of field.

SCENE
Early morning in a bright Philippine hospital medical ward, soft dawn light through a jalousie window. A Filipino ward nurse stands beside a generic flat digital floor scale placed next to the bed. A young adult patient stands on the scale in hospital-issue loose shorts and a short-sleeved patient top, one hand lightly on the nurse's offered forearm for balance. Both of his lower legs and ankles are visibly puffy with smooth, slightly shiny skin (edema), shown matter-of-factly, not exaggerated. The nurse looks down at the scale display area (which faces away from the camera) with calm attention. Beside her stands a small stainless steel trolley holding a closed plastic urine-sample cup, a capped plastic tube of urine test strips with no readable label, and a closed chart folder.

CAST (unique to this image; must not resemble any other image in the series)
- Ward nurse (hero subject): woman, early 30s, slender, straight black shoulder-length hair tucked behind her ears under no cap, oval face, fair-olive skin, renal-green scrub top with a white undershirt, small stud earrings, no mask.
- Patient: man, late 20s, slim, buzz-cut hair, medium-brown skin, slightly puffy eyelids, relaxed and cooperative expression.
Rubber hospital slippers on the patient set neatly beside the scale (he stands barefoot); closed shoes on the nurse; no logos on clothing.

SETTING
Ward bay with a white bed, a privacy curtain partly drawn, pale walls, an empty IV pole in soft background. No other patients in focus.

VISUAL HIERARCHY
The nurse's face, the patient's swollen ankles on the scale, and the trolley occupy 60–70% of the circle, right of center. The ward background forms 20–30%. Reserve the LEFT 20–25% of the circle as a calm TITLE-SAFE ZONE of soft window light and curtain, with no faces, hands, equipment, or objects in it.

STYLE
Bright, airy, natural light; gentle color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, renal green #1f7a4d, and warm neutrals; one consistent grade with the other module heroes. Correct hands and feet with five digits; plausible, generic equipment.

ABSOLUTELY NO TEXT: no title, caption, label, logo, watermark, brand name, readable scale display, readable test-strip tube, readable chart, readable name badge, or any letters or numbers anywhere.

NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermark of any kind (including no renalcarematters.com mark)
✗ No readable scale reading, strip color chart, or chart page
✗ No blood, needles, IV lines in the patient, open wounds, or skin breakdown
✗ No exaggerated or grotesque swelling; no exposed torso; patient decently dressed
✗ No blood-pressure cuff, no seated patient (another image already shows that)
✗ No dark, moody, or high-contrast lighting; no HDR, neon, or oversaturation
✗ No cartoon or flat-vector style; no rectangular border, frame, or banner
✗ No cropped circle; no subject touching or crossing the circle's edge
✗ No faces, hands, or objects inside the left title-safe zone
✗ No distorted hands, feet, or faces; no branded or real-model equipment

Render no text of any kind; the image must be completely wordless.
```

**QA after generation:**
□ Square 2048 × 2048; circle fills 85–90% with an even white margin; circle not cropped
□ Absolutely no text, letters, numbers, logos, or watermark anywhere
□ Patient standing on a floor scale; both ankles visibly but realistically swollen
□ Trolley shows a closed sample cup, a strip tube with no readable label, and a closed chart
□ Scale display faces away or is unreadable
□ Nurse is a slender woman in her early 30s in a renal-green scrub top; patient a slim man in his late 20s; neither resembles a person in the other heroes
□ Left 20–25% of the circle empty
□ No blood, needles, or blood-pressure cuff
□ Hands and feet have five digits; equipment generic
□ Light, bright color grade consistent with the module heroes

---

### Module 16 — Supportive, Palliative, and End-of-Life Kidney Care

*(Scene: Present at the chair. Copied from GPT-IMAGE-PROMPTS-ADDENDUM-2.md; keep the two in step.)*

- **File:** images/nephrology-nursing-16-supportive-palliative-kidney-care-vignette-hero.png
- **Placement:** Module 16 hero circular vignette (`figure.hero-figure > .hero-vignette`)
- **Job:** P — the learner sees supportive care as unhurried, present, family-centered nursing at the dialysis chair, not only at the deathbed.
- **Governing skill:** williamriveromd-hero-vignette v3 (Scaffold A, Clinical People Scene)
- **Canvas:** 2048 × 2048, 1:1
- **Alt text:** A dialysis nurse sits at eye level beside an older Filipino patient in a reclining chair, holding her hand while a family member listens.
- **Caption:** none (hero vignette; the page title sits beside it).
- **Source of truth:** m16.py `image` (work ID `renal-nursing-16-palliative`; alt and purpose verbatim); m16.py `model` (supportive care runs alongside every treatment, starts at diagnosis); m16.py `bedside` ("Not changing the subject is itself care"). No clinical values.
- **Reviewer flags:** (1) Compare with 14-H0 (similar brief): this one uses an older woman, a female nurse, hand-holding, and a frontal camera. (2) Confirm the mood reads as warm and alive, not as end of life; the patient is awake, on treatment, and engaged.
- **Attach when generating:** not applicable

```text
Square 1:1 photorealistic documentary-style editorial photograph on a 2048 × 2048 canvas, composed to be displayed inside a CIRCULAR vignette that fills 85–90% of the canvas diameter, with a visible plain WHITE margin all the way around. The circle never touches the canvas edge, and nothing important touches the circle's edge. Composition archetype: H (Clinical, connection). Camera: frontal, slightly to one side, at seated eye level, about two meters away, framing the patient, the nurse, and the joined hands. Shallow depth of field.

SCENE
Late morning in a bright, quiet Philippine outpatient hemodialysis unit. An older Filipino woman rests in a reclining dialysis chair with a soft knitted blanket over her lap and legs; she is awake, calm, and looking at the nurse with a faint, tired smile. A Filipino dialysis nurse sits on a low stool beside her, at her eye level, and holds the patient's right hand gently in both of hers, listening. The patient's left (access) arm lies on a pillow on the far side, covered by the blanket, so no needle, tubing, or blood is visible. The patient's adult son sits on a chair just behind the nurse's shoulder, slightly out of focus, leaning forward to listen, hands clasped. A small wooden rosary rests loosely on the blanket. A generic dialysis machine in soft background focus, screen turned away.

CAST (unique to this image; must not resemble any other image in the series)
- Nurse (hero subject): woman, late 50s, warm brown skin, short silver-streaked hair in a neat pixie cut, laugh lines, dusty-rose scrub top over a white undershirt, a simple watch, no mask.
- Patient: woman, about 80, slight and thin, white hair cropped short, deeply lined light-brown skin, a pale lavender house dress, small gold earrings.
- Son (soft focus): man, early 50s, rectangular glasses, receding hairline, navy polo shirt.
Closed shoes; no logos on clothing.

SETTING
Pale walls, soft daylight from a window behind sheer curtains, a potted plant on a side table, other chairs in deep background blur with no faces in focus.

VISUAL HIERARCHY
The joined hands and the faces of the patient and nurse occupy 60–70% of the circle, right of center. The son and unit background form 20–30%. Reserve the LEFT 20–25% of the circle as a calm TITLE-SAFE ZONE of soft window light and pale wall, with no faces, hands, equipment, or objects in it.

STYLE
Bright, warm, natural light; gentle color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, renal green #1f7a4d, and warm neutrals; one consistent grade with the other module heroes. Correct hands with five fingers; plausible, generic equipment.

ABSOLUTELY NO TEXT: no title, caption, label, logo, watermark, brand name, readable screen, readable chart, readable name badge, or any letters or numbers anywhere.

NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermark of any kind (including no renalcarematters.com mark)
✗ No deathbed, hospital bed, oxygen mask, candles, flowers arranged as a memorial, or dark room
✗ No crying, grief, or distress on any face; the patient is awake and engaged
✗ No needles, no visible blood, no visible tubing at the patient's arm
✗ No priest, religious ceremony, or anointing scene
✗ No crowd of staff; exactly three people in focus range
✗ No dark, moody, or high-contrast lighting; no HDR, neon, or oversaturation
✗ No cartoon or flat-vector style; no rectangular border, frame, or banner
✗ No cropped circle; no subject touching or crossing the circle's edge
✗ No faces, hands, or objects inside the left title-safe zone
✗ No distorted hands or faces; no branded or real-model equipment

Render no text of any kind; the image must be completely wordless.
```

**QA after generation:**
□ Square 2048 × 2048; circle fills 85–90% with an even white margin; circle not cropped
□ Absolutely no text, letters, numbers, logos, or watermark anywhere
□ Nurse seated at eye level holding the patient's hand; patient awake and calm
□ Son in soft focus listening; exactly three people in focus range
□ No end-of-life imagery: no bed, oxygen, candles, or grief
□ No needles, tubing, or blood at the covered access arm
□ Nurse is a woman in her late 50s with silver-streaked pixie hair and a dusty-rose scrub top; patient a woman about 80; neither resembles anyone in the other heroes, especially 14-H0
□ Left 20–25% of the circle empty
□ Hands have five fingers; equipment generic
□ Light, warm color grade consistent with the module heroes

---

### Module 17 — Patient Teaching, Health Literacy, and Evidence-Based Practice

*(Scene: The marked bottle. Copied from GPT-IMAGE-PROMPTS-ADDENDUM-2.md; keep the two in step.)*

- **File:** images/nephrology-nursing-17-teaching-evidence-based-practice-vignette-hero.png
- **Placement:** Module 17 hero circular vignette (`figure.hero-figure > .hero-vignette`)
- **Job:** P — the learner sees teaching at the dialysis chair as an unhurried, respectful conversation that includes the family and uses a real object.
- **Governing skill:** williamriveromd-hero-vignette v3 (Scaffold A, Clinical People Scene; archetype I, object hero)
- **Canvas:** 2048 × 2048, 1:1
- **Alt text:** A dialysis nurse sits beside a patient in a treatment chair, showing him a marked water bottle while his wife watches and listens.
- **Caption:** none (hero vignette; the page title sits beside it).
- **Source of truth:** m17.py `image` (work ID `renal-nursing-17-teaching`; alt and purpose verbatim); m17_x.py `literacy` (turn amounts into household objects the patient owns: their own glass, a marked bottle); m17.py `bedside` (show, then let them show; include the family the patient chooses; lower your voice). No clinical values.
- **Reviewer flags:** (1) The bottle must carry plain marks (lines) but no numbers or words. (2) Module 3's hero is a food-teaching scene with a dietitian; confirm this reads as a different scene and cast.
- **Attach when generating:** not applicable

```text
Square 1:1 photorealistic documentary-style editorial photograph on a 2048 × 2048 canvas, composed to be displayed inside a CIRCULAR vignette that fills 85–90% of the canvas diameter, with a visible plain WHITE margin all the way around. The circle never touches the canvas edge, and nothing important touches the circle's edge. Composition archetype: I (Object Hero) with the people engaged with the object. Camera: over-the-nurse's-shoulder three-quarter view at seated eye level, the bottle sharp in the mid-ground, the patient's and wife's faces just beyond it. Shallow depth of field.

SCENE
Early afternoon in a bright Philippine outpatient hemodialysis unit. A Filipino dialysis nurse sits on a stool beside a reclining treatment chair and holds up a clear one-liter plastic water bottle with three or four plain horizontal lines drawn on it in dark marker (lines only, no numbers or words), pointing with one finger to the top line. The patient, a man in the chair, leans slightly forward, looking at the bottle with interest and a small, engaged half-smile, as if about to answer a question. His wife sits on a chair at his side, holding a small closed notebook in her lap, watching the bottle and listening. The patient's access arm rests on a pillow on the far side, covered by a light blanket; no needles, tubing, or blood visible. A generic dialysis machine stands behind in soft focus with its screen turned away.

CAST (unique to this image; must not resemble any other image in the series)
- Nurse (seen mostly from behind and the side; face in partial profile): man, late 20s, tall and slim, wavy black hair, light-brown skin, olive-green scrub top, a plain silver ring.
- Patient: man, mid-60s, heavy build, bald crown with short gray hair at the sides, square eyeglasses, medium-brown skin, white undershirt under an open short-sleeved chambray shirt.
- Wife: woman, early 60s, short permed graying hair, round glasses on a cord, warm dark-brown skin, pink blouse.
Closed shoes; no logos on clothing.

SETTING
Pale walls, daylight from a side window, a curtain partly drawn for privacy, other chairs in deep background blur with no faces in focus.

VISUAL HIERARCHY
The bottle, the nurse's pointing hand, and the patient's and wife's faces occupy 60–70% of the circle, right of center. The unit background forms 20–30%. Reserve the LEFT 20–25% of the circle as a calm TITLE-SAFE ZONE of soft window light and pale wall, with no faces, hands, equipment, or objects in it.

STYLE
Bright, airy, natural light; gentle color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, renal green #1f7a4d, and warm neutrals; one consistent grade with the other module heroes. Correct hands with five fingers; plausible, generic equipment.

ABSOLUTELY NO TEXT: no title, caption, label, logo, watermark, brand name, numbers on the bottle, readable notebook, readable screen, readable name badge, or any letters or numbers anywhere.

NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermark of any kind (including no renalcarematters.com mark)
✗ No brand label on the bottle; a plain clear bottle with marker lines only
✗ No needles, no visible blood, no visible tubing at the patient's arm
✗ No leaflet being handed over in place of the bottle; no lecture pose; no wagging finger
✗ No dark, moody, or high-contrast lighting; no HDR, neon, or oversaturation
✗ No cartoon or flat-vector style; no rectangular border, frame, or banner
✗ No cropped circle; no subject touching or crossing the circle's edge
✗ No faces, hands, or objects inside the left title-safe zone
✗ No distorted hands or faces; no branded or real-model equipment

Render no text of any kind; the image must be completely wordless.
```

**QA after generation:**
□ Square 2048 × 2048; circle fills 85–90% with an even white margin; circle not cropped
□ Absolutely no text, letters, numbers, logos, or watermark anywhere; the bottle has lines but no numbers or brand
□ Bottle and the pointing hand are sharp and right of center; patient and wife engaged with it
□ Left 20–25% of the circle empty
□ No needles, tubing, or blood at the covered access arm
□ Nurse is a tall slim man in his late 20s in an olive-green scrub top; patient a heavy-set man in his mid-60s with glasses; wife with short permed hair; none resembles anyone in the other heroes
□ Hands have five fingers; equipment generic
□ Light, bright color grade consistent with the module heroes

---


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
| 13 | `nephrology-nursing-13-convective-therapies-crrt-hdf-vignette-hero.png` | ICU nurse checks the hanging fluid bags on a continuous kidney therapy machine beside a sedated, ventilated patient. | See entry |
| 14 | `nephrology-nursing-14-living-well-hemodialysis-vignette-hero.png` | A dialysis nurse sits at eye level beside a middle-aged Filipino patient during treatment, listening attentively while a family member sits nearby. | See entry |
| 15 | `nephrology-nursing-15-glomerular-systemic-kidney-disease-vignette-hero.png` | A ward nurse weighs a patient with swollen legs on a bedside scale at the start of the morning, with a urine dipstick and a chart on the trolley beside her. | See entry |
| 16 | `nephrology-nursing-16-supportive-palliative-kidney-care-vignette-hero.png` | A dialysis nurse sits at eye level beside an older Filipino patient in a reclining chair, holding her hand while a family member listens. | See entry |
| 17 | `nephrology-nursing-17-teaching-evidence-based-practice-vignette-hero.png` | A dialysis nurse sits beside a patient in a treatment chair, showing him a marked water bottle while his wife watches and listens. | See entry |


## 5. Instructional diagrams (separate track — do not generate freely)

These are teaching diagrams whose labels, directions and numbers must be correct. They are built as reviewed vector graphics or site-native HTML, with every label authored as real text on the page. An image generator must not be asked to render machine settings, numeric values, labels or procedural steps.

| Module | Diagram | How it is produced | Must be verified by |
|---|---|---|---|
| 6 | Dialyzer transport: blood and dialysate in countercurrent flow; diffusion of urea and potassium out and bicarbonate in; ultrafiltration of water by pressure | The house `dialysis-circuit-schematic` skill, which fixes port colors, flow directions and pressure points; labels in HTML beside the figure | Hemodialysis nurse educator and nephrologist |
| 6 | Extracorporeal circuit overview: arterial needle, blood pump, dialyzer, venous chamber and air detector, venous needle | Same skill; no numeric settings in the image | Hemodialysis nurse educator and biomedical technician |
| 8 | Water treatment train: feed water, sediment filter, softener, two carbon tanks in series, reverse osmosis, distribution loop, machine; with the total-chlorine sampling point after the carbon tanks | Site-native markup (an ordered flow built in HTML and CSS) or a verified vector; topology and sampling points must match the unit being taught, and the caption must say it is an example layout | Dialysis water technician or biomedical engineer, and nephrologist |

The tables of limits, schedules and first actions in Modules 2, 4, 6, 8 and 9 already exist as accessible HTML on the pages and must stay as HTML.
