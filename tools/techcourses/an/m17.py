# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 17: Peritoneal dialysis prescription and home follow-up.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Trial figures checked against the PubMed abstracts (ADEMEX, Lo 2003 Hong Kong trial)."""

MODULE = {'image_alt': 'A woman sets up a home dialysis cycler at her bedside in the evening.',
 'objectives': ['Design goal-directed peritoneal dialysis (PD) with the patient around residual function and daily life.',
                'Separate peritoneal transport assessment from clinical adequacy.',
                'Teach home red flags and confirm 24-hour access to the PD team.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>The Philippine '
        'Society of Nephrology (PSN) hemodialysis guidelines do not cover peritoneal dialysis, but the same duties carry over: a prescription '
        'that is yours (b4) and long-term planning with the patient (b9).[[an01_1]]</div>\n'
        '{{plain:Picture a small home water filter fitted under the kitchen sink. It runs all day, slowly. It works well only if the family '
        'actually changes the cartridge on schedule, and only if the house still gets some clean water from the main line.}}\n'
        '<p>The picture has a limit. A filter cartridge is identical from house to house. The peritoneum is not: each patient&rsquo;s membrane '
        'moves solutes and water at its own speed, and that speed decides how long each dwell can work. The &ldquo;main line&rdquo; is the '
        'patient&rsquo;s residual kidney function, which often carries a large share of the load early in PD and fades with time.</p>\n'
        '{{cards:Key numbers|Transport test::Peritoneal equilibration test (PET): dialysate-to-plasma creatinine ratio at 4 hours|Adequacy '
        'approach (ISPD 2020)::Goal-directed; Kt/V is one input, not the target|ADEMEX::965 patients; raising peritoneal clearance did not '
        'change survival (relative risk 1.00)}}\n'
        '<p>Most of your PD patients live at home, some far from your clinic, and see you every one to three months. Day to day, the PD nurse '
        'and the phone carry their care. Your work in this module is to write a prescription the patient can actually deliver at home, to read '
        'the home log for the first signs that it has stopped fitting, and to protect the urine the patient still makes.</p>\n',
 'case': {'title': 'The midday exchange that never happens',
          'html': '<p>You follow a few patients on peritoneal dialysis (PD) through a hospital program, and you see them in your clinic '
                  'every month. Ms. Herrera, 44, is a bank teller on continuous ambulatory peritoneal dialysis (CAPD), four exchanges a '
                  'day. Over three months her urine output has fallen from 800 to 250 mL a day. She is tired, her ankles are swollen, and '
                  'she has gained 2 kilograms.</p>\n'
                  '<p>The PD nurse sends you photos of her exchange log on Viber before clinic. On workdays the midday exchange is blank. '
                  '&ldquo;She says she cannot do it in the bank restroom,&rdquo; the nurse writes. In clinic, Ms. Herrera says quietly, '
                  '&ldquo;Maybe I should just move to the machine at the unit, Doc. I am failing at this.&rdquo;</p>\n',
          'questions': ['What two things have changed?',
                        'Is she failing at peritoneal dialysis, or is the prescription failing her?',
                        'What would you change, and how would you protect the urine she still makes?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>In PD the peritoneal capillaries are the blood side of the dialyzer, and the fluid in the abdomen is the dialysate. Small '
               'solutes such as urea and creatinine diffuse from the capillaries into the dialysate down their concentration gradients. Water '
               'moves by osmosis, pulled by glucose or by the large icodextrin molecule.</p>\n'
               '<p>Water takes two routes. Small pores carry water together with small solutes. Aquaporins carry free water only. Early in a '
               'hypertonic dwell, aquaporins move water faster than sodium can follow, so dialysate sodium falls for a while. This is sodium '
               'sieving, and it is established physiology.</p>\n'
               '<p>The speed of the membrane decides the dwell. The peritoneal equilibration test (PET) measures it as the '
               'dialysate-to-plasma creatinine ratio at 4 hours.[[an17_1]] A fast transporter equilibrates quickly. Small solutes clear well, '
               'but glucose is absorbed quickly too, the osmotic gradient disappears early, and fluid flows back into the body late in a long '
               'dwell. A slow transporter keeps the gradient but needs longer dwells to clear solutes.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Membrane</th><th>What happens in a long glucose dwell</th><th>What you see in the log</th><th>Usual fix</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Fast transporter</td><td>The glucose gradient fades early; fluid is reabsorbed</td><td>Low or negative drain volume '
               'after the overnight or daytime long dwell</td><td>Shorter dwells, or icodextrin for the long dwell</td></tr>\n'
               '<tr><td>Slow transporter</td><td>The gradient holds, but solutes clear slowly</td><td>Good drain volumes; rising symptoms as '
               'urine output falls</td><td>Longer dwells; review total clearance</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Transport type decides how long a dwell can work. Residual kidney function decides how much the dialysis has to do.}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the PD clinic &middot; fictional</span><p>Mrs. Lacson, a fast transporter on '
               'her peritoneal equilibration test, drains less than she infuses after her long overnight dwell.</p><p>Her membrane absorbs '
               'glucose quickly, so the osmotic gradient disappears early in the dwell, and fluid flows back. You change the long dwell to '
               'icodextrin, whose large molecules hold the gradient for many hours.</p><p class="tc-scene-take"><b>What this shows.</b> '
               'Read the drain volume of the long dwell first. It tells you the membrane&rsquo;s speed before any test does.</p></div>\n'
               '\n'
               '{{fig:an17_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Clearance targets.</strong> Two randomized trials tested whether more peritoneal small-solute clearance helps '
               'patients live longer. ADEMEX randomized 965 Mexican patients on CAPD to their usual four 2-liter exchanges or to a '
               'prescription raised to reach a peritoneal creatinine clearance of 60 L per week per 1.73 m&sup2;. Survival did not differ '
               '(relative risk of death 1.00; 2-year survival 68.3% versus 69.3%).[[an17_2]] A Hong Kong trial randomized 320 new CAPD '
               'patients to total Kt/V targets of 1.5&ndash;1.7, 1.7&ndash;2.0, or above 2.0. Two-year survival did not differ (87.3%, '
               '86.1%, and 81.5%), but the lowest-target group had more clinical problems, more withdrawals by physicians, and more severe '
               'anemia.[[an17_5]] Kt/V is a surrogate. These trials show that pushing it higher does not buy survival; they do not show that '
               'any number is safe.</p>\n'
               '<p><strong>Goal-directed PD.</strong> The International Society for Peritoneal Dialysis (ISPD) 2020 practice recommendations '
               'build on these results. They ask you to prescribe PD through shared decisions with the patient, based on the patient&rsquo;s '
               'goals, symptoms, volume status, and nutrition. Kt/V and creatinine clearance remain part of the assessment, but they are no '
               'longer the definition of adequacy.[[an17_6]][[an17_1]]</p>\n'
               '<p><strong>Residual function.</strong> Starting with fewer exchanges while urine output is preserved (incremental PD), and '
               'protecting that urine with diuretics and renin-angiotensin system (RAS) blockade, are supported mostly by observational data '
               'and by mechanism. Treat them as reasonable, low-cost steps, not proven outcome benefits.</p>\n'
               '<p><strong>Coverage.</strong> In the Philippines, PD supplies and services can be covered under the Philippine Health Insurance '
               'Corporation (PhilHealth) Z Benefits package for PD, delivered through accredited facilities.[[an17_3]][[an17_4]] Package '
               'details change; confirm them on the date of service. What the patient pays beyond the package shapes what they can do at '
               'home.</p>\n'
               '{{key:A higher Kt/V is not a better patient. Ask whether the prescription controls symptoms and volume, and whether the patient '
               'can deliver it.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Agree the goals, then the prescription.</strong> Ask what matters: work hours, sleep, who helps at home, how far the '
               'patient lives from the unit. Then choose CAPD or automated peritoneal dialysis (APD), the dwell pattern, and the solutions. '
               'Write the prescription so the PD nurse and the patient can follow it without calling you.</p>\n'
               '<p><strong>Review from the log.</strong> Between visits, the PD nurse or the patient will send you photos of the exchange log, '
               'weights, and blood pressures by Viber. Agree in advance what you want sent and when. At each review, look for missed dwells, '
               'drain volume per dwell, weight, blood pressure, edema, and residual urine output. A falling drain volume or a skipped exchange '
               'is the earliest sign the plan has stopped fitting.</p>\n'
               '<p><strong>Protect residual function.</strong> Avoid nephrotoxins, including the nonsteroidal anti-inflammatory drugs patients '
               'buy over the counter. Consider RAS blockade, and use loop diuretics to keep urine volume up. Tell the referring internist and any '
               'other prescriber that the patient still makes urine and why it matters.</p>\n'
               '<p><strong>Plan for distance.</strong> Many PD patients live in the provinces. Confirm how supplies reach the home and what '
               'happens if a delivery is late. Teach the patient to call the same day for cloudy effluent, abdominal pain, fever, exit-site pus, '
               'or poor drainage, and test the after-hours number yourself. Check the PhilHealth PD package requirements separately from the '
               'clinical plan.[[an17_3]]</p>\n'
               '\n'
               '{{fig:an17_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">Reading the exchange log &middot; fictional</span><p>You read Mr. '
               'Aquino&rsquo;s log line by line. Drain volumes fall on weekends, when he visits his mother in the province and skips the '
               'evening exchange. His weight is up 1.5 kilograms on Mondays.</p><p>You ask him what would make the weekend work. He chooses to '
               'bring supplies and do the exchange at his mother&rsquo;s house, and the PD nurse arranges a video check of his technique '
               'there.</p><p class="tc-scene-take"><b>What this shows.</b> The prescription that fits the patient&rsquo;s life is the one '
               'that gets delivered.</p></div>\n'
               '{{key:Read the log before you read the laboratory results. Missed exchanges and falling drain volumes tell you first.}}\n'
               '{{call:<ul><li>Falling urine output with new edema</li><li>Repeated missed exchanges</li><li>Poor drainage or one-way '
               'obstruction</li><li>Weight loss with low albumin</li><li>Supplies not delivered on time</li></ul>}}\n')],
 'debrief': ['<p><strong>Two changes.</strong> Her own kidneys are doing less, and the prescription is not being delivered. Early in PD, '
             'residual kidney function often does a large share of the work, so when urine output falls, a missed exchange that used to be '
             'tolerable becomes fluid overload. Check her volume, look for constipation and catheter position (both can slow drainage), '
             'and review her medicines for anything harmful to the kidneys.</p>\n'
             '<p><strong>Is she failing?</strong> No. Tell her so plainly. Under the ISPD 2020 recommendations, adequacy is goal-directed: '
             'the prescription should fit her life, her symptoms, and her volume, with Kt/V as one input among several. A plan that needs an '
             'exchange in a bank restroom does not fit her life.</p>\n'
             '<p><strong>What to change.</strong> Consider automated PD at night, with an icodextrin dwell during the day. Icodextrin pulls '
             'water by a large-molecule gradient that lasts through a long dwell, so the day stops competing with her job. Add a loop diuretic '
             'to keep her urine volume up, avoid nephrotoxic drugs, and continue RAS blockade if she tolerates it. The evidence that these '
             'steps preserve residual function is mostly observational, but the mechanism is sound and the cost is low. Ask what the cycler '
             'and icodextrin will cost her beyond her PhilHealth package before you write the order, agree on the plan with her and the PD '
             'nurse, and ask the nurse to send you her first week of cycler logs.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Reviews home logs', False),
                      ('Identifies one modifiable barrier', False),
                      ('Documents monitoring and after-hours contact instructions', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which information is essential in a PD review?',
           ['A clearance figure in isolation',
            'Symptoms, fluid balance, residual function and delivered exchanges',
            'The delivery schedule alone',
            'The catheter brand'],
           1,
           'Goal-directed assessment brings together what is delivered, residual clearance, and how the patient is doing.'),
          ('How should the team respond to recurring missed exchanges?',
           ['Identify practical barriers and redesign support with the patient',
            'Assume deliberate nonadherence',
            'Prescribe extra exchanges without discussing feasibility',
            'Transfer to hemodialysis (HD) immediately'],
           0,
           'Schedule, training, and supply barriers are common and fixable; a prescription the patient cannot deliver does not work.'),
          ('A fast transporter on a long glucose dwell is most likely to experience:',
           ['Improved phosphate clearance with no downside',
            'Excess ultrafiltration',
            'Hypernatremia from sodium sieving only',
            'Fluid reabsorption and poor ultrafiltration'],
           3,
           'The glucose gradient dissipates quickly, so fluid is reabsorbed late in the dwell; icodextrin helps.'),
          ('What did ADEMEX show about peritoneal small-solute clearance?',
           ['Kt/V below 1.0 is safe for all',
            'Higher Kt/V halved mortality',
            'Raising peritoneal clearance above moderate levels did not improve survival',
            'Only residual function matters, so no dialysis is needed'],
           2,
           'The relative risk of death was 1.00. This supports goal-directed rather than number-driven prescribing.'),
          ('Why does an early hypertonic dwell cause sodium sieving?',
           ['Sodium is actively pumped into the peritoneum',
            'Aquaporins move free water without sodium early in the dwell',
            'Glucose binds sodium',
            'Lymphatics absorb only water'],
           1,
           'Water crosses through aquaporins faster than sodium diffuses, lowering dialysate sodium for a while.')],
 'terms': [('PD', 'Peritoneal dialysis'),
           ('UF', 'Ultrafiltration'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('BP', 'Blood pressure'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis'),
           ('APD', 'Automated peritoneal dialysis'),
           ('PET', 'Peritoneal equilibration test'),
           ('RAS', 'Renin-angiotensin system'),
           ('PSN', 'Philippine Society of Nephrology'),
           ('PhilHealth', 'Philippine Health Insurance Corporation')],
 'readings': [('peritoneal-dialysis-ckd.html', 'Peritoneal Dialysis: Your Complete Guide')],
 'calcs': ['calc-pd-adequacy.html', 'calc-pd-glucose-absorption.html', 'calc-measured-crcl.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
