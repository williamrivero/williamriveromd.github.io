# Image Plan Blueprint — The Kidney–Brain Axis

**Guide:** `guides/kidney-brain-axis-cognitive-dysfunction-ckd.html` · **Images:** 20 · **Prepared:** November 10, 2026 · **Production:** ChatGPT Image Generator GPT

# Part 1 — Blueprint

## 1. What the images must do

The guide asks readers to hold several hard ideas at once: the brain and kidneys share blood vessels; several small causes add up; speed of change decides urgency; and "promising" is not "proven." Text alone carries these well for confident readers and poorly for everyone else. The images carry the same ideas so that a reader who skims, reads slowly, reads in a second language, or did not finish school still leaves with the main points.

Each image has one job:

| Reader need | Image that answers it |
|---|---|
| "What is this guide about?" | 000 hero, 001 OG card |
| "How are my kidneys connected to my brain?" | 002 crosstalk map |
| "Is what I'm seeing in my father normal?" | 003 everyday signs |
| "How fast do I need to act?" | 004 speed of change |
| "How common is this?" | 005 icon array |
| "Why does it happen?" | 006 four pathways |
| "Why do I feel foggy after dialysis?" | 007 dialysis scene, 008 dialysis-day diary |
| "Could my medicines be doing this?" | 009 medicine bag, 018 clinician medication card |
| "What can I do today?" | 010 action wheel |
| "Should I try the new treatment I read about?" | 011 evidence ladder, 019 clinician evidence map |
| "How can the family help?" | 012 family scene |
| Clinician: burden, mechanism, triage, testing, hemodynamics | 013–017 |

## 2. Reading levels

Three levels, assigned per image:

- **Level 1 — picture first (000, 001, 003, 007, 009, 012).** The image works with the words covered. Text is limited to short tags or one caption line. People, objects, and scenes do the teaching.
- **Level 2 — guided picture (002, 004, 005, 006, 008, 010, 011).** Short labels of 2–7 words, everyday vocabulary, one idea per panel. Numbers appear only as phrases the guide already uses ("about 1 in 3"), shown with countable icons rather than percentages.
- **Level 3 — clinician (013–019).** Standard clinical vocabulary and abbreviations (each defined in the figure's `fig-abbrevs` list), but still one message per figure and no invented thresholds.

Patient-tab images never use a medical term that the surrounding paragraph has not already explained.

## 3. Visual grammar (the same everywhere)

Readers learn a visual language once and reuse it. Every image follows these rules:

| Element | Meaning | Rule |
|---|---|---|
| **Solid arrow** | Link seen in people | Used only for human data |
| **Dashed arrow** | Idea still being tested | Always paired with a legend |
| **Red + triangle** | Emergency now | Only for sudden change or stroke signs |
| **Amber + circle** | Same-day check, or caution | Delirium, mixed evidence |
| **Teal + square** | Routine, planned care | Next visit, protective steps |
| **Green** | Benefit signal or protective step | Never used to mean "safe" for a number |
| **Brain above, kidneys below** | The axis | Same orientation in 000, 001, 002, 006, 010, 014 |
| **Teal #1a6b72 / navy #0f1e2e** | House palette | Light backgrounds only — never dark |

Color never carries meaning alone: every color band also has an icon or shape and words, so color-blind readers get the same message.

## 4. House rules applied to every prompt

- **Style:** softly shaded, illustrated, semi-3D, or photographic — not flat clip-art vector icons.
- **Fonts:** Inter, Nunito Sans, IBM Plex Sans, or Manrope only, named in each prompt.
- **Attribution:** `© renalcarematters.com`, small, semi-transparent navy, bottom-right (bottom-center for portrait). The vignette hero is the one exception: it carries no text at all.
- **Text discipline:** only the labels written in the prompt; no extra words, no brand names, no journal or guideline names on the image.
- **Numbers:** an image may show only numbers already in the guide (005, 013, 017). Never a dementia probability, a "safe" ultrafiltration rate or blood-pressure zone, a cognitive test cutoff, or a screening interval.
- **People:** Filipino cast, varied age, sex, body type, clothing, and setting. No repeat of earlier guides' casts, kitchens, dining tables, teal polos, or beige blouses. Dignity always: no mocking "confused elder" imagery.
- **Sizes:** generate at the model's native sizes (1536 × 1024 landscape, 1024 × 1536 portrait, 1024 × 1024 square) to avoid cropping. The hero is upscaled to 2048 × 2048; the OG card is cropped to exactly 1200 × 630.
- **Language:** images stay in English with very few words. The four-language explanation lives in each HTML `fig-desc` caption, so images never need to be redrawn per language.

## 5. Placement map and production order

**Priority:** P0 = the slot is already live (or the image carries a safety message); P1 = adds substantial understanding; P2 = enrichment.

| # | Priority | File | Skill | Size | Where it goes | Slot |
|---|---|---|---|---|---|---|
| 000 | P0 | `…-vignette-hero.png` | hero-vignette | 2048 × 2048 | Patient hero | Generated · wired |
| 001 | P0 | `…-og.png` | infographic-skill | 1200 × 630 | Page head | Generated · wired |
| 002 | P0 | `…-01-kidney-brain-crosstalk.png` | organ-crosstalk-sigil-graphic | 1536 × 1024 | Patients · The Big Picture (#what) | Generated · wired |
| 003 | P1 | `…-06-everyday-signs.png` | infographic-skill | 1536 × 1024 | Patients · What People Notice (#signs) | Generated · wired |
| 004 | P0 | `…-07-speed-of-change.png` | simple-figure | 1536 × 1024 | Patients · What People Notice (#signs) | Generated · wired |
| 005 | P1 | `…-08-how-common-icon-array.png` | simple-figure | 1536 × 1024 | Patients · How Common (#common) | Generated · wired |
| 006 | P0 | `…-02-four-pathways.png` | biomedical-mechanism-figure | 1536 × 1024 | Patients · Why It Happens (#why) | Generated · wired |
| 007 | P0 | `…-03-dialysis-brain-perfusion.png` | infographic-skill | 1536 × 1024 | Patients · If You Are on Dialysis (#dialysis) | Generated · wired |
| 008 | P2 | `…-09-dialysis-day-diary.png` | simple-figure | 1536 × 1024 | Patients · If You Are on Dialysis (#dialysis) | Generated · wired |
| 009 | P1 | `…-10-medicine-bag-check.png` | infographic-skill | 1536 × 1024 | Patients · Medicines to Review (#medicines) | Generated · wired |
| 010 | P1 | `…-11-protect-brain-and-kidneys.png` | infographic-skill | 1024 × 1024 | Patients · What Helps Today (#protect) | Generated · wired |
| 011 | P1 | `…-12-evidence-ladder.png` | simple-figure | 1536 × 1024 | Patients · What Is Being Studied (#research) | Generated · wired |
| 012 | P2 | `…-13-family-support.png` | infographic-skill | 1536 × 1024 | Patients · For Families (#family) | Generated · wired |
| 013 | P1 | `…-14-prevalence-by-modality.png` | simple-figure | 1536 × 1024 | Clinicians · Epidemiology (#md-epi) | Generated · wired |
| 014 | P0 | `…-04-mechanism-panels.png` | biomedical-mechanism-figure | 1536 × 1024 | Clinicians · Mechanisms (#md-mechanisms) | Generated · wired |
| 015 | P0 | `…-05-acute-vs-progressive-algorithm.png` | algorithm-generator-skill | 1024 × 1536 | Clinicians · Acute Change (#md-acute) | Generated · wired |
| 016 | P1 | `…-15-testing-window-dialysis-cycle.png` | simple-figure | 1536 × 1024 | Clinicians · Assessment (#md-assessment) | Generated · wired |
| 017 | P1 | `…-16-autoregulation-variability.png` | biomedical-mechanism-figure | 1536 × 1024 | Clinicians · Dialysis Hemodynamics (#md-hd) | Generated · wired |
| 018 | P1 | `…-17-medication-review-card.png` | infographic-skill | 1024 × 1536 | Clinicians · Medications (#md-meds) | Generated · wired |
| 019 | P2 | `…-18-emerging-evidence-map.png` | infographic-skill | 1536 × 1024 | Clinicians · Emerging Therapies (#md-emerging) | Generated · wired |


**Suggested order:** 000 → 001 → 002 → 004 → 006 → 007 → 014 → 015 (all P0), then P1, then P2.

## 6. Wiring the new slots

Images 000, 001, 002, 006, 007, 014, and 015 are already referenced in the guide. The other 13 need new `<figure>` slots in the sections named above. Each new slot needs:

- `<picture>` with a WebP `<source>` and a PNG `<img>`, `loading="lazy"`, and the width and height from the prompt
- `<figcaption>` with `<p class="fig-desc">` carrying the caption in all four languages (EN provided here; TL, CEB, and KAP to be written when the slot is added)
- `<dl class="fig-abbrevs">` whenever the image shows an abbreviation (013–019)

## 7. Accuracy guardrails (check before accepting any render)

- **005:** count the icons — 12 per row; filled 4, 6, 5, 3 from the left.
- **013:** every estimate and interval must match the guide table and be plotted to scale. If the generator mis-plots, rebuild this chart from data instead of regenerating it repeatedly.
- **017:** the only numbers allowed are 23.5% and 635 sessions; the axes have no values.
- **011 and 019:** the placement of each treatment must match the guide. Exercise plus training and hemodiafiltration are "promising", B vitamins "need confirmation", semaglutide "did not help" (Alzheimer trials, not CKD), and nothing reaches dementia prevention.
- **007:** the blood-pressure line dips less than the brain-flow line; the equipment is plausible (one machine, two blood lines, upright dialyzer).
- **All:** spell-check every label. AI text errors are the most common failure; regenerate rather than accept a typo on a medical figure.

## 8. Acceptance checklist (per image)

1. Light background; house palette; approved font
2. Labels exactly as written, spelled correctly; no extra text
3. Attribution present (except the hero)
4. Numbers, if any, match the guide
5. Solid and dashed arrows used correctly, with a legend
6. People look different from the cast of earlier guides
7. Readable on a phone at 360 px wide (patient images) or 860 px wide (clinician images)
8. PNG and WebP saved with the exact file name


---

# Part 2 — Production prompts

Paste each prompt into the Image Generator GPT: https://chatgpt.com/

## 000 · Circular vignette hero v3 — Scaffold C anatomy, composition archetype F (Anatomy)

IMAGE NUMBER: 000
PRIORITY: P0
SECTION PLACEMENT: Patient hero — figure.hero-figure.mode-patient > .hero-vignette (already wired)
SLOT STATUS: Slot wired
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-vignette-hero.png
STAGE 1 SKILL: williamriveromd-hero-vignette (v3, Scaffold C)
ARCHETYPE: Circular vignette hero v3 — Scaffold C anatomy, composition archetype F (Anatomy)
AUDIENCE: Everyone (patient tab hero)
READING LEVEL: Picture only; no words. Understood at a glance by any reader.
ASPECT RATIO: 1:1 (square; displayed inside an 85–90% inscribed circle with a white margin)
PIXEL DIMENSIONS: 2048 × 2048 (generate 1024 × 1024, upscale 2×)
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: semi-photoreal 3D brain, kidneys, and microvessels
- algorithm/flowchart: none
PURPOSE: Set the one idea of the whole guide: the brain and kidneys share one delicate circulation.
KEY CONCEPTS: shared small blood vessels; two organs, one system; calm and hopeful tone

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: F Anatomy. Camera: three-quarter view, slightly elevated.

Subject: a single clean render of a softly translucent human brain in the upper center of the circle and a pair of anatomically accurate kidneys in the lower center, floating on a soft, uncluttered pale-teal (#eef6f7) background. A fine, branching network of small blood vessels in muted renal red with a faint teal glow descends from the brain's surface and loops gently into both kidneys, so the two organs read as one shared circulation. Restrained clinical color (warm pink-gray brain, renal reds, teal accents), gentle studio light, soft contact shadow, shallow depth of field.

Visual hierarchy: the brain–kidney pair with its vessel network fills 60–70% of the circle; 2–3 subtle supporting cues (a faint blurred capillary close-up, soft light particles) fill 20–30%; reserve a 20–25% TITLE SAFE ZONE of empty soft gradient on the LEFT side of the circle (no anatomy, vessels, labels, or callouts in that zone). Soft falloff toward a slightly deeper neutral teal at the rim. Calm, hopeful, premium medical-textbook cover feel.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: busy layouts, collage overload, more than four supporting elements, icons, labels, baked-in text or watermark, cropped circle, cropped anatomy, objects touching the circular border, anything inside the title-safe zone, rectangular frames or banners, dark backgrounds, cartoon style, neon, HDR, glowing "electric brain" sci-fi effects, skulls, gore, distorted anatomy (kidney hilum must face medially).
```

QUALITY CHECK: 2048×2048 square; circle 85–90% of the canvas with a white margin, never cropped; one dominant subject at 60–70%; empty title-safe zone on the left; anatomically plausible brain and kidneys; zero text. (Vignette heroes carry no attribution by house rule — the circle crop would clip it.)

ALT TEXT: Semi-photorealistic 3D illustration of a human brain above a pair of kidneys on a soft pale-teal background, joined by a fine network of glowing small blood vessels that suggests the shared circulation linking the two organs.

FIGURE CAPTION (fig-desc, EN): Not applicable (hero or OG image).

OG WIDTH: 2048
OG HEIGHT: 2048


---

## 001 · OG / social share card

IMAGE NUMBER: 001
PRIORITY: P0
SECTION PLACEMENT: Page head — og:image and twitter:image meta tags (already wired)
SLOT STATUS: Slot wired
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-og.png
STAGE 1 SKILL: williamriveromd-infographic-skill (OG card)
ARCHETYPE: OG / social share card
AUDIENCE: Everyone (Facebook, Messenger, Viber, X previews)
READING LEVEL: Three short lines of text; readable on a phone feed.
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (generate 1536 × 1024, then crop/resize to exactly 1200 × 630)
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title lockup
- 3D component graphics: semi-photoreal brain and kidneys matching the hero
- algorithm/flowchart: none
PURPOSE: A recognizable share preview that matches the hero art and says exactly what the guide is about.
KEY CONCEPTS: brain–kidney shared circulation; guide title; audience line

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Landscape social share card on a white (#ffffff) to very light teal (#eef6f7) left-to-right gradient background. RIGHT half: the same semi-photorealistic 3D human brain above a pair of kidneys, joined by a fine network of small blood vessels in muted renal red with a faint teal glow, gentle studio light, soft shadow, organs fully visible. LEFT half: a title lockup set in Inter — line 1, bold, large, navy (#0f1e2e): "The Kidney–Brain Axis"; line 2, regular, teal (#1a6b72): "Thinking, memory, and kidney disease"; line 3, small, slate: "For patients, families, and clinicians · W Rivero, MD". Generous margins; nothing within 40 px of any edge so the card survives cropping. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No people, no extra text lines, no cropped organs.
```

QUALITY CHECK: Exactly three text lines plus the attribution, all spelled correctly in Inter; organs complete on the right; light background; final file exactly 1200 × 630; readable at 600 px wide.

ALT TEXT: The Kidney–Brain Axis — thinking, memory, and kidney disease: a kidney and a brain linked by shared blood vessels, a guide by W Rivero, MD

FIGURE CAPTION (fig-desc, EN): Not applicable (hero or OG image).

OG WIDTH: 1200
OG HEIGHT: 630


---

## 002 · Organ-crosstalk sigil

IMAGE NUMBER: 002
PRIORITY: P0
SECTION PLACEMENT: Patients · The Big Picture (#what) — slot 01 already wired
SLOT STATUS: Slot wired
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-01-kidney-brain-crosstalk.png
STAGE 1 SKILL: williamriveromd-organ-crosstalk-sigil-graphic (labeled variant)
ARCHETYPE: Organ-crosstalk sigil
AUDIENCE: Patients and families
READING LEVEL: Five short labels of 3–7 words each; plain words, no medical terms.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: monoline organ icons with dotted loop arrows
- 3D component graphics: soft shading only
- algorithm/flowchart: none
PURPOSE: Give readers a simple mental map: four links from kidney to brain, and one link back from thinking problems to kidney care.
KEY CONCEPTS: shared small blood vessels; wastes the kidneys clear less well; blood-pressure swings during dialysis; medicines that build up; feedback loop

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Create a simple medical organ-crosstalk sigil illustration featuring the brain and the kidneys, landscape.

ORGANS: a human brain at top center; a pair of kidneys at bottom center, symmetric.

RELATIONSHIP: Four curved arrows flow from the kidneys up toward the brain like the petals of a calm loop, each with one short label set in Inter, dark slate, large enough to read on a phone: "Shared small blood vessels" (SOLID line), "Wastes the kidneys clear less well" (DOTTED line), "Blood-pressure swings during dialysis" (SOLID line), "Medicines that build up" (SOLID line). One thinner return arrow runs down the right side from the brain back to the kidneys, labeled "Thinking problems can make kidney care harder", closing the circle.

STYLE: Minimal clinical line art with gently illustrated, softly shaded monoline strokes (not flat clip art), soft teal-blue palette (#1a6b72, slate, pale gray) with a muted renal red accent on the vessels, white background, clean rounded organ shapes, balanced sigil-like composition, generous whitespace, no photorealism, no 3D rendering. All text in Inter only. A small legend bottom-left: solid line = "Seen in people", dotted line = "Still being studied".

OUTPUT: High-resolution, publication-grade medical icon aesthetic. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No crowded or crossing arrows, no extra organs, no thick cartoon outlines, no glossy icons.
```

QUALITY CHECK: Exactly five labels plus a two-item legend, spelled correctly in Inter; one dotted arrow (wastes) and three solid; one return arrow; brain on top, kidneys below; attribution bottom-right.

ALT TEXT: Minimal line-art diagram of a kidney and a brain joined by arrows labeled shared small blood vessels, wastes the kidneys clear less well, blood-pressure swings during dialysis, and medicines that build up, with a return arrow showing that thinking problems can make kidney care harder.

FIGURE CAPTION (fig-desc, EN): The kidneys and brain are linked through shared small blood vessels, wastes the kidneys clear less well, blood-pressure swings during dialysis, and medicines. The return arrow matters too: thinking problems can make it harder to manage medicines and appointments.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 003 · Multi-panel educational infographic (6 scenes)

IMAGE NUMBER: 003
PRIORITY: P1
SECTION PLACEMENT: Patients · What People Notice (#signs) — NEW slot after the bullet list
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-06-everyday-signs.png
STAGE 1 SKILL: williamriveromd-infographic-skill (multi-panel educational)
ARCHETYPE: Multi-panel educational infographic (6 scenes)
AUDIENCE: Patients and families, including readers with limited schooling
READING LEVEL: Six captions of 3–6 words; each scene must make sense with the caption covered.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: soft illustrated Filipino people in everyday scenes
- 2D infographic: six-panel grid with one caption each
- 3D component graphics: small props (pill box, calendar)
- algorithm/flowchart: none
PURPOSE: Help families recognize what thinking changes look like in daily life — before anyone uses a medical word.
KEY CONCEPTS: mixed-up medicines; missed appointments; bills and forms harder; losing the thread of a conversation; foggy after dialysis; family notices first

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Patient-education infographic, landscape, white background (#ffffff), a clean 3 × 2 grid of six rounded cards on very light teal (#eef6f7). Each card holds one softly illustrated, semi-realistic scene (warm editorial illustration, gentle shading, not cartoon) of Filipino adults in a bright home or clinic, plus ONE short caption beneath it set in Nunito Sans, navy (#0f1e2e), large and phone-readable:
1. An older woman holding two pill bottles with a puzzled look beside an open weekly pill box — caption "Mixing up medicines".
2. A wall calendar with a dialysis day circled and a clock showing a late hour, a man hurrying with his bag — caption "Missing appointments".
3. A man at a table looking at a utility bill and a form, pen paused — caption "Bills and forms feel harder".
4. Two friends talking on a bench; one looks lost mid-sentence, small dotted speech bubble trailing off — caption "Losing the thread".
5. A woman leaving a dialysis unit, hand on forehead, soft hazy overlay — caption "Foggy after dialysis".
6. An adult daughter gently talking with her father at home — caption "Family notices first".
Top header in Inter bold, navy: "What thinking changes can look like". Calm, respectful, never mocking; people shown with dignity. Vary ages, sexes, body types, and clothing across all six scenes so no face repeats. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No exaggerated confusion, no question marks floating over heads, no elderly stereotypes, no duplicated faces, no more than one caption per card.
```

QUALITY CHECK: Six cards, six captions exactly as listed, one header; every scene understandable without its caption; respectful tone; diverse cast; attribution present.

ALT TEXT: Six illustrated everyday scenes of thinking changes in kidney disease: mixing up medicines, missing appointments, finding bills and forms harder, losing the thread of a conversation, feeling foggy after dialysis, and family noticing first.

FIGURE CAPTION (fig-desc, EN): Thinking changes in kidney disease usually show up in everyday tasks first: medicines, appointments, paperwork, conversations, and how you feel after dialysis. Family members often notice before you do.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 004 · Single comparison figure — traffic-light timeline

IMAGE NUMBER: 004
PRIORITY: P0
SECTION PLACEMENT: Patients · What People Notice (#signs) — NEW slot above the speed-of-change table
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-07-speed-of-change.png
STAGE 1 SKILL: williamriveromd-simple-figure (step sequence / comparison)
ARCHETYPE: Single comparison figure — traffic-light timeline
AUDIENCE: Patients and families
READING LEVEL: Three bands, each with a time phrase and a 2–4 word action. Color plus icon plus words, so it works for color-blind readers.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three-band horizontal timeline with icons
- 3D component graphics: none
- algorithm/flowchart: simple flow
PURPOSE: Teach the single most important safety rule in the guide: how fast the change happened decides how fast to act.
KEY CONCEPTS: minutes to hours = emergency; hours to days = same-day review; weeks to months = next visit

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Single clean patient-education figure, landscape, white background. A wide horizontal timeline arrow runs left to right, divided into three rounded bands, each with a simple shaded icon above and two lines of text below, set in Inter:
LEFT band, clinical red (#b91c1c) with an ambulance icon: "Minutes to hours" / "Emergency now — call 911".
MIDDLE band, amber (#b8860b) with a phone-and-calendar icon: "Hours to days, or comes and goes" / "See a doctor today".
RIGHT band, teal (#1a6b72) with a notebook icon: "Weeks to months" / "Tell your team at your next visit".
Above the timeline, a title in Inter bold navy: "How fast did it change?". Under the red band only, a small line in navy: "Drooping face, weak arm, slurred speech, seizure, or hard to wake". Each band also carries a distinct shape cue (triangle, circle, square) so meaning does not rely on color alone. Generous whitespace, calm and clear, softly shaded icons (not flat clip art). Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No numbers, no clocks with specific times, no medical jargon, no gore or distressed faces.
```

QUALITY CHECK: Three bands in red, amber, teal with icons and distinct shapes; text exactly as listed and spelled correctly; title present; readable at 360 px wide (phone); attribution present.

ALT TEXT: Timeline in three colored bands: minutes to hours means an emergency and calling 911; hours to days or confusion that comes and goes means seeing a doctor today; weeks to months means telling your kidney team at the next visit.

FIGURE CAPTION (fig-desc, EN): How fast a change happened tells you how fast to act. Sudden change is an emergency; change over days needs a same-day check; slow change over months should be raised at your next visit.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 005 · Icon-array data figure

IMAGE NUMBER: 005
PRIORITY: P1
SECTION PLACEMENT: Patients · How Common (#common) — NEW slot after the first paragraph
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-08-how-common-icon-array.png
STAGE 1 SKILL: williamriveromd-simple-figure (data icon array)
ARCHETYPE: Icon-array data figure
AUDIENCE: Patients and families
READING LEVEL: Counting icons replaces percentages; phrases like "about 1 in 3" match the guide text.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: four rows of 12 person icons
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Make the prevalence numbers concrete for readers who struggle with percentages, without implying one dialysis type causes the difference.
KEY CONCEPTS: about 1 in 3 before dialysis; about 1 in 2 on hemodialysis; about 2 in 5 on peritoneal dialysis; about 1 in 4 after transplant; groups not individuals

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Clean patient-education icon-array figure, landscape, white background. Title in Inter bold navy (#0f1e2e): "How many people with kidney disease have some thinking problems on testing?". Four horizontal rows, each with exactly 12 simple, softly shaded person icons (identical gender-neutral figures); filled icons in teal (#1a6b72), unfilled icons in pale gray (#d9dee5). Each row has a label on the left and a phrase on the right, set in Inter:
Row 1 — label "Before dialysis": 4 of 12 filled; phrase "About 1 in 3".
Row 2 — label "Hemodialysis": 6 of 12 filled; phrase "About 1 in 2".
Row 3 — label "Peritoneal dialysis": 5 of 12 filled; phrase "About 2 in 5".
Row 4 — label "After kidney transplant": 3 of 12 filled; phrase "About 1 in 4".
Footer line in small slate text: "Rough averages from 50 studies. Groups differ in age and health, so the rows do not show that one treatment causes more problems." Filled icons always start from the left. Generous spacing; no other numbers. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No percentages, no bar charts, no ranking language like "worst" or "best", no faces on the icons, no miscounted icons.
```

QUALITY CHECK: Exactly 12 icons per row; filled counts 4, 6, 5, 3 from the left; labels and phrases exactly as listed; footer present; attribution present. COUNT THE ICONS before accepting the image.

ALT TEXT: Icon array: about 1 in 3 people with kidney disease before dialysis, about 1 in 2 on hemodialysis, about 2 in 5 on peritoneal dialysis, and about 1 in 4 after a kidney transplant had some thinking problems on testing.

FIGURE CAPTION (fig-desc, EN): Across 50 studies, thinking problems on testing were common at every stage of kidney disease. These are rough group averages; they do not predict what will happen to you, and they do not show that one kind of dialysis causes more problems.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 006 · Biomedical mechanism figure — patient labels

IMAGE NUMBER: 006
PRIORITY: P0
SECTION PLACEMENT: Patients · Why It Happens (#why) — slot 02 already wired
SLOT STATUS: Slot wired
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-02-four-pathways.png
STAGE 1 SKILL: williamriveromd-biomedical-mechanism-figure (patient-language labels)
ARCHETYPE: Biomedical mechanism figure — patient labels
AUDIENCE: Patients and families (also readable by clinicians)
READING LEVEL: Inset titles of 2–4 words; at most two plain callouts per inset; a solid/dashed legend explains certainty.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: labeled panels and arrows
- 3D component graphics: softly shaded semi-3D kidney, brain, vessels
- algorithm/flowchart: bottom summary flow
PURPOSE: Explain the four overlapping causes in plain words while visibly separating what is proven from what is still a theory.
KEY CONCEPTS: shared vessel damage; wastes from the gut that dialysis removes poorly; blood-flow dips during dialysis; medicines that linger; several small causes add up

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Create a publication-grade biomedical mechanism schematic, landscape, in a softly shaded illustrated review-article style (gentle semi-3D shading, not flat clip art), white background, muted clinical palette, clean sans-serif labels set in Inter, thin dashed connector lines.

Topic: Why kidney disease can affect thinking. Disease context: chronic kidney disease and dialysis.

Organ-level panel (left third): a simplified kidney labeled "Kidney disease" connected by a vertical blood vessel to a simplified brain labeled "Brain", with a small dashed connector box pointing right to four magnified insets.

Magnified mechanism panels (center and right, a 2 × 2 grid of dashed insets; each has a 2–4 word title and at most two short callouts):
1. "Shared vessel damage" — a small artery with a thickened wall shown in both organs; callouts "High blood pressure", "Diabetes". SOLID arrows.
2. "Wastes that build up" — gut bacteria producing small particles that cling to blood proteins and slip through a leaky brain-vessel wall; callouts "Made partly in the gut", "Removed poorly by dialysis". DASHED arrows.
3. "Blood-flow dips during dialysis" — a dialysis line removing fluid, with a small brain shown lighter in color; callout "Fast fluid removal". SOLID arrows.
4. "Medicines that linger" — a pill bottle with a slow, narrow kidney-clearance arrow; callouts "Some sleep and cold tablets", "Some nerve-pain pills". SOLID arrows.

Bottom summary flow: left pale-pink box "Several small causes add up"; center box "Find the ones we can treat"; right pale-blue box "Protect vessels, review medicines, adjust dialysis"; arrows left to right.

Legend bottom-left: solid arrow = "Seen in people"; dashed arrow = "Still being studied". Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No chemical structures, no molecule names, no "poison" imagery, no implication that one cause explains everyone, no more than two callouts per inset.
```

QUALITY CHECK: Four insets with ≤2 callouts each, labels exactly as listed in Inter; inset 2 dashed, insets 1, 3, 4 solid; bottom flow and legend present; readable at 860 px wide; attribution present.

ALT TEXT: Mechanism figure in plain language: a kidney and brain with four magnified panels showing shared blood-vessel damage, wastes from the gut that dialysis removes poorly, blood flow to the brain dipping during dialysis fluid removal, and medicines that linger, ending in a flow from several small causes to finding the treatable ones.

FIGURE CAPTION (fig-desc, EN): Four overlapping pathways link kidney disease and thinking problems. Solid arrows show links seen in people; dashed arrows show ideas still being tested.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 007 · Illustrated procedural scene with two overlays

IMAGE NUMBER: 007
PRIORITY: P0
SECTION PLACEMENT: Patients · If You Are on Dialysis (#dialysis) — slot 03 already wired
SLOT STATUS: Slot wired
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-03-dialysis-brain-perfusion.png
STAGE 1 SKILL: williamriveromd-infographic-skill (access / procedural education scene)
ARCHETYPE: Illustrated procedural scene with two overlays
AUDIENCE: Patients and families
READING LEVEL: Two overlay labels and one action caption; no numbers on the charts.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: semi-photoreal illustrated patient and nurse
- 2D infographic: two simple overlays (gauge and trace)
- 3D component graphics: translucent head showing brain blood flow
- algorithm/flowchart: none
PURPOSE: Show that fast fluid removal can lower brain blood flow for a while, sometimes without an obvious blood-pressure drop, and that speaking up during treatment matters.
KEY CONCEPTS: fluid removal; brain blood flow; modest BP dip versus larger brain-flow dip; nurse check-in

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Landscape semi-photorealistic medical illustration, bright modern Philippine hemodialysis unit, soft daylight, white walls, calm documentary tone. A Filipino woman in her early fifties with short wavy graying hair, rectangular glasses, and a mustard cardigan reclines in a dialysis chair; an arteriovenous fistula in her left forearm is connected to two blood lines running to a single dialysis machine with an upright dialyzer. A Filipino male dialysis nurse in his thirties in navy scrubs crouches beside her at eye level, asking how she feels. Her head shows a subtle translucent overlay revealing the brain, with a soft teal-to-pale gradient of blood flow that is slightly lighter toward the top, suggesting a temporary dip.

Two clean overlays on the right side, set in Inter:
1. A rounded gauge labeled "Fluid removal" with the needle in the upper third.
2. A small line chart labeled "During treatment" with two lines: a solid navy line labeled "Blood pressure" that dips only gently mid-session, and a dotted teal line labeled "Brain blood flow" that dips more. No numbers, no axis values.
One short caption at bottom center in Nunito Sans: "Feel dizzy, foggy, or not right? Tell the team."

Palette harmonizes with teal #1a6b72 and navy #0f1e2e on a light background. Correct dialysis equipment: one machine, two blood lines, upright dialyzer. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No blood spills, no fainting or distress, no numbers on charts, no "safe zone" coloring, no extra people, no garbled equipment, no second dialyzer.
```

QUALITY CHECK: Exactly two overlays and one caption, spelled correctly; the BP line dips less than the brain-flow line; fistula, lines, and dialyzer plausible; patient and nurse visibly different from earlier guides; attribution present.

ALT TEXT: Illustration of a woman on a hemodialysis chair with a transparent head showing brain blood flow, a fluid-removal gauge, and a chart in which blood pressure dips only slightly while brain blood flow dips more, with a nurse checking in.

FIGURE CAPTION (fig-desc, EN): During hemodialysis, fluid is removed from the blood. If too much is removed too quickly, blood flow to the brain can dip for a while, sometimes without an obvious drop on the blood-pressure monitor.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 008 · Single step-sequence figure — symptom-timing strip

IMAGE NUMBER: 008
PRIORITY: P2
SECTION PLACEMENT: Patients · If You Are on Dialysis (#dialysis) — NEW slot after the bullet list
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-09-dialysis-day-diary.png
STAGE 1 SKILL: williamriveromd-simple-figure (step sequence)
ARCHETYPE: Single step-sequence figure — symptom-timing strip
AUDIENCE: Patients on hemodialysis and caregivers
READING LEVEL: Three headings and short prompts; designed to be copied by hand into a notebook.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three-panel day strip with tick boxes
- 3D component graphics: small shaded icons
- algorithm/flowchart: none
PURPOSE: Turn "notice the timing" into something a patient can actually do: a simple before/during/after record.
KEY CONCEPTS: before, during, after dialysis; what you felt; how long it lasted; bring it to the team

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Single clean patient-education figure, landscape, white background. Title in Inter bold navy: "When does the fog happen?". Three large rounded panels side by side, joined by a gentle left-to-right arrow, each with a softly shaded icon at top and three short prompt lines with empty tick boxes, set in Nunito Sans:
Panel 1, icon of a sunrise and a bag: heading "Before dialysis" — "Foggy or slow?" / "Slept well?" / "Took all medicines?".
Panel 2, icon of a dialysis chair: heading "During dialysis" — "Dizzy or yawning?" / "Cramps?" / "Told the nurse?".
Panel 3, icon of a house: heading "After dialysis" — "Foggy or very tired?" / "How many hours?" / "Better by bedtime?".
Bottom banner in teal: "Bring this to your kidney team." Calm teal (#1a6b72) and soft gray palette, generous whitespace. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No numbers, no medical terms, no clock times, no crowded text.
```

QUALITY CHECK: Three panels with exactly the headings and prompts listed, each prompt with an empty tick box; banner present; readable on a phone; attribution present.

ALT TEXT: Three-panel checklist for a dialysis day: before dialysis, during dialysis, and after dialysis, each with simple questions about fogginess, dizziness, sleep, and tiredness, ending with a reminder to bring the notes to the kidney team.

FIGURE CAPTION (fig-desc, EN): Noting when fogginess happens — before, during, or after dialysis — helps your team decide whether fluid removal, session length, sleep, or medicines are part of the cause.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 009 · Photorealistic still life with minimal labels

IMAGE NUMBER: 009
PRIORITY: P1
SECTION PLACEMENT: Patients · Medicines to Review (#medicines) — NEW slot before the medicine table
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-10-medicine-bag-check.png
STAGE 1 SKILL: williamriveromd-infographic-skill (photorealistic still life)
ARCHETYPE: Photorealistic still life with minimal labels
AUDIENCE: Patients and families
READING LEVEL: Four 2–4 word tags plus one action line; packaging carries no readable brand text.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: photorealistic still life
- 2D infographic: four small label tags
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Show what "bring every medicine" actually means, including the over-the-counter products people forget.
KEY CONCEPTS: prescription bottles; cold and allergy tablets; sleep aids; herbal products; bring them all

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Photorealistic overhead still life, landscape, on a clean light wooden table in soft daylight (bright, airy, never dark). A woven market bag (bayong) lies open, spilling out neatly arranged items: several prescription pill bottles with plain unreadable labels, a strip of generic cold-and-allergy tablets in a blister pack, a small box of sleep aid tablets, a bottle of herbal capsules, and a handwritten medicine list on lined paper (handwriting suggested but not legible). Four small rounded label tags with thin leader lines, set in Inter, navy on white: "Prescription medicines", "Cold and allergy tablets", "Sleep aids", "Herbal products". Bottom banner in teal (#1a6b72) with white Inter text: "Bring every medicine to your visit". No readable brand names or real packaging copy anywhere. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No readable brand names, no real product packaging, no loose pills scattered messily, no syringes, no alcohol.
```

QUALITY CHECK: Four tags and one banner exactly as listed; no readable brand text on any item; bright light background; attribution present.

ALT TEXT: Overhead photo of a woven market bag spilling out prescription bottles, cold and allergy tablets, sleep aids, herbal capsules, and a handwritten medicine list, with the reminder to bring every medicine to the visit.

FIGURE CAPTION (fig-desc, EN): Bring every medicine to your visit, including cold and allergy tablets, sleep aids, and herbal products. Some of these stay in the body longer when the kidneys are weak and can cloud thinking.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 010 · Circular workflow / action wheel

IMAGE NUMBER: 010
PRIORITY: P1
SECTION PLACEMENT: Patients · What Helps Today (#protect) — NEW slot after the intro paragraph
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-11-protect-brain-and-kidneys.png
STAGE 1 SKILL: williamriveromd-infographic-skill (circular workflow)
ARCHETYPE: Circular workflow / action wheel
AUDIENCE: Patients and families
READING LEVEL: Eight segments, 2–4 words each; icon carries the meaning.
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: eight-segment wheel with icons
- 3D component graphics: small shaded central organ pair
- algorithm/flowchart: none
PURPOSE: One memorable picture of the eight everyday steps that protect both organs, matching the bullet list in the guide.
KEY CONCEPTS: blood pressure; blood sugar; kidney medicines; move daily; hearing and eyesight; stay connected; sleep and mood; treat anemia

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Square circular-workflow infographic on a white background. At the center, a small softly shaded semi-3D brain above a pair of kidneys inside a pale-teal (#eef6f7) circle labeled in Inter bold navy "Protect both". Around it, a ring of eight equal rounded segments in alternating soft teal and soft green tints, each with one simple shaded icon and a 2–4 word label in Inter, navy:
1. blood-pressure cuff — "Control blood pressure"
2. glucose meter — "Steady blood sugar"
3. pill box — "Take kidney medicines"
4. walking shoes — "Move every day"
5. ear and glasses — "Check hearing and eyes"
6. two people talking — "Stay connected"
7. moon and smile — "Sleep and mood"
8. red blood drop — "Treat anemia"
Thin curved arrows link the segments clockwise. Generous spacing so every label is readable on a phone. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No numbers or targets, no drug names, no brand logos, no food items, no crowded icons.
```

QUALITY CHECK: Exactly eight segments with the labels listed, spelled correctly; central organs and "Protect both" label present; readable at 360 px; attribution present.

ALT TEXT: Circular action wheel around a brain and kidneys labeled protect both, with eight steps: control blood pressure, steady blood sugar, take kidney medicines, move every day, check hearing and eyes, stay connected, sleep and mood, and treat anemia.

FIGURE CAPTION (fig-desc, EN): The steps that protect your blood vessels and kidneys are also sensible for your brain. None is proven to prevent memory problems on its own, but each is worth doing for your health.

OG WIDTH: 1024
OG HEIGHT: 1024


---

## 011 · Evidence ladder — four-step comparison

IMAGE NUMBER: 011
PRIORITY: P1
SECTION PLACEMENT: Patients · What Is Being Studied (#research) — NEW slot before the research table
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-12-evidence-ladder.png
STAGE 1 SKILL: williamriveromd-simple-figure (comparison panel)
ARCHETYPE: Evidence ladder — four-step comparison
AUDIENCE: Patients and families (works for clinicians too)
READING LEVEL: Four step names and 2–4 short items per step; explains certainty without the word "evidence".
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: four-step staircase with icons
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Help readers judge headlines and products: what is promising, what failed, and what is not for memory at all.
KEY CONCEPTS: promising signals; needs confirmation; did not help thinking; not for memory

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Clean patient-education figure, landscape, white background. Title in Inter bold navy: "New treatments: how sure are we?". A gentle four-step staircase rising left to right; each step is a rounded card with an icon, a heading, and 2–3 short items in Nunito Sans:
Step 1 (lowest, soft gray, icon: crossed-out brain): heading "Not for memory" — "Detox products", "Most supplements".
Step 2 (soft red tint, icon: thumbs-sideways): heading "Did not help thinking" — "Cooler dialysate", "More sessions alone", "Semaglutide in Alzheimer disease".
Step 3 (soft amber tint, icon: magnifying glass): heading "Needs confirmation" — "B vitamins (one study)".
Step 4 (highest, soft teal tint, icon: seedling): heading "Promising" — "Exercise plus brain training", "Hemodiafiltration".
A small note under the staircase in slate: "Promising does not mean proven. Ask your team before trying anything new." Calm palette, softly shaded icons, generous whitespace. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No percentages, no trial names other than those listed, no brand names, no implication that any item is a cure.
```

QUALITY CHECK: Four steps with headings and items exactly as listed; the "Promising" step is the highest; note present; spelled correctly; attribution present.

ALT TEXT: Four-step evidence ladder: not for memory (detox products, most supplements); did not help thinking (cooler dialysate, more sessions alone, semaglutide in Alzheimer disease); needs confirmation (B vitamins, one study); promising (exercise plus brain training, hemodiafiltration).

FIGURE CAPTION (fig-desc, EN): Not every new treatment is equally proven. Exercise with brain training and hemodiafiltration show promising signals; others did not help thinking or still need confirmation. Promising does not mean proven.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 012 · Photorealistic editorial scene

IMAGE NUMBER: 012
PRIORITY: P2
SECTION PLACEMENT: Patients · For Families (#family) — NEW slot after the bullet list
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-13-family-support.png
STAGE 1 SKILL: williamriveromd-infographic-skill (photorealistic editorial scene)
ARCHETYPE: Photorealistic editorial scene
AUDIENCE: Families and caregivers
READING LEVEL: No text; the scene models the behaviors described in the section.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: photorealistic Filipino family scene
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Model supportive caregiving — pill organizer, simple written plan, teach-back — with dignity for the patient.
KEY CONCEPTS: pill organizer; teach-back; written plan; patient stays in charge

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Photorealistic medical editorial photograph, landscape, bright Filipino home living room in morning daylight, white and pale wood interior. A Filipina teenager of about 17 in a school-club T-shirt and a ponytail sits beside her grandfather, a lean man in his late seventies with close-cropped white hair, reading glasses pushed up, and a light blue barong-style polo. He holds a weekly pill organizer and is explaining the morning slots back to her in his own words while she listens and points to a simple handwritten plan on an index card (writing suggested but not legible). A phone with an alarm screen (no readable text) rests on the table beside a glass of water. Over-the-shoulder camera from behind the granddaughter, shallow depth of field, warm and respectful mood: he is clearly the one in charge of his medicines. Natural skin texture, calm expressions. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No readable text on the card or phone, no dining-table meal scene, no teal polo, no beige blouse, no patronizing body language, no hospital setting.
```

QUALITY CHECK: Two people only, visibly different from earlier guide casts; pill organizer and index card plausible; no readable text except the attribution; bright light setting; attribution present.

ALT TEXT: Photo of a Filipino grandfather explaining his weekly pill organizer to his teenage granddaughter, who points to a simple handwritten plan, with a phone alarm and a glass of water on the table.

FIGURE CAPTION (fig-desc, EN): Simple tools help: a weekly pill organizer, a short written plan, phone reminders, and "teach-back," where the patient explains the plan in their own words. The patient stays in charge.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 013 · Single data figure — point estimates with 95% CIs

IMAGE NUMBER: 013
PRIORITY: P1
SECTION PLACEMENT: Clinicians · Epidemiology (#md-epi) — NEW slot after the prevalence table
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-14-prevalence-by-modality.png
STAGE 1 SKILL: williamriveromd-simple-figure (data figure)
ARCHETYPE: Single data figure — point estimates with 95% CIs
AUDIENCE: Clinicians
READING LEVEL: Clinician figure; every number must match the guide table exactly.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: horizontal dot-and-whisker chart
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Show uncertainty honestly: overlapping intervals, high heterogeneity, and no modality effect implied.
KEY CONCEPTS: pooled prevalence with 95% CI; common 0–100% axis; I² 99%; not a modality effect

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Publication-grade forest-style dot-and-whisker chart, landscape, white background, set in IBM Plex Sans. Title in bold navy: "Pooled prevalence of cognitive impairment in CKD". A single horizontal axis from 0% to 100% with light gridlines at every 10% and tick labels at 0, 20, 40, 60, 80, 100%. Five rows, each with a teal (#1a6b72) dot for the estimate and a thin horizontal whisker for the 95% confidence interval, with the values printed to the right of each row:
"Nondialysis CKD" — 32% (25–38%)
"Hemodialysis" — 53% (38–69%)
"Peritoneal dialysis" — 39% (26–53%)
"Kidney transplant" — 26% (15–38%)
"All CKD" — 40% (33–46%), drawn as a navy diamond, separated from the rows above by a thin line.
Footer in small slate text: "Random-effects meta-analysis of 50 studies (25,289 adults); I² = 99%; study-defined impairment, not dementia. Differences between rows are not treatment effects." Dot and whisker positions must be drawn to scale on the 0–100% axis. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No 3D bars, no color-coding that ranks modalities, no rounding or altering the numbers, no extra rows.
```

QUALITY CHECK: All five estimates and intervals exactly as listed and plotted to scale (check that whiskers for HD span 38–69%); diamond for the overall row; footer present; attribution present. If the model mis-plots positions, regenerate or build this chart from data instead.

ALT TEXT: Dot-and-whisker chart of pooled prevalence of cognitive impairment: nondialysis CKD 32% (25–38%), hemodialysis 53% (38–69%), peritoneal dialysis 39% (26–53%), kidney transplant 26% (15–38%), and all CKD 40% (33–46%), with a note that I-squared was 99% and row differences are not treatment effects.

FIGURE CAPTION (fig-desc, EN): Pooled prevalence estimates with 95% confidence intervals on a common 0–100% axis (Zhang et al., 2024). Heterogeneity was extreme, and selection differs by modality, so the rows describe screen-defined burden, not the effect of a treatment.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 014 · Biomedical mechanism figure — clinician

IMAGE NUMBER: 014
PRIORITY: P0
SECTION PLACEMENT: Clinicians · Mechanisms (#md-mechanisms) — slot 04 already wired
SLOT STATUS: Slot wired
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-04-mechanism-panels.png
STAGE 1 SKILL: williamriveromd-biomedical-mechanism-figure (clinician)
ARCHETYPE: Biomedical mechanism figure — clinician
AUDIENCE: Clinicians
READING LEVEL: Clinician vocabulary; maximum three labels per panel.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: four mechanism panels and a convergence box
- 3D component graphics: softly shaded semi-3D vessel, blood–brain barrier, middle cerebral artery
- algorithm/flowchart: convergence arrows
PURPOSE: Clinician-level view of the four converging pathways with line style coding evidence strength.
KEY CONCEPTS: albuminuria and WMH; IS/PCS, AhR, BBB; MCA velocity and rSO₂ during UF; renally cleared CNS-active drugs; executive dysfunction

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Create a publication-grade biomedical mechanism schematic, landscape, softly shaded illustrated review-article style (gentle semi-3D, not flat clip art), white background, muted clinical palette, clean sans-serif labels set in IBM Plex Sans, thin dashed panel borders.

Organ-level panel (far left): a kidney labeled "CKD" and a brain labeled "Cognition" linked by a shared arterial tree.

Four dashed magnified panels (center, 2 × 2):
1. "Small-vessel disease" — a glomerulus with albumin leak labeled "Albuminuria", mirrored by a periventricular brain slice with bright patches labeled "WMH, lacunes". SOLID arrow.
2. "Protein-bound solutes" — colon bacteria → particles labeled "IS / PCS" bound to albumin → "AhR signaling" → endothelium with gaps labeled "BBB dysfunction". DASHED arrows.
3. "Intradialytic hypoperfusion" — a dialyzer with a "UF" arrow; middle cerebral artery labeled "↓ MCA velocity"; a small forehead sensor labeled "↓ rSO₂"; a tiny note "BP predicts poorly". SOLID arrows.
4. "Drug accumulation" — a kidney with a narrowed clearance arrow; a capsule labeled "Renally cleared CNS-active drugs". SOLID arrow.

Bottom convergence: all four panels feed a central pale-pink box "Executive dysfunction · slower processing · attention deficits"; to its right a pale-blue box "Review contributors · protect vessels · individualize UF"; left-to-right arrows.

Legend: solid = "Human association"; dashed = "Mechanistic hypothesis". Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No invented pathways, no numeric thresholds, no dementia probabilities, no chemical structures, no more than three labels per panel.
```

QUALITY CHECK: Labels exactly as listed (WMH, IS / PCS, AhR, BBB, UF, MCA, rSO₂); panel 2 dashed, others solid; convergence and action boxes present; attribution present.

ALT TEXT: Clinician mechanism schematic with four panels: small-vessel disease linking albuminuria and white matter hyperintensities; gut-derived indoxyl sulfate and p-cresyl sulfate crossing a disrupted blood-brain barrier; transcranial Doppler flow velocity and cerebral oxygen saturation falling during ultrafiltration; and accumulation of renally cleared CNS-active drugs, converging on executive dysfunction.

FIGURE CAPTION (fig-desc, EN): Four converging pathways. Panels mark observed human associations with solid lines and mechanistic hypotheses with dashed lines; none implies that a single pathway explains decline in an individual patient.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 015 · Clinical algorithm (journal-style flat flowchart)

IMAGE NUMBER: 015
PRIORITY: P0
SECTION PLACEMENT: Clinicians · Acute Change (#md-acute) — slot 05 already wired
SLOT STATUS: Slot wired
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-05-acute-vs-progressive-algorithm.png
STAGE 1 SKILL: williamriveromd-algorithm-generator-skill (journal style, Mode B)
ARCHETYPE: Clinical algorithm (journal-style flat flowchart)
AUDIENCE: Clinicians
READING LEVEL: Clinician vocabulary; no numeric cutoffs.
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: full flat flowchart
PURPOSE: Tempo-first triage of a cognitive change in CKD or dialysis.
KEY CONCEPTS: stroke pathway; delirium screen (4AT; CAM-ICU or ICDSC in ICU); precipitant and drug search; uremic encephalopathy; structured assessment; screen timing versus dialysis; referral

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Create a polished journal-style clinical algorithm flowchart, portrait, white background, conservative flat flowchart style: rounded rectangles for actions, diamonds for decisions, thin dark-gray arrows, minimal muted pastel fills (pale red for emergency, pale amber for same-day, pale teal for routine), no icons, no 3D. Crisp navy sans-serif typography set in Inter. Title top-center in bold: "Cognitive change in CKD or dialysis".

Start node: "New or worsening change in thinking".
Decision 1 (diamond): "Sudden focal signs, speech change, seizure, or hard to wake?" → YES (red branch) → "Stroke or emergency pathway now — including during dialysis".
NO → Decision 2 (diamond): "Developed over hours to days, or fluctuating?" → YES (amber branch) → "Delirium screen: 4AT (ward, long-term care); CAM-ICU or ICDSC (ICU, recovery)" → "Search precipitants: infection, hypoxia, glucose, sodium, calcium, retention, drugs" → "Renally cleared drugs: baclofen, gabapentinoids, opioids, acyclovir, cefepime" → "Consider uremic encephalopathy or disequilibrium → nephrology".
NO → teal branch, weeks to months → "Function (IADLs) + collateral history" → "Reversible contributors: medicines, sleep, mood, hearing, anemia, labs" → "Validated screen in the patient's language, at a consistent time relative to dialysis" → Decision 3 (diamond): "Progressive, atypical, or function-limiting?" → YES → "Neurology, geriatrics, or psychiatry"; NO → "Simplify regimen, teach-back, caregiver support, planned review".

Footer note in small gray text: "A low score never overrides an observed acute change." Include a small professional footer reading "© renalcarematters.com" centered at the bottom in subtle gray (#6b7280), at least 70% opacity. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
No numeric cutoffs, no MoCA thresholds, no screening intervals, no photorealism, no people, no decorative icons, no dark background, no crossing arrows, no serif fonts, no misspellings, no boxes beyond those listed.
```

QUALITY CHECK: Three decision diamonds, three color-coded branches, every listed box present once, text spelled correctly in Inter, unambiguous arrows; attribution at the bottom.

ALT TEXT: Clinical algorithm flowchart branching on tempo: sudden focal signs to the stroke pathway; hours-to-days fluctuating change to delirium screening with the 4AT and a precipitant search including drug toxicity and uremic encephalopathy; weeks-to-months decline to structured assessment with collateral history, reversible-contributor review, a validated cognitive screen at a consistent time relative to dialysis, and specialist referral when progressive or atypical.

FIGURE CAPTION (fig-desc, EN): Tempo-first pathway. Sudden focal signs go straight to the stroke pathway; fluctuating change is delirium until proven otherwise; gradual decline gets a structured, collateral-informed assessment.

OG WIDTH: 1024
OG HEIGHT: 1536


---

## 016 · Single concept schematic — testing window across the dialysis week

IMAGE NUMBER: 016
PRIORITY: P1
SECTION PLACEMENT: Clinicians · Assessment (#md-assessment) — NEW slot after the "Timing relative to dialysis" paragraph
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-15-testing-window-dialysis-cycle.png
STAGE 1 SKILL: williamriveromd-simple-figure (concept schematic)
ARCHETYPE: Single concept schematic — testing window across the dialysis week
AUDIENCE: Clinicians and dialysis nurses
READING LEVEL: Clinician vocabulary; the curve is explicitly schematic with no y-axis values.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: weekly timeline with a schematic curve
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Make "test at a consistent, stable time" concrete by showing where cognition dips across the dialysis week and where serial tests should sit.
KEY CONCEPTS: intradialytic trough; post-dialysis recovery; non-dialysis day or pre-dialysis window; match the timing for serial tests; avoid testing during acute illness

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Clean clinician schematic, landscape, white background, set in IBM Plex Sans. A horizontal weekly timeline labeled Monday through Sunday, with three hemodialysis sessions shown as navy blocks on Monday, Wednesday, and Friday. Above it, a smooth SCHEMATIC teal curve labeled "Cognitive performance (schematic)" with NO y-axis numbers: it dips during each session block, recovers over the following hours, and is highest on non-dialysis days. Two shaded green windows highlight "Preferred testing window" — one on a non-dialysis day (Tuesday or Thursday) and one just before a session. A shaded amber band over a session block reads "Avoid: intradialytic trough". A small red-outlined note on the right: "Do not use a score from acute illness as a baseline." A bottom line in navy: "For serial tests, keep the same day type, timing, language, and instrument version." Calm, uncluttered, generous whitespace. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No y-axis values, no score numbers, no MoCA cutoffs, no patient faces, no 3D.
```

QUALITY CHECK: Three sessions on Mon/Wed/Fri; curve dips at sessions and is labeled schematic with no numbers; two green windows, one amber band, one red note, one bottom line; attribution present.

ALT TEXT: Schematic weekly timeline of hemodialysis on Monday, Wednesday, and Friday with a cognitive performance curve that dips during sessions; preferred testing windows are marked on a non-dialysis day and just before a session, and the intradialytic trough is marked to avoid.

FIGURE CAPTION (fig-desc, EN): Schematic only. Cognition fluctuates across the dialysis cycle; for serial testing, keep the timing, instrument version, and language the same, ideally on a non-dialysis day or before treatment.

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 017 · Physiology figure — cerebral autoregulation curves

IMAGE NUMBER: 017
PRIORITY: P1
SECTION PLACEMENT: Clinicians · Dialysis Hemodynamics (#md-hd) — NEW slot after the "Three findings" paragraph
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-16-autoregulation-variability.png
STAGE 1 SKILL: williamriveromd-biomedical-mechanism-figure (physiology panel)
ARCHETYPE: Physiology figure — cerebral autoregulation curves
AUDIENCE: Clinicians
READING LEVEL: Clinician vocabulary; only two numbers, both from the cited study.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: two-panel physiology chart
- 3D component graphics: small shaded brain and dialyzer icons
- algorithm/flowchart: none
PURPOSE: Explain why a "normal" blood pressure can still mean cerebral hypoperfusion: the autoregulatory plateau differs between patients and shifts in chronic hypertension.
KEY CONCEPTS: autoregulation plateau; lower limit varies between patients; same MAP, different perfusion; BP poorly predicts cerebral desaturation

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Publication-grade physiology figure, landscape, softly shaded review-article style, white background, labels in IBM Plex Sans.
LEFT panel titled "Autoregulation differs between patients": x-axis "Mean arterial pressure" and y-axis "Cerebral blood flow", both WITHOUT numeric tick values. Three smooth sigmoid-plateau curves: a teal curve labeled "Patient A" whose plateau starts at a lower pressure; a navy curve labeled "Patient B" with a mid-position plateau; an amber curve labeled "Patient C (long-standing hypertension)" whose plateau is shifted to the right. A vertical dashed gray line labeled "Same intradialytic MAP" crosses all three: it sits on the plateau of A, at the shoulder of B, and on the falling limb of C, with small markers showing lower flow for C.
RIGHT panel titled "During hemodialysis": a small shaded dialyzer with an arrow labeled "Ultrafiltration", and two stacked mini-traces with no axis numbers — "Brachial BP" changing little and "Cerebral oxygenation" dipping. A callout box: "Cerebral desaturation in 23.5% of 635 sessions; BP predicted it poorly (pilot study)".
Calm palette (teal #1a6b72, navy #0f1e2e, amber #b8860b), generous whitespace. Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No numeric axis values, no target MAP number, no "safe zone" shading, no claims of stroke or dementia.
```

QUALITY CHECK: Three curves with the right-shifted curve labeled as hypertension; the dashed line hits plateau, shoulder, and falling limb respectively; only the one callout contains numbers (23.5%, 635); attribution present.

ALT TEXT: Physiology figure: three cerebral autoregulation curves show that the same mean arterial pressure during dialysis can sit on the plateau for one patient but on the falling limb for another with long-standing hypertension; a second panel shows brachial blood pressure changing little while cerebral oxygenation dips, with a note that desaturation occurred in 23.5 percent of 635 sessions and blood pressure predicted it poorly.

FIGURE CAPTION (fig-desc, EN): The lower limit of cerebral autoregulation varies between patients, so the same intradialytic blood pressure can protect one brain and underperfuse another. In a pilot study, blood pressure poorly predicted cerebral desaturation (MacEwen et al., 2017).

OG WIDTH: 1536
OG HEIGHT: 1024


---

## 018 · Clinician reference card

IMAGE NUMBER: 018
PRIORITY: P1
SECTION PLACEMENT: Clinicians · Medications (#md-meds) — NEW slot after the medication table
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-17-medication-review-card.png
STAGE 1 SKILL: williamriveromd-infographic-skill (clinician reference card)
ARCHETYPE: Clinician reference card
AUDIENCE: Clinicians and pharmacists
READING LEVEL: Dense clinician card; no doses, no stop instructions.
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: reference card with grouped rows
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: A printable bedside card for the most reversible contributor: CNS-active drugs that accumulate in CKD.
KEY CONCEPTS: drug classes; examples; kidney-relevant concern; action = review, never automatic stop

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Clinical reference card for clinicians, portrait, white background, soft gray (#f3f4f6) section cards, set in IBM Plex Sans with navy (#0f1e2e) headings and teal (#1a6b72) rules. Header in bold: "Cognition and medicines in CKD — review list". Eight compact rows, each with a class name in bold, examples, and one short concern:
"First-generation antihistamines" — diphenhydramine, chlorphenamine — "Anticholinergic; delirium in older adults"
"Other anticholinergics" — oxybutynin, tricyclic antidepressants — "Cumulative burden"
"Muscle relaxants" — baclofen — "Renally cleared; encephalopathy risk rises as eGFR falls"
"Gabapentinoids" — gabapentin, pregabalin — "Renally cleared; reduce dose; sedation, falls"
"Opioids" — morphine, codeine, tramadol — "Active metabolites accumulate"
"Sedative-hypnotics" — benzodiazepines, zolpidem — "Psychomotor slowing, falls"
"Antimicrobials and antivirals" — cefepime, acyclovir, valacyclovir — "Neurotoxicity with excess exposure"
"Others" — metoclopramide, lithium — "Extrapyramidal effects; narrow therapeutic index"
A teal footer band: "Action: review with prescriber or pharmacist. State eGFR or CrCl and modality. Do not stop abruptly." Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" centered at the bottom, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No doses, no mg values, no brand names, no "stop" icons, no pill photographs.
```

QUALITY CHECK: Eight rows exactly as listed, drug names spelled correctly; footer band present; no doses; attribution bottom-center.

ALT TEXT: Clinician reference card listing eight drug groups that can impair cognition in chronic kidney disease, with examples and concerns, and a footer advising review with the prescriber or pharmacist, stating eGFR or creatinine clearance and modality, and avoiding abrupt withdrawal.

FIGURE CAPTION (fig-desc, EN): Drug accumulation is the most reversible contributor. Review each CNS-active drug against current kidney function and modality; do not stop baclofen, benzodiazepines, or gabapentinoids abruptly.

OG WIDTH: 1024
OG HEIGHT: 1536


---

## 019 · Evidence map matrix

IMAGE NUMBER: 019
PRIORITY: P2
SECTION PLACEMENT: Clinicians · Emerging Therapies (#md-emerging) — NEW slot after the trials table
SLOT STATUS: New slot needed
FILE NAME: kidney-brain-axis-cognitive-dysfunction-ckd-18-emerging-evidence-map.png
STAGE 1 SKILL: williamriveromd-infographic-skill (clinician evidence matrix)
ARCHETYPE: Evidence map matrix
AUDIENCE: Clinicians
READING LEVEL: Clinician vocabulary; symbols replace numbers.
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: matrix with symbols
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: One glance at which interventions were tested against which kind of outcome — and that none reached a dementia endpoint.
KEY CONCEPTS: intervention × outcome class; design; direction of effect; no dementia endpoints

COPY-READY IMAGE GENERATOR GPT PROMPT:
```text
Clinician evidence-map matrix, landscape, white background, set in IBM Plex Sans. Title in bold navy: "Interventions for cognition in CKD: what has been measured". Columns (outcome class): "Objective cognitive test", "Patient-reported cognition", "Dementia diagnosis". Rows (intervention, with design in small gray text): "Exercise + cognitive training (RCT, 3 months)", "High-volume hemodiafiltration (RCT)", "Thiamin + folic acid (single RCT)", "Cooler dialysate (feasibility RCT)", "More frequent hemodialysis (RCTs)", "Kidney transplantation (cohorts)", "Semaglutide in early Alzheimer disease (RCTs, not CKD)".
Cell symbols with a legend: green filled circle = "Benefit signal"; gray open circle = "No benefit shown"; amber half circle = "Mixed or domain-specific"; dash = "Not measured".
Fill: Exercise + training — objective: green (secondary outcome; primary neutral, add a small footnote mark); patient-reported: dash; dementia: dash. Hemodiafiltration — objective: dash; patient-reported: green; dementia: dash. Thiamin + folic acid — objective: green with a small "needs replication" tag; others dash. Cooler dialysate — objective: gray; others dash. Frequent HD — objective: gray; others dash. Transplant — objective: amber; others dash. Semaglutide — objective: gray; dementia column: dash.
Footer: "No intervention has shown prevention of dementia in CKD. Footnote: primary executive-function outcome was neutral." Include a small, semi-transparent navy (#0f1e2e, about 70% opacity, 10–11px) attribution set in Inter reading "© renalcarematters.com" in the bottom-right corner, never covering content. No journal names, guideline acronyms, brand names, logos, or watermarks other than the attribution.
```

NEGATIVE INSTRUCTIONS:
```text
Avoid: dark, navy, charcoal, or black backgrounds; cartoon or clip-art style; flat generic vector icons with no shading; neon, HDR, or over-saturation; clutter; tiny unreadable labels; AI gibberish or misspelled text; serif or decorative fonts; unrealistic anatomy; distorted hands or faces; extra text beyond the labels listed; invented numbers, thresholds, or percentages; fear imagery (skulls, poison symbols, lightning in the brain). No numbers, no effect sizes, no p-values, no additional rows, no logos.
```

QUALITY CHECK: Seven rows, three columns, symbols placed exactly as specified; the dementia column is all dashes; legend and footer present; attribution present.

ALT TEXT: Evidence map of interventions for cognition in CKD against three outcome types: exercise plus cognitive training and thiamin plus folic acid show objective benefit signals, hemodiafiltration shows a patient-reported benefit, transplant is mixed, cooler dialysate, frequent hemodialysis, and semaglutide showed no benefit, and no intervention measured dementia prevention in CKD.

FIGURE CAPTION (fig-desc, EN): What each intervention has actually been tested against. Benefit signals so far are short-term, secondary, single-trial, or patient-reported; none has shown dementia prevention in CKD.

OG WIDTH: 1536
OG HEIGHT: 1024
