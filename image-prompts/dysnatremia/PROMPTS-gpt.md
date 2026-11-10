# ChatGPT Image Generator Prompt Pack — Dysnatremia (Constitution v1.0)

**Guide:** `guides/dysnatremia.html` · **Plan:** `IMAGE-PLAN.md` · **Generator:** https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Assets:** 12 prompts (H, OG, 01–10). Each prompt is self-contained: paste everything inside one code block, generate, then save
as `generated-images/<FILE NAME>` and export `.png` + `.webp` to `images/` with the same stem.

**Non-negotiables in every prompt:** seven Constitution layers in order (A → G) · light backgrounds only · Inter/Manrope sans-serif ·
illustrated semi-3D publication style (not flat vector, not cartoon) · medical term + plain English on key labels · numbers only from
the guide · no drug doses · attribution `© renalcarematters.com` specified in Layers C, E and G.

**Production tips:** generate H and OG first; if small text garbles, regenerate with "render every label crisply, spelled exactly as
written"; for portrait algorithms (03, 04) ask for "larger node text" before accepting; keep the strongest of two renders.

---

## H · dysnatremia-vignette-hero

**IMAGE NUMBER:** H  
**SECTION PLACEMENT:** Patient-tab hero disc (`figure.hero-figure > .hero-vignette`)  
**FILE NAME:** dysnatremia-vignette-hero.png  
**ARCHETYPE:** Circular vignette hero v3 — Scaffold B, still-life (non-people hero)  
**AUDIENCE:** Dual (patients and clinicians)  
**ASPECT RATIO:** 1:1  
**PIXEL DIMENSIONS:** 2048 × 2048  
**VISUAL MIX:**  
- photorealistic models: none (deliberate non-people hero)  
- 2D infographic: none  
- 3D component graphics: photoreal still-life objects  
- algorithm/flowchart: none  
**PURPOSE:** Give the guide a calm, instantly readable symbol of "water versus salt balance" without text or fear imagery.  
**KEY CONCEPTS:** water, salt, balance, measurement  
**ALT TEXT:** A clear glass carafe of water and a small mound of coarse sea salt balanced on a simple scale beside a blood sample tube, in soft morning light.  
**OG WIDTH:** 2048  
**OG HEIGHT:** 2048

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed for a CSS circular mask: the visual sits inside a central circle occupying 85–90% of the canvas with a visible white border all around (never cropped). Subject: water and salt in balance — the guide "Sodium Too Low or Too High? Understanding Dysnatremia".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Hero contains NO text, numbers, letters or logos except the tiny attribution footer
- Objects must be physically plausible: liquid level, refraction, salt crystal texture, glass thickness
- Blood tube: plain light-green-top (lithium heparin) vacutainer with blank white label — no readable writing

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Hero subject (60–70% of the circle): a minimalist two-pan brass-and-wood kitchen balance, perfectly level; LEFT pan holds a small clear glass carafe of water, RIGHT pan holds a small ceramic dish with a mound of coarse white Philippine sea salt (asin)
- Supporting elements (2–3): one blood sample tube lying in front at a slight angle; a few spilled salt crystals; a single droplet on the carafe
- Title-safe zone: keep the LEFT 20–25% of the circle as calm soft-gradient negative space (no objects)
- Camera: eye-level, 50 mm, shallow depth of field, objects right-of-center

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Setting: a light warm-white tabletop on a woven banig placemat (subtle Filipino texture), soft diffused morning window light from the right, gentle shadow
- Mood: calm, clean, premium medical-editorial cover; balance and precision rather than alarm
- Color: whites, pale teal reflections in the water, warm wood, a hint of brass; one small teal accent (e.g., ribbon on the carafe neck)
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No people, hands or faces
✗ No hospital IV bags, needles or syringes
✗ No text on the tube, scale or dish
✗ No tipped or unbalanced scale
✗ No neon, HDR or heavy vignette
✗ No dark wood or dark moody lighting
✗ No salt shaker brand labels or packaging
✗ Circle must not touch the canvas edge

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Premium medical-editorial still-life photography; hero-vignette v3 Scaffold B
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Circle occupies 85–90% with white border all around — confirmed
□ Scale perfectly level — confirmed
□ Water left pan, salt right pan — confirmed
□ Left 20–25% title-safe zone empty — confirmed
□ Tube label blank — confirmed
□ Banig texture subtle, not dominant — confirmed
□ Bright, airy lighting — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## OG · dysnatremia-og

**IMAGE NUMBER:** OG  
**SECTION PLACEMENT:** `og:image` / `twitter:image` share card; source for `dysnatremia-rg-thumb.webp`  
**FILE NAME:** dysnatremia-og.png  
**ARCHETYPE:** OG social share card (infographic-skill; fixed 1200×630)  
**AUDIENCE:** Dual  
**ASPECT RATIO:** 1.91:1  
**PIXEL DIMENSIONS:** 1200 × 630  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: title block + two value chips  
- 3D component graphics: small balance-scale icon from the hero  
- algorithm/flowchart: none  
**PURPOSE:** Make the shared link self-explanatory on Facebook/Viber/X.  
**KEY CONCEPTS:** low sodium, high sodium, water balance  
**ALT TEXT:** Share card reading "Sodium Too Low or Too High? Understanding Dysnatremia" with a balance scale of water and salt.  
**OG WIDTH:** 1200  
**OG HEIGHT:** 630

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Social share card, exactly 1200×630 px, white background, for the renalcarematters.com guide "Sodium Too Low or Too High? Understanding Dysnatremia".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Use only these numbers: "below 135" and "above 145" (mmol/L)
- No clinical claims beyond the title and the two chips

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Left 60%: text block; right 40%: illustrated semi-3D balance scale — water carafe on one pan, salt dish on the other, level
- Safe margins 48 px on all sides (platform crops)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Eyebrow (teal, Manrope caps, letter-spaced): "ELECTROLYTES · SALT & WATER"
- Title (navy, Inter bold, 2 lines): "Sodium Too Low or Too High?" / second line in ORANGE #C55A11: "Understanding Dysnatremia"
- Two rounded chips under the title: teal chip "Low sodium · below 135 mmol/L"; orange chip "High sodium · above 145 mmol/L"
- Small line under chips (navy, Manrope): "For patients, families and clinicians"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No photo of a person
✗ No more than the specified text
✗ No dark background bands
✗ No drug names or doses
✗ No emoji
✗ No text closer than 48 px to edges
✗ No gradient behind text that lowers contrast
✗ No logo other than the attribution

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: renalcarematters.com OG card house style; infographic-skill v5 OG rule
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Exactly 1200×630 — confirmed
□ Title spelled "Dysnatremia" (American spelling) — confirmed
□ Chips read 135 and 145 correctly — confirmed
□ Scale level — confirmed
□ Text contrast ≥ 4.5:1 — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 01 · dysnatremia-01-salt-water-balance

**IMAGE NUMBER:** 01  
**SECTION PLACEMENT:** Patient tab · "What your sodium number really measures" (#what)  
**FILE NAME:** dysnatremia-01-salt-water-balance.png  
**ARCHETYPE:** Visual-aid hybrid — side-by-side comparison (simple-figure Scaffold B)  
**AUDIENCE:** Patient-first, dual-labeled  
**ASPECT RATIO:** 16:9 (approx. 7:4)  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: three comparison cards + control strip  
- 3D component graphics: three soup bowls, small kidney, brain and water-glass icons  
- algorithm/flowchart: none  
**PURPOSE:** Correct the "low sodium = eat more salt" myth by showing sodium as salt-to-water ratio, then name the three control systems.  
**KEY CONCEPTS:** ratio not amount; dilution; concentration; thirst; vasopressin; kidneys  
**ALT TEXT:** Three bowls of soup with the same salt: extra water reads low sodium, normal water reads normal, too little water reads high sodium; below, thirst, vasopressin and the kidneys keep the balance.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 patient-education visual aid. Title (navy, Inter bold): "Your sodium number = how much water is mixed with your salt".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Same amount of salt in all three bowls — shown by an identical small salt-spoon icon above each bowl
- Normal blood sodium 135–145 mmol/L; low below 135; high above 145
- Vasopressin is made in the brain (hypothalamus) and released from the posterior pituitary; it acts on the kidney to keep water
- Kidney orientation inset (if any): convex border LATERAL, hilum MEDIAL facing the spine; renal pelvis exits at the medial hilum ONLY
- Minor calyces cup the papillae and drain INWARD toward the central pelvis; medullary pyramids triangular with apex (papilla) pointing inward

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Top 65%: three equal cards left→right: "TOO MUCH WATER" · "BALANCED" · "TOO LITTLE WATER"
- Bottom 35%: horizontal control strip with three linked icons: brain → water glass → kidney

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Card 1 (teal border): wide bowl filled to the brim with very pale, watery soup (sabaw) and the salt-spoon icon; label "Low sodium (hyponatremia) — below 135"; sub-label "Same salt, extra water"
- Card 2 (green border): bowl of normal-color clear soup; label "Normal — 135 to 145"; sub-label "Salt and water in balance"
- Card 3 (orange border): small bowl with reduced, darker, concentrated broth and steam; label "High sodium (hypernatremia) — above 145"; sub-label "Same salt, water lost"
- Control strip: icon 1 brain with small droplet "Thirst (makes you drink)"; icon 2 brain-pituitary with hormone arrow "Vasopressin (water-holding hormone)"; icon 3 kidney "Kidneys (keep or release water)"; thin navy arrows linking them
- Small myth-buster tag (purple) at strip right: "Low sodium usually means too much water — not too little salt"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ Do not change the salt amount between bowls
✗ No salt shaker pouring into bowls
✗ No brand names on bowls or spoons
✗ No IV bags or hospital scenes
✗ Kidney icon must not have a lateral hilum or outward calyces
✗ No numbers other than 135 and 145
✗ No more than 6 labels per card
✗ Bowls must look like Filipino home soup, not cream soup

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Netter-style clarity for icons; renalcarematters.com patient visual-aid series
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Identical salt-spoon icon above each bowl — confirmed
□ Water level visibly differs (high / normal / low) — confirmed
□ Labels: below 135 / 135 to 145 / above 145 — confirmed
□ "Vasopressin (water-holding hormone)" spelled correctly — confirmed
□ Kidney icon hilum medial — confirmed
□ Myth tag present in purple — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 02 · dysnatremia-02-brain-adaptation

**IMAGE NUMBER:** 02  
**SECTION PLACEMENT:** Patient tab · "Why the hospital corrects it slowly" (#slow); Clinician tab · Mechanism (#md-physiology)  
**FILE NAME:** dysnatremia-02-brain-adaptation.png  
**ARCHETYPE:** Biomedical mechanism figure — 4-frame timeline (organ context → magnified cells → injury → protection)  
**AUDIENCE:** Dual  
**ASPECT RATIO:** 16:9  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: timeline strip + callout cards  
- 3D component graphics: astrocyte/brain cells, myelinated axon  
- algorithm/flowchart: left-to-right sequence  
**PURPOSE:** Show why speed matters: cells swell, adapt over ~48 h, and are injured if sodium is pushed up too fast.  
**KEY CONCEPTS:** cerebral edema; osmolyte loss; adaptation; osmotic demyelination; slow correction  
**ALT TEXT:** Four frames of brain cells: normal; swollen after a sudden fall in sodium; back to normal size after about two days of adaptation; and shrunken with damaged myelin when sodium is raised too fast.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 biomedical mechanism figure. Title (navy, Inter bold): "The brain adapts slowly — so sodium must be corrected slowly".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Frame order is fixed: 1 normal → 2 acute swelling (hours) → 3 adapted after about 48 hours (cells normal size, fewer internal particles) → 4 too-fast correction (cells shrink; myelin sheath damaged)
- Osmolytes shown as small colored particles inside cells (electrolytes and organic osmolytes such as myo-inositol, taurine, glutamine) — fewer particles in frame 3
- Water movement arrows: INTO cells in frame 2; OUT of cells in frame 4
- ODS signs appear 2 to 6 days later (text only, no patient depiction)
- Small whole-brain inset on the far left with a dashed connector to the magnified cells; pons gently highlighted (ODS classic site)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Top band: four equal frames left→right, each a dashed-border magnified panel of 3–4 brain cells (astrocytes) beside one myelinated nerve fiber
- Bottom band: a clock/timeline strip under the frames: "Normal" · "Hours" · "About 48 hours" · "Too-fast rise"
- Bottom right: two summary boxes — pale pink "Injury" and pale blue "Protection"

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Frame 1 label: "Normal balance"
- Frame 2 label: "Sudden low sodium → cells swell (brain swelling)"; teal arrows of water entering
- Frame 3 label: "Cells adapt: release particles → normal size"; fewer particles shown
- Frame 4 label: "Sodium raised too fast → cells shrink, myelin injured"; water arrows leaving; myelin sheath frayed in red
- Pink box: "Osmotic demyelination syndrome (ODS) — can appear 2–6 days later"
- Blue box: "Protection: aim for a small rise (+4 to 6), stay under the 24-hour ceiling, check sodium often"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No seizure or patient scene
✗ Do not show frame 3 cells swollen
✗ Do not reverse water-arrow directions
✗ No numbers except 48 hours, 2–6 days, +4 to 6
✗ No MRI image
✗ Myelin damage only in frame 4
✗ No bloody or gory depiction
✗ No more than 2 lines per label

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Robbins & Cotran clarity; JASN/CJASN mechanism figures; biomedical-mechanism-figure house template (organ → magnified unit → injury → intervention → benefit)
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Frame order normal → swollen → adapted → shrunken — confirmed
□ Particle count lowest in frame 3 — confirmed
□ Water arrows in (2) and out (4) — confirmed
□ Myelin injured only in frame 4 — confirmed
□ Pons highlighted in brain inset — confirmed
□ "+4 to 6" and "2–6 days" correct — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 03 · dysnatremia-03-tonicity-first

**IMAGE NUMBER:** 03  
**SECTION PLACEMENT:** Clinician tab · "Establish tonicity before anything else" (#md-tonicity)  
**FILE NAME:** dysnatremia-03-tonicity-first.png  
**ARCHETYPE:** Clinical algorithm — algorithm-generator Mode C (renalcarematters.com house style), portrait  
**AUDIENCE:** Clinician (dual-labeled)  
**ASPECT RATIO:** 2:3  
**PIXEL DIMENSIONS:** 1024 × 1536  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: rounded decision/action nodes  
- 3D component graphics: small glyphs only (lab tube, urine cup)  
- algorithm/flowchart: top-to-bottom, ≤ 4 levels  
**PURPOSE:** Make the first step unmissable: classify by tonicity before treating a low sodium.  
**KEY CONCEPTS:** measured osmolality; glucose correction; pseudohyponatremia; translocational hyponatremia; hypotonic  
**ALT TEXT:** Algorithm: low sodium → measure osmolality, glucose and assay → hypotonic, isotonic or pseudo, or hypertonic categories with what each means.  
**OG WIDTH:** 1024  
**OG HEIGHT:** 1536

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Portrait 1024×1536 clinical algorithm, top-to-bottom. Title (navy, Inter bold): "Low sodium? Check tonicity first".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Thresholds are approximate and drawn as soft gray-zone bands, never hard walls
- Every terminal node names a mechanism, not a drug dose
- Hypotonic: measured osmolality below about 275 mOsm/kg (interpret with glucose and ineffective osmoles)
- Pseudohyponatremia: very high lipids or proteins with an INDIRECT electrode; normal osmolality; a direct-electrode (blood gas) sodium is normal
- Hypertonic/translocational: high glucose, mannitol or glycine; corrected sodium shown with two factors (1.6 and 2.4 per 100 mg/dL above 100)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Single trunk top-to-bottom; maximum 3 branches per level; no crossing lines
- Emergency banner (if any) sits ABOVE the tree as a separate red bar
- Caveat ribbon at the bottom

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Top node (navy outline): "Sodium below 135 mmol/L"
- Action node (teal): "Measure plasma osmolality · glucose · sodium method · ask about mannitol, irrigation, alcohol"
- Three branches: LEFT green-outlined "Hypotonic (osmolality < ~275)" → "True water excess → go to urine studies"; CENTER gray "Normal osmolality + very high lipids/proteins" → "Pseudohyponatremia (lab artifact) → repeat on blood-gas (direct electrode)"; RIGHT orange "High osmolality" → "Translocational (glucose, mannitol) → treat the cause; show corrected Na (1.6 and 2.4)"
- Side note card (purple): "Normal measured osmolality can hide hypotonicity when urea or alcohol is high (ineffective osmoles)"
- Bottom caveat ribbon (amber, Manrope): "Corrected sodium is a forecast; present tonicity uses the measured sodium"
- Attribution footer: "© renalcarematters.com" in the bottom-center corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No crossing connectors or spaghetti flow
✗ No drug doses
✗ No hard-edged threshold walls
✗ No more than 4 decision levels
✗ No tiny text below 16 px equivalent
✗ Do not recommend 3% saline in the hypertonic branch
✗ No urine thresholds on this figure
✗ Do not label the pseudo branch as true hyponatremia
✗ Do not use corrected sodium as present tonicity

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: KDIGO / ESE guideline flowchart aesthetic; algorithm-generator Mode C
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Three branches labeled hypotonic / pseudo / hypertonic — confirmed
□ "~275" written with tilde — confirmed
□ Both 1.6 and 2.4 shown — confirmed
□ Purple ineffective-osmole note present — confirmed
□ Bottom-center attribution on portrait — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 04 · dysnatremia-04-hyponatremia-pathway

**IMAGE NUMBER:** 04  
**SECTION PLACEMENT:** Clinician tab · "Diagnosing hypotonic hyponatremia" (#md-hypo-dx)  
**FILE NAME:** dysnatremia-04-hyponatremia-pathway.png  
**ARCHETYPE:** Clinical algorithm — algorithm-generator Mode C (renalcarematters.com house style), portrait  
**AUDIENCE:** Clinician (dual-labeled)  
**ASPECT RATIO:** 2:3  
**PIXEL DIMENSIONS:** 1024 × 1536  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: rounded decision/action nodes  
- 3D component graphics: small glyphs only (lab tube, urine cup)  
- algorithm/flowchart: top-to-bottom, ≤ 4 levels  
**PURPOSE:** Turn paired urine osmolality and sodium into a mechanism, with the caveats that break the cutoffs.  
**KEY CONCEPTS:** urine osmolality; urine sodium; effective arterial volume; SIAD; diuretics; adrenal; CKD caveat  
**ALT TEXT:** Algorithm from confirmed hypotonic hyponatremia: urine osmolality 100 or less suggests too much water or low solute; above 100, urine sodium 30 or less suggests low effective volume and above 30 suggests SIAD, diuretics, adrenal insufficiency or renal loss.  
**OG WIDTH:** 1024  
**OG HEIGHT:** 1536

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Portrait 1024×1536 clinical algorithm, top-to-bottom. Title (navy, Inter bold): "Hypotonic hyponatremia: what is the urine saying?".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Thresholds are approximate and drawn as soft gray-zone bands, never hard walls
- Every terminal node names a mechanism, not a drug dose
- Emergency banner above the tree: severe symptoms are treated first, before urine tests
- Urine osmolality ≤ 100 mOsm/kg = vasopressin suppressed; > 100 = vasopressin acting
- Urine sodium ≤ 30 mmol/L = low effective arterial volume; > 30 = consider SIAD, diuretics, adrenal insufficiency, severe hypothyroidism, renal salt loss
- SIAD is a diagnosis of exclusion

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Single trunk top-to-bottom; maximum 3 branches per level; no crossing lines
- Emergency banner (if any) sits ABOVE the tree as a separate red bar
- Caveat ribbon at the bottom

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Red banner on top: "Seizure, coma or breathing distress? Treat first — urine can wait"
- Start node: "Confirmed hypotonic hyponatremia — paired urine osmolality + urine sodium"
- Level 1 split on urine osmolality: LEFT "≤ 100 mOsm/kg" (soft gray band) → terminal "Water intake exceeds excretion: primary polydipsia, low solute (beer, tea-and-toast)"; RIGHT "> 100" → level 2
- Level 2 split on urine sodium (soft gray band at ~30): LEFT "≤ 30 mmol/L" → terminal "Low effective arterial volume: vomiting, diarrhea; heart failure, cirrhosis"; RIGHT "> 30 mmol/L" → terminal "Diuretic (thiazide) · adrenal insufficiency · severe hypothyroidism · renal salt loss · SIAD (exclude others first)"
- Bottom-right purple card: "Uncertain or mixed? Reassess after the first intervention — the urine response is diagnostic"
- Bottom caveat ribbon (amber, Manrope): "Diuretics, CKD and low salt intake blunt every cutoff"
- Attribution footer: "© renalcarematters.com" in the bottom-center corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No crossing connectors or spaghetti flow
✗ No drug doses
✗ No hard-edged threshold walls
✗ No more than 4 decision levels
✗ No tiny text below 16 px equivalent
✗ Do not put SIAD first in the > 30 list
✗ No numbers other than 100 and 30 on branches
✗ Do not place the emergency banner inside the tree
✗ Do not omit the uncertain/mixed card

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: KDIGO / ESE guideline flowchart aesthetic; algorithm-generator Mode C
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Red treat-first banner above the tree — confirmed
□ Cutoffs 100 and 30 drawn as gray bands — confirmed
□ SIAD listed last with "exclude others first" — confirmed
□ Caveat ribbon present — confirmed
□ Bottom-center attribution on portrait — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 05 · dysnatremia-05-correction-window

**IMAGE NUMBER:** 05  
**SECTION PLACEMENT:** Clinician tab · "Symptomatic hyponatremia: protocol, target and ceiling" (#md-hypo-emerg)  
**FILE NAME:** dysnatremia-05-correction-window.png  
**ARCHETYPE:** Data-concept chart (simple-figure Scaffold D) — conceptual, not patient data  
**AUDIENCE:** Clinician (patient-legible)  
**ASPECT RATIO:** 16:9  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: line chart with bands and annotations  
- 3D component graphics: small urine-bag and IV-bolus glyphs as event markers  
- algorithm/flowchart: none  
**PURPOSE:** Separate the early target (+4 to 6) from the ceiling (≤ 8 in ANY 24 h) and show how an unobserved water diuresis overshoots between samples.  
**KEY CONCEPTS:** target vs ceiling; rolling 24-hour window; aquaresis; sampling gaps  
**ALT TEXT:** Chart of sodium over 48 hours: two early boluses reach a +4 to 6 target band; later a water diuresis between blood draws pushes sodium past the 8 mmol/L ceiling of a rolling 24-hour window.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 concept chart. Title (navy, Inter bold): "Target first, ceiling always — any 24 hours counts".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- X axis 0–48 hours; Y axis is CHANGE from baseline (mmol/L), 0 to +12 — conceptual, no patient values
- Green target band +4 to +6 reached by ~2 hours after two bolus markers
- Red dashed ceiling at +8 drawn ONLY across a 0–24 h bracket (relative to the 0-hour value); a second, lighter bracket offset to 12–36 h labeled "Any 24 hours counts — the window slides"
- An orange "unsampled" segment between two sampling dots (hours 14–20) where a urine-output spike icon appears and the line rises from +7 to +10 — a +10 rise within the first 24 hours, so the +8 ceiling is exceeded
- After hour 20 the line is brought back down slightly (relowering) but a small red flag stays at hour 20: "Excursion stays on the record"

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Chart occupies left 72%; right 28% holds three stacked legend/explanation cards
- Sampling dots every 2–4 hours on the measured line; dashed orange for the unmeasured stretch

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Card 1 (green): "Early target: +4 to 6 mmol/L with symptom relief — not normalization"
- Card 2 (red): "Ceiling: ≤ 8 mmol/L in ANY 24 hours (site default, chronic or unknown onset)"
- Card 3 (amber): "Water diuresis between blood draws can overshoot — check sodium every 2–4 h and urine output hourly"
- Axis labels: "Hours" and "Change in sodium (mmol/L)"; event icons labeled "3% bolus" (×2) and "Urine output surges"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No calendar-day boxes (00:00–24:00) as the ceiling
✗ No absolute sodium values on the y-axis
✗ No drug doses or volumes
✗ Ceiling must not be drawn as a single horizontal line across the whole chart without the 24-h bracket
✗ No smooth extrapolated curve beyond the last dot
✗ No 3D chart effects
✗ Target band must not be drawn above the ceiling
✗ No patient names, dates or clock times on the axis

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: NEJM/JASN figure clarity; simple-figure Scaffold D
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Target band +4 to +6 — confirmed
□ Ceiling +8 tied to rolling 24-h brackets — confirmed
□ Overshoot occurs in the unsampled orange segment — confirmed
□ Two bolus markers early — confirmed
□ Y axis shows change, not absolute sodium — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 06 · dysnatremia-06-aquaresis-rescue

**IMAGE NUMBER:** 06  
**SECTION PLACEMENT:** Clinician tab · "Preventing and managing overcorrection" (#md-overcorrection)  
**FILE NAME:** dysnatremia-06-aquaresis-rescue.png  
**ARCHETYPE:** Multi-panel educational infographic (infographic-skill archetype 4)  
**AUDIENCE:** Clinician  
**ASPECT RATIO:** 16:9  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: trigger tiles + timeline  
- 3D component graphics: IV bag, urine collection bag, potassium vial, steroid tablet, meal tray glyphs  
- algorithm/flowchart: three-point timeline  
**PURPOSE:** Teach what switches off vasopressin (and unleashes aquaresis) and where proactive, reactive and rescue desmopressin strategies sit.  
**KEY CONCEPTS:** aquaresis triggers; potassium raises sodium; proactive/reactive/rescue DDAVP; D5W relowering; specialist protocol  
**ALT TEXT:** Five triggers that can start a water diuresis feed into a sodium timeline marking proactive, reactive and rescue desmopressin strategies.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 clinician infographic. Title (navy, Inter bold): "When the kidney suddenly lets water go".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Triggers: volume restored · glucocorticoid replaced · thiazide stopped · potassium replaced · nutrition/solute restored
- Potassium replacement raises plasma sodium (exchanges for sodium in cells)
- Desmopressin (DDAVP) re-establishes antidiuresis; relowering uses electrolyte-free water such as 5% dextrose (D5W) with DDAVP
- No doses — principles only; protocol is local and specialist-directed

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Left 38%: five trigger tiles stacked vertically, each with a 3D glyph, arrows converging on a kidney icon releasing dilute urine
- Right 62%: sodium timeline (change from baseline) with three marked strategy points

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Tiles: "Volume restored (IV fluid)"; "Glucocorticoid given (adrenal insufficiency)"; "Thiazide stopped"; "Potassium replaced (raises sodium too)"; "Feeding restored (more solute)"
- Kidney label: "Vasopressin switched off → large dilute urine (aquaresis)"
- Timeline point 1 (teal) at start: "PROACTIVE — DDAVP with hypertonic saline from the start (selected high-risk)"
- Point 2 (amber) mid-rise: "REACTIVE — urine surges or sodium rising fast, before the ceiling"
- Point 3 (red) after the ceiling line: "RESCUE — relower with D5W + DDAVP; specialist protocol"
- Footer bar (purple): "Pooled data: fewer overcorrections with proactive DDAVP; no proven survival benefit"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No doses, mL, mcg or rates
✗ Do not show DDAVP as emergency treatment for seizures
✗ Do not omit potassium as a trigger
✗ No patient faces
✗ Kidney icon hilum medial
✗ Do not show the rescue point before the ceiling
✗ No ICU monitors or alarm imagery
✗ Do not imply DDAVP works instantly during tolvaptan use

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: infographic-skill v5 archetype 4; NEJM review figure style
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Five triggers present including potassium — confirmed
□ Three strategy points in order proactive → reactive → rescue — confirmed
□ Rescue placed after the ceiling — confirmed
□ Footer evidence caveat present — confirmed
□ No doses anywhere — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 07 · dysnatremia-07-siad-ladder

**IMAGE NUMBER:** 07  
**SECTION PLACEMENT:** Clinician tab · "Treat the cause → SIAD stepwise" (#md-cause)  
**FILE NAME:** dysnatremia-07-siad-ladder.png  
**ARCHETYPE:** Stepwise ladder / wide algorithm (algorithm-generator Mode C, landscape)  
**AUDIENCE:** Clinician  
**ASPECT RATIO:** 16:9  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: staircase + gate  
- 3D component graphics: measuring bottle, urea sachet, tablet blister glyphs  
- algorithm/flowchart: ascending steps  
**PURPOSE:** Show the order of SIAD treatment and the urine electrolyte ratio as the gate that predicts restriction failure.  
**KEY CONCEPTS:** treat cause; count all fluids; urine (Na+K)/plasma Na ratio; urea vs tolvaptan; investigational SGLT2  
**ALT TEXT:** A four-step staircase for SIAD: treat the cause and nutrition, restrict all fluids, check the urine electrolyte ratio, then compare urea and tolvaptan, with empagliflozin marked investigational.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 stepwise treatment ladder. Title (navy, Inter bold): "SIAD: climb the ladder, read the urine".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Urine electrolyte ratio = (urine Na + urine K) ÷ plasma Na; ratio > 1 means no electrolyte-free water is being excreted → restriction alone struggles
- Fluid restriction about 1 L/day is trial-tested, not universal; count soup, coffee, fruit
- Loop diuretic + salt is NOT a routine escalation in SIAD
- Tolvaptan: specialist-directed, needs water access, avoided in liver disease, overcorrection risk; urea: solute, bitter taste
- Empagliflozin: investigational (small crossover trial)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Staircase rising left→right in 4 steps; a "gate" icon between steps 2 and 3
- Bottom strip: two-column comparison card under step 4

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Step 1 (teal): "Treat the cause · protein and salt intake"
- Step 2 (teal): "Restrict ALL fluids (water, sabaw, coffee, fruit)" with measuring-bottle glyph
- Gate (amber): "Urine (Na + K) ÷ plasma Na > 1 → restriction alone will struggle"
- Step 3 (navy): "Second line — specialist"
- Step 4 split card: left "Urea — adds solute; bitter; observational evidence"; right "Tolvaptan — blocks V2; water access; avoid in liver disease; watch overcorrection"
- Side badge (purple): "Investigational: empagliflozin"
- Red strike-through chip near step 2: "Not routine: furosemide + salt"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No doses (no g/kg, no mg)
✗ Do not show tolvaptan as emergency therapy
✗ Do not rank urea above tolvaptan or vice versa
✗ No more than 6 words per step title
✗ Do not omit the ratio gate
✗ Do not depict fluid restriction for hypovolemic patients
✗ No pill brand names
✗ Steps must ascend left → right, not descend

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: algorithm-generator Mode C; KDIGO-style ladder
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Ratio formula written exactly — confirmed
□ "> 1" gate between steps 2 and 3 — confirmed
□ Furosemide + salt marked not routine — confirmed
□ Empagliflozin labeled investigational — confirmed
□ No doses — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 08 · dysnatremia-08-hypernatremia-plan

**IMAGE NUMBER:** 08  
**SECTION PLACEMENT:** Clinician tab · "Hypernatremia: diagnose the loss, replace the water" (#md-hyper)  
**FILE NAME:** dysnatremia-08-hypernatremia-plan.png  
**ARCHETYPE:** Multi-panel infographic with tank analogy (dual-audience)  
**AUDIENCE:** Dual (clinician-led)  
**ASPECT RATIO:** 16:9  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: three panels + formula card  
- 3D component graphics: water tank with faucet and drains; small IV and cup glyphs  
- algorithm/flowchart: numbered 1-2-3 sequence  
**PURPOSE:** Make "deficit plus ongoing losses" and "perfusion first" intuitive, and show why the plan must be recalculated.  
**KEY CONCEPTS:** perfusion first; free-water deficit; ongoing renal and extrarenal losses; insensible loss; enteral water; recheck  
**ALT TEXT:** A water tank below its fill line with an open drain shows that replacing hypernatremia needs the missing water plus ongoing losses, after perfusion is restored, with sodium rechecked every few hours.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 dual-audience infographic. Title (navy, Inter bold): "High sodium: refill the tank — and close the drains".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Step order is fixed: 1 restore perfusion (isotonic fluid) → 2 replace deficit + ongoing losses → 3 recheck sodium every 2–4 h and recalculate
- Deficit formula: TBW × (current Na ÷ target Na − 1); TBW = weight × coefficient (0.5–0.6; lower in older adults)
- Ongoing losses: renal (dilute urine in AVP-D/AVP-R; osmotic diuresis from glucose can lose water even with concentrated urine), extrarenal (diarrhea, fever), insensible (skin, breath)
- Conventional fall about 0.5 mmol/L/h, 10–12/day — expert practice; adult evidence conflicting

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Center: semi-3D glass water tank labeled "Total body water" with a dashed "normal fill line" above the current level, a faucet on top, and three open drains
- Left column: numbered steps 1-2-3; right column: formula card and evidence badge

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Tank gap label: "Free-water deficit"
- Drains labeled: "Kidneys (dilute urine or sugar in urine)", "Gut (diarrhea)", "Skin and breath (fever, heat)"
- Faucet label: "Water by mouth or tube first; IV low-salt fluid if needed"
- Step 1 (red): "Shock? Restore circulation first"
- Step 2 (teal): "Replace deficit + what is still being lost"
- Step 3 (green): "Recheck sodium every 2–4 h — recalculate"
- Formula card: "Deficit ≈ TBW × (Na ÷ target − 1)" with a note "0.45% saline ≈ half free water"
- Evidence badge (amber): "Speed: about 0.5 mmol/L/h by convention — evidence conflicting"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No infusion rates or mL/h
✗ Do not show isotonic saline as free water
✗ No patient in distress
✗ Tank must be BELOW the fill line (deficit)
✗ Drains must be visibly open
✗ Do not show step 2 before step 1
✗ No pediatric or neonatal imagery
✗ Do not state faster correction is proven safe or unsafe

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: infographic-skill v5 archetype 4; simple-figure analogies
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Steps in order perfusion → replace → recheck — confirmed
□ Three drains labeled — confirmed
□ Formula exactly as written — confirmed
□ Evidence badge marks speed as conflicting — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 09 · dysnatremia-09-everyday-risks-ph

**IMAGE NUMBER:** 09  
**SECTION PLACEMENT:** Patient tab · "Everyday habits that affect sodium (Philippine setting)" (#home)  
**FILE NAME:** dysnatremia-09-everyday-risks-ph.png  
**ARCHETYPE:** Multi-panel patient infographic with photorealistic Filipino vignettes (infographic-skill archetype 4)  
**AUDIENCE:** Patients and families  
**ASPECT RATIO:** 16:9  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: six small Filipino everyday scenes  
- 2D infographic: card frames, tip lines, icons  
- 3D component graphics: measuring bottle glyph  
- algorithm/flowchart: none  
**PURPOSE:** Let Filipino readers recognize their own situations that tip sodium low or high, with one action per card.  
**KEY CONCEPTS:** fluid limits count soup; drinks replacing meals; thiazide checks; sick days; heat and elders; endurance drinking  
**ALT TEXT:** Six everyday Philippine scenes — a fluid-limit bottle with soup and coffee, crackers and coffee replacing a meal, a beer session with little food, a medicine check for water pills, an older adult offered water on a hot day, and oral rehydration during diarrhea.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 patient infographic in a 3×2 grid of photorealistic Filipino vignettes. Title (navy, Inter bold): "Everyday habits that can tip your sodium".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Messages must match the guide: count all fluids on a limit; do not replace meals with drinks; ask about sodium checks on water pills; use oral rehydration solution on sick days; give elders water regularly in heat; drink to thirst in long runs
- People: varied Filipino adults and seniors (different ages, builds, skin tones within Filipino diversity, clothing), calm expressions; at least 12 visible traits differ between people; no one ill or in distress

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- 3 columns × 2 rows of equal rounded cards; each card = photo vignette (top 70%) + one-line tip (bottom 30%)
- Left-column cards tagged teal "LOW sodium risk", right-column cards tagged orange "HIGH sodium risk" where applicable, center column mixed

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Card 1: kitchen table with a 1-liter measuring bottle, a bowl of sabaw, a cup of kape, a slice of watermelon — tip "On a fluid limit? Soup, coffee and fruit count"
- Card 2: crackers and coffee on a desk in place of a meal — tip "Don’t replace meals with drinks"
- Card 3: friends at an evening beer session with an empty pulutan plate — tip "Many beers, little food can lower sodium"
- Card 4: senior reviewing a blister pack with a pharmacist — tip "On a water pill? Ask about a sodium check"
- Card 5: daughter offering a lola a cup with a straw beside an electric fan on a hot afternoon — tip "Heat: offer water often to elders"
- Card 6: parent preparing oral rehydration solution for a family member with stomach flu — tip "Vomiting or diarrhea? Use ORS, not plain water alone"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ No readable brand names on bottles, beer or medicines
✗ No drunk or disorderly depiction
✗ No hospital beds or IV lines
✗ No dark night scenes — bright, airy interiors
✗ No repeated faces across cards
✗ No stereotyped or caricatured Filipino features
✗ Tips ≤ 9 words each
✗ No alcohol glamorization or close-up pouring shots

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Premium Philippine healthcare editorial photography; infographic-skill v5 archetype 4; hero-vignette human-variation rules
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Six cards, six distinct people/households — confirmed
□ Tips spelled exactly as written — confirmed
□ No brand names visible — confirmed
□ Bright lighting in all scenes — confirmed
□ "ORS" card shows a sachet being mixed, not IV — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---

## 10 · dysnatremia-10-collecting-duct-avp

**IMAGE NUMBER:** 10  
**SECTION PLACEMENT:** Clinician tab · "Physiology that decides every step" (#md-physiology)  
**FILE NAME:** dysnatremia-10-collecting-duct-avp.png  
**ARCHETYPE:** Biomedical mechanism figure (organ → magnified collecting-duct cell → drug sites)  
**AUDIENCE:** Clinician (dual-labeled)  
**ASPECT RATIO:** 16:9  
**PIXEL DIMENSIONS:** 1792 × 1024  
**VISUAL MIX:**  
- photorealistic models: none  
- 2D infographic: callouts and drug-site badges  
- 3D component graphics: kidney orientation inset, principal cell, receptor, aquaporin channels  
- algorithm/flowchart: signal arrows  
**PURPOSE:** Show where vasopressin, desmopressin, tolvaptan and urea act on water excretion.  
**KEY CONCEPTS:** AVP → V2 receptor → cAMP → aquaporin-2 insertion; DDAVP agonist; tolvaptan blocks V2; urea adds solute; solute sets urine volume  
**ALT TEXT:** Collecting-duct principal cell: vasopressin binds the V2 receptor on the blood side, aquaporin-2 channels move to the urine side and water returns to the blood; desmopressin activates, tolvaptan blocks, and urea carries water out in the urine.  
**OG WIDTH:** 1792  
**OG HEIGHT:** 1024

**COPY-READY IMAGE GENERATOR GPT PROMPT:**

```text
Landscape 1792×1024 biomedical mechanism figure. Title (navy, Inter bold): "How the kidney decides to keep or release water".

════════════════════════════════════
CONSTITUTION v1.0 — LAYER A: ANATOMICAL / CLINICAL TRUTH BLOCK (supreme override)
- Kidney orientation inset (if any): convex border LATERAL, hilum MEDIAL facing the spine; renal pelvis exits at the medial hilum ONLY
- Minor calyces cup the papillae and drain INWARD toward the central pelvis; medullary pyramids triangular with apex (papilla) pointing inward
- Cortex outer 1–1.5 cm pink-brown granular; corticomedullary junction clearly delineated
- Hilar order anterior→posterior: renal VEIN (blue, thin wall) → ARTERY (red, thick muscular media, circular lumen) → URETER (pale yellow, thin)
- Right kidney lower than left in any bilateral view; never mirror orientation
- Nephron/collecting duct shown as a standalone enlarged diagram; whole kidney only as a small orientation inset ≤ 12% of panel area, labeled "NOT TO SCALE"
- Principal cell polarity: BASOLATERAL (blood/interstitium) side carries the V2 receptor; APICAL (tubular lumen/urine) side receives aquaporin-2 (AQP2) channels; aquaporin-3/4 on the basolateral side let water exit to blood
- Signal: AVP binds V2R → Gs → adenylyl cyclase → cAMP → protein kinase A → AQP2 vesicles fuse with the apical membrane
- Water moves lumen → cell → blood only when AQP2 is inserted and the medullary interstitium is concentrated
- Drug sites: desmopressin (DDAVP) = V2 agonist (green check); tolvaptan = V2 antagonist (red block); urea = luminal solute carrying water out (teal)

════════════════════════════════════
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
- Far-left: small coronal kidney orientation inset (≤ 12% area, labeled "NOT TO SCALE") with a dashed connector from the medullary collecting duct to the magnified panel
- Center 60%: large dashed-border panel with one principal cell — lumen (urine) on the LEFT/top, blood/interstitium on the RIGHT/bottom (state sides with labels)
- Right column: three drug badges stacked; bottom strip: one-line solute equation

════════════════════════════════════
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
- Labels: "Arginine vasopressin (AVP, water-holding hormone)", "V2 receptor (V2R)", "cAMP signal", "Aquaporin-2 (AQP2) water channels", "Urine side (lumen)", "Blood side"
- Blue water-droplet arrows crossing the cell from urine side to blood side
- Badges: green "Desmopressin (DDAVP) — turns the signal ON"; red "Tolvaptan — blocks V2R → aquaresis"; teal "Urea — extra solute carries water out"
- Bottom strip (navy, Inter): "Urine volume ≈ solute excreted ÷ urine concentration"
- Attribution footer: "© renalcarematters.com" in the bottom-right corner — small (about 10–12 px at final size), navy #1F3864, Inter, ~65% opacity, clear of all anatomy, labels and cards.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
- Not applicable — no CT, ultrasound, MRI, fluoroscopy or nuclear images appear. ✗ Do not insert any radiology image.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No dark, navy, charcoal or black backgrounds or panels — light backgrounds only
✗ No cartoon, mascot or clip-art style; no flat vector icon-sheet look
✗ No garbled, misspelled or unreadable text; no lorem ipsum
✗ No prompt text, layer names or metadata visible in the image
✗ No missing attribution footer — "© renalcarematters.com" appears on every image
✗ No altered attribution text — not "Renal Care Matters", not www.renalcarematters.com, not any other domain
✗ No attribution footer overlapping anatomy, labels or callout boxes
✗ No attribution rendered large, centered, or in any color other than navy #1F3864
✗ No serif, condensed-display, handwritten or decorative fonts
✗ No invented numbers, drug doses or thresholds beyond those written in this prompt
✗ No anatomy visible through opaque skin; no kidney larger than the torso in any scene
✗ AQP2 must not be drawn on the basolateral membrane
✗ V2 receptor must not be drawn on the apical (urine) side
✗ Water arrows must not run blood → urine when AQP2 is inserted
✗ No glomerulus in the magnified panel (this is the collecting duct)
✗ Kidney inset must not show a lateral hilum or outward-draining calyces
✗ No drug doses
✗ Arteries in inset: thick muscular media, circular lumen; ureter thin-walled
✗ No nephron loop drawn inside the whole-kidney inset at organ scale

════════════════════════════════════
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
- References: Brenner & Rector's The Kidney; Netter's Atlas (inset); JASN mechanism figure style; biomedical-mechanism-figure template
- Illustrated semi-3D medical illustration with soft studio shading, publication-grade (Netter-like clarity, NEJM/JASN graphical-abstract polish) — NOT flat vector clip art, NOT cartoon. Light background only: white #ffffff or off-white #fafafa, cards in light teal tint #eef6f7 or soft gray #f3f4f6. Palette (accents and text only): NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Typography: Inter (titles, numbers) and Manrope (labels) — clean sans-serif only, never serif or decorative. Labels with thin leader lines and rounded callout cards; medical term paired with plain English in parentheses. Attribution footer "© renalcarematters.com" — bottom-right, small, navy #1F3864, ~65% opacity, exact lowercase string.

════════════════════════════════════
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Kidney orientation correct (convex lateral, hilum medial) — confirmed
□ Calyces drain inward toward medial pelvis — confirmed
□ Arteries have thick muscular media — confirmed
□ V2R basolateral, AQP2 apical — confirmed
□ Water flow urine → blood — confirmed
□ Three drug badges with correct colors and actions — confirmed
□ Inset ≤ 12% and labeled NOT TO SCALE — confirmed
□ Solute equation exact — confirmed
□ Background white/off-white/light tint only — confirmed
□ Only Inter/Manrope sans-serif text — confirmed
□ Every label spelled exactly as specified in Layer C — confirmed
□ No garbled labels — confirmed
□ No prompt text visible in generated image — confirmed
□ Medical term + plain-English pairing present on key labels — confirmed
□ Color codes repeated by icon or word (not color alone) — confirmed
□ Attribution footer present in bottom corner — confirmed
□ Attribution reads exactly "© renalcarematters.com" (lowercase, no www, no https://) — confirmed
□ Attribution footer legible, navy #1F3864, and not overlapping anatomy or labels — confirmed
```

**NEGATIVE INSTRUCTIONS:** see Layer E (universal + subject-specific). Never omit the attribution.  
**QUALITY CHECK:** run Layer G; regenerate if any attribution box or any number/label fails.

---
