---
name: williamriveromd-gpt-image-generator-browser
description: >
  Prepare and deliver ready-to-paste image generation prompts for williamriveromd.com,
  formatted specifically for the ChatGPT Image Generator GPT at
  https://chatgpt.com/g/g-pmuQfob8d-image-generator (browser workflow, no API key).
  Trigger this skill whenever Dr. Rivero says "GPT image: [description]", or whenever
  the williamriveromd-image-planner skill has finished producing a complete IMAGE PLAN
  and prompts are ready for execution. Also trigger when Dr. Rivero says "generate images",
  "prepare prompts", "ready to generate", or any similar confirmation after an image plan
  has been produced. The skill formats each prompt for maximum gpt-image-2 compliance,
  delivers them one at a time with copy-ready output, and tracks which images have been
  generated across the session.
---

# WilliamRiveroMD — GPT Image Generator (Browser Workflow)

Formats and delivers image prompts for the ChatGPT Image Generator GPT:
**https://chatgpt.com/g/g-pmuQfob8d-image-generator**

No API key required. No scripts. Works entirely through the browser.

---

## How This Works

Dr. Rivero uses the ChatGPT Image Generator GPT in a separate browser tab.
This skill prepares one optimized prompt at a time, displays it clearly for copying,
and tracks the queue until all images in the plan are complete.

Pipeline:
  Image Plan (from image planner)
    → This skill formats each prompt
    → Dr. Rivero copies → pastes into ChatGPT Image Generator tab
    → Downloads result → saves with suggested filename
    → Returns here → this skill delivers the next prompt

---

## Step 1 — Announce the Queue

When triggered from an image plan, read all IMAGE blocks and announce:

  Ready to generate [n] images for [Guide Title].

  Open this tab now if you haven't already:
  → https://chatgpt.com/g/g-pmuQfob8d-image-generator

  I'll deliver one prompt at a time. Copy each prompt, paste it into
  ChatGPT Image Generator, download the result, save it with the
  suggested filename, then come back and say "next".

  Rate limit reminder: ChatGPT Image Generator allows ~5 images per
  minute. If you see a slowdown, wait 60 seconds before the next prompt.

  Starting with Image 1 of [n] ▼

---

## Step 2 — Format Each Prompt

For each image, produce a clean, copy-ready prompt block — no markdown
code fences, no numbering noise, no labels that confuse the image model.

Take the 10-point image planner block and collapse it into flowing
prose optimized for gpt-image-2. Do NOT paste the numbered list directly.

Structure of the formatted prompt:

  [CONTEXT LINE]
  [STYLE + SUBJECT sentence]
  [COMPOSITION sentence]
  [BACKGROUND + LIGHTING sentence]
  [COLOR PALETTE sentence with hex values]
  [MEDICAL DETAIL sentence]
  [MOOD + QUALITY sentence]
  [DIMENSION instruction]
  [NEGATIVE PROMPTS sentence]

Context line (always prepend to every prompt):
  Medical education image for williamriveromd.com, a nephrology patient
  education website serving Filipino patients and physicians.

Example — 10-point block converted to formatted prompt:

  INPUT (10-point):
    1. IMAGE TYPE: Hero
    2. PRIMARY VISUAL STYLE: EDITORIAL_PHOTO
    3. SUBJECT: Filipino nephrologist reviewing CKD labs with elderly Filipino patient
    4. COMPOSITION: Two-person, physician standing, patient seated, lab paper visible
    5. BACKGROUND: Clean modern nephrology clinic, muted teal-white walls
    6. LIGHTING: Soft clinical window lighting, warm-neutral
    7. COLOR PALETTE: Navy #1F3864, teal #1a6b72, gold #d4af4f
    8. MEDICAL DETAILS: Printed electrolyte panel, no fake UI screens
    9. MOOD: Calm, trustworthy, reassuring
    10. DIMENSIONS: 1536x1024
    11. NEGATIVE PROMPTS: No cartoon, no AI sharpening, no stock-photo smiles

  OUTPUT (formatted prose for ChatGPT Image Generator):

    Medical education image for williamriveromd.com, a nephrology patient
    education website serving Filipino patients and physicians.

    Photorealistic editorial medical photograph. A Filipino nephrologist in
    a white coat reviews printed CKD laboratory results with an attentive
    elderly Filipino patient in a clean modern nephrology clinic. The
    physician stands slightly angled toward the patient who is seated; a
    printed electrolyte panel is visible but not legible. Soft clinical
    window lighting, warm-neutral balance. Muted teal-white clinic walls,
    minimal distractions, shallow depth of field. Color palette: deep navy
    #1F3864 clothing accents, teal #1a6b72 environment, gold #d4af4f
    highlight details. No fake holographic screens, clinically realistic
    setting. Calm, trustworthy, professionally educational. 1536x1024
    landscape format.

    Avoid: cartoon, anime, AI over-sharpening, exaggerated smiling,
    stock-photo aesthetic, plastic skin, extra fingers, distorted hands,
    fake holograms, neon colors, cyberpunk, visual clutter, dramatic poses.

---

## Step 3 — Deliver Prompt with Session Card

Display each prompt in this format:

  ─────────────────────────────────────────────────────
  IMAGE [n] of [total] — [IMAGE TYPE] — [STYLE]
  Filename to save as: [suggested-filename].png
  Dimensions: [width × height]
  Progress: [■■■□□  3 of 5 complete]
  ─────────────────────────────────────────────────────

  COPY THIS PROMPT ↓
  ══════════════════════════════════════════════════════

  [formatted prose prompt — plain text, ready to select-all and copy]

  ══════════════════════════════════════════════════════

  Paste into → https://chatgpt.com/g/g-pmuQfob8d-image-generator
  Download the result → save as [filename].png
  Say "next" when ready for Image [n+1].

---

## Step 4 — Rate Limit Awareness

The ChatGPT Image Generator GPT enforces ~5 images per minute.

When delivering image #5, append:
  ⏸ Rate limit note: You have reached 5 images. Before pasting the next
  prompt, wait ~60 seconds in the ChatGPT tab.

When delivering image #6 onward, confirm:
  "Did you wait ~60 seconds? If yes, here is Image [n]:"

---

## Step 5 — Completion and File Guidance

After the final image:

  ✓ All [n] images complete for [Guide Title].

  Save your downloaded PNGs here:
    williamriveromd.github.io/images/[filename].png

  Live URL after GitHub push:
    https://www.williamriveromd.com/images/[filename].png

  Reference in guide HTML:
    <img src="/images/[filename].png" alt="[descriptive alt text]">

Suggest alt text based on the image subject from the planner prompt.

---

## Direct Invocation (no image plan)

When triggered with "GPT image: [description]" directly:
1. Ask for image type if unclear (EDITORIAL_PHOTO / MINIMAL_MEDICAL_3D /
   CLINICAL_FLAT_VECTOR / ALGORITHM_FLOWCHART / REFERENCE_PANEL_GRID)
2. Ask for a suggested filename
3. Format a single prose prompt per Step 2 rules
4. Deliver as a single session card (n=1 of 1)

---

## Edge Cases

- Image rejected by ChatGPT: Ask for the rejection message. Rewrite the
  prompt removing likely policy triggers. Deliver a revised card labeled REVISED.

- Dr. Rivero shares a screenshot of the result: Review against original prompt.
  Note palette or accuracy deviations. Offer a refinement prompt if needed.

- Wants to regenerate with changes: Apply the requested modification to the
  original prompt only. Deliver as a REVISED card.

- No image plan in context: Offer to run the image planner first:
  "No image plan found — shall I fetch the guide URL and plan images first?"
