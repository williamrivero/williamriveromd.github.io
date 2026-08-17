---
name: biomedical-mechanism-figure
description: >-
  Create clean, publication-grade biomedical mechanism figures similar to a
  review-article schematic. Use when the user wants a multi-scale pathophysiology
  diagram explaining organ-to-cellular mechanisms — nephron schematics,
  mitochondrial dysfunction, glomerular injury, tubular pathways, immune
  activation, or any mechanism figure that needs organ-level context, a magnified
  functional-unit panel, and a bottom injury→intervention→benefit summary flow.
  Outputs a single copy-paste ChatGPT Image Generator prompt engineered for a
  flat-vector scientific style with muted clinical colors and clean sans-serif
  labels.
---

# Biomedical Mechanism Figure Skill

## Purpose
Create clean, publication-grade biomedical mechanism figures similar to a review-article schematic. The output should explain organ-to-cellular pathophysiology using simple vector-style anatomy, clear callouts, restrained colors, and clinically accurate labels.

## Visual Style
- Scientific review-article schematic
- Flat vector illustration with soft semi-3D shading
- White background
- Thin dashed boxes to separate magnified panels
- Minimal clutter
- Muted clinical palette:
  - Light gray-blue anatomy
  - Soft yellow for highlighted nephron/tubular segments
  - Red for arteries, injury, ROS, oxidative stress
  - Blue for veins/protective or therapeutic effects
  - Pale pink for pathology summary boxes
  - Pale blue for treatment/benefit summary boxes
- Clean sans-serif typography
- All text legible and medically precise
- No decorative effects, photorealism, shadows, dark backgrounds, or cartoonish styling

## Core Layout Pattern
Use a multi-scale biomedical figure layout:

1. **Left panel: Organ-level context**
   - Show a simplified organ or tissue.
   - Label the disease state, e.g. "AKI or CKD."
   - Include major vessels or structural landmarks.
   - Add a small dashed connector box pointing to the magnified mechanism panel.

2. **Center/right panel: Magnified functional unit**
   - Show the relevant biological unit (nephron, glomerulus, tubule, mitochondria, vessel wall, immune cell, or epithelial cell).
   - Use a dashed border around the magnified panel.
   - Highlight affected segments in pale yellow or muted color.
   - Add concise metabolic/pathway labels.

3. **Bottom mechanism summary**
   - Left bottom box: injury/pathology drivers (pale pink).
   - Center bottom box: intervention or mechanistic bridge.
   - Right bottom box: expected beneficial effects (pale blue).
   - Arrow flow: injury → intervention → benefit.

## Text Style
- Short, high-yield scientific labels.
- Prefer mechanisms over generic descriptions.
- Use arrows for directionality (↓ OXPHOS, ↑ Glycolysis, ↓ ATP, ↑ ROS, ↓ Apoptosis).
- Use bullet points sparingly.
- Bold only the key final mechanism when useful.

## Medical Accuracy Rules
- Do not invent pathways.
- Match anatomy to the mechanism.
- Keep nephron segment labels anatomically plausible.
- Use "hypothesis," "proposed mechanism," or "experimental therapy" for non-standard interventions.
- For preclinical concepts (e.g., mitochondrial transplantation), avoid implying routine clinical availability unless explicitly requested.

## Output Requirements
- Clean SVG-like or high-resolution PNG style
- 4:3 or 16:9 aspect ratio for educational figures
- No watermarks
- No gibberish text
- No excessive icons
- No dark theme
- Generous whitespace
- Labels readable at slide-viewing size

---

## How to Use This Skill

When the user requests a biomedical mechanism figure, gather:

1. **Topic** — what mechanism or process to illustrate
2. **Disease context** — AKI, CKD, diabetic nephropathy, etc.
3. **Central mechanism** — the core pathophysiological process
4. **Organ-level panel** — which organ/tissue and what disease label
5. **Magnified panel** — which cell/unit/pathway and the specific pathway changes (at least 3 callouts)
6. **Bottom summary flow** — left pathology box content, center intervention/bridge content, right benefit/outcome content

If any of these are missing, ask the user before generating the prompt.

---

## Output: Single Copy-Paste Prompt

Generate one complete, copy-paste prompt block using this template. Fill in all bracketed fields. Do not output anything else — just the prompt block, ready to paste into the ChatGPT Image Generator.

```
Create a publication-grade biomedical mechanism schematic.

Topic: [insert topic]
Disease context: [insert disease]
Central mechanism: [insert mechanism]

LEFT PANEL — Organ-level context:
Show [organ/tissue] with simplified internal anatomy. Label the disease state as "[disease label]." Include [major vessels or structural landmarks]. Add a small dashed connector arrow pointing to the magnified panel on the right.

CENTER/RIGHT PANEL — Magnified functional unit (dashed border):
Show [cell/unit/pathway] inside a dashed inset. Highlight [affected segment] in soft pale yellow. Add concise callout labels showing:
- [pathway change 1, e.g., ↓ OXPHOS]
- [pathway change 2, e.g., ↑ Glycolysis]
- [pathway change 3, e.g., ↓ ATP → ↑ ROS]
[add more callouts as needed]

BOTTOM SUMMARY FLOW (left to right with connecting arrows):
Left box (pale pink background): [injury/pathology drivers — 3–5 bullet points, bold the key mechanism]
Center box: [intervention or central mechanistic bridge — icon + label]
Right box (pale blue background): [expected beneficial effects — 3–5 bullet points]

Visual style: White background. Flat vector illustration with soft semi-3D shading. Muted clinical palette: light gray-blue anatomy, soft yellow for highlighted segments, red for injury/ROS/arteries, blue for protective effects/veins. Clean sans-serif typography. Thin dashed lines for panel borders and connector arrows. Minimal clutter. No photorealism. No dark background. No decorative effects. Generous whitespace. All labels readable at slide size.

Aspect ratio: [4:3 or 16:9]. High resolution. No watermarks.
```
