# Image prompt pack: Born Small, Kidneys for Life

Stage 1 output for `guides/born-small-kidneys-for-life.html`. Hand to `williamriveromd-local-image-generator` (Stage 2) for validation, manifests, and wiring. Paste each COPY-READY prompt into https://chatgpt.com/g/g-pmuQfob8d-image-generator.

House rules applied to every prompt: light background only; on-image text uses one named approved sans-serif font (Inter, Nunito Sans, IBM Plex Sans, or Manrope); `renalcarematters.com` attribution in the bottom corner (except the wordless vignette hero, which carries no text by spec); no journal names, guideline acronyms, brand names, or watermarks; no invented numbers. The study-data chart is deliberately **not** in this pack: it is drawn as code-native SVG from `assets/born-small-evidence-data.json`.

---

## 001 — Vignette hero

```
IMAGE NUMBER: 001
SECTION PLACEMENT: Hero, figure.hero-figure.mode-patient > .hero-vignette (patient mode only)
FILE NAME: born-small-kidneys-for-life-vignette-hero.png
ARCHETYPE: Circular vignette hero v3 — Scaffold B still-life; composition archetype I (Object Hero)
AUDIENCE: patients and families
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
VISUAL MIX:
- photorealistic models: none (no people)
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Connect "born small" with lifelong care through a calm, wordless object scene.
KEY CONCEPTS: newborn beginnings, keeping a record, continuity of care
CAMERA: top-down
HUMAN VARIATION (vs. previous guide): no people

COPY-READY IMAGE GENERATOR GPT PROMPT:
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: Object Hero. Camera: top-down.
Subject: a tiny hand-knitted newborn cap in soft oatmeal wool resting beside a closed, plain fabric-covered family health booklet with no visible writing, a loosely curled soft cloth measuring tape with no readable numbers, and a single small sprig of fresh green leaves, arranged on a soft light teal-tinted linen surface (#eef6f7) in gentle morning daylight with shallow depth of field.
Visual hierarchy: the knitted cap and booklet together occupy 60–70% of the circle; the tape and leaves are small supporting elements; reserve a 20–25% TITLE SAFE ZONE of empty linen surface toward the left side of the circle with no objects, labels, or icons inside it. Soft edge falloff toward a slightly deeper neutral at the rim. Calm, hopeful, clinical-but-warm color grade harmonizing with clinical teal #1a6b72 and warm neutrals.
Absolutely NO text of any kind: no readable words or numbers on the booklet or tape, no title, no caption, no logo, no watermark. Full-bleed within the inscribed circle, no rectangular borders.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, tiny unreadable labels, infographic clutter, cropped circle, cropped objects, edge clipping, objects touching the circular border, anything inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark or charcoal or black backgrounds, cartoon style, neon, HDR, over-saturation, hospital wristbands, incubators, medical equipment, babies or body parts, anything that suggests illness or fragility.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin, never cropped. One dominant subject (cap + booklet) at 60–70%, 2 supporting elements, 20–25% empty title-safe zone. No readable text anywhere. Crops cleanly inside the circle.

ALT TEXT: "" (decorative; the adjacent H1 carries the meaning). If treated as informative: "Knitted newborn cap beside a family health booklet."
OG WIDTH: 2048
OG HEIGHT: 2048
```

---

## 002 — Four birth terms

```
IMAGE NUMBER: 002
SECTION PLACEMENT: #birth-terms (patient), below the HTML term cards
FILE NAME: born-small-kidneys-for-life-02-birth-terms.png
ARCHETYPE: Simple figure — Scaffold E variant, 2 × 2 reference grid
AUDIENCE: patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: four rounded cards with simple line icons
- 3D component graphics: none
- algorithm/flowchart: none
PURPOSE: Stop readers from treating low birth weight, preterm, SGA, and FGR as the same thing.
KEY CONCEPTS: weight vs timing vs size-for-age vs growth process; the terms can overlap

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean clinical education reference figure, white (#ffffff) background, all text set in Inter. Bold navy (#0f1e2e) title at top center: "Four ways to describe a small baby". Below it, a 2 × 2 grid of four equal rounded cards on very soft gray (#f3f4f6), each with a thin colored top band, a simple monoline icon, a bold label, and one short line.
Card 1, teal band (#1a6b72), icon of a simple baby scale: "Low birth weight" — "Weighed under 2,500 grams at birth".
Card 2, navy band (#0f1e2e), icon of a calendar page: "Preterm birth" — "Born before 37 completed weeks".
Card 3, amber band (#b8860b), icon of a small dot beside a larger outlined dot: "Small for gestational age" — "Smaller than most babies of the same age in pregnancy".
Card 4, soft purple band (#6c3d8e), icon of a gently flattening growth curve: "Fetal growth restriction" — "Growth slowed before birth".
Bottom strip, full width, soft gray: "These can overlap. Each describes something different." in navy.
Generous whitespace, mobile-readable labels at least 11pt equivalent, no clutter. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, Venn diagrams or overlap proportions, percentile numbers, babies' faces, excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds. Use ONLY Inter; no serif, decorative, or handwritten fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Four cards, correct wording, spelling exact, 2,500 grams and 37 weeks as the only numbers. Light background. Attribution visible bottom-right.

ALT TEXT: "Four cards defining low birth weight, preterm birth, small for gestational age, and fetal growth restriction, noting that they can overlap."
OG WIDTH: 1792
OG HEIGHT: 1024
```

Figcaption: `p.fig-desc` "Four different descriptions of a small baby. A baby can fit one, several, or none." `dl.fig-abbrevs`: none needed (terms spelled out).

---

## 003 — Nephron development and kidney reserve

```
IMAGE NUMBER: 003
SECTION PLACEMENT: #kidney-reserve (patient); reused in #developmental-mechanism (clinician)
FILE NAME: born-small-kidneys-for-life-03-nephron-reserve.png
ARCHETYPE: Biomedical mechanism figure (organ panel → magnified inset → bottom flow)
AUDIENCE: mixed
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: flat vector anatomy with soft semi-3D shading
- 3D component graphics: none
- algorithm/flowchart: bottom three-box flow
PURPOSE: Show why fewer nephrons can leave less margin during illness, without implying a measured count or inevitable kidney failure.
KEY CONCEPTS: nephrogenesis timing, nephron endowment, single-nephron workload, second hits, protection

COPY-READY IMAGE GENERATOR GPT PROMPT:
Create a publication-grade biomedical mechanism schematic, review-article style, white background, muted clinical palette, all labels set in IBM Plex Sans.
Topic: Kidney development before birth and kidney reserve later in life.
Left panel (organ level): a horizontal pregnancy timeline band from early pregnancy to term, light gray-blue, with a soft pale-yellow shaded zone near the end labeled "Nephron formation nears completion, about 34–36 weeks". A small simplified kidney silhouette sits above the band. A thin dashed connector leads to the center panel.
Center panel (magnified, inside a thin dashed box): two kidney outlines of identical size side by side, each containing small symbolic filtering units drawn as tiny glomerulus-like circles. The left kidney, labeled "More filtering units", has many evenly spaced circles. The right kidney, labeled "Fewer filtering units", has noticeably fewer circles, each drawn slightly larger with a small upward arrow beside it labeled "↑ work per unit". A small footnote inside the box: "Symbols only — not a count".
Bottom summary flow, three boxes left to right with arrows:
Left pale-pink box, title "Early start": "Preterm birth", "Growth restriction before birth".
Center box, title "Later stress (second hits)": "Dehydration", "Severe infection", "Some medicines, such as NSAIDs".
Right pale-blue box, title "Protecting the reserve": "Check blood pressure and urine", "Treat illness early", "Medicine review".
Small gray label across the very bottom: "Conceptual mechanism. Birth weight does not measure nephron number."
Thin dashed connectors, generous whitespace, no decorative effects. Bottom-right corner: "© renalcarematters.com" in small semi-transparent navy text.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, cartoon style, numeric nephron counts, percentages, growth curves with numbers, dialysis machines, red alarming kidneys, arrows pointing to "kidney failure", gibberish text, overcrowding. Use ONLY IBM Plex Sans; no serif fonts. Never omit the attribution.

QUALITY CHECK:
Both kidney outlines the same size (only the unit count differs). The 34–36 weeks label is the only number. "Conceptual" footer present. Attribution bottom-right. Light background.

ALT TEXT: "Conceptual diagram: kidney filtering units form late in pregnancy; a kidney with fewer units has more work per unit and less margin during illness, dehydration, or exposure to some medicines."
OG WIDTH: 1792
OG HEIGHT: 1024
```

Figcaption: `p.fig-desc` "Filtering units (nephrons) finish forming late in pregnancy. Fewer units can mean each one works harder, leaving less room during illness. This is a concept drawing, not a measurement." `dl.fig-abbrevs`: `NSAID` Nonsteroidal anti-inflammatory drug.

---

## 004 — Life-course handoffs

```
IMAGE NUMBER: 004
SECTION PLACEMENT: #life-stages (patient), above the HTML step list
FILE NAME: born-small-kidneys-for-life-04-life-course.png
ARCHETYPE: Simple figure — Scaffold C horizontal step sequence (6 steps)
AUDIENCE: patients and families
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
VISUAL MIX:
- photorealistic models: none
- 2D infographic: six cards with monoline icons
- 3D component graphics: none
- algorithm/flowchart: arrows between steps
PURPOSE: Show that the birth history is carried forward at each handoff, not tied to a fixed test schedule.
KEY CONCEPTS: discharge, early childhood, school age, puberty, adulthood, pregnancy planning

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clean clinical education infographic, white (#ffffff) background, all text set in Nunito Sans. Title at top center in bold navy (#0f1e2e): "Carry your birth history forward". Six rounded cards in a single horizontal row on a very soft gray panel (#f3f4f6), joined by bold navy right-pointing arrows. Each card has a teal (#1a6b72) top band, a simple monoline icon, a bold label, and one short line:
1. icon of a small house with a heart: "Going home from the hospital" — "Ask what kidney checks were done".
2. icon of a toddler's shoe: "Around age two" — "Ask if a kidney check is planned".
3. icon of a school bag: "Childhood" — "Blood pressure at visits".
4. icon of a rising growth line: "Puberty" — "Ask about repeat checks".
5. icon of a folder: "Adult care" — "Keep the history in your record".
6. icon of two overlapping circles: "Planning a pregnancy" — "Review current kidney and blood pressure findings".
Bottom strip, full width, soft gray: "Current findings guide the plan. Your history helps your doctor read them." in navy.
Generous whitespace, labels at least 11pt equivalent. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny labels, gibberish text, dates, test names, numbers other than "two", hospital beds, dialysis imagery, dark backgrounds. Use ONLY Nunito Sans; no serif or decorative fonts. Never omit the attribution.

QUALITY CHECK:
Six cards in order, exact wording, reads left to right on mobile when scaled. Light background. Attribution bottom-right.

ALT TEXT: "Six stages from hospital discharge to adult care and pregnancy planning, each with a question to ask about kidney health."
OG WIDTH: 1792
OG HEIGHT: 1024
```

Figcaption: `p.fig-desc` "At each stage of life, bring your birth history and ask what it means for your current checks." No abbreviations.

---

## 005 — OG / social share card

```
IMAGE NUMBER: 005
SECTION PLACEMENT: <head> og:image and twitter:image only (not inline)
FILE NAME: born-small-kidneys-for-life-og.png
ARCHETYPE: OG social share card (infographic skill)
AUDIENCE: mixed
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title lockup with a small kidney line icon
- 3D component graphics: a small, calm semi-photoreal pair of kidneys at right
- algorithm/flowchart: none
PURPOSE: Clear, calm link preview for Facebook, X, and messaging apps.
KEY CONCEPTS: title, subtitle, kidney

COPY-READY IMAGE GENERATOR GPT PROMPT:
Social share card, exactly 1200 × 630 pixels, white (#ffffff) to very light teal (#eef6f7) soft horizontal gradient background. Left two-thirds: large bold navy (#0f1e2e) title in Manrope, two lines: "Born Small," / "Kidneys for Life". Below it in clinical teal (#1a6b72), Manrope regular: "Why your birth history belongs in your kidney care". Right third: a calm semi-photorealistic 3D render of a pair of human kidneys in restrained renal red-brown with soft teal rim light, floating with a gentle shadow, beside a tiny knitted newborn cap in oatmeal wool. Generous whitespace, balanced composition, nothing within 40 px of the edges. Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid dark or navy backgrounds, cartoon style, neon, HDR, extra text, statistics, babies or faces, medical devices, gibberish text, serif fonts. Use ONLY Manrope. Never omit the attribution.

QUALITY CHECK:
Exactly 1200 × 630. Title spelled exactly. Light background. Readable as a small thumbnail.

ALT TEXT: "Born Small, Kidneys for Life — renalcarematters.com"
OG WIDTH: 1200
OG HEIGHT: 630
```

---

## 006 — Clinician assessment pathway (optional)

The HTML `.algo-card` in `#clinical-assessment` is primary. Generate this only if the author wants a printable figure.

```
IMAGE NUMBER: 006
SECTION PLACEMENT: #clinical-assessment (clinician), after the .algo-card
FILE NAME: born-small-kidneys-for-life-06-clinician-pathway.png
ARCHETYPE: Simple figure — Scaffold A conservative flat flowchart (no 3D, no icons)
AUDIENCE: clinicians
ASPECT RATIO: 2:3
PIXEL DIMENSIONS: 1024 × 1536
VISUAL MIX:
- photorealistic models: none
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: boxes and diamonds, minimal color
PURPOSE: Show the practice-proposal workflow and its boundaries.
KEY CONCEPTS: acute illness first, reconstruct perinatal history, current phenotype, existing pathway, named responsibility

COPY-READY IMAGE GENERATOR GPT PROMPT:
Conservative clinical flowchart, white (#ffffff) background, thin navy (#0f1e2e) lines, all text in Inter. Title at top in bold navy: "Birth history in kidney assessment". Small amber (#b8860b) label under the title: "Practice proposal — not a validated prediction rule".
Top diamond: "Acute illness now? (suspected AKI, dehydration, sepsis, obstruction, fluid overload)". Yes arrow right to a red-outlined (#b91c1c) box: "Acute pathway for age and severity". No arrow down.
Box 1: "Reconstruct perinatal history: weight with unit, gestation, documented SGA or FGR, NICU course, newborn AKI or dialysis, congenital conditions, source".
Box 2: "Assess current findings: measured BP, growth, medicines, urine, kidney function interpreted for age".
Diamond: "Abnormal current findings?" Yes arrow right to a teal-outlined (#1a6b72) box: "Evaluate; refer where indicated". No arrow down.
Diamond: "Records incomplete?" Yes arrow right to a gray box: "Clarify records while continuing present care". No arrow down.
Box 3: "Apply the existing care pathway for age and population".
Final green-outlined (#1f7a4d) box: "Name the responsible clinician, review date, and reasons for earlier review".
Maximum four levels deep, generous whitespace, outlined boxes only (no fills except white), no icons. Bottom-center: "renalcarematters.com" in small semi-transparent navy text.
No journal names, guideline acronyms, brand names, or watermarks.

NEGATIVE INSTRUCTIONS:
Avoid 3D, icons, gradients, numeric thresholds, creatinine cutoffs, test intervals, risk scores, spaghetti arrows, dark backgrounds, serif fonts, gibberish text. Use ONLY Inter. Never omit the attribution.

QUALITY CHECK:
No numbers anywhere. "Practice proposal" label visible. Abbreviations limited to AKI, SGA, FGR, NICU, BP. Attribution bottom-center.

ALT TEXT: "Workflow: manage acute illness first, then reconstruct birth history, assess current findings, apply the existing care pathway, and record who follows up and when."
OG WIDTH: 1024
OG HEIGHT: 1536
```

Figcaption: `p.fig-desc` "A practical sequence for using birth history in a kidney assessment. It organizes care; it does not predict risk." `dl.fig-abbrevs`: AKI Acute kidney injury · SGA Small for gestational age · FGR Fetal growth restriction · NICU Neonatal intensive care unit · BP Blood pressure.
