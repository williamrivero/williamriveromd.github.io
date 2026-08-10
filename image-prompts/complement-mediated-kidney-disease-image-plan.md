# Image Plan — When Complement Injures the Kidney (C3G, aHUS/CM-TMA, IC-MPGN)

**Guide:** `guides/complement-mediated-kidney-disease.html`
**Route:** https://renalcarematters.com/guides/complement-mediated-kidney-disease.html
**Style system:** renalcarematters.com house style — light backgrounds only; sans-serif (Inter / Nunito Sans / IBM Plex Sans / Manrope) only, named in every prompt; palette navy `#0f1e2e`, clinical teal `#1a6b72`, renal green `#1f7a4d`, amber/gold `#b8860b`, clinical red `#b91c1c`, soft purple `#6c3d8e`; backgrounds white `#ffffff` / off-white `#fafafa` / soft gray `#f3f4f6` / light teal `#eef6f7`.
**Attribution:** every figure (except the wordless circular vignette hero) carries small semi-transparent navy `© renalcarematters.com` in the bottom-right corner (bottom-center for portrait). The vignette hero is wordless — no watermark.
**Paste target:** ChatGPT Image Generator GPT — https://chatgpt.com/g/g-pmuQfob8d-image-generator

> **Editorial guardrails baked into every prompt (blueprint §21):** calm medical-editorial tone; **no** combat/war imagery, **no** "attacking" antibodies, **no** exploding or bleeding kidneys, **no** genetic-code "matrix rain," **no** neon/cybernetic look, **no** pharmaceutical branding or drug logos, **no** frightening needle imagery. Every diagram is a **clearly labelled educational illustration** — never a synthetic photomicrograph presented as real tissue. All on-image words are short and mirror the guide's own figure captions.

> **Skill provenance:** hero = `williamriveromd-hero-vignette` (v3); OG card + treatment-safety shield = `williamriveromd-infographic-skill` (v5); two-compartments + complement pathway map + biopsy triptych + driver/amplifier/marker spectrum + drug-target overlay + genetics branching = `williamriveromd-simple-figure` (v1); TMA emergency algorithm + C3G diagnostic pathway = `williamriveromd-algorithm-generator-skill`.

## Asset map

| # | File | Placement in guide | Skill | Size | Status in HTML |
|---|---|---|---|---|---|
| 1 | `…-vignette-hero.{png,webp}` | Patient hero disc (`figure.hero-figure.mode-patient`) | hero-vignette | 2048×2048 | **referenced** |
| 2 | `…-og.png` | `og:image` / `twitter:image` | infographic | 1200×630 | **referenced** |
| 3 | `…-01-two-compartments.{png,webp}` | §"One System, Several Diseases" (patient) | simple-figure | 1792×1024 | **referenced** |
| 4 | `…-02-pathway-map.{png,webp}` | §"Complement 101" (patient) | simple-figure | 1792×1024 | optional add |
| 5 | `…-03-biopsy-triptych.{png,webp}` | §"Three Views of One Biopsy" (patient) | simple-figure | 1792×1024 | **referenced** |
| 6 | `…-04-spectrum.{png,webp}` | §"Driver or Marker?" (patient) | simple-figure | 2048×2048 | **referenced** |
| 7 | `…-05-tma-algorithm.{png,webp}` | §"TMA Emergency" (clinician) | algorithm-generator (AHA) | 1024×1536 | **referenced** |
| 8 | `…-06-c3g-pathway.{png,webp}` | §"Glomerular Pathway" (clinician) | algorithm-generator (house) | 1024×1536 | **referenced** |
| 9 | `…-07-drug-targets.{png,webp}` | §"Evidence" (clinician) | simple-figure | 1792×1024 | **referenced** |
| 10 | `…-08-genetics.{png,webp}` | §"Genetics" (patient) | simple-figure | 2048×2048 | **referenced** |
| 11 | `…-09-safety-shield.{png,webp}` | §"Infection Safety" (patient) | infographic | 1792×1024 | **referenced** |

> After generating, save each as `images/<name>.png` **plus a `.webp` twin**. Asset #4 (pathway map) is the one figure not yet inlined — add it to the "Complement 101" section as a `<figure>` (with `<figcaption><p class="fig-desc">…</p>` and a `<dl class="fig-abbrevs">` for MAC/C3), then re-run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, and `patch_image_lightbox.py`. All other assets are already referenced in the HTML.

---

## 1 — Circular vignette hero

FILE NAME: complement-mediated-kidney-disease-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C (calm 3D anatomy)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F — Anatomy
CAMERA: three-quarter view, gentle studio lighting
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: one calm complement cascade dividing toward two destinations — a kidney's glomerular filter on one side and a small blood vessel on the other — so the viewer grasps "one immune cascade, two very different kidney injuries" at a glance.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: F Anatomy. Camera: three-quarter view.
Subject: a single elegant complement cascade rendered as a slim vertical chain of calm glowing teal spheres descending from the upper-centre, then gently forking into TWO paths lower in the circle. The LEFT fork leads to a clean semi-photorealistic cutaway of a kidney's glomerular filter (a rounded glomerulus with a softly highlighted filtering membrane) where a few small warm-amber complement fragments settle along the wall. The RIGHT fork leads to a short cross-section of a small blood vessel whose inner lining is gently swollen, with two or three soft platelet-cluster microthrombi inside. Restrained renal reds and clinical teal on a soft, uncluttered off-white background, gentle studio lighting and soft shadow. The two destinations are clearly different in shape so the split reads instantly.
Visual hierarchy: the cascade + its two destinations occupy 60–70% of the circle; 2–3 faint connective strands and a subtle brake/regulator motif (a small calm ring around one cascade node) are supporting context 20–30%; reserve a clean 20–25% TITLE SAFE ZONE of empty soft off-white gradient in the upper-left (no anatomy, leader lines, labels, or callouts in that zone) so the HTML title can sit beside the disc. Soft falloff toward a slightly deeper neutral at the rim. Calm, restrained, textbook-cover elegance — not garish, no glow overload.
Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, dozens of icons, tiny unreadable labels, infographic clutter, cropped circle, cropped anatomy, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text/titles/captions/logos/watermarks, rectangular borders/frames/banners, dark/charcoal/black backgrounds, cartoon style, neon, cybernetic look, HDR, over-saturation, exploding or bleeding kidneys, "attacking" antibody imagery, distorted or implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant subject (cascade dividing to filter + vessel) at 60–70% of the circle, 2–4 supporting elements, 20–25% empty title-safe zone reserved upper-left. No people. Wordless — no text or watermark. The two destinations read as clearly different. Crops cleanly inside the circle with nothing lost at the edges.

---

## 2 — Open Graph / social share card

FILE NAME: complement-mediated-kidney-disease-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed (link-preview audience)
VISUAL GOAL: instantly communicate "one complement cascade, several different kidney diseases" with a clean editorial split visual and a readable title.

PROMPT:
Open Graph social share card, exactly 1200 × 630 px, calm premium medical-editorial style on a clean off-white (#fafafa) background. LEFT two-thirds: bold title in navy (#0f1e2e), clean sans-serif Inter, two lines — "When Complement Injures the Kidney" — with a smaller clinical-teal (#1a6b72) subtitle beneath in Inter reading "C3G · CM-TMA/aHUS · IC-MPGN", and a small navy tag line under that reading "One cascade. Different compartment. Different disease." Keep generous negative space and clear hierarchy. RIGHT one-third: a clean simplified illustration of a single complement cascade — a slim vertical chain of calm teal nodes — that forks into two small destinations: a rounded glomerular kidney-filter icon (upper) with a few amber deposit dots, and a small blood-vessel cross-section (lower) with two soft platelet microthrombi. Thin teal connector lines. No drug logos, no packaging. Light, airy, publication-grade.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. No pharmaceutical branding, no neon, no combat/"attack" imagery. Never omit the renalcarematters.com attribution. Do not change the 1200 × 630 dimensions.

QUALITY CHECK:
Exactly 1200 × 630. Title legible as a thumbnail. Light background, navy/teal typography. The fork-to-two-destinations visual is clean and clearly split. Attribution visible bottom-right.

---

## 3 — Two compartments (same cascade, different disease)

FILE NAME: complement-mediated-kidney-disease-01-two-compartments.png
IMAGE TYPE: Simple figure — Scaffold B (side-by-side comparison)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (also useful to clinicians)
VISUAL GOAL: show that one shared alternative pathway can injure two different kidney compartments — the glomerular filter versus the small-vessel endothelium.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style, clearly an educational illustration (not a real photomicrograph). White (#ffffff) background. Title centered at top in bold navy (#0f1e2e), clean sans-serif Inter: "Same cascade, different compartment". A slim central vertical band in clinical teal (#1a6b72) shows one shared "alternative pathway" cascade as a chain of small teal nodes, with a short caption chip below it in navy reading "Shared complement amplifier". From this central band, a soft arrow points LEFT and a soft arrow points RIGHT into two equal panels with rounded corners.
LEFT panel, header in renal-green-neutral navy reading "Filter-deposit disease — C3G": a clean semi-3D cutaway of a glomerular capillary wall / mesangium with small warm-amber complement (C3) fragments deposited along the membrane; three short navy labels: "Protein & blood in urine", "Biopsy diagnosis", "Slower course".
RIGHT panel, header in clinical red (#b91c1c) reading "Small-vessel disease — CM-TMA / aHUS": a clean semi-3D cross-section of a small blood vessel with a gently swollen endothelial lining and platelet-rich microthrombi inside, plus a few fragmented red cells; three short navy labels: "Anemia & low platelets", "Acute kidney injury", "Emergency".
Soft dashed vertical divider between panels. Ample negative space, mobile-readable labels ≥11pt, calm restrained clinical color.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter / Nunito Sans / IBM Plex Sans / Manrope. No exploding kidneys, no "attacking" antibodies, no neon, no drug branding. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Two clearly different compartments; shared cascade in the middle feeding both. Mobile-readable, calm, publication-grade. Light background. Attribution bottom-right.

---

## 4 — Complement pathway map  *(optional add — insert into "Complement 101")*

FILE NAME: complement-mediated-kidney-disease-02-pathway-map.png
IMAGE TYPE: Simple figure — Scaffold D (single mechanism / one-panel)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: show the three entry pathways converging on C3, the alternative-pathway amplification loop, the terminal C5/MAC step, and the regulator "brakes" — with a clean numbered legend.

PROMPT:
Medical pathophysiology infographic, AJKD/NEJM graphical-abstract style, clearly an educational illustration. White (#ffffff) background. Title at top in bold navy (#0f1e2e), clean sans-serif Inter: "The complement cascade, in one map"; subtitle in clinical teal (#1a6b72): "Three entry paths, one amplification hub". Three labeled entry strands on the left in rounded chips — "Classical", "Lectin", "Alternative" — each a thin arrow converging to a central prominent node labeled "C3". A curved self-returning arrow around the alternative strand and C3 is labeled "Amplification loop". From C3, a downstream arrow to a node labeled "C5", then to a final node labeled "MAC (C5b-9)". Small calm teal ring-shaped "brake" icons sit beside the pathway at two points, grouped in a soft-gray legend box labeled "Regulators (brakes): factor H, factor I, CD46". Use a numbered legend (1–5) in a soft-gray side panel matching each step. Thin navy/teal arrows, rounded nodes, generous whitespace, mobile-readable labels.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, HDR, excessive saturation. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter / Nunito Sans / IBM Plex Sans / Manrope. No genetic-code "matrix rain," no neon, no combat imagery, no drug branding. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Three entries → C3 → C5 → MAC reads clearly; amplification loop and regulator brakes are visible; numbered legend matches. Light background, mobile-readable, attribution bottom-right.

---

## 5 — Three views of one biopsy (LM / IF / EM triptych)

FILE NAME: complement-mediated-kidney-disease-03-biopsy-triptych.png
IMAGE TYPE: Simple figure — Scaffold C (horizontal 3-panel sequence)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: teach that a kidney biopsy is read three ways, each answering a different question — pattern (LM), what is deposited (IF), and where/what kind of deposits (EM).

PROMPT:
Clean clinical education infographic, white (#ffffff) background, clearly an educational illustration (stylized panels, NOT real photomicrographs presented as real tissue). Title at top center in bold navy (#0f1e2e), clean sans-serif Inter: "Three views of one biopsy". Three equal rounded cards arranged horizontally on a very soft gray panel (#f3f4f6), each with a colored top accent band, a small stylized illustrative panel, a bold navy header, and one short question line.
Card 1 — teal (#1a6b72) accent, header "Light microscopy (LM)": a simplified stylized glomerulus showing a proliferative injury pattern and some scarring; question line in navy: "What pattern & how much scarring?"
Card 2 — amber (#b8860b) accent, header "Immunofluorescence (IF)": a stylized glomerulus with a bright even glow along the capillary loops representing dominant C3 staining; question line: "What is deposited? (C3-dominant)".
Card 3 — soft purple (#6c3d8e) accent, header "Electron microscopy (EM)": a stylized magnified membrane cross-section showing dense, ribbon-like intramembranous deposits; question line: "Where & what kind? (DDD vs C3GN)".
Thin navy arrows between the cards. Bottom full-width soft-gray strip with a navy summary line: "C3G needs all three — a blood test cannot make this diagnosis." Mobile-readable ≥11pt.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR, excessive saturation, and — critically — any attempt to render a realistic photomicrograph that could be mistaken for a real slide. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter / Nunito Sans / IBM Plex Sans / Manrope. No neon, no drug branding. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Three clearly-labelled stylized panels (LM / IF / EM), each with its distinct question; summary line present. Reads as illustration, not real tissue. Light background, mobile-readable, attribution bottom-right.

---

## 6 — Driver, amplifier, or marker spectrum

FILE NAME: complement-mediated-kidney-disease-04-spectrum.png
IMAGE TYPE: Simple figure — conceptual stepped-zone spectrum (square)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
AUDIENCE: mixed
VISUAL GOAL: show complement's causal role as a spectrum — primary driver, amplifier, or bystander marker — with representative diseases and explicit uncertainty between zones.

PROMPT:
Conceptual medical education infographic, AJKD/NEJM graphical-abstract style, square 2048 × 2048, white (#ffffff) background. Title at top center in bold navy (#0f1e2e), clean sans-serif Inter: "Is complement the driver, an amplifier, or just a marker?". Three horizontal stepped zones stacked with soft gradient transitions (not hard lines) between them, to signal a spectrum with genuine uncertainty at the boundaries.
Zone 1 (top), teal (#1a6b72) band, header "Primary driver": short navy caption "Complement dysregulation is central — blockade can address the mechanism"; representative chips: "C3 glomerulopathy", "CM-TMA / aHUS".
Zone 2 (middle), amber (#b8860b) band, header "Amplifier": caption "Another disease starts the injury; complement worsens it — follow disease-specific evidence"; chips: "some lupus nephritis", "IgA nephropathy", "ANCA vasculitis", "APS", "transplant injury".
Zone 3 (bottom), soft gray band, header "Marker / bystander": caption "Complement is present but its importance is uncertain — not a treatment ticket"; chips: "many inflammatory kidney diseases".
Between zones, a small navy dashed motif with a tiny label "uncertain boundary". Rounded chips, ample whitespace, mobile-readable ≥11pt.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR, excessive saturation, hard traffic-light "good/bad" coding. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter / Nunito Sans / IBM Plex Sans / Manrope. No neon, no drug branding, no combat imagery. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Three zones read as a spectrum with soft transitions and an explicit "uncertain boundary"; representative diseases are legible; no false certainty. Light background, mobile-readable, attribution bottom-right.

---

## 7 — TMA emergency algorithm

FILE NAME: complement-mediated-kidney-disease-05-tma-algorithm.png
IMAGE TYPE: Clinical algorithm — AHA / emergency style (Style Mode A)
ASPECT RATIO: 2:3 (portrait)
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: an emergency thrombotic-microangiopathy pathway in which recognition and TTP-directed action come visually BEFORE any complement genetics.

PROMPT:
Create a polished medical guideline algorithm flowchart in the style of an American Heart Association provider algorithm, portrait 1024 × 1536. White background, clean sans-serif typography set in Inter (never a serif font), thin dark-gray arrows, pastel rounded boxes, and pink decision diamonds. Layout centered, spacious, strictly aligned, guideline-grade. Title at top center in bold navy: "Suspected TMA — emergency pathway".
Use these visual conventions:
- Peach/orange rounded box for initial assessment
- Pink diamond boxes for decision questions
- Blue rounded boxes for active treatment steps
- Green rounded boxes for supportive/monitoring actions
- Gray capsule boxes for transitional steps
- Red bold labels beside arrows for emergency branch conditions
- A dashed horizontal divider separating emergency action (top) from longitudinal work-up (bottom)
Content to render, top to bottom:
1. Peach box: "Recognize TMA: thrombocytopenia and/or microangiopathic hemolytic anemia (MAHA) + organ injury. Do not require the full triad."
2. Gray capsule: "Stabilize · draw pre-treatment complement/genetic samples when feasible"
3. Blue box: "ADAMTS13 BEFORE plasma · treat suspected TTP immediately"
4. Pink diamond: "High TTP probability?" → red branch label "Yes" to a blue box "Immediate TTP-directed therapy — do NOT wait"; "No / not severely deficient" continues down.
5. Green box: "Test Shiga toxin (STEC) when appropriate"
6. Peach box: "Evaluate context: pregnancy/HELLP, severe hypertension, drugs, infection, autoimmune/APS, cancer/HSCT, transplant/CNI, metabolic"
7. Pink diamond: "CM-TMA likely with active organ injury?" → green/blue box "Consider urgent C5 blockade under specialist care — without waiting for genetics"
8. DASHED DIVIDER labeled "Later, for planning — not the emergency decision"
9. Gray box below divider: "Genetics / anti-factor H + longitudinal phenotype refine duration, relapse, family & transplant planning"
Design requirements: title at top, no photos, no 3D, no dark background, short readable text inside boxes, professional clinical education style. Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No dark background, no photorealistic people, no cartoon styling, no clutter, no spaghetti arrows, no tiny unreadable labels, no serif or decorative fonts, no fabricated numeric thresholds. Never omit the © renalcarematters.com footer.

QUALITY CHECK:
Emergency actions (recognize → ADAMTS13/TTP → context → consider C5) sit ABOVE the dashed divider; genetics sits BELOW it, clearly labelled as later planning. Portrait, aligned, mobile-readable. Footer bottom-right.

---

## 8 — C3G / IC-MPGN diagnostic pathway

FILE NAME: complement-mediated-kidney-disease-06-c3g-pathway.png
IMAGE TYPE: Clinical algorithm — renalcarematters.com house style (Style Mode C)
ASPECT RATIO: 2:3 (portrait)
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: a phenotype-first glomerular pathway — glomerular findings → LM/IF/EM → classify deposits → exclude secondary causes → characterize complement.

PROMPT:
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style, portrait 1024 × 1536. White or very light off-white background, restrained navy (#0f1e2e) and clinical teal (#1a6b72) typography set in Inter (never a serif font), thin teal connector arrows, generous margins, centered symmetric layout. Title at top center in bold navy: "C3G / IC-MPGN — a phenotype-first pathway".
Color conventions: navy for title/structure; teal (#1a6b72) for decision/assessment nodes; green (#1f7a4d) for the final characterization endpoint; amber (#b8860b) for the caution node; soft gray for side notes.
Content to render, top to bottom:
1. Teal node: "Confirm glomerular syndrome + urgency"
2. Teal node: "Kidney biopsy: LM + IF + EM"
3. Teal decision node fanning into four short rounded branches: "C3-dominant → C3-dominant GN differential" · "Ig + complement → IC-MPGN differential" · "Monoclonal pattern → MGRS work-up" · "TMA lesions → TMA pathway"
4. Amber caution node spanning the width: "Exclude mimics: infection-related GN (can be C3-dominant), endocarditis, autoimmune, cryoglobulins, MASKED monoclonal deposits — primary IC-MPGN is a diagnosis of exclusion"
5. Green endpoint node: "Characterize complement: C3/C4, functional pathways, activation products, nephritic factors/autoantibodies, CNV-aware genetics"
Side note in soft gray: "C3 dominance = C3 ≥ 2 orders of magnitude over any other reactant on IF — a pathology threshold, not a blood ratio."
Design requirements: clear title, top-to-bottom logic, rounded rectangles for actions, diamonds for the classification decision, consistent spacing, no dark background, no clutter, no photorealistic people. Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling.

NEGATIVE INSTRUCTIONS:
No dark background, no photorealistic people, no cartoon styling, no clutter, no spaghetti arrows, no tiny unreadable labels, no serif or decorative fonts. Never omit the © renalcarematters.com footer.

QUALITY CHECK:
Phenotype-first flow reads cleanly: syndrome → biopsy → 4-way classify → exclude mimics (amber) → characterize complement (green). Side note on C3 dominance present. Portrait, aligned, mobile-readable. Footer bottom-right.

---

## 9 — Drug-target overlay (where the drugs act)

FILE NAME: complement-mediated-kidney-disease-07-drug-targets.png
IMAGE TYPE: Simple figure — Scaffold D (single mechanism / one-panel)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: annotate the cascade with three intervention points (factor B, C3/C3b, C5) and the host-defense functions each affects — explicitly WITHOUT ranking any drug.

PROMPT:
Medical pathophysiology infographic, AJKD/NEJM graphical-abstract style, clearly an educational illustration. White (#ffffff) background. Title at top in bold navy (#0f1e2e), clean sans-serif Inter: "Where the drugs act on complement"; subtitle in clinical teal (#1a6b72): "Different points, different biology — this figure ranks no drug". A clean horizontal complement cascade runs left to right as rounded nodes: entry paths → a prominent "C3 / C3b" node → "C5" node → "MAC (C5b-9)" node, with a curved "alternative-pathway amplification loop" around the early segment. Three neutral teal target markers (simple ring/bracket icons, all the same visual weight) sit at: "Factor B — alternative-pathway amplification", "C3 / C3b — proximal convergence", and "C5 — terminal C5a & MAC". Below, a soft-gray strip with three short neutral navy notes: "Proximal blockade lowers C3 activation & deposition", "Terminal (C5) blockade spares upstream C3", "All raise encapsulated-bacterial infection risk". Keep all three targets visually equal — no size, glow, or color hierarchy implying superiority. Ample whitespace, mobile-readable ≥11pt.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR, excessive saturation, and any visual ranking (checkmarks, medals, size/glow differences) among the three targets. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter / Nunito Sans / IBM Plex Sans / Manrope. No drug logos, no packaging, no neon, no combat imagery. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Three equal-weight targets on a clean cascade; neutral notes; explicit "ranks no drug" framing; infection-risk note present. Light background, mobile-readable, attribution bottom-right.

---

## 10 — Genetics: susceptibility, not destiny

FILE NAME: complement-mediated-kidney-disease-08-genetics.png
IMAGE TYPE: Simple figure — branching outcome diagram (square)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 2048 × 2048
AUDIENCE: patients (also useful to clinicians)
VISUAL GOAL: show that a variant plus a trigger plus each person's regulatory/tissue context leads to a branch of outcomes — some people affected, some not — i.e. incomplete penetrance.

PROMPT:
Conceptual medical education infographic, square 2048 × 2048, white (#ffffff) background, clearly an educational illustration. Title at top center in bold navy (#0f1e2e), clean sans-serif Inter: "Genetics is susceptibility — not destiny". A calm left-to-right branching diagram (a clean probability-tree, NOT a DNA-helix or code-rain motif). On the left, three soft rounded input chips stacked and joined by thin teal arrows into a central node: "Susceptibility variant", "Trigger (infection, pregnancy, BP…)", "Each person's regulator & tissue context". The central navy node reads "Combined risk". From it, the path FORKS into multiple thin teal branches ending in small outcome chips of visibly different sizes to convey probability: two larger green chips "No disease", one amber chip "Disease develops", one small gray chip "Uncertain". A short navy caption strip along the bottom: "Same variant, different outcomes — penetrance is incomplete. A VUS is not actionable on its own; a negative panel does not rule disease out." Rounded chips, generous whitespace, mobile-readable ≥11pt. Do NOT use red/green traffic-light "good gene / bad gene" coding.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR, excessive saturation, DNA-helix cliché, genetic-code "matrix rain," and any "good gene / bad gene" traffic-light coding. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter / Nunito Sans / IBM Plex Sans / Manrope. No neon, no drug branding. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
A clean probability tree (inputs → combined risk → branched outcomes of different sizes) conveying incomplete penetrance; bottom caption on VUS and negative panels present; no DNA-helix or code-rain. Light background, mobile-readable, attribution bottom-right.

---

## 11 — Treatment safety shield (infection prevention)

FILE NAME: complement-mediated-kidney-disease-09-safety-shield.png
IMAGE TYPE: Multi-panel educational infographic (infographic skill, Archetype 4)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (also useful to clinicians)
VISUAL GOAL: show that complement blockade is paired with a five-part safety system — and that the shield lowers risk but does not remove it.

PROMPT:
Patient education infographic poster, landscape 16:9, modern nephrology clinic aesthetic, white (#ffffff) background. Top hero header in bold navy (#0f1e2e), clean sans-serif Inter: "Complement blockade comes with a safety shield". Centered, a calm translucent teal (#1a6b72) shield outline (simple, elegant — not a combat/heraldic emblem) around a small neutral patient icon. Arranged evenly around the shield, five equal rounded cards, each with a simple flat line icon and a short navy label:
1. "Vaccinate — meningococcal ACWY & B, pneumococcal, Hib"
2. "Carry an emergency card"
3. "Treat fever urgently — don't wait for the next infusion"
4. "Direct care-team contact"
5. "Ongoing monitoring"
Below, a full-width amber (#b8860b) caution strip with navy text: "Vaccination lowers the risk — it does not remove it. Fever or meningitis symptoms are an emergency." Keep icons simple and equal; generous whitespace; mobile-readable ≥11pt. Restrained, reassuring tone.
Bottom-right: "© renalcarematters.com" in small semi-transparent navy Inter text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, HDR, excessive saturation, frightening needle close-ups, combat/heraldic weaponry, and any implication that vaccination removes all risk. NEVER dark/navy/charcoal/black backgrounds — light only. Use ONLY Inter / Nunito Sans / IBM Plex Sans / Manrope. No drug branding, no neon. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Shield + five equal safety cards + amber "lowers but does not remove risk" strip. Calm, reassuring, not alarmist, no scary needles. Light background, mobile-readable, attribution bottom-right.

---

## Production checklist

- [ ] Generate each prompt in the ChatGPT Image Generator GPT at the stated pixel dimensions.
- [ ] Export **PNG**; also make a **WebP** twin for each (the guide's `<picture>` blocks load WebP first, PNG fallback).
- [ ] Save to `images/complement-mediated-kidney-disease-<descriptor>.{png,webp}` using the exact FILE NAME stems above.
- [ ] Verify each figure's on-image text matches the guide's `<figcaption>` wording; keep labels short.
- [ ] Confirm light background + approved sans-serif + `© renalcarematters.com` on every figure (hero stays wordless).
- [ ] For asset #4 (pathway map), add the inline `<figure>` to "Complement 101," then re-run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, `patch_image_lightbox.py`.
- [ ] Optionally hand this pack to `williamriveromd-local-image-generator` (Stage 2) to build the local folder + manifest and to append the `og:image` meta once the OG card is confirmed.
