# Image Plan Blueprint and Prompt Pack: Getting Fit for a Kidney Transplant

**Guide:** `guides/transplant-prehabilitation.html` (dual-mode; patient EN/TL/CEB/KAP, clinician EN)
**Stage 1 output** for `williamriveromd-local-image-generator` (Stage 2). Paste each COPY-READY prompt into the Image Generator GPT: https://chatgpt.com/
**Skills used:** `williamriveromd-hero-vignette` (001), `williamriveromd-infographic-skill` (002, 11, 12, 18), `williamriveromd-simple-figure` (02, 05–10, 13, 14, 16, 17), `williamriveromd-biomedical-mechanism-figure` (15), `williamriveromd-organ-crosstalk-sigil-graphic` (19).
**Status:** Draft, 6 November 2026. Every number printed on an image is taken from the verified guide text; prompts that need no numbers carry none.

---

## Part A. Visual strategy

### A1. Goal

Make the guide understandable at a glance to a reader with elementary schooling, while still rewarding a nephrologist who reads every label. Each image teaches **one idea** that the paragraph next to it explains in words.

### A2. Design rules for readers of all educational levels

1. **Picture first, words second.** Every concept gets an icon, object, or body position before it gets a label. A reader who cannot read English should still get the gist from the picture.
2. **Seven words or fewer per label.** Patient images use short plain-English labels only. The guide's four-language captions (`fig-desc`) carry the translation, so on-image text stays minimal and never needs four versions.
3. **One idea per image.** If a figure needs two ideas, it becomes two figures.
4. **A fixed color meaning, used on every image:**

   | Color | Hex | Always means |
   |---|---|---|
   | Teal | `#1a6b72` | Move / exercise |
   | Renal green | `#1f7a4d` | Eat / safe / do this |
   | Soft purple | `#6c3d8e` | Mind / support |
   | Amber | `#b8860b` | Caution / ask your team |
   | Clinical red | `#b91c1c` | Stop / avoid |
   | Navy | `#0f1e2e` | Text, outlines |
   | Gray | `#9ca3af` | Not yet known / not tested |

5. **Familiar Filipino settings and foods:** a plain-wood chair, a banig mat, bangus and tilapia, tokwa, suha. The scenes are homes and dialysis units, not gyms.
6. **Honest images.** Nothing on any image promises a better transplant. Where the evidence stops, the image shows it (gray "not yet tested" zones).
7. **Data stays code-native.** Charts with trial numbers are drawn as SVG from the verified figures (A5), never by the image model, which garbles numbers.
8. **House rules on every prompt:**
   - light background only;
   - Inter, Manrope, or Nunito Sans, named explicitly;
   - `renalcarematters.com` attribution bottom-right (bottom-center on portrait);
   - no journal names, guideline acronyms, brands, or watermarks;
   - photorealistic people only in the hero, with flat illustrated people elsewhere so faces never repeat across the site.

### A3. Image map

P1 = needed before the guide goes live. P2 = core patient understanding. P3 = enrichment and clinician depth.

| # | File | Section | Audience | Archetype / skill | Size | Priority |
|---|---|---|---|---|---|---|
| 001 | `transplant-prehabilitation-vignette-hero.png` | Hero (patient) | Patients | Vignette hero, archetype J | 2048×2048 | P1 |
| 002 | `transplant-prehabilitation-og.png` | `<head>` share card | Mixed | OG card | 1200×630 | P1 |
| 02 | `transplant-prehabilitation-02-three-pillars.png` | `#what-prehab-is` | Patients | Simple figure E (3 cards) | 1792×1024 | P1 |
| 03 | `…-03-fitness-while-waiting.svg` | `#why-fitness` | Patients | **Code-native SVG (done)** | 1200×675 | Done |
| 04 | `…-04-diet-adherence-after-transplant.svg` | `#after-transplant` | Mixed | **Code-native SVG (done)** | 1200×675 | Done |
| 05 | `transplant-prehabilitation-05-reserve-tank.png` | `#why-fitness` intro | Patients | Simple figure B (analogy) | 1792×1024 | P2 |
| 06 | `transplant-prehabilitation-06-muscle-balance.png` | `#why-fitness` "What dialysis does to muscle" | Patients | Simple figure D (balance scale) | 1792×1024 | P2 |
| 07 | `transplant-prehabilitation-07-five-signs-frailty.png` | `#why-fitness` five signs | Patients | Simple figure E (icon card) | 1536×1152 | P2 |
| 08 | `transplant-prehabilitation-08-starter-week.png` | `#exercise-plan` after table | Patients | Simple figure E (week calendar) | 1792×1024 | P2 |
| 09 | `transplant-prehabilitation-09-chair-stand-talk-test.png` | `#exercise-plan` "How hard" | Patients | Simple figure C (steps) | 1792×1024 | P2 |
| 10 | `transplant-prehabilitation-10-fistula-arm.png` | `#exercise-plan` special situations | Patients | Simple figure B (do / don't) | 1792×1024 | P3 |
| 11 | `transplant-prehabilitation-11-protein-plate.png` | `#nutrition-before` | Patients | Infographic food matrix | 1536×1152 | P2 |
| 12 | `transplant-prehabilitation-12-habit-cycle.png` | `#keep-going` | Patients | Infographic circular workflow | 1024×1024 | P3 |
| 13 | `transplant-prehabilitation-13-after-transplant-plate.png` | `#after-transplant` | Patients | Simple figure B (before / after) | 1792×1024 | P2 |
| 14 | `transplant-prehabilitation-14-tacrolimus-food-safety.png` | `#after-transplant` food safety | Mixed | Simple figure E (avoid card) | 1024×1024 | P2 |
| 15 | `transplant-prehabilitation-15-uremic-muscle-mechanism.png` | `#md-frailty` physiology | Clinicians | Biomedical mechanism figure | 1792×1024 | P3 |
| 16 | `transplant-prehabilitation-16-clinician-pathway.png` | `#md-prescription` | Clinicians | Simple figure A (algorithm) | 1024×1536 | P3 |
| 17 | `transplant-prehabilitation-17-evidence-tiers.png` | `#md-evidence` appraisal | Clinicians (also patients) | Simple figure E (3 tiers) | 1792×1024 | P2 |
| 18 | `transplant-prehabilitation-18-delivery-models.png` | `#md-prescription` center vs home | Clinicians | Infographic reference card | 1536×1152 | P3 |
| 19 | `transplant-prehabilitation-19-kidney-muscle-sigil.png` | `#mind` or `#md-frailty` header | Mixed | Organ-crosstalk sigil | 1024×1024 | P3 |
| 20 | `…-20-frailmar-effects.svg` | `#md-evidence` table | Clinicians | **Code-native SVG (to build)** | 1200×675 | P2 |

### A4. Reading path

A reader who only looks at the pictures, in page order, should come away with the whole message:

1. Surgery takes reserve (05).
2. Dialysis drains muscle (06).
3. These are the warning signs (07).
4. Three pillars rebuild it (02).
5. This is your week (08), and this is how to do the key move and how hard to push (09). Protect your fistula (10).
6. This is what to eat (11).
7. Keep it a habit, because gains fade (03, 12).
8. After transplant the plate changes (13, 04), and these foods are now dangerous (14).

The clinician path is:

1. The mechanism (15).
2. What is proven, what didn't change, and what is untested (17, 20).
3. How to run it (16, 18).

### A5. Code-native figures (do not send to the image model)

- **03 Fitness while waiting:** done; labeled "illustration only, not study data."
- **04 Diet adherence after transplant:** done. The bars show fruit 22%, vegetables 28%, fiber 26%, and plant protein 12% (Doorenbos 2026).
- **20 FRAILMar effects (to build):** a point-estimate and 95% CI dot plot with one row per outcome:
  - workload +12.8 W (3.4–22.2);
  - grip +1.8 kg (0.7–2.8);
  - rectus femoris +1.2 mm (0.3–2.0);
  - three rows marked "no significant change": VO₂ max, 6-minute walk, frailty status.

  Each row gets its own axis because the units differ. This chart is the visual heart of the evidence section, and it is built from the verified numbers only.

### A6. Wiring after generation

Save each PNG to `images/` and create a matching `.webp`. In the guide, add a `<figure>` with a `<picture>` and a four-language `fig-desc` at the section given in A3. The image map is the placement contract. Then run `patch_image_lightbox.py` and `patch_hero_fetchpriority.py`. Images 001, 002, and 02 are already referenced in the HTML.

---

## Part B. Copy-ready prompts

### 001 — Vignette hero

```
IMAGE NUMBER: 001
SECTION PLACEMENT: Hero, figure.hero-figure.mode-patient > .hero-vignette (patient mode only)
FILE NAME: transplant-prehabilitation-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 — composition archetype J (Environmental Storytelling)
AUDIENCE: patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX:
- photorealistic models: two people (patient + teenage family member)
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Show prehabilitation as ordinary, doable at home, and shared with family.
KEY CONCEPTS: chair stands, family support, home exercise while waiting for a transplant
CAMERA: side profile at eye level, environmental distance
HUMAN VARIATION (vs. previous guide): previous guide had no people; this one uses a Filipino woman in her late 40s and her teenage son

COPY-READY IMAGE GENERATOR GPT PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: Environmental Storytelling, one cohesive scene, no floating panels. Camera: side profile at eye level, environmental distance.
Scene: a bright, simple Filipino home living area in soft late-morning daylight. A Filipino woman in her late 40s with medium-brown skin, short layered black hair tucked behind one ear, a slim build, wearing a loose mustard-yellow cotton T-shirt and dark gray track pants, is midway through standing up from a sturdy plain wooden chair with her arms crossed over her chest, focused and determined. Beside her, her teenage son (about 15, lean, wavy hair, round glasses, faded green shirt) sits cross-legged on a woven banig mat, holding up fingers as he counts, smiling encouragingly. On the plain white wall behind them, a small paper calendar with three days circled in teal marker hangs slightly out of focus, with no readable words or numbers. Two refilled water bottles rest on the floor near the chair as improvised hand weights.
Visual hierarchy: the woman rising from the chair occupies 60–70% of the circle; the son and the calendar are supporting elements. Reserve a 20–25% TITLE SAFE ZONE of clean, softly lit white wall toward the upper-left of the circle with nothing inside it. Natural, warm, hopeful color grade harmonizing with clinical teal #1a6b72 and warm neutrals; shallow depth of field.
Absolutely NO text of any kind: no readable words or numbers on the calendar, shirts, or bottles, no title, no caption, no logo, no watermark. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid gym equipment, treadmills, dumbbells, hospital beds, dialysis machines, IV lines, tubing, catheters, bandages, visible blood, grimacing or pain, elderly-man-eating stock archetypes, dining tables with plates, teal polo shirts, beige blouses, cartoon style, neon, HDR, over-saturation, dark backgrounds, baked-in text, captions, logos, watermarks, cropped circle, faces or limbs touching the circular border, anything inside the title safe zone.

QUALITY CHECK:
Square 2048×2048. Circle 85–90% of canvas with visible white margin, never cropped. One dominant subject at 60–70%, two supporting elements, 20–25% empty wall title-safe zone upper-left. No readable text anywhere.

ALT TEXT: "" (decorative). If informative: "A woman on dialysis practices chair stands at home while her son counts."
OG WIDTH: 2048
OG HEIGHT: 2048
```

---

### 002 — OG / social share card

```
IMAGE NUMBER: 002
SECTION PLACEMENT: <head> og:image and twitter:image; Latest guides strip thumbnail
FILE NAME: transplant-prehabilitation-og.png
ARCHETYPE: OG social share card (infographic skill)
AUDIENCE: mixed
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title lockup
- 3D component graphics: small semi-photoreal kidney beside a wooden chair and a sneaker
- algorithm/flowchart: none
PURPOSE: Clear link preview for Facebook, X, and messaging apps.
KEY CONCEPTS: title, strength before surgery, kidney

COPY-READY IMAGE GENERATOR GPT PROMPT:
Social share card, exactly 1200 × 630 pixels, white (#ffffff) to very light teal (#eef6f7) soft horizontal gradient background. Left two-thirds: large bold navy (#0f1e2e) title in Manrope, two lines: "Getting Fit for a" / "Kidney Transplant". Below it in clinical teal (#1a6b72), Manrope regular: "Build strength while you wait". Right third: a calm semi-photorealistic 3D still life of a single human kidney in restrained renal red-brown with soft teal rim light, resting beside a small plain wooden chair and one white walking sneaker, gentle shadow. Generous whitespace, balanced composition, nothing within 40 px of the edges. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text.
No journal names, guideline acronyms, brand logos on the sneaker, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark or navy backgrounds, cartoon style, neon, HDR, extra text, statistics, faces, hospital equipment, surgical imagery, blood, gibberish text, serif fonts, shoe brand marks. Use ONLY Manrope. Never omit the attribution.

QUALITY CHECK:
Exactly 1200 × 630. Title spelled exactly. Light background. Readable as a small thumbnail.

ALT TEXT: "Getting Fit for a Kidney Transplant — renalcarematters.com"
OG WIDTH: 1200
OG HEIGHT: 630
```

---

### 02 — Three pillars of prehabilitation

```
IMAGE NUMBER: 02
SECTION PLACEMENT: #what-prehab-is (patient), after the first paragraph (already referenced in HTML)
FILE NAME: transplant-prehabilitation-02-three-pillars.png
IMAGE TYPE: Simple figure — Scaffold E variant, three-column reference card
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: The three parts of prehabilitation, remembered at a glance.

PROMPT:
Clean clinical education reference figure, white (#ffffff) background, all text set in Inter. Bold navy (#0f1e2e) title at top center: "Three pillars of getting fit for a transplant". Below it, three equal tall rounded cards side by side on very soft gray (#f3f4f6), each with a thick colored top band, one large simple monoline icon, a bold one-word label, and two short lines.
Card 1, teal band (#1a6b72), icon of a person rising from a chair: "Move" — "Walk or pedal most days" — "Chair stands and light weights".
Card 2, renal green band (#1f7a4d), icon of a bowl with an egg and a fish: "Eat" — "Enough protein and energy" — "Some protein after exercise".
Card 3, soft purple band (#6c3d8e), icon of a simple head with a small leaf: "Mind" — "Sleep, stress, and mood" — "Bring family along".
Bottom strip, full width, light teal (#eef6f7): "Small steps, every week. The habit is the treatment." in navy.
Flat 2D style, generous whitespace, labels at least 11 pt equivalent. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon mascots, 3D renders, photos, faces, gym machines, supplement brand bottles, numbers, clutter, tiny labels, AI gibberish text, misspellings, serif fonts, dark backgrounds, neon. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Title and card text spelled exactly. Three equal cards in teal, green, purple. Readable on a phone in 10 seconds.

ALT TEXT: "Three pillars of prehabilitation: move, eat, and mind."
```

---

### 05 — The reserve tank (analogy)

```
IMAGE NUMBER: 05
SECTION PLACEMENT: #why-fitness, after the intro callout ("Think of a kidney transplant as a long climb")
FILE NAME: transplant-prehabilitation-05-reserve-tank.png
IMAGE TYPE: Simple figure — Scaffold B, side-by-side analogy
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families (low literacy friendly)
VISUAL GOAL: Make "physiologic reserve" obvious with a familiar picture: a fuller tank gets you further.

PROMPT:
Medical education comparison illustration, flat 2D vector style with soft shading, white (#ffffff) background, all text in Nunito Sans. Bold navy (#0f1e2e) title at top center: "Surgery uses your body's reserve". Soft dashed vertical divider splits the canvas into two equal panels.
Both panels show the same simple illustrated scene: a gentle uphill path labeled at the top with a small flag icon and the word "Recovery", and a simple stylized adult figure (flat illustration, no detailed face) about to walk up it, with a large fuel-gauge icon beside the figure.
Left panel, header in amber (#b8860b): "Low reserve". The fuel gauge needle sits near empty, colored amber; the figure looks tired, slightly stooped, and has only climbed a short way up the path. One short caption below: "Slower to get up and walk".
Right panel, header in renal green (#1f7a4d): "Built-up reserve". The fuel gauge needle sits near full, colored green; the figure stands upright and is further up the path. One short caption below: "Easier first days after surgery".
Bottom strip, light teal (#eef6f7), navy text: "Prehabilitation fills the tank before surgery."
Rounded panel corners, generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, detailed faces, hospital scenes, scalpels, blood, cars or petrol-station branding, numbers on the gauges, percentages, guarantees such as "better transplant", cartoon mascots, clutter, AI gibberish text, serif fonts, dark backgrounds. Use ONLY Nunito Sans. Never omit the attribution.

QUALITY CHECK:
Two equal panels; gauges without numbers; title and captions spelled exactly; message readable without reading (empty vs full gauge).

ALT TEXT: "Two people facing the climb of recovery: one with a near-empty reserve gauge, one with a full gauge."
```

---

### 06 — The muscle balance on dialysis

```
IMAGE NUMBER: 06
SECTION PLACEMENT: #why-fitness, under "What dialysis does to muscle"
FILE NAME: transplant-prehabilitation-06-muscle-balance.png
IMAGE TYPE: Simple figure — Scaffold D, single-concept balance scale
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Show that muscle is constantly built and broken down, and that kidney failure tips the scale toward breakdown, which exercise and food can push back.

PROMPT:
Patient education illustration, flat 2D vector with soft semi-3D shading, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "Muscle is always being built and broken down". Teal (#1a6b72) subtitle: "Kidney failure tips the balance".
Center: a large classic balance scale. The left pan is LOWER (heavier) and labeled in clinical red (#b91c1c) "Breaks muscle down"; it holds five small simple icons, each with a 1–3 word label: a small acid drop "Acid build-up", a small flame "Inflammation", a dialysis fluid bag "Protein lost in dialysis fluid", an armchair "Long hours sitting", an empty plate "Poor appetite".
The right pan is HIGHER (lighter) and labeled in renal green (#1f7a4d) "Builds muscle up"; it holds four small icons with labels: a person rising from a chair "Exercise", an egg and fish "Protein", a rice bowl "Enough energy", a crescent moon "Sleep".
A bold teal curved arrow next to the right pan points downward with the words "Prehabilitation adds weight here".
Bottom strip, soft gray (#f3f4f6), navy text: "Use it and feed it, or the body takes it back."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid medical jargon (no "catabolism", "proteasome", "cytokines"), numbers, photorealism, cartoon faces on icons, clutter, more than nine icons, AI gibberish text, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
The breakdown side is visibly lower. Every label at most 5 words, spelled exactly. Understandable without reading the subtitle.

ALT TEXT: "Balance scale: acid, inflammation, protein loss in dialysis fluid, sitting, and poor appetite outweigh exercise, protein, energy, and sleep."
```

---

### 07 — Five signs of frailty

```
IMAGE NUMBER: 07
SECTION PLACEMENT: #why-fitness, under "The five signs of frailty, in plain words"
FILE NAME: transplant-prehabilitation-07-five-signs-frailty.png
IMAGE TYPE: Simple figure — Scaffold E, icon reference card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: patients and families
VISUAL GOAL: Let anyone recognize the five frailty signs and understand the 0 / 1–2 / 3+ count.

PROMPT:
Clinical reference card, clean flat icon design, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "Five signs of frailty".
Middle: five equal rounded tiles in a single row on soft gray (#f3f4f6), each with one large simple monoline icon in teal (#1a6b72) and a bold label of 2–4 words beneath:
1. a hand squeezing a handgrip device — "Weak grip"
2. a walking figure with a small snail beside the feet — "Slow walking"
3. a figure slumped in a chair with a low-battery symbol — "Always tired"
4. a pair of resting shoes beside a sofa — "Little activity"
5. a bathroom scale with a down arrow — "Weight loss without trying"
Bottom: a horizontal three-step scale bar with rounded segments: green (#1f7a4d) segment "0 signs: robust", amber (#b8860b) segment "1–2 signs: prefrail", red (#b91c1c) segment "3 or more: frail".
Footer line in teal: "Prefrail and frail can improve with the right plan."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid elderly stereotypes such as canes or wheelchairs, photorealism, faces with expressions of distress, numeric grip or walking cutoffs, kilogram values, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Exactly five tiles and a three-segment bar colored green, amber, red; all labels spelled exactly; no numbers other than 0, 1–2, 3.

ALT TEXT: "Five frailty signs: weak grip, slow walking, always tired, little activity, weight loss without trying; 0 signs robust, 1–2 prefrail, 3 or more frail."
```

---

### 08 — Your starter week

```
IMAGE NUMBER: 08
SECTION PLACEMENT: #exercise-plan, directly after the weekly plan table
FILE NAME: transplant-prehabilitation-08-starter-week.png
IMAGE TYPE: Simple figure — Scaffold E variant, seven-day calendar strip
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Turn the weekly plan table into a picture a patient can tape to the wall.

PROMPT:
Patient education calendar infographic, flat 2D style, white (#ffffff) background, all text in Manrope. Bold navy (#0f1e2e) title at top center: "Your starter week".
A single row of seven equal rounded day columns labeled at the top "Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun".
Mon, Wed, Fri columns: very light teal fill (#eef6f7), a small dialysis-chair icon with a small pedal exerciser at its foot, label "Dialysis day", one line "Pedal 10–15 min".
Tue, Thu, Sat columns: white fill with teal (#1a6b72) top band, three small stacked icons (walking figure, person rising from a chair, hand holding a water bottle), label "Strength day", one line "Walk + chair stands + light weights".
Sun column: soft gray (#f3f4f6) fill, a small family-walk icon, label "Rest or easy walk".
Across the bottom of all seven columns, a thin purple (#6c3d8e) ribbon with a small lungs icon: "Every day: 5 minutes slow breathing, twice".
Footer in navy: "Add a little each week when it feels easy."
Note in small amber (#b8860b) text under the footer: "Your days may differ: match your own dialysis schedule."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, gym machines, heavy dumbbells, calorie numbers, heart-rate numbers, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Manrope. Never omit the attribution.

QUALITY CHECK:
Seven columns in correct order; dialysis days Mon/Wed/Fri; only the minute values written above appear; readable when printed on A4.

ALT TEXT: "Weekly plan: pedal on dialysis days, walk, chair stands, and light weights on other days, rest on Sunday, breathing exercises every day."
```

---

### 09 — How to do a chair stand, and how hard to push

```
IMAGE NUMBER: 09
SECTION PLACEMENT: #exercise-plan, under "How hard, and how to build up"
FILE NAME: transplant-prehabilitation-09-chair-stand-talk-test.png
IMAGE TYPE: Simple figure — Scaffold C, horizontal step sequence plus effort meter
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Teach the single most useful exercise safely, and the talk test for intensity.

PROMPT:
Clean clinical education infographic, flat 2D illustration with soft shading, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "The chair stand: one move, big benefit".
Upper two-thirds: four rounded cards in a single horizontal row on soft gray (#f3f4f6), connected by bold navy right-pointing arrows. Each card shows the same simple illustrated middle-aged Filipino man (flat style, short gray-black hair, plain blue shirt, no detailed facial features) beside a sturdy plain wooden chair with no armrests, with a teal (#1a6b72) step number and a short label:
1. seated near the front of the chair, feet flat on the floor — "Sit forward, feet flat"
2. arms crossed over the chest — "Cross your arms"
3. standing fully upright — "Stand up tall"
4. lowering slowly back to the seat — "Sit down slowly"
Lower third, left: a small green (#1f7a4d) tag "Start: 2 sets of 8".
Lower third, right: a horizontal three-zone effort meter with speech-bubble icons: left zone pale green "Too easy: you could sing", middle zone renal green highlighted with a star "Just right: you can talk, not sing", right zone red (#b91c1c) "Too hard: you can't talk".
Small amber (#b8860b) note under the meter: "Stop for chest pain, dizziness, or severe breathlessness."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid chairs with wheels or armrests, using the arms to push up, photorealism, gym settings, dumbbells, heart-rate numbers, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Four steps in correct order with arms crossed in steps 2–4; meter middle zone highlighted; safety note present.

ALT TEXT: "Four steps of a chair stand with arms crossed, and a talk-test meter: just right is when you can talk but not sing."
```

---

### 10 — Protecting your fistula arm

```
IMAGE NUMBER: 10
SECTION PLACEMENT: #exercise-plan, "Special situations"
FILE NAME: transplant-prehabilitation-10-fistula-arm.png
IMAGE TYPE: Simple figure — Scaffold B, do / don't comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Make it obvious which arm lifts and how to protect the access.

PROMPT:
Medical education do-and-don't comparison, flat 2D illustration, white (#ffffff) background, all text in Nunito Sans. Bold navy (#0f1e2e) title at top: "Exercise safely with a fistula".
A simple illustrated forearm with a gently raised vein along the inner forearm (an arteriovenous fistula, drawn subtly, no needles, no blood) appears in both panels for reference. Soft dashed vertical divider.
Left panel, header in renal green (#1f7a4d) with a check mark: "Do". Three rows, each with a small icon: a water bottle held in the OTHER (non-fistula) hand — "Lift with the other arm"; a soft ball gently squeezed — "Gentle hand squeezes are fine"; fingertips resting lightly on the fistula with small vibration lines — "Feel the buzz after exercise".
Right panel, header in clinical red (#b91c1c) with an X: "Don't". Three rows, each with a small icon crossed out in red: a heavy dumbbell held in the fistula arm — "No heavy weights on this arm"; a tight wristwatch or strap over the fistula — "No tight straps"; a blood pressure cuff on the fistula arm — "No blood pressure cuff".
Bottom strip, soft gray (#f3f4f6), navy text: "Leg exercises are fully allowed."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid needles, cannulation, blood, bandages, catheters, graphic anatomy, photorealism, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Nunito Sans. Never omit the attribution.

QUALITY CHECK:
The fistula appears on the same arm in both panels; "Do" weights are always in the non-fistula hand; all text spelled exactly.

ALT TEXT: "Do lift with the other arm, squeeze gently, and feel the buzz; don't use heavy weights, tight straps, or a blood pressure cuff on the fistula arm."
```

---

### 11 — The muscle-building plate on dialysis

```
IMAGE NUMBER: 11
SECTION PLACEMENT: #nutrition-before, after the Filipino protein table
FILE NAME: transplant-prehabilitation-11-protein-plate.png
ARCHETYPE: Infographic — Food matrix / nutrition infographic (archetype 6)
AUDIENCE: patients, families, renal dietitians
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none
- 2D infographic: matrix layout and labels
- 3D component graphics: semi-photoreal Filipino food items
- algorithm/flowchart: none
PURPOSE: Show which familiar protein foods help build muscle within dialysis limits, which to keep rare, and when to eat protein.
KEY CONCEPTS: better protein choices; salty processed foods; protein after exercise; ask the dietitian for your amount

COPY-READY IMAGE GENERATOR GPT PROMPT:
CKD and dialysis nutrition infographic, clean educational food matrix, white (#ffffff) background, all text in Manrope. Bold navy (#0f1e2e) title at top: "Protein builds muscle". Teal (#1a6b72) subtitle: "Choose well, and eat some after exercise".
Left two-thirds: a large rounded panel with a renal green (#1f7a4d) header "Better choices", showing semi-photorealistic 3D food items on small white plates, each with a 1–3 word label: two boiled eggs with one cut showing the white — "Egg whites, eggs"; a grilled bangus (milkfish) fillet — "Fresh fish"; a small grilled tilapia — "Tilapia"; a skinless boiled chicken breast — "Chicken, no skin"; a few cubes of plain firm tokwa (tofu) — "Tokwa".
Right third: a narrower rounded panel with an amber (#b8860b) header "Keep rare", showing smaller items with a thin amber outline: dried tuyo fish — "Tuyo, daing"; two longganisa sausages — "Longganisa"; an unbranded open can of meat — "Canned meat"; a hotdog — "Hotdog". Under them, a one-line note: "Very salty, with added phosphate".
Bottom band, light teal (#eef6f7): a clock icon showing "within 1 hour" beside a small egg icon, text "After exercise: a little protein"; and, separated by a thin divider, a dietitian icon with text "Ask your dietitian for your daily amount".
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid gram or kilogram numbers, percentages, brand labels on cans, protein powder tubs, bananas, oranges, coconut water, soy sauce bottles in the "better" panel, cartoon food faces, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds, HDR. Use ONLY Manrope. Never omit the attribution.

QUALITY CHECK:
Five "better" and four "keep rare" items, correctly labeled and identifiable as Filipino foods; no numeric targets on the image; bottom band present.

ALT TEXT: "Better protein choices on dialysis are eggs, fresh fish, tilapia, skinless chicken, and tokwa. Tuyo, longganisa, canned meat, and hotdogs should be rare. Eat a little protein after exercise."
OG WIDTH: 1536
OG HEIGHT: 1152
```

---

### 12 — The habit cycle

```
IMAGE NUMBER: 12
SECTION PLACEMENT: #keep-going, after the first paragraph
FILE NAME: transplant-prehabilitation-12-habit-cycle.png
ARCHETYPE: Infographic — Circular workflow / cycle (archetype 8)
AUDIENCE: patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: circular arrows and labels
- 3D component graphics: small soft 3D icons
- algorithm/flowchart: cycle
PURPOSE: Show that gains are kept by a repeating routine, not a one-time program.
KEY CONCEPTS: plan, move, eat, rest, measure monthly, adjust; restart after setbacks

COPY-READY IMAGE GENERATOR GPT PROMPT:
Circular workflow infographic, polished and calm, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "Keep the habit, keep the gains".
Center: a soft 3D icon of a sturdy wooden chair beside a small paper calendar, with the label "Your routine".
Around it, six evenly spaced rounded nodes connected clockwise by bold curved arrows forming a full loop, each with a small soft 3D icon and a 1–3 word label:
1. top, teal (#1a6b72), clipboard — "Plan the week"
2. teal, walking shoe — "Move"
3. renal green (#1f7a4d), egg and fish — "Eat protein"
4. soft purple (#6c3d8e), crescent moon — "Rest and sleep"
5. teal, stopwatch — "Measure monthly"
6. navy, upward arrow — "Add a little more"
Outside the loop, a small dashed amber (#b8860b) side arrow re-entering at "Plan the week", labeled "Setback? Restart at half and rebuild".
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid numbers other than step order, photorealistic people, gym machines, clutter, more than six nodes, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Six nodes in clockwise order forming a closed loop; amber setback arrow present; centered composition.

ALT TEXT: "Habit cycle: plan the week, move, eat protein, rest and sleep, measure monthly, add a little more, and restart at half after a setback."
OG WIDTH: 1024
OG HEIGHT: 1024
```

---

### 13 — The plate changes after transplant

```
IMAGE NUMBER: 13
SECTION PLACEMENT: #after-transplant, after the first paragraph (before the adherence chart 04)
FILE NAME: transplant-prehabilitation-13-after-transplant-plate.png
IMAGE TYPE: Simple figure — Scaffold B, before / after comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Show the shift from a restriction diet on dialysis to a heart-healthy diet with a working kidney.

PROMPT:
Medical education comparison infographic, white (#ffffff) background, all text in Manrope, semi-photorealistic food on simple white plates. Bold navy (#0f1e2e) title at top center: "After transplant, the plate changes".
Left panel, header in navy: "On dialysis". A plate with a modest portion of rice, a piece of grilled fish, and a small portion of boiled low-potassium vegetables; around the plate three small amber (#b8860b) limit badges with icons: a drop "Fluid limits", a banana outline "Potassium limits", a small bone "Phosphorus limits".
Center: a bold teal (#1a6b72) right-pointing arrow with a small kidney icon and the word "Transplant".
Right panel, header in renal green (#1f7a4d): "With a working kidney". A colorful plate, half filled with vegetables (pechay, string beans, tomato, carrots), a quarter with brown or red rice, a quarter with fish or tokwa, a small bowl of mixed fruit such as papaya and mango slices beside it. Three small green badges: "More vegetables and fruit", "More fiber", "More plant protein"; one small red (#b91c1c) badge with a salt shaker: "Less salt and processed meat".
Bottom strip, soft gray (#f3f4f6), amber text: "Your team decides which limits change, based on your blood tests."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid pomelo, grapefruit, oranges cut in half, raw fish, numbers, calorie or gram values, junk food in the right panel, cartoon food faces, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds, HDR. Use ONLY Manrope. Never omit the attribution.

QUALITY CHECK:
Right plate visibly more colorful and half vegetables; no citrus that could imply pomelo or grapefruit is safe; amber footer present.

ALT TEXT: "On dialysis, the plate has fluid, potassium, and phosphorus limits; after transplant it shifts to more vegetables, fruit, fiber, and plant protein with less salt."
```

---

### 14 — Foods to avoid with anti-rejection medicines

```
IMAGE NUMBER: 14
SECTION PLACEMENT: #after-transplant, under "Food safety and medicine safety"; may also be reused in #md-post-tx-diet
FILE NAME: transplant-prehabilitation-14-tacrolimus-food-safety.png
IMAGE TYPE: Simple figure — Scaffold E, square "avoid" reference card
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients, families, clinicians
VISUAL GOAL: A fridge-door card that a patient on tacrolimus or cyclosporine can recognize instantly.

PROMPT:
Clinical safety reference card, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "Taking tacrolimus or cyclosporine?" Red (#b91c1c) subtitle: "Avoid these unless your transplant team says yes".
A 2 × 2 grid of rounded tiles on soft gray (#f3f4f6), each with a semi-photorealistic item and a thin red circle-slash overlay, and a bold label:
1. a halved pomelo (suha) with pale pink segments — "Pomelo (suha)"
2. a halved grapefruit with deep pink flesh — "Grapefruit"
3. a small unbranded supplement bottle with turmeric capsules and a piece of turmeric root — "Herbal capsules, such as turmeric"
4. a small bowl of raw fish kinilaw beside a cracked soft-boiled egg — "Raw or undercooked food"
Small line under tiles 1–3 in amber (#b8860b): "Can change your medicine level".
Small line under tile 4 in amber: "Infection risk".
Bottom band, light teal (#eef6f7), navy text with a small pill-bottle icon: "Show every supplement to your transplant team."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid brand names on bottles, oranges or calamansi (not part of this warning), alarming skull symbols, numbers or drug levels, photorealistic people, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Pomelo and grapefruit clearly distinguishable; exactly four tiles; red circle-slash on each; footer present.

ALT TEXT: "With tacrolimus or cyclosporine, avoid pomelo (suha), grapefruit, herbal capsules such as turmeric, and raw or undercooked food unless your transplant team approves."
```

---

### 15 — Why muscle wastes in kidney failure (mechanism figure)

```
IMAGE NUMBER: 15
SECTION PLACEMENT: #md-frailty (clinician), after the "Physiology first" paragraph
FILE NAME: transplant-prehabilitation-15-uremic-muscle-mechanism.png
IMAGE TYPE: Biomedical mechanism figure (organ panel → magnified muscle-fiber inset → injury / intervention / benefit)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Trace the converging drivers of uremic sarcopenia to the anabolic levers prehabilitation pulls, and flag what is unproven.

PROMPT:
Scientific review-article mechanism schematic, flat vector illustration with soft semi-3D shading, white (#ffffff) background, muted clinical palette, all text in IBM Plex Sans. Title at top left in navy (#0f1e2e): "Uremic muscle wasting and the levers of prehabilitation".
Left panel: simplified light gray-blue pair of kidneys labeled "Kidney failure on dialysis", with a small dialysis-fluid bag icon beside it labeled "Amino acids lost into dialysate". A dashed connector runs to a simplified thigh silhouette with the quadriceps highlighted pale yellow, labeled "Skeletal muscle".
Center-right: a large dashed-border magnified panel showing a single skeletal muscle fiber in cross-section with myofibrils, a nucleus, and mitochondria. Short labeled callouts with arrows pointing into the fiber:
- red: "Metabolic acidosis → ↑ ubiquitin–proteasome proteolysis"
- red: "Inflammation (IL-6, TNF-α)"
- red: "Insulin resistance → ↓ Akt/mTOR signaling"
- red: "↑ Myostatin"
- red: "Inactivity → ↓ mechanical loading"
- blue, on the opposite side: "Resistance exercise → ↑ mTOR, ↑ muscle protein synthesis"
- blue: "Leucine-rich protein after exercise"
Bottom row, three boxes linked by arrows left to right:
Pale pink box (injury): "Net protein breakdown" / "↓ Fiber size, ↓ mitochondrial function" / "**Sarcopenia and frailty**".
Center box (intervention): "Prehabilitation: resistance + aerobic + inspiratory muscle training, protein after sessions, correct acidosis".
Pale blue box (benefit): "↑ Strength, grip, muscle thickness (shown in RCT)" / "VO₂ max, 6-minute walk, frailty status: not changed" / "Transplant outcomes: not yet tested", the last line in gray.
Thin dashed connectors, minimal clutter, all labels legible. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative effects, invented pathways, numeric thresholds or doses, drug brand names, implying proven transplant benefit, cartoon style, AI gibberish text, serif fonts. Use ONLY IBM Plex Sans. Never omit the attribution.

QUALITY CHECK:
Organ panel → dashed muscle-fiber inset → injury/intervention/benefit row; red drivers vs blue levers; the benefit box keeps the "not changed" and "not yet tested" lines; labels anatomically and biochemically accurate.

ALT TEXT: "Mechanism figure: acidosis, inflammation, insulin resistance, myostatin, dialysate amino-acid loss, and inactivity drive muscle breakdown; exercise and protein after sessions push synthesis; strength gains shown, transplant outcomes untested."
```

---

### 16 — Clinician prehabilitation pathway

```
IMAGE NUMBER: 16
SECTION PLACEMENT: #md-prescription (clinician), after the algo-card (printable companion)
FILE NAME: transplant-prehabilitation-16-clinician-pathway.png
IMAGE TYPE: Simple figure — Scaffold A, clinical algorithm (portrait)
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians, dialysis nurses, renal dietitians
VISUAL GOAL: One printable page showing who to screen, when to hold, and how the plan differs for living- versus deceased-donor timelines.

PROMPT:
Clinical nephrology algorithm, KDIGO-style guideline flowchart aesthetic, white (#ffffff) background, all text in Inter. Title at top in bold navy (#0f1e2e): "Prehabilitation pathway for transplant candidates". Rounded rectangular nodes, bold connecting arrows, top-to-bottom flow, maximum 10 nodes.
1. Navy action node: "Waitlisted or under evaluation".
2. Teal (#1a6b72) action node: "Screen: frailty (Fried or SPPB), grip, gait, 30-s chair stand, nutrition, PHQ-9".
3. Teal decision node: "Unstable cardiac symptoms, severe hyperkalemia, or uncontrolled BP?"
   - YES → red (#b91c1c) node: "Stabilize first; supervised exercise only" → arrow back to node 3.
   - NO → continue.
4. Teal decision node: "Living-donor surgery date known?"
   - YES → green (#1f7a4d) node: "6–8-week intensive supervised block before surgery".
   - NO → green node: "Always-on maintenance in the dialysis unit; intensify near the top of the list".
5. Both branches join into a navy node: "Every plan: aerobic + resistance + breathing training; protein after sessions; psychosocial support".
6. Teal node: "Re-measure monthly".
7. Amber (#b8860b) decision node: "Declining or after hospitalization?" YES → arrow back to "Re-intensify" (small amber node) → node 6. NO → "Maintain".
Footer in gray: "Improves strength and muscle; effect on transplant outcomes not yet tested."
Generous whitespace, mobile-readable labels. Bottom-center: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid potassium or blood pressure numbers, drug names, spaghetti arrows, more than 10 nodes, cartoon style, clutter, tiny labels, AI gibberish text, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Living/deceased branch present; the loop back from "Declining" works; footer keeps the honest caveat; attribution bottom-center.

ALT TEXT: "Pathway: screen, check safety, choose an intensive block before a living-donor date or ongoing maintenance for deceased-donor waits, then re-measure monthly and re-intensify after setbacks."
```

---

### 17 — What prehabilitation has and has not shown

```
IMAGE NUMBER: 17
SECTION PLACEMENT: #md-evidence, after the evidence table (also usable in patient #what-prehab-is beside the purple honesty box)
FILE NAME: transplant-prehabilitation-17-evidence-tiers.png
IMAGE TYPE: Simple figure — Scaffold E, three-tier evidence card
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians and patients
VISUAL GOAL: Show honestly where the evidence is solid, where it was negative, and where it is missing.

PROMPT:
Clinical evidence summary card, publication-grade, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "Prehabilitation before kidney transplant: what we know so far".
Three horizontal tiers stacked top to bottom, each a full-width rounded band with a left label block and a row of small icon chips:
Tier 1, renal green (#1f7a4d) left block, check-mark icon: "Improved in a randomized trial (8 weeks)". Chips: "Exercise workload", "Grip strength", "Thigh muscle thickness", "Breathing-muscle strength".
Tier 2, amber (#b8860b) left block, equals-sign icon: "Did not change in that trial". Chips: "Peak oxygen uptake", "6-minute walk distance", "Frailty status". Small note at the right end: "Gains faded by 6 months without ongoing support".
Tier 3, gray (#9ca3af) left block, question-mark icon: "Not yet tested in transplant trials". Chips with dashed outlines: "Graft survival", "Complications", "Hospital stay", "Survival".
Footer in teal (#1a6b72): "Safe, and builds strength now; proof of better transplants is still awaited."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid trial names, journal names, numbers, p-values, percentages, implying benefit for tier 3, photorealism, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Three tiers in green, amber, gray in that order; chip text exactly as written; tier 3 visibly "unknown" (dashed, gray).

ALT TEXT: "Evidence tiers: strength, grip, muscle thickness, and breathing muscles improved; aerobic capacity, walk distance, and frailty status did not change; transplant outcomes not yet tested."
```

---

### 18 — Three ways to deliver prehabilitation

```
IMAGE NUMBER: 18
SECTION PLACEMENT: #md-prescription, beside the "Center-based or home-based?" table
FILE NAME: transplant-prehabilitation-18-delivery-models.png
ARCHETYPE: Infographic — Clinician reference card (archetype 5)
AUDIENCE: clinicians, dialysis unit managers
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none
- 2D infographic: three-column card
- 3D component graphics: small soft 3D scene icons
- algorithm/flowchart: none
PURPOSE: Compare center-based, home-based, and intradialytic delivery for program planning in Philippine dialysis units.
KEY CONCEPTS: reach, adherence, supervision, fit for local practice

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical reference infographic card, publication-grade nephrology design, white (#ffffff) background, all text in Inter. Bold navy (#0f1e2e) title at top: "Three ways to deliver prehabilitation".
Three equal rounded columns on soft gray (#f3f4f6), each topped by a small soft 3D icon and a bold header:
Column 1, teal (#1a6b72) header, icon of a rehabilitation room with a stationary bike: "Center-based". Rows with small icons: green check "Best supervision and progression"; amber dot "Hardest to reach"; amber dot "Travel time and cost".
Column 2, purple (#6c3d8e) header, icon of a house with a chair: "Home-based". Rows: green check "Easiest to reach"; amber dot "More drop-out"; green check "Works with family and a written log".
Column 3, renal green (#1f7a4d) header, icon of a dialysis chair with a pedal exerciser at its foot: "During dialysis". Rows: green check "Uses time already in the chair"; green check "Nurse-supervised"; green check "Low-cost pedal exercisers".
Bottom band, light teal (#eef6f7), navy text: "Most scalable locally: start in the dialysis unit, add home work, refer the frailest to rehabilitation."
Generous whitespace, labels at least 11 pt equivalent. Bottom-right: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid numbers, percentages, costs in pesos, brand names on equipment, dialysis machine circuit detail, photorealistic people, clutter, AI gibberish text, misspellings, serif fonts, dark backgrounds. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
Three equal columns, three rows each, consistent check/dot icons; bottom band present.

ALT TEXT: "Center-based programs give the best supervision but are hard to reach; home programs reach more people but more drop out; programs during dialysis use chair time, are nurse-supervised, and cost little."
OG WIDTH: 1536
OG HEIGHT: 1152
```

---

### 19 — Kidney–muscle–heart–mind sigil

```
IMAGE NUMBER: 19
SECTION PLACEMENT: #mind (patient) section header accent, or #md-frailty (clinician)
FILE NAME: transplant-prehabilitation-19-kidney-muscle-sigil.png
IMAGE TYPE: Organ-crosstalk sigil (label-free)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: mixed
VISUAL GOAL: A calm symbol of the whole-body loop the guide teaches: kidney failure weakens muscle, heart, and mood, and moving, eating, and support feed back to all of them.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring four simplified organ icons: a kidney at the top center, a flexed upper-arm muscle at the right, a heart at the bottom center, and a brain at the left.
RELATIONSHIP: Show a balanced four-way loop. Thin dotted curved arrows run clockwise around all four organs, and fainter dotted arrows cross through the center, suggesting that each organ affects the others.
STYLE: Minimal clinical line art, thin monoline strokes, soft teal-blue palette (#1a6b72, muted cyan, slate), white background, clean rounded organ shapes, balanced radial sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels.
COMPOSITION: Centered radial symmetry with clean margins; a tiny teal walking-figure glyph at the exact center where the inner arrows meet.
OUTPUT: Square, high-resolution, publication-grade medical icon aesthetic. Include a small, semi-transparent "renalcarematters.com" attribution in the bottom-right corner, set in Inter.

NEGATIVE INSTRUCTIONS:
Avoid labels, photorealism, 3D shading, gradients, heavy shadows, anatomical detail, clutter, dark backgrounds, serif fonts. Never omit the attribution.

QUALITY CHECK:
Four organs evenly spaced; dotted loop clockwise; only text is the attribution.

ALT TEXT: "Line-art symbol linking kidney, muscle, heart, and brain in one loop."
```

---

## Part C. Production checklist

1. Generate in priority order: **P1** (001, 002, 02) → **P2** (05, 06, 07, 08, 09, 11, 13, 14, 17) → **P3** (10, 12, 15, 16, 18, 19).
2. Reject any output with misspelled text, invented numbers, a dark background, a missing attribution, or a circle crop touching the canvas edge (001).
3. Pomelo vs grapefruit (14): confirm the pomelo is pale-fleshed and large, so readers can tell the two apart.
4. Mechanism figure (15): check the arrows. Red drivers point into the fiber, and blue levers point toward synthesis.
5. Save PNG and WebP to `images/`, then wire each image per A3 and A6. Ask Claude to build the code-native 20 (FRAILMar effects) and to add the `<figure>` blocks with four-language captions.
