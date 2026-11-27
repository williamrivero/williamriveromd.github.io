# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 04: Potassium, calcium, phosphate and magnesium emergencies.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. Pediatric
thresholds and treatment framework checked against Zieg 2024 (full text); TLS definitions against Cairo-Bishop 2004 as
reproduced in published tables; Coiffier 2008, Goldman 2001, ASPEN 2020 and Liamis 2021 against PubMed abstracts.
Weight-based therapy is described as a principle; doses come from the unit's pediatric formulary. Fictional case."""

MODULE = {'image_alt': 'A pediatric nephrologist reviews an electrocardiogram strip with an oncology fellow beside the bed of a young boy receiving chemotherapy.',
 'objectives': ['Explain hyperkalemia at the cell membrane and apply the stabilize, shift and remove sequence in a child, with doses taken from the unit&rsquo;s pediatric formulary.',
                'Recognize laboratory and clinical tumor lysis syndrome by the Cairo&ndash;Bishop definitions and decide when the kidney needs support.',
                'Identify the calcium, phosphate and magnesium emergencies of infancy, refeeding and drug toxicity, and why magnesium must be corrected first.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the kidney consultant to the oncology and pediatric wards</span>'
        'You are called when a potassium is already high, an electrocardiogram (ECG) already looks wrong, or a child on chemotherapy has '
        'stopped passing urine. The pediatric oncologist, the intensivist and you share the child. Your duty is to read the numbers fast, '
        'separate the real from the artifact, start the right sequence, and decide early whether the child needs dialysis and where it can '
        'be done.</div>\n'
        '{{plain:Think of each heart cell as a small battery. Potassium inside the cell, far more than outside, keeps it charged. When the '
        'outside potassium rises, the battery runs down: the cell sits closer to firing but fires worse.}}\n'
        '<p>The picture has a limit. A battery that runs down simply stops. A heart cell with a raised outside potassium first becomes '
        'easier to excite, then slower to conduct, then unable to conduct at all, because the sodium channels that start each beat stay '
        'inactivated when the resting voltage drifts up. Calcium does not lower potassium; it moves the firing threshold back and buys time. '
        'That is why treatment comes in three steps that do three different things.</p>\n'
        '{{cards:Key numbers|Hyperkalemia in children (review)::Plasma potassium above 5.5 mmol/L; severe above 7 mmol/L|Laboratory tumor '
        'lysis (Cairo&ndash;Bishop)::Two or more of: uric acid &ge;476 &micro;mol/L, potassium &ge;6.0 mmol/L, phosphate &ge;2.1 mmol/L in '
        'children, calcium &le;1.75 mmol/L, or a 25% change, from 3 days before to 7 days after chemotherapy|Rasburicase versus allopurinol '
        '(pediatric randomized controlled trial)::Uric acid fell 86% versus 12% four hours after the first dose|Refeeding syndrome (ASPEN 2020)::A fall in '
        'phosphorus, potassium or magnesium of 10&ndash;20% (mild), 20&ndash;30% (moderate) or more than 30% (severe) within 5 days of '
        'feeding}}\n'
        '<p>Most high potassiums in children are real but slow, and some are artifacts from a squeezed heel or a hemolyzed sample. A few kill '
        'within minutes. Your work is to know which is which within one phone call, act in the right order, and plan removal, not only '
        'shifting.</p>\n',
 'case': {'title': 'Day 2 of chemotherapy',
          'html': '<p>It is Wednesday, 6:15 p.m., in the pediatric oncology ward of a tertiary government hospital in Manila. Joshua Ramos is '
                  '6 years old and 19 kg, with stage III Burkitt lymphoma and a large abdominal mass. Induction chemotherapy started yesterday '
                  'with hydration and allopurinol; rasburicase was recommended but the family could not afford it, and the hospital&rsquo;s '
                  'stock was out. Since noon his urine output has fallen from 2.5 to 0.6 mL/kg per hour.</p>\n'
                  '<p>His 6 p.m. results: potassium 6.6 mmol/L (5.4 this morning), phosphate 2.9 mmol/L, total calcium 1.65 mmol/L, uric '
                  'acid 690 &micro;mol/L, creatinine 1.1 mg/dL (0.4 on admission). The sample was venous and not hemolyzed. The ECG shows '
                  'peaked T waves. He complains of tingling fingers. The oncology fellow asks you two things by phone: should she give calcium '
                  'to correct his calcium, and can dialysis wait until tomorrow, when the hemodialysis unit has a free slot? His mother, Mrs. '
                  'Rowena Ramos, a market vendor from Tondo, asks whether the chemotherapy is now hurting his kidneys.</p>\n',
          'questions': ['Does Joshua have tumor lysis syndrome, and what is injuring his kidneys?',
                        'What do you do for the potassium in the next 30 minutes, and in what order?',
                        'Should his calcium be corrected now, and can dialysis wait until tomorrow?']},
 'sections': [('potassium',
               'Potassium',
               'Hyperkalemia: stabilize, shift, remove',
               '<p>Almost all of the body&rsquo;s potassium sits inside cells. The ratio of inside to outside potassium sets the resting voltage '
               'of heart and muscle cells. The kidney removes the daily load; insulin and beta-adrenergic stimulation move potassium into cells '
               'within minutes; acidosis and cell breakdown push it out.</p>\n'
               '<p>A pediatric review defines hyperkalemia as a plasma potassium above 5.5 mmol/L, moderate at 6 to 7 and severe above 7 mmol/L, '
               'and notes that normal values are higher in newborns and infants.[[apn04_1]] The ECG may progress from peaked T waves to flattened, '
               'broad P waves and QRS widening, and then to heart block, asystole or ventricular arrhythmia.[[apn04_1]] Newborns are a special '
               'group: a low GFR, immature tubules and high extrarenal losses all make electrolyte disorders more common in them.[[apn04_10]]</p>\n'
               '<p><strong>First, is it real?</strong> Pseudohyperkalemia is common in children. The same review attributes it to hemolysis and to '
               'potassium leaking from cells during or after collection, more often in small children, where small needles and squeezing the '
               'surrounding tissue contribute, as well as to very high white cell counts, clotting and delayed analysis.[[apn04_1]] A squeezed '
               'heel-prick sample from a well infant with a normal ECG should be repeated by free-flowing venous sampling before anyone gives '
               'insulin. A high potassium in a child with leukemia and a very high white count may also be spurious; ask for a whole-blood or '
               'blood-gas value taken without delay.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Step</th><th>What it does at the membrane</th><th>Options (doses from the '
               'pediatric formulary)</th><th>What it does not do</th></tr></thead><tbody>'
               '<tr><td>Stabilize</td><td>Raises the threshold for firing; restores conduction</td><td>Intravenous calcium, given slowly with '
               'monitoring</td><td>Lower potassium</td></tr>'
               '<tr><td>Shift</td><td>Moves potassium into cells</td><td>Insulin with dextrose; inhaled or intravenous beta-2 agonist; bicarbonate '
               'only in acidosis</td><td>Remove potassium from the body; effect wears off</td></tr>'
               '<tr><td>Remove</td><td>Takes potassium out of the body</td><td>Loop diuretic if the kidney responds; potassium binders; dialysis</td>'
               '<td>Act quickly (except dialysis)</td></tr>'
               '</tbody></table></div>\n'
               '<p>The review calls insulin with dextrose one of the most potent treatments short of dialysis, notes that loop diuretics have the '
               'greatest kaliuretic effect, and observes that binders are not supported by high-quality evidence in acute hyperkalemia. It '
               'advises against bicarbonate when the pH is above 7.4.[[apn04_1]] A Kidney Disease: Improving Global Outcomes (KDIGO) controversies '
               'conference reached broadly similar conclusions for kidney patients, mostly from adult data.[[apn04_2]] Pediatric trials are few; '
               'most of this sequence rests on physiology and adult evidence, and the weight-based doses must come from your unit&rsquo;s '
               'pediatric formulary, double-checked, because tenfold errors are a real risk in small children.</p>\n'
               '{{key:Stabilize, shift, remove. Calcium buys minutes, insulin buys hours, and only removal ends the problem.}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the nursery &middot; fictional</span><p>A well-looking 5-day-old has a potassium of '
               '7.2 mmol/L on a heel-prick sample taken after a long, difficult stick. The ECG is normal. The resident has drawn up '
               'insulin.</p><p>You ask him to wait, repeat a free-flowing venous sample, and keep the baby on a monitor meanwhile. The repeat is '
               '5.6 mmol/L.</p><p class="tc-scene-take"><b>What this shows.</b> A squeezed heel can raise potassium far more than the baby can. '
               'Treat the child and the ECG, and confirm the number.</p></div>\n'),
              ('tls',
               'Tumor lysis',
               'Tumor lysis syndrome: when the tumor floods the kidney',
               '<p>When chemotherapy kills a large, fast-growing tumor, the cells release potassium, phosphate and nucleic acids, which are broken '
               'down to uric acid. Cairo and Bishop describe high incidence in tumors with high proliferative rates and burden, such as acute '
               'lymphoblastic leukemia and Burkitt lymphoma.[[apn04_3]] A recent review describes a large cancer cell mass in children as 300 '
               'g/m&sup2; of body surface area or more.[[apn04_6]] The kidney is injured in two ways: uric acid and calcium phosphate crystallize in '
               'the tubules, and volume depletion and inflammation lower perfusion. Phosphate binds calcium, so serum calcium falls, and giving '
               'calcium into a high phosphate raises the calcium-phosphate product and the risk of further precipitation in kidney and '
               'tissues.</p>\n'
               '<p><strong>Definitions.</strong> Laboratory tumor lysis syndrome (TLS) by Cairo&ndash;Bishop is two or more of the following within '
               '3 days before or 7 days after starting cytotoxic therapy: uric acid &ge;476 &micro;mol/L (8 mg/dL), potassium &ge;6.0 mmol/L, '
               'phosphate &ge;2.1 mmol/L (6.5 mg/dL) in children, calcium &le;1.75 mmol/L (7 mg/dL), or a 25% change from baseline in any of '
               'them. Clinical TLS is laboratory TLS plus a rise in creatinine, an arrhythmia or sudden death, or a seizure.[[apn04_3]] An expert '
               'panel later built a risk model (low, intermediate, high) based on laboratory TLS, tumor type, bulk and stage, and kidney '
               'involvement.[[apn04_5]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Released</th><th>What happens</th><th>What you see</th></tr></thead><tbody>'
               '<tr><td>Potassium</td><td>Membrane depolarization</td><td>Peaked T waves, arrhythmia</td></tr>'
               '<tr><td>Phosphate</td><td>Binds calcium; calcium phosphate deposits in tubules</td><td>Low calcium, tingling, tetany, falling urine '
               'output</td></tr>'
               '<tr><td>Nucleic acids to uric acid</td><td>Crystals in acidic tubular fluid</td><td>Rising uric acid and creatinine</td></tr>'
               '<tr><td>Volume shifts, vomiting</td><td>Lower kidney perfusion</td><td>Concentrated urine, rising creatinine</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Evidence.</strong> The 2008 guideline from pediatric and adult oncologists recommends prevention: hydration and '
               'prophylactic rasburicase in high-risk patients, hydration with allopurinol or rasburicase at intermediate risk, and monitoring at '
               'low risk. It does not recommend urine alkalinization.[[apn04_4]] In a randomized trial in 52 children with leukemia or lymphoma '
               'at high risk, rasburicase lowered uric acid exposure over 96 hours (area under the curve 128 versus 329 mg/dL&middot;hour) and '
               'reduced uric acid by 86% versus 12% four hours after the first dose.[[apn04_7]] Uric acid is a surrogate. The trial was small and '
               'was not designed to show a difference in dialysis or death, so its strength is in rapid control of the laboratory value.</p>\n'
               '<p>Rasburicase is expensive and not always stocked in Philippine hospitals. When it is unavailable, the attending&rsquo;s job is to '
               'see the kidney injury coming earlier, keep urine flowing with hydration where the heart and lungs allow, and plan dialysis before '
               'the potassium forces it.</p>\n'
               '{{key:In tumor lysis, treat the phosphate and the urine output as seriously as the potassium. Calcium is for symptoms and the ECG, '
               'not for the number.}}\n'
               '\n{{fig:apn04_a}}\n'),
              ('minerals',
               'Calcium, phosphate, magnesium',
               'Calcium, phosphate and magnesium: infants, refeeding and drugs',
               '<p><strong>Hypocalcemia.</strong> The pediatric review lists early and late transient neonatal hypocalcemia among causes in the '
               'newborn. Symptoms appear as ionized calcium falls and include tingling of the face and limbs, carpopedal spasm, stridor, tetany, '
               'cramps and seizures, with Chvostek and Trousseau signs and reduced cardiac contractility.[[apn04_1]] In an infant, a seizure with a '
               'normal glucose should prompt an ionized calcium and a magnesium.</p>\n'
               '<p><strong>Magnesium comes first.</strong> Hypomagnesemia, defined in the review as below 0.62 mmol/L, disrupts parathyroid hormone '
               'action and causes hypocalcemia and hypokalemia that resist treatment until magnesium is replaced.[[apn04_1]] Drugs are a common '
               'cause in hospitalized children: aminoglycosides and amphotericin B, diuretics, cisplatin, calcineurin inhibitors and proton pump '
               'inhibitors all lower magnesium, through the gut or the tubule.[[apn04_9]] A child with refractory hypokalemia on amphotericin or '
               'after cisplatin needs a magnesium level before another potassium bolus.</p>\n'
               '<p><strong>Refeeding.</strong> When a malnourished child starts eating, insulin drives phosphate, potassium and magnesium into '
               'cells. The American Society for Parenteral and Enteral Nutrition (ASPEN) 2020 consensus, written for hospitalized adults and '
               'children, defines refeeding syndrome as a fall in serum phosphorus, potassium or magnesium of 10&ndash;20% (mild), 20&ndash;30% '
               '(moderate), or more than 30% or organ dysfunction (severe), occurring within 5 days of reintroducing calories.[[apn04_8]] This is a '
               'consensus definition, not a validated outcome measure. Hypophosphatemia, below 0.81 mmol/L in the review, can cause arrhythmias, '
               'weakness and seizures.[[apn04_1]] Children with severe acute malnutrition, anorexia, long fasting or a long intensive care stay '
               'are at risk.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Setting</th><th>Electrolyte</th><th>Mechanism</th><th>What you check</th></tr></thead><tbody>'
               '<tr><td>Newborn seizure, normal glucose</td><td>Calcium, magnesium</td><td>Transient neonatal hypocalcemia</td><td>Ionized calcium, '
               'magnesium, phosphate</td></tr>'
               '<tr><td>Refractory hypokalemia or hypocalcemia</td><td>Magnesium</td><td>Renal wasting from drugs; PTH resistance</td><td>Magnesium '
               'before more potassium or calcium</td></tr>'
               '<tr><td>Malnourished child starting feeds</td><td>Phosphate, potassium, magnesium</td><td>Insulin-driven shift into cells</td>'
               '<td>Levels before feeding and daily for 5 days</td></tr>'
               '<tr><td>Tumor lysis</td><td>Phosphate high, calcium low</td><td>Cell release; calcium-phosphate binding</td><td>Phosphate, calcium, '
               'urine output every few hours</td></tr>'
               '</tbody></table></div>\n'
               '{{key:When potassium or calcium will not correct, check magnesium. When a starved child starts eating, check phosphate.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>On the first call.</strong> Ask for the ECG, the sampling method, the trend, the urine output, the weight and the '
               'medicines. Decide whether to treat now or repeat first. If the ECG is abnormal, treat while you repeat.</p>\n'
               '<p><strong>Order safely.</strong> Ask the resident to read back the weight in kilograms and each dose from the pediatric '
               'formulary, and to have a second person check insulin and calcium. Write the time of the next potassium and glucose.</p>\n'
               '<p><strong>Plan removal early.</strong> If the urine output is falling, the potassium is rising despite shifting, or the phosphate '
               'is climbing in a child with tumor lysis, start the dialysis conversation now. Where can this child be dialyzed tonight? Is there '
               'pediatric vascular access, a circuit sized for the child, and a team? Acute peritoneal dialysis is a valid option in a small child '
               'when hemodialysis or continuous therapy is not available (Module 16), though it removes potassium and phosphate more slowly.</p>\n'
               '{{flow:A high potassium on the phone|Real or artifact::Sampling method, hemolysis, white count, delay; repeat by free-flowing '
               'venous sample if the child is well and the ECG is normal.|ECG::Peaked T waves, wide QRS, arrhythmia: stabilize now with calcium '
               'per formulary.|Shift::Insulin with dextrose, beta-2 agonist; glucose checks; bicarbonate only for acidosis.|Remove::Loop diuretic '
               'if the kidney responds; binder; dialysis if not.|Find the cause::Tumor lysis, acute kidney injury, drugs, acidosis, hemolysis, '
               'adrenal or tubular disease.|Recheck::Potassium and glucose at a written time; ECG after each step.}}\n'
               '{{call:<ul><li>ECG changes of hyperkalemia, or potassium above 7 mmol/L on a reliable sample</li><li>Potassium rising despite shifting '
               'therapy</li><li>Falling urine output in a child at risk of tumor lysis</li><li>Symptomatic hypocalcemia (tetany, stridor, seizure) '
               'with a high phosphate</li><li>No unit able to dialyze the child within hours</li></ul>}}\n'
               '<div class="tc-scene"><span class="tc-lab">On the intensive care unit &middot; fictional</span><p>Rhea, 11, with fungal sepsis on '
               'amphotericin B, has had three potassium infusions in two days; her potassium is still 2.8 mmol/L, and she has had two runs of '
               'ectopic beats.</p><p>You ask for a magnesium level. It is 0.45 mmol/L. After magnesium is replaced, her potassium begins to '
               'respond.</p><p class="tc-scene-take"><b>What this shows.</b> Low magnesium makes potassium leak from the tubule faster than you can '
               'replace it.</p></div>\n'
               '{{key:Every hyperkalemia plan ends with removal and a named place for dialysis if removal fails.}}\n'
               '\n{{fig:apn04_b}}\n')],
 'debrief': ['<p><strong>Tumor lysis.</strong> Yes. Within the Cairo&ndash;Bishop window he has a potassium &ge;6.0 mmol/L, phosphate '
             '&ge;2.1 mmol/L, calcium &le;1.75 mmol/L and uric acid &ge;476 &micro;mol/L, which is laboratory TLS; with the rise in creatinine it '
             'is clinical TLS. His kidneys are being injured by uric acid and calcium phosphate crystals in the tubules and by reduced '
             'perfusion. Tell Mrs. Ramos that the treatment is working on the tumor, and that the breakdown of the tumor, not a direct poison, is '
             'stressing his kidneys; this is a known risk that the team will manage.</p>\n',
             '<p><strong>The next 30 minutes.</strong> His ECG is abnormal, so treat now and repeat in parallel. Stabilize with intravenous '
             'calcium, given slowly with cardiac monitoring, at the dose in the pediatric formulary. Shift with insulin and dextrose, with glucose '
             'checks, and consider a beta-2 agonist. Then plan removal: a loop diuretic only if he is not volume depleted and his kidneys respond; '
             'otherwise, removal means dialysis. Ask for a repeat potassium and glucose at a written time.</p>\n',
             '<p><strong>Calcium and dialysis.</strong> Treat the calcium only because of his symptoms and the ECG, not to normalize the number: '
             'more calcium into a phosphate of 2.9 mmol/L raises the risk of further calcium phosphate deposition. Dialysis should not wait for '
             'tomorrow&rsquo;s slot. He has clinical TLS with a rising potassium, a high phosphate and falling urine output, and shifting '
             'therapy will wear off. Arrange kidney replacement tonight with the intensive care team, at the unit that can provide pediatric '
             'access and a circuit for a 19 kg child, and document the decision and the plan for rasburicase if it becomes available.</p>\n'],
 'skills': {'title': 'Potassium, calcium, phosphate and magnesium emergencies',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Distinguishes true hyperkalemia from pseudohyperkalemia and directs a correct repeat sample', False),
                      ('Leads a stabilize-shift-remove sequence with formulary doses read back and double-checked', False),
                      ('Applies the Cairo&ndash;Bishop definitions and identifies when a child with TLS needs dialysis', False),
                      ('Checks magnesium in refractory hypokalemia or hypocalcemia and phosphate before refeeding', False)],
            'placement': 'Pediatric ward, oncology unit, intensive care unit or simulation'},
 'quiz': [('What does intravenous calcium do in hyperkalemia?',
           ['Lowers serum potassium within minutes',
            'Stabilizes the cardiac membrane by restoring the firing threshold, without lowering potassium',
            'Removes potassium in the urine',
            'Moves potassium into cells'],
           1,
           'Calcium protects the heart while shifting and removal take effect; it does not change the potassium concentration.'),
          ('A well 5-day-old has a potassium of 7.2 mmol/L on a squeezed heel-prick sample and a normal ECG. What is the best next step?',
           ['Give insulin and dextrose immediately',
            'Start dialysis',
            'Give a potassium binder',
            'Repeat by free-flowing venous sample while monitoring the infant'],
           3,
           'Pseudohyperkalemia from hemolysis and tissue squeezing is common in small children. Treat the ECG and confirm the number.'),
          ('Which set fulfills laboratory tumor lysis syndrome by Cairo&ndash;Bishop in a child?',
           ['Potassium 6.4 mmol/L and phosphate 2.5 mmol/L on day 2 of chemotherapy',
            'Potassium 5.2 mmol/L alone',
            'Uric acid 300 &micro;mol/L and calcium 2.3 mmol/L',
            'Any single abnormal value 14 days after chemotherapy'],
           0,
           'Two or more of potassium &ge;6.0, phosphate &ge;2.1 (children), uric acid &ge;476 &micro;mol/L or calcium &le;1.75 mmol/L, within '
           '3 days before to 7 days after therapy.'),
          ('What did the pediatric randomized trial of rasburicase versus allopurinol show?',
           ['Fewer deaths with rasburicase',
            'Less dialysis with rasburicase',
            'Faster and greater lowering of plasma uric acid, a surrogate outcome',
            'No difference in uric acid'],
           2,
           'In 52 high-risk children, uric acid fell 86% versus 12% four hours after the first dose. The trial was not powered for dialysis or death.'),
          ('A child on amphotericin B has hypokalemia that does not correct despite repeated potassium. What should you check?',
           ['Serum magnesium',
            'Serum chloride only',
            'Uric acid',
            'Serum amylase'],
           0,
           'Hypomagnesemia causes refractory hypokalemia and hypocalcemia; amphotericin B and aminoglycosides are common culprits.')],
 'terms': [('ASPEN', 'American Society for Parenteral and Enteral Nutrition'),
           ('ECG', 'Electrocardiogram'),
           ('GFR', 'Glomerular filtration rate'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('PTH', 'Parathyroid hormone'),
           ('RCT', 'Randomized controlled trial'),
           ('TLS', 'Tumor lysis syndrome')],
 'readings': [('potassium-hyperkalemia-ckd.html', 'Potassium & Hyperkalemia in CKD'),
              ('onconephrology-chemotherapy-kidney.html', 'Cancer Treatment and Your Kidneys: Chemotherapy, Kidney Injury and Safe Dosing'),
              ('magnesium-supplements-ckd.html', 'Magnesium Supplements and Kidney Disease: What the Different Forms Really Do')],
 'calcs': ['calc-potassium-load.html', 'calc-pediatric-calcium.html', 'calc-corrected-calcium.html', 'calc-urine-k-creatinine-ratio.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
