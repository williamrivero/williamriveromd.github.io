---
name: williamriveromd-simple-figure
description: >-
  Produces a single, copy-paste ChatGPT Image Generator prompt for one simple
  figure or algorithm for williamriveromd.com nephrology patient-education guides.
  Use when the user wants ONE focused visual — a single flowchart, comparison
  panel, mechanism diagram, step sequence, or reference table — not a
  multi-panel infographic batch. Faster and lighter than williamriveromd-infographic-skill.
  For a review-article-style biomedical mechanism schematic (organ-level panel →
  magnified functional-unit inset → injury → intervention → benefit flow), defer to
  williamriveromd-biomedical-mechanism-figure instead.
---

# WILLIAM RIVERO MD — SIMPLE FIGURE GENERATOR v1

## PURPOSE

Generate ONE production-ready prompt for a single, self-contained figure or algorithm.

Use this skill when the request is:
- a single clinical algorithm or decision flowchart
- a single side-by-side comparison (normal vs abnormal, before vs after)
- a single step-by-step sequence (3–6 steps, horizontal or vertical)
- a single mechanism illustration (one pathway, one concept)
- a single reference table or quick-look card
- a single circular or loop diagram

Use `williamriveromd-infographic-skill` instead when:
- the user asks for a multi-panel educational poster
- the user wants a batch of images for an entire guide section
- photorealistic editorial heroes or OG cards are needed

Use `williamriveromd-biomedical-mechanism-figure` instead when:
- the request is a **biomedical mechanism / pathophysiology schematic** in the
  scientific review-article style (AJKD/NEJM-figure look)
- the figure needs the signature layout: **organ-level panel → magnified
  functional-unit inset (nephron / glomerulus / tubule / mitochondria / vessel /
  cell) in a dashed box → bottom injury → intervention → benefit summary flow**
- the topic is how a disease damages the kidney at the organ-to-cellular level
  (e.g. diabetic kidney disease, IgA nephropathy, CKD-MBD cascade, EPO axis,
  cardiorenal spiral, tubular acid handling)

Even though this skill can render "a single mechanism illustration (one pathway,
one concept)," that means a *simple* one-pathway diagram. The moment the request
implies multi-scale anatomy or the organ→inset→injury/intervention/benefit
structure, **hand off to `williamriveromd-biomedical-mechanism-figure`** and use
its template rather than producing a generic figure here.

---

## HOUSE STYLE CONSTITUTION (non-negotiable — same as main skill)

### Backgrounds
ALL images use a **light background only**.
- Permitted: white `#ffffff`, off-white `#fafafa`, soft gray `#f3f4f6`, light teal tint `#eef6f7`
- Never permitted: navy, dark navy, charcoal, black, or any dark fill

### Color palette
| Role | Color |
|---|---|
| Canvas background | `#ffffff` or `#fafafa` |
| Card / section fill | `#f3f4f6` or `#eef6f7` |
| Primary navy (text/borders) | `#0f1e2e` |
| Clinical teal (headings, rules) | `#1a6b72` |
| Renal green (positive/safe) | `#1f7a4d` |
| Amber/gold (caution) | `#b8860b` |
| Clinical red (danger/warning) | `#b91c1c` |
| Soft purple (specialist/add-on) | `#6c3d8e` |

### Typography
- **Approved fonts (MANDATORY): use only a clean sans-serif typeface — `Inter`,
  `Nunito Sans`, `IBM Plex Sans`, or `Manrope`. No other fonts, and never a serif
  font.** Name the chosen font explicitly in every generated prompt.
- Bold condensed sans-serif titles in navy `#0f1e2e` on light backgrounds
- Short labels, not paragraph text
- Mobile-readable — minimum 11pt equivalent

### Attribution (MANDATORY on every image)
- Text: `williamriveromd.com`
- Placement: bottom-right corner (landscape/square); bottom-center (portrait)
- Style: small, semi-transparent navy text, ~10–11px, 70% opacity
- Never omit. Never obscure clinical content.

---

## CANONICAL SIZES FOR SIMPLE FIGURES

| Figure type | Dimensions | Ratio |
|---|---|---|
| Single flowchart / algorithm | 1024 × 1536 | 2:3 portrait |
| Horizontal step sequence (≤5 steps) | 1792 × 1024 | 16:9 landscape |
| Side-by-side comparison | 1792 × 1024 | 16:9 landscape |
| Single mechanism / one-panel poster | 1792 × 1024 | 16:9 landscape |
| Square reference card / quick-look | 1024 × 1024 | 1:1 |
| Narrow reference table / 4:3 card | 1536 × 1152 | 4:3 |

Default to **landscape 1792 × 1024** unless the content is clearly a tall algorithm or a compact reference card.

---

## EXECUTION INSTRUCTIONS

When this skill is invoked:

1. **Read the user's request.** Identify:
   - What concept or decision needs to be visualized
   - Audience: patient, clinician, or mixed
   - Preferred figure type (flowchart, comparison, sequence, mechanism, table)
   - Any specific labels, steps, or data to include

2. **Choose the right size** from the canonical table above.

3. **Pick ONE of these prompt scaffolds** and fill it in:

### Scaffold A — Clinical Algorithm / Flowchart (portrait 1024 × 1536)
```
Clinical nephrology algorithm, KDIGO/ADA guideline flowchart aesthetic. Single focused
pathway for [TOPIC]. White (#ffffff) background. Title at top in bold navy (#0f1e2e).
Rounded rectangular nodes — decision nodes in teal (#1a6b72), action nodes in navy,
caution nodes in amber (#b8860b), escalation nodes in red (#b91c1c), optimal-path nodes
in renal green (#1f7a4d). Bold connecting arrows. Maximum 3–4 branching levels.
Generous whitespace. Mobile-readable labels. No spaghetti. Clean left-to-right or
top-to-bottom flow. Bottom-right: "williamriveromd.com" in small semi-transparent navy text.
```

### Scaffold B — Side-by-Side Comparison (landscape 1792 × 1024)
```
Medical education comparison infographic, AJKD/NEJM graphical abstract style.
White (#ffffff) background. Title centered at top in bold navy. Soft dashed vertical
divider splitting the canvas into two equal panels. Left panel labeled in renal green
(#1f7a4d): "[NORMAL/HEALTHY LABEL]". Right panel labeled in clinical red (#b91c1c):
"[ABNORMAL/DISEASE LABEL]". Each panel contains [DESCRIBE CONTENT]. Rounded panel
corners, ample negative space, mobile-readable labels ≥11pt. Bottom-right:
"williamriveromd.com" in small semi-transparent navy text.
```

### Scaffold C — Horizontal Step Sequence (landscape 1792 × 1024)
```
Clean clinical education infographic, white (#ffffff) background. Title at top center
in bold navy (#0f1e2e). [N] rounded rectangular cards arranged horizontally in a single
row, connected by bold navy right-pointing arrows. Each card has a colored top accent
band ([colors per step]), a small icon, a bold step label, and 2–3 bullet details.
Cards sit on a very soft gray panel (#f3f4f6). Generous whitespace. Mobile-readable.
Bottom strip: full-width soft gray, brief summary sentence in navy.
Bottom-right: "williamriveromd.com" in small semi-transparent navy text.
```

### Scaffold D — Single Mechanism / One-Panel Poster (landscape 1792 × 1024)
```
Medical pathophysiology infographic, AJKD/NEJM graphical abstract style. White (#ffffff)
background. Title at top in bold navy (#0f1e2e), subtitle in clinical teal (#1a6b72).
Central semi-photorealistic 3D diagram of [ANATOMY/MECHANISM]. Labeled callouts using
modular rounded cards. Color-coded arrows showing [DIRECTION/FLOW]. Bottom strip with
clinical implication in navy. Ample negative space, no clutter, mobile-readable labels.
Bottom-right: "williamriveromd.com" in small semi-transparent navy text.
```

### Scaffold E — Reference Table / Quick-Look Card (1:1 or 4:3)
```
Clinical reference card, publication-grade nephrology design. White (#ffffff) background.
Bold navy title at top. Compact well-organized table or grid with [N] rows/columns.
Column headers in teal (#1a6b72) on soft gray background (#f3f4f6). Alternating row
fills (white / very soft gray). Key values highlighted in amber or red where clinically
significant. Footer: brief takeaway sentence. Mobile-readable, not cluttered.
Bottom-right: "williamriveromd.com" in small semi-transparent navy text.
```

4. **Expand the scaffold** with the specific clinical content, labels, steps, values, and color assignments relevant to the request.

5. **Output ONE prompt block** in this format — nothing else:

```
FILE NAME: [guide-slug]-[descriptor].png
IMAGE TYPE: [Scaffold name and figure type]
ASPECT RATIO: [ratio]
PIXEL DIMENSIONS: [W × H]
AUDIENCE: [patients / clinicians / mixed]
VISUAL GOAL: [one sentence]

PROMPT:
[filled-in scaffold, fully expanded with clinical specifics]

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text,
avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only.
Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other
fonts, no serif fonts, no decorative or handwritten typefaces.
Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and
consistent with williamriveromd.com house style. Background must be white or soft light
gray — never dark. Copyright attribution williamriveromd.com must be visible in the
bottom-right corner (bottom-center for portrait).
```

---

## SIMPLICITY RULES

- **One concept per image.** If the user's request spans two or more distinct ideas, generate two separate prompt blocks rather than crowding one image.
- **Prefer fewer nodes.** Algorithms: max 8–10 nodes. Step sequences: max 6 steps. Comparisons: 2 panels only.
- **No decorative clutter.** Every element must earn its place by communicating a clinical point.
- **Prefer whitespace over density.** A figure a patient can read in 10 seconds on mobile is better than one that requires zooming.
