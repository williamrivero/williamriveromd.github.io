# Image Prompts — Hemodialysis Water Treatment Systems
**Guide:** `guides/dialysis-water-treatment-systems.html`
**URL:** https://www.williamriveromd.com/guides/dialysis-water-treatment-systems
**Destination GPT:** https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Generated:** 2026-07-01 (expanded 2026-07-01)
**Total images:** 11

---

## Visual aid architecture overview

**Audience:** Dialysis nurses and technicians (primary), nephrologists and biomedical/water-treatment engineers (secondary). This is a **single-mode clinician/technical operations reference** (`body class="physician-mode single-mode"`) — there is no patient-facing tab, so every image in this pack is technical/editorial, not warm patient-education imagery. No Filipino-patient-in-clinic imagery; the "cast" here is dialysis-unit technical staff and equipment.

**Core educational challenge.** The guide asks staff to hold a mental model of an entire engineered system — pretreatment → RO → storage/loop → UF — and to reason about how that system changes for different source waters (municipal, deep well, brackish, hard water) and different facility configurations (isolation bays, HDF, dual-pass RO). Three visual jobs fall out of that:

1. **Make the treatment train legible as a single left-to-right sequence** — nurses and techs think in checklists, not paragraphs; the flow diagram from §3 should read like a wall chart.
2. **Make the four source-water variants comparable at a glance** — the guide's key differentiator versus a generic WTS reference is that pretreatment design changes by source water; one comparison panel should let a reader instantly see what's added/changed per source.
3. **Make capacity math visual, not just arithmetic** — §5's peak-demand → margin → temperature-derate → headroom-verdict logic (also the WTS capacity calculator) reads as a sequence of steps ending in a decision, which is exactly what a step-sequence schematic is for.
4. **Make each facility-layout decision spatially concrete on its own terms** — §6 packs three physically distinct decisions (isolation-bay placement, HDF clustering, dual-pass RO) into one section of prose. Rather than one crowded diagram, this pack gives an **overview** schematic (Image 5) plus **three dedicated detail schematics** (Images 7–9) that zoom into what the overview intentionally leaves out — POU filter staging, tapered membrane arrays, dead-leg contrast.
5. **Make the microbiological limit hierarchy visually ordered** — §7's three purity tiers (dialysis water → standard dialysate → ultrapure) are easy to mix up in prose; a single ascending reference card fixes the order permanently in memory.
6. **Make the Golden Rule a literal decision path** — §9's "if in doubt, don't dialyze" logic and its four STOP triggers are already algorithm-shaped; rendering them as a flowchart matches how staff actually use it under time pressure.

The pack carries the reader from "why the room exists" (hero) → "how the baseline system flows" (Fig. 1) → "how it changes by source water" (Fig. 2) → "how to size and grow it" (Fig. 6) → "how the loop is laid out, then zoomed into three special cases" (Figs. 5, 7–9) → "how purity tiers stack" (Fig. 10) → "what to do when something's wrong" (Fig. 11).

**Design system.** House style throughout — white/off-white backgrounds, navy `#0f1e2e` text/structure, clinical teal `#1a6b72` headings/accents, amber `#b8860b` caution, clinical red `#b91c1c` danger/stop, renal green `#1f7a4d` safe/optimal. Approved sans-serif only: **Inter** (headings/labels) or **Manrope** (body/annotation), matching the guide's own type system. Every image carries the `williamriveromd.com` attribution, bottom-right (bottom-center for the portrait hero), small semi-transparent navy text.

**Continuity note:** This is a technical/engineering register, not the patient-editorial register used elsewhere on the site — closer in spirit to a biomedical-engineering trade publication or an AAMI/ISO technical bulletin than to a patient pamphlet. Keep photography and 3D renders equipment-forward; keep any people present technical staff, never patients.

---

## Image manifest

| # | Section anchor | File name | Archetype | Aspect | Dimensions |
|---|---|---|---|---|---|
| 1 | `<head>` og:image | `dialysis-water-treatment-systems-og.png` | Photorealistic Editorial — OG Card | 1.91:1 | 1200 × 630 |
| 2 | Hero (circular vignette) | `dialysis-water-treatment-systems-vignette-hero.png` | Circular Vignette Hero v3 — Clinical People | 1:1 (85–90% inscribed circle) | 2048 × 2048 |
| 3 | `#sec-design` (§3 System Design) | `wts-treatment-train-flow.png` | Clinical Algorithm / Process Flowchart | 16:9 | 1792 × 1024 |
| 4 | `#sec-source` (§4 Designing for Your Source Water) | `wts-source-water-comparison.png` | Comparison Panel / Reference Card | 4:3 | 1536 × 1152 |
| 5 | `#sec-layout` (§6 Facility Layout — overview) | `wts-facility-layout-isolation-hdf-dualpass.png` | Mechanism / Schematic Reference Diagram | 16:9 | 1792 × 1024 |
| 6 | `#sec-capacity` (§5 Sizing & Capacity Planning) | `wts-capacity-sizing-sequence.png` | Horizontal Step Sequence + Verdict | 16:9 | 1792 × 1024 |
| 7 | `#sec-layout` §6.1 (Isolation bay, detail) | `wts-isolation-bay-loop-detail.png` | Side-by-Side Comparison Schematic | 16:9 | 1792 × 1024 |
| 8 | `#sec-layout` §6.2 (HDF / POU-UF, detail) | `wts-hdf-pou-uf-detail.png` | Single-Station Mechanism Detail | 4:3 | 1536 × 1152 |
| 9 | `#sec-layout` §6.3 (Dual-pass RO, detail) | `wts-dual-pass-ro-detail.png` | Engineering Mechanism Diagram | 16:9 | 1792 × 1024 |
| 10 | `#sec-standards` (§7 Water Quality Standards) | `wts-water-quality-tiers.png` | Reference Card — Ascending Tiers | 4:3 | 1536 × 1152 |
| 11 | `#sec-trouble` (§9 Troubleshooting — Golden Rule) | `wts-golden-rule-decision-flow.png` | Clinical Algorithm / Decision Flowchart | 2:3 portrait | 1024 × 1536 |

> **OG image:** Image 1 is the `og:image`. Set `og:image:width="1200"` and `og:image:height="630"` (already wired in the guide's `<head>`). Generate at exactly 1200 × 630 px.
> **Hero image:** Image 2 is the circular-vignette hero for `figure.hero-figure > .hero-vignette`. Render at 2048 × 2048, save as both `.png` and a WebP twin, and wire via `<picture><source srcset="../images/dialysis-water-treatment-systems-vignette-hero.webp" type="image/webp"><img src="../images/dialysis-water-treatment-systems-vignette-hero.png" width="2048" height="2048" fetchpriority="high" loading="eager"></picture>` inside the guide's currently-empty `<figure class="hero-figure">` slot (see "Wiring notes" at the end of this file — the guide was shipped without a hero-figure and needs this block added once the asset exists).
> Figures 3, 4, 6, 10 are self-contained in-body illustrations. Figures 5 and 7–9 form an **overview → detail** cluster for §6: place 5 first (loop-level overview), then 7, 8, 9 in sequence as the section walks through 6.1 → 6.2 → 6.3. Figure 11 sits at the top of §9, right under the "Golden rule" alert box, since it's a visual restatement of that same box. Every in-body figure is paired with a `<figcaption><p class="fig-desc">…</p></figcaption>` per house Rule 11 when wired into the HTML (see wiring notes).

---

## IMAGE 1 — OG / Social Share Card

**IMAGE NUMBER:** 1
**SECTION PLACEMENT:** `<head>` og:image meta tag — social sharing preview
**FILE NAME:** `dialysis-water-treatment-systems-og.png`
**ARCHETYPE:** Photorealistic Editorial — OG Card (technical/engineering register)
**AUDIENCE:** Dialysis nurses, technicians, biomedical/water-treatment engineers, nephrologists
**VISUAL MIX:**
- photorealistic models: none — product/equipment-style editorial photography of the water treatment room
- 2D infographic: title + subtitle text panel on right third
- 3D component graphics: none (photographic equipment)
- algorithm/flowchart: none

**PURPOSE:** A stop-the-scroll share card that reads as authoritative and technical — the RO skid and carbon tanks signal "this is an engineering/patient-safety reference," not a general wellness article, before the reader even opens it.

**KEY CONCEPTS:** Reverse osmosis (RO) skid, pressure gauges, membrane housings, carbon tank pair, distribution-loop piping, patient-safety engineering

**DIMENSIONS:** 1200 × 630 px

**ALT-TEXT SEED:** A hemodialysis water treatment room — a reverse osmosis skid with membrane housings and pressure gauges beside a pair of carbon tanks — the subject of the new williamriveromd.com clinical and engineering reference guide for dialysis staff.

**OG SUITABILITY:** Yes — canonical `og:image` for the guide. Target file size ≤ 200 KB after PNG optimization.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialysis-water-treatment-systems-og.png
IMAGE TYPE: OG Social Share Card — Editorial Photographic (technical/engineering register)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630

AUDIENCE: Dialysis nurses, technicians, biomedical/water-treatment engineers, nephrologists
VISUAL GOAL: A single glance signals "rigorous engineering + patient-safety reference for the water room" — not a general wellness or patient-education card.

PROMPT:
Premium medical/engineering editorial social share card, 1200 × 630 pixels, clean bright white background (#ffffff) with a subtle off-white #fafafa floor tone. LEFT TWO-THIRDS: photorealistic editorial photograph of a compact hemodialysis water-treatment skid inside a clean, bright, tiled utility room — a stainless-steel reverse-osmosis unit with two vertical membrane housings, an analog pressure gauge cluster (feed, reject, permeate) reading plausible clinical values, a small digital conductivity display, and beside it a pair of matched fiberglass carbon adsorption tanks with clearly legible "1" and "2" tank labels; visible PVC distribution-loop piping running along the wall toward the top edge of frame. Soft, even daylight-balanced lighting, shallow depth of field with the gauges in sharp focus, gentle realistic shadows, no people in frame. The room reads clean, well-maintained, and clinically serious — like a photograph from a biomedical-engineering trade publication, not a stock "hospital hallway" photo. RIGHT ONE-THIRD: clean white panel with sharp readable typography in the Inter typeface — large bold condensed title in navy (#0f1e2e): "Hemodialysis Water Treatment Systems"; below it in clinical teal (#1a6b72), medium weight: "Design, Standards, Capacity & Troubleshooting"; below that a thin teal horizontal rule; then small navy text: "W. G. M. Rivero, MD · Nephrology"; below that in light navy: "A Clinical & Engineering Reference for Dialysis Staff". Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com". White and off-white background only — no dark backgrounds anywhere in the frame.

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable gauge faces, avoid AI gibberish text on any label or display (gauge numerals and tank labels must be plausible and legible, not garbled), avoid unrealistic plumbing/equipment, avoid overprocessed HDR, avoid generic stock-photo "hospital corridor" look, avoid excessive saturation, avoid any people in frame, avoid patient-facing imagery of any kind. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the Inter typeface for all on-image text — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable when shrunk to a small social-share thumbnail, technically plausible (a real biomedical engineer should not wince at the equipment), visually calm, publication-grade. Background must be white/off-white — never dark. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 2 — Guide Hero (Circular Vignette)

**IMAGE NUMBER:** 2
**SECTION PLACEMENT:** `figure.hero-figure > .hero-vignette` — inside the hero, beside the `<h1>` (add this figure to the currently image-less hero; see wiring notes)
**FILE NAME:** `dialysis-water-treatment-systems-vignette-hero.png`
**IMAGE TYPE:** Circular vignette hero v3 — Scaffold A (Clinical People Scene)
**ASPECT RATIO:** 1:1 (square — displayed inside an 85–90% inscribed circle with a visible white margin)
**PIXEL DIMENSIONS:** 2048 × 2048
**COMPOSITION ARCHETYPE:** H — Clinical (one technical scene, minimal supporting imagery)
**CAMERA:** Environmental portrait, three-quarter rear angle (over-the-shoulder toward the gauge cluster) — distinct from `pocus-nephrology.html`'s macro hands-only framing and from the standing/seated consultation framings used on recent patient-mode heroes
**HUMAN VARIATION (vs. previous single-tab clinician guide):** biological sex (woman, vs. the ungendered hands-only framing in `pocus-nephrology.html`), age (mid-30s), face largely turned away/three-quarter rear (vs. no face shown), hairstyle (hair tied back in a low bun), build (average/athletic build vs. unspecified), clothing (navy scrub top + PPE gloves vs. unspecified sleeve), accessory (safety glasses pushed up on head), posture (leaning slightly forward, one hand on the gauge cluster), activity (reading/adjusting a gauge vs. holding a probe), environment (utility/plant room vs. abstract dark background), camera distance (mid-distance environmental vs. extreme macro), camera angle (three-quarter rear vs. top-down macro), lighting (bright even daylight-balanced room light vs. clinical dark-mode-adjacent lighting implied by the anatomy overlay) — 12 traits differ.
**AUDIENCE:** Clinicians — dialysis nurses, technicians, biomedical/water-treatment engineers, nephrologists
**VISUAL GOAL:** One glance says "a careful technical professional is personally checking this system" — patient safety made visible through diligence, not drama.

**PROMPT:**
```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: H — Clinical (one technical scene, minimal supporting imagery). Camera: environmental portrait, three-quarter rear angle, mid-distance, looking over the subject's shoulder toward the equipment.

Subject: a Filipino woman in her mid-30s, biomedical/water-treatment technician, athletic build, dark hair pulled back in a low bun, wearing a navy scrub top and clear nitrile gloves with safety glasses pushed up on her head, seen from a three-quarter rear angle with her face only partly visible in profile, calm and focused expression, standing at a hemodialysis water-treatment skid in a clean, bright dialysis-unit utility room. She has one gloved hand resting near an analog pressure-gauge cluster on a stainless-steel reverse-osmosis unit, reading the gauges; behind and beside her, softly out of sharp focus, the rounded tops of a matched pair of carbon adsorption tanks and a short run of PVC distribution-loop piping are visible. Soft natural daylight from an unseen window, gentle shallow depth of field, calm and diligent mood.

Visual hierarchy: hero subject and the gauge cluster she is reading occupy 60–70% of the circle; the carbon tanks and piping form 2–4 supporting context elements at 20–30%; reserve a 20–25% TITLE SAFE ZONE in the upper-left of the circle as a softly blurred, evenly lit plain wall or gentle gradient (no equipment, faces, labels, or callouts inside that zone) so the HTML title can sit beside the disc without covering important artwork.

Calm, reassuring, documentary-realistic colour grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or williamriveromd.com watermark.
```

**NEGATIVE INSTRUCTIONS:**
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy or equipment. No patient in frame.

**QUALITY CHECK:**
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant hero subject (technician + gauge cluster) occupying 60–70% of the circle, 2–4 supporting elements (tanks, piping), 20–25% empty title-safe zone reserved. Filipino clinical-technical context, ≥12 traits visibly different from `pocus-nephrology.html`'s hero. Camera framing (environmental three-quarter rear) not repeated from the previous single-tab guide's macro hands-only framing. Crops cleanly inside the circle with no text or subject lost at the edges.

---

## IMAGE 3 — The Treatment Train (§3 System Design)

**IMAGE NUMBER:** 3
**SECTION PLACEMENT:** `#sec-design` — immediately after the "Read the flow as a sentence" callout, before §3.1 Pre-treatment
**FILE NAME:** `wts-treatment-train-flow.png`
**ARCHETYPE:** Clinical Algorithm / Process Flowchart (engineering register, not decision-tree register)
**AUDIENCE:** Dialysis nurses, technicians, biomedical engineers
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — a left-to-right process flow with rounded stage nodes
- 3D component graphics: small simplified icon-style renders per stage (filter cylinder, softener tank, carbon tank pair, membrane cartridge, RO housing, storage tank, UF cartridge) — schematic, not photoreal
- algorithm/flowchart: yes — linear, not branching

**PURPOSE:** Turn the guide's core mental model — "water always moves one direction, each stage protects the next" — into a single wall-chart image staff can mentally replay while walking the actual plumbing.

**KEY CONCEPTS:** Feed water, sediment/multimedia filter, water softener, dual carbon tanks (worker + polisher), microfilter, reverse osmosis (RO), storage tank + distribution loop, ultrafiltration (UF), dialysis machine — 8 sequential stages, unidirectional flow, carbon-before-RO / UF-after-RO ordering emphasized.

**DIMENSIONS:** 1792 × 1024 px

**ALT-TEXT SEED:** A left-to-right flow diagram of the hemodialysis water treatment train — feed water through sediment filter, softener, dual carbon tanks, microfilter, reverse osmosis, storage and distribution loop, and ultrafiltration — ending at the dialysis machine.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-treatment-train-flow.png
IMAGE TYPE: Clinical/Engineering Process Flowchart
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Dialysis nurses, technicians, biomedical engineers
VISUAL GOAL: A single, wall-chart-style left-to-right flow that makes the 8-stage water treatment train memorable and walkable in the physical plant.

PROMPT:
Clean engineering process-flow infographic, premium AAMI/ISO technical-bulletin aesthetic, landscape 16:9, white background (#ffffff). A single unbroken LEFT-TO-RIGHT horizontal pathway of 8 rounded rectangular stage nodes connected by bold navy (#0f1e2e) arrows, each node containing a small clean schematic icon (not photorealistic) above a short label in the Inter typeface:
1. "FEED" — a water tap/inlet icon with a small break tank, label "Feed water"
2. a cylindrical multimedia filter icon, label "Sediment filter"
3. a resin tank icon with a small salt/brine tank beside it, label "Softener"
4. TWO identical cylindrical tank icons side by side inside one shared node, individually labeled small "1" (worker) and "2" (polisher), label below "Carbon tanks"
5. a small cartridge-filter icon, label "Microfilter (1–5 µm)"
6. a horizontal cylindrical RO membrane housing icon with a small pressure-gauge glyph, label "Reverse osmosis (RO)", this node highlighted with a subtle clinical-teal (#1a6b72) background tint to mark it as the system's core
7. a storage tank icon with a circulating-loop arrow drawn around it, label "Storage + distribution loop"
8. a fine membrane cartridge icon, label "Ultrafiltration (UF)"
ending in a distinct final icon of a dialysis machine silhouette, label "Dialysis machine".
Beneath nodes 4 and 6, add two small amber (#b8860b) annotation callouts on thin leader lines: below node 4, "Carbon comes BEFORE RO — protects the membrane from chlorine/chloramine"; below node 8, "UF comes AFTER RO — final barrier against bacteria & endotoxin". A thin, elegant curved arrow beneath the entire chain, running from node 8 back toward node 7, labeled small "Recirculation loop" in clinical teal, showing that treated water continuously returns rather than dead-ending. Generous white negative space above and below the chain; rounded modular cards; every label legible at both full size and thumbnail scale using the Inter typeface only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid a branching/decision-tree look (this is a linear process, not a decision algorithm), avoid photorealistic equipment renders (keep icons clean and schematic), avoid overprocessed HDR, avoid excessive saturation, avoid more than 8 primary stage nodes. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the Inter typeface for all text — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, engineering-plausible (a biomedical engineer should recognize every stage), visually calm, publication-grade. Background must be white — never dark. The carbon-before-RO and UF-after-RO annotations must be clearly legible. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 4 — Designing for Your Source Water (§4)

**IMAGE NUMBER:** 4
**SECTION PLACEMENT:** `#sec-source` — after the section's opening paragraph, before §4.1 Municipal/treated water supply
**FILE NAME:** `wts-source-water-comparison.png`
**ARCHETYPE:** Clinician Reference Card — 4-column comparison panel
**AUDIENCE:** Dialysis nurses, technicians, biomedical engineers, nephrologists (especially those in provincial/coastal facilities)
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — 4-column comparison table with a small schematic icon column header per source
- 3D component graphics: none (small 2D icons only)
- algorithm/flowchart: none

**PURPOSE:** Let a reader instantly see, in one glance, what changes in the pretreatment train depending on the facility's actual water source — the guide's key differentiating content versus a generic WTS reference.

**KEY CONCEPTS:** Municipal/treated (baseline, chloramine breakthrough risk), deep well/borehole (iron/manganese removal, higher bacteriological risk pre-treatment), brackish/saline (dual-pass RO, antiscalant, lower recovery), hard water (duplex softener, antiscalant backup, CaCO₃ scaling risk if inadequate).

**DIMENSIONS:** 1536 × 1152 px

**ALT-TEXT SEED:** A four-column reference card comparing hemodialysis water treatment system design for municipal water, deep well/borehole water, brackish/saline water, and hard water — showing what pretreatment stage is added or changed for each source.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-source-water-comparison.png
IMAGE TYPE: Clinician Reference Card — 4-Column Comparison Panel
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152

AUDIENCE: Dialysis nurses, technicians, biomedical engineers, nephrologists
VISUAL GOAL: One glance shows how the pretreatment train differs across four real-world source-water scenarios, so a reader can immediately locate their own facility's situation.

PROMPT:
Clean clinical/engineering reference-card infographic, publication-grade, white background (#ffffff), landscape 4:3. A bold navy (#0f1e22) title band across the top in the Inter typeface: "Designing for Your Source Water". Below it, FOUR vertical columns of equal width, each a soft rounded card with a light gray (#f3f4f6) background, separated by thin vertical rules:

COLUMN 1 header: small icon of a city water tower + tap, label "Municipal / Treated" in clinical teal (#1a6b72). Body rows (small Manrope-typeface text with a colored dot bullet): teal dot "Baseline treatment train"; amber dot "Main risk: chloramine breakthrough"; teal dot "Dual carbon tanks (worker + polisher)".

COLUMN 2 header: small icon of a borehole/well drill with groundwater lines, label "Deep Well / Borehole" in clinical teal. Body rows: amber dot "+ Iron/manganese removal (aeration or greensand)"; amber dot "Higher, more variable turbidity — upsized prefilter"; red dot "Higher bacteriological risk pre-treatment"; teal dot "Baseline contaminant testing incl. arsenic".

COLUMN 3 header: small icon of a coastline with a wave and a water droplet, label "Brackish / Saline" in clinical teal. Body rows: amber dot "Elevated TDS — higher RO operating pressure"; amber dot "Often needs dual-pass (double-pass) RO"; amber dot "Routine antiscalant dosing"; red dot "Lower recovery, higher reject volume".

COLUMN 4 header: small icon of stacked mineral/scale crystals inside a water drop, label "Hard Water" in clinical teal. Body rows: teal dot "Handled by softener at normal loads"; amber dot "High hardness: duplex/dual-alternating softener"; amber dot "Antiscalant as defensive backup"; red dot "Undersizing → CaCO₃ scaling on the RO membrane".

Each column's icon rendered in a simple, clean, single-color line-icon style (navy or teal), not photorealistic. Consistent row height and alignment across all four columns so the eye can scan horizontally as well as vertically. Generous padding, rounded card corners, high legibility at thumbnail scale, Inter for headers and Manrope for body text only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable text, avoid AI gibberish text, avoid uneven column widths, avoid photorealistic renders (icons must stay simple line-art), avoid overprocessed HDR, avoid excessive saturation, avoid more than 4 body rows per column. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter (headers) and Manrope (body) — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, technically accurate per the source guide content, visually calm, publication-grade. Background must be white — never dark. All four columns must be legible and balanced at a glance. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 5 — Facility Layout Overview: Isolation Bay, HDF Cluster & Dual-Pass RO (§6, loop-level)

**IMAGE NUMBER:** 5
**SECTION PLACEMENT:** `#sec-layout` — right after the §6 intro sentence, BEFORE the §6.1–6.3 prose, as the orienting loop-level map. Images 7–9 (below) then zoom into each of the three decisions this overview only sketches.
**FILE NAME:** `wts-facility-layout-isolation-hdf-dualpass.png`
**ARCHETYPE:** Mechanism / Schematic Reference Diagram (floor-plan-adjacent, not photorealistic)
**AUDIENCE:** Biomedical engineers, facility planners, nephrologists, charge nurses
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — a simplified schematic of the distribution loop as a ring, with three callout zones
- 3D component graphics: none (clean 2D schematic icons only)
- algorithm/flowchart: none

**PURPOSE:** Give the reader ONE loop-level map before the section's three sub-topics unfold in prose, so §6.1–6.3 each land as "here's the zoomed-in version of the thing I just saw on the map" rather than three unrelated facts. This is deliberately the low-detail overview — Images 7, 8, and 9 carry the engineering detail this one omits.

**KEY CONCEPTS:** Distribution loop as a closed ring (supply out, return back to storage/RO), short branch to an isolation bay near the return leg (not a long dead-leg stub), a cluster of HDF stations at the takeoff closest to the post-RO/UF point, an inset showing a first-pass RO feeding a second-pass RO with an interstage booster pump.

**DIMENSIONS:** 1792 × 1024 px

**ALT-TEXT SEED:** A schematic diagram of a hemodialysis water distribution loop showing the isolation bay on a short branch near the loop's return leg, a cluster of HDF stations closest to the post-RO/ultrafiltration point, and an inset of a dual-pass reverse osmosis train with an interstage booster pump.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-facility-layout-isolation-hdf-dualpass.png
IMAGE TYPE: Engineering Schematic / Mechanism Reference Diagram
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Biomedical engineers, facility planners, nephrologists, charge nurses
VISUAL GOAL: Make three separate facility-layout decisions spatially concrete on one shared diagram — isolation-bay placement, HDF-station clustering, and dual-pass RO arrangement.

PROMPT:
Clean technical schematic infographic, engineering-bulletin style, landscape 16:9, white background (#ffffff). MAIN PANEL (left two-thirds): a simplified overhead-schematic ring representing the water distribution loop, drawn as a bold navy (#0f1e2e) rounded rectangle loop with a small labeled "RO / UF outlet" icon at the top where treated water enters the loop and a "return to storage" arrow where it exits — small directional arrowheads along the ring showing continuous one-way recirculation flow. Along the loop, four to six small identical rounded rectangle icons represent standard dialysis stations, evenly spaced, in light gray (#f3f4f6). One clearly separated branch — short, drawn noticeably SHORTER than a standard station spacing — leads off the loop near the return leg to a distinct room icon labeled "Isolation bay" in clinical red (#b91c1c) outline, with a small annotation in Manrope typeface: "Short branch, closest point to return — no dead leg". A cluster of two to three station icons positioned at the takeoff CLOSEST to the "RO / UF outlet" icon are tinted clinical teal (#1a6b72) and labeled "HDF cluster", with a small annotation: "Shortest distance from UF — ultrapure water". RIGHT ONE-THIRD: a separate clean inset panel with a thin rounded border, titled "Dual-pass RO" in navy Inter typeface, showing two horizontal cylindrical RO membrane housings in series — labeled "Pass 1" and "Pass 2" — connected by a small pump icon labeled "Interstage booster pump", with a thin arrow from the Pass-1 reject line curving back to blend into the Pass-1 feed, labeled small "Reject recirculation (optional)". Consistent iconography and color logic between the main panel and the inset. Generous white space, rounded modular shapes, all labels legible at thumbnail scale, Inter for titles/labels and Manrope for annotations only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid a literal architectural floor plan (this is a simplified schematic, not a construction drawing), avoid photorealistic equipment renders, avoid overprocessed HDR, avoid excessive saturation, avoid more than 6 station icons on the main loop. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter and Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, engineering-plausible, visually calm, publication-grade. Background must be white — never dark. The isolation-bay short-branch concept and the HDF-cluster-near-outlet concept must both be unambiguous at a glance. The dual-pass RO inset must read as a distinct, self-contained diagram. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 6 — Capacity Sizing: Peak Demand to RO Headroom (§5)

**IMAGE NUMBER:** 6
**SECTION PLACEMENT:** `#sec-capacity` — after §5.1's ordered list, before §5.2 "Increasing capacity when machines are added"
**FILE NAME:** `wts-capacity-sizing-sequence.png`
**ARCHETYPE:** Horizontal Step Sequence + Verdict (Scaffold C, extended with a decision-style final card)
**AUDIENCE:** Nephrologists, biomedical engineers, facility administrators planning an expansion
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — a left-to-right calculation sequence ending in a three-way verdict card
- 3D component graphics: none
- algorithm/flowchart: light — the final card branches into three outcomes

**PURPOSE:** Turn the capacity-planning arithmetic (peak demand → margin → temperature derate → compare to RO rating) into one memorable visual sequence, and pair it with the calculator so a reader who has just computed a number can immediately see where it lands.

**KEY CONCEPTS:** Peak demand (stations × per-station flow), design margin (+20–30%), temperature derating (~2.5%/°C below 25°C), comparison against RO's rated nameplate capacity, three-way headroom verdict (Sufficient / Marginal / Insufficient), N+1 parallel RO as the fix for "Insufficient."

**DIMENSIONS:** 1792 × 1024 px

**ALT-TEXT SEED:** A step-by-step diagram showing how to calculate hemodialysis water treatment capacity — peak demand, design margin, temperature derating — compared against RO rated capacity to reach a sufficient, marginal, or insufficient headroom verdict.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-capacity-sizing-sequence.png
IMAGE TYPE: Horizontal Step Sequence + Verdict Card
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Nephrologists, biomedical engineers, facility administrators
VISUAL GOAL: Make the capacity-sizing calculation a single memorable left-to-right sequence that ends in a clear three-way decision.

PROMPT:
Clean clinical/engineering education infographic, white (#ffffff) background, landscape 16:9. Title at top center in bold navy (#0f1e2e) Inter typeface: "Sizing Water Treatment Capacity". FOUR rounded rectangular cards arranged horizontally in a single row on a very soft gray panel (#f3f4f6), connected by bold navy right-pointing arrows:
Card 1 — small icon of stacked dialysis-station rectangles with a clock overlay, label "Peak simultaneous demand", sub-text "stations × flow rate (L/hr)".
Card 2 — small icon of a percentage/plus symbol, label "+ Design margin", sub-text "typically 20–30%".
Card 3 — small icon of a thermometer beside a downward arrow, label "÷ Temperature derate", sub-text "~2.5%/°C below 25°C feed".
Card 4 — small icon of a gauge dial, label "Compare to RO rated capacity", sub-text "manufacturer nameplate at 25°C".
An arrow from Card 4 leads to a wider final VERDICT card, divided into three vertically stacked colored bands of equal height: top band renal green (#1f7a4d) labeled "Sufficient — ≥20% headroom"; middle band amber (#b8860b) labeled "Marginal — thin headroom, re-check assumptions"; bottom band clinical red (#b91c1c) labeled "Insufficient — add a parallel RO skid (N+1)". Each band has a small matching icon (checkmark, caution triangle, stop octagon). Beneath the whole sequence, a thin full-width soft-gray strip with a brief summary sentence in navy Manrope typeface: "Peak demand, margin, and temperature derating — checked against your RO's rated output — decide whether to add stations now or add capacity first." Generous whitespace, rounded cards, mobile-readable labels using Inter (titles) and Manrope (sub-text) only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid more than 4 sequence cards plus the verdict card, avoid a branching decision-tree look for the first four cards (they are strictly sequential), avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter and Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, engineering-plausible, visually calm, publication-grade. Background must be white — never dark. The three-way verdict (green/amber/red) must be immediately distinguishable by color and icon alone. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 7 — Isolation Bay: Loop Placement & Dead-Leg Avoidance (§6.1, detail)

**IMAGE NUMBER:** 7
**SECTION PLACEMENT:** `#sec-layout` §6.1 — immediately after the isolation-bay bullet list
**FILE NAME:** `wts-isolation-bay-loop-detail.png`
**ARCHETYPE:** Side-by-Side Comparison Schematic (Scaffold B, adapted for engineering rather than clinical normal/abnormal)
**AUDIENCE:** Biomedical engineers, facility planners, infection-control leads
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — two small loop-branch excerpts side by side, plus a small HBV-vs-HCV callout strip
- 3D component graphics: none
- algorithm/flowchart: none

**PURPOSE:** Make the single highest-value engineering point in §6.1 — "short branch, correct; long branch, dead-leg risk" — impossible to misread, and pair it with the HBV-vs-HCV distinction so staff don't over-generalize the isolation requirement to every bloodborne pathogen.

**KEY CONCEPTS:** Short branch off the main loop near the return leg (correct — stays in high-velocity recirculation), long branch/dead-end stub (incorrect — low flow, biofilm risk), HBV-positive patients require a dedicated machine and room, HCV/HIV-positive patients do not require a dedicated machine given standard precautions and disinfection.

**DIMENSIONS:** 1792 × 1024 px

**ALT-TEXT SEED:** A side-by-side comparison of a correct short isolation-bay branch on a hemodialysis water loop versus an incorrect long dead-leg branch, with a callout distinguishing dedicated-machine requirements for hepatitis B versus hepatitis C.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-isolation-bay-loop-detail.png
IMAGE TYPE: Side-by-Side Engineering Comparison Schematic
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Biomedical engineers, facility planners, infection-control leads
VISUAL GOAL: Make "short branch = correct, long branch = dead-leg risk" and the HBV-vs-HCV distinction unmistakable in one glance.

PROMPT:
Clean technical schematic infographic, engineering-bulletin style, white (#ffffff) background, landscape 16:9. Title at top center in bold navy (#0f1e2e) Inter typeface: "Isolation Bay — Loop Placement". A soft dashed vertical divider splits the canvas into two equal panels, each showing a short excerpt of the same distribution-loop ring (bold navy rounded rectangle with small directional arrowheads showing continuous recirculation flow). LEFT panel labeled at top in renal green (#1f7a4d): "Correct — short branch". It shows the loop with a short branch, visibly SHORTER than the spacing between adjacent standard-station icons, leading to a small room icon labeled "Isolation bay", with a small green checkmark icon and Manrope-typeface annotation: "Stays inside high-velocity recirculation — no stagnant segment." RIGHT panel labeled at top in clinical red (#b91c1c): "Incorrect — long dead-leg branch". It shows the same loop with a noticeably LONGER branch, drawn with a visibly narrower, duller pipe segment and small wavy "biofilm" texture icon near its far end leading to the same isolation-bay room icon, with a small red warning-triangle icon and annotation: "Long, low-flow stub — breeds biofilm even when unused." Beneath both panels, a full-width horizontal strip divided into two halves: LEFT half tinted very light red (#fff0f0) with a small dedicated-machine icon, label in navy: "Hepatitis B (HBsAg+) — dedicated machine & room required"; RIGHT half tinted very light teal (#eef6f7) with a small shared-machine-with-disinfection icon, label in navy: "Hepatitis C / HIV — standard precautions, no dedicated machine required". Rounded panel corners, generous whitespace, mobile-readable labels using Inter (titles) and Manrope (annotations) only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid making the two loop excerpts look like different systems (they must clearly be the same loop, differing only in branch length), avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter and Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, engineering-plausible, visually calm, publication-grade. Background must be white — never dark. The short-branch-vs-long-branch contrast and the HBV-vs-HCV distinction must both be unambiguous without reading the body text. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 8 — HDF Bay: Point-of-Use Ultrafiltration Detail (§6.2, detail)

**IMAGE NUMBER:** 8
**SECTION PLACEMENT:** `#sec-layout` §6.2 — immediately after the HDF bullet list
**FILE NAME:** `wts-hdf-pou-uf-detail.png`
**ARCHETYPE:** Single-Station Mechanism Detail (Scaffold E-style reference card, single water path)
**AUDIENCE:** Biomedical engineers, dialysis nurses/technicians staffing HDF bays
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — one horizontal water-path diagram for a single HDF station
- 3D component graphics: none (clean 2D schematic icons only)
- algorithm/flowchart: none

**PURPOSE:** Make the extra hardware an HDF station carries — that a standard HD station doesn't — concrete and countable, since this is the detail most likely to be under-budgeted or skipped when a facility "just adds HDF" to existing stations.

**KEY CONCEPTS:** Loop takeoff, point-of-use (POU) ultrafilter #1 (dialysate polishing), POU ultrafilter #2 (sterilizing-grade, immediately upstream of substitution-fluid infusion), integrity-test port, ultrapure limits (<0.1 CFU/mL, <0.03 EU/mL) called out at the end of the path.

**DIMENSIONS:** 1536 × 1152 px

**ALT-TEXT SEED:** A single hemodialysis HDF station's water path from the loop takeoff through two point-of-use ultrafilters in series to the substitution-fluid line, with an integrity-test port and the ultrapure water limit noted.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-hdf-pou-uf-detail.png
IMAGE TYPE: Single-Station Mechanism Detail — Reference Card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152

AUDIENCE: Biomedical engineers, dialysis nurses/technicians staffing HDF bays
VISUAL GOAL: Make the extra point-of-use hardware an HDF station requires beyond a standard HD station immediately countable and clear.

PROMPT:
Clean clinical/engineering reference-card infographic, white (#ffffff) background, 4:3 aspect. Title at top in bold navy (#0f1e2e) Inter typeface: "HDF Station — Point-of-Use Ultrafiltration". Below the title, a single horizontal water-path diagram running left to right across the middle of the card on a soft gray panel (#f3f4f6): starting icon of a pipe branching off a loop labeled "Loop takeoff", a bold navy arrow to a first cylindrical cartridge filter icon labeled "POU ultrafilter 1 — dialysate polishing", a bold navy arrow to a second, visually distinct cylindrical cartridge filter icon (slightly smaller, finer-mesh appearance) tinted clinical teal (#1a6b72) labeled "POU ultrafilter 2 — sterilizing-grade", a bold navy arrow to a small IV-bag icon labeled "Substitution fluid line", ending at a small dialysis-machine silhouette icon labeled "To patient (via machine)". Below the second filter icon, a small dashed leader line to a compact circular icon labeled "Integrity-test port" with a small Manrope-typeface annotation: "Pressure-hold / diffusion test on the validated interval." At the bottom of the card, a full-width soft teal-tinted strip (#eef6f7) with bold navy Manrope text: "Target at this point: <0.1 CFU/mL and <0.03 EU/mL — ultrapure water, required for online HDF." Rounded card corners, generous whitespace, mobile-readable labels using Inter (titles) and Manrope (annotations) only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid photorealistic equipment renders (icons must stay simple line-art/schematic), avoid depicting an actual patient, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter and Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, engineering-plausible, visually calm, publication-grade. Background must be white — never dark. The two POU filters must read as clearly distinct components in series, not one filter drawn twice. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 9 — Dual-Pass RO Train: Detailed Array & Recovery (§6.3, detail)

**IMAGE NUMBER:** 9
**SECTION PLACEMENT:** `#sec-layout` §6.3 — immediately after the dual-pass RO bullet list
**FILE NAME:** `wts-dual-pass-ro-detail.png`
**ARCHETYPE:** Engineering Mechanism Diagram (single mechanism, expanded detail vs. Image 5's small inset)
**AUDIENCE:** Biomedical engineers, RO vendors/commissioning engineers, nephrologists reviewing a facility proposal
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — a labeled two-pass membrane array with pressure/recovery annotations
- 3D component graphics: none (clean 2D schematic icons only)
- algorithm/flowchart: none

**PURPOSE:** Give a reader enough detail to sanity-check a vendor's dual-pass RO proposal — array staging, interstage pump, and typical recovery ranges — beyond what Image 5's small inset can show.

**KEY CONCEPTS:** Pass 1 tapered ("Christmas tree") membrane array (more vessels early, fewer late, to manage rising reject concentration), typical Pass 1 recovery 50–75%, interstage booster pump (repressurizes low-pressure Pass-1 permeate), Pass 2 single-stage array (no antiscalant usually needed — feed already low-TDS), typical Pass 2 recovery 85–90%+, optional Pass-2-reject-to-Pass-1-feed recirculation for overall water economy.

**DIMENSIONS:** 1792 × 1024 px

**ALT-TEXT SEED:** A detailed engineering diagram of a dual-pass reverse osmosis train — a tapered first-pass membrane array feeding an interstage booster pump into a single-stage second-pass array, with typical recovery percentages and an optional reject-recirculation loop.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-dual-pass-ro-detail.png
IMAGE TYPE: Engineering Mechanism Diagram — Dual-Pass RO Array
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Biomedical engineers, RO commissioning engineers, nephrologists reviewing facility proposals
VISUAL GOAL: Give enough engineering detail to sanity-check a dual-pass RO proposal at a glance — array staging, interstage pump, and typical recovery ranges.

PROMPT:
Clean technical engineering schematic, publication-grade, white (#ffffff) background, landscape 16:9. Title at top center in bold navy (#0f1e2e) Inter typeface: "Dual-Pass RO Train". LEFT HALF, labeled "PASS 1" in clinical teal (#1a6b72): a tapered ("Christmas tree") array of horizontal cylindrical membrane-housing icons arranged in three stages — first stage 3 housings side by side, second stage 2 housings, third stage 1 housing, all connected by thin navy pipe lines narrowing stage to stage — with a small Manrope-typeface annotation beneath: "Typical recovery 50–75%. Antiscalant dosed ahead of Pass 1." A bold navy arrow from the Pass-1 permeate line leads to a small pump icon at the center of the canvas labeled "Interstage booster pump" with annotation "Repressurizes low-pressure Pass-1 permeate for Pass-2 operating pressure." RIGHT HALF, labeled "PASS 2" in clinical teal: a single straight row of 2 horizontal cylindrical membrane-housing icons (no tapering), with annotation beneath: "Typical recovery 85–90%+. Antiscalant usually unnecessary — feed is already low-TDS." From the Pass-1 reject line (drawn exiting the bottom of the Pass-1 array), a thin dashed navy arrow curves along the bottom of the canvas back to blend into the Pass-1 feed line at the far left, labeled small in amber (#b8860b): "Optional reject recirculation — verify no species reconcentration first." From the Pass-2 permeate line at the far right, a bold arrow exits the frame labeled "To storage / distribution loop". Generous whitespace, rounded/clean line-art icons (not photorealistic), mobile-readable labels using Inter (titles) and Manrope (annotations) only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid photorealistic equipment renders (icons must stay simple line-art/schematic), avoid drawing Pass 2 as tapered (it must read as a single straight stage, visually distinct from Pass 1's taper), avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter and Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, engineering-plausible, visually calm, publication-grade. Background must be white — never dark. Pass 1's taper and Pass 2's single stage must be visually unmistakable as different array designs. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 10 — Water Quality Tiers: Dialysis Water to Ultrapure (§7)

**IMAGE NUMBER:** 10
**SECTION PLACEMENT:** `#sec-standards` — immediately after the section's opening paragraph, before the §7.1 microbiological limits table
**FILE NAME:** `wts-water-quality-tiers.png`
**ARCHETYPE:** Reference Card — Ascending Tiers (Scaffold E, arranged vertically as a staircase/pyramid)
**AUDIENCE:** Dialysis nurses, technicians, biomedical engineers, nephrologists
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — three ascending tiers with limits annotated
- 3D component graphics: none
- algorithm/flowchart: none

**PURPOSE:** Fix the three-tier purity hierarchy — and which tier is required for which use — permanently in memory, since the guide's tables present the same numbers in a format that's easy to look up but hard to remember unprompted.

**KEY CONCEPTS:** Dialysis water (product water; <100 CFU/mL, <0.25 EU/mL), standard dialysate (<100 CFU/mL, <0.5 EU/mL), ultrapure dialysis water/dialysate (<0.1 CFU/mL, <0.03 EU/mL, required for online HDF) — ascending purity, ascending stringency, top tier gated behind UF/POU filtration.

**DIMENSIONS:** 1536 × 1152 px

**ALT-TEXT SEED:** A three-tier ascending reference card showing hemodialysis water quality purity levels — dialysis water, standard dialysate, and ultrapure dialysate — each with its bacteria and endotoxin limits, with ultrapure marked as required for online HDF.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-water-quality-tiers.png
IMAGE TYPE: Reference Card — Ascending Purity Tiers
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152

AUDIENCE: Dialysis nurses, technicians, biomedical engineers, nephrologists
VISUAL GOAL: Fix the three-tier water-purity hierarchy and its numeric limits in memory as a single ascending visual, not a table to look up.

PROMPT:
Clean clinical reference-card infographic, publication-grade, white (#ffffff) background, 4:3 aspect. Title at top in bold navy (#0f1e2e) Inter typeface: "Water Quality Tiers". Below the title, THREE horizontal bar-shaped tiers stacked like ascending stairs from bottom-left to top-right, each tier a rounded rectangle, each one narrower and positioned higher than the one before, connected by a thin upward navy arrow on the left side labeled small "Increasing purity":
BOTTOM (widest) tier, light gray (#f3f4f6) fill: label "Dialysis water (product water)" in navy, with two small stat badges reading "< 100 CFU/mL" and "< 0.25 EU/mL".
MIDDLE tier, light teal tint (#eef6f7) fill: label "Standard dialysate" in navy, with two stat badges reading "< 100 CFU/mL" and "< 0.5 EU/mL".
TOP (narrowest) tier, warm gold tint fill: label "Ultrapure dialysis water / dialysate" in navy bold, with two stat badges reading "< 0.1 CFU/mL" and "< 0.03 EU/mL", and a small badge beside it in clinical teal (#1a6b72) reading "Required for online HDF".
Each stat badge is a small rounded pill shape with the number in bold Inter typeface. At the very bottom of the card, a thin full-width strip in soft gray with a brief italic Manrope-typeface note in navy: "The action level is a trigger, not a pass mark — investigate at roughly half the maximum, before the limit is ever crossed." Generous whitespace, clean rounded shapes, mobile-readable labels using Inter (tier labels, stat numbers) and Manrope (footnote) only. Bottom-right corner: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable numbers, avoid AI gibberish text, avoid a literal 3D pyramid render (this is a flat 2D staircase of bars), avoid overprocessed HDR, avoid excessive saturation, avoid more than 3 tiers. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter and Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, clinically accurate against the source guide's numbers, visually calm, publication-grade. Background must be white — never dark. The ascending purity order (bottom = least strict, top = ultrapure) must be immediately legible. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 11 — Troubleshooting Decision Flow: The Golden Rule (§9)

**IMAGE NUMBER:** 11
**SECTION PLACEMENT:** `#sec-trouble` — directly beneath the "Golden rule" alert box, before the §9.1 water-chemistry troubleshooting table
**FILE NAME:** `wts-golden-rule-decision-flow.png`
**ARCHETYPE:** Clinical Algorithm / Decision Flowchart (Scaffold A)
**AUDIENCE:** Dialysis nurses and technicians making real-time go/no-go decisions
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: none (pure flowchart)
- 3D component graphics: none
- algorithm/flowchart: primary mode — single top-to-bottom decision path

**PURPOSE:** Convert the guide's "Golden rule" alert box and its paired "Four things that mean STOP" list into a literal decision path staff can mentally run through in seconds during a real-time water-quality concern, rather than re-reading two separate call-out boxes.

**KEY CONCEPTS:** Four STOP triggers (total chlorine >0.1 mg/L post-carbon; patient fever/chills/rigors/hypotension during or after a run; any positive disinfectant residual at an outlet pre-use; a microbiological/chemical result above limit or a visible leak/biofilm) feeding into one escalation action; absence of all four triggers permits continued routine monitoring.

**DIMENSIONS:** 1024 × 1536 px (portrait)

**ALT-TEXT SEED:** A portrait decision flowchart for hemodialysis water treatment troubleshooting — four stop triggers (chlorine above limit, pyrogenic reaction symptoms, positive disinfectant residual, or an above-limit result or leak) leading to stopping and escalating, otherwise continue routine monitoring.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: wts-golden-rule-decision-flow.png
IMAGE TYPE: Clinical/Engineering Decision Flowchart
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536

AUDIENCE: Dialysis nurses and technicians
VISUAL GOAL: Convert the guide's Golden Rule and four STOP triggers into a single decision path staff can run through in seconds under time pressure.

PROMPT:
Clinical/engineering decision-flowchart infographic, KDIGO-guideline aesthetic, portrait 2:3, white (#ffffff) background. Title at top in bold navy (#0f1e2e) Inter typeface: "Golden Rule — Is Water Quality in Doubt?". Below the title, a single top-to-bottom pathway. First node: a wide rounded navy-outlined question node reading "Any of the four signs below present?" Below it, in a single column, FOUR compact amber (#b8860b) trigger cards stacked vertically, each with a small warning-triangle icon and short Manrope-typeface text: "1. Total chlorine > 0.1 mg/L after carbon tanks"; "2. Patient fever, chills, rigors, or hypotension during/after a run"; "3. Any positive disinfectant residual at an outlet before use"; "4. A result above limit, or a visible leak/biofilm". A bold navy bracket visually groups all four cards and feeds them into ONE downward arrow. That arrow splits into two outcome paths side by side near the bottom: LEFT path, labeled "YES — any one present", leads to a wide rounded node filled clinical red (#b91c1c) with white bold text: "STOP. Take affected station(s)/system offline. Escalate to nurse-in-charge & medical director now." with a small stop-octagon icon. RIGHT path, labeled "NO — none present", leads to a rounded node filled renal green (#1f7a4d) with white bold text: "Continue routine monitoring and logging." with a small checkmark icon. Generous vertical whitespace between nodes, bold connecting arrows, no more than 4 trigger cards plus the two outcome nodes, mobile-readable labels using Inter (headings/outcome nodes) and Manrope (trigger card text) only. Bottom-center: small semi-transparent navy text at 70% opacity reading exactly "williamriveromd.com".

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid more than 4 trigger cards, avoid a branching/spaghetti flowchart (this is one linear question feeding two clean outcomes), avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter and Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, clinically accurate against the guide's own "Four things that mean STOP" list, visually calm, publication-grade. Background must be white — never dark. The STOP (red) and continue (green) outcomes must be immediately distinguishable by color alone. Copyright attribution williamriveromd.com must be visible bottom-center (portrait convention).
```

---

## Wiring notes (for whoever implements the images once generated)

1. **Hero (Image 2).** The guide currently ships with an image-less hero (`<div class="hero-grid"><aside class="hero-cards mode-physician">…</aside><div class="hero-copy">…</div></div>` — no `hero-figure`). Once the PNG/WebP pair exists, add a `<figure class="hero-figure">` as the **last** child of `.hero-grid` (after `.hero-copy`):
   ```html
   <figure class="hero-figure">
     <div class="hero-vignette">
       <picture>
         <source srcset="../images/dialysis-water-treatment-systems-vignette-hero.webp" type="image/webp">
         <img src="../images/dialysis-water-treatment-systems-vignette-hero.png" alt="A dialysis-unit water-treatment technician checking a reverse-osmosis skid's pressure gauges." width="2048" height="2048" fetchpriority="high" loading="eager">
       </picture>
     </div>
   </figure>
   ```
   Then run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, and `patch_hero_maxwidth.py` `--guide dialysis-water-treatment-systems.html` to lock in the standard hero-image conventions, and update `og:image`/`twitter:image` if the OG card path changes.

2. **In-body figures (Images 3, 4, 6–11).** Wire each with the house `<figure>` + lightbox-ready `<figcaption>` pattern (Rule 11):
   ```html
   <figure>
     <picture>
       <source srcset="../images/wts-treatment-train-flow.webp" type="image/webp">
       <img class="zoomable" src="../images/wts-treatment-train-flow.png" alt="…" loading="lazy" width="1792" height="1024">
     </picture>
     <figcaption>
       <p class="fig-desc">Plain-language description of the flow/diagram.</p>
       <dl class="fig-abbrevs">
         <dt>RO</dt><dd>Reverse osmosis</dd>
         <dt>UF</dt><dd>Ultrafiltration</dd>
       </dl>
     </figcaption>
   </figure>
   ```
   Suggested `fig-abbrevs` per figure: Image 4 (TDS, CaCO₃); Image 6 (RO); Image 7 (HBV, HCV, HIV); Image 8 (HDF, POU, UF, CFU, EU); Image 9 (RO, TDS); Image 10 (CFU, EU, HDF); Image 11 — none needed (plain-language node labels only).

3. **§6 image sequence.** Images 5, 7, 8, and 9 belong to the same section and read as an overview-then-detail sequence — place them in that order (5 → 7 → 8 → 9) interleaved with the §6.1/6.2/6.3 prose exactly as the manifest table's "Section anchor" column specifies, rather than clustering all four together. Don't place 7/8/9 before 5 — the detail images assume the reader has already seen the loop-level map.

4. **After wiring:** run `python3 patch_image_lightbox.py --guide dialysis-water-treatment-systems.html` to confirm the lightbox script tag (already present), `python3 validate_hero_grid.py` to confirm the hero-figure addition didn't break the grid, and re-run `patch_reading_time.py` (11 captions add a meaningful chunk of words to the count — expect the ~23 min estimate to tick up slightly).
