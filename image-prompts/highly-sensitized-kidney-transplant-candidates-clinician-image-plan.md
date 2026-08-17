# Image Plan — `highly-sensitized-kidney-transplant-candidates-clinician.html`
### Highly Sensitized Kidney Transplant Candidates — Expanding Donor Access Without Losing Immunologic Safety · renalcarematters.com

**Stage 1 prompt pack** for the new clinician-only guide *"Highly Sensitized
Kidney Transplant Candidates."* Each prompt below was authored with the correct
house image skill (`/williamriveromd-hero-vignette`,
`/williamriveromd-infographic-skill`,
`/williamriveromd-biomedical-mechanism-figure`,
`/williamriveromd-simple-figure`) and is ready to paste into the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator).

Generate each at the stated size, save the PNG **and** a `.webp` twin to
`images/` using the **exact filenames below** (they are already wired into the
guide's `<picture>`/`<meta>` tags — just drop the files in), then optionally run
Stage 2 (`williamriveromd-local-image-generator`) for manifests and og:image
validation.

House rules applied to every prompt:

- **Light background only** (white / off-white / soft gray / light teal tint).
  Navy `#0f1e2e`, clinical teal `#1a6b72`, renal green `#1f7a4d`, amber
  `#b8860b`, clinical red `#b91c1c` are typography and accent, never a page fill.
- **Approved fonts only** — Inter, Nunito Sans, IBM Plex Sans, or Manrope.
  Never a serif font.
- **Attribution mandatory** — small semi-transparent `renalcarematters.com`
  bottom-right (bottom-center for portrait) of every figure *except the circular
  hero vignette*, which is masked by CSS and must carry **no text at all**.
- **English-only on-image text.** Single-mode clinician guide — no
  Tagalog / Cebuano / Kapampangan strings inside any figure.

> **Central thesis every figure must protect:** *cPRA is an access number; DSA
> and crossmatch are donor-specific risk numbers — never trade one for the
> other.* And the guardrail baked into the mechanism and timeline art: **MFI is
> an assay signal, not a measure of injury, and never a universal safe cutoff.**

---

## Plan overview

| # | Placement | File (PNG + WebP twin) | Skill | Type | Size | Priority |
|---|-----------|------------------------|-------|------|------|----------|
| Hero | `.hero-vignette` (circular, wordless) | `highly-sensitized-kidney-transplant-candidates-clinician-hero.png` | hero-vignette | Calm 3D donor-kidney still, protective translucent gate/shield motif | 2048 × 2048 | **Core** |
| OG | head `og:image` (social share card) | `highly-sensitized-kidney-transplant-candidates-clinician-og.png` | infographic | 1.91:1 share card — kidney between a wide cPRA gate and a narrow DSA shield | 1200 × 630 | **Core** |
| 1 | §3 *Vocabulary* — injury-pathway figure | `highly-sensitized-kidney-transplant-candidates-clinician-01-injury-pathway.png` | biomedical-mechanism-figure | Organ → capillary-endothelium inset → injury / modifier / outcome flow | 1792 × 1024 | **Core** (signature mechanism) |
| 2 | §5 *Timeline* — historical vs persistent DSA | `highly-sensitized-kidney-transplant-candidates-clinician-02-antibody-timeline.png` | simple-figure | Two-trajectory DSA-vs-time comparison across a shared threshold line | 1792 × 1024 | **Core** |
| 3 | §8 *Access Hierarchy* — the staircase | `highly-sensitized-kidney-transplant-candidates-clinician-03-access-staircase.png` | simple-figure | Vertical ascending decision staircase, green→amber risk gradient | 1024 × 1536 | **Core** |

The guide body already contains each `<figure class="guide-fig">` with a
plain-language `<figcaption>` and abbreviation `<dl>` for the lightbox — you are
only replacing the placeholder PNG/WebP files in `images/`. The hero already
ships `fetchpriority="high" loading="eager"`.

**Optional follow-on figures** (not currently wired into the HTML — add a
`<figure>` + regenerate patchers if you want them): a *"cPRA is not DSA"*
two-question comparison (§1), a *"delisting changes the list, not the antibody"*
split panel (§7), and a *SAB/MFI pitfalls* reference card (§4). Prompts for
those can be produced on request with the same skills.

---

## 1 · Hero (circular vignette) — `williamriveromd-hero-vignette`

```
FILE NAME: highly-sensitized-kidney-transplant-candidates-clinician-hero.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold C (calm 3D anatomy / object hero)
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: I — Object Hero (single dominant render + minimal supporting detail)
CAMERA: three-quarter studio view, slightly above the organ
HUMAN VARIATION (vs. previous guide): no people
AUDIENCE: clinicians
VISUAL GOAL: A single donor kidney held safely behind a soft translucent gate/shield — "expand access, protect the graft" — read at a glance, wordless.

PROMPT:
Square 1:1 semi-photorealistic 3D medical illustration on a 2048×2048 canvas,
composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the
canvas diameter with a visible WHITE BORDER around the full circle (the circle
must never touch the canvas edges). Composition archetype: I — Object Hero.
Camera: gentle three-quarter view from slightly above.

Subject: one clean, anatomically accurate human donor kidney in restrained
renal tones (soft crimson-brown parenchyma, a pale hilar vessel and ureter),
rendered as the single dominant object floating on a soft, uncluttered light
teal-tinted (#eef6f7) background with gentle studio lighting and a soft contact
shadow. Around the kidney, suggest immunologic "access versus safety" purely
through form: a wide, faint translucent teal archway or gate opening on one
side (evoking a broad donor population passing through) and, closer to the
organ, a smaller, crisper translucent shield/curve of soft teal glass partly
in front of the kidney (evoking donor-specific protection). Keep these motifs
abstract, glassy, and subtle — no icons, no letters, no diagram lines.

Visual hierarchy: the kidney occupies 60–70% of the circle; the gate and shield
motifs are 20–30% supporting context; reserve a clean 20–25% TITLE SAFE ZONE of
empty soft-gradient background on the upper-left (no anatomy, glass, leader
lines, or callouts in that zone) so the HTML <h1> can sit beside the disc. Soft
edge falloff toward a slightly deeper neutral at the rim. Calm, publication-grade,
premium-medical-textbook mood.

Absolutely NO text, labels, leader lines, callouts, titles, logos, or watermark
— clean render only. Full-bleed within the inscribed circle, no rectangular
borders, frames, or banners.

NEGATIVE INSTRUCTIONS:
Avoid busy layouts, collage overload, more than four supporting elements, any
icons, tiny labels, infographic clutter, duplicated organs, cropped circle,
cropped anatomy, edge clipping, objects touching the circular border, important
content inside the title safe zone, baked-in text / titles / captions / logos /
watermarks, rectangular borders or banners, dark / charcoal / black backgrounds,
cartoon style, neon, HDR, over-saturation, implausible anatomy.

QUALITY CHECK:
Square 2048×2048. Circle occupies 85–90% of canvas with a visible white margin —
never cropped. ONE dominant hero subject (the kidney) at 60–70% of the circle,
2–3 subtle supporting glass motifs, 20–25% empty title-safe zone reserved (soft
gradient, no anatomy/glass/callouts inside). Restrained clinical color on a light
teal-tinted ground. Crops cleanly inside the circle with no subject lost at the
edges. Contains zero text.
```

---

## 2 · OG / social share card — `williamriveromd-infographic-skill`

```
FILE NAME: highly-sensitized-kidney-transplant-candidates-clinician-og.png
IMAGE TYPE: OG / social share card (Archetype 1 — editorial share card with title)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: clinicians
VISUAL GOAL: One glance conveys the guide's thesis — a donor kidney between a wide "cPRA" population gate and a narrow "DSA + crossmatch" shield — with a clean clinician title block.

PROMPT:
Publication-grade social share card for a clinician nephrology guide, exactly
1200 × 630, off-white (#fafafa) background, clean layout, Inter typography.
LEFT 58% is a text-safe block: a small eyebrow line in clinical teal (#1a6b72)
reading "TRANSPLANT IMMUNOLOGY · CLINICIANS"; below it a large bold navy
(#0f1e2e) headline "Highly Sensitized Kidney Transplant Candidates"; below that
a lighter navy subhead "Expanding donor access without losing immunologic
safety." Keep the type hierarchy strong and mobile-legible.

RIGHT 42% is a restrained clinical illustration on the same light ground: a
single anatomically accurate donor kidney in soft renal tones positioned between
two translucent gates rendered as clean flat-vector glass — a WIDE teal archway
labeled in small caps "cPRA" (the population-access gate, drawn open and broad)
and, nearer the kidney, a NARROW shield shape labeled "DSA + CROSSMATCH" (the
donor-specific risk gate, drawn as a crisp protective shield). One small amber
(#b8860b) caution dot is the only warm accent. No other objects.

Calm, premium, KDIGO/NEJM-graphical-abstract restraint. Generous negative space.
Bottom-right corner: "renalcarematters.com" in small semi-transparent navy text
(~11px, 70% opacity). No patient faces, no logos, no futuristic or molecular
clutter.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI
gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid generic
stock-photo look, avoid excessive saturation. NEVER use dark, navy, charcoal, or
black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter,
Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative typefaces.
Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Exactly 1200 × 630 (pair with og:image:width="1200" og:image:height="630", already
set in the guide). Mobile-readable title, clinically plausible kidney, calm and
publication-grade. Light background. Only two on-image labels ("cPRA", "DSA +
CROSSMATCH") plus the title block — no paragraph text. renalcarematters.com visible
bottom-right.
```

---

## 3 · Figure 1 — HLA sensitization injury pathway — `williamriveromd-biomedical-mechanism-figure`

```
FILE NAME: highly-sensitized-kidney-transplant-candidates-clinician-01-injury-pathway.png
IMAGE TYPE: Biomedical mechanism schematic (organ → magnified inset → injury/modifier/outcome flow)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: Trace how a donor-specific antibody injures a graft — and show that a negative crossmatch and adequate immunosuppression lower, but never erase, the risk.

PROMPT:
Create a publication-grade biomedical mechanism schematic in the scientific
review-article style, white (#ffffff) background, flat vector illustration with
soft semi-3D shading, thin dashed connector boxes, muted clinical palette (light
gray-blue anatomy, soft yellow highlight on the affected segment, red for
antibody/complement injury, blue for the protective modifier). Clean sans-serif
labels in Inter. Title top-left in bold navy (#0f1e2e): "How HLA sensitization
can injure a donor kidney."

LEFT — organ-level panel: a simplified transplanted donor kidney with its vascular
pedicle, labeled "Donor graft (HLA-sensitized recipient)". A thin dashed connector
box points from a peritubular/glomerular capillary to the magnified panel.

CENTER/RIGHT — magnified functional-unit inset (dashed border): a cross-section of
a graft microvascular capillary lined by endothelium. Show, in order along the
endothelium, concise red callouts:
- "Anti-HLA IgG (DSA) binds donor HLA on endothelium"
- "Complement fixation (C1q → membrane attack complex)"
- "Fc-receptor immune cells recruited (NK cell, macrophage)"
- "Microvascular inflammation → antibody-mediated rejection (AMR)"
Highlight the injured endothelial segment in soft yellow.

BOTTOM — three-box summary flow with left-to-right arrows:
- LEFT pale-pink pathology box "Injury drivers": prior exposure (pregnancy /
  transfusion / prior transplant) → memory B cells + long-lived plasma cells →
  circulating anti-HLA IgG.
- CENTER pale-blue modifier box "Risk modifier (not erasure)": negative crossmatch
  + adequate immunosuppression + no current DSA — lowers injury probability.
- RIGHT pale-blue outcome box "Outcome spectrum": no measurable injury →
  subclinical injury → active AMR; immune memory persists, so risk is reduced,
  not removed.

Add a small footnote strip in muted gray, bottom-center: "MFI estimates assay
signal — it does not measure injury." Bottom-right corner: "renalcarematters.com"
in small semi-transparent navy text (~11px, 70% opacity).

Keep generous whitespace, legible slide-size labels, correct anatomy, no invented
numeric thresholds.

NEGATIVE INSTRUCTIONS:
Avoid photorealism, dark backgrounds, decorative effects, drop shadows, cartoonish
styling, overcrowding, tiny unreadable labels, AI gibberish text, anthropomorphic
antibodies, DNA-helix decoration, invented lab numbers. Use ONLY Inter / Nunito
Sans / IBM Plex Sans / Manrope — never a serif font. Never omit the
renalcarematters.com attribution.

QUALITY CHECK:
White background, muted clinical palette, dashed inset border, organ→inset→
injury/modifier/outcome structure intact. Anatomically plausible capillary and
immune cells. The "risk modifier, not erasure" box and the "MFI ≠ injury" footnote
are both present. Mobile/slide-readable. renalcarematters.com bottom-right.
```

---

## 4 · Figure 2 — historical vs persistent DSA timeline — `williamriveromd-simple-figure`

```
FILE NAME: highly-sensitized-kidney-transplant-candidates-clinician-02-antibody-timeline.png
IMAGE TYPE: Simple figure — Scaffold B adapted to a two-trajectory timeline comparison
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians
VISUAL GOAL: A historical DSA that has cleared is not the same as a persistent DSA — and the observed composite event rates diverge accordingly.

PROMPT:
Medical education comparison infographic, AJKD/NEJM graphical-abstract style,
white (#ffffff) background. Title centered at top in bold navy (#0f1e2e): "A
historical DSA is not a persistent DSA." Subtitle in clinical teal (#1a6b72):
"Donor-specific antibody strength over time, read against the program threshold."

Draw ONE shared horizontal time axis labeled left-to-right: "Sensitizing exposure
→ Peak → Decline → Transplant → Early post-transplant." Draw ONE horizontal dashed
reference line across the middle labeled "Program MFI threshold (assay-specific)".
Overlay TWO curves:
- A renal-green (#1f7a4d) curve "Historical, cleared DSA": rises to a peak, falls
  clearly BELOW the threshold line before the Transplant mark, then shows a small
  early rebound bump just above threshold after transplant, tagged "immune memory
  remains — rebounds, then surveilled."
- A clinical-red (#b91c1c) curve "Persistent DSA": rises and stays ABOVE the
  threshold line through the Transplant mark, tagged "persistent donor-specific
  burden."

On the right, two compact rounded stat cards on soft gray (#f3f4f6):
- green card "Historical-cleared" — big number "9.8%" over small label "composite
  graft loss / death (observed)".
- red card "Persistent DSA >2000 MFI" — big number "24.4%" over the same small
  label.
Below the cards, a small muted-gray caption: "Observational French cohort
(Usureau 2026); not a universal MFI rule."

Generous whitespace, mobile-readable labels in Inter, bold navy title. Bottom-right
corner: "renalcarematters.com" in small semi-transparent navy text (~11px, 70%
opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid unrealistic charts, avoid overprocessed HDR, avoid excessive saturation.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use
ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif
fonts. Never omit the renalcarematters.com attribution. Do not add invented numbers
beyond the two shown (9.8%, 24.4%).

QUALITY CHECK:
White background, one shared time axis, one dashed threshold line, two clearly
distinguishable curves (green cleared vs red persistent), the two stat cards
(9.8% / 24.4%) and the "observational cohort, not a universal MFI rule" caption
present. Mobile-readable. renalcarematters.com bottom-right.
```

---

## 5 · Figure 3 — access-strategy staircase — `williamriveromd-simple-figure`

```
FILE NAME: highly-sensitized-kidney-transplant-candidates-clinician-03-access-staircase.png
IMAGE TYPE: Simple figure — vertical ascending decision staircase (Scaffold C adapted, portrait)
ASPECT RATIO: 2:3 portrait
PIXEL DIMENSIONS: 1024 × 1536
AUDIENCE: clinicians
VISUAL GOAL: Work up the staircase — exhaust the lowest-immunologic-risk access route likely to deliver a transplant before climbing to higher-risk strategies.

PROMPT:
Clean clinical education infographic, portrait 1024 × 1536, white (#ffffff)
background. Title at top center in bold navy (#0f1e2e): "Expanding access for a
highly sensitized candidate." Subtitle in clinical teal (#1a6b72): "Choose the
lowest-risk pathway likely to deliver a transplant in an acceptable time."

Draw an ascending STAIRCASE of eight rounded rectangular step-cards climbing from
bottom-left to top-right, each a tread of the stair, connected by a thin upward
navy arrow along the left. Bottom steps use renal green (#1f7a4d) accent, middle
steps clinical teal (#1a6b72), upper steps amber (#b8860b) — a smooth
lower-risk-to-higher-complexity gradient. Each card: a short bold label only.
From bottom to top:
1. "Prevent avoidable sensitization" (patient blood management)
2. "Compatible living-donor transplant"
3. "Kidney paired exchange (KPE)"
4. "Compatible deceased-donor priority"
5. "Acceptable-mismatch / permissible-antigen program"
6. "Candidate-specific delisting" (very high cPRA, selected)
7. "HLA-incompatible transplant / desensitization"
8. "Imlifidase-enabled transplant" (narrow, licensed, expert)

A slim vertical gradient ribbon along the right edge runs from a green bottom
label "Lower immunologic risk" to an amber top label "Higher immunologic
complexity." A small muted-gray footnote at the bottom: "A starting order, not a
rule — do not leave a candidate at a rung with negligible match probability."

Generous whitespace, mobile-readable labels in Inter, no more than eight steps.
Bottom-center (portrait convention): "renalcarematters.com" in small
semi-transparent navy text (~11px, 70% opacity).

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish
text, avoid spaghetti connectors, avoid overprocessed HDR, avoid excessive
saturation. NEVER use dark, navy, charcoal, or black backgrounds — light
backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans,
or Manrope — no serif fonts. Never omit the renalcarematters.com attribution.

QUALITY CHECK:
Portrait 1024 × 1536, white background, exactly eight ascending step-cards in the
stated order with a green→teal→amber risk gradient and a right-edge low→high risk
ribbon. The "starting order, not a rule" footnote is present. Mobile-readable, no
clutter. renalcarematters.com bottom-center.
```

---

## Production notes

1. **Filenames are load-bearing.** The guide's `<picture>` sources and
   `og:image` meta already point at the five basenames above. Save each render as
   both `<name>.png` and a `<name>.webp` twin in `images/`; no HTML edit is
   needed once the files exist.
2. **Hero stays wordless.** The `.hero-vignette` disc is CSS-masked and the
   guide's `<h1>` sits beside it — any baked text or watermark on the hero will
   be clipped or will duplicate the title. The hero is the *only* asset with no
   `renalcarematters.com` corner mark.
3. **Every other figure carries the attribution** (`renalcarematters.com`,
   bottom-right; bottom-center for the portrait staircase) and uses an approved
   sans-serif on a light background — per the loaded house skills.
4. **Numbers are frozen to the guide.** Only the two verified cohort figures
   (9.8% / 24.4%, Usureau 2026) appear on-image, with the "observational cohort,
   not a universal MFI rule" caption. Do not let the generator invent MFI cutoffs,
   pressures, or additional percentages.
5. **Alt text already exists** in the HTML for all five images — regenerating the
   art does not change the alt/figcaption, which the lightbox reads.
6. **Optional Stage 2:** hand this pack to `williamriveromd-local-image-generator`
   for manifest/og:image validation, or generate manually in the Image Generator
   GPT and drop the files in.
