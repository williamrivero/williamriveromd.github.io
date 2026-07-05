# Image Prompts — Dialyzer Reuse in Modern Times
**Guide:** `guides/dialyzer-reprocessing-reuse.html`
**URL:** https://renalcarematters.com/guides/dialyzer-reprocessing-reuse
**Destination GPT:** https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Generated:** 2026-06-29
**Total images:** 10

---

## Visual aid architecture overview

**Patient audience:** Filipino hemodialysis patients and their families — many will have wondered "is my filter being reused?" and quietly carried the worry for years. A secondary clinician audience reads the appendix; the visuals are tuned to the patient first.

**Core educational challenge.** Three abstract ideas have to land cleanly:

1. **What a dialyzer physically is** — most patients have only watched it from the chair and never seen one in their hand. Without a clear mental model of the hollow-fiber bundle and the semipermeable membrane, every later concept (TCV, integrity, residual germicide) floats.
2. **What "reprocessing" actually is, in order** — a sequence of six checks the dialyzer must pass each time before it ever touches their blood again. The visual goal is to convert "they wash and reuse it" into "they run it through a documented chain that any failure halts."
3. **Why the global story is split** — Japan, Australia and most of the EU have banned reuse; the US has retreated; much of the developing world (including the Philippines) practices it pragmatically. Climate has put it back on the high-income table. Patients deserve a single map and a single hierarchy that show where they sit.

The image pack carries the patient through that arc — anatomy → process → germicide history → world split → KDIGO hierarchy → honest balance sheet → Philippine bedside reality → six questions to ask.

**Design system.** All images use the williamriveromd.com house style — white/off-white backgrounds, navy (#0f1e2e) text, clinical teal (#1a6b72) headings, amber (#b8860b) caution, red (#b91c1c) danger, renal green (#1f7a4d) safe/positive. Filipino patients and clinicians throughout. Every image: `williamriveromd.com` attribution, bottom-right corner, ~70% opacity navy.

**Visual continuity with parent guide.** The KDIGO 5-step waste hierarchy (Image 7) intentionally echoes the Green Nephrology pyramid in palette and architecture so the two guides feel like one ecosystem.

---

## Image manifest

| # | Section anchor | File name | Archetype | Aspect | Dimensions |
|---|---|---|---|---|---|
| 1 | `<head>` og:image | `dialyzer-reprocessing-reuse-og.png` | OG / Social Share | 1.91:1 | 1200 × 630 |
| 2 | `#hook` hero (LCP) | `dialyzer-reprocessing-reuse-hero.png` | Photorealistic Editorial Hero | 1:1 | 1254 × 1254 |
| 3 | `#what-dialyzer` | `dialyzer-anatomy-cross-section.png` | 3D Component Anatomy | 16:9 | 1792 × 1024 |
| 4 | `#what-dialyzer` (membrane sub-callout) | `dialyzer-biocompatible-vs-cellulose.png` | Comparative Mechanism Card | 4:3 | 1536 × 1152 |
| 5 | `#process` | `dialyzer-reprocessing-6-steps.png` | Multi-Panel Process Infographic | 16:9 | 1792 × 1024 |
| 6 | `#germicides` | `dialyzer-germicide-history-matrix.png` | Clinical Reference Card | 4:3 | 1536 × 1152 |
| 7 | `#renaissance` | `dialyzer-reuse-kdigo-waste-hierarchy.png` | Conceptual Pyramid Infographic | 2:3 portrait | 1024 × 1536 |
| 8 | `#walked-away` & `#renaissance` (paired) | `dialyzer-reuse-global-regulatory-map.png` | Cartographic Reference Card | 16:9 | 1792 × 1024 |
| 9 | `#honest` | `dialyzer-reuse-honest-balance-scale.png` | Conceptual Editorial Diagram | 1:1 | 1024 × 1024 |
| 10 | `#philippines` | `dialyzer-reuse-philippine-clinic-vignette.png` | Photorealistic Editorial Scene | 16:9 | 1792 × 1024 |
| 11 | `#philippines` (questions checklist) | `dialyzer-reuse-questions-to-ask-card.png` | 6-Icon Pictogram Card | 4:3 | 1536 × 1152 |

> **OG image:** Image 1 (`dialyzer-reprocessing-reuse-og.png`) is the `og:image`. Meta tags `og:image:width="1200"` and `og:image:height="630"`. Generate at exactly 1200 × 630 px.
> **Hero image (LCP):** Image 2 (`dialyzer-reprocessing-reuse-hero.png`) is the inline hero — render at 1254 × 1254; embed with `fetchpriority="high" loading="eager"`; cap CSS at `max-width:600px` centered.
> Image counts as 11 because Image 4 is an inset sub-callout under §what-dialyzer — counted separately so the manifest matches one file = one row.

---

## IMAGE 1 — OG / Social Share Card

**IMAGE NUMBER:** 1
**SECTION PLACEMENT:** `<head>` og:image meta tag — social sharing preview (Facebook, X, LinkedIn, Messenger, iMessage)
**FILE NAME:** `dialyzer-reprocessing-reuse-og.png`
**ARCHETYPE:** Photorealistic Editorial — OG Card
**AUDIENCE:** General public, hemodialysis patients, caregivers, kidney-care community
**VISUAL MIX:**
- photorealistic models: none — product-style editorial photography of a single dialyzer
- 2D infographic: title + subtitle text panel on right third
- 3D component graphics: none (photographic dialyzer)
- algorithm/flowchart: none

**PURPOSE:** Stop-the-scroll social share preview that telegraphs the topic in one beat — "is my filter being reused, and is it safe?" — and immediately conveys clinical authority.

**KEY CONCEPTS:** Dialyzer (hemodialysis filter), single-patient reuse, patient name label, KDIGO 2026 reconsideration

**DIMENSIONS:** 1200 × 630 px

**ALT-TEXT SEED:** A reprocessed hemodialysis dialyzer on a clean white surface, labeled with a patient's name and reuse count — the central object of the new williamriveromd.com guide on dialyzer reprocessing in 2026.

**OG SUITABILITY:** Yes — this image is the canonical og:image for the guide. Target file size ≤ 200 KB after PNG optimization.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reprocessing-reuse-og.png
IMAGE TYPE: OG Social Share Card — Editorial Photographic
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630

AUDIENCE: Filipino hemodialysis patients, caregivers, kidney-care community, general public
VISUAL GOAL: Premium social share card that immediately communicates the topic — dialyzer reuse, single-patient, labeled — and builds clinical trust in a single glance.

PROMPT:
Premium medical editorial social share card, 1200 × 630 pixels, clean bright white background (#ffffff) with a subtle off-white #fafafa floor tone. LEFT TWO-THIRDS: photographic editorial product shot of a single modern hemodialysis dialyzer (translucent polysulfone hollow-fiber cartridge, clear plastic housing, blue and red end caps for blood inlet/outlet, white caps for dialysate ports), lying flat on a clean white seamless surface, lit with soft natural daylight, gentle realistic shadow. The dialyzer carries a clean, professionally printed adhesive label wrapped around the housing showing in legible text "PATIENT: M. SANTOS / DOB 14-MAR-1962" on one line and "REUSE COUNT: 7 / DATE: 28 JUN 2026" on the next line, with a small QR code square; the label looks hospital-grade, not toy. Subtle teal accent stripe at one end of the label. RIGHT ONE-THIRD: clean white panel with sharp readable typography — Large bold condensed sans-serif title in navy (#0f1e2e): "Dialyzer Reuse in Modern Times"; below it in clinical teal (#1a6b72), medium weight: "Is it making a comeback?"; below that a thin teal horizontal rule; then small navy text: "W. G. M. Rivero, MD · Nephrology"; below that in light navy: "A companion to Green Nephrology 2026". Bottom-right corner: very small semi-transparent navy text "williamriveromd.com" at 70% opacity. White and off-white background ONLY — no dark backgrounds. Premium healthcare publication aesthetic, warm and trustworthy, evidence-of-craft mood — never clinical-cold.

NEGATIVE INSTRUCTIONS: Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text on the label (the patient name and reuse count must be clearly legible printed text, not garbled), avoid unrealistic anatomy or product, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation, avoid any second dialyzer (only one in frame). NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable when shrunk to a small social-share thumbnail, clinically plausible, visually calm, publication-grade. Background must be white — never dark. The patient name on the label must read as a real printed label (not jumbled letters). Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 2 — Guide Hero (Inline LCP, Square)

**IMAGE NUMBER:** 2
**SECTION PLACEMENT:** Top of guide, immediately after the hero text block — first image the patient sees, will be the LCP (largest contentful paint) image on the page
**FILE NAME:** `dialyzer-reprocessing-reuse-hero.png`
**ARCHETYPE:** Photorealistic Editorial Hero — Square
**AUDIENCE:** Hemodialysis patients and caregivers landing on the guide
**VISUAL MIX:**
- photorealistic models: hands of a Filipino dialysis nurse, no faces — focus stays on the dialyzer
- 2D infographic: minimal — a small teal "Dialyzer Reuse · Patient Guide" badge top-left
- 3D component graphics: the dialyzer itself, photographed photorealistically with a visible patient-name label
- algorithm/flowchart: none

**PURPOSE:** Settle the reader. Patients arriving here are often already worried. The hero must say, in one image: *this is your dialyzer, it has your name on it, it is being handled carefully.* Calm authority over drama.

**KEY CONCEPTS:** Single-patient labeling, careful hands, dialysis-unit cleanliness, dignity

**DIMENSIONS:** 1254 × 1254 px

**ALT-TEXT SEED:** A Filipino dialysis nurse's gloved hands holding a labeled, reprocessed hemodialysis dialyzer with the patient's name visible — a visual anchor for the new williamriveromd.com guide on dialyzer reprocessing.

**OG SUITABILITY:** Not the primary OG card (that is Image 1), but acceptable as a fallback hero crop if needed.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reprocessing-reuse-hero.png
IMAGE TYPE: Photorealistic Editorial Hero — Square (LCP)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1254 × 1254

AUDIENCE: Filipino hemodialysis patients, families, caregivers — landing on the guide
VISUAL GOAL: Warm, calm editorial hero that, in one glance, tells the patient: "this is your dialyzer, your name is on it, it is being handled by careful hands."

PROMPT:
Photorealistic medical editorial hero image, 1254 × 1254 pixels, clean bright white and very soft off-white background with natural daylight. Center of frame: the gloved hands of a Filipino dialysis nurse (light blue nitrile gloves, sleeves of a clean teal scrub visible at the wrist, no face shown) carefully holding a single modern hemodialysis dialyzer in two hands at chest height. The dialyzer is a translucent polysulfone hollow-fiber cartridge with clear plastic housing, blue and red end caps, white dialysate caps — visibly clean, water droplets implying a recent rinse. Wrapped around the housing is a hospital-grade adhesive label clearly showing printed text: "PATIENT: M. SANTOS" on one line and "REUSE: 7  /  28-JUN-2026" on the next line, with a small QR code square — the label reads as real printed text, not garbled. Background: softly out-of-focus modern Philippine dialysis unit interior — light walls, a glimpse of a dialysis chair and machine column, bright daylight from a window — all rendered with shallow depth of field so the dialyzer and hands remain the hero. Top-left corner: small teal pill badge "Dialyzer Reuse · Patient Guide" in white text. Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White / off-white background dominates. Premium healthcare editorial photography mood — calm, dignified, trustworthy, never alarming.

NEGATIVE INSTRUCTIONS: Avoid showing the patient's face, avoid showing other patients or visible identifying staff faces, avoid clutter, avoid clinical-cold sterile look, avoid dramatic lighting, avoid garbled text on the label, avoid cartoon style, avoid overprocessed HDR. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: Must be mobile-readable, clinically plausible, visually calm, publication-grade. Background must be white or soft off-white — never dark. The "PATIENT: M. SANTOS" label must be clearly legible. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 3 — Dialyzer Anatomy & Physics (Cross-Section + Mechanisms)

**IMAGE NUMBER:** 3
**SECTION PLACEMENT:** `#what-dialyzer` — under the H2 "What a dialyzer actually does"; replaces or complements the three-card mechanism block
**FILE NAME:** `dialyzer-anatomy-cross-section.png`
**ARCHETYPE:** 3D Component Anatomy + Mechanism Poster
**AUDIENCE:** Patients first (must be intuitive) and clinicians (must be accurate)
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: labeled callouts, mini-legend for diffusion / ultrafiltration / convection
- 3D component graphics: a partially cut-away photorealistic dialyzer revealing the hollow-fiber bundle; magnified inset of two adjacent hollow fibers with blood flowing inside, dialysate flowing outside
- algorithm/flowchart: none

**PURPOSE:** Build the mental model that everything later in the guide depends on. After looking at this image once, a patient should be able to point to where their blood goes, where the dialysate goes, and what crosses the membrane.

**KEY CONCEPTS:** Hollow-fiber bundle, semipermeable membrane, countercurrent flow (blood vs dialysate), diffusion of small toxins, ultrafiltration of water, convection of middle molecules

**DIMENSIONS:** 1792 × 1024 px (16:9 landscape)

**ALT-TEXT SEED:** Cross-sectional 3D diagram of a hemodialysis dialyzer showing the bundle of hollow fibers, with a magnified inset of a single fiber illustrating diffusion, ultrafiltration, and convection across the semipermeable membrane.

**OG SUITABILITY:** No — too dense for social share.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-anatomy-cross-section.png
IMAGE TYPE: 3D Component Anatomy + Mechanism Poster
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Filipino hemodialysis patients (primary), clinicians (secondary)
VISUAL GOAL: Build the patient's mental model of what a dialyzer is and what is happening inside it — so every later concept in the guide has somewhere to attach.

PROMPT:
Premium medical educational poster, 1792 × 1024 pixels, clean bright white background (#ffffff). LEFT 55% of the frame: a large semi-photorealistic 3D rendering of a complete hemodialysis dialyzer cartridge lying horizontally, with the front face cut away to reveal the densely packed bundle of thousands of fine translucent hollow fibers running end to end inside. Render the housing as clear plastic, the hollow fibers as fine pale-blue translucent tubes, the potting compound at both ends (urethane) as a clean white disc holding the fibers in place. Blood inlet end cap rendered in clinical red, blood outlet end cap in deep clinical red on the opposite end; dialysate ports on the side rendered in clinical teal. Show subtle directional arrows on the cartridge: a red arrow indicating blood flow INSIDE the fibers in one direction, and a teal arrow indicating dialysate flow OUTSIDE the fibers in the OPPOSITE direction (countercurrent). Clean labels in navy (#0f1e2e) sans-serif pointing to: "Blood inlet (your blood enters)", "Hollow fibers (thousands)", "Semipermeable membrane wall", "Dialysate (clean salt solution)", "Blood outlet (back to you)". RIGHT 45% of the frame: a single large magnified inset of TWO adjacent hollow fibers, photorealistic-illustrative style, with the membrane wall rendered as a textured semipermeable barrier. Show three small mechanism cards stacked vertically, each with a tiny diagram and a one-line label: (1) navy/teal card "DIFFUSION — urea, creatinine, potassium move from your blood across the membrane to the dialysate"; (2) navy/teal card "ULTRAFILTRATION — pressure pushes excess water out of your blood"; (3) navy/teal card "CONVECTION — water dragged across the membrane carries middle-sized toxins with it". Top of the entire image: navy bold title "Inside a dialyzer". Below the title in clinical teal subhead: "Thousands of hollow fibers, one semipermeable membrane, three ways your blood gets cleaner." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background throughout, generous whitespace, no clutter.

NEGATIVE INSTRUCTIONS: Avoid garbled text on labels, avoid cartoon style, avoid clutter, avoid more than 5 labeled callouts on the main dialyzer, avoid showing realistic blood spatter, avoid medical horror imagery, avoid overprocessed HDR, avoid generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: A patient who has never seen a dialyzer up close must be able to explain the diagram back in one sentence after looking at it for 10 seconds. Anatomy must be clinically plausible (fibers run end to end inside the housing; dialysate flows outside the fibers and counter to blood flow). Background must be white — never dark. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 4 — Biocompatible vs Cellulose Membrane Comparison

**IMAGE NUMBER:** 4
**SECTION PLACEMENT:** `#what-dialyzer` — inside or directly under the amber callout "Why the membrane material matters for the reuse story"
**FILE NAME:** `dialyzer-biocompatible-vs-cellulose.png`
**ARCHETYPE:** Comparative Mechanism Card (two-column poster)
**AUDIENCE:** Patients first (why does material matter), clinicians (first-use syndrome)
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: two-column comparison layout
- 3D component graphics: matched magnified cross-section renderings of (left) older cellulose fiber and (right) modern polysulfone fiber, with stylized immune cells reacting to one vs being calm at the other
- algorithm/flowchart: none

**PURPOSE:** Explain why the membrane material is the hidden hinge of the reuse story — older cellulose membranes provoked first-use syndrome, biocompatible synthetics do not, and that single technical change removed one of the original medical arguments for reuse.

**KEY CONCEPTS:** Cellulose vs polysulfone / polyethersulfone, complement activation, first-use syndrome, biocompatibility, immunological neutrality

**DIMENSIONS:** 1536 × 1152 px (4:3)

**ALT-TEXT SEED:** Side-by-side comparison of an older cellulose hemodialysis membrane provoking an immune reaction on first use versus a modern biocompatible polysulfone membrane that does not — the technical change that quietly weakened the original case for dialyzer reuse.

**OG SUITABILITY:** No.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-biocompatible-vs-cellulose.png
IMAGE TYPE: Comparative Mechanism Card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152

AUDIENCE: Hemodialysis patients (primary), trainees (secondary)
VISUAL GOAL: Explain in one image why "modern membranes are biocompatible" matters — older cellulose triggered first-use reactions; modern polysulfone does not.

PROMPT:
Clean two-column educational comparison poster, 1536 × 1152 pixels, white background (#ffffff). Top of the image: navy bold sans-serif title "The membrane that changed the argument" with a clinical teal subhead "Why modern dialyzers don't need 'breaking in' the way old ones did". A vertical hairline rule splits the canvas exactly in half. LEFT COLUMN HEADER (amber-tinted card): "Older cellulose membrane (1980s–early 90s)". Below it: a semi-photorealistic 3D magnified cross-section of a single hollow fiber wall labeled "cellulose", textured to look slightly fibrous. Around the OUTSIDE of the membrane (the blood side), render small stylized immune complement proteins as soft orange/amber spheres clustering on the surface and a few activated neutrophils nearby — a visible but tasteful "reaction". A small navy callout beneath reads: "First-use syndrome — complement activation, sometimes flu-like reactions on the very first treatment." A second small callout: "Reusing the same dialyzer dampened the reaction — one of the historical arguments for reuse." Use the amber palette accent (#b8860b) for this side. RIGHT COLUMN HEADER (teal-tinted card): "Modern biocompatible synthetic (polysulfone / PES, today)". Below it: a matched magnified cross-section of a single hollow fiber wall labeled "polysulfone", rendered cleaner and smoother. Around the outside of the membrane, the immune cells are calm, scattered, not clustering — no visible reaction. A navy callout beneath reads: "No meaningful first-use reaction — immune-quiet on the first treatment." A second callout: "Removes the original immunologic argument for reuse — leaving cost and sustainability as the live ones." Use the teal palette accent (#1a6b72) for this side. Bottom of image, full width: a single navy take-home strip "The medical case for reuse eroded as the membrane improved — not because reuse stopped working, but because the problem reuse used to solve mostly went away." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background throughout, generous whitespace.

NEGATIVE INSTRUCTIONS: Avoid horror imagery, avoid blood spatter, avoid garbled text on labels, avoid cartoon style, avoid clutter, avoid more than two callouts per side, avoid implying that cellulose membranes were "bad" — the language must be neutral and historical. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: A reader should be able to look at this image and answer "why does membrane material matter in the reuse story?" in one sentence. Both sides must be visually balanced — not "good vs bad" but "old vs modern". Background must be white. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 5 — The 6-Step Reprocessing Chain

**IMAGE NUMBER:** 5
**SECTION PLACEMENT:** `#process` — directly under the H2 "What 'reprocessing' actually means"; replaces the 6 numbered text steps as a single scannable visual
**FILE NAME:** `dialyzer-reprocessing-6-steps.png`
**ARCHETYPE:** Multi-Panel Process Infographic (numbered horizontal chain)
**AUDIENCE:** Patients (primary), with enough rigor for clinicians
**VISUAL MIX:**
- photorealistic models: none — the dialyzer itself appears in each step
- 2D infographic: 6 numbered cards in a horizontal chain joined by arrows
- 3D component graphics: small dialyzer rendering inside each step card, showing the relevant action (rinse, gauge, pressure test, dwell, label, residual test)
- algorithm/flowchart: yes — a strict left-to-right chain

**PURPOSE:** Convert the abstract claim "they wash and reuse it" into a documented, six-link chain that any failure halts. The patient should walk away with the sequence in their head.

**KEY CONCEPTS:** Reverse rinse, total cell volume (TCV ≥ 80%), integrity/leak test, germicide dwell, labeled storage, pre-use rinse + residual germicide test

**DIMENSIONS:** 1792 × 1024 px (16:9 landscape)

**ALT-TEXT SEED:** Six numbered steps of the dialyzer reprocessing chain — reverse rinse, total cell volume test, pressure leak test, germicide dwell, labeled storage, and pre-use residual germicide test — shown as a left-to-right infographic.

**OG SUITABILITY:** No — process detail is wrong for social.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reprocessing-6-steps.png
IMAGE TYPE: Multi-Panel Process Infographic — Numbered Horizontal Chain
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Filipino hemodialysis patients, families, dialysis nurses
VISUAL GOAL: Show, in a single scannable image, the six documented checks a dialyzer must pass each cycle before it touches the patient's blood again.

PROMPT:
Premium medical process infographic, 1792 × 1024 pixels, clean white background (#ffffff). Top of image: navy bold sans-serif title "Reprocessing a dialyzer — the six-step chain"; subhead in clinical teal: "Any failure halts the chain. The dialyzer is retired, not reused." Below the title: six rounded modular cards arranged in a single horizontal chain joined by small teal right-arrows, each card 1/6 of the width, equal size, generous whitespace inside each card. Number each card with a large navy circle "1" through "6" in the top-left of the card. Inside each card: a small clean semi-photorealistic 3D illustration of the action being performed (the dialyzer is shown in each, in the relevant configuration), and below the illustration a short bold navy title and a one-line clinical-teal description. The six cards, in order:
1) "Reverse rinse & clean" — dialyzer with water flowing backward through both ports, faint residual blood clearing.
2) "TCV — fiber-bundle volume ≥ 80%" — dialyzer being measured by an automated reprocessing machine, with a small inline gauge graphic showing a needle in the green zone above 80%.
3) "Pressure / leak test" — dialyzer pressurized, small pressure dial reading stable, with a green check beside it.
4) "Germicide dwell" — dialyzer filled and capped with a translucent peracetic-acid-colored fluid, a small teal label reading "Peracetic acid (most common)".
5) "Labeled & stored" — dialyzer with a clear hospital adhesive label "PATIENT: M. SANTOS · REUSE: 7", being placed on a clean labeled shelf rack.
6) "Pre-use rinse + residual germicide test" — dialyzer being rinsed at the chairside, with a small test strip showing a green "below safe limit" indicator.
Below the six-card chain, full width: a single navy strip "Governed by ANSI/AAMI RD47:2020. Water quality by ISO 23500-3." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background dominates, navy/teal accents only, no dark fills.

NEGATIVE INSTRUCTIONS: Avoid more than six steps, avoid garbled text in the labels or gauge numbers, avoid cartoon style, avoid clinical-horror lighting, avoid showing blood, avoid clutter, avoid making any card visually heavier than the others. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: A patient who reads only this image should be able to list, in order, all six steps. Visual rhythm must read strictly left-to-right with equal-weight cards. Background must be white — never dark. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 6 — Germicide History & Comparison Matrix

**IMAGE NUMBER:** 6
**SECTION PLACEMENT:** `#germicides` — under the H2 "The germicides — then and now"; replaces or augments the 4-row table
**FILE NAME:** `dialyzer-germicide-history-matrix.png`
**ARCHETYPE:** Clinical Reference Card with embedded mini-chart
**AUDIENCE:** Patients (primary), clinicians (secondary)
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: 4-card matrix + inset trend mini-chart
- 3D component graphics: small stylized chemical vials/icon for each germicide
- algorithm/flowchart: none

**PURPOSE:** Tell the modernization story in one image — formaldehyde dominated in 1983 (~94%), peracetic acid won by 2002 (~72%) and remains dominant — and show, side by side, why peracetic acid won.

**KEY CONCEPTS:** Peracetic acid (Renalin), formaldehyde, glutaraldehyde, heat + citric acid; year-over-year shift from formaldehyde → peracetic acid; ClearFlux on the horizon

**DIMENSIONS:** 1536 × 1152 px (4:3)

**ALT-TEXT SEED:** Comparison matrix of the four germicides used to disinfect reprocessed dialyzers — peracetic acid, formaldehyde, glutaraldehyde, heat + citric acid — with a small chart showing formaldehyde's decline from ~94% of US units in 1983 to ~20% by 2002 and peracetic acid's rise to dominance.

**OG SUITABILITY:** No.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-germicide-history-matrix.png
IMAGE TYPE: Clinical Reference Card — 4-Card Comparison Matrix with Inset Trend Chart
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152

AUDIENCE: Hemodialysis patients and clinicians
VISUAL GOAL: Tell the germicide-modernization story in one image — formaldehyde dominated, peracetic acid won, the residue profile is the reason.

PROMPT:
Clinical reference infographic, 1536 × 1152 pixels, clean white background (#ffffff). TOP-LEFT: navy bold sans-serif title "The germicides — then and now". TOP-RIGHT (inset, ~30% width): a small clean trend chart titled in clinical teal "US dialyzer reuse, primary germicide", x-axis years 1983 → 2002 → present, two lines — a falling amber line labeled "Formaldehyde 94% → ~20%" and a rising teal line labeled "Peracetic acid → ~72%, dominant since mid-1980s". MAIN BODY: a 2×2 grid of four equal cards with rounded corners and light gray borders, each card with a header strip, a small icon, three short bullets, and a single-line trade-off footer. Use the palette consistently:
- Card 1 (top-left, teal-accented, marked "★ DOMINANT TODAY"): "Peracetic acid (e.g., Renalin)" — icon: a small clear vial with a teal liquid. Bullets: "Strong oxidizer, broad-spectrum"; "Breaks down to water, oxygen, acetic acid"; "Low occupational toxicity". Footer: "Residual germicide test before reuse."
- Card 2 (top-right, amber-accented, marked "HISTORICAL"): "Formaldehyde" — icon: a small amber-tinted vial with a clear caution stripe. Bullets: "Protein cross-linking; cidal"; "Known occupational carcinogen"; "Use plunged from ~94% (1983) to ~20% (2002)". Footer: "Strict residual + exposure limits."
- Card 3 (bottom-left, amber-accented, marked "NICHE"): "Glutaraldehyde" — icon: small vial with mild amber liquid. Bullets: "Protein cross-linking"; "Effective alternative to formaldehyde"; "Irritant; staff sensitization risk". Footer: "Largely a niche choice today."
- Card 4 (bottom-right, green-accented, marked "CHEMICAL-FREE"): "Heat + citric acid" — icon: small stylized heater + citrus. Bullets: "Thermal kill plus mild acid"; "No toxic chemical residue"; "Energy-intensive; equipment-specific". Footer: "Less broadly adopted."
Below the grid, a single navy take-home strip: "Whatever agent is used, the rule is the same — a residual test confirms it is below the safe limit before your next treatment." A small teal sub-line: "Looking ahead: automated systems like ClearFlux aim for a safer, greener chemical profile per cycle." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background throughout, generous whitespace.

NEGATIVE INSTRUCTIONS: Avoid garbled text in chart labels or card text, avoid cartoon style, avoid showing real chemical hazard imagery (skull/crossbones), avoid more than three bullets per card, avoid clutter, avoid making any card visually dominate except the small "★ DOMINANT TODAY" tag on peracetic acid. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: A reader should be able to name the dominant modern germicide and the reason it won after a single look. The trend chart's two lines must clearly cross over time and be readable on mobile. Background must be white. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 7 — KDIGO 5-Step Waste Hierarchy (Pyramid) with "Reuse" Highlighted

**IMAGE NUMBER:** 7
**SECTION PLACEMENT:** `#renaissance` — under the H3 "Where reuse sits on the waste hierarchy"; visually echoes the Green Nephrology pyramid for cross-guide continuity
**FILE NAME:** `dialyzer-reuse-kdigo-waste-hierarchy.png`
**ARCHETYPE:** Conceptual Pyramid Infographic
**AUDIENCE:** Patients (primary), clinicians (recognize the KDIGO 2026 hierarchy)
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: vertical 5-tier pyramid with the second tier "Reuse" highlighted
- 3D component graphics: tier-2 highlight features a small 3D dialyzer icon to anchor the topic
- algorithm/flowchart: none

**PURPOSE:** Place dialyzer reuse precisely where KDIGO 2026 places it — tier 2 of 5 — and make clear that prevention still outranks reuse. Visually echoes the Green Nephrology guide's pyramid so the two guides feel like one ecosystem.

**KEY CONCEPTS:** Prevent → Reuse → Recycle → Recover → Dispose; greatest-impact-first; reuse is useful but not the top lever

**DIMENSIONS:** 1024 × 1536 px (2:3 portrait — pyramid composition)

**ALT-TEXT SEED:** KDIGO 2026 five-step waste hierarchy for dialysis — Prevent, Reuse, Recycle, Recover, Dispose — drawn as a pyramid with "Reuse" highlighted at tier 2, the position dialyzer reprocessing occupies.

**OG SUITABILITY:** No.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reuse-kdigo-waste-hierarchy.png
IMAGE TYPE: Conceptual Pyramid Infographic
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536

AUDIENCE: Patients and clinicians
VISUAL GOAL: Show, at a glance, that "Reuse" sits at tier 2 of the KDIGO 2026 waste hierarchy — useful, but only "Prevent" outranks it.

PROMPT:
Vertical conceptual hierarchy infographic, 1024 × 1536 pixels, clean white background (#ffffff). Top of image: navy bold sans-serif title "Where dialyzer reuse sits"; clinical teal subhead "KDIGO 2026 Green Dialysis waste hierarchy — greatest impact first". Center of canvas: a five-tier pyramid stacked vertically with the widest tier at the top (representing greatest impact) and the narrowest tier at the bottom. Render each tier as a horizontally-oriented trapezoidal band with a soft border, rounded corners, and the following color logic and labels:
- Tier 1 (top, widest, deep clinical teal #1a6b72 fill, white text): "1. PREVENT — the disposable that is never produced; the largest lever."
- Tier 2 (lighter teal fill, but VISIBLY HIGHLIGHTED with a thicker navy outline and a small floating navy ribbon to its right reading "You are here — dialyzer reprocessing"; navy text on light teal): "2. REUSE — clean, test, disinfect, re-use on the same patient."
- Tier 3 (amber-soft #fdf6e3 fill, navy text): "3. RECYCLE — recover plastics from blood lines and packaging where infrastructure allows."
- Tier 4 (amber-soft fill, navy text): "4. RECOVER — energy recovery from waste; last-line, low-yield."
- Tier 5 (bottom, narrowest, soft red-soft #fff5f5 fill, navy text): "5. DISPOSE — safe landfill or incineration."
Inside Tier 2, beside the band label, include a small clean 3D dialyzer icon (translucent housing, blue/red caps) to visually anchor the topic. To the LEFT of the pyramid, a thin vertical navy arrow pointing UP with the label "Greatest environmental impact"; to the RIGHT of the pyramid, a thin vertical navy arrow pointing DOWN with the label "Last resort". Bottom of image, full width: a single navy take-home strip "KDIGO 2026 explicitly endorses dialyzer reuse as a pragmatic cost and access strategy in LMICs — when done to standard." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background throughout, no dark fills.

NEGATIVE INSTRUCTIONS: Avoid more than five tiers, avoid making tier 2 the largest band (Prevent must remain the widest), avoid cartoon style, avoid garbled text, avoid clutter. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: A reader who has read only this image must be able to say "reuse is tier 2 — prevention still beats it." Visual hierarchy must read top-to-bottom with the top tier clearly the widest and most prominent. Background must be white. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 8 — Global Regulatory Split (World Map)

**IMAGE NUMBER:** 8
**SECTION PLACEMENT:** Paired across `#walked-away` and `#renaissance` — placed under the "hard line abroad" callout in §walked-away, referenced again in §renaissance
**FILE NAME:** `dialyzer-reuse-global-regulatory-map.png`
**ARCHETYPE:** Cartographic Reference Card
**AUDIENCE:** Patients (orient themselves on the global map), clinicians (regulatory split)
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: simplified world map with three-color shading + legend + small per-region callouts
- 3D component graphics: none
- algorithm/flowchart: none

**PURPOSE:** Make the global split visually unmistakable — Japan, Australia, most EU = prohibited; United States = declining minority practice; many LMICs including the Philippines = permitted and pragmatic.

**KEY CONCEPTS:** Regulatory geography of dialyzer reuse; LMIC pragmatism; high-income retreat; KDIGO 2026 endorsing reuse with conditions in LMICs

**DIMENSIONS:** 1792 × 1024 px (16:9 landscape)

**ALT-TEXT SEED:** Simplified world map showing the regulatory status of dialyzer reuse — prohibited in Japan, Australia, and most of the European Union; declining in the United States; permitted and pragmatic in many low- and middle-income countries including the Philippines.

**OG SUITABILITY:** No.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reuse-global-regulatory-map.png
IMAGE TYPE: Cartographic Reference Card
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Patients and clinicians
VISUAL GOAL: Show, in one map, the three-way global split on dialyzer reuse — and where the Philippines sits inside it.

PROMPT:
Educational world map infographic, 1792 × 1024 pixels, clean white background (#ffffff). Top of image: navy bold sans-serif title "Where in the world is dialyzer reuse allowed?"; clinical teal subhead "The global regulatory split — high-income retreat, LMIC pragmatism." MAIN BODY (left ~80%): a simplified flat-style world map (Robinson or equirectangular projection), country borders rendered as thin pale-gray lines on white background. Shade countries using three flat colors that match the house palette:
- Soft RED-SOFT (#fff0f0) fill with thin clinical-red border: countries where dialyzer reuse is PROHIBITED — explicitly include Japan, Australia, and most European Union member states (France, Germany, Italy, Spain, Netherlands, Belgium, Sweden, Poland, etc.; United Kingdom optional, follow EU palette). Label one country in each region with a small navy text tag "Prohibited".
- Soft AMBER-SOFT (#fffbeb) fill with thin amber border: the United States and a handful of high-income countries — labeled "Declining, minority practice".
- Soft TEAL-LIGHT (#e1f5f0) fill with thin teal border: many low- and middle-income countries, including the Philippines (highlight the Philippines with a slightly stronger teal outline and a small floating navy callout pin reading "PHILIPPINES — permitted, pragmatic, AAMI RD47 standard applies"). Other LMICs to shade: most of South Asia (India, Bangladesh, Pakistan), much of Southeast Asia, much of sub-Saharan Africa, much of Latin America.
- Countries with no clear data: light neutral gray (#f3f4f6).
LEGEND (top-right of map): three swatches with one-line labels matching the three colors above. RIGHT ~20%: a thin vertical sidebar with three stacked navy callout cards: (1) "Prohibited — Japan, Australia, most EU"; (2) "Declining — United States"; (3) "Permitted, pragmatic — many LMICs incl. PH". Bottom of image, full width: a single navy take-home strip "The reason everywhere was similar — with cheap, biocompatible single-use filters available, the infection and quality-control risks of reprocessing no longer looked worth the savings in high-income systems." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background throughout.

NEGATIVE INSTRUCTIONS: Avoid garbled country labels, avoid political color choices (no red-vs-blue partisan palette), avoid showing borders that imply unsettled territorial disputes prominently, avoid cartoon style, avoid 3D globe distortion, avoid clutter, avoid more than three shading colors plus the neutral gray. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: A Filipino reader must be able to find the Philippines on the map within two seconds. The three shading colors must be clearly distinguishable on a small mobile screen. Background must be white. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 9 — Honest-Accounting Balance Scale

**IMAGE NUMBER:** 9
**SECTION PLACEMENT:** `#honest` — under the H2 "But is the green case airtight? The honest accounting"
**FILE NAME:** `dialyzer-reuse-honest-balance-scale.png`
**ARCHETYPE:** Conceptual Editorial Diagram
**AUDIENCE:** Patients and clinicians
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: a clean conceptual balance/scale with labeled trays
- 3D component graphics: small 3D-style icons for plastic-waste stack vs water-drop + electricity-bolt + chemical-flask
- algorithm/flowchart: none

**PURPOSE:** Protect credibility — show that the environmental win from reuse is real but conditional. The plastic-and-carbon savings on one tray are weighed against the water, energy, and chemicals reprocessing itself consumes on the other.

**KEY CONCEPTS:** Conditional sustainability gain; reuse footprint vs single-use footprint; the gain depends on local water + energy mix and on QA discipline

**DIMENSIONS:** 1024 × 1024 px (1:1 square)

**ALT-TEXT SEED:** A clean conceptual balance scale weighing the environmental savings of dialyzer reuse (less plastic, less manufacturing carbon) against its own footprint (water for rinsing, electricity for the cycle, chemical germicides) — illustrating why the green case for reuse is real but conditional.

**OG SUITABILITY:** No.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reuse-honest-balance-scale.png
IMAGE TYPE: Conceptual Editorial Diagram — Balance Scale
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024

AUDIENCE: Patients and clinicians
VISUAL GOAL: Show, in one image, that the green case for reuse is real but conditional — savings on one side, reprocessing's own cost on the other.

PROMPT:
Conceptual editorial diagram, 1024 × 1024 pixels, clean white background (#ffffff). Top of image: navy bold sans-serif title "The honest accounting"; clinical teal subhead "Reuse saves — and reuse also costs. The net depends on how it is done." Center of canvas: a clean, elegant two-tray balance scale rendered in semi-photorealistic style, navy and brushed-metal palette, slightly tilted to the LEFT to indicate the savings tray is heavier — but only slightly tilted, not dramatically, to convey "real but conditional". LEFT TRAY (heavier, labeled in teal): a clean stacked composition of (a) a small pile of single-use dialyzers crossed out with a soft teal slash, (b) a small CO₂ cloud icon, (c) a small plastic-bag icon. Below the tray a teal label: "SAVED — single-use dialyzers not manufactured · less plastic to incinerate · lower transport emissions". RIGHT TRAY (lighter but visibly present, labeled in amber): a small composition of (a) a blue water droplet, (b) an electricity bolt icon, (c) a small chemistry flask icon. Below the tray an amber label: "SPENT — rinse water · cycle electricity · germicide manufacture, transport, and disposal". On either side of the scale, two thin navy guide rails labeled "Patient outcomes must hold either way — sustainability is a quality metric, not a substitute for it." Bottom of image, full width: a single navy take-home strip "Reuse is a tool, not a virtue — strongest where waste dominates and reprocessing is run on relatively clean water and energy." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background throughout, generous whitespace.

NEGATIVE INSTRUCTIONS: Avoid moralistic imagery (no halos, no devils), avoid dramatic over-tilt (the scale should be only slightly off-balance), avoid cartoon style, avoid clutter, avoid more than three icons per tray, avoid garbled labels. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: A reader must walk away with the idea "real saving, with a real footprint of its own". The scale must feel scientifically calm — not editorial-cartoonish. Background must be white. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 10 — Philippine Clinic Vignette (Editorial Scene)

**IMAGE NUMBER:** 10
**SECTION PLACEMENT:** `#philippines` — at the top of the section, before the "questions to ask" checklist
**FILE NAME:** `dialyzer-reuse-philippine-clinic-vignette.png`
**ARCHETYPE:** Photorealistic Editorial Scene
**AUDIENCE:** Filipino hemodialysis patients and families
**VISUAL MIX:**
- photorealistic models: Filipino nephrologist and Filipino patient at a dialysis chair
- 2D infographic: minimal — a small teal callout pointing to the dialyzer label
- 3D component graphics: the dialyzer on the dialysis machine is the same photorealistic asset used elsewhere in the pack, visibly labeled
- algorithm/flowchart: none

**PURPOSE:** Localize the entire conversation. After the global map and the conceptual diagrams, the patient sees the actual people having this conversation in a Philippine unit — the nephrologist explaining, the dialyzer labeled with the patient's name in clear view, the tone respectful and conversational.

**KEY CONCEPTS:** Filipino clinical setting, conversation not interrogation, the labeled dialyzer as proof of single-patient practice

**DIMENSIONS:** 1792 × 1024 px (16:9 landscape)

**ALT-TEXT SEED:** A Filipino nephrologist sitting beside a Filipino dialysis patient at the dialysis chair, calmly explaining the patient's reprocessed dialyzer — visibly labeled with the patient's name — mounted on the dialysis machine.

**OG SUITABILITY:** Acceptable secondary OG candidate if the primary is not used.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reuse-philippine-clinic-vignette.png
IMAGE TYPE: Photorealistic Editorial Scene
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024

AUDIENCE: Filipino hemodialysis patients and families
VISUAL GOAL: Localize the conversation — show the actual people, in a Philippine dialysis unit, having the talk this guide prepares the patient for.

PROMPT:
Photorealistic medical editorial scene, 1792 × 1024 pixels, clean bright white walls and natural daylight. Setting: a modern, well-kept Philippine outpatient hemodialysis unit — bright walls, light wood and clinical teal accents, a row of dialysis chairs visible softly in the background. Center foreground: a Filipino male nephrologist in his 40s, wearing a clean white coat over a light teal shirt, seated on a low stool next to a Filipino male patient in his late 50s who is comfortably reclined in a dialysis chair, blanket over his lap, an arteriovenous fistula on his left forearm with the dialysis lines connected and tracked toward the machine (not gory, soft focus on the line entry). The nephrologist is leaning slightly forward, hand resting open on the armrest, in mid-conversation — calm, respectful, attentive. The patient is listening, expression peaceful and engaged, not anxious. Mounted on the dialysis machine column directly above the patient's right shoulder: a single reprocessed dialyzer (translucent polysulfone, blue and red end caps), wrapped with a clean adhesive label clearly showing "PATIENT: M. SANTOS / REUSE: 7" — the label is the small visual hero of the image. A small teal callout arrow gently points from open negative space to the label, with a tiny navy line reading "Single-patient · labeled · logged". Background dialysis unit softly out of focus, no other identifiable patient faces. Natural soft daylight from a window on the left, no harsh shadows. Top-left corner: small teal pill badge "In the Philippines" in white text. Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White and soft off-white tones dominate; navy and teal accents only.

NEGATIVE INSTRUCTIONS: Avoid showing the patient's face in distress, avoid showing blood, avoid showing other identifiable patient faces in the background, avoid dramatic lighting, avoid clinical-cold sterility, avoid cartoon style, avoid clutter, avoid showing the nephrologist's screen or laptop prominently, avoid lab-coat overload (no white coats in the background). NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: The scene must feel like a conversation, not a procedure. The labeled dialyzer must be the second thing the eye finds (after the two people). Filipino identity must read clearly and respectfully. Background must be white-walled and bright. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## IMAGE 11 — "Questions to Ask Your Unit" — 6-Icon Pictogram Card

**IMAGE NUMBER:** 11
**SECTION PLACEMENT:** `#philippines` — directly under the dark "checklist" panel in the HTML (the six questions to ask the dialysis unit)
**FILE NAME:** `dialyzer-reuse-questions-to-ask-card.png`
**ARCHETYPE:** 6-Icon Pictogram Reference Card
**AUDIENCE:** Patients — meant to be screenshotted and brought to the next appointment
**VISUAL MIX:**
- photorealistic models: none
- 2D infographic: 6 numbered icon-cards in a 3×2 grid, each with one question
- 3D component graphics: small flat-iconographic component per question (no full 3D)
- algorithm/flowchart: none

**PURPOSE:** Turn the checklist into something portable — a screenshot a patient can show their nurse or nephrologist. Each question is one icon plus one sentence.

**KEY CONCEPTS:** Patient agency, six exact questions matching the in-guide checklist

**DIMENSIONS:** 1536 × 1152 px (4:3)

**ALT-TEXT SEED:** Six numbered icon cards laying out the six questions a hemodialysis patient should ask their dialysis unit about dialyzer reuse, including germicide, residual testing, reuse count, and access to their dialyzer log.

**OG SUITABILITY:** No.

---

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```
FILE NAME: dialyzer-reuse-questions-to-ask-card.png
IMAGE TYPE: 6-Icon Pictogram Reference Card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152

AUDIENCE: Hemodialysis patients (a screenshot they can show their nurse / nephrologist)
VISUAL GOAL: A portable, screenshot-ready card listing the six questions a patient should ask their unit about dialyzer reuse.

PROMPT:
Patient-agency pictogram reference card, 1536 × 1152 pixels, clean white background (#ffffff). Top of image: navy bold sans-serif title "Six questions to ask your dialysis unit"; clinical teal subhead "About dialyzer reuse — bring this card with you." Main body: a 3-column × 2-row grid of six equal-sized rounded cards with thin pale-gray borders, generous whitespace between cards. Each card contains:
- A large numbered teal circle ("1" through "6") top-left.
- A clean flat icon centered in the upper portion of the card, all icons drawn in matching navy line-art style with teal accent, simple and recognizable.
- A single short question in navy sans-serif text below the icon.

The six cards, in order, top-left to bottom-right:
1) Icon: a single dialyzer with a small question mark — Question: "Does this unit reuse dialyzers, or is it single-use only?"
2) Icon: a small chemistry vial labeled with a tiny "germicide" tag — Question: "If reuse — which germicide do you use, and how long is the contact time?"
3) Icon: a small dialyzer with a circular counter "#" — Question: "What is the maximum number of reuses per dialyzer in this unit?"
4) Icon: a small test strip with a checkmark — Question: "How is the residual germicide tested before each treatment?"
5) Icon: a clipboard with a small label icon — Question: "May I see my dialyzer's label and reuse log?"
6) Icon: a small dialyzer with a discard arrow — Question: "What is your policy when a dialyzer fails TCV or the leak test?"

Below the grid, full width: a single teal take-home strip "These are reasonable, respectful questions. A good unit will answer all six." Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at 70% opacity. White background throughout.

NEGATIVE INSTRUCTIONS: Avoid more than six cards, avoid garbled icons or text, avoid adversarial language anywhere on the card, avoid cartoon style, avoid clutter, avoid making any one card visually heavier than the others, avoid emojis. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK: When viewed as a phone screenshot, all six questions must still be readable without zoom. Icons must look like they came from the same icon family (consistent stroke weight, palette). Background must be white. Copyright attribution williamriveromd.com must be visible bottom-right.
```

---

## Embedding map (where each image lands in the guide HTML)

| File | Embed target | Notes |
|---|---|---|
| `dialyzer-reprocessing-reuse-og.png` | `<head>` `og:image`, `twitter:image` | width=1200, height=630 meta tags |
| `dialyzer-reprocessing-reuse-hero.png` | First `<img>` inside `<section class="hero">` or first content `<figure>` after the hero text | `fetchpriority="high" loading="eager"`, max-width:600px, centered |
| `dialyzer-anatomy-cross-section.png` | `<section id="what-dialyzer">` — after the H2, before the three-card grid | Caption: "Inside a dialyzer — hollow fibers, semipermeable membrane, three ways your blood gets cleaner." |
| `dialyzer-biocompatible-vs-cellulose.png` | `<section id="what-dialyzer">` — inside the amber callout `Why the membrane material matters for the reuse story` or directly under it | Caption: "Modern biocompatible synthetic membranes (polysulfone, PES) quietly removed one of the original medical arguments for reuse." |
| `dialyzer-reprocessing-6-steps.png` | `<section id="process">` — directly under the H2, before or replacing the numbered steps | Caption: "Six documented checks; any failure halts the chain." |
| `dialyzer-germicide-history-matrix.png` | `<section id="germicides">` — under the H2, replacing or augmenting the comparison table | Caption: "Formaldehyde (1983) → peracetic acid (today) — the modernization in one chart." |
| `dialyzer-reuse-global-regulatory-map.png` | First placement: `<section id="walked-away">` under the red `hard line abroad` callout. Re-reference: linked from `<section id="renaissance">`. | Caption: "Where in the world reuse is allowed — and where the Philippines sits." |
| `dialyzer-reuse-kdigo-waste-hierarchy.png` | `<section id="renaissance">` — under H3 "Where reuse sits on the waste hierarchy" | Caption: "Reuse is tier 2 of 5 — useful, but only Prevent outranks it." |
| `dialyzer-reuse-honest-balance-scale.png` | `<section id="honest">` — directly under the H2 | Caption: "Real saving, real footprint of its own." |
| `dialyzer-reuse-philippine-clinic-vignette.png` | `<section id="philippines">` — top of section, before the checklist | Caption: "Single-patient, labeled, logged — the visible proof inside a Philippine unit." |
| `dialyzer-reuse-questions-to-ask-card.png` | `<section id="philippines">` — directly under the dark `checklist` panel | Caption: "Screenshot and bring to your next appointment." |

---

## Production checklist (for the local-image-generator skill)

- [ ] Validate every prompt has FILE NAME, IMAGE TYPE, ASPECT RATIO, PIXEL DIMENSIONS, AUDIENCE, VISUAL GOAL, PROMPT, NEGATIVE INSTRUCTIONS, QUALITY CHECK.
- [ ] Confirm OG card is exactly 1200 × 630 with matching og:image:width / og:image:height meta tags.
- [ ] Build local folder `/Users/williamgregoryrivero/Downloads/dialyzer-reprocessing-reuse/` with `images/` and `og/` subfolders.
- [ ] Write `image-manifest.csv` and `image-manifest.json` from the manifest table above.
- [ ] Write `README-image-generation.md` with paste-in instructions for the Image Generator GPT.
- [ ] Hand prompts to user for generation in https://chatgpt.com/g/g-pmuQfob8d-image-generator.
- [ ] After images arrive, run `patch_hero_fetchpriority.py --guide dialyzer-reprocessing-reuse.html`, then `patch_hero_fullwidth.py`, then `patch_hero_maxwidth.py`.
- [ ] Append `og:image` / `og:image:width` / `og:image:height` / `og:image:alt` meta tags to the guide HTML.
