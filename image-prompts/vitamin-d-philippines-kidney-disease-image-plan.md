# Image Plan — *Vitamin D in the Philippines: The Sunshine Paradox and the Kidney Connection* (`vitamin-d-philippines-kidney-disease.html`)

**Guide:** Why Filipinos can be vitamin D–low despite year-round sun; the skin–liver–kidney activation chain; testing, thresholds, and safe treatment in CKD — dual patient/clinician.
**Prepared:** 2026-08-13 · **Pipeline:** Stage 1 (prompt authoring). Paste each `COPY-READY … PROMPT` block into the ChatGPT **Image Generator** GPT → https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Skills used:** `williamriveromd-hero-vignette` · `williamriveromd-infographic-skill` · `williamriveromd-simple-figure` · `williamriveromd-biomedical-mechanism-figure`
**Stage 2:** hand this pack to `williamriveromd-local-image-generator` to validate fields, build `generated-images/`, and write the manifests. Every block below already carries the full Stage-2 schema (`IMAGE NUMBER … OG WIDTH/HEIGHT`).

---

## House rules baked into every prompt
- **Light backgrounds only** — white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, pale teal `#eef6f7`. Never navy / charcoal / black.
- **Fonts:** on-image type is one of **Inter · Nunito Sans · IBM Plex Sans · Manrope** — no serif, no decorative. The font is named in every prompt.
- **Palette:** navy `#0f1e2e` (text/accents), clinical teal `#1a6b72`, renal green `#1f7a4d` (safe/everyday), amber/gold `#b8860b` (caution/discuss), clinical red `#b91c1c` (danger — used sparingly), soft purple `#6c3d8e` (specialist add-on) — used **only** as text/accents on light fills.
- **Attribution:** small semi-transparent navy `renalcarematters.com` bottom-right (bottom-center for portrait) on every image **except the wordless vignette hero** (asset 1), which carries no text at all.
- **No guideline/journal/brand names as on-image text.** Never render "KDIGO", "Endocrine Society", "NEJM", "JCEM", a year-stamped guideline, or a product brand. Every text-bearing prompt ends with: *"No journal names, guideline acronyms, brand names, or watermarks."*
- **Save each asset** as `.png` **and** a matching `.webp` twin under `images/`, using the exact FILE NAME below.

## Clinical guardrails for THIS guide (must hold in every graphic — medical-teaching standard)
- **The ~80–90% clinic observation is NOT a prevalence.** Never render "80–90% of Filipinos are deficient" or any national-prevalence number. It is one practice's indication-driven testing population — keep it off every image.
- **No universal cutoff as a target.** The guide retires the universal 30 ng/mL disease-prevention target. Do **not** draw a "30 ng/mL = healthy" line, gauge, or traffic-light. Where a number is unavoidable, label it *"laboratories and frameworks differ — not one universal target."* Prefer showing **no numeric cutoffs at all.**
- **Two different molecules, two different questions.** `25(OH)D` = the storage form / the routine status test. `Calcitriol (1,25(OH)₂D)` = the active hormone the kidney makes; it is **not** the routine screening test. Never imply calcitriol is the test to order, and never imply one form is "better" — they answer different questions.
- **Sun is not a toxicity source.** Skin (cutaneous) vitamin D production is self-limited; **toxicity comes from excess supplements**, acting through **hypercalcemia**. Never imply sunlight causes toxicity.
- **Never tell readers to skip sun protection.** Sunscreen and heat safety still matter — no "ditch the sunscreen" message anywhere.
- **Kidney anatomy:** bean-shaped, convex border **lateral** (outward), hilum **medial** (inward); never mirrored, never hilum-on-the-convex-border.
- **Active vitamin D is clinician-directed and selective** — reserved for severe/progressive secondary hyperparathyroidism in selected CKD, not routine. Never depict it as an everyday supplement.
- **No fabricated lab values** on the mechanism / lab-relationship figures — show **trends and relationships (arrows), not numbers.**
- **Calm, Filipino clinical context.** No fear imagery, no distressed patients, no needles or machines dominating a frame.

## Asset roster

| # | File (`images/…`) | Section placement | Skill | Archetype | Size |
|---|---|---|---|---|---|
| 1 | `…-vignette-hero.png` | Hero disc (`figure.hero-figure`) — **already wired** | hero-vignette | Vignette hero v3 (Scaffold A) | 2048×2048 |
| 2 | `…-og.png` | `og:image` / `twitter:image` — **already wired** | infographic | Editorial hero + title (OG card) | 1200×630 |
| 3 | `…-01-sunshine-paradox.png` | Patient § `pt-opening` (The Paradox) | infographic | Multi-panel Educational | 1792×1024 |
| 4 | `…-02-activation-chain.png` | Patient § `pt-pathway` (The Pathway) | simple-figure | Scaffold C — horizontal sequence | 1792×1024 |
| 5 | `…-03-five-reasons.png` | Patient § `pt-why-low` (Why Levels Are Low) | infographic | Multi-panel Educational | 1792×1024 |
| 6 | `…-04-storage-vs-active.png` | Patient § `pt-reading` (Reading Your Result) | simple-figure | Scaffold B — comparison | 1792×1024 |
| 7 | `…-05-nutritional-vs-active-therapies.png` | Patient § `pt-active-vs-nutritional` | simple-figure | Scaffold E — reference table | 1536×1152 |
| 8 | `…-06-safety-boundary.png` | Patient § `pt-safety` (Safety) | simple-figure | Scaffold B — two-zone | 1792×1024 |
| 9 | `…-md-01-ckd-mbd-mechanism.png` | Clinician § `md-ckd-mbd` (CKD-MBD Framework) | biomedical-mechanism | Organ→inset→injury/intervention/benefit | 1792×1024 |
| 10 | `…-md-02-lab-constellation.png` | Clinician § `md-evidence`/`md-ckd-mbd` | simple-figure | Scaffold D — radial hub (square) | 1024×1024 |

> **Wiring status (2026-08-13):** Assets 1 and 2 are **already referenced** by the guide HTML (hero `<picture>` + `og:image`/`twitter:image`, dimensions 2048² and 1200×630). **No image files exist yet** — all ten are pending generation. Assets 3–10 have **no `<figure>` inserted yet** (deliberately, to avoid broken images). Generate, save the `.png`+`.webp` pair into `images/`, then paste the matching `<figure>` block from the **Wiring appendix** at the named section anchor. After inserting any inline figure, re-run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, `patch_image_lightbox.py`, then `patch_hero_meta.py`.
>
> **Derived asset (no separate prompt):** `vitamin-d-philippines-kidney-disease-rg-thumb.webp` — a 1:1 center-crop of the OG card (asset 2), for Related-guides cards on sibling guides. Export it once asset 2 is final.

---

## 1 · Circular vignette hero  *(already wired — patient hero disc)*

```
IMAGE NUMBER: 1
SECTION PLACEMENT: Hero — figure.hero-figure > .hero-vignette (patient mode)
FILE NAME: vitamin-d-philippines-kidney-disease-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 — Scaffold A (clinical/lifestyle people scene)
AUDIENCE: mixed (patients + clinicians)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with a white margin)
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX:
- photorealistic models: yes (single subject)
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Convey the "sunshine paradox" at a glance — abundant warm daylight in the room, yet only a thin band actually falls on the subject's skin.
KEY CONCEPTS: sunlight present in the environment ≠ UVB reaching skin; indoor/covered life; calm Filipino everyday context.
COMPOSITION ARCHETYPE: J — Environmental Storytelling
CAMERA: environmental side-profile portrait, subject offset to the RIGHT of the circle
HUMAN VARIATION: young-adult Filipina, late 20s; oval face, soft jaw; straight shoulder-length dark-brown hair loosely tied; slim build; mustard smart-casual blouse; minimal jewelry; relaxed seated posture, one forearm in the light; calm thoughtful expression; indoor daytime office-by-a-window setting.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: Environmental Storytelling. Camera: environmental side-profile portrait, subject placed toward the RIGHT of the circle.
Subject: a Filipina office worker in her late twenties — oval face, soft jawline, straight shoulder-length dark-brown hair loosely tied, slim build, mustard-yellow smart-casual blouse, calm thoughtful expression — seated at a desk beside a large bright window in a clean, modern Philippine office, one forearm resting on the sill where a single soft band of warm daylight touches her skin. Gentle natural daylight, shallow depth of field, the rest of the room in soft airy blur.
Visual hierarchy: the subject and window occupy 60–70% of the circle on the right; 2–4 supporting context cues (desk edge, a small potted plant, softly blurred glass) fill 20–30%; reserve the LEFT 20–25% of the circle as a clean TITLE SAFE ZONE of bright, softly graded window light and pale wall — no faces, anatomy, icons, text, or objects in that zone — so the HTML title can sit beside the disc. Calm, reassuring, documentary-realistic colour grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light, warm background; soft edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.
Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, icons, labels, cropped circle, edge clipping, objects touching the circular border, any content inside the title-safe zone, baked-in text/titles/logos/watermarks, rectangular borders/frames/banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces. No sunburn, no reddened skin, no medical distress.

QUALITY CHECK:
Square 2048×2048. Circle 85–90% of canvas with a visible white margin, never cropped. ONE dominant subject (60–70%), 2–4 supporting elements, left 20–25% reserved as a clean title-safe zone. Filipino everyday context, wordless. Crops cleanly inside the circle with nothing lost at the edges.

ALT TEXT: A Filipina office worker seated by a bright office window in soft daylight, a thin band of sunlight touching her forearm — illustrating that sunlight in the room is not the same as UVB reaching the skin.
OG WIDTH: (not an OG asset — see asset 2)
OG HEIGHT: (not an OG asset — see asset 2)
```

---

## 2 · OG / social share card  *(already wired — `og:image` / `twitter:image`)*

```
IMAGE NUMBER: 2
SECTION PLACEMENT: <head> og:image + twitter:image (not shown in body)
FILE NAME: vitamin-d-philippines-kidney-disease-og.png
ARCHETYPE: Photorealistic Editorial Hero + title (OG / social share card)
AUDIENCE: mixed (patients, families, clinicians)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630  (FIXED — never any other size for an OG card)
VISUAL MIX:
- photorealistic models: yes (left scene)
- 2D infographic: yes (right title panel + simple sun→kidney line motif)
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: One glance says "sunny country, still low vitamin D — and the kidney is central."
KEY CONCEPTS: sunshine paradox; skin→kidney link; calm Filipino context; title legible in a link preview.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Photorealistic medical editorial OG / social share card, exactly 1200×630 px, for a nephrology education guide, on a clean WHITE / off-white background. Split composition: on the LEFT ~55%, a bright, calm, naturally lit photorealistic scene of a Filipino adult in warm daylight near a window, a soft band of sunlight falling across a bare forearm — warm, reassuring, documentary-realistic, shallow depth of field. On the RIGHT ~45%, a clean off-white panel carrying the title text in a large bold navy #0f1e2e sans-serif (Inter or Manrope): "Vitamin D in the Philippines" with a smaller clinical-teal #1a6b72 subtitle "The sunshine paradox and the kidney connection." Below the subtitle, one simple flat line motif in teal #1a6b72 and renal green #1f7a4d: a small sun glyph → a stylized skin line → a correctly oriented kidney silhouette (convex edge outward, hilum inward), connected by a thin arrow, suggesting "sun to skin to kidney." Generous negative space, mobile-safe margins, nothing important within 40 px of any edge. Small semi-transparent navy "renalcarematters.com" in the bottom-right corner.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, HDR, over-saturation, stock-photo blandness. NEVER a dark/navy/charcoal/black background. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No numeric lab cutoffs, no "30 ng/mL", no prevalence percentage, no sunburned skin. Kidney silhouette must not be mirrored (hilum stays on the inner/medial side). Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. Title and subtitle crisp and legible as a link preview thumbnail. Light background, calm Filipino scene, correct kidney orientation, no cutoff numbers or prevalence claims. Attribution bottom-right.

ALT TEXT: Vitamin D in the Philippines: The Sunshine Paradox and the Kidney Connection — a Filipino adult in warm window light beside a sun-to-skin-to-kidney motif.
OG WIDTH: 1200
OG HEIGHT: 630
```

---

## 3 · The sunshine paradox  *(Patient § `pt-opening`)*

```
IMAGE NUMBER: 3
SECTION PLACEMENT: Patient mode, section id="pt-opening" (after the "Key idea" callout)
FILE NAME: vitamin-d-philippines-kidney-disease-01-sunshine-paradox.png
ARCHETYPE: Multi-panel Educational Infographic
AUDIENCE: patients (mixed-friendly)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: light (small simplified figures per panel)
- 2D infographic: yes (four panels + shared sun + broken-ray glyphs)
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Show that sunlight is in the environment for everyone, yet very little UVB actually lands on skin in common Filipino daily patterns.
KEY CONCEPTS: same sun overhead; four everyday scenarios; a broken/interrupted ray to each figure; "environment ≠ dose on skin."

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean patient-education infographic, landscape 16:9, modern nephrology-clinic aesthetic, on a white #ffffff background. Bold navy #0f1e2e sans-serif title (Inter) across the top: "Sunlight in the sky is not the same as UVB on your skin." A single warm sun glyph sits centered along the top, its soft rays fanning down over four equal panels below. Four rounded light-gray #f3f4f6 cards in one row, each a simple flat scene of a Filipino person: (1) an office worker at a desk beside a window; (2) a night-shift worker under warm indoor light with a dark window; (3) an older adult seated indoors away from any window; (4) a commuter in a jeepney wearing long sleeves and holding an umbrella. From the shared sun to each figure's forearm runs one thin teal #1a6b72 dashed ray interrupted partway by a small "✕" — showing the ray is blocked before reaching skin. Small plain labels under each card in navy: "Indoor work", "Night shift", "Housebound", "Covered commute". A slim bottom strip in soft teal tint #eef6f7 with one navy takeaway line: "Same sun overhead — very different amounts actually reaching the skin." Generous whitespace, mobile-readable, consistent icon stroke weight. Small semi-transparent navy "renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, HDR, over-saturation, dark/navy/charcoal/black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No sunburn or reddened skin, no medical mask (the commuter's covering is sun-protection, not illness), no implication any one figure is definitely "deficient", no percentages or lab numbers. Do NOT suggest avoiding sunscreen.

QUALITY CHECK:
Four panels read as one shared scene (single sun, consistent light direction). Broken-ray "✕" glyph legible in all four. No numbers, no prevalence claim. Light background, calm tone, attribution bottom-right.

ALT TEXT: Four everyday Filipino scenes — indoor work, night shift, housebound, covered commute — under one shared sun, each with an interrupted ray showing little UVB reaches the skin.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## 4 · The skin → liver → kidney activation chain  *(Patient § `pt-pathway`)*

```
IMAGE NUMBER: 4
SECTION PLACEMENT: Patient mode, section id="pt-pathway" (replacing/illustrating the 4-step table)
FILE NAME: vitamin-d-philippines-kidney-disease-02-activation-chain.png
ARCHETYPE: Simple figure — Scaffold C (horizontal step sequence)
AUDIENCE: mixed (patients + clinicians)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes (labeled flow)
- 3D component graphics: light (simple schematic organ icons)
- algorithm/flowchart: yes (left-to-right sequence)
PURPOSE: Show vitamin D as a stepwise pathway whose FINAL activation happens in the kidney — the step that can weaken in CKD.
KEY CONCEPTS: UVB/food/supplement → vitamin D → liver → 25(OH)D (storage / the test) → kidney → calcitriol (active hormone) → intestine, bone, parathyroid.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean clinical-education infographic, white #ffffff background, landscape 16:9. Bold navy #0f1e2e sans-serif title (Inter) at top: "Vitamin D is a step-by-step pathway", teal #1a6b72 subtitle: "the kidney performs the final activation step." A single left-to-right flow of rounded cards on a very soft gray #f3f4f6 panel, connected by bold navy right-pointing arrows: (1) an input cluster icon (small sun + fork + capsule) labeled "UVB · food · supplement" with an amber #b8860b accent band; (2) a simple hexagon molecule glyph labeled "Vitamin D"; (3) a simple schematic LIVER silhouette labeled "Liver"; (4) a molecule glyph labeled "25(OH)D — storage form · the usual blood test" with a slate/navy accent; (5) a simple schematic KIDNEY icon (bean-shaped, convex edge outward, hilum facing inward, not mirrored) with a teal #1a6b72 accent band, labeled "Kidney — activation step"; (6) a molecule glyph labeled "Calcitriol — active hormone"; (7) a small three-way fan-out to renal-green #1f7a4d mini-icons: "Intestine (absorbs calcium)", "Bone (mineral balance)", "Parathyroid (calcium sensor)". A small teal callout above the kidney card: "This step can weaken in kidney disease." Bottom strip in soft teal tint #eef6f7, navy takeaway: "Sun and skin are only the start — the kidney finishes the job." Uniform icon stroke weight, generous whitespace, mobile-readable labels. Small semi-transparent navy "renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, real chemical structural formulas (use simple generic molecule glyphs), HDR, dark/navy/charcoal/black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Kidney icon must NOT be mirrored (hilum stays medial/inward, convex border outward). Do not imply 25(OH)D is the "active" hormone or that calcitriol is the routine test. No numeric lab values or cutoffs. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Seven-node left-to-right order correct and legible; kidney icon correctly oriented and not mirrored; 25(OH)D labeled as storage/test and calcitriol as active hormone; kidney callout points at the activation step; no chemical formulas, no numbers. Light background, attribution bottom-right.

ALT TEXT: A left-to-right pathway — UVB, food and supplements to vitamin D, to the liver making 25(OH)D (the storage form and usual test), to the kidney making active calcitriol, acting on intestine, bone and parathyroid — with a note that the kidney step can weaken in kidney disease.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## 5 · Five reasons levels can still be low  *(Patient § `pt-why-low`)*

```
IMAGE NUMBER: 5
SECTION PLACEMENT: Patient mode, section id="pt-why-low" (alongside/illustrating the five-card grid)
FILE NAME: vitamin-d-philippines-kidney-disease-03-five-reasons.png
ARCHETYPE: Multi-panel Educational Infographic
AUDIENCE: patients (mixed-friendly)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes (five equal cards)
- 3D component graphics: light (simple organ/skin glyphs)
- algorithm/flowchart: none
PURPOSE: Present the five non-ranked, co-existing reasons a vitamin D level can be low even in a sunny country.
KEY CONCEPTS: exposure; skin & body; diet; absorption & liver; kidney disease — equal visual weight, not a severity ladder.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient-education infographic, landscape 16:9, on a white #ffffff background. Bold navy #0f1e2e sans-serif title (Inter) at top: "Five reasons a level can still be low", teal #1a6b72 subtitle: "these add up together — no single one is the whole story." Five equal rounded cards in one row on soft gray #f3f4f6, each with a colored top accent band, one simple flat icon, a short bold label, and a one-line plain-English note: (1) amber #b8860b "Exposure" — sun-with-broken-ray glyph — "Indoor work, night shifts, shade, umbrellas, covered skin"; (2) teal #1a6b72 "Skin & body" — simple skin-tone swatch / cross-section glyph — "Skin tone, age, and body size change how much is made and stored"; (3) renal green #1f7a4d "Diet" — neutral fork/plate glyph — "Few everyday Filipino foods are naturally rich in vitamin D"; (4) soft purple #6c3d8e "Absorption & liver" — small intestine loop + liver glyph — "Fat-malabsorption or liver disease lowers uptake and processing"; (5) navy #0f1e2e "Kidney disease" — correctly oriented kidney icon (convex outward, hilum inward) — "CKD can weaken the final activation step and lose the carrier protein in urine". All five cards identical size and icon weight (a balanced list, not a ranking). Bottom strip soft teal tint #eef6f7, navy line: "Usually several of these overlap in one person." Generous whitespace, mobile-readable. Small semi-transparent navy "renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, AI gibberish, HDR, dark/navy/charcoal/black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No implied ranking or severity ladder (equal card sizes). No body-shaming or diet-shaming imagery (neutral glyphs only). No prevalence percentages or lab numbers. Kidney icon not mirrored. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Five equal-weight cards, no ranking; kidney icon correct; neutral non-stigmatizing icons; no invented numbers. Light background, mobile-readable, attribution bottom-right.

ALT TEXT: Five equal cards showing why vitamin D can be low — exposure, skin and body, diet, absorption and liver, and kidney disease — presented as co-existing factors, not a ranking.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## 6 · Storage form vs active hormone (25(OH)D vs calcitriol)  *(Patient § `pt-reading`)*

```
IMAGE NUMBER: 6
SECTION PLACEMENT: Patient mode, section id="pt-reading" (near the unit-converter tool)
FILE NAME: vitamin-d-philippines-kidney-disease-04-storage-vs-active.png
ARCHETYPE: Simple figure — Scaffold B (two-panel comparison)
AUDIENCE: mixed (patients + clinicians)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes (two comparison columns + bottom banner)
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Make clear that the routine test (25(OH)D) and the active hormone (calcitriol) answer different questions — the two are not interchangeable, and neither is "better."
KEY CONCEPTS: 25(OH)D = storage form, the usual test, stable, reflects stores; calcitriol = active hormone, made by the kidney, tightly regulated, not the routine screening test.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Medical-education comparison infographic, graphical-abstract style, white #ffffff background, landscape 16:9. Centered bold navy #0f1e2e sans-serif title (Inter): "Two different tests, two different questions." A soft dashed vertical divider splits the canvas into two equal rounded panels — BOTH neutral (this is not good-vs-bad). LEFT panel header in clinical teal #1a6b72: "25(OH)D — the storage form"; a simple hexagon molecule glyph; three short rows: "What it reflects — your overall vitamin D stores", "What's usually tested — yes, this is the standard status test", "Behavior — stable, changes slowly over weeks". RIGHT panel header in navy #0f1e2e: "Calcitriol (1,25(OH)₂D) — the active hormone"; a simple molecule glyph beside a small correctly-oriented kidney icon (convex outward, hilum inward) labeled "made by the kidney"; three short rows: "What it reflects — how much active hormone the kidney is making now", "What's usually tested — no, only in specific situations", "Behavior — tightly regulated; can be normal or high even when 25(OH)D is low". A full-width bottom banner in soft teal tint #eef6f7 with a bold navy line: "Testing calcitriol does not tell you your vitamin D stores." Rounded corners, ample negative space, mobile-readable labels ≥11pt, simple generic molecule glyphs only. Small semi-transparent navy "renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, AI gibberish, real chemical structural formulas, HDR, dark/navy/charcoal/black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Do NOT color one panel "good" and the other "bad" (no green-vs-red framing) — both neutral. Do not imply calcitriol is the routine or preferred test. No numeric reference ranges or cutoffs. Kidney icon not mirrored. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Two neutral columns, same row order; 25(OH)D framed as the routine test / stores, calcitriol as active/kidney-made/not routine; bottom banner present and legible; no cutoffs; no good-vs-bad coloring. Light background, attribution bottom-right.

ALT TEXT: A two-column comparison — 25(OH)D as the stable storage form and usual blood test, versus calcitriol as the kidney-made active hormone that is not the routine test — with a banner noting calcitriol does not tell you your vitamin D stores.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## 7 · Nutritional vs active vitamin D therapies  *(Patient § `pt-active-vs-nutritional`)*

```
IMAGE NUMBER: 7
SECTION PLACEMENT: Patient mode, section id="pt-active-vs-nutritional" (illustrating the therapy table)
FILE NAME: vitamin-d-philippines-kidney-disease-05-nutritional-vs-active-therapies.png
ARCHETYPE: Simple figure — Scaffold E (reference table / quick-look card)
AUDIENCE: mixed (patients + clinicians)
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes (clean comparison table)
- 3D component graphics: light (small generic capsule glyphs per row)
- algorithm/flowchart: none
PURPOSE: Restate the guide's own therapy table — which forms still need kidney activation and each form's main safety concern — as one clean, mobile-readable card.
KEY CONCEPTS: cholecalciferol (D3), ergocalciferol (D2), calcifediol, calcitriol, active analogues; "needs kidney activation?"; main safety concern; active forms are clinician-directed.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical reference card, publication-grade nephrology design, white #ffffff background, 4:3. Bold navy #0f1e2e sans-serif title (Inter) at top: "Not all 'vitamin D' is the same." A compact, well-organized table with four columns — header row in white text on a clinical teal #1a6b72 band: "Form", "Supplies", "Needs kidney activation?", "Main safety concern". Five rows with alternating white / very soft gray #f3f4f6 fills, each row led by a small neutral generic capsule glyph: (1) "Cholecalciferol (D3)" · "Vitamin D3 substrate" · "Yes — substantially" · "Overdosing; hypercalcemia in susceptible people"; (2) "Ergocalciferol (D2)" · "Vitamin D2 substrate" · "Yes — substantially" · "Same principle; response may vary"; (3) "Calcifediol" · "25(OH)D" · "Final activation still needed" · "Hypercalcemia; overshooting"; (4) "Calcitriol" · "Active hormone" · "No" · "Hypercalcemia; high phosphate; PTH over-suppression"; (5) "Active analogues" · "Receptor-active compounds" · "No" · "Hypercalcemia; phosphate effects; over-suppression". The "Needs activation? No" cells for calcitriol and active analogues carry a small amber #b8860b tag "clinician-directed." Footer line in navy on soft teal tint #eef6f7: "Nutritional and active forms are not interchangeable — dosing is individualized by your clinician." Mobile-readable, not cluttered. Small semi-transparent navy "renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, HDR, dark/navy/charcoal/black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No real drug brand names, no pill imprints or reproduced packaging (generic capsule glyphs only). No doses, no numeric thresholds. Do not imply active forms are everyday supplements. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Five rows match the guide's therapy table exactly; "needs activation" column correct (D3/D2/calcifediol require it, calcitriol/analogues do not); active forms tagged clinician-directed; no brands, no doses, no numbers. Light background, mobile-readable, attribution bottom-right.

ALT TEXT: A reference table of vitamin D forms — cholecalciferol, ergocalciferol, calcifediol, calcitriol, and active analogues — showing which still need kidney activation and each form's main safety concern, with active forms marked clinician-directed.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## 8 · The safety boundary  *(Patient § `pt-safety`)*

```
IMAGE NUMBER: 8
SECTION PLACEMENT: Patient mode, section id="pt-safety" (after the toxicity paragraph)
FILE NAME: vitamin-d-philippines-kidney-disease-06-safety-boundary.png
ARCHETYPE: Simple figure — Scaffold B (two-zone comparison)
AUDIENCE: patients (mixed-friendly)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes (two zones of icons + divider)
- 3D component graphics: light (small kidney caution glyph)
- algorithm/flowchart: none
PURPOSE: Draw the line between everyday-and-fine and needs-a-conversation — without alarm — and locate vitamin D toxicity as a supplement issue acting through high calcium.
KEY CONCEPTS: safe = foods, reasonable sun, clinician-set dosing; discuss = duplicate products, repeated megadoses, hypercalcemia, kidney-injury risk with toxicity.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Medical-education two-zone comparison infographic, white #ffffff background, landscape 16:9. Bold navy #0f1e2e sans-serif title (Inter) at top: "Same vitamin, different context." A soft vertical divider labeled "The safety boundary" splits the canvas. LEFT zone, renal-green #1f7a4d accented, header "Generally safe / everyday", lighter and airier, three simple icons with short labels: "Vitamin D–containing foods" (plate/fish glyph), "Reasonable, sensible sun in moderation" (clothed walking figure under a small sun — fully clothed, no bare-skin sunbathing), "Supplement dose set by your clinician" (capsule + small prescription-pad glyph). RIGHT zone, amber #b8860b accented (NOT alarm-red), header "Discuss with your clinician", slightly tighter grouping, four simple icons with short labels: "More than one vitamin D product at once" (two overlapping bottles), "Repeated high doses without monitoring" (stacked pills), "High blood calcium — hypercalcemia" (a simple gauge tipped toward 'high'), "Kidney-injury risk with toxicity" (a correctly oriented kidney icon — convex outward, hilum inward — ringed by a thin amber caution outline, no gore). A slim bottom strip soft teal tint #eef6f7, navy line: "Food and sensible sun rarely cause trouble; repeated high-dose supplements can — through high calcium." Calm, non-alarming; the contrast reads as 'everyday' vs 'needs a conversation', not 'safe' vs 'emergency'. Mobile-readable, consistent icon weight. Small semi-transparent navy "renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, AI gibberish, HDR, dark/navy/charcoal/black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. No true alarm/emergency iconography (no sirens, skull-and-crossbones, poison symbols), no true alert-red as the zone color (use amber), no gory or bloody kidney, no bare-skin sunbathing figure, no advice to skip sunscreen, no numeric calcium or dose thresholds, no brand packaging. Kidney icon not mirrored. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Left zone = 3 everyday-safe icons (green), right zone = 4 discuss icons (amber, not red); tone is "know the boundary," not emergency; kidney caution icon outline-only and correctly oriented; no numbers, no brands. Light background, attribution bottom-right.

ALT TEXT: A two-zone safety diagram — generally-safe everyday choices (foods, sensible sun, clinician-set dosing) versus items to discuss with a clinician (duplicate products, repeated megadoses, high blood calcium, kidney-injury risk) — framed calmly, not as an emergency.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## 9 · CKD-MBD: why the activation step fails  *(Clinician § `md-ckd-mbd`)*

```
IMAGE NUMBER: 9
SECTION PLACEMENT: Clinician mode, section id="md-ckd-mbd" (with the stage-by-stage card)
FILE NAME: vitamin-d-philippines-kidney-disease-md-01-ckd-mbd-mechanism.png
ARCHETYPE: Biomedical mechanism figure (organ-level panel → magnified inset → injury/intervention/benefit flow)
AUDIENCE: clinicians
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes (review-article schematic)
- 3D component graphics: light (soft semi-3D vector organ/tubule)
- algorithm/flowchart: partial (bottom summary flow)
PURPOSE: Explain why calcitriol production falls in progressive CKD and how that drives secondary hyperparathyroidism within CKD-MBD — trends only, no numbers.
KEY CONCEPTS: reduced renal 1-alpha-hydroxylase (CYP27B1); early FGF23 rise suppressing calcitriol; falling calcitriol → less intestinal calcium absorption, less PTH suppression → SHPT; intervention = correct modifiable factors, selective active vitamin D in severe/progressive SHPT; benefit = better mineral balance and PTH control.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Publication-grade biomedical mechanism schematic, scientific review-article style, flat vector illustration with soft semi-3D shading on a WHITE background, landscape 16:9, muted clinical palette, thin dashed connector boxes, clean sans-serif labels in Inter. Title in navy #0f1e2e: "Why the kidney's activation step fails in CKD."
LEFT — organ-level panel: a simplified light gray-blue kidney (bean-shaped, convex border LATERAL/outward, hilum MEDIAL/inward, not mirrored) labeled "Chronic kidney disease"; a thin dashed connector box points from the cortex to the magnified panel.
CENTER/RIGHT — magnified functional-unit inset inside a dashed border: a proximal tubule cell with the activation enzyme highlighted in pale yellow, concise callouts (arrows only, no numbers): "↓ 1-alpha-hydroxylase (CYP27B1)", "↓ Calcitriol produced"; a small adjacent bone glyph with "↑ FGF23 (rises early) → suppresses calcitriol".
BOTTOM — three summary boxes with left-to-right arrow flow: LEFT pale-pink pathology box "Injury: ↓ renal activation, ↑ FGF23 → ↓ calcitriol → ↓ gut calcium, ↓ PTH suppression → secondary hyperparathyroidism"; CENTER neutral box "Intervention: correct modifiable factors and nutritional 25(OH)D first; reserve active vitamin D / analogues for severe or progressive SHPT (clinician-directed)"; RIGHT pale-blue benefit box "Goal: mineral balance and PTH control, tracked by trends — not a single value". Muted colors, generous whitespace, labels legible at slide size. Small semi-transparent navy "© renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark/navy/charcoal/black backgrounds, decorative effects, shadows-heavy rendering, cartoon styling, overcrowding, tiny unreadable labels, AI gibberish. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Kidney must not be mirrored (hilum medial). Do NOT invent numeric lab values, cutoffs, or doses (arrows/trends only). Do not imply active vitamin D is routine for all CKD. Never omit the © renalcarematters.com attribution.

QUALITY CHECK:
Organ panel → dashed magnified tubule inset → bottom injury/intervention/benefit flow all present; kidney correctly oriented; FGF23 shown rising early and suppressing calcitriol; active vitamin D framed as selective/clinician-directed; no numbers. White background, attribution bottom-right.

ALT TEXT: A review-article mechanism schematic — a CKD kidney, a magnified proximal-tubule inset showing reduced 1-alpha-hydroxylase and calcitriol with early FGF23 rise, and a bottom injury-to-intervention-to-benefit flow ending in mineral and PTH control tracked by trends.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## 10 · The CKD-MBD laboratory constellation  *(Clinician § `md-evidence` / `md-ckd-mbd`)*

```
IMAGE NUMBER: 10
SECTION PLACEMENT: Clinician mode, section id="md-ckd-mbd" (or md-evidence claim ledger)
FILE NAME: vitamin-d-philippines-kidney-disease-md-02-lab-constellation.png
ARCHETYPE: Simple figure — Scaffold D adapted to a radial hub (square)
AUDIENCE: clinicians
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: yes (radial hub-and-spoke)
- 3D component graphics: light (small kidney glyph on the eGFR node)
- algorithm/flowchart: none
PURPOSE: Reinforce that CKD-MBD labs are read together as a pattern of trends, not one value in isolation.
KEY CONCEPTS: central CKD-MBD panel; six satellites — 25(OH)D, calcium, phosphate, PTH, ALP, eGFR; primary hub spokes plus lighter test–test interaction lines; interpret together, trends over time.

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean clinical radial hub-and-spoke reference diagram, white #ffffff background, square 1:1. Bold navy #0f1e2e sans-serif title (Inter) at top: "Read the CKD-MBD panel together, not one at a time." A central teal #1a6b72 hub disc labeled "CKD-MBD panel". Six evenly spaced satellite nodes (about 60° apart), each a small rounded card with an icon, an abbreviation, and a one-line plain gloss: "25(OH)D — vitamin D storage form", "Ca — calcium", "PO₄ — phosphate", "PTH — parathyroid hormone", "ALP — alkaline phosphatase (bone turnover)", "eGFR — kidney function" (this last node carries a small correctly-oriented kidney glyph, convex outward, hilum inward). Bold teal primary spokes connect each satellite to the hub; thinner, lighter slate #64748b secondary lines connect the clinically interacting pairs (calcium–phosphate, PTH–calcium, eGFR–phosphate) so the hierarchy stays clear. Place a small up/down/flat trend-arrow glyph on two or three nodes (e.g. ↑ PTH, ↑ phosphate, ↓ 25(OH)D) to signal "trends, not single values" — with NO numbers attached. A small navy callout near the hub: "Interpret together, over time." Generous whitespace, uniform icon weight, mobile-readable. Small semi-transparent navy "renalcarematters.com" bottom-right.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, AI gibberish, HDR, dark/navy/charcoal/black backgrounds. Use ONLY Inter, Nunito Sans, IBM Plex Sans, or Manrope. Exactly six satellite nodes — no more, no fewer, do not invent extra labs. No numeric lab values or reference ranges (trend arrows only). No alarm-red danger coding. Secondary interaction lines must stay lighter than the six primary spokes. Kidney glyph not mirrored. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly six satellites (25(OH)D, calcium, phosphate, PTH, ALP, eGFR); primary spokes bolder than secondary interaction lines; trend arrows present, no numbers; "interpret together" callout present; kidney glyph correct. White background, attribution bottom-right.

ALT TEXT: A radial hub-and-spoke diagram with a central CKD-MBD panel and six satellite labs — 25(OH)D, calcium, phosphate, PTH, ALP, and eGFR — joined by primary spokes and lighter interaction lines, with trend arrows and a note to interpret them together over time.
OG WIDTH: (in-body figure — not an OG asset)
OG HEIGHT: (in-body figure — not an OG asset)
```

---

## Wiring appendix — where each in-body figure goes

After generating an asset and saving the `.png`+`.webp` pair into `images/`, paste the matching `<figure>` at the named section anchor (in the correct mode block), then run the hero/lightbox patchers listed in the roster note. Every `<figure>` needs a `<figcaption>` with a `<p class="fig-desc">` (use the ALT TEXT) so the image lightbox has a caption; add a `<dl class="fig-abbrevs">` for any acronym the image shows (e.g. `FGF23`, `PTH`, `ALP`, `eGFR`, `25(OH)D`).

Template (patient in-body figure):
```html
<figure>
  <picture>
    <source srcset="../images/[FILE].webp" type="image/webp">
    <img src="../images/[FILE].png" alt="[ALT TEXT]" loading="lazy" width="[W]" height="[H]">
  </picture>
  <figcaption>
    <p class="fig-desc">[ALT TEXT / plain-language description]</p>
    <dl class="fig-abbrevs"><dt>25(OH)D</dt><dd>25-hydroxyvitamin D (storage form)</dd><!-- add others shown --></dl>
  </figcaption>
</figure>
```

| Asset | Anchor (section id) | Mode | W×H |
|---|---|---|---|
| 3 sunshine-paradox | `pt-opening` | patient | 1792×1024 |
| 4 activation-chain | `pt-pathway` | patient | 1792×1024 |
| 5 five-reasons | `pt-why-low` | patient | 1792×1024 |
| 6 storage-vs-active | `pt-reading` | patient | 1792×1024 |
| 7 nutritional-vs-active-therapies | `pt-active-vs-nutritional` | patient | 1536×1152 |
| 8 safety-boundary | `pt-safety` | patient | 1792×1024 |
| 9 ckd-mbd-mechanism | `md-ckd-mbd` | physician | 1792×1024 |
| 10 lab-constellation | `md-ckd-mbd` / `md-evidence` | physician | 1024×1024 |

> Multilingual note: figcaption `fig-desc` text is patient-facing prose — add `data-lang` en/tl/ceb/kap siblings for the six patient-mode figures (3–8), matching the rest of the guide. Clinician figures (9–10) may stay English-only.
