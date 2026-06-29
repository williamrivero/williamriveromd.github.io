# Image Prompt — `hero-cat-other-tools`
### Category hero for the "Other Tools" section of `guides/calculators.html`

**Stage 1 prompt pack** for a single category hero image. Generate in the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator),
save the PNG (+ a paired `.webp` twin) to `images/`. Once present, the file
auto-surfaces in the Latest-calculators carousel for any calc that lives under
the `other-tools` section, including `calc-icd10-search.html`.

| Slot | File | Skill | Size | Section color |
|---|---|---|---|---|
| Other Tools category hero | `hero-cat-other-tools.png` | infographic-skill — Archetype 5 (Reference Card) hybrid w/ Archetype 1 (still-life) | 1254 × 1254 (1:1) | `#475569` (slate) |

The slate `#475569` section color is the muted-neutral tone that distinguishes
this catch-all section from the colorful clinical-calculator categories. The
image should pick up that neutral slate as an accent — not a heavy fill — and
otherwise stay on a light, airy background per house rules.

---

## Prompt

*Skill: williamriveromd-infographic-skill · Mixed archetype — semi-photorealistic clinical still-life with subtle icon overlay*

```
FILE NAME: hero-cat-other-tools.png
IMAGE TYPE: Calculator-index category hero — clinical reference / documentation still-life
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1254 × 1254
AUDIENCE: clinicians (mixed)
VISUAL GOAL: Convey "reference tools, code lookups, documentation work" without being literally about ICD-10 — a clean, calm tableau of the tools a Filipino clinician reaches for when looking something up. Slate-tinted accent that ties to the section's #475569 colour, otherwise light and airy.

PROMPT:
Premium medical editorial still-life for a nephrology calculator-index category hero. Square 1:1, 1254 × 1254. Bright, airy, naturally lit clinical workspace — soft daylight from upper-left, gentle shadows, restrained depth-of-field. The scene reads as the desk of a thoughtful Filipino clinician who has stepped away to grab coffee: nothing posed, nothing busy.

Composition (top-down or shallow three-quarter view, neutral cream/off-white desk surface #fafafa):
  - CENTER, slightly left: a slim modern tablet, screen tilted toward the viewer, displaying a clean clinical reference interface — a search bar at the top and three or four neat rows underneath, each row a short alphanumeric code label and a one-line description. Render the rows abstractly (no specific real ICD-10 codes; legible-looking but generic shapes, in a sans-serif type, dark navy ink on a near-white screen). The UI mirrors the look of a code-lookup tool without being literally the ICD-10 widget.
  - JUST RIGHT of the tablet: a small stack of two clinical reference books, one closed (a slate-grey cloth-bound cover, subtle silver hot-stamped spine reading just "REFERENCE"), one open on top — pages crisp, two visible columns of small clean type, a thin teal ribbon bookmark trailing off the edge.
  - LOWER LEFT: a small open notebook with a fountain-pen capped on top, partial handwritten clinician's note showing "Top differentials:" and three short bullet lines (handwritten in dark navy ink, just legible enough to read as notes — no medical details that risk inaccuracy). Beside it, a black-frame pair of reading glasses, folded.
  - UPPER RIGHT: a stethoscope coiled loosely, soft warm leather strap of an analog watch peeking under it. A simple ceramic mug of black coffee at the far upper-right corner, a thin curl of steam.
  - SUBTLE accent: a single slate-grey index card visible behind the tablet, edge just peeking out, suggesting the section's slate (#475569) colour without dominating.

Palette: off-white #fafafa desk; light cool grey shadows; dark navy #0f1e2e for type/ink; clinical teal #1a6b72 only for the ribbon bookmark and the tablet's search-bar accent line; warm leather brown only on the watch strap; slate #475569 as the index-card accent. No other colours. No saturated reds, oranges, or pinks. No bright synthetic blue UI mockups — the tablet screen should feel like a calm reference document, not a sci-fi dashboard.

Mood: thoughtful, professional, calm. Filipino clinical context implied through small details — a small Philippine-flag pin discreetly on the open notebook's cover corner is acceptable but not required.

Composition rules:
  - Hero composition is balanced and tidy; objects breathe with space between them.
  - Frame the still-life so that meaningful content sits inside the central 80% safe zone (the calculator-index card crops in slightly).
  - No people in this hero. No faces. A clinician's tools, not the clinician.
  - Tablet UI rows must use simple sans-serif type (Inter, Manrope, Nunito Sans, or IBM Plex Sans only). No fictional logos, no real ICD code numbers visible in full, no PhilHealth wordmark, no hospital name.

Bottom-right corner: subtle attribution "williamriveromd.com" in small semi-transparent navy text, ~10–11 px equivalent, 70% opacity — placed on the desk surface, not overlapping any object.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid stocky over-styled product-photography look, avoid neon UI mockups, avoid tiny unreadable labels, avoid AI gibberish text on the tablet screen or the open book pages — text must be either visibly abstract type-blocks or short legible English phrases. NEVER use dark, navy, charcoal, or black backgrounds — desk surface and surround must be light cream / off-white only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope for any visible type — no serif fonts on the tablet UI or notebook label. Do NOT render real PhilHealth, WHO, AHA, or hospital logos. Do NOT render any specific ICD code that maps to a real diagnosis with a fictional title (better to keep code shapes abstract than risk inaccuracy). Never omit the williamriveromd.com attribution.

QUALITY CHECK:
A calm Filipino-clinical workspace still-life, square 1:1, that reads in one second as "reference / lookup / documentation tools" without being literally about ICD-10. Tablet UI is calm and abstract; reference book is closed/open pair with a teal ribbon; notebook + pen + glasses ground the lower-left; stethoscope + watch + coffee ground the upper-right; a slate index card peeks from behind the tablet as the only saturated colour cue. Light cream desk surface, no dark fill anywhere. Bottom-right williamriveromd.com attribution visible. The image must crop cleanly to the Latest-calculators thumbnail (round-cornered card with peeking edge) without losing the tablet or book.
```

---

## Post-generation steps

1. Save as `images/hero-cat-other-tools.png` and a paired WebP twin
   `images/hero-cat-other-tools.webp` (PIL: `Image.open(png).save(webp, 'WEBP', quality=82, method=6)`).
2. Re-run `python3 generate_latest_calculators.py` &mdash; the script's
   `SECTION_HERO_MAP` already includes `"other-tools": "hero-cat-other-tools"`,
   so the file will start appearing as the thumbnail for any calc filed
   under the `other-tools` section.
3. (Optional) Also generate the related-guides thumbnail variant
   `hero-cat-other-tools-rg-thumb.webp` &mdash; the rest of the
   `hero-cat-*` family has these; the Latest-calculators carousel uses the
   full image, but `related_guides.json`-driven related-card thumbs use
   the `-rg-thumb` variant.
