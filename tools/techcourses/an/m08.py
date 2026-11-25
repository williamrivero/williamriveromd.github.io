# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 08: CRRT delivery.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Figures checked against the PubMed abstracts (RENAL, VA/NIH ATN, RICH), the KDIGO 2012 AKI guideline, and
Schneider 2017 (citrate accumulation)."""

MODULE = {'image_alt': 'A continuous dialysis machine with fluid bags and a mounted filter beside an ICU bed.',
 'objectives': ['Audit prescribed versus delivered effluent dose and fluid balance.',
                'Adjust drug dosing and anticoagulation to delivered therapy.',
                'Identify when toxicology, apheresis or a stopping trial is appropriate.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you provide the dialysis prescription (b4) and stay in active management with '
        'the team that delivers it (b7).[[an01_1]]</div>\n'
        '{{plain:A continuous kidney replacement therapy (CRRT) order is like a jeepney route that should run all day. If the jeepney '
        'breaks down three times and stops for an hour at the terminal, the passengers it was meant to carry are still waiting, whatever '
        'the schedule on the wall says.}}\n'
        '<p>The picture has a limit. In CRRT, driving faster later does not fix a clotting filter, and the drugs were dosed for clearance '
        'the patient may not be getting. What matters is what was delivered.</p>\n'
        '{{cards:Key numbers|Delivered effluent dose (KDIGO 2012, 1A)::20&ndash;25 mL/kg/h; prescribe higher to cover downtime|RENAL and '
        'VA/NIH ATN::Higher intensity, no survival benefit|Citrate accumulation signal::Total-to-ionized calcium ratio &gt;2.5|RICH, '
        'median filter life::47 h citrate vs 26 h heparin|RICH, bleeding::5.1% citrate vs 16.9% heparin}}\n'
        '<p>In the Philippines, CRRT runs mainly in tertiary ICUs, often staffed by a dialysis unit&rsquo;s nurses, and the family '
        'usually pays for every bag and filter. Your work is to turn the flowsheet into four numbers a day, fix delivery before raising '
        'the dose, and make the drugs follow the real clearance.</p>\n',
 'case': {'title': 'The filter that keeps clotting',
          'html': '<p>Your unit staffs the continuous kidney replacement therapy service at a partner hospital&rsquo;s intensive care unit '
                  '(ICU). On your morning round, the nurse shows you the flowsheet for Mr. Lim, 70 kg, who is on continuous venovenous '
                  'hemodiafiltration for acute kidney injury (AKI) after cardiac surgery.</p>\n'
                  '<p>The prescription is 2,100 mL/hour of effluent. In the last 24 hours the filter clotted three times, and with priming '
                  'and a trip to computed tomography (CT) he received only 12 hours of treatment. He is on systemic heparin at a low dose '
                  'because of a bleeding drain. His meropenem was dosed by the ICU pharmacist &ldquo;for full-time CRRT.&rdquo; His '
                  'daughter asks how many more filters she should buy. The nurse asks, &ldquo;Doctor, should we just increase the effluent '
                  'to make up for it?&rdquo;</p>\n',
          'questions': ['How much treatment did he actually receive?',
                        'Should you raise the dose to make up for lost hours?',
                        'What happens to his antibiotic when the machine stops and starts?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>In CRRT, small-solute clearance is close to the effluent flow rate, so the dose is written in mL/kg/h and downtime cuts it '
               'in proportion. Pre-dilution thins the blood before the filter, extending filter life but lowering clearance; '
               'post-dilution keeps clearance high but concentrates the blood in the filter.</p>\n'
               '<p>The filtration fraction is ultrafiltration divided by plasma flow; above a commonly used working limit of about '
               '20&ndash;25%, blood thickens in the filter and clots.</p>\n'
               '<p>Regional citrate binds ionized calcium in the circuit and stops the clotting cascade there. The liver turns returning '
               'citrate into bicarbonate. When the liver cannot, citrate builds up: total calcium rises while ionized calcium falls, and '
               'acidosis worsens. A total-to-ionized calcium ratio above 2.5 is the usual bedside signal.[[an08_7]]</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Problem</th><th>Mechanism</th><th>What you see on the flowsheet</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Downtime</td><td>Clearance lost for every hour off</td><td>Run time well under 24 hours</td></tr>\n'
               '<tr><td>High filtration fraction</td><td>Blood thickens in the filter</td><td>Filters clotting within hours</td></tr>\n'
               '<tr><td>Citrate accumulation</td><td>Liver cannot metabolize citrate</td><td>Total-to-ionized calcium ratio rising, '
               'acidosis worsening, more calcium needed</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Filter life is a dose problem. Every clotted filter is lost treatment time, and in the Philippines it is also a cost the '
               'family pays.}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the CRRT machine &middot; fictional</span><p>The night nurse sends you a photo '
               'of a filter that clotted after 7 hours. The filtration fraction on the screen is 31%.</p><p>You call back: raise the blood flow, '
               'move part of the replacement fluid before the filter, and review the anticoagulation.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> Most clotted filters have a cause you can read off the screen.</p></div>\n'
               '\n'
               '{{fig:an08_b}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Dose.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 guideline recommends delivering an '
               'effluent volume of 20&ndash;25 mL/kg/h for CRRT in AKI (1A), adds that this usually requires a higher prescription '
               '(ungraded), and recommends frequent assessment of the delivered dose (1B).[[an08_1]] Two large trials sit behind the '
               'ceiling. RENAL randomized 1,508 patients to 40 or 25 mL/kg/h; 90-day mortality was 44.7% in both groups.[[an08_3]] The '
               'Veterans Affairs and National Institutes of Health (VA/NIH) Acute Renal Failure Trial Network (ATN) study randomized 1,124 patients to intensive or less-intensive support (35 '
               'versus 20 mL/kg/h for continuous therapy); day-60 mortality was 53.6% versus 51.5%, with no difference in kidney '
               'recovery.[[an08_2]] More dose did not save lives.</p>\n'
               '<p><strong>Anticoagulation.</strong> KDIGO 2012 suggests regional citrate rather than heparin for CRRT in patients without '
               'contraindications (2B).[[an08_1]] The RICH trial randomized 596 completed patients in Germany. Median filter life was 47 '
               'hours with citrate and 26 with heparin. Bleeding complications were 5.1% versus 16.9%, but new infections were more common '
               'with citrate (68.0% versus 55.4%). The trial stopped early and was underpowered for mortality, which did not differ '
               'significantly.[[an08_4]]</p>\n'
               '<p><strong>Poisoning.</strong> The Extracorporeal Treatments in Poisoning (EXTRIP) workgroup publishes toxin-specific '
               'recommendations for extracorporeal removal, for example for lithium, salicylates, metformin-associated lactic acidosis and '
               'toxic alcohols.[[an08_5]]</p>\n'
               '{{key:The target is delivered, not prescribed: 20&ndash;25 mL/kg/h. Going above it buys no survival in the trials.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Read four numbers every morning.</strong> Hours run, delivered effluent in mL/kg/h, filter life, and net fluid '
               'removed against the target, with the cause of each interruption. Off site, ask the nurse to send these four numbers.</p>\n'
               '<p><strong>Fix delivery before raising the dose.</strong> If the delivered dose falls below 20 mL/kg/h, check catheter '
               'position and flows, the filtration fraction, and the anticoagulation first. With a bleeding risk and repeated clotting, '
               'consider citrate if the liver can clear it.</p>\n'
               '<p><strong>Make the drugs follow the clearance.</strong> Under-dosing beta-lactams and vancomycin in sepsis is the more common '
               'error.</p>\n'
               '<p><strong>Know when to stop or call others.</strong> Involve toxicology early for poisonings, and refer suspected thrombotic '
               'thrombocytopenic purpura (TTP) to hematology for plasma exchange. Try stopping CRRT when urine output recovers and the '
               'indication has resolved, with a defined observation period. Tell the family what each day costs and why.</p>\n'
               '\n'
               '{{fig:an08_a}}\n'
               '<div class="tc-scene"><span class="tc-lab">On the morning round &middot; fictional</span><p>You write four numbers on Mr. '
               'Lim&rsquo;s chart each morning: hours run, delivered effluent in mL/kg/hour, filter life, and net fluid removed against the '
               'target. On day three, after citrate, the delivered dose reaches 23 mL/kg/hour, and the pharmacist re-doses meropenem.</p><p class="tc-scene-take"><b>What this shows.</b> What gets '
               'written down every morning gets fixed.</p></div>\n'
               '{{key:Four numbers a day, written by you: run time, delivered dose, filter life, net fluid. They tell you what to fix next.}}\n'
               '{{call:<ul><li>Filter life repeatedly under 12 hours</li><li>Rising total-to-ionized calcium ratio with worsening '
               'acidosis</li><li>Antibiotic doses based on an assumed, not delivered, dose</li><li>Thrombocytopenia with hemolysis on CRRT '
               '(consider TTP or heparin-induced thrombocytopenia)</li></ul>}}\n')],
 'debrief': ['<p><strong>The arithmetic.</strong> The prescribed dose is 2,100 &divide; 70 = 30 mL/kg/hour. Delivered over 24 hours, it is '
             'about 15 mL/kg/hour, half the order and below the 20 to 25 mL/kg/hour that KDIGO recommends delivering.</p>\n'
             '<p><strong>Raise the dose?</strong> Not first. Fix the delivery. Check the catheter position and flows, review the filtration '
             'fraction, and review the anticoagulation. With a bleeding drain and repeated clotting, regional citrate is the better choice '
             'if his liver can clear it; watch the total-to-ionized calcium ratio. Then reassess whether the prescription covers the '
             'downtime you expect.</p>\n'
             '<p><strong>The antibiotic.</strong> Dosed for continuous treatment, meropenem is too much while the machine is off and may be too '
             'little when it runs. Dose it to the clearance he actually gets.</p>\n'
             '<p><strong>The daughter&rsquo;s question.</strong> Fewer clotted filters is the honest answer. Tell her what you are changing, '
             'and write the trigger for switching to intermittent therapy.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Calculates delivered treatment time and dose', False),
                      ('Reviews downtime causes with the intensive care unit (ICU) team', False),
                      ('Confirms a medication review', False),
                      ('States stopping criteria', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which measure best reveals a delivery gap?',
           ['The signed prescription alone',
            'Actual run time and delivered effluent dose',
            'The number of replacement fluid bags ordered',
            'The dialysate brand'],
           1,
           'Interruptions can greatly reduce delivered treatment despite a correct order; KDIGO recommends frequent assessment of the '
           'delivered dose (1B).'),
          ('Which team should review drug exposure after an unexpected CRRT interruption?',
           ['The treating team with pharmacy input',
            'The billing team alone',
            'No further review if the order is unchanged',
            'The water treatment technician'],
           0,
           'Delivered therapy affects drug clearance and can change exposure.'),
          ('A 70-kg patient receives 2,100 mL/h effluent for 12 of 24 hours. What is the delivered dose?',
           ['45 mL/kg/h', '30 mL/kg/h', '25 mL/kg/h', 'About 15 mL/kg/h'],
           3,
           '2,100 &times; 12 / 24 / 70 = 15 mL/kg/h, below the 20&ndash;25 mL/kg/h target.'),
          ('During regional citrate anticoagulation, a total-to-ionized calcium ratio of 2.8 with worsening acidosis suggests:',
           ['Normal citrate kinetics',
            'Inadequate citrate dose',
            'Citrate accumulation from impaired metabolism',
            'Hypercalcemia from bone resorption'],
           2,
           'Unmetabolized citrate binds ionized calcium while total calcium rises, widening the ratio above 2.5.'),
          ('What did the RENAL and ATN trials show about CRRT intensity?',
           ['Doubling the dose halved mortality',
            'Higher intensity did not improve survival compared with standard intensity',
            'Lower intensity was harmful at 20 mL/kg/h',
            'Intensity only mattered in sepsis'],
           1,
           'RENAL: 44.7% mortality in both arms. ATN: 53.6% versus 51.5%. Both support a delivered 20&ndash;25 mL/kg/h without '
           'escalation.')],
 'terms': [('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('AKI', 'Acute kidney injury'),
           ('ICU', 'Intensive care unit'),
           ('CT', 'Computed tomography'),
           ('CRRT', 'Continuous kidney replacement therapy'),
           ('ATN', 'VA/NIH Acute Renal Failure Trial Network study'),
           ('EXTRIP', 'Extracorporeal Treatments in Poisoning workgroup'),
           ('TTP', 'Thrombotic thrombocytopenic purpura'),
           ('RICH', 'Regional citrate versus heparin trial')],
 'readings': [('crrt-continuous-renal-replacement-therapy.html', 'Continuous Renal Replacement Therapy (CRRT): A Clinical Reference')],
 'calcs': ['calc-crrt-dose.html',
           'calc-crrt-flowsheet.html',
           'calc-crrt-uf-rate.html',
           'calc-vancomycin-auc.html',
           'calc-renal-abx-dosing.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
