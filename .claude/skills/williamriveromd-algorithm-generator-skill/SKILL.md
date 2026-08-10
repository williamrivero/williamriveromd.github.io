---
name: williamriveromd-algorithm-generator-skill
description: Generate image-generation prompts for clean clinical algorithm flowcharts resembling AHA-style resuscitation algorithms and journal-style nephrology treatment algorithms, with renalcarematters.com copyright attribution.
---

# williamriveromd Algorithm Generator Skill

## Purpose

Generate high-quality image-generation prompts that produce polished, elegant
clinical algorithm diagrams with the visual logic, spacing, hierarchy, and finish
of:

1. AHA-style emergency care algorithms
2. Journal-style medical and nephrology treatment algorithms
3. renalcarematters.com branded house-style education algorithms

The output should usually be a complete image-generation prompt, not the algorithm
itself, unless the user explicitly asks for the algorithm content.

The bar is *publication-grade and beautiful* — a figure that could sit on the
cover of a guideline supplement or a premium medical app: restrained, confident,
and visually calm, never busy, garish, or clip-art-like.

---

## Aesthetic Foundation (shared design system — inherited by every mode)

**Always embed these design tokens in every prompt, regardless of mode.** They are
what separate a polished, modern figure from a generic flowchart. Adapt only the
palette per mode; keep the geometry, depth, typography scale, and spacing constant.

### Canvas & grid
- White or very light cool-neutral background (`#FCFCFB` / `#FAFBFC`), never pure
  clinical gray and never a tint that competes with the nodes.
- Generous, breathing margins — at least 7–8% of the canvas on every edge.
- An invisible column grid: nodes snap to shared centerlines and column widths so
  every tier lines up. Equal vertical rhythm between rows; equal gutters between
  side branches. Alignment is the single biggest driver of "expensive" feel.

### Nodes
- Soft, consistent corner radius (roughly 14–18 px feel) on every rounded box —
  identical across the whole figure.
- **Two-tone fills:** a soft, low-saturation tinted fill paired with a slightly
  deeper 1.5 px hairline border in the *same hue family* (e.g. pale mint fill with
  a muted green border). This tint-plus-hairline treatment reads as modern and
  premium; flat saturated blocks read as cheap.
- **One subtle soft shadow** per node — low opacity (~8–12%), small blur, tiny
  downward offset — for gentle depth. Never harsh, never multiple, never a hard
  drop shadow.
- Consistent node width within each tier; comfortable, even internal padding so
  text never touches the border.
- Optional small **uppercase eyebrow tag** (tracked, ~10–11 px, muted) at the top
  of key nodes to label phase/tier ("ASSESS", "DECIDE", "TREAT", "MAINTAIN").

### Connectors
- Thin (1.5–2 px) connectors in a muted accent color drawn from the palette —
  **never pure black.** Choose one routing style and keep it consistent: clean
  orthogonal elbows with rounded corners, *or* gentle smooth curves — not both.
- Small, refined arrowheads — slim, not oversized triangles.
- Even arrow lengths; connectors meet node edges squarely at their centers.

### Typography
- Approved sans-serif only (see Mandatory Typeface). House default: titles in
  **Inter Tight**, body/node text in **Manrope**; at most two approved families
  per figure.
- A real type scale, not one size everywhere:
  - **Title** — bold, largest.
  - **Optional subtitle** — regular, muted, ~55–60% of title size.
  - **Eyebrow / tier tag** — uppercase, letter-spaced, small, muted.
  - **Node heading** — semibold.
  - **Node body / bullets** — regular, comfortable line-height.
  - **Branch labels** — medium weight, short.
- Body and structural text in a soft near-navy (`#1a2535` / `#0f1e2e`), never pure
  `#000000`. Keep line-height open; never cram text edge-to-edge.

### Color discipline
- A cohesive, cool, desaturated "modern-medical" palette — soft, sophisticated
  tones (emerald, indigo-blue, teal, amber, rose over cool neutrals),
  **never neon, candy, or fully saturated primaries.**
- Cap the palette at ~4–5 hues, each mapped to a consistent semantic role. Repeat
  roles by color so a reader learns the key at a glance.
- Allow the background to stay quiet; let the nodes carry the color.

### Overall finish
- Optional slim **header band** or rule under the title/subtitle to anchor the top.
- Optional compact **legend row** of small color-key chips (bottom-left) when the
  color coding benefits from a key.
- Balanced negative space; nothing crowds the edges; the composition reads as calm
  and deliberate. Crisp, flat vector rendering — no gradients-as-decoration, no
  textures, no 3D bevels.

### Universal exclusions (state these in every prompt)
- No photorealistic people, no cartoon or clip-art styling, no stock icons.
- No dark background, no heavy or multiple shadows, no glow, no 3D.
- No decorative clutter, no watermark tiling, no faux "AI shimmer" gradients.

---

## Mandatory Copyright Attribution

Every generated algorithm image must include a discreet but visible copyright
attribution.

Text:

© renalcarematters.com

Placement:

- Bottom-right corner preferred
- Centered footer acceptable if the layout requires it
- Never inside a flowchart node
- Never overlapping arrows, branches, or captions
- Maintain adequate page-edge margin
- Must remain visible after typical web/social cropping

Typography:

- Small sans-serif font (one of the approved faces)
- Medium gray, approximately #6b7280 to #8a8a8a
- Professional and unobtrusive
- Readable at publication resolution
- Watermark opacity should not be lower than 70%

Default instruction to append to every image prompt:

Include a small professional footer reading “© renalcarematters.com” positioned at the bottom-right corner in subtle gray medical-publication styling.

---

## Mandatory Typeface

Every generated algorithm prompt must specify a clean, modern sans-serif font, and
may use **only** one of these approved faces. Prefer the primary set; the alternates
are acceptable when a slightly different tone is wanted.

**Primary (default — modern editorial medical):**

- Inter Tight — display / titles (tight, confident, contemporary)
- Manrope — body, UI, and node text (geometric humanist, highly legible)
- IBM Plex Sans — technical/reference figures and dense data nodes

**Approved alternates:**

- Inter (when Inter Tight is unavailable)
- Public Sans (clean, neutral, government-grade legibility)
- Nunito Sans (softer, warmer, patient-facing tone)

**Recommended pairing:** set titles/eyebrow tags in **Inter Tight** and node/body
text in **Manrope** for the most polished result — this is the house default.
A single-family figure is also fine (e.g. all Inter Tight, or all Manrope), driving
hierarchy through weight and size.

Never use a serif font, a condensed display font outside this list, or any
decorative or handwritten typeface. Name the chosen approved font(s) explicitly
inside every image prompt (e.g. “titles in Inter Tight, body text in Manrope”).
Do not mix more than two approved families in one figure.

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

## Refined palette (cool contemporary medical — fill / hairline border)

- **Safety / monitoring / supportive** (emerald): fill `#E4F1EA`, border `#4E9E77`
- **Assessment / activation** (amber): fill `#F7EEDA`, border `#C79A3A`
- **Decision** (rose diamond): fill `#FBE6E7`, border `#D06B73`
- **Active treatment — CPR / shock / drugs** (indigo-blue): fill `#E8ECFA`, border `#6B84C9`
- **Transitional / timing capsule** (cool slate): fill `#EEF1F5`, border `#B7C0CD`
- **Urgent branch labels:** deep crimson `#C2413B`, medium/bold, short
- **Connectors:** muted slate `#64707F`, not black
- Text: near-navy `#16202E`

## Visual Rules

- Portrait orientation, preferably 4:5, 3:4, or 8.5 × 11
- Title top-left or top-center in bold sans-serif, with an optional muted subtitle
  and a slim divider rule beneath the header
- Main pathway runs vertically down a strong center spine, snapped to one centerline
- Rounded rectangles (soft radius) for actions; rose diamonds for decisions;
  slate capsules for transitional/timing steps
- Two-tone tinted fills + hairline borders + one subtle soft shadow per node
- Short red branch labels beside arrows for urgent clinical states
- Optional dashed horizontal divider separating early assessment from the
  resuscitation phase
- Balanced side branches left and right with clean return arrows
- Short bullet lists only when needed; never dense paragraphs
- Optional compact legend row of color-key chips at the bottom-left

## Prompt Template

Create a polished, publication-grade medical algorithm flowchart in the refined style of an American Heart Association provider algorithm. Use a very light cool-neutral background (#FCFCFB), clean modern sans-serif typography — titles and eyebrow tags in Inter Tight, node and body text in Manrope (never a serif font) — and a calm, modern, uncluttered composition with generous margins (≥7–8% on every edge).

Design system:
- Rounded rectangles with a soft, consistent corner radius for action/process steps; rose diamonds for decision questions; slate-gray capsules for transitional or timing steps
- Two-tone nodes: a soft low-saturation tinted fill paired with a 1.5 px hairline border in the same hue family, plus a single very subtle soft drop shadow (low opacity, small blur) for gentle depth — never harsh
- A real type scale: bold title, optional muted subtitle, small uppercase tracked eyebrow tags on key nodes (ASSESS / DECIDE / TREAT), semibold node headings, regular body; near-navy text (#16202E), never pure black
- Thin (1.5–2 px) connectors in muted slate (#64707F), consistent routing with small refined arrowheads — never thick black arrows
- Strict alignment on a shared column grid, a strong central spine, equal vertical rhythm, and balanced left-right branches

Muted color roles (fill / hairline border):
- Emerald #E4F1EA / #4E9E77 for safety, monitoring, or supportive care
- Amber #F7EEDA / #C79A3A for initial assessment and activation steps
- Rose #FBE6E7 / #D06B73 for decision diamonds
- Indigo-blue #E8ECFA / #6B84C9 for active treatment (CPR, shock, drugs)
- Cool slate #EEF1F5 / #B7C0CD for transitional equipment or timing capsules
- Deep crimson #C2413B for short bold branch labels beside arrows
- An optional dashed horizontal divider may separate assessment from intervention

Content to render:
[INSERT ALGORITHM CONTENT HERE]

Design requirements:
- Bold title at top with a slim divider rule; optional compact color-key legend row at bottom-left
- Only short, readable text inside nodes; no dense paragraphs
- No photos, no photorealistic people, no cartoon or clip-art, no 3D, no dark background, no heavy or multiple shadows, no decorative clutter
- Crisp flat vector rendering, guideline-grade clarity, legible at both full size and thumbnail
- Include a small professional footer reading “© renalcarematters.com” positioned at the bottom-right corner in subtle gray medical-publication styling

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

## Refined palette (cool journal tones — fill / hairline border)

- **Diagnosis / disease category / severity** (warm stone): fill `#F1ECE1`, border `#C6B79A`
- **Assessment phase / treatment stage** (cool blue): fill `#E8EDF6`, border `#8AA6CC`
- **Therapy / maintenance / disease control / remission** (sage green): fill `#E4F1EA`, border `#6BA588`
- **Connectors:** muted teal `#4C8B8D`
- Text: near-black slate `#1B2733`

## Visual Rules

- White background; portrait or square layout
- Restrained, minimal, symmetrical — the look of a modern nephrology review figure
- Top-down treatment trunk with balanced left-right branching from the center
- Two-tone tinted fills + hairline borders + one whisper-soft shadow; consistent
  soft corner radius and consistent node widths per tier
- Thin muted teal arrows with small refined arrowheads
- Minimal text per node; no bullet-heavy boxes
- Optional small uppercase tier tags (DIAGNOSE / STAGE / TREAT / MAINTAIN)
- Figure-caption-compatible, generous margins, calm negative space

## Prompt Template

Create a clean, elegant academic medical journal treatment algorithm flowchart on a white background. It should read as a modern, minimal, publication-ready nephrology review figure: symmetrical, calm, and refined, with generous margins (≥7–8% on every edge). Set titles and tier tags in Inter Tight and node/body text in Manrope (never a serif font).

Design system:
- Rounded rectangles with a soft, consistent corner radius and consistent node widths per tier
- Two-tone nodes: a soft low-saturation tinted fill with a 1.5 px hairline border in the same hue family, plus a single whisper-soft drop shadow for subtle depth — never heavy
- A real type scale: bold title, optional muted subtitle, small uppercase tracked tier tags (DIAGNOSE / STAGE / TREAT / MAINTAIN), semibold node headings, regular body; near-black slate text (#1B2733), never pure black; titles in Inter Tight and body text in Manrope (never a serif font)
- Thin muted teal connectors (#4C8B8D) with small refined arrowheads; a top-down central trunk with balanced, symmetrical left-right branching snapped to a shared column grid

Cool journal color roles (fill / hairline border):
- Warm stone #F1ECE1 / #C6B79A for diagnosis, disease category, or severity classification
- Cool blue #E8EDF6 / #8AA6CC for assessment phases or treatment stages
- Sage green #E4F1EA / #6BA588 for therapeutic options, maintenance, disease control, and remission outcomes

Content to render:
[INSERT ALGORITHM CONTENT HERE]

Design requirements:
- Keep all text concise; preserve clinical hierarchy; centered, symmetrical alignment
- Wide margins, calm negative space, no clutter
- No icons unless clinically necessary, no photos, no photorealistic people, no cartoon, no 3D, no dark background, no heavy shadows
- Crisp flat vector rendering that looks like a real medical-journal figure, legible at full size and thumbnail
- Add a small caption area only if requested
- Include a small professional footer reading “© renalcarematters.com” positioned at the bottom-right corner in subtle gray medical-publication styling

---

# Style Mode C: renalcarematters.com House-Style Clinical Algorithm

## Use Cases

Use this style when the user wants a more branded, modern, visually polished
algorithm for renalcarematters.com guides (patient- or clinician-facing).

## Refined palette (brand tokens — text / accent, and soft fill)

- **Navy** `#0f1e2e` — title, body text, structural emphasis
- **Teal** `#1a6b72` — decision nodes and connector accents; soft fill `#E2EFF0`
- **Green** `#1f7a4d` — final recommended actions / qualifying endpoints; soft fill `#E4F1EA`
- **Amber** `#b8860b` — caution or conditional nodes; soft fill `#F7EEDA`
- **Soft slate** `#64707F` — side notes, exclusions, reminders; soft fill `#EEF1F5`
- Background: bright white / very light off-white `#FCFCFB`

## Visual Rules

- Centered, symmetric layout with strong negative space and a premium, branded feel
- Two-tone tinted fills + hairline borders in the same hue + one subtle soft
  shadow; soft consistent corner radius throughout
- Optional slim navy header band or rule beneath a title + subtitle
- Thin teal connector arrows with small refined arrowheads
- Rounded rectangles for actions/endpoints; diamonds for decisions
- Optional simple flat medical line icons only if clinically relevant; icons must
  not touch node borders and must stay monoline in a palette color
- Optional compact legend row of brand-color chips at the bottom-left
- Publication-ready flat vector look; no heavy 3D

## Prompt Template

Create a clean, premium, publication-ready clinical algorithm flowchart in the renalcarematters.com house style. Use a bright white / very light off-white background (#FCFCFB), restrained navy-and-teal typography — titles and eyebrow tags in Inter Tight, node and body text in Manrope (never a serif font) — thin teal connector arrows, and generous margins (≥7–8% on every edge). The composition should be centered, symmetrical, calm, and modern — suitable for a patient-facing or clinician-facing nephrology education guide.

Design system:
- Optional slim navy header band or divider rule beneath a clear title and subtitle
- Rounded rectangles with a soft consistent corner radius for actions/endpoints; diamonds for decision points
- Two-tone nodes: a soft brand-tinted fill with a 1.5 px hairline border in the same hue, plus a single subtle soft drop shadow for gentle depth — never heavy
- A real type scale: bold navy title, muted subtitle, small uppercase tracked tier tags, semibold node headings, regular body; text in navy #0f1e2e, never pure black
- Thin teal (#1a6b72) connectors with small refined arrowheads; strict alignment on a shared column grid with balanced, symmetrical branching

Brand color roles (text/accent · soft fill):
- Navy #0f1e2e for title, body text, and structural emphasis
- Teal #1a6b72 · fill #E2EFF0 for decision nodes and connector accents
- Green #1f7a4d · fill #E4F1EA for final recommended actions or qualifying endpoints
- Amber #b8860b · fill #F7EEDA for caution or conditional nodes
- Soft slate #64707F · fill #EEF1F5 for explanatory side notes and exclusions

Content to render:
[INSERT ALGORITHM CONTENT HERE]

Design requirements:
- Clear title and optional subtitle; optional compact brand-color legend row at bottom-left
- Top-to-bottom clinical logic, consistent spacing and alignment
- Optional simple flat monoline medical icons only if genuinely useful; icons must not touch node borders
- No dark background, no clutter, no photorealistic people, no cartoon, no 3D, no heavy or multiple shadows
- Crisp flat vector rendering, legible at full size and thumbnail
- Include a small professional footer reading “© renalcarematters.com” positioned at the bottom-right corner in subtle gray medical-publication styling

---

# Style Selection Logic

When the user asks for:

- CPR, ACLS, BLS, PALS, emergency, dialysis code blue, arrest, bradycardia, tachycardia, airway, opioid emergency → use Style Mode A.
- CKD, AAV, vasculitis, glomerulonephritis, nephrology treatment, remission, induction, maintenance, pharmacotherapy → use Style Mode B.
- Website guide algorithms, patient education diagrams, branded renalcarematters.com assets, PWD-card workflows, CKD education visuals → use Style Mode C.
- If unclear, ask the user to choose: “AHA emergency algorithm,” “journal treatment algorithm,” or “renalcarematters.com house style.”

Whichever mode is chosen, always fold in the shared **Aesthetic Foundation** tokens
(grid alignment, two-tone nodes, subtle shadow, type scale, refined connectors,
generous margins) so the result is elegant and cohesive, not just correct.

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
- Complete color and shape instructions (with the mode's hex tokens)
- The shared aesthetic-foundation cues (grid, two-tone nodes, subtle shadow, type scale, refined connectors, margins)
- Full algorithm content supplied by the user
- Copyright footer instruction
- Any requested filename if provided by the user

---

# Prompt Quality Checklist

Before finalizing the prompt, ensure:

- The algorithm has clear top-to-bottom clinical logic.
- Decision nodes are visually distinct.
- Treatment and action nodes are color-coded consistently by semantic role, using the mode's muted palette (soft tinted fill + same-hue hairline border).
- Nodes share a consistent soft corner radius, sit on a common column grid, and carry one subtle soft shadow (never heavy).
- Connectors are thin, muted (not black), evenly routed, with small refined arrowheads.
- Typography uses a real scale (title / subtitle / eyebrow tag / heading / body) in near-navy, not pure black.
- Branch labels are short and readable.
- Margins are generous and the composition reads as calm and deliberate, not crowded.
- The prompt names an approved sans-serif font (Inter, Nunito Sans, IBM Plex Sans, or Manrope) and forbids serif fonts.
- The prompt prevents dark backgrounds, clutter, cartoons, 3D, heavy shadows, and unnecessary decoration.
- The copyright footer is included.
- The image could plausibly appear in a clinical guideline, a modern medical journal, a premium conference slide, or a renalcarematters.com guide — and look genuinely handsome doing so.

---

# Example Instruction Add-On

Use this add-on when a user wants maximum consistency and polish:

Make the diagram publication-grade and vector-like, with crisp typography, perfectly aligned nodes on a shared column grid, two-tone nodes (soft tinted fill + same-hue 1.5 px hairline border) each with a single subtle soft shadow, consistent soft corner radii, thin muted connectors with small refined arrowheads, consistent arrow lengths, balanced left-right branches, and generous margins. Keep the palette restrained and muted (no neon or candy tones). Ensure all text is legible at full size and thumbnail size. Include footer attribution “© renalcarematters.com” in small subtle gray text at the bottom-right corner.
