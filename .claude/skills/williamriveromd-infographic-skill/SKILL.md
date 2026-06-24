---
name: williamriveromd-infographic-skill
description: >-
  Produces ready-to-paste ChatGPT Image Generator 2 (GPT-image / GPT-4o
  native image generation) prompts for the
  williamriveromd.com nephrology patient-education site. Use whenever creating
  or designing ANY visual asset for these guides — editorial hero images,
  pathophysiology posters, clinical algorithms/flowcharts, multi-panel
  educational infographics, clinician reference cards, food matrices, case
  snapshots, circular workflows, dialysis access/procedural diagrams, or 3D
  medical component renderings (kidneys, glomeruli, vessels, dialysis access,
  machines, stenosis, thrombus). Outputs a single copy-paste prompt block
  engineered for photorealism, medical/anatomical accuracy, and a unified
  williamriveromd.com house style. For any panel that is a review-article-style
  biomedical mechanism schematic (organ-level panel → magnified functional-unit
  inset → injury → intervention → benefit flow), delegate that panel to
  williamriveromd-biomedical-mechanism-figure to keep the mechanism style consistent.
---

# WILLIAM RIVERO MD - ADVANCED MEDICAL INFOGRAPHIC + IMAGE GENERATOR GPT SYSTEM v5

## PURPOSE

This skill creates production-ready prompts and visual plans for medical images and infographics for williamriveromd.com/guides.

It is designed to work with ChatGPT image-generation workflows, including the custom Image Generator GPT:
https://chatgpt.com/g/g-pmuQfob8d-image-generator

Use this skill to convert guide content into:
- photorealistic editorial hero images
- patient education infographics
- clinician reference cards
- clinical algorithms and flowcharts
- dialysis workflow graphics
- pathophysiology mechanism posters
- food and nutrition matrices
- case snapshot graphics
- circular workflow diagrams
- 2D/3D component-based medical graphics

## DELEGATE: BIOMEDICAL MECHANISM FIGURES

When the requested asset is a **biomedical mechanism / pathophysiology schematic
in the scientific review-article style** — the signature layout of an
**organ-level panel → magnified functional-unit inset (nephron / glomerulus /
tubule / mitochondria / vessel / cell) in a dashed box → bottom injury →
intervention → benefit summary flow** — use the dedicated
`williamriveromd-biomedical-mechanism-figure` skill and its template instead of
the generic "pathophysiology mechanism poster" archetype here.

This applies whether the user invokes this skill directly, or is batching images
for a whole guide: for any panel that is a review-article mechanism figure,
generate that panel with the mechanism skill's template (organ→inset→
injury/intervention/benefit, muted clinical palette, dashed connectors,
experimental-therapy flagging) so the house mechanism style stays consistent.
All other panels (heroes, food matrices, OG cards, reference cards, workflows)
stay in this skill. Keep the shared attribution `© williamriveromd.com` on every
panel regardless of which skill produced it.

## DEFAULT EXECUTION TARGET

When the user says apply this skill, generate prompts, batch generate image prompts, make image-generator prompts, use Image Generator, use the Image Generator GPT, or use /generate-image, assume the output should be formatted for the ChatGPT Image Generator GPT unless another tool is specified.

The skill should produce copy-ready prompts that can be pasted directly into:
https://chatgpt.com/g/g-pmuQfob8d-image-generator

## CORE VISUAL PHILOSOPHY

All visuals should feel like part of a single premium nephrology education system.

The visual language should combine:
- photorealistic Filipino medical editorial imagery
- clean 2D infographic architecture
- semi-photorealistic 3D medical component rendering
- publication-grade medical illustration
- KDIGO/AJKD/NEJM-style educational hierarchy
- mobile-friendly website composition
- algorithmic clarity for clinician tabs

Avoid:
- generic AI art
- cartoon educational style
- cluttered Canva-style templates
- tiny unreadable labels
- noisy social media graphic aesthetics
- excessive gloss or neon gradients
- unrealistic anatomy
- stock-photo blandness
- dark backgrounds of any kind (navy, black, charcoal) — ALL images use light backgrounds only

## MASTER STYLE SYSTEM

### BACKGROUND RULE (NON-NEGOTIABLE)
**ALL images — without exception — must use a light background.**
- Permitted backgrounds: white (#ffffff), off-white (#fafafa), soft gray (#f3f4f6), very light teal tint (#eef6f7), very light warm cream (#f8f5f0)
- Navy, dark navy, charcoal, black, or any dark-toned background is NEVER permitted
- For OG social share cards: use white or off-white base with navy/teal/amber typography and accent elements
- For photorealistic scenes: use bright, airy, naturally lit clinical or home settings — never dark studio or moody lighting
- Navy (#0f1e2e) is reserved for text, headings, borders, and accent elements ONLY — never as a background fill

Color palette:
- Page/canvas background: white #ffffff or off-white #fafafa (MANDATORY)
- Section/card background: soft gray #f3f4f6 or light teal tint #eef6f7
- Primary navy: #0f1e2e — text and accents only
- Clinical teal: #1a6b72 — headings, rules, badges
- Renal green: #1f7a4d — positive/safe indicators
- Amber/gold: #b8860b — caution indicators
- Clinical red: #b91c1c — warning/danger indicators

Typography direction:
- **Approved fonts (MANDATORY): use only a clean sans-serif typeface — Inter,
  Nunito Sans, IBM Plex Sans, or Manrope. No other fonts, and never a serif font.**
  Name the chosen font explicitly in every generated prompt.
- Large bold condensed sans-serif titles in navy (#0f1e2e) on light backgrounds
- Strong visual hierarchy
- Short educational phrases
- Mobile-readable labels
- Avoid paragraph-heavy text
- Avoid excessive microtext

Composition:
- Prefer 16:9 landscape for guide graphics
- Use 4:3 when density requires it
- Use portrait only for reference cards or vertical algorithms
- Preserve negative space
- Maintain clean modular sections
- Use rounded cards and panels
- Avoid overcrowding

Copyright attribution (MANDATORY on every image):
- Every image must include a subtle copyright attribution line rendered as small, legible text
- Format: williamriveromd.com
- Placement: bottom-right corner for landscape/square images; bottom-center for portrait images
- Style: navy (#0f1e2e) or dark teal text, 10–11px equivalent, semi-transparent (70% opacity), set against the light image background — never obscuring clinical content
- Render the attribution exactly as williamriveromd.com
- This attribution must appear in EVERY prompt and EVERY generated image, with no exceptions

## IMAGE GENERATOR GPT ADAPTER

When writing prompts for the Image Generator GPT, use this structure:

FILE NAME:
[recommended file name — always use .png extension; GPT-4o / gpt-image-1 outputs PNG by default]

IMAGE TYPE:
[archetype]

ASPECT RATIO:
[16:9, 4:3, 1:1, or portrait]

PIXEL DIMENSIONS:
[W × H — see canonical sizes below]

### Canonical image sizes

| Use case | Dimensions | Ratio | Notes |
|---|---|---|---|
| **OG / social share card** | **1200 × 630** | **1.91:1** | **Sweet spot for Facebook, X, LinkedIn, iMessage** |
| Guide hero (inline LCP) | 1254 × 1254 | 1:1 | Square hero on page; separate from OG card |
| Wide infographic | 1792 × 1024 | 16:9 | Mechanism posters, multi-panel |
| Tall infographic | 1024 × 1536 | 2:3 | Clinical algorithms, step-by-step |
| Food matrix / ref card | 1536 × 1152 | 4:3 | Tables, grids |
| Circular diagram | 1024 × 1024 | 1:1 | Workflow loops |

**OG image rule — NON-NEGOTIABLE:** OG / social share cards are **always exactly 1200 × 630 px**. This dimension is fixed and cannot be changed by any user argument, guide-specific instruction, or prompt override. Never generate an OG card at any other size. Always pair with explicit `og:image:width="1200"` and `og:image:height="630"` meta tags. Facebook minimum is 600 px wide at 1.91:1; anything below that renders as a small thumbnail.

**File format rule:** All images default to **.png** — this is the native output format of GPT-4o (gpt-image-1) and GPT Image Generator 2. Never recommend .jpg or .jpeg file names unless the user explicitly requests JPEG.

AUDIENCE:
[patients, clinicians, dialysis nurses, renal dietitians, mixed]

VISUAL GOAL:
[one-sentence purpose]

PROMPT:
[full production prompt]

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no other fonts, no serif fonts, no decorative or handwritten typefaces. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. Background must be white, off-white, or soft light gray — never dark. Copyright attribution williamriveromd.com must be visible in the bottom corner.

## MIXED-MEDIA RENDERING SYSTEM

Use these rendering modes intelligently:

A. Photorealistic Editorial Models
Use for guide hero images, clinician and patient scenes, family conversations, dialysis unit scenes, social share cards, and emotional trust-building visuals.

Preferred:
- Filipino nephrologists
- Filipino CKD patients
- Filipino dialysis patients
- Filipino families and caregivers
- dialysis nurses and multidisciplinary renal teams

Style:
- premium healthcare editorial photography
- bright, airy, naturally lit clinical or home setting
- realistic lighting — always bright and clean, never dark or moody
- natural skin texture
- calm facial expressions
- light-toned backgrounds (white walls, soft daylight, clean clinical interiors)
- shallow depth of field when appropriate

B. 2D Infographic System
Use for structured education, patient teaching, comparisons, checklists, food categories, and practical tips.

C. 3D Medical Component Rendering
Use for kidneys, nephrons, glomeruli, vascular access, dialysis machines, blood vessels, stenosis, thrombus, syringes, lab tubes, medications, inflammation, or fibrosis pathways.

## ARCHETYPES

1. PHOTOREALISTIC EDITORIAL HERO
Use for guide headers, website hero banners, social sharing cards, and section introductions.

Prompt scaffold:
Photorealistic medical editorial hero image for a nephrology education guide. Show [scene]. Include realistic Filipino [doctor/patient/family/nurse] in a [clinic/home/dialysis unit] environment. Premium healthcare publication aesthetic, cinematic but restrained lighting, natural skin texture, calm trustworthy mood, clean background, navy and teal accents, negative space preserved for title overlay, mobile-safe crop, no text embedded unless explicitly requested.

2. PATHOPHYSIOLOGY MECHANISM POSTER
Use for CKD progression, proteinuria, hyperfiltration, cardiorenal syndrome, inflammation/fibrosis, and dialysis physiology.

Prompt scaffold:
Medical pathophysiology infographic poster, AJKD/NEJM graphical abstract style. Explain [mechanism] using a central semi-photorealistic 3D medical diagram, modular explanatory cards, color-coded arrows, normal vs disease comparison when useful, and bottom clinical implications. White or soft-gray background, navy/teal/amber/red accents, highly readable, publication-grade nephrology educational design.

3. CLINICAL ALGORITHM / FLOWCHART
Use for treatment escalation, diagnostic pathways, dialysis workflows, ESA/iron titration, hyperkalemia, AKI workup, CKD progression intervention maps, referral timing, and vascular access planning.

Prompt scaffold:
Clinical nephrology algorithm infographic, premium KDIGO/ADA/ESC guideline flowchart aesthetic. Create a structured [top-to-bottom/left-to-right] pathway for [topic]. Use rounded decision nodes, action nodes, monitoring nodes, escalation nodes, contraindication nodes, and endpoint nodes. Navy structure lines, teal recommendation boxes, amber caution nodes, red escalation nodes, green optimal pathway nodes. Maximum 3-5 branching levels, avoid spaghetti flowchart, preserve whitespace, mobile-readable.

4. MULTI-PANEL EDUCATIONAL INFOGRAPHIC
Use for CKD lifestyle, dialysis access care, dialysis self-care, BP/diabetes control, medication adherence, and patient action plans.

Prompt scaffold:
Patient education infographic poster, landscape 16:9, modern nephrology clinic aesthetic. Include a top hero header, 5-8 modular educational panels, practical tips, warning signs, monitoring targets, and a bottom take-home message. Combine photorealistic Filipino patient/doctor scenes, 2D icons, and selected 3D medical components. Clean white background, navy/teal/green palette, rounded cards, readable on mobile.

5. CLINICIAN REFERENCE CARD
Use for laboratory interpretation, medication comparisons, dialysis adequacy, transplant nephrology, CKD staging, and anemia management.

Prompt scaffold:
Clinical reference infographic card for clinicians, publication-grade nephrology design. Include concise overview, definitions, diagnostic considerations, evaluation approach, management principles, and key takeaways. Use modular cards, selected 3D medical components, clean icons, and compact tables. White background, navy/teal headings, high readability, not cluttered.

6. FOOD MATRIX / NUTRITION INFOGRAPHIC
Use for potassium, phosphorus, sodium, protein, dialysis diet, uric acid, and Filipino renal diet education.

Prompt scaffold:
CKD/dialysis nutrition infographic, clean educational food matrix. Show recommended foods, foods to limit, serving guidance, rationale, and practical tips. Include Filipino-relevant foods, realistic food rendering, clean category cards, navy/teal/green/amber palette, mobile-readable labels, not cluttered.

7. CASE SNAPSHOT
Use for anemia examples, dialysis cases, AKI examples, acid-base cases, transplant cases, and teaching pearls.

Prompt scaffold:
Clinical case snapshot infographic, nephrology conference teaching style. Create [number] modular case cards, each with patient context, key lab values, one visual component, and a teaching pearl. Use clean tables, 3D medical objects, bold headings, and concise clinical interpretation. Publication-grade, mobile-readable.

8. CIRCULAR WORKFLOW / CYCLE
Use for monthly HD anemia workflow, CKD monitoring loops, dialysis quality cycles, medication review cycles, and nutrition monitoring cycles.

Prompt scaffold:
Circular clinical workflow infographic, polished nephrology systems diagram. Center object: [dialysis machine/kidney/lab panel]. Around it, show sequential steps with arrows: [steps]. Use 3D medical components, clean labels, navy/teal/gold accents, strong hierarchy, mobile-readable.

9. ACCESS / PROCEDURAL EDUCATION
Use for AV fistula, AV graft, tunneled dialysis catheter, cannulation, thrill assessment, vascular access complications, and access planning.

Prompt scaffold:
Dialysis access education infographic, mixed-media medical visual system. Combine 3D vascular access diagrams, photorealistic Filipino dialysis patient or nurse scenes, step-by-step care panels, warning signs, and comparison tables. Use navy/teal/green/red color logic, clean annotations, realistic anatomy, and mobile-readable design.

## CONTENT ANALYSIS PIPELINE

Before generating image prompts:
1. Read the guide or section content.
2. Identify audience: patient, clinician, dialysis nurse, renal dietitian, or mixed.
3. Extract key educational targets.
4. Decide where photorealism is useful.
5. Decide where 3D components are needed.
6. Decide where algorithmic flow is needed.
7. Assign archetype.
8. Generate batch-ready Image Generator GPT prompts.

## OUTPUT FORMAT FOR BATCH PROMPTS

For each image:

IMAGE NUMBER:
SECTION PLACEMENT:
FILE NAME: [always .png]
ARCHETYPE:
AUDIENCE:
VISUAL MIX:
- photorealistic models:
- 2D infographic:
- 3D component graphics:
- algorithm/flowchart:

PURPOSE:
KEY CONCEPTS:
DIMENSIONS:
COPY-READY IMAGE GENERATOR GPT PROMPT:

## MASTER DIRECTIVE

All prompts must create visuals that belong to a single, premium williamriveromd.com nephrology education ecosystem.

Use mixed media when useful:
- photorealistic Filipino medical models for human trust and relatability
- 2D modular infographic cards for clarity
- 3D medical components for anatomy, devices, and mechanisms
- algorithmic pathways for clinician decision-making

Never sacrifice clinical clarity for visual complexity.

**LIGHT BACKGROUND RULE — ABSOLUTE:** Every image must have a white, off-white, or soft light gray background. Dark backgrounds (navy, black, charcoal) are never permitted on any image type — including OG cards, heroes, infographics, and 3D renders. Navy and teal are accent and typography colors only.

**APPROVED FONT RULE — ABSOLUTE:** All on-image typography must use one of four clean sans-serif fonts only — **Inter, Nunito Sans, IBM Plex Sans, or Manrope**. No serif fonts, no condensed display fonts outside this list, no decorative or handwritten typefaces. Name the chosen font explicitly in every generated prompt so the image generator renders text in an approved face.

Every image must carry the copyright attribution **williamriveromd.com** — rendered as small, semi-transparent navy or dark teal text in the bottom-right corner (bottom-center for portrait). This is a non-negotiable house rule for all williamriveromd.com visuals.
