# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 06: CAKUT, antenatal urinary tract dilation and posterior urethral valves.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. UTD thresholds
checked against published reproductions of the 2014 consensus tables; registry, nadir creatinine and valve-bladder figures
against PubMed abstracts. No doses or fluid orders. Fictional case."""

MODULE = {'image_alt': 'A pediatric nephrologist examines a newborn boy in a provincial hospital nursery while his parents watch and a nurse holds an ultrasound printout.',
 'objectives': ['Explain how congenital anomalies of the kidney and urinary tract (CAKUT) reduce nephron number and tubular function, and where they rank among causes of kidney failure in children.',
                'Classify antenatal and postnatal urinary tract dilation (UTD) with the 2014 consensus system and time the postnatal ultrasound correctly.',
                'Manage the first year of a boy with posterior urethral valves: relieve obstruction, track nadir creatinine, replace salt and water losses, and protect the bladder.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the first year of a child born with a structural kidney problem</span>'
        'These children are found on an antenatal scan, on a newborn examination or after a first urinary infection, often in a provincial '
        'hospital far from a pediatric urologist. You coordinate the urologist, the neonatologist, the family and the local pediatrician, and '
        'you own the kidney function, the salt and water, the growth and the long-term plan.</div>\n'
        '{{plain:Think of CAKUT as a house whose plumbing was installed wrong while the house was still being built. Water backs up, pipes '
        'swell, and the rooms nearest the blockage are damaged.}}\n'
        '<p>The picture has a limit. In a house you fix the pipe and the rooms are as good as before. In the kidney the blockage was present '
        'while nephrons were forming. Many never formed properly (dysplasia), and relieving the obstruction cannot create them. The tubules '
        'that did form may not concentrate urine or keep salt. So the child who leaves the operating room with an open urethra still has '
        'fewer nephrons, a kidney that wastes water and sodium, and often a bladder changed by months of high pressure.</p>\n'
        '{{cards:Key numbers|Antenatal urinary tract dilation::Seen on ultrasound in 1&ndash;2% of fetuses|Postnatal UTD P1::Anterior-posterior '
        'renal pelvic diameter 10 to &lt;15 mm, on an ultrasound done more than 48 hours after birth|Postnatal UTD P2::Pelvic diameter &ge;15 '
        'mm or peripheral calyceal dilation|Valves meta-analysis (1,731 boys, mean 5.5 years)::CKD in 37.9% and kidney failure in 13.6%|Nadir '
        'creatinine cut-off most often used::1 mg/dL (88.4 &micro;mol/L) in the first year}}\n'
        '<p>Most antenatal dilation resolves or stays mild and needs little more than a well-timed scan. A few infants have obstruction or '
        'dysplasia that will shape their whole childhood, and posterior urethral valves are the most serious of these in boys. Your work is to '
        'sort the two quickly, relieve obstruction, measure the kidney the boy has left, and plan the year of salt, water, infection and '
        'bladder care that follows.</p>\n',
 'case': {'title': 'The full bladder in the provincial nursery',
          'html': '<p>Thursday, 2 p.m. A pediatrician in Tuguegarao, Cagayan, sends you a Viber message with photos. Gabriel Garcia was born '
                  'yesterday at 37 weeks, weighing 2.8 kg. An antenatal scan at 32 weeks showed bilateral hydronephrosis and reduced amniotic '
                  'fluid. This morning he has a palpable bladder and dribbles urine. His creatinine at 20 hours is 1.0 mg/dL; sodium 133 '
                  'mmol/L; potassium 5.6 mmol/L. An ultrasound done at 12 hours of life was read as &ldquo;mild pelvic fullness.&rdquo;</p>\n'
                  '<p>The nearest pediatric urologist is in Manila, about ten hours by road. His father, Mr. Ramil Garcia, a rice farmer, asks '
                  'whether the operation can wait until Gabriel is bigger, because he cannot leave the harvest. The pediatrician asks whether a '
                  'feeding tube can be passed as a bladder catheter tonight, and whether the creatinine of 1.0 means the kidneys have already '
                  'failed.</p>\n',
          'questions': ['What is the likely diagnosis, and what must happen in the first 24 hours?',
                        'What does a creatinine of 1.0 mg/dL on day 1 mean, and what will tell you Gabriel&rsquo;s prognosis?',
                        'What will his first year look like, and what will you ask his parents and pediatrician to watch?']},
 'sections': [('physiology',
               'Physiology',
               'Why structural anomalies cost nephrons and tubules',
               '<p>The kidney and urinary tract form together from the ureteric bud and the metanephric mesenchyme. When the bud branches poorly, or '
               'when urine cannot drain during development, fewer nephrons form and those that do may be disorganized. The result ranges from a '
               'small, otherwise normal kidney to cystic dysplasia. An obstruction that persists through the second and third trimesters adds '
               'back-pressure, inflammation and fibrosis.</p>\n'
               '<p>Two consequences follow. First, fewer nephrons each filter more, and over years that hyperfiltration can injure the glomeruli '
               'that remain. Second, the dysplastic medulla concentrates poorly and the tubules lose sodium. A boy with valves may pass large '
               'volumes of dilute urine, become dehydrated quickly with diarrhea, and grow poorly if salt and water are not replaced.</p>\n'
               '<p>CAKUT matter in every region. A 2026 global registry analysis of 23,620 children starting maintenance kidney replacement '
               'therapy (KRT) in 80 countries found that CAKUT and hereditary nephropathies were the predominant causes in younger children, while '
               'adolescents more often had immune-mediated glomerular disease; immune-mediated glomerulopathies were the most common cause in '
               'Southeast Asia and accounted for 43% of diagnoses in low-income countries.[[apn06_2]] So in a Philippine unit, the infant and '
               'toddler starting dialysis is likely to have CAKUT, while the teenager is more likely to have glomerular disease. A review notes '
               'that about 35% of children with CKD who require KRT have a significant urological abnormality, including valves, neuropathic '
               'bladder and severe reflux.[[apn06_7]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>What developed abnormally</th><th>Physiological consequence</th><th>What you see</th></tr></thead><tbody>'
               '<tr><td>Fewer nephrons (hypoplasia, dysplasia)</td><td>Lower GFR; hyperfiltration of survivors</td><td>Raised nadir creatinine; '
               'proteinuria and hypertension later</td></tr>'
               '<tr><td>Dysplastic medulla and tubules</td><td>Poor concentration; sodium wasting</td><td>Polyuria, thirst, dehydration with '
               'minor illness, low sodium, poor growth</td></tr>'
               '<tr><td>Obstructed outflow (valves)</td><td>High bladder and upper-tract pressure</td><td>Hydronephrosis, thick-walled bladder, '
               'poor stream, urinary infection</td></tr>'
               '<tr><td>Reflux</td><td>Infected urine reaches the kidney</td><td>Febrile urinary tract infection (UTI), scarring (Module 7)</td></tr>'
               '</tbody></table></div>\n'
               '{{key:Relieving obstruction stops further damage. It does not restore nephrons that never formed, so measure what is left.}}\n'),
              ('utd',
               'Urinary tract dilation',
               'Antenatal and postnatal urinary tract dilation',
               '<p>Urinary tract dilation is seen on ultrasound in 1&ndash;2% of fetuses and covers a spectrum from transient pelvic fullness to '
               'severe obstruction. A 2014 consensus of eight radiology, urology, nephrology and maternal-fetal societies proposed one '
               'classification for before and after birth, built on six ultrasound findings: anterior-posterior renal pelvic diameter (APRPD), '
               'calyceal dilation, parenchymal thickness, parenchymal appearance, bladder abnormalities and ureteral abnormalities.[[apn06_1]] '
               'The authors were explicit that the system correlates with the risk of postnatal uropathy and still needs evaluation against '
               'outcomes such as surgery or kidney function.[[apn06_1]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Category</th><th>Criteria</th><th>Meaning</th></tr></thead><tbody>'
               '<tr><td>Antenatal normal</td><td>APRPD &lt;4 mm at 16&ndash;27 weeks; &lt;7 mm at &ge;28 weeks</td><td>No follow-up for '
               'dilation</td></tr>'
               '<tr><td>UTD A1 (low risk)</td><td>APRPD 4 to &lt;7 mm at 16&ndash;27 weeks, or 7 to &lt;10 mm at &ge;28 weeks; at most central '
               'calyceal dilation; otherwise normal</td><td>Postnatal scan</td></tr>'
               '<tr><td>UTD A2&ndash;3 (increased risk)</td><td>APRPD &ge;7 mm at 16&ndash;27 weeks or &ge;10 mm at &ge;28 weeks, or peripheral '
               'calyceal dilation, abnormal parenchyma, dilated ureter, abnormal bladder or unexplained oligohydramnios</td><td>Closer antenatal '
               'and early postnatal evaluation</td></tr>'
               '<tr><td>Postnatal normal</td><td>APRPD &lt;10 mm, no other findings</td><td>&mdash;</td></tr>'
               '<tr><td>UTD P1 (low risk)</td><td>APRPD 10 to &lt;15 mm or central calyceal dilation</td><td>Follow-up ultrasound</td></tr>'
               '<tr><td>UTD P2 (intermediate)</td><td>APRPD &ge;15 mm or peripheral calyceal dilation</td><td>Closer follow-up; consider further '
               'imaging</td></tr>'
               '<tr><td>UTD P3 (high risk)</td><td>Any APRPD with abnormal parenchyma, dilated ureter or bladder abnormality</td><td>Early '
               'specialist evaluation</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Timing.</strong> The postnatal categories assume an ultrasound done more than 48 hours after birth.[[apn06_1]] In the '
               'first two days a newborn is relatively oliguric, and a scan can underestimate dilation; a &ldquo;mild&rdquo; scan at 12 hours does '
               'not exclude obstruction. The exception is the baby whose findings demand action now: a boy with bilateral hydronephrosis, a '
               'thick-walled or distended bladder, or oligohydramnios, who needs an early scan and catheter drainage rather than a wait.</p>\n'
               '<p><strong>When does CKD start?</strong> Chronic kidney disease (CKD) is usually defined by abnormalities present for more than 3 '
               'months. The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline makes an exception for newborns with clear kidney '
               'disease, who do not need to wait 3 months to be recognized as having CKD.[[apn06_3]] An infant with dysplastic kidneys and valves '
               'should enter CKD care from the start.</p>\n'
               '{{key:A postnatal scan before 48 hours can be falsely reassuring. Time the routine scan after 48 hours, but never let the clock '
               'delay a boy with a full bladder.}}\n'
               '\n{{fig:apn06_a}}\n'),
              ('valves',
               'Posterior urethral valves',
               'Posterior urethral valves and the nadir creatinine',
               '<p>Posterior urethral valves are folds of tissue in the posterior urethra that obstruct outflow in boys. The bladder works against '
               'them from fetal life, hypertrophies, and transmits pressure to the ureters and kidneys. After birth the infant may have a palpable '
               'bladder, a poor stream, urinary infection, or respiratory problems from lung hypoplasia when amniotic fluid was low.</p>\n'
               '<p><strong>Fetal intervention.</strong> A 2016 review concluded that prenatal intervention probably reduces perinatal mortality by '
               'relieving oligohydramnios during lung development between 16 and 28 weeks, but has not improved postnatal kidney outcome, and that '
               'the proportion of boys with valves who progress to chronic and end-stage kidney disease has not changed in 25 years.[[apn06_8]]</p>\n'
               '<p><strong>Nadir creatinine.</strong> The lowest creatinine in the first year after relief of obstruction is the most consistent '
               'predictor of long-term kidney function. In one series of 96 boys treated by endoscopic ablation and followed for a median 9.4 '
               'years, 29 (30.2%) developed chronic renal insufficiency and 9 (9.4%) reached kidney failure. All 10 boys with a nadir above 88.4 '
               '&micro;mol/L (1 mg/dL), and all 14 above 75 &micro;mol/L, developed renal insufficiency, compared with 2 of 36 (5.6%) below 35 '
               '&micro;mol/L.[[apn06_4]] In a second series of 104 boys, nadir creatinine was the only independent predictor of final kidney '
               'function on multivariable analysis.[[apn06_5]] A meta-analysis of 13 studies and 1,731 boys, mean follow-up 5.5 years, found CKD in '
               '37.9% and kidney failure in 13.6%; most studies used a 1 mg/dL cut-off, and the relative risk of CKD above the cut-off was 7.69, '
               'with marked heterogeneity between studies.[[apn06_6]] These are retrospective cohorts. They show prognosis, not the effect of any '
               'treatment, and the cut-offs differ between centers and creatinine assays.</p>\n'
               '<p><strong>Polyuria and the valve bladder.</strong> Many boys with valves pass large volumes of dilute urine. A full, poorly '
               'emptying bladder then stays overdistended, the condition called valve bladder. A sustained bladder pressure above 40 cm H&#8322;O '
               'impedes drainage from the upper tracts, and overnight continuous bladder drainage has been reported to reduce hydronephrosis and '
               'stabilize or improve kidney function in most cases.[[apn06_7]] In a series of 297 boys from a tertiary center in India, 12.8% '
               'progressed to kidney failure; severe bladder dysfunction, recurrent febrile infection, polyuria and polydipsia were independent '
               'predictors on multivariable analysis.[[apn06_9]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Marker</th><th>What the evidence shows</th><th>Caveat</th></tr></thead><tbody>'
               '<tr><td>Nadir creatinine &gt;1 mg/dL in year 1</td><td>Strongly predicts CKD and kidney failure</td><td>Retrospective; '
               'thresholds vary; lower cut-offs may be more sensitive</td></tr>'
               '<tr><td>Polyuria, polydipsia</td><td>Independent predictors of kidney failure in one large series</td><td>Single center; reflect '
               'tubular damage</td></tr>'
               '<tr><td>Bladder dysfunction, high pressures</td><td>Impede upper-tract drainage; predict progression</td><td>Requires urodynamic '
               'assessment</td></tr>'
               '<tr><td>Recurrent febrile UTI</td><td>Associated with progression</td><td>Confounded by bladder dysfunction</td></tr>'
               '</tbody></table></div>\n'
               '{{key:The nadir creatinine of the first year is the boy&rsquo;s prognosis. Record it, explain it to the family, and plan around '
               'it.}}\n'),
              ('practice',
               'Practice',
               'The first year: what the attending does',
               '<p><strong>The first 24 hours.</strong> A boy with suspected valves needs bladder drainage now, with a urethral catheter of suitable '
               'size placed by someone experienced, and a plan for valve ablation by a pediatric urologist. A feeding tube is sometimes used as a '
               'temporary catheter in small infants when nothing else fits; agree on it with the urologist by phone and secure it well. Watch for '
               'a post-obstructive diuresis once drainage starts: urine output can rise sharply, and sodium, potassium and bicarbonate can swing. '
               'Measure intake, output, weight and electrolytes often in the first days.</p>\n'
               '<p><strong>Transfer.</strong> A palpable bladder, bilateral hydronephrosis and a rising creatinine need a center with pediatric '
               'urology and neonatal care. The ten-hour road trip is safer with the bladder drained, electrolytes checked, and a written endorsement '
               'naming the accepting doctor.</p>\n'
               '<p><strong>Salt, water and growth.</strong> Polyuric infants need free access to water and feeds, and many need sodium '
               'supplementation, set by weight and serum and urine sodium according to the unit&rsquo;s protocol. Teach parents that vomiting or '
               'diarrhea is an emergency for this child, because he cannot concentrate his urine to compensate. Plot growth monthly in the first '
               'year.</p>\n'
               '<p><strong>Infection and bladder.</strong> Treat febrile illness as a possible urinary infection until a properly collected urine '
               'says otherwise (Module 7). Arrange regular urology review with assessment of bladder emptying and pressures, and timed or overnight '
               'drainage when the urologist advises it.</p>\n'
               '<p><strong>Solitary or single functioning kidney.</strong> A child with one working kidney, from agenesis, multicystic dysplasia or '
               'a destroyed kidney, carries the hyperfiltration risk above. Follow blood pressure, urine protein and kidney function periodically '
               'throughout childhood, and teach the family why.</p>\n'
               '{{flow:A boy with suspected valves|Drain::Urethral catheter now; record output hourly.|Measure::Creatinine, sodium, potassium, '
               'bicarbonate, weight, daily at first.|Image::Ultrasound with bladder view; voiding study as the urologist plans.|Relieve::Valve '
               'ablation or temporary diversion by a pediatric urologist.|Track::Creatinine monthly in year 1 to find the nadir.|Protect::Salt and '
               'water, infection plan, bladder care, growth, blood pressure.}}\n'
               '{{call:<ul><li>A newborn boy with bilateral hydronephrosis and a distended bladder or poor stream</li><li>Urine output above or '
               'below the planned range after catheter drainage, or sodium or potassium moving quickly</li><li>Fever in an infant with valves or '
               'reflux</li><li>Vomiting or diarrhea in a polyuric infant</li><li>Nadir creatinine above 1 mg/dL: start CKD and KRT planning '
               '(Modules 17 and 19)</li></ul>}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the six-month visit &middot; fictional</span><p>Enzo, 6 months, had valve ablation '
               'at 2 weeks. His creatinine fell to 0.5 mg/dL by month 3 and has stayed there. His mother says he soaks a diaper every hour and '
               'drinks constantly. He has dropped from the 25th to the 10th percentile for weight.</p><p>You check his sodium and bicarbonate, '
               'review salt supplementation with the dietitian, and ask the urologist about bladder emptying.</p><p class="tc-scene-take"><b>What '
               'this shows.</b> A reassuring nadir does not mean the tubules are normal. Growth tells you whether salt and water are '
               'enough.</p></div>\n'
               '{{key:In the first year, the attending owns four lines on the chart: the creatinine trend, the sodium, the weight and the urine '
               'cultures.}}\n'
               '\n{{fig:apn06_b}}\n')],
 'debrief': ['<p><strong>Diagnosis and the first 24 hours.</strong> Bilateral hydronephrosis, reduced amniotic fluid, a palpable bladder '
             'and dribbling in a newborn boy point to posterior urethral valves. Ask the pediatrician to drain the bladder tonight with the '
             'most suitable catheter available, a fine feeding tube if nothing else fits, agreed with the pediatric urologist by phone. Measure '
             'urine output hourly, and repeat electrolytes and creatinine within 12&ndash;24 hours, watching for a post-obstructive diuresis. '
             'Arrange transfer to a center with pediatric urology. The operation cannot wait until he is bigger; drainage now and ablation soon '
             'protect what kidney he has. Talk with Mr. Garcia about the harvest honestly and help the family plan who travels.</p>\n',
             '<p><strong>What the creatinine means.</strong> On day 1 a newborn&rsquo;s creatinine largely reflects his mother&rsquo;s, so 1.0 '
             'mg/dL does not yet tell you his own kidney function, and it does not mean his kidneys have failed. A rising value over the next '
             'days would be more worrying. His prognosis will come from the nadir creatinine over the first year after the obstruction is '
             'relieved: values above about 1 mg/dL are strongly associated with later CKD and kidney failure, while low nadirs carry a much '
             'smaller risk. Tell the pediatrician that the 12-hour scan was too early to grade the dilation.</p>\n',
             '<p><strong>The first year.</strong> Expect a boy who may pass large amounts of dilute urine, lose salt and dehydrate quickly. Ask '
             'the parents to watch feeding, wet diapers, vomiting and diarrhea, and fever, and to come in early. Ask the pediatrician to plot '
             'growth monthly, check electrolytes and creatinine on the schedule you set, treat fever as a possible urinary infection with a '
             'proper urine sample, and keep the urology appointments for bladder assessment. Recognize him as having CKD from now, as KDIGO 2024 '
             'allows for newborns with clear kidney disease, and plan with the family for the possibility of dialysis or transplant later if '
             'his nadir is high.</p>\n'],
 'skills': {'title': 'CAKUT, antenatal urinary tract dilation and posterior urethral valves',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Classifies antenatal and postnatal dilation by the UTD system and times the postnatal ultrasound', False),
                      ('Directs emergency bladder drainage and monitors for post-obstructive diuresis in a newborn with suspected valves', False),
                      ('Records and explains the nadir creatinine to a family, with its prognostic meaning', False),
                      ('Writes a first-year plan covering salt and water, infection, bladder care, growth and blood pressure', False)],
            'placement': 'Neonatal unit, pediatric ward, outpatient clinic or simulation'},
 'quiz': [('A postnatal ultrasound at 12 hours of life shows mild pelvic fullness in a boy with antenatal bilateral hydronephrosis. Why is this reassuring finding unreliable?',
           ['Ultrasound cannot see the bladder in newborns',
            'The UTD postnatal categories assume a scan done more than 48 hours after birth, when the newborn is no longer relatively oliguric',
            'Hydronephrosis always resolves by 12 hours',
            'The kidneys are not yet visible on ultrasound'],
           1,
           'Early relative oliguria can underestimate dilation. A boy with a distended bladder still needs action now.'),
          ('In the UTD system, how is a postnatal APRPD of 16 mm with no other findings classified?',
           ['Normal',
            'P1, low risk',
            'P3, high risk',
            'P2, intermediate risk'],
           3,
           'P2 is APRPD &ge;15 mm or peripheral calyceal dilation. P3 requires parenchymal, ureteral or bladder abnormalities.'),
          ('What is the strongest predictor of long-term kidney function in boys with posterior urethral valves?',
           ['The nadir creatinine in the first year after relief of obstruction',
            'Birth weight',
            'The creatinine on day 1 of life',
            'The degree of antenatal hydronephrosis alone'],
           0,
           'Multiple cohorts and a meta-analysis of 1,731 boys support nadir creatinine; day 1 creatinine reflects the mother&rsquo;s.'),
          ('What did a 2016 review conclude about fetal intervention for bladder outlet obstruction?',
           ['It improves postnatal kidney outcome',
            'It eliminates the need for postnatal ablation',
            'It probably reduces perinatal mortality but has not improved postnatal kidney outcome',
            'It increases kidney failure rates'],
           2,
           'The benefit is thought to come from relieving oligohydramnios during lung development; kidney outcomes have not changed.'),
          ('A 6-month-old with valves and a low nadir creatinine is polyuric and falling across weight percentiles. What is the most likely reason?',
           ['Tubular salt and water wasting despite preserved GFR',
            'Excess protein intake',
            'Normal growth variation',
            'Hypertension'],
           0,
           'Dysplastic tubules concentrate poorly and waste sodium; a good nadir does not mean the tubules are normal.')],
 'terms': [('APRPD', 'Anterior-posterior renal pelvic diameter'),
           ('CAKUT', 'Congenital anomalies of the kidney and urinary tract'),
           ('CKD', 'Chronic kidney disease'),
           ('GFR', 'Glomerular filtration rate'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('KRT', 'Kidney replacement therapy'),
           ('UTD', 'Urinary tract dilation'),
           ('UTI', 'Urinary tract infection')],
 'readings': [('ckd-children-young-adults.html', 'CKD in Children & Young Adults'),
              ('born-small-kidneys-for-life.html', 'Born Small, Kidneys for Life: Birth History and Kidney Health'),
              ('recurrent-uti-ckd.html', 'Recurrent UTI as a CKD Peril')],
 'calcs': ['calc-pediatric-egfr.html', 'calc-schwartz-egfr.html', 'calc-pediatric-uo.html', 'calc-pediatric-growth-percentiles.html', 'calc-pediatric-ckd-krt-risk.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
