# Organ & Kidney Donation in the Philippines — Supplemental Image Pack
Guide: `guides/organ-donation-philippines.html`
Generated: 2026-06-11 · williamriveromd-infographic-skill v5
Generator: https://chatgpt.com/g/g-pmuQfob8d-image-generator

Image audit summary: the Organ Donation tab currently carries only ONE image
(`organ-donation-ph-overview.png`, in #what-organs) across seven sections; the
Kidney Donation tab has three (`kd-01`–`kd-03`). The five prompts below fill the
visual gaps: the new #not-for-sale section, #myths, #how-to, #family, and a
dedicated 1200×630 OG social share card (the page currently borrows the inline
1536×1024 overview infographic for og:image). After generating, place each
inline image with a `<picture>` block (webp + png), `loading="lazy"`, explicit
width/height, and run
`patch_hero_maxwidth.py --guide organ-donation-philippines.html`.
For Image 5 (OG card), instead update the guide's `<head>`:
`og:image` / `twitter:image` → `https://www.williamriveromd.com/images/organ-donation-ph-og.png`,
`og:image:width="1200"`, `og:image:height="630"`, and refresh `og:image:alt`.

---

IMAGE NUMBER: 1
SECTION PLACEMENT: `#not-for-sale` — after the intro paragraph, before the red alert
FILE NAME: organ-donation-ph-od-04-not-for-sale.png
ARCHETYPE: Photorealistic editorial hero (conceptual, mixed-media)
AUDIENCE: patients, general public (meme-aware younger Filipinos)
VISUAL MIX:
- photorealistic models: young Filipino adult with smartphone
- 2D infographic: subtle "NOT FOR SALE" typographic element
- 3D component graphics: semi-photorealistic 3D kidney
- algorithm/flowchart: none

PURPOSE: Anchor the "I'll sell my kidney for concert tickets" section — visually separate the viral joke from the trafficking reality without sensationalism.
KEY CONCEPTS: kidney is not currency; organ selling is illegal (R.A. 7170, R.A. 9208/10364); the meme vs the reality.
DIMENSIONS: 1792 × 1024 (16:9)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Photorealistic medical editorial image for a nephrology education guide, conceptual split composition on a bright white-to-soft-gray (#ffffff → #f3f4f6) background. LEFT: a young Filipino adult in casual streetwear smiling at a smartphone showing a glowing concert-ticket purchase screen, light airy daylight, natural skin texture, gently humorous everyday mood. RIGHT: the same light canvas turns serious — a single semi-photorealistic 3D human kidney rendered with anatomical accuracy rests on a clean white pedestal behind a thin teal (#1a6b72) price-tag outline that is crossed out, with a small navy (#0f1e2e) "NOT FOR SALE" label in bold condensed sans-serif. A thin teal divider separates the two halves. Premium healthcare publication aesthetic, calm and restrained, generous negative space, navy and teal accents only, no gore, no surgery imagery, no dark background anywhere. Small semi-transparent attribution "williamriveromd.com" in navy, bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. No money imagery glamourizing the sale, no surgical scenes, no fear-mongering blood. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. Background must be white, off-white, or soft light gray — never dark. Copyright attribution williamriveromd.com must be visible in the bottom-right corner.

---

IMAGE NUMBER: 2
SECTION PLACEMENT: `#myths` — after the myth-grid
FILE NAME: organ-donation-ph-od-05-myths-vs-facts.png
ARCHETYPE: Multi-panel educational infographic
AUDIENCE: patients, families, mixed
VISUAL MIX:
- photorealistic models: none (icon-led)
- 2D infographic: 6 myth/fact paired cards
- 3D component graphics: small 3D kidney + heart accents
- algorithm/flowchart: none

PURPOSE: Shareable one-glance summary of the six Filipino organ-donation myths the guide debunks.
KEY CONCEPTS: doctors still save donors; religion supports donation; PODRRS allocation is wealth-blind; open-casket burial remains possible; no absolute age limit; register AND tell your family.
DIMENSIONS: 1792 × 1024 (16:9)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient education infographic poster, landscape 16:9, modern nephrology clinic aesthetic, clean white (#ffffff) background. Title band in bold navy (#0f1e2e) condensed sans-serif: "ORGAN DONATION MYTHS — PHILIPPINES" with teal (#1a6b72) underline rule. Below, a 3×2 grid of six rounded soft-gray (#f3f4f6) cards. Each card has a red (#b91c1c) "MYTH" pill with one short myth line and a green (#1f7a4d) "FACT" pill with one short fact line: 1) MYTH "Doctors won't try to save a donor" / FACT "Brain-death doctors are legally separate from the transplant team"; 2) MYTH "My religion forbids it" / FACT "The Catholic Church calls donation an act of love"; 3) MYTH "The rich get organs first" / FACT "PODRRS allocates by medical score, never wealth"; 4) MYTH "The body can't be viewed at the wake" / FACT "Open-casket burial is fully possible"; 5) MYTH "I'm too old to donate" / FACT "No absolute age limit — the team decides"; 6) MYTH "A donor card is enough" / FACT "Register AND tell your family". Small flat 2D icons per card (stethoscope, praying hands, balance scale, candle, calendar, family). Mobile-readable typography, generous whitespace, no microtext. Small semi-transparent attribution "williamriveromd.com" in navy, bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. Background must be white, off-white, or soft light gray — never dark. Copyright attribution williamriveromd.com must be visible in the bottom-right corner.

---

IMAGE NUMBER: 3
SECTION PLACEMENT: `#how-to` — between the 4 steps and the CTA box
FILE NAME: organ-donation-ph-od-06-how-to-register.png
ARCHETYPE: Clinical algorithm / step infographic (vertical)
AUDIENCE: patients, general public
VISUAL MIX:
- photorealistic models: none
- 2D infographic: 4-step vertical pathway
- 3D component graphics: realistic donor card, driver's licence, phone render
- algorithm/flowchart: yes — linear 4-node flow

PURPOSE: Make registration feel concrete and 10-minutes easy.
KEY CONCEPTS: decide what to donate → get a donor card (NKTI / KFP / HOPE-PSN / REGALO) → carry it and tell your family → optional LTO licence annotation.
DIMENSIONS: 1024 × 1536 (2:3 portrait — matches kd-02 process-flow style)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Vertical step-by-step patient infographic, portrait 2:3, premium KDIGO-guideline aesthetic on an off-white (#fafafa) background. Header in bold navy (#0f1e2e) condensed sans-serif: "BECOME AN ORGAN DONOR — 4 STEPS, 10 MINUTES" with thin teal (#1a6b72) rule. Four large numbered rounded nodes connected by a teal vertical spine: STEP 1 "Decide what to donate" with small flat icons of kidney, heart, liver, cornea; STEP 2 "Get a donor card" with a realistic 3D-rendered signed donor card and the labels NKTI · KFP · HOPE-PSN · REGALO; STEP 3 "Carry it & tell your family" with a wallet card plus a warm flat illustration of a Filipino family talking at a table; STEP 4 "Optional: mark your LTO driver's licence" with a realistic Philippine driver's licence render bearing a small teal organ-donor heart mark. Footer band in renal green (#1f7a4d): "One donor can save up to 8 lives." Clean modular cards, generous whitespace, mobile-readable labels, navy/teal/green palette. Small semi-transparent attribution "williamriveromd.com" in navy, bottom-center.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. Do not invent official government logos or seals. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. Background must be white, off-white, or soft light gray — never dark. Copyright attribution williamriveromd.com must be visible at bottom-center (portrait rule).

---

IMAGE NUMBER: 4
SECTION PLACEMENT: `#family` — after the two-col feature cards
FILE NAME: organ-donation-ph-od-07-family-conversation.png
ARCHETYPE: Photorealistic editorial hero
AUDIENCE: grieving families, patients
VISUAL MIX:
- photorealistic models: Filipino family + transplant coordinator
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none

PURPOSE: Humanize the hardest moment in the guide — the family-consent conversation — with dignity and zero pressure.
KEY CONCEPTS: trained coordinator approaches the family; the decision belongs to the family; donation as "the last act of love."
DIMENSIONS: 1792 × 1024 (16:9)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Photorealistic medical editorial photograph for a nephrology education guide. A bright, calm hospital family-conference room in the Philippines with soft natural daylight through large windows, white and light-wood interior. A compassionate Filipina transplant coordinator in a neat teal-accented hospital uniform sits at eye level with a middle-aged Filipino couple, leaning forward gently, hands open in a respectful, unhurried gesture; the family looks pensive but supported, holding each other's hands. A closed folder and a cup of water on the light table — no paperwork being pushed. Premium healthcare publication aesthetic, shallow depth of field, natural skin texture, restrained warm-neutral grading with navy and teal accents, generous negative space at top for optional title overlay, no text embedded. Small semi-transparent attribution "williamriveromd.com" in navy, bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation, avoid melodramatic crying or deathbed imagery, no visible patient or medical equipment in frame. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. Background must be bright and airy — never dark or moody. Copyright attribution williamriveromd.com must be visible in the bottom-right corner.

---

IMAGE NUMBER: 5
SECTION PLACEMENT: `<head>` — og:image / twitter:image social share card (not placed inline on the page)
FILE NAME: organ-donation-ph-og.png
ARCHETYPE: OG / social share card
AUDIENCE: mixed — social feeds (Facebook, X, LinkedIn, iMessage previews)
VISUAL MIX:
- photorealistic models: none
- 2D infographic: title typography + stat chips
- 3D component graphics: one semi-photorealistic 3D kidney pair
- algorithm/flowchart: none

PURPOSE: Make shares of the guide legible and compelling at thumbnail size, replacing the borrowed 1536×1024 inline infographic with a purpose-built card.
KEY CONCEPTS: guide title; one donor saves up to 8 lives; register today; donation is a gift, never for sale.
DIMENSIONS: 1200 × 630 (1.91:1 — fixed, non-negotiable for OG cards)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Social share (Open Graph) card, exactly 1200 × 630 pixels, clean white (#ffffff) background with a very light teal tint (#eef6f7) panel on the right third. LEFT two-thirds: bold condensed sans-serif headline in navy (#0f1e2e), large and thumbnail-legible: "ORGAN & KIDNEY DONATION IN THE PHILIPPINES" with a thin teal (#1a6b72) rule beneath and a smaller teal subline "A Complete Patient & Family Guide". Below the subline, three small rounded chips: a renal-green (#1f7a4d) chip "1 donor = up to 8 lives", a teal chip "How to register", and an amber (#b8860b) chip "A gift — never for sale". RIGHT third: a single semi-photorealistic, anatomically accurate pair of healthy human kidneys floating on the light teal panel with a soft shadow, subtle and premium, no gore. Generous margins so nothing is cropped in platform previews, strong visual hierarchy, maximum 12 words of large text, no paragraph text, no microtext. Premium medical-publication aesthetic consistent with williamriveromd.com. Small semi-transparent attribution "williamriveromd.com" in navy, bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation. No money or price-tag imagery, no surgical scenes. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never output any size other than 1200 × 630. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be legible at small thumbnail size, visually calm, publication-grade, and consistent with williamriveromd.com. Exactly 1200 × 630. Background must be white or very light teal — never dark. Pair with og:image:width="1200" and og:image:height="630" meta tags when wired into the guide. Copyright attribution williamriveromd.com must be visible in the bottom-right corner.

---

IMAGE NUMBER: 6
SECTION PLACEMENT: Kidney Donation tab, `#kd-stats` — REPLACES the portrait `organ-donation-ph-kd-01-living-donor-consultation.png` (864×1821), which is too tall for the column
FILE NAME: organ-donation-ph-kd-01b-living-donor-consultation-landscape.png
ARCHETYPE: Photorealistic editorial hero
AUDIENCE: patients, families considering living donation
VISUAL MIX:
- photorealistic models: Filipino nephrologist/coordinator, donor, recipient
- 2D infographic: none
- 3D component graphics: none
- algorithm/flowchart: none

PURPOSE: Replace the oversized portrait consultation image with a landscape version that sits comfortably in the article column.
KEY CONCEPTS: a calm, professional living-donor consultation at a Philippine transplant centre; donor and recipient both present; trust and no pressure.
DIMENSIONS: 1792 × 1024 (16:9 landscape)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Photorealistic medical editorial photograph for a nephrology education guide, landscape 16:9. A bright, modern consultation room at a Philippine transplant centre with soft natural daylight and white-and-light-wood interior. A Filipina nephrologist in a white coat and a transplant coordinator in a teal-accented uniform sit across a light table from a potential living kidney donor (a healthy Filipino adult in his 30s) and the intended recipient (his older sibling), reviewing a tablet together; open, unhurried body language, warm professional eye contact, gentle smiles, no paperwork being pushed. Premium healthcare publication aesthetic, shallow depth of field, natural skin texture, restrained warm-neutral grading with navy and teal accents, generous negative space at one side, no text embedded. Small semi-transparent attribution "williamriveromd.com" in navy, bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look, avoid excessive saturation, no surgical or hospital-bed imagery, no fearful expressions. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Must be mobile-readable, clinically plausible, visually calm, publication-grade, and consistent with williamriveromd.com. Bright, airy lighting — never dark or moody. Copyright attribution williamriveromd.com must be visible in the bottom-right corner.
