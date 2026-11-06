# Blueprint: Cancer Treatment and Your Kidneys (Onconephrology)

**File:** `guides/onconephrology-chemotherapy-kidney.html`
**Canonical:** `https://renalcarematters.com/guides/onconephrology-chemotherapy-kidney.html`
**Status:** New guide. Implementation handoff for Claude Code (`/setup-guide onconephrology-chemotherapy-kidney.html`), to be opened in its own thread.
**Shape:** Dual-mode (Patients & Families / Clinicians). Patient mode EN/TL/CEB/KAP; clinician mode English-only.
**Index section:** `internal` (orange `#c55a11`) or `advanced` (purple `#6b46c1`) — choose to match where `kidney-cancers.html` and `prostate-cancer-ckd.html` sit in `guides/index.html`.
**Template to copy:** `guides/anemia-management.html` (dual-mode wiring). Drug-table pattern: `guides/medicines-and-your-kidneys.html`.
**Companion calculator (separate build, review item NC-3):** `calc-chemo-renal-dosing.html` — carboplatin (Calvert) dose plus renal adjustment for cisplatin, methotrexate, and others. Build only after this guide's clinician section is verified, and from primary sources (product labels, ADQI tables), not from this blueprint.
**Origin:** Journal review of 6 November 2026, item NG-2 (priority 3).
**Evidence check:** Abstract/skim level (6 Nov 2026). ✔ = read in the paper; **[verify]** = confirm in full text. Build all citations from PubMed (APA 7).
**Review status:** Draft blueprint. Not medically reviewed.

---

## 0. Why this guide

"Onconephrology" appears nowhere on the site, yet it is one of the most common inpatient nephrology consults: AKI during chemotherapy, electrolyte wasting, dosing anticancer drugs in CKD and dialysis, and whether a person on dialysis can receive cancer treatment at all. Kidney International (May 2026) published the 34th ADQI consensus on conventional cytotoxic chemotherapy nephrotoxicity, which gives the guide an authoritative spine.

**Scope (in):** conventional cytotoxic drugs covered by ADQI 34 (cisplatin, ifosfamide, high-dose methotrexate, pemetrexed, gemcitabine, mitomycin C, melphalan); how kidney function should be measured before chemotherapy; prevention, monitoring, and rescue (hydration, magnesium, mesna, glucarpidase); chemotherapy-associated TMA; tumor lysis (brief, link out); kidney cancer screening concepts (Rossi mini review); paraprotein kidney injury pointers (link to `al-amyloidosis-kidneys.html`).

**Scope (out, or brief pointer only):** immune checkpoint inhibitor nephritis and targeted therapies (VEGF inhibitors, TKIs) — not in ADQI 34. Give them one short clinician paragraph with sources verified separately, or defer to a second guide (`onconephrology-immunotherapy-targeted.html`). Do not write chemotherapy regimens or oncologic dosing decisions for patients.

---

## 1. Source papers (on the Mac, `~/Downloads/Journals/`)

| # | File | Type | Contribution | Key data |
|---|---|---|---|---|
| S1 | `Kidney International_20260527/Conventional-cytotoxic-chemotherapy–associated-nep.pdf` | ADQI 34 consensus report, Lentini, Whitman, Jaimes, Forni, Cosmai, Perazella et al., KI 2026;109:1114–1124 | Core of the clinician side | ✔ Drug-by-drug mechanisms, risk factors, histopathologic patterns (Fig 1), prevention, and dose adjustment in CKD (Table 2). ✔ Cisplatin risk factors: female sex, older age, smoking, hypoalbuminemia, reduced GFR, concomitant nephrotoxins, diabetes, heart failure, pre-existing hypomagnesemia. ✔ Cisplatin injury is mainly proximal tubular (outer medulla); MATE1 efflux; magnesium supplementation reduces hypomagnesemia and may protect. ✔ Ifosfamide via OCT2; chloroacetaldehyde/acrolein; risk with cumulative dose >60 g/m² (pediatric data); mesna for bladder. ✔ High-dose methotrexate: AKI 2–50%, dose-dependent (>500 mg/m²), usually nonoliguric and reversible; glucarpidase within 48–60 h lowers plasma MTX up to 99% in 15 min with rebound; use HPLC, not immunoassay, after glucarpidase; consider rechallenge after recovery. ✔ Gemcitabine and mitomycin C: dose-dependent type 1 TMA; mitomycin cumulative >60–70 mg markedly increases TMA/HUS risk (incidence 4–15%), onset 8–12 weeks (gemcitabine 2–6 months, up to 12). ✔ Pemetrexed tubular uptake via reduced folate carrier and folate receptor-α. ✔ Knowledge gaps: no RCTs of nephroprotective agents (magnesium, SGLT2i), early biomarkers not in routine use. **[verify]** the exact consensus statements (wording and whether graded), the kidney-function assessment recommendation (eGFR vs measured GFR vs cystatin C for dosing), the dose-adjustment table values (one row reads: CrCl 46–60 ↓≈20%, 31–45 ↓≈25%, <30 ↓≈30%, HD not recommended — identify which drug), and the validated cisplatin-AKI risk model the report cites (variables include magnesium and cisplatin dose). |
| S2 | `Kidney International_20260620/Kidney-cancer-screening--novel-concepts-beyond-pop.pdf` | Mini review, Rossi et al., KI 2026;110:70–77, doi 10.1016/j.kint.2026.02.039 | Patient section "Should I be screened for kidney cancer?" | ✔ Low prevalence limits cost-effectiveness of population screening; risk-stratified screening with phenotypic scores has moderate predictive ability; adding genetics adds little; piggy-backing on existing imaging (AAA ultrasound, lung-cancer CT) may be more efficient and acceptable. **[verify]** high-risk groups named (e.g., long-term dialysis/acquired cystic disease, hereditary syndromes). |
| S3 | `Kidney International_20260829/Extramedullary-plasmacytoma-with-renal-involvement.pdf` | Nephrology image, KI 2026;110:753–754, doi 10.1016/j.kint.2026.02.014 | Optional clinical image | Paraprotein/plasma-cell kidney involvement; AKI and chemotherapy keywords. **[verify]** details. |
| S4 | `Kidney International_20260829/Diffuse-marrow-FDG-uptake-revealing-lymphoma-assoc.pdf` | Nephrology image | Hypercalcemia from lymphoma | Optional teaching image for "cancer can harm the kidney before treatment." |

**External anchors to verify on PubMed / official sources before use:** ADQI methodology paper; KDIGO Controversies Conference on onconephrology (if current); product labels (cisplatin, carboplatin, methotrexate, pemetrexed) for renal thresholds; the Calvert formula original paper (Calvert 1989, J Clin Oncol) and the FDA/NCI guidance on capping GFR at 125 mL/min for carboplatin dosing **[verify]**; EXTRIP workgroup recommendations on methotrexate (cited in S1); the myeloma-kidney recommendations cited in S1.

---

## 2. Head, meta, structured data

```
<title>Cancer Treatment and Your Kidneys: Chemotherapy, Kidney Injury and Safe Dosing · W Rivero, MD</title>
description: How chemotherapy can affect the kidneys, which drugs carry the most risk (cisplatin, ifosfamide, methotrexate, gemcitabine), how doctors protect the kidneys, and what people with CKD or on dialysis should ask before cancer treatment.
keywords: onconephrology Philippines, chemotherapy kidney damage, cisplatin nephrotoxicity, methotrexate kidney, chemotherapy CKD dialysis dosing, kidney cancer screening
canonical: https://renalcarematters.com/guides/onconephrology-chemotherapy-kidney.html
og image: images/onconephrology-chemotherapy-kidney-og.webp (1200×630)
JSON-LD: Article + MedicalWebPage; about: Neoplasms; Antineoplastic Agents; Acute Kidney Injury; Renal Insufficiency, Chronic. audience Patient + MedicalAudience.
localStorage keys: wgmr-onconeph-mode / wgmr-onconeph-lang
```

---

## 3. Page structure

House chrome per CLAUDE.md. Hero: H1 "Cancer Treatment and Your Kidneys"; subtitle "Protecting the kidneys during chemotherapy"; tag "Onconephrology". Evidence Snapshot in the clinician hero; patient-only vignette.

**One-minute answer (patient, 4 languages)**
1. Some chemotherapy medicines are cleared by the kidneys or can injure them, so your kidney function is checked before and during treatment.
2. Having CKD or being on dialysis does not automatically rule out cancer treatment; the dose or the medicine may need to change.
3. Drinking enough (when your team says so), avoiding pain relievers like NSAIDs, and keeping magnesium and other blood tests on schedule help protect the kidneys.
4. Tell your oncologist and nephrologist about each other; they should plan your treatment together.

**Urgent box (red, both modes):** passing much less urine, swelling or breathlessness, confusion, severe vomiting or diarrhea that stops you drinking, muscle cramps or palpitations (electrolytes), or bruising with dark urine (possible TMA) during or after chemotherapy.

---

## 4. Section map

### Patient mode (EN/TL/CEB/KAP)

| Anchor | Pill | Content |
|---|---|---|
| `#why-kidneys` | Why kidneys | Kidneys filter and secrete many cancer medicines; injury can lower the next dose's safety. Intuition: the kidney is both the exit door and a target. |
| `#before-treatment` | Before | What is checked (creatinine/eGFR, sometimes cystatin C or a measured test, urine, magnesium, potassium, uric acid); why a "normal" creatinine can mislead in thin or older people; bring your medicine list |
| `#higher-risk-drugs` | Medicines | Plain table: cisplatin, ifosfamide, high-dose methotrexate, pemetrexed, gemcitabine/mitomycin — what each can do to the kidney and what the team does to prevent it (hydration, magnesium, mesna, level checks, rescue drug) |
| `#ckd-dialysis` | CKD/dialysis | Cancer care is still possible; dose changes; dialysis timing around chemotherapy; who coordinates |
| `#protect` | Protect | Fluids as advised, no NSAIDs/herbal "detox" products (link `herbal-nephropathy.html`, `nsaid-kidney-injury.html`), keep lab appointments, report symptoms early |
| `#screening` | Screening | Kidney cancer screening (S2): why everyone is not screened; who may benefit; link `kidney-cancers.html` |
| `#questions` | Ask | Question builder (pattern from `first-nephrology-visit-guide.html`) |
| `#faq` | FAQ | Will my kidneys recover? Can I take chemo on dialysis? Should I drink a lot of water? |

### Clinician mode

| Anchor | Pill | Content |
|---|---|---|
| `#md-adqi` | ADQI 34 | What ADQI is, how the consensus was made, statement list with grades/wording verbatim **[verify]** |
| `#md-kidney-function` | Measuring GFR | eGFR vs measured GFR vs cystatin C for anticancer dosing; BSA de-indexing; when to measure (link `how-to-properly-assess-kidney-function.html`, `calc-egfr-cystatin.html`, `calc-measured-crcl.html`, `calc-bsa.html`) |
| `#md-drugs` | Drug by drug | One card per drug: mechanism (transporters: OCT2, MATE1, folate receptor-α), lesion pattern, risk factors, prevention, monitoring, rescue (S1, Table 2, Fig 1) |
| `#md-tma` | Chemo TMA | Gemcitabine/mitomycin dose-dependent type 1 TMA, timing, management; link `complement-mediated-kidney-disease.html#md-tma` |
| `#md-methotrexate` | HD-MTX | AKI mechanism, levels, glucarpidase timing (48–60 h), HPLC after glucarpidase, rebound, rechallenge, dialysis role per EXTRIP **[verify]** |
| `#md-dosing` | Dosing | ADQI dose-adjustment table reproduced from source with drug names; carboplatin Calvert formula (link the planned calculator); dialysis timing |
| `#md-other-classes` | Beyond cytotoxics | One paragraph each: checkpoint inhibitor AIN, VEGF-pathway proteinuria/TMA, TLS — with separately verified citations, or defer |
| `#md-gaps` | Gaps | No RCTs for nephroprotection (magnesium, SGLT2i), biomarkers, genetics (S1 knowledge gaps) |
| `#md-philippines` | Philippines | Access to drug levels, glucarpidase availability, PhilHealth/oncology packages **[verify each claim]** |

**Evidence Snapshot (`.v` ≤ 8 chars)**

| `.v` | `.l` |
|---|---|
| ADQI 34 | Consensus on cytotoxic chemotherapy nephrotoxicity (KI 2026) |
| 2–50% | Reported AKI incidence with high-dose methotrexate |
| >500 | MTX dose (mg/m²) most associated with AKI |
| 99% | Plasma MTX drop within 15 min after glucarpidase (rebound follows) |
| 4–15% | Mitomycin C TMA/HUS incidence at high cumulative dose |

---

## 5. Figures

1. Hero vignette: patient in a chemotherapy chair with a nephrologist and oncologist conferring (patient-mode only).
2. Mechanism (biomedical-mechanism-figure skill): proximal tubule cell with OCT2 uptake and MATE1 efflux of cisplatin → injury → magnesium wasting.
3. Histopathology pattern map redrawn from S1 Fig 1 as an original schematic (do not copy the figure).
4. Algorithm (algorithm-generator skill): "Before cisplatin" checklist — GFR method, magnesium, hydration plan, nephrotoxin review, monitoring schedule.

---

## 6. Calculators and related guides

Link: `calc-egfr-cystatin.html`, `calc-cockcroft-gault.html`, `calc-measured-crcl.html`, `calc-bsa.html`, `calc-electrolyte-repletion.html`, `calc-aki-staging.html`, `calc-renal-med-safety.html`. Planned: `calc-chemo-renal-dosing.html` (NC-3).

Related guides: `kidney-cancers.html`, `prostate-cancer-ckd.html`, `al-amyloidosis-kidneys.html`, `esa-dose-cancer-risk.html`, `contrast-nephropathy.html`, `medicines-and-your-kidneys.html`, `nsaid-kidney-injury.html`, `complement-mediated-kidney-disease.html`, `magnesium-supplements-ckd.html`.

## 7. Glossary seed

AAA, ADQI, AIN, AKI, BSA, CKD, CrCl, CT, eGFR, EXTRIP, FDG, GFR, HD, HPLC, HUS, MATE1, MTX, NSAID, OCT2, SGLT2i, TKI, TLS, TMA, VEGF. Terms: nephrotoxicity, glucarpidase, mesna, Fanconi syndrome, tumor lysis, cumulative dose, de-indexed GFR.

## 8. Build checklist

1. Read S1 in full; transcribe every consensus statement and table value with the drug it belongs to; resolve all **[verify]**.
2. Verify external anchors (labels, Calvert, EXTRIP) on PubMed/official sources.
3. Build the guide from the template; four languages in patient mode; dark-mode contrast check.
4. `/setup-guide onconephrology-chemotherapy-kidney.html`; APA and acronym audits; `validate_hero_grid.py`; `generate_latest_guides.py`; `generate_sitemap.py`.
5. Independent verification pass before pushing. Then scope the companion calculator (NC-3) as a separate thread.
