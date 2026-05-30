# Image Generation — fiber-patient-education
## Guide: By the way, Fiber Is Not the Same as Vegetables
## URL: https://www.williamriveromd.com/guides/fiber-patient-education

---

## How to generate

1. Open the Image Generator GPT: https://chatgpt.com/g/g-pmuQfob8d-image-generator
2. Copy the **COPY-READY IMAGE GENERATOR GPT PROMPT** from each prompt file below
3. Paste into the GPT and generate
4. Save the output to `generated-images/[filename]` as listed below
5. Upload the generated images to the Claude Code session to wire them into the guide

---

## Image roster (8 images)

### 001 — Hero Image
- **File:** `fiber-patient-education-hero-market.png`
- **Prompt file:** `image-prompts/001-hero-market.md`
- **Archetype:** Photorealistic Editorial Hero
- **Dimensions:** 1024 × 1024 px (square — OG image)
- **Save to:** `generated-images/fiber-patient-education-hero-market.png`
- **Purpose:** Hero section LCP image + OG image for social sharing
- **Is OG image:** YES

---

### 002 — The Three Jobs of Fiber
- **File:** `fiber-patient-education-three-jobs-infographic.png`
- **Prompt file:** `image-prompts/002-three-jobs-mechanism.md`
- **Archetype:** Pathophysiology Mechanism Poster
- **Dimensions:** 1792 × 1024 px
- **Save to:** `generated-images/fiber-patient-education-three-jobs-infographic.png`
- **Purpose:** Section 2 — shows bulk/transit, gel/cholesterol, and fermentation/SCFA in one poster

---

### 003 — Fiber ≠ Vegetables
- **File:** `fiber-patient-education-fiber-vs-vegetables-infographic.png`
- **Prompt file:** `image-prompts/003-fiber-vs-vegetables.md`
- **Archetype:** Multi-panel Educational
- **Dimensions:** 1792 × 1024 px
- **Save to:** `generated-images/fiber-patient-education-fiber-vs-vegetables-infographic.png`
- **Purpose:** Section 3 — the central myth-bust: big salad (2g) vs ½ cup monggo (8g)

---

### 004 — Soluble vs Insoluble Fiber
- **File:** `fiber-patient-education-two-types-infographic.png`
- **Prompt file:** `image-prompts/004-two-types.md`
- **Archetype:** Multi-panel Educational
- **Dimensions:** 1792 × 1024 px
- **Save to:** `generated-images/fiber-patient-education-two-types-infographic.png`
- **Purpose:** Section 4 — split panel showing where each type acts and Filipino food sources

---

### 005 — Cholesterol-Lowering Mechanism (Circular)
- **File:** `fiber-patient-education-cholesterol-mechanism-infographic.png`
- **Prompt file:** `image-prompts/005-cholesterol-mechanism.md`
- **Archetype:** Circular Workflow
- **Dimensions:** 1024 × 1024 px
- **Save to:** `generated-images/fiber-patient-education-cholesterol-mechanism-infographic.png`
- **Purpose:** Section 5 — 4-step bile acid trap cycle → LDL drops

---

### 006 — Filipino Food Matrix
- **File:** `fiber-patient-education-filipino-food-matrix-infographic.png`
- **Prompt file:** `image-prompts/006-filipino-food-matrix.md`
- **Archetype:** Food Matrix
- **Dimensions:** 1536 × 1152 px
- **Save to:** `generated-images/fiber-patient-education-filipino-food-matrix-infographic.png`
- **Purpose:** Section 6 — color-coded grid of 20 Filipino foods ranked by fiber; patient photo-and-keep reference

---

### 007 — Daily Fiber Target Builder
- **File:** `fiber-patient-education-daily-target-infographic.png`
- **Prompt file:** `image-prompts/007-daily-target.md`
- **Archetype:** Clinical Algorithm
- **Dimensions:** 1024 × 1536 px
- **Save to:** `generated-images/fiber-patient-education-daily-target-infographic.png`
- **Purpose:** Section 7 — step-by-step Filipino meal day hitting 25–38g target with running gram total

---

### 008 — Special Situations Reference Card
- **File:** `fiber-patient-education-special-situations-infographic.png`
- **Prompt file:** `image-prompts/008-special-situations.md`
- **Archetype:** Compact Reference Card
- **Dimensions:** 1536 × 1152 px
- **Save to:** `generated-images/fiber-patient-education-special-situations-infographic.png`
- **Purpose:** Section 8 — one-card clinical reference for CKD, diabetes, gout, diverticulosis, kidney stones

---

## After generating

Upload images to this Claude Code session. The session will:
1. Convert to `.webp` pairs
2. Place in `/images/` in the repo
3. Wire each image into the correct section of the guide HTML
4. Append OG image meta tags (`og:image`, `og:image:width`, `og:image:height`, `og:image:alt`)
5. Commit and push to `main`

---

## OG image (primary)
The hero image (001) will be used as the Open Graph image:
```html
<meta property="og:image" content="https://www.williamriveromd.com/images/fiber-patient-education-hero-market.webp"/>
<meta property="og:image:width" content="1024"/>
<meta property="og:image:height" content="1024"/>
<meta property="og:image:alt" content="By the way, Fiber Is Not the Same as Vegetables — williamriveromd.com"/>
```
