# Image Plan: *Workforce Issues in Nephrology: Crisis or Opportunity?* (`nephrology-workforce-crisis-or-opportunity.html`)

**Guide:** Kidney care workforce (capacity, distribution, staffing and outcomes, redesign). Dual audience (Patients & Families in EN/TL/CEB/KAP; Clinicians in English).
**Prepared:** 2026-11-11 · **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the ChatGPT **Image Generator** GPT → https://chatgpt.com/
**Skills used:** `williamriveromd-infographic-generator` (Constitution v1.0, 7-layer architecture, applied to every figure) · `williamriveromd-hero-vignette` v3 · `williamriveromd-infographic-skill` v5 · `williamriveromd-simple-figure` · `williamriveromd-algorithm-generator-skill` (flow and loop rules)

---

## Design intent: understandable at every education level

This guide asks readers to understand an abstract idea: that **a shortage is not a number of names, but hours of care that reach a person**. Every figure turns that idea into something a reader can see.

1. **Picture first, words second.** Each patient figure must make sense with the labels covered: a person, an action, an outcome.
2. **One idea per figure.** No figure mixes workforce data with clinical advice.
3. **No numbers in any image.** All statistics live in the HTML text and the accessible HTML bar charts, where they are sourced and correct. Image generators garble digits, and a wrong number in a shareable graphic cannot be corrected by a footnote.
4. **Color means the same thing everywhere:** teal = capacity and care delivered; orange = demand and pressure; green = an action that helps; amber = caution and balancing measure; red = never or emergency; navy = text and structure.
5. **Labels of four to eight words**, plain verbs ("Bring your results"), in American English.
6. **Respect the workforce.** Show clinicians as skilled and calm, never collapsing, crying, or faceless. Pressure is shown through clocks, queues, and empty chairs, not through suffering people.
7. **Filipino life as it is:** barangay health stations, jeepneys and bancas, provincial clinics, capiz windows, but no disaster spectacle and no real hospital names or logos.

## House rules baked into every prompt

- **Light backgrounds only:** white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, pale teal `#eef6f7`. Never navy, charcoal, or black.
- **Fonts:** on-image type uses **Inter** only (one of the four approved faces: Inter, Nunito Sans, IBM Plex Sans, Manrope). No serif, no handwriting fonts.
- **Palette:** navy `#0f1e2e` / `#1F3864` (text, structure), teal `#1A6B72`, orange `#C55A11`, green `#2E6B3E`, amber `#b8860b`, red `#C00000`, purple `#4B3280`, on light fills.
- **Rendering finish:** illustrated, softly shaded, semi-3D editorial illustration with natural light. **Not flat clip-art or flat SVG vector style**, and not cartoonish.
- **Attribution:** `© renalcarematters.com`, exact lowercase string, small, navy, bottom-right (bottom-center on portrait), clear of all content, on every image **except the wordless vignette hero**. It is specified in Layer C, Layer E, and Layer G of each prompt.
- **Save** each asset as `.png` plus a `.webp` twin in `images/`, using the exact FILE NAME.

### Clinical and factual guardrails for THIS guide

- **No staffing ratios, patient counts, percentages, or densities** drawn in any image (they are in the text).
- **No "safe" or "unsafe" ratio badges**, no traffic-light verdicts on a roster, no implied regulatory pass or fail.
- **No burnout imagery that blames individuals** (no head-in-hands clinician, no crying nurse).
- **No real people, hospital names, society logos, or government seals** (no DOH, PhilHealth, PSN, ISN marks).
- **No US flags or US-specific scenes** in patient figures; the guide's US data are labeled examples, not the patient's world.
- **Home dialysis and transplant are never shown as "replacing" staff.**
- **Kidney anatomy is not needed in this guide.** Where a kidney icon appears, it is a small stylized symbol, not an anatomical rendering, so Constitution v1.0 Layer A is applied as a *Clinical & factual truth block*.

---

## Asset roster

| # | File name (`images/`) | Placement | Type / skill | Audience | Size |
|---|---|---|---|---|---|
| 1 | `nephrology-workforce-crisis-or-opportunity-vignette-hero.png` | Patient hero disc | Hero vignette v3, Scaffold A | Mixed | 2048 × 2048 |
| 2 | `nephrology-workforce-crisis-or-opportunity-og.png` | `og:image` share card | Infographic skill, OG card | Mixed | **1200 × 630 (fixed)** |
| 3 | `…-01-headcount-vs-capacity.png` | § Why Waits Happen (patients) | Simple figure, Scaffold B comparison | Patients | 1792 × 1024 |
| 4 | `…-02-kidney-care-team.png` | § Your Team (patients) | Infographic, circular workflow | Patients | 1792 × 1024 |
| 5 | `…-08-prepare-for-visit.png` | § What You Can Do (patients) | Simple figure, Scaffold C steps | Patients | 1792 × 1024 |
| 6 | `…-03-workload-attrition-loop.png` | § Definitions (clinicians) | Algorithm skill loop + simple figure | Clinicians | 1792 × 1024 |
| 7 | `…-05-annual-ratio-vs-bedside.png` | § Patient Impact (clinicians) | Simple figure, Scaffold B comparison | Clinicians | 1792 × 1024 |
| 8 | `…-06-redesign-levers.png` | § The Opportunity (clinicians) | Infographic, multi-panel | Clinicians | 1792 × 1024 |
| 9 | `…-07-ninety-day-roadmap.png` | § 90-Day Plan (clinicians) | Simple figure, Scaffold C steps | Clinicians | 1792 × 1024 |
| 10 | `…-09-archipelago-access-domains.png` | § Philippine Context (clinicians) | Simple figure, Scaffold D | Clinicians | 1792 × 1024 |

(`…` = `nephrology-workforce-crisis-or-opportunity`.) The HTML already references these exact names, with alt text and plain-language captions. Figure numbers follow the HTML (04 is intentionally unused: the global density chart is an accessible HTML chart, not an image).

**Cast plan (human variation across this guide):** hero = nurse in her thirties seen from behind; Fig 01 = no people (objects); Fig 02 = six different health workers plus an older man and his adult daughter; Fig 05 = one male nurse at chairside; Fig 07 = a mixed leadership table including a patient representative in a wheelchair; Fig 08 = hands-only plus one teenage granddaughter; Fig 09 = no people. No two figures reuse a face, outfit color, or pose.

---

## 1 · Circular vignette hero *(patient hero disc)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A people
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling
CAMERA: rear three-quarter view at shoulder height
HUMAN VARIATION (vs. previous guide): woman in her mid-thirties (previous: grandmother and grandson); slim build; hair in a low practical bun, black with a few strands loose; warm medium-brown Filipina skin tone; rounded face, soft jawline; light teal scrub top with a navy long-sleeve undershirt; small analog watch; mid-stride walking pose rather than seated; one hand lifted to a machine screen; calm, focused expression seen in partial profile; dialysis unit at dawn instead of a home; camera behind rather than high-angle front.
AUDIENCE: mixed
VISUAL GOAL: One skilled nurse moving through a bright dialysis unit at the start of a shift conveys that kidney care depends on real people's time.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: J Environmental Storytelling, one cohesive scene with no floating panels. Camera: rear three-quarter view at shoulder height.

CONSTITUTION v1.0 — LAYER A (CLINICAL TRUTH): a realistic modern hemodialysis unit; each treatment chair has its own dialysis machine beside it; bloodlines are neat, closed, and clipped, with no visible blood spills; staff wear clean scrubs and closed shoes; no patient is shown connected in close-up; equipment is generic, unbranded.
LAYER B (SPATIAL): the nurse occupies the left-center foreground, walking away from camera toward the right along an aisle of four to five treatment chairs that recede in soft focus; large windows on the far right admit early-morning daylight.
LAYER C (RENDER): Subject: a Filipina dialysis nurse in her mid-thirties, slim, black hair in a low bun, light teal scrub top over a navy long-sleeve undershirt, small analog watch, walks mid-stride between treatment chairs at the start of a morning shift, her right hand lightly touching the screen of a dialysis machine as she passes. In the soft background, one colleague (a man in his fifties in navy scrubs) prepares a chair, and one seated older patient raises a hand in greeting; both are out of focus. Hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE in the upper-right quadrant of clean pale window light and blurred wall, with no faces, equipment, icons, or callouts inside it. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; gentle edge falloff toward a slightly deeper neutral at the rim. Absolutely NO text of any kind and no watermark (this is the only image in the set without the attribution footer).
LAYER D (IMAGING): not applicable; no medical imaging shown.
LAYER E (NEGATIVE): ✗ no text, labels, logos, or watermark ✗ no exhausted, crying, or head-in-hands staff ✗ no blood, needles in close-up, or open wounds ✗ no crowded chaotic ward ✗ no dark or moody lighting ✗ no hospital or brand names ✗ no faces inside the title safe zone ✗ no cropped circle or subject touching the circle edge ✗ no duplicated people ✗ no cartoon style, HDR, or neon.
LAYER F (STYLE): premium healthcare editorial photography; natural skin texture; shallow depth of field; light airy palette with teal and navy accents.
LAYER G (QA): □ square 2048×2048 with full white-bordered circle — confirmed □ one dominant subject (nurse) — confirmed □ rear three-quarter camera — confirmed □ machines beside each chair, bloodlines tidy — confirmed □ no blood or needle close-ups — confirmed □ title safe zone empty upper right — confirmed □ calm, competent expression and posture — confirmed □ Filipino cast with ≥12 traits different from the previous guide — confirmed □ no text or watermark anywhere — confirmed □ no logos — confirmed □ light, bright background — confirmed □ no garbled artifacts — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin, never cropped. ONE dominant hero subject occupying 60–70% of the circle, 2–4 supporting elements, 20–25% empty title-safe zone. Filipino clinical context with ≥12 traits visibly different from the last guide. Crops cleanly inside the circle with no text.
```

---

## 2 · Open Graph share card *(og:image — FIXED 1200 × 630)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-og.png
IMAGE TYPE: OG / social share card (infographic skill)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed
VISUAL GOAL: In a social feed, the reader sees a whole kidney care team and an island map and understands that the guide is about who delivers kidney care, and where.

PROMPT:
CONSTITUTION v1.0 — LAYER A (CLINICAL TRUTH): five Filipino health workers shown as distinct professions by realistic cues only: nephrologist with stethoscope, dialysis nurse in teal scrubs, dialysis technician holding a closed bloodline set, dietitian with a printed meal plan, pharmacist with a pill organizer. No medical procedure shown.
LAYER B (SPATIAL): left 58% of the card holds the title block on white; right 42% holds the illustrated team standing in a loose semicircle in front of a faint, stylized outline of the Philippine archipelago in pale teal.
LAYER C (RENDER): White #ffffff background. Title in bold Inter, navy #0f1e2e, two lines: "Workforce Issues in Nephrology:" and on the second line, in orange #C55A11, "Crisis or Opportunity?". Beneath it, a single teal #1A6B72 subtitle in Inter regular: "Kidney care capacity, explained for patients and teams". A thin teal rule under the subtitle. Right side: the five health workers (two women, three men, ages from late twenties to sixties, varied heights, hairstyles, and Filipino skin tones; varied scrub and clinic-coat colors in teal, navy, white, and soft green), rendered as a softly shaded semi-3D editorial illustration with natural light, smiling slightly, facing the viewer. The archipelago outline behind them is decorative, with no place names. Bottom-right corner: "© renalcarematters.com" in small navy Inter, 70% opacity, clear of all figures and text.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no dark background ✗ no numbers or statistics ✗ no logos, seals, or hospital names ✗ no flags ✗ no misspelled title ✗ no extra words beyond title, subtitle, and attribution ✗ no flat clip-art style ✗ no cartoon faces ✗ attribution never omitted, enlarged, centered, or reworded (not "Renal Care Matters", not www.) ✗ attribution never overlapping people or text.
LAYER F (STYLE): premium health-publication cover; NEJM-style restraint; palette navy, teal, orange accent on white; Inter only.
LAYER G (QA): □ exactly 1200×630 — confirmed □ title spelled exactly, two lines, question mark present — confirmed □ subtitle spelled exactly — confirmed □ five distinct professions recognizable — confirmed □ no numbers anywhere — confirmed □ archipelago outline unlabeled and faint — confirmed □ white background — confirmed □ Inter font only — confirmed □ no logos or seals — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, generic stock-photo look, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY the Inter font. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Readable as a small thumbnail; title legible at 300 px wide; light background; attribution visible bottom-right.
```

---

## 3 · Figure 01 — Names on a list vs hours of care *(§ Why Waits Happen, patients)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-01-headcount-vs-capacity.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (also clear to clinicians)
VISUAL GOAL: A reader with little schooling sees that a long list of names can still mean little time for patients, and understands "capacity" without a definition.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical abstract restraint. White #ffffff background.

CONSTITUTION v1.0 — LAYER A (FACTUAL TRUTH): no numbers, ratios, or counts anywhere; the comparison is purely visual. The jeepney analogy from the guide is shown literally: drivers versus trips that actually reach the barangay.
LAYER B (SPATIAL): two equal panels separated by a soft dashed vertical divider. Left panel = what a list shows. Right panel = what patients feel. Reading order left to right.
LAYER C (RENDER): Title centered at top in bold Inter, navy #0f1e2e: "A list of names is not the same as time for patients". LEFT panel, header in orange #C55A11: "Names on a list". It shows a clipboard with a long column of anonymous name lines (unreadable gray bars, not real names) beside a parked row of five jeepneys at a city terminal, all idle. Below, a small icon row: a building with many windows (city), a stack of paperwork, a car on a long road. Caption under panel (Inter, navy, 2 short lines): "Some work in other places. Some time goes to paperwork and travel." RIGHT panel, header in teal #1A6B72: "Hours of care that reach you". It shows a single jeepney driving along a green provincial road toward a small barangay health station, where a nurse greets an older woman; above the road a clean clock face with a teal filled sector (no numbers on the clock) suggests the share of time spent with patients. Caption (2 short lines): "What matters is the care that actually reaches your community." Bottom strip, soft gray #f3f4f6, one navy sentence: "Health planners call this capacity." All figures rendered as softly shaded semi-3D editorial illustration, natural daylight, Filipino setting. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of all content.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no numbers, percentages, or digits on clocks or lists ✗ no readable personal names ✗ no sad or suffering patients ✗ no exhausted staff ✗ no hospital or jeepney brand names, no route signboard text ✗ no dark background ✗ no flat vector clip-art ✗ no cartoon faces ✗ no more than the listed words ✗ attribution present, exact, small, navy, bottom-right, not overlapping.
LAYER F (STYLE): editorial health illustration; palette navy, teal, orange, soft green on white; Inter only.
LAYER G (QA): □ two equal panels with dashed divider — confirmed □ left = idle list and jeepneys, right = one trip reaching a barangay — confirmed □ no digits anywhere, including clock — confirmed □ title spelled exactly — confirmed □ captions short and legible on mobile — confirmed □ Filipino setting — confirmed □ no brand or route text — confirmed □ white background — confirmed □ Inter only — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Understandable with all text covered. Mobile-readable. Light background. Attribution bottom-right.
```

---

## 4 · Figure 02 — Your kidney care team *(§ Your Team, patients)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-02-kidney-care-team.png
IMAGE TYPE: Infographic — circular workflow (archetype 8)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: The patient sees six helpers around them, each with one clear job, and that information flows between helpers rather than through the patient alone.

PROMPT:
Circular care-team infographic, polished patient-education systems diagram. White #ffffff background.

CONSTITUTION v1.0 — LAYER A (CLINICAL TRUTH): each role is shown doing a real, in-scope task: barangay health worker taking a blood pressure with an arm cuff; family doctor reviewing a printed lab sheet; nephrologist explaining with a simple kidney-shaped icon card (stylized symbol, not anatomy); dialysis nurse beside a dialysis machine holding a clipboard; dietitian holding a plate model with rice, fish, and vegetables; pharmacist holding a weekly pill organizer. No role performs another's task.
LAYER B (SPATIAL): center: an older Filipino man (late sixties, short gray hair, eyeglasses, light blue polo) seated with his adult daughter (thirties, shoulder-length hair, mustard blouse) standing behind him with a hand on his shoulder. Six role vignettes arranged evenly on a ring around them, clockwise from the top: nephrologist, dialysis nurse, dietitian, pharmacist, social worker and help desk, barangay health worker and family doctor (paired). Thin teal curved arrows connect neighboring roles along the ring, showing information passing between them.
LAYER C (RENDER): Title at top in bold Inter navy #0f1e2e: "Your kidney care team". Each vignette sits in a soft rounded card (#eef6f7) with a short Inter label: "Nephrologist", "Dialysis nurse and technician", "Dietitian", "Pharmacist", "Social worker and help desk", "Family doctor and health worker". Under each label one 3–5 word job line: "Finds the cause, plans treatment"; "Runs each treatment safely"; "Plans meals you can afford"; "Checks doses and supplements"; "Helps with benefits and travel"; "Checks pressure, sugar, urine". Bottom strip, soft gray #f3f4f6: "When specialists are few, the whole team shares the work." Six different people with clearly different ages, sexes, faces, hairstyles, and clothing colors (no two alike, none reused from the hero). Softly shaded semi-3D editorial illustration, natural light. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of all content.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no anatomical kidney rendering (icon only) ✗ no logos, PhilHealth or DOH marks, or real hospital names ✗ no numbers ✗ no role doing another's task ✗ no duplicated faces ✗ no arrows pointing only at the patient (information flows around the ring) ✗ no dark background ✗ no flat clip-art ✗ no cartoon faces ✗ no tiny unreadable text ✗ attribution present, exact, small, navy, bottom-right, not overlapping.
LAYER F (STYLE): Filipino clinical editorial illustration; palette teal, navy, soft green, orange accents on white; Inter only.
LAYER G (QA): □ six role vignettes around a central patient and caregiver — confirmed □ each label spelled exactly — confirmed □ each role shown in-scope — confirmed □ teal arrows link roles around the ring — confirmed □ kidney shown only as a simple icon — confirmed □ six visibly different people — confirmed □ no logos or numbers — confirmed □ white background — confirmed □ readable on mobile — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Each role readable at phone width; calm, respectful mood; light background; attribution bottom-right.
```

---

## 5 · Figure 08 — Before your kidney appointment *(§ What You Can Do, patients)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-08-prepare-for-visit.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Five objects in a row show exactly what to bring and do, so a reader can prepare even without reading the labels.

PROMPT:
Clean clinical education infographic, white #ffffff background.

CONSTITUTION v1.0 — LAYER A (CLINICAL TRUTH): lab papers are generic and unreadable (gray lines, no values); medicine bottles and herbal sachets have no readable brand names; the referral letter shows only gray lines and a signature scribble; the phone shows a generic video-call screen with a clinician silhouette, no app logo.
LAYER B (SPATIAL): five rounded cards in a single left-to-right row, joined by bold navy right-pointing arrows, on a very soft gray #f3f4f6 panel.
LAYER C (RENDER): Title at top center in bold Inter navy #0f1e2e: "Before your kidney appointment". Each card has a colored top band, a large illustrated object, a step number in a circle, and a bold 3–5 word label in Inter. Card 1 (teal band): a folder of lab result sheets and a small home blood pressure log — "Bring your recent results". Card 2 (teal band): a clear bag holding medicine bottles, a blister pack, and an herbal tea sachet — "Bring every medicine you take". Card 3 (teal band): an envelope and a one-page letter — "Ask for a referral letter". Card 4 (green band #2E6B3E): a hand-written list with three bullet lines beside a teenage granddaughter (about sixteen, ponytail, school-uniform polo) helping hold it, shown from the shoulders down plus the paper — "Write your three questions". Card 5 (green band): a phone showing a teleconsult, next to a small provincial clinic building — "Ask about care closer to home". Bottom strip, full width soft gray: one navy sentence, "A prepared visit is a shorter wait for everyone." Hands and objects rendered as softly shaded semi-3D illustration with natural light. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of all content.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no readable lab values or patient names ✗ no drug brand names ✗ no app or company logos ✗ no numbers other than the step numbers 1–5 ✗ no red emergency imagery in this figure ✗ no dark background ✗ no flat clip-art ✗ no cartoon style ✗ no more than five cards ✗ attribution present, exact, small, navy, bottom-right, not overlapping.
LAYER F (STYLE): patient-education editorial illustration; teal and green palette on white; Inter only.
LAYER G (QA): □ exactly five cards with arrows left to right — confirmed □ step numbers 1–5 correct and in order — confirmed □ labels spelled exactly — confirmed □ no readable values, names, or brands — confirmed □ granddaughter shown respectfully, shoulders down — confirmed □ bottom sentence spelled exactly — confirmed □ white background — confirmed □ Inter only — confirmed □ mobile-readable — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Objects alone tell the story; light background; attribution bottom-right.
```

---

## 6 · Figure 03 — The workload–attrition loop *(§ Definitions, clinicians)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-03-workload-attrition-loop.png
IMAGE TYPE: Circular loop diagram (algorithm-generator loop rules + simple figure)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians and service leaders
VISUAL GOAL: Show a self-reinforcing loop and three places to break it, while making clear it is conceptual, not measured.

PROMPT:
Clean clinical systems diagram, journal-figure aesthetic, white #ffffff background.

CONSTITUTION v1.0 — LAYER A (FACTUAL TRUTH): this is a CONCEPTUAL model. No arrow carries a number, coefficient, or thickness implying effect size. All five arrows are the same weight.
LAYER B (SPATIAL): five rounded nodes evenly spaced on a clockwise circle occupying the center-left 65% of the canvas; a narrow legend column on the right 30%.
LAYER C (RENDER): Title at top in bold Inter navy #0f1e2e: "A loop worth breaking". Subtitle in teal #1A6B72 italic-free Inter: "Conceptual model, not a measured pathway". Nodes, clockwise from the top, in orange-outlined rounded rectangles with a small icon each: "Rising workload" (stacked folders), "Staff leave" (an open door), "Less capacity" (a half-empty clock), "Longer delays" (an hourglass), "Later, more complex care" (a patient chart with a rising line, no numbers). Equal-weight navy arrows connect each node to the next, closing the loop back to "Rising workload". Three green #2E6B3E circular markers sit on the arrows where the loop can be broken, each with a short label in a green pill: on the arrow from "Rising workload" to "Staff leave": "Retain and support staff"; on the arrow from "Less capacity" to "Longer delays": "Redesign the team"; on the arrow from "Longer delays" to "Later, more complex care": "Earlier, risk-based care". Right legend column: an orange swatch "pressure", a green swatch "intervention point", and the note "Arrows show direction only". Softly shaded, gentle 3D depth on nodes. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of all nodes and arrows.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no numbers, percentages, or arrow thickness differences ✗ no people's faces (icons only) ✗ no spaghetti crossing lines ✗ no extra nodes beyond five ✗ no red alarm styling ✗ no dark background ✗ no flat clip-art ✗ no serif fonts ✗ no garbled labels ✗ attribution never inside a node or on an arrow; present, exact, small, navy, bottom-right.
LAYER F (STYLE): AHA/journal-style clinical diagram restraint; navy, orange, green, teal on white; Inter only.
LAYER G (QA): □ five nodes in correct clockwise order — confirmed □ loop closes back to "Rising workload" — confirmed □ all arrows equal weight, no numbers — confirmed □ three green intervention markers on the correct arrows — confirmed □ subtitle "Conceptual model, not a measured pathway" present — confirmed □ legend present — confirmed □ labels spelled exactly — confirmed □ white background — confirmed □ Inter only — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Loop readable in five seconds; conceptual status explicit; light background; attribution bottom-right.
```

---

## 7 · Figure 05 — Annual facility ratio is not a bedside assignment *(§ Patient Impact, clinicians)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-05-annual-ratio-vs-bedside.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians, dialysis managers
VISUAL GOAL: Prevent the most common misreading of staffing studies: using an annual facility ratio as a shift ratio.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical abstract style. White #ffffff background.

CONSTITUTION v1.0 — LAYER A (CLINICAL TRUTH): the right panel shows a realistic dialysis start-up moment: four treatment chairs each with its own machine; one male nurse (forties, close-cropped hair, glasses, navy scrubs) at the second chair checking a machine; patients seated, lines closed and tidy, no blood visible. No ratio numbers appear anywhere.
LAYER B (SPATIAL): two equal panels with a soft dashed divider; a bold navy "not equal" sign (≠) centered on the divider.
LAYER C (RENDER): Title at top in bold Inter navy #0f1e2e: "Two different staffing measures". LEFT panel header in purple #4B3280: "Annual facility ratio". Content: a wall calendar showing a full year (month blocks without numbers), beside a stylized tally sheet and a simple division-bar symbol between a group of small patient icons and a smaller group of staff icons. Caption (Inter, 2 lines): "Used in cohort studies. Averages a whole year across the facility." RIGHT panel header in teal #1A6B72: "Who is at the chairs right now". Content: the start-up scene described in Layer A with a small analog wall clock (no numerals, hands only). Caption: "Decides coverage on a shift. Peaks at start-up and take-down." Bottom strip in soft amber #fbf0dc with navy text: "Study quartiles cannot be used as shift ratios." Softly shaded semi-3D editorial illustration. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of all content.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no numbers, ratios, or numerals on the calendar or clock ✗ no "safe/unsafe" badges or traffic lights ✗ no blood or needle close-ups ✗ no distressed patients or staff ✗ no brand names on machines ✗ no dark background ✗ no flat clip-art ✗ no cartoon faces ✗ no third panel ✗ attribution present, exact, small, navy, bottom-right, not overlapping.
LAYER F (STYLE): journal graphical-abstract clarity; purple, teal, amber, navy on white; Inter only.
LAYER G (QA): □ two panels with centered ≠ sign — confirmed □ left = year calendar and tally, right = live chairside moment — confirmed □ four chairs each with its own machine — confirmed □ no numbers anywhere — confirmed □ no blood visible — confirmed □ bottom sentence spelled exactly — confirmed □ no safety verdict styling — confirmed □ white background — confirmed □ Inter only — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
The ≠ message is obvious at thumbnail size; light background; attribution bottom-right.
```

---

## 8 · Figure 06 — Eight redesign levers *(§ The Opportunity, clinicians)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-06-redesign-levers.png
IMAGE TYPE: Multi-panel educational infographic (infographic skill archetype 4)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians, service and policy leaders
VISUAL GOAL: One glance shows the eight levers from the guide's matrix, each paired with a balancing-measure cue, so redesign never looks like moving work elsewhere.

PROMPT:
Modular clinician infographic, landscape, white #ffffff background.

CONSTITUTION v1.0 — LAYER A (FACTUAL TRUTH): no effect sizes, no arrows implying proven benefit, no numbers. Each tile is an option to test, not a promised result. The AI tile shows a person reviewing a screen, never a robot replacing a clinician.
LAYER B (SPATIAL): a 4 × 2 grid of equal rounded tiles around the full canvas; a slim header band at top; a slim footer band at bottom.
LAYER C (RENDER): Title in bold Inter navy #0f1e2e: "Eight levers for redesigning kidney care". Each tile (#eef6f7 fill, teal #1A6B72 heading, small illustrated scene, and a tiny amber #b8860b balance-scale icon in the tile corner) carries a 3–5 word heading: Row 1: "Retain the staff you have" (a nurse and senior colleague in a mentoring conversation); "Recruit into sustainable jobs" (a young physician reading a clear posted call schedule); "Protect teaching time" (a calendar block marked with a book icon, no dates); "Supported team roles" (a pharmacist and community health worker with a supervising nurse). Row 2: "E-consults and shared care" (two clinicians in different clinics exchanging a secure message on screens); "Prioritize by risk and need" (a sorting tray of referral folders with colored tabs, no text on tabs); "Strengthen underserved areas" (a small boat and a jeepney heading to a provincial clinic); "Test digital tools carefully" (a clinician checking an on-screen draft with a magnifier). Footer band soft gray #f3f4f6 with navy text: "Every lever comes with a balancing measure." and a legend: amber scale icon = "check where the work moved". Diverse Filipino health workers, none repeated from other figures. Softly shaded semi-3D editorial illustration. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of all tiles.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no numbers or percentages ✗ no robots, humanoid AI, or glowing brains ✗ no "solved" checkmarks implying proven benefit ✗ no logos or app names ✗ no readable patient data on screens ✗ no more than eight tiles ✗ no dark background ✗ no flat clip-art ✗ no cartoon style ✗ attribution present, exact, small, navy, bottom-right, not overlapping.
LAYER F (STYLE): publication-grade clinical infographic; teal, amber, navy on white; Inter only.
LAYER G (QA): □ exactly eight tiles in a 4 × 2 grid — confirmed □ headings spelled exactly — confirmed □ amber scale icon on every tile — confirmed □ footer sentence and legend present — confirmed □ AI tile shows human review, no robot — confirmed □ no numbers or logos — confirmed □ distinct people per tile — confirmed □ white background — confirmed □ Inter only — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, generic stock-photo look, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Tile headings readable on a tablet; calm and balanced; light background; attribution bottom-right.
```

---

## 9 · Figure 07 — A 90-day service plan *(§ 90-Day Plan, clinicians)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-07-ninety-day-roadmap.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence (3 stages)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians and service leaders
VISUAL GOAL: Measure, pilot one change, then compare and decide with patients present.

PROMPT:
Clean clinical roadmap infographic, white #ffffff background.

CONSTITUTION v1.0 — LAYER A (FACTUAL TRUTH): the only numbers allowed are the stage headings "Days 1–30", "Days 31–60", "Days 61–90". No outcome or result numbers. A short pilot is shown as testing feasibility, not proving benefit.
LAYER B (SPATIAL): three equal stage cards on a single horizontal road that runs left to right across the canvas, joined by bold navy arrows.
LAYER C (RENDER): Title at top center in bold Inter navy #0f1e2e: "A 90-day service plan". Stage 1 card (teal #1A6B72 band): heading "Days 1–30: Measure"; illustration: a clipboard, a wall clock without numerals, and two staff in a listening session with one patient; label "Baseline time and access, by role". Stage 2 card (orange #C55A11 band): heading "Days 31–60: Pilot one change"; illustration: a single flag planted on the road and a small stop sign beside it; label "Escalation and stopping rules set first". Stage 3 card (green #2E6B3E band): heading "Days 61–90: Compare and decide"; illustration: a balance scale on a meeting table with four leaders, one of them a patient representative using a wheelchair; label "Access, workload, safety, cost, together". Bottom strip soft gray #f3f4f6, navy text: "A short pilot shows feasibility, not mortality benefit." Diverse Filipino cast distinct from other figures. Softly shaded semi-3D editorial illustration. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of all content.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no numbers other than the three day ranges ✗ no charts with fake data ✗ no trophies or "success" icons ✗ no more than three stages ✗ no logos ✗ no dark background ✗ no flat clip-art ✗ no cartoon style ✗ no garbled day ranges ✗ attribution present, exact, small, navy, bottom-right, not overlapping.
LAYER F (STYLE): clean clinical roadmap; teal, orange, green, navy on white; Inter only.
LAYER G (QA): □ three stages in correct order with exact day ranges — confirmed □ headings and labels spelled exactly — confirmed □ stop sign present in stage 2 — confirmed □ patient representative present in stage 3 — confirmed □ bottom sentence spelled exactly — confirmed □ no other numbers — confirmed □ white background — confirmed □ Inter only — confirmed □ mobile-readable — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Three-step logic clear in five seconds; light background; attribution bottom-right.
```

---

## 10 · Figure 09 — Planning domains for an archipelago *(§ Philippine Context, clinicians)*

```
FILE NAME: nephrology-workforce-crisis-or-opportunity-09-archipelago-access-domains.png
IMAGE TYPE: Simple figure — Scaffold D single-concept poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians, planners
VISUAL GOAL: Show that, in the Philippines, workforce is one of five linked access limits, without implying any regional data.

PROMPT:
Medical systems infographic, white #ffffff background.

CONSTITUTION v1.0 — LAYER A (FACTUAL TRUTH): the archipelago is a simplified, recognizable silhouette in pale teal with NO place names, no region boundaries, no pins on real cities, and no shading that could be read as data. The figure illustrates planning domains only.
LAYER B (SPATIAL): archipelago silhouette centered, occupying about 45% of the canvas height; five domain icons in rounded cards placed around it (top-left, top-right, right, bottom-right, bottom-left) with thin gray leader lines to empty sea space, not to any island; a sixth central badge below the map.
LAYER C (RENDER): Title in bold Inter navy #0f1e2e: "Planning for an archipelago". Subtitle in teal Inter: "Workforce is one of several limits". Five domain cards (#eef6f7) with icon and 2–4 word Inter label: a banca boat and jeepney — "Transport and cost"; a clock — "Patient travel time"; signal bars on a phone — "Connectivity for teleconsults"; a test tube rack — "Laboratory access"; an ambulance — "Emergency transfer". Central badge below the map, navy outline, teal people icon: "Trained staff where patients live". Bottom note in small gray Inter: "Illustrative map. No data shown." Softly shaded semi-3D icons, flat pale map. Bottom-right corner: "© renalcarematters.com" in small navy Inter at 70% opacity, clear of the map and cards.
LAYER D (IMAGING): not applicable.
LAYER E (NEGATIVE): ✗ no place names, region labels, or city pins ✗ no heat-map or choropleth shading ✗ no numbers ✗ no flags, seals, or government logos ✗ leader lines never point to a specific island ✗ no dark background or satellite imagery ✗ no flat clip-art icons ✗ no cartoon style ✗ no garbled labels ✗ attribution present, exact, small, navy, bottom-right, not overlapping.
LAYER F (STYLE): calm public-health planning graphic; pale teal map, navy and teal text on white; Inter only.
LAYER G (QA): □ archipelago silhouette recognizable but unlabeled — confirmed □ five domain cards with exact labels — confirmed □ central badge text exact — confirmed □ "Illustrative map. No data shown." present — confirmed □ no shading implying data — confirmed □ no numbers or logos — confirmed □ white background — confirmed □ Inter only — confirmed □ mobile-readable — confirmed □ attribution present bottom-right — confirmed □ attribution reads exactly "© renalcarematters.com" — confirmed □ attribution legible, navy, not overlapping content — confirmed.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Domains readable at phone width; map clearly illustrative; light background; attribution bottom-right.
```

---

## After generation (Stage 2 checklist)

1. Check every image against its Layer G list; regenerate rather than edit if any number, logo, or misspelling appears.
2. Save PNG to `images/` with the exact file name, then make the WebP twin (e.g., `cwebp -q 82 in.png -o out.webp`).
3. OG card: confirm exactly 1200 × 630; the guide's `og:image` already points to `…-og.png`.
4. Optional: run `python3 generate_rg_thumbs.py` so the guide's Related-guides card gets a thumbnail.
5. Open the guide in light and dark mode and check each figure's caption panel in the lightbox.
