# Mechanisms of Interorgan Crosstalk in Kidney Health and Diseases

**RenalCareMatters · Guide blueprint for Claude Code · Evidence checked 21 November 2026**

## Handoff for Claude Code

Build an evidence-linked RenalCareMatters guide for clinicians, trainees, and informed patients. Start by inspecting the target repository for its guide template, routes, navigation, references, and calculator registry. The source repository was unavailable during blueprint preparation. Treat the proposed slug `interorgan-crosstalk-kidney-health-disease` as an integration default. Reuse existing components and link existing calculators when equivalent. Ship the guide and the two priority tools behind the site's normal clinical content review process. Keep calculations local to the browser and exclude entered values from URLs, analytics, and persistence.

**Public-facing introduction.** The kidneys help regulate blood pressure, fluid balance, acid–base status, red blood cell production, and mineral metabolism. The heart, lungs, liver, gut, and other organs also change how the kidneys work. During acute kidney injury (AKI) or chronic kidney disease (CKD), these feedback loops can amplify illness. Understanding which pathway is active helps explain why the same creatinine rise can have different clinical implications.

## Page structure

1. **How healthy organs communicate.** Introduce pressure and flow, endocrine signaling, neural reflexes, metabolite handling, and immune signaling. Show that kidney filtration and tubular secretion change systemic exposure to solutes, and that regulation also runs through renin, erythropoietin, and calcitriol.
2. **What changes in AKI and CKD.** Present an acute timeline from insult through recovery or persistent dysfunction, next to longer-term CKD adaptations. A shared insult such as sepsis can affect several organs simultaneously. Temporal sequence, experimental perturbation, and human validation answer different causal questions.
3. **Organ systems.** Render the modules below as accessible cards with a paired direction of travel, clinical correlate, evidence labels, and linked sources.
4. **Three cases.** Use the synthetic examples below to connect mechanisms with clinical reasoning.
5. **Calculators and evidence.** Put each tool beside its relevant module and link its method. Add a sortable evidence table and a brief glossary for AKI, AKD, eGFR, uACR, KRT, RAAS, FGF23, and TSAT.

## Organ modules

| Axis | Healthy exchange and disease mechanisms | Clinical implication and evidence |
|---|---|---|
| Heart and circulation | Cardiac output and arterial pressure support renal perfusion. Natriuretic peptides favor natriuresis. Renin–angiotensin–aldosterone and sympathetic activity defend effective perfusion. In heart failure, elevated venous pressure can impair renal function alongside low forward flow. AKI can affect the heart through volume overload, hyperkalemia, and acidemia. Chronic mineral and endocrine changes add cardiovascular burden. | Interpret creatinine changes alongside congestion, perfusion, urine output, and time course. Teach the five cardiorenal phenotypes as a taxonomy with overlap. Link final ESC–ERA 2026 guidance for cardiovascular care in CKD and KDIGO 2024 for CKD-specific risk staging and therapy. [ESC26] [CKD24] [ICU25] |
| Lung | Ventilation governs carbon dioxide removal while kidneys adjust bicarbonate handling and net acid excretion. AKI can increase pulmonary edema through positive fluid balance. Animal models also implicate cytokine-dependent permeability and altered alveolar fluid transport. Hypoxemia, shock, and positive-pressure ventilation can alter renal perfusion and venous pressure. | Show hydrostatic edema, inflammatory permeability, and mixed cases. Integrate respiratory status, fluid trajectory, hemodynamics, and urine output. Label direct cytokine transfer as model-dependent. [ICU25] [AKI26R] |
| Liver | Hepatic metabolism and kidney excretion jointly handle circulating solutes. In advanced cirrhosis, splanchnic vasodilation lowers effective arterial filling and triggers vasoconstrictor systems, reducing renal perfusion. Inflammation, tubular injury, and congestive physiology may coexist. Sarcopenia can lower creatinine production. | Teach the 2024 ADQI–ICA criteria for hepatorenal syndrome–AKI (HRS-AKI). Cirrhosis with ascites, qualifying AKI, absent improvement within 24 hours of adequate resuscitation when indicated, and no strong alternative primary cause are required. A routine 48-hour albumin challenge is no longer required by this consensus. Show terlipressin benefit and respiratory risk side by side. [HRS24] [CONFIRM] [LABEL] |
| Gut and liver | Microbes metabolize dietary precursors. The liver converts indole and p-cresol to indoxyl sulfate and p-cresyl sulfate. Impaired kidney clearance increases exposure. CKD-related diet changes, medications, intestinal edema, and the uremic milieu can reshape microbial composition and barrier function. | Distinguish metabolite generation, host processing, and clearance. SYNERGY assessed short-term toxin concentrations. Its primary indoxyl sulfate result was not significant and its p-cresyl sulfate result was a secondary surrogate. Keep microbiome-targeted therapy in the research section. [SYNERGY] [MICRO25] |
| Bone, parathyroid, and vasculature | Bone-derived FGF23 promotes phosphaturia through renal signaling that depends on α-Klotho and suppresses calcitriol. Parathyroid hormone and vitamin D participate in feedback across kidney, intestine, and bone. In CKD, phosphate handling, calcitriol, and PTH change as kidney function falls. Experimental FGFR4 signaling links FGF23 to cardiac hypertrophy. | Teach serial calcium, phosphate, and PTH interpretation together, with alkaline phosphatase where indicated. Label FGF23 cardiac causality as experimental and routine clinical management under CKD-MBD guidance. [MBD17] [FGF23] |
| Bone marrow and immune system | Renal oxygen sensing regulates erythropoietin and marrow red-cell production. CKD anemia also involves iron restriction, inflammation, blood loss, and other reversible causes. Hepatic hepcidin reduces iron availability through ferroportin. Systemic inflammatory signals can contribute to kidney injury. Injured kidneys can release mediators that affect distant tissues in experimental models. | Pair Hb with iron indices and evaluate other causes before attributing anemia to CKD. Discuss the distinction between iron initiation and monitoring during therapy. Present immune signaling alongside the clinical uncertainty of identifying its organ of origin in sepsis. [ANEMIA26] [SIGNAL26] |
| Brain and autonomic nervous system | Renal sympathetic efferents regulate vascular tone, renin, and sodium handling. Renal afferents can influence central sympathetic activity. Severe kidney dysfunction may contribute to encephalopathy through metabolic disturbances and retained solutes. Vascular disease, medications, critical illness, and delirium complicate attribution. Experimental AKI studies implicate endothelial and blood–brain barrier injury. | Use a differential diagnosis for acute mental-status change. Separate established metabolic complications from experimental neuroinflammation. Show that brain injury can also alter renal perfusion through autonomic and systemic responses. [ICU25] [AKI26R] |
| Skeletal muscle and metabolic organs | Muscle generates creatinine. CKD-related acidosis, inflammation, inactivity, and anorexia can contribute to muscle loss. Severe muscle injury releases myoglobin, which can injure tubules through pigment-related toxicity and obstruction. Diabetes and adipose-derived metabolic signals can influence renal hemodynamics and inflammation. | Low muscle mass can bias creatinine-based eGFR upward. Describe use of combined creatinine–cystatin C assessment when creatinine is less reliable and GFR affects decisions, with attention to non-GFR determinants of both markers. Keep eGFR interpretation separate from acute non-steady-state creatinine. [CKD24] [MET26] |

Add a mechanism strip to each card showing **source tissue → route or mediator → target → response → feedback**. Put experimental extracellular vesicles, tissue-specific tracing, and multi-omics in a research panel. Detecting a molecule in blood or finding a spatial or transcriptional signature does not establish its source, target engagement, or benefit from treatment. [SIGNAL26] [CELL26]

## Quantitative evidence for the guide

| Study and design | Population and endpoint | Result | Interpretation |
|---|---|---|---|
| EMPA-KIDNEY randomized trial [EMPA] | 6,609 adults with eligible CKD. Kidney disease progression or cardiovascular death over median 2.0 years. | 432/3,304 (13.1%) vs 558/3,305 (16.9%). HR 0.72 (95% CI 0.64–0.82). | Clinical benefit in the studied population. Composite result does not isolate cardiovascular mortality or prove a particular signaling pathway. |
| ASSESS-AKI prospective matched cohort [ASSESS] | 1,538 hospital survivors, 769 with AKI. uACR assessed at approximately 3 months after discharge. Progression was halving of eGFR or kidney failure. | In the AKI subgroup, unadjusted HR per doubling of uACR 1.53 (95% CI 1.43–1.64), C statistic 0.82. | Supports uACR measurement at follow-up. The cohort association cannot be converted into individual absolute risk. |
| CONFIRM randomized trial [CONFIRM] [LABEL] | 300 adults with HRS-1 using the trial definition. Verified reversal of HRS. | Reversal 63/199 (32%) vs 17/101 (17%). U.S. label reports serious or fatal respiratory failure in 14% vs 5% in the safety population. | Report benefit and harm as distinct endpoints with their own analysis populations. Avoid generalizing trial eligibility to all cases meeting modern HRS-AKI criteria. |
| VExUS derivation [VEX] and general ICU cohort [VEXICU] | Post-cardiac surgery derivation cohort of 145. Separate prospective multicenter general ICU cohort with 145 participants. | Severe derivation grade and subsequent AKI HR 3.69 (95% CI 1.65–8.24). Day-one grade was not associated with AKI in the general ICU cohort (P=.372). | Setting and pretest context matter. Treat VExUS as an ultrasound phenotype with conditional portability. |
| FGF23 experimental study with human cohort component [FGF23] | Human CKD cohort and cardiomyocyte/rodent experiments. Left ventricular hypertrophy. | Human association and experimental hypertrophy after perturbation. | Demonstrates a mechanistic line of evidence and a separate human association. Do not infer a proven human treatment target. |

### Data contract

Store content in the site's existing content format. Each quantitative record needs a stable ID, source ID, publication date where known, design, population, eligibility, sample size, endpoint, comparison, follow-up, adjusted status, effect measure, estimate, CI bounds, arm numerators and denominators where reported, and limitations. Allow null for unreported fields. Use distinct record IDs for off-target harms, subgroup results, surrogates, and composite endpoints. Preserve exact source precision. Charts should show the comparator, population, follow-up, and uncertainty next to the displayed number.

Each mechanism record needs source and target organs, direction, mediator, acute/chronic context, model/species, evidence design, measured outcome, applicability, and source IDs. Maintain separate labels for guideline, human intervention, human observational, experimental mechanism, and narrative synthesis. Recommendations also need authority, version, status, recommendation or practice-point identifier, and publication review date. Draft recommendations can appear only in the evidence watchlist. Keep implementation choices and synthetic fixtures out of published data.

## Calculators and decision aids

### Priority 1 · Post-AKI follow-up planner

**Job.** Turn a documented adult AKI hospitalization into a follow-up checklist and review dates. [AKI12] [ASSESS]

- **Inputs.** AKI onset date if known, discharge date, assessment date, documented maximum AKI stage or unknown, baseline and latest creatinine with units and dates if available, ongoing dialysis at discharge, known CKD, and clinician-entered concerns about incomplete recovery, heart failure, or unresolved electrolyte issues.
- **Rules.** Anchor the guideline reassessment to 3 calendar months after AKI onset. If onset is unknown, show a separate discharge-based 3-month checkpoint and label the date as an operational fallback. Month addition clamps to the final valid day. Show creatinine and kidney function assessment, spot uACR, BP and volume review, and medication reconciliation. Allow follow-up earlier than the 3-month milestone. Mark dialysis at discharge or unresolved findings for clinician-directed scheduling and use a dedicated dialysis-transition pathway where available.
- **Outputs.** Milestone date, due status, checklist, and optional absolute/percentage change from a credible positive creatinine baseline. Store date-only values as calendar dates. Convert creatinine once to a canonical unit. Use 88.4 μmol/L per mg/dL. Show unknown baseline explicitly.
- **Fixtures.** AKI onset 2026-08-31 → 2026-11-30. Missing onset with discharge 2026-09-10 → fallback 2026-12-10. Baseline 88.4 μmol/L and latest 1.5 mg/dL → +0.5 mg/dL and +50%. A latest test timestamp before the baseline must prevent a trend calculation. Dialysis dependence must override any routine-only checklist.
- **Scope.** Planning aid. Provide no automatic recovery designation, derived AKI stage, risk estimate, or medication instruction. Evaluate for CKD using established chronicity criteria.

### Priority 1 · CKD anemia iron criteria checker

**Job.** Show whether measured ferritin and TSAT meet the KDIGO 2026 iron initiation criteria for the chosen CKD modality. [ANEMIA26]

- **Inputs.** Adult with confirmed CKD and documented anemia, modality (hemodialysis, peritoneal dialysis, or no dialysis), ferritin in ng/mL or μg/L, TSAT in percent, test dates, current iron treatment, and known or suspected active systemic infection. Route pregnancy and kidney transplant to specialist review in the first release.
- **Initiation branch.** In CKD G5HD, ferritin ≤500 and TSAT ≤30 meet recommendation 2.1 criteria. In non-dialysis CKD or CKD G5PD, use ferritin <100 with TSAT <40, or ferritin ≥100 and <300 with TSAT <25, per recommendation 2.3. These are graded suggestions, both 2D.
- **Monitoring branch.** For patients already receiving iron, report the practice-point condition for withholding routine iron at ferritin >700 or TSAT ≥40. With active systemic infection, display the guideline's infection precaution and suppress the routine threshold interpretation pending clinician review. Use an insufficient-data state for an unknown modality, missing required values, or unconfirmed anemia. Flag date discordance for clinician review.
- **Outputs.** Criteria met, criteria unmet, or unable to assess, with the applicable branch, units, thresholds and source. For current iron use, show the monitoring rule separately. Output no dose or prescription.
- **Fixtures.** HD 500/30 → meets. HD 500/30.1 → does not meet. PD 99/39 → meets. PD 100/25 → does not meet. PD 100/24.9 → meets. Non-dialysis 300/24 → does not meet. On iron 700/39.9 → withholding threshold not met, 700.1/39.9 or 700/40 → met. Infection → clinician review regardless of numeric result.

### Next release · Targeted opportunities

| Opportunity | Inputs and outputs | Build decision |
|---|---|---|
| Kidney Failure Risk Equation | Age, model-defined sex input, stable eGFR and quantitative uACR. Show 2- and 5-year treated kidney failure probability, calibration provenance, and applicable KDIGO practice points. | Reuse or deep-link validated implementation first. If implementing, pin coefficients and region-specific baseline survival from the original validated model, distinguish mg/g and mg/mmol (1 mg/mmol ≈ 8.84 mg/g), and compare golden cases against the reference. Adult stable CKD G3–G5 scope. Show KDIGO 5-year 3–5% referral range, 2-year >10% multidisciplinary care, and >40% KRT preparation context. Verify local calibration before claiming Philippine applicability. [KFRE] [CKD24] [ESC26] |
| HRS-AKI criteria worksheet | Document ascites, creatinine change and dates, measured urine output and duration, response after clinically indicated resuscitation, and evidence of an alternative primary cause. Output criteria present, absent, or unknown with prompt for clinical assessment. | Clinician-only after hepatology review. Test alternate primary cause, missing resuscitation assessment, and diuresis/measurement confounders. Use the consensus criteria as written, including the cirrhosis-specific urine output wording. No automated diagnosis or vasoconstrictor dosing. [HRS24] |
| VExUS grading worksheet | IVC diameter and operator-classified hepatic, portal, and intrarenal Doppler patterns. Output original VExUS C grade, criteria trace, and incomplete-data status. | Clinician-only after ultrasound review. Encode original grading table, test IVC at 2.0 cm and each severe-waveform count, and block definitive grading with incomplete data unless supported by the source rule. Highlight limitations with cirrhosis, severe tricuspid regurgitation, ventilation, and technically inadequate windows. Do not output AKI probability or diuretic recommendations. [VEX] [VEXICU] |

Defer any composite crosstalk score or gut toxin index. A research model would need a prespecified outcome, a development cohort, external validation, calibration, missing-data handling, and evidence that the output improves decisions. The current studies answer different questions in different populations.

## Cases for the guide

- **Heart failure and rising creatinine.** After decongestion, a synthetic patient's creatinine rises from 1.2 to 1.5 mg/dL while edema and dyspnea improve. Ask what the interval, BP, perfusion, urine output, and congestion trajectory add before assigning a cause. Include a second state with hypotension and falling urine output to show why similar creatinine results can imply different next steps.
- **Cirrhosis with ascites and oliguria.** Use a creatinine rise from 0.8 to 1.2 mg/dL over 36 hours. Ask learners to review response to clinically appropriate volume management and examine infection, shock, obstruction, nephrotoxin exposure, and tubular injury. Have them identify the respiratory safety considerations that matter before treatment.
- **Post-AKI follow-up with CKD anemia.** At reassessment after AKI, review persistent albuminuria and kidney function before applying CKD staging. A patient with established non-dialysis CKD, anemia, ferritin 150 ng/mL, and TSAT 22% meets the corresponding iron initiation thresholds. Ask learners how infection, bleeding, or existing iron treatment changes interpretation.

## Repository acceptance criteria

- All eight cards have readable bidirectional pathways and evidence labels. Provide a text reading order for any interactive diagram. Match repository navigation, keyboard operation, focus states, and mobile breakpoints.
- All guideline statements resolve to the cited source and version. Editors verify drug-specific recommendations against applicable labeling and local pathways. Show a dated review note and configured clinical reviewer after review.
- Test calculator boundaries at and immediately around every cutoff, missing data, unsupported populations, invalid numbers, TSAT outside 0–100%, zero creatinine, mixed units, leap dates, future event dates, and midnight/time-zone behavior. Normalize before evaluating and round only for display. Render a clear failure state when a calculation cannot proceed.
- Run the repository's standard tests and build. Confirm direct URLs, reference links, responsive layouts, keyboard-only use, and the absence of lab values in analytics requests. Require a nephrology review of published medical copy and both calculator fixture sets.
- Refresh the evidence watchlist at major guideline releases. The KDIGO 2026 AKI/AKD update and KDIGO 2027 CKD medications update were listed as public-review drafts at review. Keep the site tied to final guidance until the applicable update publishes. [AKIWATCH] [CKDWATCH]

## References

- **[SIGNAL26]** Interorgan Signaling in Kidney Health and Disease. JASN, online October 2026. [PubMed abstract](https://pubmed.ncbi.nlm.nih.gov/42950243/)
- **[CELL26]** Cell–cell crosstalk in kidney health and disease. Nature Reviews Nephrology, 2026. [Article](https://www.nature.com/articles/s41581-025-01025-1)
- **[MET26]** Organ crosstalk in kidney diseases. Life Sciences, 2026. [Article](https://doi.org/10.1016/j.lfs.2026.124637)
- **[AKI26R]** AKI as a systemic syndrome and its impact on other organ systems. Critical Care, 2026. [Article](https://doi.org/10.1186/s13054-026-06252-x)
- **[ICU25]** Kidney-organ interactions. Current Opinion in Critical Care, 2025. [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC13323966/)
- **[MICRO25]** Microbiota and kidney disease. Nature Reviews Nephrology, published online 2025. [Article](https://www.nature.com/articles/s41581-025-00988-5)
- **[ESC26]** 2026 ESC–ERA cardiovascular disease and CKD guideline. See Section 3.5 and Recommendation Table 5. [Guideline](https://doi.org/10.1093/eurheartj/ehag098)
- **[CKD24]** KDIGO 2024 CKD guideline. See Section 2.2 and practice points 2.2.1–2.2.3. [Guideline](https://kdigo.org/wp-content/uploads/2024/03/KDIGO-2024-CKD-Guideline.pdf)
- **[AKI12]** KDIGO 2012 AKI guideline. See recommendation 2.3.4 for post-AKI reassessment at 3 months. [Guideline](https://kdigo.org/wp-content/uploads/2016/10/KDIGO-2012-AKI-Guideline-English.pdf)
- **[AKIWATCH]** [KDIGO AKI and AKD guideline status](https://kdigo.org/guidelines/acute-kidney-injury/)
- **[CKDWATCH]** [KDIGO CKD guideline status](https://kdigo.org/guidelines/ckd-evaluation-and-management/)
- **[ANEMIA26]** KDIGO 2026 anemia in CKD guideline. See recommendations 2.1 and 2.3 and Chapter 2 practice points. [Guideline](https://kdigo.org/wp-content/uploads/2026/04/KDIGO-2026-Anemia-in-CKD-Guideline.pdf)
- **[MBD17]** KDIGO 2017 CKD-MBD update. [Guideline hub](https://kdigo.org/guidelines/ckd-mbd/)
- **[HRS24]** ADQI–ICA consensus on AKI in cirrhosis. Journal of Hepatology, 2024. [Article](https://doi.org/10.1016/j.jhep.2024.03.031)
- **[CONFIRM]** Wong et al. Terlipressin plus albumin for the treatment of type 1 hepatorenal syndrome. NEJM, 2021. [Trial](https://doi.org/10.1056/NEJMoa2008290)
- **[LABEL]** TERLIVAZ U.S. prescribing information. [DailyMed label](https://dailymed.nlm.nih.gov/dailymed/fda/fdaDrugXsl.cfm?setid=3a35b86c-f451-4fac-8499-43019e4da354)
- **[EMPA]** EMPA-KIDNEY Collaborative Group. Empagliflozin in patients with CKD. NEJM, 2023. [Trial](https://doi.org/10.1056/NEJMoa2204233)
- **[ASSESS]** Hsu et al. Post-AKI proteinuria and kidney disease progression. JAMA Internal Medicine, 2020. Use Table 2 for the AKI subgroup. [Cohort](https://doi.org/10.1001/jamainternmed.2019.6390)
- **[KFRE]** Tangri et al. Multinational assessment of kidney failure prediction equations. JAMA, 2016. [Validation](https://doi.org/10.1001/jama.2015.18202)
- **[VEX]** Beaubien-Souligny et al. Development of the VExUS grading system. Ultrasound Journal, 2020. [Derivation](https://pubmed.ncbi.nlm.nih.gov/32270297/)
- **[VEXICU]** Prospective multicenter study of VExUS and AKI in a general ICU cohort. Critical Care, 2023. [Cohort](https://pmc.ncbi.nlm.nih.gov/articles/PMC10249288/)
- **[FGF23]** Faul et al. FGF23 induces left ventricular hypertrophy. JCI, 2011. [Experimental and cohort study](https://doi.org/10.1172/JCI46122)
- **[SYNERGY]** Rossi et al. Synbiotics easing renal failure by improving gut microbiology. CJASN, 2016. [Trial](https://pubmed.ncbi.nlm.nih.gov/26772193/)
