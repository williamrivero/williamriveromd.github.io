# Blueprint: Anti-GBM Disease (Goodpasture Disease)

**File:** `guides/anti-gbm-disease.html`
**Canonical:** `https://renalcarematters.com/guides/anti-gbm-disease.html`
**Status:** New guide. Implementation handoff for Claude Code (`/setup-guide anti-gbm-disease.html`), to be opened in its own thread.
**Shape:** Dual-mode (Patients & Families / Clinicians). Patient mode EN/TL/CEB/KAP; clinician mode English-only.
**Index section:** `nephrology` (teal `#1a6b72`).
**Template to copy:** `guides/anemia-management.html` (dual-mode wiring). Glossary: `guides/complement-mediated-kidney-disease.html`.
**Origin:** Journal review of 6 November 2026, item NG-3 (priority 4).
**Evidence check:** Abstract/skim level (6 Nov 2026). ✔ = read in the paper; **[verify]** = confirm in full text. Build all citations from PubMed (APA 7).
**Review status:** Draft blueprint. Not medically reviewed.

---

## 0. Why this guide

Anti-GBM disease is rare, but it is the glomerular emergency where hours matter: kidney survival depends on starting plasma exchange and immunosuppression before dialysis dependence. The site mentions it only in passing (6 guides, mostly in differential-diagnosis lists). Two 2026 papers provide a modern framework: the Peking University review that groups the variant forms into four categories, and a European pediatric-vs-adult outcomes cohort.

**Key teaching message:** urgent recognition (RPGN ± lung bleeding), same-day antibody test, do not wait for the biopsy to start treatment when the clinical picture and serology fit **[verify the exact wording in the current KDIGO chapter]**, and know the variants that break the textbook pattern (double-positive with ANCA, seronegative, atypical/IgG4, Alport post-transplant, drug-associated).

**Out of scope:** detailed ANCA vasculitis management (one pointer to a future vasculitis guide or `glomerulonephritis.html`); Alport genetics beyond the post-transplant alloimmune form (link `hematuria-blood-in-urine.html#md-followup`).

---

## 1. Source papers (on the Mac, `~/Downloads/Journals/`)

| # | File | Type | Contribution | Key data |
|---|---|---|---|---|
| S1 | `Kidney International_20260806/Anti–glomerular-basement-membrane-disease--variant.pdf` (duplicate copy in `_20260816`) | Review, Kuang, Lin, Jia, Cui, Borza, Zhao, KI 2026;110:337–348, doi 10.1016/j.kint.2026.03.029 | Clinician spine: variant forms and mechanisms | ✔ Most severe autoimmune GN; antibodies against α3(IV)NC1 in kidney and alveolar basement membranes; RPGN, lung hemorrhage, crescents. ✔ Patient survival improved with plasma exchange + intensive immunosuppression; kidney survival still poor because of late recognition. ✔ Four variant categories: (1) overlapping autoimmune syndromes — with ANCA (about one-third, "double-positive," usually MPO-ANCA), concurrent MN, or IgAN; (2) immunologically distinct — Alport post-transplant anti-GBM (alloimmune, targets α5NC1) and seronegative anti-GBM; (3) clinical phenotypic variants — recurrence in the native kidney, elderly patients, normal kidney function; (4) medication-associated. ✔ Native recurrence is rare (<6%), can occur months to years later, often with lung hemorrhage (up to 60%), associated with smoking. ✔ IgG4-restricted antibodies (atypical/indolent forms) activate complement less. ✔ Post-transplant recurrence of autoimmune anti-GBM is low; long-term graft survival achievable. ✔ Imlifidase trial (GOOD-IDES-02) named. **[verify]** double-positive outcome comparison, drug list for medication-associated cases, the authors' treatment suggestions per variant, and imlifidase trial status/results. |
| S2 | `Kidney International Reports_20260629/Outcomes-in-Children-and-Adults-With-Antiglomerula.pdf` | Cohort, Suhlrie, Kanzelmeyer et al., Kidney Int Rep 2026;11:106353, doi 10.1016/j.ekir.2026.106353 | Children vs adults | ✔ European patients diagnosed 2020–2024; n=72 (35% children); median follow-up 18 months. ✔ Children more often female and had higher eGFR at diagnosis (P<0.01); children had better eGFR outcomes, at least partly because of better eGFR at diagnosis. ✔ Need for dialysis was a strong predictor of outcome regardless of age. **[verify]** treatment used, kidney recovery rates, lung hemorrhage frequency. |
| S3 | `Kidney International_20260806/Disappearing-glomeruli--loss-of-linear-IgG-in-anti.pdf` | Nephrology image, doi 10.1016/j.kint.2025.12.041 | Pathology teaching point | **[verify]** content: loss of linear IgG staining as glomeruli are destroyed (pitfall: a late biopsy can under-show linear IgG). Use as a clinician figure caption only after reading. |

**External anchors to verify on PubMed:** KDIGO 2021 Glomerular Diseases guideline, anti-GBM chapter (grades verbatim; check whether a 2024–2026 chapter update exists); the classic Levy et al. 2001 Ann Intern Med outcome data on dialysis dependence and crescents **[verify citation before use]**; GOOD-IDES-01/02 imlifidase trial publications; any COVID-19-era incidence data cited in S1.

---

## 2. Head, meta, structured data

```
<title>Anti-GBM Disease (Goodpasture Disease): A Kidney and Lung Emergency · W Rivero, MD</title>
description: Anti-GBM disease attacks the kidney filters and sometimes the lungs. The warning signs, why treatment must start within hours, the antibody test, plasma exchange, and the newer variant forms doctors now recognize.
keywords: anti-GBM disease, Goodpasture syndrome Philippines, rapidly progressive glomerulonephritis, plasma exchange kidney, double positive ANCA anti-GBM, lung bleeding kidney failure
canonical: https://renalcarematters.com/guides/anti-gbm-disease.html
og image: images/anti-gbm-disease-og.webp (1200×630)
JSON-LD: Article + MedicalWebPage; about: Anti-Glomerular Basement Membrane Disease; Glomerulonephritis; Plasmapheresis. audience Patient + MedicalAudience.
localStorage keys: wgmr-antigbm-mode / wgmr-antigbm-lang
```

---

## 3. Page structure

House chrome per CLAUDE.md. Hero: H1 "Anti-GBM Disease"; subtitle "When the immune system attacks the kidney and lung filters"; tag "Glomerular emergency". The term "Goodpasture" appears in the subtitle or first paragraph because patients search for it.

**One-minute answer (patient, 4 languages)**
1. Anti-GBM disease is rare: the body makes antibodies against the thin filter layer in the kidneys and sometimes the lungs.
2. It can destroy kidney function within days, so treatment is an emergency, often started before every test result is back.
3. Treatment removes the harmful antibodies from the blood (plasma exchange) and stops the body making more (steroids and other immune medicines).
4. Once controlled it rarely comes back, especially if you do not smoke.

**Urgent box (red, both modes):** coughing up blood or sudden breathlessness; dark, cola-colored or bloody urine with swelling or much less urine; sudden rise in blood pressure. Go to an emergency department today and say "possible kidney inflammation."

---

## 4. Section map

### Patient mode (EN/TL/CEB/KAP)

| Anchor | Pill | Content |
|---|---|---|
| `#what-it-is` | What it is | Basement membrane as the "fine mesh" under the filter cells; antibodies attach and trigger inflammation; why lungs too (similar mesh) |
| `#warning-signs` | Signs | Blood in urine, less urine, swelling, coughing blood, tiredness; fast course |
| `#tests` | Tests | Anti-GBM antibody blood test (and ANCA, because the two can occur together), urine tests, kidney biopsy (linear antibody pattern); why treatment may start first |
| `#treatment` | Treatment | Plasma exchange sessions (what it feels like, catheter), steroids, cyclophosphamide or other agents; infection protection; dialysis as support while waiting for recovery |
| `#recovery` | Recovery | Who recovers kidney function; dialysis-dependent at presentation predicts worse kidney outcome (S2); children often fare better (S2) |
| `#after` | After | Relapse is uncommon; stop smoking and avoid inhaled hydrocarbons **[verify inhaled-exposure evidence before stating]**; transplant is possible after antibodies are gone for a period **[verify waiting interval in KDIGO]** |
| `#questions` | Ask | Question builder |
| `#faq` | FAQ | Is it inherited? Is it contagious? Can it come back after a transplant? Is it related to lupus/vasculitis? |

### Clinician mode

| Anchor | Pill | Content |
|---|---|---|
| `#md-pathophysiology` | Mechanism | α3(IV)NC1 epitopes (EA, EB), conformational change of the hexamer, IgG1/IgG3 vs IgG4 complement activation (S1 Fig 3), lung involvement and smoking |
| `#md-diagnosis` | Diagnosis | Serology (assay types and false negatives), biopsy (linear IgG, crescents), S3 pitfall (disappearing linear IgG in destroyed glomeruli), always test ANCA |
| `#md-treatment` | Treatment | KDIGO-based: plasma exchange schedule and endpoint, glucocorticoids, cyclophosphamide; rituximab as alternative **[verify grade]**; who not to treat (dialysis-dependent, 100% crescents, no lung hemorrhage — per guideline wording) **[verify]**; imlifidase (GOOD-IDES) as investigational |
| `#md-variants` | Variants | S1 four-category table: definition · distinguishing feature · prognosis · management note |
| `#md-double-positive` | ANCA overlap | Double-positive: anti-GBM-like early course plus ANCA-like relapse risk → consider maintenance therapy **[verify per S1/KDIGO]** |
| `#md-alport-tx` | Alport post-Tx | Alloimmune anti-α5 antibodies after transplant in Alport; risk factors; link the hematuria guide's Alport block |
| `#md-children` | Children | S2: female predominance, higher eGFR at diagnosis, better eGFR outcome, dialysis need predicts outcome |
| `#md-philippines` | Philippines | Access to urgent anti-GBM serology (turnaround time), plasma exchange availability (link `hemoperfusion-blood-purification.html` and `calc-plasma-volume.html`), transfer pathways **[verify]** |
| `#md-evidence` | Evidence | Claim · source · evidence type table |

**Evidence Snapshot (`.v` ≤ 8 chars)**

| `.v` | `.l` |
|---|---|
| ~1/3 | Also ANCA-positive ("double-positive") |
| <6% | Recurrence in the native kidney (often with lung bleeding, smoking) |
| 4 types | Variant categories: overlap, immunologic, phenotypic, drug-associated |
| n=72 | European cohort 2020–24; 35% children |
| Dialysis | Need for dialysis predicted outcome at any age |

---

## 5. Figures

1. Hero vignette (patient-only): patient in an emergency department with a nephrologist, plasma exchange machine in background.
2. Mechanism (biomedical-mechanism-figure skill): kidney and lung → glomerular basement membrane magnified → α3(IV)NC1 hexamer → antibody binding → crescent.
3. Variant map (simple-figure skill): four boxes from S1.
4. Algorithm (algorithm-generator skill): suspected RPGN ± hemoptysis → same-day anti-GBM + ANCA + urinalysis → start plasma exchange + steroids if high suspicion → biopsy → treatment course.

---

## 6. Calculators and related guides

Link: `calc-plasma-volume.html` (TPE volume), `calc-aki-staging.html`, `calc-anca-renal-risk.html`, `calc-corticosteroid-conversion.html`, `calc-proteinuria-uacr.html`.
Related: `glomerulonephritis.html`, `hematuria-blood-in-urine.html`, `hemoperfusion-blood-purification.html`, `acute-kidney-injury-on-ckd.html`, `kidney-transplant.html`, `complement-mediated-kidney-disease.html`.
Add to `related_guides.json` for `glomerulonephritis.html` and `hematuria-blood-in-urine.html`.

## 7. Glossary seed

AAV, ANCA, CI, ELISA, GBM, GN, IgA, IgAN, IgG, KDIGO, KRT, MN, MPO, NC1, PR3, RPGN, TPE. Terms: basement membrane, crescent, plasma exchange, linear staining, double-positive, seronegative, alloimmune, hexamer.

## 8. Build checklist

1. Read S1–S3 in full; resolve every **[verify]**; extract S1's variant table and per-variant management points.
2. Pull the current KDIGO anti-GBM chapter; quote grades verbatim.
3. Build from the template; four languages in patient mode; dark-mode check.
4. `/setup-guide anti-gbm-disease.html`; APA + acronym audits; `validate_hero_grid.py`; `generate_latest_guides.py`; `generate_sitemap.py`.
5. Independent verification pass before pushing.
