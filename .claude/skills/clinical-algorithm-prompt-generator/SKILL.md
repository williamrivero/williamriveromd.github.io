---
name: clinical-algorithm-prompt-generator
description: Generate image prompts for clean clinical algorithm flowcharts resembling AHA-style resuscitation algorithms and journal-style nephrology treatment algorithms.
---

# Clinical Algorithm Image Prompt Generator Skill

## Purpose

Generate high-quality image prompts that produce polished clinical algorithm diagrams with the visual logic, spacing, hierarchy, and formatting of:

1. AHA-style emergency care algorithms  
2. Journal-style treatment regimen algorithms, similar to nephrology/medical review figures

The output must be a complete image-generation prompt, not the algorithm itself unless requested.

---

## Core Visual Style

Use a clean medical guideline aesthetic:

- White or very light background
- Centered vertical flow
- Rounded rectangles for process/action steps
- Diamonds for decision points
- Thin directional arrows
- Muted pastel medical colors
- Spacious layout with generous margins
- Minimal decorative elements
- Professional journal/guideline typography
- Clear hierarchy from top to bottom
- No clutter, no cartoon styling, no photorealistic people

---

## Style Mode A: AHA / Resuscitation Algorithm

Use this style for BLS, ACLS, PALS, dialysis code-blue, emergency response, triage, or CPR-related workflows.

### Visual rules

- Portrait orientation, preferably 4:5 or 8.5×11
- Title at top-left or top-center in bold black sans-serif
- Main flow runs vertically down the center
- Pastel green rounded rectangles for safety, monitoring, or supportive actions
- Peach/orange rounded rectangles for initial assessment or activation steps
- Pink/red diamond shapes for decision nodes
- Blue rounded rectangles for CPR, shock, or active treatment steps
- Gray rounded capsule for transitional steps such as “AED arrives”
- Red bold branch labels for urgent clinical states
- Thin black arrows
- Optional dashed horizontal divider separating early assessment from resuscitation phase
- Side branches allowed left and right with return arrows

### Prompt template

Create a polished medical guideline algorithm flowchart in the style of an American Heart Association provider algorithm. Use a white background, clean sans-serif typography, thin black arrows, pastel rounded boxes, and pink decision diamonds. Layout should be portrait, centered, spacious, and easy to read.

Use these visual conventions:
- Green rounded boxes for safety, monitoring, or supportive care
- Peach/orange rounded boxes for initial assessment and activation steps
- Pink diamond boxes for decision questions
- Blue rounded boxes for active treatment steps
- Gray capsule boxes for transitional equipment or timing steps
- Red bold labels beside arrows for emergency branch conditions
- A dashed horizontal divider may separate assessment from intervention
- Maintain strict alignment, consistent spacing, and guideline-grade clarity

Content to render:
[INSERT ALGORITHM CONTENT HERE]

Design requirements:
- Title at top
- No decorative icons unless clinically necessary
- No photos
- No 3D elements
- No dark background
- No excessive shadows
- Use only short, readable text inside boxes
- Professional clinical education style

---

## Style Mode B: Journal / Nephrology Treatment Algorithm

Use this style for nephrology, vasculitis, CKD, glomerulonephritis, metabolic, pharmacotherapy, and disease-treatment algorithms.

### Visual rules

- White background
- Portrait or square layout
- Top-down treatment pathway
- Beige rounded rectangles for diagnostic or severity categories
- Pale blue rounded rectangles for assessment and treatment phases
- Pale green rounded rectangles for therapies, maintenance, remission, or outcomes
- Thin muted blue or teal arrows
- Symmetrical branching from central trunk
- Minimal text per node
- No bullet-heavy boxes
- Figure-caption-compatible appearance
- Academic medical journal look

### Prompt template

Create a clean academic medical journal treatment algorithm flowchart on a white background. The design should resemble a nephrology review figure: minimal, centered, symmetrical, and publication-ready.

Use these visual conventions:
- Beige rounded rectangles for diagnosis, disease category, or severity classification
- Pale blue rounded rectangles for assessment phases or treatment stages
- Pale green rounded rectangles for therapeutic options, maintenance, disease control, and remission outcomes
- Thin muted blue/teal arrows
- Top-down flow with balanced left-right branching
- Consistent rounded corners, box widths, and vertical spacing
- No icons, no decorative graphics, no dark background
- Typography should be clean, black, and journal-like

Content to render:
[INSERT ALGORITHM CONTENT HERE]

Design requirements:
- Keep all text concise
- Preserve clinical hierarchy
- Use centered alignment
- Maintain wide margins
- Avoid clutter
- Add a small caption area only if requested
- Make the final image look like a medical journal figure

---

## Decision Logic

When the user asks for:
- CPR, ACLS, BLS, PALS, emergency, dialysis code blue, arrest, bradycardia, tachycardia → use Style Mode A.
- CKD, AAV, vasculitis, glomerulonephritis, nephrology treatment, remission, induction, maintenance, pharmacotherapy → use Style Mode B.
- If unclear, ask which style: “AHA emergency algorithm” or “journal treatment algorithm.”

---

## Output Format

Return only the final image-generation prompt unless the user asks for explanation.

Do not include JSON unless explicitly requested.

---

## Quality Checklist

Before finalizing the prompt, ensure:

- The algorithm has a clear top-to-bottom clinical logic.
- Decision nodes are visually distinct.
- Treatment/action nodes are color-coded consistently.
- Branch labels are short and readable.
- The prompt prevents dark backgrounds, clutter, cartoons, and unnecessary icons.
- The image could plausibly appear in a clinical guideline or medical journal.

## Branding and Copyright Requirements

Every generated algorithm image must include a discreet but visible copyright attribution.

Placement:
- Bottom-right corner preferred
- Alternative: centered footer if layout requires
- Never overlap algorithm nodes or arrows
- Maintain adequate margin from page edge

Format:
© williamriveromd.com

Typography:
- Small sans-serif font
- Medium gray (#6b7280 to #8a8a8a)
- Professional and unobtrusive
- Fully readable at publication resolution

Rules:
- Include on every image
- Must remain visible after cropping
- Do not place inside any flowchart node
- Do not use watermark opacity lower than 70%
- Should appear as a publisher attribution rather than a decorative watermark

Prompt instruction to append automatically:

Include a small professional footer reading:
"© williamriveromd.com"
positioned at the bottom-right corner in subtle gray medical-publication styling.
