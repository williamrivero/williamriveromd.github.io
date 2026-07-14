# Image Plan — `physical-activity-sports-ckd.html`
### "Move Right, Kidneys Right" — Physical Activity & Sports for Filipino CKD Patients
**Stage-1 prompt pack for the ChatGPT Image Generator GPT** → https://chatgpt.com/g/g-pmuQfob8d-image-generator
Authored with the `williamriveromd-hero-vignette`, `williamriveromd-organ-crosstalk-sigil-graphic`, and `williamriveromd-infographic-skill` skills.

---

## 1 · Image inventory (what the guide + calculator reference)

| # | File (save to `images/`) | Type | Dimensions | Where it appears | Skill |
|---|---|---|---|---|---|
| 1 | `physical-activity-sports-ckd-vignette-hero.png` **+ `.webp`** | Circular vignette hero (people) | 2048 × 2048 (1:1) | Guide hero disc (`figure.hero-figure > .hero-vignette`) | hero-vignette |
| 2 | `physical-activity-sports-ckd-01-triangle.png` **+ `.webp`** | Organ-crosstalk sigil | 1024 × 1024 (1:1) | Inline figure in **Why Move** (`#why`) | organ-crosstalk-sigil |
| 3 | `physical-activity-sports-ckd-02-met-chart.png` **+ `.webp`** | MET intensity color-tier chart | 1792 × 1024 (16:9) | Inline figure in **Sports** (`#sports`) | simple-figure |
| 4 | `physical-activity-sports-ckd-03-rpe-scale.png` **+ `.webp`** | Borg RPE / talk-test gauge | 1792 × 1024 (16:9) | Inline figure in **Green Light** (`#greenlight`) | simple-figure |
| 5 | `physical-activity-sports-ckd-04-home-routine.png` **+ `.webp`** | 3-panel home-routine sequence | 1792 × 1024 (16:9) | Inline figure in **Home Routine** (`#home`) | simple-figure |
| 6 | `physical-activity-sports-ckd-og.png` | OG / social share card | **1200 × 630** (1.91:1, fixed) | `og:image` / `twitter:image` | infographic-skill |
| 7 | `physical-activity-sports-ckd-rg-thumb.webp` | Related-guides thumbnail | 480 × 480 (1:1) crop | "Related Guides" cards on sibling pages + the MET calculator | crop of #1 or #6 |

**7 assets total** (5 inline/hero + OG + thumbnail). Each inline figure and the hero also ship a `.webp` twin; the OG card is PNG-only and the thumbnail is `.webp`.

**Already present, no generation needed:** `images/hero-cat-lifestyle.webp` (OG fallback used by the MET calculator page), `images/avatar.png/webp`, `images/dr-rivero-contact-qr.svg`.

> The head `<meta og:image ... width="1200" height="630">` tags and the `<picture>`/`<img width height>` markup are **already wired into the guide** — you only need to drop the rendered files into `images/` with these exact names and their `.webp` twins.

---

## 2 · Prompt 1 — Circular vignette hero

```
FILE NAME: physical-activity-sports-ckd-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A (people)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: E — Lifestyle
CAMERA: environmental portrait (rear three-quarter, slightly low angle)
HUMAN VARIATION (vs. previous guides): early-60s Filipina · female · short cropped salt-and-pepper hair · round face · soft jawline · broad nose · warm mid-brown skin · sturdy/stocky build · coral-red athletic t-shirt · charcoal jogging pants · white rubber shoes · small handheld water bottle · relaxed mid-stride posture · calm content half-smile · brisk-walking activity · outdoor barangay court at sunrise · rear-three-quarter framing (≥12 traits differ from prior heroes)
AUDIENCE: patients (non-dialysis and dialysis)
VISUAL GOAL: convey safe, everyday movement — an ordinary Filipino patient walking briskly at sunrise in her own neighborhood.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be
displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a
visible WHITE BORDER around the full circle (the circle must never touch the canvas
edges). Composition archetype: E — Lifestyle. Camera: environmental portrait, rear
three-quarter view from a slightly low angle.

Subject: a Filipina woman in her early sixties with short cropped salt-and-pepper hair,
a round face and soft jawline, warm mid-brown skin, and a sturdy build, walking briskly
across a clean concrete barangay basketball court at sunrise. She wears a coral-red
athletic t-shirt, charcoal jogging pants, and white rubber shoes, and loosely carries a
small water bottle; her posture is easy and mid-stride with a calm, content half-smile.
Soft golden early-morning daylight, gentle shallow depth of field.

Supporting context (2–3 elements only, lower third and mid-frame): a simple badminton
racket resting on a low bench, a couple of blurred palm trees and a low barangay
fence, and the faint chalk lines of the court — all understated. Warm sunrise haze.

Visual hierarchy: the walking figure occupies 60–70% of the circle; the bench, fence,
and court lines are 20–30%; reserve a 20–25% TITLE SAFE ZONE of open, softly gradient
sunrise SKY across the upper-left of the circle (no faces, anatomy, icons, food, or
callouts in that zone) so the HTML title can sit beside the disc without covering
important artwork.

Calm, reassuring, documentary-realistic colour grade harmonizing with clinical teal
#1a6b72 and navy #0f1e2e on a light, airy background; warm renal-green and gold sunrise
accents. Soft edge falloff toward a slightly deeper neutral at the rim. Full-bleed
within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or
renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons,
tiny unreadable labels, infographic clutter, duplicated people, repeated compositions,
cropped circle, cropped objects, cropped anatomy, edge clipping, objects touching the
circular border, important content inside the title safe zone, baked-in text/titles/
captions/logos/watermarks, rectangular borders/frames/banners, dark/charcoal/black
backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces,
implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin — never
cropped. ONE dominant hero subject (the walking woman) at 60–70% of the circle, 2–4
supporting elements, 20–25% empty sunrise-sky title-safe zone reserved. Filipino
clinical/community context, ≥12 traits different from prior heroes. Rear-three-quarter
framing not repeated from the previous guide. Crops cleanly inside the circle with no
text or subject lost at the edge.
```

---

## 3 · Prompt 2 — Kidney–heart–muscle crosstalk sigil (inline `#why` figure)

```
FILE NAME: physical-activity-sports-ckd-01-triangle.png
IMAGE TYPE: Organ-crosstalk sigil (triangular, three organs)
ASPECT RATIO: 1:1 (square)
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: patients
VISUAL GOAL: show the kidney–heart–muscle triangle as one connected loop — inactivity
strains all three; regular movement relieves all three.

PROMPT:
Create a simple medical organ-crosstalk sigil illustration featuring three organs
arranged in a balanced triangle:
- a pair of kidneys (bottom-center, the anchor organ)
- a heart (top-left)
- a skeletal-muscle / flexed-arm-muscle icon (top-right)

RELATIONSHIP:
Show the kidney–heart–muscle axis as a calm, continuous three-way loop. Use thin dotted
curved arrows travelling clockwise around the triangle — heart → muscle → kidneys →
heart — with a second, lighter set of dotted return arrows completing a gentle
bidirectional circuit. The loop should read as one connected system, not three separate
icons. Suggest that movement flows benefit around the whole triangle.

STYLE:
Minimal clinical line-art, thin monoline strokes, soft teal-blue palette (clinical teal
#1a6b72, muted slate-blue, pale cyan) with a single warm renal-green accent on the
kidneys, white background, clean rounded organ shapes, balanced sigil-like composition,
generous whitespace, no photorealism, no 3D, no heavy shadows. If any small label is
added, set all type in a clean sans-serif font — Inter, Nunito Sans, IBM Plex Sans, or
Manrope only, never a serif font (default is label-free).

COMPOSITION:
Place the kidneys at the bottom-center as the visual anchor, the heart at the upper-left
vertex, and the muscle icon at the upper-right vertex, forming an equilateral triangle
with generous margins. Connect the three with dotted curved arrows forming a smooth
circular loop. Keep the design simple, symbolic, airy, and suitable for a
patient-education nephrology website.

OUTPUT:
Square high-resolution image, clean margins, publication-grade medical icon aesthetic.
Include a small, semi-transparent "renalcarematters.com" attribution in the bottom-right
corner, navy or dark-teal, ~10–11px, ~70% opacity, not obscuring the sigil.

NEGATIVE INSTRUCTIONS:
Avoid photorealistic anatomy, surgical detail, excessive labels, dark background, neon
colors, complex infographics, crowded/tangled arrows, thick cartoon outlines, 3D
rendering, glossy icons, dramatic lighting, stock-photo style. If text is present, never
use serif or decorative fonts — Inter, Nunito Sans, IBM Plex Sans, or Manrope only.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Clean white background, three clearly recognizable organ icons in a balanced triangle,
one continuous dotted loop (not crowded), soft teal palette with a green kidney accent,
generous whitespace, renalcarematters.com attribution visible bottom-right.
```

> **Figcaption already in the guide** (rule 11 satisfied): the `<figcaption>` carries a
> plain-language `.fig-desc` plus a `<dl class="fig-abbrevs">` for CKD, eGFR, and BP, so
> the lightbox caption panel is populated. No further caption work needed.

---

## 4 · Prompt 3 — OG / social share card (1200 × 630, fixed)

```
FILE NAME: physical-activity-sports-ckd-og.png
IMAGE TYPE: OG / social share card (archetype: multi-panel editorial header)
ASPECT RATIO: 1.91:1 (fixed — never resize)
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed (patients + referring clinicians)
VISUAL GOAL: a clean, shareable card that says at a glance "safe movement for kidney
patients, by CKD stage and sport."

PROMPT:
Premium nephrology OG / social share card, landscape 1200×630, on a WHITE / off-white
(#fafafa) background — light background only. Left two-thirds: bold headline typography in
navy #0f1e2e set in Inter (or Manrope) — primary line "Move Right, Kidneys Right" with a
smaller teal #1a6b72 subtitle underneath "Physical activity & sports for Filipino kidney
patients — non-dialysis & dialysis". Below the subtitle, a single tidy row of three small
rounded intensity chips reading "LIGHT" (renal-green #1f7a4d), "MODERATE" (amber-gold
#b8860b) and "VIGOROUS" (clinical-red #b91c1c), each as a clean pill — the only chips on
the card.

Right third: a bright, airy, photorealistic vignette of a Filipino patient in light
athletic clothing mid brisk-walk or a gentle badminton swing on a sunlit barangay court,
naturally lit, calm and trustworthy, softly faded into the white background at its left
edge (no hard rectangle). A subtle 2D line-icon of a pair of kidneys with a small heart
and muscle mark sits as a light watermark-scale accent near the imagery, teal monoline,
low prominence.

Layout: generous whitespace, strong hierarchy, rounded soft panels, mobile-thumbnail
legible. Palette strictly navy #0f1e2e (text) + clinical teal #1a6b72 + renal-green
#1f7a4d + amber-gold #b8860b + clinical-red #b91c1c on white. All type in Inter, Nunito
Sans, IBM Plex Sans, or Manrope only — no serif, no decorative fonts.

Include the copyright attribution "renalcarematters.com" as small semi-transparent navy
text (10–11px, ~70% opacity) in the bottom-right corner, not obscuring content.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic stock-photo look,
avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light
backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or
Manrope — no serif fonts, no decorative or handwritten typefaces. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200×630. White/off-white background. Headline "Move Right, Kidneys Right"
crisp and mobile-legible; only three intensity chips; one photoreal Filipino movement
vignette softly blended on the right; approved sans-serif throughout; renalcarematters.com
visible bottom-right. Clinically calm, publication-grade.
```

---

## 5 · Prompt 4 — Related-guides thumbnail (optional standalone, or crop)

The simplest route is a **square center-crop of the hero (Prompt 1)** exported at 480×480
as `physical-activity-sports-ckd-rg-thumb.webp`. If you prefer a purpose-built thumbnail,
reuse Prompt 1's subject with a tighter crop:

```
FILE NAME: physical-activity-sports-ckd-rg-thumb.png  (export a 480×480 .webp twin)
IMAGE TYPE: Related-guides thumbnail (tight lifestyle crop)
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024 (downscale to 480×480 webp for use)
PROMPT:
Square photorealistic lifestyle thumbnail, light airy background. A Filipino kidney
patient in light athletic clothing mid brisk-walk on a sunlit barangay court at sunrise,
tight waist-up-to-full-body crop, calm and trustworthy, soft natural daylight, shallow
depth of field. Colour grade harmonizing with clinical teal #1a6b72 on a bright
background. No text, no labels, no logo, no watermark. Clean, mobile-legible at small size.
NEGATIVE INSTRUCTIONS: no dark backgrounds, no text, no clutter, no cartoon/HDR, no
distorted anatomy.
```

---

## 5b · Prompt 5 — MET intensity color-tier chart (inline `#sports` figure)

```
FILE NAME: physical-activity-sports-ckd-02-met-chart.png
IMAGE TYPE: Simple figure — Scaffold E (reference/matrix card), color-tier chart
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients
VISUAL GOAL: sort Filipino activities into green/amber/red intensity tiers so a patient
picks a stage-appropriate sport at a glance.

PROMPT:
Clean clinical reference chart, publication-grade nephrology design, white (#ffffff)
background. Bold navy (#0f1e2e) title in Inter: "Match the Sport to Your Tier". Three
horizontal color-banded rows stacked top to bottom, each a rounded card:
- TOP row, renal-green (#1f7a4d) accent, header "LIGHT (under 3 MET)": small clean line
  icons + short labels for walking (leisurely), household chores, tai chi. Sub-note
  "All groups, including frail and G5."
- MIDDLE row, amber-gold (#b8860b) accent, header "MODERATE (3–6 MET)": brisk walking,
  leisure cycling, badminton doubles, pickleball, half-court basketball. Sub-note
  "The everyday target — G1–G4, HD & PD off-days."
- BOTTOM row, clinical-red (#b91c1c) accent, header "VIGOROUS (over 6 MET)": Zumba,
  full-court basketball, competitive badminton. Sub-note "Cardiac-cleared, higher-
  functioning non-dialysis only."
A slim vertical MET gauge on the left edge (2 → 8+) aligns the three bands. Soft gray
(#f3f4f6) panel behind the rows, generous whitespace, mobile-readable labels ≥11pt, all
type in Inter or Manrope (no serif). Bottom-right: "renalcarematters.com" in small
semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY
the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or
decorative fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9, white background, three clearly separated green/amber/red tier rows with correct
sports in each, a left MET gauge, mobile-legible sans-serif labels, renalcarematters.com
bottom-right. (Figcaption + MET/HD/PD abbreviation list already in the guide.)
```

---

## 5c · Prompt 6 — Borg RPE / talk-test gauge (inline `#greenlight` figure)

```
FILE NAME: physical-activity-sports-ckd-03-rpe-scale.png
IMAGE TYPE: Simple figure — Scaffold D/E (single gauge + talk-test key)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients
VISUAL GOAL: show the Borg 6–20 scale with the moderate 11–13 band highlighted and tied
to the talk test.

PROMPT:
Clean clinical education figure, white (#ffffff) background. Bold navy (#0f1e2e) title in
Inter: "How Hard Should It Feel?". A single large horizontal gauge/ruler running left to
right from 6 (labeled "No effort") to 20 (labeled "All-out maximal"), with tick numbers
6, 9, 11, 13, 15, 17, 20. A soft gradient along the gauge from renal-green (#1f7a4d, low)
through amber-gold (#b8860b, middle) to clinical-red (#b91c1c, high). The 11–13 segment is
clearly highlighted with an amber rounded bracket labeled "MODERATE — your target". Three
compact "talk test" callout chips beneath the gauge, aligned to their zones: green "Can
talk AND sing = too easy", amber "Can talk in short sentences, cannot sing = just right",
red "Too breathless to talk = ease off". Generous whitespace, soft gray (#f3f4f6) base
panel, mobile-readable sans-serif labels in Inter or Manrope (no serif). Bottom-right:
"renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY
the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or
decorative fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9, white background, one clear 6–20 gauge with a green→amber→red gradient, the 11–13
"moderate" band bracketed, three talk-test chips correctly zoned, sans-serif labels,
renalcarematters.com bottom-right. (Figcaption + RPE abbreviation already in the guide.)
```

---

## 5d · Prompt 7 — Home-routine 3-panel sequence (inline `#home` figure)

```
FILE NAME: physical-activity-sports-ckd-04-home-routine.png
IMAGE TYPE: Simple figure — Scaffold C (3-panel horizontal sequence)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients
VISUAL GOAL: three no-equipment routine levels — chair, standing, balance — shown with a
calm Filipino patient.

PROMPT:
Clean patient-education figure, white (#ffffff) background. Bold navy (#0f1e2e) title in
Inter: "No-Equipment Home Routine". Three rounded cards in a single horizontal row on a
soft gray (#f3f4f6) panel, each with a colored top accent band, a small semi-photoreal
illustration of a Filipino patient (varied ages, home setting, light athletic clothing),
and 2–3 short labels:
- Card 1, teal (#1a6b72) band, "CHAIR-BASED": sit-to-stands, seated marching, wall
  push-ups — labeled "frail, elderly, G5, dialysis days".
- Card 2, amber-gold (#b8860b) band, "STANDING BODYWEIGHT": modified squats, calf raises,
  step-ups, resistance bands — labeled "stronger days".
- Card 3, renal-green (#1f7a4d) band, "BALANCE": single-leg stand near a wall, tai-chi
  weight shifts — labeled "prevent falls".
Bold navy right-pointing arrows between the cards. Bright, airy, naturally lit home
scenes, calm and trustworthy. Bottom strip in soft gray with a navy takeaway: "Two
strength days a week — start low, build over weeks." Mobile-readable sans-serif labels in
Inter or Manrope (no serif). Bottom-right: "renalcarematters.com" in small semi-
transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY
the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or
decorative fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
16:9, white background, three connected cards (chair / standing / balance) with correct
exercises and audience labels, calm Filipino home illustrations, arrows between cards, a
navy takeaway strip, sans-serif labels, renalcarematters.com bottom-right.
```

---

## 6 · Production checklist (Stage 2)

1. Generate each PNG in the Image Generator GPT with the prompts above.
2. For files 1–5 (hero + all inline figures), also export a **`.webp` twin** at the same
   name (the guide's `<picture>` markup already points at both). File 6 (OG) is PNG-only.
   File 7 (thumbnail) ships as `.webp`.
3. Drop all files into `images/` using the **exact filenames** in §1.
4. No HTML edits needed — the guide already references every path and the OG meta tags
   already carry `width="1200" height="630"`. Confirm the hero disc renders (open the
   guide, check the circle crops cleanly, and re-check in dark mode).
5. Optional: after images land, run `python3 patch_hero_fetchpriority.py --guide physical-activity-sports-ckd.html`
   and `python3 patch_hero_maxwidth.py --guide physical-activity-sports-ckd.html` again to
   re-confirm the LCP hints on the now-real hero image (both are idempotent).

## 7 · House-rule compliance baked into every prompt
- **Light backgrounds only** — no navy/black/charcoal fills (infographic + OG rules).
- **Approved sans-serif only** — Inter / Nunito Sans / IBM Plex Sans / Manrope; never serif.
- **`renalcarematters.com` attribution** on the sigil (§3) and OG card (§4); the wordless
  vignette hero (§1) and thumbnail (§5) stay text-free by design.
- **Filipino clinical/community context**, calm documentary realism, ≥12 varied human
  traits on the hero so it can't be mistaken for another guide's model.
