# Image Regeneration Prompts — KDIGO Accuracy Remediation

**For:** ChatGPT Image Generator GPT (https://chatgpt.com/g/g-pmuQfob8d-image-generator)
**Date:** 2026-08-09
**Why:** These 13 figures were flagged during the KDIGO reconciliation because their
**baked-in pixels still assert corrected/obsolete claims**. The guide alt text and
captions were already fixed; these prompts regenerate the artwork to match.

**House rules applied to every prompt (do not remove):**
- **Light background only** — white `#ffffff`, off-white `#fafafa`, or soft gray `#f3f4f6`. **Never** navy/black/charcoal (this alone fixes the ADPKD abstract, which is currently dark).
- Palette: navy `#0f1e2e` (text/lines only), teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b`, red `#b91c1c`.
- Fonts: **Inter** (or Nunito Sans / IBM Plex Sans / Manrope) — sans-serif only, no serif/decorative.
- Attribution `renalcarematters.com`, small semi-transparent navy, bottom-right (bottom-center for portrait).
- **Keep the exact pixel dimensions listed** so the images drop in without layout shift.
- After generating, save both `<name>.png` and a `<name>.webp` companion (I can wire them like the OG card).

**Global clinical framing to preserve across all of these:** distinguish *association* from *causation*; label KDIGO **Practice Points** vs graded recommendations; **22–26 mmol/L bicarbonate = laboratory reference interval, not a treatment target**; anemia thresholds are **population-specific**, not universal; ADPKD water is **~2–3 L/day, conditional and supportive — not 3–4 L/day, not guaranteed**; NSAIDs in ADPKD are **clinician-directed/cautious, not "absolutely contraindicated."**

---

## A. Metabolic Acidosis in CKD (5 images)

### A1 — `metabolic-acidosis-bicarb-explainer.png`
- **IMAGE TYPE:** Reference gauge / lab-value explainer · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** patients
- **VISUAL GOAL:** Read a bicarbonate value without implying 22–26 is a treatment "target."
- **PROMPT:**
> Clean patient-education infographic, white `#ffffff` background, font **Inter**. A single horizontal segmented gauge for serum bicarbonate (HCO₃⁻) with four labeled bands, left to right: red `#b91c1c` "Below 18 — clinically important low, confirm promptly"; amber `#b8860b` "18–21 — low, repeat and find the cause"; teal `#1a6b72` "22–26 mmol/L — laboratory reference interval (not a treatment target)"; soft green-gray "Above 26 — evaluate for alkalosis or overtreatment". Below the gauge, one small row of equal chips reading "HCO₃⁻ = tCO₂ = bicarbonate = CO₂ — the same value on your labs". Under that, three tiny linked cards showing the workflow: "1 Confirm the result" → "2 Confirm the disorder" → "3 Find the cause". Navy `#0f1e2e` text, generous white space, mobile-readable, no dark panels. Small semi-transparent navy "renalcarematters.com" bottom-right.
- **NEGATIVE:** No "normal/target 22–26" wording; no dark background; no serif fonts; no gibberish micro-text; no auto-prescription.

### A2 — `metabolic-acidosis-kidney-damage.png`
- **IMAGE TYPE:** Pathophysiology mechanism flow · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** patients/mixed
- **PROMPT:**
> Medical mechanism infographic, soft-gray `#f3f4f6` background, font **Inter**, AJKD graphical-abstract style. A left-to-right / top-to-bottom arrow flow: "CKD reduces acid excretion" → "Blood becomes slightly more acidic" → "Tubular stress (ammoniagenesis, complement, endothelin)" → "Inflammation & fibrosis" → "Faster eGFR decline", using a small semi-photorealistic 3D kidney at the start. A prominent teal `#1a6b72` banner across the bottom reads: "Lower bicarbonate is ASSOCIATED with faster decline — association, not proven cause." Navy arrows and labels, amber accents on the middle steps. Light background only, mobile-readable. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No "KDIGO recommends treating below 22"; no claim that correction is proven to prevent kidney failure; no dark background.

### A3 — `metabolic-acidosis-treatment.png`
- **IMAGE TYPE:** Treatment reference card · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** patients
- **PROMPT:**
> Patient treatment infographic, white background, font **Inter**. Three stacked cards: (1) "Sodium bicarbonate — take tablets with food", small 3D tablet render; (2) "Philippines: widely available, low cost (₱)", peso motif; (3) a teal card "Goal: keep within the laboratory reference interval (≈22–26 mmol/L) — your exact goal is individualized", explicitly noting "Raises the lab value; effect on long-term outcomes is uncertain". A red-bordered caution strip: "Watch sodium — ankle swelling, weight gain, rising BP; caution in heart failure." Navy text, light background, mobile-readable. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No "KDIGO target 22–26"; no "simple, cheap, and effective" outcome overclaim; no dark background.

### A4 — `metabolic-acidosis-monitoring.png`
- **IMAGE TYPE:** Monitoring 4-card grid · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** patients
- **PROMPT:**
> Four-card monitoring infographic, off-white `#fafafa` background, font **Inter**. Card 1 "Bicarbonate (HCO₃⁻ / tCO₂) every 1–3 months — aim for the laboratory reference interval (≈22–26), goal individualized"; Card 2 "Blood pressure — watch the sodium load"; Card 3 "Potassium — recheck after starting"; Card 4 "eGFR — track CKD progression". Each card a rounded light panel with a simple line icon, teal headers, navy body. Light background, calm, mobile-readable. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No "target 22–26"; no dark background; no serif fonts.

### A5 — `metabolic-acidosis-ckd-clinician-infographic.png`  *(also has a .webp)*
- **IMAGE TYPE:** Clinician reference card (dense) · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** clinicians
- **PROMPT:**
> Clinician reference infographic, white background, font **IBM Plex Sans**, publication-grade, modular cards. Header "Metabolic Acidosis in CKD — Clinical Summary". A prominent evidence-status band: "KDIGO 2024 Practice Point (ungraded): consider alkali therapy to prevent acidosis with potential clinical consequences — example <18 mmol/L in adults. 22–26 mmol/L is a laboratory reference interval, NOT a treatment target." Cards for: Pathophysiology (ammoniagenesis, complement activation, TGF-β fibrogenesis, bone/muscle/potassium); Diagnostic approach (Winter's formula); Evidence base with a neutral-trials note ("de Brito-Ashurst 2009 and UBI 2019 suggested benefit; BiCARB 2020 and VALOR-CKD 2023 were neutral on hard outcomes — threshold uncertain"); Prescribing (sodium bicarbonate 650 mg PO BID start, titrate, sodium load); Dialysis (pre-HD HCO₃⁻ 22–24, PD 22–26). Navy/teal headings on light cards, amber caution accents, mobile-legible. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No "KDIGO target 22–26" or "graded recommendation"; no "treat persistent <22" as a rule; **no dark/navy background**; no serif.

---

## B. Contrast & the Kidneys (1 in-body figure)

### B1 — `contrast-injury-mechanism.png`  *(also has a .webp; in-body mechanism figure — the OG share card is already replaced)*
- **IMAGE TYPE:** Pathophysiology mechanism, association-framed · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** mixed
- **PROMPT:**
> Medical mechanism infographic, soft-gray `#f3f4f6` background, font **Inter**. Title "How contrast MAY contribute to kidney injury — and what else can." Center: a semi-photorealistic 3D kidney with two labeled proposed pathways (teal): "Renal vasoconstriction → medullary hypoxia" and "Direct tubular cell stress". To the side, a clearly separated amber panel headed "Competing causes of post-procedure AKI" listing hypotension, sepsis, heart failure, cholesterol emboli, bleeding, nephrotoxins, dehydration, the underlying illness. A bottom teal banner: "AKI after contrast is often ASSOCIATED (CA-AKI), not proven to be caused by contrast (contrast-induced AKI is a causal subset)." Navy labels, light background, mobile-readable. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No depiction of contrast as the sole/definite cause; no "leading cause of hospital AKI"; no dark background.

---

## C. Polycystic Kidney Disease (3 images)

### C1 — `pkd-visual-clinical-abstract-umj.png`  *(also .webp; currently DARK navy — must become LIGHT)*
- **IMAGE TYPE:** Visual clinical abstract (3-column) · **RATIO:** 4:3 · **DIMENSIONS:** 1448 × 1086 · **AUDIENCE:** mixed/clinicians
- **PROMPT:**
> Visual clinical abstract, **white `#ffffff` background** (light, not dark), teal `#1a6b72` header bar, font **Inter**. Title "Autosomal Dominant PKD — Clinical Abstract (KDIGO 2025)". Three columns on light rounded cards:
> • **Genetics & progression:** PKD1/PKD2 autosomal dominant; kidneys enlarge over decades; Mayo Imaging Classification 1A–1E is a **prognostic** category (requires typical morphology + the validated calculator).
> • **Key complications:** hypertension, hematuria, liver cysts, mitral valve prolapse, intracranial aneurysms in a minority ("worst headache of life = emergency").
> • **Management:** BP control with ACE/ARB (intensive control considered in selected younger patients); **water ~2–3 L/day when eGFR ≥30 and not on tolvaptan — supportive, not guaranteed**; tolvaptan for adults at risk of rapid progression (eGFR ≥25, shared decision-making) — "may slow kidney growth and eGFR decline in selected patients"; **NSAIDs used cautiously/clinician-directed (not absolutely contraindicated)**.
> Bottom metric chips: "≈1 in 400–1000", "prognosis by Mayo class", "tolvaptan in selected patients", "water ~2–3 L/day (conditional)". Navy text on light cards, teal/green/amber accents. "renalcarematters.com" bottom-right.
- **NEGATIVE:** **No dark navy background;** no "hydration 3–4 L/day"; no flat "reduces TKV 49%" headline; no "NSAIDs absolutely contraindicated"; no "eligibility confirmed"; no serif.

### C2 — `pkd-treatment-hydration-bp-nsaid-lifestyle.png`
- **IMAGE TYPE:** Four-quadrant photoreal + caption · **RATIO:** ~16:9 · **DIMENSIONS:** 1672 × 941 · **AUDIENCE:** patients
- **PROMPT:**
> Four-quadrant patient infographic, white background, font **Inter**, photorealistic Filipino subjects, bright natural light.
> • Top-left: a Filipino woman with a measured water bottle — caption "Spread water through the day, about 2–3 L/day if your eGFR ≥30 and you are not on tolvaptan — supportive, not a cure".
> • Top-right: a Filipino man checking blood pressure (~118/76) beside a Losartan box — caption "Control BP — ACE/ARB first-line".
> • Bottom-left: a paracetamol box with a green check and NSAID boxes (ibuprofen, mefenamic acid) with an amber caution (not a hard red X) — caption "Paracetamol preferred; NSAIDs only if your doctor directs, avoid regular use".
> • Bottom-right: a Filipino man doing moderate exercise — caption "Regular moderate activity".
> Navy captions on light cards, teal/green/amber accents. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No "3–4 L/day"; no "suppresses vasopressin" as a promise; **no "NSAIDs absolutely contraindicated"** (use cautionary amber, not a ban); no dark background.

### C3 — `pkd-living-well-water-exercise-monitoring-daily.png`
- **IMAGE TYPE:** Portrait daily-living guide (4 quadrants) · **RATIO:** 2:3 · **DIMENSIONS:** 1024 × 1536 · **AUDIENCE:** patients
- **PROMPT:**
> Portrait four-quadrant daily-living infographic, off-white `#fafafa` background, font **Inter**, photorealistic Filipino subjects, bright light.
> • Top-left: a Filipino man on a stationary bike in the morning — "Regular moderate exercise".
> • Top-right: a Filipino woman filling a measured water bottle — "Spread water across the day (about 2–3 L/day if eGFR ≥30 and not on tolvaptan)".
> • Bottom-left: a "My PKD Log" journal with an Omron BP monitor (~118/76) and a circled next appointment — "Track BP and eGFR; keep appointments".
> • Bottom-right: a Filipino man resting, small inset of contact sports with an amber caution — "Avoid contact sports when kidneys are very large".
> Navy captions, teal/green accents, light background. Attribution "renalcarematters.com" bottom-center.
- **NEGATIVE:** No "3–4 L/day"; no dark background; no serif fonts.

---

## D. Anemia in Kidney Disease (4 images)

> **Units note:** KDIGO 2026 uses g/L (100–115 g/L ≈ 10.0–11.5 g/dL). Show g/L with the g/dL equivalent in parentheses. Emphasize **population-specific**, not universal.

### D1 — `anemia-kdigo-targets-infographic.png`  *(also .webp)*
- **IMAGE TYPE:** Reference-range card, population-specific · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** clinicians/mixed
- **PROMPT:**
> Anemia reference infographic, white background, font **Inter**, header "KDIGO 2026 anemia references — individualized by population (not one universal target)". Cards: "Hemoglobin ~100–115 g/L (10.0–11.5 g/dL) as a general range — DO NOT use ESAs to maintain Hb ≥115 g/L (≥11.5 g/dL)"; "Hemodialysis iron: initiate when ferritin ≤500 ng/mL AND TSAT ≤30%; IV iron generally preferred"; "Withhold iron at ferritin >700 ng/mL OR TSAT ≥40%"; a footer band "Values are population-specific reference points, not universal orders." Teal headers, navy body, amber caution on the withhold card. Light background, mobile-readable. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No single universal Hb "target"; no "KDIGO 2024"; no dark background.

### D2 — `anemia-thresholds-reference.png`  *(also .webp)*
- **IMAGE TYPE:** Quick-reference threshold card · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** clinicians
- **PROMPT:**
> Clinician quick-reference infographic, off-white background, font **IBM Plex Sans**, title "CKD anemia thresholds (population-specific, KDIGO 2026)". Rows: anemia diagnosis; iron initiation (HD ferritin ≤500 & TSAT ≤30; non-dialysis ferritin <100 & TSAT <40, or 100–300 & TSAT <25); iron withhold (ferritin >700 or TSAT ≥40); ESA individualized, do not maintain Hb ≥115 g/L (≥11.5 g/dL). A footer: "Values differ by population and are not universal orders." Compact light table, teal headers, navy text, amber on withhold. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No universal cutoffs presented as orders; no ferritin-800 hold; no dark background.

### D3 — `anemia-diagnosis-infographic.png`  *(also .webp)*
- **IMAGE TYPE:** Diagnosis/classification reference · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** mixed/clinicians
- **PROMPT:**
> Anemia diagnosis infographic, white background, font **Inter**, title "Diagnosing anemia in CKD". Left: MCV categories (micro/normo/macrocytic) with small 3D lab-tube icons. Right: iron studies with two defined terms — "Systemic iron deficiency (low circulating AND stored iron)" and "Iron-restricted erythropoiesis (not enough circulating iron despite adequate stores; inflammation/hepcidin)". A teal note: "Ferritin & TSAT are imperfect and interpreted by population (non-dialysis CKD vs hemodialysis); ferritin can be inflammation-driven." Navy text on light cards. "renalcarematters.com" bottom-right.
- **NEGATIVE:** No single universal ferritin/TSAT cutoff; no claim that IV-iron response proves deficiency; no dark background.

### D4 — `anemia-iv-iron-algorithm.png`  *(also .webp)*
- **IMAGE TYPE:** Population-branched decision tree · **RATIO:** 1:1 · **DIMENSIONS:** 1024 × 1024 · **AUDIENCE:** clinicians
- **PROMPT:**
> Clinical algorithm infographic, white background, font **Inter**, KDIGO-style flowchart. Top node "Iron decision in CKD anemia" splits FIRST by population into two branches: "Hemodialysis — IV iron generally preferred (ferritin ≤500 & TSAT ≤30 to initiate)" and "Non-dialysis CKD — oral or IV individualized (ferritin <100 & TSAT <40, or 100–300 & TSAT <25)". Both converge on a shared amber withhold node "Withhold at ferritin >700 or TSAT ≥40; hold during active infection". Rounded teal action nodes, amber caution nodes, navy connectors, light background, ≤4 levels, no spaghetti. Use "consider / evaluate / discuss" verbs, not "give". "renalcarematters.com" bottom-right.
- **NEGATIVE:** No single universal tree; no "IV route is standard of care"; no auto "give iron"; no dark background.

---

## Wiring after generation

When you have the new PNGs (and optional WebP companions) in `images/`, tell me and I'll: optimize/resize if needed, generate any missing `.webp`, and confirm each guide's `<img>`/`<picture>` and alt text point at them. The alt text is already correct — only the pixels change — so most need no HTML edit beyond confirming the filename.
