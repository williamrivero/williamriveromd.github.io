# Image Plan Blueprint — `medicines-and-your-kidneys.html`

**Guide:** Multiple Medicines and Your Kidneys: How Everyday Drugs, Doses, and
Timing Can Quietly Cause Kidney Failure
**Author:** Dr. William Gregory M. Rivero, MD, FPCP, DPSN · williamriveromd.com
**Prompt pack version:** v1.0
**Target tool:** [ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator)
**Output format:** All images render as `.png`. Convert each to a `.webp` twin
after download (site convention: `<picture><source srcset=".webp">` +
`<img src=".png">`).

---

## 1. Image Plan Summary

| # | File | Placement | Dimensions | Skill used | Status |
|---|---|---|---|---|---|
| 1 | `medicines-and-your-kidneys-og.png` | `<meta property="og:image">` / Twitter card | 1200 × 630 | `williamriveromd-infographic-skill` | Not yet generated |
| 2 | `medicines-and-your-kidneys-vignette-hero.png` | Hero (`figure.hero-figure > .hero-vignette`) | 2048 × 2048 → displayed square | `williamriveromd-hero-vignette` | Not yet generated |
| 3 | `renal-clearance-drug-accumulation-visual-aid-hybrid-v2.png` | Section 1 — "Why the Kidney Is the Body's Drug Filter" | 1672 × 941 | `williamriveromd-biomedical-mechanism-figure` | Not yet generated |
| 4 | `triple-whammy-arteriole-visual-aid-hybrid-v2.png` | Section 2 — "The Triple Whammy" | 1672 × 941 | `williamriveromd-biomedical-mechanism-figure` | Not yet generated (shared asset — will also serve the sibling guide once built) |
| 5 | `brown-bag-medication-review-visual-aid-hybrid-v2.png` | Section 6 — "The Brown-Bag Review" | 1672 × 941 | `williamriveromd-simple-figure` | Not yet generated |

**Not included:** IMG-C ("usual culprits map"), marked optional in the original
blueprint. Section 3 ended up carrying a data table + feature-cards instead —
adding a sixth image there would overload an already content-dense section
without adding new information. See prior image-plan review in this session.

**Every `.png` must be paired with a hand-exported `.webp` twin** at the same
filename before wiring into the guide (`patch_hero_fullwidth.py` /
`patch_hero_maxwidth.py` / the guide's own `<picture>` markup expect both).

---

## 2. Production Order

Generate in this order — each prompt is fully self-contained and can be
pasted directly into the Image Generator GPT with no further editing:

1. **Hero vignette** (sets the page's first visual impression)
2. **OG card** (needed for any early social-sharing/testing)
3. **IMG-A — Renal clearance** (Section 1)
4. **IMG-B — Triple whammy** (Section 2, shared asset)
5. **IMG-D — Brown-bag review** (Section 6)

After generation: save each `.png` to `images/`, export a matching `.webp`,
then confirm the guide's existing `<picture>` tags (already wired to these
exact filenames) render correctly in both light and dark mode.

---

## 3. Prompts

### 3.1 Hero Vignette

```
FILE NAME: medicines-and-your-kidneys-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A (people, hands-only variant)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: A — Editorial Portrait (hands-only variant: one dominant subject, no face)
CAMERA: hands-only composition, close overhead angle
HUMAN VARIATION (vs. previous guides): hands-only framing (no face at all — a first for this rotation), middle-aged adult hands (not elderly, not young), medium-brown Filipino skin tone, faint visible wrist veins, short trimmed unpolished nails, a thin worn wedding band on the ring finger, rolled-up long-sleeve cotton shirt cuff (soft sage green, not the recurring teal polo), left hand steadying a pill organizer while the right hand places a blister pack into it, seated at a home dining table (not kitchen, not clinic), warm midday window light from the left, shallow macro depth of field, no other body parts visible, no dishware in frame
AUDIENCE: patients
VISUAL GOAL: A calm, ordinary home moment of a patient sorting their own medicines — conveying quiet responsibility and self-management without any clinical or alarming tone.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed
to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas
diameter with a visible WHITE BORDER around the full circle (the circle must
never touch the canvas edges). Composition archetype: A — Editorial Portrait,
hands-only variant. Camera: close overhead hands-only composition, shallow
macro depth of field.

Subject: the hands of a middle-aged Filipino patient (medium-brown skin tone,
faint visible wrist veins, short trimmed unpolished nails, a thin worn wedding
band on the ring finger, rolled-up soft sage-green long-sleeve cotton shirt
cuff visible at the wrist) at a home dining table, one hand steadying a
weekly pill organizer while the other hand carefully places a blister pack of
tablets into one compartment. Two or three additional medicine bottles and a
glass of water sit softly out of focus nearby. Warm midday window light from
the left, soft natural daylight, gentle shallow depth of field, no face or
other body parts in frame.

Visual hierarchy: the hands and pill organizer occupy 60–70% of the circle;
the blurred bottles and water glass provide 20–30% supporting context; reserve
a 20–25% TITLE SAFE ZONE of soft out-of-focus tabletop or window-light
gradient (no hands, objects, or labels inside that zone) so the HTML title can
sit beside the disc without covering important artwork.

Calm, reassuring, documentary-realistic colour grade harmonizing with clinical
teal #1a6b72 and navy #0f1e2e on a light, warm-neutral background. Edge
falloff toward a slightly deeper neutral at the rim. Full-bleed within the
inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or
williamriveromd.com watermark. No readable text on any bottle or blister pack.

NEGATIVE INSTRUCTIONS:
Avoid: busy layouts, collage overload, more than four supporting scenes,
dozens of icons, tiny unreadable labels, infographic clutter, duplicated
people, repeated compositions, cropped circle, cropped objects, cropped
anatomy, edge clipping, objects touching the circular border, important
content inside the title safe zone, baked-in text, titles, captions, logos,
watermarks, rectangular borders, frames, banners, dark/charcoal/black
backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or
faces, implausible anatomy, readable pharmaceutical branding.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin
— never cropped. ONE dominant hero subject (hands + pill organizer) occupying
60–70% of the circle, 2–4 supporting elements (blurred bottles, water glass),
20–25% empty title-safe zone reserved (soft out-of-focus gradient — no hands,
objects, or callouts inside). Filipino clinical context conveyed through skin
tone and setting. Hands-only framing has not been used in the recent guide
rotation. Crops cleanly inside the circle with no text or subject lost at the
edges.
```

---

### 3.2 OG / Social Share Card

```
FILE NAME: medicines-and-your-kidneys-og.png
IMAGE TYPE: OG / social share card — 2D infographic motif (medicine-and-kidney)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: patients (social-share thumbnail, mixed clinician/patient reach)
VISUAL GOAL: At small thumbnail size, instantly signal "combining medicines can harm your kidneys" via three pill/bottle icons converging toward a simple kidney silhouette.

PROMPT:
Clean 2D editorial infographic on a white (#ffffff) background, 1200×630px,
1.91:1 social-share card. Left-of-center: three simple, flat, semi-realistic
medicine icons rendered as small modular cards in a row — an orange pill
bottle, a blister pack of white tablets, and a blue-capped water-pill bottle
— each with a thin navy #0f1e2e outline and a soft light-teal #eef6f7 card
background, connected by three thin converging navy arrows/lines that meet
at a single point. Right-of-center: a simple, clean, semi-photorealistic 3D
kidney silhouette rendered in clinical teal #1a6b72 with a soft renal-red
#b91c1c highlight glow at the point where the three converging lines meet it,
symbolizing combined risk landing on the kidney. Generous white negative
space in the lower-left third reserved for large bold title typography.

Baked-in title text, set in Inter (bold, condensed weight), navy #0f1e2e,
large and mobile-thumbnail-legible: "Multiple Medicines and Your Kidneys" as
the primary line, with a smaller Manrope-set subtitle line beneath in
clinical teal #1a6b72: "How Drugs, Doses & Timing Can Quietly Cause Kidney
Failure". Small "W. Rivero, MD" byline in dark teal, bottom-left, Manrope
regular weight, 70% opacity.

Copyright attribution "williamriveromd.com" rendered as small, semi-
transparent (70% opacity) navy #0f1e2e text in the bottom-right corner.

Overall composition: generous white space, rounded card corners, restrained
color palette (white/off-white background, navy structure, clinical teal
accents, one renal-red highlight only at the convergence point), no gradient
noise, no clutter — must read clearly even scaled down to a small thumbnail.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid
generic stock-photo look, avoid excessive saturation. NEVER use dark, navy,
charcoal, or black backgrounds — light backgrounds only. Use ONLY the
sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces. Never omit
the williamriveromd.com attribution. Avoid readable pharmaceutical branding
on the bottle icons. Avoid more than one accent color competing with teal/navy.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-
grade, and consistent with williamriveromd.com. Background must be white,
off-white, or soft light gray — never dark. Copyright attribution
williamriveromd.com must be visible in the bottom-right corner. Title text
must remain legible when the card is scaled down to a Facebook/X/LinkedIn
thumbnail (~360px wide).
```

---

### 3.3 IMG-A — Renal Clearance & Drug Accumulation (Section 1)

```
FILE NAME: renal-clearance-drug-accumulation-visual-aid-hybrid-v2.png
IMAGE TYPE: Biomedical mechanism schematic — two-lane eGFR comparison (organ-level inset + magnified nephron functional unit)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1672 × 941
AUDIENCE: patients (plain-language labels), dual-audience-friendly
VISUAL GOAL: Show, at a glance, why the same drug dose becomes toxic as kidney filtration slows — a healthy eGFR-90 filter clears a drug briskly while a slowed eGFR-45 filter lets it accumulate to a dangerous blood level.

PROMPT:
Create a publication-grade biomedical mechanism schematic, review-article
figure style, on a white background, 1672×941px (16:9).

**Topic:** Renal drug clearance and accumulation — why the same medicine dose
becomes a higher effective dose as kidney filtration slows.

**Disease context:** Reduced kidney filtration (declining eGFR) in chronic
kidney disease.

**Organ-level context (small inset, ≤12% of canvas):** A simplified,
correctly oriented whole-kidney silhouette (convex lateral border, hilum
medial, light gray-blue anatomy) in the upper corner, with a thin dashed
connector line pointing to the magnified nephron panel — this inset exists
only to orient the viewer to where the nephron sits; it is NOT the dominant
subject and must not be enlarged or made the visual focus.

**Magnified functional-unit panel:** A single STANDALONE enlarged nephron
(glomerulus + afferent/efferent arterioles + proximal tubule), drawn at
large scale as the true subject of the figure — not shrunk inside a
full-kidney outline. Glomerular capillary tuft anatomically correct;
arterioles drawn thick-walled with a clear circular lumen (not thin,
ureter-like tubes). This nephron unit is duplicated into two horizontal
lanes, stacked top and bottom, each inside its own thin dashed panel border:

- **Top lane, labeled "eGFR 90 — Healthy Filter":** Blood enters from the
  left carrying small colored particles (the drug). The nephron clears them
  briskly into a urine-output stream on the right. A simple vertical
  blood-level meter/gauge on the far right of this lane reads low and steady,
  in blue/green, labeled "Safe dose."
- **Bottom lane, labeled "eGFR 45 — Slowed Filter":** The identical dose of
  colored drug particles enters from the left, but clearance into the urine
  stream is visibly slower and incomplete — particles are shown accumulating
  inside the tubule and in the blood. The matching blood-level meter on the
  right rises into a red/pale-pink danger zone, labeled "Same dose, toxic
  level."

Use soft yellow to highlight the active nephron segments in both lanes; use
the muted clinical palette throughout — light gray-blue anatomy, red for the
danger-zone meter fill, blue/green for the safe-zone meter fill, pale pink
for the toxic-level label chip.

**Plain-language callout labels (short, high-yield):**
- "eGFR (filter speed)"
- "Clearance (how fast the drug leaves)"
- "Accumulation (build-up)"

**Bottom caption bar, centered, bold:** "You didn't change the dose — your
kidney did."

Use clean sans-serif typography set in Manrope throughout (headings,
lane labels, and the bottom caption), thin dashed connector lines separating
the organ inset from the magnified nephron panel and separating the two
lanes from each other, minimal clutter, generous whitespace between the two
lanes so they read as clearly distinct before/after states.

**Attribution (mandatory):** small, semi-transparent navy #0f1e2e text
"© williamriveromd.com" in the bottom-right corner, ~10–11px, not obscuring
any figure element.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark or navy/black backgrounds, decorative shadows or
gloss, cartoonish styling, gibberish text, excessive icons, and overcrowding.
Do not shrink the nephron inside a full-kidney outline at organ scale. Do not
draw arterioles as thin ureter-like tubes. Do not enlarge the whole-kidney
orientation inset beyond ~12% of the canvas or place it off-orientation
(must be convex-lateral, hilum-medial). Do not make the blood-level meter
read equally in both lanes — the eGFR-45 lane must clearly read higher/
danger-zone than the eGFR-90 lane. No serif fonts. No fabricated numeric lab
thresholds beyond the eGFR 90/45 example values already specified.

QUALITY CHECK:
□ Two eGFR lanes clearly labeled (90 healthy vs. 45 slowed) □ same input
dose shown entering both lanes □ eGFR-45 lane shows visible accumulation and
a higher blood-level reading than eGFR-90 □ nephron drawn standalone at
large scale, not organ-embedded □ whole-kidney orientation inset ≤12% of
canvas, correctly oriented □ plain-English labels present □ bottom caption
"You didn't change the dose — your kidney did." present and legible □ WCAG
AA-readable text contrast □ no garbled or gibberish text □ no prompt text
baked into the image □ williamriveromd.com watermark present □ 1672×941px,
16:9, white background.
```

---

### 3.4 IMG-B — The Triple Whammy (Section 2, shared asset)

```
FILE NAME: triple-whammy-arteriole-visual-aid-hybrid-v2.png
IMAGE TYPE: Biomedical mechanism schematic — glomerular arteriole hemodynamics (organ-level inset + magnified glomerulus + 3-driver convergence + bottom summary flow)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1672 × 941
AUDIENCE: patients (plain-language labels), dual-audience-friendly
VISUAL GOAL: Show how three individually common, individually "safe" drug classes — an NSAID, an ACE-inhibitor/ARB, and a diuretic — converge on the same glomerulus and collapse filtration pressure when combined.
REUSE NOTE: This asset is shared across guides (also used by the sibling guide on when to see a nephrologist) — keep the mechanism generic/canonical, not over-specific to any one guide's phrasing.

PROMPT:
Create a publication-grade biomedical mechanism schematic, review-article
figure style, on a white background, 1672×941px (16:9).

**Topic:** The "triple whammy" — concurrent NSAID + ACE-inhibitor/ARB +
diuretic use and acute kidney injury risk.

**Disease context:** Acute kidney injury (AKI) risk from combined
glomerular-hemodynamic drug effects, established pharmacological mechanism
(not experimental).

**Organ-level context (small inset, ≤12% of canvas):** A simplified,
correctly oriented whole-kidney silhouette (convex lateral border, hilum
medial, light gray-blue anatomy) in the upper corner, with a thin dashed
connector line pointing to the magnified glomerulus panel — orientation only,
not the dominant subject.

**Magnified functional-unit panel (dashed border, center-right, the true
subject of the figure):** A single glomerulus (capillary tuft) with its
afferent arteriole (blood in, left side) and efferent arteriole (blood out,
right side), anatomically correct — both arterioles drawn thick-walled with
a clear circular lumen, never thin ureter-like tubes.

Show three mechanism callouts converging on this same glomerulus, each with
a short label and a thin arrow pointing to the vessel it affects:
1. **NSAID** (e.g. ibuprofen, mefenamic acid) → constricts the AFFERENT
   arteriole (inflow). Draw the afferent arteriole visibly narrowed at the
   callout point, highlighted in red.
2. **ACE-inhibitor / ARB** → relaxes the EFFERENT arteriole (outflow),
   lowering the pressure gradient that drives filtration. Draw the efferent
   arteriole visibly widened at the callout point, highlighted in amber.
3. **Diuretic ("water pill")** → lowers circulating blood volume. Show a
   visibly smaller/lighter blood-volume stream flowing into the afferent
   arteriole, highlighted in blue.

**Bottom summary flow** (three boxes, left-to-right arrow flow):
- Left pathology box (pale pink): "Inflow down + outflow pressure down +
  volume down"
- Center mechanism box: "Filtration pressure collapses"
- Right outcome box (pale pink, since this is the harm outcome not a
  benefit): "Acute Kidney Injury (AKI) risk — especially when dehydrated,
  during illness, or on a hot day"

Use clean sans-serif typography set in Manrope throughout (organ label,
arteriole callouts, and the bottom summary flow), thin dashed connector
lines separating the organ inset from the magnified glomerulus panel,
minimal clutter, generous whitespace so the three converging mechanisms
read as clearly distinct before they meet at the glomerulus.

**Attribution (mandatory):** small, semi-transparent navy #0f1e2e text
"© williamriveromd.com" in the bottom-right corner, ~10–11px, not obscuring
any figure element.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark or navy/black backgrounds, decorative shadows or
gloss, cartoonish styling, gibberish text, excessive icons, and overcrowding.
Do not shrink the glomerulus inside a full-kidney outline at organ scale. Do
not draw arterioles as thin ureter-like tubes. Do not enlarge the
whole-kidney orientation inset beyond ~12% of the canvas or place it
off-orientation (must be convex-lateral, hilum-medial). Do not narrow the
efferent arteriole or widen the afferent arteriole — the direction of each
vessel's change must match the labeled mechanism exactly. No serif fonts. No
fabricated numeric pressure thresholds — describe the mechanism qualitatively.

QUALITY CHECK:
□ afferent arteriole visibly narrowed (NSAID) □ efferent arteriole visibly
widened (ACE-inhibitor/ARB) □ blood volume visibly reduced (diuretic) □ all
three converge on one glomerulus □ glomerulus/arterioles drawn standalone at
large scale, not organ-embedded □ whole-kidney orientation inset ≤12% of
canvas, correctly oriented □ bottom 3-box summary flow present and legible
□ WCAG AA-readable text contrast □ no garbled or gibberish text □ no prompt
text baked into the image □ williamriveromd.com watermark present □
1672×941px, 16:9, white background.
```

---

### 3.5 IMG-D — The Brown-Bag Review (Section 6)

```
FILE NAME: brown-bag-medication-review-visual-aid-hybrid-v2.png
IMAGE TYPE: Scaffold C (Horizontal Step Sequence, adapted 3-stage workflow) — clinical-education scene, not anatomy/mechanism
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1672 × 941 (matched to sibling in-body figures in this guide, overriding the skill's 1792×1024 default)
AUDIENCE: patients (plain-language labels)
VISUAL GOAL: Show, at a glance, that bringing every medicine bottle to one review turns a cluttered, risky list into a shorter, safer one — sorted into keep / adjust / stop.

PROMPT:
Clean clinical-education infographic, white (#ffffff) background, 1672×941px
(16:9). Title at top center in bold navy (#0f1e2e), set in Manrope: "The
Brown-Bag Medication Review." Three-stage horizontal workflow, left to
right, connected by bold navy arrows:

**Stage 1 (left, ~25% width):** An open brown paper bag on a light gray
panel (#f3f4f6), with an assortment of generic, non-brand-readable product
packaging spilling out onto a table: a prescription pill bottle, an OTC
pain-reliever bottle, a vitamin bottle, a small herbal/slimming sachet, a
whitening-capsule bottle, and an antacid/PPI box. No real logos, no readable
drug names — plain colored bottle/box shapes with simple generic icon
labels only (pill icon, leaf icon, droplet icon). Small caption beneath:
"Every product you take."

**Stage 2 (center, ~45% width, the visual anchor):** Three labeled rounded
sorting bins/baskets side by side:
- Left bin, renal-green (#1f7a4d) top accent band: "KEEP — still needed,
  right dose"
- Center bin, amber (#b8860b) top accent band: "ADJUST — dose changed for
  your kidneys"
- Right bin, clinical-red (#b91c1c) top accent band: "STOP — deprescribe,
  no longer needed or risky"
Each bin contains 1–2 small generic bottle icons already sorted into it,
in a muted tint of its accent color.

**Stage 3 (right, ~25% width):** A single short row of just 2–3 bottle
icons on a soft teal-tinted panel (#eef6f7), visibly and clearly SHORTER
than the Stage 1 spill, tagged above in bold navy: "Fewer, safer,
right-dosed."

**Persistent bottom CTA banner**, full-width, soft gray (#f3f4f6) strip
beneath the three stages, bold navy text centered: "Bring EVERY bottle —
prescribed, OTC, herbal, vitamins."

If any kidney silhouette appears at all, it must be a small inset no larger
than 12% of the canvas, clearly labeled "NOT TO SCALE" — no anatomy or
internal organs visible through skin anywhere in the image; the entire
focus stays on the bag, bottles, and sorting workflow.

Generous whitespace between the three stages, rounded card and bin corners,
mobile-readable labels ≥11pt equivalent, clean sans-serif typography set in
Manrope throughout.

Bottom-right corner: small, semi-transparent (70% opacity) navy #0f1e2e
text "williamriveromd.com".

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid
excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds —
light backgrounds only. Use ONLY the sans-serif font Manrope for all
typography — no serif fonts, no decorative or handwritten typefaces. Never
omit the williamriveromd.com attribution. No readable brand names, logos, or
real pharmaceutical packaging designs on any bottle. No internal organs or
anatomy visible through skin. If a kidney inset is included, it must not
exceed 12% of the canvas and must be labeled "NOT TO SCALE." Do not make the
final Stage 3 list the same length as or longer than the Stage 1 spill — it
must read as clearly shorter.

QUALITY CHECK:
□ brown bag + assorted generic products shown in Stage 1 □ three sorting
bins (KEEP/ADJUST/STOP) clearly labeled with correct accent colors in
Stage 2 □ Stage 3 final list visibly shorter than Stage 1 □ "Fewer, safer,
right-dosed" tag present □ bottom CTA banner present and legible □ no
internal anatomy visible through skin anywhere □ any kidney inset ≤12% of
canvas and labeled "NOT TO SCALE" □ no real brand logos or readable drug
names □ mobile-readable labels ≥11pt □ WCAG AA-readable text contrast □ no
garbled or gibberish text □ no prompt text baked into the image □
williamriveromd.com watermark present in bottom-right □ 1672×941px, 16:9,
white background.
```

---

## 4. After Generation — Wiring Checklist

1. Save each `.png` to `images/`, export a matching `.webp` twin at the same slug.
2. Confirm the guide's existing `<picture>` tags already point to these exact
   filenames — no HTML changes should be needed if names match exactly.
3. Run `python3 patch_hero_fetchpriority.py --guide medicines-and-your-kidneys.html`
   and `python3 patch_hero_fullwidth.py --guide medicines-and-your-kidneys.html`
   and `python3 patch_hero_maxwidth.py --guide medicines-and-your-kidneys.html`
   to confirm hero loading/sizing attributes are correct once the real files exist.
4. Add `og:image:width="1200"`, `og:image:height="630"`, and an `og:image:alt`
   description once the OG card is confirmed.
5. Spot-check every figure's `<figcaption><p class="fig-desc">` text against the
   final image (already written into the guide) — update only if the generated
   image diverges materially from the prompt.
6. Verify WCAG AA contrast and dark-mode rendering are unaffected (these are
   static images, not theme-aware, so no dark-mode variant is needed).
