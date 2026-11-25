# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 09: CKD staging, progression and risk reduction.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine private-clinic practice. Grades checked against the KDIGO 2024 CKD guideline summary; trial figures against the
PubMed abstracts (DAPA-CKD, EMPA-KIDNEY, FLOW, CONFIDENCE, Tangri 2016)."""

MODULE = {'image_alt': 'A three-dimensional glomerulus with its incoming and outgoing arterioles.',
 'objectives': ['Classify chronic kidney disease (CKD) by cause, glomerular filtration rate (GFR) and albuminuria (CGA) and estimate '
                'kidney failure risk.',
                'Build layered kidney and cardiovascular protection matched to evidence.',
                'Plan monitoring that is feasible and affordable for the patient.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you discuss and carry out long-term medical planning with the patient '
        '(b9).[[an01_1]] The years before dialysis are where that planning does the most good.</div>\n'
        '{{plain:Picture a small office that loses staff and never hires replacements. The workers who remain take on the extra files and '
        'work overtime. For a while the output holds. Then the overtime starts to break the people doing it, and they leave faster.}}\n'
        '<p>The picture has a limit. Overtime in a nephron is not a matter of effort. It is pressure: the surviving glomeruli filter at a '
        'higher capillary pressure, and that pressure injures the cells that hold the filter together. The leaked albumin then harms the '
        'tubule downstream. And unlike the office, you can lower the load without new staff, by lowering the pressure from both ends of the '
        'glomerulus.</p>\n'
        '{{cards:Key numbers|Kidney Failure Risk Equation (KFRE), 5-year risk 3%&ndash;5%::Can be used to decide nephrology referral '
        '(KDIGO 2024, practice point)|KFRE, 2-year risk &gt;10%::Can be used to time multidisciplinary care (practice point)|KFRE, 2-year '
        'risk &gt;40%::Can be used to time modality education (practice point)|DAPA-CKD::Primary outcome 9.2% vs 14.5% over 2.4 years; '
        'number needed to treat (NNT) 19|FLOW, semaglutide::Major kidney events 18.7% vs 23.2% over 3.4 years}}\n'
        '<p>Most of your patients with CKD are not yet yours alone. They are referred by an internist or an endocrinologist, they pay for '
        'their own laboratory tests and medicines, and they see you in a private clinic every one to three months. Your work in this module '
        'is to give each of them a risk number, a layered plan, and a monitoring schedule they can actually afford, and to put that plan in '
        'writing for the doctor who shares their care.</p>\n',
 'case': {'title': 'The patient who is not on your floor yet',
          'html': '<p>Every Thursday afternoon you hold clinic in a medical arts building near the hospital. Your secretary has already '
                  'taken the vital signs and stacked the laboratory results the patients brought, some on paper and some as photos on '
                  'their phones.</p>\n'
                  '<p>Mrs. Aquino, 62, has type 2 diabetes. Her internist referred her. Her estimated glomerular filtration rate (eGFR) has '
                  'been about 37 for a year, and her urine albumin-to-creatinine ratio is 850 mg/g on losartan 50 mg. Her potassium is '
                  '5.1 mmol/L and her blood pressure is 142/88 mm Hg.</p>\n'
                  '<p>Her cousin is on dialysis, and she asks, &ldquo;Doc, how long before I am in one of those chairs?&rdquo; She tells '
                  'you she can afford laboratory tests only every three months. Your secretary mentions that the pharmacy across the street '
                  'sells a generic sodium-glucose cotransporter 2 (SGLT2) inhibitor.</p>\n',
          'questions': ['How would you answer her question with a number?',
                        'Which treatment would you add first, and why?',
                        'How do you fit a careful plan into one laboratory visit every three months?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Start with the healthy kidney. Each glomerulus holds its capillary pressure in a narrow range. The afferent arteriole '
               'controls what comes in, and the efferent arteriole controls what goes out.</p>\n'
               '<p>As nephrons are lost, the survivors hyperfilter. Angiotensin II constricts the efferent arteriole and raises the pressure '
               'inside the glomerular capillaries. That pressure stretches and injures the podocytes, and albumin leaks into the urine. '
               'Albumin in the tubule is not inert. It triggers inflammation and fibrosis, which destroy more nephrons and load the '
               'survivors further. The cycle feeds itself.</p>\n'
               '<p>Two drug classes break the cycle from opposite ends. Renin-angiotensin system (RAS) blockers dilate the efferent '
               'arteriole and let pressure out. SGLT2 inhibitors block sodium reabsorption in the proximal tubule, so more sodium reaches the '
               'macula densa. The macula densa reads this as volume excess, tubuloglomerular feedback switches back on, and the afferent '
               'arteriole constricts. Less pressure comes in. That is established physiology, and it explains the expected early dip in '
               'eGFR with either drug: the filter pressure falls on purpose.</p>\n'
               '<p>A third pathway runs beside the pressure story. Overactivation of the mineralocorticoid receptor drives inflammation and '
               'fibrosis that persist despite RAS blockade. Nonsteroidal antagonists such as finerenone target it. Glucagon-like peptide-1 '
               '(GLP-1) receptor agonists act through weight, glucose and blood pressure, and are hypothesized to have direct '
               'anti-inflammatory effects in the kidney. Because the pathways are separate, their effects can add.</p>\n'
               '{{key:Name the end of the glomerulus each drug works on. A plan that lowers pressure from both ends and calms the fibrosis '
               'pathway beside it is the plan that protects the nephrons left.}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the clinic &middot; fictional</span><p>Mr. Dela Paz, 58, asks why you are '
               'adding a &ldquo;diabetes tablet&rdquo; when his sugar is controlled. You draw two pipes into a small balloon on the back '
               'of a prescription pad.</p><p>&ldquo;The pipe coming in is the afferent arteriole. Empagliflozin narrows it. The pipe going '
               'out is the efferent arteriole. Your losartan widens it. Both lower the pressure in the balloon, which is the filter. Less '
               'pressure means less damage to the filters you still have.&rdquo;</p><p class="tc-scene-take"><b>What this shows.</b> '
               'Patients stay on protective drugs once they see that the drugs work on pressure, not on sugar.</p></div>\n'
               '\n'
               '{{fig:an09_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Risk first.</strong> KDIGO 2024 recommends an externally validated risk equation to estimate the absolute risk '
               'of kidney failure in CKD G3 to G5 (1A).[[an09_1]] The 4-variable KFRE was tested in 31 cohorts with 721,357 participants '
               'in more than 30 countries. It discriminated well (C statistic 0.90 at 2 years). It overestimated risk in some cohorts '
               'outside North America, and a calibration factor improved those.[[an09_2]] Treat a Filipino patient&rsquo;s KFRE as a '
               'useful estimate that may run high, not as a verdict. The thresholds in the key numbers above are practice points, not '
               'graded recommendations.[[an09_1]]</p>\n'
               '<p><strong>SGLT2 inhibitors.</strong> KDIGO 2024 recommends an SGLT2 inhibitor for adults with type 2 diabetes, CKD and '
               'eGFR &ge;20 (1A), and for adults with CKD and eGFR &ge;20 with a urine albumin-to-creatinine ratio (UACR) &ge;200 mg/g or '
               'heart failure, with or without diabetes (1A). It suggests one for eGFR 20 to 45 with UACR &lt;200 mg/g (2B).[[an09_1]] '
               'DAPA-CKD randomized 4,304 patients with eGFR 25 to 75 and UACR 200 to 5,000 mg/g. Over a median 2.4 years, the primary '
               'kidney and cardiovascular composite occurred in 9.2% on dapagliflozin and 14.5% on placebo (hazard ratio 0.61; NNT 19). '
               'Death from any cause fell from 6.8% to 4.7%.[[an09_4]] EMPA-KIDNEY randomized 6,609 patients, including many without '
               'heavy albuminuria. Over a median 2.0 years, progression or cardiovascular death occurred in 13.1% versus 16.9% (hazard '
               'ratio 0.72), an absolute difference of 3.8 percentage points. All-cause death did not differ significantly.[[an09_5]] '
               'These are outcomes patients feel: dialysis, death, and the loss of half their kidney function.</p>\n'
               '<p><strong>RAS blockade, finerenone and GLP-1 receptor agonists.</strong> KDIGO 2024 recommends a RAS blocker for CKD with '
               'severely increased albuminuria without diabetes (1B) and for CKD with moderately to severely increased albuminuria with '
               'diabetes (1B). It suggests a nonsteroidal mineralocorticoid receptor antagonist for type 2 diabetes with eGFR &gt;25, '
               'normal potassium and albuminuria &gt;30 mg/g despite maximum tolerated RAS blockade (2A). It recommends a long-acting GLP-1 '
               'receptor agonist for adults with type 2 diabetes and CKD who have not reached their glycemic target (1B).[[an09_1]] FLOW '
               'randomized 3,533 such patients to semaglutide or placebo. Over a median 3.4 years, major kidney events occurred in 18.7% '
               'versus 23.2% (hazard ratio 0.76), and cardiovascular death was also lower (hazard ratio 0.71).[[an09_6]]</p>\n'
               '<p><strong>Starting two drugs at once.</strong> CONFIDENCE randomized about 800 patients with type 2 diabetes and '
               'albuminuric CKD to finerenone, empagliflozin, or both. At 180 days, UACR fell 29% more with the combination than with '
               'finerenone alone and 32% more than with empagliflozin alone.[[an09_7]] UACR is a surrogate. The trial does not show that '
               'starting both together prevents dialysis or death, and hard-outcome data for the combination are still pending.</p>\n'
               '<p><strong>Blood pressure.</strong> KDIGO 2024 suggests a systolic target below 120 mm Hg when tolerated, measured by '
               'standardized office technique (2B).[[an09_1]] The grade is weak, and few Philippine clinics measure pressure the way the '
               'trials did. Use the target as a direction, not a reflex.</p>\n'
               '{{key:Quote the absolute numbers, not only the hazard ratios. A patient at high baseline risk, like one with heavy '
               'albuminuria, gains more from the same relative effect.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Classify, then put a number on it.</strong> Confirm chronicity with results more than 3 months apart. The old '
               'results your patient brings in an envelope often settle this. Stage by cause, eGFR and albuminuria. Use the race-free '
               'CKD-EPI 2021 equation.[[an09_3]] Cystatin C sharpens the estimate when creatinine misleads, as in sarcopenia or amputation; '
               'KDIGO 2024 recommends the combined equation when cystatin C is available (1B),[[an09_1]] but many Philippine laboratories '
               'do not run it and the patient pays for it. Order it when the answer will change a decision. Calculate the KFRE in G3 to G5 '
               'and tell the patient the number.</p>\n'
               '<p><strong>Build the plan in layers.</strong> Raise the RAS blocker to the maximum dose the pressure and potassium allow. Add '
               'an SGLT2 inhibitor. Add finerenone where the patient qualifies and can afford it. Discuss a GLP-1 receptor agonist in type 2 '
               'diabetes when glucose is above target, knowing it is the most expensive layer. Add a statin for adults aged 50 or older with '
               'eGFR below 60 (1A),[[an09_1]] stop smoking, update vaccines, and refer to a dietitian.</p>\n'
               '<p><strong>Fit it to Philippine practice.</strong> Most patients pay out of pocket, so cost decides adherence. Check the PSN guideline and protocol page for local guidance,[[an09_8]] and choose '
               'registered generics where they exist. Change one drug at a time, and time each change so that a routine laboratory visit '
               'falls 2 to 4 weeks later; KDIGO 2024 advises checking pressure, creatinine and potassium within that window after starting '
               'a RAS blocker (practice point).[[an09_1]] When UACR is not affordable at every visit, agree on a schedule: UACR at '
               'baseline and after each major change, creatinine and potassium more often. Results will reach you as photos on Viber '
               'between visits. Agree in advance which results the patient sends you, and which values make your secretary call you the same '
               'day.</p>\n'
               '<p><strong>Share the plan in writing.</strong> The referring internist will see the patient between your visits and may '
               'renew the prescriptions. Write a short letter with the CKD stage, the KFRE, each drug with its reason, the next laboratory '
               'date, and the values that should prompt a call to you. A plan in your head stops at the clinic door.</p>\n'
               '\n'
               '{{fig:an09_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the clinic, the same patient a month later &middot; fictional</span><p>Mr. '
               'Dela Paz returns worried. His creatinine rose from 2.0 to 2.3 mg/dL after empagliflozin. His daughter, a nurse abroad, '
               'messaged him to stop it.</p><p>You explain that a small early fall in filtration is expected, because the drug lowers the '
               'pressure inside the filters, and that it usually steadies. KDIGO 2024 states that this reversible dip is generally not a '
               'reason to stop.[[an09_1]] You keep the drug, check again in four weeks, and write a short note he can forward to his '
               'daughter.</p><p class="tc-scene-take"><b>What this shows.</b> An expected change is not a side effect. Stopping '
               'protection because of it takes away the benefit, and the family needs the reason as much as the patient does.</p></div>\n'
               '{{key:A plan is only as good as the schedule the patient can pay for. Agree on it out loud, then write it to the patient '
               'and to the referring doctor.}}\n'
               '{{call:<ul><li>eGFR decline &gt;5 mL/min/1.73 m² per year</li><li>UACR rising despite therapy</li><li>Potassium &gt;5.5 '
               'mmol/L after starting a RAS blocker or finerenone</li><li>Creatinine rise &gt;30% within 4 weeks of starting RAS '
               'blockade (look for renovascular disease or volume depletion)</li></ul>}}\n')],
 'debrief': ['<p><strong>Her question.</strong> She is CKD G3b A3, a very high-risk group. Calculate her Kidney Failure Risk Equation '
             '(KFRE) result and give it to her as a number she can picture: how many of 100 women like her would need dialysis or a '
             'transplant within two and five years. Tell her it is an estimate and may run a little high. A number she can see is the '
             'strongest reason she has to stay on treatment, and it tells you when to start preparing her.</p>\n'
             '<p><strong>What first.</strong> Add an SGLT2 inhibitor now. It lowers the pressure inside each glomerulus from the afferent '
             'side, which is why it protects the nephrons still working. In DAPA-CKD, 19 patients treated for about two and a half years '
             'prevented one major kidney or cardiovascular event. Her own absolute benefit should be larger than average, because her '
             'albuminuria puts her at high baseline risk. The generic is a good choice if it is registered and affordable. Raise losartan '
             'if her pressure allows. Add finerenone once her potassium is normal and she can afford it. If her glucose is above target, a '
             'GLP-1 receptor agonist is worth discussing; in FLOW, semaglutide lowered major kidney events from 23.2% to 18.7%.</p>\n'
             '<p><strong>Fitting it to her budget.</strong> Change one thing at a time. Time each change so her next routine laboratory '
             'visit falls two to four weeks later, or arrange one extra potassium test after finerenone starts. Ask her to send you the '
             'potassium result on Viber the day it comes out. Write the plan in a letter to her internist. The goal of this clinic is that '
             'she reaches the dialysis unit as late as possible, and, if she does, with a fistula and a transplant referral already in '
             'place.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Documents CGA classification and KFRE', False),
                      ('Reviews eligibility for each pillar with reasons', False),
                      ('Assigns affordable follow-up monitoring', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which measure adds important prognostic information to eGFR?',
           ['Serum sodium alone', 'Urine albumin-to-creatinine ratio', 'A single office pulse', 'Serum uric acid alone'],
           1,
           'Albuminuria carries prognostic information independent of eGFR and changes which treatments apply.'),
          ('Which finding helps establish CKD chronicity?',
           ['Persistent abnormalities documented over more than 3 months',
            'A single low eGFR during shock',
            'An isolated elevated potassium',
            'One positive urine dipstick'],
           0,
           'Serial results more than 3 months apart separate chronic disease from an acute change. Old results the patient brings often '
           'settle it.'),
          ('How do SGLT2 inhibitors lower intraglomerular pressure?',
           ['By increasing renin release',
            'By dilating the afferent arteriole',
            'By blocking aldosterone synthesis',
            'By restoring macula densa sodium delivery, activating tubuloglomerular feedback and constricting the afferent arteriole'],
           3,
           'Feedback-mediated afferent constriction complements the efferent dilation from RAS blockade.'),
          ('What did CONFIDENCE demonstrate?',
           ['Fewer dialysis starts at 5 years',
            'Lower mortality with the combination',
            'Greater UACR reduction with combined finerenone and empagliflozin than either alone (a surrogate outcome)',
            'No added effect from combination'],
           2,
           'The trial measured albuminuria change at 180 days. It does not show fewer dialysis starts or deaths.'),
          ('In KDIGO 2024, a KFRE 2-year risk above 40% can be used to:',
           ['Discharge the patient to primary care',
            'Time education about kidney replacement therapy options, with access and transplant planning',
            'Repeat the KFRE in 5 years',
            'Stop all kidney-protective drugs'],
           1,
           'Practice Point 2.2.3 uses a 2-year risk above 40% to time modality education. It is a practice point, not a graded '
           'recommendation.')],
 'terms': [('CKD', 'Chronic kidney disease'),
           ('SGLT2', 'Sodium-glucose cotransporter 2'),
           ('ACE', 'Angiotensin-converting enzyme'),
           ('ARB', 'Angiotensin receptor blocker'),
           ('GLP-1', 'Glucagon-like peptide-1'),
           ('HR', 'Hazard ratio'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('KFRE', 'Kidney Failure Risk Equation'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('UACR', 'Urine albumin-to-creatinine ratio'),
           ('KRT', 'Kidney replacement therapy'),
           ('RAS', 'Renin-angiotensin system'),
           ('GLP-1 RA', 'Glucagon-like peptide-1 receptor agonist'),
           ('NNT', 'Number needed to treat'),
           ('CV', 'Cardiovascular'),
           ('BP', 'Blood pressure')],
 'readings': [('slowing-ckd-progression.html', 'Slowing CKD Progression'),
              ('new-therapeutic-agents-ckd.html', 'New Therapeutic Agents for CKD')],
 'calcs': ['calc-egfr-ckd-epi.html',
           'calc-kfre.html',
           'calc-proteinuria-uacr.html',
           'calc-uacr-trend.html',
           'calc-ckd-progression-slope.html',
           'calc-sglt2i-eligibility.html',
           'calc-prevent-cvd.html',
           'calc-ckm-staging.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
