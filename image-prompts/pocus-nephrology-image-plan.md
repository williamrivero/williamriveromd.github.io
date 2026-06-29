# Image Generation Plan — Point-of-Care Ultrasound in Nephrology
### `guides/pocus-nephrology.html` · williamriveromd.com · Clinician + Trainee guide · Reviewed June 2026

> **How to use:** Paste each `COPY-READY PROMPT` block directly into the [ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator). Generate every image, save each at the FILE NAME listed below into `/images/` (both `.png` and a WebP twin). The guide HTML already references these filenames — no markup changes are needed when the renders come back. After all are received, run `python3 patch_hero_fetchpriority.py --guide pocus-nephrology.html` (and the OG `<head>` width/height/alt lines are already in place).
>
> **House style:** williamriveromd.com nephrology clinician system — NAVY `#1F3864` (text/structure), TEAL `#1A6B72` (accents, decision diamonds), GREEN `#2E6B3E` (preferred path / restored state), AMBER `#C9A84C` (caveat / mismatch), RED `#C00000` (harm / severe), soft GOLD `#b8962e` (single accent line), soft warm-white background. All typography in **Inter** sans-serif. Every infographic carries the **© williamriveromd.com** attribution bottom-right (omitted on the hero vignette — it would be clipped by the circle).
>
> **Sonographic conventions** (apply to every figure that shows an ultrasound panel): grayscale B-mode only (no colored CT); anechoic fluid = black; hyperechoic structures (stone, calcification, ribs) cast **posterior acoustic shadows**; cysts/bladders demonstrate **posterior enhancement**; pleural reverberation = **horizontal A-lines**; ring-down = **vertical B-lines reaching the screen edge**; spectral Doppler waveforms drawn white on a dark Doppler field, baseline horizontal, time on the x-axis.

---

## Image Inventory

| # | Image | Where it lives | Archetype | Skill | Dimensions |
|---|---|---|---|---|---|
| 1 | Hero vignette | Hero `figure.hero-figure > .hero-vignette` | Circular vignette (hands + probe + soft anatomy overlay) | `williamriveromd-hero-vignette` (Scaffold A hybrid) | 1024 × 1024 |
| 2 | OG / Twitter share card | `<head>` meta (`og:image`, `twitter:image`) | Editorial OG share card with title | `williamriveromd-infographic-skill` | **1200 × 630** |
| 3 | F1 · Probe selection visual aid | §1 Foundations (optional inline figure) | Comparison figure — three probes mapped to nephrology jobs | `williamriveromd-simple-figure` | 1672 × 941 |
| 4 | **F2 ★ · Hydronephrosis POCUS grading** | §2 Renal & Bladder (top of body) | Grayscale US 3-panel + anatomy hybrid (FLAGSHIP) | `williamriveromd-infographic-skill` | 1672 × 941 |
| 5 | F3 · Bladder volume / PVR | §2 Renal & Bladder | Two-panel US + volume-formula visual aid | `williamriveromd-simple-figure` | 1672 × 941 |
| 6 | F4 · IVC → RAP assessment | §3 IVC & VEXUS (top of body) | US panel + three-tier table + confounder list | `williamriveromd-simple-figure` | 1672 × 941 |
| 7 | **F5 ★ · VEXUS 4-grade Doppler ladder** | §3 IVC & VEXUS | Doppler-waveform grid hybrid (FLAGSHIP) | `williamriveromd-infographic-skill` | 1672 × 941 |
| 8 | **F6 ★ · Lung B-lines & EVLW** | §4 Lung & Cardiac | A-lines vs B-lines US panels + 8/28-zone grid (FLAGSHIP) | `williamriveromd-infographic-skill` | 1672 × 941 |
| 9 | F7 · Focused cardiac windows | §4 Lung & Cardiac | Four-window comparison + targets | `williamriveromd-simple-figure` | 1672 × 941 |
| 10 | F8 · AV fistula rule of 6s | §5 Access & Procedures | Fistula anatomy + rule-of-6s callouts + complication panels | `williamriveromd-simple-figure` | 1672 × 941 |
| 11 | F9 · POCUS volume phenotypes | §6 Integration (top of body) | Clinical algorithm — five-point scan → phenotype → action | `williamriveromd-algorithm-generator-skill` | 1672 × 941 |

> Three of the figures are flagged **FLAGSHIP** — they carry the heaviest clinical signal and follow the Constitution v1.0 seven-layer architecture in full. The other six are simple-figure / algorithm-generator class.

---

## IMAGE 1 — Hero vignette

- **FILE NAME:** `pocus-nephrology-hero.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** Hero — `figure.hero-figure > .hero-vignette` (already wired)
- **ARCHETYPE:** Circular vignette — Filipino clinician's hands + curvilinear probe + soft anatomical thought-layer
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1024 × 1024 (1:1, square — displayed circle-cropped)

### COPY-READY PROMPT

```
Square 1:1 photorealistic editorial photograph for a medical hero image, composed to be cropped into a CIRCLE. A Filipino nephrologist's hands — mid-career, professional, wearing soft-white scrubs and a thin watch — holding a modern CURVILINEAR ultrasound probe (handheld, low-frequency abdominal transducer with a slim cable trailing softly out of frame) gently against the right flank of an out-of-frame patient covered by a warm, soft, light-teal clinical drape. The probe sits at the mid-axillary line in coronal orientation, just above where the right kidney would lie. Through the patient's drape, a SOFT, TRANSLUCENT, SEMI-PHOTOREAL anatomical overlay glows under the probe footprint — the silhouette of a single right kidney in coronal long-axis (convex border lateral, hilum medial), with a gentle hint of the inferior vena cava as a thin pale-blue vertical vessel just medial to the kidney, the way the structures would actually project onto a bedside scan. The overlay is restrained, almost watercolor — never garish, never a CT render — and reads as a clinician's anatomical "thought layer" rather than a baked-in graphic. Soft natural daylight from camera-left, gentle shallow depth of field, calm reassuring documentary mood, clean modern Philippine hospital surface visible in soft bokeh in the background. Compose the probe and the kidney overlay in the UPPER-MIDDLE of the frame (~42% from top), fully inside a centered circular safe zone — keep all four corners empty soft background, since the image will be masked to a circle. Background falls off into a slightly deeper light-teal/warm-neutral tone toward the edges. Light, airy, professional color grade harmonizing with clinical teal #1a6b72, navy #0f1e2e, and a soft gold accent on the probe trim. Absolutely NO text, NO title, NO captions, NO logo, NO watermark, NO graphic overlays beyond the soft anatomical thought-layer just described — a clean photograph only. Full-bleed, no borders or frames.
```

**Negative:** No text of any kind (no title, subtitle, captions, numbers, labels, on-screen ultrasound readouts/measurements, brand or machine names, logo, or williamriveromd.com watermark). No legible interface or B-mode image on a background monitor — keep any background screen as soft abstract light. No rectangular borders/frames/banners/UI. No important content in the corners. No dark, navy, charcoal, or black background. No CT-render colored anatomy and no neon/sci-fi glows — the overlay must read as calm clinical "thought layer," not 3D. Avoid cartoon style, distorted hands, implausible probe anatomy, or stocky staged poses.

---

## IMAGE 2 — OG / Twitter share card

- **FILE NAME:** `pocus-nephrology-og.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** `<head>` `og:image` / `twitter:image` (already wired)
- **ARCHETYPE:** Editorial typographic share card with subtle imagery
- **AUDIENCE:** Clinicians + trainees (visible in social previews and chat embeds)
- **DIMENSIONS:** **1200 × 630** (Open Graph standard)

### COPY-READY PROMPT

```
Educational medical OG share card, 1200×630 px landscape (Open Graph standard). A clean editorial composition for the williamriveromd.com nephrology guide "Point-of-Care Ultrasound in Nephrology — A Bedside Field Guide."

LAYOUT:
LEFT TWO-THIRDS — typographic block on a warm-white background.
- Small uppercase eyebrow line in Inter semibold, navy #1F3864: "WILLIAMRIVEROMD.COM · CLINICIAN GUIDE"
- Large bold title in Inter, navy: "Point-of-Care Ultrasound in Nephrology"
- Sub-title in Inter medium, navy with 80% opacity: "A bedside field guide — image → mechanism → action"
- Thin gold #b8962e horizontal accent line (~2 px) under the title block.
- Below the gold line, a single row of four small uppercase chips in teal #1A6B72, separated by middots: "RENAL & BLADDER · IVC & VEXUS · LUNG & CARDIAC · AV ACCESS"

RIGHT ONE-THIRD — subtle vector-style imagery on a faint cool-mint tint (#e1f5f0 at ~40% opacity):
- A simple line-art curvilinear ultrasound probe held at a 30° angle, drawn in navy outlines.
- Below the probe, a soft thin grayscale B-mode panel mock-up suggesting a coronal kidney in long-axis (anechoic central pelvis, brighter cortex outline) — non-photoreal, very light, almost watermark-like.
- A small set of three Doppler waveform glyphs stacked along the right edge in teal — a normal continuous wave, a biphasic, and a monophasic — labels NOT shown (purely graphic shorthand).

GLOBAL:
- Generous whitespace, restrained clinical mood.
- All typography in Inter sans-serif.
- Palette: warm white background, navy #1F3864 text, teal #1A6B72 chips and waveforms, soft gold #b8962e accent line, light cool-mint #e1f5f0 right-side wash.
- Small "© williamriveromd.com" line in light navy at the very bottom-right, ~12 px Inter regular.
```

**Negative:** No photorealism. No dark background. No serif typography (Inter only). No decorative gradients, neon glows, or 3D rendering. No machine brand marks. No gibberish or fake measurements on the B-mode panel — it must read as a soft graphic, not a real scan. No emojis. No additional logos beyond the © line.

---

## IMAGE 3 — F1 · Probe selection visual aid

- **FILE NAME:** `pocus-probe-selection-visual-aid-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §1 Foundations (optional inline figure — can be added in body or carried separately)
- **ARCHETYPE:** Three-probe comparison schematic with nephrology applications
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, ULTRASOUND PROBE COMPARISON DIAGRAM, 1672×941 px landscape 16:9. Subject: matching the three POCUS transducers to their nephrology applications, with the frequency-vs-penetration trade-off explicitly drawn.

LAYOUT:
TOP STRIP (10% of canvas) — navy thin band, uppercase Inter semibold, white text: "ULTRASOUND PROBES FOR NEPHROLOGY POCUS · MATCH THE TRANSDUCER TO THE QUESTION".

MAIN CANVAS — three vertical columns of equal width, each headed by a clean semi-photoreal vector rendering of one transducer (handle and footprint visible, slim cable trailing). The probes are drawn in soft navy / gunmetal with a teal accent stripe and a subtle gold tip detail.

COLUMN 1 — CURVILINEAR (2–5 MHz)
- Probe rendering top, label "CURVILINEAR (CONVEX) · 2–5 MHz" in Inter semibold navy.
- Below, three thumbnail use-cases in a vertical strip, each a tiny grayscale B-mode panel + caption:
  • Kidney long-axis (coronal): central echogenic sinus, cortex outer.
  • IVC long-axis: an anechoic vessel with a thin wall, sitting on the liver.
  • Bladder transverse: anechoic dome with posterior enhancement.
- Caption line below: "Workhorse — deep retroperitoneum, volume status."

COLUMN 2 — PHASED ARRAY (1–5 MHz)
- Probe rendering top, label "PHASED ARRAY · 1–5 MHz" in Inter semibold navy.
- Use-cases below:
  • PLAX cardiac window: parasternal long-axis silhouette.
  • A4C cardiac window.
  • Subcostal IVC reaching the RA.
- Caption: "Small footprint between ribs — focused echo + subcostal IVC."

COLUMN 3 — LINEAR (HIGH FREQUENCY) (7–12 MHz)
- Probe rendering top, label "LINEAR · 7–12 MHz" in Inter semibold navy.
- Use-cases below:
  • AV fistula short-axis: round anechoic lumen + thin wall + color flow tag (small red/blue swatch).
  • Internal jugular vein: anechoic compressible vessel adjacent to carotid (with a small "compressible ✓" annotation).
  • Subcutaneous vascular mapping: cephalic + basilic vein tracing.
- Caption: "Superficial high-resolution — AV access & vascular mapping."

BOTTOM STRIP (~18% of canvas) — frequency-vs-penetration trade-off curve:
- Horizontal axis labeled "FREQUENCY (MHz)" with markers at 2, 5, 7, 12.
- Vertical axis labeled "DEPTH OF PENETRATION (cm)" with markers at 5, 10, 15, 20.
- A single smooth decreasing teal line shows penetration falling as frequency rises.
- Three dots on the curve, color-keyed and labeled with their organ targets:
  • Navy dot at 3.5 MHz — "Kidney / IVC / Bladder ~ 15 cm"
  • Amber dot at 2.5 MHz — "Focused echo ~ 18 cm"
  • Teal dot at 10 MHz — "AV access / IJ ~ 4 cm"
- Below the curve, in small Inter italic: "Higher frequency = better resolution, less depth — pick the lowest frequency that resolves your target."

STYLE:
- Flat vector + soft semi-3D shading on the probe renderings.
- White background. Restrained palette: navy #1F3864 (structure/text), teal #1A6B72 (accents, curve), amber #C9A84C (caveat dot), soft gold #b8962e (decorative tip stripes), grayscale for all B-mode thumbnails.
- All typography in Inter sans-serif.
- Generous whitespace. Each column reads top-down independently.
- Small "© williamriveromd.com" in navy, bottom-right, Inter regular ~11 px.
```

**Negative:** No photorealism on the B-mode thumbnails — they should read as clean clinician illustrations, not photographs. No colored CT renders. No machine brand marks. No serif fonts. No decorative gradients or neon glows. No gibberish on axis labels — values must be real and consistent (kidney/IVC at 3.5 MHz, echo at 2.5 MHz, vascular at 10 MHz). No additional watermarks.

---

## IMAGE 4 — F2 ★ Hydronephrosis POCUS grading (FLAGSHIP)

- **FILE NAME:** `hydronephrosis-pocus-grading-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §2 Renal & Bladder (top of body)
- **ARCHETYPE:** Grayscale US 3-panel + paired anatomy hybrid
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, GRAYSCALE ULTRASOUND B-mode panels + anatomy hybrid, 1672×941 px landscape 16:9. Subject: POCUS grading of hydronephrosis (mild / moderate / severe) with matched anatomy, dual audience.

════ LAYER A — ANATOMICAL TRUTH BLOCK
Kidney: convex border LATERAL, hilum MEDIAL; renal pelvis funnel-shaped exiting MEDIAL hilum ONLY; calyces cup papillae and drain INWARD toward central pelvis; cortex outer 1–1.5 cm; medullary pyramids triangular, apex INWARD. Renal sinus = central echogenic fat. Right kidney lower than left. Ureter thin-walled, descends medially. Obstruction dilates pelvis/calyces first, then thins parenchyma.

════ LAYER B — SPATIAL ORIENTATION
Three ULTRASOUND panels left→right (Mild, Moderate, Severe), each paired with a small coronal anatomy inset above (convex LEFT, hilum RIGHT toward midline). Long-axis renal view; cortex peripheral, sinus central. Panel label band in navy at the top of each column.

════ LAYER C — RENDER SPECIFICATIONS
Mild: anechoic dilatation of pelvis and a FEW calyces, preserved cortical thickness (~1–1.5 cm).
Moderate: rounded/ballooned interconnected calyces ("bear-paw"), EARLY cortical thinning.
Severe: massively dilated anechoic calyces, MARKED cortical thinning.
Each panel labeled with the medical term + a plain-English note (e.g., "Dilated calyces (urine backed up)."). Include a measurement caliper on cortical thickness in each panel.
Bottom callout strip in teal: "Hydronephrosis = downstream obstruction → rising intratubular pressure → falling GFR; relieve to recover function."

════ LAYER D — IMAGING PHYSICS
ULTRASOUND: dilated collecting system ANECHOIC (black); cortex/sinus appropriately echogenic; if a stone is shown — HYPERECHOIC bright white + posterior ACOUSTIC SHADOWING. Cysts (if any) anechoic + posterior enhancement. Grayscale only. Depth scale bar on each panel.

════ LAYER E — NEGATIVE CONSTRAINTS
✗ No mirrored kidney  ✗ No hilum on convex border  ✗ No calyces pointing outward  ✗ No renal pelvis floating disconnected from hilum  ✗ No cartoon style  ✗ No garbled text  ✗ No prompt text visible in the rendered image  ✗ No stone shown without acoustic shadow  ✗ No colored CT renders  ✗ No cortical thinning in the Mild panel  ✗ No identical dilatation across all three panels  ✗ No anatomy "through opaque skin."

════ LAYER F — STYLE REFERENCE
References: Netter, Brenner & Rector, ACEP Sonoguide renal, POCUS Journal kidney review. Palette NAVY #1F3864 / TEAL #1A6B72 / ORANGE #C55A11 (severity emphasis only); grayscale US panels. Inter (DM Sans-equivalent) sans-serif typography throughout. White background. Watermark "© williamriveromd.com" bottom-right navy, ~11 px.

════ LAYER G — QA CHECKLIST
□ Three severity panels distinct  □ Kidney orientation correct (convex lateral, hilum medial)  □ Calyces drain inward  □ Dilated system anechoic  □ Cortical thinning progresses with grade  □ Any stone hyperechoic + posterior acoustic shadow  □ Grayscale US only  □ Caliper / measurement shown  □ Dual labels (medical + plain) present  □ No garbled text  □ No prompt text visible  □ Watermark present.
```

**Negative:** No colored CT renders, no cartoon style, no neon glow, no missing shadows on stones, no calyces drawn outward, no hilum on the convex border, no identical-looking panels, no fewer than 3 distinct grades, no serif fonts, no readable prompt text in the rendered image, no decorative borders/frames.

---

## IMAGE 5 — F3 · Bladder volume / PVR measurement

- **FILE NAME:** `bladder-pvr-measurement-visual-aid-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §2 Renal & Bladder
- **ARCHETYPE:** Two-panel B-mode + volume formula visual aid
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, ULTRASOUND B-mode panels + diagram, 1672×941 px landscape 16:9. Subject: suprapubic bladder POCUS — transverse + sagittal acquisition, three-dimension volume formula, PVR thresholds, and the AKI-decision crossover.

LAYOUT:
TOP STRIP — navy band, uppercase Inter semibold, white: "POCUS — BLADDER VOLUME & POST-VOID RESIDUAL".

MAIN CANVAS — split into THREE vertical columns:

COLUMN 1 (left, ~28%) — TRANSVERSE B-mode panel.
- Suprapubic transverse view: a single anechoic dome (the bladder), bright echogenic posterior wall with subtle posterior enhancement, dark prostate shadow below in a male schematic (or uterus shadow in a female schematic — render the male variant).
- Two measurement calipers drawn across the bladder: a horizontal AP diameter (W) and a vertical transverse diameter (T), each marked with crosshairs and a dotted measurement line.
- Caption below: "TRANSVERSE — measure Width (W) and Transverse (T)."

COLUMN 2 (center, ~28%) — SAGITTAL B-mode panel.
- Sagittal view: bladder anechoic, oval long-axis; symphysis pubis casting a small acoustic shadow at the cranial edge; rectum a faint posterior shadow.
- One measurement caliper: a craniocaudal Height/Depth (H or D) diameter.
- Caption below: "SAGITTAL — measure Height (H)."

COLUMN 3 (right, ~44%) — FORMULA + THRESHOLD CARD.
- Top: an elegant Inter equation card on a soft teal-tinted background:
   "Bladder Volume (mL) ≈ 0.52 × W × T × H"
- Below the formula, an annotated diagram of an ellipsoid in light teal with the three orthogonal axes labeled (W along x, T along y, H along z), reinforcing the formula.
- Below the diagram, a clean thresholds table on white:
   "Normal PVR <50 mL (<65 y)"
   "Normal PVR <100 mL (≥65 y)"
   "High PVR → consider retention → catheterize FIRST"
- Bottom callout strip in amber: "A high PVR reframes 'renal failure' as post-renal / retention. Decompress before pursuing intrinsic causes."

GLOBAL STYLE:
- Grayscale US panels in columns 1–2. Restrained clinical illustration in column 3.
- Palette: navy #1F3864 (text/structure), teal #1A6B72 (formula card, ellipsoid axes), amber #C9A84C (decision callout). White background.
- All typography in Inter sans-serif.
- Depth scale bar on each US panel.
- Small navy "© williamriveromd.com" at bottom-right.
```

**Negative:** No colored CT renders. No cartoon style. No fake decimal volumes. No measurement calipers on the wrong axis (W and T must be in the transverse panel; H must be in the sagittal panel). No formula errors — must read exactly 0.52 × W × T × H. No serif fonts. No readable prompt text.

---

## IMAGE 6 — F4 · IVC → RAP assessment

- **FILE NAME:** `ivc-rap-assessment-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §3 IVC & VEXUS (top of body)
- **ARCHETYPE:** US panel + three-tier RAP table + confounder list
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, ULTRASOUND IVC long-axis schematic + RAP table, 1672×941 px landscape 16:9. Subject: IVC diameter and respiratory collapse → estimated RAP, the three-tier ranges, and the confounder list.

LAYOUT:
TOP STRIP — navy thin band, uppercase Inter semibold, white text: "IVC ASSESSMENT — RIGHT ATRIAL PRESSURE ESTIMATE".

MAIN CANVAS — left half (~55%): a single large grayscale subcostal/subxiphoid US panel.
- Anatomy: the IVC drawn anechoic in long axis, walls thin/echogenic, entering the right atrium superiorly. The hepatic vein joins the IVC just caudal to the cavo-atrial junction (clearly labeled).
- A measurement caliper bracket sits 2–3 cm CAUDAL to the IVC–hepatic vein confluence with a calibrated "2.1 cm" dotted line annotation. A small respirophasic arrow shows the IVC narrowing during a sniff inspiration (a thin dashed silhouette overlaid on the IVC indicating ~50% collapse).
- Tiny annotation: "Measure 2–3 cm caudal to cavo-atrial junction, long axis."
- Depth scale bar on the right edge of the panel.

RIGHT HALF (~45%) — vertical stack of three threshold cards in a single column:
Card 1 — GREEN tint, Inter semibold:
   "≤ 2.1 cm + > 50% collapse  →  RAP ~ 3 mmHg (0–5) — NORMAL"
Card 2 — AMBER tint:
   "Intermediate pattern  →  RAP ~ 8 mmHg — INTEGRATE WITH OTHER WINDOWS"
Card 3 — RED tint:
   "> 2.1 cm + < 50% collapse  →  RAP ~ 15 mmHg — PLETHORIC IVC"

Below the three cards, a CONFOUNDER LIST card on a navy/blue tint with white text:
   "Confounders — read IVC as a gate, not the whole story:
   • Mechanical ventilation (positive pleural pressure inverts variation)
   • Raised intra-abdominal pressure
   • Pulmonary hypertension
   • Athletic physiology
   • Severe tricuspid regurgitation"

BOTTOM STRIP — narrow teal band with white Inter italic: "If IVC ≥ 2 cm → proceed to VEXUS (Figure 5). If IVC < 2 cm → do NOT grade VEXUS."

GLOBAL STYLE:
- Grayscale US panel only on the left.
- Right-side cards in flat color: pale green #d3eede, pale amber #fff3d0, pale red #fde0e0, navy text on all.
- Confounder card: navy #1F3864 background, white Inter regular text.
- Palette: navy #1F3864, teal #1A6B72 (header/footer bands), green #2E6B3E (normal), amber #C9A84C (intermediate), red #C00000 (elevated). White background overall.
- All typography in Inter sans-serif.
- Small navy "© williamriveromd.com" at bottom-right, ~11 px.
```

**Negative:** No colored CT, no neon glows. The caliper line must be 2–3 cm CAUDAL to the confluence (never measured at the atrial junction). No tricuspid valve drawn in the IVC lumen. No serif fonts. No additional thresholds beyond the three published tiers. No readable prompt text.

---

## IMAGE 7 — F5 ★ VEXUS 4-grade Doppler ladder (FLAGSHIP)

- **FILE NAME:** `vexus-grading-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §3 IVC & VEXUS
- **ARCHETYPE:** Doppler-waveform grid hybrid (FLAGSHIP)
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, ULTRASOUND + Doppler waveform schematic, 1672×941 px landscape 16:9. Subject: the four-grade VEXUS (Venous Excess Ultrasound) venous-congestion ladder for nephrology, dual clinician/trainee audience.

════ LAYER A — ANATOMICAL TRUTH BLOCK
Inferior vena cava: large, thin-walled, BLUE, draining into right atrium; measured 2–3 cm caudal to the IVC–hepatic vein confluence. Hepatic vein joins IVC near the cavo-atrial junction. Portal vein within hepatoduodenal ligament. Intrarenal interlobar vein adjacent to interlobar artery within the renal sinus; kidney shown only as a small labeled orientation inset (≤12% of canvas area, labeled NOT TO SCALE): convex border LATERAL, hilum MEDIAL, calyces drain INWARD. Veins thin-walled, large caliber, BLUE — clearly distinct from thick-walled muscular arteries.

════ LAYER B — SPATIAL ORIENTATION
Four horizontal rows = Grade 0, 1, 2, 3 (top→bottom). Each row has three columns: Hepatic vein | Portal vein | Intrarenal vein Doppler tracing. Left margin: vertical IVC reference strip (Grade 0 IVC < 2 cm; Grades 1–3 IVC ≥ 2 cm, plethoric). Waveforms drawn on standard Doppler axis, baseline horizontal, time on x-axis.

════ LAYER C — RENDER SPECIFICATIONS
Row Grade 0 (No congestion, GREEN): IVC < 2 cm; hepatic S > D; portal pulsatility < 30%; renal continuous.
Row Grade 1 (Mild, AMBER): IVC ≥ 2 cm; hepatic S < D (S still antegrade); portal 30–49%; renal biphasic (S + D).
Row Grade 2 (Moderate, ORANGE): severe abnormality in EXACTLY ONE bed.
Row Grade 3 (Severe, RED): severe in ≥ 2 beds — hepatic S-wave REVERSAL; portal ≥ 50% pulsatility; renal monophasic D-only.
Each waveform labeled with the medical term + a plain-English note, e.g. "Hepatic S-reversal (blood backing up toward liver)."
Right-side callout box: "Higher grade = backward venous congestion → reduced kidney perfusion gradient → falling GFR; decongest and re-scan."
Color-code grades: green → amber → orange → red along the row eyebrow only.

════ LAYER D — IMAGING PHYSICS
Pulsed-wave Doppler tracings on a dark Doppler field where waveforms are shown; spectral waveforms WHITE on dark, with a clearly drawn horizontal baseline. If a grayscale B-mode IVC inset is shown: anechoic lumen black, vessel walls echogenic. No color CT. Doppler scale bar included.

════ LAYER E — NEGATIVE CONSTRAINTS
✗ No mirrored anatomy  ✗ No cartoon style  ✗ No garbled text  ✗ No prompt text visible in the rendered image  ✗ No thick-walled (artery-like) veins  ✗ No kidney shown full-size (inset ≤ 12% only)  ✗ No calyces pointing outward  ✗ No portal waveform drawn identical across all grades  ✗ No hepatic S-reversal placed in Grade 0/1  ✗ No CT colored  ✗ No grade colors out of order  ✗ No IVC < 2 cm paired with Grade 1–3.

════ LAYER F — STYLE REFERENCE
References: Nature Reviews Nephrology, CJASN VEXUS literature, Brenner & Rector. Palette: NAVY #1F3864, TEAL #1A6B72, ORANGE #C55A11, GREEN #2E6B3E, RED #C00000. Typography: Inter (DM Sans-equivalent) sans-serif for plain labels; Inter mono / DM Mono for medical terms. White background. Watermark "© williamriveromd.com" bottom-right navy, ~11 px.

════ LAYER G — QA CHECKLIST
□ Four grades present and correctly ordered  □ Grade 0 IVC < 2 cm; Grades 1–3 IVC ≥ 2 cm  □ Hepatic S > D normal; S-reversal only in severe  □ Portal pulsatility thresholds 30% / 50% labeled  □ Renal continuous → biphasic → monophasic progression  □ Grade 2 = one bed, Grade 3 = ≥ 2 beds  □ Veins thin-walled blue, not artery-like  □ Kidney inset ≤ 12%, labeled NOT TO SCALE  □ Dual clinician/plain labels present  □ No garbled text  □ Doppler waveforms on correct axis  □ Watermark present.
```

**Negative:** No colored CT, no cartoon. No portal waveform repeated identically across grades. No hepatic S-reversal placed at Grade 0 or 1. No kidney at full panel size. No grade colors out of order. No serif fonts. No readable prompt text. No drawings of an arterial wall on a venous vessel.

---

## IMAGE 8 — F6 ★ Lung A-lines vs B-lines & EVLW (FLAGSHIP)

- **FILE NAME:** `lung-blines-evlw-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §4 Lung & Cardiac
- **ARCHETYPE:** US panels + 8/28-zone grid hybrid (FLAGSHIP)
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, ULTRASOUND LUNG schematic, 1672×941 px landscape 16:9. Subject: A-lines vs B-lines and zone scoring for extravascular lung water in nephrology, dual audience.

════ LAYER A — ANATOMICAL TRUTH BLOCK
Chest wall layers top→deep: skin, two ribs (with posterior acoustic shadows) flanking an intercostal space, bright pleural line beneath/between ribs. "Bat sign" = two rib shadows + pleural line. Lung deep to pleura. No kidney needed; if a volume-status body map is used, kidney appears only as a small labeled inset ≤ 12% of canvas; no anatomy "through opaque skin."

════ LAYER B — SPATIAL ORIENTATION
LEFT HALF: two side-by-side US panels — "A-lines (dry)" vs "B-lines (wet)".
RIGHT HALF: anterior chest torso diagram with an 8-zone scanning grid (4 zones per hemithorax) and a small 28-zone reference inset.
Probe orientation marker shown on each US panel.

════ LAYER C — RENDER SPECIFICATIONS
A-line panel: horizontal repeating lines parallel to and equidistant below the pleural line (reverberation) = NORMAL aeration. Label: "A-lines — horizontal reverberation = aerated lung."
B-line panel: ≥ 3 vertical, laser-like hyperechoic lines arising from the pleural line, extending to the bottom of the screen, ERASING A-lines, moving with lung sliding = interstitial fluid (EVLW). Label: "B-lines — vertical ring-down = interstitial fluid."
Plain-English note on each panel (e.g., "B-lines = water in the lung's scaffolding.")
Scoring callout: "≥ 3 B-lines in a single intercostal field = positive zone; sum zones for congestion score; use to set dry weight and guide ultrafiltration."
Briefly indicate pleural-effusion sign in a small sub-callout (anechoic stripe above the diaphragm with "spine sign").

════ LAYER D — IMAGING PHYSICS
ULTRASOUND: pleural line bright (hyperechoic); ribs cast posterior acoustic SHADOW; A-lines = horizontal reverberation artifact; B-lines = vertical ring-down artifact, hyperechoic, reaching the screen edge. Grayscale only. Depth scale bar on each panel.

════ LAYER E — NEGATIVE CONSTRAINTS
✗ No cartoon style  ✗ No garbled text  ✗ No prompt text visible in the rendered image  ✗ No B-lines drawn horizontally  ✗ No A-lines drawn vertically  ✗ No B-lines that stop mid-screen (must reach the screen edge)  ✗ No ribs without acoustic shadow  ✗ No colored CT  ✗ No fewer than 3 B-lines in the "wet" panel  ✗ No anatomy "through opaque skin"  ✗ No mirrored zone grid  ✗ No missing pleural line.

════ LAYER F — STYLE REFERENCE
References: NephroPOCUS lung review, CJASN / Nature Reviews Nephrology lung-US, Brenner & Rector. Palette NAVY #1F3864 / TEAL #1A6B72 / ORANGE #C55A11 / RED #C00000 — used sparingly as accents on the zone grid only; the US panels themselves are pure grayscale. Inter sans-serif typography throughout. White background. Watermark "© williamriveromd.com" bottom-right navy, ~11 px.

════ LAYER G — QA CHECKLIST
□ Bat sign (2 rib shadows + pleural line) shown  □ A-lines horizontal, B-lines vertical  □ ≥ 3 B-lines reaching screen edge in wet panel  □ Pleural line present and bright  □ 8-zone grid (4 per side) correct  □ Scoring rule labeled  □ Grayscale US only  □ Dual labels present  □ Any kidney inset ≤ 12%, labeled  □ No garbled text  □ No prompt text visible  □ Watermark present.
```

**Negative:** No horizontal B-lines, no vertical A-lines, no B-lines that stop short of the screen edge, no fewer than three B-lines in the wet panel, no missing pleural line, no ribs without acoustic shadows. No colored CT, no cartoon style. No serif fonts. No readable prompt text.

---

## IMAGE 9 — F7 · Focused cardiac windows

- **FILE NAME:** `focused-cardiac-windows-visual-aid-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §4 Lung & Cardiac
- **ARCHETYPE:** Four-window comparison + target per window
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, FOCUSED CARDIAC POCUS, four-window comparison, 1672×941 px landscape 16:9. Subject: the four focused-echo windows used in nephrology bedside scans and the binary question each one answers.

LAYOUT:
TOP STRIP — navy band, uppercase Inter semibold, white text: "FOCUSED CARDIAC POCUS — FOUR WINDOWS, FOUR QUESTIONS".

MAIN CANVAS — a 2×2 grid of four equal panels:

PANEL 1 (top-left) — PLAX (Parasternal Long-Axis)
- Small torso silhouette inset (top-left of panel) showing the probe at the 3rd–4th left intercostal space, indicator pointing toward the patient's right shoulder. Probe orientation marker visible.
- Main panel: a clean grayscale B-mode PLAX view — LV chamber on the left of the screen, LA on the right, aortic valve, mitral valve, anterior RV in the near field, descending aorta as a small circle behind the LA.
- Label: "PLAX — LV function, AV/MV, pericardium."
- Sub-label: "Eyeball EF · pericardial effusion."

PANEL 2 (top-right) — PSAX (Parasternal Short-Axis, mid-papillary)
- Torso inset, probe rotated 90° clockwise from PLAX.
- Main panel: short-axis mid-papillary view — donut-shaped LV with two papillary muscles, crescentic RV at the top.
- Label: "PSAX — LV cavity geometry."
- Sub-label: "Regional wall motion · 'D-shaped' septum → RV pressure/volume overload."

PANEL 3 (bottom-left) — A4C (Apical 4-Chamber)
- Torso inset, probe at the apex, indicator toward the patient's left.
- Main panel: A4C view — LV and LA on the right of the screen, RV and RA on the left, tricuspid and mitral valves visible.
- Label: "A4C — all four chambers."
- Sub-label: "RV size vs LV (RV ≥ LV at base = abnormal) · atrial size."

PANEL 4 (bottom-right) — SUBCOSTAL
- Torso inset, probe at the subxiphoid space, indicator toward the patient's left.
- Main panel: subcostal four-chamber view + adjacent IVC long-axis sub-inset.
- Label: "Subcostal — rescue view + IVC for RAP."
- Sub-label: "Use when PLAX/A4C fail (COPD, post-op)."

GLOBAL STYLE:
- Each B-mode panel pure grayscale with a depth scale bar.
- Torso insets in light teal vector outline with a small navy probe icon.
- Palette: navy #1F3864 (text/structure), teal #1A6B72 (torso insets, panel header bars), grayscale (B-mode), soft red #b94343 (sub-label emphasis on overload finding).
- All typography in Inter sans-serif.
- Small navy "© williamriveromd.com" at bottom-right, ~11 px.
- Bottom strip — teal band, white italic: "Focused echo rules IN gross findings — it does NOT exclude regional wall motion abnormality, valvular disease, or HFpEF."
```

**Negative:** No colored CT renders. No machine brand marks. No cartoon style. No misplaced probe positions (PLAX must be parasternal long, PSAX rotated 90°, A4C at the apex, subcostal at the subxiphoid). No serif fonts. No readable prompt text. No fake EF numbers or measurements on the panels.

---

## IMAGE 10 — F8 · AV fistula rule of 6s

- **FILE NAME:** `av-fistula-rule-of-6s-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §5 Access & Procedures
- **ARCHETYPE:** Fistula anatomy + rule-of-6s callouts + complication mini-panels
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical infographic, AV FISTULA SCHEMATIC + complication panels, 1672×941 px landscape 16:9. Subject: a mature left-arm AV fistula with the rule-of-6s callouts and three complication mini-panels.

LAYOUT:
TOP STRIP — navy band, uppercase Inter semibold, white: "AV FISTULA POCUS — RULE OF 6s + COMPLICATIONS".

LEFT TWO-THIRDS — MAIN FISTULA SCHEMATIC
A semi-anatomical illustration of the left forearm in three-quarter view, soft skin tone. The brachial artery (deep red) gives off the radial artery; a radial-cephalic AVF (Brescia-Cimino style) is shown at the wrist with a clear anastomosis and a swollen mature cephalic vein (blue) coursing proximally up the forearm. The vein is shown in cross-section bulging slightly above the skin.
Four prominent callouts radiate from the fistula:
1. "FLOW > 600 mL/min" (teal) — with a small PW Doppler waveform glyph showing pulsatile arterial-style flow.
2. "DIAMETER ≥ 6 mm" (teal) — caliper across the vein cross-section.
3. "DEPTH ≤ 6 mm" (teal) — caliper from skin to vein wall.
4. "ASSESS AT ~ 6 WEEKS" (gold #b8962e) — small calendar icon.
A small downstream arrow shows the venous needle direction "AWAY from anastomosis" (Inter italic, small).

RIGHT ONE-THIRD — three vertical complication mini-panels stacked:
PANEL A — STENOSIS:
- Linear-probe US panel showing focal narrowing at the juxta-anastomotic segment with color-flow aliasing (a small color insert), and a PW Doppler velocity-ratio annotation "> 2:1 PSV ratio."
- Label: "Juxta-anastomotic stenosis — > 50% diameter reduction."

PANEL B — THROMBOSIS:
- Linear-probe panel: non-compressible lumen with echogenic intraluminal material; no color signal.
- Label: "Thrombosis — non-compressible, no flow."

PANEL C — PSEUDOANEURYSM:
- Linear-probe panel: saccular outpouching with yin-yang color flow inside and a feeding neck.
- Label: "Pseudoaneurysm — yin-yang sign with neck."

GLOBAL STYLE:
- Anatomical art in semi-3D vector with soft shading on the forearm.
- US complication panels grayscale + a small color-Doppler swatch where indicated.
- Palette: navy #1F3864 (text/structure), teal #1A6B72 (rule-of-6s callouts), gold #b8962e (timing callout), red #C00000 (severe), green #2E6B3E (normal flow reference). Skin in soft warm beige; vein blue, artery deep red. White background.
- All typography in Inter sans-serif.
- Small navy "© williamriveromd.com" at bottom-right, ~11 px.
- Bottom strip — teal italic: "Left arm preferred · venous needle points AWAY from anastomosis."
```

**Negative:** No cartoon style. No machine brand marks. No anatomical errors (artery is red, vein is blue; anastomosis is at the wrist for a Brescia-Cimino). No serif fonts. No readable prompt text. No additional complication panels beyond the three listed. No misplaced calipers — "Depth ≤ 6 mm" must be skin-to-vein, "Diameter ≥ 6 mm" must be vein-lumen.

---

## IMAGE 11 — F9 · POCUS volume phenotypes (five-point scan algorithm)

- **FILE NAME:** `pocus-volume-phenotypes-visual-aid-hybrid-v2.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §6 Integration (top of body)
- **ARCHETYPE:** Clinical algorithm — five-point scan flow → phenotype → action
- **AUDIENCE:** Clinicians + trainees
- **DIMENSIONS:** 1672 × 941 (16:9 landscape)

### COPY-READY PROMPT

```
Educational medical clinical algorithm, 1672×941 px landscape 16:9, in the style of an AHA/ACC ACLS algorithm card or a Kidney International decision algorithm. Subject: the integrated five-point POCUS scan → hemodynamic phenotype → guideline-anchored action.

LAYOUT:
TOP STRIP — navy band, uppercase Inter semibold, white: "INTEGRATED POCUS — FIVE-POINT SCAN → PHENOTYPE → ACTION".

ROW 1 (top, ~22% canvas height) — FIVE-POINT SCAN STRIP
Five equal-width cards left→right, each a small navy header + iconic vector glyph + one-line bedside finding:
  1. KIDNEY / BLADDER — coronal kidney + small bladder icon — "Hydronephrosis? PVR?"
  2. IVC — vertical IVC silhouette — "Diameter + collapse → RAP tier"
  3. LUNGS — chest + 8-zone grid icon — "B-line count per zone"
  4. CARDIAC — heart icon — "Eyeball EF · pericardial effusion · RV size"
  5. VEXUS — three stacked waveform glyphs — "Hepatic · Portal · Intrarenal (only if IVC ≥ 2 cm)"

Below row 1, a navy "↓ COMBINE" funnel arrow points downward.

ROW 2 (middle, ~52% canvas height) — FIVE PHENOTYPE PATHWAYS
A wide horizontal flow with five colored decision boxes left→right, each with a small POCUS-signature thumbnail row and a guideline-anchored action box below it:

A. CONGESTIVE NEPHROPATHY / CRS-1/2 (RED)
   Signature: plethoric IVC · VEXUS 2–3 · multi-zone B-lines · ± reduced LV.
   Action: "DECONGEST — loop ± UF; SGLT2i where indicated (KDIGO 2024 / ADA / ACC)."

B. CARDIORENAL w/ PUMP FAILURE (ORANGE)
   Signature: reduced LV · B-lines · high VEXUS · ± pericardial effusion.
   Action: "DECONGEST + neurohormonal therapy (ARNI / MRA / SGLT2i, ACC/AHA HF). Avoid reflex fluid bolus."

C. TRUE HYPOVOLEMIA / PRE-RENAL (GREEN)
   Signature: small collapsible IVC · dry lungs (A-pattern) · hyperdynamic LV ('kissing walls').
   Action: "VOLUME RESUSCITATE (balanced crystalloid); reassess dynamically."

D. OBSTRUCTIVE / POST-RENAL AKI (TEAL)
   Signature: hydronephrosis ± high PVR (full bladder).
   Action: "DECOMPRESS FIRST (Foley / nephrostomy). Then revisit the intrinsic workup."

E. TAMPONADE PHYSIOLOGY (DEEP RED, STAT)
   Signature: pericardial effusion + RA systolic / RV diastolic collapse + plethoric IVC.
   Action: "STAT PERICARDIOCENTESIS. Fluid is a bridge, not the treatment."

ROW 3 (bottom strip, ~10%) — UNIFYING TEACHING BAND (navy):
"The kidney lives between FORWARD perfusion and BACKWARD congestion — POCUS lets the clinician see both sides at the bedside and titrate to an objective, repeatable endpoint."

GLOBAL STYLE:
- Flat vector with soft semi-3D shading on the organ glyphs.
- Each phenotype column gets its own accent color band (RED #C00000 / ORANGE #C55A11 / GREEN #2E6B3E / TEAL #1A6B72 / DEEP RED for tamponade — used on the column eyebrow ONLY; the action box below stays on white).
- All typography in Inter sans-serif.
- White background overall.
- Generous whitespace; clear top-down reading order.
- Small navy "© williamriveromd.com" at bottom-right, ~11 px.
```

**Negative:** No colored CT. No cartoon. No more than five phenotypes (the columns are the canonical set). No tamponade action that reads "give fluids first." No serif fonts. No readable prompt text. No drug-brand names — class names only (loop, SGLT2i, ARNI, MRA). No additional guideline acronyms outside the cited set (KDIGO / ADA / ACC / AHA).

---

## Post-generation checklist

After all 11 images are produced and saved into `/images/` (with WebP twins):

1. **Hero** — confirm `pocus-nephrology-hero.png` is 1024×1024 and crops cleanly into the circle (no critical content in corners).
2. **OG** — confirm `pocus-nephrology-og.png` is 1200×630 with the title text legible at thumbnail size.
3. **In-body figures** — F1–F9 should each carry the © williamriveromd.com watermark and the QA-checklist constraints baked in.
4. **Run** `python3 patch_hero_fetchpriority.py --guide pocus-nephrology.html` after the hero file is in place.
5. **Run** `python3 patch_hero_fullwidth.py --guide pocus-nephrology.html && python3 patch_hero_maxwidth.py --guide pocus-nephrology.html` so the hero image renders at the intended size — and then re-check `python3 validate_hero_grid.py` to confirm the `<figure class="hero-figure">` class is intact (these scripts have been known to strip it; if so, restore the class manually).
6. **Refresh Latest strip** — `python3 generate_latest_guides.py` so the new OG image surfaces in the carousel.
7. **Optional** — once all figures are wired into the guide body, run `python3 patch_references_accordion.py --report` to confirm reference coverage is intact.

> **Authoring note.** The three FLAGSHIP prompts (F2, F5, F6) follow the Constitution v1.0 seven-layer architecture verbatim from the source blueprint. Any future edits to these prompts should preserve LAYERS A–G (anatomical truth, spatial orientation, render specifications, imaging physics, negative constraints, style reference, QA checklist).
