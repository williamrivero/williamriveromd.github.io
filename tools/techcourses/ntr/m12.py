# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 12: Blood pressure and cardiovascular kidney care.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. KDIGO 2021
recommendations and grades checked against the KDIGO executive summary; KDIGO 2024 RASi and statin grades against the KDIGO
2024 summary; 2025 AHA/ACC statements against the guideline record and society summaries (COR given only where verified);
SPRINT, SPRINT CKD subgroup, PATHWAY-2, CLICK, SHARP and ESCAPE against PubMed abstracts and full text. No doses. Fictional case."""

MODULE = {'image_alt': 'A Filipino medical intern measures the blood pressure of a seated tricycle driver whose back is supported, feet flat and arm resting at heart level, in a quiet clinic room.',
 'objectives': ['<strong>Intern:</strong> Measure blood pressure the standardized way, record it with the cuff size and the conditions, and recognize the readings that need a physician now.',
                '<strong>Resident:</strong> Choose a blood pressure target and drug classes for a patient with chronic kidney disease (CKD), starting with renin-angiotensin system inhibitors (RASi) where albuminuria calls for them, and monitor potassium and creatinine safely.',
                '<strong>Fellow:</strong> Reconcile the Kidney Disease: Improving Global Outcomes (KDIGO) 2021 target, the 2025 American Heart Association/American College of Cardiology (AHA/ACC) target and the Systolic Blood Pressure Intervention Trial (SPRINT) evidence, and work up and treat resistant hypertension and cardiovascular risk.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the pressure in CKD, from cuff to plan</span>As an <strong>intern</strong>, '
        'you own the number: a reading taken badly will mislead every decision after it. As a <strong>resident</strong>, you own the plan for the '
        'day: the target your attending sets, the drug that protects the kidney, and the potassium and creatinine checked at the right time. As a '
        '<strong>fellow</strong>, you own the hard cases: the patient whose pressure will not come down, the guideline disagreement a resident asks '
        'you about at 2 a.m., and the cardiovascular risk that kills more patients with CKD than kidney failure does.</div>\n'
        '{{plain:Think of the glomerulus as a coffee filter attached to a garden hose. The water pressure in the street (systemic blood pressure) '
        'is passed through a tap (the afferent arteriole) to the filter. In a healthy kidney the tap adjusts itself so that the filter sees '
        'roughly the same pressure whatever the street does.}}\n'
        '<p>The picture has a limit. In CKD the tap stops adjusting. Fewer nephrons, scarred arterioles and the dilation that comes with '
        'hyperfiltration mean that more of the street pressure reaches each remaining glomerulus. High systemic pressure then becomes high '
        'glomerular pressure, more albumin leaks, and scarring speeds up. At the same time, a stiff, calcified arterial tree and sodium '
        'retention keep the systemic pressure high. That is why pressure control in CKD protects both the heart and the kidney, and why drugs '
        'that relax the efferent arteriole (the outflow side of the filter) lower glomerular pressure more than their effect on the arm cuff '
        'suggests.</p>\n'
        '{{cards:Key numbers|Measurement (KDIGO 2021)::Standardized office measurement preferred over routine office readings (1B)|Target (KDIGO '
        '2021)::Systolic below 120 mm Hg when tolerated, by standardized office measurement (2B)|Target (2025 AHA/ACC)::Below 130/80 mm Hg for all '
        'adults, with encouragement to reach a systolic below 120 mm Hg|SPRINT, 9,361 adults without diabetes::Primary outcome 1.65% vs 2.19% per '
        'year; number needed to treat 61 over a median 3.26 years|Sodium (KDIGO 2021)::Below 2 g of sodium a day (2C)|RASi (KDIGO 2021)::Recommended '
        'for CKD with severely increased albuminuria without diabetes (1B) and for CKD with moderately to severely increased albuminuria with diabetes (1B)}}\n'
        '<p>Most patients with CKD and high blood pressure can be controlled with an accurate measurement, less salt, a RASi where albuminuria '
        'calls for it, and two or three other drugs taken every day. A few have resistant hypertension with a cause you can find, such as primary '
        'aldosteronism, and a few have a hypertensive emergency. Your work is to get the number right, to pick a target and say why, to choose '
        'drugs that protect the kidney, and to remember the heart.</p>\n',
 'case': {'title': 'The tricycle driver with the pounding headache',
          'html': '<p>Thursday, 3 p.m., the internal medicine clinic of a provincial hospital in Tarlac City. Mr. Danilo Ramos, 59, drives a '
                  'tricycle near the public market. He came because of a headache that started this morning. He has had high blood pressure for '
                  '10 years and takes amlodipine &ldquo;when the head is heavy.&rdquo; He does not have diabetes. Lunch today was instant noodles '
                  'and dried fish with rice, eaten with patis; at home his wife cooks with bagoong and soy sauce most days.</p>\n'
                  '<p>The triage nurse took his pressure on arrival, with the cuff over his sleeve, right after he climbed two flights of stairs: '
                  '<strong>168/100 mm Hg</strong>. His creatinine is 2.0 mg/dL, eGFR 36 mL/min/1.73 m&sup2; (it was 44 a year ago), urine '
                  'albumin-to-creatinine ratio (ACR) 120 mg/g, potassium 4.8 mmol/L. He has no chest pain, breathlessness, confusion or visual '
                  'change. His 10-year-old daughter sells kakanin outside the clinic; he cannot afford to lose a day&rsquo;s driving.</p>\n'
                  '<p>The intern asks you whether to give &ldquo;something to bring it down now&rdquo; and which target to write: 140, 130 or '
                  '120.</p>\n',
          'questions': ['Is this reading reliable, and is it an emergency?',
                        'Which target will you set for him, and how will you defend it?',
                        'Which drugs will you suggest to the attending, and what will you monitor?']},
 'sections': [('measure',
               'Measure it right',
               'Measurement: the number every decision rests on',
               '<p>A blood pressure reading is a physical measurement with known sources of error, and almost all of them push the number up. A cuff '
               'that is too small, an unsupported arm, legs crossed, a full bladder, talking, a cigarette or coffee within the half hour, and no '
               'rest after walking in can each add several mm Hg. Together they can add enough to move a patient from controlled to uncontrolled, or '
               'from one drug to three.</p>\n'
               '<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2021 blood pressure guideline made measurement its first chapter because '
               'every large outcome trial behind its targets used a standardized protocol. It recommends standardized office blood pressure '
               'measurement in preference to routine office measurement (1B), and suggests out-of-office measurement, by ambulatory or home '
               'monitoring, as a complement (2B).[[ntr12_1]][[ntr12_2]] The National Kidney Foundation&rsquo;s Kidney Disease Outcomes Quality '
               'Initiative (KDOQI) commentary on the 2025 guideline repeats the same point: decisions made on wrong numbers are wrong decisions.[[ntr12_6]]</p>\n'
               '{{flow:Standardized office measurement|Prepare::No caffeine, smoking or exercise in the 30 minutes before; empty bladder; seated in a quiet '
               'room.|Position::Back supported, feet flat, legs uncrossed, bare upper arm supported at heart level.|Cuff::Bladder sized to the arm; write the '
               'size used.|Rest::Five minutes without talking, by the patient or by you.|Measure::Use a validated device; take two or more readings a minute or '
               'two apart and average them.|Record::Average, arm, cuff size, device, and time since the last medicine dose.}}\n'
               '<div class="table-wrap"><table><thead><tr><th>Source of error</th><th>Why it raises the reading</th><th>What you do</th></tr></thead><tbody>'
               '<tr><td>Cuff too small for a large arm</td><td>More pressure is needed to compress the artery</td><td>Measure arm circumference; use the '
               'larger cuff</td></tr>'
               '<tr><td>Cuff over clothing</td><td>Fabric adds compression and slips</td><td>Bare the arm</td></tr>'
               '<tr><td>No rest after walking or stairs</td><td>Sympathetic activation</td><td>Five minutes seated first</td></tr>'
               '<tr><td>Talking during the reading</td><td>Raises pressure for the duration</td><td>Silence, by both of you</td></tr>'
               '<tr><td>Arm hanging below the heart</td><td>Hydrostatic pressure adds to the reading</td><td>Support the arm at heart level</td></tr>'
               '<tr><td>White-coat effect</td><td>Anxiety in the clinic</td><td>Home or ambulatory readings to compare</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Home readings in the Philippines.</strong> Many families own an automatic upper-arm device bought at a drugstore. Ask them '
               'to bring it to clinic once, check it against your reading, and teach the same preparation at home. A phone photo of each morning and '
               'evening reading for a week is a practical substitute for ambulatory monitoring, which few provinces can offer. Wrist devices and '
               'devices of unknown validation give less reliable readings.</p>\n'
               '<p><strong>When it is an emergency.</strong> Very high pressure alone is hypertensive urgency at most. It becomes an emergency when '
               'an organ is being injured: encephalopathy, acute coronary syndrome, acute heart failure with pulmonary edema, aortic dissection, '
               'eclampsia, or acute kidney injury with a rising creatinine. That patient needs a monitored bed and a titratable intravenous agent. The '
               'patient without organ injury needs an accurate repeat measurement and oral treatment, not a rapid drop that can starve a brain '
               'whose autoregulation has shifted upward.</p>\n'
               '{{key:Never treat a blood pressure you did not measure properly. Repeat it the standardized way before you change a single drug.}}\n'
               '\n{{fig:ntr12_a}}\n'),
              ('targets',
               'Targets',
               'The target: why KDIGO and AHA/ACC say different numbers',
               '<p><strong>What SPRINT showed.</strong> The Systolic Blood Pressure Intervention Trial (SPRINT) randomized 9,361 adults at high '
               'cardiovascular risk but without diabetes to a systolic target below 120 mm Hg or below 140 mm Hg. Mean systolic pressure at 1 year was '
               '121.4 versus 136.2 mm Hg. The trial stopped early at a median 3.26 years because the primary outcome (myocardial infarction, other '
               'acute coronary syndromes, stroke, heart failure or cardiovascular death) occurred at 1.65% versus 2.19% per year (hazard ratio [HR] '
               '0.75), and all-cause death was also lower (HR 0.73).[[ntr12_4]] The authors gave numbers needed to treat of 61 to prevent one primary '
               'outcome event and 90 to prevent one death over the trial period.[[ntr12_4]] Hypotension, syncope, electrolyte abnormalities and acute '
               'kidney injury were more frequent with intensive treatment; injurious falls were not.[[ntr12_4]] Participants needed on average 2.8 '
               'drugs in the intensive arm and 1.8 in the standard arm.[[ntr12_4]]</p>\n'
               '<p><strong>The CKD subgroup.</strong> In the 2,646 participants with an eGFR of 20 to 59 mL/min/1.73 m&sup2;, the primary '
               'cardiovascular outcome hazard ratio was 0.81 (95% confidence interval 0.63 to 1.05), not statistically significant on its own, while '
               'all-cause death was lower (HR 0.72, 0.53 to 0.99); the treatment effect did not differ from participants without CKD. The main kidney '
               'outcome (50% eGFR fall or kidney failure) was not reduced (15 versus 16 events), and after the first 6 months eGFR declined slightly '
               'faster with intensive control (&minus;0.47 versus &minus;0.32 mL/min/1.73 m&sup2; per year).[[ntr12_5]] The benefit, in other words, '
               'was for the heart and for survival, not for the kidney. The eGFR slope is a surrogate; the early dip reflects lower glomerular '
               'pressure, not necessarily injury.</p>\n'
               '<p><strong>Who SPRINT did not enroll.</strong> People with diabetes, heavy proteinuria, polycystic kidney disease, an eGFR below '
               '20 and people in nursing homes were excluded. That matters for the Philippine CKD clinic, where diabetes causes most CKD.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Source</th><th>Target in adults with CKD</th><th>Grade or class</th><th>How BP is to be '
               'measured</th></tr></thead><tbody>'
               '<tr><td>KDIGO 2021</td><td>Systolic &lt;120 mm Hg when tolerated</td><td>2B (weak recommendation, moderate certainty)</td><td>Standardized '
               'office measurement</td></tr>'
               '<tr><td>2025 AHA/ACC</td><td>&lt;130/80 mm Hg for all adults, systolic &lt;120 encouraged</td><td>See guideline for class and level of '
               'evidence</td><td>Proper office technique plus out-of-office readings</td></tr>'
               '<tr><td>KDOQI commentary on AHA/ACC 2025 (October 2026)</td><td>Supports &lt;130/80; individualize, weighing tolerance and limited '
               'evidence in advanced CKD</td><td>Commentary, not a graded guideline</td><td>Stresses accurate technique</td></tr>'
               '<tr><td>SPRINT</td><td>&lt;120 vs &lt;140 systolic</td><td>RCT: 1.65% vs 2.19% per year, NNT 61</td><td>Automated device, mean of three '
               'readings after 5 minutes&rsquo; rest</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Why the numbers differ, honestly.</strong> First, measurement. SPRINT measured with an automated device, averaging three '
               'readings after 5 minutes of quiet rest.[[ntr12_4]] Routine clinic readings taken the way Mr. Ramos&rsquo;s was are usually higher. A '
               'systolic of 120 by the SPRINT method is not the same as 120 by a rushed triage reading, and treating a routine reading to 120 risks '
               'overtreatment. KDIGO tied its target to standardized measurement for exactly that reason, and calls its own recommendation weak '
               '(2B).[[ntr12_1]][[ntr12_2]] Second, population. KDIGO wrote for CKD and leaned on the SPRINT CKD subgroup and related trials; the '
               'AHA/ACC guideline writes for all adults, including people with diabetes, for whom the evidence below 130 is less consistent, and chose '
               'one target that most clinics can measure and reach.[[ntr12_3]] Third, philosophy. KDIGO gives a number to aim at when tolerated; the '
               'AHA/ACC gives a number to reach and encourages going lower. The two agree on far more than they disagree: measure accurately, treat '
               'most adults with CKD to well below 140, and lower further when the patient tolerates it.[[ntr12_3]][[ntr12_6]]</p>\n'
               '<p><strong>What you do at your stage.</strong> The intern measures properly. The resident writes the target the attending chooses, '
               'with its source, and checks for orthostatic symptoms, falls and a rising creatinine. The fellow individualizes: a 59-year-old without '
               'diabetes who tolerates it well may be treated toward below 120 by standardized measurement; an 82-year-old with orthostatic '
               'dizziness and falls, or a patient whose only readings are routine clinic readings, is better served by below 130 and careful '
               'review.</p>\n'
               '{{key:A target means nothing without its measurement method. Write the number and how it was measured: &ldquo;below 120 systolic by '
               'standardized office reading&rdquo; is a plan; &ldquo;below 120&rdquo; alone is a risk.}}\n'
               '\n{{fig:ntr12_b}}\n'),
              ('drugs',
               'Drugs',
               'Drug classes in CKD: protect the glomerulus, then add what works',
               '<p><strong>Renin-angiotensin system inhibitors (RASi).</strong> Angiotensin II constricts the efferent arteriole more than the '
               'afferent. Blocking it with an angiotensin-converting enzyme (ACE) inhibitor or an angiotensin receptor blocker (ARB) lowers '
               'glomerular pressure, lowers albuminuria, and slows progression in albuminuric CKD. KDIGO 2021, and KDIGO 2024 in the same words, '
               'recommends starting a RASi for people with high blood pressure, CKD and severely increased albuminuria (A3) without diabetes (1B); '
               'suggests it for moderately increased albuminuria (A2) without diabetes (2C); and recommends it for moderately to severely increased '
               'albuminuria (A2 and A3) with diabetes (1B).[[ntr12_1]][[ntr12_7]] Both recommend avoiding any combination of an ACE inhibitor, an ARB '
               'and a direct renin inhibitor (1B).[[ntr12_1]][[ntr12_7]] Use the highest approved dose the patient tolerates, from the label and the '
               'attending.</p>\n'
               '<p><strong>The expected creatinine rise.</strong> Because the RASi lowers glomerular pressure, eGFR often falls a little in the first '
               'weeks. KDIGO 2024 advises continuing the ACE inhibitor or ARB unless creatinine rises by more than 30% within 4 weeks of starting or '
               'increasing the dose (practice point).[[ntr12_7]] Check creatinine and potassium within that window. A rise beyond 30% asks for a '
               'cause: volume depletion, a nonsteroidal anti-inflammatory drug (NSAID), renal artery stenosis, or worsening heart failure.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Class</th><th>Mechanism in CKD</th><th>What you watch</th></tr></thead><tbody>'
               '<tr><td>ACE inhibitor or ARB</td><td>Efferent dilation lowers glomerular pressure and albuminuria</td><td>Potassium and creatinine '
               'within 2 to 4 weeks; cough with ACE inhibitors; fetal risk</td></tr>'
               '<tr><td>Dihydropyridine calcium channel blocker</td><td>Arterial vasodilation; no albuminuria benefit alone</td><td>Ankle edema</td></tr>'
               '<tr><td>Thiazide-like diuretic</td><td>Sodium loss lowers volume-driven pressure</td><td>Sodium, potassium, uric acid, glucose</td></tr>'
               '<tr><td>Loop diuretic</td><td>Sodium loss when GFR is low or edema is present</td><td>Volume, potassium</td></tr>'
               '<tr><td>Mineralocorticoid receptor antagonist</td><td>Blocks aldosterone-driven sodium retention</td><td>Potassium closely</td></tr>'
               '<tr><td>Beta-blocker</td><td>For coronary disease, heart failure, rate control</td><td>Heart rate; not first-line for pressure alone</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Thiazides in advanced CKD.</strong> The old teaching that thiazides stop working below an eGFR of 30 was tested. The '
               'Chlorthalidone in Chronic Kidney Disease (CLICK) trial randomized 160 patients with stage 4 CKD (mean eGFR 23) and uncontrolled '
               'hypertension confirmed by 24-hour ambulatory monitoring, most already on loop diuretics and a mean of 3.4 drugs. At 12 weeks, '
               'ambulatory systolic pressure fell by 11.0 mm Hg with chlorthalidone and 0.5 mm Hg with placebo, a difference of 10.5 mm Hg; '
               'albuminuria fell by 50 percentage points more. Hypokalemia, reversible creatinine rises, hyperglycemia, dizziness and hyperuricemia '
               'were more common.[[ntr12_9]] The outcome was blood pressure, a surrogate, over 12 weeks; CLICK did not test kidney failure or '
               'cardiovascular events.</p>\n'
               '<p><strong>Salt.</strong> KDIGO suggests a sodium intake below 2 g a day in people with high blood pressure and CKD (2C), with care in '
               'salt-wasting conditions and with potassium-based salt substitutes in patients at risk of hyperkalemia.[[ntr12_1]] Sodium restriction '
               'potentiates every class above, especially the RASi. The Filipino table is a hard place to start: patis, bagoong, toyo, daing, tuyo, '
               'instant noodles with their seasoning packets, canned meat and chips. Ask what the family actually eats in a day, then change one '
               'thing at a time: less sawsawan, half the noodle seasoning, dried fish once a week instead of daily.</p>\n'
               '<div class="tc-keyp"><span class="tc-lab">In children</span>Blood pressure is classified by percentiles for age, sex and height '
               'until age 13. In children with CKD, KDIGO 2021 suggests lowering 24-hour mean arterial pressure by ambulatory monitoring to the 50th '
               'percentile or below (2C), based largely on the Effect of Strict Blood Pressure Control and ACE Inhibition on the Progression of CRF in '
               'Pediatric Patients (ESCAPE) trial, in which 29.9% of children with intensified control and 41.7% with conventional control reached '
               'a 50% fall in glomerular filtration rate (GFR) or kidney failure over 5 years.[[ntr12_1]][[ntr12_12]] See <a href="attending-pediatric-nephrologist-05-pediatric-hypertension.html">'
               'Attending Pediatric Nephrologist, Module 5</a>.</div>\n'
               '{{key:In albuminuric CKD, the RASi comes first and goes to the highest tolerated dose; check potassium and creatinine within 4 weeks, '
               'and keep going unless creatinine rises more than 30%.}}\n'),
              ('resistant',
               'Resistant hypertension',
               'Resistant hypertension: pseudo-resistance, salt, aldosterone',
               '<p>Resistant hypertension is usually defined as pressure above target despite three drugs of different classes, including a diuretic, '
               'at maximally tolerated doses, or pressure controlled only with four or more. Before you accept the label, rule out the common '
               'impostors. Most &ldquo;resistant&rdquo; patients in a Philippine clinic are not taking all their tablets every day, often because of '
               'cost, or were measured badly, or are eating a great deal of salt.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Step</th><th>What you look for</th><th>Why</th></tr></thead><tbody>'
               '<tr><td>1. Confirm the reading</td><td>Standardized office and home readings</td><td>White-coat effect and poor technique mimic resistance</td></tr>'
               '<tr><td>2. Confirm the tablets</td><td>Pill count, pharmacy receipts, &ldquo;which ones did you skip this week?&rdquo;</td><td>Cost and side '
               'effects drive nonadherence</td></tr>'
               '<tr><td>3. Look for interfering substances</td><td>NSAIDs, decongestants, oral contraceptives, steroids, licorice, stimulants, alcohol</td>'
               '<td>Each raises pressure or blocks drug effects</td></tr>'
               '<tr><td>4. Measure salt</td><td>Diet history; 24-hour urine sodium if available</td><td>Sodium retention is the commonest driver in CKD</td></tr>'
               '<tr><td>5. Screen for causes</td><td>Primary aldosteronism, sleep apnea, renal artery stenosis, CKD progression itself</td><td>Some are '
               'treatable</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Primary aldosteronism.</strong> Autonomous aldosterone production retains sodium, wastes potassium and drives pressure up and '
               'fibrosis forward. It is under-diagnosed because clinicians wait for hypokalemia, which many patients do not have. The 2025 AHA/ACC '
               'guideline recommends screening every adult with resistant hypertension for primary aldosteronism, whether or not potassium is low (Class '
               'of Recommendation 1), and advises continuing most antihypertensive drugs other than mineralocorticoid receptor antagonists while '
               'screening, so that testing is not delayed.[[ntr12_3]] The screen is the aldosterone-to-renin ratio; confirmation and subtype testing '
               'belong to endocrinology and nephrology. In CKD, interpret the ratio with care, because reduced GFR and medicines change both '
               'numbers.</p>\n'
               '<p><strong>The fourth drug.</strong> The PATHWAY-2 crossover trial randomized 335 patients with resistant hypertension on three drugs '
               'to rotate through spironolactone, bisoprolol, doxazosin and placebo. Spironolactone lowered home systolic pressure by 8.70 mm Hg more '
               'than placebo and by 4.26 mm Hg more than the average of the other two drugs; its advantage was largest in patients with low renin. '
               'Serum potassium exceeded 6.0 mmol/L on one occasion in 6 of 285 patients given spironolactone.[[ntr12_8]] The outcome was blood '
               'pressure over 12-week periods, and PATHWAY-2 was not a trial in advanced CKD, where hyperkalemia is more likely; in CKD the fourth '
               'drug is chosen with the attending and with a potassium plan.</p>\n'
               '<p><strong>Renal denervation.</strong> Catheter-based ablation of the renal sympathetic nerves lowers pressure modestly in '
               'sham-controlled trials, and the 2025 AHA/ACC guideline addresses it for selected adults with resistant hypertension.[[ntr12_3]] Evidence '
               'in advanced CKD and evidence on hard outcomes are limited, and the procedure is a specialist referral that few Philippine patients can '
               'reach or afford. Treat it as a question for the attending, not a routine step.</p>\n'
               '{{call:Stop and call the attending nephrologist (per unit protocol, but always ask the attending nephrologist for guidance) when you '
               'find:<ul><li>Very high pressure with headache and confusion, chest pain, breathlessness, visual loss, seizure or a rising creatinine</li>'
               '<li>Creatinine rising more than 30% within 4 weeks of starting or increasing a RASi</li><li>Potassium of 6.0 mmol/L or higher on any '
               'antihypertensive</li><li>Symptomatic hypotension, syncope or a fall after intensifying treatment</li><li>Pressure uncontrolled on four '
               'drugs taken correctly</li></ul>}}\n'
               '{{key:Call hypertension resistant only after you have confirmed the reading, the tablets and the salt; then screen for primary '
               'aldosteronism even when potassium is normal.}}\n'),
              ('cv-risk',
               'Cardiovascular risk',
               'Beyond pressure: statins and cardiovascular risk in CKD',
               '<p>A patient with CKD G3b is, in most cohorts, more likely to have a cardiovascular event than to reach dialysis. The mechanisms add '
               'up: hypertension, diabetes, dyslipidemia, vascular calcification from mineral disorders, anemia, inflammation and left ventricular '
               'hypertrophy. Blood pressure is one lever. Lipids are the next.</p>\n'
               '<p><strong>Statins.</strong> The Study of Heart and Renal Protection (SHARP) randomized 9,270 patients with CKD (3,023 on dialysis) and no '
               'known coronary disease to simvastatin plus ezetimibe, which lowers low-density lipoprotein (LDL) cholesterol, or to placebo; high-density lipoprotein (HDL) cholesterol was not the target. Over a median 4.9 years, major atherosclerotic events occurred in 11.3% '
               'versus 13.4% (rate ratio 0.83), a difference of about 2 per 100 patients; myopathy was rare.[[ntr12_10]] KDIGO 2024 recommends a statin or '
               'statin/ezetimibe combination for adults aged 50 or older with an eGFR below 60 (1A), a statin for adults aged 50 or older with an eGFR of '
               '60 or more (1B), and suggests a statin for adults aged 18 to 49 with coronary disease, diabetes, prior ischemic stroke or a 10-year '
               'risk above 10% (2A).[[ntr12_7]] Statin dose selection in CKD comes from the label and the attending.</p>\n'
               '<p><strong>Risk estimation.</strong> The AHA Predicting Risk of cardiovascular disease EVENTs (PREVENT) equations include eGFR and can add '
               'ACR; they were derived and validated in US adults aged 30 to 79.[[ntr12_11]] The 2025 AHA/ACC guideline uses PREVENT to decide when stage 1 '
               'hypertension needs medicine, but recommends starting medicine at 130/80 or above in adults with CKD, diabetes or cardiovascular disease '
               'regardless of the score (Class of Recommendation 1).[[ntr12_3]] It also recommends a urine ACR for every adult with hypertension, a test '
               'that, the National Kidney Foundation notes, fewer than 1 in 10 patients with hypertension alone receive.[[ntr12_6]] In the '
               'Philippines the ACR is often an out-of-pocket test; it is still the cheapest way to find the patients who need a RASi most.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Lever</th><th>Evidence</th><th>What you do</th></tr></thead><tbody>'
               '<tr><td>Blood pressure</td><td>SPRINT: lower events and death; CKD subgroup consistent for death</td><td>Standardized measurement, '
               'target with its method</td></tr>'
               '<tr><td>Statin</td><td>SHARP: 11.3% vs 13.4% major atherosclerotic events</td><td>Statin per KDIGO 2024 by age and eGFR</td></tr>'
               '<tr><td>Albuminuria</td><td>Marker and driver of risk</td><td>ACR in every hypertensive patient; RASi when indicated</td></tr>'
               '<tr><td>Smoking</td><td>Major modifiable risk</td><td>Ask, advise, refer to cessation support</td></tr>'
               '</tbody></table></div>\n'
               '{{key:In CKD, a blood pressure plan without a statin decision and a urine ACR is half a plan.}}\n')],
 'debrief': ['<p><strong>Reliable, and an emergency?</strong> No to both, for now. The reading was taken over a sleeve, right after stairs, without '
             'rest: every error pushed it up. Repeat it the standardized way: bare arm, correct cuff, 5 minutes seated in silence, two or more readings '
             'averaged. He has no sign of organ injury: no confusion, chest pain, breathlessness or visual change, and his creatinine change is over a '
             'year, not a day. This is not a hypertensive emergency, and a rapid drop could harm him. Start or adjust oral treatment and see him '
             'again soon.</p>\n',
             '<p><strong>The target.</strong> He is 59, without diabetes, with CKD G3b A2: close to the SPRINT CKD population. If his attending '
             'chooses the KDIGO 2021 target, write &ldquo;systolic below 120 mm Hg by standardized office measurement, when tolerated (KDIGO 2021, '
             '2B)&rdquo;; if the AHA/ACC 2025 target, &ldquo;below 130/80, lower if tolerated.&rdquo; Either is defensible; what is not defensible '
             'is treating triage readings to 120. Ask his family to measure at home with a validated device and send phone photos for a week. Check '
             'for dizziness and falls at every visit.</p>\n',
             '<p><strong>Drugs and monitoring.</strong> His ACR of 120 mg/g without diabetes makes a RASi a suggested first step (KDIGO 2C), titrated '
             'to the highest tolerated dose, with potassium and creatinine checked within 2 to 4 weeks and continued unless creatinine rises more than '
             '30%. Amlodipine should be taken daily, not &ldquo;when the head is heavy.&rdquo; Cut sodium below 2 g a day starting with the patis, '
             'noodle seasoning and dried fish. Add a thiazide-like diuretic if needed. He is over 50 with an eGFR below 60, so a statin is '
             'recommended (KDIGO 2024, 1A). Ask about cost early: generic amlodipine and losartan are on the PhilHealth Guaranteed and Accessible Medications for Outpatient Treatment (GAMOT) list, within its annual limit, and a regimen '
             'he can buy every month beats a better one he buys twice a year.[[ntr12_13]]</p>\n'],
 'skills': {'title': 'Blood pressure and cardiovascular kidney care',
            'intro': 'Complete with a preceptor, in clinic or on the ward. Sign-off is local.',
            'items': [('Measures blood pressure by the standardized protocol and records cuff size, arm and conditions', False),
                      ('Distinguishes hypertensive emergency from severe hypertension without organ injury', False),
                      ('States the KDIGO 2021 and 2025 AHA/ACC targets with their grades and explains why they differ', False),
                      ('Starts a RASi plan with the timing of potassium and creatinine checks and the 30% rule', False),
                      ('Works through pseudo-resistance and screens resistant hypertension for primary aldosteronism', False),
                      ('Makes a statin decision by age and eGFR using KDIGO 2024', False)],
            'placement': 'Outpatient clinic, CKD clinic or ward'},
 'quiz': [('An intern is about to take a blood pressure in clinic. Which practice best matches standardized office measurement?',
           ['Measure immediately on arrival so the patient does not wait',
            'Seat the patient with back supported and feet flat, bare arm at heart level, correct cuff, 5 minutes of silent rest, and average two or more readings',
            'Take one reading over the sleeve, then repeat only if high',
            'Use the standing position to reflect daily activity'],
           1,
           'This is the protocol KDIGO 2021 recommends (1B). Measuring on arrival or over clothing adds error, and a single reading is less reliable.'),
          ('A 55-year-old woman without diabetes has CKD G3a with an ACR of 650 mg/g and high blood pressure. Which statement matches KDIGO 2021?',
           ['A RASi is recommended (1B), titrated to the highest tolerated dose',
            'An ACE inhibitor plus an ARB is preferred for more albuminuria reduction',
            'A RASi is only suggested because she has no diabetes (2C)',
            'RASi should wait until the eGFR falls below 30'],
           0,
           'Severely increased albuminuria (A3) without diabetes earns a 1B recommendation. The 2C suggestion applies to A2. Dual blockade should be '
           'avoided (1B).'),
          ('A resident asks why KDIGO 2021 says systolic below 120 mm Hg while the 2025 AHA/ACC guideline says below 130/80. Which explanation is most '
           'accurate?',
           ['KDIGO used different trials that found harm below 130',
            'The AHA/ACC guideline does not use SPRINT',
            'KDIGO ties its weak (2B) target to standardized measurement as used in SPRINT, while AHA/ACC sets one target for all adults, including '
            'people with diabetes, and encourages going lower',
            'The difference is only about diastolic pressure'],
           2,
           'SPRINT-style readings run lower than routine clinic readings, SPRINT excluded diabetes, and the guidelines serve different populations. '
           'Neither guideline found harm at the other&rsquo;s target.'),
          ('Two weeks after starting an ARB, a patient&rsquo;s creatinine rises from 1.8 to 2.1 mg/dL and potassium is 5.1 mmol/L. He feels well. '
           'What is the best response?',
           ['Stop the ARB permanently',
            'Continue the ARB and recheck, because the rise is under 30%',
            'Add a second RASi to strengthen kidney protection',
            'Start dialysis planning'],
           1,
           'A rise of about 17% is within the KDIGO practice point of 30% within 4 weeks, and reflects lower glomerular pressure. Stopping would '
           'remove kidney protection; dual RASi is to be avoided.'),
          ('A 61-year-old man with CKD G3a is on amlodipine, losartan and chlorthalidone at full doses, takes them daily by pill count, and has '
           'standardized office and home readings above target. Potassium is 4.2 mmol/L. What next?',
           ['Screen for primary aldosteronism with an aldosterone-to-renin ratio',
            'Wait for hypokalemia before testing for aldosteronism',
            'Stop all drugs for 6 weeks before any testing',
            'Refer for renal denervation as the next routine step'],
           0,
           'The 2025 AHA/ACC guideline recommends screening adults with resistant hypertension for primary aldosteronism regardless of potassium, '
           'continuing most drugs. Renal denervation is a specialist option with limited CKD evidence.')],
 'terms': [('ACC', 'American College of Cardiology'),
           ('ACE', 'Angiotensin-converting enzyme'),
           ('ACR', 'Albumin-to-creatinine ratio'),
           ('AHA', 'American Heart Association'),
           ('ARB', 'Angiotensin receptor blocker'),
           ('BP', 'Blood pressure'),
           ('CKD', 'Chronic kidney disease'),
           ('CLICK', 'Chlorthalidone in Chronic Kidney Disease (trial)'),
           ('CRF', 'Chronic renal failure'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('ESCAPE', 'Effect of Strict Blood Pressure Control and ACE Inhibition on the Progression of CRF in Pediatric Patients (trial)'),
           ('GAMOT', 'Guaranteed and Accessible Medications for Outpatient Treatment (PhilHealth)'),
           ('GFR', 'Glomerular filtration rate'),
           ('HR', 'Hazard ratio'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('KDOQI', 'Kidney Disease Outcomes Quality Initiative'),
           ('NNT', 'Number needed to treat'),
           ('NSAID', 'Nonsteroidal anti-inflammatory drug'),
           ('PATHWAY-2', 'Spironolactone versus placebo, bisoprolol and doxazosin in drug-resistant hypertension (trial)'),
           ('PREVENT', 'Predicting Risk of cardiovascular disease EVENTs (AHA equations)'),
           ('RASi', 'Renin-angiotensin system inhibitor'),
           ('RCT', 'Randomized controlled trial'),
           ('SHARP', 'Study of Heart and Renal Protection'),
           ('SPRINT', 'Systolic Blood Pressure Intervention Trial')],
 'readings': [('ckd-blood-pressure-target-standardized.html', 'CKD Blood Pressure Target and Standardized Measurement'),
              ('difficult-to-control-hypertension.html', 'Difficult-to-Control Hypertension'),
              ('primary-aldosteronism.html', 'Primary Aldosteronism'),
              ('physician-on-duty-14-high-blood-pressure-breathless-patient.html', 'Physician on Duty, Module 14: High blood pressure and the breathless patient')],
 'calcs': ['calc-bp-map.html', 'calc-prevent-cvd.html', 'calc-aldosterone-renin-ratio.html', 'calc-sodium-intake.html', 'calc-lipid-panel.html']}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
