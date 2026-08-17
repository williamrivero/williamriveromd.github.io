# Image Plan — Complement-Targeted Therapy in Kidney Disease

**Guide:** `guides/complement-targeted-therapy-kidney-disease.html`
**Route:** https://renalcarematters.com/guides/complement-targeted-therapy-kidney-disease.html
**Style system:** renalcarematters.com house style — light backgrounds only; sans-serif (Inter / Nunito Sans / IBM Plex Sans / Manrope) only; palette navy `#0f1e2e`, clinical teal `#1a6b72`, renal green `#1f7a4d`, amber/gold `#b8860b`, clinical red `#b91c1c`, backgrounds white `#ffffff` / off-white `#fafafa` / soft gray `#f3f4f6` / light teal `#eef6f7`.
**Attribution:** every figure (except the wordless circular vignette hero) carries small semi-transparent navy `© renalcarematters.com` in the bottom-right corner (bottom-center for portrait). The vignette hero is wordless — no watermark.
**Paste target:** ChatGPT Image Generator GPT — https://chatgpt.com/g/g-pmuQfob8d-image-generator

> **Skill provenance:** hero = `williamriveromd-hero-vignette` (v3); OG + spectrum + TMA algorithm + biopsy triptych + benefit/risk + before-first-dose + response hierarchy = `williamriveromd-infographic-skill` (v5); cascade + kidney-vulnerability = `williamriveromd-biomedical-mechanism-figure`.

## Asset map

| # | File | Placement in guide | Skill | Size | Status in HTML |
|---|---|---|---|---|---|
| 1 | `…-vignette-hero.{png,webp}` | Patient hero disc (`figure.hero-figure.mode-patient`) | hero-vignette | 2048×2048 | **referenced** |
| 2 | `…-og.png` | `og:image` / `twitter:image` (1200×630) | infographic | 1200×630 | **referenced** |
| 3 | `…-01-kidney-vulnerability.{png,webp}` | §"Why kidneys are vulnerable" (patient) | mechanism | 1792×1024 | **referenced** |
| 4 | `…-02-cascade.{png,webp}` | §"The complement cascade" (clinician) | mechanism | 1792×1024 | **referenced** |
| 5 | `…-03-driver-spectrum.{png,webp}` | §"Driver, amplifier, clue or bystander" | infographic | 1792×1024 | optional add |
| 6 | `…-04-tma-pathway.{png,webp}` | §"Suspected TMA" pathway | infographic (algorithm) | 1024×1536 | optional add |
| 7 | `…-05-biopsy-triptych.{png,webp}` | §"Biopsy pathway: C3G / IC-MPGN" | infographic (ref card) | 1792×1024 | optional add |
| 8 | `…-06-blockade-benefit-risk.{png,webp}` | §"Choosing where to block" | infographic | 1792×1024 | optional add |
| 9 | `…-07-before-first-dose.{png,webp}` | §"Infection prevention" / patient "Infection Safety" | infographic (multi-panel) | 1792×1024 | optional add |
| 10 | `…-08-response-hierarchy.{png,webp}` | §"What counts as response?" | infographic | 1792×1024 | optional add |

> After generating, save each as `images/<name>.png` **plus a `.webp` twin**. Files 5–10 are the blueprint's full visual program; embed them in their sections as inline `<figure>` blocks (each needs a `<figcaption><p class="fig-desc">…</p>` and, where an acronym appears in the image, a `<dl class="fig-abbrevs">`). Then re-run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, and `patch_image_lightbox.py`.

---

## 1 — Circular vignette hero

FILE NAME: complement-targeted-therapy-kidney-disease-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C (calm 3D anatomy)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: F — Anatomy
CAMERA: three-quarter view, gentle studio lighting
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: one kidney beside a simplified complement cascade converging on two glowing nodes, with a small protective shield — "a defense system that can injure the kidney."

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: F Anatomy. Camera: three-quarter view.
Subject: a single anatomically accurate human kidney rendered in restrained renal reds and soft clinical teal, floating on a soft, uncluttered light off-white background, positioned on the lower-left. To its right, a clean simplified branching schematic of the complement cascade — three thin entry strands merging into one prominent central sphere labelled only by shape (a larger node) and then a second node below it — suggesting convergence at C3 and C5, rendered as calm glowing spheres with gentle depth of field. A small, elegant translucent teal shield icon sits low and near the kidney to hint at immune defence, with one subtle amber caution dot. Gentle studio lighting, soft shadow.
Visual hierarchy: kidney + cascade occupy 60–70% of the circle; the shield and 2–3 connective strands are supporting context 20–30%; reserve a clean 20–25% TITLE SAFE ZONE of empty soft off-white gradient in the upper-left (no anatomy, leader lines, labels, or callouts in that zone) so the HTML title can sit beside the disc. Soft falloff toward a slightly deeper neutral at the rim. Restrained clinical colour (renal reds, teal accents, one amber dot), not garish.
Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark — clean render only. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, dozens of icons, tiny unreadable labels, infographic clutter, cropped circle, cropped anatomy, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text/titles/captions/logos/watermarks, rectangular borders/frames/banners, dark/charcoal/black backgrounds, cartoon style, neon, HDR, over-saturation, distorted or implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never cropped. ONE dominant subject (kidney + cascade) at 60–70% of the circle, 2–4 supporting elements, 20–25% empty title-safe zone reserved upper-left. No people. Wordless — no text or watermark. Crops cleanly inside the circle with nothing lost at the edges.

---

## 2 — Open Graph / social share card

FILE NAME: complement-targeted-therapy-kidney-disease-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (fixed — never change)
AUDIENCE: mixed (clinicians + patients)
VISUAL GOAL: publication-grade share card announcing the guide, with a restrained cascade-and-kidney motif and an infection-risk caution dot.

PROMPT:
Publication-grade social share card for a clinician nephrology guide, exactly 1200 × 630 pixels, off-white #fafafa background, clean sans-serif typography in Inter. LEFT 56% text-safe block: a small clinical-teal #1a6b72 eyebrow reading "PRECISION NEPHROLOGY · CLINICIANS + PATIENTS"; a large bold navy #0f1e2e headline "Complement-Targeted Therapy in Kidney Disease"; a smaller navy subhead "From cascade to clinical decision." RIGHT 44%: a restrained biomedical illustration of a single anatomically accurate kidney beside a simplified branching complement cascade that converges at two labelled nodes "C3" and "C5", with four small tidy blockade markers labelled "Factor B", "C3", "C5aR", and "C5". One amber #b8860b caution dot sits near a small teal shield icon to signal infection risk. Calm AJKD/NEJM editorial aesthetic, generous whitespace, mobile-legible labels, light background only. Small semi-transparent navy attribution "renalcarematters.com" in the bottom-right corner.
No pills, no product packaging, no manufacturer logos, no molecular clutter.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY Inter — no serif fonts, no decorative typefaces. Never omit the renalcarematters.com attribution. Do not change the 1200×630 dimensions.

QUALITY CHECK:
Exactly 1200×630. Off-white background, navy/teal/amber accents. Headline and four blockade labels mobile-readable. Attribution present bottom-right. Pair with `og:image:width="1200"` and `og:image:height="630"`.

---

## 3 — Kidney vulnerability (mechanism, organ → glomerulus → tubulointerstitium)

FILE NAME: complement-targeted-therapy-kidney-disease-01-kidney-vulnerability.png
IMAGE TYPE: Biomedical mechanism figure (review-article schematic)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed
VISUAL GOAL: show why the kidney is exposed to complement — organ panel, magnified glomerulus/endothelium inset, and an injury→persistence summary.

PROMPT:
Create a publication-grade biomedical mechanism schematic, landscape 16:9, white background, flat vector illustration with soft semi-3D shading, clean sans-serif labels in Inter, thin dashed connector boxes, muted clinical palette (light gray-blue anatomy, soft yellow highlight, red for injury, blue for protective/therapeutic).
LEFT organ-level panel: a simplified human kidney cross-section labelled "Kidney — continuous plasma exposure", showing cortex, a few glomeruli, and small vessels; a thin dashed connector box points to the magnified panel.
CENTER/RIGHT magnified panel (dashed border): a glomerular capillary loop and its endothelium, with the glycocalyx and surface complement regulators drawn as a thin protective layer. Highlight in soft yellow the amplification surface where immune deposits or faulty regulation let complement switch on. Concise callouts: "↑ Alternative-pathway amplification", "Endothelial injury → thrombotic microangiopathy (TMA)", "Injury spreads to tubules + interstitium". Show a small red arrow from the glomerulus into the tubulointerstitium.
BOTTOM summary flow (arrow left → right): left pale-pink pathology box "Exposure + filtration + faulty local regulation"; center box "Complement amplification on the kidney surface"; right pale-blue box "Even after inflammation settles: nephron loss + fibrosis may continue". 
White background, generous whitespace, no photorealism, no dark theme, no decorative effects. Small semi-transparent navy "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, photorealism, shadows-heavy rendering, dark backgrounds, neon, over-saturation. Inter only, no serif fonts. Do not invent numeric thresholds. Never omit the attribution.

QUALITY CHECK:
16:9, white background, muted clinical palette, dashed magnified inset, injury→persistence bottom flow, all labels legible at slide size, attribution bottom-right.

---

## 4 — The complement cascade, made clinically useful (mechanism)

FILE NAME: complement-targeted-therapy-kidney-disease-02-cascade.png
IMAGE TYPE: Biomedical mechanism figure (review-article schematic)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (also patient-legible)
VISUAL GOAL: three pathways → C3 → amplification → C5 → C5a + C5b-9, with four blockade bars and one clinical consequence each.

PROMPT:
Create a publication-grade biomedical schematic, landscape 16:9, white background, flat vector with soft semi-3D shading, clean sans-serif labels in Inter, muted clinical palette, thin connector lines.
Three activation pathways enter from the LEFT — "Classical", "Lectin", "Alternative" — and converge on a large clean central node labelled "C3". Draw the alternative pathway as an amplification loop through a smaller node labelled "Factor B" feeding back into C3. Continue rightward to a node labelled "C5", which then splits into two branches: upper "C5a — inflammatory signaling (neutrophil recruitment)" and lower "C5b-9 — membrane attack complex (MAC)".
Place FOUR restrained colored blockade bars across the pathway at: "Factor B", "C3 / C3b", "C5a receptor (C5aR)", and "C5". Under each bar, one short clinical-consequence line: Factor B → "Oral proximal alternative-pathway strategy (IgAN, C3G)"; C3/C3b → "Broad proximal control; encapsulated-bacteria precautions"; C5aR → "Neutrophil signaling blocked; other functions remain"; C5 → "Established in complement-mediated HUS; meningococcal risk remains".
Use navy, teal, renal green, gray, and one amber safety accent. Accurate hierarchy, generous whitespace. No decorative DNA, no glowing effects, no dark background, no photorealism. Small semi-transparent navy "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, decorative DNA, glowing/neon effects, dark backgrounds, over-saturation. Inter only, no serif fonts. No manufacturer/brand names. Never omit the attribution.

QUALITY CHECK:
16:9, white background. Left-to-right hierarchy correct: three pathways → C3 (with Factor B loop) → C5 → C5a + C5b-9. Exactly four blockade bars, each with one consequence line. Labels legible; attribution bottom-right.

---

## 5 — Driver vs amplifier spectrum (infographic)

FILE NAME: complement-targeted-therapy-kidney-disease-03-driver-spectrum.png
IMAGE TYPE: Multi-panel educational infographic (evidence spectrum)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: four zones from certainty to speculation, disease cards placed with honest uncertainty gradients.

PROMPT:
Clinical evidence-spectrum infographic, landscape 16:9, off-white #fafafa background, clean sans-serif typography in Inter, navy #0f1e2e headings, teal #1a6b72 rules. Four vertical zones left → right with a subtle certainty gradient (solid borders on the left, dashed borders on the right): "PRIMARY DRIVER", "MAJOR AMPLIFIER", "TISSUE CLUE", "INVESTIGATIONAL ASSOCIATION". Place rounded disease cards: in PRIMARY DRIVER — "Complement-mediated HUS / aHUS" and "C3 glomerulopathy (C3G)"; in MAJOR AMPLIFIER — "Primary IC-MPGN", "Primary IgA nephropathy at risk", and "ANCA-associated vasculitis (see avacopan alert)"; in TISSUE CLUE (dashed) — "Lupus nephritis", "Membranous nephropathy", "Infection-related GN"; in INVESTIGATIONAL (dashed) — "FSGS", "Diabetic kidney disease", "AKI", "Transplant-associated TMA". Footer strip in teal: "Complement present ≠ complement-targeted therapy indicated." No arrows implying a fixed classification; show soft uncertainty gradients between zones. Light background only. Small semi-transparent navy "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, dark backgrounds, neon, over-saturation, generic stock look. Inter only, no serif fonts. No brand/manufacturer names. Never omit the attribution.

QUALITY CHECK:
16:9, off-white background, four labelled zones with left-solid → right-dashed gradient, disease cards placed as specified, footer disclaimer present, attribution bottom-right, mobile-readable.

---

## 6 — Suspected TMA pathway (clinical algorithm, portrait)

FILE NAME: complement-targeted-therapy-kidney-disease-04-tma-pathway.png
IMAGE TYPE: Clinical algorithm / flowchart (portrait)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: urgent branching work-up with NO numeric score and NO automatic treatment recommendation.

PROMPT:
Clinical nephrology algorithm infographic, portrait 2:3, premium KDIGO/guideline flowchart aesthetic, off-white background, clean sans-serif typography in Inter, navy structure lines. Top entry node (teal): "AKI or organ injury + falling platelets and/or microangiopathic hemolysis". Branch downward with rounded nodes to urgent checks: "TTP? — send ADAMTS13 (do not delay emergency treatment)", "STEC / Shiga-toxin", "Pregnancy / HELLP", "DIC / sepsis", "Severe (malignant) hypertension", "Transplant / drugs", "Complement-mediated HUS". Amber caution boxes carry two key messages prominently: "Do NOT wait for genetics to stabilize time-critical disease" and "Complement studies & genetics are risk tools, not prerequisites". End node (teal, not red): "Urgent expert review + start infection-risk mitigation". Use teal arrows, navy text, amber for urgent cautions, green for the optimal-pathway node. Maximum 3–5 branching levels, preserve whitespace, avoid spaghetti flowchart. Absolutely NO numeric probability score and NO automatic treatment/dose recommendation. Light background only. Small semi-transparent navy "renalcarematters.com" bottom-center.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, spaghetti flowchart, clutter, tiny unreadable labels, AI gibberish, dark backgrounds, neon, over-saturation. Inter only, no serif fonts. Do NOT render any numeric aHUS score or treatment threshold. No brand names. Never omit the attribution.

QUALITY CHECK:
Portrait 1024×1536, off-white background, clean branching pathway, both amber "do not wait for genetics" messages visible, no numeric score, no treatment recommendation, endpoint is "urgent expert review", attribution bottom-center.

---

## 7 — Three views of a complement-pattern biopsy (reference triptych)

FILE NAME: complement-targeted-therapy-kidney-disease-05-biopsy-triptych.png
IMAGE TYPE: Clinician reference card (triptych)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians, renal pathologists
VISUAL GOAL: LM / IF / EM panels teaching that C3 dominance is a clue, not the whole diagnosis.

PROMPT:
Clean nephropathology triptych infographic, landscape 16:9, white background, clean sans-serif labels in Inter, restrained scientific illustration (NOT photorealistic patient tissue). Three equal panels with navy headers: "Light Microscopy (LM)", "Immunofluorescence (IF)", "Electron Microscopy (EM)". LM panel: a stylised glomerulus with an MPGN-like membranoproliferative pattern, with small callouts "Activity" and "Chronicity". IF panel: a glomerulus glowing bright teal-green for C3 with weaker other reactants faintly shown, and a caption "C3 dominance is a clue, not the whole diagnosis". EM panel: schematic capillary wall showing "dense intramembranous deposits (DDD)" vs "other electron-dense deposits (C3GN)". A small side box in amber: "Exclude infection, autoimmune disease, cryoglobulins, and monoclonal proteins (consider paraffin IF for masked deposits)". Muted clinical palette, generous whitespace, light background only. Small semi-transparent navy "© renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic patient tissue, cartoon style, clutter, tiny unreadable labels, AI gibberish, dark backgrounds, neon, over-saturation. Inter only, no serif fonts. Do not label the biopsy "C3G" as an automatic conclusion. Never omit the attribution.

QUALITY CHECK:
16:9, white background, three clearly labelled panels (LM/IF/EM), IF caption "a clue, not the whole diagnosis" present, exclusion side-box present, attribution bottom-right, legible at slide size.

---

## 8 — Where blockade trades disease control for host defense (benefit–risk)

FILE NAME: complement-targeted-therapy-kidney-disease-06-blockade-benefit-risk.png
IMAGE TYPE: Multi-panel educational infographic (benefit–risk)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians + patients
VISUAL GOAL: same cascade in the center, "disease control" above and "host-defense cost" below, four aligned blockade cards, no drug ranking.

PROMPT:
Balanced benefit–risk infographic, landscape 16:9, off-white background, clean sans-serif typography in Inter, navy/teal/green/amber/red accents. CENTER: a simplified complement cascade (Factor B → C3 → C5 → C5a + C5b-9). ABOVE it a green-tinted band "Disease control" listing "↓ endothelial injury", "↓ glomerular inflammation", "↓ proteinuria", "↓ TMA activity". BELOW it an amber/red-tinted band "Host-defense cost" listing "↑ meningococcal risk", "↑ encapsulated-bacteria risk". Four aligned comparison cards across the bottom for the blockade levels — "Factor B (proximal, alternative pathway)", "C3 (central)", "C5a receptor", "C5 (terminal)" — each with a short trade-off line, all the SAME size (do NOT rank or crown a 'best' drug). One prominent teal message strip: "Vaccination reduces risk; it does not eliminate it." Light background only. Small semi-transparent navy "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, dark backgrounds, neon, over-saturation. Inter only, no serif fonts. Do NOT rank drugs or mark any agent "best". No manufacturer/brand names or packaging. Never omit the attribution.

QUALITY CHECK:
16:9, off-white background, central cascade with "disease control" above and "host-defense cost" below, four equal blockade cards (no ranking), "vaccination reduces risk; it does not eliminate it" message present, attribution bottom-right.

---

## 9 — Before the first dose (patient-friendly checklist)

FILE NAME: complement-targeted-therapy-kidney-disease-07-before-first-dose.png
IMAGE TYPE: Multi-panel educational infographic (checklist)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients + clinicians
VISUAL GOAL: six rounded readiness cards, with a bottom safety strip; no antibiotic names or doses.

PROMPT:
Patient-friendly clinical checklist infographic, landscape 16:9, off-white #fafafa background, clean sans-serif typography in Inter, navy #0f1e2e headings, teal #1a6b72 accents, small tidy line icons. Six rounded cards, each with a simple icon and a short label: 1) "Confirm exact drug & target"; 2) "Review MenACWY and MenB vaccination"; 3) "Review pneumococcal & Hib needs for the specific drug"; 4) "Document the antimicrobial plan"; 5) "Carry an emergency safety card"; 6) "Know the symptoms needing immediate emergency care". A bottom teal strip reads: "Serious infection can occur even after vaccination or while taking prevention." Light background only, generous whitespace, mobile-readable. Small semi-transparent navy "renalcarematters.com" bottom-right. Do NOT show any antibiotic names or doses.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, dark backgrounds, neon, over-saturation, generic stock look. Inter only, no serif fonts. No antibiotic names or doses. No brand/manufacturer names. Never omit the attribution.

QUALITY CHECK:
16:9, off-white background, six clearly labelled readiness cards, bottom teal safety strip present, no antibiotic names/doses, attribution bottom-right, mobile-readable.

---

## 10 — Response is more than proteinuria (evidence hierarchy)

FILE NAME: complement-targeted-therapy-kidney-disease-08-response-hierarchy.png
IMAGE TYPE: Multi-panel educational infographic (hierarchy)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians + patients
VISUAL GOAL: five ascending layers with example markers placed at the correct layer, and an honest footer.

PROMPT:
Evidence-hierarchy infographic, landscape 16:9, off-white background, clean sans-serif typography in Inter, navy/teal accents. Five ascending horizontal layers (a stacked pyramid or tier stack), from bottom to top: 1) "Target engagement (pharmacodynamic assay)"; 2) "Tissue response (C3 deposit clearance)"; 3) "Disease activity (proteinuria, hematuria, platelets/LDH, complement markers)"; 4) "Kidney-function trajectory (eGFR slope)"; 5) "Patient-important outcomes (survival, avoiding dialysis, serious infection, quality of life)". Place small example chips at the correct layer: "proteinuria" at Disease activity, "eGFR slope" at Kidney-function trajectory, "tissue C3 clearance" at Tissue response. Footer strip in teal: "Improvement at one layer does not automatically prove benefit at every layer." Light background only, generous whitespace, mobile-readable. Small semi-transparent navy "renalcarematters.com" bottom-right.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish, dark backgrounds, neon, over-saturation. Inter only, no serif fonts. No brand/manufacturer names. Never omit the attribution.

QUALITY CHECK:
16:9, off-white background, five correctly ordered layers (patient-important on top), example chips at the correct layers, footer disclaimer present, attribution bottom-right, mobile-readable.

---

### Production notes

- **Order of generation:** 1 (hero) and 2 (OG) unblock the page's LCP + share preview — do these first. Then 3 and 4 (already referenced inline). Then 5–10 as the section figures are added.
- **After receiving images:** drop `.png` + `.webp` twins into `images/`, confirm the OG tags already read `og:image:width="1200"` / `og:image:height="630"` (they do), and run the hero patch scripts listed in the asset-map note.
- **Alt text (house rule):** each inline `<figure>` needs a `<figcaption><p class="fig-desc">` describing the clinical relationship and the safety implication (not just the title), ≤ ~180 characters, plus a `<dl class="fig-abbrevs">` whenever the image contains an acronym.
- **Never** show manufacturer logos, brand trade dress, pills/packaging, drug rankings, or numeric probability/treatment thresholds in any panel — these mirror the guide's non-negotiable red lines.
