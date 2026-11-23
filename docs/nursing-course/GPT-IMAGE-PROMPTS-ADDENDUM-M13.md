# GPT image prompts — Addendum: Module 13 and the competency framework

**Site:** renalcarematters.com (Renal Care Academy) · **Prepared:** November 23, 2026 · **Figures:** 14

This addendum covers content added after the first brief (GPT-IMAGE-PROMPTS.md): advanced Module 13 on continuous renal replacement therapy (CRRT) and hemodiafiltration (HDF), and the competency framework on the course home. Every prompt in a gray block is complete on its own.

## How to produce

1. **One figure per chat.** Paste one prompt into a fresh ChatGPT image chat and ask for the canvas size on the entry.
2. **Attach when told.** Only 13-D (the CVVHDF circuit) needs an attachment: `catheter-hub-connection-reference.png`, provided with the first brief.
3. **Check every label** against the verbatim label list in the prompt; ask for a one-word fix rather than regenerating when a single word is wrong.
4. **Run the QA list.** Reject any image with an invented number, a dark background, a missing or altered footer (`© renalcarematters.com`), or a wrong circuit connection.
5. **Clinical review.** Entries with reviewer flags need your check before publishing, especially 13-D (citrate and calcium line sites) and 13-E (citrate watch).
6. **Save** under the exact filename on each entry (PNG) into the same `Module images` folder as before; I will process, place, and publish them.
7. **Dense figures.** If 13-K (trials table) or H-3 garbles after two tries, say so; the page already carries the HTML version of the trials table.

## Standing rules (already written into every prompt)

- Light background; Inter font; navy #0f1e2e text, teal #1a6b72 accent. Circuit colors: arterial red #C00000, venous blue #1F6FC0, replacement green #2E6B3E, dialysate and effluent teal #1A6B72; citrate amber #C9A84C and calcium purple #4B3280 (13-D only, declared in its legend).
- Footer `© renalcarematters.com`, bottom right, small, semi-transparent navy, on every figure except the hero (no text at all).
- American English. Numbers only as the lesson states them; no doses, rates, targets, or alarm limits.

## Production checklist

| # | ID | Figure | File | Canvas | Placement | Reviewer flag |
|---|---|---|---|---|---|---|
| 1 | 13-H0 | The ICU nurse and the hanging bags | `nephrology-nursing-13-convective-therapies-crrt-hdf-vignette-hero.png` | 2048 × 2048, 1:1 | Module 13 hero circular vignette (`figure.hero-figure > .hero-vignette`) | yes |
| 2 | 13-A | A tea bag and a sieve: three ways across the membrane | `nephrology-nursing-13-convection-sieving.png` | 1792 × 1024, 16:9 | Module 13, section `physiology` (Convection, replacement fluid, and the filtration fraction); analogy introduced in `model` (A sieve as well as a tea bag) | yes |
| 3 | 13-B | Pre-dilution or post-dilution, and the filtration fraction | `nephrology-nursing-13-pre-post-dilution.png` | 1792 × 1024, 16:9 | Module 13, section `physiology` (Convection, replacement fluid, and the filtration fraction) | yes |
| 4 | 13-C | The four continuous modes, and SLED | `nephrology-nursing-13-crrt-modes.png` | 1536 × 1152, 4:3 | Module 13, section `crrt-modes` (The four continuous modes, and the prolonged intermittent alternative) | yes |
| 5 | 13-D | CVVHDF circuit with regional citrate and calcium | `nephrology-nursing-13-cvvhdf-citrate-circuit.png` | 1672 × 941, 16:9 | Module 13, section `crrt-anticoag` (Keeping the circuit open: no anticoagulant, heparin, or regional citrate); also supports `crrt-circuit` (The circuit: priming, pressures, filter life, and alarms) | yes |
| 6 | 13-E | Citrate: how it works, what to watch, when to report | `nephrology-nursing-13-citrate-watch.png` | 1024 × 1536, 2:3 portrait | Module 13, section `crrt-anticoag` (Keeping the circuit open: no anticoagulant, heparin, or regional citrate) | yes |
| 7 | 13-F | Three fluid numbers that must agree | `nephrology-nursing-13-three-fluid-numbers.png` | 1536 × 1152, 4:3 | Module 13, section `crrt-fluid` (Hourly fluid balance: three numbers that must agree); also supports `bedside` (Safety rules shared by every convective therapy) | — |
| 8 | 13-G | Circuit alarms: patient first, then the circuit | `nephrology-nursing-13-crrt-pressure-alarms.png` | 1024 × 1536, 2:3 portrait | Module 13, section `crrt-circuit` (The circuit: priming, pressures, filter life, and alarms) | yes |
| 9 | 13-H | What continuous clearance takes away: the watch table | `nephrology-nursing-13-crrt-complications-watch.png` | 1536 × 1152, 4:3 | Module 13, section `crrt-complications` (Complications, and what continuous clearance takes away) | yes |
| 10 | 13-I | Online HDF: the machine makes its own infusion fluid | `nephrology-nursing-13-online-hdf-fluid-path.png` | 1792 × 1024, 16:9 landscape | Module 13 page, section `hdf-principles` (Online hemodiafiltration: how the machine makes fluid safe to infuse) | yes |
| 11 | 13-J | Convection volume: the arithmetic that decides the dose | `nephrology-nursing-13-convection-volume-arithmetic.png` | 1792 × 1024, 16:9 landscape | Module 13 page, section `hdf-prescription` (The HDF prescription: convection volume and what drives it) | — |
| 12 | 13-K | The HDF trials at a glance | `nephrology-nursing-13-hdf-trials.png` | 1536 × 1152, 4:3 | Module 13 page, section `hdf-evidence` (What the trials show, and what they do not) | yes |
| 13 | 13-L | HDF alarms: meaning, first check, escalate | `nephrology-nursing-13-hdf-alarms.png` | 1024 × 1536, 2:3 portrait | Module 13 page, section `hdf-session` (Running an HDF session: before, during, and after), beside the alarm table | yes |
| 14 | H-3 | Four levels of competence, and one skill climbing them | `nephrology-nursing-competency-levels.png` | 1792 × 1024, 16:9 landscape | Hub page `academy/nephrology-nursing.html`, section `progression` (How competence builds from module to module), above the progression table | yes |

---

# Part 1 — The plan

Same rules as the main plan (IMAGE-PLAN.md): every figure has a job (U understand, A apply, P appreciate); light background; Inter font; navy #0f1e2e text, teal #1a6b72 accent; footer `© renalcarematters.com` bottom right on every figure except the hero; American English; every number copied from the module text (`tools/nursing/content/m13.py`, `m13_x.py` for CRRT, `m13_x2.py` for HDF, `common.py` for the competency levels) — not in the text, not in the figure; no doses, alarm limits or device settings ("per protocol / manufacturer").

Filenames: `images/nephrology-nursing-13-<short-name>.png`; hub figure `images/nephrology-nursing-competency-levels.png`.

| ID | Type | Placement (section id) | Job | What it must show | Governing skill |
|---|---|---|---|---|---|
| 13-H0 | HERO 2048×2048 | Module 13 hero | P | A Filipino ICU nurse at the bedside of a ventilated or sedated patient, checking the hanging fluid bags on a continuous therapy machine with integrated scales; calm, focused; machine screen unreadable; no other module's scene repeated (Module 4 hero is an ICU phone escalation). | williamriveromd-hero-vignette v3 |
| 13-A | MECH 1792×1024 | physiology | U | Diffusion vs ultrafiltration vs convection across a membrane: tea bag and sieve pictures walked back to the fiber wall; sieving coefficient near 1 for urea/potassium, lower for beta-2 microglobulin (about 11,800 daltons, as in the text), near 0 for albumin and cells. | williamriveromd-biomedical-mechanism-figure |
| 13-B | COMP 1792×1024 | physiology | U/A | Pre-dilution vs post-dilution side by side (where fluid enters, blood thickness in the filter, clearance per liter, filter life) plus the worked filtration-fraction example from the text (blood flow 200 mL/min, hematocrit 30%, plasma flow 140 mL/min, 35 mL/min removed → 25%). | williamriveromd-simple-figure |
| 13-C | CARD 1536×1152 | crrt-modes | U | SCUF, CVVH, CVVHD, CVVHDF (and SLED as the prolonged intermittent alternative): what each moves, by which mechanism, fluids used, typical use — from the module's mode table. | williamriveromd-simple-figure |
| 13-D | CIRC 1672×941 | crrt-anticoag (or crrt-circuit) | U | CVVHDF circuit (both dialysate and replacement fluid) with regional citrate and calcium infusion lines placed exactly as the module text describes (if the text does not fix the sites, label "per unit protocol" and do not draw a specific site). Follow the circuit skill's locked topology and colors; modality CVVHDF means countercurrent dialysate PLUS a replacement line. | dialysis-circuit-schematic |
| 13-E | ALGO 1024×1536 | crrt-anticoag | A | Citrate: how it works (binds ionized calcium in the circuit; calcium replaced; citrate metabolized to bicarbonate) and the watch-and-report sequence: symptoms of low ionized calcium, samples per protocol, signs of accumulation as worded in the text (rising total-to-ionized calcium ratio, worsening acidosis, rising calcium requirement), who is at risk; "per protocol" for targets. | williamriveromd-algorithm-generator-skill |
| 13-F | CARD 1536×1152 | crrt-fluid | A | The three fluid numbers that must agree (prescribed net removal, machine net removal, total patient balance) with the hourly accounting example from the text, and when to call. | williamriveromd-simple-figure |
| 13-G | ALGO 1024×1536 | crrt-circuit | A | Continuous-therapy pressure alarms: alarm/trend → likely cause → first nursing check (patient and catheter first) → escalate; clotting signs; never override air detection. Names only as in the module table. | williamriveromd-algorithm-generator-skill |
| 13-H | CARD 1536×1152 | crrt-complications | A | Watch table: hypothermia (masks fever), electrolyte losses (phosphate, potassium, magnesium), acid–base, bleeding, catheter problems, drug removal (ask pharmacy/prescriber), nutrition losses, low platelets — each with what to watch and what to report. | williamriveromd-simple-figure |
| 13-I | MECH 1792×1024 | hdf-principles | U | Online HDF fluid path: treated water → ultrapure dialysate → cascade ultrafilters → sterile substitution fluid into the blood line (post-dilution), high-flux dialyzer; what convection adds (middle molecules). | williamriveromd-biomedical-mechanism-figure (+ circuit skill port rules) |
| 13-J | SEQ 1792×1024 | hdf-prescription | A | Convection volume = substitution volume + net ultrafiltration, with the module's worked arithmetic (23 L over 240 min ≈ 96 mL/min; 96 ÷ 350 ≈ 27% of blood flow; the 300 mL/min shortfall example; 21.0 + 2.5 = 23.5 L) — labeled "convective flow ÷ blood flow" as in the text. | williamriveromd-simple-figure |
| 13-K | CARD 1536×1152 | hdf-evidence | U/P | The trials at a glance (CONTRAST, Turkish OL-HDF, ESHOL, CONVINCE, pooled 2016, pooled 2024): comparator, size, result, with numbers copied exactly from the text; one line on why results differed (achieved convection volume; association vs randomized). | williamriveromd-simple-figure |
| 13-L | ALGO 1024×1536 | hdf-session | A | HDF session alarms (transmembrane pressure high, substitution/infusion fault, blood leak, conductivity, filtration-fraction limit): meaning → first check → escalate, as in the module's alarm table. | williamriveromd-algorithm-generator-skill |
| H-3 | SEQ/pyramid 1792×1024 | Hub, section `progression` | U/P | Miller's pyramid with the four course levels (Knows, Shows how, Does supervised, Does independent) — names and one-line meanings copied from COMPETENCY_LEVELS — and one example thread rising across modules (Clinical assessment and fluid status: Module 1 does-supervised → Module 9 does-independent after sign-off), plus "Self-study reaches Knows; higher levels need a verifier." | williamriveromd-simple-figure |


---

# Part 2 — Production prompts

## Module 13 — Convective Therapies: CRRT and Hemodiafiltration (base and CRRT)

Module page slug (from `common.py`): `nephrology-nursing-13-convective-therapies-crrt-hdf`. Sources: `tools/nursing/content/m13.py` (sections `model`, `physiology`, `evidence`, `bedside`, plus case, quiz, terms) and `tools/nursing/content/m13_x.py` (sections `crrt-modes`, `crrt-prescription`, `crrt-anticoag`, `crrt-fluid`, `crrt-circuit`, `crrt-complications`, `crrt-transitions`). Only 13-D needs an attachment.

---

### 13-H0 — The ICU nurse and the hanging bags
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

### 13-A — A tea bag and a sieve: three ways across the membrane
- **File:** images/nephrology-nursing-13-convection-sieving.png
- **Placement:** Module 13, section `physiology` (Convection, replacement fluid, and the filtration fraction); analogy introduced in `model` (A sieve as well as a tea bag)
- **Job:** U — the learner can see why convection removes middle molecules that diffusion leaves behind, and what the sieving coefficient means.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure (+ circuit-skill filter rules: blood in at the bottom, out at the top)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Diffusion, ultrafiltration, and convection across a filter fiber wall, with sieving coefficients near one for urea, lower for larger molecules, near zero for albumin.
- **Caption:** Diffusion moves small solutes down a concentration difference; convection drags solutes of any size up to the pore limit along with water pushed through by pressure. Each solute's sieving coefficient says how freely it crosses.
- **Source of truth:** m13.py `model`: tea bag = diffusion (urea, potassium drift across because there is more on one side); sieve = pressure pushes plasma water through and anything dissolved and small enough is carried along; larger "middle molecules" removed much better this way; sterile replacement fluid given back so the net effect is cleansing, not dehydration; correction: membrane also has charge and protein layers, so behavior is described by the sieving coefficient. m13.py `physiology` table: Diffusion — concentration difference — small solutes (urea, creatinine, potassium); Ultrafiltration — pressure difference — water (with whatever is dissolved); Convection — ultrafiltration large enough to drag solutes — small and middle molecules up to the pore size. Beta-2 microglobulin about 11,800 daltons, cleared poorly by diffusion alone; sieving coefficient close to 1 for urea and potassium, lower for larger molecules, close to 0 for albumin and blood cells. Terms: sieving coefficient 1 = as freely as water, 0 = not at all.
- **Reviewer flags:** The text gives "lower for larger molecules" and names beta-2 microglobulin as the example of a larger molecule cleared poorly by diffusion; the figure places beta-2 microglobulin in the "lower" band without a number. Confirm that wording. No numeric sieving coefficient is shown other than the text's "close to 1" and "close to 0".
- **Attach when generating:** not applicable

```text
Publication-grade biomedical mechanism schematic, 1792 × 1024 landscape (16:9), review-article style: how solutes cross a dialysis membrane by diffusion, ultrafiltration, and convection. Flat vector illustration with soft semi-3D shading, white #ffffff background, thin dashed boxes for magnified panels, clean sans-serif typography set in Inter (never serif). Text navy #0f1e2e; headings and accents clinical teal #1a6b72.

LAYOUT
Title at top left, bold navy: "A tea bag and a sieve". Subtitle in teal beneath: "Three ways to move things across a membrane".

LEFT PANEL (about 22% width) — organ-level context
A simple vertical hollow-fiber filter cartridge in light gray-blue, blood entering the bottom end cap (red #C00000 short tube) and leaving the top end cap (blue #1F6FC0 short tube); fine parallel lines inside suggest thousands of fibers. Label: "Filter: thousands of hollow fibers". A small dashed square on the cartridge wall connects by a thin dashed leader to the center panel. Under it two small icons side by side with labels: a tea bag "Tea bag = diffusion" and a kitchen sieve "Sieve = convection".

CENTER PANEL (about 50% width) — magnified fiber wall inside a dashed box titled "Magnified: one fiber wall"
Draw ONE vertical semipermeable wall (light gray-blue band with visible pores) dividing the box: "Blood side" on the left (pale red tint), "Outside the fiber" on the right (pale teal tint #eef6f7). Three horizontal lanes stacked top to bottom, each crossing the same wall:
1. Lane label "Diffusion". Many small dots on the blood side, few on the other; small dots drift right through pores. Small arrow caption: "Driven by a concentration difference". Removes best: "Small solutes: urea, creatinine, potassium".
2. Lane label "Ultrafiltration". Water droplets pushed right by a broad pressure arrow. Caption: "Driven by a pressure difference". Removes best: "Water".
3. Lane label "Convection". A large stream of water crosses the wall carrying small dots AND larger particles with it (solvent drag). Caption: "Water drags solutes with it". Removes best: "Small and middle molecules, up to pore size".
A thin note along the wall: "Membrane also has charge and protein layers".

RIGHT PANEL (about 28% width) — "Sieving coefficient: how freely it crosses"
A vertical scale bar from "1 = as freely as water" at top (teal) to "0 = does not cross" at bottom (gray). Three markers with small particle icons:
- top, near 1: "Urea, potassium: close to 1"
- middle band, no number: "Larger molecules: lower" with sub-label "e.g., beta-2 microglobulin (about 11,800 daltons)"
- bottom, near 0: "Albumin, blood cells: close to 0"

BOTTOM SUMMARY FLOW (full width, three boxes linked by arrows)
- Left box, pale pink: "Diffusion slows as molecules get larger" / "Beta-2 microglobulin: poorly cleared by diffusion alone"
- Center box, pale gray: "Convection removes liters of plasma water" / "Replacement fluid is given back into the blood"
- Right box, pale blue: "Net effect: cleaner plasma, not dehydration"

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No numeric sieving coefficient other than "close to 1" and "close to 0"; no 0.5, 0.6, or similar invented values
✗ No molecular weights other than "about 11,800 daltons" for beta-2 microglobulin
✗ No albumin or blood cells crossing the wall
✗ No convection lane showing only small dots; larger particles must cross with the water
✗ No diffusion lane driven by a pressure arrow; no ultrafiltration lane driven by a concentration gradient
✗ No dialysate countercurrent stream drawn in the convection lane
✗ No kidney or nephron anatomy; this is a filter fiber, not a glomerulus
✗ No dark background, no 3D photorealism, no cartoon style, no serif or decorative font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Three lanes cross the SAME wall: diffusion (gradient), ultrafiltration (pressure, water), convection (water dragging small and larger solutes)
□ Convection lane visibly carries larger particles; diffusion lane mainly small dots
□ Sieving scale shows urea/potassium close to 1, larger molecules lower (no number), albumin/blood cells close to 0
□ "about 11,800 daltons" spelled exactly; no other molecular weights or coefficients
□ Albumin and cells stay on the blood side
□ Filter cartridge: red at the bottom cap, blue at the top cap; no blood line on the side
□ Tea bag and sieve icons present with their labels
□ Bottom flow ends with "Net effect: cleaner plasma, not dehydration"
□ Label spelling correct throughout ("ultrafiltration", "microglobulin", "daltons"); no placeholder text
□ No invented numbers anywhere
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-B — Pre-dilution or post-dilution, and the filtration fraction
- **File:** images/nephrology-nursing-13-pre-post-dilution.png
- **Placement:** Module 13, section `physiology` (Convection, replacement fluid, and the filtration fraction)
- **Job:** U/A — the learner can predict how the replacement-fluid site changes clearance and filter life, and can work the filtration fraction from blood flow and hematocrit.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B comparison with a worked-example strip; circuit-skill port rules for the two mini filters)
- **Canvas:** 1792 × 1024, 16:9
- **Alt text:** Pre-dilution versus post-dilution replacement fluid compared, with the worked filtration fraction: 35 mL/min removed from 140 mL/min plasma flow equals 25%.
- **Caption:** Replacement fluid given before the filter keeps blood thinner and the filter alive longer, at some cost in clearance; given after, every liter removed is the patient's own plasma water, but blood thickens in the fibers. The filtration fraction measures how hard the filter is working.
- **Source of truth:** m13.py `physiology` comparison table — Pre-dilution: blood diluted before it reaches the fibers, stays thinner; clearance per liter lower (part of each liter removed is replacement fluid just added); filter life longer; typical use: CRRT when clotting limits filter life, HDF when blood flow or hematocrit limits post-dilution. Post-dilution: blood concentrated as water leaves, then diluted again after the filter; clearance per liter higher (every liter removed is the patient's own plasma water); filter life shorter if too much water is removed (blood thickens and clots); typical use: usual mode for HDF, common in CRRT when filter life allows. Filtration fraction = share of plasma flow removed as ultrafiltrate; plasma flow = blood flow × (1 − hematocrit); example 200 mL/min, hematocrit 30%, plasma flow 140 mL/min, 35 mL/min removed, 35 ÷ 140 = 25%; units set a ceiling for post-dilution by protocol; when reached, the prescriber can raise blood flow, lower the exchange, or move some replacement fluid to pre-dilution. Expression "200 × (1 − 0.30) = 140" from m13.py quiz item 3. m13_x.py `crrt-modes`: replacement site pre-filter, post-filter, or both (split) in CVVH.
- **Reviewer flags:** The 25% in the worked example is the text's illustrative arithmetic, not a ceiling; the figure labels it "worked example" and states that the ceiling is set by unit protocol. Confirm. No percentage clearance loss for pre-dilution is shown (the circuit skill's "about 15%" is not in the module and was removed).
- **Attach when generating:** not applicable

```text
Medical education comparison figure, 1792 × 1024 landscape (16:9), AJKD/NEJM graphical-abstract style: where replacement fluid enters the circuit, and the filtration fraction. White #ffffff background; clean sans-serif typography set in Inter (never serif); text navy #0f1e2e; headings clinical teal #1a6b72; card fills soft gray #f3f4f6.

LAYOUT
Title top center, bold navy: "Before the filter or after it?" Subtitle in teal: "Same replacement fluid, different entry point".
Upper 68% of the canvas: two equal panels separated by a soft dashed vertical divider. Lower 32%: a full-width worked-example strip.

EACH PANEL — mini circuit drawn the same way in both
A vertical filter cartridge with blood entering the BOTTOM end cap through a red #C00000 line from below and leaving the TOP end cap through a blue #1F6FC0 line going upward; a teal #1A6B72 effluent line leaves the LOWER SIDE port. A green #2E6B3E replacement-fluid line from a small bag ends as a SHORT STUB at a T-junction on the blood line. The green line never enters a side port and never continues past the junction.
- Left panel heading, teal: "Pre-dilution". The green stub joins the RED line just below the filter. Inside the fibers the blood is drawn pale and thin.
- Right panel heading, teal: "Post-dilution". The green stub joins the BLUE line just above the filter. Inside the fibers the blood darkens toward the top (thickening).
Under each mini circuit, four labeled rows in a soft gray card, verbatim:

Pre-dilution card:
- "Blood in filter: diluted, stays thinner"
- "Clearance per liter: lower"
- "Filter life: longer"
- "Typical use: CRRT when clotting limits filter life"

Post-dilution card:
- "Blood in filter: concentrates as water leaves"
- "Clearance per liter: higher"
- "Filter life: shorter if too much water removed"
- "Typical use: usual mode for HDF"

Mark "Filter life: longer" with a small renal-green #1f7a4d check icon and "Clearance per liter: higher" with a small green check; mark "Filter life: shorter if too much water removed" with a small amber #b8860b caution triangle.

WORKED-EXAMPLE STRIP (full width, light teal fill #eef6f7, rounded corners)
Strip heading, bold navy: "Filtration fraction: the share of plasma removed". Small gray tag at its right end: "Worked example, not a target".
Four boxes left to right, joined by navy arrows:
1. "Blood flow 200 mL/min" and beneath "Hematocrit 30%"
2. "Plasma flow = 200 × (1 − 0.30) = 140 mL/min"
3. "Ultrafiltrate removed 35 mL/min"
4. "35 ÷ 140 = 25%" (large, bold teal)
Below the boxes, one line in navy: "Higher fraction in post-dilution = thicker blood, faster clotting. Ceiling set by unit protocol."
Small side note at the far right, soft gray box: "At the ceiling, the prescriber may raise blood flow, lower the exchange, or move fluid to pre-dilution".

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No numbers other than 200 mL/min, 30%, 0.30, 140 mL/min, 35 mL/min, and 25%
✗ No percentage clearance loss for pre-dilution (no "15%" or similar)
✗ No ceiling value printed; "25%" appears only as the worked result, never as a limit or target
✗ No replacement fluid entering a side port of the filter; no green line continuing past its junction
✗ No blood line attached to the side of a filter; blood only at the end caps, entering at the bottom
✗ No dialysate bag or dialysate line in either panel
✗ No panel styled as "right" and the other "wrong"; both are valid choices
✗ No dark background, no photorealism, no cartoon style, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Pre-dilution green stub joins the RED line below the filter; post-dilution joins the BLUE line above it
□ Green stubs end at the junction; nothing green enters a side port or continues along a blood line
□ Blood enters the bottom cap and leaves the top cap in both panels; effluent leaves a side port
□ Post-dilution fibers drawn darker toward the outlet; pre-dilution blood drawn thinner
□ All eight card rows present and verbatim
□ Arithmetic reads 200 × (1 − 0.30) = 140 mL/min and 35 ÷ 140 = 25%, digits correct
□ "Worked example, not a target" tag and "Ceiling set by unit protocol" line present
□ No other numbers anywhere (no 15%, no ceiling value)
□ Both panels have equal visual weight
□ Label spelling correct ("Hematocrit", "Filtration fraction", "Ultrafiltrate"); American spelling
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-C — The four continuous modes, and SLED
- **File:** images/nephrology-nursing-13-crrt-modes.png
- **Placement:** Module 13, section `crrt-modes` (The four continuous modes, and the prolonged intermittent alternative)
- **Job:** U — the learner can name which pumps and fluids run in each mode, by which mechanism it clears, and why it is chosen.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Reference card comparing SCUF, CVVH, CVVHD, and CVVHDF by fluids used, mechanism, what each removes best, and why chosen, with SLED as the prolonged alternative.
- **Caption:** The name of the mode tells you which pumps are running, and therefore which fluids, bags, and checks apply. Every mode can also remove fluid, and no mode has proven survival benefit over another.
- **Source of truth:** m13_x.py `crrt-modes` mode table — SCUF: blood pump and effluent pump only, no dialysate, no replacement fluid; ultrafiltration alone; water, with only small amounts of solute; fluid overload (e.g., heart failure resistant to diuretics) when potassium, acid–base, and urea are acceptable. CVVH: replacement fluid pre-filter, post-filter, or both, no dialysate; convection; small and middle molecules in proportion to volume filtered; unit preference or larger molecules a target; demands attention to filtration fraction. CVVHD: dialysate countercurrent, no replacement fluid; diffusion; small molecules (potassium, urea, hydrogen ions); common with regional citrate protocols, lower filtration fraction so filters tend to last longer. CVVHDF: both; diffusion plus convection; small molecules efficiently plus some middle molecules; flexible default in many ICUs, the mode used in the two large dose trials. Net UF in every mode, set separately. "No mode has proven survival benefit over another." SLED: one form of PIRRT, standard HD machine with reduced blood and dialysate flows, roughly 6 to 12 hours, often overnight; hemodynamic gentleness intermediate to high; consumables cost lower than CRRT. Full mode names spelled out as in the text ("venovenous", one word).
- **Reviewer flags:** "Roughly 6 to 12 hours" for SLED is flagged in m13_x.py FLAGS as a general-practice description without a single cited source; it appears here verbatim. Confirm.
- **Attach when generating:** not applicable

```text
Clinical reference card, 1536 × 1152 (4:3), publication-grade nephrology design: the four continuous kidney replacement modes and the prolonged intermittent alternative. White #ffffff background; clean sans-serif typography set in Inter (never serif); text navy #0f1e2e; column headers clinical teal #1a6b72 on soft gray #f3f4f6; alternating row fills white and very soft gray.

LAYOUT
Title top left, bold navy: "Continuous therapy modes". Subtitle in teal: "The mode name tells you which pumps run".

MAIN GRID — four columns (one per mode), five rows. Column headers (bold teal), each with the full name in small navy text beneath:
- "SCUF" / "Slow continuous ultrafiltration"
- "CVVH" / "Continuous venovenous hemofiltration"
- "CVVHD" / "Continuous venovenous hemodialysis"
- "CVVHDF" / "Continuous venovenous hemodiafiltration"

Row 1, "Fluids hung" — draw small bag icons: a green #2E6B3E bag labeled "Replacement" and a teal #1A6B72 bag labeled "Dialysate"; a gray empty outline where a fluid is absent.
- SCUF: no bags (two gray outlines), text "No dialysate, no replacement"
- CVVH: green bag only, text "Replacement, pre, post, or both"
- CVVHD: teal bag only, text "Dialysate, countercurrent"
- CVVHDF: green and teal bags, text "Dialysate and replacement"

Row 2, "Mechanism":
- SCUF "Ultrafiltration alone" · CVVH "Convection" · CVVHD "Diffusion" · CVVHDF "Diffusion plus convection"

Row 3, "Removes best":
- SCUF "Water, little solute"
- CVVH "Small and middle molecules"
- CVVHD "Small molecules: potassium, urea, hydrogen ions"
- CVVHDF "Small molecules, plus some middle molecules"

Row 4, "Often chosen for":
- SCUF "Fluid overload with acceptable chemistry"
- CVVH "Larger molecules a target; watch filtration fraction"
- CVVHD "Common with regional citrate; filters last longer"
- CVVHDF "Flexible default in many ICUs"

Row 5, "Every mode": a single merged cell across all four columns: "Also removes fluid: net ultrafiltration, set separately"

SIDE TILE (right edge or below the grid, bordered in teal, light teal fill #eef6f7), heading bold navy: "The prolonged intermittent alternative: SLED". Three short lines:
- "Standard HD machine, reduced blood and dialysate flows"
- "Roughly 6 to 12 hours, often overnight"
- "Gentler than intermittent HD; lower cost than CRRT"

BOTTOM TAKEAWAY BAR (full width, soft gray): "No mode has proven survival benefit over another. Know which mode is running, and which checks apply."

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No blood flow, dialysate rate, replacement rate, or dose numbers; the only numbers allowed are "6 to 12 hours"
✗ No dialysate bag in the SCUF or CVVH columns; no replacement bag in the SCUF or CVVHD columns
✗ No green dialysate bag or teal replacement bag; colors fixed: replacement green, dialysate teal
✗ No ranking stars, "best mode" badge, or survival claim for any mode
✗ No IHD column and no PD; SLED appears only in its side tile
✗ No circuit diagrams inside cells; bag icons only
✗ No acronym without its full name beneath it
✗ No dark background, no photorealism, no cartoon style, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Four mode columns in order SCUF, CVVH, CVVHD, CVVHDF, each with its full name spelled correctly ("venovenous", one word)
□ Bag icons correct: SCUF none; CVVH green only; CVVHD teal only; CVVHDF both
□ Mechanism row: ultrafiltration alone / convection / diffusion / diffusion plus convection
□ "Removes best" and "Often chosen for" rows verbatim
□ Merged row states every mode also removes fluid by net ultrafiltration
□ SLED tile present with "Roughly 6 to 12 hours, often overnight"; no other numbers anywhere
□ Takeaway bar: "No mode has proven survival benefit over another."
□ No "best mode" badge or ranking
□ Label spelling correct throughout; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-D — CVVHDF circuit with regional citrate and calcium
- **File:** images/nephrology-nursing-13-cvvhdf-citrate-circuit.png
- **Placement:** Module 13, section `crrt-anticoag` (Keeping the circuit open: no anticoagulant, heparin, or regional citrate); also supports `crrt-circuit` (The circuit: priming, pressures, filter life, and alarms)
- **Job:** U — the learner can trace blood, dialysate, replacement fluid, citrate, and calcium through a CVVHDF circuit and say where each pressure and sample is taken.
- **Governing skill:** dialysis-circuit-schematic (locked topology; modality CVVHDF: countercurrent dialysate PLUS replacement)
- **Canvas:** 1672 × 941, 16:9
- **Alt text:** CVVHDF circuit from a jugular dialysis catheter: citrate enters the red access line, dialysate runs countercurrent, replacement fluid joins one blood line, calcium returns separately.
- **Caption:** Citrate enters the blood line just after it leaves the patient and binds calcium so the circuit cannot clot; much of it leaves in the effluent, and calcium is replaced into the patient by a separate infusion. Dialysate runs outside the fibers against the blood; replacement fluid joins the blood line itself.
- **Source of truth:** m13_x.py `crrt-modes`: CVVHDF = both dialysate and replacement fluid, diffusion plus convection; building blocks: blood pump, filter, effluent pump, dialysate pump, one or two replacement pumps, syringe or infusion pumps for anticoagulant; integrated scales; usually a non-tunneled dialysis central venous catheter. `crrt-prescription`: replacement site pre-filter, post-filter, or split. `crrt-anticoag` citrate steps: (1) citrate infused into the blood line just after it leaves the patient, binds ionized calcium; (2) in the filter much of the citrate–calcium complex passes into the effluent and is discarded; (3) calcium replaced by a separate calcium infusion into the patient, either through the return line or a separate central line, according to the machine and protocol; (4) citrate reaching the patient is metabolized (liver, muscle) to bicarbonate. Post-filter ionized calcium sampled from the circuit after the filter (circuit anticoagulated enough? guides citrate rate); patient ionized calcium from an arterial line or the patient's own vein (patient safe? guides calcium infusion); label every sample with site and time; never run calcium through the same line as citrate. `crrt-circuit` pressure table: access (between catheter and blood pump, normally negative), pre-filter (after pump, before filter, positive), return/venous (after filter, before re-entry, positive), effluent pressure (fluid side of the filter), transmembrane pressure (calculated across the membrane), air trap; air detector and blood leak detector (red cells in the effluent). m13.py `physiology`: convection, solvent drag. Topology, port rules, colors, catheter course from the dialysis-circuit-schematic skill.
- **Reviewer flags:** (1) Calcium site: the text allows the return line OR a separate central line; the figure draws a separate purple line to a separate central venous line, labeled "per protocol", and notes the alternative. Confirm. (2) Citrate site: the text says "just after it leaves the patient"; the figure places the citrate tee on the red line after the access-pressure point and before the blood pump (simple-figure skill order). Confirm against the ICU's machine. (3) Post-filter sample site placed on the blue line between the filter outlet and the post-dilution tee; the text says only "from the circuit after the filter". Confirm. (4) Removed from the circuit-skill template because the module does not state them: KDIGO dose 20–25 mL/kg/h on the circuit, "about 15%" pre-dilution clearance loss, filtration fraction 20–25%, IHD 500 mL/min, five-modality legend, and blood pump "mL/min" label. (5) Catheter in the right internal jugular with the tip at the SVC–right atrial junction is a circuit-skill anatomy rule; the module says only "non-tunneled dialysis central venous catheter". (6) Amber #C9A84C (citrate) and purple #4B3280 (calcium) are additions to the circuit palette, declared in the legend.
- **Attach when generating:** /root/.claude/skills/synced/e7f3cdd9-a361-44a3-a710-a92e74c17604_d5a9b0e0-f0c3-4377-8b81-f15e9ba9cc14/dialysis-circuit-schematic/assets/catheter-hub-connection-reference.png (the same file is provided as /mnt/user-data/outputs/nursing/image-plan/catheter-hub-connection-reference.png; attach it to the ChatGPT message together with the prompt)

```text
Flat 2D medical schematic, 1672 × 941 landscape (16:9) — CVVHDF (continuous venovenous hemodiafiltration) circuit with regional citrate anticoagulation and a separate calcium infusion. Two panels: (L) whole-circuit map of blood, dialysate, replacement, effluent, citrate, and calcium paths; (R) hollow-fiber cutaway showing countercurrent diffusion PLUS solvent drag. White #ffffff background. An attached reference image shows correct versus wrong catheter hub connections; follow the CORRECT example.

════════════════════════════════════
LAYER A — CIRCUIT TRUTH BLOCK (supreme override)
- MODALITY IS CVVHDF: BOTH a dialysate bag AND a replacement-fluid bag. Both panels teach diffusion plus convection.
- RED #C00000 = blood leaving the patient (arterial/access). BLUE #1F6FC0 = blood returning (venous/return). Red and blue are used for blood only.
- DIALYSATE (TEAL #1A6B72): dialysate bag → dialysate pump → filter's UPPER SIDE PORT (near the blood outlet). Flows DOWN outside the fibers, countercurrent to blood, and leaves with the effluent at the LOWER SIDE PORT.
- REPLACEMENT FLUID (GREEN #2E6B3E): bag → replacement pump → THREE-WAY SELECTOR → EITHER the pre-dilution tee (red line, between blood pump and filter inlet) OR the post-dilution tee (blue line, after the filter outlet). ONE ROUTE AT A TIME. Badge the selector "OR — select one route"; both branches equal visual weight. Replacement NEVER enters a side port.
- EFFLUENT (TEAL #1A6B72): filter's LOWER SIDE PORT → effluent pressure point → blood leak detector → effluent pump → waste bag. Effluent = spent dialysate + ultrafiltrate (with the citrate–calcium complex).
- CITRATE (AMBER #C9A84C): citrate bag → small citrate pump → SHORT STUB tee into the RED line just after it leaves the patient: AFTER the access pressure point, BEFORE the blood pump.
- CALCIUM (PURPLE #4B3280): calcium bag → small calcium pump → its OWN separate line to a separate small central venous line in the patient's upper chest. It never joins the citrate line, never joins the red line, and never enters the filter.
- AN INFUSION JOINS A LINE, IT NEVER REROUTES OR RECOLORS IT. Green and amber branches end at their tees as SHORT STUBS. The red line stays red and unbroken from the red hub to the filter's bottom cap; the blue line stays blue and unbroken from the filter's top cap to the blue hub.
- ENDS ARE FOR BLOOD, SIDES ARE FOR FLUID. Bottom END CAP (red) = blood inlet; top END CAP (blue) = blood outlet. Side ports carry dialysate and effluent only. The red line approaches the bottom cap FROM BELOW along the filter axis; the blue line leaves the top cap UPWARD along the same axis.
- CATHETER: temporary, non-tunneled, dual-lumen, right internal jugular — ONE catheter bifurcating into TWO limbs, each ending in a luer hub with a colored terminal cap (one RED, one BLUE), a clamp on each limb. Translucent course: internal jugular → brachiocephalic vein → superior vena cava, tip at the SVC–right atrial junction. Only bifurcation and hubs outside the skin.
- Lines connect END-TO-END at the hub tips: one continuous tube of constant width, no gap, no side attachment, NO ARROWHEAD STANDING IN FOR A CONNECTION. No hub-tip zoom inset.
- HUB HEIGHTS MATCH LINE HEIGHTS: BLUE hub HIGH, level with the venous line along the top; RED hub LOW, level with the arterial line along the bottom.
- FLIPPED LAYOUT: red half along the BOTTOM, blue half along the TOP; blood ascends the filter.
- Blood path order (mandatory): patient (RED hub, low) → ACCESS PRESSURE (negative) → CITRATE TEE (amber) → BLOOD PUMP (roller) → PRE-DILUTION TEE → PRE-FILTER PRESSURE → FILTER bottom cap → up inside fibers → top cap → POST-FILTER SAMPLE SITE → POST-DILUTION TEE → VENOUS PRESSURE → AIR TRAP AND AIR DETECTOR → patient (BLUE hub, high).
- Anchor to landmarks: the venous pressure gauge sits just after the post-dilution tee; the air detector sits immediately beside the patient's BLUE hub, the last thing blood passes. Nothing between the air detector and the blue hub.
- Blood pump on the RED side only. Pre-filter pressure INLINE between pump and filter inlet.
- Arrows: red arrows patient → machine; blue arrows machine → patient; teal dialysate arrows run downward outside the fibers.

════════════════════════════════════
LAYER B — SPATIAL ORIENTATION
- Left panel (about 64% width): patient head, neck, upper chest at far left in light-gray outline; catheter in the right neck, limbs splayed (blue hub high, red hub low); a separate small purple central line in the upper chest. Red line along the bottom to a vertical filter at the panel's right; blue line returns along the top. Bags hang along the right edge, each drawn sitting on a small scale cradle: dialysate (teal) and replacement (green) upper right; effluent waste bag lower right. Citrate (amber) and calcium (purple) small bags and pumps lower left, near the patient.
- Right panel (about 36% width): standalone vertical filter cutaway, blood bottom → top.

════════════════════════════════════
LAYER C — RENDER SPECIFICATIONS
Panel heading, top left: "CVVHDF circuit with regional citrate". Component labels, verbatim:
- "Dialysis catheter, internal jugular (temporary)"
- "Access pressure (suction, normally negative)"
- "Citrate in: binds calcium, circuit can't clot"
- "Blood pump"
- "Pre-filter pressure"
- "Filter"
- "Blood in" (bottom cap) and "Blood out" (top cap)
- "Dialysate in" (upper side port) and "Effluent out" (lower side port)
- "Transmembrane pressure (calculated)" as a thin double-headed annotation across the filter wall, not a flow arrow
- "Post-filter sample: is the circuit anticoagulated?"
- "Venous (return) pressure"
- "Air trap and air detector: never override"
- "Dialysate pump" · "Replacement pump" · "Effluent pump"
- "Replacement fluid" · "Dialysate" · "Effluent bag"
- "OR — select one route"
- "Pre-dilution: longer filter life"
- "Post-dilution: more clearance per liter"
- "Effluent pressure"
- "Blood leak detector"
- "Integrated scales: hands off"
- "Citrate per protocol"
- "Calcium per protocol: separate line"
Small gray note under the calcium label: "Or via return line, per machine and protocol".
Small note box near the patient, teal outline: "Patient sample: arterial line or vein. Is the patient safe?"
Right panel cutaway, title: "Inside the filter: diffusion plus convection". Labels:
- "Blood rises inside the fibers"
- "Dialysate flows the opposite way"
- "Water drags solutes across"
- "Citrate–calcium complex leaves in effluent"
- "Cells and albumin stay in the blood"
Cutaway: teal dialysate enters at the upper side port and flows DOWN outside the fibers; small arrows also cross the wall outward (solvent drag); effluent leaves the lower side port.
Legend box (small, lower right of left panel): red "Blood out of patient"; blue "Blood back to patient"; teal "Dialysate and effluent"; green "Replacement fluid"; amber "Citrate"; purple "Calcium".
Typeface: Inter for all text. Leader lines thin navy. Text navy #0f1e2e.
Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all structures and labels.

════════════════════════════════════
LAYER D — IMAGING PHYSICS
Not applicable — schematic.

════════════════════════════════════
LAYER E — NEGATIVE CONSTRAINTS
✗ No missing dialysate bag or replacement bag — CVVHDF shows both.
✗ No dialysate entering the blood line; no replacement fluid entering a side port.
✗ No cocurrent dialysate; dialysate enters near the blood OUTLET (upper) and leaves near the INLET (lower).
✗ No permanently forked green line feeding both tees; no selector without the "OR — select one route" badge.
✗ No green or amber segment replacing any stretch of blood line; no infusion color continuing past its tee.
✗ No citrate tee on the blue line, after the blood pump, or on the filter.
✗ No calcium line joining the citrate line, the red line, or the filter; calcium and citrate never share a line.
✗ No blood line touching the side of the filter; no fluid line on an end cap.
✗ No air detector before the venous pressure gauge; nothing between the detector and the blue hub.
✗ No blood pump on the return side; no pre-filter gauge on a side branch.
✗ No filter with blood descending.
✗ No line attached to the side of a hub; no arrowhead in place of a connection; no hub-tip zoom inset; no both hubs at mid-height.
✗ No catheter tip in the neck, mid-SVC, or ventricle; no two dialysis catheters.
✗ No numbers anywhere: no flow rates, doses, mL/kg/h, percentages, calcium targets, pressures, or alarm limits.
✗ No modality legend listing other therapies; no heparin line.
✗ No kidney drawn in the circuit; no red or blue on anything but blood.
✗ No dark background, no 3D render, no DM Sans, no serif font, no cartoon style, no garbled or placeholder text, no prompt text in the image.
✗ No missing or altered footer.

════════════════════════════════════
LAYER F — STYLE REFERENCE
Flat vector schematic, white background, leader-line labels, colors exactly as in Layers A and C, card fill #f3f4f6, Inter.

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Header, bags, and cutaway agree: CVVHDF, both a dialysate bag and a replacement bag, countercurrent stream plus outward solvent-drag arrows
□ Dialysate (teal) enters the UPPER side port and flows down; effluent (teal) leaves the LOWER side port
□ Replacement (green) reaches the blood line only, through the selector badged "OR — select one route"; both branches equal weight; short stub at the tee
□ Citrate (amber) is a short stub on the RED line, after access pressure and before the blood pump
□ Calcium (purple) runs on its own line to a separate central line; it never meets the citrate line, the red line, or the filter; "Or via return line, per machine and protocol" note present
□ Post-filter sample site on the blue line after the filter; patient-sample note near the patient
□ Exactly four filter connections: two end caps (blood), two side ports (fluid); no blood line on a side wall
□ Red line enters the bottom cap from below; blue leaves the top cap upward; blood ascends
□ Blood path order: access pressure → citrate tee → blood pump → pre-dilution tee → pre-filter pressure → filter → post-filter sample → post-dilution tee → venous pressure → air trap and detector → blue hub
□ Air detector is the last component before the patient
□ Effluent line carries effluent pressure point and blood leak detector before the effluent pump
□ Transmembrane pressure drawn as an annotation across the wall, not a flow arrow
□ Blue hub high, red hub low; trace each line hub to filter with no gap or arrowhead substitute
□ Catheter: one dual-lumen catheter in the internal jugular, red and blue terminal caps, clamps, tip at the SVC–right atrial junction
□ Legend shows all six colors, including amber citrate and purple calcium
□ No numbers anywhere (no rates, doses, targets, pressures, percentages)
□ Label spelling correct throughout ("hemodiafiltration", "anticoagulated", "Transmembrane"); American spelling; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-E — Citrate: how it works, what to watch, when to report
- **File:** images/nephrology-nursing-13-citrate-watch.png
- **Placement:** Module 13, section `crrt-anticoag` (Keeping the circuit open: no anticoagulant, heparin, or regional citrate)
- **Job:** A — the learner can recognize low ionized calcium, citrate accumulation, and citrate excess, take the first nursing check, and report.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, house style)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Citrate anticoagulation algorithm: how citrate works, two calcium samples, and the signs of low calcium, accumulation, and excess, each ending in report per protocol.
- **Caption:** Two calcium samples answer two questions: is the circuit anticoagulated, and is the patient safe. Low calcium, citrate accumulation, and citrate excess each have a recognizable pattern; the nurse checks the infusions and reports, and targets and adjustments come from the protocol.
- **Source of truth:** m13_x.py `crrt-anticoag`: citrate infused just after blood leaves the patient, binds ionized calcium so the circuit cannot clot; much of the citrate–calcium complex passes into the effluent; calcium replaced by a separate infusion; citrate reaching the patient metabolized mainly by liver and also muscle to bicarbonate. Post-filter ionized calcium — "Is the circuit anticoagulated enough?" — guides the citrate rate; patient ionized calcium (arterial line or patient's own vein) — "Is the patient safe?" — guides the calcium infusion; label every sample with site and time; targets from the protocol. Low ionized calcium: tingling around the mouth or in the fingers, muscle cramps or spasm, falling BP, arrhythmia, prolonged QT; check first that the calcium infusion is running, connected, not empty; report at once. Accumulation: at risk — severe liver failure, severe shock with poor tissue perfusion (high or rising lactate); pattern — total calcium rising while patient ionized calcium low or falling (ratio rises), rising calcium infusion requirement, worsening metabolic acidosis with increasing anion gap; reported, not managed alone; threshold and response set by protocol and prescriber. Excess: metabolic alkalosis, sometimes high sodium; report rising bicarbonate or pH. Safety: high-alert medicines; double-check bag, concentration, rate, line at every change; never calcium through the same line as citrate; never restart a stopped citrate or calcium infusion without knowing why. `crrt-transitions`: when the circuit stops, stop or adjust citrate and calcium exactly as the protocol directs. m13.py case (empty calcium bag as cause).
- **Reviewer flags:** No ionized calcium targets, ratio threshold, or rates are shown; m13_x.py FLAGS confirms these are deliberately left to the unit protocol. Confirm the wording against the ICU's citrate protocol (also flagged in m13.py).
- **Attach when generating:** not applicable

```text
Clean publication-ready clinical algorithm flowchart, 1024 × 1536 portrait (2:3), renalcarematters.com house style: regional citrate anticoagulation in continuous therapy. White #ffffff background; restrained typography set in Inter (never serif); navy #0f1e2e text; thin teal #1a6b72 connector arrows; generous margins; publication-grade vector look; no photos, no people, no 3D.

COLOR CONVENTIONS
Navy #0f1e2e text; teal #1a6b72 decision diamonds and arrows; amber #C9A84C fill tint for citrate boxes; purple #4B3280 outline for calcium boxes; caution amber #b8860b for warning nodes; renal green #1f7a4d for "report" endpoints; soft gray #f3f4f6 side notes. A small legend at the top right: amber swatch "Citrate", purple swatch "Calcium".

TITLE (top): "Citrate: watch and report" in bold navy. Subtitle in teal: "Targets, rates, and adjustments: per protocol".

SECTION 1 — "How it works" (four small boxes in a horizontal row, joined by arrows)
1. "Citrate enters the blood line" (amber tint)
2. "Binds calcium: circuit can't clot"
3. "Much leaves in the effluent"
4. "Calcium replaced into the patient" (purple outline)
Below, one gray side note: "Citrate reaching the patient → liver and muscle → bicarbonate".

SECTION 2 — "Two calcium samples, two questions" (two side-by-side boxes)
- Left: "Post-filter ionized calcium" / "Is the circuit anticoagulated?" / "Guides citrate"
- Right: "Patient ionized calcium" / "Is the patient safe?" / "Guides calcium infusion"
A thin bar beneath both: "Label every sample: site and time".

SECTION 3 — "What you see" (three columns, each a vertical path ending in a green "report" box)
Column A heading (amber caution node): "Low ionized calcium"
- Signs box: "Tingling: mouth, fingers" / "Cramps or spasm" / "Falling BP, arrhythmia, long QT"
- Action box: "Check calcium infusion: running, connected, not empty"
- Endpoint (green): "Report at once"
Column B heading (amber caution node): "Citrate accumulation"
- At-risk box (gray): "Severe liver failure" / "Severe shock, rising lactate"
- Pattern box: "Total calcium up, ionized low" / "Ratio rising" / "Calcium needs keep rising" / "Worsening acidosis"
- Endpoint (green): "Report; follow protocol"
Column C heading (amber caution node): "Citrate excess"
- Pattern box: "Metabolic alkalosis" / "Rising bicarbonate or pH" / "Sometimes high sodium"
- Endpoint (green): "Report for fluid or rate change"

SECTION 4 — bottom safety strip (soft gray, full width), heading bold navy "Every bag change":
- "Double-check bag, concentration, rate, line"
- "Never run calcium in the citrate line"
- "Never restart a stopped infusion without knowing why"
- "Circuit stopped? Stop or adjust both per protocol"

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), subtle gray-navy at 70% opacity, never inside a node or overlapping arrows.

NEGATIVE CONSTRAINTS
✗ No ionized calcium targets, ranges, or units (no mmol/L values)
✗ No total-to-ionized calcium ratio threshold (no "2.5" or any number)
✗ No citrate or calcium doses, rates, or concentrations
✗ No node instructing the nurse to change a rate, give calcium, or stop citrate on their own; endpoints say "report" or "per protocol"
✗ No heparin, low-molecular-weight heparin, or other anticoagulant branches
✗ No circuit diagram, filter drawing, or pump illustration
✗ No "alkalosis" under accumulation or "acidosis" under excess (do not swap them)
✗ No more than four sections; no paragraph text in boxes
✗ No dark background, no photorealism, no cartoon icons, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Four "How it works" steps in order, ending with calcium replaced into the patient
□ Two sample boxes: post-filter guides citrate; patient guides calcium infusion; "site and time" bar present
□ Low calcium column: tingling, cramps/spasm, falling BP/arrhythmia/long QT → check the calcium infusion → report at once
□ Accumulation column: at-risk box (liver failure, shock with rising lactate) and four-part pattern including "Worsening acidosis"
□ Excess column: "Metabolic alkalosis", rising bicarbonate or pH, sometimes high sodium
□ Acidosis and alkalosis not swapped between columns
□ Every path ends in a green "report" endpoint; no nurse-initiated rate change
□ No numbers, targets, ratio thresholds, or doses anywhere
□ Safety strip shows all four rules
□ Amber = citrate, purple = calcium, legend present
□ Label spelling correct ("ionized", "anticoagulated", "bicarbonate"); American spelling; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent

---

### 13-F — Three fluid numbers that must agree
- **File:** images/nephrology-nursing-13-three-fluid-numbers.png
- **Placement:** Module 13, section `crrt-fluid` (Hourly fluid balance: three numbers that must agree); also supports `bedside` (Safety rules shared by every convective therapy)
- **Job:** A — the learner can reconcile the machine's net removal with the patient's total balance and the prescribed goal, and knows when to call.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E reference card with a worked-hour strip)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Machine net removal, patient total balance, and prescribed goal compared, with a worked hour where the machine removes 250 mL yet the patient is 50 mL short.
- **Caption:** The machine counts only its own fluids; it knows nothing about the infusions, the feed, or the urine bag. Record all three numbers every hour and report when they drift apart or the patient cannot tolerate removal.
- **Source of truth:** m13_x.py `crrt-fluid`: table — Machine net removal: fluid the machine took out after subtracting dialysate and replacement put back; from the machine's balance display for the hour. Patient total balance: everything in minus everything out (infusions, flushes, medicines, nutrition, blood products minus urine, drains, gastric losses, stool, and machine net removal); from the nurse's hourly intake and output record. Prescribed goal: what the prescriber wants per hour or per day, with limits; from the order. "The machine knows nothing about the antibiotic infusion, the nutrition feed, or the urine bag." Worked hour (illustrative): goal 100 mL negative per hour; intake infusions 180 mL, enteral feed 60 mL, line flushes 10 mL = 250 mL; output urine 20 mL, surgical drain 30 mL = 50 mL; machine net removal 250 mL; patient total balance = 250 − 50 − 250 = 50 mL negative; 50 mL short of the goal; follow the order and protocol, document which number was adjusted and why. Citrate and calcium infusions add volume: counted once, not twice and not never. When to call: BP falls, vasopressor needs rise, heart rate climbs, or lactate rises during removal; cumulative balance drifts beyond the protocol's limit over several hours, in either direction; machine balance error or fluid-loss limit reached; urine output rises noticeably, or weight, edema, or lung findings move against the goal. m13.py `bedside`: three numbers that must agree; report when they drift apart.
- **Reviewer flags:** none (all values are the text's illustrative arithmetic; the drift limit is "the protocol's limit" with no number).
- **Attach when generating:** not applicable

```text
Clinical reference card, 1536 × 1152 (4:3), publication-grade design: the three fluid numbers in continuous therapy, with one worked hour. White #ffffff background; clean sans-serif typography set in Inter (never serif); text navy #0f1e2e; headings clinical teal #1a6b72; card fills soft gray #f3f4f6 and light teal #eef6f7.

LAYOUT
Title top left, bold navy: "Three numbers that must agree". Subtitle in teal: "Record all three, every hour".

TOP ROW — three equal cards side by side, each with a simple flat line icon, a bold name, a one-line meaning, and a small "From:" source line:
1. Icon: generic machine console. "Machine net removal" / "What the machine took out, minus what it put back" / "From: the machine's balance display"
2. Icon: clipboard with in/out arrows. "Patient total balance" / "Everything in minus everything out" / "From: your hourly intake and output"
3. Icon: order sheet. "Prescribed goal" / "Balance the prescriber wants, with limits" / "From: the order"
Below the three cards, a thin amber #b8860b banner: "The machine knows nothing about infusions, feeds, or the urine bag".

MIDDLE STRIP — "A worked hour" (light teal fill, rounded, full width). Small gray tag at its right end: "Illustrative, not an order".
Goal chip at left, bold: "Goal: 100 mL negative per hour".
Three columns joined by minus signs into an equals box:
- "Intake 250 mL" with three small lines beneath: "Infusions 180" · "Enteral feed 60" · "Line flushes 10"
- "Output 50 mL" with two lines: "Urine 20" · "Surgical drain 30"
- "Machine net removal 250 mL"
Equation in large navy type: "250 − 50 − 250 = 50 mL negative"
Result chip in amber: "Machine performed as set; patient 50 mL short of goal"
One line beneath: "Act within the order and protocol. Document which number you adjusted and why."

BOTTOM-LEFT CARD — "Count once" (soft gray): "Citrate and calcium infusions add volume. Counted once: not twice, not never."

BOTTOM-RIGHT CARD — "When to call" (white with red #b91c1c left accent bar), four bullet lines:
- "BP falls, pressors rise, heart rate or lactate climbs"
- "Cumulative balance drifts past protocol limit"
- "Machine balance error or fluid-loss limit"
- "Urine output rises; weight, edema, or lungs move against goal"

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No numbers other than 100, 180, 60, 10, 250, 20, 30, 50 (mL) in the worked hour
✗ No drift limit, hourly removal limit, or maximum removal rate printed; "protocol limit" only
✗ No equation result other than "50 mL negative"; do not write "50 mL positive" or "100 mL negative" as the result
✗ No machine screen with readable numbers; icons are simple line drawings
✗ No circuit diagram, filter, or bags with labels
✗ No instruction for the nurse to change machine removal on their own; "act within the order and protocol" only
✗ No dark background, no photorealism, no cartoon style, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Three cards present: machine net removal, patient total balance, prescribed goal, each with its "From:" source
□ Amber banner "The machine knows nothing about infusions, feeds, or the urine bag" present
□ Worked hour: intake 180 + 60 + 10 = 250; output 20 + 30 = 50; machine 250
□ Equation reads exactly "250 − 50 − 250 = 50 mL negative"; goal 100 mL negative; "50 mL short of goal"
□ "Illustrative, not an order" tag present
□ "Count once" card present for citrate and calcium volume
□ "When to call" card shows all four triggers
□ No other numbers; no limits printed
□ Label spelling correct ("Enteral", "Cumulative", "edema" in American spelling); no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-G — Circuit alarms: patient first, then the circuit
- **File:** images/nephrology-nursing-13-crrt-pressure-alarms.png
- **Placement:** Module 13, section `crrt-circuit` (The circuit: priming, pressures, filter life, and alarms)
- **Job:** A — the learner can match each continuous-therapy alarm or trend to its likely cause, take the first nursing check, and escalate, without ever overriding air detection.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, house style)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Continuous therapy alarm algorithm: access, return, pre-filter and transmembrane trends, air and blood leak alarms, each mapped to likely cause, first check, and escalation.
- **Caption:** Look at the patient before the machine. Rising transmembrane pressure or pressure drop predicts clotting hours ahead, which gives time to report and plan a change with blood return; air and blood-leak detectors are never overridden.
- **Source of truth:** m13_x.py `crrt-circuit` troubleshooting table — Access pressure too negative (often with coughing or position change): catheter tip against vessel wall, kink, low circulating volume, clot in lumen → position of head and hip (femoral catheters kink when the patient sits up), external kinks and clamps, dressing tension, gentle flush per protocol, report persistent alarms; reversing lines only on physician order or protocol, increases recirculation. Return pressure high: kinked or clamped return line, clot in air trap or return lumen, patient position → line path and clamps, air trap for clot, patient position, report if not resolved. Return pressure suddenly low: disconnection or line separation → look at every connection at once, stop the blood pump if blood is leaking, emergency. Pre-filter pressure, TMP, or pressure drop rising steadily: filter clotting, post-dilution with high filtration fraction, low blood flow, inadequate anticoagulation → anticoagulant and calcium infusions running and connected, recent interruptions, filter and air trap for dark streaks, report the trend and prepare for a planned change. Air detector alarm: air in return line (loose connection, empty bag, micro-leak) → do not override, inspect line and air trap, remove air only by manufacturer's procedure, check every connection and bag. Blood leak detector alarm: red cells in effluent from ruptured fiber, or dirty/misread sensor → look at the effluent, follow manufacturer's procedure, confirmed leak means the filter is changed. "Always look at the patient before the machine." Trends matter more than single numbers; record pressures hourly. Planned change vs clotted circuit: most protocols forbid returning blood from a clotted circuit; follow yours. m13.py `bedside`: an air detector or blood-leak detector is never overridden; escalate repeated alarms.
- **Reviewer flags:** Balance/scale alarm (seventh row of the module table) is left to 13-F to keep this portrait readable; confirm. Alarm names follow the module; machines name pressures differently (m13_x.py FLAGS).
- **Attach when generating:** not applicable

```text
Clean publication-ready clinical algorithm flowchart, 1024 × 1536 portrait (2:3), renalcarematters.com house style: first response to continuous kidney therapy circuit alarms. White #ffffff background; restrained typography set in Inter (never serif); navy #0f1e2e text; thin teal #1a6b72 connector arrows; generous margins; publication-grade vector look; no photos, no people, no 3D.

COLOR CONVENTIONS
Teal #1a6b72 alarm-name boxes; soft gray #f3f4f6 "likely cause" boxes; white boxes with navy outline for "first check"; renal green #1f7a4d "report" endpoints; clinical red #b91c1c for the emergency row and the never-override rule; amber #b8860b for the clotting-trend row.

TITLE (top): "Circuit alarm: first response" in bold navy. Subtitle in teal: "Patient first, then circuit, then machine".

ENTRY NODE (centered, navy outline, full width): "Alarm or rising trend" → arrow down to a teal diamond: "Patient safe? Look before touching the machine". Arrow down into the six lanes.

SIX HORIZONTAL LANES (stacked top to bottom; each lane: alarm box → cause box → first-check box → endpoint chip on the right). Column headers above the first lane: "Alarm or trend" · "Likely cause" · "First check" · "Then".

1. "Access pressure too negative" → "Catheter against wall, kink, low volume, clot" → "Head and hip position; kinks, clamps; flush per protocol" → green "Report if persistent"
2. "Return pressure high" → "Kinked or clamped line, clot in air trap" → "Line path, clamps, air trap, position" → green "Report if not resolved"
3. RED-OUTLINED LANE: "Return pressure suddenly low" → "Disconnection or line separation" → "Check every connection; stop blood pump if leaking" → red "Emergency: call now"
4. AMBER LANE: "Pre-filter, TMP, or pressure drop rising" → "Filter clotting" → "Anticoagulant and calcium running? Dark streaks?" → green "Report trend; plan change"
5. "Air detector alarm" → "Loose connection, empty bag, micro-leak" → "Inspect line and air trap; check every connection" → red "Never override"
6. "Blood leak detector alarm" → "Ruptured fiber or dirty sensor" → "Look at the effluent; manufacturer's steps" → green "Confirmed leak: filter changed"

SIDE NOTE (small gray box at right of lane 1): "Reversing lines: only on order or protocol".

BOTTOM STRIP (soft gray, full width), two short lines:
- "Trends beat single numbers: record pressures hourly"
- "Clotted circuit: return blood only if your protocol allows"

RED RULE BAR (very bottom, above footer, white text on clinical red #b91c1c): "Never override the air or blood leak detector"

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), subtle gray-navy at 70% opacity, never inside a node or overlapping arrows.

NEGATIVE CONSTRAINTS
✗ No pressure values, mmHg numbers, or alarm limits anywhere
✗ No "silence and restart" node; no override option for air or blood leak alarms
✗ No node telling the nurse to change blood flow, replacement rate, or anticoagulant dose
✗ No reversal of lines shown as a routine first check
✗ No circuit diagram, machine drawing, or filter illustration
✗ No more than six lanes; no paragraph text in boxes
✗ No swapping of lanes 3 and 2 (suddenly low = disconnection; high = blockage)
✗ No dark background, no photorealism, no cartoon icons, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Entry diamond puts the patient before the machine
□ Six lanes in order with alarm → cause → first check → endpoint, all verbatim
□ "Return pressure suddenly low" lane red, ending "Emergency: call now"; "Return pressure high" lane points to blockage, not disconnection
□ Clotting-trend lane names pre-filter, TMP, and pressure drop, and ends "Report trend; plan change"
□ Air detector lane ends "Never override"; red rule bar present at the bottom
□ "Reversing lines: only on order or protocol" side note present
□ No pressure numbers or alarm limits anywhere
□ No node directs a rate or dose change
□ Label spelling correct ("Anticoagulant", "detector", "effluent"); no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent

---

### 13-H — What continuous clearance takes away: the watch table
- **File:** images/nephrology-nursing-13-crrt-complications-watch.png
- **Placement:** Module 13, section `crrt-complications` (Complications, and what continuous clearance takes away)
- **Job:** A — the learner knows what each complication looks like on continuous therapy and what to report.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Watch table for continuous therapy: hypothermia, electrolyte losses, acid–base, bleeding, catheter problems, drug removal, nutrition, low platelets, each with signs and action.
- **Caption:** Continuous clearance does not choose what it removes: heat, electrolytes, nutrients, and medicines leave as steadily as urea and potassium. Notice the trend and report it; replacement and dosing come from the prescriber, pharmacist, and dietitian.
- **Source of truth:** m13_x.py `crrt-complications`: "Continuous clearance does not choose what it removes." Hypothermia — blood cools outside the body; cooling hides fever; look for rising white cell count, new hypotension, rising lactate, rising warmer setting; core temperature trend, cool skin, shivering; check warmer, warming per protocol, report. Electrolytes — low phosphate common (more frequent with higher intensity in RENAL), low potassium and magnesium common after the first day; scheduled labs, weakness, new arrhythmia; report, replace as ordered, confirm bag composition. Acid–base — bicarbonate fluids correct acidosis; overcorrection can cause metabolic alkalosis, particularly with citrate; rising bicarbonate and pH; report for adjustment. Bleeding — catheter site, wounds, gut, airway; heparin increases risk; falling hemoglobin, blood in drains, stool, or airway; pressure where appropriate, report, review anticoagulation with prescriber. Catheter — infection and dysfunction; fever (may be masked), redness, discharge, pain, rising white cell count, repeated access alarms; report, cultures as ordered, aseptic handling. Drug removal — many antibiotics removed; under-dosing in sepsis as dangerous as overdosing; new antibiotic order or change in effluent rate; ask pharmacist or prescriber about continuous therapy dosing; note time of long interruptions. Nutrition — amino acids, glucose (with some fluids), water-soluble vitamins, trace elements lost in effluent; high protein needs; dietitian and prescriber set the plan; record feeding interruptions. Low platelets — sepsis, medicines, circuit consumption, or heparin-induced thrombocytopenia; daily blood count trend; report, ask whether HIT should be considered.
- **Reviewer flags:** Nutrition row is drawn from the section's prose (it is not a row of the module's watch table); low ionized calcium, citrate ratio, and hemodynamic-instability rows of the module table are left to 13-E and 13-F. m13_x.py FLAGS notes the complications content is general clinical knowledge except low phosphate (RENAL).
- **Attach when generating:** not applicable

```text
Clinical reference card, 1536 × 1152 (4:3), publication-grade nephrology design: complications of continuous kidney therapy and what the nurse watches. White #ffffff background; clean sans-serif typography set in Inter (never serif); text navy #0f1e2e; column headers clinical teal #1a6b72 on soft gray #f3f4f6; alternating row fills white and very soft gray.

LAYOUT
Title top left, bold navy: "What continuous clearance takes away". Subtitle in teal: "It removes heat, salts, nutrients, and drugs too".

TABLE — eight rows, three columns. Column headers: "Watch for" · "How you notice" · "What you do". Each "Watch for" cell has a small simple flat line icon in teal at its left.

1. Icon thermometer. "Hypothermia (hides fever)" | "Core temperature trend; cool skin; shivering" | "Check warmer; warm per protocol; report"
2. Icon lab tube. "Low phosphate, potassium, magnesium" | "Scheduled labs; weakness; new arrhythmia" | "Report; replace as ordered; check bag"
3. Icon pH scale. "Metabolic alkalosis" | "Rising bicarbonate and pH" | "Report for fluid or rate change"
4. Icon drop. "Bleeding" | "Sites, drains, stool, airway; falling hemoglobin" | "Pressure if appropriate; report"
5. Icon catheter. "Catheter infection or dysfunction" | "Fever, redness, discharge; repeated access alarms" | "Report; cultures as ordered; aseptic care"
6. Icon pill. "Drugs removed by the circuit" | "New antibiotic; effluent rate change" | "Ask pharmacist or prescriber about dosing"
7. Icon bowl. "Nutrients lost in effluent" | "Protein, vitamins, trace elements lost" | "Dietitian plan; record feeding interruptions"
8. Icon platelet. "Falling platelet count" | "Daily blood count trend" | "Report; ask about HIT"

Below the table, two small side-by-side note boxes:
- Amber #b8860b outline: "Fever may be hidden: watch white cells, lactate, BP, warmer setting"
- Teal outline: "Under-dosing an antibiotic is as dangerous as overdosing"

Small gray glossary line at the bottom left: "HIT = heparin-induced thrombocytopenia".

Footer: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all content.

NEGATIVE CONSTRAINTS
✗ No numbers anywhere: no temperatures, electrolyte values, platelet counts, protein targets, or doses
✗ No drug names, antibiotic doses, or electrolyte replacement amounts
✗ No row telling the nurse to adjust a dose, start replacement, or change fluids on their own; actions are "report", "as ordered", "ask", "per protocol"
✗ No metabolic acidosis as the complication in row 3; the row is alkalosis
✗ No more than eight rows; no paragraph text in cells
✗ No circuit diagram or machine drawing
✗ No dark background, no photorealism, no cartoon style, no serif font
✗ No garbled, misspelled, or placeholder text; no prompt text in the image
✗ No missing or altered footer

Render all text exactly as written above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Eight rows in order: hypothermia, electrolytes, alkalosis, bleeding, catheter, drugs, nutrients, platelets
□ Every cell verbatim; three columns "Watch for / How you notice / What you do"
□ Hypothermia row says it hides fever; amber note on hidden fever present
□ Drug row says to ask the pharmacist or prescriber; teal under-dosing note present
□ Every action is report / as ordered / ask / per protocol; no independent dosing
□ "HIT = heparin-induced thrombocytopenia" glossary line present
□ No numbers, drug names, or doses anywhere
□ Label spelling correct ("hemoglobin", "thrombocytopenia", "bicarbonate"); American spelling; no placeholder text
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

## Module 13 — Convective Therapies: CRRT and Hemodiafiltration (HDF)

Page: `academy/nephrology-nursing-13-convective-therapies-crrt-hdf.html`. All values below are copied from `tools/nursing/content/m13_x2.py` (section ids given per entry); shared terms checked against `m13.py`.

### 13-I — Online HDF: the machine makes its own infusion fluid
- **File:** images/nephrology-nursing-13-online-hdf-fluid-path.png
- **Placement:** Module 13 page, section `hdf-principles` (Online hemodiafiltration: how the machine makes fluid safe to infuse)
- **Job:** U — the learner sees how treated water becomes ultrapure dialysate and then sterile substitution fluid that joins the blood line after the dialyzer, and what convection adds.
- **Governing skill:** williamriveromd-biomedical-mechanism-figure, with dialysis-circuit-schematic port rules (end caps blood only, side ports fluid only, substitution joins the blood line)
- **Canvas:** 1792 × 1024, 16:9 landscape
- **Alt text:** Online HDF fluid path: treated water and concentrates become dialysate, pass two ultrafilters, and enter the venous blood line after a high-flux dialyzer.
- **Caption:** In online HDF the machine filters its own dialysate twice: once to make ultrapure dialysate for the dialyzer, and again to make sterile substitution fluid that runs straight into the blood. That is why the substitution line is handled like an intravenous line.
- **Source of truth:** m13_x2.py `hdf-principles`: chain — treated water from the unit's reverse osmosis (RO) loop mixed with acid and bicarbonate concentrates inside the machine; fresh dialysate through a first ultrafilter (holds back bacteria and endotoxin) → ultrapure dialysate, used on the dialysate side of the dialyzer; a portion drawn off through a second ultrafilter ("on some machines a further stage as well") → substitution fluid, infused by the substitution pump directly into the blood line. Filters in series reduce bacteria and endotoxin far below any single stage. ISO 23500-5:2024 requires online substitution fluid to be sterile and non-pyrogenic and the process validated. Sterility cannot be proved by culturing at the bedside. Substitution fluid handled as an intravenous medicine. High-flux dialyzer required; "20 or more liters of plasma water" per session. Convection: small solutes (urea, potassium) changed little; gain is in middle molecules; beta-2 microglobulin lowered more than HD; phosphate somewhat more, but time and diet remain the main tools; albumin largely retained, small losses. `hdf-prescription`: post-dilution = substitution fluid enters the venous line after the dialyzer; major trials used post-dilution. `hdf-session`: substitution line connects after the dialyzer for post-dilution. Values used: ISO 23500-5:2024 only. No other numbers.
- **Reviewer flags:** (1) Resolved: the lesson now gives beta-2 microglobulin as about 11,800 daltons throughout; this figure still omits the number. (2) The circuit is simplified: no pressure monitors, air detector or anticoagulant line are drawn, because this figure teaches the fluid path. A reviewer may want the air detector added on the venous line between the substitution junction and the patient. (3) Dialysate enters at the upper side port, countercurrent; the HDF text does not say which way the dialysate flows, so this comes from the house circuit rule.

```text
Flat 2D biomedical mechanism schematic, 1792 × 1024 landscape (16:9). Subject: online hemodiafiltration (HDF) fluid path. Review-article style, clean vector, white #ffffff background, thin dashed boxes around panels, generous margins. Font: Inter throughout (never serif).

TITLE BLOCK (top left):
- Title, bold navy #0f1e2e: "Online HDF: the machine makes its own infusion fluid"
- Subtitle, teal #1a6b72: "Hemodialysis by diffusion, plus high-volume convection"

PANEL 1 — FLUID PREPARATION CHAIN (left two-thirds, upper half). A horizontal chain of rounded boxes joined by teal #1A6B72 arrows, left to right:
1. Water-tap-and-pipe icon box: "Treated water (RO loop)"; beside it two small jug icons: "Acid and bicarbonate concentrates". Both arrows merge into:
2. "Fresh dialysate"
3. A cylindrical filter icon with a fine-mesh symbol: "Ultrafilter 1". Small note under it: "Holds back bacteria and endotoxin"
4. "Ultrapure dialysate" (teal outline). From here the path splits in two:
   - Branch A, teal line, runs down to the dialyzer's UPPER SIDE PORT, labeled "To dialysate side of dialyzer"
   - Branch B, a smaller "portion drawn off" arrow, runs right to a second filter icon: "Ultrafilter 2" with tiny gray note "Some machines add a further stage"
5. After Ultrafilter 2 the line turns GREEN #2E6B3E: box "Sterile, non-pyrogenic substitution fluid" → small pump icon "Substitution pump" → green line runs to the blood circuit.
Under the chain, a thin gray bracket: "Filters in series: far fewer bacteria and endotoxin than one stage"

PANEL 2 — BLOOD CIRCUIT (lower left and center). A vertical hollow-fiber cartridge labeled "High-flux dialyzer".
- RED #C00000 arterial line runs along the BOTTOM from a box at far left "From patient (access)", through a roller-pump icon "Blood pump", and enters the dialyzer's BOTTOM END CAP from below.
- Blood rises inside the fibers and leaves by the TOP END CAP; the BLUE #1F6FC0 venous line runs upward, then left along the TOP back to a box "Back to patient".
- On the blue line just after the top cap, the green substitution line meets it at a T-junction as a SHORT STUB. Badge at the junction: "Post-dilution: joins after the dialyzer". The blue line stays blue all the way to the patient.
- Dialyzer side ports carry fluid only: UPPER side port receives the teal ultrapure dialysate; LOWER side port sends a teal line to a waste drain icon: "Effluent out".
- Small gray callout near the substitution line: "Handled like an IV line"

PANEL 3 — FIBER CLOSE-UP (right third, dashed box, magnified from the dialyzer). One hollow fiber, blood rising inside (red at bottom fading to blue at top). Teal dialysate stream outside running downward. Two arrow types cross the fiber wall outward: thin arrows labeled "Diffusion" and broad arrows labeled "Convection: water drags solutes". Beside the fiber, a four-row checklist with small icons:
- "Urea, potassium: little change"
- "Middle molecules: more removed"
- "Beta-2 microglobulin: lower than HD"
- "Albumin: largely retained"

BOTTOM STRIP (full width, soft gray #f3f4f6, three linked boxes with navy arrows):
"Validated machine and filters" → "Clean water, disinfection on schedule" → "Sterile only if used as the manufacturer intends"
Small navy note at the right end of the strip: "Standard: ISO 23500-5:2024"

COLORS: navy #0f1e2e text; teal #1a6b72 headings; arterial blood #C00000 only on the arterial line; venous blood #1F6FC0 only on the venous line; substitution fluid #2E6B3E only from Ultrafilter 2 to the T-junction; dialysate and effluent #1A6B72. Pale fills only.

FOOTER: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, clear of all drawings.

DO NOT:
✗ No green substitution line entering any side port of the dialyzer; it joins the BLUE blood line only.
✗ No blood line touching a side wall of the dialyzer; blood uses the two end caps only.
✗ No fluid line attached to an end cap.
✗ No green segment continuing past the T-junction or replacing any stretch of blue line.
✗ No substitution line drawn teal, and no dialysate line drawn green.
✗ No pre-dilution branch, selector, or second substitution junction.
✗ No numbers except "23500-5:2024"; no flows, volumes, pressures, or daltons.
✗ No machine screen with readable values; no brand names or logos.
✗ No kidney drawn in the circuit; no catheter anatomy.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render every label exactly as written in quotation marks above, spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Chain order: treated water + concentrates → fresh dialysate → Ultrafilter 1 → ultrapure dialysate → Ultrafilter 2 → substitution fluid → substitution pump
□ Ultrapure dialysate goes to the UPPER side port; effluent leaves the LOWER side port
□ Green substitution line joins the BLUE venous line after the top cap as a short stub; "Post-dilution: joins after the dialyzer" badge present
□ Blood enters the bottom end cap (red) and leaves the top end cap (blue); no blood line on a side wall
□ Blood pump on the red line only
□ Fiber close-up shows both "Diffusion" and "Convection: water drags solutes"; four solute rows correct
□ No numbers other than ISO 23500-5:2024; no daltons, volumes, or flows
□ Label spelling: hemodiafiltration, ultrafilter, non-pyrogenic, microglobulin, effluent
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-J — Convection volume: the arithmetic that decides the dose
- **File:** images/nephrology-nursing-13-convection-volume-arithmetic.png
- **Placement:** Module 13 page, section `hdf-prescription` (The HDF prescription: convection volume and what drives it)
- **Job:** A — the learner adds substitution and net UF volumes and sees how a lower blood flow or a shortened session misses the target.
- **Governing skill:** williamriveromd-simple-figure (Scaffold C, horizontal step sequence)
- **Canvas:** 1792 × 1024, 16:9 landscape
- **Alt text:** Convection volume equals substitution plus net ultrafiltration; worked example shows how lower blood flow or a shorter session drops 23 liters to 19.4 or 17.8.
- **Caption:** Convection volume is everything filtered across the membrane: the substitution volume plus the net ultrafiltration. With the same fraction of blood flow, a weaker access or a shorter session misses the target even though the substitution setting never changed.
- **Source of truth:** m13_x2.py `hdf-prescription`: "Convection volume = substitution volume + net ultrafiltration (UF) volume"; net UF filtered out and not replaced; substitution filtered out and given back. Measure: "convective flow divided by blood flow, a simpler bedside cousin of the plasma-based filtration fraction." Determinants: effective blood flow (single biggest lever), effective treatment time, filtration fraction the circuit tolerates. Worked illustration ("arithmetic for teaching only; not a prescription"): 240 minutes; 23 liters (23,000 mL); 23,000 ÷ 240 = about 96 mL/min; blood flow 350 mL/min; 96 ÷ 350 = about 27%; access 300 mL/min at the same 27% → about 81 mL/min; over 240 minutes about 19.4 liters; ends 20 minutes early → about 17.8 liters; substitution 21.0 liters + net UF 2.5 liters = 23.5 liters. Many units use 23 liters per session as a working target; the target is the physician's order and unit protocol. Net UF set by fluid status, "never raised to make the convection number look better."
- **Reviewer flags:** none. (All arithmetic checked: 0.27 × 300 = 81; 81 × 240 = 19,440 mL; 81 × 220 = 17,820 mL.)

```text
Clean clinical education infographic, 1792 × 1024 landscape (16:9). Subject: how convection volume is calculated in hemodiafiltration (HDF), and how blood flow and time decide whether the target is reached. White #ffffff background, flat vector, rounded cards, generous whitespace. Font: Inter throughout (never serif).

TITLE BLOCK (top center):
- Title, bold navy #0f1e2e: "Convection volume: what decides the dose"
- Subtitle, teal #1a6b72: "Arithmetic for teaching only; not a prescription"

EQUATION BAND (full width below the title, light teal fill #eef6f7, rounded):
Large bold navy text: "Convection volume = substitution volume + net UF volume"
Two small labels under the two right-hand terms, each with a thin pointer:
- under "substitution volume": "Filtered out, then given back" (green #2E6B3E small droplet icon)
- under "net UF volume": "Filtered out, not replaced" (navy small droplet icon)

SEQUENCE ROW (four equal cards in one horizontal row on a soft gray panel #f3f4f6, joined by bold navy right-pointing arrows). Each card has a colored top band, a short heading, and two or three large worked lines.

Card 1 — teal band #1a6b72, white heading: "Set the pace"
  "Target 23 L in 240 min"
  "23,000 mL ÷ 240 min ≈ 96 mL/min"
  Small gray note: "Convective flow needed"

Card 2 — teal band #1a6b72: "Compare with blood flow"
  "Blood flow 350 mL/min"
  "96 ÷ 350 ≈ 27%"
  Small boxed label under it: "Convective flow ÷ blood flow"

Card 3 — amber band #b8860b: "Weaker access"
  "Blood flow 300 mL/min, same 27%"
  "≈ 81 mL/min"
  "× 240 min ≈ 19.4 L"
  Small amber tag: "Below target"

Card 4 — clinical red band #b91c1c, white heading: "Weaker access and early end"
  "Session ends 20 min early"
  "≈ 17.8 L"
  Small red tag: "Further below target"

RIGHT-SIDE OR BELOW-ROW BOX (rounded, green #2E6B3E outline, white fill), a small clipboard icon:
  Heading: "Reading the session record"
  "Substitution 21.0 L + net UF 2.5 L"
  Bold: "= 23.5 L convection volume"

LEVERS STRIP (row of three pill-shaped chips, navy outline, small icons):
  "Effective blood flow: the biggest lever" (pump icon) · "Effective treatment time" (clock icon) · "Fraction the circuit tolerates" (filter icon)

BOTTOM STRIP (full width, soft gray #f3f4f6, two lines in navy, a small red caution icon before the second):
  "Blood flow and time, not the substitution setting alone, decide the volume"
  "Net UF follows fluid status. Never raise it to improve the number"
Small gray note at far right of the strip: "Each patient's target: physician's order"

COLORS: navy #0f1e2e text and arrows; teal #1a6b72 headings and first two bands; amber #b8860b caution; clinical red #b91c1c for the fourth band and the caution icon only; green #2E6B3E for substitution cues and the session-record box. Pale fills only. Numbers large and high-contrast.

FOOTER: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, outside every card.

DO NOT:
✗ No numbers other than those written above: 23, 240, 23,000, 96, 350, 27%, 300, 81, 19.4, 20, 17.8, 21.0, 2.5, 23.5.
✗ Do not round or change any value (keep "≈" where shown).
✗ Do not call the 27% "filtration fraction"; the label is exactly "Convective flow ÷ blood flow".
✗ No hematocrit, plasma flow, or plasma-based filtration-fraction formula.
✗ No net UF subtracted from substitution volume; the equation adds them.
✗ No suggestion to raise net UF, blood flow, or substitution to "hit" the target.
✗ No machine screens, alarm limits, needle gauges, or weights in kilograms.
✗ No circuit drawing; icons only.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render every label exactly as written in quotation marks above, spelled correctly, in Inter, with the mathematical symbols ÷, ×, ≈, = exactly as shown. Add no other text.
```

**QA after generation:**
□ Equation reads "Convection volume = substitution volume + net UF volume" (plus sign, not minus)
□ Card 1: 23,000 mL ÷ 240 min ≈ 96 mL/min
□ Card 2: 96 ÷ 350 ≈ 27%, labeled "Convective flow ÷ blood flow" (not "filtration fraction")
□ Card 3: 300 mL/min, ≈ 81 mL/min, ≈ 19.4 L, "Below target"
□ Card 4: 20 min early, ≈ 17.8 L
□ Session record: 21.0 L + 2.5 L = 23.5 L
□ No invented or rounded-off numbers; no hematocrit or plasma flow
□ "Never raise it to improve the number" present
□ Label spelling: convection, substitution, ultrafiltration abbreviation "UF" exactly
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-K — The HDF trials at a glance
- **File:** images/nephrology-nursing-13-hdf-trials.png
- **Placement:** Module 13 page, section `hdf-evidence` (What the trials show, and what they do not)
- **Job:** U/P — the learner sees why early trials looked neutral, why CONVINCE was different, and which findings are associations.
- **Governing skill:** williamriveromd-simple-figure (Scaffold E, reference card)
- **Canvas:** 1536 × 1152, 4:3
- **Alt text:** Six HDF studies compared: CONTRAST, Turkish, ESHOL, CONVINCE, and two pooled analyses, with patients, comparator, and result; volume link shown as association.
- **Caption:** The trials that delivered lower convection volumes found no overall survival difference; CONVINCE randomized only patients able to receive high volumes and found lower mortality. The link between higher achieved volume and better survival is an association, not proof.
- **Source of truth:** m13_x2.py `hdf-evidence` table and text. CONTRAST (2012): 714 patients; post-dilution online HDF versus low-flux HD; all-cause death no significant difference (hazard ratio 0.95; 95% CI 0.75 to 1.20); on-treatment: higher volumes, lower mortality; "required confirmation". Turkish online HDF study (2013): 782; versus high-flux HD; composite of death and nonfatal cardiovascular events no significant difference (event-free survival 77.6% versus 74.8%); mean filtration volume about 17.2 liters; post hoc above 17.4 liters better survival. ESHOL (2013): 906; high-efficiency post-dilution online HDF versus continued HD; all-cause death 30% lower (HR 0.70; 95% CI 0.53 to 0.92). CONVINCE (2023): 1,360 on high-flux HD for at least 3 months, all judged able to receive at least 23 liters; high-volume HDF versus continued high-flux HD; all-cause death 17.3% (118 of 683) versus 21.9% (148 of 677), median 30 months, HR 0.77 (95% CI 0.65 to 0.93); mean delivered 25.3 liters. Pooled 2016 (peters2016): four trials, 2,793 participants; 14% lower all-cause death, 23% lower cardiovascular death; largest benefit above 23 liters per 1.73 m². Pooled 2024 (vernooij2024): five trials, 4,153 patients; all-cause death 23.3% HDF versus 27.0% HD, median 30 months, HR 0.84 (95% CI 0.74 to 0.95); lower risk with higher convection volume in a graded pattern. Text: post hoc and on-treatment analyses "show an association, not proof"; dose–response "drawn from volumes that patients achieved rather than volumes assigned at random, so it supports, but does not prove"; CONVINCE "addressed this directly by enrolling only patients able to receive high volumes and randomizing them".
- **Values left out (leanest version):** CONVINCE event counts (118 of 683, 148 of 677); Turkish 17.4-liter post hoc threshold; ESHOL secondary findings (fewer hypotensive sessions, fewer hospitalizations); CONVINCE quality-of-life results; the "required confirmation" wording.
- **Reviewer flags:** (1) Dense: six rows × four columns plus a footer band. If the hazard ratios or intervals come back garbled after two tries, use an HTML table (the page already has this table in HTML) and keep the image to the "Why results differed" band only. (2) The ESHOL comparator is "continued HD" (the text does not say low-flux or high-flux); the figure keeps that wording. (3) Pooled 2016 has no hazard ratio in the text, so only the percentages are shown.

```text
Clinical evidence reference card, 1536 × 1152 (4:3). Subject: randomized trials and pooled analyses comparing online hemodiafiltration (HDF) with hemodialysis (HD). Publication-grade table, white #ffffff background, flat design, no illustrations except tiny icons. Font: Inter throughout (never serif). Short lines; large enough to read on a phone.

TITLE BLOCK (top left):
- Title, bold navy #0f1e2e: "HDF versus HD: what the trials found"
- Subtitle, teal #1a6b72: "Outcome: death, unless stated"

TABLE (full width, rounded outer border, column headers in teal #1a6b72 on soft gray #f3f4f6, alternating white and very soft gray rows). Four columns: "Study" · "Patients and comparator" · "Result" · "Convection volume". Six rows:

Row 1: "CONTRAST (2012)" | "714 · vs low-flux HD" | "No significant difference" / "HR 0.95 (0.75–1.20)" | "Higher volume, lower mortality (on-treatment)"
Row 2: "Turkish online HDF study (2013)" | "782 · vs high-flux HD" | "Death or nonfatal cardiovascular event: no significant difference" / "Event-free 77.6% vs 74.8%" | "Mean about 17.2 L"
Row 3: "ESHOL (2013)" | "906 · vs continued HD" | "30% lower" / "HR 0.70 (0.53–0.92)" | "High-efficiency HDF"
Row 4 (highlighted with a thin teal left bar): "CONVINCE (2023)" | "1,360 · vs high-flux HD" / "All able to receive at least 23 L" | "17.3% vs 21.9% over median 30 months" / "HR 0.77 (0.65–0.93)" | "Mean 25.3 L delivered"
Row 5 (separated by a thin divider labeled "Pooled analyses"): "Pooled, 2016" | "4 trials · 2,793" | "14% lower death" / "23% lower cardiovascular death" | "Largest benefit above 23 L per 1.73 m²"
Row 6: "Pooled, 2024" | "5 trials · 4,153" | "23.3% vs 27.0% over median 30 months" / "HR 0.84 (0.74–0.95)" | "Graded: higher volume, lower risk"

Result cell styling: "No significant difference" cells in neutral gray-blue text #43536a; cells showing lower mortality in teal #1a6b72 bold. Percentages always written "HDF vs HD" order; add tiny gray header note above the Result column: "HDF vs HD".

LEGEND LINE (small gray, under the table): "HR = hazard ratio (95% confidence interval)"

WHY-RESULTS-DIFFERED BAND (full width, light teal fill #eef6f7, three boxes joined by navy arrows, small icons):
Box 1: "Neutral trials delivered lower volumes"
Box 2 (amber outline #b8860b, small "association" tag): "Higher achieved volume, better survival: an association, not proof"
Box 3 (teal outline): "CONVINCE randomized patients able to reach high volumes"
Under the band, one bold navy line: "Benefit shown for high-volume HDF, not for every patient or any volume"

FOOTER: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, outside the table.

DO NOT:
✗ No numbers other than those in quotation marks above; do not round, recompute, or convert any value.
✗ No word "proves", "proven", or "cause" applied to the volume finding.
✗ No "HDF benefits all patients" or "HD is unsafe" wording.
✗ No quality-of-life, hospitalization, or cost claims.
✗ No p-values, numbers needed to treat, or forest-plot drawing.
✗ No journal names, author names, or logos.
✗ Do not change comparators: CONTRAST is low-flux HD; Turkish and CONVINCE are high-flux HD; ESHOL is "continued HD".
✗ No country flags or maps.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render every label exactly as written in quotation marks above, spelled correctly, in Inter, including the en dash in each interval and "m²" with a superscript 2. Add no other text.
```

**QA after generation:**
□ Six rows in order: CONTRAST, Turkish, ESHOL, CONVINCE, Pooled 2016, Pooled 2024
□ Sample sizes exact: 714, 782, 906, 1,360, 2,793, 4,153
□ Hazard ratios and intervals exact: 0.95 (0.75–1.20), 0.70 (0.53–0.92), 0.77 (0.65–0.93), 0.84 (0.74–0.95)
□ Percentages exact: 77.6 vs 74.8; 17.3 vs 21.9; 23.3 vs 27.0; 30%; 14%; 23%
□ Volumes exact: about 17.2 L; at least 23 L; 25.3 L; above 23 L per 1.73 m²
□ Comparators correct: low-flux (CONTRAST), high-flux (Turkish, CONVINCE), continued HD (ESHOL)
□ Volume–survival box says "an association, not proof"
□ No invented numbers, no QoL or hospitalization claims
□ Label spelling: hemodiafiltration abbreviations, cardiovascular, CONVINCE, ESHOL
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

### 13-L — HDF alarms: meaning, first check, escalate
- **File:** images/nephrology-nursing-13-hdf-alarms.png
- **Placement:** Module 13 page, section `hdf-session` (Running an HDF session: before, during, and after), beside the alarm table
- **Job:** A — the learner matches each HDF-specific alarm to its likely meaning, first nursing check, and the point at which to escalate.
- **Governing skill:** williamriveromd-algorithm-generator-skill (Style Mode C, house style)
- **Canvas:** 1024 × 1536, 2:3 portrait
- **Alt text:** Algorithm for six HDF alarms: transmembrane pressure, substitution fault, blood leak, conductivity, filtration fraction limit, failed ultrafilter test, with first checks and escalation.
- **Caption:** Find the cause before resetting any alarm, and never widen a limit to keep the session running. A blood leak or a failed ultrafilter test always goes to the charge nurse and the physician or technician.
- **Source of truth:** m13_x2.py `hdf-session` alarm table (six rows, wording condensed): transmembrane pressure high (too much filtration for the blood flow; hemoconcentration; fibers clotting / confirm actual blood flow — very negative arterial pressure means the pump is not filling; dark streaks or clots; kinks; reduce substitution rate as the protocol allows / recurs after correction, clotting visible, or protocol does not cover next step); substitution or infusion fault (line, pump segment, connection, or online fluid supply / kinks, clamps, secure connection, air, machine prompts / persists, air found, or contamination suspected); blood leak (blood on dialysate side, usually fiber rupture; more likely at high transmembrane pressures / stop as the machine directs; dialysate outflow pink or red / always: dialyzer changed per protocol, blood not returned unless protocol allows); conductivity (composition wrong; dialysate and substitution fluid both affected / concentrate containers, connections, match order; machine diverts fluid until corrected / does not correct, or fluid of uncertain composition received); filtration fraction limit (convective flow too high relative to blood flow / blood flow at ordered level, access delivering; reduce substitution as the protocol allows / target cannot be reached at a safe filtration fraction: report for prescription review); ultrafilter integrity test failed (barrier may be breached / do not start or continue HDF on that machine / always: technician and charge nurse; HD on another machine only by order). Rule: cause found before reset; limits never widened. Temperature: rigor treated as possible pyrogenic reaction or infection until shown otherwise — stop substitution, follow unit protocol, keep patient safe, notify the physician. Hemoconcentration signs: darkening venous blood, clots or foam in the venous drip chamber. No numbers.
- **Reviewer flags:** (1) The plan listed five alarms; the module table has six, so the ultrafilter integrity test is included. (2) The rigor banner comes from the "Temperature" bullet of `hdf-session`, not the alarm table. (3) Limits and permitted substitution-rate changes depend on the machine and protocol (module quiz flag); the figure shows reasoning only.

```text
Clinical algorithm flowchart, 1024 × 1536 portrait (2:3). Subject: alarms specific to online hemodiafiltration (HDF), each with meaning, first nursing check, and when to escalate. renalcarematters.com house style. White #ffffff background, clean vector, thin navy arrows, rounded rectangles, generous margins. Font: Inter throughout (never serif).

TITLE BLOCK (top):
- Title, bold navy #0f1e2e: "HDF alarm? Find the cause first"
- Subtitle, teal #1a6b72: "Meaning, first check, escalate"

TOP NODE (wide, light teal #eef6f7, navy text): "Look at the patient, the lines, and the alarm message"
Arrow down into a teal decision diamond: "Which alarm?" with arrows fanning to a 2-column × 3-row grid of six equal cards.

SIX CARDS (each: colored header band, then three short labeled lines "Means", "Check", "Escalate", with these sub-labels in small teal caps):

Card 1 — header pale amber #fdf3dd, amber #8a5a00 text: "Transmembrane pressure high"
  Means: "Too much filtration for the blood flow; clotting"
  Check: "Actual blood flow? Very negative arterial pressure" · "Dark streaks, clots, kinks" · "Lower substitution per protocol"
  Escalate: "Recurs, clotting seen, or beyond protocol"

Card 2 — header pale amber #fdf3dd: "Substitution or infusion fault"
  Means: "Line, pump segment, connection, or fluid supply"
  Check: "Kinks, clamps, secure connection" · "Air in line?" · "Follow machine prompts"
  Escalate: "Persists, air found, or contamination suspected"

Card 3 — header clinical red #b91c1c, white text: "Blood leak"
  Means: "Blood on the dialysate side, usually a fiber rupture"
  Check: "Stop as the machine directs" · "Dialysate outflow pink or red?"
  Escalate: "Always. Change dialyzer per protocol; return blood only if protocol allows"

Card 4 — header pale amber #fdf3dd: "Conductivity"
  Means: "Wrong composition; substitution fluid affected too"
  Check: "Concentrates and connections match the order" · "Machine diverts fluid until corrected"
  Escalate: "Does not correct, or uncertain fluid given"

Card 5 — header pale amber #fdf3dd: "Filtration fraction limit"
  Means: "Convective flow too high for the blood flow"
  Check: "Blood flow at ordered level? Access delivering?" · "Lower substitution per protocol"
  Escalate: "Target unreachable safely: report for prescription review"

Card 6 — header clinical red #b91c1c, white text: "Ultrafilter integrity test failed"
  Means: "Barrier for sterile fluid may be breached"
  Check: "Do not start or continue HDF on this machine"
  Escalate: "Always. Technician and charge nurse; HD elsewhere only by order"

RED BANNER (full width under the grid, white text on clinical red #b91c1c, small thermometer icon):
"Chills or rigor: possible pyrogenic reaction" and second line "Stop substitution, keep patient safe, notify physician"

RULES STRIP (soft gray #f3f4f6, two navy lines with small icons):
"Find the cause before resetting" · "Never widen limits to keep running"

ESCALATE NODE (bottom, amber outline #b8860b, light amber fill): "Unresolved: notify and escalate per protocol"
Small gray note under it: "Limits and settings: manufacturer and unit protocol"

COLORS: navy #0f1e2e text and arrows; teal #1a6b72 diamond, subtitle, and sub-labels; clinical red #b91c1c only for cards 3 and 6 headers and the rigor banner; amber for the other headers and escalate node. Pastel fills only. Card text at least 12 pt equivalent.

FOOTER: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, outside every node.

DO NOT:
✗ No numbers anywhere: no pressures, mmHg, percentages, flows, volumes, temperatures, or alarm limits.
✗ No step that resets, silences, or widens a limit before the cause is found.
✗ No "increase substitution", "increase ultrafiltration", or "give anticoagulant bolus" step.
✗ No suggestion that HDF may continue after a failed ultrafilter test.
✗ No suggestion that blood is routinely returned after a blood leak.
✗ No more than six alarm cards; no air-detector or venous-pressure cards.
✗ No machine screens with readable text; no brand names.
✗ No circuit drawing beyond tiny icons.
✗ No dark background, no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render every label exactly as written in quotation marks above, plus the sub-labels "Means", "Check", "Escalate", spelled correctly, in Inter. Add no other text.
```

**QA after generation:**
□ Six cards: transmembrane pressure high, substitution or infusion fault, blood leak, conductivity, filtration fraction limit, ultrafilter integrity test failed
□ Blood leak and failed ultrafilter test have red headers and "Always" escalation
□ Transmembrane card includes "Very negative arterial pressure" as the pump-not-filling clue
□ Filtration fraction card ends "report for prescription review"
□ Rigor banner present: stop substitution, notify physician
□ Rules strip and "notify and escalate per protocol" node present
□ No numbers of any kind
□ Label spelling: transmembrane, substitution, conductivity, ultrafilter, integrity, pyrogenic
□ White background; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy

---

## Hub — Competency progression

### H-3 — Four levels of competence, and one skill climbing them
- **File:** images/nephrology-nursing-competency-levels.png
- **Placement:** Hub page `academy/nephrology-nursing.html`, section `progression` (How competence builds from module to module), above the progression table
- **Job:** U/P — the learner sees the four course levels as a pyramid, what verifies each, and how one thread climbs from Module 1 to Module 9.
- **Governing skill:** williamriveromd-simple-figure (Scaffold B/C hybrid: pyramid plus step sequence)
- **Canvas:** 1792 × 1024, 16:9 landscape
- **Alt text:** Pyramid of four levels: Knows, Shows how, Does supervised, Does independent; clinical assessment thread rises from Module 1 to Module 9.
- **Caption:** Each level is verified by someone other than the learner, except Knows, which self-study can reach. Clinical assessment climbs from explaining fluid balance in Module 1 to completing treatment assessments independently, after sign-off, in Module 9.
- **Source of truth:** common.py `COMPETENCY_LEVELS`: K "Knows" — "Explains the reasoning and applies it to cases. Verified by the self-assessment and the nursing case."; S "Shows how" — "Demonstrates the skill in simulation, a skills station, or teach-back. Verified by an educator."; D "Does, supervised" — "Performs the task with real patients under direct supervision. Verified by preceptor observation."; I "Does, independent" — "Performs the task without direct supervision after preceptor sign-off under the unit's policy." Comment: "Levels follow Miller's pyramid; self-study alone never exceeds 'knows'." `COMPETENCY_THREADS["assessment"]` = "Clinical assessment and fluid status". m01_c.py, thread assessment: K "Explains how filtration, tubular reabsorption, and secretion keep fluid, electrolytes, and acid–base status stable…" (Self-assessment, Nursing case); S "Demonstrates standardized seated and standing blood pressure measurement…" (Skills station); D "Performs a focused renal assessment in priority order, assessing breathing first…" (Observed practice). m09_c.py, thread assessment: I "Completes and documents pre-, intra-, and post-treatment assessments for stable patients on routine sessions." (Observed practice, Record review). Hub section text: "from explaining fluid assessment in Module 1 to completing full treatment assessments on your own, after sign-off, in Module 9." Chip colors from the site CSS (`.nc-lv-K/S/D/I`, light theme): K #43536a on #eef1f5 (border #d5dbe4); S #8a5a00 on #fdf3dd (border #f1d899); D #13636a on #e3f2f1 (border #b6dcd9); I white on #1f3864.
- **Reviewer flags:** (1) Level names use the site's exact spelling with commas ("Does, supervised", "Does, independent"), not the plan's "Does supervised". (2) The four thread statements are shortened to fit; the shortened wording should be approved. (3) Module 4 also reaches "Does, independent" in this thread (hourly urine output and intake and output records), and Module 9 also has a supervised assessment item; the figure shows one path and does not say Module 9 is the first independent level. (4) The line "Higher levels need a verifier" is a synthesis of the "Verified by…" clauses and the course scope note.

```text
Clean education infographic, 1792 × 1024 landscape (16:9). Subject: the four competency levels of a nursing course, drawn as Miller's pyramid, with one example skill climbing the levels across modules. White #ffffff background, flat vector, rounded shapes, generous whitespace. Font: Inter throughout (never serif).

TITLE BLOCK (top left):
- Title, bold navy #0f1e2e: "How competence builds"
- Subtitle, teal #1a6b72: "Four levels, based on Miller's pyramid"

LEFT HALF — PYRAMID (four stacked horizontal tiers, widest at the bottom, each tier a flat trapezoid with a thin border; tier name centered in bold, a one-line meaning beside the tier on its right, and a small verifier tag at the far right of each row):

Tier 4 (top, smallest) — fill navy #1f3864, white text: "Does, independent"
  Meaning: "Performs without direct supervision after preceptor sign-off"
  Verifier tag: "Preceptor sign-off"
Tier 3 — fill #e3f2f1, text #13636a, border #b6dcd9: "Does, supervised"
  Meaning: "Performs with real patients under direct supervision"
  Verifier tag: "Preceptor observation"
Tier 2 — fill #fdf3dd, text #8a5a00, border #f1d899: "Shows how"
  Meaning: "Demonstrates in simulation, skills station, or teach-back"
  Verifier tag: "Educator"
Tier 1 (bottom, widest) — fill #eef1f5, text #43536a, border #d5dbe4: "Knows"
  Meaning: "Explains the reasoning and applies it to cases"
  Verifier tag: "Self-assessment and nursing case"

A thin vertical bracket on the left edge of the pyramid, spanning only the bottom tier, labeled in small teal: "Self-study reaches here". A second bracket spanning the top three tiers labeled: "Needs a verifier".

RIGHT HALF — ONE THREAD CLIMBING (a rising staircase of four steps from lower left to upper right, joined by a teal #1a6b72 arrow that climbs step to step). Header above the staircase, bold navy: "Example thread: Clinical assessment and fluid status". Each step is a small rounded card whose left edge carries a level chip in the matching tier colors (same fills and text colors as the pyramid):

Step 1 (lowest) — chip "Knows" · "Module 1" · "Explains how the kidney keeps fluid and electrolytes stable"
Step 2 — chip "Shows how" · "Module 1" · "Demonstrates standardized blood pressure measurement"
Step 3 — chip "Does, supervised" · "Module 1" · "Performs a focused renal assessment in priority order"
Step 4 (highest) — chip "Does, independent" · "Module 9" · "Completes treatment assessments for stable patients"

BOTTOM STRIP (full width, soft gray #f3f4f6, bold navy centered text, a small checkmark-badge icon at left):
"Self-study reaches Knows. Higher levels need a verifier."

COLORS: navy #0f1e2e text; teal #1a6b72 subtitle, arrow, brackets; level colors exactly as specified and used ONLY for the four levels (gray-blue Knows, amber Shows how, teal Does supervised, navy Does independent). Everything else white or soft gray.

FOOTER: "© renalcarematters.com" bottom-right corner, small (about 11 px), navy #0f1e2e at 70% opacity, below the bottom strip's right end.

DO NOT:
✗ No fifth level, and no level names other than "Knows", "Shows how", "Does, supervised", "Does, independent".
✗ Do not reorder the tiers: Knows at the base, Does, independent at the apex.
✗ No percentages, scores, pass marks, hours, or dates.
✗ No module numbers other than 1 and 9.
✗ No other thread names and no grid or table of modules.
✗ No suggestion that a quiz or self-study alone certifies practice.
✗ No people photographs, faces, hospital logos, or certificates with readable text.
✗ No dark background (the only dark fill is the small top tier and its chip), no serif font, no cartoon style, no garbled or placeholder text.
✗ No missing or altered footer.

Render every label exactly as written in quotation marks above, spelled correctly, in Inter, including the commas in "Does, supervised" and "Does, independent". Add no other text.
```

**QA after generation:**
□ Four tiers bottom to top: Knows, Shows how, Does, supervised, Does, independent (commas present)
□ Tier colors match site chips: #43536a on #eef1f5; #8a5a00 on #fdf3dd; #13636a on #e3f2f1; white on #1f3864
□ Verifier tags: self-assessment and nursing case; educator; preceptor observation; preceptor sign-off
□ "Self-study reaches here" bracket covers the bottom tier only
□ Thread header reads "Example thread: Clinical assessment and fluid status"
□ Steps: Module 1 Knows, Module 1 Shows how, Module 1 Does supervised, Module 9 Does independent
□ Bottom strip exact: "Self-study reaches Knows. Higher levels need a verifier."
□ No invented numbers; only module numbers 1 and 9
□ White background apart from the navy top tier; Inter font only
□ Footer reads exactly "© renalcarematters.com", bottom right, small, semi-transparent navy


---

Prepared for renalcarematters.com. Figures are teaching aids for the self-study course; they do not replace orders, unit procedures, or manufacturer instructions. © renalcarematters.com
