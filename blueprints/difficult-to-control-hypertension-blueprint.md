# Complete blueprint: Difficult-to-Control Hypertension in Filipinos

Consolidated handoff edition · 27 September 2026

This file contains the complete modular blueprint and Claude Code execution prompt. The companion files remain available for focused review.



---

<!-- Source document: README.md -->

# Difficult-to-Control Hypertension in Filipinos

**Architectural blueprint and Claude Code handoff · 27 September 2026 · v1.0**

Build a mobile-friendly, searchable clinical web guide with a patient companion and printable algorithms. Clinician content is English. Patient content must support **English, Tagalog, Cebuano, and Kapampangan**, matching the language set requested by the owner and observed on [Renal Care Matters](https://renalcarematters.com/).

This package defines the product, clinical content, research foundation, implementation contracts, and release criteria. It is a researched development blueprint, not an already medically signed-off treatment protocol. Research was checked on 27 September 2026 Manila time. This was a targeted primary-source search, not a systematic review.

## Read in this order

1. [Product and content architecture](01-PRODUCT-AND-CONTENT.md)
2. [Clinical pathways and print specifications](02-CLINICAL-PATHWAYS.md)
3. [Evidence register and research update plan](03-EVIDENCE-REGISTER.md)
4. [Technical architecture and acceptance tests](04-TECHNICAL-ARCHITECTURE.md)
5. [Patient language and editorial specification](05-PATIENT-LANGUAGES.md)
6. [Calculator audit and gap specifications](06-CALCULATOR-AUDIT-AND-SPECIFICATIONS.md)
7. [Philippine medication hierarchy and local-market evidence](07-PHILIPPINE-MEDICATION-HIERARCHY.md)
8. [Claude Code execution prompt](CLAUDE-CODE-HANDOFF.md)

## Decisions already made

- Dual audience, explicitly switchable; retain the corresponding topic when switching.
- Four patient languages; clinician pages remain English.
- Philippine practice context, with international guidance clearly attributed.
- Use the existing Renal Care Matters repository and components if supplied. Do not assume its technology from the public website.
- No new account system or patient database in the initial release.
- Use source-linked, deterministic educational tools; no generative treatment chatbot.
- Separate established care, guideline differences, specialist options, and emerging research.
- Keep pregnancy/postpartum, dialysis, transplant, and pediatric care outside the generic adult medication pathway, with prominent dedicated exits or specialist overlays.
- Deliver print layouts from the same content records as the web pages.
- Reuse the site's existing tools; implement the specified gaps only after checking for unindexed equivalents in the repository.
- Show an explicit medication hierarchy with dated Philippine product evidence and conditional branches for locally unverified options.

## What makes this guide distinct

Start with **why BP remains high**, rather than immediately adding another drug: measurement, out-of-office confirmation, regimen adequacy, practical access, adherence, interfering substances, secondary causes, and volume status. Explain the difference between difficult-to-control, apparent resistant, and confirmed resistant hypertension.

Local relevance comes from real Philippine studies, access pathways, food examples, laboratory constraints, and care coordination. It must not become an unsupported claim that Filipino ancestry requires its own universal drug ladder.

## Important research findings incorporated

- The 2020 Philippine general hypertension CPG remains the national general-management anchor located in this search; verify with PSH/PHA before release that it has not been superseded.
- The **2024 Philippine acute severe BP CPG executive summary was published in January 2026**. Guideline year and publication year must be stored separately.
- Include AHA/ACC 2025, ESC 2024, Endocrine Society 2025, KDIGO 2024, ADA 2026, and the 2026 Asian expert consensus.
- Include Bax24 (2026), BaxHTN (2025), lorundrostat trials (2025), and the 2025 amiloride comparison. Trial results do not establish Philippine registration, supply, or reimbursement.
- ISH announced its 2026 global guideline for **October 2026**; as of this research cutoff, treat it as forthcoming, not a published source of recommendations. See the linked official announcement in the evidence register.

## Completion boundaries

The architecture and implementation brief are complete. The future implementation still needs repository inspection, full recommendation extraction, clinical sign-off, and native-language review. Drug registration, local prices, participating facilities, full dose tables, assay-specific ARR interpretation, and review identities must never be invented to make the site appear complete.

All source links and evidence limitations are in the evidence register. The handoff directs Claude Code to build a complete reviewable preview and keep unsigned clinical material out of a production release.


---

<!-- Source document: 01-PRODUCT-AND-CONTENT.md -->

# Product and content architecture

## 1. Product definition

Working title: **When Blood Pressure Stays High**.

Clinical subtitle: **Difficult-to-Control and Resistant Hypertension in Filipinos**.

Patient promise: Understand why your BP may still be high, measure it properly, prepare for the next visit, and know when to seek help.

Clinical promise: Move from an elevated reading to a defensible phenotype, a cause-directed evaluation, and a monitored treatment plan, with Philippine context and traceable evidence.

Primary users are internists, general practitioners, nephrologists, cardiologists, trainees, nurses, patients, and caregivers. The clinician experience supports fast consultation and deeper reading. The patient experience supports understanding and practical action, without exposing dose-escalation tools as self-treatment instructions.

The initial implementation should be a new guide within the existing Renal Care Matters library if its repository is provided. The public [library](https://renalcarematters.com/guides/) demonstrates patient and professional entry points, topic navigation, tools, and four languages. These are integration references, not evidence that the underlying code or every existing clinical statement has been audited.

## 2. Scope

Core population: adults with persistently elevated BP despite prescribed treatment, especially suspected or confirmed resistant hypertension in Philippine outpatient practice.

Include:

- Sustained uncontrolled BP, white-coat effect, masked uncontrolled BP, and measurement error.
- Apparent resistance, confirmed resistance, treatment intolerance, access-related interruptions, and clinical inertia.
- Secondary hypertension, organ damage, CKD, diabetes, obesity/OSA, and volume excess.
- Established treatment optimization and monitored add-on therapy.
- Specialist therapies and current trials, labeled by evidence and local availability status.
- Patient home monitoring, medication understanding, food choices, care access, and appointment preparation.

Boundary modules: suspected emergencies, pregnancy/postpartum, pediatrics, dialysis, and transplant. These need clear exits from the generic adult algorithm. Dialysis and transplant get focused explanatory modules because this is a kidney-care library; do not apply nondialysis BP targets automatically.

Not in version 1: automated diagnosis, autonomous prescribing, emergency infusion calculators, authenticated patient records, clinician messaging, remote surveillance, or a chatbot that generates treatment plans.

## 3. Information architecture

The paths below are proposed route contracts. Adapt names to existing repository conventions without breaking stable topic IDs.

| Route | Purpose |
|---|---|
| `/guides/difficult-to-control-hypertension` | Canonical entry; audience choice and guide summary |
| `…/clinician` | Clinical overview and consultation checklist |
| `…/clinician/confirm` | Measurement, HBPM/ABPM, phenotype |
| `…/clinician/causes` | Regimen, adherence, substances, secondary causes |
| `…/clinician/treatment` | Optimization, monitoring, add-on options |
| `…/clinician/ckd` | CKD, potassium, volume, diabetes overlays |
| `…/clinician/specialist` | Referral, devices, complex phenotypes |
| `…/clinician/evidence` | Guidelines, trials, conflicts, update ledger |
| `…/patient/{en,tl,ceb,pam}` | Language-specific patient landing page |
| `…/patient/{locale}/{topic}` | Readings, medicines, food, tests, follow-up, urgent help |
| `…/print/{artifact}/{locale}` | Print-ready document with version and provenance |

Keep a mapping between clinical and patient topics. A clinician on the adherence page who chooses patient mode should land on “Making your medicines easier to take,” not the homepage. When there is no equivalent topic, land on the closest reviewed summary and say so.

Language choice and audience are separate controls. Keep a patient's preferred language when visiting clinician English pages and restore it when returning. URLs must reconstruct the mode and language on another device. Save only preferences by default, not health information.

## 4. Clinical content map

Each module has a 30-second summary, a practical checklist, deeper explanation, evidence drawer, Philippine applicability note, and printable output where useful.

| ID | Module | Required content and output |
|---|---|---|
| C01 | Start with the clinical problem | Definitions, above-goal versus diagnostic threshold, apparent/confirmed resistance, controlled resistance under the relevant framework; consultation map |
| C02 | Is this urgent? | Symptoms and acute organ-injury assessment; emergency versus severe asymptomatic BP; pregnancy/postpartum and acute stroke exits; triage card |
| C03 | Can the readings be trusted? | Device validation, cuff fit, posture, rest, repeated readings, arrhythmia considerations, office versus home versus ambulatory measurement; technique checklist |
| C04 | Confirm the phenotype | HBPM and ABPM protocols, insufficient data, discordant values, nocturnal patterns; BP summary tool |
| C05 | Reconcile what is actually taken | Drug name, class, formulation, dose, timing, last dose, missed doses, dispensing access, side effects; medication checklist |
| C06 | Find contributors | Sodium, alcohol, sleep, pain, relevant OTC/prescription/herbal substances, occupational schedules; contributor inventory |
| C07 | Assess consequences and baseline risk | Kidney function, electrolytes, urine albumin, cardiometabolic tests, ECG and targeted organ assessment; investigation checklist |
| C08 | Look for secondary causes | PA, renal disease, renovascular disease, OSA, endocrine and uncommon causes; clue-to-test-to-referral table |
| C09 | Primary aldosteronism | Renin and aldosterone assays, potassium, interfering drugs, contextual interpretation, specialist confirmation/subtyping; screening preparation sheet |
| C10 | Optimize the core regimen | Appropriate complementary drug classes, formulation/adherence, diuretic strategy, tolerability and follow-up; optimization map |
| C11 | Add-on therapy | MRA selection, kidney/potassium constraints, alternatives, monitoring and interactions; clinician-only drug reference |
| C12 | CKD and volume | Albuminuria, advanced CKD, potassium risk, diuretic choices, volume assessment, AKI/illness context; CKD overlay |
| C13 | Other complex phenotypes | Diabetes, older age/frailty, orthostatic symptoms, obesity/OSA, HF/CAD, prior stroke; linked disease-specific modules |
| C14 | Dialysis and transplant | Dry-weight/sodium/dialysis adequacy and medication timing; transplant drugs and interactions; specialist-only contextual guidance |
| C15 | Refer and reassess | Referral indications, information bundle, follow-up ownership, missed follow-up, specialist options; referral packet |
| C16 | Emerging treatments | Aprocitentan, aldosterone synthase inhibitors, renal denervation; regulatory and evidence separation |
| C17 | Philippine implementation | Actual access barriers, essential versus enhanced testing, medicine access, local evidence; practical care-planning worksheet |
| C18 | Evidence and updates | Guideline comparison, study cards, uncertainty, corrections, review dates, editorial decisions |

## 5. Patient content map

All of the following must be available in English, Tagalog, Cebuano, and Kapampangan. Translate the patient adaptation, not the technical chapter.

| ID | Patient question | Practical endpoint |
|---|---|---|
| P01 | Why is my BP still high? | Explain multiple possible causes without blame or implying that treatment cannot work |
| P02 | What do my BP numbers mean? | Distinguish a reading, an average, a diagnosis, and the personal target set by the clinician |
| P03 | How do I measure BP at home? | Illustrated technique, repeat-reading routine, device/cuff checklist |
| P04 | When do I need urgent help? | Simple symptom-first action card, accessible without navigating the rest of the guide |
| P05 | Why do I need several medicines? | Explain complementary roles, daily use, side effects, refill barriers, and who to contact |
| P06 | What can raise my BP? | Practical review of medicines, supplements, food, sleep, alcohol, and pain with clinician discussion |
| P07 | What can I change in Filipino meals? | Portions, labels, sauces and processed foods; kidney/potassium caveats |
| P08 | Why am I being sent for tests? | Kidney, hormone, sleep and urine tests, with questions about preparation and cost |
| P09 | What if I have kidney disease or diabetes? | Personalization of targets, diet and monitoring; no generic fluid or potassium prescription |
| P10 | How can I make treatment affordable? | Refill plan, generic-name list, care-team discussion, dated official access links |
| P11 | How do I prepare for the next visit? | BP log, medication list, symptom record, questions, test dates |
| P12 | How can my family help? | Consent-based support, reminders and shared meals without policing or blame |

## 6. Content presentation

Desktop clinician layout: left topic navigation, central text, right evidence/quick-reference rail. Mobile: one column with a compact topic menu, persistent mode control, and a visible urgent-help link. Avoid drawers nested inside drawers.

Clinician cards should answer: “What should I assess?”, “What changes management?”, “What prevents the next step?”, and “Which source supports this?” Patient cards should answer one question and end with one clear action.

Use an existing site type scale and palette. If starting independently, use a readable sans-serif, restrained teal/navy, warm neutral backgrounds, generous spacing, and red only for urgent actions. Do not use flags to represent languages. Charts must distinguish series by labels and line styles as well as color.

A visible evidence label should distinguish:

- Philippine guideline;
- international guideline;
- randomized trial;
- observational/local pilot evidence;
- expert consensus;
- editorial implementation choice;
- emerging evidence/local status unverified.

Do not invent a single confidence score that conceals different grading systems. Show the source's actual recommendation class or certainty when verified, with an explanation.

## 7. Philippine adaptation

Localize practical decisions rather than prescribing by ethnicity. Include cost, travel, laboratory access, ABPM/device access, continuity of supply, and dosing schedules compatible with work and caregiving. Offer an essential-resource workflow and an enhanced-resource workflow; unavailable ABPM must remain a documented limitation, not silently count as normal out-of-office BP.

Food examples may include patis, toyo, bagoong, seasoning cubes, instant noodles, dried/salted fish and processed meats. Do not imply these are consumed by every Filipino or publish precise sodium amounts without product/portion data. Explain serving size and cumulative sodium. Preserve enjoyment, affordability, and regional food variation.

Keep separate fields for Philippine FDA registration, local stock, formulary inclusion, insurance coverage, and cost. Registration does not prove supply. A guideline recommendation does not prove reimbursement. Link current official YAKAP/GAMOT guidance with the date checked; avoid promises of universal free availability.

Describe Philippine studies with their sample size, site, recruitment and limitations. Separate local Filipino studies from Asian studies and diaspora research. No national resistant-hypertension prevalence estimate should appear unless an appropriate representative source supports it.

## 8. Success criteria

In usability testing, clinicians should locate the confirmation checklist, PA pathway, CKD cautions, and a source in under one minute each. Patients should demonstrate the measurement sequence, identify an urgent symptom scenario, and explain why they should not change medicines based on a single reading. Include users of all four patient languages and older adults.

Measure navigation success, comprehension, print usability, missing-language coverage and editorial freshness. Do not present page engagement as proof of clinical benefit. Research evaluating real BP outcomes would need a separate study design and governance.


---

<!-- Source document: 02-CLINICAL-PATHWAYS.md -->

# Clinical pathways and printable artifacts

The following is the content and behavior specification for clinician review. Source IDs resolve to the evidence register. It defines what the application must represent; drug-dose tables and laboratory protocols require complete source extraction and named clinical review before production use.

## 1. Keep three different concepts separate

**Diagnostic threshold** establishes a hypertension category. **Treatment target** is the goal for an individual. **Resistant-hypertension definition** determines whether a particular framework's resistance criteria are met. Do not store these as one `bpThreshold` variable.

| Framework | Essential distinction to preserve |
|---|---|
| Philippine general CPG 2020 | Office diagnosis at ≥140/90 mmHg; its general target is <130/80, with population-specific recommendations. Confirm using repeated and out-of-office measurements. [G01] |
| AHA/ACC 2025 | Resistance is above-goal BP on three complementary agents including a diuretic at maximally tolerated doses, or controlled BP requiring at least four. Its MRA recommendation specifies eGFR ≥45. [G03] |
| ESC 2024 | Resistant definition uses office ≥140/90 despite optimized RAS blocker, CCB and diuretic, with out-of-office confirmation. Its spironolactone framework uses eGFR ≥30 and potassium ≤4.5 mmol/L. It does not use controlled resistant hypertension as a category. [G04] |
| KDIGO 2024 / BP 2021 | The suggested SBP <120 target, when tolerated, requires standardized office measurement in the applicable CKD population. Do not apply it directly to casual readings or dialysis. [G06] |
| ADA 2026 | Add the current diabetes-specific target and monitoring recommendations after extracting the full recommendation text and applicability criteria. Do not assume an older diabetes target covers every risk group. [G07] |

Default presentation: Philippine context first, with clearly labeled international comparison. Never silently blend the eGFR criteria into an invented consensus. A target reference may show multiple frameworks but a patient's displayed personal goal must identify the selected framework, measurement method and clinician-entered exceptions.

## 2. Consultation pathway

```text
Persistently high BP / difficulty reaching the chosen target
  → assess urgent symptoms and special-population exclusions
  → verify office measurement and out-of-office evidence
  → reconcile the actual regimen and practical medication access
  → review contributors, organ involvement and secondary causes
  → optimize an appropriate tolerated regimen
  → if resistance persists, apply source-specific add-on criteria
  → document monitoring, follow-up, referral and patient plan
```

These are overlapping clinical tasks, not a requirement to delay secondary-cause evaluation until every prior task is complete. Urgent findings interrupt the sequence at any point.

### A. Urgent assessment

Use an always-visible symptom-first exit. Clinician content must distinguish severe BP elevation from acute organ injury and provide links to local emergency pathways. Do not diagnose an emergency solely from a number, or rule one out because a number is below a threshold.

The Philippine acute severe BP guideline favors the term acute severe hypertension when acute organ injury is absent, gradual rather than immediate normalization, and close follow-up. Its executive summary has an internal **DBP 120 versus 110 mmHg discrepancy** between a formal statement and adjacent synthesis. Record this in the editorial conflict ledger; do not silently turn that discrepancy into calculator logic. [G02]

Patient urgent-help card: acute chest pain, severe breathlessness, new weakness or speech difficulty, confusion, or other concerning acute symptoms require emergency assessment; do not wait to complete a home log. For a very high reading without symptoms, show correct repeat measurement and immediate clinician contact if it remains very high. The final localized card must use reviewed wording and a verified local emergency contact, and must not teach rescue dosing. [P01]

Pregnancy/postpartum must have its own visible warning and care pathway; the general adult very-high-BP threshold must not be presented as its safe waiting threshold.

### B. Confirm measurement and phenotype

Document technique, device, cuff, measurement context, repeated office BP, home monitoring quality, and ABPM if available. Store “not done,” “unreliable,” and “unknown” separately from normal.

Output one or more descriptive findings: insufficient evidence; possible white-coat effect; possible masked uncontrolled BP; sustained uncontrolled BP; apparent resistance; or resistance criteria met under a named framework. A clinician confirms the diagnosis.

Do not label a patient resistant solely because a medication counter reaches three. Count active classes, inspect whether an appropriate diuretic is included, document dose/tolerability, and assess out-of-office confirmation and adherence. Combination pills contain multiple active ingredients but are one physical pill.

The historical AHA resistant-hypertension statement supplies the detailed confirmation and evaluation structure; use the newer guideline when recommendations have changed. [G05]

### C. Regimen and contributor review

Create fields for actual use, last dose, refill gaps, adverse effects, daily complexity, affordability and preferred routine. Use neutral language: “What made it hard to take this?” rather than “noncompliant.” Offer a printable generic-name list and question prompts.

The clinical chapter must evaluate medication-induced BP elevation and relevant substances, including NSAIDs, selected decongestants/stimulants, corticosteroids, hormones, calcineurin inhibitors, erythropoiesis-stimulating agents, alcohol, licorice-containing products and undisclosed supplements. The final per-agent explanations require citations and an interaction review; do not assume that all herbal products have the same effect. [G05]

### D. Secondary causes

| Clinical area | Required content | Tool behavior |
|---|---|---|
| Primary aldosteronism | Renin/aldosterone and potassium, assay type, medication interference, specialist confirmation and subtyping | Reuse and update existing ARR tool; no universal unit-free cutoff |
| Kidney parenchymal disease | eGFR/creatinine trend, urine findings and albuminuria, targeted imaging | Link existing kidney calculators; do not infer chronicity from one result |
| Renovascular disease | Clinical clues and selective imaging/referral | No blanket CT angiography order or automatic revascularization recommendation |
| OSA | Symptoms, screening and diagnostic testing | Reuse STOP-BANG; do not call a screening score a diagnosis |
| Other endocrine/uncommon causes | Pheochromocytoma/paraganglioma, thyroid disease, Cushing syndrome, coarctation and selected genetic causes | Clue-driven referral, no unvalidated “secondary hypertension probability” score |

The 2025 Endocrine Society guideline conditionally suggests PA screening in all people with hypertension, depending on feasibility. The guide should emphasize resistant cases without incorrectly describing screening as limited to hypokalemia. Medication withdrawal is an individualized supervised strategy; an application must never tell patients to stop antihypertensives for testing. Confirmation and subtyping are conditional clinical decisions, not a universal mandatory sequence. [G08]

### E. Treatment and CKD overlay

Show a medication-optimization checklist before an add-on card. For general adult resistant hypertension, the core framework is a RAS blocker, long-acting dihydropyridine CCB, and appropriate diuretic; assess dose, tolerance, volume and adherence. Separate contraindications and compelling indications from the generic sequence. [G03, G04]

Do not allow ACE inhibitor plus ARB to appear as an acceptable complementary combination. [G04, G07]

When the user opens an MRA card, require kidney function, potassium, pregnancy status, interacting medicines, and a monitoring plan. Unknown or stale safety information must produce “information needed,” not “eligible.” eGFR 30–44 is an explicit guideline-difference/specialist-review branch, not a rounding error between the AHA/ACC and ESC criteria.

Advanced CKD content must explain the distinction between a loop-diuretic strategy and the CLICK evidence for chlorthalidone. CLICK supports BP lowering in advanced CKD, but does not justify indiscriminate dose escalation without adverse-event monitoring. AMBER addresses persistence with spironolactone using patiromer; do not recast its endpoint as proof of cardiovascular benefit. [T02, T03]

Medication table required columns:

`generic | class | place in pathway | formulation | starting dose | titration | maximum relevant dose | kidney/potassium constraints | pregnancy constraints | interactions | adverse effects | monitoring | source section | Philippine status | last verification`

Populate with source-verified entries for the core agents, spironolactone, relevant alternatives, and specialist drugs. Do not extrapolate a drug's HF dosing or CKD indication into resistant-hypertension dosing. Finerenone, SGLT2 inhibitors and GLP-1 therapies belong in indicated cardiorenal care; do not present them as interchangeable with the resistant-hypertension fourth-line evidence.

Monitoring records must identify who orders tests, when results are reviewed, which symptoms change timing, and what happens if the patient cannot obtain testing. Exact intervals and action thresholds are drug- and patient-specific source records, not one universal calendar.

### F. Referral and follow-up

Referral packet: chosen BP framework; device/technique; office and out-of-office data; medication classes/doses and barriers; recent electrolytes/kidney results with dates; albuminuria; relevant symptoms; secondary-cause workup; adverse effects; and the specific clinical question.

The follow-up plan must have an owner, a date/window, a BP measurement plan, required tests, contact instructions and explicit responsibility for reviewing results. Include routine reassessment, earlier symptom/lab-driven review, and referral if control or safety remains uncertain.

Renal denervation belongs in the specialist section with patient selection, center expertise, shared decision-making, and limits of outcome evidence. Do not display a “cure” promise or imply that medication can routinely stop afterward. [G03, T05]

## 3. Printable specifications

| ID | Audience/languages | Artifact | Required structure |
|---|---|---|---|
| A01 | Clinician EN | Difficult-to-control BP consultation algorithm | One-page sequence, urgent/special exits, confirmation requirements, referral and citations |
| A02 | Clinician EN | Apparent versus confirmed resistance checklist | One page; explicit unknowns and active-class reconciliation |
| A03 | Clinician EN | Secondary causes and PA preparation | Two pages if needed; assay fields and supervised-medication caveat |
| A04 | Clinician EN | CKD/add-on treatment safety map | Source-specific kidney/potassium branches, testing and follow-up fields |
| A05 | Clinician EN | Specialist referral sheet | One page with blank fields; no patient identifiers required by the website |
| A06 | Patient all four | How to measure BP | One page, illustrated positioning and readable step sequence |
| A07 | Patient all four | BP log and visit summary | Reuse existing log; clear calculation window and space for questions |
| A08 | Patient all four | Medicines and refill plan | Generic name, purpose, prescribed schedule, refill date, contact person |
| A09 | Patient all four | Urgent-help action card | Symptom-first, large text, no reliance on red/green alone |
| A10 | Patient all four | Food and sodium worksheet | Label/portion exercise, practical swaps, kidney/potassium caveat |
| A11 | Clinician EN | Philippine medication hierarchy | Core regimen, appropriate diuretic, preferred add-on, conditional later options, local verification date and source-specific constraints; draw from file 07 |

Support A4 and US Letter, monochrome printing, and actual browser print-to-PDF. Print only the selected language. Every artifact has title, intended audience, version, review status/date, short source references and canonical link. QR codes are optional, never the only way to access instructions. If content cannot fit legibly, use another page rather than shrink essential text. Shared source records must drive both web and print.


---

<!-- Source document: 03-EVIDENCE-REGISTER.md -->

# Evidence register and update plan

Checked 27 September 2026, Asia/Manila. Targeted searches covered Philippine hypertension guidelines and studies, resistant hypertension, secondary causes, major add-on trials, CKD, diabetes, patient monitoring, local access and recent 2025–2026 publications. This is a curated research foundation, not a systematic review or an assurance that every publication has been retrieved.

**Verification depth:** guideline recommendations and trial findings below were checked against publisher, society, PubMed, institutional manuscript or official government material. Some full pages were intermittently blocked; accessible indexed primary-source text or abstracts were used. Full recommendation tables, supplementary protocols, corrections and drug labels still need extraction for production decision rules. Numbers are deliberately limited to findings checked here.

## Guidelines and statements

| ID | Source and date | Architectural use |
|---|---|---|
| G01 | Ona et al. **2020 Philippine hypertension CPG executive summary**, published 2021. [Full article](https://pmc.ncbi.nlm.nih.gov/articles/PMC8678709/), DOI 10.1111/jch.14335 | National general-management anchor found in this search. Confirm current status with PSH/PHA before release. |
| G02 | **2024 Philippine CPG on acute severe BP elevation**, executive summary published 30 January 2026. [Publisher](https://doi.org/10.1111/jch.70199), [article](https://pmc.ncbi.nlm.nih.gov/articles/PMC12856959/) | Acute assessment and follow-up. Keep guideline year distinct from publication date. Flag the 110/120 DBP inconsistency for editorial resolution. |
| G03 | **2025 AHA/ACC multisociety high BP guideline**. [Guideline](https://www.jacc.org/doi/10.1016/j.jacc.2025.05.007) | Updated resistance definition, MRA and RDN recommendations. Record Section 5.6 and relevant tables in individual claim records. |
| G04 | **2024 ESC elevated BP and hypertension guideline**. [Guideline](https://academic.oup.com/eurheartj/article/45/38/3912/7741010), DOI 10.1093/eurheartj/ehae178 | Framework comparison, measurement and resistant-hypertension pathway. The treated SBP target of 120–129 when tolerated must remain distinct from its resistance definition. |
| G05 | Carey et al. **AHA resistant hypertension scientific statement**, 2018. [Statement](https://www.ahajournals.org/doi/10.1161/HYP.0000000000000084) | Detailed pseudoresistance, adherence, contributors and secondary-cause workup. Reconcile with 2025 guidance. |
| G06 | **KDIGO CKD 2024**, with **BP in CKD 2021**. [CKD PDF](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf), [BP guideline hub](https://kdigo.org/guidelines/blood-pressure-in-ckd/) | Measurement-dependent targets, CKD and monitoring overlays. Extract the applicable population and exceptions, not only the target number. |
| G07 | **ADA Standards of Care 2026**, cardiovascular risk management. [Chapter](https://doi.org/10.2337/dc26-s010) | Diabetes-specific BP decisions, albuminuria, drug combinations and monitoring. Capture recommendations 10.3 onward directly. |
| G08 | **Endocrine Society primary aldosteronism guideline 2025**. [Official recommendations](https://www.endocrine.org/clinical-practice-guidelines/primary-aldosteronism-2) | Updated screening, assay-dependent interpretation and conditional follow-on pathways; replaces relying solely on 2016. |
| G09 | **ISH Global Hypertension Practice Guidelines 2020**. [Official hub](https://ish-world.com/global-hypertension-practice-guidelines) | Essential versus optimal resource model. Useful implementation context for uneven diagnostic access. |
| G10 | Liu et al. **Asian expert consensus on high-quality hypertension management**, online May 2026, July issue. [Article](https://doi.org/10.1038/s41440-026-02644-2) | Regional context for out-of-office measurement, long-acting combinations and collaborative care. Consensus is not a Filipino outcome trial. |
| G11 | **ISH 2026 guideline announcement**, 7 September 2026. [Official news](https://ish-world.com/publications-and-press-releases) | Publication announced for October, presentation 24 October 2026. Forthcoming at this cutoff; add a manual update task, not fabricated recommendations. |

## Landmark and recent trials

For every final study card extract PICO, geography, randomized/analyzed sample, background therapy, endpoint measurement, time horizon, between-group effect with CI, harms, exclusions, funding and applicability. Never compare effect sizes across trials as if they came from a head-to-head experiment.

| ID | Study/source | Finding and appropriate interpretation |
|---|---|---|
| T01 | **PATHWAY-2**, 2015. [Author manuscript and abstract](https://discovery.ucl.ac.uk/id/eprint/1478906/), DOI 10.1016/S0140-6736(15)00257-3 | 335 randomized in a crossover trial. Spironolactone lowered home SBP more than placebo by 8.70 mmHg (95% CI 7.69–9.72 in magnitude). Supports add-on choice, not extrapolation to all advanced CKD or proof of CV outcome benefit. |
| T02 | **CLICK**, 2021. [Primary publication](https://www.nejm.org/doi/full/10.1056/NEJMoa2110730) | In advanced CKD, chlorthalidone improved 24-hour SBP versus placebo by 10.5 mmHg at 12 weeks (95% CI 6.4–14.6 in magnitude). Hypokalemia, reversible creatinine increases and other adverse events matter. Use for the CKD evidence discussion; Philippine product access needs independent verification. |
| T03 | **AMBER**, 2019. [Abstract](https://pubmed.ncbi.nlm.nih.gov/31533906/), DOI 10.1016/S0140-6736(19)32135-X | 295 randomized, eGFR 25–45. At 12 weeks, 86% on patiromer versus 66% on placebo remained on spironolactone. This is treatment enablement, not a hard-outcome trial. Local binder access cannot be assumed. |
| T04 | **TRIUMPH**, 2021. [Primary manuscript](https://pmc.ncbi.nlm.nih.gov/articles/PMC8511053/), DOI 10.1161/CIRCULATIONAHA.121.055329 | Structured diet/exercise/weight intervention in resistant hypertension. Supports a practical lifestyle module while acknowledging that a supervised program is more intensive than simply giving advice. |
| T05 | **RADIANCE-HTN TRIO**, 2021. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/34010611/), DOI 10.1016/S0140-6736(21)00788-1 | Sham-controlled trial, 136 randomized. Median between-group daytime ambulatory SBP difference was −4.5 mmHg at two months. BP efficacy does not establish cure or a CV outcome benefit. |
| T06 | **PRECISION**, 2022. [Primary publication](https://www.sciencedirect.com/science/article/pii/S0140673622020347), DOI 10.1016/S0140-6736(22)02034-7 | Phase 3 aprocitentan study in resistant hypertension, 730 randomized. Extract magnitude, fluid-retention harms and withdrawal phase before building a full card. No direct comparison with spironolactone. |
| T07 | **Spironolactone versus amiloride**, 2025. [JAMA](https://jamanetwork.com/journals/jama/fullarticle/2834040), DOI 10.1001/jama.2025.5129 | Korean randomized open-label, blinded-endpoint study, 118 randomized; amiloride met noninferiority for home SBP reduction. Regional evidence is relevant but not Filipino validation; verify local amiloride supply before putting it in the routine ladder. |
| T08 | **BaxHTN**, 2025. [NEJM](https://www.nejm.org/doi/full/10.1056/NEJMoa2507109) | Phase 3 mixed uncontrolled/resistant population. Twelve-week seated SBP changes: −14.5 and −15.7 mmHg with 1 and 2 mg versus −5.8 placebo. These are within-arm changes; do not label them placebo-adjusted. |
| T09 | **Bax24**, 2026. [Primary abstract](https://pubmed.ncbi.nlm.nih.gov/41794437/), DOI 10.1016/S0140-6736(25)02549-8 | Resistant population; 12-week placebo-corrected 24-hour ambulatory SBP difference −14.0 mmHg (95% CI −17.2 to −10.8). Current evidence section; separately extract potassium/adverse events and verify regulatory status. |
| T10 | **Advance-HTN**, 2025. [NEJM](https://www.nejm.org/doi/10.1056/NEJMoa2501440) | Lorundrostat trial with standardized background therapy and ambulatory confirmation; 285 randomized. Include ambulatory BP endpoint and safety rather than sponsor headlines. |
| T11 | **Launch-HTN**, 2025. [JAMA primary article](https://jamanetwork.com/journals/jama/fullarticle/2835763), [PubMed record](https://pubmed.ncbi.nlm.nih.gov/40587141/) | Phase 3 lorundrostat, 1,083 randomized, uncontrolled/apparent-resistant population. PubMed links a 2026 correction: check it before extracting exact estimates. |
| T12 | **BPROAD**, online 2024, NEJM 2025. [Primary article](https://www.nejm.org/doi/full/10.1056/NEJMoa2412006) | Chinese type 2 diabetes population, 12,821 participants. Intensive versus standard targets reduced the primary CV outcome, HR 0.79 (95% CI 0.69–0.90), with more symptomatic hypotension/hyperkalemia. Important for target discussions; not a resistant-hypertension or Filipino-specific trial. |

Additional full-guide context to retrieve during implementation: SPRINT final report, STEP, ESPRIT, salt-substitution outcome evidence and relevant CPAP trials. They are not substitute evidence for the resistant-hypertension drug hierarchy. Do not insert unsourced numerical summaries for these until primary articles are checked.

## Philippine evidence and access

| ID | Source | Use and limitation |
|---|---|---|
| L01 | **PRESYON-4**, nationwide survey conducted Jan–Apr 2021. [Philippine Journal of Cardiology primary report](https://pjc.philheart.org/elib/journal/identifier/pjc.2021.0712.053068/pdf) | Local hypertension, awareness and treatment context. Verify each denominator and BP definition before quoting control percentages. Do not equate survey hypertension prevalence with resistant hypertension prevalence. |
| L02 | **DOST-FNRI 2023 National Nutrition Survey**, adult results. [Official presentation](https://enutrition.fnri.dost.gov.ph/uploads/7_2023_NNS_ADULTS.pdf) | Adults 20–59 in this document. Extract older-adult data separately. Measured elevated BP, treated hypertension and total prevalence are not interchangeable. |
| L03 | **Prevalence and Factors Associated with Hypertension among Filipino Adults in Different Survey Periods**, 2023. [Philippine Journal of Science](https://philjournalsci.dost.gov.ph/prevalence-and-factors-associated-with-hypertension-among-filipino-adults-in-different-survey-periods/) | National survey trend context; do not merge with PRESYON without reconciling sampling and definitions. |
| L04 | Luardo-Taruc et al. **Primary Aldosteronism among Adult Filipinos with Resistant Hypertension: A Pilot Study**, 2021. [Primary report](https://pjim.pcp.org.ph/elib/journal/identifier/2021-59.3-4/pdf) | Single center, Cagayan de Oro; 14 participants, 3 confirmed cases under its protocol (21.43%). Small selected sample, substantial exclusions and incomplete follow-on testing. Illustrates local relevance; not a national estimate or current diagnostic protocol. |
| L05 | **Philippine FDA verification portal**. [Official advisory](https://www.fda.gov.ph/fda-advisory-no-2023-2238-utilization-of-the-food-and-drug-administration-fda-verification-portal/), [portal](https://verification.fda.gov.ph/) | Verify exact product, strength, registration dates, manufacturer and label. Ingredient classifications alone do not prove an active marketed product. |
| L06 | **PhilHealth YAKAP/GAMOT 2026 issuances**. [Official issuances](https://www.philhealth.gov.ph/yakap/issuances/), [January advisory](https://www.philhealth.gov.ph/advisories/2026/PA2026-0007.pdf) | Dated access module. Verify current eligibility, medicine list, participating provider and supply before promising coverage. |
| L07 | **PHA Formulary, first edition 2023**. [Official PDF](https://www.philheart.org/images/00_PHA_Formulary_First_Edition_2023_01122024.pdf) | Supporting local drug reference. Reconcile with current product labels and later recommendations; not real-time inventory. |

## Patient and tool sources

| ID | Source | Use |
|---|---|---|
| P01 | [AHA home BP monitoring](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings/monitoring-your-blood-pressure-at-home), reviewed Aug 2025 | Technique and patient action wording. Localize emergency contact; do not import US phone assumptions. |
| P02 | [WHO sodium reduction](https://www.who.int/news-room/fact-sheets/detail/sodium-reduction) | General adult sodium guidance; sodium/salt conversion; portion literacy. |
| P03 | [WHO lower-sodium salt substitutes guideline 2025](https://www.who.int/publications/i/item/9789240105591), [recommendation/exclusions](https://www.ncbi.nlm.nih.gov/books/NBK612035/) | Avoid universal potassium-salt advice in kidney impairment or impaired potassium excretion. |
| P04 | [Target:BP home measurement workflow](https://targetbp.org/patient-measured-bp/how-it-works/) | Home measurement education and averaging workflow; select and document a single protocol. |

## Editorial rules for updating the research

1. Preserve source IDs across updates; store publication, online publication, guideline year, access date and review date separately.
2. Separate evidence extraction from recommendation adoption. A new trial does not automatically replace a guideline.
3. Store exact source section/page/table for every threshold, dose, exception and contraindication.
4. Check corrections/retractions and trial supplements; do not cite an obsolete abstract when a correction changes results.
5. Mark the scope of inference: direct Filipino evidence, other Asian population, or international extrapolation.
6. Keep a conflict ledger: competing recommendation, applicable population, measurement method, chosen presentation, reviewer and date.
7. Suggested maintenance: quarterly literature review; drug/access evidence every 90 days; immediate review for major guidelines, safety alerts or substantive corrections. These are proposed editorial intervals, not an automation created by this handoff.
8. Specifically check the forthcoming ISH guideline after October 2026 and recheck PSH/PHA for a superseding general CPG before launch.

## Open evidence items before clinical release

- Full source extraction and approval of dose, titration, monitoring and abnormal-result action tables.
- Exact assay/unit-specific ARR rules and pathways reconciled with 2025 guidance.
- Approved home/ambulatory averaging and classification protocol, including missing-data criteria.
- Current Philippine product registrations, indications and geographic supply for every selectable routine drug.
- Native-language clinical review of all patient action statements.
- No unsupported national prevalence, ethnicity-specific efficacy or price/coverage claims.


---

<!-- Source document: 04-TECHNICAL-ARCHITECTURE.md -->

# Technical architecture and acceptance tests

## 1. Integration strategy

Inspect the Renal Care Matters repository first: AGENTS instructions, route conventions, build commands, language attributes, shared CSS/JS, calculator registration, guide metadata, print utilities and tests. The public pages inspected expose static HTML, shared assets, embedded widgets and legacy `data-lang="kap"` values. This does not establish the private repository's build system.

**Preferred implementation:** retain the site's stack and deploy model. Extract shared data/functions where practical; avoid a new framework solely for this guide. If no repository is supplied, create an isolated static prototype with HTML/CSS and typed TypeScript modules compiled to browser JavaScript. No server or database is required for the core guide.

Architecture:

```text
Reviewed sources → claim and protocol records → clinical/patient content
                                          ↘ deterministic tool functions
Content + locale + audience → web pages / search / print views
All records → validation → preview → clinical/language review → release
```

A component name or filename is a proposed contract, not a demand to restructure the existing site.

## 2. Suggested repository organization

```text
content/hypertension/
  guide.json
  sources.json
  claims.json
  protocols.json
  medication-hierarchy.json
  local-formulary.json
  studies.json
  clinician/*.md
  patient/en/*.md
  patient/tl/*.md
  patient/ceb/*.md
  patient/pam/*.md
  translations/review-manifest.json
  editorial/conflicts.json
  editorial/changelog.json
src/hypertension/
  domain/validation.ts
  domain/bp-summary.ts
  domain/phenotype.ts
  domain/orthostatic.ts
  domain/abpm-summary.ts
  domain/local-formulary.ts
  components/*
  adapters/existing-tools.ts
  print/*
tests/hypertension/
  fixtures/*
  calculations.test.*
  pathways.test.*
  content-validation.test.*
  accessibility-and-print.spec.*
```

Maintain one source of truth for numeric thresholds, safety language, formulas, medication role and evidence. Do not scatter literal clinical thresholds across translations and DOM event handlers.

## 3. Core data contracts

```ts
type Audience = 'clinician' | 'patient';
type Locale = 'en' | 'tl' | 'ceb' | 'pam';
type ReviewStatus = 'draft' | 'needs-review' | 'approved' | 'superseded';
type Known<T> = { state: 'known'; value: T } | { state: 'unknown' };
type Measurement = 'standardized-office' | 'routine-office' | 'home'
  | 'abpm-awake' | 'abpm-asleep' | 'abpm-24h';

interface Source {
  id: string; title: string; url: string;
  doi?: string; guidelineYear?: number; publishedAt?: string;
  accessedAt: string; verificationDepth: 'full-text' | 'abstract' | 'metadata';
  jurisdiction: string; kind: string; correctionUrl?: string;
}
interface Claim {
  id: string; text: string;
  sourceRefs: { sourceId: string; sectionOrPage: string }[];
  population: string; exclusions: string[];
  measurement?: Measurement; originalEvidenceGrade?: string;
  filipinoApplicability: 'direct' | 'regional-extrapolation' | 'international-extrapolation';
  reviewStatus: ReviewStatus; reviewer?: string; reviewedAt?: string;
  version: string;
}
interface BPThresholdRule {
  id: string; purpose: 'diagnosis' | 'target' | 'resistance' | 'urgent-assessment';
  framework: string; measurement: Measurement;
  systolic: number; diastolic?: number;
  comparator: '>=' | '>' | '<' | '<=';
  join: 'or' | 'and' | 'systolic-only';
  population: string; exclusions: string[]; claimId: string;
}
interface TranslationReview {
  contentId: string; locale: Locale; sourceVersion: string;
  translatedVersion: string; status: ReviewStatus;
  linguisticReviewer?: string; clinicalReviewer?: string;
  reviewedAt?: string;
}
interface ToolResult {
  status: 'ready' | 'incomplete' | 'invalid' | 'review-required' | 'urgent';
  values: Record<string, number | string>;
  messages: { contentKey: string; parameters?: Record<string, string | number> }[];
  sourceIds: string[]; protocolId?: string; protocolVersion?: string;
  excludedInputs: { id: string; reason: string }[];
}
```

Map legacy site language code `kap` to canonical `pam` at the integration boundary. Keep visible language names familiar. Do not globally rename existing attributes without a compatibility adapter.

`MedicationHierarchy` needs tier, clinical purpose, eligibility/contraindication references, alternatives, source IDs and local formulary IDs. An unavailable or expired local product must not become the default next-drug suggestion. Clinician confirmation remains necessary even if rules match.

## 4. Calculation and decision boundaries

Pure domain functions accept typed inputs and return structured results. They must not read the DOM, call a network service, render HTML, or translate text. Units are explicit. Rounding is for display only; compare using unrounded values.

An educational checklist is not a validated risk score. A hypertension phenotype helper describes which criteria are documented and which are missing; it does not estimate a probability or independently diagnose resistant hypertension.

Dangerous-looking but valid readings must remain visible and trigger the reviewed action message. Impossible entries should be rejected with a clear correction request. Never silently discard high readings as “outliers.” Missing values are not zero and an unchecked item is not automatically “no.”

Input precedence: urgent symptoms → pregnancy/postpartum or out-of-scope population → data validity → data sufficiency → framework-specific interpretation → informational next steps. A reassuring average must never suppress an urgent symptomatic reading.

## 5. Search and navigation

Use the existing search/index infrastructure. Index reviewed headings, synonyms, drug generic names, local brand aliases, acronyms and patient phrases separately by audience/locale. Examples: resistant hypertension, uncontrolled BP, high blood, presyon, ARR, spironolactone, PA, sleep apnea, and refill difficulty. Search should expose clinician results as clinician results, not mix them into a patient action card.

For a no-result query, offer relevant topics and alternate terms. Do not send a clinical search to an LLM for invented answers. Deep links preserve the topic and locale; back navigation restores the previous view.

## 6. Privacy and offline behavior

Calculations run in memory by default. No names, birthdays, diagnoses or medication lists are required to read the guide. Explicit local save may be offered only if it clearly states that data remains on that device and is unsuitable for a shared computer; provide delete/export controls. Do not place health inputs in URLs, analytics, error logs or third-party session replay.

Printable reports include health values only after deliberate print/export. QR codes encode the public guide URL, never readings or medication data. Prefer self-hosted assets. Offline support may cache approved guide content, but must display the cached version and last-review date. Service-worker updates must not mix old thresholds with new text.

The role toggle is a navigation aid, not authentication or a claim that viewers are licensed clinicians.

## 7. Review and release model

Build a complete private preview with conspicuous draft labels where appropriate. Production build validation fails for missing clinical citations, unsigned critical thresholds, incomplete mandatory patient translations, or routine medications lacking required local verification.

Translations become stale when the source content version changes. Safety-critical stale content cannot silently remain served as reviewed. Permit a clearly labeled English fallback only for a reviewer-approved noncritical section; do not show mixed-language emergency instructions.

Editorial roles may be held by the same owner, but record actual decisions: medical editor; medication/local-access reviewer; and native-language reviewer. Do not fabricate names, professional endorsements, society logos or approval dates.

## 8. Acceptance tests

| Test | Expected result |
|---|---|
| Three drugs but no appropriate diuretic | No confirmed resistance label; explains missing regimen requirement |
| Three classes, unknown adherence or no reliable out-of-office BP | Apparent/insufficiently confirmed status |
| Above-goal office BP, normal reliable home data | Possible white-coat effect; no automatic escalation |
| Normal office BP, elevated reliable home data | Possible masked uncontrolled BP, clinician review |
| Controlled on four agents | Framework-specific output; do not force the ESC and AHA categories to match |
| MRA assessment, potassium missing | Incomplete, not eligible |
| eGFR 29.9 / 30 / 44.9 / 45 | Correct unrounded boundaries and visible framework difference |
| Potassium 4.5 / 4.6 under ESC rule | Boundary handled as specified, without rounding 4.6 down |
| Pregnancy/postpartum selected | Exits generic adult medication flow |
| Dialysis selected | Does not inherit nondialysis CKD targets or MRA eligibility |
| Fixed-dose ARB/CCB plus extra ARB | Duplicate class/ingredient review flagged |
| Drug local registration expired/unverified | Cannot be the default local next-drug choice |
| Clonidine 75 micrograms | Does not become 75 mg during formatting or translation |
| High symptomatic reading with lower weekly average | Urgent advice has priority |
| Home log missing days/unequal sessions | Transparent denominators and protocol-quality flag |
| ARR renin zero/below assay limit | No divide-by-zero or false precision; requests assay-aware interpretation |
| ARR PRA versus DRC | Different units/cutpoints remain separate; no generic conversion assumption |
| PREVENT linked | Does not claim Filipino calibration solely because it lacks a race input |
| Mode/language switch | Correct paired topic, no loss of preference, no hidden-language text read aloud |
| Source changes | Translation review status invalidated and affected print views updated |
| Print | One locale, legible A4/Letter, references retained, no clipped decision branches |
| Network inspection while calculating | No health inputs transmitted |

Add independent arithmetic fixtures, boundary tests and pathway tests. Use browser checks at 360 px and desktop width, keyboard-only navigation, screen-reader labels, 200% zoom and automated accessibility checks. Target WCAG 2.2 AA as a design/testing objective. Verify actual print output, not only CSS declarations.

## 9. Implementation order

1. Inventory repository and existing tools; create a compatibility map.
2. Build content schemas, source register, locale mapping and review validators.
3. Implement guide shell, all page routes and search.
4. Add reviewed clinical content and the locally grounded medication hierarchy.
5. Adapt patient content and all four languages with review tracking.
6. Reuse/update existing calculators; build prioritized gaps from file 06.
7. Generate print artifacts and accessible reports.
8. Run clinical logic, unit, locale, privacy, navigation and print checks.
9. Deliver a preview, change summary, evidence gaps and review checklist. Deployment is a separate action; do not publish unsigned medical content.


---

<!-- Source document: 05-PATIENT-LANGUAGES.md -->

# Patient language and editorial specification

## Required language coverage

Clinician mode: English. Patient mode: **English, Tagalog, Cebuano, Kapampangan**. This matches the owner's instruction and the visible language choices on [Renal Care Matters](https://renalcarematters.com/).

Use canonical locale identifiers `en`, `tl`, `ceb`, `pam`, with a compatibility mapping to existing `kap` attributes where needed. Do not assume that inserting Tagalog vocabulary into another language produces a valid translation.

## Patient content is an adaptation

Create the English patient source first, then translate that source. Shorten concepts without changing their meaning. Avoid clinical staging jargon unless necessary, define BP and generic medicine names, and explain “resistant” as a technical description that does not mean a person is hopeless or at fault.

Use short sentences, familiar verbs, concrete steps, local food examples and one action per card. Aim for broadly accessible reading complexity, but assess comprehension with speakers rather than applying an English readability formula to Philippine languages.

Each topic should include: the patient's question; a plain explanation; what they can do; what to discuss with the care team; and warning signs if relevant. Keep technical evidence available behind a sources link without interrupting the instructions.

## Translation workflow

1. Medical editor approves source patient content and numeric/action tokens.
2. Translate by content ID, preserving all units, conditions, negations and timing.
3. Native-language reviewer checks naturalness, dialect/register, ambiguous terms and mixed-language errors.
4. Clinical reviewer checks equivalence, especially urgent actions, medication instructions, lab preparation and kidney-diet caveats.
5. Test with patients/caregivers using teach-back; document misunderstandings and revise.
6. Approve each locale/version explicitly. Any changed source instruction reopens its translations.

Do not present AI-generated translations as native-reviewed. A complete implementation preview may contain clearly marked translation drafts. The public release requires reviewed versions for all four requested languages.

## Protected meaning and formatting

Keep drug generic names, numbers and units controlled by shared tokens. Translate surrounding prose. Preserve distinctions such as “and” versus “or,” “at least” versus “more than,” “call now” versus “bring to the next visit,” and “do not change” versus “stop.” Translate accessible names, validation errors, result messages, chart labels, empty states, print headings, help text and captions—not only article paragraphs.

The two mode controls must not interfere. A patient selecting Kapampangan should receive Kapampangan patient text and printouts; visiting a clinician page should show English with a clear mode label and restore Kapampangan on return.

## Source English copy examples for adaptation

These are editorial drafts, not final translated clinical instructions.

**Why BP may remain high:** “There may be more than one reason your blood pressure is still high. Your care team may check how it is measured, which medicines you take, whether refills are difficult to get, and whether another condition is affecting it.”

**Several medicines:** “Different medicines lower blood pressure in different ways. Bring all your medicine names, doses and supplements to your next visit. If side effects or cost make treatment difficult, tell your care team so you can make a plan together.”

**Personal target:** “Your BP goal depends on your health and how the reading was taken. Write down the goal your clinician gives you. A single reading does not tell the whole story.”

**Before hormone testing:** “Some medicines can affect the test. Ask the clinic how to prepare. Do not stop or change your medicines on your own.”

The reviewed home-measurement sequence should cover an appropriate upper-arm device and cuff, resting and positioning, repeated readings and recording. Patient monitoring must not replace follow-up or become an instruction to change treatment from one result. [AHA home monitoring](https://www.heart.org/en/health-topics/high-blood-pressure/understanding-blood-pressure-readings/monitoring-your-blood-pressure-at-home)

Food advice should explain sodium across an entire day rather than blaming one meal. The general adult WHO goal is less than 2,000 mg sodium/day, approximately 5 g salt from all sources. Potassium-containing salt substitutes are not a universal recommendation for people with impaired potassium excretion. [WHO sodium](https://www.who.int/news-room/fact-sheets/detail/sodium-reduction), [WHO salt-substitute exclusions](https://www.ncbi.nlm.nih.gov/books/NBK612035/)

## Patient-mode exclusions

- No drug selection, dose escalation, medication withdrawal or “take an extra tablet now” outputs.
- No ARR interpretation or MRA eligibility controls.
- No automatic diagnosis based on a log.
- No suggestion that absence of symptoms means BP is controlled.
- No generic instruction to increase water, potassium or salt substitutes for everyone with kidney disease.

Patient-accessible tools are measurement/log summaries, food-label arithmetic, appointment preparation and a prescription-based cost/refill worksheet. Clinical interpretation remains in the clinician experience.


---

<!-- Source document: 06-CALCULATOR-AUDIT-AND-SPECIFICATIONS.md -->

# Calculator audit and gap specifications

## Audit method and limits

On 27 September 2026, inspected the public [calculator index](https://renalcarematters.com/guides/calculators), extracted **197 tool cards** from its public HTML, searched their titles/descriptions, inspected relevant individual pages, and inspected the existing hypertension guide and its embedded BP-log link. This was a public-content/source inspection, not a repository audit or runtime validation of every calculator.

“Not found” below means not identified in that index or the relevant pages inspected. Claude Code must search the actual repository for embedded or unindexed equivalents before building anything new. Search-engine silence is not proof that a tool does not exist.

## Reuse and update rather than duplicate

| Existing tool | Action for this guide |
|---|---|
| [BP log](https://renalcarematters.com/guides/bp-monitoring-log), embedded in [Managing Hypertension](https://renalcarematters.com/guides/managing-hypertension.html) | Reuse/extend. The parent calls it a 14-day log while the embedded title says 7-day: reconcile the protocol and labels. |
| [MAP, pulse pressure and BP target](https://renalcarematters.com/guides/calc-bp-map) | Reuse arithmetic; review target logic before integration. |
| [ARR](https://renalcarematters.com/guides/calc-aldosterone-renin-ratio) | Update to 2025 PA guidance and assay-aware interpretation; do not build a second ARR. |
| [Sodium intake](https://renalcarematters.com/guides/calc-sodium-intake) | Reuse with label/portion entry and uncertainty; avoid a parallel food database. |
| [Race-free eGFR](https://renalcarematters.com/guides/calc-egfr-ckd-epi.html) | Reuse for kidney context; retain units and population limits. |
| [Combined creatinine/cystatin C eGFR](https://renalcarematters.com/guides/calc-egfr-cystatin.html) | Link when clinically relevant. |
| [KFRE](https://renalcarematters.com/guides/calc-kfre.html) | Link for appropriate CKD risk context; not a BP target or resistant-HTN probability. |
| [PREVENT](https://renalcarematters.com/guides/calc-prevent-cvd.html) | Link; independently review implementation/population limits and do not imply Filipino calibration. |
| [STOP-BANG](https://renalcarematters.com/guides/calc-stop-bang.html) | Link for OSA screening; preserve screening-versus-diagnosis distinction. |
| [BMI/BSA/weight](https://renalcarematters.com/guides/calc-bmi-bsa-ibw.html) | Reuse for relevant anthropometry. |
| [Renal medication safety](https://renalcarematters.com/guides/calc-renal-med-safety) | Reuse checked drug data/functions where appropriate; not an unreviewed safety oracle. |

Two targeted updates are prerequisites:

1. The BP target page attributes a simplified proteinuria-stratified target table to KDIGO. Reconcile it with the actual measurement-dependent KDIGO recommendation and current guideline comparisons before embedding it. MAP remains an approximation and should not become the chronic-treatment target. [Existing page](https://renalcarematters.com/guides/calc-bp-map), [KDIGO source](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf)
2. The ARR page relies on 2016 guidance, a fixed aldosterone minimum and universal confirmation language. Update these to current assay/context-dependent pathways; do not copy its medication-withdrawal language into patient instructions. [Existing page](https://renalcarematters.com/guides/calc-aldosterone-renin-ratio), [2025 guideline](https://www.endocrine.org/clinical-practice-guidelines/primary-aldosteronism-2)

## K01 — Enhanced HBPM summary, existing tool extension, priority 0

**Audience:** patient in four languages; clinician summary in English.

Inputs: timestamp/date, wake/morning versus evening session, SBP, DBP, optional pulse/symptoms, repeat number, measurement quality, selected protocol and exclusion reasons. Preserve the existing log's useful behavior and add missing structure after code inspection.

Calculation: separate arithmetic means of included SBP and DBP readings. Also show morning/evening means, included counts, covered days and excluded entries. Never average a combined string such as “140/90.” Do not average rounded daily means unless the protocol intentionally gives days equal weight.

Protocol option: a source-labeled NICE diagnostic collection uses two readings at least one minute apart, morning/evening, at least four days and ideally seven, excluding day 1 from its diagnostic average. Do not silently use that exclusion for every longitudinal follow-up log. [NICE NG136](https://www.nice.org.uk/guidance/ng136/chapter/recommendations)

Missing sessions produce an explicit quality status. Ordinary HBPM cannot determine asleep BP or nocturnal dipping. Raw high/symptomatic readings remain visible even if excluded from a diagnostic average.

Test fixture: included pairs 140/90, 130/80, 120/70, 130/80 → **130/80**. Empty data → incomplete. A one-day log may show a descriptive mean but cannot claim protocol-complete confirmation.

Output: printable chart/table, method, dates, counts, missingness, clinician-entered target and visit questions. No dose advice.

## K02 — Office/out-of-office phenotype and resistance checklist, new candidate, priority 0

**Type:** deterministic clinical decision helper, not a calculator or validated score.

Inputs: named framework and goal, standardized/routine office context, reliable home/ABPM summary, drugs by active class, appropriate diuretic, dose optimization, adherence assessment, symptoms and scope exclusions. Every evidence field supports yes/no/unknown.

Output: criteria met, criteria missing, discordance requiring review, and possible phenotype. Do not output a numerical confidence percentage. Connect directly to the relevant clinical chapter and printable checklist.

Tests: high clinic/normal valid home values do not automatically trigger escalation; three drugs without a diuretic do not meet the optimized-three-class criterion; uncontrolled on three with unassessed adherence remains unconfirmed. Controlled four-agent categories must reflect the selected guideline.

## K03 — Orthostatic BP change, new candidate, priority 1

**Audience:** clinician. Inputs: baseline supine BP after appropriate rest; timed standing readings, ideally at one and three minutes; symptoms; measurement conditions.

Formula for each time point: `SBP drop = baseline SBP − standing SBP`; same for DBP. Also show absolute standing BP and change in pulse when entered. Flag a pattern meeting the conventional ≥20 mmHg systolic or ≥10 mmHg diastolic fall within three minutes, while explaining that sustained change, technique and symptoms need clinical interpretation. [AHA scientific statement 2024](https://www.ahajournals.org/doi/10.1161/HYP.0000000000000236)

Fixture: supine 150/85, standing 125/73 at three minutes → drops **25/12 mmHg**, criterion flag. No standing time or invalid baseline → incomplete. Symptomatic patients need review even below the numeric criterion. Do not automatically stop antihypertensives or infer neurogenic disease.

## K04 — ABPM report summary and asleep/awake fall, new candidate, priority 1

**Audience:** clinician. Initial scope: enter already validated awake, asleep and 24-hour means from a clinical ABPM report, recording valid-reading counts, device report quality and actual sleep periods. This avoids pretending that the website has validated proprietary raw device data.

Formula: `systolic asleep fall (%) = 100 × (awake mean SBP − asleep mean SBP) / awake mean SBP`. Compute diastolic percentage separately. Do not calculate 24-hour mean by simply averaging awake and asleep means; require the report's 24-hour mean.

Fixture: awake SBP 140, asleep 126 → **10%**; asleep 147 → **−5%**. Zero/missing awake mean → invalid/incomplete. Sleep periods must accommodate shift workers. Do not infer sleep from fixed clock hours.

Compare means with a named source's ABPM thresholds only after clinical approval; the BP measurement statement and ESC guidance provide the review sources. [AHA measurement statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC11409525/), [ESC 2024](https://academic.oup.com/eurheartj/article/45/38/3912/7741010)

Do not convert dipping patterns into automatic bedtime dosing. Raw CSV import, weighted means and full recording-quality validation are a later feature requiring a specific supported device format, published quality criteria and independent tests.

## K05 — MRA suitability and monitoring worksheet, new extension candidate, priority 0

**Type:** clinician checklist/rule reference, not a risk score. Integrate with the existing renal-medication tool if its architecture permits.

Inputs: drug considered, indication, eGFR and date, potassium and date, acute illness/AKI context, pregnancy, interacting drugs, adverse-effect history, local formulation status, named guideline and capacity for follow-up.

Output: missing information, source-specific constraints, conflicts requiring specialist review and a clinician-completed monitoring plan. Never label a patient universally “safe.” See the clinical-pathway file for the AHA/ACC-versus-ESC kidney-function distinction.

Fixtures must cover missing potassium, eGFR on both sides of 30 and 45, pregnancy, duplicate potassium-sparing therapy, unverified local supply and inability to obtain monitoring. Output no patient-directed start/stop prescription.

## K06 — 24-hour urinary sodium unit converter, new candidate, priority 2

**Audience:** clinician. Inputs: measured sodium excretion in mmol/24h, or concentration in mmol/L with a complete 24-hour volume in liters. Explicitly distinguish these input modes.

Arithmetic: `mmol/day = mmol/L × L/day`; `sodium mg/day = mmol/day × 22.99`; `salt-equivalent g/day ≈ sodium g/day × 2.54`. A practical WHO approximation is 1 g salt ≈400 mg sodium; label the convention used rather than mixing constants. [WHO sodium reference](https://www.who.int/news-room/fact-sheets/detail/sodium-reduction)

Fixture: 100 mmol/day → **2,299 mg sodium/day**, approximately **5.84 g salt-equivalent/day** with the chemical factor. Include collection completeness, diuretics, recent diet and day-to-day variability as interpretation notes. This measures/converts excretion; it is not an exact individualized dietary intake estimate. Do not use a spot-urine equation to promise an accurate daily intake for one patient.

## K07 — Prescribed-regimen cost and refill worksheet, new candidate, priority 1

**Audience:** patients in four languages and clinicians. This is financial arithmetic about an existing prescription, not treatment selection.

Inputs: exact product/formulation, prescribed tablets per day, current price per tablet/pack, pack size, existing tablet count and quote date. Support different schedules only with explicit prescription-derived quantities. No brand ranking or inferred equivalence.

Formula: `30-day tablet cost = unit price × prescribed units/day × 30`; `days remaining = usable units on hand / units/day` for a constant schedule. Separately display laboratory, transport and consultation costs if user-entered. Never represent their total as a verified market price.

Fixture: ₱10/tablet, one/day, 12 tablets remaining → **₱300/30 days and 12 days remaining**. Zero daily use or unspecified schedule → no depletion estimate. Stock from an incompatible strength must not be combined automatically.

## Shared tool requirements

- Formula, scope, inputs, units, limitations, sources, version, print action and reset action on every tool.
- Existing tools remain canonical; new guide embeds or links to them through a shared adapter.
- No health data in analytics or URLs; no automatic persistence.
- Test decimals, equality boundaries, missing values, incorrect units, extreme valid readings and translation parity.
- Separate educational tools from validated prediction models and clinical decision helpers in both labels and index metadata.
- Do not add a fabricated Filipino hypertension-risk score, antihypertensive-equivalence calculator, predicted BP-drop calculator, or “best drug for you” generator.


---

<!-- Source document: 07-PHILIPPINE-MEDICATION-HIERARCHY.md -->

# Clinician medication hierarchy for Philippine practice

Required by the owner: a visible hierarchy with drugs that can be obtained locally. Use generic names first. Brands below are examples of located products, not endorsements. The hierarchy is for nonpregnant adults after assessment, and must be modified for contraindications, volume status, comorbid indications and adverse effects.

**Verification boundary:** public Philippine pharmacy listings and several Philippine FDA-hosted labels were located on 27 September 2026. They support local marketing/formulation evidence. They do not guarantee inventory at a particular branch, nor establish an active registration for every retail SKU. The production formulary must pair a current exact-product FDA record with dated local supply evidence. Do not relabel this research as branch-stock confirmation.

## 1. Hierarchy shown on the clinical page

| Level | Clinical role | Philippine-facing choices | Display/decision requirements |
|---|---|---|---|
| 0 | Correct the reason treatment appears to fail | Measurement, actual use, access, secondary causes and regimen adequacy | This is not a drug step. Do not automatically escalate on an isolated reading. |
| 1 | Establish appropriate complementary therapy | **One ACE inhibitor or one ARB**, plus a long-acting dihydropyridine CCB when combination treatment is indicated | Local examples: losartan or telmisartan; perindopril as an ACE-inhibitor option; amlodipine as a CCB. Do not imply that these three RAS drugs are ranked against one another for all Filipinos. |
| 2 | Complete and optimize the three-class regimen | RAS blocker + amlodipine/appropriate CCB + **appropriate diuretic** | **Indapamide SR** is the locally evidenced thiazide-like option in this package. HCTZ is an access/formulation alternative, with optimization discussed. Chlorthalidone is a guideline-supported option only if the exact local product and supply are verified. |
| 2K | Change diuretic strategy when kidney function/volume requires | **Furosemide** is a locally listed loop option | This is an overlay, not “fourth-line for everyone.” Do not extrapolate indapamide efficacy/labeling into advanced CKD. Combination diuretic strategies require specialist supervision and monitoring. |
| 3 | Preferred add-on for confirmed resistance when suitable | **Spironolactone** | Apply the source-specific kidney/potassium constraints and monitoring requirements in the clinical-pathway document; assess contraindications and interactions. |
| 3A | Intolerance/contraindication to preferred add-on | Individualized alternative branch | Eplerenone or amiloride require exact local supply/label verification before becoming selectable local options. They must not be silently substituted or described as potassium-safe. |
| 4 | Further therapy or a compelling comorbid indication | **Bisoprolol or carvedilol**, when clinically appropriate | Clinical indications may place these earlier. Do not present “beta blocker always fifth” as a universal guideline mandate. Bradycardia, conduction disease, decompensation and other relevant contraindications need reviewed content. |
| 5 | Selected later-line therapy | **Clonidine**, only with a considered follow-up/adherence plan; other agents by specialist assessment | Explain sedation and withdrawal/rebound concerns in reviewed content. Never turn local availability into a recommendation for PRN home rescue dosing. |
| 6 | Specialist reserve/device or emerging options | Alpha blockers, hydralazine, oral minoxidil, aprocitentan, aldosterone synthase inhibitors, renal denervation as appropriate | Separate local-confirmed options from unverified-access therapies. Oral versus IV hydralazine and oral versus topical minoxidil are different products. |

Levels 1–3 follow the established resistant-hypertension treatment structure; later levels are an editorial presentation of conditional options, not a new evidence-graded ranking. Use the [2018 AHA statement](https://www.ahajournals.org/doi/10.1161/HYP.0000000000000084), [2025 AHA/ACC guideline](https://www.jacc.org/doi/10.1016/j.jacc.2025.05.007), [ESC 2024](https://academic.oup.com/eurheartj/article/45/38/3912/7741010), and [PHA formulary](https://www.philheart.org/images/00_PHA_Formulary_First_Edition_2023_01122024.pdf) for final clinical extraction and review.

## 2. Located local-market evidence

Listed strengths below are **product strengths**, not prescribed starting doses or a complete dosing range.

| Generic | Located Philippine evidence | Status for the blueprint |
|---|---|---|
| Losartan | [Watsons dispensary listing](https://www.watsons.com.ph/c/shop-watsons-dispensary) includes 100 mg; [FDA Lifezar 100 mg record](https://verification.fda.gov.ph/ALL_DrugProductslist.php/ALL_DrugProductsview.php?registration_number=DRP-16159&showdetail=) | Local retail and FDA product evidence located; exact chosen SKU/current registration to match before release |
| Telmisartan | [Watsons generic 40 mg](https://www.watsons.com.ph/watsons-generics-telmisartan-40mg-sold-per-piece-prescription-required/p/BP_50034362) | Local retail listing verified; current product registration to complete |
| Perindopril | [Coversyl 5 mg](https://www.watsons.com.ph/perindopril-arginine-5mg-tablet-1-tablet-%5Bprescription-required%5D/p/BP_10074832) | Local retail listing; distinguish arginine/erbumine salt and strengths before dose mapping |
| Amlodipine | [Watsons generic listing](https://www.watsons.com.ph/c/shop-watsons-dispensary) includes 10 mg | Local retail listing; verify exact SKU and other desired strengths |
| Indapamide SR | [Natrilix 1.5 mg retail listing](https://www.watsons.com.ph/natrilix-natrilix-indapamide-hemihydrate-1.5mg-1-tablet-prescription-required/p/BP_10001415); [Vazamide SR Philippine FDA label](https://verification.fda.gov.ph/files/DR-XY32026_PI_01.pdf) | Strong local-market evidence. FDA-hosted label is a different brand; match its own CPR if selected. SR formulation must remain distinct from immediate-release products. |
| HCTZ in an ARB combination | [Losartan/HCTZ 50/12.5 mg](https://www.watsons.com.ph/zarnat-zarnat-losartan-hctz-50-mg-12.5-mg-sold-per-piece-prescription-required/p/BP_10101686) | Local combination listing verified; do not infer that all standalone strengths are in stock |
| Furosemide | [Lasix 40 mg](https://www.watsons.com.ph/lasix-furosemide-40mg-1-tablet-prescription-required/p/BP_10003736) | Local retail listing; other brands can have different stock status |
| Spironolactone | [Aldactone 25, 50 and 100 mg listings](https://www.watsons.com.ph/all-brands/list/152070/aldactone); [FDA-hosted label](https://verification.fda.gov.ph/files/DRP-2013_PI_01.pdf) | Local retail and label evidence; use relevant low-dose resistant-HTN evidence rather than copying a retailer's multi-indication dosing text |
| Bisoprolol | [Bisosten 5 mg](https://www.watsons.com.ph/bisosten-bisosten-bisoprolol-fumarate-5mg-per-film-coated-tablet-sold-per-piece-prescription-required/p/BP_50044959) | Local retail listing; verify exact indication/formulation |
| Carvedilol | [Watsons dispensary listing](https://www.watsons.com.ph/c/shop-watsons-dispensary) includes 6.25 mg | Local retail listing; do not infer availability of every strength |
| Clonidine | [RiteMED 75 micrograms](https://www.watsons.com.ph/ritemed-ritemed-clonidine-75mcg-1-tablet-prescription-required/p/BP_10093544) and [150 micrograms](https://www.watsons.com.ph/ritemed-ritemed-clonidine-150mcg-1-tablet-prescription-required/p/BP_10093545) | Local listings; microgram/milligram validation mandatory |
| Amlodipine/losartan combination | [Watsons dispensary listing](https://www.watsons.com.ph/c/shop-watsons-dispensary) includes 5/50 mg | Local fixed-dose option; count both ingredients and prevent duplicate ARB/CCB use |

Retailer pages are used **only for product-market evidence**, not as the authoritative prescribing source. No prices are hardcoded because they vary by brand, outlet, promotion and date. A later cost worksheet should accept current patient/pharmacy quotations.

## 3. Options that must remain conditional

- **Standalone chlorthalidone:** no convincing current local retail supply was established in this search. An FDA hypertension ingredient/strength list includes azilsartan/chlorthalidone, but that is not proof of standalone availability or current stock. Do not force a combination product just to obtain chlorthalidone. [FDA list](https://verification.fda.gov.ph/med_hypertensionlist.php?export=pdf)
- **Eplerenone:** a Philippine FDA-hosted Epnone 25/50 label exists, but the located label lists HF indications. Verify present supply and explicitly identify off-label resistant-HTN use if applicable; never inherit a US hypertension indication. [Label](https://verification.fda.gov.ph/files/DRP-13441_PI_01.pdf)
- **Amiloride, doxazosin, oral hydralazine, oral minoxidil:** require exact product, oral formulation and supply confirmation before selection. A drug-information page or an injectable/topical product does not meet this requirement.
- **Aprocitentan, baxdrostat, lorundrostat and patiromer:** local access was not established here. Keep in specialist/evidence pages until verified. Do not label a medicine “not approved anywhere” merely because Philippine status is unknown.

## 4. Mandatory interaction design

Every hierarchy card has: role, why this level, when to choose, when to avoid, verified dose/formulation, monitoring, adverse effects, evidence, and local status. Users must be able to compare appropriate locally evidenced choices and see why a normally preferred option is unavailable or unsuitable.

An “unavailable locally” branch should offer clinician-reviewed choices within the same clinical purpose, plus reassessment/referral. It must not blindly advance the patient to a less appropriate later-line class. HCTZ access does not make it dose-equivalent to indapamide or chlorthalidone. No dose-equivalence calculator should be built for these drugs.

The treatment map must show why compelling indications change order: HF, CAD/arrhythmia, primary aldosteronism, volume overload and pregnancy need their own clinical reasoning. Patients see purposes and prescribed schedules, not the clinician titration ladder.

## 5. Local formulary data contract

Required per product:

`generic; brand; salt; releaseForm; route; strength; registrationNumber; registrationStatus; issuedAt; expiresAt; approvedIndications; labelUrl; labelRevision; supplierUrl; supplyEvidenceType; observedAt; locality; stockStatus; coverageSource; priceQuoteDate; reviewer; reviewStatus`

Use `unknown` for information not checked. A public listing gets `supplyEvidenceType=retailer_listing`, not `branch_stock_confirmed`. Use the label's renal measure—CrCl or indexed eGFR—as specified; do not treat these as numerically interchangeable.

Release acceptance: every routine selectable drug has a clinical citation, exact local formulation, current registration check, and dated supply evidence. Locally uncertain options remain visible in a separate evidence panel but cannot appear as the default practical next drug.


---

<!-- Source document: CLAUDE-CODE-HANDOFF.md -->

# Claude Code execution brief

Copy the prompt below into Claude Code with this entire blueprint folder and the Renal Care Matters repository. If the repository is unavailable, the same prompt specifies an isolated prototype. This brief requests implementation, not another planning-only response.

---

## Your assignment

Build **Difficult-to-Control Hypertension in Filipinos**, a searchable, mobile-friendly Renal Care Matters web guide with clinician and patient modes, integrated educational tools, and printable algorithms. Use this blueprint as the product specification. Read all eight accompanying Markdown documents before implementation. The research cutoff is **27 September 2026**; recheck sources for updates before finalizing clinical claims.

The owner has already chosen:

- Clinician mode in English, with detailed assessment, medication hierarchy, Philippine availability, references and study summaries.
- Patient mode in **English, Tagalog, Cebuano and Kapampangan**, including tool labels, validation messages and printouts.
- Printable clinical algorithms and patient action sheets.
- Reuse of existing site calculators and addition of relevant missing tools.
- An explicit medication sequence grounded in drugs obtainable in the Philippines.

Do not ask the owner to reconfirm these choices. Make routine implementation decisions using the existing repository and this brief. Complete a reviewable implementation; identify factual or clinical-review gaps precisely instead of inventing content or reviewer approval.

## Scope and integration

First read applicable repository instructions and inspect routes, components, styling, calculators, language handling, print conventions, content registration, build commands and test setup. Produce a compact compatibility inventory as a development artifact. Preserve the established technology and avoid a framework migration solely for this guide.

If no repository is supplied, build a standalone static prototype with the same content/data architecture and document the integration points. Do not claim it has been installed on renalcarematters.com. Deployment and publishing are outside this implementation brief.

Use the proposed routes and page/component contracts in files 01 and 04 unless existing conventions require an equivalent mapping. Record that mapping. Include every clinician module C01–C18 and patient module P01–P12, paired topic navigation, search, evidence details, a language switch and print controls. Maintain the user’s topic when changing audience or language.

Provide an always-visible urgent-help entry and separate exits for pregnancy/postpartum and other excluded populations. A role switch is not credential authentication. The patient interface must not expose clinician prescribing controls as patient instructions.

## Clinical content implementation

Load the evidence register into structured records. Retrieve the current primary sources, their corrections, and exact relevant recommendation sections. Store guideline year separately from publication date. Record whether full text, abstract or metadata was actually checked. Preserve original evidence grades when available; do not invent grades or create a blended guideline.

Represent diagnostic thresholds, treatment targets, resistance definitions, measurement settings and urgent-assessment rules separately. Use named frameworks throughout. Implement the explicit differences documented in file 02, including source-specific MRA constraints and controlled-on-four-agent terminology. Unknown, not assessed and normal are different states.

Build all required medication fields, including source-verified starting dose, titration, formulation, relevant maximum, contraindications, interactions, monitoring and local status. Product strengths in file 07 are not dosing recommendations. Unresolved clinical text belongs in clearly marked review records; it must not be fabricated to pass a content validator.

Create an editorial conflict ledger for unresolved source discrepancies, especially the Philippine acute severe BP executive-summary discrepancy documented in file 02. Such discrepancies must not silently become production logic.

## Required medication hierarchy

Use file 07 as the hierarchy specification and initial local-market evidence map. The clinical UI and print artifact A11 must show assessment before escalation, complementary core therapy, appropriate diuretic selection, preferred add-on when suitable, and individualized subsequent options. Comorbid indications and contraindications can change the order.

Indapamide SR is the locally evidenced thiazide-like option in this research. Do not default to standalone chlorthalidone without verifying its actual Philippine product and supply. Do not assume amiloride or eplerenone is routinely obtainable or has the same locally approved indication as in another country. Keep emerging therapies visibly separate from practical local defaults.

For each routine selectable drug, match the exact generic, brand if used, salt, release form, route and strength to a current Philippine FDA record and dated supply evidence. A retailer listing does not prove branch stock. Preserve unknown values, registration validity dates and source URLs. Use generic names first. Do not hardcode unsupported prices or claim reimbursement from a formulary mention alone.

Treat availability as a branch in clinical reasoning, not an instruction to skip to a less suitable later drug. Do not build dose-equivalence substitutions, automatic prescriptions, patient-directed titration or PRN rescue instructions.

## Existing tools and new work

File 06 documents a public audit of 197 calculator cards. Before adding tools, search repository filenames, metadata, functions, embedded widgets and aliases for equivalents. Produce a reuse/extend/new decision for K01–K07 with the canonical location of any existing implementation.

Reuse the existing BP log, MAP, ARR, sodium, kidney function, KFRE, PREVENT, STOP-BANG and renal-medication tools as appropriate. Resolve the existing BP-log duration inconsistency. Review the existing BP-target and ARR logic against current sources before integrating it. Share validated functions rather than copy an old widget’s thresholds into new pages.

Implement file 06’s prioritized specifications:

1. K01: extend the home BP summary and protocol-quality reporting.
2. K02: phenotype/resistance criteria checklist, explicitly not a validated score.
3. K05: source-specific MRA information and monitoring worksheet.
4. K03: orthostatic BP changes.
5. K04: summary of validated ABPM report means and asleep/awake percentage fall.
6. K07: prescription-based cost/refill arithmetic.
7. K06: 24-hour urinary sodium unit conversion.

Implement all in the review preview unless an equivalent already exists. Reuse that equivalent when appropriate and report the mapping. Raw-device ABPM import is outside the initial scope. Patient tools cannot independently recommend starting, stopping or changing medicines.

## Languages, accessibility and print

Follow file 05’s content adaptation and review process. Keep clinician content English and create equivalent patient content for all four languages. Use the site’s established language adapter; canonical Kapampangan `pam` must interoperate with legacy `kap` attributes. Do not silently change unrelated site pages.

Track translation against the English patient source version. Draft translations may be included in the review preview, clearly labeled; do not represent machine-generated text as native-speaker approved. No invented translations, untranslated emergency fragments or fabricated sign-off. A source change invalidates the corresponding translation review.

Build A01–A11 print views from shared content records. Patient printouts use one selected language. Verify A4 and Letter, monochrome, readable type, unclipped branches, reference footers and deliberate inclusion of entered health data. Add page breaks rather than shrinking essential text. Include accessible text equivalents for diagrams.

Use responsive layouts, semantic headings, keyboard controls, labeled fields, visible focus, sufficient contrast and accessible error messages. Check at 360 px, desktop width and 200% zoom. Do not rely on color alone to convey urgency or eligibility.

## Data and privacy

Use pure, deterministic calculation functions with explicit units, structured results and independently checked fixtures. Store clinical content, translations, sources, thresholds and local formulary data separately but link them by stable IDs. Keep clinical constants out of scattered UI conditionals.

Keep health inputs in memory by default. No patient database, login, LLM advice endpoint, health-data analytics or third-party session replay. Do not put readings, medicines or diagnoses in URLs. Optional device-only saving requires clear user choice and delete/export controls. QR codes must contain only public guide URLs.

## Verification and deliverables

Run existing project checks and meaningful new tests for the formulas and safety-relevant pathway boundaries in files 04 and 06. Validate content references, exact units, locale completeness, source-version dependencies, medication registration status and review records. Test actual mode/language navigation, search, mobile layout, privacy and print output. Do not merely write tests without running them or report visual checks that were not performed.

Deliver:

1. Working guide preview with all routes, modules, tools and print views.
2. Source/claim register and explicit clinical-conflict records.
3. Philippine medication hierarchy and exact-product verification ledger.
4. Existing-calculator reuse map and specifications/fixtures for additions.
5. Four-language patient content and translation-review manifest.
6. Test and accessibility/print verification report, including limitations.
7. Maintainer instructions for content updates, source changes, local availability and stale translations.
8. A concise handoff separating implemented functionality, clinically reviewed material and remaining review items, without declaring draft medical material ready for clinical use.

Complete the preview autonomously. Use production validation to block unsigned critical clinical rules, unreviewed required translations and unverified routine local drug defaults. This is a content-release boundary, not a reason to leave the software implementation unfinished. Do not publish the site as part of this task.

## Definition of done

The implementation is complete when the repository builds, all specified interfaces work, tools reuse or extend existing canonical implementations, tests pass, printouts are verified, all four language variants exist in the review workflow, and remaining factual/review gaps are explicit records rather than hidden assumptions. A production release additionally requires actual clinical, local-medication and language review recorded by the responsible reviewers.
