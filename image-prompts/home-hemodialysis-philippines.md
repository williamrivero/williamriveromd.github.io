# IMAGE PLAN — Why Home Hemodialysis Is Difficult to Run in the Philippines

**Guide:** `guides/home-hemodialysis-philippines.html`
**Canonical URL:** https://renalcarematters.com/guides/home-hemodialysis-philippines.html *(not yet deployed)*
**Total images:** 8 (2 already specified, 6 new)
**Visual anchor:** `ckd-understanding-overview.webp`
**Skills used:** `williamriveromd-image-planner` (plan structure) · `williamriveromd-hero-vignette` (IMG 1) · `williamriveromd-infographic-skill` (IMG 2, 5) · `williamriveromd-simple-figure` (IMG 4, 6, 7, 8) · `williamriveromd-biomedical-mechanism-figure` (IMG 3)
**Generated:** 17 August 2026

Stage 1 output (prompt authoring). Paste each **PROMPT** block into the ChatGPT
Image Generator GPT: https://chatgpt.com/g/g-pmuQfob8d-image-generator

---

## 0. Architecture decisions (read before generating)

### 0.1 Why 8 images and not the planner's cap of 6

The planner caps a guide at 6 images "unless the guide is explicitly a
multi-chapter reference." This guide qualifies: **17 sections, ~9,000 English
words, dual-mode**, with eight discrete barrier chapters and a separate
first-principles physiology chapter. The image budget is split deliberately —
**4 patient-mode, 4 clinician-mode** — so neither audience tab carries an
unillustrated wall of text.

### 0.2 Three visuals deliberately NOT generated as images

The source blueprint required a barrier system map, a "where responsibility
moves" comparison, and an evidence map. All three are **already built as
accessible inline HTML inside the guide** and must stay that way:

| Blueprint visual | Where it lives | Why it stays HTML |
|---|---|---|
| Barrier system map (7-step feedback loop) | `#md-thesis` → `.chain` | Carries a `role="figure"` label and a prose text equivalent in the DOM; a raster image would drop both. |
| Where responsibility moves (3 columns) | `#md-responsibility` → `.resp-cols` | Reflows to a single column at 320 px; a fixed-width image would force horizontal scroll. |
| Evidence map (barrier × source-type matrix) | `#md-evidence-map` → `.table-wrap` | Its cells change whenever a regulator answers. Editable HTML; a rendered image would go stale silently. |

Generating raster duplicates of these would create two sources of truth for the
guide's most contestable claims. Do not add them later without removing the
inline versions.

### 0.3 Style-system arbitration

The four skills disagree on two points. Resolved as follows, and applied
uniformly across all eight prompts:

| Conflict | Resolution | Reason |
|---|---|---|
| Gold accent: planner `#d4af4f` vs infographic/simple-figure/mechanism `#b8860b` | **`#b8860b`** | Three of four skills concur; `#d4af4f` fails contrast as text on white. |
| File extension: planner `.webp` vs infographic `.png` | **Generate `.png`, ship `.png` + `.webp` twin** | `.png` is gpt-image-1's native output; the guide's `<picture>` markup already expects both. |

**Absolute rules enforced in every prompt** (from the infographic skill's
constitution, which overrides the planner where they differ): light backgrounds
only — navy/charcoal/black are never a background fill; typography restricted to
Inter, Nunito Sans, IBM Plex Sans or Manrope, named explicitly; and the
`williamriveromd.com` attribution on every image except IMG 1, which is wordless
by vignette-hero spec.

### 0.4 Editorial constraint inherited from the guide

This guide's discipline is calibrated certainty. **No image may state a claim
more confidently than the prose does.** Concretely: surrogate outcomes must be
labelled as surrogates (IMG 7), household assessment must read as a conversation
rather than a pass/fail checklist (IMG 6), and no image may imply that home
hemodialysis is prohibited in the Philippines or that a national pathway exists.
No image contains needles in skin, blood, or distress imagery.

### 0.5 Batching (5 requests / 60 s hard limit)

| Batch | Images | Action |
|---|---|---|
| 1 | IMG 1, 2, 3, 4, 5 | Submit all five |
| — | — | **Wait a full 60 seconds** |
| 2 | IMG 6, 7, 8 | Submit remaining three |

---

## IMAGE 1 — HERO (circular vignette)

**Placement:** `figure.hero-figure > .hero-vignette`, beside the `<h1>`
**Style:** Circular vignette hero v3, Scaffold B (still-life / object hero) — the guide's thesis is that a machine arrives without the system around it, so an empty, waiting room states it before a word is read.
**Filename:** `home-hemodialysis-philippines-vignette-hero.png` (+ `.webp`)
**Already wired in the guide:** yes — `width="2048" height="2048"`

```
FILE NAME: home-hemodialysis-philippines-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold B (still-life / object hero, no people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling
CAMERA: Wide-angle environmental, slightly low eye level, from the doorway
HUMAN VARIATION (vs. previous guide): No people — deliberate rotation away from the
  previous two guides in this library, which both featured Filipino human subjects
  (a nephrologist portrait collage and a family meal scene).
AUDIENCE: Mixed (patients, families, clinicians, policymakers)
VISUAL GOAL: A hospital-grade dialysis machine standing alone in an ordinary Filipino
  living room — clinical technology dropped into domestic space, with nobody yet
  trained to run it.

PROMPT:
Square 1:1 photorealistic editorial still-life on a 2048×2048 canvas, composed to be
displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a
visible WHITE BORDER around the full circle (the circle must never touch the canvas
edges). Composition archetype: J, Environmental Storytelling — one cohesive scene, no
floating panels or collage tiles. Camera: wide-angle environmental view from the
doorway, slightly below eye level.

Subject: a single modern hemodialysis machine on castors — a tall white-and-grey
clinical console with a hollow-fibre dialyzer mounted vertically on its front, coiled
clear blood tubing, and a small dark screen that is switched off — standing on the
tiled floor of an ordinary, modest Filipino living room. Beside it, one empty reclining
chair with a folded clean towel on the armrest. Supporting environmental details, small
and quiet: morning light falling through jalousie windows, a plain painted wall, a
single household electrical outlet low on the wall with the machine's cable running to
it, and a short length of drainage tubing disappearing toward a doorway. Everything is
clean, ordinary and domestic — a family home, not a clinic.

Visual hierarchy: the dialysis machine and chair occupy 60–70% of the circle, placed
right of centre; 2–4 supporting environmental elements (window light, wall outlet,
drainage line, tiled floor) occupy 20–30%; reserve the UPPER-LEFT 20–25% of the circle
as a TITLE SAFE ZONE of softly lit blank wall and diffuse window glow, containing no
objects, equipment, cables, furniture, faces or callouts.

Bright, airy, calm documentary colour grade harmonizing with clinical teal #1a6b72 and
navy #0f1e2e against a light background of warm white wall and pale floor tile. Gentle
shallow depth of field, soft natural daylight, no dramatic shadows. Soft edge falloff
toward a slightly deeper warm neutral at the rim. Full-bleed within the inscribed
circle, no rectangular borders, frames or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, machine screen
readout, readable equipment branding, logo, or williamriveromd.com watermark. The
machine's display is dark and blank.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons,
tiny unreadable labels, infographic clutter, any people at all, cropped circle, cropped
objects, edge clipping, objects touching the circular border, important content inside
the title safe zone, baked-in text, titles, captions, logos, watermarks, readable
branding on the machine, rectangular borders, frames, banners, dark / charcoal / black
backgrounds, hospital-ward or ICU look, cartoon style, neon, HDR, over-saturation,
implausible equipment anatomy, tangled or physically impossible tubing.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never
cropped. ONE dominant hero subject (machine + chair) at 60–70% of the circle, 2–4
supporting environmental elements, upper-left 20–25% title-safe zone left as soft lit
wall. Unmistakably a home rather than a clinic. No people, no text anywhere. Dialyzer
mounted plausibly with physically coherent tubing. Nothing lost at the circle's edge.
```

---

## IMAGE 2 — OG / SOCIAL SHARE CARD (also the inline lead figure)

**Placement:** first `<figure>` inside `<main>`, immediately above the evidence-status banner
**Style:** Photorealistic editorial hero + light diagrammatic overlay (Archetype 1) — the argument is a *transfer* of responsibility, which needs two places in one frame.
**Filename:** `home-hemodialysis-philippines-og.png` (+ `.webp`)
**Already wired in the guide:** yes — `og:image:width` 1200, `og:image:height` 630

```
FILE NAME: home-hemodialysis-philippines-og.png
IMAGE TYPE: Photorealistic editorial hero + light diagrammatic overlay (Archetype 1)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: Mixed (patients, families, clinicians, policymakers, health journalists)
VISUAL GOAL: The article's whole argument in one frame — everything a licensed clinic
  supplies as a *building* has to be rebuilt as a *service* that reaches one living room.

PROMPT:
Photorealistic medical editorial share card for a nephrology policy article, landscape
1200 × 630, split composition on a bright light background.

LEFT HALF (approximately 45% of the frame): a bright, busy, licensed Philippine
hemodialysis clinic photographed in clean natural daylight — an orderly row of four or
five hemodialysis machines beside reclining chairs, a Filipino dialysis nurse in scrubs
standing attentively mid-frame checking a machine, a glimpse through an interior window
of a water-treatment room with vertical reverse-osmosis columns and blue pressure
vessels, and a wall-mounted emergency light. Institutional, staffed, supervised.

RIGHT HALF (approximately 45% of the frame): the same lighting and colour grade, but a
single modest Filipino living room — one hemodialysis machine beside one reclining
chair, one older Filipino woman seated calmly with a light blanket over her lap, and one
adult daughter standing beside her looking at the machine. Domestic tiled floor, plain
painted wall, jalousie window, a small stack of supply boxes in the corner. Quiet,
ordinary, unsupervised.

CONNECTING THE TWO HALVES: five or six thin dashed teal (#1a6b72) lines arcing from the
clinic side across the seam into the living room, each carrying one short label set in
small clean sans-serif navy (#0f1e2e) capitals: TRAINING · TECHNICAL SERVICE · TREATED
WATER · SUPPLIES · 24/7 SUPPORT · BACKUP CARE. Keep these labels sparse, legible on
mobile, and clearly secondary to the photography — they are annotation, not an
infographic.

TITLE: across the upper portion of the frame, in bold navy (#0f1e2e) Inter, two lines,
generously letterspaced and mobile-readable: "HOME HEMODIALYSIS" / "IS A PROGRAM, NOT AN
APPLIANCE". Beneath it, one smaller line in clinical teal (#1a6b72) Inter medium: "Why
the Philippines has no clear pathway yet". Reserve clean, uncluttered light space behind
all typography.

Overall: premium healthcare publication aesthetic, restrained and calm, natural Filipino
skin texture, realistic equipment, bright airy daylight throughout, white to off-white
(#fafafa) base with soft grey (#f3f4f6) section separation, navy and teal accents only.
No red, no alarm imagery, no distressed or frightened expressions — analytical, not
fearful.

Include the copyright attribution rendered exactly as williamriveromd.com in small,
semi-transparent (70% opacity) navy (#0f1e2e) sans-serif text in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic
anatomy, overprocessed HDR, generic stock-photo look, excessive saturation. Avoid needles
in skin, blood, distress, or fear imagery. Avoid more than six dashed connector labels.
Avoid a hard vertical dividing line or picture-frame border between the halves — the seam
should be a soft gradient. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY
Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the williamriveromd.com
attribution.

QUALITY CHECK:
Exactly 1200 × 630. Mobile-readable, clinically plausible, visually calm,
publication-grade. Both halves share one lighting scheme and one colour grade so the
frame reads as a single image, not a collage. Machines, dialyzers and tubing mechanically
plausible. Background white / off-white / soft light grey. Title occupies clean negative
space. Attribution visible bottom-right.
```

---

## IMAGE 3 — THE THREE FAILURE MODES (biomedical mechanism schematic)

**Placement:** clinician tab, `#md-physiology`, after the intro paragraph and before the "1. The blood is outside the body" H3
**Style:** `williamriveromd-biomedical-mechanism-figure` — this is the guide's load-bearing physiology chapter, and it has the skill's signature shape exactly: patient-level panel → magnified dialyzer inset → injury → containment → benefit flow.
**Filename:** `home-hemodialysis-philippines-failure-modes.png` (+ `.webp`)

> **Accuracy note for the operator:** this is **chronic intermittent hemodialysis**,
> not CVVH/CRRT. There is **no replacement fluid and no citrate circuit**. If the
> generator adds a replacement-fluid bag or a citrate line, regenerate — those
> belong to continuous therapies only.

```
FILE NAME: home-hemodialysis-philippines-failure-modes.png
IMAGE TYPE: Biomedical mechanism schematic (review-article style)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Clinicians, dialysis nurses, policymakers
VISUAL GOAL: Show that the three physiologic failure modes of hemodialysis are
  unchanged by moving treatment home — only the containment around them is.

PROMPT:
Create a publication-grade biomedical mechanism schematic in scientific review-article
style. White (#ffffff) background, flat vector illustration with soft semi-3D shading,
thin dashed boxes separating magnified panels, generous whitespace, clean sans-serif
labels set in Inter. Muted clinical palette: light gray-blue anatomy, soft yellow
highlights, red for injury and oxidative/exposure pathways, blue for protective or
containment effects, pale pink for the pathology summary box, pale blue for the benefit
summary box.

TOPIC: Why hemodialysis is physiologically demanding wherever it is performed.
CONTEXT: Chronic intermittent hemodialysis in the home setting.

LEFT PANEL — patient-level context:
A simplified seated human figure in side view, in a domestic interior suggested with two
or three light line strokes (a chair, a window frame). Label the panel "HOME
HEMODIALYSIS — chronic intermittent". Show a simple extracorporeal blood circuit leaving
and returning to a forearm vascular access: access line out, a blood pump roller, the
dialyzer, and the return line. Annotate the blood path "300–400 mL/min · ~70–100 L per
4-hour treatment". A thin dashed connector box points from the dialyzer to the magnified
panel on the right.

CENTER PANEL — magnified dialyzer, inside a dashed border:
A vertical hollow-fibre dialyzer cartridge drawn in cutaway, with fine parallel lines
inside suggesting the fibre bundle. Port topology must be exactly as follows and must not
be altered:
  · ARTERIAL port (blood IN) at the BOTTOM end cap.
  · VENOUS port (blood OUT) at the TOP end cap.
  · DIALYSATE IN as a SIDE port set back from the TOP (venous / blood-out) end.
  · EFFLUENT OUT as a SIDE port set back from the BOTTOM (arterial / blood-in) end.
  · Draw dialysate flow as a downward arrow inside the shell, explicitly COUNTERCURRENT
    to the upward blood flow, and label it "countercurrent".
Annotate the membrane "1.5–2.1 m² surface area" and the shell path "~500 mL/min ·
~120 L dialysate per treatment". There is NO replacement-fluid line and NO citrate line
anywhere in this figure.

THREE FAILURE-MODE CALLOUTS, as small rounded cards with thin leader lines, one to each
relevant part of the circuit:
  1. On the vascular access / needle: "VENOUS NEEDLE DISLODGEMENT — blood loss at pump
     speed; venous-pressure alarm may not detect it" (red accent).
  2. On the dialyzer membrane: "DIALYSATE-BORNE EXPOSURE — no gut barrier, no first-pass
     liver; chloramine → haemolysis, aluminium → CNS and bone, endotoxin →
     inflammation" (red accent).
  3. Beside a small inset of a capillary and surrounding interstitium: "ULTRAFILTRATION >
     PLASMA REFILL — intravascular volume falls despite total-body fluid excess →
     hypotension, myocardial / gut / cerebral stunning" (red accent).

BOTTOM SUMMARY FLOW, three boxes left to right joined by bold arrows:
  LEFT (pale pink, "Three failure modes"): Circuit — exsanguination risk at pump speed ·
    Dialysate — 60× drinking-water exposure without gut or liver · Volume — removal
    outruns refill.
  CENTER (white with teal border, "What a clinic supplies as a building"): Trained person
    in the room · Treated water plant and scheduled ISO 23500 testing · Prescribed and
    supervised ultrafiltration rate.
  RIGHT (pale blue, "What must be rebuilt as a service at home"): Competency training and
    24/7 escalation · Home water treatment, service contract and testing schedule ·
    Remote prescription oversight and monitoring.

Bottom rule in clinical teal (#1a6b72) with a single line in navy: "Moving treatment home
does not remove the failure modes — it relocates the containment."

Bottom-right corner: "© williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark or navy backgrounds, decorative effects, drop shadows, cartoon
styling, overcrowding, gibberish text, tiny unreadable labels. Do NOT add a replacement-
fluid bag, a citrate/anticoagulant infusion, or any CVVH/CRRT component — this is
intermittent hemodialysis. Do NOT place both side ports at the same end of the dialyzer
and do NOT swap dialysate and effluent. Do NOT draw dialysate flowing in the same
direction as blood. Do NOT show needles entering skin, blood spillage, or a distressed
patient. Do NOT invent numeric pressure or alarm thresholds. Use ONLY Inter, Nunito Sans,
IBM Plex Sans, or Manrope.

QUALITY CHECK:
White background, review-article figure discipline, generous whitespace. Dialyzer port
topology correct: blood bottom-in / top-out, dialysate in near the top, effluent out near
the bottom, countercurrent arrow present and labelled. Exactly three failure-mode
callouts. Bottom flow reads injury → clinic containment → home service. All labels
legible at slide-viewing size. Attribution present bottom-right.
```

---

## IMAGE 4 — 120 LITRES vs 2 LITRES (side-by-side comparison)

**Placement:** patient tab, `#how-it-works`, directly after the "2. About 120 litres of water pass beside your blood" subsection
**Style:** `williamriveromd-simple-figure` Scaffold B — one idea, two panels. This is the single most memorable teaching point in the guide and the one that stops readers equating a clean tap with dialysis-grade water.
**Filename:** `home-hemodialysis-philippines-water-exposure.png` (+ `.webp`)

```
FILE NAME: home-hemodialysis-philippines-water-exposure.png
IMAGE TYPE: Scaffold B — side-by-side comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients, families, and clinicians
VISUAL GOAL: Make it immediately obvious why water that is safe to drink is not
  automatically safe to dialyse with.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical abstract style. White
(#ffffff) background. Title centred at top in bold navy (#0f1e2e) Inter: "Safe to drink
is not safe to dialyse with". Subtitle beneath in clinical teal (#1a6b72): "The same
water meets two completely different standards". Soft dashed vertical divider splitting
the canvas into two equal panels.

LEFT PANEL, header band in renal green (#1f7a4d), label "DRINKING — about 2 litres a
day": a simple flat-vector drinking glass, then a downward flow through two labelled
protective stages drawn as rounded cards — first "GUT WALL — a selective barrier that
admits some substances and refuses others", then "LIVER — first-pass clearance before
the bloodstream". End with a small card: "Standard: household drinking-water quality".

RIGHT PANEL, header band in amber (#b8860b), label "DIALYSING — about 120 litres per
treatment": a simple flat-vector hollow-fibre dialyzer shown in cutaway with fine
parallel fibre lines, blood on one side and dialysate on the other, separated by a thin
membrane drawn as a dotted line. Beside it, two crossed-out grey cards mirroring the left
panel — "NO GUT BARRIER" and "NO FIRST-PASS LIVER" — each with a thin diagonal strike.
Below, three small red-accented (#b91c1c) chips naming what this exposes the blood to:
"Chloramine → red-cell damage", "Aluminium → bone and brain", "Endotoxin fragments →
inflammation". End with a card in teal: "Standard: ISO 23500 dialysis fluid quality —
treated, tested on a schedule, signed off by a technician".

Between the two panels, centred low, a single bold navy annotation: "≈ 60× the volume,
straight past the blood, with neither barrier in between".

Bottom strip, full width, soft gray (#f3f4f6), one sentence in navy: "A clean-tasting
tap, a trusted refilling station, or a home filter cannot answer this question on their
own."

Rounded panel corners, ample negative space, mobile-readable labels at 11pt equivalent or
larger, flat illustration with no directional lighting. Bottom-right: "williamriveromd.com"
in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic
anatomy, overprocessed HDR, excessive saturation. Avoid photorealistic organs — flat
vector only. Avoid showing blood spillage, needles in skin, or anything alarming. Avoid
implying that Philippine tap water is dangerous to drink — the comparison is about
dialysis standards, not drinking-water safety. NEVER use dark, navy, charcoal, or black
backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the
williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1792 × 1024. Two clearly equal panels. The "no gut barrier / no first-pass liver"
strike-throughs on the right visually mirror the two protective stages on the left — that
mirroring is the whole point of the figure. The ≈60× annotation is legible on mobile.
White background, calm tone, attribution bottom-right.
```

---

## IMAGE 5 — SIX LAYERS CROSSING THE FRONT DOOR

**Placement:** patient tab, `#not-appliance`, immediately before the six-layer `.table-wrap`
**Style:** `williamriveromd-infographic-skill` Archetype 4 (multi-panel educational infographic) — six parallel items, each one idea, which is exactly the panel-grid anchor pattern.
**Filename:** `home-hemodialysis-philippines-six-layers.png` (+ `.webp`)

```
FILE NAME: home-hemodialysis-philippines-six-layers.png
IMAGE TYPE: Multi-panel educational infographic (Archetype 4)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Patients, families, and health journalists
VISUAL GOAL: Show that the machine is the smallest part — six separate systems have to
  cross the front door, and each has to keep working on a bad day.

PROMPT:
Patient education infographic poster, landscape 16:9, modern nephrology clinic aesthetic,
white (#ffffff) background. Title top-left in bold navy (#0f1e2e) Inter: "Six things have
to cross the front door". Subtitle in clinical teal (#1a6b72): "The machine is the
smallest of them".

LEFT THIRD: a simple flat-vector elevation of a modest Filipino house with an open front
door, drawn in light gray-blue line work with a soft teal tint. A single small dialysis
machine icon sits just inside the doorway, deliberately drawn no larger than any other
icon on the poster. Six thin navy arrows fan out from the doorway toward the panel grid
on the right.

RIGHT TWO THIRDS: a clean 3 × 2 grid of six rounded panels on a very soft gray (#f3f4f6)
field. Each panel has a teal (#1a6b72) header bar with white text, one simple flat icon,
and two short lines of body text in navy. No panel exceeds two lines.
  1. CLINICAL — "Nephrologist oversight, the prescription, vascular-access care, lab
     monitoring." Icon: stethoscope.
  2. TRAINING — "Weeks of supervised teaching, tested on real competence, then refreshed."
     Icon: two figures, one teaching.
  3. TECHNICAL — "A machine authorised for home use, its water arrangement, safe wiring,
     drainage, maintenance." Icon: wrench and droplet.
  4. REMOTE SUPPORT — "Someone to call at any hour, records that reach the team, missed
     treatments noticed." Icon: phone with a clock.
  5. EMERGENCY NETWORK — "A plan for power and water failure, a route to hospital, a
     guaranteed backup slot." Icon: shield with a cross.
  6. GOVERNANCE — "Informed choice, home assessment, infection control, incident
     reporting, who pays for what." Icon: clipboard with a checkmark.

FULL-WIDTH FOOTER BANNER in clinical teal (#1a6b72), white Inter text, one line: "Every
layer has to keep working on a bad day — a brownout, a typhoon, a fever at 2 a.m."

Clean panel-grid structure with even panel sizes and consistent colour across panels.
Generous whitespace, mobile-readable at 900 px width, flat illustration with no
directional lighting. Bottom-right, just above the teal footer: "williamriveromd.com" in
small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon appearance, visual clutter, text walls, tiny unreadable text, mismatched
panel sizes, uneven grid, missing teal header bars, inconsistent colour across panels,
floating elements without panel containers, AI gibberish text, stock-photo corporate
aesthetic. Do not draw the dialysis machine larger or more prominent than the six panels
— its small size is the message. Avoid fear-inducing imagery, storm damage, or alarm
symbols. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY Inter, Nunito
Sans, IBM Plex Sans, or Manrope. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1792 × 1024. Even 3 × 2 grid, every panel the same size with a teal header bar and
at most two lines of body text. House and doorway occupy roughly the left third. Machine
icon visibly no larger than the panel icons. Full-width teal footer present. Background
white. Attribution present.
```

---

## IMAGE 6 — WHAT THE HOUSE IS BEING ASKED TO DO

**Placement:** patient tab, `#your-home`, after the intro paragraph and before the household `.table-wrap`
**Style:** `williamriveromd-simple-figure` Scaffold E adapted to a labelled cutaway — a reference card rather than a checklist, because the guide explicitly refuses to publish a pass/fail household test.
**Filename:** `home-hemodialysis-philippines-household.png` (+ `.webp`)

```
FILE NAME: home-hemodialysis-philippines-household.png
IMAGE TYPE: Scaffold E — annotated reference card / labelled cutaway
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: Patients, families, and home-assessment teams
VISUAL GOAL: Show the six domains a provider and engineer would actually walk through in
  a home — framed as a conversation to have, never as a test to pass.

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background.
Bold navy (#0f1e2e) Inter title at top: "What the house is being asked to do". Subtitle
in clinical teal (#1a6b72): "A conversation with your provider and an engineer — not a
test you pass or fail".

CENTRE: a clean flat-vector cutaway of a modest single-storey Filipino home in light
gray-blue line work — one room shown in section with a tiled floor, a jalousie window, a
plain wall, a treatment chair and a small dialysis machine. Keep the drawing simple and
uncluttered; it is a diagram, not an illustration.

SIX LABELLED CALLOUTS with thin navy leader lines pointing to specific parts of the
cutaway, each a small rounded card with a teal header word and one short line of navy body
text:
  · SPACE → pointing at the room: "Machine, chair, supplies, medicines, hand hygiene and
    separated waste — clean and reachable, not stacked in a corridor."
  · TENURE → pointing at the wall: "Renting may need the owner's written consent for
    plumbing and electrical work."
  · WATER → pointing at a pipe entering the wall: "Availability and dialysis suitability
    are different questions. Suitability is measured, treated, then monitored on a
    schedule."
  · POWER → pointing at a wall outlet: "Correct voltage and capacity, proper grounding and
    protection — and a plan for losing power mid-treatment."
  · DRAINAGE → pointing at a floor drain line: "Used fluid needs somewhere safe to go."
  · ACCESS → pointing at the doorway: "Delivery trucks and technicians must reach this
    address, and keep reaching it in the rainy season."

BOTTOM STRIP, full width, soft gray (#f3f4f6), one line in navy: "Acceptance criteria
depend on the specific machine and configuration — only the provider, a qualified
technician and the device manufacturer can set them."

Flat illustration, no directional lighting, ample whitespace, mobile-readable labels at
11pt equivalent or larger, rounded card corners. Bottom-centre: "williamriveromd.com" in
small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR,
excessive saturation, stock-photo aesthetic. Do NOT render this as a checklist with
tickboxes, checkmarks, crosses, red/green pass-fail coding, or a score — the guide
explicitly refuses to publish a universal pass/fail household test. Do NOT depict a poor
or crowded home as inadequate, and do not use any imagery that stigmatises housing,
income, or tenure. Avoid photorealism. NEVER use dark, navy, charcoal, or black
backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never omit the
williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1536 × 1152. Six callouts, each anchored by a leader line to a real feature of the
cutaway. No tickboxes, no pass/fail colour coding, no score anywhere. Tone neutral and
respectful about housing. White background. Attribution bottom-centre.
```

---

## IMAGE 7 — WHAT THE RANDOMIZED TRIALS ACTUALLY SHOWED

**Placement:** clinician tab, `#md-benefits`, immediately after the ACTIVE Dialysis paragraph and before the purple "honest summary" alert
**Style:** `williamriveromd-simple-figure` Scaffold E (clinician reference card) — three trials with quantified results that must be read side by side; a table is the honest form.
**Filename:** `home-hemodialysis-philippines-trial-evidence.png` (+ `.webp`)

> **This is the most important figure in the plan.** It carries the guide's
> correction of the source blueprint. Every number below has been verified against
> PubMed — do not let the generator round, reword, or "improve" any of them, and
> do not let it drop the surrogate labelling.

```
FILE NAME: home-hemodialysis-philippines-trial-evidence.png
IMAGE TYPE: Scaffold E — clinician reference card / comparison table
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: Clinicians, policymakers, payers
VISUAL GOAL: Separate what intensified hemodialysis reliably moves (surrogates) from what
  it has not been shown to move (quality of life and hard outcomes) — and flag that the
  only randomized trial of home delivery was null.

PROMPT:
Clinical reference infographic card for clinicians, publication-grade nephrology design,
white (#ffffff) background. Bold navy (#0f1e2e) Inter title at top: "Intensified
hemodialysis: what the randomized trials actually showed". Subtitle in clinical teal
(#1a6b72): "Surrogates move. Quality of life and hard outcomes have not been shown to."

MAIN ELEMENT: a compact three-row comparison table with four columns. Column headers in
white on a clinical teal (#1a6b72) band: "Trial", "Design", "Primary result",
"Read it as". Alternating row fills, white and very soft gray (#f3f4f6). Reproduce the
following text exactly — do not round, rephrase, or omit any value:

Row 1 — FHN Daily Trial (NEJM 2010) | 245 patients, 6×/week vs 3×/week, IN-CENTRE,
12 months | Both coprimary composites favoured frequent HD: death or increase in LV mass
HR 0.61 (95% CI 0.46–0.82); death or decline in physical-health score HR 0.70 (95% CI
0.53–0.92). Vascular-access interventions increased, HR 1.71 (95% CI 1.08–2.73). |
Composites anchored on a SURROGATE (LV mass on MRI). Conducted in-centre — evidence about
FREQUENCY, not about the home.

Row 2 — FHN Nocturnal Trial (Kidney Int 2011) | 87 patients, 6×/week HOME nocturnal vs
3×/week conventional | NEGATIVE on both coprimary outcomes: death or change in LV mass
HR 0.68; death or change in physical-health composite HR 0.91 — neither significant.
Phosphate and BP control improved. | The only randomized trial of HOME nocturnal HD. Small
and underpowered — a failure to demonstrate benefit, not a demonstration of no benefit.

Row 3 — ACTIVE Dialysis (JASN 2017) | 200 patients, ≥24 h/week vs 12–15 h/week, in-centre
and home, 12 months | NO difference in EQ-5D quality of life: mean difference 0.04 (95% CI
−0.03 to 0.11), p = 0.29. LV mass substudy null. Lower phosphate and potassium, higher
haemoglobin, fewer BP and phosphate-binder medications. | The autonomy argument's own
primary endpoint was not met. Medication burden fell — an intermediate outcome.

BENEATH THE TABLE, three small summary chips in a single row:
  · Renal green (#1f7a4d): "RELIABLY IMPROVES — phosphate, blood pressure, medication
    burden, haemoglobin (all surrogates or intermediate outcomes)".
  · Amber (#b8860b): "NOT DEMONSTRATED — generic quality of life; benefit of home delivery
    specifically".
  · Clinical red (#b91c1c): "CONSISTENT COST — vascular-access interventions".

BOTTOM STRIP, full width, soft gray (#f3f4f6), one line in navy: "A business case built on
superior hard outcomes rests on evidence that does not exist. One built on autonomy and
eliminated travel rests on something real."

Compact, well-organised, generous line spacing, mobile-readable at 11pt equivalent or
larger, no clutter. Bottom-right: "williamriveromd.com" in small semi-transparent navy
text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR,
excessive saturation. Do NOT alter, round, or invent any numeric value, confidence
interval, sample size, journal, or year — reproduce them exactly as written. Do NOT drop
the word SURROGATE from row 1 or the word NEGATIVE from row 2. Do NOT add a fourth trial.
Do NOT render this as a bar chart or forest plot — hazard ratios from different composite
endpoints must not be plotted on a shared axis as if comparable. Do NOT use green
checkmarks or red crosses that imply an overall verdict on home dialysis. NEVER use dark,
navy, charcoal, or black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or
Manrope. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1536 × 1152. Three rows, four columns, all numbers reproduced verbatim and legible.
"SURROGATE" appears in row 1's interpretation cell; "NEGATIVE" appears in row 2's result
cell. Three summary chips present in green / amber / red. No chart, no forest plot, no
overall verdict symbol. White background. Attribution bottom-right.
```

---

## IMAGE 8 — THE FIVE READINESS GATES

**Placement:** clinician tab, `#md-gates`, after the intro paragraph and before the Gate 0 card
**Style:** `williamriveromd-simple-figure` Scaffold A (portrait algorithm) — a strictly sequential, gated pathway with no branching; portrait suits five stacked gates.
**Filename:** `home-hemodialysis-philippines-readiness-gates.png` (+ `.webp`)

```
FILE NAME: home-hemodialysis-philippines-readiness-gates.png
IMAGE TYPE: Scaffold A — clinical algorithm / gated pathway (portrait)
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Policymakers, regulators, payers, hospital and dialysis-provider leadership
VISUAL GOAL: Show that a Philippine home hemodialysis program has an order of operations,
  and that national clarification is Gate 0 — before any patient is enrolled.

PROMPT:
Clinical nephrology algorithm, KDIGO guideline flowchart aesthetic, portrait orientation.
White (#ffffff) background. Title at top in bold navy (#0f1e2e) Inter: "Five gates before
a Philippine home hemodialysis program is ready". Subtitle in clinical teal (#1a6b72): "A
staged policy argument — not an operating blueprint".

FIVE rounded rectangular gate nodes stacked vertically, connected by bold navy downward
arrows. Each gate is a wide card with a coloured left edge, a bold gate label, and two or
three short bullet lines in navy. Between each pair of gates, place a small horizontal
teal bar labelled "GATE" to make the sequence read as gated rather than merely ordered.

  GATE 0 — NATIONAL CLARIFICATION (left edge clinical red #b91c1c, the blocking gate):
    · Written DOH-HFSRB position: licence holder, home-site status, device authorisation,
      personnel scope, inspection, reporting.
    · Written PhilHealth position or a dedicated package.
    · PSN-led clinical and program standard aligned to ISO 23500 and manufacturer IFU.

  GATE 1 — SPONSOR AND NETWORK READINESS (left edge amber #b8860b):
    · An accountable licensed parent hemodialysis clinic or hospital, named in writing.
    · Named clinical, nursing, technical, supply, data, legal and emergency leads.
    · 24/7 support and contracted backup clinic capacity.

  GATE 2 — CONTROLLED PILOT (left edge clinical teal #1a6b72):
    · Small, ethically governed cohort with transparent inclusion and exclusion logic.
    · Independent home and social assessment, separate from the enrolling provider.
    · Predefined stop rules, incident review, guaranteed backup treatment.

  GATE 3 — MEASURE BEFORE SCALING (left edge clinical teal #1a6b72):
    · Publish the enrolment denominator AND the reasons for non-entry.
    · Adverse events, hospitalisation, technique survival, water and technical failures.
    · Household cost, care-partner strain, and equity by income, region and disability.

  GATE 4 — SCALE THROUGH HUBS (left edge renal green #1f7a4d):
    · Regional hubs supporting spoke facilities: shared training, pooled procurement,
      technical coverage, quality dashboards.
    · Scale only after safety, affordability, equity and continuity thresholds are met
      and published.

Beside Gate 0, a small red-outlined annotation card: "Nothing below this line should begin
until Gate 0 is answered in writing."

BOTTOM STRIP, full width, soft gray (#f3f4f6), one line in navy: "No patient should be
charged experimental or unclear costs without fully informed agreement and regulatory
approval."

Strictly linear top-to-bottom flow with no branching and no decision diamonds. Generous
whitespace, mobile-readable labels, no spaghetti connectors. Bottom-centre:
"williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, spaghetti
connectors, excessive saturation. Do NOT add branching paths, decision diamonds, loops, or
a sixth gate. Do NOT imply that any gate has already been cleared in the Philippines, and
do not add checkmarks, progress bars, or completion indicators of any kind. Do NOT add
dates, timelines, or duration estimates — none are stated in the source. NEVER use dark,
navy, charcoal, or black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or
Manrope. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1024 × 1536 portrait. Five gates, in order, strictly linear. Gate 0 is visually the
blocking gate (red left edge plus the annotation card). No checkmarks, progress indicators,
dates, or completion states anywhere. No branching. White background. Attribution
bottom-centre.
```

---

## IMPLEMENTATION NOTES

### Already wired in the guide
- **IMG 1** and **IMG 2** are referenced by the guide's HTML with correct
  dimensions and alt text; they 404 until generated. No markup changes needed.

### Requires markup after generation
**IMG 3–8 are not yet referenced in the guide.** Each needs a `<figure>` inserted
at its placement anchor, and — per the guide-wide policy in `CLAUDE.md` — each
figcaption must carry a `<p class="fig-desc">` plain-language description, plus a
`<dl class="fig-abbrevs">` block wherever the image contains an acronym. IMG 3
and IMG 7 both contain acronyms (HD, LV, HR, CI, EQ-5D, ISO, IFU) and cannot ship
without the abbreviation list, or the lightbox caption panel will be incomplete.

Insertion anchors, in document order:

| Image | Anchor |
|---|---|
| IMG 4 | `#how-it-works`, after the "≈60× / no liver in between" paragraph |
| IMG 5 | `#not-appliance`, before the six-layer `.table-wrap` |
| IMG 6 | `#your-home`, before the household `.table-wrap` |
| IMG 3 | `#md-physiology`, after the intro paragraph, before the first H3 |
| IMG 7 | `#md-benefits`, after the ACTIVE paragraph, before the purple alert |
| IMG 8 | `#md-gates`, after the intro paragraph, before the Gate 0 card |

### After the images are received
1. Save each as `.png` **and** a `.webp` twin in `images/`.
2. Wire IMG 3–8 as `<figure><picture>…</picture><figcaption>…</figcaption></figure>`
   blocks at the anchors above.
3. Run, in order:
   ```
   python3 patch_hero_fetchpriority.py --guide home-hemodialysis-philippines.html
   python3 patch_hero_fullwidth.py --guide home-hemodialysis-philippines.html
   python3 patch_hero_maxwidth.py --guide home-hemodialysis-philippines.html
   python3 patch_img_dimensions.py
   python3 patch_image_lightbox.py --guide home-hemodialysis-philippines.html
   python3 patch_reading_time.py --guide home-hemodialysis-philippines.html
   ```
4. Re-check dark mode: IMG 4, 6, 7 and 8 are white-background figures and will sit
   on a dark card in dark mode. They are self-contained images with their own white
   field, so no contrast remap is needed — but confirm the figcaption text below
   them still resolves through the `--text-mid` token rather than a literal colour.

### Flagged for the operator
- **IMG 3** is the highest regeneration risk. Dialyzer port topology is the single
  most common failure across this library's past figures; check blood bottom-in /
  top-out, dialysate side-port near the top, effluent side-port near the bottom, and
  a labelled countercurrent arrow before accepting.
- **IMG 7** must be proofread character by character against the prompt. Every
  hazard ratio, confidence interval and sample size is PubMed-verified, and a
  transcription error here would misrepresent the trial evidence the guide exists
  to correct.
- **IMG 8** must not acquire checkmarks or progress indicators. Gate 0 is
  unanswered in the Philippines; any completion state would be a factual error.
