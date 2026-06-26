# Image Plan — `dry-weight-determination.html`
### Finding Your True Dry Weight — Why It Keeps Changing · williamriveromd.com

**Stage 1 prompt pack** for the new dual-mode guide *"Finding Your True Dry Weight."*
Each prompt below was authored with the correct house image skill and is ready to
paste into the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator).
Generate each at the stated size, save the PNG **and** a `.webp` twin to `images/`,
then optionally run Stage 2 (`williamriveromd-local-image-generator`) for manifests.

House rules applied to every prompt: **light background only** (navy/teal are
typography + accent, never a fill), the navy `#1F3864` / teal `#1A6B72` /
green `#2E6B3E` / amber `#C9A84C` / red `#C00000` palette, sans-serif type
(Inter / Nunito Sans / Manrope), mobile-readable labels, and — on every figure
*except the circular hero vignette* — the mandatory `williamriveromd.com`
attribution bottom-right.

> **On-image text is English only.** The guide's four-language toggle (EN / TL /
> CEB / KAP) lives in the HTML body and `<figcaption>`s, never inside the raster
> images. Insert each finished figure as a `<figure>` with a
> `<figcaption class="illus-caption">` (and `fig-desc` / `fig-abbrevs` for the
> lightbox) in its section.

> **Thesis to keep visible in every figure:** dry weight is a *moving target you
> triangulate*, not a single number a machine prints — and when the machine
> disagrees with the patient, **believe the patient.**

---

## Plan overview

| # | Placement | File | Skill | Type | Size | Priority |
|---|-----------|------|-------|------|------|----------|
| Hero | `.hero-vignette` (circular) | `dry-weight-determination-vignette-hero.png` | hero-vignette | Circular people scene | 1024×1024 | **Core** |
| OG | head `og:image` + inline banner | `dry-weight-determination-og.png` | infographic | Split-concept editorial banner | 1536×1024 | **Core** |
| A | §1 `#what-dry-weight` | `dry-weight-determination-01-two-compartment.png` | biomedical-mechanism-figure | Two-compartment refill mechanism | 1536×1024 | **Core** (conceptual anchor) |
| B | §2 `#triangulation` | `dry-weight-determination-02-triangulation.png` | simple-figure | Hub-and-spoke reliability diagram | 1536×1024 | **Core** (signature visual) |
| C | §3 `#bedside-signals` | `dry-weight-determination-03-bp-curves.png` | simple-figure | 3-panel intra-HD BP curves | 1536×1024 | **Core** |
| D | §5 `#probing-protocol` | `dry-weight-determination-04-probing-flowchart.png` | algorithm-generator | Vertical clinical flowchart | 1024×1536 | **Core** |

> Hero + OG are wired to the page (hero `<img>`, `og:image`/`twitter:image`).
> Figures A–D are the four blueprint placeholders already embedded in the body —
> generate them to replace the live `images/dry-weight-determination-0N-*.png`
> references. All are patient-mode figures with four-language captions; the
> clinician sections reuse the same evidence in prose.

---

## Hero vignette

*Skill: williamriveromd-hero-vignette*

**Target file:** `images/dry-weight-determination-vignette-hero.png` (+ `images/dry-weight-determination-vignette-hero.webp` twin)
**Size:** 1024 × 1024 (square 1:1, displayed circle-cropped) — set `width="1024" height="1024"` on the `<img>`
**Audience:** Mixed (patients + dialysis staff)
**Visual goal:** A calm hemodialysis patient on a clinic weighing scale mid-session, a nurse's hand checking a BP cuff — the human, reassuring center of "dry weight" (the patient, not the machine).

**ALT text to use in HTML:**
`Filipino hemodialysis patient calmly standing on a clinic weighing scale while a nurse checks a blood-pressure cuff in a bright dialysis unit`

```
FILE NAME: dry-weight-determination-vignette-hero.png
IMAGE TYPE: Circular vignette hero — Scaffold A people scene
ASPECT RATIO: 1:1 (square — displayed circle-cropped)
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: mixed (patients + dialysis staff)
VISUAL GOAL: A hemodialysis patient calmly standing on a clinic weighing scale, mid-session vibe, with a nurse's hand checking a blood-pressure cuff — the reassuring human center of "dry weight."

PROMPT:
Square 1:1 photorealistic editorial photograph for a medical hero image, composed to be cropped
into a CIRCLE. A calm, dignified Filipino hemodialysis patient (middle-aged, gentle expression,
in comfortable everyday clothes with one arm rolled up) standing quietly on a low clinical
weighing scale in a clean, bright modern Philippine dialysis unit, mid-treatment atmosphere with
softly blurred dialysis chairs and machines in the background. A Filipino nurse (in light teal
scrubs) leans in beside the patient, her caring hands gently securing and reading a blood-pressure
cuff on the patient's upper arm. Warm, trusting, reassuring documentary mood — the focus is the
human, not the equipment. Soft natural daylight, gentle shallow depth of field. Compose the
patient's face and the nurse's hands on the cuff in the UPPER-MIDDLE of the frame, fully inside a
centered circular safe zone — keep all four corners empty soft background, since the image will be
masked to a circle. Background falls off into a soft, slightly deeper light-teal/neutral tone
toward the edges. Light, airy, professional color grade harmonizing with clinical teal #1a6b72
and navy #0f1e2e accents on a light background. Absolutely NO text, NO title, NO captions, NO
numbers on the scale or monitor, NO logo, NO watermark, NO graphic overlays — a clean photograph
only. Full-bleed, no borders or frames.

NEGATIVE INSTRUCTIONS:
No text of any kind (no title, subtitle, captions, readable numbers on the scale/monitor/cuff,
labels, logo, or williamriveromd.com watermark). No infographic or UI elements. No rectangular
borders, frames, or banners. No important content in the corners (they get clipped by the circle).
No dark, navy, charcoal, or black background. Avoid cartoon style, clutter, over-saturation, HDR,
distorted hands/faces, implausible anatomy or equipment, or stocky staged poses.

QUALITY CHECK:
Square 1:1. Single clear subject (patient on scale + nurse's hands on BP cuff) centered in the
circular safe zone with empty soft corners. Faces/key detail in the upper-middle (~42% from top).
Light, calm, warm, trustworthy Filipino dialysis-unit context, publication-grade. Crops cleanly to
a circle with no text or subject lost at the edges.
```

---

## OG / hero banner

*Skill: williamriveromd-infographic-skill · Photorealistic editorial hero / OG share card*

**Notes**
- **Target file:** `images/dry-weight-determination-og.png` (also export `.webp`)
- **Size:** 1536 × 1024 px (landscape, ~3:2). Used as the 1200×630 OG card crop AND the inline hero banner — keep title, both scenes, and attribution inside a horizontally centered safe band (avoid the outer ~12% left/right and outer ~15% top/bottom so the 1.91:1 OG crop never clips key content).
- **og:image alt text:** `Editorial banner for "Finding Your True Dry Weight": on the left a bathroom scale showing a single number with a question mark; on the right a Filipino dialysis team reading many signals — blood-pressure cuff, a cramping calf, lungs with B-lines, a relative-blood-volume trend line, and a bioimpedance Body Composition Monitor — illustrating one number versus triangulated signals.`

```
FILE NAME: dry-weight-determination-og.png

IMAGE TYPE: Photorealistic editorial hero / OG social-share banner (split-concept poster)

ASPECT RATIO: 3:2 landscape

PIXEL DIMENSIONS: 1536 × 1024

AUDIENCE: Mixed — dialysis patients, families, and clinical staff

VISUAL GOAL: Convey in one glance that a true dry weight is not one measured number but a target you converge on by triangulating many imperfect signals — "one number vs. triangulated signals."

PROMPT:
A clean, premium landscape editorial banner for a nephrology patient-education guide, on a LIGHT background only (white #ffffff fading to a very light teal tint #eef6f7) — never any dark, navy, or charcoal fill. Publication-grade, calm, mobile-readable, with generous negative space. Split-concept composition divided by a soft vertical seam down the middle.

LEFT THIRD — "one number": a realistic modern flat bathroom-style digital scale shown at a gentle three-quarter angle on a clean light floor, its display showing a single large numeric readout with a prominent question mark beside it (render the display as "?? . ? kg ?"), implying the number is uncertain. A thin clinical-red #C00000 accent circles the lone number. Above it, a short label in clean sans-serif: "ONE NUMBER?".

RIGHT TWO-THIRDS — "triangulated signals": a bright, airy dialysis-unit scene with a small Filipino multidisciplinary renal team (a nephrologist and a dialysis nurse) calmly reading MULTIPLE signals around a seated dialysis patient. Arrange five clearly separated, labeled signal elements as semi-photorealistic 3D / clean infographic components connected by thin teal #1A6B72 converging arrows pointing toward a central typographic node reading "TRUE DRY WEIGHT":
  1. an automated blood-pressure cuff with a small reading, labeled "BLOOD PRESSURE";
  2. a patient's lower leg with a subtle muscle-tension highlight, labeled "CRAMPS / SYMPTOMS";
  3. a simplified pair of lungs showing faint vertical "B-line" streaks, labeled "LUNG B-LINES";
  4. a small monitor with a gently declining curve, labeled "RBV TREND";
  5. a bioimpedance Body Composition Monitor device with a printout, labeled "BIOIMPEDANCE (BCM) — TREND ONLY" tinted amber #C9A84C to signal caution.
Use green #2E6B3E accents for the converging/positive signal arrows and the central node, amber #C9A84C only on the BCM caution element, clinical-red #C00000 only on the left single-number warning. Navy #1F3864 and teal #1A6B72 are typography and accent colors ONLY — never background fills.

TITLE TEXT (top of banner, large bold sans-serif, navy #1F3864, mobile-readable): "Finding Your True Dry Weight". Optional smaller teal #1A6B72 kicker beneath it: "One number vs. many signals". All on-image text in English only, set in the Inter typeface (clean sans-serif), crisp and correctly spelled, no gibberish, no microtext.

Keep the title, both scenes, the central node, and all five labels inside a horizontally centered safe band so a 1.91:1 crop never clips them. Bright natural clinical lighting, natural Filipino skin texture, restrained realistic shadows, no moody studio lighting.

Bottom-right corner: small, legible, semi-transparent (about 70% opacity) dark-teal sans-serif attribution reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter for all on-image text — no serif fonts, no decorative or handwritten typefaces, no other typeface. Do not translate any label — English only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. The "one number vs. triangulated signals" contrast must read instantly. Background must be white / off-white / very light teal — never dark. Title "Finding Your True Dry Weight" spelled correctly. Copyright attribution williamriveromd.com visible in the bottom-right corner. All key content centered within the safe band for the 1200×630 OG crop.
```

---

## Image A — Two-compartment refill (§1 #what-dry-weight)

*Skill: williamriveromd-biomedical-mechanism-figure*

**Notes**
- Target file: `images/dry-weight-determination-01-two-compartment.png` (plus `.webp` companion)
- Size: 1536 × 1024 (3:2 landscape)
- Figure alt text: "Two-compartment fluid diagram: a large interstitial compartment refills a smaller intravascular blood-vessel compartment through a slow refill valve, while an ultrafiltration straw removes fluid from the intravascular side during dialysis. Plasma refill lags behind ultrafiltration, so intravascular volume drops faster than it can be replenished, leading to low blood pressure and cramps."
- On-image text: English only. Light background. Mobile-readable labels. `williamriveromd.com` attribution bottom-right.

```
Create a publication-grade biomedical mechanism schematic in a clean scientific review-article style. Flat vector illustration with soft semi-3D shading, generous whitespace, on a light (near-white, very pale gray) background. Landscape 3:2 composition, 1536 x 1024. Use clean sans-serif typography in Inter throughout (never a serif font). Restrained, muted clinical palette only: light gray-blue anatomy, navy (#1F3864) for primary labels and outlines, teal (#1A6B72) for fluid/water, soft red (#C00000) for the danger/crash outcome, pale pink for the pathology summary box. No photorealism, no dark background, no decorative effects, no cartoonish styling, no emoji. All text must be crisp, correctly spelled, and legible at mobile size.

TOPIC: Why dialysis patients crash above their dry weight and cramp below it — the plasma refill lag.

MAIN FIGURE — TWO CONNECTED FLUID COMPARTMENTS (center of frame):
Draw two transparent tank-like chambers side by side, both partly filled with teal water/fluid.
- LEFT: a LARGE rounded compartment, clearly the bigger of the two, labeled "INTERSTITIAL SPACE" with a small sub-label "(fluid around the cells — the body's reservoir)". Fill it generously with teal fluid.
- RIGHT: a SMALLER compartment shaped like a simplified blood vessel / vein segment (rounded tube with rounded ends), labeled "INTRAVASCULAR SPACE" with sub-label "(blood inside the vessels — what the heart & BP feel)". Fill it only partway, noticeably lower than the interstitial side.
- Connect the two chambers with a short horizontal pipe containing a small valve symbol. Label this connector "REFILL VALVE — plasma refill (SLOW)". Draw a teal arrow flowing LEFT to RIGHT through the valve, but render it as a THIN, dashed, slow trickle to signal a rate-limited, lagging flow. Add a small italic note beside it: "refill is the rate-limiting step".

ULTRAFILTRATION STRAW (right side, the driver of the problem):
From the top of the smaller INTRAVASCULAL (blood vessel) compartment, draw a "straw"/cannula tube angling up and out, with a BOLD teal arrow pulling fluid OUT and away from the intravascular side. Label it "ULTRAFILTRATION (UF) — fluid removed during dialysis". Make this outflow arrow visibly THICKER and faster-looking than the thin refill trickle, so the viewer instantly reads: water leaves the blood faster than the interstitium can refill it.

VISUALIZE THE LAG (the conceptual anchor — make it unmistakable):
- Show the intravascular fluid level as LOW and DROPPING, with a small downward arrow and a faint "previous level" dashed line above the current level to show how far it has fallen.
- Show the interstitial side still relatively FULL, with its trickle barely keeping up.
- Add a concise callout banner spanning above both chambers: "THE LAG: UF removes fluid faster than the interstitium can refill the blood → intravascular volume falls."
- Optional small inset tag near the vessel: "↓ blood volume".

BOTTOM SUMMARY FLOW (single horizontal chain of 3-4 boxes connected by navy arrows, review-article style):
Box 1 (navy outline): "Too-fast UF + slow refill lag"
→ Box 2 (navy outline): "Low intravascular volume"
→ Box 3 (pale pink pathology box, soft red text): "Low blood pressure · cramps · crashing"
Keep arrows clean and directional left-to-right.

A small explanatory strip at the very bottom in muted gray: "Above dry weight the vessels stay full; push UF too far or too fast and refill cannot keep up — that lag is why patients crash and cramp."

ATTRIBUTION: place small, semi-transparent navy text "williamriveromd.com" in the bottom-right corner, about 11px, not overlapping any figure element. This is the only mark — no other watermark or logo.

Keep the whole figure uncluttered, anatomically plausible (the vessel chamber simplified but recognizable), with short high-yield labels and arrows showing directionality. All on-image text in English only.
```

---

## Image B — Triangulation hub-and-spoke (§2 #triangulation)

*Skill: williamriveromd-simple-figure*

**Notes**
- **Target file:** `images/dry-weight-determination-02-triangulation.png` (+ `.webp` companion)
- **Size:** 1536 × 1024 (per request; clean landscape hub-and-spoke)
- **Audience:** mixed (patient + clinician)
- **Visual thesis:** dry weight is the *convergence* of six imperfect signals — no single one gets a veto; bioimpedance/BCM is the visibly weakest spoke.
- **Figure alt text:** "Hub-and-spoke triangulation diagram with DRY WEIGHT at the center and six labeled signal spokes — symptoms, blood pressure, physical exam, relative blood volume monitoring, lung ultrasound B-lines/IVC, and bioimpedance/BCM — each with a signal-strength reliability bar; lung ultrasound and blood pressure read as the strongest signals while bioimpedance is shown as the weakest, drawn as a dashed, de-emphasized spoke."

**Copy-paste prompt**

```
FILE NAME: dry-weight-determination-02-triangulation.png
IMAGE TYPE: Scaffold D — single one-panel conceptual diagram (hub-and-spoke / radial network)
ASPECT RATIO: 3:2 landscape
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Show that dry weight is found by triangulating six imperfect signals — none has a veto, and bioimpedance is the weakest spoke.

PROMPT:
Clean, journal-style medical education infographic, AJKD/NEJM graphical-abstract aesthetic. Light background only — pure white (#ffffff) with a very soft light-gray (#f3f4f6) radial wash behind the center. Landscape 1536 × 1024. All text in the Inter sans-serif typeface (no serif, no handwritten, no decorative fonts), bold for labels, mobile-readable at minimum 11pt equivalent.

Title at top center in bold navy (#0f1e2e): "Triangulating Dry Weight". One-line subtitle directly beneath in clinical teal (#1a6b72): "No single signal gets a veto — you converge on the answer".

CENTER: a single prominent rounded hub circle, navy (#0f1e2e) fill with white text, large bold label inside reading "DRY WEIGHT". A faint teal concentric ring or soft glow surrounds the hub to mark it as the convergence point.

SIX spokes radiate outward symmetrically (clock positions roughly 1, 3, 5, 7, 9, 11 o'clock), each a clean connecting line from the hub to a rounded rectangular signal card. Every signal card contains: a small simple line icon, a bold short signal name, a one-line plain descriptor, and a horizontal SEGMENTED SIGNAL-STRENGTH BAR (five small segments) where MORE FILLED segments = MORE reliable. Use color to encode reliability tier (green strong, teal/amber moderate, muted gray weak). Keep spokes radial and evenly spaced — no crossing lines, no spaghetti, generous whitespace.

The six spokes:
1. "Symptoms" — descriptor "cramps · dizziness · breathlessness" — reliability bar: MODERATE (3 of 5 filled), teal segments. Solid spoke.
2. "Blood Pressure" — descriptor "inter-dialytic & intra-HD" — reliability bar: STRONG (4 of 5 filled), renal green (#1f7a4d) segments. Solid bold spoke.
3. "Physical Exam" — descriptor "JVP · edema · crackles — cheap, fast" — reliability bar: MODERATE (3 of 5 filled), teal segments. Solid spoke.
4. "RBV Monitoring" — descriptor "relative blood volume — good trend tool" — reliability bar: GOOD (3 of 5 filled), teal/green segments. Solid spoke.
5. "Lung Ultrasound" — descriptor "B-lines / IVC — most sensitive" — reliability bar: HIGH (5 of 5 filled), renal green (#1f7a4d) segments. Solid bold spoke, slightly emphasized as the strongest.
6. "Bioimpedance / BCM" — descriptor "overhydration (OH) — trend only" — reliability bar: LOW (1 of 5 filled), muted gray segments. THIS SPOKE IS VISUALLY DE-EMPHASIZED: drawn as a thin DASHED line, the card outlined in dashed gray with a faded/lower-opacity fill, set slightly apart so it reads clearly as the weakest, least-trusted signal.

Below or beside the diagram, a small legend strip on soft gray (#f3f4f6): a filled segmented bar labeled "Signal strength — more filled = more reliable". Keep it compact and unobtrusive.

Bottom strip / takeaway line in navy: "Believe where the signals converge — not any single machine." Restrained navy / teal / renal-green / amber palette on light background; ample negative space; no clutter; no photoreal anatomy; flat clean vector style.

Bottom-right corner: "williamriveromd.com" in small semi-transparent navy text (~70% opacity, ~10–11px). English text only.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation, avoid crossing/tangled spokes. Do NOT make the bioimpedance spoke look strong or equal — it must read as the weakest, dashed, de-emphasized signal. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter — no other fonts, no serif fonts, no decorative or handwritten typefaces. No emoji. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com house style. Six clearly labeled spokes each with a readable signal-strength bar; lung ultrasound and blood pressure read strongest, bioimpedance clearly weakest (dashed, faded). Background must be white or soft light gray — never dark. Copyright attribution williamriveromd.com visible in the bottom-right corner.
```

---

## Image C — Three intra-HD BP curves (§3 #bedside-signals)

*Skill: williamriveromd-simple-figure*

**Notes**
- **Target file:** `images/dry-weight-determination-03-bp-curves.png` (+ `.webp` derivative)
- **Size:** 1536 × 1024 (landscape comparison panel, three charts side by side)
- **Section:** §3 — Bedside Signals You Can Read Without Machines (GREEN), anchor `#bedside-signals`
- **Figure alt text:** "Three side-by-side line charts of systolic blood pressure across a 4-hour hemodialysis session. Left (green, TOLERATED): blood pressure stays stable and level the whole session — the goal. Middle (red, LATE CRASH): blood pressure holds steady then drops sharply in the last hour, signalling ultrafiltration that is too aggressive or probing below the true dry weight. Right (amber, SUSTAINED HYPERTENSION): blood pressure runs high and stays high throughout, signalling the patient is sitting above their dry weight."
- Scaffold B (side-by-side comparison) extended from two panels to a three-panel chart comparison; on-image text is English only.

```
Clean clinical education figure, AJKD / NEJM graphical-abstract style, journal-quality line charts. Three labeled line charts arranged side by side in one horizontal row (a comparison panel), separated by thin soft-gray vertical dividers. Pure white (#ffffff) background. Landscape 1536 × 1024.

Title centered at top in bold navy (#0f1e2e), font Inter: "READING THE INTRA-DIALYSIS BP CURVE". Small clinical-teal (#1a6b72) subtitle beneath in Inter: "Systolic blood pressure across a 4-hour HD session". All on-image text in English only. Use only the sans-serif font Inter (or Manrope) throughout — never a serif font.

Every one of the three panels is an identical small line chart with the SAME axes: a horizontal x-axis labeled "Time into session" with light tick marks at 0h, 1h, 2h, 3h, 4h; a vertical y-axis labeled "Systolic BP (mmHg)" with light gridlines. Thin light-gray axis lines and faint gridlines, generous whitespace, no clutter. Each chart has a single bold trend line in its panel color, a small round end-marker, and a bold panel heading above it plus one short one-line interpretation caption below it.

PANEL 1 (left) — heading in renal green (#1f7a4d), bold: "TOLERATED". A renal-green (#1f7a4d) line that stays essentially flat and stable at a comfortable mid-level across the full 4 hours, with only gentle, minor variation. A small green check-circle icon near the heading. Caption below in navy: "BP stays level all session — this is the goal."

PANEL 2 (middle) — heading in clinical red (#b91c1c), bold: "LATE CRASH". A clinical-red (#b91c1c) line that holds steady and level through the first 2.5–3 hours, then drops sharply and steeply downward in the final hour to a low value; mark the steep late drop clearly. A small red warning-triangle icon near the heading. Caption below in navy: "Stable, then a sharp late fall — UF too aggressive or probing BELOW true dry weight."

PANEL 3 (right) — heading in amber/gold (#b8860b), bold: "SUSTAINED HYPERTENSION". An amber (#b8860b) line that sits HIGH near the top of the y-axis and stays high and nearly flat across the whole 4 hours, never coming down. A small amber up-arrow icon near the heading. Caption below in navy: "Runs high and stays high — patient sitting ABOVE dry weight."

Keep all three y-axes on the same visual scale so the three trajectories are directly comparable: the green line mid-band and stable, the red line starting mid-band then plunging late, the amber line pinned high throughout. Bold, clean, mobile-readable lines (≥3px) and labels (≥11pt equivalent). Calm, restrained palette: navy (#0f1e2e), teal (#1a6b72), green (#1f7a4d), amber (#b8860b), red (#b91c1c) on a light background. Ample negative space.

Bottom-right corner: "williamriveromd.com" in small semi-transparent navy text, about 70% opacity, not obscuring any chart.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation, avoid 3D bevels or drop shadows on the charts, avoid spaghetti multi-line tangles within a single panel (one trend line per panel only).
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com house style. Three charts share identical axes and scale for direct comparison. Background must be white or soft light gray — never dark. The williamriveromd.com attribution must be visible in the bottom-right corner.
```

---

## Image D — Probing-protocol flowchart (§5 #probing-protocol)

*Skill: williamriveromd-algorithm-generator-skill*

**Target file:** `images/dry-weight-determination-04-probing-flowchart.png` (+ `.webp`)
**Size:** 1024 × 1536 (portrait, vertical top-to-bottom flow)
**Style mode:** C — williamriveromd.com house-style clinical algorithm
**Figure alt text:** "Systematic dry-weight probing protocol flowchart: establish a baseline dry-weight estimate, then if blood pressure is high with overload signs probe down 0.2–0.5 kg per session while watching relative blood volume and symptoms, or if cramping or intradialytic hypotension occurs probe up 0.2–0.5 kg per session; a hard red safety stop caps ultrafiltration rate at 13 mL/kg/h, reassess after a set number of sessions, cross-check against a lung-ultrasound or BCM trend rather than a single value, then document and hand off."

```
Create a clean, publication-ready clinical algorithm flowchart in the williamriveromd.com house style, designed as a journal/AHA-style nephrology treatment algorithm. Portrait orientation, 1024 × 1536 pixels (vertical top-to-bottom flow). Use a bright white / very light off-white background, generous margins, strong negative space, and a centered, symmetrical layout. The diagram must look like a polished medical-guideline figure and be fully legible at both full size and thumbnail size on a mobile screen.

Typography: clean sans-serif set in Inter (never a serif font). Title in bold navy at the top; concise, readable text inside every node; short red branch labels beside decision arrows.

Color conventions (use exactly these):
- Navy #0f1e2e for the title, structural text, and main connector arrows
- Teal #1a6b72 for decision diamonds and process/action nodes and accents
- Green #1f7a4d for the final documentation/hand-off endpoint
- Amber #b8860b for caution / "probe-up" nodes
- Red #c00000 for the hard safety-stop box only (filled red banner, white text)
- Soft gray for the small loop-back "reassess" note and the side cross-check note

Title at top (two lines):
"Systematic Dry-Weight Probing Protocol"
small navy subtitle: "Converge on dry weight by small, monitored increments — never a single jump"

Render this top-to-bottom clinical logic with rounded rectangles for action/process steps, diamonds for decision points, and thin navy arrows:

1. START node (teal rounded rectangle, top center):
   "Establish baseline dry-weight estimate
   (clinical exam + blood pressure + IDWG pattern)"

   ↓ arrow down to

2. DECISION DIAMOND #1 (teal diamond):
   "BP high + signs of fluid overload?"
   - YES branch (red label "YES") goes to a teal action box:
     "PROBE DOWN
     ↓ 0.2–0.5 kg per session
     Watch relative blood volume (RBV) + symptoms"
   - NO branch (gray label "NO") flows down to Decision Diamond #2

3. DECISION DIAMOND #2 (teal diamond), centered below:
   "Cramping, intradialytic hypotension, or post-HD washout?"
   - YES branch (red label "YES") goes to an amber caution box:
     "PROBE UP
     ↑ 0.2–0.5 kg per session"
   - NO branch (gray label "NO") flows down to the Reassess step

   Both the "PROBE DOWN" box and the "PROBE UP" box feed their arrows down into the Reassess step.

4. HARD SAFETY-STOP BOX (solid red #c00000 banner with white bold text, placed prominently — spanning across, with a small warning triangle icon):
   "HARD SAFETY STOP — Ultrafiltration rate ceiling ≤ 13 mL/kg/h (Flythe).
   NEVER exceed, regardless of target weight."
   Position this so it visually gates the probing steps (a red horizontal stop band that both probe-down and probe-up paths must respect before continuing).

5. REASSESS / LOOP-BACK node (teal rounded rectangle):
   "Reassess after a defined number of sessions"
   Draw a thin gray curved loop-back arrow from this node returning UP to Decision Diamond #1, labeled in small gray text "Re-enter loop".

   ↓ arrow down to

6. CROSS-CHECK node (teal rounded rectangle, with a small soft-gray side note):
   "Cross-check against lung-ultrasound or BCM TREND
   — never a single value"

   ↓ arrow down to

7. END node (green rounded rectangle, bottom center):
   "Document & hand off"

Branch and arrow labels ("YES" in red, "NO" in gray) must be short and sit cleanly beside the arrows, never overlapping nodes. Maintain strict alignment, consistent node widths, consistent rounded corners, equal vertical spacing, and balanced left-right branching from the central trunk.

Design requirements:
- All on-image text in English only.
- No emoji, no photos, no photorealistic people, no cartoon styling, no 3D elements, no dark background, no heavy shadows, no decorative clutter.
- Only a single small warning-triangle line icon on the red safety-stop box is permitted; no other icons.
- Keep text concise and legible at thumbnail size.
- Make the final image look like a clean clinical-guideline / medical-journal figure suitable for a nephrology patient- and clinician-facing education guide.
- Include a small professional footer reading "© williamriveromd.com" positioned at the bottom-right corner in subtle medium-gray (#6b7280) medical-publication styling, not inside any node or overlapping any arrow, with adequate page-edge margin.
```

---

## After generation

1. Save each `*.png` to `images/` and create a `.webp` twin (the guide's
   `<picture>` blocks reference both).
2. The guide already references every path above; once the files exist they render
   automatically — no HTML edit needed for the inline figures.
3. Confirm the OG card crops cleanly to 1200×630 (key content sits in the centered
   safe band) and the hero crops cleanly to a circle (no text/subject at the edges).
4. (Optional) run `python3 build_companion_pdfs.py` is **not** needed here; instead
   run Stage 2 `williamriveromd-local-image-generator` if you want manifests.

*End of image plan.*
