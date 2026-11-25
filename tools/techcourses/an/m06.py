# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 06: Electrolyte emergencies.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Doses and grades checked against the UK Kidney Association hyperkalemia guideline (updated July 2026), the
2014 European hyponatremia guideline (Spasovski), the Ayus 2025 meta-analysis (PubMed), and KDIGO 2012."""

MODULE = {'image_alt': 'A cardiac monitor, an ampule and syringe, and a nebulizer mask on a bedside tray.',
 'objectives': ['Prioritize immediately dangerous electrolyte abnormalities using electrocardiogram (ECG) and clinical context.',
                'Run a monitored hyperkalemia protocol including hypoglycemia surveillance and rebound planning.',
                'Plan safe hyponatremia correction with explicit limits and a rescue plan.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you coordinate with the nurses and the physician on duty during emergencies '
        '(b8).[[an01_1]] They act at the chair; you are the person they call.</div>\n'
        '{{plain:Think of each electrolyte emergency as a fire in a different room. Potassium burns the heart, sodium the brain, and acid '
        'everything. Every fire is fought the same way: protect what is burning, push the fuel aside, then carry it out of the '
        'house.}}\n'
        '<p>The picture has a limit. A fire that is out stays out. These do not. Potassium pushed into cells comes back out within hours. '
        'Sodium that rises safely can keep rising once the kidney starts making dilute urine. Acid returns if its cause is still there. '
        'Each emergency therefore has a second, delayed danger, and the plan must name it.</p>\n'
        '{{cards:Key numbers|Calcium gluconate 10%::30 mL IV over 10 minutes when the ECG shows hyperkalemia (UKKA, 2C)|Insulin-glucose::10 '
        'units soluble insulin in 25 g glucose (UKKA, 1B for K &ge;6.5); then 10% glucose 50 mL/h for 5 h if pre-treatment glucose &lt;7 '
        'mmol/L (126 mg/dL) (2B)|Salbutamol, nebulized::10&ndash;20 mg; adjunct only, never alone (UKKA)|Severe hyponatremia::150 mL 3% '
        'saline over 20 min, up to three times, aiming for +5 mmol/L; limit +10 in the first 24 h, +8 each day after (European '
        'guideline, 2014)|Winter&rsquo;s formula::Expected pCO&#8322; = 1.5 &times; HCO&#8323;&#8315; + 8 &plusmn; 2}}\n'
        '<p>You will rarely be at the chair. The physician on duty (POD) or a ward resident calls or sends an ECG on Viber. Your work is '
        'to say what protects the patient now, what removes the problem, and what to watch after you hang up.</p>\n',
 'case': {'title': 'The man who missed Friday and Monday',
          'html': '<p>Mr. Ocampo, 62, dialyzes on Mondays, Wednesdays, and Fridays. He missed Friday because his tricycle driver was sick, '
                  'and he missed Monday because he had no money for the fare. On Tuesday morning his son brings him to your unit because '
                  '&ldquo;his legs are weak.&rdquo; He makes no urine.</p>\n'
                  '<p>The nurse draws blood while the physician on duty, Dr. Salonga, records an electrocardiogram. The potassium is 7.1 '
                  'mmol/L. The QRS is wide. Dr. Salonga calls your mobile: &ldquo;Doctor, there is no free chair until his regular slot '
                  'tomorrow. Should I give calcium and send him home with a binder?&rdquo;</p>\n',
          'questions': ['What happens in the next ten minutes?',
                        'Can his dialysis wait until tomorrow?',
                        'What will stop this from happening again?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p><strong>Potassium.</strong> The resting membrane potential depends on the ratio of potassium inside the cell to '
               'potassium outside it. As blood potassium rises, the resting potential creeps toward threshold: repolarization speeds up (peaked '
               'T waves), then sodium channels inactivate and conduction slows (wide QRS, then sine wave). Calcium raises the threshold and '
               'restores the gap. Insulin and beta-2 agonists shift potassium into cells through the sodium-potassium pump for some '
               'hours.</p>\n'
               '<p><strong>Sodium.</strong> When sodium falls slowly, brain cells protect their volume over about 48 hours by exporting '
               'osmolytes. Correction that outpaces their return shrinks the cells and risks osmotic demyelination. Alcohol use, '
               'malnutrition, low potassium and liver disease raise that risk.</p>\n'
               '<p><strong>Acid.</strong> First ask whether compensation matches expectation. Winter&rsquo;s formula predicts the carbon '
               'dioxide pressure (pCO&#8322;) for a given bicarbonate; a higher measured value means a second, respiratory problem. The '
               'albumin-corrected anion gap and delta ratio uncover mixed disorders.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Step</th><th>What it does</th><th>What it does not do</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Calcium</td><td>Restores the gap between resting and threshold potential</td><td>Lower potassium</td></tr>\n'
               '<tr><td>Insulin-glucose, salbutamol</td><td>Shift potassium into cells for some hours</td><td>Remove potassium; can cause '
               'late hypoglycemia</td></tr>\n'
               '<tr><td>Binder, dialysis</td><td>Remove potassium from the body</td><td>Act within minutes (binder) or happen without a '
               'chair (dialysis)</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Calcium buys minutes, shifting buys hours, removal ends the emergency. A plan that stops at the first two has not '
               'finished.}}\n'
               '<div class="tc-scene"><span class="tc-lab">By Viber, 7:15 a.m. &middot; fictional</span><p>Dr. Ilagan, the physician on '
               'duty, sends you photos of two electrocardiograms. Mrs. Cortez, potassium 6.4, has tall peaked T waves. Mr. Ocampo, '
               'potassium 7.1, has a wide QRS. &ldquo;The higher one first?&rdquo; he asks.</p><p>Both have ECG changes, so both get calcium '
               'now; the wide QRS means his removal cannot wait.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> The electrocardiogram tells you what potassium is doing to the heart now. Act '
               'on it, then remove the potassium.</p></div>\n'
               '\n'
               '{{fig:an06_a}}\n'
               '\n'
               '{{fig:an06_c}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Hyperkalemia.</strong> The UK Kidney Association (UKKA) guideline, updated July 2026, uses the GRADE system. It '
               'suggests 30 mL of 10% calcium gluconate over 10 minutes when the ECG shows hyperkalemia (2C; calcium chloride in '
               'resuscitation). It recommends 10 units of soluble insulin in 25 g of glucose '
               'for potassium &ge;6.5 mmol/L (1B), followed by 10% glucose at 50 mL an hour for 5 hours when the pre-treatment glucose is '
               'below 7.0 mmol/L (2B), with glucose checked through 6 hours (1C). Nebulized salbutamol 10&ndash;20 mg is an adjunct and is '
               'never used alone (1A). Sodium zirconium cyclosilicate is used in severe hyperkalemia (1B); calcium resonium no longer '
               'routinely (2B). Hemodialysis patients with '
               'potassium &ge;6.5 mmol/L receive dialysis urgently (1A), and calcium is still given for toxic ECG changes even when dialysis '
               'is immediately available (1C). Potassium is rechecked at 1, 2, 4, 6 and 24 hours (2C).[[an06_1]] Most grades rest on low or '
               'moderate certainty: sensible protocol, not proven survival benefit.</p>\n'
               '<p><strong>When to dialyze.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 guideline advises emergent kidney replacement therapy for life-threatening changes in '
               'fluid, electrolyte and acid-base balance (ungraded).[[an06_3]] For poisonings, the Extracorporeal Treatments in Poisoning (EXTRIP) workgroup publishes '
               'toxin-specific criteria for extracorporeal removal, including toxic alcohols.[[an06_4]]</p>\n'
               '<p><strong>Hyponatremia.</strong> The 2014 European guideline recommends 150 mL of 3% saline over 20 minutes for severely '
               'symptomatic hyponatremia, repeated up to twice more until sodium rises 5 mmol/L, then a limit of 10 mmol/L in the first 24 '
               'hours and 8 mmol/L in each 24 hours after.[[an06_5]] A 2025 meta-analysis pooled 16 cohort studies with 11,811 '
               'hospitalized adults. Faster correction (&ge;8&ndash;10 mmol/L a day) was associated with 32 fewer in-hospital deaths per '
               '1,000 patients than slow correction, at moderate certainty, and was not associated with a significant rise in osmotic '
               'demyelination.[[an06_2]] The studies were observational, and sicker patients may have been corrected more slowly. The finding '
               'argues against needless caution, not against the ceiling.</p>\n'
               '{{key:Keep the source&rsquo;s own grade next to each dose. A 2C suggestion and a 1A recommendation deserve different '
               'confidence at 3 a.m.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Hyperkalemia by phone.</strong> Confirm it is not hemolysis, but act on ECG changes at once. Tell the POD what to '
               'give and in what order: monitor, calcium, insulin-glucose with salbutamol, a binder. Then solve the chair: for an anuric '
               'patient, removal means dialysis today, here or at a hospital that can do it now. Name who reads the 1, 2, 4 and 6 hour '
               'potassium and the glucose checks.</p>\n'
               '<p><strong>Hyponatremia on a ward.</strong> Severe symptoms get 150 mL boluses of 3% saline aiming for a 5 mmol/L rise. '
               'Then write the 24-hour ceiling in the order, check sodium every 2&ndash;4 hours, and watch for a water diuresis as the cause '
               'resolves. Have the rescue ready: desmopressin with 5% '
               'dextrose to bring sodium back down if the limit is crossed. The ward team holds the patient overnight, so leave the numbers in '
               'writing.</p>\n'
               '<p><strong>Acid-base.</strong> Treat the cause; no routine bicarbonate for lactic acidosis. An anion gap with an osmolal gap '
               'is a toxic alcohol until proven otherwise.</p>\n'
               '\n'
               '{{fig:an06_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">By phone, the sodium that rose too fast &middot; fictional</span><p>A ward resident '
               'calls at noon. Mrs. Abad, admitted with a sodium of 112 mmol/L after a thiazide, received 3% saline at 6 a.m. Her sodium is '
               'now 121, and she has passed 1.5 liters of dilute urine since morning.</p><p>Nine mmol/L in six hours is close to the daily '
               'limit, and the water diuresis will push it higher. You ask the team to stop all saline, measure sodium every 2 hours, and '
               'prepare desmopressin with 5% dextrose, and text the plan to the internist of record.</p><p class="tc-scene-take"><b>What this shows.</b> When the cause of hyponatremia goes away, '
               'the kidney can overcorrect faster than any infusion.</p></div>\n'
               '{{key:Before you hang up, the caller should be able to repeat three things: what to give now, how the problem leaves the '
               'body, and the number that makes them call you back.}}\n'
               '{{call:<ul><li>Wide QRS, bradycardia or sine wave with high potassium</li><li>Hyponatremia with seizure or reduced '
               'consciousness</li><li>Urine output surging during hyponatremia correction</li><li>Anion gap acidosis with an osmolal gap '
               '(toxic alcohol; consider EXTRIP criteria and urgent hemodialysis)</li></ul>}}\n')],
 'debrief': ['<p><strong>The next ten minutes.</strong> This is an emergency, and Dr. Salonga should treat it as one. He puts Mr. Ocampo '
             'on a cardiac monitor and gives 30 mL of 10% calcium gluconate intravenously over 10 minutes, then rechecks the ECG. He gives '
             '10 units of soluble insulin with 25 g of glucose, nebulized salbutamol as an adjunct, and a potassium binder.</p>\n'
             '<p><strong>Can dialysis wait?</strong> No. Calcium and shifting drugs buy minutes to hours; an anuric man cannot excrete '
             'potassium, and the UKKA guideline recommends urgent dialysis at &ge;6.5 mmol/L. Ask the head nurse to move a stable '
             'patient&rsquo;s start time or add an end-of-day session, or transfer him. Do not send him home. Recheck potassium at 1 and 2 '
             'hours and glucose through 6 hours.</p>\n'
             '<p><strong>Next time.</strong> The cause was transport and money. Ask the social worker about fare support or a unit closer '
             'to home, and write that a missed session means a same-day call.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Recognizes ECG toxicity', False),
                      ('Orders correct calcium and insulin-glucose doses with glucose monitoring', False),
                      ('Assigns definitive removal with a time', False),
                      ('Writes a sodium-correction ceiling and rescue plan', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which disposition is appropriate for potassium 7.1 mmol/L with a broad QRS in an HD patient?',
           ['Wait for the routine session',
            'Emergency monitored management and same-day dialysis',
            'Repeat an outpatient sample tomorrow',
            'Give oral binder and discharge'],
           1,
           'ECG toxicity signals immediate arrhythmia risk. The UKKA guideline recommends urgent dialysis for HD patients with potassium '
           '&ge;6.5 mmol/L.'),
          ('What must be anticipated when correcting chronic severe hyponatremia?',
           ['Overcorrection risk and a serial monitoring plan with a rescue strategy',
            'A fixed correction rate for all patients',
            'No monitoring once symptoms improve',
            'Routine use of 3% saline until sodium is normal'],
           0,
           'Duration, risk factors and an evolving water diuresis determine safety.'),
          ('Why is a 10% glucose infusion added after insulin-glucose when baseline glucose is below 7 mmol/L?',
           ['To raise the calcium level',
            'To push more potassium into cells',
            'To treat hyponatremia',
            'To prevent delayed hypoglycemia, which can occur hours after insulin'],
           3,
           'Insulin&rsquo;s effect outlasts the 25 g glucose, especially in chronic kidney disease (CKD) with reduced insulin clearance. '
           'UKKA suggests 10% glucose at 50 mL/h for 5 hours (2B).'),
          ('Which treatment actually removes potassium from the body?',
           ['IV insulin with glucose', 'Calcium gluconate', 'Hemodialysis', 'Nebulized salbutamol'],
           2,
           'Calcium protects the membrane, insulin and salbutamol shift potassium; only the gut, the kidney or dialysis remove it.'),
          ('HCO&#8323;&#8315; 12 mmol/L with pCO&#8322; 38 mm Hg indicates:',
           ['Appropriate respiratory compensation',
            'Metabolic acidosis with a concomitant respiratory acidosis',
            'Primary respiratory alkalosis',
            'Pure metabolic alkalosis'],
           1,
           'Winter&rsquo;s formula predicts pCO&#8322; of 26 &plusmn; 2; a value of 38 means ventilation is inadequate.')],
 'terms': [('ECG', 'Electrocardiogram'),
           ('POD', 'Physician on duty'),
           ('Na-K ATPase', 'Sodium-potassium pump'),
           ('IV', 'Intravenous'),
           ('CKD', 'Chronic kidney disease'),
           ('HD', 'Hemodialysis'),
           ('ESKD', 'End-stage kidney disease'),
           ('UKKA', 'UK Kidney Association'),
           ('GRADE', 'Grading of Recommendations Assessment, Development and Evaluation'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('EXTRIP', 'Extracorporeal Treatments in Poisoning workgroup')],
 'readings': [('potassium-hyperkalemia-ckd.html', 'Potassium & Hyperkalemia in CKD'),
              ('dysnatremia.html', 'Dysnatremia: When Blood Sodium Is Too Low or Too High'),
              ('metabolic-acidosis-ckd.html', 'Metabolic Acidosis in CKD')],
 'calcs': ['calc-sodium-correction-rate.html',
           'calc-dysnatremia-toolkit.html',
           'calc-anion-gap-acid-base.html',
           'calc-winters-formula.html',
           'calc-osmolal-gap.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
