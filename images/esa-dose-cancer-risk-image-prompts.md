# Image Prompt Pack — `esa-dose-cancer-risk.html`

**Guide:** *More EPO Is Not Stronger Blood — ESA Dose, Hemoglobin Targets & Cancer Risk in Dialysis*
**Pipeline:** Stage 1 prompt pack. Paste each `COPY-READY PROMPT` into the ChatGPT Image Generator GPT
(https://chatgpt.com/g/g-pmuQfob8d-image-generator). Then hand this folder to Stage 2
(`williamriveromd-local-image-generator`) for manifests + `og:image` wiring.

**Skills used:**
- `williamriveromd-infographic-skill` — OG card, hero, target-band reference card, risk card, **and the decision algorithm** (Archetype 3, Clinical Algorithm / Flowchart).
- `williamriveromd-biomedical-mechanism-figure` — Image 4 (EPO-receptor → cancer schematic).
- `williamriveromd-algorithm-generator` — **not installed** in this repo; the algorithm (Image 6) is produced with the infographic skill's Clinical Algorithm / Flowchart archetype, which is the house tool for flowcharts.

**House rules applied to every image:** light background only (white / off-white / soft gray);
navy/teal/green/amber/red as typography + accent colors only; mobile-readable; `williamriveromd.com`
attribution in the bottom-right (bottom-center for portrait).

---

## Image Map

| # | Section placement | Archetype | Ratio / px | File |
|---|---|---|---|---|
| 1 | OG / social share (meta tags) | Editorial OG card | 1.91:1 · 1200×630 | `esa-dose-cancer-risk-og.png` |
| 2 | Hero (inline LCP, top of guide) | Photorealistic editorial | 1:1 · 1254×1254 | `esa-dose-cancer-risk-hero.png` |
| 3 | "The Safe Zone: Your Hemoglobin Target" | Reference card / infographic | 4:3 · 1536×1152 | `esa-hemoglobin-target-bands.png` |
| 4 | "How EPO Might Feed Cancer" (mechanism) | Biomedical mechanism figure | 16:9 · 1792×1024 | `esa-epo-receptor-cancer-mechanism.png` |
| 5 | "The New Evidence (2026)" | Clinician reference / case snapshot | 4:3 · 1536×1152 | `esa-kim2026-risk-card.png` |
| 6 | "But I Still Feel Tired — The Real Fix" | Clinical algorithm / flowchart | 2:3 portrait · 1024×1536 | `esa-tired-at-target-algorithm.png` |

---

## IMAGE 1 — OG / Social Share Card

- **SECTION PLACEMENT:** `og:image` / `twitter:image` meta tags (not inline)
- **FILE NAME:** `esa-dose-cancer-risk-og.png`
- **ARCHETYPE:** Editorial OG card (typographic)
- **AUDIENCE:** Mixed (patients + clinicians scrolling social/iMessage)
- **VISUAL MIX:** 2D infographic typography (primary) · single small 3D component (EPO vial + ascending dose bars)
- **PURPOSE:** Stop-the-scroll card carrying the one-line thesis: more EPO past target = risk, not benefit.
- **KEY CONCEPTS:** "More EPO ≠ stronger blood"; target ceiling 11.5 g/dL; 2026 cancer signal in older patients.
- **DIMENSIONS:** 1200 × 630 (FIXED — never change)

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
> Premium editorial social-share card for a nephrology patient-education website, exactly 1200×630 px, on a clean white (#ffffff) background. Left two-thirds: large bold condensed navy (#0f1e2e) headline reading "More EPO Isn't Stronger Blood", with a smaller clinical-teal (#1a6b72) subhead "Once hemoglobin hits target, a higher EPO dose adds risk — not benefit." Right third: a restrained semi-photorealistic 3D render of a small labelled EPO/erythropoietin medication vial and prefilled syringe beside a row of ascending dose bars where the tallest bars turn amber (#b8860b) then red (#b91c1c) to signal "too high". A thin teal rule and a small green→amber→red hemoglobin band motif along the bottom edge. Generous negative space, strong hierarchy, mobile-thumbnail-readable, calm and authoritative. Bottom-right corner: small semi-transparent navy text "williamriveromd.com". Light background only.

**NEGATIVE INSTRUCTIONS:** Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, stock-photo look, excessive saturation. NEVER use dark/navy/charcoal/black backgrounds. Never omit the williamriveromd.com attribution.

**QUALITY CHECK:** Headline legible at thumbnail size; exactly 1200×630; white base with navy/teal/amber/red accents; attribution present bottom-right.

---

## IMAGE 2 — Photorealistic Editorial Hero

- **SECTION PLACEMENT:** Top of guide, inline LCP hero (square)
- **FILE NAME:** `esa-dose-cancer-risk-hero.png`
- **ARCHETYPE:** Photorealistic editorial hero
- **AUDIENCE:** Patients & families
- **VISUAL MIX:** Photorealistic Filipino models (primary)
- **PURPOSE:** Trust-building image of a shared-decision conversation — the nephrologist explaining "we've reached your target."
- **KEY CONCEPTS:** Reassurance; dialysis context; shared decision over dose escalation.
- **DIMENSIONS:** 1254 × 1254 (1:1)

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
> Photorealistic medical editorial hero image for a nephrology patient-education guide, square 1254×1254. Show a calm, reassuring Filipino nephrologist (white coat) seated beside an older Filipino dialysis patient (around 60–70) in a bright, airy, naturally lit clinic, gently showing a simple hemoglobin chart on a tablet where the value sits comfortably inside a green "target" band. Warm, trustworthy mood, natural skin texture, soft daylight, clean white-walled clinical interior, shallow depth of field. Restrained navy and teal accents in the setting. Preserve calm negative space in the upper area for a title overlay. No embedded text except a small semi-transparent navy "williamriveromd.com" in the bottom-right corner. Light, bright background only — never dark or moody.

**NEGATIVE INSTRUCTIONS:** Avoid cartoon style, clutter, AI gibberish text, unrealistic anatomy, overprocessed HDR, moody/dark lighting, stock-photo blandness. NEVER dark/navy/black backgrounds. Never omit attribution.

**QUALITY CHECK:** Believable Filipino clinical scene, bright lighting, calm faces, room for title, attribution bottom-right.

---

## IMAGE 3 — Hemoglobin Target "Traffic-Light" Reference Card

- **SECTION PLACEMENT:** "The Safe Zone: Your Hemoglobin Target"
- **FILE NAME:** `esa-hemoglobin-target-bands.png`
- **ARCHETYPE:** Clinician/patient reference card (2D infographic)
- **AUDIENCE:** Mixed
- **VISUAL MIX:** 2D infographic bands + small 3D blood-tube component
- **PURPOSE:** Make the 10–11.5 g/dL ceiling instantly legible and show what action each zone implies.
- **KEY CONCEPTS:** <10 below target (check iron first) · 10–11.5 target/goal (hold steady) · >11.5 above ceiling (reduce/hold; stroke & clot risk).
- **DIMENSIONS:** 1536 × 1152 (4:3)

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
> Clean nephrology patient-education reference card, 1536×1152, white background. A horizontal hemoglobin scale from 8 to 14 g/dL rendered as three rounded color bands: an amber (#b8860b) band labelled "Below target (<10 g/dL) — check iron first", a green (#1f7a4d) band labelled "TARGET 10–11.5 g/dL — the goal · hold the dose steady", and a red (#b91c1c) band labelled ">11.5 g/dL — above ceiling · reduce or hold EPO; more strokes & clots in trials". A clear navy marker arrow points to the middle of the green band with the caption "Aim here — not higher." To the left, a small semi-photorealistic 3D blood collection tube with red cells. Large bold navy (#0f1e2e) title "Your Hemoglobin Target", clinical-teal (#1a6b72) subheadings, generous whitespace, mobile-readable labels, no microtext. Bottom-right: small semi-transparent navy "williamriveromd.com". Light background only.

**NEGATIVE INSTRUCTIONS:** Avoid cartoon style, clutter, tiny labels, AI gibberish, neon gradients, dark backgrounds. Never omit attribution.

**QUALITY CHECK:** Three bands clearly colour-coded green/amber/red; numbers legible on mobile; teal/navy typography on white; attribution bottom-right.

---

## IMAGE 4 — Biomedical Mechanism Figure (EPO Receptor → Cancer)

> **Generated with `williamriveromd-biomedical-mechanism-figure`.** Flag the oncogenic pathway as a
> **proposed mechanism** — the 2026 data are associative, not proof of causation.

- **SECTION PLACEMENT:** "How EPO Might Feed Cancer" (clinician detail; also referenced in patient mode)
- **FILE NAME:** `esa-epo-receptor-cancer-mechanism.png`
- **ARCHETYPE:** Review-article mechanism schematic (organ → magnified unit → injury/intervention/benefit flow)
- **AUDIENCE:** Clinicians + motivated patients
- **VISUAL MIX:** Flat vector anatomy with soft semi-3D shading
- **PURPOSE:** Show that EPO receptors exist on erythroid precursors **and** on tumor/premalignant cells, so high ESA dose can drive proliferation, angiogenesis, and an immunosuppressive microenvironment.
- **DIMENSIONS:** 1792 × 1024 (16:9)

**COPY-READY PROMPT (mechanism-skill template):**
> Create a publication-grade biomedical mechanism schematic, 1792×1024, flat vector style with soft semi-3D shading on a white background, thin dashed connector boxes, muted clinical palette (light gray-blue anatomy, soft yellow highlights, red for proliferation/injury, blue for protective context), clean sans-serif labels.
>
> **Topic:** Erythropoiesis-stimulating agents (ESAs) and a proposed oncogenic pathway in kidney failure.
> **Disease context:** Anemia of dialysis-dependent CKD treated with high-dose ESA.
>
> **Organ-level panel (left):** Simplified bone marrow inside a long bone, labelled "Bone marrow — intended target", with a small dashed connector box pointing right to the magnified cellular panel. Add a faint second simplified organ cluster (colon and lung) labelled "Off-target tissues (digestive, respiratory)".
>
> **Magnified mechanism panel (center/right, dashed border):** Show two cells side by side, each displaying an "EPO receptor (EPO-R)" on its surface with an erythropoietin molecule binding.
> - Left cell = "Erythroid precursor (intended)": label "↑ RBC production → corrects anemia (at target dose)".
> - Right cell = "Tumor / premalignant cell (off-target)": concise callouts:
>   - ↑ Proliferation
>   - ↓ Apoptosis
>   - ↑ Angiogenesis (small new-vessel sprout icon)
>   - Immunosuppressive tumor microenvironment
>
> **Bottom summary flow (left → center → right):**
> - Left pale-pink pathology box "Drivers": High ESA dose · EPO-R activation on malignant cells · Pro-angiogenesis · Immune modulation · Synergy with immunosenescence & inflammation in age ≥60.
> - Center box (bridge): bold label "Proposed mechanism (associative, not proven)".
> - Right pale-blue outcome box: ↑ de novo cancer risk with high-dose ESA (digestive, respiratory); risk concentrated in patients ≥60 (Kim et al. 2026).
>
> Generous whitespace, slide-readable labels, no photorealism, no dark background, no decorative effects. Small semi-transparent navy "© williamriveromd.com" in the bottom-right corner.

**MEDICAL-ACCURACY NOTES:** Do not imply proven causation — keep "proposed mechanism / associative." EPO-R expression on tumor cells and pro-angiogenic/immune effects are the literature-cited hypotheses; anatomy (marrow erythroid line vs epithelial tumor cell) must stay plausible.

**QUALITY CHECK:** Two-cell EPO-R contrast clear; injury→bridge→benefit flow legible; "proposed/associative" wording visible; white background; attribution bottom-right.

---

## IMAGE 5 — Kim et al. 2026 "Risk at a Glance" Card

- **SECTION PLACEMENT:** "The New Evidence (2026): High ESA Doses & Cancer"
- **FILE NAME:** `esa-kim2026-risk-card.png`
- **ARCHETYPE:** Clinician reference / case-snapshot card with a simple forest-plot
- **AUDIENCE:** Clinicians (readable by patients)
- **VISUAL MIX:** 2D infographic + minimalist forest-plot
- **PURPOSE:** Summarize the study's adjusted odds ratios and the decisive age interaction in one glance.
- **KEY CONCEPTS:** AOR 1.23 overall (CI 1.11–1.35); ≥60y 1.47; <60y no association; digestive 1.37; respiratory 1.48; sensitivity 1.31.
- **DIMENSIONS:** 1536 × 1152 (4:3)

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
> Clean clinician reference infographic, 1536×1152, white background, publication-grade nephrology design. Title in bold navy (#0f1e2e): "High-Dose ESA & Cancer Risk in Dialysis — Kim et al., JAMA Network Open 2026". Below, a minimalist horizontal forest plot with a vertical "no effect" reference line at AOR 1.0 and clean rounded markers with horizontal confidence-interval whiskers for these rows, each labelled with its value:
> - "All patients — high-dose ESA: AOR 1.23 (1.11–1.35)" (teal marker, right of the line)
> - "Sensitivity (censor last 6 mo): 1.31 (1.18–1.46)" (teal marker)
> - "Age ≥60 years: 1.47" (red marker, furthest right)
> - "Age <60 years: no association" (gray marker sitting on the 1.0 line)
> - "Digestive cancers: 1.37" and "Respiratory cancers: 1.48" (amber markers)
> A small side panel of stat chips: "35,165 dialysis patients", "2,320 cancers vs 7,456 controls", "median follow-up 6.5 y". A one-line caption in clinical teal: "Risk tracked the ESA dose and was concentrated in older patients." Strong hierarchy, generous whitespace, mobile-readable numerals, no microtext. Bottom-right: small semi-transparent navy "williamriveromd.com". Light background only.

**NEGATIVE INSTRUCTIONS:** Avoid cartoon style, clutter, tiny labels, AI gibberish numbers, neon, dark backgrounds. Numbers must read exactly as specified. Never omit attribution.

**QUALITY CHECK:** Forest plot reads left-to-right against the 1.0 line; ≥60 marker clearly the most extreme; all ORs legible; white base; attribution bottom-right.

---

## IMAGE 6 — Clinical Algorithm: "Tired at Target?"

> **Generated with `williamriveromd-infographic-skill` Archetype 3 (Clinical Algorithm / Flowchart)** —
> standing in for the unavailable `williamriveromd-algorithm-generator`. House flowchart aesthetic.

- **SECTION PLACEMENT:** "But I Still Feel Tired — The Real Fix"
- **FILE NAME:** `esa-tired-at-target-algorithm.png`
- **ARCHETYPE:** Clinical algorithm / flowchart (top-to-bottom)
- **AUDIENCE:** Mixed (clinician decision logic, patient-legible)
- **VISUAL MIX:** 2D algorithm nodes
- **PURPOSE:** Replace the reflex "raise the EPO" with the real work-up — confirm target, fix iron, exclude other causes; escalate ESA only when genuinely below target.
- **DIMENSIONS:** 1024 × 1536 (2:3 portrait)

**COPY-READY IMAGE GENERATOR GPT PROMPT:**
> Clinical nephrology algorithm infographic, portrait 1024×1536, premium KDIGO-style guideline flowchart on a white background. Top-to-bottom pathway titled "Tired Dialysis Patient Asking for More EPO?" with rounded nodes connected by clean navy lines; maximum branching, no spaghetti, generous whitespace, mobile-readable.
> - Start node (teal): "Patient feels tired / requests higher EPO".
> - Decision node: "Is hemoglobin already at the KDIGO target (10–11.5 g/dL)?"
>   - "NO → below target" branch (amber action node): "Check iron first; ESA dose may be increased ~25% if iron adequate — recheck in 2–4 weeks".
>   - "YES → at/above target" branch (green): proceed down.
> - Action node: "Do NOT raise EPO. Look for the real cause."
> - Parallel check nodes (teal): "Iron deficiency — check TSAT & ferritin (most common)"; "Inflammation or infection"; "Blood loss (often GI)"; "Under-dialysis"; "High parathyroid hormone".
> - Caution node (amber): "Hgb >11.5 g/dL → reduce or hold EPO".
> - Red escalation/warning node: "Pushing past target = ↑ stroke, clots, and (age ≥60) cancer signal — coverage ≠ recommended".
> - Endpoint node (green): "Fix the treatable cause → energy improves, usually with NO extra EPO".
> Use navy structure lines, teal recommendation boxes, amber caution nodes, red warning node, green optimal-path nodes. Bottom-center: small semi-transparent navy "williamriveromd.com". Light background only.

**NEGATIVE INSTRUCTIONS:** Avoid cartoon style, spaghetti connectors, tiny unreadable labels, AI gibberish, dark backgrounds. Keep ≤5 branching levels. Never omit attribution.

**QUALITY CHECK:** Single clear top-to-bottom path; node colours match logic (teal/green/amber/red); legible on mobile; portrait attribution bottom-center.

---

## Stage 2 hand-off notes

- Once images are generated and confirmed, run `williamriveromd-local-image-generator` to build the
  guide folder, `image-manifest.csv/json`, and to append `og:image` / `og:image:width="1200"` /
  `og:image:height="630"` / `og:image:alt` tags for **Image 1** to `guides/esa-dose-cancer-risk.html`.
- The hero (**Image 2**) is the inline LCP; after adding it to the guide, run
  `patch_hero_fetchpriority.py`, `patch_hero_fullwidth.py`, and `patch_hero_maxwidth.py` on this guide
  (they were intentionally skipped while the guide had no hero image).
