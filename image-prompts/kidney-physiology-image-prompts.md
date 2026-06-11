# Image Prompts — "Your Amazing Kidneys" (Normal Physiology)
## kidney-physiology.html · williamriveromd.com
### Generated 2026-06-11

The guide's current `og:image` / `twitter:image` points at `photo-hero.jpg`, a
stock portrait that is **not** Dr. Rivero — it must be replaced. This pack has
the one replacement: a proper OG social-share card.

**House rules:** light background only, navy/teal/green/amber as accents and
type only, `williamriveromd.com` attribution bottom-right, no human faces.

---

## IMAGE 1 — OG / SOCIAL SHARE CARD

**IMAGE NUMBER:** 1 of 1
**SECTION PLACEMENT:** `<meta property="og:image">` + `twitter:image` (replaces the stock portrait `photo-hero.jpg`). Also reused as the homepage "New to CKD" learning-path thumbnail for Step 1.
**FILE NAME:** `kidney-physiology-og.png`
**ARCHETYPE:** Editorial OG card (title typography + 3D kidney on light base)
**AUDIENCE:** Mixed — link-preview audience (patients, families, students)
**DIMENSIONS:** 1200 × 630 px (1.91:1) — FIXED OG size. Pair with `og:image:width="1200"` / `og:image:height="630"`.

**VISUAL MIX:**
- photorealistic models: none (no faces)
- 2D infographic: dominant — title block + three concept pills
- 3D component graphics: semi-photorealistic anatomical kidney
- algorithm/flowchart: none

**PURPOSE:** Replace the incorrect stock portrait with a branded, on-style OG card that reads as a friendly normal-physiology explainer.

**KEY CONCEPTS:** "Your Amazing Kidneys," normal physiology in plain language, filters ~180 L/day, balances fluid & salt, makes blood and bone signals.

---

### COPY-READY IMAGE GENERATOR GPT PROMPT

```
FILE NAME: kidney-physiology-og.png
IMAGE TYPE: OG / social share card — title typography + 3D kidney on light base
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: General social-media link-preview audience (patients, families, students)
VISUAL GOAL: A premium, legible link-preview card for "Your Amazing Kidneys" that pairs a clean title block with a realistic 3D kidney, signaling a friendly normal-physiology explainer.

PROMPT:
Clean editorial social-share card on a crisp white (#ffffff) background with a very subtle light teal-tint (#eef6f7) panel on the right third. Premium medical-publication aesthetic, calm, airy, and uncluttered.

LEFT TWO-THIRDS — typography block, left-aligned with generous margins:
- A small teal (#1a6b72) eyebrow label in bold uppercase: "NEPHROLOGY · PATIENT GUIDE".
- Main title in large bold condensed navy (#0f1e2e) sans-serif on two lines:
  "Your Amazing Kidneys"
  then slightly smaller below: How your kidneys keep you alive — the normal physiology, in plain language.
- A thin teal underline rule beneath the title.
- A single row of three tiny teal pill-badges with short labels: "Filters 180 L/day", "Balances fluid & salt", "Makes blood & bone signals".

RIGHT ONE-THIRD — a softly rendered, semi-photorealistic 3D anatomical kidney in warm clinical tones (deep red-brown cortex, visible renal artery in red and vein in blue, ureter), gently lit, floating on the light teal-tint panel with a soft shadow. Anatomically accurate, calm and clean, not gory — publication-grade medical illustration. Optionally one or two thin teal callout lines hinting at internal nephron detail, but keep it minimal and uncluttered.

All text must be real, correctly spelled, crisp, and mobile-thumbnail legible. Generous safe-zone margins; keep all text and the kidney well inside the edges (platforms may crop). No human faces or portraits anywhere in the image.

Bottom-right corner: "williamriveromd.com" in small semi-transparent (70% opacity) navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish or misspelled words, avoid neon gradients, avoid busy backgrounds, avoid any human face or portrait, avoid gory/wet realism. NEVER use a dark, navy, charcoal, or black background — light base only. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Title perfectly spelled, mobile-thumbnail legible, anatomically plausible 3D kidney, calm premium look, light background, no human face, attribution bottom-right, exactly 1200 × 630.
```

---

**After generating:** push `kidney-physiology-og.png`, then I will (1) resize to exactly 1200×630 + build the WebP companion, (2) replace `photo-hero.jpg` in the guide's `og:image` and `twitter:image` tags (adding `og:image:width/height/alt`), and (3) regenerate the homepage Step-1 learning-path thumbnail from this card so the portrait is gone everywhere.
