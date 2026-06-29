# Image Plan — `filipino-nephrologist-challenges.html`
### A Filipino Nephrologist's Challenges — A Perspective · williamriveromd.com

**Stage 1 prompt pack** for the sections added in the enhancement build-out (AKI
feeder, why-late barriers, reasons for hope, the data blind spot, diagnostic
access, disaster continuity). Each figure is authored with the correct house
skill. Generate in the
[ChatGPT Image Generator GPT](https://chatgpt.com/g/g-pmuQfob8d-image-generator),
save PNG (+ `.webp`) outputs to `images/`, then optionally run Stage 2
(`williamriveromd-local-image-generator`) for manifests.

House rules applied to every prompt: **light background only** (navy/teal are
typography + accent, never a fill), the navy/teal/green/amber/red palette,
sans-serif type (Inter / Nunito Sans / IBM Plex Sans / Manrope), mobile-readable
labels, and the mandatory `williamriveromd.com` attribution bottom-right.

> **On-image text is English only** — matching this guide's existing figures
> (`…-the-gap`, `…-rescue-to-preservation`), whose `<figcaption>`s are also
> English. The four-language toggle lives in the HTML body text, not inside the
> raster images. Insert each finished figure as a `<figure>` with a
> `<figcaption class="illus-caption">…` in its section.

---

## Existing images (keep — do **not** regenerate)

| File | Section | Notes |
|---|---|---|
| `filipino-nephrologist-challenges-og.png` | hero / OG | 1200×630 share card + inline hero |
| `filipino-nephrologist-challenges-the-gap.png` | `#the-gap` | editorial line chart (demand vs capacity) |
| `filipino-nephrologist-challenges-rescue-to-preservation.png` | `#the-pivot` | two-state "bridge of 8 priorities" diagram |
| `filipino-nephrologist-challenges-rg-thumb.webp` | related-guides | thumbnail |

---

## Plan overview — new figures

| # | Section | File | Skill | Type | Size | Priority |
|---|---------|------|-------|------|------|----------|
| 1 | `#aki-feeder` | `filipino-nephrologist-challenges-aki-to-ckd.png` | simple-figure | Feeder→flow sequence (C/D) | 1792×1024 | **Core** (blueprint-required; can replace the inline CSS flow) |
| 2 | `#why-late` | `filipino-nephrologist-challenges-why-late.png` | infographic | 6-panel reason grid (Archetype 4) | 1792×1024 | **Core** |
| 3 | `#reasons-for-hope` | `filipino-nephrologist-challenges-reasons-for-hope.png` | infographic | 4-panel bright-spots (Archetype 4) | 1792×1024 | **Core** |
| 4 | `#built-to-rescue` (storm callout) | `filipino-nephrologist-challenges-storm-continuity.png` | simple-figure | One-panel concept (D) | 1792×1024 | Optional |
| 5 | `#md-data` | `filipino-nephrologist-challenges-ckd-iceberg.png` | simple-figure | Iceberg metaphor (D) | 1792×1024 | **Core (clinician flagship)** |
| 6 | `#md-access` | `filipino-nephrologist-challenges-access-gap.png` | simple-figure | Tiered availability card (E) | 1536×1152 | Optional |

> Figures 5–6 sit in `mode-physician` sections → hidden in patient mode
> automatically; give them **English-only** captions. Figures 1–4 are patient-mode.

---

## 1 · AKI → CKD — the sudden hit that becomes lifelong disease
*Skill: williamriveromd-simple-figure · Scaffold C/D hybrid (feeder chips → linear flow)*

> This is the flow diagram the blueprint requested. It mirrors the inline
> HTML/CSS diagram already in `#aki-feeder` — you can **replace** that inline
> figure with this raster once generated, or keep the CSS version and use this as
> the OG/section illustration. Matches the editorial chart style of `…-the-gap`.

```
FILE NAME: filipino-nephrologist-challenges-aki-to-ckd.png
IMAGE TYPE: Simple figure — feeder chips into a linear progression flow
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (mixed)
VISUAL GOAL: Show that Philippine-specific acute insults cause AKI that, after incomplete recovery, becomes lifelong CKD and eventually dialysis.

PROMPT:
Clean clinical education infographic, editorial graphical-abstract style, white (#ffffff) background. Title at top center in bold navy (#0f1e2e): "When a Sudden Hit Becomes Lifelong Kidney Disease". Subtitle in clinical teal (#1a6b72): "How acute kidney injury feeds chronic kidney disease in the Philippines".
TOP ROW — five small rounded "trigger" chips on a soft gray (#f3f4f6) band, each with a simple line icon and a short label, evenly spaced: "Leptospirosis (flood wading)", "Dengue", "Sepsis", "Obstetric bleeding / preeclampsia", "Nephrotoxins (NSAIDs, aminoglycosides, contrast, herbal)". From all five chips, thin navy arrows converge downward into the first stage of the flow.
MAIN FLOW — a single left-to-right sequence of four bold rounded nodes connected by thick navy right-pointing arrows:
  1) Clinical-red (#b91c1c) node: "ACUTE KIDNEY INJURY (AKI)" with a small wilting/strained kidney glyph.
  2) Amber (#b8860b) node: "INCOMPLETE RECOVERY" — small caption "kidney never fully heals".
  3) Navy (#0f1e2e) node: "CHRONIC KIDNEY DISEASE (CKD)".
  4) Soft gray node with navy text: "DIALYSIS".
BOTTOM STRIP — full-width very light teal tint (#eef6f7) band, navy text takeaway: "AKI is not always reversible. Survivors carry a markedly higher lifetime risk of CKD — and need a repeat eGFR and urine test months later, even when they feel well." 
Use one semi-3D kidney component for visual anchoring, otherwise clean 2D. Generous whitespace, rounded corners, mobile-readable labels ≥11pt, sans-serif (Inter). Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, clinically plausible (AKI→CKD continuum accurate), calm editorial palette, white background, attribution bottom-right.
```

---

## 2 · Why we meet so late — the six human barriers
*Skill: williamriveromd-infographic-skill · Archetype 4 (multi-panel educational infographic)*

```
FILE NAME: filipino-nephrologist-challenges-why-late.png
IMAGE TYPE: Multi-panel educational infographic (6 reason cards)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (mixed)
VISUAL MIX:
- photorealistic models: none (icon-led)
- 2D infographic: primary (6 modular cards + header + footer strip)
- 3D component graphics: none
- algorithm/flowchart: none

PURPOSE: Name, without blame, the six real reasons Filipino patients arrive at the nephrologist too late — and end on the agency message that one early test defeats most of them.
KEY CONCEPTS: silent disease · cost of testing · fear/fatalism · alternative medicine detour · geography · well-meaning delay
DIMENSIONS: 1792 × 1024

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient-education infographic poster, landscape 16:9, modern nephrology clinic aesthetic, white (#ffffff) background. Top header band in soft gray (#f3f4f6) with bold navy (#0f1e2e) title "Why We Meet So Late" and a clinical-teal (#1a6b72) subtitle "Six real, understandable reasons kidney disease is caught late — named without blame". Below, six equal rounded cards in a 3-across × 2-down grid, each with a colored top accent band, a simple clean line icon, a short bold heading, and one plain-language line:
1. (teal) "No symptoms, no alarm" — "CKD is silent through Stages 1–3; without a test there is nothing to feel."
2. (amber) "The cost of looking" — "Tests and travel cost money a well-feeling person rarely spends."
3. (red) "Fear and fatalism" — "'Sakit sa bato' is heard as a death sentence, so the visit is delayed."
4. (soft purple #6c3d8e) "The herbal detour" — "Teas, supplements and faith cures come first; some are harmless, some are nephrotoxic, all cost months."
5. (navy) "Geography" — "The nearest nephrologist can be a province and a full day's fare away."
6. (renal green #1f7a4d) "The well-meaning delay" — "The first doctor may treat the sugar and pressure but not order the kidney tests."
Bottom full-width very light teal (#eef6f7) strip, bold navy take-home: "One early test — eGFR + urine ACR — defeats most of these barriers." Clean 2D icons, rounded cards, generous whitespace, strong hierarchy, mobile-readable labels, sans-serif (Inter / Manrope). Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, six cards clearly separated, empathetic not accusatory tone, calm palette, white background, attribution bottom-right.
```

---

## 3 · Reasons for hope — what is actually working
*Skill: williamriveromd-infographic-skill · Archetype 4 (multi-panel educational infographic)*

```
FILE NAME: filipino-nephrologist-challenges-reasons-for-hope.png
IMAGE TYPE: Multi-panel educational infographic (4 bright-spot cards, each paired with "what still needs")
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (mixed)
VISUAL MIX:
- photorealistic models: none (icon-led)
- 2D infographic: primary (4 paired cards + header + footer)
- 3D component graphics: none
- algorithm/flowchart: none

PURPOSE: Balance the essay with credible, nameable progress — each bright spot honestly paired with what still needs to happen, so it reads true, not promotional.
KEY CONCEPTS: PhilHealth expansion · PD-First · falling SGLT2i prices · telenephrology + awareness
DIMENSIONS: 1792 × 1024

COPY-READY IMAGE GENERATOR GPT PROMPT:
Patient-education infographic poster, landscape 16:9, optimistic but restrained nephrology design, white (#ffffff) background. Top header in soft gray (#f3f4f6): bold navy (#0f1e2e) title "Reasons for Hope" with a clinical-teal (#1a6b72) subtitle "Real progress already underway — and what still needs to happen". Below, four equal rounded cards in a single row (or 2×2 grid), each split into a top renal-green (#1f7a4d) "WORKING" half and a lower amber (#b8860b) "STILL NEEDS" half, with a small clean line icon:
1. icon shield/heart — WORKING: "PhilHealth now covers hemodialysis at a higher rate across 156 sessions/yr, an expanded PD benefit, and a larger transplant package." STILL NEEDS: "the same generosity for prevention and early-CKD care."
2. icon house — WORKING: "A PD-First direction — home-based dialysis suited to a scattered archipelago." STILL NEEDS: "training, supplies and patient education to make it everyday practice."
3. icon pill/down-arrow — WORKING: "SGLT2-inhibitor prices easing as patents lapse — the key kidney-protective class coming within reach." STILL NEEDS: "coverage and steady supply so cost never loses a kidney."
4. icon phone/signal — WORKING: "Telenephrology and rising awareness (World Kidney Day, patient resources) narrowing the gap." STILL NEEDS: "turning awareness into routine yearly eGFR + ACR."
Bottom full-width very light teal (#eef6f7) strip, bold navy take-home: "The system shifts one informed patient at a time." Clean 2D icons, rounded cards, two-tone (green over amber) panels, generous whitespace, mobile-readable, sans-serif (Inter / Manrope). Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, four paired cards legible, credible-not-triumphant tone, calm palette, white background, attribution bottom-right.
```

---

## 4 · When the storm comes — dialysis continuity *(optional)*
*Skill: williamriveromd-simple-figure · Scaffold D (single-concept panel)*

```
FILE NAME: filipino-nephrologist-challenges-storm-continuity.png
IMAGE TYPE: Simple figure — single-concept threat→consequence→action panel
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: patients (mixed)
VISUAL GOAL: Show that Philippine weather regularly threatens dialysis continuity, and that planning ahead protects the patient.

PROMPT:
Clean clinical education infographic, single-concept panel, white (#ffffff) background. Bold navy (#0f1e2e) title at top: "When the Storm Comes". Clinical-teal (#1a6b72) subtitle: "Keeping the dialysis chair running through Philippine weather". A simple left-to-right three-stage flow with bold navy arrows:
  STAGE 1 — "THREATS": a soft amber (#b8860b) rounded card holding four small line icons with labels — typhoon, flood, brownout/power outage, El Niño extreme heat.
  STAGE 2 — "RISK": a clinical-red (#b91c1c) rounded card — "Missed dialysis sessions · fluid & electrolyte overload between sessions · little built-in surge capacity".
  STAGE 3 — "PLAN AHEAD": a renal-green (#1f7a4d) rounded card — "Know your unit's storm plan · a backup unit & contact list · go-bag with meds & records · stricter fluid/diet limits in heat".
Bottom strip in very light teal (#eef6f7), navy take-home: "Continuity is survival — plan before the rainy season and the heat, not during them." One small semi-3D dialysis-machine or kidney glyph for anchoring. Generous whitespace, rounded cards, mobile-readable, sans-serif (Inter). Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, threat→risk→action logic clear, calm palette, white background, attribution bottom-right.
```

---

## 5 · The blind spot — we count dialysis, not CKD *(clinician flagship)*
*Skill: williamriveromd-simple-figure · Scaffold D (iceberg metaphor) · English only*

```
FILE NAME: filipino-nephrologist-challenges-ckd-iceberg.png
IMAGE TYPE: Simple figure — iceberg visual metaphor (counted vs uncounted)
ASPECT RATIO: 16:9
PIXEL DIMENSIONS: 1792 × 1024
AUDIENCE: clinicians (English only)
VISUAL GOAL: Show that Philippine kidney data captures the small "tip" on dialysis but leaves the vast pre-dialysis CKD population uncounted — an epidemic we cannot fully measure.

PROMPT:
Medical concept infographic, clean editorial graphical-abstract style, white (#ffffff) background with a calm horizontal waterline across the middle (very light teal #eef6f7 below the line to suggest water; white above). Bold navy (#0f1e2e) title at top: "We Count Dialysis, Not CKD". Clinical-teal (#1a6b72) subtitle: "The Philippine kidney-data blind spot". 
ABOVE THE WATERLINE — a small iceberg tip, labeled in navy "WHAT WE COUNT", with a teal callout card: "Patients ON renal replacement therapy — ~65,000 on dialysis (Philippine Renal Disease Registry / RRT well captured)."
BELOW THE WATERLINE — a much larger submerged iceberg mass (5–6× the tip), shaded soft gray-blue, labeled in navy "WHAT WE DO NOT COUNT", with an amber (#b8860b) callout card: "Pre-dialysis CKD Stages 1–4 — largely uncounted · no robust national Stage 1–4 registry · prevalence rests on small screening studies & modeling (the ~1-in-7 figure is an estimate, not registry data)."
BOTTOM STRIP — very light gray (#f3f4f6) band, navy text: "Without denominator data, prevention cannot be targeted, funded, or evaluated. A primary-care-linked CKD registry (routine eGFR + ACR reporting) is achievable on existing UHC infrastructure." 
Restrained palette, clean 2D, generous whitespace, mobile-readable labels, sans-serif (Inter / IBM Plex Sans). Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only (the waterline tint must stay very light). Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, iceberg proportion conveys the message, the ~1-in-7 figure flagged as an estimate, light background throughout, attribution bottom-right.
```

---

## 6 · You cannot treat what you cannot measure — the access gap *(optional)*
*Skill: williamriveromd-simple-figure · Scaffold E (reference card) · English only*

```
FILE NAME: filipino-nephrologist-challenges-access-gap.png
IMAGE TYPE: Simple figure — tiered availability reference card
ASPECT RATIO: 4:3
PIXEL DIMENSIONS: 1536 × 1152
AUDIENCE: clinicians (English only)
VISUAL GOAL: Show how diagnostic and monitoring access for guideline CKD care falls off from city to province, making early care impossible where screening must happen.

PROMPT:
Clinical reference card, publication-grade nephrology design, white (#ffffff) background. Bold navy (#0f1e2e) title: "You Cannot Treat What You Cannot Measure". Clinical-teal (#1a6b72) subtitle: "The CKD diagnostic & monitoring access gap". A compact three-row table; teal column headers on soft gray (#f3f4f6): "Tier", "Tests", "Reality on the ground". Rows, each with a small left accent tab:
- (teal tab) "Screening" — "eGFR · urine ACR" — "Not universally available or affordable at primary care — exactly where screening must happen."
- (amber #b8860b tab) "Monitoring (KDIGO)" — "iPTH · iron studies · CKD-MBD & bone markers" — "Largely out-of-pocket; often unavailable outside cities."
- (red #b91c1c tab) "Imaging" — "Renal ultrasound · AVF Doppler · 2D echo" — "Concentrated in urban centers; adds travel and delay to every workup."
To the right of the table, a small calm gradient bar from renal green (#1f7a4d, "City") to clinical red (#b91c1c, "Remote province") labeled "Availability falls with distance". Footer takeaway in navy: "Until the denominator tests are cheap, local, and routine, 'screen early, refer at Stage 3' stays an aspiration, not a workflow." Alternating soft row fills, mobile-readable, not cluttered, sans-serif (Inter / IBM Plex Sans). Bottom-right: "williamriveromd.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, or Manrope — no serif or decorative fonts. Never omit the williamriveromd.com attribution.

QUALITY CHECK:
Mobile-readable, three tiers accurate, city→province gradient clear, white background, attribution bottom-right.
```

---

## After generating

1. Drop each PNG (plus a `.webp` copy) into `images/`.
2. Insert each figure into its section as a `<figure>` block, mirroring the
   existing `…-the-gap` figure pattern:
   ```html
   <figure style="margin:28px 0">
     <picture>
       <source srcset="../images/<file>.webp" type="image/webp">
       <img loading="lazy" decoding="async" src="../images/<file>.png" width="1792" height="1024"
            alt="<descriptive alt>" style="width:100%;height:auto;display:block;border-radius:12px;">
     </picture>
     <figcaption class="illus-caption" style="margin-top:8px;text-align:center;font-size:13px;color:#5a6472;"><!-- English caption --></figcaption>
   </figure>
   ```
   - Figure 1 goes in `#aki-feeder` (optionally replacing the inline CSS flow).
   - Figures 5–6 go in `mode-physician` sections (`#md-data`, `#md-access`) —
     English-only captions, hidden in patient mode automatically.
3. Re-run the hero/lightbox scripts (idempotent; they only touch the first image):
   `python3 patch_hero_fetchpriority.py --guide filipino-nephrologist-challenges.html`,
   `patch_hero_fullwidth.py`, `patch_hero_maxwidth.py`, then `patch_image_lightbox.py`.
4. No `og:image` change needed — the existing OG card stays. (If you ever want a
   refreshed OG, keep it exactly 1200×630.)
5. Optionally run Stage 2 — `williamriveromd-local-image-generator` — to build the
   manifest and verify wiring.

---

*Prompt pack authored with `williamriveromd-infographic-skill` + `williamriveromd-simple-figure`, June 2026.*
