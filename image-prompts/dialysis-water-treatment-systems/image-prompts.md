# Image Prompts — Hemodialysis Water Treatment Systems
**Guide:** `guides/dialysis-water-treatment-systems.html`
**URL:** https://www.williamriveromd.com/guides/dialysis-water-treatment-systems
**Destination GPT:** https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Generated:** 2026-07-01
**Total images:** 5

---

## Visual aid architecture overview

**Audience:** Dialysis nurses and technicians (primary), nephrologists and biomedical/water-treatment engineers (secondary). This is a **single-mode clinician/technical operations reference** (`body class="physician-mode single-mode"`) — there is no patient-facing tab, so every image in this pack is technical/editorial, not warm patient-education imagery. No Filipino-patient-in-clinic imagery; the "cast" here is dialysis-unit technical staff and equipment.

**Core educational challenge.** The guide asks staff to hold a mental model of an entire engineered system — pretreatment → RO → storage/loop → UF — and to reason about how that system changes for different source waters (municipal, deep well, brackish, hard water) and different facility configurations (isolation bays, HDF, dual-pass RO). Three visual jobs fall out of that:

1. **Make the treatment train legible as a single left-to-right sequence** — nurses and techs think in checklists, not paragraphs; the flow diagram from §3 should read like a wall chart.
2. **Make the four source-water variants comparable at a glance** — the guide's key differentiator versus a generic WTS reference is that pretreatment design changes by source water; one comparison panel should let a reader instantly see what's added/changed per source.
3. **Make the facility-layout decisions (§6) — isolation-bay placement, HDF clustering, dual-pass RO — spatially concrete**, since these are physical/plumbing decisions that are easy to describe in prose but easy to get wrong in the field.

The pack carries the reader from "why the room exists" (hero) → "how the baseline system flows" (Fig. 1) → "how it changes by source water" (Fig. 2) → "how the loop is laid out for special cases" (Fig. 3).

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
| 5 | `#sec-layout` (§6 Facility Layout & Special Configurations) | `wts-facility-layout-isolation-hdf-dualpass.png` | Mechanism / Schematic Reference Diagram | 16:9 | 1792 × 1024 |

> **OG image:** Image 1 is the `og:image`. Set `og:image:width="1200"` and `og:image:height="630"` (already wired in the guide's `<head>`). Generate at exactly 1200 × 630 px.
> **Hero image:** Image 2 is the circular-vignette hero for `figure.hero-figure > .hero-vignette`. Render at 2048 × 2048, save as both `.png` and a WebP twin, and wire via `<picture><source srcset="../images/dialysis-water-treatment-systems-vignette-hero.webp" type="image/webp"><img src="../images/dialysis-water-treatment-systems-vignette-hero.png" width="2048" height="2048" fetchpriority="high" loading="eager"></picture>` inside the guide's currently-empty `<figure class="hero-figure">` slot (see "Wiring notes" at the end of this file — the guide was shipped without a hero-figure and needs this block added once the asset exists).
> Figures 3–5 are in-body illustrations, each paired with a `<figcaption><p class="fig-desc">…</p></figcaption>` per house Rule 11 when wired into the HTML (see wiring notes).

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

## IMAGE 5 — Facility Layout: Isolation Bay, HDF Cluster & Dual-Pass RO (§6)

**IMAGE NUMBER:** 5
**SECTION PLACEMENT:** `#sec-layout` — after the §6.1–6.3 prose, as a single unifying schematic before §7
**FILE NAME:** `wts-facility-layout-isolation-hdf-dualpass.png`
**ARCHETYPE:** Mechanism / Schematic Reference Diagram (floor-plan-adjacent, not photorealistic)
**AUDIENCE:** Biomedical engineers, facility planners, nephrologists, charge nurses
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: primary mode — a simplified schematic of the distribution loop as a ring, with three callout zones
- 3D component graphics: none (clean 2D schematic icons only)
- algorithm/flowchart: none

**PURPOSE:** Make three physically-distinct facility-layout decisions — where the isolation bay sits on the loop, where HDF stations cluster, and how a dual-pass RO train is arranged — visually concrete on one shared diagram, since these are spatial/plumbing decisions easy to get wrong from prose alone.

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

2. **In-body figures (Images 3–5).** Wire each with the house `<figure>` + lightbox-ready `<figcaption>` pattern (Rule 11):
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
   Image 4's abbreviation list should include TDS (total dissolved solids) and CaCO₃ (calcium carbonate); Image 5's should include HDF (hemodiafiltration) and RO.

3. **After wiring:** run `python3 patch_image_lightbox.py --guide dialysis-water-treatment-systems.html` to confirm the lightbox script tag (already present), `python3 validate_hero_grid.py` to confirm the hero-figure addition didn't break the grid, and re-run `patch_reading_time.py` (image captions add a few words to the count).
