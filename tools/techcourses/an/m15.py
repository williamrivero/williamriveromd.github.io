# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 15: Hemodialysis emergencies and shared hazards.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice (attending off site, physician on duty and nurses at the chair). MyTEMP and the 2025 cooled-dialysate
meta-analysis checked against PubMed abstracts."""

MODULE = {'image_alt': 'A physician on duty walks between dialysis stations in a bright unit, with an emergency cart nearby.',
 'objectives': ['Support immediate bedside action for hypotension, hemolysis, air embolism, reactions and arrhythmia.',
                'Distinguish individual from shared hazards and trigger a unit-level response.',
                'Document the event, the disposition and the learning.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the Philippine '
        'Society of Nephrology (PSN) guidelines, you coordinate with the nurses and the physician on duty during emergencies '
        '(b8).[[an15_1]] Unit-wide hazards are led by the clinical head; your patients are yours.</div>\n'
        '{{plain:One sick passenger on a bus is a medical problem. Ten passengers getting sick at the same time is a problem with the bus: '
        'the fuel, the air, the food everyone ate at the last stop.}}\n'
        '<p>The picture has a limit. In a dialysis unit, the shared supply is not air or food but water, dialysate, and a batch of lines '
        'or dialyzers. A shared hazard reaches every patient on the loop within minutes, so a cluster changes the first question to '
        '&ldquo;who else is on this supply?&rdquo;</p>\n'
        '{{cards:Key numbers|Hemolysis rule::Do not return circuit blood|Personalized cooler dialysate (MyTEMP)::No reduction in '
        'cardiovascular death or admission (21.4% vs 22.4%)|Cooled dialysate, small trials (meta-analysis)::Intradialytic hypotension risk '
        'ratio 0.67, with more discomfort}}\n'
        '<p>You will hear about most emergencies by phone, off site. Your work is to give clear orders for your own patient, recognize a '
        'cluster at once, and hand the unit-wide response to the clinical head.</p>\n',
 'case': {'title': 'Two patients, one minute apart',
          'html': '<p>It is 10:40 on a Tuesday morning, and you are in your clinic across town. Dr. Alonzo, the physician on duty, calls '
                  'you. &ldquo;Doc, station 3 has chest pain and back pain, and the blood in his venous line looks dark, almost like wine. '
                  'Then station 7 said the same thing a minute later. Station 7&rsquo;s blood pressure is 80/50.&rdquo;</p>\n'
                  '<p>Station 3 is your patient; station 7 belongs to another attending nephrologist. Both started at 10 a.m. from the '
                  'same water loop. Twelve other patients are running. The water technician changed the carbon tanks yesterday afternoon. '
                  'Dr. Alonzo asks, &ldquo;Should I return their blood and stop?&rdquo;</p>\n',
          'questions': ['What is this until proven otherwise?',
                        'What do you tell Dr. Alonzo to do with the two patients, and with the other twelve?',
                        'Who must be told, and what must be kept?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p><strong>Hypotension.</strong> Blood pressure falls when fluid removal outpaces refill from the tissues and the vessels '
               'cannot tighten enough to compensate. Autonomic neuropathy, heart failure, warm dialysate and food during the session all '
               'weaken that compensation.</p>\n'
               '<p><strong>Hemolysis.</strong> Red cells burst when they meet hypotonic or overheated dialysate, oxidants such as '
               'chloramine, copper, or mechanical shear from a kinked line or a faulty pump. Each burst cell releases potassium. Returning '
               'the circuit blood pushes that potassium straight into the heart.</p>\n'
               '<p><strong>Air.</strong> Air entering the venous line travels to the right heart and the lungs, or across a patent foramen '
               'ovale to the brain.</p>\n'
               '<p><strong>Reactions.</strong> Dialyzer reactions range from early anaphylactoid responses to sterilants or membrane '
               'components to milder complement-mediated reactions later in the session.</p>\n'
               '{{key:Name the mechanism before you treat: volume, red cells, air or reaction. Each has a different first move.}}\n'
               '<div class="tc-scene"><span class="tc-lab">By telemedicine, warm dialysate &middot; fictional</span><p>Mr. Santos becomes '
               'hypotensive in the third hour of most sessions. His target weight was lowered last month. The dialysate is set at 37 '
               '&deg;C.</p><p>Fluid removal is outpacing refill, and warm dialysate opens his skin vessels when he needs them closed. You '
               'ask for a target-weight review, a cap on his ultrafiltration rate, and a trial of cooler dialysate, explaining that it may '
               'feel cold.</p><p class="tc-scene-take"><b>What this shows.</b> Intradialytic hypotension is fluid removal minus refill, '
               'made worse by heat and food.</p></div>\n'
               '\n'
               '{{fig:an15_b}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Emergencies.</strong> Hemolysis, air embolism and reaction management rest on physiology, case series and '
               'outbreak investigations, not trials. Outbreaks caused by chemical contaminants in the water used to make dialysate are '
               'documented, and Centers for Disease Control and Prevention (CDC) guidance treats water quality as a patient-safety system, '
               'not a utility.[[an15_5]] Holding treatments on a shared supply and investigating the water is standard practice built on '
               'that history.[[an15_4]]</p>\n'
               '<p><strong>Cooler dialysate.</strong> A 2025 meta-analysis of 31 mostly small studies found cooled dialysate associated '
               'with less intradialytic hypotension (risk ratio 0.67) and higher mean arterial pressure, but more discomfort from cold '
               '(risk ratio 1.55). The authors judged study quality limited.[[an15_6]] Blood pressure during dialysis is a surrogate. The '
               'one large outcome trial, MyTEMP, randomized 84 Ontario centers serving 15,413 patients to personalized cooler dialysate '
               '(0.5 to 0.9 &deg;C below body temperature) or 36.5 &deg;C. Cardiovascular death or admission occurred in 21.4% versus '
               '22.4% (adjusted hazard ratio 1.00), and the fall in pressure during sessions did not differ.[[an15_7]] As a unit-wide '
               'policy, cooling did not prevent cardiovascular events.</p>\n'
               '<p>UK guidance on hemodialysis addresses low blood pressure during dialysis and dialyzer reactions, and advises working '
               'closely with the patient on fluid and symptoms.[[an15_3]]</p>\n'
               '{{key:Use cooler dialysate for the patient who drops, not as a promise of fewer heart attacks.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p>Your orders by phone should be short, specific and read back.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Event</th><th>What the team sees</th><th>First moves</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Hypotension</td><td>Yawning, cramps, dimming vision, low pressure</td><td>Stop ultrafiltration, lay flat, saline '
               'bolus within protocol; review the target weight</td></tr>\n'
               '<tr><td>Hemolysis</td><td>Dark &ldquo;port-wine&rdquo; blood, chest or back pain, dyspnea</td><td>Stop the pump, clamp '
               'lines, do not return blood; urgent potassium, treat hyperkalemia, transfer</td></tr>\n'
               '<tr><td>Air embolism</td><td>Sudden dyspnea, cough, chest pain or neurologic signs after a line problem</td><td>Clamp the '
               'venous line, left side down with head down, 100% oxygen, emergency help</td></tr>\n'
               '<tr><td>Anaphylactoid reaction</td><td>Early burning, urticaria, dyspnea, hypotension</td><td>Stop, do not return blood, '
               'epinephrine and supportive care</td></tr>\n'
               '</tbody></table></div>\n'
               '<p>Whenever more than one patient is affected, the response changes. Treatments on the shared supply stop, the clinical '
               'head is called to lead, samples and logs are kept, and the event is notified as unit protocol and Department of Health '
               '(DOH) rules require. The event also belongs in the unit&rsquo;s quality records, including the standards PhilHealth uses '
               'as its reference for maintenance hemodialysis.[[an15_2]]</p>\n'
               '\n'
               '{{fig:an15_a}}\n'
               '<div class="tc-scene"><span class="tc-lab">The drill &middot; fictional</span><p>On your monthly visit you sit in on the '
               'air embolism drill the clinical head runs with the floor team. The nurse clamps the venous line in 20 seconds. Turning the '
               '&ldquo;patient&rdquo; onto the left side with the head down takes 90 seconds, because nobody knew how the chair '
               'reclined.</p><p>The team repeats the drill until it takes 30 seconds, and the chair instructions go on the wall.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> Rare emergencies are handled the way they were practiced.</p></div>\n'
               '{{key:Two patients with the same symptoms at the same time is a unit emergency. Stop the shared supply first, then '
               'investigate.}}\n'
               '{{call:<ul><li>Two or more patients with similar symptoms within minutes</li><li>Dark or cherry-red blood in the venous '
               'line</li><li>Sudden dyspnea, cough or neurologic signs after a line disconnection</li><li>Chest pain with '
               'electrocardiogram (ECG) changes during hemodialysis (HD)</li></ul>}}\n')],
 'debrief': ['<p><strong>What it is.</strong> Two patients with the same symptoms within minutes, and dark blood in the lines, is a '
             'cluster hemolysis event until proven otherwise. Think of the water first: chloramine breaking through a newly changed carbon '
             'tank is a known cause. Every patient on that water is at risk.</p>\n'
             '<p><strong>The two patients.</strong> Tell Dr. Alonzo to stop both pumps, clamp the lines, and not return the blood; it is '
             'full of potassium from broken red cells. Both go on monitors, with an urgent potassium and an electrocardiogram. Treat '
             'hyperkalemia, and transfer the hypotensive patient for monitored care.</p>\n'
             '<p><strong>The other twelve.</strong> Most are not your patients. Tell Dr. Alonzo to follow the unit protocol now: every '
             'treatment on the same water and dialysate supply is held before anyone else develops symptoms, and the clinical head is '
             'called to lead. Holding them is a unit safety decision, not a prescription for another doctor&rsquo;s patients.</p>\n'
             '<p><strong>Who is told, and what is kept.</strong> Make sure the clinical head, the water and biomedical technicians and the '
             'head nurse have been called, and offer to come in. Keep water and dialysate samples, lines, dialyzers, chlorine records and '
             'machine logs. Do not restart until the water is tested and released. Notify the DOH as protocol requires.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Uses a closed-loop call', False),
                      ('Identifies a shared-exposure trigger', False),
                      ('Documents event, actions and disposition', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What is the priority when several patients deteriorate concurrently?',
           ['Treat each as routine cramping',
            'Activate emergency response and alert leadership to a possible shared hazard',
            'Wait until the end of the shift to report',
            'Increase dialysate flow'],
           1,
           'Clustering changes the immediate risk to other patients and requires parallel unit action.'),
          ('Why is circuit blood not returned in suspected hemolysis?',
           ['It carries free hemoglobin and released potassium that can cause arrhythmia',
            'It is needed for culture',
            'It contains excess heparin only',
            'Returning it delays billing'],
           0,
           'Lysed red cells release potassium; reinfusion adds to the cardiac risk.'),
          ('Immediate positioning for suspected venous air embolism:',
           ['Right side down with head up',
            'Sitting upright',
            'Prone with legs raised',
            'Left side down with head down, after clamping the venous line'],
           3,
           'This position aims to trap air in the right atrium and away from the pulmonary outflow.'),
          ('First steps for intradialytic hypotension:',
           ['Give a large potassium dose',
            'Increase ultrafiltration to finish faster',
            'Stop ultrafiltration, lay flat and give a small saline bolus within protocol',
            'Remove the needles immediately in all cases'],
           2,
           'Removing the cause and restoring blood volume usually resolves it; recurrent episodes need target-weight review.'),
          ('Which exposure classically causes cluster hemolysis in HD units?',
           ['High-flux dialyzers',
            'Chloramine breakthrough in the water treatment system',
            'Low blood flow rates',
            'Bicarbonate dialysate'],
           1,
           'Chloramine oxidizes hemoglobin; carbon tank exhaustion is a classic outbreak cause.')],
 'terms': [('HD', 'Hemodialysis'),
           ('UF', 'Ultrafiltration'),
           ('ECG', 'Electrocardiogram'),
           ('BP', 'Blood pressure'),
           ('PSN', 'Philippine Society of Nephrology'),
           ('DOH', 'Department of Health'),
           ('CDC', 'Centers for Disease Control and Prevention'),
           ('MyTEMP', 'Personalised cooler dialysate trial (Ontario, Canada)')],
 'readings': [('hemodialysis-complications.html', 'Managing Complications of Hemodialysis')],
 'calcs': ['calc-ultrafiltration-rate.html', 'calc-qtc.html', 'calc-hd-session-review.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
