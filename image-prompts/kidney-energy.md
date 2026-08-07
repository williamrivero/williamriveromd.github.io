# Image prompts — Kidney Energy guide

**Guide:** `guides/kidney-energy.html`
**Target folder on disk:** `images/`
**House style:** renalcarematters.com — clean, publication-grade biomedical illustration; restrained clinical palette (deep teal `#1a6b72`, navy `#1f3864`, muted amber, soft slate neutrals, white background); flat/semi-flat vector or soft-3D medical-textbook look; **NOT** futuristic, neon, cybernetic, or "glowing tech." Accurate anatomy. Qualitative labels only — **no fabricated percentages or numbers on any figure.** Small `© renalcarematters.com` credit, bottom-right, 11 px, muted grey.

Each block below is a ready-to-paste ChatGPT Image Generator prompt. Filenames and dimensions are fixed — the guide already references them (`../images/<name>.webp` with `.png` fallback), so keep names exact. Export **PNG** at the stated pixel size; a WebP twin is generated afterward.

---

## 1. `kidney-energy-hero` — Hero (circular vignette)
- **Size:** 2048 × 2048 (square; renders inside a circular vignette on the page)
- **Alt (already in HTML):** "A kidney cutaway transitioning into a magnified nephron and a proximal tubular cell whose mitochondria generate ATP to power sodium recovery."

**Prompt:**
> Publication-grade medical illustration, square composition, clean clinical style (not futuristic or cybernetic), soft studio lighting on a white-to-pale-mint background. A cross-sectioned human kidney on the left smoothly transitions, via one dashed magnifier line, into a magnified single nephron, which transitions again into one enlarged proximal tubular epithelial cell on the right. Inside that cell, show several realistic mitochondria (cristae visible) as small warm-toned "power plants" emitting tidy ATP tokens; a row of basolateral sodium-potassium pumps on the cell's blood-facing membrane uses those ATP tokens to move sodium ions out, with small arrows showing sodium and water being reclaimed from the tubule lumen back toward a peritubular capillary. Restrained palette: deep teal, navy, muted amber for mitochondria, soft slate outlines, white background. Balanced negative space in the upper-left title-safe area (keep it clean, no text there). Labels minimal and qualitative. Reserve the outer 10–12% as clean margin so the circle crop does not clip anatomy. No baked-in headline text. Small "© renalcarematters.com" bottom-right in muted grey.

*(Optional: if a text version is wanted instead of the clean vignette, overlay top-left — Title "Kidney Energy", subtitle "How mitochondria power filtration, recovery, and repair" — in Inter, navy. Default is the no-text clean version.)*

---

## 2. `kidney-energy-01-filtration-reabsorption` — Where the energy goes
- **Size:** 1536 × 1024 (landscape)
- **Alt:** "A two-stage schematic: a glomerulus performing pressure-driven filtration on the left, and a tubule performing ATP-intensive selective recovery on the right."

**Prompt:**
> Clean two-panel medical schematic, landscape, white background, restrained clinical palette (teal, navy, amber, slate). LEFT panel labeled "Filtration — pressure-driven": a glomerulus with an afferent and efferent arteriole and Bowman's capsule; show blood pressure pushing a broad mixture of water and small molecules across the filter into the tubule; a small pressure-gauge motif conveys "driven by pressure, not by cellular energy"; deliberately NO mitochondria/ATP here. RIGHT panel labeled "Selective recovery — ATP-intensive": a proximal tubule segment lined with epithelial cells packed with small mitochondria emitting ATP tokens, with labeled arrows reclaiming sodium, water, glucose, amino acids, and bicarbonate back into a peritubular capillary; a few unwanted wastes continue down toward urine. A slim central divider with a right-pointing flow arrow. Bottom caption band: "Filtration begins the job. Reabsorption uses the energy." Flat vector textbook style, qualitative labels only, no numbers. "© renalcarematters.com" bottom-right.

---

## 3. `kidney-energy-02-atp-chain` — The renal energy chain
- **Size:** 1536 × 1024 (landscape)
- **Alt:** "The renal energy chain: fatty acids and other fuels enter mitochondria, which produce ATP; ATP powers the Na/K-ATPase, which builds the sodium gradient that drives solute and water recovery."

**Prompt:**
> Clean horizontal process-chain infographic, landscape, white background, teal/navy/amber palette, flat vector medical style. Five linked stages connected by bold right-pointing arrows: (1) "Fuels" — a small cluster of labeled fatty-acid chains plus smaller glucose, lactate, and glutamine icons (make clear fatty acids are one of several fuels, not the only one); (2) "Mitochondria" — a realistic mitochondrion with cristae, with a small oxygen (O₂) inflow icon; (3) "ATP" — a stack of ATP tokens; (4) "Na⁺/K⁺-ATPase" — a membrane pump exchanging 3 sodium out / 2 potassium in; (5) "Solute & water recovery" — arrows reclaiming sodium and water into a capillary. Under stage 2 add tiny secondary labels "TCA cycle → respiratory chain → ATP synthase." Keep it uncluttered and legible on mobile. No fabricated numbers. Caption strip: "More fuel does not help if the generators are damaged." "© renalcarematters.com" bottom-right.

---

## 4. `kidney-energy-03-nephron-fuels` — Nephron metabolic map
- **Size:** 1536 × 1024 (landscape)
- **Alt:** "A nephron metabolic map showing proximal tubule, thick ascending limb, distal tubule, and collecting duct across cortex, outer medulla, and inner medulla, with qualitative labels for mitochondrial density, oxidative metabolism, glycolytic capacity, and oxygen vulnerability."

**Prompt:**
> Clean anatomical nephron diagram, landscape, white background, restrained clinical palette. Draw a single nephron correctly oriented across three faint horizontal zone bands labeled at the right edge: "Cortex" (top), "Outer medulla" (middle), "Inner medulla" (bottom). Label the segments: proximal tubule (in cortex), thick ascending limb (crossing into outer medulla), distal convoluted tubule (cortex), collecting duct (descending through medulla), plus the glomerulus and loop of Henle. For each labeled segment, attach a small qualitative legend chip using filled/half/empty dot indicators (NOT numbers) for four attributes: mitochondrial density, oxidative metabolism, glycolytic capacity, oxygen vulnerability — e.g., proximal tubule = high mitochondria / high oxidative / low glycolysis / high O₂ vulnerability; thick ascending limb = high transport / high O₂ vulnerability; collecting duct = more glycolytic capacity. Add a subtle blue-to-pale gradient making the medulla read as lower-oxygen. Include a compact legend key explaining the dot scale. Avoid the oversimplification "cortex = fat, medulla = sugar" — show a spectrum. Flat medical-textbook vector. "© renalcarematters.com" bottom-right.

---

## 5. `kidney-energy-04-healthy-vs-failed-repair` — Healthy vs. failed-repair tubule
- **Size:** 1536 × 1024 (landscape)
- **Alt:** "A side-by-side comparison of a healthy proximal tubular cell versus an injured, failed-repair cell."
- *(Used in both the patient injury section and the clinician oxygenation section.)*

**Prompt:**
> Clean split-comparison medical illustration, landscape, white background, two enlarged proximal tubular epithelial cells side by side. LEFT, framed in calm green, labeled "Healthy": abundant well-formed mitochondria with clear cristae actively burning fatty acids (fatty-acid oxidation), plentiful ATP tokens, an intact brush border and preserved cell polarity, tidy basolateral sodium pumps, effective transport arrows. RIGHT, framed in muted red, labeled "Injured / failed repair": swollen fragmented mitochondria, few ATP tokens, intracellular lipid droplets accumulating, scattered reactive-oxygen-species spark motifs, a lost/blunted brush border, disrupted polarity, and small inflammatory/pro-fibrotic signal arrows radiating outward with a hint of surrounding scar (collagen) texture. Restrained palette (teal/navy accents, green vs red framing only for the two states). Clear qualitative labels, no numbers. "© renalcarematters.com" bottom-right.

---

## 6. `kidney-energy-05-oxygen-balance` — Oxygen supply vs. demand
- **Size:** 1536 × 1024 (landscape)
- **Alt:** "A balance scale weighing oxygen supply against oxygen demand, with output states of balanced metabolism, hypoxic stress, and ATP failure."

**Prompt:**
> Clean conceptual medical infographic, landscape, white background, teal/navy/amber palette. Center: a balance scale. LEFT pan labeled "Oxygen supply" holding small labeled icons: renal blood flow, hemoglobin (red cells), oxygen saturation (O₂), microcirculation (capillary network). RIGHT pan labeled "Oxygen demand" holding icons: filtered sodium load, tubular transport (a pump), hormonal stimulation, overall nephron workload. Below the scale, three horizontal outcome states shown as a small traffic-light-style row (qualitative, not numeric): "Balanced metabolism" (green, level scale), "Hypoxic stress" (amber, tipping), "ATP failure" (red, fully tipped). Add a small side note motif of countercurrent vessels illustrating that high blood flow can still leave tissue oxygen-tight. Flat clinical vector, legible on mobile. "© renalcarematters.com" bottom-right.

---

## 7. `kidney-energy-06-diet-reality` — Diet reality check
- **Size:** 1536 × 1024 (landscape)
- **Alt:** "A contrast between a misleading model (eat more fat leads to more kidney ATP) and an accurate model."

**Prompt:**
> Clean two-part "myth vs. reality" infographic, landscape, white background, restrained clinical palette. TOP row labeled "Misleading" with a faded/greyed style and a small red struck-through arrow: a bowl of fatty food → a big arrow → a kidney glowing with energy, captioned "Eat more fat → more kidney ATP" (shown as incorrect). BOTTOM row labeled "Accurate" in confident teal: four input tiles combining with plus signs — "Balanced nutrition" + "Intact mitochondria" + "Oxygen delivery" + "Manageable workload" → a single arrow → "Effective ATP production" (a healthy tubule cell). Make the visual message clear that ATP emerges only from the combination, not from fat alone. Flat vector, qualitative, no numbers. "© renalcarematters.com" bottom-right.

---

## 8. `kidney-energy-07-protection-layers` — Protect the renal power system
- **Size:** 1536 × 1024 (landscape)
- **Alt:** "A layered framework for protecting the renal power system."

**Prompt:**
> Clean layered/stacked framework infographic, landscape, white background, teal/navy palette with subtle amber accents. Show six concentric or stacked protective layers around a central healthy kidney icon, each labeled: (1) "Avoid new injury"; (2) "Reduce transport & pressure burden"; (3) "Protect perfusion & oxygen delivery"; (4) "Support metabolic health"; (5) "Use evidence-based kidney-protective treatment"; (6) "Monitor & correct reversible abnormalities." Each layer gets one or two tiny representative icons (e.g., blood-pressure cuff, water drop for hydration, running figure for activity, pill for guideline therapy, lab tube for monitoring). Keep hierarchy clear and calm. Do NOT label these as official guideline "pillars" — neutral wording only. Flat clinical vector. "© renalcarematters.com" bottom-right.

---

## 9. `kidney-energy-og` — Open Graph share card
- **Size:** 1200 × 630 (landscape, exact — social crop)
- **Alt:** "A proximal tubular cell rich in mitochondria generating ATP that powers sodium reabsorption."

**Prompt:**
> Landscape 1200×630 social share card, clean biomedical style, deep-teal-to-navy background with a bright focal area on the right. RIGHT side: a single enlarged proximal tubular cell rich in realistic mitochondria emitting ATP tokens that power a membrane sodium pump — clear, elegant, not cluttered. LEFT side: generous text-safe area with headline "How Do Your Kidneys Stay Energized?" and subheadline "ATP, mitochondria, fatty acids, oxygen and kidney protection" in Inter/Manrope, white and pale-gold, high contrast for legibility at small sizes. Keep all text well inside the safe margins (Facebook/X may crop edges). Restrained clinical palette, no neon. Small "renalcarematters.com" wordmark bottom-left. "© renalcarematters.com".

---

### Post-generation (per repo convention)
1. Save each PNG into `images/` with the exact filename above.
2. Create a WebP twin for each (`cwebp -q 82 name.png -o name.webp`); the guide loads WebP first with PNG fallback.
3. From the repo root, re-run so the hero/OG ship optimized:
   `python3 patch_hero_fetchpriority.py --guide kidney-energy.html` and
   `python3 patch_hero_fullwidth.py --guide kidney-energy.html`.
4. The `og:image` is already set to `kidney-energy-og.png` (1200×630) in the head.
