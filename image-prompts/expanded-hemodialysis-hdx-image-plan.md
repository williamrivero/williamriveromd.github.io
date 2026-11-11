# Image Plan: *Expanded Hemodialysis (HDx): What a Different Filter Can Change* (`expanded-hemodialysis-hdx.html`)

**Guide:** Expanded hemodialysis with medium cut-off (MCO) and super high-flux (SHF) membranes. Dual audience: Patients & Families (EN/TL/CEB/KAP) and Clinicians.
**Prepared:** 2026-11-10. **Pipeline:** Stage 1 (prompt authoring). Paste each `PROMPT` block into the ChatGPT **Image Generator** GPT at https://chatgpt.com/
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` · `williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure` · `williamriveromd-algorithm-generator-skill` (Mode C) · `williamriveromd-organ-crosstalk-sigil-graphic`

---

## Design intent: one idea per image, readable at every education level

HDx is an invisible change: the machine, chair and nurse look the same; only the filter's pores differ. The image set has to make that invisible difference **visible**, then keep readers honest about what is and is not proven. Each image carries one idea, so a reader who only looks at the pictures still leaves with the core message.

| Idea the reader must get | Patient image | Clinician image |
|---|---|---|
| Same chair, same machine — **only the filter changes** | #3 A different filter | #6 Internal filtration mechanism |
| Wastes come in **sizes**; HDx reaches the larger medium ones and tries to **keep albumin** | #4 Size ladder | #7 Sieving profiles |
| **How sure are we?** Removal is proven; living longer is not | #5 Evidence staircase | #8 Three evidence lanes |
| HDx is a **trial with a goal and a review date**, not a permanent switch on faith | — | #9 Pilot algorithm |
| Albumin has **many causes**; the filter is usually the smallest | (text only) | #10 Albumin sigil |

**Reading-level ladder.** Every patient image is built so it works at three levels at once:
1. **Picture level (no reading needed):** shapes, color and size carry the message (small dots pass, big spheres stay; a staircase with solid and dotted steps).
2. **Label level (Grade 4–6 English):** at most about 8 words per label, everyday words ("big waste," "the protein we keep"), no acronyms except HDx.
3. **Detail level:** the HTML caption and the guide text carry the numbers and terms, in four languages. Images never carry translated text, so one image serves EN/TL/CEB/KAP readers.

Clinician images may use correct technical labels (β2M, λ-FLC, MCO, SC) but keep each callout short and every number traceable to the guide.

## House rules baked into every prompt
- **Light backgrounds only** (white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, pale teal `#eef6f7`). Never navy, charcoal, or black fills.
- **Font:** on-image type is set in **Inter** (named in each prompt). Approved alternatives: Nunito Sans, IBM Plex Sans, Manrope. No serif or decorative faces.
- **Palette:** navy `#0f1e2e` (text and accents only), clinical teal `#1a6b72` (dialysis, the filter, HDx), renal green `#1f7a4d` (small wastes / safe / proven), amber `#b8860b` and orange `#c55a11` (the larger "target" wastes, caution), purple `#6c3d8e` (albumin — the protein we keep), red `#b91c1c` (urgent only).
- **Fixed color code across the set:** *green dots = small wastes*, *orange = larger medium wastes (the HDx target)*, *purple spheres = albumin*. Readers learn it in #4 and reuse it in #3, #6 and #7.
- **Attribution:** small, semi-transparent `© renalcarematters.com`, bottom-right (bottom-center on portrait), on every image **except the wordless vignette hero**.
- **American English** in all rendered text (hemodialysis, hemodiafiltration, fiber, color).
- **Style:** illustrated, softly rendered (GPT-rendered editorial or semi-3D), not flat clip-art vector. Mechanism figures follow the review-article schematic style but with gentle shading.
- **Save each asset** as `.png` plus a matching `.webp` twin in `images/`, using the exact FILE NAME given.

### Clinical guardrails for THIS guide (each must hold in every graphic)
1. **No promise of feeling better or living longer.** No glowing "after" faces, no heart-with-plus icons, no upward survival arrows next to HDx. Proven = removal; everything else is shown as partial, early, or unproven.
2. **HDx is not hemodiafiltration.** Never draw replacement-fluid bags or an HDF machine in an HDx image. HDF appears only in #8, in its own lane.
3. **Albumin is not an alarm.** Show albumin as "kept" (purple spheres staying in the blood), with at most one or two small spheres slipping through. Never a red warning on albumin in patient art.
4. **No brand names or readable packaging.** The dialyzer has no logo, model name, or text. No "Theranova," "Elisio," etc. anywhere.
5. **Dialyzer anatomy is correct (house hemofilter reference):** two END ports for blood (arterial in, venous out), two SIDE ports for dialysate on the shell with **countercurrent** flow (dialysate in near the venous end, out near the arterial end). Hollow fibers drawn as fine parallel lines. No replacement-fluid line on an HDx filter.
6. **Numbers only where supplied.** Do not let the generator invent pore sizes, sieving values, mmHg, or g/dL. #7 uses a qualitative y-axis; #8 shows only the numbers written in its prompt.
7. **No money imagery** (peso signs, wallets) in any image; cost lives in the text and calculator.
8. **Filipino clinical context**, calm daylight, no needles or blood visible in the hero.

## Asset roster

| # | File (`images/…`) | Placement in guide | Skill | Size |
|---|---|---|---|---|
| 1 | `expanded-hemodialysis-hdx-vignette-hero.png` | Patient hero disc | hero-vignette (Scaffold A, archetype H) | 2048×2048 |
| 2 | `expanded-hemodialysis-hdx-og.png` | `og:image` / social share | infographic (OG card) | 1200×630 |
| 3 | `expanded-hemodialysis-hdx-01-different-filter.png` | Patient §A Different Filter | infographic (editorial + 3D cutaway) | 1792×1024 |
| 4 | `expanded-hemodialysis-hdx-02-size-ladder.png` | Patient §Waste Sizes | simple-figure (Scaffold B, comparison) | 1792×1024 |
| 5 | `expanded-hemodialysis-hdx-03-what-we-know.png` | Patient §What the Research Shows | simple-figure (Scaffold C, steps) | 1792×1024 |
| 6 | `expanded-hemodialysis-hdx-04-internal-filtration.png` | Clinician §Mechanism | biomedical-mechanism | 1792×1024 |
| 7 | `expanded-hemodialysis-hdx-05-sieving-curves.png` | Clinician §Mechanism | simple-figure (Scaffold D) | 1792×1024 |
| 8 | `expanded-hemodialysis-hdx-06-three-lanes.png` | Clinician §Overview | infographic (clinician reference card) | 1792×1024 |
| 9 | `expanded-hemodialysis-hdx-07-pilot-algorithm.png` | Clinician §Practice & Pilot | algorithm (Mode C, house style) | 1792×1024 |
| 10 | `expanded-hemodialysis-hdx-08-albumin-crosstalk.png` | Clinician §Albumin | organ-crosstalk sigil (labeled) | 1792×1024 |

> **Wiring status (updated 2026-11-10).** All 10 images plus the `-rg-thumb.webp` are generated, committed, and rendering (sizes verified: hero 2048×2048, OG 1200×630, figures 1792×1024, thumb 600×600). All 10 references exist in the guide HTML with matching file names, `width`/`height`, `alt` text, and lightbox captions (`.fig-desc` plus `.fig-abbrevs`). Until each file is committed, that figure shows its alt text. #9 is declared 1792×1024 in the HTML, so it is drawn **landscape** (left-to-right algorithm) rather than the usual portrait.
>
> **Derived asset (no separate prompt):** `expanded-hemodialysis-hdx-rg-thumb.webp`, a 1:1 center crop of the OG card (#2), for Related-guides cards on sibling guides.

---

## 1 · Circular vignette hero *(patient hero disc)*

```
FILE NAME: expanded-hemodialysis-hdx-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3, Scaffold A clinical people scene
ASPECT RATIO: 1:1 (square, displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: H, Clinical (one calm consultation moment at the dialysis chair)
CAMERA: side-profile environmental portrait, seated eye level, gentle shallow depth of field
HUMAN VARIATION (vs. previous guide, incremental-dialysis, one woman in her late 30s standing at
  home, seen from behind): two people (not one); patient in her mid-60s (not 30s); seated in a
  dialysis chair (not standing); dialysis unit (not home); side profile (not rear three-quarter);
  short silver-gray bob with a soft side part (not long dark bun); fuller, rounded build (not slim);
  deep warm-brown skin (not medium-tan); thin tortoiseshell reading glasses on a beaded chain; a
  soft lavender cardigan over a cream blouse (not mustard linen); a small jade bangle; hands resting
  together on a folded knit blanket; open, curious smile looking at the object (not quiet profile);
  afternoon light (not morning); clinician present: a Filipino male dialysis nurse in his early 30s
  with a neat undercut, light-medium skin, navy scrubs, a clip-on ID badge with no readable text.
AUDIENCE: patients and families
VISUAL GOAL: "Same chair, same care — the team is showing me a different filter," wordless.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER
around the full circle (the circle must never touch the canvas edges). Composition archetype:
Clinical. Camera: side-profile environmental portrait at seated eye level, gentle shallow depth
of field.

Subject: in a bright, clean, modern Philippine hemodialysis unit, a Filipino woman in her mid-60s
sits comfortably reclined in a light-gray dialysis chair. She has a short silver-gray bob with a soft
side part, deep warm-brown skin, a fuller rounded build, thin tortoiseshell reading glasses on a
beaded chain, a soft lavender cardigan over a cream blouse, and a small jade bangle; a folded
cream knit blanket covers her forearms (no needles, tubing at the arm, or blood visible). She looks
with an open, curious smile at a clean, unbranded dialysis filter cartridge — a clear cylinder with
fine parallel hollow fibers visible inside, two capped end ports and two small side ports, with NO
logo or printed text — that a Filipino male dialysis nurse in his early 30s (neat undercut,
light-medium skin, navy scrubs, ID badge with no readable text) holds up at her eye level with
both hands, mid-explanation, friendly and unhurried. Supporting context, softly out of focus: the
side of a dialysis machine in pale teal and white behind the chair, a window with afternoon light,
and a small potted plant on a sill.

Visual hierarchy: the patient, the nurse's hands and the filter occupy 60–70% of the circle; 2–3
supporting context cues fill 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft out-of-focus pale
wall and window glow in the upper-left of the circle (no faces, hands, equipment or objects inside
that zone).

Calm, warm, documentary-realistic color grade harmonizing with clinical teal #1a6b72, navy
#0f1e2e accents and warm neutrals on a light background. Slight edge falloff toward a soft neutral
at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, brand name on the
filter or machine, screen readouts, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, dozens of icons, tiny
unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle,
cropped objects, edge clipping, objects touching the circular border, important content inside
the title safe zone, baked-in text, titles, captions, logos, brand names, watermarks, rectangular
borders, frames, banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR,
over-saturation, distorted hands or faces, needles, visible blood, blood-filled tubing, replacement
fluid bags, money imagery.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin, never cropped.
One dominant moment (patient looking at the filter the nurse holds) at 60–70%; 20–25% empty
title-safe zone upper-left. Filter has two end ports, two side ports, fine fibers, no text.
No needles or blood. Patient and nurse differ in ≥12 traits from the incremental-dialysis hero.
No text anywhere.
```

---

## 2 · OG / social share card *(`og:image`)*

```
FILE NAME: expanded-hemodialysis-hdx-og.png
IMAGE TYPE: OG / social share card (infographic skill, editorial + 3D component)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed (patients, families, clinicians on Facebook / Viber / LinkedIn)
VISUAL GOAL: In one glance: "a different dialysis filter lets more medium-sized wastes out while
keeping albumin in."

PROMPT:
Social share card, exactly 1200×630 px, landscape, white (#ffffff) background with a very soft
pale-teal (#eef6f7) panel on the right 45%. LEFT 55%: typography stack set in Inter — small teal
(#1a6b72) uppercase eyebrow "DIALYSIS · NEW GUIDE"; bold navy (#0f1e2e) title on two lines
"Expanded Hemodialysis (HDx)"; teal subtitle "What a different filter can change"; one short navy
line "More large wastes out · albumin kept · evidence explained". Generous left margin, nothing
closer than 60 px to any edge. RIGHT 45%: a semi-photorealistic 3D render of a single hollow fiber
cut lengthwise and magnified, lying diagonally, with its wall shown as a porous membrane; small
green dots (small wastes) and slightly larger orange beads (medium wastes) pass outward through
the pores into the surrounding pale fluid, while two or three larger soft-purple spheres (albumin)
stay inside the fiber. A faint, out-of-focus silhouette of a dialysis filter cartridge (no logo,
no text) sits behind the fiber for context. Soft studio light, gentle shadow, calm clinical look.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, brand names or logos on any
device, unrealistic anatomy, HDR, excessive saturation, money imagery, people's faces. NEVER use a
dark, navy, charcoal, or black background — light only. Use ONLY Inter (or Nunito Sans, IBM Plex
Sans, Manrope) — no serif or decorative fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Title readable at thumbnail size. Color code holds (green small, orange medium,
purple albumin kept). Text spelled exactly as given, American English. Attribution bottom-right.
```

---

## 3 · A different filter *(patient §A Different Filter)*

```
FILE NAME: expanded-hemodialysis-hdx-01-different-filter.png
IMAGE TYPE: Patient education infographic — photorealistic scene + 3D cutaway inset (infographic skill)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families (any education level)
VISUAL GOAL: Show that everything at the chair is familiar and only the filter's pores change.

PROMPT:
Landscape 16:9 patient-education illustration, white (#ffffff) background, set in Inter. Title at
top-left in bold navy (#0f1e2e): "Same chair. Same machine. A different filter." LEFT HALF: a
softly rendered, photorealistic-illustrated scene of a Filipino man in his fifties (short graying
hair, light-brown skin, gray polo shirt) resting in a light-gray hemodialysis chair beside a
white-and-pale-teal dialysis machine, a calm nurse adjusting nothing in particular in the
background, soft daylight; his access arm under a blanket (no needles or blood visible). The
dialysis filter on the machine's side is circled with a thin teal (#1a6b72) ring, and a dashed teal
leader line runs to the RIGHT HALF.
RIGHT HALF: a large magnified 3D cutaway inside a dashed rounded box: one hollow fiber cut
lengthwise, blood flowing left to right inside it (soft red-pink), cleaning fluid flowing the
opposite way outside it (pale blue arrows), wall drawn as a porous membrane with evenly sized,
slightly larger pores. Small green dots (labeled "small wastes") and medium orange beads (labeled
"larger wastes") pass out through the pores into the cleaning fluid; two or three large soft-purple
spheres (labeled "albumin — kept in") stay inside the blood, with just one small purple sphere
near the wall to suggest "a little may pass." Three short labels only, each ≤ 4 words, in navy.
Bottom strip in very soft gray (#f3f4f6), one navy sentence: "HDx changes only the filter — your
team checks how it works for you." Bottom-right: "© renalcarematters.com" in small semi-transparent
navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, AI gibberish text, brand names or logos, replacement-fluid
bags, HDF equipment, needles, visible blood in tubing near the patient, distorted hands or faces,
HDR, dark backgrounds. Inter (or approved sans-serif) only. Never omit the attribution.

QUALITY CHECK:
Readable on a phone. Exactly three object labels plus title and bottom sentence. Countercurrent
flow shown (blood one way, cleaning fluid the other). Albumin clearly mostly stays in. Matches the
alt text: man in his fifties, magnified fiber, small and medium wastes pass, albumin stays.
```

---

## 4 · Waste size ladder *(patient §Waste Sizes)*

```
FILE NAME: expanded-hemodialysis-hdx-02-size-ladder.png
IMAGE TYPE: Simple figure — Scaffold B side-by-side comparison (two sieves)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Wastes have sizes; the regular filter lets small ones through, the HDx filter also lets
larger medium ones through, and both hold back albumin.

PROMPT:
Medical education comparison infographic, white (#ffffff) background, set in Inter. Title centered
at top in bold navy (#0f1e2e): "Different sizes of waste — and the protein we keep". Under the
title, a horizontal SIZE RULER running left to right from "small" to "large" (words only, no
numbers), with four softly shaded 3D objects sitting on it, growing in size: a tiny green dot
"urea", a small teal-green bead "β2-microglobulin", a medium orange bead "light chains", and a
large soft-purple sphere "albumin". Below the ruler, two stacked horizontal panels separated by a
soft dashed line, each showing a curved sieve membrane with evenly drawn pores:
Upper panel, label at left in teal: "Regular filter" — only the green dot and the small bead pass
through the pores (arrows down into pale-blue fluid); the orange bead and purple sphere rest above.
Lower panel, label at left in teal: "HDx filter" — slightly larger, more even pores: green dot, small
bead AND orange bead pass through; the purple sphere still rests above the sieve, with one tiny
purple sphere just at a pore to suggest "a little may pass."
To the right of the lower panel, a small purple tag: "Albumin mostly stays — the team checks it."
Rounded corners, generous whitespace, labels ≥ 11 pt equivalent, no more than 6 words per label.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, numbers or dalton values on
the image, red warning colors on albumin, brand names, dark backgrounds. Inter (or approved
sans-serif) only. Never omit the attribution.

QUALITY CHECK:
Color code holds (green/teal-green small, orange medium, purple albumin). The ONLY difference
between panels is which beads pass. No numbers rendered. Readable on a phone.
```

---

## 5 · How sure are we? *(patient §What the Research Shows)*

```
FILE NAME: expanded-hemodialysis-hdx-03-what-we-know.png
IMAGE TYPE: Simple figure — Scaffold C horizontal step sequence (evidence staircase)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients and families
VISUAL GOAL: Make the strength of evidence visible: one solid step, one firm step, one dotted step,
one outlined "not yet" step.

PROMPT:
Clean patient-education infographic, white (#ffffff) background, set in Inter. Title at top center
in bold navy (#0f1e2e): "How sure are we about HDx?" Four wide steps rising left to right like a
gentle staircase, each step a rounded block with a small icon on top and a short label underneath:
Step 1 (lowest, SOLID renal-green #1f7a4d fill, crisp edges): icon of a filter with small beads
passing; label "Removes more large wastes"; tag "Proven".
Step 2 (SOLID clinical-teal #1a6b72 fill, slightly lighter): icons of a scratching hand crossed out
softly and a small clock; label "Less itch, quicker recovery"; tag "Some evidence".
Step 3 (amber #b8860b, DASHED outline with pale amber fill): icon of a small kidney with a drop;
label "Protects remaining kidney work"; tag "Early, promising".
Step 4 (highest, GRAY dotted outline, white fill, a soft question mark inside): icon of a calendar
with a heart outline; label "Helps people live longer"; tag "Not yet proven — large trial under way".
Tags in small rounded pills under each label. A thin navy line under the staircase reads: "The
higher the step, the less certain we are." Generous whitespace, no more than 6 words per label.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, AI gibberish text, numbers, percentages, upward arrows
implying guaranteed benefit, smiling "after" faces, trophies, brand names, dark backgrounds. Inter
(or approved sans-serif) only. Never omit the attribution.

QUALITY CHECK:
Step 1 visibly the most solid, step 4 visibly the least (outline + question mark). Wording exactly
as given. Readable on a phone.
```

---

## 6 · Inside one MCO fiber *(clinician §Mechanism)*

```
FILE NAME: expanded-hemodialysis-hdx-04-internal-filtration.png
IMAGE TYPE: Biomedical mechanism figure (organ/device panel → magnified inset → bottom flow)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show internal filtration and backfiltration along one fiber, and why MCO pores remove
large middle molecules while retaining most albumin.

PROMPT:
Create a publication-grade biomedical mechanism schematic in review-article style, softly shaded
semi-3D, white background, muted clinical palette, labels set in Inter, thin dashed connectors.
Title top-left in navy: "Expanded hemodialysis: internal convection in a medium cut-off fiber".

LEFT PANEL (device-level context): a vertical hollow-fiber dialyzer cartridge drawn per house
anatomy — blood IN at the bottom END port ("arterial, blood in"), blood OUT at the top END port
("venous, blood out"), fine parallel fiber lines inside; dialysate IN through a SIDE port near the
top (venous end) and dialysate OUT through a SIDE port near the bottom (arterial end), arrows
showing countercurrent flow. NO replacement-fluid line. A small dashed box on one fiber connects
to the magnified panel.

CENTER-RIGHT MAGNIFIED PANEL (dashed border): one hollow fiber drawn horizontally, blood flowing
left to right (soft red), dialysate flowing right to left outside (pale blue). Beneath the fiber, a
thin gradient bar labeled "blood-side pressure ↓ along fiber" and "dialysate-side pressure ↑".
Near the blood inlet (left third): outward teal arrows labeled "Internal filtration". Near the
outlet (right third): inward blue arrows labeled "Backfiltration". In the middle, the membrane wall
enlarged to show a tight, uniform pore distribution, with small green dots (urea), teal beads
(β2M), and orange beads (λ-FLC) crossing outward, while purple spheres (albumin) are retained, one
small purple sphere at a pore labeled "small albumin loss". Two short side callouts: "Narrower
fiber → ↑ axial pressure drop" and "Tighter pore size distribution".

BOTTOM SUMMARY FLOW (three boxes with arrows):
Left pale-pink box "Design": "Larger, uniform pores" · "Smaller fiber inner diameter".
Center pale-gray box "Process": "↑ Internal convection" · "Net fluid removal unchanged".
Right pale-blue box "Result": "↑ Large middle-molecule removal" · "Small albumin loss — monitor" ·
"Dialysate purity matters (backfiltration)".

Footnote line in small gray: "Internal convection is not measured or prescribed like HDF convection volume."
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, AI gibberish text, brand
names, numeric pressures or pore sizes, replacement-fluid bags or lines, swapped dialysate ports,
co-current dialysate flow. Inter (or approved sans-serif) only. Never omit the attribution.

QUALITY CHECK:
Port topology correct (two end blood ports, two side dialysate ports, countercurrent). Filtration
near inlet, backfiltration near outlet. No invented numbers. Labels legible at slide size.
```

---

## 7 · Sieving profiles *(clinician §Mechanism)*

```
FILE NAME: expanded-hemodialysis-hdx-05-sieving-curves.png
IMAGE TYPE: Simple figure — Scaffold D single mechanism (qualitative curve chart)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Show, qualitatively, where each membrane class loses permeability relative to the
molecular landmarks — the MCO goal is a steep drop between λ-FLC and albumin.

PROMPT:
Clean scientific chart illustration, white (#ffffff) background, set in Inter. Title top-left in
bold navy: "Membrane sieving profiles (schematic, not bench data)". A single chart: x-axis
"Molecular mass (log scale)" with NO numeric tick values; y-axis "Sieving coefficient" with only
the words "high" at top and "low" at bottom, no numbers. Four smooth S-shaped descending curves,
each a distinct color and labeled at its right end:
"Low-flux" (gray) drops earliest, at the far left;
"High-flux" (teal #1a6b72) stays high past urea and drops before the β2M marker region ends;
"MCO" (orange #c55a11, slightly thicker line) stays high through the β2M and λ-FLC markers, then
drops steeply just before albumin;
"High cut-off" (muted purple, dashed line) stays high past albumin.
Four thin vertical dashed landmark lines with small labels at the top: "urea", "β2M ~12 kDa",
"λ-FLC ~45 kDa", "albumin ~66 kDa". A soft orange shaded wedge between the λ-FLC and albumin lines
labeled "MCO design goal: steep drop here". Small note under the chart in gray: "Curves are
illustrative; device sieving depends on test conditions." Generous whitespace.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid numeric y-axis values, invented sieving coefficients, numeric x ticks other than the four
landmark labels given, clutter, AI gibberish text, brand names, 3D effects on the chart, dark
backgrounds. Inter (or approved sans-serif) only. Never omit the attribution.

QUALITY CHECK:
Order of drop-off left to right: low-flux → high-flux → MCO → high cut-off. MCO drop sits between
λ-FLC and albumin. Only the landmark labels carry kDa values. Matches the HTML caption.
```

---

## 8 · Three evidence lanes *(clinician §Overview)*

```
FILE NAME: expanded-hemodialysis-hdx-06-three-lanes.png
IMAGE TYPE: Clinician reference card — three-lane comparison (infographic skill)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Keep MCO HDx, Japanese SHF, and high-volume online HDF visibly separate, each with its
own setup and its own strongest evidence.

PROMPT:
Clinical reference infographic card, publication-grade nephrology design, white (#ffffff)
background, set in Inter. Title top-left in bold navy (#0f1e2e): "Three lanes, three evidence bases".
Three tall rounded columns side by side, each with a small semi-3D device icon at the top, a
one-line setup description, and an evidence badge at the bottom.
Column 1, header band teal (#1a6b72): "MCO HDx". Icon: standard dialysis machine with a single
unbranded filter highlighted. Setup: "Standard HD machine · MCO dialyzer". Middle bullets: "↑ λ-FLC
removal (33% vs 17%, RCT)" · "Small early albumin dip". Badge (green check + gray question mark):
"Removal: strong · Survival: unproven".
Column 2, header band slate-blue: "Japanese SHF". Icon: filter with a small registry/database
symbol. Setup: "Classified by β2M clearance ≥ 70 mL/min and albumin sieving". Badge (purple):
"Registry associations (Japan)".
Column 3, header band renal green (#1f7a4d): "High-volume online HDF". Icon: HDF machine with an
ultrapure-fluid module and a substitution line into the BLOOD line (post-filter). Setup: "≥ 23 L
convection per session". Middle bullet: "All-cause death HR 0.77 (CONVINCE)". Badge (green
double-check): "Randomized survival evidence".
A thin gray footer across all columns: "Do not transfer evidence between lanes."
Generous whitespace, column headers ≥ 14 pt equivalent, bullets ≤ 7 words.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid clutter, tiny labels, AI gibberish text, brand names, any numbers other than those written
above, replacement fluid shown entering a filter's side port, dark backgrounds, photorealistic
people. Inter (or approved sans-serif) only. Never omit the attribution.

QUALITY CHECK:
Exactly three lanes with distinct colors. Only these numbers appear: 33% vs 17%, ≥ 70 mL/min,
≥ 23 L, HR 0.77. HDF substitution line enters the blood line, not the filter shell.
```

---

## 9 · Selective HDx pilot algorithm *(clinician §Practice & Pilot)*

```
FILE NAME: expanded-hemodialysis-hdx-07-pilot-algorithm.png
IMAGE TYPE: Clinical algorithm — Style Mode C (renalcarematters.com house style), landscape
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians, dialysis nurses, medical directors
VISUAL GOAL: Optimize standard HD first, offer high-volume HDF where deliverable, and run HDx as a
goal-defined, time-limited trial with clear continue / revert / escalate exits.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house
style, landscape, flowing LEFT TO RIGHT. White background, navy (#0f1e2e) and teal (#1a6b72)
typography set in Inter, thin teal connector arrows, generous margins, rounded rectangles for
actions, diamonds for decisions.
Title top-left in navy: "Selective HDx pilot".

Content to render:
1. Start node (navy outline): "Stable adult on maintenance HD".
2. Action (teal): "Optimize standard care — time, Kt/V, access, volume, nutrition, symptom causes".
3. Decision diamond (teal): "High-volume online HDF deliverable and suitable?"
   - YES branch (upward, green node #1f7a4d): "Discuss HDF — randomized survival evidence".
   - NO branch (forward): continue.
4. Decision diamond: "One measurable goal? (itch, recovery time, fatigue)"
   - NO branch (downward, soft gray node): "Stay on current dialyzer; review later".
   - YES: continue.
5. Action (teal): "Baseline: goal score · albumin (same assay, same weekday) · adequacy".
6. Action (teal): "Switch to MCO dialyzer · monitor at 2–4 weeks, then monthly".
7. Decision diamond (amber #b8860b node border): "Review at ~12 weeks: goal improved and safe?"
   - YES (green endpoint): "Continue HDx".
   - NO (gray endpoint): "Return to prior dialyzer".
8. Side caution node attached below step 6 by a dashed line (amber fill pale, red #b91c1c text
   header "Escalate now"): "Sustained unexplained albumin fall · nutritional decline · falling
   adequacy · suspected reaction".
Small gray side note under the title: "Proposed local workflow — not a guideline."
Consistent node widths, maximum 8 words per line inside nodes, no more than three branching levels.
Include a small professional footer reading "© renalcarematters.com" positioned at the bottom-right
corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid spaghetti arrows, crossing lines, clutter, tiny text, AI gibberish, brand names, photorealistic
people, numeric albumin thresholds, dark backgrounds, serif fonts.

QUALITY CHECK:
Reads left to right in one pass. HDF branch appears BEFORE the HDx trial. Three exits are distinct
(continue, revert, escalate). Only "2–4 weeks" and "~12 weeks" appear as numbers.
```

---

## 10 · What moves serum albumin *(clinician §Albumin)*

```
FILE NAME: expanded-hemodialysis-hdx-08-albumin-crosstalk.png
IMAGE TYPE: Organ-crosstalk sigil (labeled variant)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians and dietitians (also readable by patients)
VISUAL GOAL: Serum albumin sits at the meeting point of many forces; dialyzer loss is usually the
smallest one.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration on a white background, landscape.
CENTER: a single soft-purple droplet icon labeled "Serum albumin". Around it, in a balanced radial
arrangement, six minimal monoline icons, each connected to the center by a dotted curved arrow:
top: a liver icon labeled "Synthesis" (arrow pointing IN, solid-looking dots);
upper right: a small flame icon labeled "Inflammation" (arrow pointing OUT);
lower right: a bowl-and-spoon icon labeled "Protein intake" (arrow IN);
bottom: a water-drop icon labeled "Dilution (fluid excess)" (arrow OUT);
lower left: a kidney icon labeled "Urinary loss" (arrow OUT);
upper left: a dialyzer cartridge icon (two end ports, two side ports, no text) labeled "Dialyzer
loss" — its dotted arrow drawn the THINNEST and lightest of all six.
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette with the purple droplet as
the only purple element, generous whitespace, no photorealism, no 3D. All labels set in Inter,
navy, short. Small gray line at the bottom center: "Look at the whole picture before blaming the
membrane." Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, excessive labels, numbers, dark background, neon,
crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, serif or decorative fonts.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Six spokes, balanced. Dialyzer spoke visibly the faintest. Arrow directions: synthesis and intake
IN; inflammation, dilution, urinary and dialyzer loss OUT. Only the labels given appear.
```

---

## After generation: checklist

1. Save each PNG to `images/` with the exact file name, and export a `.webp` twin (quality about 82).
2. Keep #1 square at 2048×2048 (the HTML declares `width="2048" height="2048"`). All in-body figures are declared 1792×1024; if a render comes back at a different size, update that `<img>`'s `width`/`height`.
3. Export `expanded-hemodialysis-hdx-rg-thumb.webp` (1:1 center crop of #2, about 600×600).
4. Run `python3 patch_hero_fetchpriority.py --guide expanded-hemodialysis-hdx.html` and `python3 patch_image_lightbox.py --guide expanded-hemodialysis-hdx.html`.
5. Spot-check every rendered label for spelling (American English) and for invented numbers; regenerate any image that adds a number, a brand name, or a replacement-fluid line to an HDx filter.
6. Open the guide in light and dark mode: figures sit on light `.illus-wrap-light` cards in both themes, so no dark variant is needed.
7. Commit the images to `main`.
