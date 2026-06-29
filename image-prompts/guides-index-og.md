# guides/index.html — Unignorable OG Share Card

Generated with **`williamriveromd-infographic-skill`**. Single prompt, ready to paste into the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator).

**House rules respected:** light background only, fonts limited to **Inter / Nunito Sans / IBM Plex Sans / Manrope** (no serif), OG dimensions locked at **1200 × 630**, `williamriveromd.com` attribution in the bottom-right.

---

## Card spec

| Field | Value |
|---|---|
| **File name** | `guides-index-og.png` |
| **Replaces** | `images/guides-hero-banner.png` (currently used as og:image at 2172 × 724 — wrong aspect for social) |
| **Image type** | OG / social share card |
| **Aspect ratio** | 1.91 : 1 |
| **Pixel dimensions** | **1200 × 630** |
| **Audience** | Mixed — Filipino patients, families, referring clinicians, journalists |
| **Visual goal** | Stop the scroll on FB / X / LinkedIn / iMessage and convey instantly: this is the master library of evidence-based kidney guides by a practising nephrologist. |

After generation, also update the guide's `<head>`:
```html
<meta property="og:image"        content="https://www.williamriveromd.com/images/guides-index-og.png">
<meta property="og:image:width"  content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt"    content="W. Rivero, MD — Real answers. 135+ kidney-disease patient guides, 174 calculators, KDIGO-2024 evidence.">
<meta name="twitter:image"       content="https://www.williamriveromd.com/images/guides-index-og.png">
```

---

## COPY-READY PROMPT (paste into the Image Generator GPT)

```
Create a publication-grade OG / social-share card for williamriveromd.com — the
master library hub for Dr. W. Rivero, MD's nephrology and internal-medicine
patient guides. Editorial, premium healthcare design, scroll-stopping at
thumbnail size on Facebook / X / LinkedIn / iMessage.

DIMENSIONS: exactly 1200 × 630 px (1.91:1). Render as a single PNG.

BACKGROUND (NON-NEGOTIABLE — LIGHT):
Off-white / warm cream base #f8f5f0 with an extremely subtle warm gradient
(very pale amber wash #fdf6e3 in the upper-left fading to clean cream
toward the lower-right). Optional: a faint, low-contrast paper-grain texture
to give an editorial feel — never noisy, never noisy. NO dark navy / oxblood /
black backgrounds anywhere. The whole card reads light and airy.

LAYOUT (split 60 / 40, editorial magazine cover):

LEFT PANEL (60% width, generous left padding ~80 px, vertically centred):
  1) AMBER EYEBROW CHIP — a small pill-shaped chip with text:
     "NEPHROLOGY · INTERNAL MEDICINE · CLINICAL NUTRITION"
     Font: Inter, weight 700, size ~13 px, letter-spacing 0.18em, all caps.
     Chip background #b8860b (amber-gold) on a thin amber border, text white,
     padding 6 × 14 px, border-radius 999px. Subtle, not garish.
  2) MASSIVE HEADLINE on two lines:
     "Real answers."   ← line 1, weight 900 (Inter Black), size ~92 px, color
                          #0f1e2e (deep navy ink), tracking -0.02em. Place a
                          short amber-gold (#b8860b) horizontal underline (~80
                          px × 6 px, slightly rotated -1°) tucked under the
                          period for editorial emphasis.
     "Plain language.  ← line 2, weight 600 (Inter Semibold), size ~36 px,
      Evidence you       color #1a6b72 (clinical teal), tracking -0.01em.
      can trust."        Single line if it fits, otherwise wrap at "Evidence".
  3) STAT ROW directly below the sub-headline, separated by a thin amber rule
     at full panel width (1 px, #b8860b at 40% opacity). Four stats, each a
     small column with a big number above a small all-caps label:
       "135"  GUIDES
       "174"  CALCULATORS
       "4"    LANGUAGES
       "2024" KDIGO
     Numbers: Inter Black weight 900, size ~32 px, color #0f1e2e.
     Labels: Inter weight 700, size 10 px, letter-spacing 0.18em, all caps,
     color #1a6b72. Equal gaps between the four columns.

RIGHT PANEL (40% width):
  A single hero clinical motif — a HYPER-DETAILED 3D anatomical kidney
  rendered in cross-section, ¾-view from the right. Realistic medical
  illustration quality (NEJM / AJKD educational standard), warm cream and
  rust tones on the renal cortex, deeper amber-gold #b8860b accent inside
  the medullary pyramids and along the arcuate vasculature so the kidney
  glows softly from within, as if backlit. Visible structures: smooth
  capsule, cortex, medullary pyramids, renal pelvis, branching arcuate +
  interlobar vessels, a few representative nephrons rendered as fine
  golden filaments radiating from cortex into medulla — clinically
  accurate, never abstract or sci-fi. Soft natural light from upper-left,
  gentle shadow on the cream background, no harsh rims. Subject sits on
  the light background with generous negative space around it (~10% margin
  to card edge).

ATTRIBUTION (MANDATORY):
Bottom-right corner, 22 px in from each edge: small text
"williamriveromd.com" in Inter weight 600, 11 px, color #0f1e2e at 60%
opacity. Not obscuring any anatomy or text.

TYPOGRAPHY RULES — ABSOLUTE:
Use ONLY Inter (with weights 400, 600, 700, 800, 900 as specified above).
NO serif fonts, NO italic styles, NO display or handwritten faces. All
text rendered crisply with proper kerning, anti-aliased, perfectly legible
at thumbnail size (a 500-px-wide preview should still read "Real answers.
135 guides" cleanly).

COLOR PALETTE — STRICTLY:
- Background cream     #f8f5f0 (with subtle #fdf6e3 wash, never darker)
- Ink navy             #0f1e2e (headline, big numbers, attribution)
- Clinical teal        #1a6b72 (sub-headline, stat labels)
- Amber-gold accent    #b8860b (eyebrow chip, headline underline,
                        kidney inner glow, hairline rules)
- White                #ffffff (eyebrow chip text only)
No reds. No purples. No saturated blues. No dark backgrounds anywhere.

MOOD: confident · clinical · editorial · premium · trustworthy ·
calm. Like the cover of a quality medical magazine, not a flashy ad.
Loads of negative space; deliberate typographic hierarchy; every
element earns its place. The kidney is the visual anchor; the
typography is the message; the amber accents tie them together.

NEGATIVE INSTRUCTIONS:
- Avoid dark / navy / black / oxblood backgrounds (light only).
- Avoid serif fonts, italic stylings, hand-lettered or decorative
  typefaces (Inter only).
- Avoid stock-photo aesthetic, AI-art shine, neon gradients, glitter,
  excessive bloom, lens flare, or HDR over-processing.
- Avoid cartoonish or stylised kidney anatomy.
- Avoid clutter, overcrowding, decorative borders or frames.
- Avoid embedded URLs other than the bottom-right attribution.
- Avoid stray words or gibberish text; render every label exactly as
  specified above.

QUALITY CHECK: must be instantly readable as a Facebook/X thumbnail;
must look like a premium medical publication cover; must carry the
"williamriveromd.com" attribution; must use a light background;
must use Inter for every piece of text.
```
