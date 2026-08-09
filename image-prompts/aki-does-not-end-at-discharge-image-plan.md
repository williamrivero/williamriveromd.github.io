# Image Plan — `aki-does-not-end-at-discharge.html`
### AKI Does Not End at Discharge — The 90-Day Pathway to Recovery, AKD, or CKD · renalcarematters.com

**Stage 1 prompt pack** for the new dual-mode (patient + clinician) cornerstone
guide *"AKI Does Not End at Discharge."* Each prompt below was authored with the
correct house image skill (`/williamriveromd-hero-vignette`,
`/williamriveromd-infographic-skill`) and is ready to paste into the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator).

Generate each at the stated size, save the PNG **and** a `.webp` twin to
`images/`, then optionally run Stage 2 (`williamriveromd-local-image-generator`)
for manifests and the `og:image` wiring. The guide already references every file
name below (hero, OG, and the four inline `<figure>` slots), so dropping the
finished assets into `images/` lights them up with no further HTML edits.

House rules applied to every prompt:

- **Light background only** (white / off-white `#fafafa` / soft gray `#f3f4f6` /
  light teal tint `#eef6f7`). Navy `#0f1e2e` and clinical teal `#1a6b72` are
  typography and accent, never a background fill.
- **Approved fonts only** — Inter, Nunito Sans, IBM Plex Sans, or Manrope. Never
  a serif font. The chosen font is named inside each prompt.
- **Attribution mandatory** — small semi-transparent `renalcarematters.com` in
  the bottom-right corner (bottom-center for the portrait algorithm) of every
  figure **except** the circular hero vignette (masked by CSS — it must stay
  wordless).
- **Palette:** navy `#0f1e2e`, clinical teal `#1a6b72`, renal green `#1f7a4d`
  (verified recovery only), amber/gold `#b8860b` (caution), clinical red
  `#b91c1c` (danger). No neon, no HDR, no dark scenes.
- **Draft honesty:** where a figure shows a threshold or recovery definition,
  keep a small teal outlined `KDIGO 2026 DRAFT` chip near it (these are
  proposed, not final).

> **Central thesis carried by every figure:** AKI can improve biochemically
> without complete biological recovery. Measure *both* kidney function and
> kidney damage, place results in context, and keep recovery under active review
> through day 90 — recovery is a trajectory and a transition of care, not a
> single "back to normal" creatinine.

---

## Plan overview

| # | Placement | File (PNG + WebP twin) | Skill | Type | Size | Priority |
|---|-----------|------------------------|-------|------|------|----------|
| Hero | `.hero-vignette` (circular) | `aki-does-not-end-at-discharge-vignette-hero.png` | hero-vignette | Journey archetype — doorway → 90-day path branching to Recovered / AKD / CKD | 2048 × 2048 | **Core** |
| OG | head `og:image` (social share card) | `aki-does-not-end-at-discharge-og.png` | infographic | 1.91:1 share card, navy + teal on off-white | 1200 × 630 | **Core** |
| 1 | §*The 0–90-day map* (`#timeline`) | `aki-does-not-end-at-discharge-01-timeline-bridge.png` | infographic | Horizontal 4-zone recovery timeline | 1792 × 1024 | **Core** |
| 2 | §*What "recovered" means* (`#recovered`) | `aki-does-not-end-at-discharge-02-five-domains.png` | infographic | Central kidney + 5 recovery-domain cards | 1792 × 1024 | **Core** |
| 3 | §*Restarting medicines* (`#medications`) | `aki-does-not-end-at-discharge-03-medication-restart.png` | infographic (algorithm) | Portrait 3-gate restart matrix | 1024 × 1536 | **Core** |
| 4 | §*If dialysis continues* (`#dialysis`) | `aki-does-not-end-at-discharge-04-akid-pathway.png` | infographic (algorithm) | AKI-D recovery process schematic | 1792 × 1024 | **Core** |

The four inline figures are already wired as `<figure class="illus-wrap
illus-wrap-light">` with rule-11 `<figcaption>` (`<p class="fig-desc">` +
`<dl class="fig-abbrevs">`) — the lightbox reads those captions, so only the
`images/` PNG+WebP files need to be produced. The hero is wired in
`figure.hero-figure > .hero-vignette` with `fetchpriority="high"`.

---

## Hero — `/williamriveromd-hero-vignette`

```
FILE NAME: aki-does-not-end-at-discharge-vignette-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold A clinical people scene (journey)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: B — Journey (one visual pathway + max 3 milestones)
CAMERA: environmental wide-angle, slight low-to-eye level, following the subject from behind-three-quarter
HUMAN VARIATION (vs. previous guides): early-40s Filipino man of average build; short neat black hair with a side part; broad face, rounded jaw, warm brown skin; wearing a soft sage-green polo and dark trousers; carrying a small hospital discharge folder; relaxed hopeful posture mid-step; morning light — deliberately different cast, wardrobe, age, and setting from recent guides
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: One glance says "leaving the hospital is the start of a 90-day recovery path, not the end of the story."

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed
to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas
diameter with a visible WHITE BORDER around the full circle (the circle must
never touch the canvas edges). Composition archetype: B — Journey. Camera:
environmental wide-angle, subject seen from a gentle behind-three-quarter angle
as he steps forward.

Subject: a Filipino man in his early forties, average build, short neat black
hair with a side part, broad rounded face and warm brown skin, wearing a soft
sage-green polo and dark trousers, walking calmly out through a bright modern
Philippine hospital doorway into soft morning daylight, holding a small
discharge folder. Ahead of him a clean light pathway curves gently into the
distance and softly splits into three faint diverging routes, suggested rather
than labelled — one bright and open, one neutral, one shaded — evoking the
possible destinations of recovery, an in-between phase, and long-term care. Keep
the branching abstract and unlabelled (no words).

Visual hierarchy: the man and the doorway occupy 60–70% of the circle; the
gently branching pathway is the 20–30% supporting element; reserve a 20–25%
TITLE SAFE ZONE of soft, uncluttered morning sky / clean pale wall in the upper
-left of the circle (no faces, anatomy, icons, or callouts inside that zone) so
the HTML title can sit beside the disc without covering important artwork.

Calm, reassuring, documentary-realistic colour grade harmonizing with clinical
teal #1a6b72 and navy #0f1e2e on a light, airy background; a single renal-green
#1f7a4d accent only on the brightest of the three forward routes. Soft edge
falloff toward a slightly deeper neutral at the rim. Full-bleed within the
inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, or
renalcarematters.com watermark.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting scenes, dozens of
icons, tiny unreadable labels, infographic clutter, duplicated people, repeated
compositions, cropped circle, cropped objects, cropped anatomy, edge clipping,
objects touching the circular border, important content inside the title safe
zone, baked-in text/titles/captions/logos/watermarks, rectangular borders /
frames / banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR,
over-saturation, distorted hands or faces, implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin —
never cropped. ONE dominant hero subject (man + doorway) at 60–70% of the circle,
the branching path as supporting element, 20–25% empty title-safe zone reserved
(soft sky / pale wall). Filipino clinical context, ≥12 traits different from
recent guides, camera framing not repeated. Crops cleanly inside the circle with
no text or subject lost at the edges. NO embedded words.
```

---

## OG share card — `/williamriveromd-infographic-skill`

```
FILE NAME: aki-does-not-end-at-discharge-og.png
IMAGE TYPE: OG / social share card
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: A calm editorial share card that reads instantly as "AKI recovery has a 90-day pathway."

PROMPT:
Publication-grade social share card for a nephrology recovery guide, exactly
1200 × 630 pixels, off-white #fafafa background, ALL typography in the Inter
sans-serif font. LEFT 58% is a mobile-safe text block: a small clinical-teal
#1a6b72 uppercase eyebrow "AKI RECOVERY • PATIENTS + CLINICIANS"; a large bold
navy #0f1e2e headline "AKI Does Not End at Discharge"; a smaller navy subhead
"The 90-day pathway to recovery, AKD, or CKD." RIGHT 42% shows a restrained,
clean clinical timeline on the light background: a simple horizontal path
beginning at a small hospital doorway icon, passing a single anatomically
accurate kidney, and ending at a "Day 90" checkpoint that softly splits into
three subtle labelled branches — "Recovered" (renal-green #1f7a4d), "AKD"
(teal #1a6b72), and "CKD" (navy #0f1e2e). Place one small amber #b8860b caution
marker at a "Day 7" point along the path. Generous whitespace, calm AJKD/NEJM
editorial aesthetic. Include a small semi-transparent navy "renalcarematters.com"
in the bottom-right corner. No people, no medical drama, no neon, no futuristic
interface.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic
stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or
black backgrounds — light backgrounds only (navy is text/accents only). Use ONLY
the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif
fonts. Keep the card exactly 1200 × 630. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
Exactly 1200 × 630, off-white background, Inter typography, mobile-readable
headline, three clean day-90 branches, one amber day-7 marker, renalcarematters.com
bottom-right. Pair with og:image:width="1200" og:image:height="630".
```

---

## Figure 1 — 0-to-90-day bridge · `/williamriveromd-infographic-skill`

```
IMAGE NUMBER: 1
SECTION PLACEMENT: §"The 0-to-90-day map" (#timeline)
FILE NAME: aki-does-not-end-at-discharge-01-timeline-bridge.png
ARCHETYPE: 3/4 — clinical timeline + multi-panel education
AUDIENCE: mixed (patients + clinicians)
VISUAL MIX: 2D infographic (dominant) · light iconography · one small 3D kidney marker
PURPOSE: Show that "AKI" becomes different labels over time, and day 7–90 (AKD) is the active recovery window.
KEY CONCEPTS: transient vs persisting AKI (first 48 h) → persistent AKI (day 2–7) → AKD (day 7–90) → CKD assessment (day 90)
DIMENSIONS: 1792 × 1024 (16:9)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical education infographic, landscape 16:9, exactly 1792 × 1024, white #ffffff
background, ALL typography in the Inter sans-serif font. Title in bold navy
#0f1e2e: "AKI Recovery Is a 90-Day Journey." Below the title, a single clean
horizontal pathway crossing the full width, divided into four proportional
labelled zones with rounded segment cards: "0–48 hours • transient or persisting
AKI" (teal #1a6b72), "48 hours–7 days • persistent AKI" (teal, slightly deeper),
"7–90 days • AKD" (amber #b8860b accent — the highlighted recovery window), and
"At 90 days • assess for CKD" (navy #0f1e2e) where the path softly splits into
three faint sub-branches (Recovered / AKD / CKD). Above the pathway, a row of
five small clean line-icons with short labels: creatinine trend, urine output,
blood pressure & volume, medication review, and urine ACR. Use renal-green
#1f7a4d only on a small "verified recovery" checkpoint marker. Include a small
boxed note in the lower area: "Feeling better is not the same as completing
follow-up." Add a small teal outlined chip reading "KDIGO 2026 DRAFT" beside the
AKD/definition zone. Generous whitespace, calm publication-grade nephrology
design, mobile-readable labels. Small semi-transparent navy "renalcarematters.com"
in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text,
unrealistic anatomy, HDR, stock-photo look, excessive saturation. NEVER use dark
backgrounds — light only. Use ONLY Inter/Nunito Sans/IBM Plex Sans/Manrope — no
serif fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
1792 × 1024, white background, four proportional timeline zones, five clean
concept icons, AKD window highlighted, KDIGO 2026 DRAFT chip present, mobile-
readable, renalcarematters.com bottom-right.
```

---

## Figure 2 — Five domains of recovery · `/williamriveromd-infographic-skill`

```
IMAGE NUMBER: 2
SECTION PLACEMENT: §"When is AKI truly recovered?" (#recovered)
FILE NAME: aki-does-not-end-at-discharge-02-five-domains.png
ARCHETYPE: 2/5 — central 3D component + modular reference cards
AUDIENCE: mixed (patients + clinicians)
VISUAL MIX: one central 3D kidney · five 2D domain cards · clean icons
PURPOSE: Recovery is judged across five domains, not one creatinine number.
KEY CONCEPTS: filtration · kidney damage · electrolytes & volume · clinical resilience · dialysis independence
DIMENSIONS: 1792 × 1024 (16:9)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Publication-grade biomedical education infographic, landscape 16:9, exactly
1792 × 1024, white #ffffff background, ALL typography in the Inter sans-serif
font. Center: one anatomically accurate pair of human kidneys in restrained
renal red-brown, semi-photorealistic 3D render, softly lit. Around the kidneys,
arrange FIVE equal rounded cards connected to the center by thin neutral lines
(NOT implying a sequence), each with one clean line-icon, a short bold navy
#0f1e2e heading and a single short question: "Filtration — is it filtering
again?", "Kidney damage — any protein leak?", "Electrolytes + volume — is
balance restored?", "Clinical resilience — still fragile when ill?", and
"Dialysis independence — still needed?". Use clinical teal #1a6b72 for headings
and rules, renal-green #1f7a4d on the filtration/positive card accent, one amber
#b8860b accent on the "kidney damage" card. Footer strip in navy: "Creatinine
answers one part of recovery — not all of it." Generous whitespace, calm,
restrained clinical palette, mobile-readable. Small semi-transparent navy
"renalcarematters.com" in the bottom-right corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text,
unrealistic anatomy, HDR, stock-photo look, excessive saturation, futuristic or
neon rendering. NEVER use dark backgrounds — light only. Use ONLY Inter/Nunito
Sans/IBM Plex Sans/Manrope — no serif fonts. Never omit the renalcarematters.com
attribution.

QUALITY CHECK:
1792 × 1024, white background, ONE accurate central kidney, five equal non-
sequential domain cards each with one icon and one short question, footer take-
home line, mobile-readable, renalcarematters.com bottom-right.
```

---

## Figure 3 — Medication restart matrix · `/williamriveromd-infographic-skill` (clinical algorithm)

```
IMAGE NUMBER: 3
SECTION PLACEMENT: §"Restarting medicines" (#medications)
FILE NAME: aki-does-not-end-at-discharge-03-medication-restart.png
ARCHETYPE: 3 — clinical algorithm / decision gates
AUDIENCE: mixed (patients + clinicians)
VISUAL MIX: 2D algorithm · rounded decision gates · color-coded class rows
PURPOSE: There is no single "safe day" — restart runs through indication × readiness × monitoring.
KEY CONCEPTS: three gates (indication, physiology, monitoring) applied per drug class
DIMENSIONS: 1024 × 1536 (2:3 portrait)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical nephrology algorithm infographic, portrait 2:3, exactly 1024 × 1536,
off-white #fafafa background, ALL typography in the Inter sans-serif font. Title
in bold navy #0f1e2e: "Restarting Medicines After AKI." Below it, three stacked
rounded decision gates connected by clean navy connectors, each numbered: gate 1
"Indication still present?", gate 2 "Acute illness resolved & physiology
stable?", gate 3 "Monitoring arranged?" Use teal #1a6b72 for the gate frames.
Below the gates, four restrained color-coded class rows as rounded cards, each
with a short "Check before restart" and "Check after restart" line: ACEi/ARB,
SGLT2 inhibitor, Diuretic, Metformin. Use green #1f7a4d, teal #1a6b72, amber
#b8860b accents sparingly to distinguish rows (never neon). Add a prominent amber
#b8860b note near the bottom: "Do not restart or stop prescription medicines on
your own." Include a small teal outlined chip "KDIGO 2026 DRAFT" beside the
ACEi/ARB row. High legibility, generous whitespace, no pills spilling, no brand
logos. Small semi-transparent navy "renalcarematters.com" in the bottom-center.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, spaghetti flowchart, clutter, tiny unreadable labels, AI
gibberish text, unrealistic anatomy, HDR, stock-photo look, excessive saturation,
brand logos, spilled pills. NEVER use dark backgrounds — light only. Use ONLY
Inter/Nunito Sans/IBM Plex Sans/Manrope — no serif fonts. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
1024 × 1536 portrait, off-white background, three numbered gates, four class rows
with before/after checks, prominent amber self-medication warning, KDIGO 2026
DRAFT chip, mobile-readable, renalcarematters.com bottom-center.
```

---

## Figure 4 — AKI-D recovery pathway · `/williamriveromd-infographic-skill` (clinical process)

```
IMAGE NUMBER: 4
SECTION PLACEMENT: §"Dialysis after AKI may still be temporary" (#dialysis)
FILE NAME: aki-does-not-end-at-discharge-04-akid-pathway.png
ARCHETYPE: 3/8 — clinical process schematic with a monitoring loop
AUDIENCE: mixed (patients + clinicians)
VISUAL MIX: 2D process schematic · a circular monitoring loop · two endpoint cards
PURPOSE: Dialysis-requiring AKI is a recovery-focused condition; look actively for returning function.
KEY CONCEPTS: AKI-D discharge → weekly recovery-monitoring loop → trial off dialysis vs prepare long-term therapy
DIMENSIONS: 1792 × 1024 (16:9)

COPY-READY IMAGE GENERATOR GPT PROMPT:
Clinical process schematic infographic, landscape 16:9, exactly 1792 × 1024,
white #ffffff background, ALL typography in the Inter sans-serif font. Title in
bold navy #0f1e2e: "Dialysis After AKI May Still Be Temporary." LEFT: a rounded
card "Hospital discharge" tagged with a small teal #1a6b72 label "AKI-D".
CENTER: a clean circular recovery-monitoring loop (teal arrows) whose six nodes
read: "predialysis creatinine & BUN", "urine output", "timed clearance",
"BP & weight", "symptoms", and "avoid intradialytic hypotension". RIGHT: two
balanced clinician-led endpoint cards side by side — "Trial off dialysis when
kidney function can meet demand" (renal-green #1f7a4d accent) and "Prepare
long-term kidney replacement therapy when needed" (navy #0f1e2e accent) — drawn
as two equally weighted destinations, neither dominating. Put a small amber
#b8860b caution ring around the "avoid intradialytic hypotension" node. Footer in
navy: "No single number should stop dialysis." Do not let permanent-access
imagery dominate the recovery side. Calm publication-grade design, mobile-
readable. Small semi-transparent navy "renalcarematters.com" in the bottom-right
corner.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, spaghetti flowchart, clutter, tiny unreadable labels, AI
gibberish text, unrealistic anatomy, HDR, stock-photo look, excessive saturation.
NEVER use dark backgrounds — light only. Use ONLY Inter/Nunito Sans/IBM Plex
Sans/Manrope — no serif fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
1792 × 1024, white background, AKI-D discharge card, six-node circular monitoring
loop, two balanced endpoint cards, amber caution on the hypotension node, footer
take-home line, mobile-readable, renalcarematters.com bottom-right.
```

---

## Production notes

1. **Order of generation.** Produce the **Hero** and **OG** first (they gate the
   page's LCP and social preview), then Figures 1 → 4.
2. **File twins.** For each PNG, export a matching `.webp` at the same base name
   (e.g. via `cwebp -q 82`). The guide's `<picture>` blocks already point at both.
3. **Alt text is already in the HTML.** Each inline `<figure>` carries a
   descriptive `alt` and a rule-11 `<figcaption>` (`fig-desc` + `fig-abbrevs`) —
   do not bake those words into the image.
4. **Draft chips.** Figures 1 and 3 must keep the small teal outlined
   `KDIGO 2026 DRAFT` chip — the recovery definitions and restart guidance are
   proposals from the March 2026 public-review draft, not final guidance.
5. **Consistency.** All six assets share the same off-white/white ground, the
   navy+teal+green+amber palette, and Inter typography so the guide reads as one
   system. The OG card and Figure 1 both use the doorway→90-day→three-branch
   motif, tying the share card to the on-page timeline.
6. **Stage 2 (optional).** Hand this pack to
   `williamriveromd-local-image-generator` to build `image-manifest.csv/json`
   and confirm the `og:image` width/height tags (already set to 1200 × 630 in the
   guide `<head>`).
