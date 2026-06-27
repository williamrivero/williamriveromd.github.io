# Image Plan — `philhealth-acr-to-drg.html`
### From All Case Rates to DRG — What PhilHealth's Payment Overhaul Means for Filipino Patients · williamriveromd.com

**Stage 1 prompt pack** for the four raster assets the guide references. Each
figure is authored with the correct house skill. Generate in the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator),
save the PNG (+ `.webp` twin) outputs into `images/`, then optionally run
Stage 2 (`williamriveromd-local-image-generator`) for manifests.

House rules applied to every prompt: **light background only** (navy/teal are
typography + accent, never a fill), the navy/teal/green/amber/red palette,
sans-serif type (Inter / Nunito Sans / IBM Plex Sans / Manrope), mobile-readable
labels, and the mandatory `williamriveromd.com` attribution bottom-right
(bottom-center for portrait).

> **On-image text is English only** — matching every other Perspectives guide
> (HMO, Filipino-nephrologist-challenges). The four-language toggle lives in the
> HTML body text, not inside the raster images.

---

## Plan overview

| # | Section / use | File | Skill | Type | Size | Priority |
|---|---|---|---|---|---|---|
| 1 | Hero circular vignette (beside `<h1>`) | `philhealth-acr-to-drg-vignette-hero.png` | hero-vignette | Scaffold A — people scene | 1024 × 1024 (1:1) | **Core** |
| 2 | §1 The Case — pull-quote card | `philhealth-acr-to-drg-marvin-quote.png` | infographic | Editorial quote card (1:1) | 1024 × 1024 (1:1) | **Core** |
| 3 | §3 Why ACR Is Breaking — chart | `philhealth-acr-to-drg-rate-vs-cost.png` | simple-figure | Single-panel concept (D) | 1792 × 1024 (16:9) | **Core** |
| 4 | OG / Twitter share card | `philhealth-acr-to-drg-og.png` | infographic | OG editorial poster | **1200 × 630 (fixed)** | **Core** |
| 5 | §2 Two Different Problems — split diagram | `philhealth-acr-to-drg-two-problems.png` | simple-figure | Side-by-side comparison (B) | 1792 × 1024 (16:9) | **Core (thesis visualizer)** |
| 6 | §7 The Kidney Lens — CKD cardiorenal storm → DRG forks | `philhealth-acr-to-drg-kidney-lens.png` | simple-figure | Single-panel concept (D) | 1792 × 1024 (16:9) | **Core (specialty angle)** |

> Note on `<img width/height>` attributes already in the guide HTML:
>
> - hero `width="1254" height="1254"` — square, will work with the new
>   1024×1024 hero (CSS does the round mask + ring). Bump to `1024 1024` if you
>   want the markup to match exactly.
> - marvin-quote `width="1200" height="900"` — change to `1024 1024` when the
>   final square card is saved.
> - rate-vs-cost `width="1200" height="800"` — change to `1792 1024` when the
>   16:9 landscape is saved.
> - OG `og:image:width="1200" og:image:height="630"` — already correct.

---

## 1 · Hero vignette — billing window, ACR-sheet vs DRG-tablet
*Skill: williamriveromd-hero-vignette · Scaffold A — Filipino clinical people scene*

> Square, masked into the round hero disc. No baked-in text or logos. Faces
> sit in the upper-middle (~42% from top) so the CSS circle crop doesn't lose
> the key detail.

```
FILE NAME: philhealth-acr-to-drg-vignette-hero.png
IMAGE TYPE: Circular vignette hero — Scaffold A (people scene)
ASPECT RATIO: 1:1 (square — displayed circle-cropped)
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Capture the human moment the whole essay turns on — a Filipino family at a Philippine hospital billing window, with a clerk who has one foot in the old paper case-rate world and one foot in the new DRG severity-grouper world.

PROMPT:
Square 1:1 photorealistic editorial photograph for a medical guide hero image, composed to be cropped into a CIRCLE. A Filipino family on one side of a hospital billing window — a calm working-age son in a clean polo standing close to his elderly mother in a soft cardigan; she's holding a folded paper and a blue PhilHealth member card. On the other side of the counter, a Filipino billing clerk in a light teal uniform looks attentively at them; on her counter sit a printed paper "case-rate" sheet (a one-page rate table, unreadable typography, no legible words) next to a small clinical tablet whose screen shows a clean, simplified bar / ladder graphic suggesting a severity grouper — only abstract bars in clinical teal #1a6b72 and navy #0f1e2e, no readable text. Setting: a bright modern Philippine private-hospital lobby billing window with soft daylight through tall windows, light teal-tinted clean walls. Mood: serious, civic, hopeful-but-cautious — not despairing, not cheery. The family looks worried but composed; the clerk looks empathetic. Compose the three faces and the hands holding the PhilHealth card in the UPPER-MIDDLE of the frame (about 38–48% from the top), fully inside a centered circular safe zone — keep all four corners empty soft background, since the image will be masked to a circle. Background falls off into a slightly deeper light-teal / warm neutral tone toward the edges. Light, airy, professional color grade harmonizing with teal #1a6b72 and navy #0f1e2e, with a small renal-green accent on a lanyard or sign element. Absolutely NO text, NO title, NO captions, NO logos (no real PhilHealth logo, no hospital signage with readable words), NO graphic overlays, NO watermark on the image itself — a clean photograph only. Full-bleed, no borders or frames.

NEGATIVE INSTRUCTIONS:
No text of any kind (no title, subtitle, captions, numbers, labels, logo, or williamriveromd.com watermark — the page footer carries attribution; a baked watermark would be clipped by the circle). No rectangular borders, frames, banners, or UI chrome. No important content in the corners (they get clipped by the circle). No dark, navy, charcoal, or black background. Avoid cartoon style, clutter, over-saturation, HDR, distorted hands/faces, implausible anatomy, or stocky staged poses. Do NOT render an accurate PhilHealth logo, hospital name signage, or any readable Filipino/English text inside the scene.

QUALITY CHECK:
Square 1:1. Three faces (mother, son, clerk) and the hands holding the PhilHealth card centered in the circular safe zone with empty soft corners. Faces and key detail in the upper-middle (~42% from top). Light, calm, Filipino clinical context, publication-grade. Crops cleanly to a circle with no text or subject lost at the edges.
```

---

## 2 · Pull-quote card — "the moral one"
*Skill: williamriveromd-infographic-skill · Editorial typographic card (Archetype 1 / quote-card variant)*

> A typographic-only card used inside §1 ("The Case"). It is the closing-quote
> on the Marvin frame and should feel like an editorial pull-quote, not a
> stocky social tile.

```
FILE NAME: philhealth-acr-to-drg-marvin-quote.png
IMAGE TYPE: Editorial pull-quote card — typographic only
ASPECT RATIO: 1:1
PIXEL DIMENSIONS: 1024 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: A quiet, paper-feel pull-quote that anchors the Marvin section's moral argument with the essay's thesis line.

PROMPT:
Square 1:1 editorial pull-quote card, publication-grade nephrology design. Light warm cream background (#f8f5f0) with a very subtle paper-grain texture, soft warm vignette in the corners. Centered typographic composition with generous whitespace.

Decorative mark — top-left corner: a small, restrained line-art glyph in clinical teal (#1a6b72) at about 8% opacity — a tiny stethoscope curl OR a stylized PhilHealth-style member card outline (no logo, no text), no larger than ~7% of the canvas, used only as a quiet visual mark.

Opening quote glyph — a large stylized opening quotation mark in clinical teal (#1a6b72) at ~25% opacity, sitting just above and slightly left of the headline block, sized to ~14% of the canvas height. Do not double it at the end of the quote.

Main quote block — large, set in bold Inter or Manrope (sans-serif), navy (#0f1e2e), centered, 4–6 lines, with line-height generous enough to breathe. The text must read EXACTLY:

"A family contributes for 25 years, and a technical rule erases the benefit at the worst possible moment. That is not an actuarial problem — it is a moral one."

Below the quote, a short hairline rule in clinical teal (#1a6b72) about 80–100 px wide, centered.

Attribution line under the rule, smaller, set in medium clinical teal (#1a6b72), all-caps tracking widened slightly, single line, centered, exactly:

— W. RIVERO, MD · A NEPHROLOGIST'S PERSPECTIVE

Bottom-right corner: small semi-transparent navy text "williamriveromd.com" at ~10–11 px equivalent, 70% opacity.

Use ONLY sans-serif type (Inter or Manrope). No serif fonts. No additional text, no numbering, no decorative flourishes beyond the small corner glyph and the opening quote mark. Restrained palette: cream background, navy quote text, teal accents.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid AI mis-spellings — the quote must be reproduced exactly as written. NEVER use dark, navy, charcoal, or black backgrounds — cream / off-white only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative or handwritten typefaces. Do not draw the real PhilHealth logo or any hospital wordmark. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Quote text is rendered verbatim, perfectly spelled, in bold sans-serif navy on cream. Attribution line is teal, single line, exact wording. Single restrained corner mark only. Bottom-right attribution williamriveromd.com is visible and unobtrusive. Mobile-readable when scaled into a 600 px-wide guide column.
```

---

## 3 · Rate vs Cost across severity — the ACR under-reimbursement gap
*Skill: williamriveromd-simple-figure · Scaffold D — single-panel concept figure*

> The visual centerpiece of §3 ("Why ACR Is Breaking"). One clean editorial
> chart showing the flat ACR line against a rising real-cost line over three
> severity tiers, with the under-reimbursement gap shaded as the figure's
> takeaway message.

```
FILE NAME: philhealth-acr-to-drg-rate-vs-cost.png
IMAGE TYPE: Simple figure — single-panel concept chart (Scaffold D, editorial graphical abstract)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Make the flat-rate-vs-real-cost mismatch visible at a glance, and name the shaded gap as the patient's balance-billed amount.

PROMPT:
Clean editorial graphical-abstract figure, publication-grade nephrology / health-policy design. White (#ffffff) background. Sans-serif typography only (Inter).

Title at top center, bold navy (#0f1e2e): "When the Case Rate Stops Matching the Bill". Subtitle below in clinical teal (#1a6b72), smaller: "ACR pays the same flat amount no matter how sick the patient was".

Main panel — a single clean Cartesian plot, centered:
  - X-axis: three evenly spaced category tiers labeled in bold navy below the axis: "Mild", "Moderate", "Severe". Small subtitle under the axis in muted navy: "Severity of admission". Subtle navy axis line, no heavy gridlines.
  - Y-axis: peso amounts increasing upward. Y-axis label vertical, navy: "Cost per admission (₱)". Tick labels formatted with the Filipino peso sign: ₱0, ₱50K, ₱100K, ₱150K, ₱200K, ₱250K — clean rounded sans-serif numerals, no decimals.
  - Series A — "ACR — flat case rate": a single perfectly horizontal line in navy (#0f1e2e) ~3 px stroke, sitting at about the ₱40K–₱50K level across all three tiers. Three small navy filled circles mark the tier midpoints. Label the line at the right end with a small navy chip: "ACR — flat case rate".
  - Series B — "Real cost of care": a rising curve in clinical teal (#1a6b72), ~3 px stroke, climbing from just above the ACR line at "Mild" to roughly the ₱220K level at "Severe", through a midpoint at "Moderate" near ₱110K. Three small teal filled circles mark the tier values. Label the line at the right end with a small teal chip: "Real cost of care".
  - Gap fill — the area between the rising real-cost curve and the flat ACR line is filled with a soft clinical-teal tint (#1a6b72 at ~16% opacity) bounded above by the teal curve and below by the navy ACR line. A small angled callout arrow points into the widest part of the gap (over the Severe tier) ending in a compact rounded amber (#b8860b) badge: "Balance-billed to the patient".

Bottom strip — a full-width soft very-light-gray panel (#f3f4f6) running across the bottom ~14% of the canvas. Inside it, navy text reads, in one line, sans-serif: "PIDS analysis: ~98.8% of PhilHealth claims exceed the case rate — the shortfall lands on patients."

Bottom-right corner of the canvas (over the soft gray strip): small semi-transparent navy text "williamriveromd.com" at ~10–11 px equivalent, 70% opacity.

Restrained clinical palette only — navy #0f1e2e structure and text, clinical teal #1a6b72 for the real-cost curve and gap, amber #b8860b for the single callout badge, soft gray #f3f4f6 for the bottom strip. No other colors. Generous whitespace, mobile-readable labels ≥11 pt equivalent, rounded line caps.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts. Do not draw the real PhilHealth logo. No 3D, no shadows under the chart. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
A single clear plot — three labeled severity tiers, a flat navy ACR line, a rising teal real-cost curve, a soft teal gap fill, one amber "Balance-billed to the patient" callout, a bottom strip with the PIDS one-liner. Mobile-readable at 600 px. Bottom-right williamriveromd.com attribution visible.
```

---

## 4 · OG / Twitter share card — ACR → DRG, severity-adjusted ladder
*Skill: williamriveromd-infographic-skill · Archetype 1 / OG editorial poster · **fixed 1200 × 630***

> The share-card surfaced on Facebook, X, LinkedIn, iMessage. Strict 1200×630.
> Big headline + subtitle + central two-panel ACR-vs-DRG metaphor + tagline +
> attribution. The guide HTML already declares
> `og:image:width="1200"` / `og:image:height="630"`.

```
FILE NAME: philhealth-acr-to-drg-og.png
IMAGE TYPE: OG / social share card — editorial poster
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630 (FIXED — do not change)
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Set the editorial tone of the piece on a single social-share frame — old flat case rate giving way to a severity-adjusted DRG ladder, with the author byline and brand cue.

PROMPT:
Open-Graph / Twitter share card for a williamriveromd.com nephrology + health-policy essay. Landscape canvas, exactly 1200 × 630 px. Off-white (#fafafa) background with a very subtle paper-grain texture; soft warm vignette at the corners. Layout uses a 12-column editorial grid with generous margins. Sans-serif typography only (Inter for headlines, Nunito Sans or Manrope for supporting text).

LEFT COLUMN (≈55% of width) — typography stack, vertically centered, left-aligned:
  - Eyebrow tag, small, clinical teal (#1a6b72), all-caps with slight tracking: "PERSPECTIVES · PHILIPPINES · POLICY".
  - Headline, very large, bold Inter, navy (#0f1e2e), two lines max, tight leading:
        From All Case Rates
        to DRG
    The word "DRG" set in clinical teal (#1a6b72).
  - Subtitle, medium sans-serif, navy at ~85% opacity, two lines max:
        What PhilHealth's payment overhaul
        means for Filipino patients.
  - A short hairline rule in clinical teal, ~120 px wide, just below the subtitle.
  - Byline directly under the rule, single line, small teal text, all-caps tracking:
        — W. RIVERO, MD · A NEPHROLOGIST'S PERSPECTIVE

RIGHT COLUMN (≈45% of width) — central metaphor panel, vertically centered, illustrative not data-heavy:
  - Two small rounded cards side by side on a soft light-teal tint (#eef6f7) sub-panel with a navy outline, each card ~46% wide.
  - LEFT card: header chip "ACR" in muted navy on a soft gray background; below it a single flat horizontal navy bar suggesting one fixed rate across three faint tier markers labeled lightly "Mild · Moderate · Severe". Caption under the bar in small navy text: "One flat rate".
  - A short navy right-pointing arrow connects the two cards across a soft gap.
  - RIGHT card: header chip "DRG" in clinical teal on the same soft gray background; below it a stepped severity ladder of three clinical-teal stair-blocks rising left-to-right above the same three tier markers "Mild · Moderate · Severe", each step subtly taller than the last. A renal-green (#1f7a4d) check-tick sits at the upper-right of the rightmost step. Caption under the ladder in small navy text: "Severity-adjusted bundle".
  - Floating just above the metaphor panel: a small stylized member-card glyph (rounded rectangle in clinical teal with a tiny chip mark, NO real PhilHealth logo, NO readable words on the card) — a quiet brand cue, ~6% of canvas width.

Bottom strip — a full-width very-light-teal (#eef6f7) band across the lower ~10% of the canvas with a faint top hairline in clinical teal. Inside it, on the left, in small navy text: "williamriveromd.com / guides / philhealth-acr-to-drg". On the right, in small semi-transparent navy text (70% opacity): "williamriveromd.com".

Palette is strictly limited to off-white #fafafa, navy #0f1e2e (text and structural lines), clinical teal #1a6b72 (DRG accent + eyebrow + rule), renal green #1f7a4d (single tick mark), and soft gray #f3f4f6 / light teal tint #eef6f7 for sub-panels. No other colors.

Generous whitespace. Mobile/Facebook/LinkedIn preview-safe — important content lives in the central 80% of the canvas. Headline must be perfectly legible at small preview sizes.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid AI mis-spellings — every word in the headline, subtitle, byline, and footer must render exactly as written. NEVER use dark, navy, charcoal, or black backgrounds — off-white only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative typefaces. Do NOT render the real PhilHealth logo, the actual Department of Health seal, hospital signage, or any other wordmark. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Exactly 1200 × 630 px landscape. Headline "From All Case Rates to DRG" with "DRG" in teal. Subtitle exact. Byline single line in teal. Two-card ACR-vs-DRG metaphor on the right with three labeled severity tiers under both, a single navy arrow between them, a renal-green tick on the DRG side. Quiet member-card brand glyph. Bottom-strip path + williamriveromd.com attribution visible. Renders cleanly at Facebook / X / iMessage preview sizes.
```

---

## 5 · Two different problems — the essay's thesis in one frame
*Skill: williamriveromd-simple-figure · Scaffold B — side-by-side comparison*

> The visual operationalization of the essay's core argument: the Marvin denial
> (Problem A — eligibility) is not the same thing as the ACR→DRG migration
> (Problem B — payment). DRG fixes B; it does not fix A. Drop this into §2,
> after the prose lede and before the existing HTML table — or in place of the
> table once the figure is finalized.

```
FILE NAME: philhealth-acr-to-drg-two-problems.png
IMAGE TYPE: Simple figure — side-by-side comparison (Scaffold B)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients + clinicians)
VISUAL GOAL: Make it visually unambiguous that the 24-hour denial and the ACR→DRG payment reform are two distinct problems, and that DRG only solves one of them.

PROMPT:
Medical-education comparison infographic, editorial / AJKD graphical-abstract style. White (#ffffff) background, sans-serif typography only (Inter). Generous whitespace, mobile-readable labels, rounded corners.

Title at top center, bold navy (#0f1e2e): "Two Different Problems — Don't Confuse Them". Subtitle directly below in clinical teal (#1a6b72), smaller: "PhilHealth's eligibility rules vs PhilHealth's payment model".

Soft dashed vertical divider in muted navy splits the canvas into two equal panels with a small navy chip in the middle that reads "vs" — but the chip is small enough not to dominate. A faint background tint differentiates the panels: very-light-red wash (#fff5f5) on the LEFT, very-light-teal wash (#eef6f7) on the RIGHT.

LEFT PANEL — "Problem A":
  - Header chip, large, on a soft red (#fff0f0) pill background with clinical-red (#b91c1c) text: "PROBLEM A — ELIGIBILITY". A small line-icon of a hospital billing window / shut counter window in clinical red sits to the right of the header chip.
  - Subheader navy: "Who gets told 'no' at the window".
  - Three short bullet rows, each with a small clinical-red dot bullet and navy text:
        • 24-hour confinement rule applied too rigidly
        • Member unaware of emergency benefit (PC 2024-0033)
        • Hospital billing office uninformed or unwilling
  - Bottom of panel: a compact rounded badge in clinical red on a soft red fill: "DRG does NOT fix this".

RIGHT PANEL — "Problem B":
  - Header chip, large, on a soft teal (#eef6f7) pill background with clinical-teal (#1a6b72) text: "PROBLEM B — PAYMENT MODEL". A small line-icon of a stack of coins / case-rate sheet → tablet ladder in clinical teal sits to the right of the header chip.
  - Subheader navy: "How hospitals are paid for a case".
  - Three short bullet rows, each with a small clinical-teal dot bullet and navy text:
        • Flat case rate ignores severity
        • Hospitals balance-bill the shortfall to patients
        • Migrating to DRG = severity-adjusted bundles
  - Bottom of panel: a compact rounded badge in clinical teal on a soft teal fill: "DRG addresses this".

BOTTOM STRIP — a full-width soft very-light-gray panel (#f3f4f6) across the bottom ~14% of the canvas. Inside it, centered, bold navy text in one line, sans-serif Inter:
"DRG fixes how hospitals are paid. It does not fix who gets told 'no' at the billing window. We need both repairs."

Bottom-right corner of the canvas (over the soft gray strip): small semi-transparent navy text "williamriveromd.com" at ~10–11 px equivalent, 70% opacity.

Palette: white #ffffff canvas, navy #0f1e2e text, clinical red #b91c1c (Problem A markers + badge), clinical teal #1a6b72 (Problem B markers + badge), light-red wash #fff5f5 and light-teal wash #eef6f7 for panel tints, soft gray #f3f4f6 for the bottom strip. No other colors. No 3D, no shadow drops.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid AI mis-spellings — bullet text must render exactly as written. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative typefaces. Do NOT draw the real PhilHealth logo or any hospital wordmark. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Two clearly distinct panels under a single banner. Left = red eligibility problem with a "DRG does NOT fix this" badge. Right = teal payment problem with a "DRG addresses this" badge. A single bottom-strip sentence carrying the essay's thesis. Mobile-readable at 600 px width. Bottom-right williamriveromd.com attribution visible.
```

---

## 6 · Kidney lens — cardiorenal storm into two DRG outcomes
*Skill: williamriveromd-simple-figure · Scaffold D — single-panel concept poster*

> The nephrologist's reason to care: a CKD admission is rarely one problem. A
> well-built DRG pays severity for the storm; a weak DRG nudges hospitals to
> discharge a fragile dialysis patient a day too early. The figure makes that
> two-outcome fork visible at the bottom of §7.

```
FILE NAME: philhealth-acr-to-drg-kidney-lens.png
IMAGE TYPE: Simple figure — single-panel concept poster (Scaffold D)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: mixed (patients + clinicians, leaning clinician)
VISUAL GOAL: Show that one CKD admission braids multiple severity drivers ("the storm"), and that DRG forks into a good-for-patients path (severity-paid) or a bad-for-patients path (early discharge) depending on guardrails.

PROMPT:
Medical pathophysiology / health-policy concept poster, AJKD/NEJM graphical-abstract style. White (#ffffff) background, sans-serif typography only (Inter). Generous whitespace, mobile-readable labels, rounded corners.

Title at top center, bold navy (#0f1e2e): "The Kidney Lens — Why DRG Design Matters for Severe Cases". Subtitle in clinical teal (#1a6b72): "A CKD admission is rarely one problem. The payment model should know that."

LEFT THIRD — "The cardiorenal storm" tile:
  - A single rounded card on a very-light-gray fill (#f3f4f6) with a soft navy outline. Header in bold navy: "ONE CKD ADMISSION". Beneath the header, a small semi-photorealistic 3D pair of human kidneys (clinical reds, restrained, anatomically accurate) on a transparent backdrop with five short label chips arranged radially around the kidneys — each chip is a small rounded pill with a colored dot and a short navy label:
        • clinical-red dot: "Fluid overload"
        • amber dot: "Hyperkalemia"
        • amber dot: "Acidosis"
        • soft-purple (#6c3d8e) dot: "Anemia"
        • clinical-red dot: "Cardiorenal strain"
  - Card footer caption in muted navy, single line: "Severity-rich, multi-system storm."

A bold navy right-pointing arrow exits the card to the right, splitting into TWO branches that fan out into the right two-thirds of the canvas — an upper branch labeled in renal green (#1f7a4d) "Severity-paid (good design)" and a lower branch labeled in amber (#b8860b) "Fixed-price logic, weak guardrails (bad design)". The two branch labels sit on the arrows as small pill chips.

UPPER RIGHT — "Well-built DRG" outcome card:
  - Header chip on a soft renal-green fill: "WELL-BUILT DRG". Renal-green border on the card.
  - Three short bullet rows, navy text with renal-green dot bullets:
        • Severity-adjusted payment recognizes the storm
        • Complex transplant + cardiorenal cases properly resourced
        • Hospitals rewarded for keeping the sickest alive
  - Card footer badge, renal-green: "Good for kidney patients."

LOWER RIGHT — "Weak DRG" outcome card:
  - Header chip on a soft amber fill: "WEAK DRG (no guardrails)". Amber border on the card.
  - Three short bullet rows, navy text with amber dot bullets:
        • Early discharge of fragile dialysis patients
        • Avoidance of complex transplant / cardiorenal admissions
        • Outcomes invisible, readmissions unmeasured
  - Card footer badge, amber: "Hurts the very sickest."

BOTTOM STRIP — a full-width very-light-teal tint (#eef6f7) band across the bottom ~12% of the canvas, with a faint top hairline in clinical teal. Centered navy text, one line, sans-serif:
"Severity-adjusted payment is good news for complex renal care — only if it is paired with outcome tracking."

Bottom-right corner of the canvas (over the light-teal strip): small semi-transparent navy text "williamriveromd.com" at ~10–11 px equivalent, 70% opacity.

Palette: white #ffffff canvas, navy #0f1e2e structure/text, clinical teal #1a6b72 (subtitle, hairline), renal green #1f7a4d (good-outcome branch + badge), amber #b8860b (bad-outcome branch + badge), clinical red #b91c1c (storm chips), soft purple #6c3d8e (anemia chip only), soft gray #f3f4f6 (storm card fill), light-teal #eef6f7 (bottom strip). No other colors. Semi-3D kidney anchor only — otherwise clean 2D. No heavy shadows.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid AI mis-spellings — every chip label and bullet must render exactly as written. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif fonts, no decorative typefaces. Anatomy: a clinically plausible pair of human kidneys, not a stylized cartoon and not multiple kidneys. Do NOT draw the real PhilHealth logo. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
A single storm card on the left with kidneys + five severity chips. A navy arrow forks into two outcome cards on the right — upper renal-green "Well-built DRG / Good for kidney patients", lower amber "Weak DRG / Hurts the very sickest". Bottom-strip one-liner present. Mobile-readable at 600 px width. Bottom-right williamriveromd.com attribution visible.
```

---

## Post-generation checklist

1. Save each PNG to `images/<filename>.png` and write a paired WebP twin
   `images/<filename>.webp` (the guide HTML already references both with
   `<picture><source srcset="…webp"><img src="…png">`).
2. Update the `<img width/height>` attributes in `guides/philhealth-acr-to-drg.html`
   to match the actual files where they currently differ from this plan:
   - marvin-quote → `width="1024" height="1024"`
   - rate-vs-cost → `width="1792" height="1024"`
3. **Wire in the two new figures** (§5 and §6 of this plan). The guide doesn't
   yet reference them. Add a `<figure>` block to §2 ("Two Different Problems")
   pointing to `philhealth-acr-to-drg-two-problems.{webp,png}` and a second
   `<figure>` block to §7 ("The Kidney Lens") pointing to
   `philhealth-acr-to-drg-kidney-lens.{webp,png}`. Mirror the inline-figcaption
   pattern used by the existing `philhealth-acr-to-drg-rate-vs-cost` figure
   (`<figcaption><p class="fig-desc">…</p></figcaption>`) so the lightbox shows
   the caption.
4. Optionally run Stage 2 (`williamriveromd-local-image-generator`) to build
   the local guide folder, manifests, and append the OG meta block — though
   `og:image*` is already present in the guide head.
5. Re-run `python3 generate_latest_guides.py` if the hero / OG file dates
   change (it reads file mtimes for the strip thumbnail).
