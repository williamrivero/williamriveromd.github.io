# Image Generation Plan — Isolated Ultrafiltration, Sodium & UF Ramping
### `guides/iso-uf-sodium-uf-ramping.html` · williamriveromd.com · Clinician guide · Reviewed June 2026

> **How to use:** Paste each `COPY-READY PROMPT` block directly into the [ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator). Generate all four images, then save each at the FILE NAME listed below into `/images/` (both `.png` and a WebP twin). The guide HTML already references these filenames — no markup changes are needed when the renders come back.
>
> **House style:** williamriveromd.com nephrology clinician system — NAVY `#1F3864` (text/structure), TEAL `#1A6B72` (accents, decision diamonds), GREEN `#2E6B3E` (preferred path / restored state), AMBER `#C9A84C` (caveat / mismatch), RED `#C00000` (harm / de-selection), soft GOLD `#b8962e` (single accent line), soft warm-white background. All typography in **Inter** sans-serif. Every image carries the **© williamriveromd.com** attribution bottom-right (bottom-center for the hero vignette, where it gets clipped by the circle). Light backgrounds only.

---

## Image Inventory

| # | Image | Where it lives | Archetype | Skill | Dimensions |
|---|---|---|---|---|---|
| 1 | Hero vignette | Hero `.hero-figure > .hero-vignette` | Circular vignette still-life | `williamriveromd-hero-vignette` (Scaffold B) | 1024 × 1024 |
| 2 | Figure 1 — Refilling / osmolality / tone cascade | §1 (replaces `<!-- FIGURE 1 -->` placeholder) | Biomedical mechanism schematic | `williamriveromd-biomedical-mechanism-figure` | 1659 × 948 |
| 3 | Figure 2 — Patient-selection algorithm | §6 ★ Patient Selection (top of body) | Clinical algorithm (Style Mode C — house style) | `williamriveromd-algorithm-generator-skill` | 1659 × 948 |
| 4 | OG / Twitter share card | `<head>` meta (`og:image`, `twitter:image`) | OG share card (typographic editorial) | `williamriveromd-infographic-skill` | **1200 × 630** |
| 5 | Figure 3 — Sequential dialysis prescription | §2 Iso-UF (between operational notes and EAG) | Time-axis mechanism schematic | `williamriveromd-simple-figure` (Scaffold D) | 1659 × 948 |
| 6 | Figure 4 — Na & UF profile-shape catalogue | §4 UF Ramping (top of body) | Two-panel stacked line chart | `williamriveromd-simple-figure` (Scaffold D) | 1659 × 948 |
| 7 | Figure 5 — Comparative positioning matrix | §5 Comparison (top of body) | Single-panel 2-axis bubble matrix | `williamriveromd-simple-figure` (Scaffold D) | 1659 × 948 |

---

## IMAGE 1 — Hero vignette

- **FILE NAME:** `iso-uf-sodium-uf-ramping-hero.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** Hero — `figure.hero-figure > .hero-vignette` (already wired in the guide HTML)
- **ARCHETYPE:** Circular vignette still-life (Scaffold B — single object)
- **AUDIENCE:** Clinicians (IM / Nephrology / dialysis nurses)
- **DIMENSIONS:** 1024 × 1024 (1:1, square — displayed circle-cropped)

### COPY-READY PROMPT

```
Square 1:1 photorealistic still-life for a medical hero image, composed to be cropped into a CIRCLE. A single modern hemodialysis machine seen in a clean three-quarter view, centered on a soft, uncluttered light teal-tinted clinic-floor surface in a calm Philippine dialysis-unit ambient. The dialyzer (vertical hollow-fiber cartridge) is the visual heart of the composition — glowing softly from within with a warm-amber dialysate tone, and translucent fluid-circuit tubing curves gracefully out of it in soft photographic bokeh, suggesting movement without distracting from the machine. The machine's chassis is brushed off-white and pale teal, with a dark display panel that reads as a soft gradient of light (no legible interface, no text, no numbers, no waveforms). Gentle natural daylight from camera-left, shallow depth of field, restrained clinical palette of navy #1F3864, teal #1A6B72, soft gold #b8962e accents on the warm white background. Compose the dialyzer and the machine's silhouette in the UPPER-MIDDLE of the frame, fully inside a centered circular safe zone — keep all four corners empty, soft warm-white-to-light-teal background only, since the image will be masked to a circle. Soft falloff toward a slightly deeper teal-neutral tone at the rim. Calm, mechanism-aware, publication-grade mood — a clinician's reference object, not a sales rendering. Absolutely NO text, NO labels, NO interface readouts, NO brand marks, NO logo, NO watermark, NO graphic overlays, NO curves, NO charts, NO numbers — a clean photograph only. Full-bleed, no borders or frames.
```

**Negative:** No text of any kind (no title, subtitle, captions, numbers, percentages, labels, logo, machine brand or model name, or williamriveromd.com watermark). No legible interface readouts on the display panel — it must read as soft abstract light only. No graph/curve/waveform/annotation overlays. No rectangular borders, frames, or banners. No important content in the corners (they get clipped by the circle). No dark backgrounds. Avoid cartoon style, clutter, over-saturation, HDR, neon glows, sci-fi aesthetic, or busy patient activity in the background.

---

## IMAGE 2 — Figure 1 · Refilling / osmolality / tone cascade

- **FILE NAME:** `iso-uf-sodium-uf-ramping-refilling-cascade.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §1 Shared Physiology (replaces the `<!-- FIGURE 1 -->` placeholder; already wired)
- **ARCHETYPE:** Biomedical mechanism schematic (organ panel → magnified inset → bottom injury → intervention → benefit flow)
- **AUDIENCE:** Clinicians
- **DIMENSIONS:** 1659 × 948 (16:9 landscape)

### COPY-READY PROMPT

```
Create a publication-grade biomedical mechanism schematic in the style of a Kidney International review-article figure.

Topic: The refilling / osmolality / tone cascade — why blood pressure fails during fluid removal in hemodialysis, and which tool addresses which physiologic axis.

Disease context: Intradialytic hypotension (IDH) in maintenance hemodialysis patients.

Central mechanism: The four physiologic axes that govern hemodynamic stability during fluid removal — (1) plasma refilling vs UFR mismatch, (2) osmolar / tonicity collapse, (3) autonomic and vascular tone failure, (4) cardiac reserve limits — each addressed by a specific intervention from the iso-UF / sodium-ramping / UF-ramping toolkit, with cool dialysate and time/frequency optimization layered alongside.

LEFT PANEL — Organ-level circuit:
A clean schematic of the extracorporeal hemodialysis circuit drawn in flat vector with soft semi-3D shading. Show a simplified vertical hollow-fiber DIALYZER cross-section (parallel fibers in light gray-blue) at center-left, joined by an arterial line (deep red) entering from the bottom and a venous line (medium blue) returning at the top, closing the loop on a small simplified human silhouette to the far left (head and torso outline only, light gray-blue, no facial detail). Inside the silhouette show a small heart icon (muted red) and an implied vascular tree (a few medium blue and red branching lines into the periphery). Above the dialyzer, an amber DOWN-arrow labeled "UFR (set rate)" in Inter sans-serif. Below the dialyzer, a teal UP-arrow labeled "Plasma refilling (finite, falls over session)". Between them a small label: "Mismatch → falling relative blood volume → IDH". A dashed thin navy connector line points from the dialyzer membrane to the MAGNIFIED PANEL on the right.

CENTER / RIGHT PANEL — Magnified mechanism inset (dashed thin navy border):
Show a magnified capillary-level plasma → interstitium boundary as a thin vector vessel cross-section in light gray-blue. Inside the lumen, label "PLASMA" with three small circles representing urea/osmolytes (small amber dots) being drawn outward through the capillary wall toward the "INTERSTITIUM" label on the right; an arrow labeled "Diffusive osmolyte loss (conventional HD)" runs left-to-right in amber.

Concise callouts (Inter sans-serif, short, mechanism-first):
• ↓ plasma osmolality
• ↓ tonicity drive to vasoconstriction
• → intracellular water shift
• → impaired refilling
A small downstream label: "Blunted vasoconstrictor response" pointing to a small arteriole drawn nearby in muted red, slightly dilated.

A SUB-INSET in the top-right corner of the magnified panel (smaller dashed thin teal border) labeled "During Iso-UF": same vessel cross-section, but the amber osmolyte dots remain INSIDE the plasma, an arrow now labeled "No diffusive solute removal", and a green ✓ next to "Tonicity preserved → refilling intact → PVR maintained". Keep this sub-inset visually clearly subordinate to the main pathology inset.

BOTTOM SUMMARY FLOW — four parallel axes, left-to-right strip:
Each axis a thin horizontal three-cell strip: pale pink injury box → soft pale blue intervention box → soft pale green benefit box, connected by a thin right-arrow.

Axis 1 — Refilling vs UFR mismatch  →  UF ramping (descending profile)  →  UFR matched to refill curve
Axis 2 — Osmolar / tonicity collapse  →  Iso-UF · Na-balance-neutral ramping  →  Preserved tonicity & refilling
Axis 3 — Autonomic / vascular tone failure  →  Iso-UF (preserves PVR) · Cool dialysate  →  Maintained peripheral vascular resistance
Axis 4 — Cardiac reserve limits  →  ↑ time / ↑ frequency · Dry-weight reassessment  →  Preserved preload, lower mean UFR

Across all four axes, above the bottom strip, a thin navy band reads in small uppercase Inter: "FOUR PHYSIOLOGIC AXES · ONE TOOLKIT".

VISUAL STYLE:
- Flat vector illustration with soft semi-3D shading on the dialyzer fibers and the small heart.
- White background.
- Restrained clinical palette: light gray-blue for anatomy and circuit, navy #1F3864 for primary structural lines and labels, teal #1A6B72 for refilling / intact-tonicity arrows, amber #C9A84C for the osmolyte loss / mismatch arrows, soft red for the injury cells and the heart, green #2E6B3E ✓ marks and benefit boxes, pale pink for the injury boxes, pale blue for the intervention boxes.
- All typography in Inter sans-serif (medium and semibold weights). Labels short, high-yield, scientific.
- Thin dashed navy and teal connector borders around the magnified inset and sub-inset.
- Generous whitespace; nothing crowded.
- Small semi-transparent navy attribution "© williamriveromd.com" in the bottom-right corner, ~11px, not overlapping any figure element.
```

**Negative:** No photorealism. No dark or colored background — pure white only. No decorative gradients, glows, drop shadows beyond the soft anatomical shading, or 3D rendering. No serif typography (Inter only). No cartoon or stylized illustration. No machine brand marks. No gibberish or filler text on any label. No decorative icons unrelated to the mechanism. No overlapping callouts. No watermark other than the single © williamriveromd.com line.

---

## IMAGE 3 — Figure 2 · Patient-selection algorithm

- **FILE NAME:** `iso-uf-sodium-uf-ramping-selection-algorithm.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §6 ★ Patient Selection (top of body, before 7.1 high-yield phenotype list; already wired)
- **ARCHETYPE:** Clinical algorithm (williamriveromd.com Style Mode C — house style)
- **AUDIENCE:** Clinicians
- **DIMENSIONS:** 1659 × 948 (16:9 landscape)

### COPY-READY PROMPT

```
Create a clean publication-ready clinical algorithm flowchart in the williamriveromd.com house style. Use a bright white background, restrained navy and teal typography set in Inter (never a serif font), thin teal connector arrows, and generous margins. Landscape 16:9 layout, sized 1659 × 948 px. The layout should read as a polished nephrology-journal treatment algorithm a clinician would reference at the dialysis-unit handover.

Title at top-left in bold navy Inter: "Patient-selection algorithm — Iso-UF / Sodium / UF Ramping"
Subtitle directly under the title in smaller medium-gray Inter: "Five gating prerequisites → four-branch tool-to-phenotype matrix → three red de-selection nodes"

Use these color and shape conventions:
- Navy #1F3864 for title, body text, structural emphasis, and the frame.
- Teal #1A6B72 for decision diamonds and connector arrows.
- Green #2E6B3E rounded-rectangle nodes for the preferred path and the four matching-matrix endpoints.
- Amber #C9A84C rounded-rectangle "caveat" tags hanging below each endpoint.
- Red #C00000 rounded-rectangle STOP / de-selection nodes that branch out of the trunk.
- Soft medium-gray Inter for explanatory side notes.

Top-to-bottom-left clinical logic, with the gating sequence running down the left two-thirds and the matching matrix laid out across the right third in four parallel columns. Connector arrows thin and teal. Rounded corners. Consistent node widths inside each color class. Generous whitespace between nodes.

Content to render (use this layout exactly):

START NODE (navy outline, white fill, top-left):
"HD patient with recurrent intradialytic hypotension (IDH)"
↓
GATING PREREQUISITES — five teal decision diamonds stacked vertically, each with YES going down (green arrow) and NO branching right to a red stop-and-fix node:

Decision 1 (teal diamond): "Dry weight reassessed (clinical ± BIA / lung US)?"
  NO → red node: "Correct dry weight FIRST. Do not proceed."
  YES ↓

Decision 2 (teal diamond): "Treatment time / frequency optimized?"
  NO → red node: "Extend time or → 4×/week. Do not proceed."
  YES ↓

Decision 3 (teal diamond): "IDWG counselled & salt-restriction documented?"
  NO → amber node: "Counsel + recheck in 4 sessions."
  YES ↓

Decision 4 (teal diamond): "Cool dialysate 35.5°C trialled ≥4 sessions?"
  NO → amber node: "Trial cool dialysate first."
  YES ↓

Decision 5 (teal diamond): "Antihypertensive timing reviewed (long-acting agents off AM of HD)?"
  NO → amber node: "Adjust timing first."
  YES ↓

PASS NODE (green rounded rectangle): "All prerequisites met → enter matching matrix"

MATCHING MATRIX — four green rounded-rectangle endpoint columns laid out left-to-right across the right half/lower half of the canvas, each headed by a small teal phenotype label:

Column A — phenotype label (teal): "Osmolar-collapse–driven IDH; large solute shifts"
  ↓ endpoint (green): "Iso-UF (sequential UF → HD)"
  ↓ caveat (amber): "Adequacy trade-off; longer session"

Column B — phenotype label (teal): "Late-session IDH clustering; mean UFR already safe"
  ↓ endpoint (green): "Descending UF profile"
  ↓ caveat (amber): "Distribution ≠ dose — mean UFR must remain ≤ ceiling"

Column C — phenotype label (teal): "IDH-prone with TOLERABLE IDWG"
  ↓ endpoint (green): "Na-balance-neutral ramping ± UF profile"
  ↓ caveat (amber): "Strict net-zero Na; STOP if IDWG ↑ >0.5 kg or pre-HD SBP ↑ >10 mmHg over 4 sessions"

Column D — phenotype label (teal): "Frequent unpredictable IDH AND BVM-capable machine"
  ↓ endpoint (green): "BV-UFC biofeedback"
  ↓ caveat (amber): "Cost; evidence mixed"

A unifying ENDPOINT footer node (navy outline, white fill) below the four columns spans full width: "Define exact Rx parameters · monitoring plan · reassessment date 4–6 sessions"

DE-SELECTION SIDEBAR — a vertical column of three red rounded-rectangle STOP nodes anchored to the bottom-right, each prefixed with a small "DO NOT" header in white-on-red, connected back to the trunk by short dashed gray "exit" arrows:

Red stop 1: "High IDWG · interdialytic HTN · salt non-adherence → DO NOT use Na ramping"
Red stop 2: "Suspected under-dialysis or wrong dry weight → DO NOT cover with these techniques; fix the root cause"
Red stop 3: "Hemodynamically stable patient → No indication; do not initiate"

Section divider: a thin dashed teal horizontal line separates the gating-prerequisites block from the matching matrix and de-selection sidebar.

Design requirements:
- Rounded rectangles for actions and endpoints (uniform corner radius).
- Teal diamonds for decision points, with YES below and NO to the right.
- Consistent vertical spacing in the gating trunk; consistent column widths in the matching matrix.
- Thin teal connector arrows for the trunk and matrix; thin dashed gray arrows for de-selection exits.
- Crisp Inter sans-serif throughout — bold for titles and node headers, regular for body labels.
- No icons inside nodes. No photographs. No 3D effects. No drop shadows beyond a very subtle 1px lift on the green endpoint nodes. No dark background.
- All text legible at full size and at thumbnail. Concise per-node phrasing.
- Generous margins on all four sides.
- Include a small professional footer reading "© williamriveromd.com" positioned at the bottom-right corner in subtle gray medical-publication styling.

Make the diagram publication-grade and vector-like, with crisp typography, perfectly aligned nodes, consistent arrow lengths, balanced columns in the matrix, and generous margins.
```

**Negative:** No serif typography. No dark or colored background — pure white only. No cartoon styling. No photorealistic people. No decorative clutter or unrelated icons. No 3D rendering or heavy shadows. No filler text or gibberish. No watermark other than the single "© williamriveromd.com" footer.

---

## IMAGE 4 — OG / Twitter share card

- **FILE NAME:** `iso-uf-sodium-uf-ramping-og.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** `<head>` meta — `og:image` and `twitter:image` (already wired in the guide HTML with width/height/alt tags)
- **ARCHETYPE:** OG share card (typographic editorial)
- **AUDIENCE:** Clinicians (preview tile in Slack / iMessage / WhatsApp / LinkedIn / X)
- **DIMENSIONS:** **1200 × 630** (1.91:1 — fixed by the OG-card house rule; do not resize)

### COPY-READY PROMPT

```
Create a publication-grade Open Graph share card for the williamriveromd.com guide "Isolated Ultrafiltration, Sodium & UF Ramping — A clinician's selection & prescription guide." Landscape 1.91:1, exactly 1200 × 630 px. Soft warm-white background (#faf7f2 — never dark). Typography is the visual centerpiece; the card is editorial, calm, and confidently clinical.

LEFT TWO-THIRDS — typographic stack, left-aligned, generous left margin (~80 px):
• A small uppercase teal tag pill at the top reading "CLINICIAN GUIDE · HEMODIALYSIS PRESCRIPTION" in Inter SemiBold, 14 px, teal #1A6B72, letter-spacing 0.14 em.
• Below it, the main title in bold navy #1F3864 Inter Black, 56–60 px, tight line-height (1.1), set on two lines:
    Line 1: "Isolated Ultrafiltration, Sodium &"
    Line 2: "UF Ramping"
• Below the title, a thin soft-gold (#b8962e) horizontal accent line, ~120 px wide, 2 px thick.
• Subtitle directly under the accent line in medium-weight navy Inter, 22 px:
    "A clinician's selection & prescription guide"
• A second smaller subtitle line in medium-gray Inter Regular, 16 px:
    "Hemodynamic stabilization tools — not adequacy tools — for the IDH-prone HD patient subset."

RIGHT THIRD — visual motif, vertically centered, right-aligned with ~80 px right margin:
• A stylized vertical hemodialyzer silhouette in restrained navy #1F3864 line-art (thin 2 px strokes, no fill except a very pale teal tint #eef6f7 inside the housing). Parallel hollow-fiber lines inside the cartridge. No labels, no numbers, no machine brand marks.
• Behind the dialyzer, two thin curve overlays in soft teal #1A6B72 (1.5 px stroke) implying the central UFR / refill mechanism — one descending S-curve from upper-left to lower-right behind the dialyzer head, one ascending mirror curve from lower-left to upper-right behind the dialyzer base. Treat the curves as restrained editorial line decoration only — they do NOT carry labels or axis tick marks, and they sit far enough behind the dialyzer to read as a quiet background motif, not a chart.

BOTTOM STRIP — discreet author credit + URL, full-width, ~36 px from bottom edge:
• Left side: small Inter SemiBold, 14 px, navy #1F3864:
    "William Gregory Rivero, MD · FPCP · DPSN"
  with a smaller Inter Regular, 12 px, medium-gray subline directly under it:
    "Internal Medicine · Nephrology · Philippines"
• Right side, aligned to the right margin: small semi-transparent navy Inter Regular, 11 px, 70% opacity:
    "williamriveromd.com"

VISUAL STYLE:
- Soft warm-white background, fully light — never dark.
- All typography in Inter (Black / SemiBold / Medium / Regular). Never a serif font.
- Restrained palette: navy #1F3864 primary text and line-art, teal #1A6B72 tag pill + curve overlays, soft gold #b8962e single accent line, medium gray for the secondary subtitle.
- Generous whitespace; the layout reads instantly even at 600 × 315 small-preview size.
- No decorative gradients, glows, drop shadows, 3D effects, or photography.
- Crisp vector look — publication-grade editorial card aesthetic.
```

**Negative:** Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only (warm white #faf7f2). Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope. No machine brand marks, no axis tick marks, no chart numbers on the curve overlays. Never omit the williamriveromd.com attribution.

---

## IMAGE 5 — Figure 3 · Sequential dialysis prescription on a time axis

- **FILE NAME:** `iso-uf-sodium-uf-ramping-sequential-prescription.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §2 Iso-UF (between operational notes list and the Evidence-at-a-glance card; already wired)
- **ARCHETYPE:** Time-axis mechanism schematic (Scaffold D)
- **AUDIENCE:** Clinicians
- **DIMENSIONS:** 1659 × 948 (16:9 landscape)

### COPY-READY PROMPT

```
Medical pathophysiology infographic, AJKD/NEJM graphical abstract style. Pure white (#ffffff) background. Title at top in bold navy (#1F3864) Inter SemiBold: "Sequential dialysis — front-loaded iso-UF block followed by conventional HD". Subtitle directly under the title in medium-gray Inter Regular: "Two physiologic regimes, one session. Document the trade-off in the order."

Central panel — a single horizontal time axis labelled "Session time (min)" along the bottom edge, with tick marks at 0, 60, 120, 180, 240. The panel is divided into two STACKED horizontal regions that run across the full width and share the time axis:

UPPER REGION — "ISO-UF PHASE" (label set in teal #1A6B72 Inter Bold, top-left):
- Spans the first ~25% of the width (0–60 min), filled in a soft, low-saturation teal #1A6B72 at ~12% opacity so the type stays legible.
- Vertical hollow-fiber dialyzer icon (clean line-art, navy strokes) anchored at the left edge of this region; an amber #C9A84C DOWN arrow drawn inside the dialyzer labelled "UFR active (high)".
- Two short stacked labels inside the region in navy Inter Medium: "Dialysate flow: OFF" and "Diffusive clearance: NONE".
- A teal UP arrow above the dialyzer icon labelled in teal: "Plasma refilling intact — osmolality preserved".
- A subtle pill-shaped green #2E6B3E ✓ badge on the right side of the region, white text inside: "PVR preserved · IDH risk lowered".

LOWER REGION — "HD PHASE" (label set in navy #1F3864 Inter Bold, top-left):
- Spans the remaining ~75% of the width (60–240 min), filled in a soft light gray #f3f4f6.
- Same vertical hollow-fiber dialyzer icon at the left edge of this region; amber DOWN arrow drawn inside, smaller in scale than the upper one, labelled "UFR (tapered)".
- Two short stacked labels inside in navy Inter Medium: "Dialysate flow: ON (500 mL/min)" and "Diffusive clearance: full Kt/V dose delivered HERE".
- A thin navy right-pointing arrow inside the region labelled: "Convective + diffusive clearance simultaneous".

ABOVE both stacked regions, a thin teal #1A6B72 line plot for "Plasma osmolality" (label at the left end of the line in teal Inter Regular) that stays HIGH and FLAT across the iso-UF region, then slopes gently downward as it crosses into the HD region — the slope is subtle, not steep. A small inline italic note above the slope reads in medium gray: "preserved → progressively diluted".

BELOW both stacked regions, a thin amber #C9A84C line plot for "Cumulative UF removed (L)" (label at the left end in amber Inter Regular) that climbs STEEPLY during the iso-UF region (capturing the front-loaded UF removal), then continues at a noticeably gentler slope through the HD region, ending at the prescribed total UF at the right edge. A small inline note in medium gray near the inflection: "front-loaded → tapered". The y-axis label on this plot, in tiny medium-gray Inter Regular, reads "UF removed (L)".

RIGHT EDGE — a compact "Trade-off" callout card anchored to the right margin, vertically centered, with a 4 px amber #C9A84C left border, white fill, soft 1 px gray outer border, and rounded corners. Header inside the card in amber Inter Bold (small caps): "ADEQUACY TRADE-OFF". Three short bullet lines in navy Inter Regular:
• "Iso-UF block delivers ZERO clearance."
• "HD block must compensate — verify Kt/V ≥ 1.2."
• "Session may need extension if HD block is shortened."

BELOW THE PANEL, a thin compact key line in medium-gray Inter Regular, centered: "Front-load UF when refill reserve is highest → reserve the diffusive dose for the HD block. Document rationale + total time + achieved Kt/V."

Layout discipline: every label is short, mechanism-first, and mobile-readable (≥11 pt equivalent). Whitespace generous; no overlapping labels; the two stacked region fills clearly separable; the two trend lines clearly distinguishable by color and label position. The dialyzer icons inside the two regions match in style but differ in scale to suggest the relative UF intensity. Bottom-right corner: "williamriveromd.com" in small semi-transparent navy Inter Regular, ~11 px, 70 % opacity.
```

**Negative:** Avoid cartoon style, clutter, tiny labels, AI gibberish, dark backgrounds. No machine brand marks. No legible interface readouts on the dialyzer icons. No filler text. No 3D rendering or drop-shadow effects beyond the soft 1 px card border. Use only Inter / Nunito Sans / IBM Plex Sans / Manrope.

---

## IMAGE 6 — Figure 4 · Na & UF profile-shape catalogue

- **FILE NAME:** `iso-uf-sodium-uf-ramping-profile-catalogue.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §4 UF Ramping (top of body — also references §3 Na Ramping; already wired)
- **ARCHETYPE:** Two-panel stacked mechanism poster (Scaffold D)
- **AUDIENCE:** Clinicians
- **DIMENSIONS:** 1659 × 948 (16:9 landscape)

### COPY-READY PROMPT

```
Medical pathophysiology infographic, AJKD/NEJM graphical abstract style. Pure white (#ffffff) background. Title at top in bold navy (#1F3864) Inter SemiBold: "Profile-shape catalogue — sodium and ultrafiltration". Subtitle directly under the title in medium-gray Inter Regular: "Distribution, not dose. The operative variables: TIME-AVERAGED dialysate Na and MEAN UFR — not the bookend values."

The canvas is divided into two stacked horizontal panels by a thin soft-gray (#e2e6eb) divider line. Each panel is a clean line-chart with its own axes, but the two panels share the same x-axis convention (session time, 0 → 240 min) for cognitive alignment.

═══ TOP PANEL — "Dialysate sodium profiles" (Inter Bold, navy panel label, top-left) ═══
Line chart with:
- X-axis: "Session time (min)" — tick marks 0, 60, 120, 180, 240, in navy Inter Regular.
- Y-axis: "Dialysate Na (mEq/L)" — tick marks at 134, 140, 146, 152, 158, in navy Inter Regular.
Four overlaid profile traces, each with distinct color AND distinct stroke style:
  1. Step (navy #1F3864 solid line, 2 px) — starts at 155, holds flat to minute 80, drops to 145, holds to minute 160, drops to 138.
  2. Linear descending (teal #1A6B72 solid line, 2 px) — starts at 152, falls in a straight line to 137 by minute 240.
  3. Exponential (amber #C9A84C dashed line, 2 px) — starts at 158, decays steeply early and plateaus near 137 by minute 180.
  4. Ascending–descending A/D (purple #6c3d8e dash-dot line, 2 px) — starts at 142, rises to 152 at minute 100, falls to 137 at minute 240.
A horizontal DASHED REFERENCE LINE in medium gray at y=138, labelled at its right end in medium-gray Inter Regular: "Pre-HD plasma Na (138) — the anchor".
A pale TEAL-tinted shaded band (≈±1 mEq/L wide) hugs the linear-descending trace, labelled inside in teal Inter Regular Italic: "Time-averaged Na (operative variable)".
Below the chart, a small navy-bordered callout card with white fill, Inter Regular navy text: "Net diffusive Na ≈ time-averaged dialysate Na − pre-HD plasma Na. Aim: net-neutral. A profile that LOOKS aggressive can still be net-zero if its time-average lands on the anchor."
Bottom-right corner of this panel: a small rounded RED (#C00000) pill, white Inter SemiBold text inside, ~12 px: "Non-neutral profile = sodium loading → IDWG ↑ → masked volume overload".
A small inline LEGEND in the upper-right corner of the panel: four short rows, each showing the trace's stroke style, color swatch, and short name (Step / Linear / Exponential / A/D), in Inter Regular navy.

═══ BOTTOM PANEL — "Ultrafiltration profiles vs the refill curve" (Inter Bold, navy panel label, top-left) ═══
Line chart with:
- X-axis: "Session time (min)" — tick marks 0, 60, 120, 180, 240, in navy.
- Y-axis (left): "UFR (mL/hr)" in navy Inter Regular.
- Secondary Y-axis (right): "Plasma refill rate (mL/min)" in teal Inter Regular.
Background reference curve drawn FIRST (so it sits behind the UFR traces) — the PLASMA REFILL CURVE in soft teal #1A6B72, 1.5 px stroke, a smooth monotone-descending curve from a high starting point to a low plateau by minute 240. Labelled inline in teal Inter Regular: "Plasma refilling — finite, falls over session".
Four overlaid UFR profile traces in the SAME color/style mapping as the top panel for cognitive consistency:
  1. Constant (navy #1F3864 solid line, 2 px) — flat horizontal line at the mean UFR. Labelled "Constant" in small navy at the right end.
  2. Descending (teal #1A6B72 solid line, 2 px) — high early (≈1.4 × mean), tapers gently to a floor at ≈0.5 × mean by minute 240. Labelled "Descending" at the right end in teal.
  3. Step (amber #C9A84C dashed line, 2 px) — three flat tiers stepping down at minutes 80 and 160. Labelled "Step".
  4. Ascending–descending A/D (purple #6c3d8e dash-dot line, 2 px) — rises early, peaks at ≈mid-session, tapers. Labelled "A/D".
A horizontal DASHED CEILING LINE in red #C00000 at the patient-specific safe UFR ceiling, labelled at its right end in red Inter Regular: "Patient-specific ceiling (≤13 mL/kg/hr; consider ≤10)".
A pale GRAY HORIZONTAL BAND running across the full plot width at the mean UFR level (the same height as the constant trace), labelled inside in dark-gray Inter Regular: "MEAN UFR — same for all four shapes. Profiling changes distribution, NOT dose."
Bottom-right corner of this panel: a small rounded AMBER (#C9A84C) pill, white Inter SemiBold text, ~12 px: "Profiling does not lower mean UFR. Verify mean UFR before adding a profile."
A small inline LEGEND in the upper-right corner of the panel mirroring the top panel's: Constant / Descending / Step / A/D, with stroke style and color swatch.

═══ BOTTOM STRIP (full width, below both panels) ═══
A single clear KEY LINE centered, in navy #1F3864 Inter Regular: "Same total Na delivered ≠ same Na balance. Same total UF removed ≠ same hemodynamic stress. The operative variables are TIME-AVERAGED Na and MEAN UFR — both must be calculated, both must be documented."

VISUAL DISCIPLINE:
- All typography in Inter (SemiBold for titles and panel labels, Regular for axis text and callouts, Italic Regular only for the time-averaged band note).
- Light gridlines on each chart in very pale gray (#f3f4f6), minor only.
- Generous left/right margins (≥60 px) so traces don't crowd the labels.
- Trace stroke widths equal (2 px) so no profile reads as "louder" than another.
- Color/style mapping is IDENTICAL across both panels — the eye should recognize "the same four profile families, applied to two different parameters".
- No decorative gradients, glows, drop shadows, or 3D rendering. Clean publication-grade line-chart aesthetic.
- Small semi-transparent navy "williamriveromd.com" attribution in the bottom-right corner of the canvas, ~11 px, 70% opacity.
```

**Negative:** Avoid cartoon style, clutter, tiny labels, AI gibberish, dark backgrounds. No filler text. No stylized infographic pictograms — clean line charts only. No grid clutter. No log scales. Use only Inter / Nunito Sans / IBM Plex Sans / Manrope.

---

## IMAGE 7 — Figure 5 · Comparative positioning matrix

- **FILE NAME:** `iso-uf-sodium-uf-ramping-positioning-matrix.png` (+ `.webp` twin)
- **SECTION PLACEMENT:** §5 Comparison (top of body, above the alternatives table; already wired)
- **ARCHETYPE:** Single-panel 2-axis bubble matrix (Scaffold D)
- **AUDIENCE:** Clinicians
- **DIMENSIONS:** 1659 × 948 (16:9 landscape)

### COPY-READY PROMPT

```
Medical pathophysiology infographic, AJKD/NEJM graphical abstract style. Pure white (#ffffff) background. Title at top in bold navy (#1F3864) Inter SemiBold: "Comparative positioning — IDH stabilization toolkit". Subtitle directly under the title in medium-gray Inter Regular: "Where each technique sits on the evidence-vs-cost map. Cool dialysate and dry-weight / time optimization are the high-evidence, low-cost first moves; the ramping / iso-UF toolkit is layered onto the refractory subset."

A single bubble-chart panel occupies ~80% of the canvas. Clean publication-grade chart aesthetic — thin axes, faint pale-gray (#f3f4f6) gridlines, no glow, no drop shadows.

X-AXIS (horizontal, navy Inter Regular): "Evidence strength →"
Tick labels along the x-axis, left to right:
"Limited / consensus only" · "Small RCTs / crossover" · "Multiple RCTs" · "Cochrane / meta-analysis / strong observational"

Y-AXIS (vertical, navy Inter Regular): "Resource / equipment cost ↑"
Tick labels along the y-axis, bottom to top:
"Operational only" · "Programmable machine" · "Specialty equipment" · "Pharmacy / staffing burden"

BUBBLES — nine interventions, each plotted at its (evidence, cost) coordinate, with size encoding implementation friction (small / medium / large). Each bubble carries a short label INSIDE in bold white Inter SemiBold, and a one-line CAVEAT just below or beside the bubble in medium-gray Inter Regular. Bubble color encodes which physiologic axis the intervention targets (per the guide's four-axis cascade):
- TEAL #1A6B72 = refilling axis
- NAVY #1F3864 = tonicity / osmolality axis
- PURPLE #6c3d8e = autonomic / vascular tone axis
- GREEN #2E6B3E = cardiac reserve / preload axis
- A bubble that spans more than one axis has a thin secondary ring of the second axis color around its outer edge.

Plot these bubbles at the following approximate positions and sizes:

1. "Dry-weight reassessment" — GREEN fill with a TEAL outer ring (cardiac + refilling), MEDIUM bubble. Position: far right ("Cochrane / strong observational"), bottom ("Operational only"). Caveat below: "First-line. Clinical ± BIA + lung ultrasound."

2. "Cool dialysate 35.5°C" — PURPLE fill (autonomic), MEDIUM bubble. Position: far right ("Cochrane"), bottom ("Operational only"). Caveat: "High evidence, near-zero cost. Trial first."

3. "Treatment time / frequency ↑" — GREEN fill with a TEAL outer ring (cardiac + refilling), LARGE bubble (highest implementation friction). Position: far right ("strong observational"), middle ("Programmable machine / chair-time"). Caveat: "Lowers MEAN UFR — the structural fix."

4. "Antihypertensive timing review" — PURPLE fill (autonomic), SMALL bubble. Position: middle-right ("Multiple RCTs / pragmatic"), bottom ("Operational only"). Caveat: "Free win in poly-treated patients."

5. "Sodium-balance-neutral ramping" — NAVY fill (tonicity), MEDIUM bubble. Position: middle ("Multiple RCTs"), low-middle ("Programmable machine"). Caveat: "Net-zero Na or STOP. Not for high IDWG."

6. "Iso-UF (sequential)" — NAVY fill with a PURPLE outer ring (tonicity + tone), MEDIUM bubble. Position: middle-left ("Small RCTs + KDIGO consensus"), low ("Programmable machine"). Caveat: "Adequacy trade-off; longer session."

7. "UF profiling (descending / A/D)" — TEAL fill (refilling), MEDIUM bubble. Position: middle ("Small RCTs / crossover"), low ("Programmable machine"). Caveat: "Distribution ≠ dose."

8. "BV-UFC biofeedback" — TEAL fill (refilling), LARGE bubble (high cost). Position: middle ("Crossover RCT 2025"), high ("Specialty equipment"). Caveat: "Specialty machine; evidence mixed."

9. "Midodrine" — PURPLE fill (autonomic), SMALL bubble. Position: far left ("Limited / KDIGO: insufficient"), middle-high ("Pharmacy / staffing burden"). Caveat: "Supine HTN risk; refractory tail only."

LEGEND — upper-LEFT corner of the plot, a compact white-fill legend card with a thin navy 1 px border and rounded corners. Title in navy Inter SemiBold: "Bubble color = mechanism axis targeted". Below it, five rows, each a small colored chip + a one-line label in Inter Regular navy:
- Teal — Refilling
- Navy — Tonicity / osmolality
- Purple — Autonomic / vascular tone
- Green — Cardiac reserve / preload
- A small chip with a two-color ring — "Multi-color ring = spans more than one axis"

Just under the legend, a tiny note in medium-gray Inter Regular: "Bubble size = implementation friction (chair-time / cost / staffing)."

RULES OF THE ROAD — a thin strip BELOW the plot, full width, very subtle pale-gray (#f3f4f6) fill, three short bullets in a single horizontal row in medium-gray Inter Regular:
• "Move RIGHT before moving UP — exhaust low-cost, high-evidence moves first."
• "Match the bubble color to the patient's failing axis."
• "Cost is per-session and operational, not per-patient lifetime."

VISUAL DISCIPLINE:
- All typography in Inter (SemiBold for titles and bubble labels, Regular for caveats and tick labels). Never a serif font.
- Bubble fills slightly transparent (≈85% opacity) so where two bubbles sit near each other they remain individually legible; outer rings (where present) are solid.
- Generous whitespace — at least 60 px of margin on every side of the canvas.
- Bubble caveats kept to one short line; no caveat may overlap an axis tick label or another bubble.
- The four-axis legend in the upper-left is small but legible at thumbnail size.
- No decorative icons or pictograms inside bubbles — text label only.
- Small semi-transparent navy "williamriveromd.com" attribution in the bottom-right corner of the canvas, ~11 px, 70% opacity.
```

**Negative:** Avoid cartoon style, clutter, tiny labels, AI gibberish, dark backgrounds. No decorative icons inside bubbles. No 3D rendering or glow effects on bubbles. No log axes. No filler text. Bubble overlaps must not hide labels. Use only Inter / Nunito Sans / IBM Plex Sans / Manrope.

---

## Post-render checklist

After all four images are generated:

1. Save each `.png` and the matching `.webp` twin into `/images/` at the FILE NAME above.
2. Run `python3 patch_hero_fetchpriority.py --guide iso-uf-sodium-uf-ramping.html` so the hero is `fetchpriority="high" loading="eager"`.
3. Run `python3 patch_hero_maxwidth.py --guide iso-uf-sodium-uf-ramping.html` so the hero `<img>` is capped at `max-width:600px` centered (the wrapping `<figure>` remains full-width).
4. Re-render the PDF: start the local static server, run `python3 /tmp/.../render_pdf.py` (the script lives in scratchpad) — the rendered PDF picks up the three in-body figures + the hero automatically.
5. The OG/Twitter meta is already wired with width, height, and alt — paste the `og:image` URL into the Facebook Sharing Debugger and the Twitter Card Validator to confirm preview.
