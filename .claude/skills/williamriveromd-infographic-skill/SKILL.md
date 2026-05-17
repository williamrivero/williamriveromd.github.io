---
name: williamriveromd-infographic-skill
description: >-
  Produces ready-to-paste ChatGPT (DALL·E 3 / GPT-image) prompts for the
  williamriveromd.com nephrology patient-education site. Use whenever creating
  or designing ANY visual asset for these guides — editorial hero images,
  pathophysiology posters, clinical algorithms/flowcharts, multi-panel
  educational infographics, clinician reference cards, food matrices, case
  snapshots, circular workflows, dialysis access/procedural diagrams, or 3D
  medical component renderings (kidneys, glomeruli, vessels, dialysis access,
  machines, stenosis, thrombus). Outputs a single copy-paste prompt block
  engineered for photorealism, medical/anatomical accuracy, and a unified
  williamriveromd.com house style.
---

# WILLIAM RIVERO MD — CHATGPT IMAGE PROMPT SYSTEM (v5)

This skill does **not** render images. It writes the **exact prompt text** to
paste into ChatGPT's image generator (DALL·E 3 / GPT-image). That tool has
**no** negative-prompt flag, no weights, no style-reference parameter — so
every control must live *inside the prompt text*. This system encodes that
control to fix the three recurring failures: **flat/non-photorealistic
output, anatomical/medical errors, and inconsistent style across guides.**

## How to use

1. Pick the archetype (§4).
2. Assemble the prompt in this exact order:
   **STYLE LOCK (§1) → DO-NOT CLAUSE (§2) → ANATOMY SPEC (§3, only if anatomy appears) → ARCHETYPE TEMPLATE (§4) → TEXT RULES (§5).**
3. Fill every `[BRACKET]`. Delete nothing from the verbatim blocks.
4. Paste into ChatGPT as one message. Generate.
5. Run the QC checklist (§7). If it fails, iterate with the §7 phrasing — do **not** start a fresh prompt (you lose consistency).

The STYLE LOCK and DO-NOT CLAUSE are **pasted verbatim in every single prompt** — that repetition *is* the consistency engine, since the tool has no `--sref`.

## 1. STYLE LOCK — paste verbatim, every prompt

> Style: premium medical-publication editorial illustration in the visual
> language of KDIGO, AJKD, and NEJM. Clean, calm, authoritative, modern.
> Color palette strictly limited to: deep teal #1a6b72 (primary), dark slate
> #1e2a38 (text/structure), near-white #f9fafb (background), with restrained
> medical accents — clinical red #c0392b (danger/escalation), amber #e0a800
> (caution), green #2e7d57 (safe/recommended), violet #6b4fa1 (specialist).
> Generous negative space. Soft, even, diffused studio lighting. Subtle
> depth, no heavy drop shadows, no gradients-as-decoration. Flat-plus-dimensional
> hybrid: 2D layout discipline with semi-photorealistic 3D medical elements.
> Filipino clinical context where people or settings appear. Crisp,
> mobile-first legibility. Photographed on a full-frame camera, 50mm lens,
> f/4, high dynamic range, ultra-detailed, sharp focus, professional medical
> photography quality. No stock-photo cheesiness, no AI sheen, no neon, no
> sci-fi, no cartoon.

## 2. DO-NOT CLAUSE — paste verbatim, every prompt

> Do not include: garbled, misspelled, or invented text/labels; lorem-ipsum;
> watermarks or signatures; duplicated, fused, or extra anatomical structures;
> anatomically impossible organs or vessels; distorted hands or faces; more
> than the specified number of people; clutter or decorative noise; rainbow or
> neon colors; heavy bokeh; surreal or fantastical elements. Every anatomical
> structure must be medically accurate and correctly positioned. If you cannot
> render a label with correct spelling, render no label there.

## 3. ANATOMY SPEC — include the relevant lines whenever anatomy is shown

- **Kidney:** bean-shaped, ~11–12 cm, smooth capsule, deep red-brown,
  retroperitoneal; concave hilum medial; renal artery/vein/ureter exiting the
  hilum in correct order. Two kidneys only. No liver/spleen substitution.
- **Glomerulus:** tuft of capillary loops inside Bowman's capsule, afferent
  arteriole wider than efferent, podocytes wrapping capillaries.
- **Nephron:** glomerulus → proximal tubule → loop of Henle → distal tubule →
  collecting duct, in correct sequence.
- **AV fistula (AVF):** native artery-to-vein anastomosis at the wrist or
  elbow, dilated superficial vein, no synthetic tubing.
- **AV graft (AVG):** synthetic loop/straight conduit connecting artery to vein.
- **Central venous catheter (CVC):** dual-lumen catheter in internal jugular,
  tip at cavoatrial junction.
- **Hemodialysis circuit:** access → arterial line → blood pump → dialyzer →
  venous line → return, directionally correct.
- Append: "Anatomically accurate, medically correct, suitable for a
  peer-reviewed nephrology publication."

## 4. ARCHETYPE TEMPLATES

Each: when to use · aspect ratio · fill-in template.

### A. Editorial Hero — guide top banner
Ratio 16:9 (or 1200×630 for share). People/scene, minimal/no text.
> A photorealistic editorial photograph for a nephrology patient guide on
> [TOPIC]. Scene: [e.g., a Filipino nephrologist in a modern Manila clinic
> reviewing results with an older Filipino patient]. Composition: subject
> right third, clean negative space left for headline overlay. Warm,
> reassuring, dignified mood. No text in the image.

### B. Pathophysiology Poster
Ratio 4:5 or 1:1. One mechanism, labeled.
> A clean medical pathophysiology illustration explaining [MECHANISM, e.g.,
> how hypertension damages the glomerulus]. Central semi-photorealistic 3D
> [STRUCTURE]; 3–5 stages left-to-right with short callouts: [STAGE 1] /
> [STAGE 2] / [STAGE 3]. Each label ≤4 words, exact spelling provided below.

### C. Clinical Algorithm / Flowchart
Ratio 4:5 portrait. KDIGO/ADA/ESC-style.
> A clean clinical decision algorithm for [DECISION, e.g., managing
> hyperkalemia in CKD]. Vertical flow, max 3–5 branch levels, rounded nodes,
> straight orthogonal connectors. Teal = recommended path, red = escalate/
> emergency, amber = caution. Nodes contain only the exact text listed below.
> No spaghetti crossings.

### D. Multi-panel Educational Infographic
Ratio 4:5 or 9:16. 3–6 panels.
> A [N]-panel patient-education infographic on [TOPIC]. Even grid, each panel
> = one icon-style semi-realistic illustration + ≤6-word caption (exact text
> below). Consistent icon weight and panel size. Calm, uncluttered.

### E. Clinician Reference Card
Ratio 1:1 or 4:5. Dense but ordered.
> A clinician quick-reference card for [TOPIC]. Structured table/zoned layout,
> clear hierarchy, dosing/targets in a monospaced-style block. Professional,
> dense, legible at mobile size. All values exactly as listed below.

### F. Food Matrix
Ratio 1:1. Grid of foods by a metric.
> A kidney-diet food matrix for [NUTRIENT, e.g., potassium]. Photorealistic
> Filipino foods ([LIST]) arranged in a grid, color-coded green=low /
> amber=moderate / red=high. Each cell: realistic food photo + name (exact
> spelling below) + a small badge.

### G. Case Snapshot
Ratio 4:5. One patient vignette.
> A single-case clinical snapshot for [SCENARIO]. Left: semi-realistic patient
> figure; right: 3–4 vitals/labs in a clean stat stack (exact numbers below).
> One takeaway banner at the bottom.

### H. Circular Workflow
Ratio 1:1. Cyclical process.
> A circular workflow diagram of [CYCLE, e.g., the dialysis treatment cycle].
> 4–6 evenly spaced stages around a ring, directional arrows, central title
> hub. Each stage: icon + ≤3-word label (exact below).

### I. Access / Procedural Education
Ratio 4:5. Stepwise procedure/anatomy.
> A patient-education illustration of [PROCEDURE/ACCESS, e.g., an AV fistula
> for hemodialysis]. Semi-photorealistic 3D anatomy with the §3 spec,
> 2–4 numbered steps, clean leader lines to correctly spelled labels (below).

## 5. TEXT-IN-IMAGE RULES

- GPT-image renders short text fairly well but still errs. **List every word
  that must appear, verbatim, at the end of the prompt**, e.g.:
  `Exact labels, spelled exactly: "Stage 1", "eGFR ≥ 90", "Monitor".`
- Keep on-image text minimal — prefer ≤6 words per element.
- Hero images (archetype A): **"No text in the image."** Headlines are
  overlaid in HTML later.
- If a render still garbles text, switch that label to "no label" and add it
  in HTML instead of fighting the model.

## 6. CONSISTENCY PROTOCOL (whole-site cohesion)

- STYLE LOCK + DO-NOT CLAUSE pasted **identically** every time — never paraphrase.
- Fixed aspect ratio per archetype (above) — don't vary within a type.
- To match an existing approved image, append: *"Match the exact palette,
  lighting, line weight, and composition discipline of my established
  williamriveromd.com series."*
- One archetype change at a time when iterating.
- File naming: `[guide-slug]-[archetype]-[short-desc].png` (e.g.
  `aki-on-ckd-hero-clinic-consult.png`) so the set stays auditable.

## 7. QC CHECKLIST — reject & iterate

Reject if any: anatomy wrong/duplicated · misspelled or invented text ·
palette drift (colors outside §1) · >specified people · cartoonish/AI-sheen ·
clutter / lost negative space · style mismatch vs the series.

Iterate **in the same chat**, never from scratch:
> "Keep the composition, palette, lighting, and style **exactly** the same.
> Only change: [the kidney shape is wrong — make it bean-shaped with the hilum
> medial] / [fix the label to read exactly 'eGFR']. Change nothing else."

## QUALITY BAR

Publication-grade for a peer-reviewed nephrology journal · medically accurate ·
photorealistic where photographic · unified williamriveromd.com identity ·
mobile-first legible · zero gibberish.
