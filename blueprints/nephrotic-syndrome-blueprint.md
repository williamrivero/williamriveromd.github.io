# Blueprint: Nephrotic Syndrome — When the Kidney Filter Leaks Protein

**File:** `guides/nephrotic-syndrome.html`
**Canonical:** `https://renalcarematters.com/guides/nephrotic-syndrome.html`
**Status:** New guide. Implementation handoff for Claude Code (`/setup-guide nephrotic-syndrome.html`), to be opened in its own thread.
**Shape:** Dual-mode (Patients & Families / Clinicians). Patient mode in EN/TL/CEB/KAP; clinician mode English-only.
**Index section:** `nephrology` (teal `#1a6b72`); tile icon: kidney or flask (`data-icon` key from the `ICONS` map in `guides/index.html`).
**Template to copy:** `guides/anemia-management.html` (dual-mode wiring, Evidence Snapshot aside, patient-scoped vignette). Glossary markup: `guides/complement-mediated-kidney-disease.html`.
**Origin:** Journal review of 6 November 2026 (`renalcarematters-journal-review-opportunities.xlsx`, item NG-1, priority 1).
**Evidence check:** Abstract-level only (6 Nov 2026). Every number below marked ✔ was read in the paper's abstract or results; anything marked **[verify]** must be confirmed against the full text before it is written. All citations must be built from PubMed metadata (APA 7); none are pre-verified here.
**Review status:** Draft blueprint. Not medically reviewed. Do not stamp review dates by hand; the patch scripts stamp them at merge.

---

## 0. Why this guide, and scope decision

Nephrotic syndrome appears in 19 guides but has no home of its own; the closest page, `glomerulonephritis.html`, treats it as one row among many. The May–September 2026 journals in `~/Downloads/Journals` contain a cluster of papers that change how clinicians diagnose and monitor the three main adult causes (minimal change disease, FSGS, membranous nephropathy): antigen-specific serology beyond PLA2R (NELL1), anti-nephrin antibodies as the first marker of "autoimmune podocytopathy," a steroid-sparing MCD trial, and B-cell predictors of relapse after rituximab.

**Decision:** one hub guide, adult-focused, with a clinician section on children and genetics. The review spreadsheet suggested a possible split (MCD/FSGS vs. membranous). Do not split now: the shared physiology (podocyte injury → protein leak → edema, clots, lipids, infection) is the teaching spine, and patients rarely know which subtype they have when they first search. If the clinician side exceeds ~45 minutes reading time, split membranous nephropathy into `membranous-nephropathy-clinician.html` later.

**Out of scope:** dosing tables for immunosuppressants beyond what guidelines state; diabetic, amyloid, lupus, and HIV-associated nephrotic disease (link out instead to `diabetes-kidneys.html`, `al-amyloidosis-kidneys.html`, `lupus-nephritis.html`, `hivan-hiv-kidney-disease.html`); a pediatric management protocol (link to `ckd-children-young-adults.html`).

---

## 1. Source papers (on the Mac)

Read each in full before writing. Stage with the device tools from `/Users/williamgregoryriveromd/Downloads/Journals/`. Prefer the markitdown MCP for PDF → Markdown (CLAUDE.md, PDF handling).

| # | Folder / file | Type | What it contributes | Key data |
|---|---|---|---|---|
| S1 | `Kidney International_20260527/A-randomized-controlled-non-inferiority-trial-exam.pdf` | RCT (ADAPT), Kristensen et al., KI 2026;109:1308–1317, doi 10.1016/j.kint.2026.02.035 | Lower-dose prednisolone + alfacalcidol vs standard 1 mg/kg in adult MCD | ✔ n=67, open-label, multicenter. ✔ Non-inferiority **not** reached. ✔ Remission 88% (95% CI 74–96) vs 91% (78–98). ✔ Median time to remission 28 vs 23 days; relapse 35% vs 32%. ✔ Cumulative prednisolone 3.7 g vs 8.0 g; fewer serious AEs; glucocorticoid toxicity score 46 vs 74. **[verify]** exact dosing schedule, alfacalcidol dose, toxicity index used, follow-up length. |
| S2 | `Kidney International_20260527/Anti-PLA2R1-IgG-mediated-podocyte-PLA2R1-cleavage-.pdf` | Basic/translational, KI 2026;109:1282–1295, doi 10.1016/j.kint.2026.02.021 | Mechanism: anti-PLA2R1 IgG accelerates ADAM10/17 shedding of the podocyte PLA2R1 ectodomain, which anchors to GBM collagen IV/laminin | Mechanism only (cell lines, biopsies). Use for the "why deposits sit under the podocyte" teaching; label as laboratory evidence. |
| S3 | `Kidney International_20260829/Quantitative-serological-detection-of-NELL1-autoan.pdf` | Diagnostic study, Burbelo et al., KI 2026;110:698–703, doi 10.1016/j.kint.2026.05.017 | Blood test (LIPS assay) for anti-NELL1, the second most common MN antigen | ✔ Validation 20 NELL1+ vs 20 PLA2R+/NELL1–: sensitivity 90%, specificity 100%. ✔ 6 NELL1+ of 63 MN in NIH cohort. ✔ Titers tracked proteinuria in 3 patients. Research assay; **not commercially available**. |
| S4 | `Kidney International Reports_20260629/Early-Stage-B-cells-Predict-Relapse-After-Rituxima.pdf` | Research letter (PMMN trial substudy, NCT03804359) | B-cell reconstitution pattern after rituximab in PLA2R-MN predicts relapse | ✔ 39 included, 36 given rituximab; 19 sustained remission, 9 no remission, 8 relapses (2 clinical, 6 immunologic; immunologic relapse = anti-PLA2R >14 RU/mL after <14). **[verify]** which early-stage (transitional/naïve) subset and the effect size. |
| S5 | `Kidney International Reports_20260629/Utility-of-Antinephrin-Autoantibody–to–IgG-Ratio-i.pdf` | Research letter (Japan) | Anti-nephrin antibody adjusted for serum IgG (because IgG is lost in urine) in SRNS and post-transplant FSGS recurrence | **[verify]** n, ratio behavior vs raw titer. Includes 2 recurrent-FSGS cases (one graft loss at 2 y; one remission with pulse steroid + rituximab + plasma exchange). |
| S6 | `Kidney International_20260922/Monitoring-anti-nephrin-antibodies-in-the-manageme.pdf` | Clinical journey (case), Fernandez et al., KI 2026;110:1055–1057, doi 10.1016/j.kint.2026.06.013 | Serial anti-nephrin antibodies guiding management of recurrent diffuse podocytopathy after living-related transplant | Single case (33-year-old, MCD → FSGS → kidney failure, negative genetics). Illustrative only. |
| S7 | `Kidney International_20260922/Nephrin-missense-variants-affecting-post-translati.pdf` | Letter | Genetic side of nephrin | **[verify]** content; likely clinician-only footnote. |
| S8 | `Kidney International_20260922/A-multi-national-study-examined-the-response-susta.pdf` | Research letter, Malakasioti et al., KI 2026;110:1022–1028 | CNI response in children with **genetic** podocytopathies | ✔ n=136; median follow-up 42.1 months; at-least-partial response 28% at 6 months, 22% at last follow-up. **[verify]** kidney-failure outcomes in responders vs non-responders. |
| S9 | `Kidney International_20260527/Polygenic-risk-scores-and-HLA-class-II-variants-ar.pdf` | GWAS, KI 2026;109:1256–1268, doi 10.1016/j.kint.2026.01.026 | Predicting steroid response in childhood NS | ✔ 1,997 children + 3,558 controls. ✔ HLA-DQB1/DRB1/DQA1 and CLEC16A loci for SSNS (not SRNS). ✔ HLA-DRB1\*07:01∼DQA1\*02:01∼DQB1\*02:02 ≈4× risk of SSNS. ✔ Model AUC 0.68–0.70; accuracy 67–71%. Research tool; not for clinical decisions. |
| S10 | `Kidney International_20260527/Toward-personalized-medicine-in-childhood-nephroti.pdf` | Commentary on S9 | Context and limits | Read for framing. |
| S11 | `Kidney International Reports_20260629/NPHS2-Revisited-Through-208-Cases-and-Podocin-Comp.pdf` | Case series + structural model | Podocin (NPHS2) genotype–onset relationships | ✔ 208 cases; median onset 2.75 y (0–30). ✔ Later onset with p.R229Q compound heterozygosity and certain missense variants. Clinician genetics box only. |
| S12 | `Kidney International_20260620/The-Case---Relapsing-nephrotic-syndrome_kint.pdf` | Case | **[verify]** diagnosis and teaching point before using. |

**Guideline anchors to fetch and verify on PubMed (not in the folder):** KDIGO 2021 Glomerular Diseases guideline and its chapter updates since 2024 (check which chapters cover MN, MCD, FSGS, and childhood nephrotic syndrome; the KDIGO "life cycle" mini review in KI says 4 chapters have been updated). Use the current chapter for every graded statement and quote its grade (1/2, A–D) exactly; see `ckd-blood-pressure-target-standardized.html#md-guidelines` for the house "How to read a KDIGO recommendation" box.

---

## 2. Head, meta, structured data

```
<title>Nephrotic Syndrome: When the Kidney Filter Leaks Protein · W Rivero, MD</title>
description: Foamy urine, swelling, low albumin: what nephrotic syndrome is, the three common adult causes (minimal change disease, FSGS, membranous nephropathy), the new antibody tests, and how treatment works.
keywords: nephrotic syndrome Philippines, minimal change disease, FSGS, membranous nephropathy, PLA2R, NELL1, anti-nephrin antibody, rituximab nephrotic syndrome, proteinuria edema
canonical: https://renalcarematters.com/guides/nephrotic-syndrome.html
og/twitter image: images/nephrotic-syndrome-og.webp (1200 × 630, width/height/alt tags)
JSON-LD: Article + MedicalWebPage; about: Nephrotic Syndrome; Minimal Change Disease; Focal Segmental Glomerulosclerosis; Membranous Glomerulonephritis. audience Patient + MedicalAudience. Dates left to patchers.
localStorage keys: wgmr-nephrotic-mode / wgmr-nephrotic-lang
```

No `williamriveromd.com` anywhere.

---

## 3. Page structure

House chrome exactly as CLAUDE.md "Site-wide chrome conventions" and the anemia template: header (brand · header-lang · header-nav as direct child) → audience tabs → hero (hero-copy, `aside.hero-cards.mode-physician` Evidence Snapshot, `figure.hero-figure.mode-patient` vignette; nothing else inside `.hero-grid`) → `div.container` with one-minute answer + urgent box → nav pills → `<main>` → glossary → references accordion → dr-card → related-guides → footer.

**Hero**
- H1: Nephrotic Syndrome
- Subtitle: When the kidney filter leaks protein
- Tag: Glomerular disease · Diagnosis & treatment

**One-minute answer (patient, 4 languages)**
1. Nephrotic syndrome is a pattern, not one disease: heavy protein in the urine, low blood albumin, swelling, and usually high cholesterol.
2. In adults the three common causes are minimal change disease, FSGS, and membranous nephropathy. A blood antibody test or a biopsy tells them apart.
3. Most people respond to treatment, but it takes weeks, and relapses are common, so follow-up matters.
4. The leak also raises the risk of blood clots and infections; know the warning signs below.

**Urgent box (red, both modes):** sudden one-sided leg swelling or calf pain, chest pain or sudden breathlessness (clot); fever with abdominal pain or a red, hot, swollen skin area (infection, peritonitis in a swollen abdomen); passing very little urine; severe swelling with weight gain over days. Seek same-day care.

---

## 4. Section map

Teaching order in every section: intuition → physiology → evidence → application (medical-teaching standard).

### Patient mode (EN/TL/CEB/KAP)

| Anchor | Pill | Content | Component |
|---|---|---|---|
| `#what-it-is` | What it is | The four features; foamy urine; why albumin matters (holds water in the blood vessels like a sponge) | intro + Fig 1 |
| `#why-swelling` | Swelling | Physiology walkthrough: filter leaks albumin → oncotic pressure falls and the kidney holds on to salt → fluid moves to legs, eyelids, abdomen. Name both mechanisms (underfill vs overfill) in plain words; avoid claiming one dominates. | Fig 2 mechanism |
| `#three-causes` | Causes | MCD, FSGS, MN in one comparison table: who gets it, how it is diagnosed, how it usually responds | table |
| `#tests` | Tests | Urine protein/creatinine or 24-h protein; albumin; lipids; anti-PLA2R blood test; why a biopsy may still be needed; new tests in research (NELL1, anti-nephrin) explained as "coming, not routine yet" | table + teal alert |
| `#treatment` | Treatment | Steroids (why weeks, what side effects to watch), steroid-sparing options, rituximab as an infusion that removes B cells; supportive care (ACE inhibitor/ARB, salt restriction, diuretics, statin, sometimes blood thinner); vaccines before immune-suppressing treatment | green/amber alerts |
| `#lower-dose-steroids` | New: lower dose | ADAPT in plain words: a lower prednisolone dose plus activated vitamin D worked about as often and caused fewer steroid side effects, but the trial could not prove it was "as good." Not a reason to change your own dose. | purple alert (honesty box) |
| `#relapse` | Relapse | What a relapse looks like (foamy urine, puffiness, dipstick); home dipstick log; why antibody levels are rechecked | checklist |
| `#daily-life` | Daily life | Salt, protein (no high-protein diet), fluids only if told, infection prevention, clot warning signs, pregnancy planning (link `ckd-and-pregnancy.html`) | alerts |
| `#questions` | Ask your doctor | Question list (copy/print pattern from `first-nephrology-visit-guide.html` `qb-*`) | builder |
| `#faq` | FAQ | Is it cancer? Will I need dialysis? Can it come back after transplant? Is it inherited? | `.qa-item` |

### Clinician mode (English-only)

| Anchor | Pill | Content |
|---|---|---|
| `#md-framework` | Framework | Podocytopathy vs membranous pattern; primary vs secondary vs genetic vs maladaptive FSGS; the role of the biopsy; KDIGO terminology |
| `#md-mn-serology` | MN antigens | PLA2R (≈70% of MN, S4 intro), THSD7A, NELL1 (S3: 90/100 sensitivity/specificity, research LIPS assay, titers track proteinuria); mechanism box from S2 labeled "laboratory evidence"; secondary-cause search by antigen (e.g., NELL1 and malignancy/drugs **[verify in KDIGO/literature before stating]**) |
| `#md-mn-treatment` | MN treatment | Risk stratification per current KDIGO chapter; rituximab; immunologic vs clinical remission and relapse definitions (S4: anti-PLA2R threshold 14 RU/mL); B-cell reconstitution as a relapse predictor (S4) labeled exploratory |
| `#md-anti-nephrin` | Anti-nephrin | Autoimmune podocytopathy concept; anti-nephrin in MCD/FSGS and post-transplant recurrence; S5 (IgG-adjusted ratio, because antibody is lost in urine) and S6 (serial monitoring case); assays not standardized, no validated cutoffs; not available locally **[verify]** |
| `#md-mcd` | MCD therapy | Standard 1 mg/kg prednisolone; ADAPT (S1) full appraisal: n=67, open-label, non-inferiority not met, remission 88% vs 91%, cumulative dose 3.7 vs 8.0 g, fewer serious AEs. Bottom line: hypothesis-generating steroid-sparing option, not a new standard. Alfacalcidol rationale **[verify from paper]**; calcium monitoring. |
| `#md-fsgs` | FSGS | Primary vs genetic vs maladaptive; when to test genetics; CNI in genetic podocytopathy (S8: 28% → 22% response; continue only in responders) |
| `#md-children-genetics` | Children & genes | SSNS vs SRNS; HLA/PRS (S9, AUC 0.68–0.70 — research only, S10 caveats); NPHS2 genotype–onset (S11); link `ckd-children-young-adults.html` |
| `#md-complications` | Complications | Thromboembolism (MN highest risk; prophylactic anticoagulation decisions per albumin and bleeding risk — **[verify current KDIGO practice point and any validated tool]**), infection and vaccination, dyslipidemia (link `dyslipidemia-2026.html`), AKI, edema and diuretic resistance |
| `#md-recurrence` | Transplant | Recurrence risk by cause; anti-nephrin and anti-PLA2R before transplant; S5/S6 cases |
| `#md-philippines` | Philippines | Availability and cost of anti-PLA2R testing and rituximab; biopsy access; PhilHealth coverage **[verify every claim; state "check with your center" where uncertain]** |
| `#md-evidence` | Evidence grade | Table: claim · evidence type · certainty (RCT / cohort / case / laboratory) |

**Evidence Snapshot (`.v` ≤ 8 chars)**

| `.v` | `.l` |
|---|---|
| 88% v 91% | ADAPT: MCD remission, lower-dose + alfacalcidol vs standard (non-inferiority not met) |
| 3.7 g | ADAPT: cumulative prednisolone with the lower-dose arm (vs 8.0 g) |
| 90%/100% | NELL1 LIPS assay sensitivity/specificity (research assay) |
| ~70% | MN with anti-PLA2R antibodies |
| 22% | Genetic podocytopathy: sustained CNI response at last follow-up |

(`88% v 91%` is 9 characters; shorten to `88 v 91%` if the audit or layout complains.)

---

## 5. Figures (prompt pack to be written in this guide's thread)

Use the repo skills (`williamriveromd-biomedical-mechanism-figure`, `williamriveromd-simple-figure`, `williamriveromd-hero-vignette`). Each figure needs a `figcaption` with `.fig-desc` and a `dl.fig-abbrevs` (rule 11).

1. Hero vignette: adult Filipino patient checking ankle swelling at home, family member beside them (patient-mode only).
2. Mechanism: glomerulus → podocyte foot processes → albumin leak → edema/lipids/clots (organ → magnified podocyte → consequences).
3. Membranous mechanism: PLA2R ectodomain shed and anchored to the GBM with IgG (S2), labeled "laboratory model."
4. Comparison panel MCD / FSGS / MN (who, test, response).
5. Code-native SVG (not AI): ADAPT remission and cumulative dose bars, exact numbers from S1.

---

## 6. Calculators to link (confirm each slug exists)

`calc-proteinuria-uacr.html`, `calc-urine-protein-excretion.html`, `calc-corticosteroid-conversion.html`, `calc-lipid-panel.html`, `calc-egfr-ckd-epi.html`, `calc-ckid-u25-egfr.html` (children). No new calculator in scope; a thromboprophylaxis decision aid for MN would need its own validated source first.

## 7. Related guides

`glomerulonephritis.html`, `proteins-proteinuria.html`, `hematuria-blood-in-urine.html`, `complement-targeted-therapy-kidney-disease.html`, `ckd-children-young-adults.html`, `dyslipidemia-2026.html`, `kidney-transplant.html`, `viral-infections-vaccinations-ckd.html`. Add `nephrotic-syndrome.html` to `related_guides.json` for `glomerulonephritis.html` and `proteins-proteinuria.html`, and a one-line cross-link from `glomerulonephritis.html`.

## 8. Glossary seed (Abbreviations)

ACE, ADAM, AE, ARB, AUC, CI, CNI, FSGS, GBM, GWAS, HLA, IgG, KDIGO, LIPS, MCD, MN, NELL1, NPHS2, NS, PLA2R, PRS, RU, SRNS, SSNS, THSD7A. Terms: podocyte, foot process, oncotic pressure, remission (complete/partial), immunologic remission, relapse, steroid-dependent, steroid-resistant, autoimmune podocytopathy.

## 9. Build checklist (in the guide's thread)

1. Stage and read S1–S12 in full; replace every **[verify]**.
2. Pull current KDIGO chapters; record grades verbatim.
3. Build references via PubMed MCP in APA 7 (`--overrides refs.json`).
4. Author the page from the anemia template; patient strings in 4 languages; dark-mode contrast check.
5. Run `/setup-guide nephrotic-syndrome.html` (patch pipeline), then `audit_apa_references.py --guide`, `audit_acronym_expansion.py --guide`, `validate_hero_grid.py`, `generate_latest_guides.py`, `generate_sitemap.py`.
6. Independent verification pass (numbers vs papers, citations vs PubMed, translations, HTML balance) before pushing to `main`.
