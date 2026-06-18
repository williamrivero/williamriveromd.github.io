---
name: williamriveromd-biomedical-mechanism-figure
description: >-
  Produces a clean, publication-grade biomedical mechanism figure prompt for
  williamriveromd.com nephrology patient-education guides — a review-article
  schematic that explains organ-to-cellular pathophysiology using simple
  vector-style anatomy, dashed magnified panels, restrained clinical colors,
  and clinically accurate labels. Use when the user wants a mechanism/pathway
  schematic (e.g. kidney mitochondrial dysfunction, glomerular injury, tubular
  pathways) with an organ-level panel, a magnified functional-unit inset
  (nephron/glomerulus/tubule/mitochondria/vessel/cell), and a bottom
  injury → intervention → benefit summary flow. Prefer this over the
  infographic or simple-figure skills when the request is specifically a
  scientific review-article mechanism diagram.
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
- Use clean sans-serif typography
- Keep all text legible and medically precise
- Avoid decorative effects, photorealism, shadows, dark backgrounds, or cartoonish styling

## Core Layout Pattern
Use a multi-scale biomedical figure layout:

1. **Left panel: Organ-level context**
   - Show a simplified organ or tissue.
   - Label the disease state, e.g. “AKI or CKD.”
   - Include major vessels or structural landmarks.
   - Add a small dashed connector box that points to the magnified mechanism panel.

2. **Center/right panel: Magnified functional unit**
   - Show the relevant biological unit:
     - nephron
     - glomerulus
     - tubule
     - mitochondria
     - vessel wall
     - immune cell
     - epithelial cell
   - Use a dashed border around the magnified panel.
   - Highlight affected segments in pale yellow or muted color.
   - Add concise metabolic/pathway labels.

3. **Bottom mechanism summary**
   - Left bottom box: injury/pathology drivers.
   - Center bottom box: intervention or mechanistic bridge.
   - Right bottom box: expected beneficial effects.
   - Use arrow flow from injury → intervention → benefit.

## Text Style
- Use short, high-yield scientific labels.
- Prefer mechanisms over generic descriptions.
- Use arrows for directionality:
  - ↓ OXPHOS
  - ↑ Glycolysis
  - ↓ ATP
  - ↑ ROS
  - ↓ Apoptosis
- Use bullet points sparingly.
- Bold only the key final mechanism when useful.

## Example Figure Logic
For a kidney mitochondrial dysfunction figure:

- Left: kidney cross-section labeled “AKI or CKD.”
- Small inset: damaged mitochondria.
- Main panel: nephron schematic.
- Proximal tubule callout:
  - ↓ OXPHOS
  - ↓ β-oxidation
  - ↓ Gluconeogenesis
- Collecting/tubular callout:
  - ↓ OXPHOS
  - ↑ Glycolysis
- Loop/tubular energy callout:
  - ↓ ATP
- Bottom left pink box:
  - Increased cellular oxidative stress
  - Increased ROS
  - Loss of mitochondrial quality control mechanisms
  - **Mitochondrial dysfunction**
- Bottom center:
  - Mitochondrial transplantation
  - healthy mitochondria icon
- Bottom right blue box:
  - Increased ATP and viability
  - Transcriptomic and proteomic modulation
  - Decreased apoptosis, ROS, lipid peroxidation

## Medical Accuracy Rules
- Do not invent pathways.
- Match anatomy to the mechanism.
- Keep nephron segment labels anatomically plausible.
- Use “hypothesis,” “proposed mechanism,” or “experimental therapy” when the intervention is not standard clinical care.
- For preclinical concepts such as mitochondrial transplantation, avoid implying routine clinical availability unless explicitly requested.

## Output Requirements
- Clean SVG-like or high-resolution PNG style
- Prefer 4:3 or 16:9 aspect ratio for educational figures
- No watermarks unless requested
- No gibberish text
- No excessive icons
- No dark theme
- Maintain generous whitespace
- Make labels readable at slide-viewing size

## Prompt Template

Create a publication-grade biomedical mechanism schematic about:

**Topic:** [insert topic]

**Disease context:** [insert disease]

**Central mechanism:** [insert mechanism]

**Organ-level panel:**  
Show [organ/tissue] with simplified internal anatomy and a disease label.

**Magnified mechanism panel:**  
Show [cell/unit/pathway] inside a dashed inset. Highlight the affected region. Add concise callouts showing:
- [pathway change 1]
- [pathway change 2]
- [pathway change 3]

**Bottom summary flow:**  
Left pathology box: [injury drivers]  
Center intervention/mechanism box: [intervention or central process]  
Right benefit/outcome box: [expected effects]

Use a white background, muted clinical colors, clean sans-serif labels, thin dashed connector lines, and a review-article figure style. Avoid photorealism, dark backgrounds, decorative elements, and overcrowding.
