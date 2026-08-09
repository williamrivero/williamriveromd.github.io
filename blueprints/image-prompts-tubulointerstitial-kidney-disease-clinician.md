# Image Prompt Pack — Beyond the Glomerulus (TIN clinician series)

**Companion to** `tubulointerstitial-kidney-disease-clinician-blueprint.md` (§M).
**Production target:** ChatGPT Image Generator GPT — https://chatgpt.com/g/g-pmuQfob8d-image-generator
**Pipeline:** Stage 1 (these prompts, authored via the `williamriveromd-*` graphic skills) → generate in GPT → save PNG + WebP twin into `images/` → wire `og:image` / `<picture>` per guide.

## House constants (baked into every prompt below)
- **Backgrounds:** light only — white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, light teal tint `#eef6f7`. **Never** navy/charcoal/black.
- **Palette (accents/type only):** navy `#0f1e2e`, clinical teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b` (caution only), clinical red `#b91c1c` (danger only), soft purple `#6c3d8e` (specialist/add-on).
- **Type:** sans-serif only — **Inter** (default here), Nunito Sans, IBM Plex Sans, or Manrope. No serif, no decorative faces.
- **Attribution (mandatory):** small semi-transparent navy `renalcarematters.com`, bottom-right (bottom-center for portrait), ~70% opacity, never obscuring content.
- **Never** fabricate diagnostic photomicrographs — schematics only, clearly labeled.
- **OG cards are ALWAYS 1200 × 630** and get explicit `og:image:width="1200"` / `og:image:height="630"`.

## Plan matrix (16 assets across 5 pages)

| ID | Page | Asset | Skill used | Size | Reuse |
|---|---|---|---|---|---|
| H1 | Hub | OG social card | infographic | 1200×630 | — |
| H2 | Hub | Circular vignette hero | hero-vignette | 2048×2048 | — |
| H3 | Hub + Part 1 | Filter vs recovery system (mechanism) | biomedical-mechanism | 1792×1024 | shared |
| H4 | Hub + Part 1 | Three patterns (AIN/ATI/chronic TIN) | simple-figure | 1792×1024 | shared |
| H5 | Hub + Part 2 | Eight overlapping causes | infographic | 1792×1024 | shared |
| P1a | Part 1 | OG social card | infographic | 1200×630 | — |
| P1b | Part 1 | "The classic triad is uncommon" + modern biomarkers | simple-figure | 1792×1024 | — |
| P2a | Part 2 | OG social card | infographic | 1200×630 | — |
| P2b | Part 2 | Philippine exposure history (6-card checklist) | infographic | 1792×1024 | — |
| P3a | Part 3 | OG social card | infographic | 1200×630 | — |
| P3b | Part 3 | Pattern → cause diagnostic workflow | algorithm-generator (Mode C) | 1024×1536 | — |
| P3c | Part 3 | Biopsy is an integration problem | infographic | 1792×1024 | — |
| P3d | Part 3 | Steroid safety gate | algorithm-generator (Mode C) | 1659×948 | — |
| P4a | Part 4 | OG social card | infographic | 1200×630 | — |
| P4b | Part 4 | Emerging entity atlas (2×5) | infographic | 1792×1024 | — |
| P4c | Part 4 | Systemic → tubulointerstitium crosstalk sigil | organ-crosstalk-sigil | 1024×1024 | — |

> Each part's in-page hero uses the **HTML Evidence-Snapshot card** (`aside.hero-cards.mode-physician`), so only the **Hub** needs a rendered vignette hero (H2). Parts 1–4 use their OG card for sharing and in-body figures for teaching.

---

# HUB — tubulointerstitial-kidney-disease-clinician.html

## H1 — Hub OG social card
- **FILE NAME:** `tubulointerstitial-kidney-disease-clinician-og.png`
- **SKILL:** infographic-skill (OG card) · **DIMENSIONS:** 1200 × 630 (1.91:1)
- **PLACEMENT / WIRING:** `og:image` for the hub. Add `og:image:width="1200"` `og:image:height="630"` `og:image:alt` (below).
- **ALT TEXT:** "Kidney cutaway highlighting a nephron tubule and surrounding interstitium, with the series title Beyond the Glomerulus — emphasizing disease beyond the glomerular filter."

**PROMPT:**
Generate one image, exactly 1200 × 630 pixels, landscape Open Graph social card, off-white #fafafa background, publication-grade nephrology editorial aesthetic, generous whitespace, all typography in Inter. LEFT 58% is a text-safe block: a small uppercase clinical-teal #1a6b72 eyebrow reading "TUBULES & INTERSTITIUM · CLINICIANS"; below it a large bold navy #0f1e2e headline reading "Beyond the Glomerulus"; below that a smaller navy subhead reading "A Philippine clinician's guide to tubulointerstitial kidney disease." RIGHT 42% shows one anatomically accurate semi-photorealistic 3D human kidney in restrained renal red-brown with a clean semi-transparent cutaway revealing one highlighted nephron tubule glowing soft clinical teal #1a6b72 and a pale-mint #eef6f7 interstitial halo around it; the glomerulus is visible but deliberately smaller than the tubule. One small amber #b8860b caution accent dot only. Bottom-right: "renalcarematters.com" in small navy at ~70% opacity. Calm, premium, medically accurate, mobile-legible.

**NEGATIVE INSTRUCTIONS:** Avoid dark/navy/charcoal/black backgrounds, neon, cybernetic styling, clutter, pills as a motif, fabricated histopathology, tiny unreadable text, serif or decorative fonts, AI gibberish text. Never omit the renalcarematters.com attribution.

---

## H2 — Hub circular vignette hero
- **FILE NAME:** `tubulointerstitial-kidney-disease-clinician-vignette-hero.png`
- **SKILL:** hero-vignette v3 (Scaffold C — anatomy) · **DIMENSIONS:** 2048 × 2048 (square, 85–90% inscribed circle)
- **COMPOSITION ARCHETYPE:** F (Anatomy) · **CAMERA:** three-quarter cross-section
- **PLACEMENT / WIRING:** in `figure.hero-figure > .hero-vignette` via `<picture>` (PNG + WebP twin), `width="2048" height="2048"`. Wordless — the HTML `<h1>` sits beside it.
- **ALT TEXT:** "Semi-photorealistic 3D kidney with one enlarged nephron whose tubular segments glow teal against a pale-mint interstitial halo, the glomerulus small — the tubule is the hero."

**PROMPT:**
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: F Anatomy. Camera: three-quarter cross-section. Subject: one anatomically accurate human kidney in restrained warm renal red-brown with a subtle translucent cutaway revealing a single enlarged nephron whose tubular segments glow softly in clinical teal #1a6b72, surrounded by a delicate pale-mint #eef6f7 interstitial halo; keep the glomerulus visible but smaller so the tubule reads as the hero. Gentle studio lighting, soft contact shadow, light off-white background. Visual hierarchy: the nephron/kidney occupies 60–70% of the circle; 2–3 subtle supporting tubular structures 20–30%; reserve a 20–25% TITLE SAFE ZONE on the LEFT of soft empty background (no anatomy, leader lines, labels, or callouts in that zone). Soft falloff toward a slightly deeper neutral at the rim. Premium medical-textbook-cover feel.
Absolutely NO text of any kind: no title, subtitle, caption, label, leader line, logo, or watermark.

**NEGATIVE INSTRUCTIONS:** Avoid busy layouts, collage, cropped circle, cropped anatomy, objects touching the circular border, content inside the title-safe zone, baked-in text/titles/labels/logos/watermarks, rectangular borders/frames/banners, dark/charcoal/black backgrounds, cartoon/neon/HDR/over-saturation, distorted or implausible anatomy.

---

## H3 — Filter vs recovery system (shared: Hub + Part 1)
- **FILE NAME:** `tin-filter-vs-recovery-mechanism.png`
- **SKILL:** biomedical-mechanism-figure · **DIMENSIONS:** 1792 × 1024 (16:9)
- **PLACEMENT:** Hub "simplified nephron map" module; Part 1 §A. Inline `<figure>` — author `.fig-desc` + `.fig-abbrevs` (Na, HCO₃, RTA).
- **ALT TEXT:** "Review-article schematic: the glomerulus filters plasma while the tubule reclaims, acidifies, concentrates, and fine-tunes electrolytes — kidney function depends on both compartments."

**PROMPT:**
Create a publication-grade biomedical mechanism schematic, scientific review-article style, flat vector with soft semi-3D shading, white #ffffff background, generous whitespace, all typography in Inter. Title at top in navy #0f1e2e: "The filter and the recovery system." LEFT organ-level panel: a clean glomerular capillary tuft filtering pale fluid into Bowman's space, labeled "Glomerulus — filters plasma," with a thin dashed connector box pointing to the magnified panel. RIGHT larger magnified panel inside a thin dashed border: a nephron tubule (proximal → loop of Henle → distal → collecting) with four restrained clinical-teal #1a6b72 callouts reading exactly "Reclaims (Na, water, HCO₃, glucose)", "Acidifies (H⁺ / NH₄⁺)", "Concentrates (medullary gradient)", and "Fine-tunes electrolytes (K, PO₄)"; soft-yellow highlight on the proximal tubule; blue arrows returning useful solutes and water to an adjacent peritubular capillary. Bottom summary flow: left pale-pink box "Injury to the recovery system → tubular dysfunction (glycosuria, phosphate/bicarbonate wasting, concentrating defect)"; center bridge box "Filter intact ≠ kidney intact"; right pale-blue box "Recognizing tubular clues reframes a bland-sediment AKI." Muted clinical palette (light gray-blue anatomy, soft yellow highlight, red arteries, blue return arrows), thin dashed connectors. Bottom-right: "© renalcarematters.com" small semi-transparent navy.

**NEGATIVE INSTRUCTIONS:** Avoid photorealism, dark backgrounds, decorative effects, shadows, cartoon styling, overcrowding, invented pathways, fabricated numeric thresholds, serif fonts, AI gibberish text. Never omit the renalcarematters.com attribution.

---

## H4 — Three patterns, not one disease (shared: Hub + Part 1)
- **FILE NAME:** `tin-three-patterns-comparison.png`
- **SKILL:** simple-figure (three-card comparison) · **DIMENSIONS:** 1792 × 1024 (16:9)
- **PLACEMENT:** Hub tissue-pattern module; Part 1 §B. Inline `<figure>` — `.fig-abbrevs`: AIN, ATI, TIN, IFTA.
- **ALT TEXT:** "Comparison of acute interstitial nephritis, acute tubular injury, and chronic tubulointerstitial nephritis — inflammation, epithelial injury, and fibrosis respectively — under a caution that a pattern does not name the cause."

**PROMPT:**
Clean medical education comparison infographic, AJKD/NEJM graphical-abstract style, white #ffffff background, title centered at top in bold navy #0f1e2e reading "Three patterns, not one disease," all typography in Inter, clinical-teal #1a6b72 rules. Arrange THREE equal rounded cards horizontally on a very soft gray #f3f4f6 panel. CARD 1 heading "AIN" — a simplified schematic tubule surrounded by interstitial inflammatory cells and edema; caption "Inflammation + tubulitis; little fibrosis." CARD 2 heading "ATI" — visibly stressed tubular epithelial cells with few inflammatory cells; caption "Tubular epithelial injury; little inflammation." CARD 3 heading "Chronic TIN" — thinned tubules and pale interstitial scar; caption "Fibrosis + tubular atrophy (IFTA); variable inflammation." Below the cards, a full-width amber #b8860b caution strip reading "A tissue pattern does not by itself name the cause." Use clearly simplified schematics, never photomicrographs. Mobile-readable labels ≥11pt, generous whitespace. Bottom-right: "renalcarematters.com" small semi-transparent navy.

**NEGATIVE INSTRUCTIONS:** Avoid realistic pathology slides/photomicrographs, dark backgrounds, neon, clutter, tiny labels, serif/decorative fonts, AI gibberish text, over-saturation. Never omit the renalcarematters.com attribution.

---

## H5 — Eight causes behind one pattern (shared: Hub + Part 2)
- **FILE NAME:** `tin-eight-causes.png`
- **SKILL:** infographic-skill (multi-panel) · **DIMENSIONS:** 1792 × 1024 (16:9)
- **PLACEMENT:** Hub eight-cause overview; Part 2 §7.1. Inline `<figure>`.
- **ALT TEXT:** "Eight overlapping etiologic categories that can produce a tubulointerstitial pattern, shown as translucently overlapping cards to signal that categories co-occur."

**PROMPT:**
Generate one image, landscape 16:9, 1792 × 1024 pixels, WHITE #ffffff background, publication-grade clinician infographic, all typography in Inter, generous whitespace. Title in navy #0f1e2e: "Eight causes behind one tubulointerstitial pattern." Create exactly EIGHT rounded cards in two rows of four, with subtle overlapping translucent edges to signal that categories overlap. Card labels exactly: "Drug effect", "Autoimmune / immune-mediated", "Infection-associated", "Hereditary / genetic", "Toxic / metabolic", "Monoclonal protein-associated", "Mimics", "Idiopathic / other." Each card carries one minimal flat line icon and one short clue phrase only (e.g. Drug effect → "PPI · NSAID · antibiotic"; Monoclonal → "light chains, casts"; Mimics → "leukemia / lymphoma"). A central small teal #1a6b72 caption between the rows: "The categories overlap — clinicopathologic correlation finds the cause." Palette navy #0f1e2e, teal #1a6b72, renal green #1f7a4d, amber #b8860b (used only on Mimics / Idiopathic to signal uncertainty), soft gray #f3f4f6, pale mint #eef6f7. Bottom-right: "renalcarematters.com" small semi-transparent navy.

**NEGATIVE INSTRUCTIONS:** Avoid a rigid wheel/pie layout, dark fills, tiny text, clutter, serif/decorative fonts, neon, AI gibberish text. Never omit the renalcarematters.com attribution.

---

# PART 1 — recognizing-tubulointerstitial-kidney-disease-clinician.html
*(also uses H3 + H4)*

## P1a — Part 1 OG social card
- **FILE NAME:** `recognizing-tubulointerstitial-kidney-disease-clinician-og.png`
- **SKILL:** infographic-skill (OG card) · **DIMENSIONS:** 1200 × 630
- **WIRING:** `og:image` + width/height/alt.
- **ALT TEXT:** "Part 1 share card — When the Tubules Are the Problem: recognizing tubulointerstitial injury before the diagnosis is obvious."

**PROMPT:**
Generate one image, exactly 1200 × 630 pixels, landscape Open Graph card, off-white #fafafa background, publication-grade nephrology editorial aesthetic, all typography in Inter, generous whitespace. LEFT 58% text-safe block: small uppercase teal #1a6b72 eyebrow "PART 1 · CLINICIANS"; large bold navy #0f1e2e headline "When the Tubules Are the Problem"; smaller navy subhead "Recognizing tubulointerstitial injury before the diagnosis is obvious." RIGHT 42%: a restrained semi-3D nephron tubule in soft clinical teal with a faint bland urine-drop motif and a small magnifying-glass line icon (recognition), glomerulus small in the background. Bottom-right "renalcarematters.com" small navy ~70% opacity.

**NEGATIVE INSTRUCTIONS:** Avoid dark backgrounds, neon, clutter, fabricated histopathology, tiny text, serif/decorative fonts, AI gibberish. Never omit the renalcarematters.com attribution.

---

## P1b — "The classic triad is uncommon" + modern biomarkers
- **FILE NAME:** `tin-classic-triad-uncommon.png`
- **SKILL:** simple-figure (comparison / stat panel) · **DIMENSIONS:** 1792 × 1024 (16:9)
- **PLACEMENT:** Part 1 §D myth cards / evidence callout. Inline `<figure>` — `.fig-abbrevs`: AIN, CXCL9, TNF-α, IL-9, AUC.
- **ALT TEXT:** "Teaching figure: the classic fever-rash-eosinophilia triad occurs in only about 10% of biopsy-proven drug-induced AIN and urine eosinophils perform poorly, while modern urine biomarkers CXCL9 and TNF-α/IL-9 outperform them."

**PROMPT:**
Clean clinical education comparison infographic, AJKD/NEJM graphical-abstract style, white #ffffff background, title centered at top in bold navy #0f1e2e reading "The classic AIN triad is uncommon," subtitle in clinical teal #1a6b72 "Modern urine biomarkers outperform eosinophils," all typography in Inter. LEFT panel (amber #b8860b accent) "Old signals — unreliable": three stacked chips — "Fever + rash + eosinophilia ≈ 10% of biopsy-proven drug AIN"; "Urine eosinophils: poor accuracy (sens ~31%, spec ~68%)"; "Bland sediment does NOT exclude AIN." RIGHT panel (renal green #1f7a4d accent) "Newer signals — better": chips — "Urine CXCL9 — validated AIN biomarker"; "Urine TNF-α + IL-9 (aOR ~11 and ~7)"; "Adding biomarkers: AUC 0.62 → 0.84." A thin dashed vertical divider between panels. Small footer strip in navy: "Availability limited — interpret in clinical context; none replaces biopsy." Rounded cards, ample whitespace, mobile-readable ≥11pt. Bottom-right "renalcarematters.com" small semi-transparent navy.

**NEGATIVE INSTRUCTIONS:** Avoid dark backgrounds, clutter, tiny labels, invented statistics beyond those given, fabricated photomicrographs, serif/decorative fonts, AI gibberish, over-saturation. Never omit the renalcarematters.com attribution.

---

# PART 2 — tubulointerstitial-disease-causes-clinician.html
*(also uses H5)*

## P2a — Part 2 OG social card
- **FILE NAME:** `tubulointerstitial-disease-causes-clinician-og.png`
- **SKILL:** infographic-skill (OG card) · **DIMENSIONS:** 1200 × 630
- **WIRING:** `og:image` + width/height/alt.
- **ALT TEXT:** "Part 2 share card — What Is Injuring the Tubules? An eight-bucket differential adapted to Philippine clinical practice."

**PROMPT:**
Generate one image, exactly 1200 × 630 pixels, landscape Open Graph card, off-white #fafafa background, publication-grade nephrology editorial aesthetic, all typography in Inter. LEFT 58% text-safe: small uppercase teal #1a6b72 eyebrow "PART 2 · CLINICIANS"; large bold navy #0f1e2e headline "What Is Injuring the Tubules?"; smaller navy subhead "An eight-bucket differential for Philippine practice." RIGHT 42%: eight small translucent overlapping rounded chips in a compact 2×4 cluster tinted navy/teal/green with one amber chip, suggesting overlapping etiologic categories, one small nephron tubule motif behind them. Bottom-right "renalcarematters.com" small navy ~70% opacity.

**NEGATIVE INSTRUCTIONS:** Avoid flags, maps, stereotypes, dark backgrounds, neon, clutter, tiny text, serif/decorative fonts, AI gibberish. Never omit the renalcarematters.com attribution.

---

## P2b — The Philippine exposure history
- **FILE NAME:** `tin-philippine-exposure-history.png`
- **SKILL:** infographic-skill (multi-panel checklist) · **DIMENSIONS:** 1792 × 1024 (16:9)
- **PLACEMENT:** Part 2 §7.3 exposure callout. Inline `<figure>` — `.fig-abbrevs`: NSAID, PPI, ART, TB, HIV, UTI, BPH, PPE.
- **ALT TEXT:** "Six-card Philippine exposure-history checklist — medicines, anti-infective and cancer therapy, supplements and unlabeled products, infection epidemiology, urinary tract, and work and environment — under the reminder that exposure is a clue, not proof."

**PROMPT:**
Generate one image, landscape 16:9, 1792 × 1024 pixels, WHITE #ffffff background, flat publication-grade clinician checklist infographic, all typography in Inter, generous whitespace. Title in navy #0f1e2e: "The Philippine exposure history clinicians should ask." Create SIX equal rounded cards in a balanced 3-by-2 grid, each with a small clean flat line icon, a navy heading, and a short teal #1a6b72 example line: 1 "Medicines" — NSAIDs, PPIs, antibiotics, allopurinol; 2 "Anti-infective & cancer therapy" — anti-TB, ART, aminoglycosides, checkpoint inhibitors; 3 "Supplements & unlabeled products" — herbal, detox, slimming, bodybuilding, high-dose vitamin C (amber #b8860b caution accent on this card); 4 "Infection epidemiology" — floodwater, rodents, TB, HIV, recurrent UTI; 5 "Urinary tract" — stones, retention, BPH, catheter, pelvic disease; 6 "Work & environment" — heat, dehydration, pesticides, batteries, welding, mining. Full-width footer strip in navy: "Ask for names, photos, doses, dates, and competing events — exposure is a clue, not proof." Bottom-right "renalcarematters.com" small semi-transparent navy.

**NEGATIVE INSTRUCTIONS:** Avoid national flags, maps, ethnic stereotypes, dark backgrounds, clutter, tiny text, serif/decorative fonts, AI gibberish, over-saturation. Never omit the renalcarematters.com attribution.

---

# PART 3 — tubulointerstitial-nephritis-workup-biopsy-clinician.html

## P3a — Part 3 OG social card
- **FILE NAME:** `tubulointerstitial-nephritis-workup-biopsy-clinician-og.png`
- **SKILL:** infographic-skill (OG card) · **DIMENSIONS:** 1200 × 630
- **WIRING:** `og:image` + width/height/alt.
- **ALT TEXT:** "Part 3 share card — From Pattern to Cause: workup, biopsy, and cause-directed management of suspected tubulointerstitial disease."

**PROMPT:**
Generate one image, exactly 1200 × 630 pixels, landscape Open Graph card, off-white #fafafa background, publication-grade nephrology editorial aesthetic, all typography in Inter. LEFT 58% text-safe: small uppercase teal #1a6b72 eyebrow "PART 3 · CLINICIANS"; large bold navy #0f1e2e headline "From Pattern to Cause"; smaller navy subhead "Workup, biopsy, and cause-directed management." RIGHT 42%: a minimal vertical 3-node flow (phenotype → exclude infection/obstruction → biopsy-if-it-changes-management) in teal connectors with a small kidney-biopsy-needle line icon, one amber caution node. Bottom-right "renalcarematters.com" small navy ~70% opacity.

**NEGATIVE INSTRUCTIONS:** Avoid dark backgrounds, neon, clutter, fabricated histopathology, tiny text, serif/decorative fonts, AI gibberish. Never omit the renalcarematters.com attribution.

---

## P3b — Suspected TIN: from pattern to cause (workflow)
- **FILE NAME:** `tin-pattern-to-cause-workflow.png`
- **SKILL:** algorithm-generator (Style Mode C — house style) · **DIMENSIONS:** 1024 × 1536 (portrait 2:3)
- **PLACEMENT:** Part 3 §8.1 main workflow. Inline `<figure>` — `.fig-abbrevs`: AKI, AKD, CKD, LM, IF, EM.
- **ALT TEXT:** "Vertical clinical algorithm: confirm trajectory, define phenotype, build the exposure timeline, exclude infection and obstruction, order targeted tests, decide whether biopsy changes management, treat the cause, and follow the AKI-to-CKD transition."

**PROMPT:**
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style. White #ffffff background, restrained navy #0f1e2e and teal #1a6b72 typography in Inter, thin teal connector arrows, generous margins, portrait layout, centered and symmetrical. Title at top in navy: "Suspected tubulointerstitial disease — from pattern to cause." Top-to-bottom nodes: 1 (navy action) "Confirm AKI / AKD / CKD trajectory"; 2 (navy action) "Define the phenotype — glomerular, tubular, interstitial, obstructive, vascular, or mixed"; 3 (navy action) "Build the medicine, supplement, infection, cancer, urinary, and occupational timeline"; 4 (amber #b8860b caution node) "Exclude active infection and obstruction"; 5 (navy action) "Order targeted tests by phenotype and resource level"; 6 (teal #1a6b72 decision diamond) "Will biopsy materially change management?" — YES branch to a renal-green #1f7a4d node "Plan LM + IF + EM / special studies with renal pathology," NO branch to a soft-gray node "Document rationale; monitor response and competing diagnoses"; both converge on a renal-green node "Treat the cause — not the pattern label"; final navy node "Follow recovery and the AKI-to-CKD transition." A small clinical-red #b91c1c side-alert box: "Urgent: severe AKI, oliguria, hyperkalemia, acidosis, pulmonary edema, uremia, infected obstruction." Include a small professional footer reading "© renalcarematters.com" at the bottom-center in subtle gray.

**NEGATIVE INSTRUCTIONS:** Avoid crossing/spaghetti arrows, dense text, dark background, photorealistic people, cartoon styling, decorative clutter, serif/decorative fonts, AI gibberish, invented numeric thresholds. Never omit the renalcarematters.com attribution.

---

## P3c — Biopsy is an integration problem
- **FILE NAME:** `tin-biopsy-integration.png`
- **SKILL:** infographic-skill (reference/mechanism convergence) · **DIMENSIONS:** 1792 × 1024 (16:9)
- **PLACEMENT:** Part 3 §8.6 clinicopathologic integration. Inline `<figure>` — `.fig-abbrevs`: LM, IF, EM, IHC, SV40, BK.
- **ALT TEXT:** "Integration diagram: light microscopy, immunofluorescence, and electron microscopy/special studies plus clinical timeline, imaging, microbiology/serology, and genetics/hematology converge on an etiologic or attributive diagnosis, under the caution that no single feature is pathognomonic."

**PROMPT:**
Generate one image, landscape 16:9, 1792 × 1024 pixels, WHITE #ffffff background, publication-grade biomedical integration diagram, all typography in Inter, generous whitespace. Title in navy #0f1e2e: "Kidney biopsy is an integration problem." LEFT group of three equal rounded teal-accented cards labeled "LM — architecture & injury pattern", "IF — immune deposits & light chains", and "EM / special studies — ultrastructure, crystals, organisms". RIGHT group of four smaller navy cards labeled "Clinical timeline", "Imaging", "Microbiology + serology", and "Genetics / hematology". Thin teal #1a6b72 arrows from both groups converge on one large renal-green #1f7a4d bordered endpoint reading "Etiologic or attributive diagnosis". Beneath it, an amber #b8860b caution line: "No single eosinophil, granuloma, plasma cell, TBM deposit, crystal, or scar is automatically pathognomonic." Simplified flat icons only, never fabricated photomicrographs. Bottom-right "renalcarematters.com" small semi-transparent navy.

**NEGATIVE INSTRUCTIONS:** Avoid dark backgrounds, excessive/crossing arrows, fabricated histopathology, clutter, tiny text, serif/decorative fonts, AI gibberish. Never omit the renalcarematters.com attribution.

---

## P3d — Before corticosteroids for presumed TIN (safety gate)
- **FILE NAME:** `tin-steroid-safety-gate.png`
- **SKILL:** algorithm-generator (Style Mode C — house style) · **DIMENSIONS:** 1659 × 948 (16:9)
- **PLACEMENT:** Part 3 §8.7 glucocorticoid section. Inline `<figure>` — `.fig-abbrevs`: TB, HIV, GI.
- **ALT TEXT:** "A safety-gate graphic with six checkpoints — exposure withdrawn, active infection assessed, TB and HIV context considered, obstruction excluded, biopsy decision documented, and organ-risk review — before any empirical corticosteroid decision, explicitly stating the gate does not decide that steroids are indicated."

**PROMPT:**
Create a clean publication-ready clinical safety-gate graphic in the renalcarematters.com house style. White #ffffff background, navy #0f1e2e and teal #1a6b72 typography in Inter, generous whitespace, centered. Title in navy: "Before corticosteroids for presumed TIN." Place one large amber #b8860b outlined gate shape at center with exactly SIX checkpoint cards arranged around it, each a rounded teal-accented node: "Suspected exposure withdrawn?", "Active infection assessed?", "TB and HIV context considered?", "Obstruction excluded?", "Biopsy decision documented?", and "Diabetes, GI, psychiatric, bone, and infection risks reviewed?". Beyond the gate, a renal-green #1f7a4d bordered endpoint reads "Cause-specific plan + monitoring ownership". A small clinical-red #b91c1c warning dot appears only beside "Active infection assessed?". Bottom caption in soft gray: "This safety gate does not decide that steroids are indicated." Include a small professional footer reading "© renalcarematters.com" at the bottom-right in subtle gray.

**NEGATIVE INSTRUCTIONS:** Avoid drug-dose numbers or regimens, shield clichés, dark backgrounds, clutter, photorealistic people, serif/decorative fonts, AI gibberish. Never omit the renalcarematters.com attribution.

---

# PART 4 — emerging-tubulointerstitial-diseases-clinician.html

## P4a — Part 4 OG social card
- **FILE NAME:** `emerging-tubulointerstitial-diseases-clinician-og.png`
- **SKILL:** infographic-skill (OG card) · **DIMENSIONS:** 1200 × 630
- **WIRING:** `og:image` + width/height/alt.
- **ALT TEXT:** "Part 4 share card — Emerging Tubulointerstitial Diseases Clinicians Now Need to Recognize: new entities, overlaps, and mimics from modern renal pathology."

**PROMPT:**
Generate one image, exactly 1200 × 630 pixels, landscape Open Graph card, off-white #fafafa background, publication-grade advanced-nephrology aesthetic, all typography in Inter. LEFT 58% text-safe: small uppercase teal #1a6b72 eyebrow "PART 4 · ADVANCED · NEPHROLOGY"; large bold navy #0f1e2e headline "Emerging Tubulointerstitial Diseases"; smaller navy subhead "New entities, overlaps, and mimics to recognize." RIGHT 42%: a compact 2×3 cluster of small labeled evidence chips in teal/green with two amber "emerging" chips, suggesting an atlas of new entities, a faint nephron motif behind. Bottom-right "renalcarematters.com" small navy ~70% opacity.

**NEGATIVE INSTRUCTIONS:** Avoid dark backgrounds, neon, clutter, fabricated histopathology, tiny text, serif/decorative fonts, AI gibberish. Never omit the renalcarematters.com attribution.

---

## P4b — Emerging entity atlas
- **FILE NAME:** `tin-emerging-entity-atlas.png`
- **SKILL:** infographic-skill (multi-panel atlas) · **DIMENSIONS:** 1792 × 1024 (16:9)
- **PLACEMENT:** Part 4 §9.1 entity cards. Inline `<figure>` — `.fig-abbrevs`: ICI, TIN, IgG4, VEXAS, ADTKD, PH1.
- **ALT TEXT:** "A two-row atlas of ten emerging tubulointerstitial entities, each with a simplified schematic clue and an evidence badge from established through emerging."

**PROMPT:**
Generate one image, landscape 16:9, 1792 × 1024 pixels, WHITE #ffffff background, publication-grade advanced-nephrology atlas, all typography in Inter, two rows of five clean rounded cards. Title in navy #0f1e2e: "Tubulointerstitial diseases clinicians now need to recognize." Card labels exactly: "ICI-associated TIN", "IgG4-related TIN", "IgM plasma-cell TIN", "Anti-brush-border disease", "VEXAS", "ADTKD", "Primary hyperoxaluria", "Monoclonal tubular lesions", "Vancomycin cast nephropathy", "Infiltrative mimics". Each card contains one simplified flat schematic clue and a small evidence badge chip reading one of: "established", "consensus", "cohort", "rare series", or "emerging" (teal #1a6b72 / renal green #1f7a4d for established/consensus/cohort; amber #b8860b for rare series / emerging). Footer strip in navy: "Recognize the clue; confirm with clinical, pathology, microbiology, hematology, or genetic context." Bottom-right "renalcarematters.com" small semi-transparent navy.

**NEGATIVE INSTRUCTIONS:** Avoid fabricated pathology micrographs, dark fills, tiny text, neon, clutter, serif/decorative fonts, AI gibberish. Never omit the renalcarematters.com attribution.

---

## P4c — Systemic → tubulointerstitium crosstalk sigil
- **FILE NAME:** `tin-systemic-crosstalk-sigil.png`
- **SKILL:** organ-crosstalk-sigil · **DIMENSIONS:** 1024 × 1024 (1:1)
- **PLACEMENT:** Part 4 opener / systemic-disease framing. Inline `<figure>` — `.fig-desc` describing the axes; no acronyms needed in-image.
- **ALT TEXT:** "A minimal line-art sigil showing systemic sources — a salivary/lacrimal gland (IgG4), bone marrow (VEXAS), and liver (oxalate) — connected by dotted arrows down to the kidneys, symbolizing that tubulointerstitial injury often begins outside the kidney."

**PROMPT:**
Create a simple medical organ-crosstalk sigil illustration.
ORGANS: a salivary/lacrimal gland (representing IgG4-related disease), a bone-marrow/long-bone icon (representing VEXAS), a liver (representing oxalate overproduction), and two kidneys at the base.
RELATIONSHIP: show that systemic and distant-organ processes converge on the tubulointerstitium — dotted curved arrows flow downward from each upper organ to both kidneys, with a soft returning loop, symbolizing "the injury often begins outside the kidney."
STYLE: minimal clinical line-art, thin monoline strokes, soft teal-blue palette (clinical teal #1a6b72, muted slate, pale gray) on a white background, clean rounded organ shapes, balanced radial sigil-like composition, generous whitespace, no photorealism, no 3D, no text labels.
COMPOSITION: place the three source organs across the top in a gentle arc, the two kidneys symmetrically at the bottom center, connected by dotted arrows forming a calm converging loop. Symbolic and suitable for a clinician-education nephrology website.
OUTPUT: square 1024 × 1024, clean margins, high-resolution, publication-grade medical icon aesthetic. Include a small semi-transparent "renalcarematters.com" attribution in the bottom-right corner, not obscuring the sigil.

**NEGATIVE INSTRUCTIONS:** Avoid photorealistic anatomy, surgical detail, excessive labels, dark backgrounds, neon, crowded arrows, thick cartoon outlines, 3D rendering, glossy icons, dramatic lighting, stock-photo style. Never omit the renalcarematters.com attribution.

---

## Production checklist (Stage 2)
1. Paste each **PROMPT** block into the ChatGPT Image Generator GPT; download the PNG.
2. Save to `images/<file-name>.png` **and** create a WebP twin `images/<file-name>.webp`.
3. Verify: light background, Inter type, correct size, `renalcarematters.com` mark present, no fabricated photomicrographs, exact labels rendered (regenerate if text is garbled).
4. Wire per guide:
   - **OG cards (H1, P1a, P2a, P3a, P4a):** `<meta property="og:image" content="https://renalcarematters.com/images/<file>.png">` + `og:image:width="1200"` + `og:image:height="630"` + `og:image:alt="<alt text>"`, mirror to `twitter:image`.
   - **Hub vignette (H2):** `<picture>` inside `figure.hero-figure > .hero-vignette`, `width="2048" height="2048"`; then run `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`.
   - **In-body figures (H3–H5, P1b, P2b, P3b–d, P4b–c):** wrap in `<figure>` with `<figcaption><p class="fig-desc">…</p><dl class="fig-abbrevs">…</dl></figcaption>`; `assets/image-lightbox.js` reads them (`patch_image_lightbox.py`).
5. Keep every acronym in each figure's `.fig-abbrevs` also present in the guide's Glossary accordion (rule 12) and expanded on first body use (rule 13).
