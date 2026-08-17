# IMAGE PLAN — Roadmap to Adding a Peritoneal Dialysis Program

**Guide:** `guides/adding-peritoneal-dialysis-program.html`
**Live URL (after merge):** https://renalcarematters.com/guides/adding-peritoneal-dialysis-program.html
**Total images:** 7 (1 hero vignette · 1 OG card · 5 inline figures)
**Visual anchor:** `ckd-understanding-overview.webp`
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Generated:** 17 August 2026

---

## Architecture of the plan

The guide is a multi-chapter professional reference: 19 nav sections, ~12,500 words, an
audience of administrators and clinicians. The planner rubric caps most guides at six
images; this one is explicitly a multi-chapter reference and carries seven, allocated by
**where the reader's mental model is most likely to fail**, not evenly across sections.

| Reader failure the image prevents | Image | Skill used |
|---|---|---|
| "PD is just another dialysis modality — our HD setup covers it" | 01 · Membrane mechanism | `williamriveromd-biomedical-mechanism-figure` |
| "We're a hospital, so acute care and microbiology are handled" | 02 · FSDC vs HBDC | `williamriveromd-infographic-skill` (ref card) |
| "The gates are a formality once the date is announced" | 03 · Phase-gate roadmap | `williamriveromd-algorithm-generator-skill` (Mode C) |
| "Supply is procurement's problem" | 04 · Supply chain | `williamriveromd-infographic-skill` (workflow) |
| "Microbiology is on site, so that domain is closed" | 05 · Peritonitis tracer | `williamriveromd-algorithm-generator-skill` (Mode C) |
| Hero / share identity | HERO + OG | `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` |

### Deliberately NOT generated as raster images

- **Capability maturity matrix** (10 domains × 5 levels) — already an accessible HTML table in
  `#capability`. A raster duplicate would be unreadable on mobile, unsearchable, and would go
  stale the moment the table is edited.
- **Quality dashboard / KPI dictionary** — same reason; it lives as three HTML tables in
  `#dashboard`, where the denominators stay copy-pasteable.
- **SOP index (23 rows)** and **sequenced approval register (9 stages)** — tables, not pictures.

Per the planner skill's own guidance: when a reference card is really a table, ship the table.

### House rules applied to every prompt below

- **Light background only.** White `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, or light
  teal tint `#eef6f7`. Navy `#0f1e2e` is text and accent only — never a background fill.
- **Approved fonts only:** Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never a serif.
  The chosen face is named explicitly inside each prompt.
- **Attribution `renalcarematters.com`** in small semi-transparent navy at the bottom-right
  (bottom-centre for portrait) on **every image except the hero vignette**, which the
  hero-vignette skill explicitly requires to be wordless and unmarked.
- **Palette:** navy `#0f1e2e`, clinical teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b`,
  clinical red `#b91c1c`.
- **Scope guard specific to this guide:** it is a professional-use programme-development
  resource that deliberately excludes clinical procedure. **No image may depict or imply an
  exchange technique, a connect/disconnect sequence, catheter flushing, dressing change,
  specimen collection technique, drug names, doses, dwell volumes, or glucose strengths.**
  Figure 05 maps accountability and response time, not treatment.

### Batching (5 requests / 60 s limit)

**Batch 1** — HERO → OG → 01 → 02 → 03
*wait 60 seconds*
**Batch 2** — 04 → 05

---

# HERO

**Placement:** `figure.hero-figure > .hero-vignette`, beside the `<h1>` — top of page
**Style:** Circular vignette hero v3, Scaffold A (Clinical People) — the guide's subject is an
organisational decision made by a named, accountable team, so people carry the meaning better
than anatomy or a still life; anatomy is already spoken for by Figure 01.
**File:** `adding-peritoneal-dialysis-program-vignette-hero.png` (+ `.webp` twin)

```
FILE NAME: adding-peritoneal-dialysis-program-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A (Clinical People Scene)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J — Environmental Storytelling (one cohesive scene, no floating panels)
CAMERA: Over-the-shoulder, from behind and slightly left of the seated administrator
AUDIENCE: Administrators and clinicians
VISUAL GOAL: A small accountable team deciding whether their centre is ready — planning, not treating.

HUMAN VARIATION (vs. previous guides in this library):
1. Age — mid-30s lead figure, not an older patient
2. Biological sex — woman in the dominant foreground role
3. Gender presentation — professional-androgynous second figure
4. Face shape — broad, square jaw on the standing woman
5. Nose — short, wide bridge
6. Eye shape — deep-set, heavy upper lid
7. Eyebrow shape — straight, low-set
8. Hairstyle — tight low bun with a centre part
9. Hair colour — near-black with visible grey at the temple on the seated man
10. Body habitus — tall and slight, not stocky
11. Skin tone — deeper brown within Filipino diversity
12. Clothing — charcoal scrub top and a lanyard, NOT a teal polo or beige blouse
13. Accessories — wire-rim glasses pushed up, tablet under arm
14. Posture — standing, weight on one hip, turned three-quarters away from camera
15. Hand position — one hand resting flat on a printed floor plan
16. Expression — concentrated, mid-thought, not smiling at camera
17. Environment — a bright administrative meeting room, not a clinic bay, kitchen, or dining table
18. Camera distance — over-the-shoulder mid-range, not a seated three-quarter portrait

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed
inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER
around the full circle — the circle must never touch the canvas edges and must never be cropped.
Composition archetype: J, Environmental Storytelling — one single cohesive scene, no floating
panels or collage elements. Camera: over-the-shoulder, positioned behind and slightly left of a
seated figure, looking past their shoulder toward a standing colleague and a planning wall.

Subject: three Filipino health-service professionals in a bright administrative meeting room of a
modern Philippine dialysis centre, mid-discussion about whether to open a new home-therapy service.
The dominant figure is a tall, slight Filipino woman in her mid-thirties with deeper brown skin, a
broad square jaw, short wide-bridged nose, deep-set heavy-lidded eyes and straight low-set eyebrows,
her near-black hair in a tight low bun with a centre part, wearing a charcoal scrub top with a plain
lanyard and wire-rim glasses pushed up on her head, standing with her weight on one hip and turned
three-quarters away from camera, one hand resting flat on a large printed floor plan spread on the
table, expression concentrated and mid-thought — not smiling at the camera. Seated in the near
foreground with their back to us is an older man with visible grey at the temples, a tablet resting
on his knee. A third colleague is softly out of focus at the far side of the table. On the wall
behind them: a large paper planning sheet showing a simple vertical column of seven blank numbered
cards with small diamond shapes between them, a plain hand-drawn room layout, and a single line
running to a small house symbol — all rendered as abstract marks and shapes with NO legible words.
On the table beside the floor plan, one clear peritoneal dialysis solution bag lies flat as a quiet,
medically accurate object — not a clinical close-up, no tubing connected to anyone, no procedure
being performed.

Visual hierarchy: the standing woman and the planning wall occupy 60–70% of the circle; the seated
foreground shoulder, the table objects and the blurred third colleague make up 20–30%; reserve a
20–25% TITLE SAFE ZONE in the upper-left of the circle as a clean, softly lit pale wall with gentle
gradient and no faces, anatomy, icons, objects, or callouts inside it, so the HTML headline can sit
beside the disc without covering important artwork.

Soft natural daylight from a large window at the left, gentle shallow depth of field, calm and
competent documentary-realistic colour grade harmonising with clinical teal #1a6b72 and navy
#0f1e2e against light walls and pale wood. Edge falloff toward a slightly deeper neutral at the
rim. Full-bleed within the inscribed circle. Mood: serious professional planning, never crisis,
never celebration.

Absolutely NO text of any kind: no title, subtitle, caption, label, signage, legible writing on the
planning wall, logo, or renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid: busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny
unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle,
cropped objects, cropped anatomy, edge clipping, objects touching the circular border, important
content inside the title safe zone, baked-in text, titles, captions, logos or watermarks,
rectangular borders, frames or banners, dark / charcoal / black backgrounds, cartoon style, neon,
HDR, over-saturation, distorted hands or faces, implausible anatomy. Also avoid: any procedure in
progress, needles, catheter insertion, exposed abdomen, blood, patient distress, hospital gowns,
smiling stock-photo handshake, teal polo shirts, beige blouses, dining tables, kitchens.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped.
ONE dominant hero subject at 60–70% of the circle, 2–4 supporting elements, 20–25% empty
title-safe zone in the upper-left. Filipino professional context with ≥12 traits visibly different
from the last guide in the library. Over-the-shoulder framing not repeated from the previous guide.
Crops cleanly inside the circle with nothing lost at the edges. Zero legible text anywhere.
```

---

# OG — SOCIAL SHARE CARD

**Placement:** `og:image` / `twitter:image` — not rendered in-page
**Style:** Editorial share card. **1200 × 630 is fixed and non-negotiable** per house rule; the
guide's meta tags already declare `og:image:width="1200"` `og:image:height="630"`.
**File:** `adding-peritoneal-dialysis-program-og.png`

```
FILE NAME: adding-peritoneal-dialysis-program-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: Administrators, medical directors, dialysis-centre owners
VISUAL GOAL: Communicate "seven gated phases, professional guide" in a 2-second feed glance.

PROMPT:
Clean editorial social share card on a pure white #ffffff background, 1200 × 630, in a premium
medical-publication style. Typography set in Inter throughout — never a serif font.

Left two-thirds: a large bold navy #0f1e2e headline on three lines reading "Roadmap to Adding a
Peritoneal Dialysis Program", with a single smaller clinical-teal #1a6b72 subtitle line beneath
reading "Seven gated phases · Freestanding or hospital-based dialysis centre". Below the subtitle,
a compact horizontal row of seven small evenly spaced rounded rectangles numbered 1 to 7 in navy
outline, with a tiny teal diamond between each pair, and a very thin progression rule beneath them
shading softly from renal green #1f7a4d at the left through amber #b8860b in the middle to navy
#0f1e2e at the right. No paragraph text anywhere.

Right third: a restrained flat vector illustration on a very light teal tint #eef6f7 rounded
panel — a simplified peritoneal dialysis solution bag, a small clean house outline, and a single
dotted line connecting the two, drawn in muted teal-blue tones with thin confident strokes. No
anatomy, no people, no procedure.

Generous whitespace, strong hierarchy, crisp alignment, mobile-thumbnail-readable at small size.
Flat vector, no directional lighting, no drop shadows, no 3D bevels, no gradients other than the
single thin progression rule.

Include the attribution "renalcarematters.com" as small semi-transparent navy #0f1e2e text in the
bottom-right corner, roughly 11px equivalent at 70% opacity, clear of all other elements.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid
unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive
saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use
ONLY Inter — no other fonts, no serif fonts, no decorative or handwritten typefaces. Never omit
the renalcarematters.com attribution. No photographs, no patients, no hospital logos, no brand
names, no needles or catheters entering a body.

QUALITY CHECK:
Exactly 1200 × 630. White background. Headline legible as a feed thumbnail. Seven-step row reads
as a sequence, not decoration. Attribution present bottom-right. No text errors or invented words.
```

---

# 01 — MEMBRANE MECHANISM

**Placement:** `#physiology` — "Why PD Differs · The Physiology That Earns Every Requirement",
immediately after the *"The derivation, in one line"* callout and before *"Why suspected
peritonitis is the programme's time-critical pathway"*.
**Style:** `williamriveromd-biomedical-mechanism-figure` — review-article schematic. This is the
one figure that has to carry causal reasoning rather than structure, so it uses the mechanism
skill's organ → dashed inset → injury/intervention/benefit layout rather than a panel grid.
**File:** `adding-peritoneal-dialysis-program-01-membrane-mechanism.png`

```
FILE NAME: adding-peritoneal-dialysis-program-01-membrane-mechanism.png
IMAGE TYPE: Biomedical mechanism figure (review-article schematic)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Clinicians, PD nurses, medical directors
VISUAL GOAL: Show why an irreplaceable membrane plus a permanent transcutaneous catheter makes
infection an organ-loss event — the mechanism from which the programme requirements derive.

PROMPT:
Create a publication-grade biomedical mechanism schematic in a scientific review-article style on
a pure white background, 1792 × 1024. Flat vector illustration with soft semi-3D shading, muted
clinical palette, thin dashed connector lines, generous whitespace, no photorealism, no shadows,
no dark background, no cartoon styling. All typography in IBM Plex Sans — never a serif font.

LEFT PANEL — organ-level context:
A simplified anterior abdominal cross-section in light gray-blue, showing the peritoneal cavity
filled with pale teal dialysate, loops of bowel suggested simply, and a peritoneal dialysis
catheter entering through the abdominal wall and curling into the pelvis. Label the panel
"Peritoneal cavity on CAPD". Mark the catheter's subcutaneous tunnel and two small Dacron cuffs.
Two thin dashed connector boxes lead from this panel to the two magnified insets on the right.

UPPER RIGHT INSET (dashed border) — "Peritoneal membrane, magnified":
Show the mesothelial cell layer over the interstitium and a capillary in cross-section. Illustrate
two transport routes with small arrows: solute diffusion across small pores between endothelial
cells, and free water crossing through aquaporin water channels in the endothelial membrane.
Show a glucose gradient in the dialysate compartment driving osmotic ultrafiltration. Concise
callouts only:
- Diffusion down solute gradient
- Osmotic UF via AQP-1 free-water pathway
- Membrane is patient-specific and drifts over time

LOWER RIGHT INSET (dashed border) — "Exit site and tunnel, magnified":
Show the catheter crossing skin and subcutaneous tissue, with fibrous tissue ingrowth into the
Dacron cuff highlighted in pale yellow as the mechanical anchor and biological barrier. Two small
red arrows show the two routes organisms take: touch contamination entering at the external
connection and travelling down the catheter lumen, and tunnel tracking travelling inward along an
immature or infected tract. Concise callouts only:
- Cuff ingrowth = anchor + barrier
- Ingrowth takes time — break-in interval is device- and protocol-specific, use your unit's
  approved SOP and the manufacturer's instructions

BOTTOM SUMMARY FLOW — three boxes, left to right, joined by thick arrows:
Left box, pale pink, headed "Injury drivers":
- Touch contamination at the connection
- Tunnel tracking from exit site
- Neutrophil influx, fibrin deposition
- Repeated or refractory episodes
- **Membrane injury accumulates and is not reversible**

Centre box, white with teal border, headed "Programme controls":
- Competency-based training and retraining
- Scheduled exit-site assessment
- 24/7 route to a clinician who can act
- Validated specimen and culture pathway
- Lot-traceable, on-time supply

Right box, pale blue, headed "Expected benefit":
- Preserved membrane function
- Preserved residual kidney function
- Sustained technique survival

Add a small italic note beneath the bottom flow reading "Mechanism figure. Clinical management,
antimicrobial selection and dwell prescriptions are governed by approved local SOPs and current
ISPD guidance." Include the attribution "renalcarematters.com" as small semi-transparent navy
#0f1e2e text in the bottom-right corner at roughly 70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative elements, overcrowding, cartoon styling, drop
shadows, glossy 3D. Avoid tiny unreadable labels and AI gibberish text. Do not invent numeric
thresholds — no dwell volumes, no glucose strengths, no antibiotic names or doses, no day counts
for the break-in interval. Do not depict a person, an exchange being performed, a hand connecting
tubing, an open wound, or blood. Use ONLY IBM Plex Sans. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
Anatomically plausible peritoneum, capillary, catheter tunnel and cuff. Two dashed insets clearly
connected to the organ panel. Bottom three-box flow reads left to right without ambiguity. All
labels legible at slide-viewing size. White background, muted clinical colours. Attribution
present bottom-right.
```

---

# 02 — FSDC vs HBDC CAPABILITY COMPARISON

**Placement:** `#starting-point` — "Choose Your Starting Point", after the baseline-question table.
**Style:** `williamriveromd-infographic-skill` Archetype 5 (clinician reference card), 4:3 matrix.
**File:** `adding-peritoneal-dialysis-program-02-fsdc-vs-hbdc.png`

```
FILE NAME: adding-peritoneal-dialysis-program-02-fsdc-vs-hbdc.png
IMAGE TYPE: Clinician reference card — two-column capability comparison matrix
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: Administrators, medical directors, compliance and quality leads
VISUAL GOAL: Show that both settings face the same ten domains but fail in opposite ways —
unsigned external agreements versus unvalidated internal assumptions.

PROMPT:
Clinical reference infographic card for clinicians and administrators, publication-grade nephrology
design, on an off-white #fafafa background, 1536 × 1152. Typography set in Manrope throughout —
never a serif font.

Header: a bold navy #0f1e2e title reading "Same ten domains. Two failure patterns." with a thin
clinical-teal #1a6b72 rule beneath it and a small subtitle line "Freestanding vs hospital-based
dialysis centre adding peritoneal dialysis".

Body: a clean three-column matrix on soft gray #f3f4f6 alternating row bands.
- The narrow CENTRE spine column lists ten domain labels stacked vertically in navy, each with a
  small flat monoline icon to its left: Governance, Regulation, Acute care, Catheter access,
  Microbiology, Pharmacy, Backup HD, Training, Logistics, Quality.
- The LEFT column sits under a clinical-teal #1a6b72 header bar reading "FSDC · Freestanding".
  Each cell holds one short phrase, three to six words maximum, emphasising external dependency:
  external network accountability; clarify FSDC scope; executed receiving agreements; multiple
  external routes and transport; courier and after-hours contract; external dispensing access;
  reserved pathway and payer rules; protect trainer from HD gaps; vendor and carrier SLAs;
  cross-organisation data exchange.
- The RIGHT column sits under a navy #0f1e2e header bar reading "HBDC · Hospital-based". Each cell
  holds one short phrase emphasising internal validation: internal service-line accountability;
  clarify hospital and service scope; validated internal workflow; theatre scheduling and protected
  access; laboratory prioritisation and downtime; formulary and after-hours dispensing; protected
  slots and coordination; protect PD team from redeployment; hospital receiving plus last-mile;
  avoid burying PD in aggregates.

Footer band in clinical teal #1a6b72 with white text, one line only: "Signed agreement = designed.
Tested tracer case = validated."

Consistent row heights, consistent column widths, strict alignment, generous margins, rounded card
corners, no drop shadows, no 3D, no photographs, flat vector only. Mobile-readable label sizes —
no microtext. Include the attribution "renalcarematters.com" as small semi-transparent navy text in
the bottom-right corner at roughly 70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid
overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark,
navy, charcoal, or black backgrounds — light backgrounds only; navy is for text and header bars
only. Use ONLY Manrope. No hospital branding, no real institution names, no logos, no photographs,
no uneven grid, no mismatched panel sizes. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly ten aligned rows across all three columns. Left and right cells clearly distinguishable by
header colour. Every phrase six words or fewer. Footer line present. Attribution bottom-right.
No invented domain names beyond the ten listed.
```

---

# 03 — PHASE-GATE ROADMAP

**Placement:** `#roadmap` — "Roadmap at a Glance", after the seven-phase table and the
"Durations are not a schedule" caution.
**Style:** `williamriveromd-algorithm-generator-skill` **Style Mode C — house-style clinical
algorithm**. Mode A is for resuscitation and Mode B for drug-treatment ladders; this is a branded
guide algorithm, so Mode C is correct.
**File:** `adding-peritoneal-dialysis-program-03-phase-gate-roadmap.png`

```
FILE NAME: adding-peritoneal-dialysis-program-03-phase-gate-roadmap.png
IMAGE TYPE: Clinical algorithm flowchart — renalcarematters.com house style (Mode C)
ASPECT RATIO: 2:3 (portrait)
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Administrators, medical directors, quality and compliance leads
VISUAL GOAL: Make visible that each phase is closed by a gate that can send the programme
backwards, and that one critical finding overrides any aggregate score.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house
style, on a very light off-white #fafafa background, portrait 1024 × 1536. Restrained navy and
teal typography set in Inter — never a serif font. Thin teal connector arrows, generous margins,
centred and symmetrical, suitable for a clinician- and administrator-facing nephrology guide.

Title at the top in bold navy #0f1e2e: "Phase-gate roadmap — adding a peritoneal dialysis
programme". Small gray subtitle beneath: "A critical finding blocks launch regardless of the
overall readiness score."

Main vertical trunk, top to bottom, eight navy #0f1e2e rounded rectangles with white text, evenly
spaced and identical width:
0 Mandate and baseline → 1 Regulation and payment → 2 Operating model → 3 Detailed design →
4 Build and contract → 5 Validate → 6 Controlled launch → 7 Stabilise and scale

Between each consecutive pair, a clinical-teal #1a6b72 diamond decision node containing the short
label "GATE" with three exit routes marked in small text: "go" continuing downward on a teal
arrow, "conditional go" continuing downward on a teal arrow with a small amber #b8860b dot, and
"no go" leaving to the left on a clinical-red #b91c1c arrow that curves back up into the preceding
phase box. Keep the return arrows on the left side only, cleanly separated, never crossing the
central trunk.

Two amber #b8860b caution callouts branch to the right side:
- From Gate 0, a rounded amber box reading "Stop conditions: no accountable medical director or
  PD nurse lead · enrolment framed as a target · no plausible route to access, 24/7 support,
  microbiology, admission or backup HD"
- From Gate 5, a rounded amber box reading "Independent readiness review — all critical findings
  must be closed before first enrolment"

At the bottom, a small soft-gray legend panel defining three finding severities using BOTH an icon
shape and a colour so the meaning never depends on colour alone: a red filled octagon labelled
"Critical — blocks launch", an amber filled triangle labelled "Major — fix or formally risk-accept",
and a green filled circle labelled "Improvement — assign and monitor". Beside the legend, one short
gray note: "Durations depend on authority response, contracts, construction, staffing and
procurement — do not sum them into a fixed opening date."

Consistent rounded corners, identical box widths, equal vertical spacing, arrows of consistent
length, no crossing or tangled connectors, no icons inside nodes, no photographs, no 3D, no dark
background, no clutter. Include a small professional footer reading "renalcarematters.com"
positioned at the bottom-centre in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, 3D effects, drop shadows, neon or rainbow gradients, crossing or tangled
connectors, tiny unreadable text, decorative medical imagery, photographs, dark backgrounds. Use
ONLY Inter. Do not add clinical content, drug names, patient criteria, or eligibility rules — this
is a programme-management pathway, not a treatment algorithm. Do not invent phase durations or
dates inside the boxes. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly eight phase boxes numbered 0 through 7 in the stated order, seven gate diamonds between
them, red no-go returns on the left only, two amber callouts on the right, a three-severity legend
distinguished by shape as well as colour. All text legible at full size and at thumbnail. Footer
attribution present.
```

---

# 04 — SUPPLY CHAIN AS A CLINICAL SAFETY SYSTEM

**Placement:** `#logistics` — "Logistics Is a Clinical Safety System", after the text flow diagram.
**Style:** `williamriveromd-infographic-skill` Archetype 8 adapted to a linear closed loop, 16:9.
**File:** `adding-peritoneal-dialysis-program-04-supply-chain.png`

```
FILE NAME: adding-peritoneal-dialysis-program-04-supply-chain.png
IMAGE TYPE: Process-flow infographic — closed-loop logistics workflow
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: Administrators, procurement and logistics leads, pharmacists, PD nurses
VISUAL GOAL: Reframe supply as a clinical safety system by showing where the four controls sit and
exactly which harm each one prevents.

PROMPT:
Clean process-flow infographic on a white #ffffff background, 1792 × 1024, publication-grade
nephrology educational design. Flat vector, no lighting, no drop shadows, no 3D. Typography set in
Nunito Sans throughout — never a serif font.

Header: bold navy #0f1e2e title "The PD supply chain is a clinical safety system", with a thin
clinical-teal #1a6b72 rule and a small gray subtitle "From authorised prescription to the patient's
home — and back".

CENTRE: one wide horizontal chain of nine rounded navy-outlined nodes running left to right, each
with a small flat monoline icon above its two- or three-word label, joined by thin teal arrows of
equal length:
Authorised plan → Forecast and order → Supplier allocation → Receiving and inspection → Controlled
storage → Patient-specific pick → Protected transport → Home delivery → Home reconciliation

RETURN LOOP: from the ninth node, a smooth curved teal arc sweeps back beneath the chain from right
to left into a single soft-gray rounded group labelled "Returns · Quarantine · Recall · Waste",
which then feeds a short arrow back up into Controlled storage. The loop must read as one clean arc,
never as tangled or crossing lines.

CONTROL POINTS: above the chain, four clinical-teal #1a6b72 markers drop down onto Receiving,
Controlled storage, Patient-specific pick, and Home delivery. Each marker carries a two- or
three-word label in teal: "Lot and expiry capture", "Environment monitoring", "Dual verification",
"Identity-safe handover".

RISK BAND: below the chain, a slim amber #b8860b band divided into five aligned segments, each
sitting under the control it corresponds to, reading: "Wrong lot", "Temperature excursion",
"Picking error", "Address disclosure", "Untraceable recall".

RIGHT EDGE: a small simplified house outline in muted teal-blue with three stacked solution boxes
inside it and a tiny clipboard icon, representing home inventory. No people, no delivery vehicles
with visible branding, no anatomy.

FOOTER STRIP: one clinical-teal band with white text reading "Substitution of solution,
concentration, connector, set, drug or device is a clinical decision — pharmacy and medical
approval, never logistics."

Generous whitespace, strict alignment between control markers, chain nodes and risk segments,
mobile-readable label sizes, no microtext, no paragraphs. Include the attribution
"renalcarematters.com" as small semi-transparent navy text in the bottom-right corner at roughly
70% opacity.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid
overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation, avoid tangled or
crossing arrows. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY Nunito Sans. No courier or delivery-company branding, no real manufacturer names, no
product packaging copy, no photographs, no drug names, no dwell volumes or glucose strengths.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly nine chain nodes in the stated order, one clean return arc, four control markers vertically
aligned to their nodes, five risk segments aligned beneath. Footer strip present and legible.
Attribution bottom-right. No invented steps or brand marks.
```

---

# 05 — AFTER-HOURS PERITONITIS TRACER

**Placement:** `#phase5` — "End-to-End Validation and Launch Authorisation", after the
twelve-simulation table and before "Scoring findings". This is simulation #2, the guide's most
time-critical pathway.
**Style:** `williamriveromd-algorithm-generator-skill` **Style Mode C**. Deliberately NOT Mode A
or B: this maps organisational accountability and response time, not resuscitation and not
treatment selection.
**File:** `adding-peritoneal-dialysis-program-05-peritonitis-tracer.png`

> **Scope guard:** the guide excludes clinical procedure by design. This figure names *who acts and
> by when*, never what is given. No antibiotic names, no doses, no routes, no specimen technique.

```
FILE NAME: adding-peritoneal-dialysis-program-05-peritonitis-tracer.png
IMAGE TYPE: Operational tracer pathway — renalcarematters.com house style (Mode C)
ASPECT RATIO: 2:3 (portrait)
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: Medical directors, PD nurses, microbiology and quality leads, compliance reviewers
VISUAL GOAL: Prove or disprove that a suspected-peritonitis call at 2 a.m. on a Sunday reaches a
clinician who can act and a laboratory that will process the specimen.

PROMPT:
Create a clean publication-ready operational pathway flowchart in the renalcarematters.com house
style, on a very light off-white #fafafa background, portrait 1024 × 1536. Restrained navy and teal
typography set in Inter — never a serif font. Thin teal connector arrows, centred, symmetrical,
generous margins, publication-grade vector look.

Title in bold navy #0f1e2e: "After-hours suspected peritonitis — programme tracer". Small gray
subtitle: "Simulation 2 of 12. Tests accountability and response time, not treatment."

Vertical pathway from top to bottom:
1. Soft-gray rounded capsule, top: "Patient or care partner notices cloudy effluent, abdominal pain
   or fever — after hours"
2. Navy rounded box: "Single published contact number reached"
3. Clinical-teal #1a6b72 decision diamond: "Clinical or technical call?" — a short branch to the
   right in soft gray reads "Technical → device and supply route" and ends in a small gray terminal
   box; the main trunk continues downward labelled "Clinical"
4. Navy rounded box: "Contact with a clinician empowered to change management"
5. Navy rounded box: "Effluent specimen obtained under approved SOP"
6. Navy rounded box: "Transport and laboratory accessioning"
7. Navy rounded box: "Gram stain and culture processed"
8. Navy rounded box: "Empiric therapy authorised under local policy" — with a small gray side note
   reading "Regimen governed by local microbiology, pharmacy policy and current ISPD guidance —
   not by this diagram"
9. Clinical-teal decision diamond: "Critical result communicated to a clinician who can act?" —
   a red #b91c1c "no" branch curves left into an amber caution box, and a teal "yes" continues down
10. Green #1f7a4d rounded box: "Organism-directed review and follow-up"
11. Green rounded box: "Apparent-cause analysis · retraining decision · surveillance coding"

Two amber #b8860b caution boxes on the left margin, each connected by a short dashed line to the
step it threatens:
- Beside step 2: "Most common breakpoint — no answer after hours"
- Beside step 7: "Second breakpoint — no laboratory processing at weekends"

Right margin: a narrow soft-gray legend column headed "Record for every step" listing three short
lines with small icons: "Response target", "Named owner", "Documented fallback".

Bottom band in soft gray with navy text, one line: "If any step cannot be demonstrated on a Sunday
night, this is a critical finding — the programme does not launch."

Consistent rounded corners, identical box widths on the trunk, equal vertical spacing, arrows of
consistent length, no crossing or tangled connectors, no photographs, no 3D, no dark background.
Include a small professional footer reading "renalcarematters.com" at the bottom-centre in subtle
gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, 3D effects, drop shadows, neon gradients, crossing connectors, tiny unreadable
text, decorative medical imagery, photographs, dark backgrounds. Use ONLY Inter. Absolutely no
antibiotic names, no drug classes, no doses, no routes, no dwell volumes, no glucose strengths, no
cell-count thresholds, no turnaround-time numbers in hours — this is an accountability map, not a
treatment or diagnostic algorithm. Do not depict specimen collection technique, a catheter being
handled, an exchange in progress, or any body part. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Eleven trunk steps in the stated order with two decision diamonds. Technical branch clearly
terminates to the side. Two amber breakpoint callouts on the left, legend column on the right,
bottom band present. Zero drug names or numeric clinical thresholds anywhere in the image. Footer
attribution present.
```

---

## Post-generation checklist

1. Save each as `images/<file-name>.png` **and** a WebP twin at the same base name (q88).
2. Confirm delivered pixel dimensions match the `width`/`height` attributes already wired into the
   guide — hero `2048×2048`, 01 `1792×1024`, 02 `1536×1152`, 03 `1024×1536`, 04 `1792×1024`,
   05 `1024×1536`. The OG card must be exactly `1200×630`; the guide's meta tags already declare it.
3. Read every generated image for text errors. Image models mangle labels — a garbled domain name
   or a hallucinated antibiotic in Figure 05 is a publication defect, not a cosmetic one.
4. Re-run the hero patchers after the files land:
   ```bash
   python3 patch_hero_fetchpriority.py --guide adding-peritoneal-dialysis-program.html
   python3 patch_hero_maxwidth.py --guide adding-peritoneal-dialysis-program.html
   python3 patch_img_dimensions.py --guide adding-peritoneal-dialysis-program.html
   ```
5. Verify each figure's `<figcaption class="fig-desc">` still describes what the image actually
   shows — the lightbox reads that line, and the descriptions in the guide were written against
   this plan, not against the rendered result.

## Local-generation fallback

`image-prompts/adding-peritoneal-dialysis-program-images.json` runs the same seven prompts through
`generate_image.py` (gpt-image-1). That API accepts only `1024x1024`, `1536x1024`, and `1024x1536`,
so the JSON carries the nearest legal size and the assets need a crop or upscale afterwards. **The
Markdown prompts above are authoritative** — the house canonical sizes are what the guide's markup
expects.

```bash
python3 generate_image.py --batch image-prompts/adding-peritoneal-dialysis-program-images.json --dry-run
```
