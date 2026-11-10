# A Dialysis Access Lifeline That Lasts a Lifetime — Image Plan Blueprint and GPT Prompt Pack

**Guide:** `guides/hemodialysis-access-lifeline.html` · **Calculators:** `calc-catheter-exposure.html`, `calc-access-infection-rate.html`, `calc-access-intervention-burden.html`, `calc-access-flow-cardiac.html`
**Production target:** ChatGPT Image Generator GPT (https://chatgpt.com/g/g-pmuQfob8d-image-generator)
**Prepared:** November 11, 2026 · **Version:** 1
**Skills used:** `williamriveromd-hero-vignette` (v3, Scaffold A, archetype H) · `williamriveromd-infographic-skill` (v5 archetypes 2, 3, 4, 5, 9 and the hemofilter reference anatomy) · `williamriveromd-biomedical-mechanism-figure` (image 03) · `williamriveromd-algorithm-generator-skill` style (images 09, 10) · `williamriveromd-organ-crosstalk-sigil-graphic` style (image 13) · Stage 2 handled by `williamriveromd-local-image-generator`

**House rules for every prompt in this pack**
- Light backgrounds only (white, ivory, or soft light gray). Navy and teal are accents and text, never backgrounds.
- Illustrated, softly shaded semi-3D medical rendering or photorealistic editorial photography. **No flat clip-art or flat-vector look**, no cartoons, no neon.
- On-image type uses one approved sans-serif font only (Inter, Nunito Sans, IBM Plex Sans, or Manrope), named in each prompt.
- American English spelling and number style.
- `renalcarematters.com` in small semi-transparent navy type, bottom-right (bottom-center on portrait images). Every prompt carries it.
- Every number on an image comes from the guide's PubMed-verified sources. No invented values, no drug or device brands, no readable packaging.
- No journal names, guideline acronyms, trial names, brand names, or watermarks on any image.
- **No needle shown piercing skin, no blood spray, no surgical gore.** Needles may appear taped in place, capped, or in diagrams.
- Deliver a `.png` master and a same-size `.webp` twin.

---

## Part 1 — The image plan

### 1.1 The teaching job

Vascular access is hard for lay readers for four reasons. Each image is assigned to one of them.

| Barrier | Why readers struggle | What the pictures do |
|---|---|---|
| **Invisible plumbing** | Few people can picture an artery joined to a vein, or how blood leaves the arm, passes a filter, and comes back | One consistent "bridge" picture of the circuit (01), then three access types side by side (02) |
| **Slow biology** | "Maturation" and "stenosis" are abstract, and failure feels like someone's fault | A cut-away showing the vein wall thickening inward (03) and a calendar-style path from surgery to dependable use (06) |
| **A lifetime made of many steps** | People expect one operation to last forever | A road with five signposts and four destinations (04), plus vein protection made concrete (05) |
| **Knowing when to act** | Patients wait too long; clinicians over-react to single numbers | A daily look-listen-feel check (07), a red-flag poster (12), and two clinician algorithms that separate concern, confirmation, and decision (09, 10) |

The emotional job matters as much: the reader should finish feeling that the access is **protectable, fixable, and part of a plan**, not a ticking bomb. The hero (001), the roadmap (04), and the daily check (07) carry that tone. Catheters are shown as a legitimate bridge, never as a failure, so patients who have one are not shamed.

### 1.2 Designing for every educational level

Readers range from people with elementary schooling reading on a phone, often with a family member translating aloud into Tagalog, Cebuano, or Kapampangan, to nephrologists, access surgeons, and dialysis nurses.

| Depth | Who | What they must get | How the image delivers it |
|---|---|---|---|
| **Glance (5 seconds)** | Everyone | One idea, stated in a headline of 8 words or fewer | One focal subject; color and position carry meaning |
| **Grasp (30 seconds)** | Motivated patients and caregivers | How the parts connect | Arrows in reading order (left to right, top to bottom), labels of 6 words or fewer, a single consistent metaphor (the bridge) |
| **Go deeper** | Clinicians | Mechanism, decision points, evidence readiness | Clinician figures (03 inset, 08, 09, 10, 13, 14) with abbreviations defined in each figure's `fig-abbrevs` list |

**Rules that make images readable at any education level**
1. **One idea per image.** If a picture needs two headlines, it becomes two pictures.
2. **Pictures before words.** Patient images use 12 words or fewer per panel.
3. **The same thing always looks the same** (see 1.3). A reader who learns "red tube = blood leaving, blue tube = blood returning" in image 01 can read every later image.
4. **Plain verbs on patient labels:** "blood out," "cleaned," "blood back," "feel the buzz." No acronyms on patient images.
5. **Color plus shape.** Urgent = red triangle, caution = amber circle-bar, do this = green check. Meaning survives in grayscale and for color-vision deficiency.
6. **Phone first.** Every label legible at 360 px wide; QC at 50% zoom.
7. **Translation lives in the caption.** Images carry short English labels; the four-language `fig-desc` under each image does the translating, so nothing is re-rendered per language.
8. **Read-aloud friendly.** Each patient image can be explained in one sentence; that sentence is its `fig-desc`.
9. **Filipino context.** People, clinics, and homes are recognizably Filipino, varied in age, sex, build, and skin tone; calm and dignified, never frightened or caricatured as ill.
10. **No blame.** Failure images show biology (thickening vein wall), not careless people.

### 1.3 Shared visual vocabulary

| Element | Always drawn as | Color |
|---|---|---|
| Artery | Round, firm tube with a slightly thicker wall | Warm red `#c0392b` family |
| Vein (normal) | Thinner-walled, softer tube | Muted blue `#4a7fb5` |
| Fistula vein (matured) | Visibly wider, gently raised under the skin | Blue-violet `#5b6fb5` |
| Graft | Smooth soft tube, pale cream-white, in a gentle loop | Ivory with gray edge |
| Catheter | Two-lumen tube, red and blue clamps, exit site on the upper chest | Red and blue clamps, white tube |
| Blood leaving the body | Arrow and tubing in red | `#b91c1c` |
| Blood returning | Arrow and tubing in blue | `#2563eb` |
| Dialyzer | Upright cylinder with fine parallel fibers; blood through the ends, dialysate through side ports in the opposite direction | Teal shell `#1a6b72` |
| The "buzz" (thrill) | Three small concentric ripple arcs over the access | Teal |
| Narrowing (stenosis) | Inward-thickened wall, hourglass lumen | Amber-tan wall `#b8860b` |
| Clot | Dark-red irregular mass filling the lumen | `#7f1d1d` |
| Safe / do this | Check mark in a circle | Green `#1f7a4d` |
| Caution | Circle with a bar | Amber `#b8860b` |
| Urgent | Triangle | Red `#b91c1c` |
| Text | Navy only | `#0f1e2e` |

### 1.4 Story arc: one image per teaching step

| Section | Teaching step | Image(s) |
|---|---|---|
| Hero | "My access is cared for" | 001 |
| `#what-is` | What the bridge is | 01 |
| `#why-fails` | Why the bridge narrows | 03 |
| `#plan` | Save one arm | 05 |
| `#choose` / `#md-choose` | Three access types, three trade-offs | 02 |
| `#after-surgery` / `#md-mature` | From surgery to dependable use | 06 |
| `#daily-care` | Look, listen, feel; then the red flags | 07, 12 |
| `#catheter` / `#md-catheter` | Catheter safety and the plan off it | 11 |
| `#rescue` / `#md-plan` | A lifetime is a road | 04 |
| `#md-physiology` | Neointimal hyperplasia mechanism | 03 |
| `#md-cannulation` | Rope-ladder, buttonhole, area puncture | 08 |
| `#md-monitor` | Concern, confirmation, decision | 09 |
| `#md-rescue` | Rescue algorithm and succession | 10 |
| `#md-cardiac` | Access–heart crosstalk | 13 |
| `#md-new` | What is new and what is ready | 14 |
| OG / social | Instant recognition in a feed | 006 |

### 1.5 Asset register

**Status:** every figure below is already wired into the guide (`<figure>` with `<picture>`, alt text, a plain-language `fig-desc`, and a `fig-abbrevs` list where needed). Only the image files are needed. Drop `images/<file>.png` and its `.webp` twin in place and the guide picks them up.

| ID | File (`images/`) | Size | Skill / archetype | Anchor | Tab |
|---|---|---|---|---|---|
| 001 | `hemodialysis-access-lifeline-vignette-hero.png` | 2048 × 2048 | hero-vignette v3, Scaffold A, archetype H | Hero disc | Patient |
| 006 | `hemodialysis-access-lifeline-og.png` | 1200 × 630 | infographic, OG card | `og:image` | — |
| 01 | `hemodialysis-access-lifeline-01-access-circuit.png` | 1792 × 1024 | infographic 9, access/procedural + hemofilter anatomy | `#what-is` | Patient |
| 02 | `hemodialysis-access-lifeline-02-three-access-types.png` | 1792 × 1024 | infographic 4, multi-panel comparison | `#choose`, `#md-choose` | Both |
| 03 | `hemodialysis-access-lifeline-03-why-access-fails.png` | 1792 × 1024 | biomedical mechanism figure (dual register) | `#why-fails`, `#md-physiology` | Both |
| 04 | `hemodialysis-access-lifeline-04-lifetime-roadmap.png` | 1792 × 1024 | infographic 4, journey | `#rescue`, `#md-plan` | Both |
| 05 | `hemodialysis-access-lifeline-05-save-your-veins.png` | 1792 × 1024 | infographic 4, do/avoid | `#plan` | Patient |
| 06 | `hemodialysis-access-lifeline-06-maturation-timeline.png` | 1792 × 1024 | infographic, timeline | `#after-surgery`, `#md-mature` | Both |
| 07 | `hemodialysis-access-lifeline-07-look-listen-feel.png` | 1792 × 1024 | infographic 9, three photo panels | `#daily-care` | Patient |
| 08 | `hemodialysis-access-lifeline-08-cannulation-techniques.png` | 1792 × 1024 | infographic 5, clinician reference | `#md-cannulation` | Clinician |
| 09 | `hemodialysis-access-lifeline-09-monitoring-vs-surveillance.png` | 1024 × 1536 | algorithm (portrait) | `#md-monitor` | Clinician |
| 10 | `hemodialysis-access-lifeline-10-rescue-algorithm.png` | 1024 × 1536 | algorithm (portrait) | `#md-rescue` | Clinician |
| 11 | `hemodialysis-access-lifeline-11-catheter-safety.png` | 1792 × 1024 | infographic 4 + photo panel | `#catheter`, `#md-catheter` | Both |
| 12 | `hemodialysis-access-lifeline-12-urgent-signs.png` | 1024 × 1536 | infographic, red-flag poster | `#daily-care` | Patient |
| 13 | `hemodialysis-access-lifeline-13-access-heart-crosstalk.png` | 1024 × 1024 | organ-crosstalk sigil | `#md-cardiac` | Clinician |
| 14 | `hemodialysis-access-lifeline-14-evidence-timeline.png` | 1792 × 1024 | infographic 5, timeline + readiness | `#md-new` | Clinician |

**Totals:** 16 images: 2 hero/social (001, 006), 4 patient-only (01, 05, 07, 12), 5 shared by both tabs (02, 03, 04, 06, 11), and 5 clinician-only (08, 09, 10, 13, 14). Every patient section has at least one picture, and the urgent message has its own poster.

### 1.6 Production order

Most-read and most-explanatory first:

1. 001 hero · 2. 006 OG · 3. 01 circuit · 4. 02 three access types · 5. 12 urgent signs · 6. 07 look, listen, feel · 7. 05 save your veins · 8. 04 lifetime roadmap · 9. 03 why access fails · 10. 06 maturation timeline · 11. 11 catheter safety · 12. 09 monitoring algorithm · 13. 10 rescue algorithm · 14. 08 cannulation techniques · 15. 13 access–heart sigil · 16. 14 evidence timeline

### 1.7 QC rubric (every render, before it ships)

| Check | Pass standard |
|---|---|
| **5-second test** | A non-medical adult can state the single message after 5 seconds |
| **Tell-back test** (patient images) | The reader can say the `fig-desc` sentence in their own words |
| **Exact words** | Every label matches the quoted text. Reject misspellings, extra words, stray numbers; regenerate rather than edit pixels |
| **Numbers** | Only the numbers quoted in the prompt |
| **Anatomy** | Radiocephalic fistula at the wrist joins the radial artery to the cephalic vein; arterial (red) needle upstream nearer the join, venous (blue) needle downstream toward the shoulder; catheter tip in the large chest vein near the heart, exit site on the upper chest below the collarbone, cuff under the skin |
| **Circuit** | Blood out through the red line → pump → dialyzer (blood through the end ports) → blue line back; dialysate enters the side port near the blood-out end and leaves near the blood-in end (countercurrent) |
| **Phone legibility** | All labels readable at 50% zoom |
| **Color plus shape** | Meaning survives in grayscale |
| **People** | Filipino, varied, calm, dignified; no needle piercing skin; no gore |
| **Clinician images** | Every abbreviation on the image appears in that figure's `fig-abbrevs` list in the guide |
| **House style** | Light background, approved font named, `renalcarematters.com` present and legible, no flat-vector clip-art look |

---

## Part 2 — Prompts

#### Hero and social

### 001 — Hero vignette (patient)

```
FILE NAME: hemodialysis-access-lifeline-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A people
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H — Clinical (one consultation scene, minimal supporting imagery)
CAMERA: close over-the-shoulder from behind the nurse, focused on hands and forearm
HUMAN VARIATION (vs. previous guide, primary aldosteronism: one man in his late 30s, side profile, home study, evening lamp light): two people instead of one; a clinical dialysis unit instead of a home; daylight instead of lamp light; over-the-shoulder instead of side profile. Patient: Filipina woman in her early 60s, soft round face, full cheeks, small rounded nose, gentle smile lines, silver-gray hair in a low bun with a few loose strands, rimless reading glasses pushed up on her head, deep warm-brown skin, medium-full build, mustard-yellow cotton blouse with short sleeves, thin gold bangle on the right wrist. Nurse: Filipino man in his late 20s, slim, short black hair with a neat side part, clean-shaven, light-medium skin, navy scrub top, surgical mask lowered under his chin, seen mostly from behind his right shoulder. At least 12 characteristics differ from the previous hero.
AUDIENCE: mixed (patients and families first)
VISUAL GOAL: A trusted nurse gently feeling the buzz of a patient's fistula: the access as something protected and cared for.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H — Clinical, one calm scene. Camera: close over-the-shoulder from behind the nurse, focus on the hands and the patient's forearm, moderate depth of field.

Subject: a bright, clean Philippine hemodialysis unit in mid-morning daylight. A Filipina woman in her early 60s (soft round face, full cheeks, small rounded nose, gentle smile lines, silver-gray hair in a low bun with a few loose strands, rimless reading glasses pushed up on her head, deep warm-brown skin, medium-full build, mustard-yellow short-sleeved cotton blouse, thin gold bangle on her right wrist) sits relaxed in a cream-colored dialysis recliner with her LEFT forearm resting palm-up on a folded white towel on the armrest. Along the inner forearm, from the wrist toward the elbow, a gently raised, slightly wider vein is visible under smooth skin (a mature fistula), with no needles, no tape, and no tubing on it. A Filipino male nurse in his late 20s (slim, short black hair with a neat side part, clean-shaven, light-medium skin, navy scrub top, surgical mask lowered under his chin, light blue examination gloves) is seen from behind his right shoulder, resting two gloved fingertips lightly on the raised vein near the wrist as if feeling the buzz. The patient looks at her own forearm with a calm, attentive half-smile.

Supporting context (soft, out of focus): a dialysis machine edge in white and teal at the far right; a small potted pothos plant on a side table; a folded light blanket on the patient's lap. No screens with readable numbers.

Visual hierarchy: the two hands and the forearm fistula fill 60–70% of the circle (lower and center-right); the patient's face and the blurred machine edge are the supporting context (20–30%); reserve a 20–25% TITLE SAFE ZONE in the upper-left of the circle of soft, out-of-focus pale wall and window light, with no faces, hands, objects, or equipment inside it.

Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, and warm mustard accents on a light background. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle; no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, readable machine numbers, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, needles in skin, blood, tubing on the arm, bandages, a frightened or sickly look.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. Hands and fistula forearm are the dominant subject (60–70%), 2–4 supporting elements, 20–25% empty title-safe zone upper-left. Fistula vein runs along the inner LEFT forearm from wrist toward elbow. Exactly five fingers per hand. No needles, no blood, no readable text anywhere.
```

### 006 — OG social card

```
IMAGE NUMBER: 006
SECTION PLACEMENT: <meta property="og:image">, Latest guides strip, related-guide thumbnail source
FILE NAME: hemodialysis-access-lifeline-og.png
ARCHETYPE: OG / social share card
AUDIENCE: mixed
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes (typography)
- 3D component graphics: yes (semi-photorealistic forearm vessels)
- algorithm/flowchart: no
PURPOSE: Signal "your dialysis access can be planned and protected for the long run" in a Facebook or Messenger preview.
KEY CONCEPTS: forearm fistula; lifeline; plan ahead

COPY-READY IMAGE GENERATOR GPT PROMPT:
OG social share card, 1200 × 630 px, very light warm-ivory background (#fbf8f2), typography in Inter (never a serif font), renalcarematters.com house style.
Left 58%, left-aligned with a 60 px safe margin:
- small teal (#1a6b72) uppercase eyebrow: "DIALYSIS VASCULAR ACCESS"
- large bold navy (#0f1e2e) title on two lines: "A Dialysis Access Lifeline" / "That Lasts a Lifetime"
- slate subtitle on two lines: "Plan early. Protect every vein." / "Rescue wisely. Keep the next option."
- white rounded pill with teal outline and teal text: "Patients & Clinicians · EN TL CEB KAP"
- small gray line: "renalcarematters.com"
Right 42%: inside a soft pale-teal circle, a softly shaded semi-photorealistic 3D cut-away of a human forearm seen from the palm side: a warm-red radial artery and a wider blue-violet cephalic vein joined near the wrist, the joined vein running up the forearm and gently glowing; a thin teal ripple of three concentric arcs above the joint suggests the buzz. A faint dotted path continues from the forearm toward the upper right, ending in three small soft-focus milestone dots, hinting at a road ahead. Mood: confidence and care, not alarm.
Use only these words. No faces, no needles, no numbers, no dark background, no extra icons.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat-vector clip-art, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy (artery and vein must join near the wrist on the thumb side), overprocessed HDR, generic stock-photo look, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No journal names, guideline acronyms, brand names, or watermarks.

QUALITY CHECK:
Exactly 1200 × 630; all text inside the 60 px safe margin and readable at 50% thumbnail size; light background; renalcarematters.com present.

ALT TEXT: Hemodialysis access lifeline — renalcarematters.com
OG WIDTH: 1200
OG HEIGHT: 630
```

#### Patient tab

### 01 — The access is a bridge: the dialysis circuit (patient)

```
IMAGE NUMBER: 01
SECTION PLACEMENT: #what-is, after the intro callout
FILE NAME: hemodialysis-access-lifeline-01-access-circuit.png
ARCHETYPE: Access / procedural education (infographic 9) with hemofilter reference anatomy
AUDIENCE: patients and families
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: yes (one seated patient, arm only in focus)
- 2D infographic: yes (arrows, short labels)
- 3D component graphics: yes (forearm vessels, dialyzer)
- algorithm/flowchart: no
PURPOSE: Show in one glance how blood leaves the arm, is cleaned, and comes back.
KEY CONCEPTS: access as a bridge; blood out (red); cleaned in the filter; blood back (blue)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 patient-education infographic, 1792 × 1024, white background (#ffffff), clean renalcarematters.com house style, all text in Nunito Sans, navy (#0f1e2e) text.
Top-left headline, bold, two lines: "Your access is a bridge" / "for your blood".
LEFT HALF: a softly shaded semi-photorealistic 3D view of a Filipino adult's LEFT forearm resting palm-up on a white armrest (no face shown). A semi-transparent skin window reveals a warm-red radial artery joined near the wrist (thumb side) to a wider blue-violet cephalic vein running up the forearm. Two small needles are TAPED flat on the skin over the vein (shown as capped clinical needles with tape, not piercing visibly): the lower one, nearer the wrist join, connects to RED tubing; the upper one, nearer the elbow, connects to BLUE tubing.
RIGHT HALF: a simplified dialysis machine front in white and teal with a vertical upright dialyzer cylinder (teal shell, fine parallel fibers visible inside). RED tubing runs from the arm, through a small round roller pump on the machine, into the BOTTOM end port of the dialyzer; BLUE tubing leaves the TOP end port and returns to the upper needle on the arm. Two small side ports on the dialyzer carry a pale-yellow dialysate line: in near the TOP, out near the BOTTOM (opposite direction to the blood).
Large clear arrows along the tubing with three labels only: red arrow "Blood out", a teal sparkle on the dialyzer labeled "Cleaned", blue arrow "Blood back".
Small caption under the arm: "Fistula: artery joined to vein".
Bottom strip, centered, one line: "About 3 to 4 hours, 3 times a week".
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat-vector clip-art, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, needles shown piercing deep tissue, blood drops, overprocessed HDR, stock-photo blandness, excessive saturation. Never place both dialysate ports at the same end or merge the dialysate with the blood tubing. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brand names, no readable machine numbers, no watermarks. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Red line starts at the needle nearer the wrist join and enters the dialyzer at one end; blue line leaves the other end and returns to the upper needle; dialysate countercurrent through side ports; only the quoted words appear; legible at 50% zoom.
```

### 02 — Three access types, three trade-offs (shared)

```
IMAGE NUMBER: 02
SECTION PLACEMENT: #choose (patient) and #md-choose (clinician)
FILE NAME: hemodialysis-access-lifeline-02-three-access-types.png
ARCHETYPE: Multi-panel educational infographic (infographic 4), comparison
AUDIENCE: mixed
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (three access renders)
- algorithm/flowchart: no
PURPOSE: Compare fistula, graft, and catheter without ranking them.
KEY CONCEPTS: time to use; long-term upkeep; infection risk

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 comparison infographic, 1792 × 1024, off-white background (#fafafa), all text in Inter, navy text, renalcarematters.com house style.
Headline across the top, bold: "Three kinds of access. Each trades something."
Three equal rounded cards (soft light-gray #f3f4f6), each with a softly shaded semi-photorealistic 3D render on top and three icon rows below.
Card 1 title "Fistula": forearm cut-away, red radial artery joined to a widened blue-violet vein at the wrist.
Card 2 title "Graft": forearm cut-away with a smooth ivory tube in a gentle U-shaped loop joining a red artery near the elbow to a blue vein.
Card 3 title "Catheter": upper chest and neck, a soft white two-lumen tube entering a large neck vein, tunneling under the skin, exiting below the right collarbone with one red and one blue clamp; a small cuff shown as a tiny ring under the skin.
Icon rows under each card (same three rows in every card):
Row 1 hourglass icon + "Ready in": Fistula "weeks to months", Graft "about weeks", Catheter "right away".
Row 2 wrench icon + "Upkeep": Fistula "least, once working", Graft "more", Catheter "daily care".
Row 3 shield icon + "Infection risk": Fistula "lowest", Graft "middle", Catheter "highest".
Under the cards, a thin teal ribbon: "The right choice depends on you, your veins, and your plan."
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid medals, rankings, "best" badges, cartoon style, flat-vector clip-art, clutter, tiny labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no numbers, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Three cards equal in size and visual weight (no implied winner); graft loop joins artery to vein; catheter exits on the chest, not the neck; only quoted words.
```

### 03 — Why an access narrows: neointimal hyperplasia (shared, dual register)

```
IMAGE NUMBER: 03
SECTION PLACEMENT: #why-fails (patient) and #md-physiology (clinician)
FILE NAME: hemodialysis-access-lifeline-03-why-access-fails.png
ARCHETYPE: Biomedical mechanism figure (organ panel → magnified dashed inset → injury → intervention → outcome flow), rendered softly shaded semi-3D rather than flat vector
AUDIENCE: mixed (top half readable by patients; inset and bottom strip for clinicians)
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (vessel cut-aways)
- algorithm/flowchart: no (bottom summary flow only)
PURPOSE: Show that narrowing is the vein wall's own reaction to fast, disturbed flow, not anyone's fault.
KEY CONCEPTS: swirling flow at the join; wall thickening inward; outward widening that fails; narrowed channel; clot

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 review-article style mechanism figure, 1792 × 1024, white background, softly shaded semi-3D medical illustration (not flat vector), restrained clinical colors, all text in IBM Plex Sans, navy text.
Headline top-left, bold: "Why an access can narrow".
LEFT PANEL (organ level, about 35% width): a semi-transparent forearm with a red radial artery joined at the wrist to a widened blue-violet vein. A dashed teal rectangle highlights the first few centimeters of vein just after the join, labeled "Swing segment".
CENTER PANEL (magnified inset, about 40% width, connected to the dashed rectangle by dashed lines): a longitudinal cut-away of that vein segment. Left half labeled "Healthy remodeling": smooth straight flow arrows, the vein wall stretched outward evenly, wide lumen. Right half labeled "Narrowing": curling turbulent flow arrows near the join, amber-tan tissue bulging INWARD from the wall into the lumen (hourglass narrowing), small spindle-shaped cells streaming from the outer wall into the inner layer. Small labels with leader lines: "Disturbed flow", "Wall thickens inward", "Channel narrows".
RIGHT PANEL (about 25% width): a small cross-section pair: a round wide lumen above, labeled "Open", and below it a lumen mostly filled with a dark-red irregular clot, labeled "Clot can form".
BOTTOM STRIP (full width, three rounded boxes joined by arrows): amber box "Fast, swirling flow at the join" → amber box "Inner wall overgrows (neointimal hyperplasia)" → red box "Narrowing → low flow → clot". Under the strip, small teal text: "Biology, not blame. Early reporting allows early repair."
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid flat-vector clip-art, cartoon style, clutter, tiny unreadable labels, AI gibberish text, outward thickening drawn as narrowing, clot drawn in the artery, gore, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No journal names, trial names, brands, or watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Thickening grows INTO the lumen on the narrowing side; healthy side shows outward widening; dashed inset correctly linked to the swing segment just downstream of the join; only quoted words.
```

### 05 — Save one arm (patient)

```
IMAGE NUMBER: 05
SECTION PLACEMENT: #plan, after the do/avoid cards
FILE NAME: hemodialysis-access-lifeline-05-save-your-veins.png
ARCHETYPE: Multi-panel patient infographic (do / avoid)
AUDIENCE: patients and families
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: yes (one person)
- 2D infographic: yes
- 3D component graphics: no
- algorithm/flowchart: no
PURPOSE: Make "protect your veins" concrete: one arm is saved, the other hand is used for needles.
KEY CONCEPTS: saved arm; other hand for blood tests and drips; tell every nurse

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 patient-education infographic, 1792 × 1024, white background, all text in Nunito Sans, navy text.
Headline top-center, bold: "Save one arm for your future access".
CENTER: a photorealistic Filipino man in his early 50s (stocky build, short salt-and-pepper crew cut, round face, light mustache, medium-brown skin, sky-blue polo shirt) seated in a bright clinic, calmly holding his LEFT forearm slightly raised; a soft teal glowing band wraps his left forearm like a gentle protective sleeve, with a small green check badge. His RIGHT hand rests on a small padded armboard where a nurse's gloved hands are placing a small bandage on the back of his hand after a blood test (no needle visible, no blood).
LEFT column, three green check rows with small icons: "Blood tests on the other hand", "Drips on the other hand", "Tell every nurse: save this arm".
RIGHT column, three amber circle-bar rows with small icons: "No blood tests here", "No long arm IV lines", "No tight cuffs or bags here".
Bottom ribbon in teal: "Every needle you avoid keeps a future vein healthy."
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat-vector clip-art, needles in skin, blood, clutter, tiny labels, AI gibberish text, distorted hands, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
The saved arm (teal band) and the arm receiving care are different arms; only quoted words; legible at 50% zoom.
```

### 06 — From surgery to dependable use (shared)

```
IMAGE NUMBER: 06
SECTION PLACEMENT: #after-surgery (patient) and #md-mature (clinician)
FILE NAME: hemodialysis-access-lifeline-06-maturation-timeline.png
ARCHETYPE: Timeline infographic
AUDIENCE: mixed
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (four small forearm vein renders)
- algorithm/flowchart: no
PURPOSE: Show that a new fistula grows over weeks and is checked before needles; a date alone does not decide.
KEY CONCEPTS: heal; check; first gentle needles; dependable use

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 timeline infographic, 1792 × 1024, off-white background, all text in Inter, navy text.
Headline top-left, bold: "A new fistula needs time to grow".
A horizontal teal timeline arrow across the middle with four milestone stations. Above each station, a small softly shaded semi-3D forearm vein render that gets progressively wider and more visible from left to right:
Station 1 label "Heal" (thin vein, small closed wound near the wrist), sub-label "first 2 weeks".
Station 2 label "Check" (wider vein; a small handheld ultrasound probe resting beside the forearm), sub-label "about 4 to 6 weeks".
Station 3 label "First gentle needles" (wide vein; two small capped needles shown beside the arm on a tray, not in the arm), sub-label "when the team says ready".
Station 4 label "Dependable use" (wide, well-developed vein; small green check).
Below the timeline, one amber circle-bar note with a calendar icon crossed lightly: "A date alone does not decide. Your team checks first."
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat-vector clip-art, needles in skin, blood, invented numbers beyond those quoted, clutter, tiny labels, AI gibberish text, overprocessed HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Vein visibly widens across the four stations; only the quoted time phrases appear; legible at 50% zoom.
```

### 07 — Look, listen, feel (patient)

```
IMAGE NUMBER: 07
SECTION PLACEMENT: #daily-care, after the first paragraph
FILE NAME: hemodialysis-access-lifeline-07-look-listen-feel.png
ARCHETYPE: Access / procedural education (infographic 9), three photo panels
AUDIENCE: patients and families
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: yes (the same person in three panels)
- 2D infographic: yes (headers, small icons)
- 3D component graphics: no
- algorithm/flowchart: no
PURPOSE: Teach the two-minute daily self-check.
KEY CONCEPTS: look; listen; feel; tell the team the same day

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 patient-education infographic, 1792 × 1024, white background, all text in Nunito Sans, navy text.
Headline top-center, bold: "Your 2-minute daily check".
Three equal rounded photo panels, each showing the same photorealistic Filipina woman in her mid-40s (slim, shoulder-length straight black hair tucked behind one ear, oval face, light-tan skin, coral sleeveless blouse) at home by a sunny window, with a mature fistula on her LEFT inner forearm.
Panel 1 header with an eye icon: "LOOK" — she holds her forearm up in the light, studying it. Caption: "Redness, swelling, sores?"
Panel 2 header with an ear icon: "LISTEN" — she brings the forearm close to her ear. Three teal ripple arcs near the arm. Caption: "A steady whoosh".
Panel 3 header with a hand icon: "FEEL" — two fingertips of her right hand rest lightly on the vein near the wrist. Three teal ripple arcs. Caption: "The buzz is there".
Bottom ribbon: amber circle-bar icon + "Something changed? Call your dialysis unit today."
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat-vector clip-art, needles, blood, bandages, a worried expression, distorted hands, clutter, tiny labels, AI gibberish text, overprocessed HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Same person and same arm in all three panels; fistula on the left inner forearm; only quoted words.
```

### 12 — Go now: five warning signs (patient)

```
IMAGE NUMBER: 12
SECTION PLACEMENT: #daily-care, end of section
FILE NAME: hemodialysis-access-lifeline-12-urgent-signs.png
ARCHETYPE: Red-flag poster (portrait)
AUDIENCE: patients and families
DIMENSIONS: 1024 × 1536 (2:3 portrait)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (five small softly shaded icons)
- algorithm/flowchart: no
PURPOSE: Five signs that need the emergency room now.
KEY CONCEPTS: bleeding that will not stop; lost buzz; cold or blue hand; fever or chills; trouble breathing

COPY-READY IMAGE GENERATOR GPT PROMPT:
Portrait 2:3 poster, 1024 × 1536, white background, all text in Inter, navy text with red accents.
Top band (light rose #fdecec background strip only behind the title, page otherwise white): a red triangle icon and bold title "Go to the ER now" with subtitle "if your access shows any of these".
Five stacked rounded rows, each with a small softly shaded semi-3D icon on the left and a short bold label on the right:
1. a folded white cloth pressed on a forearm with a small red droplet at its edge — "Bleeding won't stop after 10 minutes of pressure"
2. a forearm with the three ripple arcs crossed out in gray — "The buzz is gone"
3. a pale bluish hand with a small snowflake — "Hand cold, blue, numb, or very painful"
4. a thermometer — "Fever or shaking chills"
5. lungs with a small heart — "Trouble breathing or chest pain"
At the bottom, a bold red rounded button shape with a right arrow: "Go now. Call your dialysis unit on the way."
Small semi-transparent "renalcarematters.com" bottom-center.

NEGATIVE INSTRUCTIONS:
Avoid gore, blood pools or spray, frightening faces, cartoon style, flat-vector clip-art, clutter, tiny labels, AI gibberish text, overprocessed HDR. NEVER use a dark or full-red background. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Exactly five rows in this order; only quoted words; red used for urgency with the triangle shape; legible at 50% zoom.
```

### 11 — Catheter safety and the plan off it (shared)

```
IMAGE NUMBER: 11
SECTION PLACEMENT: #catheter (patient) and #md-catheter (clinician)
FILE NAME: hemodialysis-access-lifeline-11-catheter-safety.png
ARCHETYPE: Multi-panel infographic (infographic 4) with one photo panel
AUDIENCE: mixed
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: yes (a nurse's gloved hands)
- 2D infographic: yes
- 3D component graphics: yes (catheter with clamps)
- algorithm/flowchart: no
PURPOSE: Show the clean-care bundle and keep the exit plan visible.
KEY CONCEPTS: clean hands; mask; scrub the hub; dry dressing; lock; plan

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 infographic, 1792 × 1024, white background, all text in Inter, navy text.
Headline top-left, bold: "Catheter days: keep them safe".
LEFT (about 40%): photorealistic close-up of a Filipina dialysis nurse's gloved hands (light purple gloves, navy scrub sleeve cuffs) scrubbing the hub of a white two-lumen catheter end with a small antiseptic pad; red and blue clamps visible; a clean square transparent dressing on the patient's upper right chest in soft focus; the nurse and patient both wear surgical masks (only lower faces partially visible at the frame edge).
CENTER (about 35%): a vertical checklist of six rounded rows with green check icons: "Clean hands", "Masks on", "Scrub the hub", "Clean the exit site", "Lock the line", "Dry, closed dressing".
RIGHT (about 25%): a soft road sign post with one arrow labeled "The plan:" and four small destination tiles beneath it: "Fistula", "Graft", "Transplant", "Peritoneal dialysis"; plus a fifth small gray tile: "Or a catheter by choice, with a safety plan".
Bottom ribbon in teal: "Ask at every review: what is the next step, and who is arranging it?"
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid shaming imagery, a red X over the catheter, cartoon style, flat-vector clip-art, blood, clutter, tiny labels, AI gibberish text, distorted hands, overprocessed HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no readable product labels, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Catheter exit on the upper chest below the collarbone; six checklist rows; the "by choice" tile present; only quoted words.
```

### 04 — A lifetime is a road, not one access (shared)

```
IMAGE NUMBER: 04
SECTION PLACEMENT: #rescue (patient) and #md-plan (clinician)
FILE NAME: hemodialysis-access-lifeline-04-lifetime-roadmap.png
ARCHETYPE: Journey infographic (infographic 4)
AUDIENCE: mixed
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (miniature landscape road and signposts)
- algorithm/flowchart: no
PURPOSE: Reframe "lifetime" as a succession plan with five habits and several destinations.
KEY CONCEPTS: plan early; protect every vessel; recognize trouble; rescue wisely; preserve the next option

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 journey infographic, 1792 × 1024, very light teal-tinted background (#eef6f7), all text in Manrope, navy text.
Headline top-left, bold: "A lifetime plan is a road".
A softly shaded semi-3D miniature landscape: a gentle winding road runs from lower-left to upper-right through soft green hills. Along it stand five wooden-and-teal signposts in order, each with a short bold label: 1 "Plan early", 2 "Protect every vein", 3 "Recognize trouble", 4 "Rescue wisely", 5 "Keep the next option".
Branching off the road at different points are four small destination markers, each a rounded pin with an icon and a one-word label: a forearm with a vein — "Fistula"; a forearm with a looped tube — "Graft"; a small belly outline with a soft catheter — "Peritoneal dialysis"; a kidney with a small green leaf — "Transplant". A small gray pin near the start: a neck catheter icon — "Catheter bridge".
A dotted teal line connects the destinations, showing a person can move between them over time.
Bottom ribbon: "No single access lasts forever. A good plan keeps the next one ready."
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat-vector clip-art, game-board look, people, clutter, tiny labels, AI gibberish text, overprocessed HDR, excessive saturation. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Five signposts in the stated order; five destination pins including "Catheter bridge"; only quoted words.
```

#### Clinician tab

### 08 — Cannulation techniques (clinician)

```
IMAGE NUMBER: 08
SECTION PLACEMENT: #md-cannulation, after the technique table
FILE NAME: hemodialysis-access-lifeline-08-cannulation-techniques.png
ARCHETYPE: Clinician reference card (infographic 5)
AUDIENCE: clinicians and dialysis nurses
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (three fistula renders)
- algorithm/flowchart: no
PURPOSE: Compare rope-ladder, buttonhole, and area puncture at a glance.
KEY CONCEPTS: site rotation; single tract; clustered punctures and aneurysm

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 clinician reference card, 1792 × 1024, white background, all text in IBM Plex Sans, navy text.
Headline top-left, bold: "Cannulation technique shapes the fistula".
Three equal columns, each with a softly shaded semi-3D render of the same straight forearm fistula vein (viewed from above, skin semi-transparent), and two short text lines below.
Column 1 title "Rope-ladder": eight small evenly spaced dot-pairs along the full vein length, numbered faintly 1 to 8; vein wall uniform. Line 1: "Sites rotate along the vessel". Line 2 with green check: "Default for most fistulas and all grafts".
Column 2 title "Buttonhole": one arterial and one venous small tract marked as tiny tunnels through the skin into the vein, reused; vein wall uniform. Line 1: "Same tract every session". Line 2 with amber circle-bar: "Selected patients; strict tract care; infection risk".
Column 3 title "Area puncture": many clustered dots in two small zones; the vein bulges into two aneurysmal swellings at those zones. Line 1: "Punctures cluster". Line 2 with red triangle: "Promotes aneurysm; discourage".
Bottom strip: "Assess before every session · Match difficult access to experienced cannulators · Ultrasound for new, deep, or tortuous vessels".
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, flat-vector clip-art, needles piercing visibly, blood, clutter, tiny labels, AI gibberish text, numbers other than site numbering, overprocessed HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No journal names, guideline acronyms, brands, or watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Aneurysms appear only in column 3; buttonhole shows two reused tracts; only quoted words.
```

### 09 — Monitoring versus surveillance (clinician algorithm)

```
IMAGE NUMBER: 09
SECTION PLACEMENT: #md-monitor
FILE NAME: hemodialysis-access-lifeline-09-monitoring-vs-surveillance.png
ARCHETYPE: Clinical algorithm (portrait), guideline-flowchart aesthetic
AUDIENCE: clinicians and dialysis nurses
DIMENSIONS: 1024 × 1536 (2:3 portrait)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: no
- algorithm/flowchart: yes
PURPOSE: Separate clinical concern, confirmation, and treatment decision; isolated numbers loop back.
KEY CONCEPTS: clinical indicators; confirm; decide with the team; repeat under comparable conditions

COPY-READY IMAGE GENERATOR GPT PROMPT:
Portrait clinical algorithm, 1024 × 1536, white background, all text in Inter, navy structure lines, rounded nodes, maximum 4 levels, generous whitespace.
Title, bold: "Concern, confirm, decide".
Level 1, teal monitoring node: "Clinical indicators at the chair" with a compact bullet list inside: "Abnormal exam (thrill, pulse, arm elevation)", "Difficult cannulation", "Prolonged bleeding after needles", "Rising venous pressure", "Falling achievable Qb", "Unexplained fall in Kt/V", "Arm or face swelling".
Side input on the right, gray dashed node feeding into Level 1 with a small loop arrow: "Isolated abnormal number (Qa or pressure)" → loop label "Repeat under comparable conditions; trend, don't react".
Level 2, teal node: "Confirm: duplex or angiography" with sub-text "Lesion present and hemodynamically relevant?"
Level 3, two branches: left green node "No relevant lesion → continue monitoring"; right amber node "Relevant lesion → team decision".
Level 4, under the amber node, navy-outlined node: "Weigh: access history, future options, patient goals → treat or observe".
Bottom footnote in small text: "A percentage stenosis alone is not a trigger."
Small semi-transparent "renalcarematters.com" bottom-center.

NEGATIVE INSTRUCTIONS:
Avoid spaghetti flowchart, more than 4 levels, cartoon style, flat clip-art icons, tiny unreadable labels, AI gibberish text, invented thresholds or numbers, drug names, overprocessed HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No journal names, guideline acronyms, brands, or watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
No numeric thresholds anywhere; the isolated-number node loops back rather than pointing to treatment; abbreviations used (Qa, Qb, Kt/V) match the figure's fig-abbrevs list.
```

### 10 — Rescue and succession (clinician algorithm)

```
IMAGE NUMBER: 10
SECTION PLACEMENT: #md-rescue
FILE NAME: hemodialysis-access-lifeline-10-rescue-algorithm.png
ARCHETYPE: Clinical algorithm (portrait)
AUDIENCE: clinicians (nephrology, interventional, vascular surgery)
DIMENSIONS: 1024 × 1536 (2:3 portrait)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (two tiny balloon and stent-graft icons)
- algorithm/flowchart: yes
PURPOSE: Show lesion-focused rescue chosen with future options in mind, and the review loop for repeated failure.
KEY CONCEPTS: dysfunction vs thrombosis; imaging; treatment options; MDT review; succession

COPY-READY IMAGE GENERATOR GPT PROMPT:
Portrait clinical algorithm, 1024 × 1536, white background, all text in Inter, navy structure lines, rounded nodes, maximum 5 levels.
Title, bold: "Rescue wisely, keep the next option".
Level 1, two entry nodes side by side: amber "Dysfunction (confirmed lesion)"; red "Thrombosed access".
Level 2: under the amber node, teal node "Lesion-focused treatment"; under the red node, red-outlined node "Prompt thrombectomy, then treat the cause".
Level 3, one wide teal options card listing four options with small softly shaded icons: balloon icon "Angioplasty (PTA)"; balloon with fine dots "Drug-coated balloon (DCB)"; covered tube icon "Stent-graft: uses outflow vein"; scalpel icon "Surgical revision".
Level 4, amber decision diamond: "Failure recurring?" → "No" arrow to green node "Monitor clinically; update the passport"; "Yes" arrow to navy node "MDT review: whole circuit, central veins, goals".
Level 5, under the MDT node, teal node "Succession: next access, PD, or transplant pathway".
Bottom footnote, small text: "Each procedure is also a decision about future sites."
Small semi-transparent "renalcarematters.com" bottom-center.

NEGATIVE INSTRUCTIONS:
Avoid spaghetti flowchart, more than 5 levels, drug doses, numeric thresholds, brand or device names, cartoon style, flat clip-art, tiny labels, AI gibberish text, overprocessed HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No journal names, guideline acronyms (other than PTA, DCB, MDT, PD), brands, or watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
No numbers anywhere; the stent-graft label mentions outflow; abbreviations on the image (PTA, DCB, MDT, PD) appear in the guide's fig-abbrevs or glossary.
```

### 13 — Access and heart: organ crosstalk sigil (clinician)

```
IMAGE NUMBER: 13
SECTION PLACEMENT: #md-cardiac
FILE NAME: hemodialysis-access-lifeline-13-access-heart-crosstalk.png
ARCHETYPE: Organ-crosstalk sigil (monoline organ icons with dotted flow lines)
AUDIENCE: clinicians
DIMENSIONS: 1024 × 1024 (1:1)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes (monoline sigil)
- 3D component graphics: no
- algorithm/flowchart: no
PURPOSE: Show the arteriovenous shunt adding to cardiac work, and the assessment loop.
KEY CONCEPTS: shunt flow (Qa); cardiac output (CO); congestion; assessment

COPY-READY IMAGE GENERATOR GPT PROMPT:
Square 1:1 minimal medical sigil, 1024 × 1024, ivory background (#fbf8f2), elegant monoline organ icons in navy with teal and amber accents, generous negative space, all text in Manrope.
Title top-center, small bold: "A high-flow access adds work for the heart".
Center: a monoline heart. Lower-left: a monoline forearm with a widened vein loop at the wrist labeled "Access (Qa)". Upper-left: monoline lungs labeled "Congestion". Lower-right: a monoline kidney labeled "Volume". Upper-right: a small monoline echocardiography probe labeled "Assess".
Connections: a thick teal dotted arrow from the forearm loop back to the heart labeled "Shunt flow"; a navy dotted arrow from the heart outward labeled "Cardiac output (CO) rises"; an amber dotted arrow from the heart to the lungs; a thin navy dotted arrow between the kidney and the heart; a teal dotted loop from "Assess" circling the heart.
Small footnote: "A flow value prompts assessment, not a diagnosis."
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid dense infographic, photorealism, 3D renders, numbers or thresholds, cartoon faces, clutter, tiny labels, AI gibberish text. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No brands, no watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
No numbers; abbreviations Qa and CO match fig-abbrevs; monoline style consistent across all icons.
```

### 14 — What is new and what is ready (clinician)

```
IMAGE NUMBER: 14
SECTION PLACEMENT: #md-new, after the table
FILE NAME: hemodialysis-access-lifeline-14-evidence-timeline.png
ARCHETYPE: Clinician reference card (infographic 5), dated timeline with readiness meters
AUDIENCE: clinicians
DIMENSIONS: 1792 × 1024 (16:9)
VISUAL MIX:
- photorealistic models: no
- 2D infographic: yes
- 3D component graphics: yes (small device icons)
- algorithm/flowchart: no
PURPOSE: Separate publication, validation, regulatory status, and local availability.
KEY CONCEPTS: dated milestones; evidence type; readiness

COPY-READY IMAGE GENERATOR GPT PROMPT:
Landscape 16:9 clinician timeline card, 1792 × 1024, white background, all text in IBM Plex Sans, navy text.
Headline top-left, bold: "Published is not the same as ready".
A horizontal timeline from left to right with year ticks: 2017, 2019, 2023, 2024, 2025, 2026.
Markers above the line, each a rounded card with a small softly shaded icon, a one-line label, and a readiness meter of five small segments filled to the stated level (filled segments teal, empty segments light gray):
2017 — capsule icon — "Fish oil and aspirin: no benefit" — meter 0 of 5, with a small gray "Not recommended" tag.
2019 — document icon — "Individualized Life-Plan" — meter 5 of 5.
2023 — balloon-with-dots icon — "Drug-coated balloon for fistula stenosis" — meter 3 of 5.
2023 — catheter-end icon — "Antimicrobial catheter lock" — meter 3 of 5.
2024 — tablet icon — "Anticoagulation after thrombectomy" — meter 2 of 5.
2025 — document icon — "Choice-based access guideline update" — meter 5 of 5.
2026 — tube-vessel icon — "Bioengineered vessel trial" — meter 1 of 5.
2026 — needle-catheter icon — "Endovascular fistula pooled data" — meter 2 of 5.
2026 — infrared lamp icon — "Far-infrared therapy: no benefit" — meter 0 of 5, gray "Not recommended" tag.
Legend bottom-left: "Readiness = evidence strength + replication + availability in the Philippines".
Small semi-transparent "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid journal names, trial acronyms, guideline acronyms, brand or device names, percentages, cartoon style, flat clip-art, clutter, tiny labels, AI gibberish text, overprocessed HDR. NEVER use dark backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No watermarks. Never omit renalcarematters.com.

QUALITY CHECK:
Nine markers with the stated years and meter levels; no trial or brand names; only quoted words.
```

---

## Part 3 — Wiring status

All 16 figures are already in the guide with `<picture>` (webp + png), descriptive `alt`, a plain-language `fig-desc` (four languages in patient sections), and `fig-abbrevs` lists for every abbreviation that appears on a clinician image. No HTML edits are needed when images arrive. If a render changes a label, update the matching `fig-abbrevs` list.

| ID | Abbreviations the guide already defines for that figure |
|---|---|
| 01 | AV |
| 02 | AVF, AVG, CVC (clinician copy) |
| 03 | AVF, NO, SMC, WSS (clinician copy) |
| 04 | AVF, AVG, PD (clinician copy) |
| 06 | US (clinician copy) |
| 08 | AVF |
| 09 | Qa, Qb, Kt/V |
| 10 | DCB, PTA, MDT |
| 11 | CRBSI, CVC (clinician copy) |
| 13 | Qa, CO |
| 14 | DCB, ATEV, eAVF |

## Part 4 — Stage 2 hand-off

1. Generate in the order in 1.6, saving each render under its exact file name.
2. Run the 1.7 QC rubric on every render; regenerate rather than edit pixels.
3. Convert each `.png` to a same-size `.webp`; place both in `images/`.
4. Run `python3 generate_rg_thumbs.py` once the OG card (006) is in place, then `python3 generate_latest_guides.py`.
5. Spot-check the guide in light and dark mode at 360 px and 1280 px wide.
