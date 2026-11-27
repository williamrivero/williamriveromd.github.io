# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 05: Hypertension in children.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. AAP 2017
categories, key action statements and grades checked against the guideline text; ESCAPE against the PubMed abstract;
KDIGO 2021 Recommendation 5.1 (2C) and practice points against the guideline; KDIGO 2024 pediatric targets against
KDIGO's pediatric takeaways. No doses. Fictional case."""

MODULE = {'image_alt': 'A pediatric nephrologist fits an ambulatory blood pressure monitor on a teenage boy&rsquo;s arm while his mother listens.',
 'objectives': ['Classify blood pressure in children and adolescents by the American Academy of Pediatrics (AAP) 2017 categories, and use ambulatory monitoring to confirm hypertension and find white-coat and masked forms.',
                'Look for the secondary cause that fits the child&rsquo;s age, and lower a hypertensive emergency at the speed the guideline describes.',
                'Set and monitor a blood pressure target in a child with chronic kidney disease (CKD), using the ESCAPE trial and the Kidney Disease: Improving Global Outcomes (KDIGO) guidelines with their stated grades.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the hypertension referral and the emergency call</span>You see '
        'two kinds of hypertensive child: the one referred from a school or clinic with a reading nobody trusts, and the one in an emergency '
        'room with a headache and a pressure that frightens everyone. Your duty is to confirm the first properly, and to keep the second from '
        'being harmed by a pressure lowered too fast.</div>\n'
        '{{plain:Think of the brain&rsquo;s blood supply as a house with a pressure regulator on its water main. Within a range, the regulator '
        'keeps the taps steady whatever the street pressure does.}}\n'
        '<p>The picture has a limit. A regulator is fixed; the brain&rsquo;s autoregulation is not. In a child with long-standing high '
        'pressure, the range shifts upward. A pressure that is normal for a healthy child may then be too low for that child&rsquo;s brain, '
        'kidneys and eyes, and lowering it to &ldquo;normal&rdquo; within an hour can cause the ischemia you meant to prevent. In a child whose '
        'pressure rose suddenly, as in acute glomerulonephritis, the regulator has had no time to adapt, and encephalopathy can appear at '
        'pressures that would seem modest in an adult.</p>\n'
        '{{cards:Key numbers|Adolescents 13 and older (AAP 2017)::Stage 1 130/80 to 139/89 mm Hg; stage 2 &ge;140/90 mm Hg|Acute severe '
        'hypertension (AAP 2017)::Lower by no more than 25% of the planned reduction over the first 8 hours (expert opinion, grade D, weak)|'
        'ESCAPE trial, 5 years::Primary end point in 29.9% with intensified control versus 41.7% with conventional control|KDIGO 2021, children '
        'with CKD::24-hour mean arterial pressure (MAP) by ambulatory blood pressure monitoring (ABPM) lowered to &le;50th percentile for age, sex and height (2C)|Share of pediatric hypertension '
        'attributable to CKD (AAP 2017)::Almost 20%}}\n'
        '<p>Most children referred for hypertension have white-coat readings, a wrong cuff, or obesity-related primary hypertension. A few '
        'have a kidney or vascular cause that can be found and sometimes fixed, and a few arrive in crisis. Your work is to confirm before '
        'you label, to look for the cause that fits the age, to lower an emergency slowly and deliberately, and to protect the kidneys of '
        'children with CKD with a target that has trial evidence behind it.</p>\n',
 'case': {'title': 'The headache in the emergency room',
          'html': '<p>Tuesday, 11 p.m., the emergency room of a provincial hospital in Iloilo City. Rafael Aquino, 14 years old and 48 kg, has '
                  'had a headache for three days and vomited twice this evening. He says the lights look blurred. His blood pressure, taken '
                  'twice on the right arm with a correctly sized cuff, is 182/112 and 178/110 mm Hg. He is alert and oriented, with no focal '
                  'deficit. His creatinine is 1.6 mg/dL; his urine shows 2+ protein and no red cell casts.</p>\n'
                  '<p>A bedside ultrasound shows a scarred left kidney of 7.2 cm and a right kidney of 9.4 cm. His mother, Mrs. Nora Aquino, '
                  'recalls &ldquo;fevers with smelly urine&rdquo; when he was a baby that were treated at a health center and never imaged. The '
                  'emergency resident has given an oral antihypertensive and wants &ldquo;120/80 within the hour.&rdquo; Mrs. Aquino says his '
                  'father also has high blood pressure, &ldquo;so it is in the family.&rdquo;</p>\n',
          'questions': ['Is this a hypertensive emergency, and how fast should his pressure come down?',
                        'What is the likely cause, and what will you look for?',
                        'What long-term target will you set, and how will you know he is reaching it?']},
 'sections': [('definitions',
               'Definitions',
               'Defining hypertension in a growing child',
               '<p>Blood pressure rises with age and height, so a single number cannot define hypertension across childhood. The American Academy '
               'of Pediatrics (AAP) 2017 guideline uses percentiles for age, sex and height in children aged 1 to under 13, and fixed cut points '
               'aligned with adult categories from age 13.[[apn05_1]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Category</th><th>Ages 1 to &lt;13 years</th><th>Ages &ge;13 years</th></tr></thead><tbody>'
               '<tr><td>Normal</td><td>&lt;90th percentile</td><td>&lt;120/&lt;80 mm Hg</td></tr>'
               '<tr><td>Elevated</td><td>90th to &lt;95th percentile, or 120/80 to &lt;95th percentile, whichever is lower</td><td>120/&lt;80 to '
               '129/&lt;80 mm Hg</td></tr>'
               '<tr><td>Stage 1 hypertension</td><td>95th percentile to &lt;95th + 12 mm Hg, or 130/80 to 139/89, whichever is lower</td><td>130/80 '
               'to 139/89 mm Hg</td></tr>'
               '<tr><td>Stage 2 hypertension</td><td>&ge;95th percentile + 12 mm Hg, or &ge;140/90, whichever is lower</td><td>&ge;140/90 mm Hg</td></tr>'
               '</tbody></table></div>\n'
               '<p>The guideline puts the prevalence of clinical hypertension in children and adolescents at about 3.5%.[[apn05_1]] Measurement '
               'decides much of that. Use the right arm, a cuff bladder at least 40% of arm circumference in width and 80% to 100% in length, a '
               'seated, rested child, and confirm high oscillometric readings by auscultation.[[apn05_1]] Module 2 covers technique.</p>\n'
               '<p><strong>Ambulatory blood pressure monitoring (ABPM).</strong> A clinic reading is a snapshot taken in a frightening place. The '
               'AAP recommends ABPM to confirm hypertension in children and adolescents whose office readings have been in the elevated category for '
               '1 year or more, or in stage 1 over three clinic visits (grade C, moderate recommendation).[[apn05_1]] For suspected white-coat '
               'hypertension, it recommends ABPM, with the diagnosis confirmed by mean systolic and diastolic pressures below the 95th percentile '
               'and loads below 25% (grade B, strong).[[apn05_1]] ABPM also finds masked hypertension: normal clinic readings with high readings '
               'at home or at night, common in children with CKD, where night-time pressure often fails to dip.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Clinic reading</th><th>ABPM</th><th>What it means</th></tr></thead><tbody>'
               '<tr><td>High</td><td>Normal</td><td>White-coat hypertension: monitor, do not treat on clinic readings</td></tr>'
               '<tr><td>Normal</td><td>High</td><td>Masked hypertension: risk is real, and the clinic misses it</td></tr>'
               '<tr><td>High</td><td>High</td><td>Confirmed hypertension: evaluate and treat</td></tr>'
               '<tr><td>Any</td><td>No nocturnal dip</td><td>Common in CKD; adds to target-organ risk</td></tr>'
               '</tbody></table></div>\n'
               '{{key:Confirm before you label. A child called hypertensive on one reading carries the label, the tests and the medicines for '
               'years.}}\n'),
              ('causes',
               'Causes by age',
               'Finding the cause that fits the age',
               '<p>Secondary hypertension is relatively more common in children than in adults, and renal disease is a more common cause in '
               'younger children, as the AAP guideline notes; almost 20% of pediatric hypertension may be attributable to CKD.[[apn05_1]] The '
               'guideline advises a high index of suspicion for renal and renovascular disease, particularly under age 6, and suggests that '
               'children and adolescents 6 years and older do not need an extensive search for secondary causes if they have a positive family '
               'history of hypertension, are overweight or obese, and have no history or examination findings that suggest a secondary cause '
               '(grade C, moderate).[[apn05_1]] It advises suspecting renovascular hypertension in selected children with stage 2 '
               'hypertension.[[apn05_1]]</p>\n'
               '<p>The mechanisms are worth tracing. A scarred or ischemic kidney releases renin; angiotensin II constricts arterioles and drives '
               'aldosterone, and the pressure rises with a high-renin pattern. A kidney with fewer working nephrons retains sodium and water, and '
               'the pressure rises with volume. A narrowed aorta (coarctation) raises pressure in the arms and lowers it in the legs. Endocrine '
               'tumors add catecholamines, cortisol or mineralocorticoid. Obesity adds sympathetic activity, insulin resistance and sodium '
               'retention.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Age</th><th>Causes to think of first</th><th>Clue at the bedside</th></tr></thead><tbody>'
               '<tr><td>Infant</td><td>Renal artery or venous thrombosis after umbilical catheters, coarctation, CAKUT, bronchopulmonary '
               'dysplasia</td><td>History of umbilical lines; weak femoral pulses; arm-leg pressure gap</td></tr>'
               '<tr><td>Young child</td><td>Renal parenchymal disease (scarring after UTI, glomerulonephritis, CAKUT), renovascular disease, '
               'coarctation</td><td>Past febrile UTIs, abnormal urinalysis, small or asymmetric kidneys, bruit</td></tr>'
               '<tr><td>School age</td><td>Glomerulonephritis, reflux nephropathy, renovascular disease; primary hypertension rising</td><td>Edema, '
               'cola urine, proteinuria; obesity and family history</td></tr>'
               '<tr><td>Adolescent</td><td>Primary hypertension with obesity; still renal disease, drugs (stimulants, steroids, oral contraceptives), '
               'endocrine causes</td><td>Body mass index, sleep apnea symptoms, medication and supplement history</td></tr>'
               '</tbody></table></div>\n'
               '<p>The workup starts with a urinalysis, creatinine, electrolytes and a kidney ultrasound in almost every child, and grows with the '
               'clues. Echocardiography to look for left ventricular hypertrophy is recommended when medication is being considered (grade C, '
               'moderate).[[apn05_1]] A strong family history does not exclude a secondary cause, especially in a child with stage 2 pressures and '
               'abnormal kidneys.</p>\n'
               '{{key:Match the search to the age and the clues. Under 6, or with stage 2 pressure and abnormal kidneys, assume a cause until you '
               'find one or exclude it.}}\n'
               '<div class="tc-scene"><span class="tc-lab">In clinic &middot; fictional</span><p>Bianca, 4, is referred for a pressure of 128/86 '
               'mm Hg found during a cough. Her height is at the 25th percentile. Her mother mentions two hospital admissions for &ldquo;kidney '
               'infection&rdquo; before age 2.</p><p>The pressure is above the 95th percentile on repeat. Her ultrasound shows a small, scarred '
               'right kidney, and you arrange a nuclear scan and an ABPM.</p><p class="tc-scene-take"><b>What this shows.</b> In a young child, '
               'hypertension is a kidney question until proven otherwise.</p></div>\n'
               '\n{{fig:apn05_a}}\n'),
              ('emergency',
               'The emergency',
               'Acute severe hypertension: lower it slowly on purpose',
               '<p>Acute severe hypertension becomes an emergency when organs are being injured: encephalopathy (headache, vomiting, visual change, '
               'confusion, seizures), heart failure, or acute kidney injury. In children, posterior reversible encephalopathy can present with '
               'seizures and cortical blindness, and acute glomerulonephritis can cause encephalopathy at pressures that would seem moderate in an '
               'adult because the rise was sudden.</p>\n'
               '<p>The danger in treatment is speed. In chronic hypertension the autoregulatory range has shifted upward. A fast fall below that '
               'range lowers flow to the brain, retina and kidney. The AAP recommends immediate treatment with short-acting antihypertensive '
               'medication for acute severe hypertension with life-threatening symptoms, reducing the pressure by no more than 25% of the planned '
               'reduction over the first 8 hours (expert opinion, grade D; weak recommendation).[[apn05_1]] The grade tells you this is careful '
               'clinical consensus rather than trial evidence; the physiology behind it is well established.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Phase</th><th>Physiology</th><th>What the attending does</th></tr></thead><tbody>'
               '<tr><td>First minutes</td><td>Organs at risk from the pressure</td><td>Confirm the reading; look for encephalopathy, heart failure, '
               'kidney injury; secure monitoring and intravenous access</td></tr>'
               '<tr><td>First 8 hours</td><td>Autoregulation shifted upward; fast falls cause ischemia</td><td>Titratable intravenous agent per '
               'pediatric formulary in a monitored bed; no more than a quarter of the planned reduction</td></tr>'
               '<tr><td>Next 1&ndash;2 days</td><td>Range begins to readjust</td><td>Continue gradual lowering toward the target; start oral therapy</td></tr>'
               '<tr><td>After</td><td>Cause still present</td><td>Complete the workup; set the long-term target</td></tr>'
               '</tbody></table></div>\n'
               '<p>Choose an agent whose effect can be titrated and stopped, given in a bed with frequent pressure monitoring, ideally a pediatric '
               'intensive care unit. Avoid drugs whose fall in pressure cannot be predicted or reversed. The specific drugs and doses come from '
               'your unit&rsquo;s pediatric formulary. In a volume-overloaded child with glomerulonephritis, removing salt and water may matter '
               'more than any vasodilator.</p>\n'
               '{{call:<ul><li>Blood pressure at stage 2 levels with headache, vomiting, visual change, confusion or seizure</li><li>Signs of heart '
               'failure or pulmonary edema</li><li>Pressure falling faster than the written plan, or new neurological signs during treatment</li>'
               '<li>No monitored bed available for intravenous treatment</li></ul>}}\n'
               '{{key:In a hypertensive emergency, write the target for the first 8 hours as a number, and make it a quarter of the way, not the '
               'whole way.}}\n'),
              ('evidence',
               'Targets and evidence',
               'Targets in children with CKD: ESCAPE and KDIGO',
               '<p><strong>ESCAPE.</strong> The Effect of Strict Blood Pressure Control and ACE Inhibition on the Progression of CRF in Pediatric '
               'Patients (ESCAPE) trial randomized 385 children aged 3 to 18 with an estimated GFR of 15 to 80 mL/min per 1.73 m&sup2;, all '
               'receiving a fixed high dose of an angiotensin-converting enzyme (ACE) inhibitor after a 6-month run-in, to intensified control '
               '(target 24-hour mean arterial pressure [MAP] below the 50th percentile) or conventional control (50th to 95th percentile), with '
               'other antihypertensives added as needed. Over 5 years, 29.9% of the intensified group and 41.7% of the conventional group reached '
               'the primary end point of a 50% fall in GFR or kidney failure (hazard ratio 0.65, 95% confidence interval 0.44 to 0.94). Adverse '
               'events and withdrawals did not differ significantly (28.0% versus 26.5%). Proteinuria fell by about half and then gradually '
               'rebounded despite good pressure control.[[apn05_2]] In absolute terms, about 12 fewer children per 100 reached the end point over '
               '5 years, roughly one for every 8 or 9 treated to the lower target. The end point is a hard kidney outcome, not a surrogate. The '
               'trial was in European and other centers with reliable ABPM; it does not tell you the effect of lowering clinic pressure alone.</p>\n'
               '<p><strong>KDIGO.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2021 blood pressure guideline suggests that in '
               'children with chronic kidney disease (CKD), 24-hour MAP by ABPM be lowered to the 50th percentile or below for age, sex and height '
               '(2C).[[apn05_3]] Its ungraded practice points suggest ABPM once a year and standardized auscultatory office readings every 3 to 6 '
               'months; when ABPM is unavailable, targeting an office systolic pressure below the 90th percentile is a reasonable approach; and an '
               'ACE inhibitor or angiotensin receptor blocker (ARB) is first-line, with attention to hyperkalemia and to fetal risk in adolescents '
               'who could become pregnant.[[apn05_3]] The KDIGO 2024 CKD guideline keeps the 24-hour MAP target below the 50th percentile and, '
               'where ABPM is unavailable, suggests a manually measured systolic pressure at the 50th to 75th percentile.[[apn05_4]][[apn05_5]] '
               'Note the difference between the two office targets: the newer guideline&rsquo;s office target is lower. Both rest on ESCAPE, which '
               'used ambulatory MAP, so the office figures are extrapolations.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Source</th><th>Target</th><th>Grade or status</th></tr></thead><tbody>'
               '<tr><td>AAP 2017, children with hypertension</td><td>&lt;90th percentile and &lt;130/80 mm Hg from age 13</td><td>Grade C, '
               'moderate</td></tr>'
               '<tr><td>KDIGO 2021, children with CKD</td><td>24-hour MAP &le;50th percentile by ABPM</td><td>2C</td></tr>'
               '<tr><td>KDIGO 2021, no ABPM</td><td>Office systolic &lt;90th percentile</td><td>Practice point (ungraded)</td></tr>'
               '<tr><td>KDIGO 2024, no ABPM</td><td>Manual systolic at 50th&ndash;75th percentile</td><td>As stated in KDIGO pediatric summary</td></tr>'
               '<tr><td>ESCAPE</td><td>24-hour MAP &lt;50th percentile</td><td>RCT: 29.9% vs 41.7% reached end point at 5 years</td></tr>'
               '</tbody></table></div>\n'
               '<p>The AAP treatment goal for children with hypertension generally is below the 90th percentile and below 130/80 mm Hg from age 13 '
               '(grade C, moderate).[[apn05_1]] For children with CKD, the lower ambulatory target has the trial behind it.</p>\n'
               '<p>ABPM is not available in every Philippine province. When it is not, measure carefully in clinic, teach home measurement with a '
               'validated device and a correctly sized cuff, and send the child for ABPM at the nearest center at least once a year if the family '
               'can manage the trip.</p>\n'
               '{{key:In a child with CKD, the target is ambulatory: a 24-hour MAP at or below the 50th percentile. Office readings are a '
               'fallback, not the goal.}}\n'
               '\n{{fig:apn05_b}}\n')],
 'debrief': ['<p><strong>Emergency, and how fast.</strong> Yes. Stage 2 pressure with headache, vomiting and blurred vision is acute '
             'severe hypertension with signs of encephalopathy and a kidney that is already impaired. He needs a monitored bed and a titratable '
             'intravenous agent from the pediatric formulary, not a single oral dose and not 120/80 within the hour. His scarred kidney suggests '
             'long-standing hypertension with a shifted autoregulatory range. Plan a reduction of no more than a quarter of the planned fall over '
             'the first 8 hours, then continue gradually over the next one to two days, watching vision and consciousness.</p>\n',
             '<p><strong>The likely cause.</strong> A small, scarred left kidney beside a larger right kidney, with a history of untreated febrile '
             'urinary infections, points to reflux nephropathy with renin-mediated hypertension and CKD. His father&rsquo;s hypertension does not '
             'explain stage 2 pressures and scarred kidneys at 14. Look for proteinuria quantity, electrolytes, a nuclear scan of differential '
             'function, an echocardiogram for left ventricular hypertrophy, and fundoscopy. Consider renovascular disease if the picture does not '
             'fit, as the AAP suggests for selected children with stage 2 hypertension.</p>\n',
             '<p><strong>The long-term target.</strong> He has CKD, so aim for a 24-hour MAP at or below the 50th percentile on ABPM, as ESCAPE '
             'tested and KDIGO 2021 suggests (2C). An ACE inhibitor or ARB is first-line once his potassium and creatinine allow, with monitoring. '
             'Arrange ABPM at least yearly, home readings with a correctly sized cuff in between, and growth, urine protein and kidney function at '
             'each visit. Explain to Mrs. Aquino that lowering his pressure steadily is the best-proven way to protect his remaining kidney.</p>\n'],
 'skills': {'title': 'Hypertension in children',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Classifies blood pressure by AAP 2017 categories for a child under 13 and an adolescent', False),
                      ('Fits and interprets an ABPM, including white-coat, masked and non-dipping patterns', False),
                      ('Writes a first-8-hour plan for acute severe hypertension that limits the fall to a quarter of the planned reduction', False),
                      ('Sets a CKD blood pressure target with its source and grade, and a monitoring schedule', False)],
            'placement': 'Outpatient clinic, emergency department or simulation'},
 'quiz': [('A 15-year-old has repeated office readings of 134/82 mm Hg, confirmed by auscultation. How does AAP 2017 classify this?',
           ['Elevated blood pressure',
            'Stage 1 hypertension',
            'Stage 2 hypertension',
            'Normal for age'],
           1,
           'From age 13, AAP 2017 uses adult-style cut points: 130/80 to 139/89 mm Hg is stage 1.'),
          ('How fast should acute severe hypertension with encephalopathy be lowered, according to AAP 2017?',
           ['To normal within 1 hour',
            'By 50% of the planned reduction in the first hour',
            'Not at all until the cause is known',
            'By no more than 25% of the planned reduction over the first 8 hours'],
           3,
           'Expert opinion (grade D, weak): a shifted autoregulatory range makes fast falls dangerous.'),
          ('What did ESCAPE show?',
           ['Intensified control to a 24-hour MAP below the 50th percentile reduced the 5-year primary end point from 41.7% to 29.9%',
            'Intensified control increased adverse events substantially',
            'No difference in kidney outcomes',
            'Benefit only in children with normal kidney function'],
           0,
           'HR 0.65; about 12 fewer children per 100 reached a 50% GFR fall or kidney failure over 5 years. Withdrawals did not differ.'),
          ('Which child most needs an extensive search for a secondary cause of hypertension?',
           ['An obese 15-year-old with a family history and no other findings',
            'A 16-year-old with white-coat readings normal on ABPM',
            'A 4-year-old with stage 2 hypertension and an asymmetric kidney on ultrasound',
            'A 12-year-old with elevated readings that normalized on repeat'],
           2,
           'Renal and renovascular causes are more common in younger children; stage 2 pressure with abnormal kidneys needs a full workup.'),
          ('KDIGO 2021 suggests which blood pressure target for children with CKD?',
           ['24-hour MAP by ABPM at or below the 50th percentile for age, sex and height (2C)',
            'Office pressure below 140/90 mm Hg',
            'Systolic pressure below 120 mm Hg by office measurement in all children',
            'No specific target in children'],
           0,
           'Recommendation 5.1 (2C), based largely on ESCAPE. When ABPM is unavailable, office targets are ungraded practice points.')],
 'terms': [('AAP', 'American Academy of Pediatrics'),
           ('ABPM', 'Ambulatory blood pressure monitoring'),
           ('ACE', 'Angiotensin-converting enzyme'),
           ('ARB', 'Angiotensin receptor blocker'),
           ('CAKUT', 'Congenital anomalies of the kidney and urinary tract'),
           ('CKD', 'Chronic kidney disease'),
           ('CRF', 'Chronic renal failure'),
           ('ESCAPE', 'Effect of Strict Blood Pressure Control and ACE Inhibition on the Progression of CRF in Pediatric Patients (trial)'),
           ('GFR', 'Glomerular filtration rate'),
           ('HR', 'Hazard ratio'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('MAP', 'Mean arterial pressure'),
           ('RCT', 'Randomized controlled trial'),
           ('UTI', 'Urinary tract infection')],
 'readings': [('managing-hypertension.html', 'Managing High Blood Pressure'),
              ('hypertensive-kidney-disease.html', 'Hypertensive Kidney Disease (Non-Diabetic)'),
              ('ckd-children-young-adults.html', 'CKD in Children & Young Adults')],
 'calcs': ['calc-pediatric-bp.html', 'calc-bp-map.html', 'calc-pediatric-bmi-zscore.html', 'calc-pediatric-egfr.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
