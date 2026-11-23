# GPT image prompts — replacements after the November 23, 2026 audit

These four figures failed the image audit and were **not** placed on the site. Regenerate each from the corrected prompt below, save it under the same file name (PNG master plus same-size WebP) in `Nephrology Nursing/Module images`, and the next install run will place it. Every other figure from the Module 13 add-on and add-on 2, and the refreshed heroes for Modules 1–12, passed and are live.

| ID | File | Why it failed | Fix |
|---|---|---|---|
| 13-H0 | `nephrology-nursing-13-convective-therapies-crrt-hdf-vignette-hero.png` | The nurse's fingertip touches the hanging bag. The module teaches that bags and scales must hang free and must not be touched, so the picture contradicts the lesson. | Keep everything else. The pointing fingertip must stop a clear gap short of the bag (about the width of two fingers); no part of the nurse's hand, sleeve, or order sheet touches any bag, hook, or scale. |
| 03-E | `nephrology-nursing-03-hd-day-plate.png` | Garbled lettering: the subtitle renders as “Youı ıenal dietitian sets your own amounts” and “Many contain potassium” has a malformed letter. Content and layout were otherwise correct. | Regenerate with the same layout; every label must match the TEXT LOCK below letter for letter. If a generator keeps breaking the small subtitle, set it at the same size as the panel captions. |
| 15-E | `nephrology-nursing-15-pkd-inheritance.png` | The figure states “Children of an affected parent: blood pressure checked regularly, as the team advises.” The lesson does not give a frequency, and the 2025 KDIGO guideline sets yearly ambulatory monitoring only for some children (early-onset disease or blood pressure at or above the 75th percentile), so the fixed interval is not supported. | Change item 5 to “Children of an affected parent: blood pressure checked regularly, as the team advises.” Everything else stays. |
| 16-B | `nephrology-nursing-16-symptom-wheel.png` | The title renders as “The syrnptom wheel” (malformed “m”), and the wheel's outer ring overlaps the subtitle line. | Regenerate with the title exactly “The symptom wheel”; leave a clear band of white space between the subtitle and the top of the wheel's outer ring so no text touches or overlaps it. Keep all wedge texts and side panels as they were. |

## 13-H0 — The ICU nurse and the hanging bags — replacement

**Audit finding:** The nurse's fingertip touches the hanging bag. The module teaches that bags and scales must hang free and must not be touched, so the picture contradicts the lesson.

**What to change:** Keep everything else. The pointing fingertip must stop a clear gap short of the bag (about the width of two fingers); no part of the nurse's hand, sleeve, or order sheet touches any bag, hook, or scale.

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
Night shift in a bright, calm Philippine tertiary-hospital intensive care unit. A Filipino ICU nurse stands beside a generic, unbranded continuous kidney-therapy machine: a tall upright console on wheels with four large, clear, soft plastic fluid bags hanging freely from hooks on its lower sides, each bag resting in its own integrated weighing cradle. Clear fluid lines run from the bags into the console. The nurse holds a small printed order sheet (unreadable, soft rows only) in one hand and, with the other, steadies nothing: her fingertip points toward one bag's label area and stops a clear gap (about two finger-widths) short of it, never touching the bag, hook, or scale, as she compares the bag against the order. Her expression is calm, focused, unhurried. In the soft-focus background lies a sedated adult patient on a ventilator: a woman in her late fifties, eyes closed, sheet folded neatly at the chest, a ventilator tube at the mouth, peaceful and dignified, mostly out of focus.

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
✗ No fingertip, hand, sleeve, or paper touching or resting against any bag, hook, or scale (keep a visible gap)
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

**QA after regeneration (in addition to the checklist above):**
□ No fingertip, hand, sleeve, or paper touching or resting against any bag, hook, or scale (keep a visible gap)


## 03-E — The Filipino plate on a dialysis day — replacement

**Audit finding:** Garbled lettering: the subtitle renders as “Youı ıenal dietitian sets your own amounts” and “Many contain potassium” has a malformed letter. Content and layout were otherwise correct.

**What to change:** Regenerate with the same layout; every label must match the TEXT LOCK below letter for letter. If a generator keeps breaking the small subtitle, set it at the same size as the panel captions.

- **File:** images/nephrology-nursing-03-hd-day-plate.png
- **Placement:** Module 3, section `hd-meals` (Filipino meals on dialysis days); also supports `hd-nutrition` (How eating changes once hemodialysis starts)
- **Job:** A — the learner can coach a patient on HD to build a familiar plate with more protein, less salt, and lower-potassium choices, and to count sabaw as fluid.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B, plate diagram with swap cards)
- **Canvas:** 1792 × 1024, 16:9 landscape
- **Alt text:** A Filipino dialysis-day plate with measured rice, a palm-sized portion of fish or egg, and a lower-potassium vegetable, with swaps for salty and processed foods, a small cup of sabaw counted as fluid, and the binder taken with the first spoonful.
- **Caption:** On hemodialysis, protein needs go up while salt, potassium, and phosphate still count every day. Change the portion, the preparation, or one ingredient at a time, starting from what the patient ate yesterday; the renal dietitian sets the individual plan.
- **Source of truth:** m03_x2.py `hd-meals`: plate pattern (measured portion of rice, palm-sized portion of protein food at each meal, a lower-potassium vegetable, less salt); do not cut rice in a patient losing weight without the dietitian; swap table (tuyo and daing → fresh galunggong or tilapia; hotdog, longganisa, tocino, corned beef, luncheon meat → eggs, fresh chicken, fresh fish; instant noodles → little or none of the seasoning packet; fish sauce, soy sauce, bagoong → calamansi, vinegar, garlic, onion, ginger, pepper; banana or ripe mango → apple, pineapple, pear, grapes; sweet potato, taro, mung beans → small, peeled, cut small, boiled in water that is discarded; cola and chocolate drinks count as fluid and carry phosphate or potassium; salt substitutes not without physician approval); sabaw: eat the solids, small cup of broth counted as fluid, sayote, upo, cabbage; rice porridge counts as fluid; fiesta plan; eggs as low-cost protein, egg whites less phosphate. m03_x2.py `hd-nutrition`: protein goes up; sodium and fluid stay tight; potassium highest before the long-gap session; binders with meals and phosphate-containing snacks. m17_x.py `literacy`: "Take with your first spoonful of rice". The KDOQI numbers in `hd-nutrition` (1.0 to 1.2 g/kg, less than 100 mmol sodium) are deliberately left off the plate.
- **Reviewer flags:** (1) Distinct from 03-C (Filipino food guide by nutrient) in the first brief; this figure is the dialysis-day plate and swaps. Confirm both are wanted. (2) Portion sizes are relative ("measured", "palm-sized"); no grams or cups are shown. The renal dietitian should confirm the plate proportions.
- **Attach when generating:** not applicable

```text
Medical nutrition education figure, 1792 × 1024 landscape (16:9), clean editorial infographic with appetizing flat-vector food illustration: building a Filipino meal on a hemodialysis day. White #ffffff background; clean sans-serif typography set in Inter (never serif); text navy #0f1e2e; headings clinical teal #1a6b72; card fills soft gray #f3f4f6. Foods drawn realistically enough to recognize, in a warm flat-illustration style.

LAYOUT
Title top left, bold navy: "The dialysis-day plate". Subtitle in teal: "More protein, less salt, smarter fruit and vegetables".
Left 45%: one plate seen from above. Right 55%: swap cards in two columns. Bottom strip: soup and binder tips.

THE PLATE (round white enamel plate with a thin blue rim, on a woven placemat):
- One section: a neat mound of steamed white rice shaped by a cup, labeled "Measured rice: energy without much potassium".
- One section: a pan-fried fresh galunggong fish and a boiled egg, sized together about the size of an adult palm, labeled "Palm-sized protein at every meal".
- One section: sautéed sayote and cabbage strips, labeled "Lower-potassium vegetable".
- Beside the plate: a small cut of calamansi and a small dish of vinegar with garlic, labeled "Flavor with calamansi, vinegar, garlic".
- A small white tablet beside the spoon, labeled "Binder with your first spoonful of rice".
- Off to the side, a glass of water and a small cup of clear broth, with a teal tag: "These count as fluid".

SWAP CARDS (right side; each card shows the usual food on the left with a small amber #b8860b arrow pointing to the swap on the right with a green #1f7a4d check):
1. "Tuyo or daing" → "Fresh galunggong or tilapia" / reason line: "Same protein, much less salt"
2. "Hotdog, longganisa, corned beef" → "Egg, fresh chicken, fresh fish" / "Processed meats add salt and phosphate"
3. "Fish sauce, soy sauce, bagoong at the table" → "Calamansi, vinegar, garlic, ginger, pepper" / "Flavor without sodium"
4. "Banana or ripe mango" → "Apple, pineapple, pear, or grapes" / "Lower potassium"
5. "Cola or chocolate drink" → "Water within the allowance" / "Cola carries phosphate; all drinks count as fluid"
6. "Salt substitute" → amber stop icon "Only if the physician approves" / "Many contain potassium"
Draw each food as a small recognizable illustration with no packaging or brand labels.

BOTTOM STRIP (full width, pale teal #eef6f7), three short tips with icons:
- soup bowl icon: "Sinigang or tinola: eat the solids; one small cup of broth, counted as fluid"
- calendar icon with no dates: "Most careful before the long gap between sessions"
- egg icon: "Eggs: low-cost protein; ask the dietitian how many"

Small gray line under the title: "Your renal dietitian sets your own amounts".

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No malformed, missing, or substituted letters in any label (check the subtitle and the salt-substitute caption letter by letter)
✗ No numbers: no grams, cups, milligrams, millimoles, kilocalories, or portion counts
✗ No brand names, logos, cans, packets with labels, or bottle labels
✗ No foods not named above on the plate; no banana, mango, or processed meats on the plate itself
✗ No people or faces
✗ No dark background, no photorealism, no cartoon faces on food, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.

TEXT LOCK (render exactly, letter for letter):
- The dialysis-day plate
- More protein, less salt, smarter fruit and vegetables
- Measured rice: energy without much potassium
- Palm-sized protein at every meal
- Lower-potassium vegetable
- Flavor with calamansi, vinegar, garlic
- Binder with your first spoonful of rice
- These count as fluid
- Tuyo or daing
- Fresh galunggong or tilapia
- Same protein, much less salt
- Hotdog, longganisa, corned beef
- Egg, fresh chicken, fresh fish
- Processed meats add salt and phosphate
- Fish sauce, soy sauce, bagoong at the table
- Calamansi, vinegar, garlic, ginger, pepper
- Flavor without sodium
- Banana or ripe mango
- Apple, pineapple, pear, or grapes
- Lower potassium
- Cola or chocolate drink
- Water within the allowance
- Cola carries phosphate; all drinks count as fluid
- Salt substitute
- Only if the physician approves
- Many contain potassium
- Sinigang or tinola: eat the solids; one small cup of broth, counted as fluid
- Most careful before the long gap between sessions
- Eggs: low-cost protein; ask the dietitian how many
- Your renal dietitian sets your own amounts
- © renalcarematters.com
```

**QA after generation:**
□ Plate shows measured rice, palm-sized fish and egg, sayote and cabbage; nothing else on the plate
□ Binder tablet beside the spoon with "first spoonful of rice"; water and broth tagged as fluid
□ Six swap cards in order with correct directions (usual → swap)
□ Salt substitute card says only if the physician approves
□ Soup tip says eat the solids and one small cup of broth, counted as fluid
□ Filipino food names spelled correctly ("galunggong", "longganisa", "bagoong", "calamansi", "sayote", "sinigang", "tinola")
□ No numbers or brands
□ American spelling for English words ("flavor", "sautéed" acceptable); no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

**QA after regeneration (in addition to the checklist above):**
□ No malformed, missing, or substituted letters in any label (check the subtitle and the salt-substitute caption letter by letter)


## 15-E — Polycystic kidney disease runs in families: one chance in two — replacement

**Audit finding:** The figure states “Children of an affected parent: blood pressure checked regularly, as the team advises.” The lesson does not give a frequency, and the 2025 KDIGO guideline sets yearly ambulatory monitoring only for some children (early-onset disease or blood pressure at or above the 75th percentile), so the fixed interval is not supported.

**What to change:** Change item 5 to “Children of an affected parent: blood pressure checked regularly, as the team advises.” Everything else stays.

- **File:** images/nephrology-nursing-15-pkd-inheritance.png
- **Placement:** Module 15, section `diabetic-pkd` (Diabetic kidney disease, when it may not be diabetic, and polycystic kidney disease)
- **Job:** U/A — the learner can explain one-in-two inheritance in plain words and carry out the nurse's family-screening steps with respect for choice and confidentiality.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B, family tree plus action steps)
- **Canvas:** 1792 × 1024, 16:9 landscape
- **Alt text:** Family tree showing that each child of a parent with polycystic kidney disease has a one-in-two chance of inheriting the gene, with the nurse's five family-screening steps and key teaching points.
- **Caption:** Each child of an affected parent has a one-in-two chance of inheriting the gene, and the chance is the same for every child. A relative who carries the gene can still benefit from early blood pressure control and kidney protection.
- **Source of truth:** m15_x.py `diabetic-pkd`: autosomal dominant polycystic kidney disease is the most common inherited kidney disease; cysts grow from the tubules over decades; kidney function usually falls in middle age; each child of an affected parent has a one-in-two chance; KDIGO 2025: blood pressure often rises early; children of affected parents need blood pressure checks (the lesson sets no interval); high water intake for early and moderate CKD; tolvaptan for some adults (thirst, large urine volumes, liver injury; report yellow eyes, dark urine, unusual tiredness, right-sided abdominal pain); cyst pain, bleeding, infection, stones; aneurysm screening for those with personal or family history; sudden severe headache is an emergency; family screening by ultrasound first, genetic testing when unclear; five nurse steps (family tree; explain one-in-two; offer BP checks and refer interested adults; respect choice not to be tested and confidentiality; children need BP checked even if not tested). "One in two" is the only number.
- **Reviewer flags:** The family tree is illustrative (one affected parent, four children, two affected); real families vary, and the figure says "the chance is the same for every child". Confirm that showing two of four affected does not mislead; an alternative is a single coin-toss icon per child with no outcome drawn.
- **Attach when generating:** not applicable

```text
Medical education figure, 1792 × 1024 landscape (16:9), clean editorial infographic: how polycystic kidney disease is inherited, and what the nurse does for the family. White #ffffff background; clean sans-serif typography set in Inter (never serif); text navy #0f1e2e; headings clinical teal #1a6b72; card fills soft gray #f3f4f6. Flat vector style; people shown as simple rounded silhouettes with no facial features.

LAYOUT
Title top left, bold navy: "Polycystic kidney disease: one chance in two". Subtitle in teal: "The most common inherited kidney disease".
Left 55%: family tree. Right 45%: two stacked cards.

LEFT — FAMILY TREE
Top row: two parent silhouettes joined by a horizontal line. The left parent is filled teal #1a6b72 with a small kidney icon dotted with tiny round cysts, labeled "Parent with the gene". The right parent is filled pale gray, labeled "Parent without the gene".
A vertical line drops to a horizontal sibling bar with four child silhouettes of mixed sexes and heights beneath. Above EACH child sits a small two-sided coin icon, half teal and half gray, labeled once at the left: "Each child: 1 in 2 chance". Two children are filled teal (labeled "Inherited the gene") and two are pale gray (labeled "Did not inherit"), placed in a non-alternating order (teal, gray, gray, teal).
Under the tree, a navy note in a soft gray box: "The chance is the same for every child, every time. It does not skip because a brother or sister was affected."
A small inset beside the parent: a kidney outline growing larger with fluid-filled round cysts, labeled "Cysts grow from the tubules over decades".

RIGHT CARD 1 — heading teal: "The nurse and the family" (numbered 1 to 5)
1. "Draw a family tree: kidney disease, dialysis, transplant, brain bleed, early death"
2. "Explain one in two, in plain words"
3. "Offer blood pressure checks; refer interested adults to the physician"
4. "Respect a choice not to be tested; keep results private unless the patient agrees"
5. "Children of an affected parent: blood pressure checked regularly, as the team advises"

RIGHT CARD 2 — heading renal green #1f7a4d: "Teach"
- "Blood pressure often rises early: check it at home"
- "Drink plenty of water, as the team advises"
- "On tolvaptan? Report yellow eyes, dark urine, tiredness, right-sided belly pain"
- "Sudden, severe headache: emergency"
Small gray gloss beneath: "Tolvaptan: a medicine that can slow cyst growth in some adults"

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No interval (yearly, every year, annually) attached to children's blood pressure checks
✗ No numbers other than "1 in 2", the step numbers 1 to 5, and "one in two"
✗ No percentages, ages, kidney sizes, or blood pressure values
✗ No DNA double helix, no chromosomes, no gene names
✗ No faces on silhouettes; no real family photographs
✗ No alternating teal-gray-teal-gray pattern among the children (avoid implying a fixed rule)
✗ No dark background, no photorealism, no cartoon caricature, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ One affected parent, one unaffected; four children each with a coin icon; "Each child: 1 in 2 chance"
□ Children order teal, gray, gray, teal (not alternating)
□ "The chance is the same for every child, every time" note present
□ Five nurse steps and four teaching points verbatim; tolvaptan glossed
□ No numbers other than 1 in 2 and step numbers
□ No faces, DNA, or gene names
□ Label spelling correct ("polycystic", "tolvaptan", "tubules"); American spelling; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

**QA after regeneration (in addition to the checklist above):**
□ No interval (yearly, every year, annually) attached to children's blood pressure checks


## 16-B — The symptom wheel: assess, comfort, report — replacement

**Audit finding:** The title renders as “The syrnptom wheel” (malformed “m”), and the wheel's outer ring overlaps the subtitle line.

**What to change:** Regenerate with the title exactly “The symptom wheel”; leave a clear band of white space between the subtitle and the top of the wheel's outer ring so no text touches or overlaps it. Keep all wedge texts and side panels as they were.

- **File:** images/nephrology-nursing-16-symptom-wheel.png
- **Placement:** Module 16, section `symptoms-pc` (Symptom by symptom: assess, comfort, report, refer); the six-step nurse's role is in `bedside`
- **Job:** A — the learner can run the same assess-comfort-report pattern for each common symptom and knows the medicine-safety warning signs in kidney failure.
- **Governing skill:** williamriveromd-simple-figure (Scaffold D, wheel with a center and an outer safety ring)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Symptom wheel with eight segments, pain, itch, breathlessness, nausea and appetite, fatigue, restlessness, low mood, and sleep, each with the nursing comfort measure, around the steps ask, rate, comfort, report, and reassess.
- **Caption:** For every symptom the pattern is the same: ask, rate it from 0 to 10, relieve what nursing can relieve, report with enough detail for the physician to act, and reassess. After any new symptom medicine, watch for drowsiness, confusion, twitching, and slowed breathing.
- **Source of truth:** m16.py `bedside` six steps (ask routinely, assess with 0 to 10 severity, comfort, document, report with SBAR, refer; nurses do not prescribe). m16_x.py `symptoms-pc`: pain (rate 0 to 10, behavioral signs if cannot rate, positioning, warmth or cool packs as care plan allows; anti-inflammatory pain relievers harm kidneys; bowel plan with opioids); itch (ask directly, unperfumed moisturizer, lukewarm water, short nails, loose cotton, cool room, distraction; report with phosphate and missed sessions); breathlessness (emergency first: sudden or severe, falling saturation, chest pain, frothy sputum, confusion; then upright, fan to the face, open window, pursed-lip breathing, calm presence; oxygen only as ordered); nausea and appetite (small frequent portions, cool food, mouth care before meals, ask whether restrictions can be relaxed when goal is comfort); fatigue (recovery time, treatable causes, plan energy for what matters); restlessness (restless legs versus delirium; check pain, full bladder, constipation, oxygen, glucose, fever, medicines; family close; avoid restraints); low mood (screen per Module 14; hopelessness, loss of interest, guilt more telling); sleep from m16.py physiology and bedside list. Medicine-safety rule verbatim in substance: watch for increasing drowsiness, new confusion, twitching or jerks, slowed or shallow breathing, unsteadiness, falls; hold per order or protocol and notify. "0 to 10" is the only number.
- **Reviewer flags:** "Sleep" is drawn as its own segment from the `bedside` ask-list and the physiology table; the `symptoms-pc` section covers sleep under fatigue and low mood. Confirm.
- **Attach when generating:** not applicable

```text
Clinical reference figure, 1536 × 1152 (4:3), publication-grade nursing design: a symptom assessment wheel for kidney supportive care. White #ffffff background; clean sans-serif typography set in Inter (never serif); text navy #0f1e2e; headings clinical teal #1a6b72. Flat vector icons, calm palette.

LAYOUT
Title top left, bold navy: "The symptom wheel". Subtitle in teal: "Same steps for every symptom".
A large circular wheel fills the center-left two-thirds; a narrow note column sits on the right.

WHEEL CENTER (pale teal #eef6f7 disc) with five steps arranged in a small circle of arrows:
"Ask" → "Rate 0 to 10" → "Comfort" → "Report (SBAR)" → "Reassess"
Under the small circle, tiny navy text: "The physician chooses medicines; the nurse gives them as ordered and watches."

EIGHT SEGMENTS around the center (alternating very soft gray and white), each with a small icon, a bold symptom name, and one comfort line:
1. Pain (icon: joint with a small spark): "Position, pressure relief, warmth or cool packs as planned; behavior signs if cannot rate"
2. Itch (icon: hand over forearm): "Unperfumed moisturizer, lukewarm water, short nails, loose cotton"
3. Breathlessness (icon: lungs with a fan): "Sit upright, fan to the face, open window, slow pursed-lip breathing"
4. Nausea and appetite (icon: small bowl): "Small, cool portions; mouth care before meals"
5. Fatigue (icon: low battery): "Find treatable causes; save energy for what matters"
6. Restlessness (icon: legs with motion lines and a question mark): "Restless legs or delirium? Check bladder, bowels, oxygen, glucose, fever, medicines"
7. Low mood (icon: small cloud): "Screen per policy; listen for hopelessness"
8. Sleep (icon: moon): "Ask about night itch, breathlessness lying flat, worry"

OUTER SAFETY RING (a thin amber #b8860b ring around the whole wheel, with small text running along its top arc): "After any new symptom medicine: drowsiness · confusion · twitching · slowed breathing · falls → hold per order, notify"

RIGHT NOTE COLUMN (soft gray #f3f4f6), two boxes:
- Amber-outlined box, heading "Breathless: emergency first": "Sudden or severe, falling oxygen, chest pain, frothy sputum, confusion: call the physician now"
- Teal-outlined box, heading "Kidney-safe pain relief": "Anti-inflammatory tablets and gels can harm the kidneys: teach patients not to buy them"

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No overlap between the subtitle and the wheel's outer ring; title spelled exactly “The symptom wheel”
✗ No numbers other than "0 to 10" and the segment order (do not print segment numbers)
✗ No medicine names, doses, or drug classes other than "anti-inflammatory tablets and gels"
✗ No people, faces, or bodies in distress; small icons only
✗ No oxygen mask or tank drawn
✗ No dark background, no photorealism, no cartoon caricature, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.

TEXT LOCK (render exactly, letter for letter):
- The symptom wheel
- Same steps for every symptom
- Ask
- Rate 0 to 10
- Comfort
- Report (SBAR)
- Reassess
- The physician chooses medicines; the nurse gives them as ordered and watches.
- Position, pressure relief, warmth or cool packs as planned; behavior signs if cannot rate
- Unperfumed moisturizer, lukewarm water, short nails, loose cotton
- Sit upright, fan to the face, open window, slow pursed-lip breathing
- Small, cool portions; mouth care before meals
- Find treatable causes; save energy for what matters
- Restless legs or delirium? Check bladder, bowels, oxygen, glucose, fever, medicines
- Screen per policy; listen for hopelessness
- Ask about night itch, breathlessness lying flat, worry
- 

RIGHT NOTE COLUMN (soft gray #f3f4f6), two boxes:
- Amber-outlined box, heading 
- : 
- 
- Teal-outlined box, heading 
- 

Footer: 
- 0 to 10
- anti-inflammatory tablets and gels
```

**QA after generation:**
□ Center shows Ask → Rate 0 to 10 → Comfort → Report (SBAR) → Reassess
□ Eight segments with exact names and comfort lines
□ Amber outer ring lists drowsiness, confusion, twitching, slowed breathing, falls, and "hold per order, notify"
□ Breathlessness emergency box present
□ No numbers other than 0 to 10; no medicine names
□ Label spelling correct ("unperfumed", "pursed-lip", "delirium"); American spelling; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

**QA after regeneration (in addition to the checklist above):**
□ No overlap between the subtitle and the wheel's outer ring; title spelled exactly “The symptom wheel”

