# Nano Banana 2 image prompts — Complement-Mediated Kidney Disease guide

**Guide:** `guides/complement-mediated-kidney-disease.html`
**Model:** Nano Banana 2 (Gemini 3 Pro Image) — Gemini app, Google AI Studio, or the Gemini API (`gemini-3-pro-image`).

## How to use this file (for the operator / Cowork)

Each image below has three parts:

1. **Save as** — the output filename(s). Not part of the prompt.
2. **Aspect ratio** — set this with the app/AI-Studio aspect-ratio control (or the API `aspectRatio`). Not part of the prompt.
3. **A single prompt inside a ``` code block ``` — paste ONLY that block into Nano Banana. Nothing else.**

Rules that keep Nano Banana accurate:

- **Paste only the code block.** Do not paste the "Save as" or "Aspect ratio" lines, and do not paste any of this instructions section — Gemini treats stray form text as things to draw.
- **Aspect ratio is a control, not prompt text.** Every prompt already states the orientation in words ("square", "wide horizontal", "tall vertical") so the two agree; set the matching aspect ratio in the tool.
- **No pixel sizes, no cropping instructions inside a prompt.** Generate at 2K (4K for the hero/posters if offered). The only crop is the OG card — noted in its "Save as" line as a post-step, never in the prompt.
- **On-image words are given in quotes and must be rendered verbatim.** Nano Banana renders text well; if one label comes out wrong, keep the image and tell it *"fix the label to read exactly ‘…’, change nothing else"* rather than regenerating.
- **The hero is wordless** — no text and no attribution line. **Every other figure** must show `© renalcarematters.com` (already written into each prompt).
- Save each as PNG **and** a WebP twin (`images/<name>.png` + `.webp`). Nano Banana adds an invisible SynthID watermark — harmless, and separate from the visible © line.

## Asset map

| # | Save-as stem (`images/…`) | Guide section | Aspect ratio |
|---|---|---|---|
| 1 | `complement-mediated-kidney-disease-vignette-hero` | Patient hero disc | **1:1** (square) |
| 2 | `complement-mediated-kidney-disease-og` | `og:image` / share card | **16:9**, then crop to 1200×630 |
| 3 | `complement-mediated-kidney-disease-01-two-compartments` | "One System, Several Diseases" | **16:9** |
| 4 | `complement-mediated-kidney-disease-02-pathway-map` | "Complement 101" *(optional add)* | **16:9** |
| 5 | `complement-mediated-kidney-disease-03-biopsy-triptych` | "Three Views of One Biopsy" | **16:9** |
| 6 | `complement-mediated-kidney-disease-04-spectrum` | "Driver or Marker?" | **1:1** (square) |
| 7 | `complement-mediated-kidney-disease-05-tma-algorithm` | "TMA Emergency" (clinician) | **2:3** (tall) |
| 8 | `complement-mediated-kidney-disease-06-c3g-pathway` | "Glomerular Pathway" (clinician) | **2:3** (tall) |
| 9 | `complement-mediated-kidney-disease-07-drug-targets` | "Evidence" (clinician) | **16:9** |
| 10 | `complement-mediated-kidney-disease-08-genetics` | "Genetics" | **1:1** (square) |
| 11 | `complement-mediated-kidney-disease-09-safety-shield` | "Infection Safety" | **16:9** |

---

## 1 — Circular vignette hero  (wordless)

**Save as:** `images/complement-mediated-kidney-disease-vignette-hero.png` (+ `.webp`)
**Aspect ratio:** 1:1 (square)

```
A calm, elegant semi-photorealistic 3D medical illustration on a square canvas with a soft off-white background. In the center, a single complement cascade is drawn as a slim vertical chain of glowing teal spheres descending from the upper area, then gently splitting into two paths lower down. The left path ends at a cutaway of a kidney's glomerular filter — a rounded glomerulus with a softly highlighted filtering membrane, where a few small warm-amber deposits settle along the wall. The right path ends at a short cross-section of a small blood vessel whose inner lining is gently swollen and holds two or three soft platelet-cluster clots. Restrained clinical colors — renal reds and clinical teal — on the off-white background, with gentle studio lighting, a soft shadow, and shallow depth of field. Compose so all important elements stay within a central circular area and the four corners are left as plain soft off-white, so the picture crops cleanly into a circle. Textbook-cover calm and simplicity. No people. Absolutely no text, letters, numbers, labels, logos, or watermark anywhere. No violence, no bleeding, no exploding organs.
```

---

## 2 — Open Graph / social share card

**Save as:** `images/complement-mediated-kidney-disease-og.png` — generate 16:9, then crop the result to 1200×630 (title is kept centered so the crop is safe)
**Aspect ratio:** 16:9

```
A clean, modern medical editorial banner, wide horizontal layout, on a light off-white background. On the left side, large bold navy sans-serif title text on two lines reading exactly "When Complement Injures the Kidney". Directly below it, smaller clinical-teal text reading exactly "C3G · CM-TMA/aHUS · IC-MPGN". Below that, a small navy line reading exactly "One cascade. Different compartment. Different disease." Use a clean geometric sans-serif similar to Inter. On the right side, a simple flat illustration of a complement cascade drawn as a slim vertical chain of teal nodes that forks into two small destinations: an upper rounded glomerular kidney-filter icon with a few small amber dots, and a lower small blood-vessel cross-section holding two soft platelet clusters, joined by thin teal lines. Generous empty space, calm and premium, publication-grade. Keep every line of title text well inside the frame with clear margins on all sides. In the bottom-right corner, small semi-transparent gray text reading exactly "© renalcarematters.com". Light background only, no dark background, no drug logos, no clutter.
```

---

## 3 — Two compartments (same cascade, different disease)

**Save as:** `images/complement-mediated-kidney-disease-01-two-compartments.png` (+ `.webp`)
**Aspect ratio:** 16:9

```
A clean medical education comparison illustration, wide horizontal layout, white background, in the style of a journal graphical abstract — clearly a diagram, not a photo. A centered bold navy title reads exactly "Same cascade, different compartment", in a clean sans-serif like Inter. A slim central vertical band shows a shared complement cascade as a chain of small teal nodes, with a small navy caption chip below it reading exactly "Shared complement amplifier". From this central band, a soft arrow points left and a soft arrow points right into two equal rounded-corner panels separated by a soft dashed vertical divider. The left panel header, in navy, reads exactly "Filter-deposit disease — C3G"; it shows a simple cutaway of a kidney filter wall with small amber complement deposits along the membrane, and three short navy labels reading exactly "Protein & blood in urine", "Biopsy diagnosis", and "Slower course". The right panel header, in clinical red, reads exactly "Small-vessel disease — CM-TMA / aHUS"; it shows a simple cross-section of a small blood vessel with a swollen lining, platelet-rich clots inside, and a few fragmented red cells, with three short navy labels reading exactly "Anemia & low platelets", "Acute kidney injury", and "Emergency". Calm restrained clinical colors, generous white space, clearly legible labels. Small semi-transparent navy text in the bottom-right corner reads exactly "© renalcarematters.com". Light background only, no realistic tissue photo, no clutter.
```

---

## 4 — Complement pathway map  *(optional add to "Complement 101")*

**Save as:** `images/complement-mediated-kidney-disease-02-pathway-map.png` (+ `.webp`)
**Aspect ratio:** 16:9

```
A clean medical pathway diagram, wide horizontal layout, white background, journal graphical-abstract style. A bold navy title reads exactly "The complement cascade, in one map", with a clinical-teal subtitle reading exactly "Three entry paths, one amplification hub", in a clean sans-serif like Inter. On the left, three rounded chips labeled exactly "Classical", "Lectin", and "Alternative" each send a thin arrow converging into one prominent central node labeled exactly "C3". A curved looping arrow around the alternative path and C3 is labeled exactly "Amplification loop". From "C3", an arrow leads down to a node labeled exactly "C5", then to a final node labeled exactly "MAC (C5b-9)". Two small calm teal ring icons beside the pathway represent the regulators, grouped in a soft-gray legend box labeled exactly "Regulators (brakes): factor H, factor I, CD46". Thin navy and teal arrows, rounded nodes, generous white space, legible labels. Small semi-transparent navy text in the bottom-right corner reads exactly "© renalcarematters.com". Light background only, no genetic-code motifs, no neon, no clutter.
```

---

## 5 — Three views of one biopsy (LM / IF / EM)

**Save as:** `images/complement-mediated-kidney-disease-03-biopsy-triptych.png` (+ `.webp`)
**Aspect ratio:** 16:9

```
A clean clinical education diagram, wide horizontal layout, white background, showing three stylized illustrative panels — clearly diagrams, never realistic photomicrographs of real tissue. A centered bold navy title reads exactly "Three views of one biopsy", in a clean sans-serif like Inter. Three equal rounded cards sit in a row on a very light gray strip, each with a colored top accent bar, a small simple illustration, a bold navy header, and one short question line. Card 1 has a teal accent bar, a header reading exactly "Light microscopy (LM)", a simplified glomerulus with a proliferative pattern and some scarring, and a question line reading exactly "What pattern & how much scarring?". Card 2 has an amber accent bar, a header reading exactly "Immunofluorescence (IF)", a stylized glomerulus with an even bright glow along the capillary loops, and a question line reading exactly "What is deposited? (C3-dominant)". Card 3 has a soft-purple accent bar, a header reading exactly "Electron microscopy (EM)", a magnified membrane cross-section with dense ribbon-like deposits, and a question line reading exactly "Where & what kind? (DDD vs C3GN)". Thin navy arrows connect the cards. A bottom light-gray strip carries a navy summary line reading exactly "C3G needs all three — a blood test cannot make this diagnosis.". Legible labels, generous space. Small semi-transparent navy text in the bottom-right corner reads exactly "© renalcarematters.com". Light background only, and keep every panel obviously an illustration, never a real slide photo.
```

---

## 6 — Driver, amplifier, or marker spectrum

**Save as:** `images/complement-mediated-kidney-disease-04-spectrum.png` (+ `.webp`)
**Aspect ratio:** 1:1 (square)

```
A clean conceptual medical education diagram, square layout, white background, journal graphical-abstract style. A centered bold navy title reads exactly "Is complement the driver, an amplifier, or just a marker?", in a clean sans-serif like Inter. Three horizontal zones are stacked vertically with soft gradient transitions between them (not hard dividing lines), to read as a spectrum. The top zone has a teal band, a header reading exactly "Primary driver", a short navy caption reading exactly "Complement dysregulation is central — blockade can address the mechanism", and rounded chips reading exactly "C3 glomerulopathy" and "CM-TMA / aHUS". The middle zone has an amber band, a header reading exactly "Amplifier", a caption reading exactly "Another disease starts the injury; complement worsens it — follow disease-specific evidence", and chips reading exactly "some lupus nephritis", "IgA nephropathy", "ANCA vasculitis", "APS", and "transplant injury". The bottom zone has a soft-gray band, a header reading exactly "Marker / bystander", a caption reading exactly "Complement is present but its importance is uncertain — not a treatment ticket", and a chip reading exactly "many inflammatory kidney diseases". Within each soft transition, a small dashed motif carries a tiny label reading exactly "uncertain boundary". Legible labels, generous space. Small semi-transparent navy text in the bottom-right corner reads exactly "© renalcarematters.com". Light background only, no traffic-light good/bad coloring, no clutter.
```

---

## 7 — TMA emergency algorithm

**Save as:** `images/complement-mediated-kidney-disease-05-tma-algorithm.png` (+ `.webp`)
**Aspect ratio:** 2:3 (tall vertical)

```
A clean clinical algorithm flowchart in the style of an American Heart Association emergency algorithm, tall vertical layout, white background, clean sans-serif like Inter, thin dark-gray arrows, rounded boxes and pink decision diamonds, generous spacing, strictly aligned. A bold navy title at the top reads exactly "Suspected TMA — emergency pathway". The flow runs top to bottom as connected boxes:
A peach rounded box reading exactly "Recognize TMA: low platelets and/or hemolytic anemia (MAHA) + organ injury. Do not require the full triad."
then a gray capsule reading exactly "Stabilize · draw pre-treatment complement and genetic samples when feasible"
then a blue rounded box reading exactly "ADAMTS13 BEFORE plasma · treat suspected TTP immediately"
then a pink decision diamond reading exactly "High TTP probability?" — a red "Yes" arrow leads to a blue box reading exactly "Immediate TTP-directed therapy — do NOT wait", and a "No" arrow continues down
then a green rounded box reading exactly "Test Shiga toxin (STEC) when appropriate"
then a peach box reading exactly "Evaluate context: pregnancy/HELLP, severe hypertension, drugs, infection, autoimmune/APS, cancer/HSCT, transplant/CNI, metabolic"
then a pink diamond reading exactly "CM-TMA likely with active organ injury?" leading to a green box reading exactly "Consider urgent C5 blockade under specialist care — without waiting for genetics"
then a dashed horizontal divider carrying a small label reading exactly "Later, for planning — not the emergency decision"
then, below the divider, a gray box reading exactly "Genetics and anti-factor H plus longitudinal phenotype refine duration, relapse, family and transplant planning".
Every box is clearly connected by arrows and every line of text is legible. Small gray text in the bottom-right corner reads exactly "© renalcarematters.com". White background only, no photos, no 3D, no dark background.
```

---

## 8 — C3G / IC-MPGN diagnostic pathway

**Save as:** `images/complement-mediated-kidney-disease-06-c3g-pathway.png` (+ `.webp`)
**Aspect ratio:** 2:3 (tall vertical)

```
A clean, publication-ready clinical algorithm flowchart, tall vertical layout, white background, restrained navy and clinical-teal styling, clean sans-serif like Inter, thin teal arrows, generous margins, centered. A bold navy title at the top reads exactly "C3G / IC-MPGN — a phenotype-first pathway". The flow runs top to bottom as connected nodes:
a teal node reading exactly "Confirm glomerular syndrome + urgency"
then a teal node reading exactly "Kidney biopsy: LM + IF + EM"
then a teal decision node that fans into four short rounded branch boxes reading exactly "C3-dominant → C3-dominant GN differential", "Ig + complement → IC-MPGN differential", "Monoclonal pattern → MGRS work-up", and "TMA lesions → TMA pathway"
then a full-width amber caution box reading exactly "Exclude mimics: infection-related GN (can be C3-dominant), endocarditis, autoimmune, cryoglobulins, MASKED monoclonal deposits — primary IC-MPGN is a diagnosis of exclusion"
then a green endpoint box reading exactly "Characterize complement: C3/C4, functional pathways, activation products, nephritic factors and autoantibodies, CNV-aware genetics".
A soft-gray side note reads exactly "C3 dominance = C3 at least 2 orders of magnitude over any other reactant on IF — a pathology threshold, not a blood ratio." Every node is connected by thin teal arrows and every line of text is legible. Small gray text in the bottom-right corner reads exactly "© renalcarematters.com". White or very light background only, no dark background, no people, no clutter.
```

---

## 9 — Drug-target overlay (where the drugs act)

**Save as:** `images/complement-mediated-kidney-disease-07-drug-targets.png` (+ `.webp`)
**Aspect ratio:** 16:9

```
A clean medical mechanism diagram, wide horizontal layout, white background, journal graphical-abstract style, clearly a diagram. A bold navy title reads exactly "Where the drugs act on complement", with a clinical-teal subtitle reading exactly "Different points, different biology — this figure ranks no drug", in a clean sans-serif like Inter. A horizontal complement cascade of rounded nodes runs left to right: entry paths, then a prominent node labeled exactly "C3 / C3b", then a node labeled exactly "C5", then a final node labeled exactly "MAC (C5b-9)", with a curved loop around the early segment labeled exactly "alternative-pathway amplification loop". Three identical teal bracket markers of the same size and style sit on the cascade, labeled exactly "Factor B — alternative-pathway amplification", "C3 / C3b — proximal convergence", and "C5 — terminal C5a & MAC"; keep all three markers visually identical so none looks preferred. Below the cascade, a light-gray strip carries three short navy notes reading exactly "Proximal blockade lowers C3 activation & deposition", "Terminal (C5) blockade spares upstream C3", and "All raise encapsulated-bacterial infection risk". Legible labels, generous space. Small semi-transparent navy text in the bottom-right corner reads exactly "© renalcarematters.com". Light background only; no medals, stars, checkmarks, or size differences implying one drug is best; no drug logos.
```

---

## 10 — Genetics: susceptibility, not destiny

**Save as:** `images/complement-mediated-kidney-disease-08-genetics.png` (+ `.webp`)
**Aspect ratio:** 1:1 (square)

```
A clean conceptual medical education diagram, square layout, white background, clearly an illustration. A bold navy title reads exactly "Genetics is susceptibility — not destiny", in a clean sans-serif like Inter. Draw a calm left-to-right branching probability tree — NOT a DNA double helix and NOT falling code characters. On the left, three stacked rounded input chips read exactly "Susceptibility variant", "Trigger (infection, pregnancy, BP)", and "Each person's regulator & tissue context", joined by thin teal arrows into a central navy node reading exactly "Combined risk". From that node, thin teal branches fan out to outcome chips of visibly different sizes to suggest probability: two larger green chips each reading exactly "No disease", one medium amber chip reading exactly "Disease develops", and one small gray chip reading exactly "Uncertain". Along the bottom, a navy caption strip reads exactly "Same variant, different outcomes — penetrance is incomplete. A VUS is not actionable on its own; a negative panel does not rule disease out." Legible labels, generous space. Small semi-transparent navy text in the bottom-right corner reads exactly "© renalcarematters.com". Light background only. Do not draw a DNA helix, do not draw falling-code motifs, and do not use red-versus-green good-gene/bad-gene coloring beyond the neutral chips described.
```

---

## 11 — Treatment safety shield (infection prevention)

**Save as:** `images/complement-mediated-kidney-disease-09-safety-shield.png` (+ `.webp`)
**Aspect ratio:** 16:9

```
A clean patient-education infographic, wide horizontal layout, white background, calm and reassuring. A bold navy title at the top reads exactly "Complement blockade comes with a safety shield", in a clean sans-serif like Inter. In the center, a simple elegant translucent teal shield outline — a plain rounded shield, not a heraldic or military emblem — surrounds a small neutral patient icon. Arranged evenly around the shield are five equal rounded cards, each with a simple flat line icon and a short navy label, reading exactly "Vaccinate — meningococcal ACWY & B, pneumococcal, Hib", "Carry an emergency card", "Treat fever urgently — don't wait for the next infusion", "Direct care-team contact", and "Ongoing monitoring". Along the bottom, a full-width amber strip carries navy text reading exactly "Vaccination lowers the risk — it does not remove it. Fever or meningitis symptoms are an emergency." Keep the five icons simple and equal, with generous white space and legible labels. Small semi-transparent navy text in the bottom-right corner reads exactly "© renalcarematters.com". Light background only, no scary needle close-ups, no weapons, no clutter.
```

---

## After generating

- Save each as `images/<name>.png` **and** a WebP twin. The guide's `<picture>` blocks load WebP first, PNG fallback.
- Confirm the on-image words match the guide's figure captions; if a label renders wrong, keep the image and tell Nano Banana *"fix only that label to read exactly ‘…’"*.
- The hero has no text and no attribution; every other figure must show `© renalcarematters.com` bottom-right.
- Asset #4 (pathway map) still needs its inline `<figure>` added to "Complement 101"; the other ten are already referenced in the HTML.
