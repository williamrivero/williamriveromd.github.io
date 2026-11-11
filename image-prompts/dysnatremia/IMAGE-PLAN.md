# Image Plan Blueprint — Dysnatremia: When Blood Sodium Is Too Low or Too High

**Guide:** `guides/dysnatremia.html` (dual-mode: Patients & Families in EN/TL/CEB/KAP · Clinicians in EN)
**Asset path:** `images/dysnatremia-*.{webp,png}` — every `<picture>` in the guide already points to these names.
**Prompt pack:** `PROMPTS-gpt.md` (this folder) — Constitution v1.0 seven-layer prompts for the ChatGPT Image Generator GPT
(https://chatgpt.com/).
**Skills applied:** Constitution v1.0 infographic generator (7-layer architecture, dual-audience rule, triple attribution) ·
hero-vignette v3 · infographic-skill v5 (house style, canonical sizes, OG rule) · algorithm-generator (Mode C house style) ·
biomedical-mechanism-figure (organ → magnified unit → injury → intervention → benefit) · simple-figure (comparison / step / chart scaffolds) ·
local-image-generator (Stage 2 schema fields, manifest).

---

## 1. Visual strategy — why each picture exists

The guide's hardest ideas are invisible: a concentration that is really a *ratio*, a brain that *adapts* over days, a
kidney that can *suddenly* switch to dumping water, and a correction limit that applies to *any* 24-hour window rather
than a calendar day. Each image carries exactly one of those ideas, so a reader with no science background and a
nephrology fellow can both get the point in under ten seconds.

| Idea the reader must "see" | Why words alone fail | Visual device |
|---|---|---|
| Sodium reflects **water relative to salt**, not salt eaten | People equate "low sodium" with "eat more salt" | Three identical soup bowls (same salt, different water) — the *sabaw* analogy from the text |
| The brain **adapts over ~48 h**, and fast correction injures it | Time and cell volume are abstract | Four-frame cell timeline with a clock strip |
| **Tonicity first** — not every low sodium is water excess | Clinicians skip the step | Three-door portrait algorithm |
| Urine tells you **which mechanism** | Thresholds blur in prose | Two-question portrait algorithm with caveat ribbon |
| **Target vs ceiling** and the **rolling** 24-h window | Readers confuse +4–6 goal with the 8 limit | Sodium-vs-time chart with a target band, a rolling window bracket and an aquaresis spike |
| **Aquaresis** can overshoot between blood draws; three DDAVP strategies | Abstract timing | Trigger icons feeding a timeline with three labeled intervention points |
| SIAD treatment is a **ladder** guided by urine electrolytes | Lists hide the order | Staircase graphic with a "ratio > 1" gate |
| Hypernatremia = **deficit + ongoing losses**, perfusion first | One-shot formula thinking | Bathtub/tank analogy: fill line, open drain, faucet |
| Filipino **daily-life triggers** | Generic advice feels foreign | Six photorealistic Philippine vignettes |
| **AVP → V2 → aquaporin-2**, where drugs act | Pharmacology is cellular | Kidney → collecting-duct cell mechanism figure |

### Reading-level design rules (all educational levels)

1. **One idea per figure;** at most 6 panels; each label ≤ 10 words.
2. **Dual labels** on every medical term: *Medical term (plain English)*, e.g. "Vasopressin (water-holding hormone)".
3. **Color is never the only signal:** every color code repeats as an icon or word (red + "STOP", amber + "CAUTION", green + "OK").
4. **Analogy first, anatomy second:** the patient figures (01, 02, 09) open with an everyday object, then show the real physiology beside it, so the analogy never stands alone.
5. **Numbers only from the guide** (135, 145, +4–6, ≤8 per any 24 h, 0.5 mmol/L/h, 10–12 per day, 275 mOsm/kg, 100 mOsm/kg, 30 mmol/L, urine ratio 1). No invented values.
6. **Filipino context** in people and objects (sabaw, lugaw, kape, beer sessions, banig, electric fan, lola at home).
7. **Mobile first:** labels legible at 360 px width; no microtext; generous whitespace.
8. **Calm, non-alarming imagery:** no seizures shown, no gore, no ICU distress; urgency is conveyed by color and icons.

### House rules (non-negotiable, every prompt)

- **Light backgrounds only** — white `#ffffff` / off-white `#fafafa` / light teal tint `#eef6f7`. Navy is never a fill.
- Palette: navy `#1F3864` (text/lines) · teal `#1A6B72` · orange `#C55A11` · green `#2E6B3E` · red `#C00000` · purple `#4B3280` · amber `#C9A84C`.
- Typography: **Inter** (titles, numbers) and **Manrope** (labels) only — never serif, never decorative.
- Style: polished **illustrated semi-3D medical illustration** consistent with existing site figures — **not flat vector clip art, not cartoon** (owner preference).
- Attribution `© renalcarematters.com` — bottom-right (bottom-center on portrait), small, navy, ~65% opacity, specified in Layers C, E and G.
- Export each as `.png` (GPT native) and convert to `.webp`; keep the pixel sizes below (the HTML width/height attributes match).

---

## 2. Asset manifest

| # | File stem (`dysnatremia-…`) | Tab · section | Archetype / skill | Canvas | Audience |
|---|---|---|---|---|---|
| H | `vignette-hero` | Patient hero disc | Hero vignette v3, Scaffold B still-life | 2048×2048 | Dual |
| OG | `og` | `og:image` share card (also `rg-thumb` source) | Infographic-skill OG card | 1200×630 | Dual |
| 01 | `01-salt-water-balance` | Patient · Basics | Visual aid, comparison (simple-figure B) | 1792×1024 | Patient-first |
| 02 | `02-brain-adaptation` | Patient · Why Slowly; Clinician · Mechanism | Biomedical mechanism, 4-frame timeline | 1792×1024 | Dual |
| 03 | `03-tonicity-first` | Clinician · Tonicity | Clinical algorithm, Mode C | 1024×1536 | Clinician |
| 04 | `04-hyponatremia-pathway` | Clinician · Diagnosis | Clinical algorithm, Mode C | 1024×1536 | Clinician |
| 05 | `05-correction-window` | Clinician · Emergency | Data-concept chart (simple-figure D) | 1792×1024 | Clinician (patient-legible) |
| 06 | `06-aquaresis-rescue` | Clinician · Overcorrection | Multi-panel educational | 1792×1024 | Clinician |
| 07 | `07-siad-ladder` | Clinician · Cause & SIAD | Stepwise ladder (algorithm, wide) | 1792×1024 | Clinician |
| 08 | `08-hypernatremia-plan` | Clinician · Hypernatremia | Multi-panel with tank analogy | 1792×1024 | Dual |
| 09 | `09-everyday-risks-ph` | Patient · Daily Life | Multi-panel photorealistic Filipino vignettes | 1792×1024 | Patient |
| 10 | `10-collecting-duct-avp` | Clinician · Mechanism | Biomedical mechanism (kidney Layer A rules) | 1792×1024 | Clinician (dual labels) |
| RG | `rg-thumb` | Related-guide / latest-strip thumb | Derived crop of OG (no new prompt) | 440×320 → export 220×160 @2x | — |

**Order of production:** H and OG first (they ship the guide's share preview and hero), then 01, 02, 09 (patient tab),
then 03–08 and 10.

---

## 3. Section-by-section placement map

```
PATIENT TAB                         CLINICIAN TAB
hero disc ............ H            Evidence Scorecard (no image)
Basics ............... 01           Mechanism .......... 10, 02
Low / High sodium .... (text)       Tonicity ........... 03
Why slowly ........... 02           Diagnosis .......... 04
Daily life ........... 09           Emergency .......... 05
                                    Overcorrection ..... 06
                                    Cause & SIAD ....... 07
                                    Hypernatremia ...... 08
Share preview ........ OG (+ rg-thumb)
```

---

## 4. Medical-accuracy guardrails for the generator

- Hyponatremia < 135 mmol/L; hypernatremia > 145 mmol/L.
- Emergency target "+4 to 6 mmol/L"; conservative ceiling "≤ 8 mmol/L in ANY 24 hours" (site default for chronic or unknown onset). Never draw the ceiling as a calendar-day box.
- Brain adaptation "about 48 hours"; ODS signs "2 to 6 days later".
- Hypernatremia conventional fall "about 0.5 mmol/L per hour, 10–12 per day" labeled *expert practice*.
- Urine thresholds: osmolality "≤ 100 mOsm/kg", sodium "30 mmol/L", plasma osmolality "< 275 mOsm/kg" — drawn as soft gray-zone bands, not hard walls.
- No drug doses on any image (dose-content gate). Tolvaptan, urea, DDAVP appear by name and mechanism only.
- Collecting-duct figure must follow kidney Layer A rules (hilum medial, calyces drain inward) in its orientation inset.

---

## 5. Post-generation wiring (Stage 2)

1. Save renders to `generated-images/`, rename to the stems above, export `.png` + `.webp` into `images/`.
2. Build `dysnatremia-rg-thumb.webp` (220×160) from the OG card.
3. Confirm `og:image` = `dysnatremia-og.webp` (1200×630) — already set in `<head>`.
4. Re-run `generate_latest_guides.py` so the strip picks up the real thumbnail.
5. Check each figure's lightbox caption (`fig-desc` + `fig-abbrevs`) still matches the final render.
