# Image Plan & Prompt Pack — Dialysis Decisions in the ICU

**Guide:** `guides/aki-icu-dialysis-decisions.html` · **Canonical:** https://renalcarematters.com/guides/aki-icu-dialysis-decisions.html
**Pipeline:** Stage 1 (this file, written with the repo graphic skills) → generate in the ChatGPT Image Generator GPT → Stage 2 `williamriveromd-local-image-generator` (validation, manifests, `og:image` tags).
**Prepared:** 8 November 2026. Every label inside a prompt comes from the guide's verified sources (KDIGO 2012 AKI guideline; ATS 2024 time-limited trial workshop report). Do not let the generator add numbers, drug doses, or trial names.

**Skills used:** `williamriveromd-hero-vignette` (00) · `williamriveromd-algorithm-generator-skill`, Style Mode C (01) · `williamriveromd-simple-figure`, Scaffold C (02, 03) · OG card (house constitution).

## Inventory

| # | Status | Pri | File stem | Section | Audience | Size |
|---|---|---|---|---|---|---|
| 00 | ● referenced | P1 | `aki-icu-dialysis-decisions-vignette-hero` | Hero (patient tab) | Families | 2048 × 2048 |
| 01 | ● referenced | P1 | `aki-icu-dialysis-decisions-01-bedside-pathway` | `#md-bedside` | Clinicians | 1536 × 1152 |
| 02 | ● referenced | P1 | `aki-icu-dialysis-decisions-02-trial-cycle` | `#md-trial` | Clinicians | 1536 × 1152 |
| OG | ● referenced | P1 | `aki-icu-dialysis-decisions-og` | `og:image` / `twitter:image` | Social | 1200 × 630 |
| 03 | ○ optional | P2 | `aki-icu-dialysis-decisions-03-bridge` | `#what` (patient tab) | Families | 1792 × 1024 |

Save each `.png` in `images/` with a `.webp` twin of the same stem. Until 00–02 exist, the page shows alt text in their place.

House rules for every image: light backgrounds only; Inter, Nunito Sans, IBM Plex Sans, or Manrope only (never serif); on-image text in English (the four-language explanation lives in the HTML); attribution `© renalcarematters.com` bottom-right (hero vignette is wordless by spec). Tone for this topic: calm and dignified. No dramatic ICU imagery, no visible blood, no distress on faces, no deathbed staging.

---

## 00 · Hero vignette (hero-vignette v3 · Archetype J, Environmental Storytelling · Scaffold A)

```
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle must never touch the canvas edges). Composition archetype: J — Environmental Storytelling, one cohesive scene with no floating panels. Camera: eye-level medium-wide shot from the foot of a bed, slightly off-axis, gentle shallow depth of field.

Subject: a family meeting at the bedside in a bright, modern Philippine intensive care unit. A Filipina nephrologist in her early 40s — short layered black hair tucked behind one ear, round face, wire-rimmed glasses, light-brown skin, navy scrubs under an open white coat, a small silver wristwatch — sits on a low stool at eye level, leaning slightly forward, one open hand resting on her knee as she listens. Facing her, a Filipino man in his late 20s with a buzz cut, lean build, darker morena skin, wearing a faded maroon T-shirt and holding a folded paper with handwritten questions, sits beside his aunt, a heavy-set woman in her 60s with chin-length gray-streaked hair, a floral duster blouse, and a rosary looped around her fingers. A male ICU nurse in his 30s with a neat undercut and ceil-blue scrubs stands quietly to one side, adjusting an IV pump. The patient is visible only in soft focus in the bed — a blanket, a hand resting on top, the face turned away and out of frame. A continuous dialysis machine stands in calm soft focus behind the bed with its tubing neatly arranged; no visible blood. Morning daylight through a window with sheer white curtains.

Mood: attentive, honest, unhurried — a shared decision, not bad news. Hands and faces anatomically correct; expressions thoughtful, not distressed.

Visual hierarchy: the three seated people and the clinician occupy 60–70% of the circle; the bed, dialysis machine, and nurse are 20–30% supporting context; reserve a 20–25% TITLE SAFE ZONE on the upper-left of the circle of soft-focus pale wall and window light (no faces, equipment, icons, or callouts inside that zone).

Calm, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; warm neutral skin tones. Edge falloff toward a slightly deeper neutral at the rim. Full-bleed within the inscribed circle, no rectangular borders, frames, or banners.

Absolutely NO text of any kind: no title, subtitle, caption, label, logo, monitor numbers, or watermark.

Avoid: busy layouts, collage, duplicated people, cropped circle, objects touching the circular border, important content inside the title safe zone, readable monitor screens, blood in tubing, a visible patient face, crying or anguished expressions, dark or charcoal backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces.
```

---

## 01 · Bedside pathway (algorithm generator · Style Mode C)

```
Create a clean publication-ready clinical algorithm flowchart in the renalcarematters.com house style, landscape 1536×1152. Use a white (#ffffff) background, restrained navy and teal typography set in Inter (never a serif font), thin teal connector arrows, and generous margins. The layout should be centered and suitable for a clinician-facing nephrology education guide.

Color conventions: Navy #0f1e2e for title, body text, and structural emphasis; Teal #1a6b72 for decision nodes and connector accents; Green #1f7a4d for recommended actions and endpoints; Amber #b8860b for caution nodes; Clinical red #b91c1c for the urgent branch only; soft gray for side notes.

Content to render:
Title: "Dialysis decisions in the ICU — four starting points"
Subtitle: "Adults with acute kidney injury (AKI) in the intensive care unit"
Top teal diamond: "Urgent indication for KRT?"
  Branch YES (red rounded rectangle): "Temporize + start KRT" with three short lines: "Hyperkalemia / acidemia / pulmonary edema / uremic complications" · "Reach surrogate in parallel" · "Set first reassessment point". A thin dashed arrow from this box to the trial box labeled "can begin as a trial".
  Branch NO → second teal diamond: "Is benefit plausible and the goal reachable?"
    Branch "Plausible" (navy rounded rectangle): "Active surveillance" with three short lines: "Owner — who reviews" · "Interval — when" · "Triggers — what starts KRT".
    Branch "Uncertain" (green rounded rectangle): "Time-limited trial" with three short lines: "One defined uncertainty" · "Patient-valued milestones" · "Review date + owner".
    Branch "KRT forgone" (amber rounded rectangle): "Supportive care plan" with three short lines: "Symptom orders" · "Family updates" · "Lead clinician named".
Bottom full-width soft-gray band (#f3f4f6) in navy text: "Every path ends with a named person, a review time, and a plan."

Design requirements: top-to-bottom logic; rounded rectangles for actions; diamonds for the two decisions; consistent spacing; short branch labels; all text legible at thumbnail size; no clutter; no photorealistic people; no dark background; optional simple flat line icons only (a heart-rhythm line for hyperkalemia, a clock for surveillance, a calendar for the trial, a hand for supportive care), never touching node borders. Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle gray medical-publication styling.
```

---

## 02 · Time-limited trial cycle (simple-figure · Scaffold C adapted to a cycle)

```
Clean clinical education infographic, landscape 1536×1152, white (#ffffff) background. Clean sans-serif typography set in Manrope (never serif). Title at top center in bold navy (#0f1e2e): "A time-limited trial of dialysis". Subtitle in clinical teal (#1a6b72): "Four phases from the ATS 2024 workshop definition".

Center-left: four rounded cards arranged clockwise in a circle on a very soft gray panel (#f3f4f6), connected by bold navy curved arrows:
1. "CONSIDER" (teal top band) — "Plausible benefit" · "Real uncertainty"
2. "PLAN" (navy top band) — "Patient-valued goal" · "Milestones + review date"
3. "SUPPORT" (soft purple #6c3d8e top band) — "Symptoms + family" · "Hand over at shift change"
4. "REASSESS" (teal top band) — "Treatment effect" · "Illness trajectory" · "Goal progress"

Right side: from the REASSESS card, three outcome pills stacked vertically with short arrows:
- renal green (#1f7a4d) pill with a check mark: "CONTINUE"
- amber (#b8860b) pill with a small calendar icon: "EXTEND — named reason, new date"
- soft purple (#6c3d8e) pill with a dove-outline icon: "STOP — comfort-focused care"
Small gray note under the pills: "Review sooner if the patient worsens."

Generous whitespace, maximum 6 words per label, mobile-readable labels ≥11pt, color always paired with an icon or word. No people, no numbers, no drug names. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text at 70% opacity.
```

---

## OG · Social card (1200 × 630)

```
Social share card, exactly 1200×630 landscape, light off-white (#fafafa) background with a soft teal-tint (#eef6f7) panel on the right half. Left half: title in bold navy (#0f1e2e) Inter, three lines: "Dialysis Decisions" / "in the ICU". Below in clinical teal (#1a6b72) Nunito Sans: "What can dialysis do — and how will we know it is helping?" Small line under it in gray: "Clinician guide + family section in 4 languages". Right half: a calm semi-flat illustration of a continuous dialysis machine beside a hospital bed, with a simple calendar card and a check-mark pill floating gently above it to signal a planned review — no people's faces, no blood, no screen numbers. Thin teal rule separating halves. Bottom-left small navy text: "W Rivero, MD · renalcarematters.com". Bottom-right: "© renalcarematters.com" in small gray at 70% opacity. No dark backgrounds, no clutter, all text crisp and correctly spelled.
```

---

## 03 · Optional — "A bridge, not a cure" (patient tab, simple-figure · Scaffold B)

```
Medical education comparison infographic for patients and families, landscape 1792×1024, white (#ffffff) background, clean sans-serif typography set in Nunito Sans (never serif). Title centered in bold navy (#0f1e2e): "Dialysis is a bridge, not a cure". Left panel labeled in renal green (#1f7a4d) with check marks: "What dialysis can do" — three icon+word rows: a potassium "K" droplet "Lowers potassium", an acid-drop icon "Corrects acid", a water-droplet icon "Removes extra fluid". Right panel labeled in amber (#b8860b) with circle-slash icons: "What it cannot do" — "Cure the infection", "Heal heart or lungs", "Wake the brain". Across the bottom, a simple stone footbridge drawing in soft teal spanning a gentle river, with a small sign on the far bank reading "Recovery?" in navy. Soft dashed vertical divider between panels. Rounded panel corners, ample negative space, labels ≥11pt, color always paired with an icon or word. Bottom-right: "© renalcarematters.com" in small semi-transparent navy text.
```

Placement snippet once 03 exists (insert after the `.three-col` block in `#what`):

```html
<figure class="illus-wrap illus-wrap-light" style="margin:28px 0;">
  <picture>
    <source srcset="../images/aki-icu-dialysis-decisions-03-bridge.webp" type="image/webp">
    <img src="../images/aki-icu-dialysis-decisions-03-bridge.png" alt="Two panels: what dialysis can do (lower potassium, correct acid, remove fluid) and what it cannot do (cure infection, heal heart or lungs, wake the brain), above a footbridge leading toward recovery." width="1792" height="1024" loading="lazy" decoding="async" style="width:100%;height:auto;display:block;border-radius:12px;">
  </picture>
  <figcaption>
    <p class="fig-desc">Dialysis takes over some of the kidneys' work while the team treats the illness. It is a bridge: whether a person recovers depends mostly on the illness itself.</p>
  </figcaption>
</figure>
```
