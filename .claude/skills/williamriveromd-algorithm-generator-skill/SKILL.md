---
name: williamriveromd-algorithm-generator-skill
description: Generate image-generation prompts for clean clinical algorithm flowcharts resembling AHA-style resuscitation algorithms and journal-style nephrology treatment algorithms, with williamriveromd.com copyright attribution.
---

# williamriveromd Algorithm Generator Skill

## Purpose

Generate high-quality image-generation prompts that produce polished clinical algorithm diagrams with the visual logic, spacing, hierarchy, and formatting of:

1. AHA-style emergency care algorithms
2. Journal-style medical and nephrology treatment algorithms

The output should usually be a complete image-generation prompt, not the algorithm itself, unless the user explicitly asks for the algorithm content.

---

## Universal Design Principles

Every generated prompt should create an image with:

- White or very light neutral background
- Clean medical guideline aesthetic
- Centered top-to-bottom clinical logic
- Rounded rectangles for process/action/treatment nodes
- Diamonds for decision nodes when applicable
- Thin directional arrows
- Muted pastel medical colors
- Consistent node size, padding, and spacing
- Clear hierarchy from diagnosis/assessment to treatment/outcome
- Generous margins and uncluttered negative space
- Crisp black or navy sans-serif typography, set in one of the four approved
  fonts only: Inter, Nunito Sans, IBM Plex Sans, or Manrope (never a serif font)
- Publication-grade vector infographic quality
- No photorealistic people
- No cartoon styling
- No decorative clutter
- No dark background
- No unnecessary icons unless requested

---

## Mandatory Copyright Attribution

Every generated algorithm image must include a discreet but visible copyright attribution.

Text:

© williamriveromd.com

Placement:

- Bottom-right corner preferred
- Centered footer acceptable if the layout requires it
- Never inside a flowchart node
- Never overlapping arrows, branches, or captions
- Maintain adequate page-edge margin
- Must remain visible after typical web/social cropping

Typography:

- Small sans-serif font
- Medium gray, approximately #6b7280 to #8a8a8a
- Professional and unobtrusive
- Readable at publication resolution
- Watermark opacity should not be lower than 70%

Default instruction to append to every image prompt:

Include a small professional footer reading “© williamriveromd.com” positioned at the bottom-right corner in subtle gray medical-publication styling.

---

## Mandatory Typeface

Every generated algorithm prompt must specify a clean sans-serif font, and may use
**only** one of these four approved faces:

- Inter
- Nunito Sans
- IBM Plex Sans
- Manrope

Never use a serif font, condensed display font outside this list, or any decorative
or handwritten typeface. Name the chosen approved font explicitly inside every image
prompt (e.g. “clean sans-serif typography set in Inter”).

---

## Hemofilter / Dialyzer Reference Anatomy (if the algorithm includes a circuit/filter legend or inset)

CRRT/HD algorithm cards sometimes benefit from a small circuit or pressure-point
legend alongside the decision logic. If one is requested (or the model adds one
unprompted), it must follow this verified anatomy — earlier prompts got this
wrong (missing points, garbled labels, a confusing left-right loop) and had to be
corrected:

- Hemofilter/dialyzer has **two end ports** (Arterial = blood in, Venous = blood
  out) and **two side ports** (Dialysate in, near the venous end; Effluent out,
  near the arterial end — true countercurrent flow). Replacement fluid merges
  into the blood line itself, never the filter's shell port. TMP is a pressure
  annotation across the filter, not a flow arrow.
- For a **small inset/legend**, draw the filter **vertically** (blood in at the
  bottom, out at the top) rather than horizontally — this avoids the left-right
  loop-back that causes tangled or garbled small diagrams. Explicitly instruct
  the model to include every pressure landmark the surrounding algorithm refers
  to (e.g. if the card has 4 alarm columns, the legend must show all 4 points).
- Never invent specific numeric pressure/alarm thresholds (mmHg values) unless
  they come from the source guide or a cited reference — real limits are
  device-specific; use device-dependent language ("use your unit's validated
  alarm limits") instead of a fabricated number.

---

# Style Mode A: AHA / Resuscitation Algorithm

## Use Cases

Use this style for:

- BLS
- ACLS
- PALS
- CPR
- Code blue
- Dialysis code blue
- Bradycardia algorithms
- Tachycardia algorithms
- Cardiac arrest algorithms
- Airway algorithms
- Opioid-associated emergency algorithms
- Emergency response and triage workflows

## Visual Rules

- Portrait orientation, preferably 4:5, 3:4, or 8.5 × 11
- Title at top-left or top-center in bold black sans-serif
- Main pathway runs vertically down the center
- Pastel green rounded rectangles for safety, monitoring, or supportive actions
- Peach/orange rounded rectangles for initial assessment and activation steps
- Pink/red diamond shapes for decision nodes
- Blue rounded rectangles for CPR, shock, or active treatment steps
- Gray rounded capsule boxes for transitional steps such as “AED arrives”
- Red bold branch labels for urgent clinical states
- Thin black or dark-gray arrows
- Optional dashed horizontal divider separating early assessment from resuscitation phase
- Side branches allowed left and right with return arrows
- Use short bullet lists only when needed; avoid dense paragraphs

## Prompt Template

Create a polished medical guideline algorithm flowchart in the style of an American Heart Association provider algorithm. Use a white background, clean sans-serif typography set in one of Inter, Nunito Sans, IBM Plex Sans, or Manrope (never a serif font), thin black arrows, pastel rounded boxes, and pink decision diamonds. Layout should be portrait, centered, spacious, and easy to read.

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
- Include a small professional footer reading “© williamriveromd.com” positioned at the bottom-right corner in subtle gray medical-publication styling

---

# Style Mode B: Journal / Nephrology Treatment Algorithm

## Use Cases

Use this style for:

- CKD algorithms
- ANCA-associated vasculitis algorithms
- Glomerulonephritis treatment pathways
- IgA nephropathy algorithms
- Nephrotic syndrome algorithms
- Metabolic acidosis algorithms
- CKD-MBD algorithms
- Pharmacotherapy pathways
- Disease-severity and treatment-selection pathways
- Induction, maintenance, remission, and tapering regimens

## Visual Rules

- White background
- Portrait or square layout
- Top-down treatment pathway
- Beige rounded rectangles for diagnosis, disease category, or severity classification
- Pale blue rounded rectangles for assessment phases or treatment stages
- Pale green rounded rectangles for therapeutic options, maintenance, disease control, or remission outcomes
- Thin muted blue or teal arrows
- Symmetrical branching from the central trunk
- Minimal text per node
- No bullet-heavy boxes
- Figure-caption-compatible appearance
- Academic medical journal look
- Balanced left-right branches
- Consistent node widths whenever possible

## Prompt Template

Create a clean academic medical journal treatment algorithm flowchart on a white background. The design should resemble a nephrology review figure: minimal, centered, symmetrical, and publication-ready.

Use these visual conventions:
- Beige rounded rectangles for diagnosis, disease category, or severity classification
- Pale blue rounded rectangles for assessment phases or treatment stages
- Pale green rounded rectangles for therapeutic options, maintenance, disease control, and remission outcomes
- Thin muted blue/teal arrows
- Top-down flow with balanced left-right branching
- Consistent rounded corners, box widths, and vertical spacing
- No icons, no decorative graphics, no dark background
- Typography should be clean, black, and journal-like, set in one of Inter, Nunito Sans, IBM Plex Sans, or Manrope (never a serif font)

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
- Include a small professional footer reading “© williamriveromd.com” positioned at the bottom-right corner in subtle gray medical-publication styling

---

# Style Mode C: williamriveromd.com House-Style Clinical Algorithm

## Use Cases

Use this style when the user wants a more branded, modern, visually polished algorithm for williamriveromd.com guides.

## Visual Rules

- Bright white or very light off-white background
- Navy #0f1e2e for title and structural text
- Teal #1a6b72 for decision nodes, arrows, or section accents
- Green #1f7a4d for qualifying endpoints, success states, or recommended actions
- Amber #b8860b for caution or conditional nodes
- Soft gray for side notes, exclusions, or reminders
- Centered, symmetric layout
- Strong use of negative space
- Publication-ready vector look
- Optional simple flat medical line icons if clinically relevant
- Icons must not touch node borders
- Avoid heavy 3D elements unless specifically requested

## Prompt Template

Create a clean publication-ready clinical algorithm flowchart in the williamriveromd.com house style. Use a white or very light off-white background, restrained navy and teal typography set in one of Inter, Nunito Sans, IBM Plex Sans, or Manrope (never a serif font), thin teal connector arrows, and generous margins. The layout should be centered, symmetrical, and suitable for a patient-facing or clinician-facing nephrology education guide.

Use these color conventions:
- Navy #0f1e2e for title, body text, and structural emphasis
- Teal #1a6b72 for decision nodes and connector accents
- Green #1f7a4d for final recommended actions or qualifying endpoints
- Amber #b8860b for caution nodes
- Soft gray for explanatory side notes

Content to render:
[INSERT ALGORITHM CONTENT HERE]

Design requirements:
- Clear title and optional subtitle
- Top-to-bottom clinical logic
- Rounded rectangles for actions and endpoints
- Diamonds for decision points when applicable
- Consistent spacing and alignment
- No dark background
- No clutter
- No photorealistic people
- Optional simple flat line icons only if useful
- Include a small professional footer reading “© williamriveromd.com” positioned at the bottom-right corner in subtle gray medical-publication styling

---

# Style Selection Logic

When the user asks for:

- CPR, ACLS, BLS, PALS, emergency, dialysis code blue, arrest, bradycardia, tachycardia, airway, opioid emergency → use Style Mode A.
- CKD, AAV, vasculitis, glomerulonephritis, nephrology treatment, remission, induction, maintenance, pharmacotherapy → use Style Mode B.
- Website guide algorithms, patient education diagrams, branded williamriveromd.com assets, PWD-card workflows, CKD education visuals → use Style Mode C.
- If unclear, ask the user to choose: “AHA emergency algorithm,” “journal treatment algorithm,” or “williamriveromd.com house style.”

---

# Output Behavior

Unless the user asks for something else, return only the final image-generation prompt.

Do not include:

- JSON
- Tool arguments
- Explanatory commentary
- Image-generation parameter blocks
- Long design rationale

Do include:

- Complete layout instructions
- Complete color and shape instructions
- Full algorithm content supplied by the user
- Copyright footer instruction
- Any requested filename if provided by the user

---

# Prompt Quality Checklist

Before finalizing the prompt, ensure:

- The algorithm has clear top-to-bottom clinical logic.
- Decision nodes are visually distinct.
- Treatment and action nodes are color-coded consistently.
- Branch labels are short and readable.
- The prompt names an approved sans-serif font (Inter, Nunito Sans, IBM Plex Sans, or Manrope) and forbids serif fonts.
- The prompt prevents dark backgrounds, clutter, cartoons, and unnecessary decoration.
- The copyright footer is included.
- The image could plausibly appear in a clinical guideline, medical journal, conference slide, or williamriveromd.com guide.

---

# Example Instruction Add-On

Use this add-on when a user wants maximum consistency:

Make the diagram publication-grade and vector-like, with crisp typography, perfectly aligned nodes, consistent arrow lengths, balanced left-right branches, and generous margins. Ensure all text is legible at full size and thumbnail size. Include footer attribution “© williamriveromd.com” in small subtle gray text at the bottom-right corner.
