# Graph Report - .  (2026-05-27)

## Corpus Check
- Large corpus: 117 files · ~2,350,102 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 257 nodes · 439 edges · 16 communities
- Extraction: 74% EXTRACTED · 26% INFERRED · 0% AMBIGUOUS · INFERRED: 112 edges (avg confidence: 0.82)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Dialysis Care & Quality of Life|Dialysis Care & Quality of Life]]
- [[_COMMUNITY_CKD Disease Management|CKD Disease Management]]
- [[_COMMUNITY_Hemodialysis Prescription & Complications|Hemodialysis Prescription & Complications]]
- [[_COMMUNITY_Vascular Access & CKD Progression|Vascular Access & CKD Progression]]
- [[_COMMUNITY_Dialysis Access & Fluid Management|Dialysis Access & Fluid Management]]
- [[_COMMUNITY_Anemia, Iron & Electrolytes|Anemia, Iron & Electrolytes]]
- [[_COMMUNITY_Alternative Remedies & Monitoring|Alternative Remedies & Monitoring]]
- [[_COMMUNITY_Philippine Context & Patient Education|Philippine Context & Patient Education]]
- [[_COMMUNITY_Infectious AKI & Infection Control|Infectious AKI & Infection Control]]
- [[_COMMUNITY_Cardiorenal & Metabolic Syndrome|Cardiorenal & Metabolic Syndrome]]
- [[_COMMUNITY_Acute Kidney Injury|Acute Kidney Injury]]
- [[_COMMUNITY_Renal Nutrition & Phosphorus|Renal Nutrition & Phosphorus]]
- [[_COMMUNITY_Kidney Stones & UTI|Kidney Stones & UTI]]
- [[_COMMUNITY_Dyslipidemia & Cooking Oils|Dyslipidemia & Cooking Oils]]
- [[_COMMUNITY_Pediatric & Glomerular Disease|Pediatric & Glomerular Disease]]
- [[_COMMUNITY_Blood Pressure & Physiology|Blood Pressure & Physiology]]

## God Nodes (most connected - your core abstractions)
1. `Living with Dialysis` - 10 edges
2. `Dialysis Adequacy` - 9 edges
3. `Proteins & Proteinuria` - 9 edges
4. `Obesity & CKD` - 9 edges
5. `Pain Management in CKD` - 8 edges
6. `Nutrition for Kidney Patients` - 8 edges
7. `Potassium & Hyperkalemia in CKD` - 8 edges
8. `Glomerulonephritis: Inflamed Kidney Filters` - 8 edges
9. `Managing High Blood Pressure` - 8 edges
10. `GLP-1 Drugs & Kidneys (Ozempic/Semaglutide)` - 8 edges

## Surprising Connections (you probably didn't know these)
- `Dialysis Access Care` --conceptually_related_to--> `Dialysis Adequacy`  [INFERRED]
  guides/dialysis-access-care.html → guides/dialysis-adequacy.html
- `Dialysis Access Care` --conceptually_related_to--> `Cardiovascular Disease and Sudden Death in Dialysis`  [INFERRED]
  guides/dialysis-access-care.html → guides/cardiovascular-death-dialysis.html
- `Patient Guides Index — W. G. M. Rivero, MD` --references--> `PhilHealth Benefits: HD, PD and Kidney Transplant`  [INFERRED]
  guides/index.html → guides/philhealth-z-packages.html
- `Kain Pa Rin: CKD Nutrition Guide for Filipino Patients` --conceptually_related_to--> `Sodium and Salt Reduction in CKD`  [INFERRED]
  guides/kain-pa-rin.html → guides/sodium-salt-reduction-ckd.html
- `CKD, Mental Health and Sleep` --conceptually_related_to--> `CKD Dietary Reference Intake Calculator`  [INFERRED]
  guides/ckd-mental-health-sleep.html → guides/ckd-dri-calculator.html

## Hyperedges (group relationships)
- **Dialysis Patient Management Guides** — guides_dialysis_access_care, guides_eating_on_dialysis, guides_dialysis_adequacy, guides_post_dialysis_fatigue, guides_cardiovascular_death_dialysis, guides_el_nino_heat_dialysis, guides_hemodialysis_transfer_guide [INFERRED 0.95]
- **CKD Foundation and Understanding Guides** — guides_understanding_ckd, guides_first_nephrology_visit_guide, guides_hypertensive_kidney_disease, guides_lupus_nephritis, guides_tuberculosis_kidney_disease [INFERRED 0.85]
- **CKD Diet and Supplement Guides** — guides_eating_on_dialysis, guides_uremic_toxin_precursors, guides_natural_supplements_kidney, guides_vinegar_acv_guide [INFERRED 0.85]
- **CKD Patient Support and Psychosocial Guides** — guides_ckd_financial_stress, guides_symptom_checker, guides_ckd_skin_darkening_body_changes, guides_bp_log_blank [INFERRED 0.75]

## Communities (16 total, 0 thin omitted)

### Community 0 - "Dialysis Care & Quality of Life"
Cohesion: 0.10
Nodes (32): Advance Care Planning, Cardiovascular Disease in Dialysis, CKD Dermatological Changes, Post-Dialysis Fatigue, Dialysis Adequacy (Kt/V, URR), Dialysis Nutrition and Diet, Dialysis Withdrawal, Disaster Preparedness for Dialysis Patients (+24 more)

### Community 1 - "CKD Disease Management"
Cohesion: 0.15
Nodes (31): ACE Inhibitor / ARB Therapy, Cholesterol & Dyslipidemia in CKD, Chronic Kidney Disease (CKD), Diabetes & Kidney Disease, Glomerular Disease, GLP-1 Receptor Agonists, Gut-Kidney Axis & Uremic Toxins, HIV-Associated Kidney Disease (+23 more)

### Community 2 - "Hemodialysis Prescription & Complications"
Cohesion: 0.12
Nodes (23): Kidney Allograft Rejection — Causes and Management, Caregiver Burnout in CKD, Muscle Cramps During Hemodialysis, Dialysis Prescription — Kt/V and Adequacy, ESA Dose Adjustment in CKD, Fistula Care at Home, Hormonal Disruption in Dialysis Patients, Intradialytic Hypotension Management (+15 more)

### Community 3 - "Vascular Access & CKD Progression"
Cohesion: 0.12
Nodes (23): AVF Aneurysm and Degeneration, Arteriovenous Fistula (AVF), Blood Pressure Control in CKD, CKD-Mineral Bone Disease (CKD-MBD), Slowing CKD Progression (SGLT2i, RAAS, BP control), Diabetic Diet (Filipino context), Ketoanalogue Supplementation, Kidney Toxins from Food (+15 more)

### Community 4 - "Dialysis Access & Fluid Management"
Cohesion: 0.15
Nodes (22): Safe Analgesics in CKD, Dialysis (Hemodialysis/Peritoneal), Dialysis Vascular Access (AV Fistula, Graft, Catheter), End-Stage Kidney Disease (ESKD), AV Fistula & Dialysis Access Care, Fluid Management in Dialysis, Fluid Restriction & Dry Weight, Neuropathic Pain in CKD (+14 more)

### Community 5 - "Anemia, Iron & Electrolytes"
Cohesion: 0.16
Nodes (18): Anemia in CKD, Sodium Bicarbonate Treatment, ESA Therapy (Erythropoiesis-Stimulating Agents), Hyperkalemia (High Potassium), Iron Deficiency & IV Iron, Iron Therapy in CKD Anemia, Ketogenic & Low-Carb Diet, Metabolic Acidosis (+10 more)

### Community 6 - "Alternative Remedies & Monitoring"
Cohesion: 0.16
Nodes (18): Apple Cider Vinegar and Metabolic Health, Blood Pressure Monitoring, Benign Prostatic Hyperplasia (BPH), Chronic Kidney Disease (CKD), Systemic Lupus Erythematosus (SLE), Natural Supplements and Herbal Remedies, Patient Symptom Triage, Tuberculosis (TB) (+10 more)

### Community 7 - "Philippine Context & Patient Education"
Cohesion: 0.15
Nodes (16): Alcohol Self-Monitoring for Kidney and Heart Patients, CKD Epidemiology in the Philippines, CKD Patient Education and Self-Management, Dialysis Access and Rates in the Philippines, Herbal Remedy Danger in Kidney Disease, Nephrectomy for Kidney Cancer, Nephrology Visual Atlas — Anatomy, Pathology, Procedures, NSAID-Induced Acute Kidney Injury (+8 more)

### Community 8 - "Infectious AKI & Infection Control"
Cohesion: 0.16
Nodes (16): Acute Kidney Injury from Infectious Causes, Dialysis Management and Preparation, Herbal and Alternative Medicine Kidney Toxicity, Infection Control and Serology in Dialysis, Emerging Technologies in Kidney Disease Treatment, Mental Health and Psychosocial Aspects of CKD, PhilHealth Z-Benefit Packages for Kidney Disease, CKD and Alternative Holistic Medicine: Fact vs Fiction (+8 more)

### Community 9 - "Cardiorenal & Metabolic Syndrome"
Cohesion: 0.20
Nodes (16): Cardiorenal Syndrome and Heart-Kidney Interaction, CKD Nutrition and Dietary Management, Diabetic Nephropathy and CKD from Diabetes, Hyperuricemia, Gout, and Kidney Disease Interaction, Laboratory Result Interpretation in CKD (eGFR, Creatinine, KDIGO), Cardiac Rehabilitation for CKD Patients After Heart Attack, CKD Dietary Reference Intake Calculator, CKD Recipe Nutrition Analyzer (+8 more)

### Community 10 - "Acute Kidney Injury"
Cohesion: 0.25
Nodes (11): Acute Kidney Injury (AKI), Contrast-Induced AKI, Dengue-Associated Kidney Injury, Hantavirus / HFRS, NSAIDs & Kidney Toxicity, Urinary Tract Infection (UTI), Acute Kidney Injury on CKD (AKI-on-CKD), Contrast-Induced Nephropathy (+3 more)

### Community 11 - "Renal Nutrition & Phosphorus"
Cohesion: 0.31
Nodes (9): CKD-Friendly Filipino Regional Recipes, Hyperphosphatemia in CKD, Phosphate Binders in CKD, Protein Intake in CKD, Sarcopenia and Muscle Wasting in CKD, Vascular Calcification in CKD, CKD-Friendly Regional Philippine Recipes, Muscle Building & Supplements in CKD (+1 more)

### Community 12 - "Kidney Stones & UTI"
Cohesion: 0.47
Nodes (6): Kidney Stone Prevention and Diet, Kidney Stone Types and Treatment, Antibiotic Management of UTI in CKD, UTI-Driven Kidney Scarring in CKD, Managing Kidney Stones, Recurrent UTI as a CKD Peril

### Community 13 - "Dyslipidemia & Cooking Oils"
Cohesion: 0.40
Nodes (6): Cooking Oils for Dyslipidemia and CKD, Dyslipidemia in CKD — LDL Targets and Statin Safety, PCSK9 Inhibitors in CKD, Statin Use in CKD and Dialysis Patients, Cooking Oils & Fats: An Evidence-Based Patient Guide, Dyslipidemia: 2026 Guidelines Update

### Community 14 - "Pediatric & Glomerular Disease"
Cohesion: 0.60
Nodes (6): Hematuria (Blood in Urine), IgA Nephropathy (IgAN / Berger Disease), Pediatric CKD & Transitional Nephrology, CKD in Children & Young Adults, Hematuria — Blood in Urine, IgA Nephropathy Patient Guide

### Community 15 - "Blood Pressure & Physiology"
Cohesion: 0.67
Nodes (4): Blood Pressure Management, Normal Kidney Physiology, 7-Day Blood Pressure Monitoring Log, Kidney Physiology — Normal Function

## Ambiguous Edges - Review These
- `Hematuria — Blood in Urine` → `Hematuria — Blood in Urine`  [AMBIGUOUS]
  guides/hematuria-blood-in-urine.html · relation: conceptually_related_to
- `Glomerulonephritis: Inflamed Kidney Filters` → `GLP-1 Drugs & Kidneys (Ozempic/Semaglutide)`  [AMBIGUOUS]
  guides/glomerulonephritis.html · relation: conceptually_related_to

## Knowledge Gaps
- **11 isolated node(s):** `Safe Medications in CKD Pregnancy`, `PCSK9 Inhibitors in CKD`, `ESA Dose Adjustment in CKD`, `CKD Patient Education and Self-Management`, `Herbal Remedy Danger in Kidney Disease` (+6 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Hematuria — Blood in Urine` and `Hematuria — Blood in Urine`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Glomerulonephritis: Inflamed Kidney Filters` and `GLP-1 Drugs & Kidneys (Ozempic/Semaglutide)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Hypertensive Kidney Disease` connect `Alternative Remedies & Monitoring` to `CKD Disease Management`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Why does `Advance Care Planning for Dialysis Patients` connect `Dialysis Care & Quality of Life` to `CKD Disease Management`?**
  _High betweenness centrality (0.028) - this node is a cross-community bridge._
- **Why does `Pain Management in CKD` connect `Dialysis Access & Fluid Management` to `CKD Disease Management`, `Acute Kidney Injury`?**
  _High betweenness centrality (0.027) - this node is a cross-community bridge._
- **Are the 3 inferred relationships involving `Chronic Kidney Disease (CKD)` (e.g. with `7-Day Blood Pressure Monitoring Log` and `Kidney Physiology — Normal Function`) actually correct?**
  _`Chronic Kidney Disease (CKD)` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `Dialysis (Hemodialysis/Peritoneal)` (e.g. with `Pain Management in CKD` and `Iron & Anemia in Kidney Disease`) actually correct?**
  _`Dialysis (Hemodialysis/Peritoneal)` has 2 INFERRED edges - model-reasoned connections that need verification._