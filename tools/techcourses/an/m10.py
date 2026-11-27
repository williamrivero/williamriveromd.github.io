# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 10: CKD complications and multidisciplinary review.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. KDIGO 2026 anemia statements checked against the published executive summary and central illustrations
(the summary text available to us did not carry GRADE labels, so no grades are quoted); KDIGO 2024 acidosis practice point
checked against the guideline summary; TREAT and PIVOTAL figures against the PubMed abstracts."""

MODULE = {'image_alt': 'Top-down arrangement of a blood tube, an iron vial, an injection syringe and binder tablets.',
 'objectives': ['Separate iron deficiency, inflammation and erythropoietin deficiency as drivers of anemia.',
                'Apply the Kidney Disease: Improving Global Outcomes (KDIGO) 2026 anemia guideline to iron, erythropoiesis-stimulating '
                'agent (ESA) and hypoxia-inducible factor (HIF) prolyl hydroxylase inhibitor (HIF-PHI) decisions.',
                'Interpret chronic kidney disease–mineral and bone disorder (CKD-MBD), acidosis and symptoms as trends within one plan.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you plan long-term care with the patient (b9).[[an01_1]] The physician on '
        'duty and the nurses bring you the new laboratory results; acting on them is yours.</div>\n'
        '{{plain:Picture a rice mill with three problems at once. The farmer delivers too little palay. The warehouse door is padlocked, '
        'so the rice already stored cannot reach the mill. And the foreman who balances the books has stopped coming to work. Ordering '
        'more palay does nothing while the warehouse stays locked.}}\n'
        '<p>The picture has a limit. In the failing kidney the three problems are not separate accidents. One illness drives all of them: '
        'too little erythropoietin from a scarred kidney, iron locked away by hepcidin when there is inflammation, and mineral control '
        'that slips as phosphate excretion falls. And the lock opens again when the inflammation settles. That is why the same patient '
        'can look iron deficient in one month and iron replete in the next.</p>\n'
        '{{cards:Key numbers (KDIGO 2026 anemia, unless noted)|Anemia definition::Hemoglobin (Hb) &lt;13 g/dL in men; &lt;12 g/dL in '
        'women|Severe iron deficiency::Ferritin &lt;45 ng/mL|Start an ESA, non-dialysis::Generally at Hb 8.5&ndash;10 g/dL, guided by '
        'symptoms|Start an ESA, dialysis::Hb &le;9&ndash;10 g/dL is a reasonable threshold|Withhold routine iron::Ferritin &gt;700 ng/mL '
        'or transferrin saturation (TSAT) &ge;40%, and during systemic infection|Alkali therapy (KDIGO 2024, practice point)::Consider when '
        'serum bicarbonate is &lt;18 mmol/L}}\n'
        '<p>Most anemia in your patients is the anemia of kidney disease. Some of it is blood loss, poor intake or infection wearing the '
        'same mask. Your work is to sort the cause before you change a dose, and to keep one plan for hemoglobin, minerals and acid that the '
        'unit, the patient and the family can follow between your visits.</p>\n',
 'case': {'title': 'Hemoglobin 8.9 after pneumonia',
          'html': '<p>On your monthly visit to the dialysis center, the head nurse flags Mr. Fajardo, 71, one of your patients, who has '
                  'been on hemodialysis for two years. He spent last week in a provincial hospital with pneumonia, under another '
                  'physician. His hemoglobin is 8.9 g/dL, down from 10.5. Ferritin is 780 ng/mL, transferrin saturation 14%, and his '
                  'C-reactive protein (CRP) is high.</p>\n'
                  '<p>The unit&rsquo;s standing order, which covers every attending nephrologist&rsquo;s patients, calls for 100 mg of '
                  'intravenous iron every session when transferrin saturation is below 20%, and the nurse has an ampoule ready. The '
                  'physician on duty suggests doubling his erythropoietin dose. Mr. Fajardo buys his own erythropoietin, and his son in '
                  'Dubai sends money for it each month. He tells you he is tired and has barely eaten since he was discharged.</p>\n',
          'questions': ['Is he iron deficient?',
                        'Should the nurse give the iron today, and should the erythropoietin be doubled?',
                        'What else needs checking before you call this the anemia of kidney disease?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Start with the healthy kidney. Peritubular fibroblasts sense oxygen through hypoxia-inducible factor (HIF). When oxygen '
               'delivery falls, HIF is no longer broken down, and the cells make erythropoietin. In CKD, fibrosis destroys these sensing '
               'cells. The kidney makes too little erythropoietin for the degree of anemia.</p>\n'
               '<p>Iron is the second problem. Inflammation and reduced kidney clearance raise hepcidin. Hepcidin degrades ferroportin, the '
               'only exit for iron from macrophages and gut cells. Iron is trapped where the marrow cannot reach it. Ferritin rises, because '
               'it is an acute-phase protein, while transferrin saturation (TSAT) falls. This is functional iron deficiency: stores look full '
               'and the marrow starves. HIF prolyl hydroxylase inhibitors (HIF-PHIs) stabilize HIF, which raises the body&rsquo;s own '
               'erythropoietin and lowers hepcidin.</p>\n'
               '<p>Mineral control fails in parallel. As phosphate excretion falls, bone cells release fibroblast growth factor 23 (FGF23). '
               'FGF23 holds phosphate down for years, but it suppresses calcitriol. Low calcitriol, and later high phosphate, drive '
               'parathyroid hormone (PTH) up. Acid handling fails too. The kidney excretes less ammonium, bicarbonate falls, and the body '
               'buffers the acid with muscle and bone.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Signal that fails</th><th>What breaks it</th><th>What you see on the results</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Erythropoietin</td><td>Fibrosis of the oxygen-sensing cells</td><td>Low Hb with adequate iron and a low '
               'reticulocyte count</td></tr>\n'
               '<tr><td>Iron release</td><td>Hepcidin raised by inflammation</td><td>High ferritin, low TSAT, high CRP</td></tr>\n'
               '<tr><td>Phosphate and PTH</td><td>Falling phosphate excretion, FGF23, low calcitriol</td><td>Rising phosphate and PTH, '
               'then rising alkaline phosphatase</td></tr>\n'
               '<tr><td>Acid excretion</td><td>Less ammonium made by the tubule</td><td>Falling serum bicarbonate</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Ferritin is an acute-phase protein. Read it with TSAT and CRP before you call a patient iron deficient or iron '
               'replete.}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the monthly anemia review &middot; fictional</span><p>Nurse Cabral lists six '
               'of your patients whose erythropoietin doses have doubled in three months. Four of them have a transferrin saturation below '
               '20% with a ferritin above 500 ng/mL. Three had infections.</p><p>You explain the lock. Inflammation raises hepcidin, '
               'hepcidin closes the iron exit from cells, and the marrow starves while the stores look full. Higher erythropoietin doses '
               'cannot make red cells without available iron. For families paying for every vial, that is money spent for nothing.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> A rising ESA dose is a question about iron and inflammation before it is a '
               'question about erythropoietin.</p></div>\n'
               '\n'
               '\n'
               '{{fig:an10_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>The 2026 guideline.</strong> KDIGO published its updated anemia guideline in January 2026, replacing the 2012 '
               'version. It defines anemia as Hb &lt;13 g/dL in men and &lt;12 g/dL in women. It screens with a complete blood count, '
               'reticulocytes, ferritin and TSAT, and treats severe iron deficiency (ferritin &lt;45 ng/mL). In hemodialysis it suggests '
               'intravenous rather than oral iron, started when ferritin is &le;500 ng/mL and TSAT &le;30%. It considers it reasonable to '
               'withhold routine iron when ferritin is &gt;700 ng/mL or TSAT &ge;40%, and to hold iron during systemic infection.[[an10_2]] '
               'Most of these are suggestions or practice points, not strong recommendations. Check the grade in the full guideline before '
               'you quote one.</p>\n'
               '<p><strong>ESA or HIF-PHI.</strong> The guideline suggests an ESA rather than a HIF-PHI as first-line therapy, because the '
               'long-term cardiovascular and thrombotic safety of HIF-PHIs remains uncertain. It places the start of an ESA generally at Hb '
               '8.5&ndash;10 g/dL in non-dialysis CKD, guided by symptoms, and at &le;9&ndash;10 g/dL in dialysis. It advises against using an '
               'ESA to maintain Hb &ge;11.5 g/dL. A HIF-PHI remains an option for a patient who prefers an oral agent, cannot tolerate an ESA, '
               'or has no refrigeration at home. It should not be used with active malignancy or a recent cardiovascular or thrombotic event, '
               'and it should be stopped after 3&ndash;4 months if the response is insufficient.[[an10_2]]</p>\n'
               '<p><strong>Why the ceiling exists.</strong> TREAT randomized 4,038 patients with type 2 diabetes and non-dialysis CKD to '
               'darbepoetin targeting Hb about 13 g/dL or to placebo with rescue therapy. Death or a cardiovascular event did not differ '
               '(hazard ratio 1.05). Stroke occurred in 101 patients (5.0%) on darbepoetin versus 53 (2.6%) on placebo (hazard ratio 1.92), and '
               'fatigue improved only modestly.[[an10_3]] Hemoglobin is a surrogate. Raising it to normal did not deliver the outcomes '
               'patients feel, and it doubled the stroke risk.</p>\n'
               '<p><strong>Iron in hemodialysis.</strong> PIVOTAL randomized 2,141 hemodialysis patients to proactive high-dose intravenous '
               'iron sucrose (400 mg a month unless ferritin was &gt;700 ng/mL or TSAT &ge;40%) or reactive low-dose iron. Over a median 2.1 '
               'years, the composite of myocardial infarction, stroke, heart failure hospitalization or death occurred in 29.3% versus 32.3% '
               '(hazard ratio 0.85), the ESA dose was lower, and infection rates did not differ.[[an10_4]]</p>\n'
               '<p><strong>Acid.</strong> KDIGO 2024 suggests considering drug treatment, with or without diet, to prevent acidosis with '
               'clinical implications, giving serum bicarbonate &lt;18 mmol/L as an example. This is a practice point, not a graded '
               'recommendation.[[an10_1]]</p>\n'
               '{{key:Hemoglobin is a surrogate. Treat to relieve symptoms and avoid transfusion, never to normalize the number.}}\n' '\n{{fig:an10_fig_anemia_2026_thresholds_treat}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Sort the cause first.</strong> Before you call it the anemia of kidney disease, look for blood loss, check B12, '
               'folate and signs of hemolysis, and read ferritin with TSAT and CRP. Hold intravenous iron during an active infection. Use '
               'intravenous iron in hemodialysis, and oral or intravenous iron in non-dialysis CKD according to the patient&rsquo;s '
               'preference and response. Start an ESA at the lowest effective dose and check Hb every 2&ndash;4 weeks after each '
               'change.[[an10_2]]</p>\n'
               '<p><strong>Fit it to Philippine practice.</strong> Many of your patients buy their own erythropoietin and iron, and a missed '
               'vial is often a missed paycheck, not forgetfulness. Ask before you assume nonadherence. A patient from a province without '
               'reliable refrigeration may be a candidate for an oral agent if one is registered and affordable. Standing orders in a shared '
               'unit cover every attending&rsquo;s patients. Review them with the clinical head, so that each one has a ferritin ceiling, a '
               'CRP check and a stop for infection. You are not in the unit most days, so agree in writing which results the nurses send you '
               'and which values make them call you the same day.</p>\n'
               '<p><strong>Minerals, acid and symptoms.</strong> Follow calcium, phosphate, PTH and alkaline phosphatase as trends, not as '
               'single values. Lower phosphate toward normal with diet and binders, avoid hypercalcemia, and treat a progressive PTH rise. '
               'Screen for itch, poor sleep, frailty and poor intake, and bring the renal dietitian into each review.</p>\n'
               '\n'
               '{{fig:an10_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">On your monthly visit, the binder taken at the wrong time &middot; '
               'fictional</span><p>Mrs. Garcia&rsquo;s phosphate stays high despite three binder tablets a day. You ask when she takes '
               'them. &ldquo;Before breakfast, all three, so I don&rsquo;t forget.&rdquo;</p><p>A binder works only when it meets the '
               'phosphate in food. You ask her to take one with each meal, and you ask the dietitian to look at the instant noodles and '
               'processed meats in her week.</p><p class="tc-scene-take"><b>What this shows.</b> Before adding a drug, check how the '
               'current one is being taken.</p></div>\n'
               '{{key:Change one thing at a time, and write each change where the unit and the patient can both see it.}}\n'
               '{{call:<ul><li>Falling hemoglobin with positive stool occult blood</li><li>Very high ferritin with low TSAT during '
               'infection (hold intravenous iron)</li><li>Hypercalcemia on calcitriol or calcium-based binders</li><li>Calciphylaxis (painful '
               'violaceous skin lesions)</li></ul>}}\n')],
 'debrief': ['<p><strong>Is he iron deficient?</strong> Not in the way the order assumes. A high ferritin with a low transferrin '
             'saturation during an infection means hepcidin is locking iron inside his cells. His stores are not empty, but iron given now '
             'cannot reach his bone marrow. KDIGO 2026 advises holding iron during systemic infection.</p>\n'
             '<p><strong>Today&rsquo;s iron, and the erythropoietin.</strong> Hold the intravenous iron while the infection settles, and '
             'write the reason in the order so the next shift does not give it. Do not double the erythropoietin on one value taken during '
             'an illness. Inflammation blunts the response, and chasing hemoglobin with high doses spends his son&rsquo;s money without '
             'helping his marrow. Recheck hemoglobin and iron indices in four to six weeks, after the infection has settled.</p>\n'
             '<p><strong>What else.</strong> Look for blood loss: ask about black stools, check stool occult blood, and look for bleeding '
             'from the access. Check B12 and folate. Ask the renal dietitian to see him this week, because poor intake after an admission '
             'makes everything worse. Then raise the standing order with the clinical head, because it covers every attending&rsquo;s '
             'patients, not only yours. A rule that runs on transferrin saturation alone, with no ferritin, no CRP, and no stop for '
             'infection, will do this again to the next patient.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Interprets anemia data with inflammation in context', False),
                      ('Interprets serial mineral labs together', False),
                      ('Documents symptom and nutrition goals', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Why review transferrin saturation with ferritin?',
           ['Ferritin directly measures red cell production',
            'Inflammation can raise ferritin despite restricted iron availability',
            'TSAT determines phosphate control',
            'TSAT is unaffected by iron status'],
           1,
           'Ferritin rises as an acute-phase protein; TSAT shows how much iron is actually available to the marrow.'),
          ('How should CKD-MBD labs guide reassessment?',
           ['Interpret calcium, phosphate and PTH trends together',
            'Act on every isolated PTH result without context',
            'Assess calcium only after symptoms develop',
            'Check vitamin D only'],
           0,
           'Trends in related measures support one coordinated plan.'),
          ('Per KDIGO 2026, what is first-line therapy for renal anemia once correctable causes are addressed?',
           ['Androgens', 'A HIF-PHI for all patients', 'Blood transfusion', 'An ESA, with HIF-PHIs as alternatives in selected situations'],
           3,
           'The guideline suggests an ESA rather than a HIF-PHI because long-term cardiovascular and thrombotic safety of HIF-PHIs is '
           'uncertain.'),
          ('In which patient should a HIF-PHI be avoided?',
           ['A patient without refrigeration at home',
            'A patient who prefers oral medication',
            'A patient with active malignancy or a recent thrombotic event',
            'A patient with ESA hyporesponsiveness'],
           2,
           'KDIGO 2026 advises against HIF-PHI use with active malignancy or a recent cardiovascular or thrombotic event.'),
          ('What did TREAT show when darbepoetin targeted a hemoglobin of about 13 g/dL?',
           ['Lower mortality',
            'No reduction in death or cardiovascular events, and about twice the stroke rate',
            'That ESAs cause iron overload',
            'Fewer dialysis starts'],
           1,
           'Stroke occurred in 5.0% versus 2.6%, with no benefit on the primary outcomes; this is why ESAs are not used to normalize '
           'hemoglobin.')],
 'terms': [('CKD', 'Chronic kidney disease'),
           ('EPO', 'Erythropoietin'),
           ('HIF', 'Hypoxia-inducible factor'),
           ('TSAT', 'Transferrin saturation'),
           ('FGF23', 'Fibroblast growth factor 23'),
           ('PTH', 'Parathyroid hormone'),
           ('ESA', 'Erythropoiesis-stimulating agent'),
           ('Hb', 'Hemoglobin'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('CBC', 'Complete blood count'),
           ('CRP', 'C-reactive protein'),
           ('CKD-MBD', 'Chronic kidney disease–mineral and bone disorder'),
           ('IV', 'Intravenous'),
           ('HD', 'Hemodialysis'),
           ('HIF-PHI', 'Hypoxia-inducible factor prolyl hydroxylase inhibitor')],
 'readings': [('anemia-management.html', 'Anemia Management'), ('ckd-mbd.html', 'CKD-MBD: Kidney, Bone & Heart')],
 'calcs': ['calc-iron-status-tsat.html',
           'calc-iv-iron-dose.html',
           'calc-iron-deficit-ganzoni.html',
           'calc-esa-dose-adjustment.html',
           'calc-reticulocyte-rpi.html',
           'calc-ckd-mbd.html',
           'calc-corrected-calcium.html',
           'calc-bicarb-deficit.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
