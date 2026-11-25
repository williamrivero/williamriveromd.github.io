# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 18: Peritoneal dialysis peritonitis and catheter problems.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Grades checked against the ISPD 2022 peritonitis guideline text (ISPD grading, 1A to 2D)."""

MODULE = {'image_alt': 'A peritoneal dialysis nurse holds a drained dialysis bag up to the window to check its clarity.',
 'objectives': ['Evaluate cloudy effluent the same day and start empiric therapy promptly.',
                'Follow cultures and response, and decide on catheter removal.',
                'Distinguish leaks, migration, constipation and drainage problems from infection.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>The Philippine '
        'Society of Nephrology (PSN) hemodialysis guidelines do not cover peritoneal dialysis, but the same principle applies: you stay in '
        'active management with the team that sees the patient first (b7, b8).[[an01_1]]</div>\n'
        '{{plain:Think of the peritoneum as the patient&rsquo;s only water filter at home. A cloudy bag is the filter telling you it is '
        'infected. Every day the infection runs, it scratches the filter a little more.}}\n'
        '<p>The picture has a limit. A home filter can be replaced from a shelf. The peritoneum cannot. Each episode of peritonitis, and each '
        'day it goes untreated, can injure the mesothelium, and repeated injury can end the patient&rsquo;s ability to do PD at all. The '
        'other limit is the diagnosis: most cloudy bags are infection, but a few are not, and clear bags that will not drain are usually a '
        'plumbing problem, not an infection.</p>\n'
        '{{cards:Key numbers|Effluent diagnostic threshold::White blood cell count (WBC) &gt;100/µL with &gt;50% neutrophils after a dwell '
        'of at least 2 hours|Unit peritonitis rate (ISPD 2022, 1C)::No more than 0.40 episodes per year at risk|Peritonitis-free patients '
        '(2C)::&gt;80% per year|Culture-negative episodes (1C)::&lt;15% of all episodes|Refractory peritonitis::Effluent not clear after 5 '
        'days of appropriate antibiotics}}\n'
        '<p>Most PD patients will call your unit, not you, when the bag turns cloudy, and often at night or on a weekend. Your work in this '
        'module is to make sure that call leads to same-day assessment every time, to direct treatment and the catheter decision, and to '
        'watch your program&rsquo;s numbers so you see a pattern before the next patient does.</p>\n',
 'case': {'title': '&ldquo;Just come to clinic next week&rdquo;',
          'html': '<p>On a Sunday evening, Mr. Castro, 60, calls your unit&rsquo;s after-hours number. He has been on PD for two years. '
                  'His bags are cloudy, his abdomen hurts, and his temperature is 38.4 &deg;C. The call is answered by Nurse Ruiz, who '
                  'joined the unit two weeks ago from the hemodialysis floor.</p>\n'
                  '<p>She tells him to take paracetamol and come to the PD clinic on Thursday. She mentions the call to you on Monday '
                  'morning, almost in passing, in a Viber message. When you look at the unit&rsquo;s PD records, you find this is the fourth '
                  'peritonitis episode among your 14 PD patients this year, and two of the effluent cultures were negative.</p>\n',
          'questions': ['What should have happened on Sunday night, and what happens now?',
                        'Why does a delay of days matter to the peritoneum?',
                        'What do the four episodes and two negative cultures tell you about the program?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Organisms reach the peritoneal cavity by four main routes. Touch contamination at the connection is the commonest. Others '
               'track along an infected exit site and tunnel, cross the bowel wall (constipation, diverticular disease, procedures), or arrive '
               'through the blood. Once inside, they draw neutrophils into the cavity. Millions of white cells in two liters of fluid are what '
               'make the bag cloudy.</p>\n'
               '<p>The inflammation is the harm. Severe or repeated episodes strip the mesothelial lining and drive fibrosis. The membrane '
               'then transports faster and holds water less well, which ends in ultrafiltration failure and, rarely, encapsulating peritoneal '
               'sclerosis. That chain is why time matters.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Problem</th><th>Mechanism</th><th>What the patient reports</th><th>Effluent</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Peritonitis</td><td>Infection draws neutrophils into the cavity</td><td>Pain, fever, cloudy bag</td><td>Cloudy; '
               'WBC &gt;100/µL, mostly neutrophils</td></tr>\n'
               '<tr><td>Constipation</td><td>A full colon presses on the catheter</td><td>Slow drain, no fever</td><td>Clear</td></tr>\n'
               '<tr><td>Catheter migration or omental wrap</td><td>The tip moves or is wrapped; outflow blocks</td><td>Fills well, drains '
               'poorly</td><td>Clear</td></tr>\n'
               '<tr><td>Leak</td><td>Fluid tracks into the abdominal wall or genitals</td><td>Swelling of the wall or scrotum, low drain '
               'volumes</td><td>Clear</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Cloudy fluid is infection until proven otherwise. Clear fluid that will not drain is usually mechanical.}}\n'
               '<div class="tc-scene"><span class="tc-lab">By phone, the constipated patient &middot; fictional</span><p>Mr. Rosales calls '
               'because his bags drain slowly. The fluid is clear and he has no fever. He has not moved his bowels in four '
               'days.</p><p>This is a drainage problem, not an infection. A full colon presses on the catheter and blocks outflow. You '
               'start a laxative and ask him to call back after his bowels move, and you book an abdominal X-ray if drainage does not '
               'improve.</p><p class="tc-scene-take"><b>What this shows.</b> Ask about the color of the fluid before you ask about anything '
               'else.</p></div>\n'
               '\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p>The International Society for Peritoneal Dialysis (ISPD) 2022 guideline grades its statements on its own scale, 1A to '
               '2D. It recommends diagnosing peritonitis when at least two of three are present: compatible clinical features, an effluent '
               'white cell count above 100/µL after a dwell of at least 2 hours with more than 50% neutrophils, and a positive effluent '
               'culture.[[an18_2]]</p>\n'
               '<p><strong>Getting a reliable culture.</strong> ISPD recommends blood-culture bottles as the preferred culture technique for '
               'PD effluent (1C), and recommends that culture-negative episodes stay below 15% of all episodes (1C).[[an18_2]] A high '
               'culture-negative rate usually points to how the sample was taken, not to the patients.</p>\n'
               '<p><strong>Treating.</strong> ISPD recommends center-specific empiric regimens that cover both gram-positive and '
               'gram-negative organisms (1C): a first-generation cephalosporin or vancomycin for gram-positive organisms, and a '
               'third-generation cephalosporin or an aminoglycoside for gram-negative organisms (1B). It recommends the intraperitoneal '
               'route (1B), and antifungal prophylaxis whenever a PD patient receives an antibiotic course (1B).[[an18_2]]</p>\n'
               '<p><strong>The catheter.</strong> Refractory peritonitis is defined as effluent that has not cleared after 5 days of '
               'appropriate antibiotics. ISPD recommends catheter removal for refractory episodes (1D), but the 2022 update suggests that '
               'watching beyond 5 days is reasonable when the effluent white cell count is falling (2C). It recommends immediate catheter '
               'removal when fungi are identified in the effluent (1C).[[an18_2]] The &ldquo;D&rdquo; grade means the removal rule rests '
               'largely on clinical experience; the reasoning is to save the membrane and the patient when the infection will not clear.</p>\n'
               '<p><strong>Program targets.</strong> ISPD recommends an overall peritonitis rate of no more than 0.40 episodes per year at risk '
               '(1C), with more than 80% of patients peritonitis-free per year (2C).[[an18_2]][[an18_1]] These are program measures, not '
               'patient outcomes on their own, but a rising rate is the earliest sign that training or technique has slipped.</p>\n'
               '{{key:Treat the same day, culture in blood-culture bottles, and decide about the catheter by day 5. Each step has a grade; the '
               'timing is what protects the membrane.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Make same-day assessment the only option.</strong> The patient will call the unit, often after hours, and the nurse '
               'who answers may be new to PD. Write a one-page pathway every staff member can follow: cloudy bag means come in today, bring '
               'the first cloudy bag, and call the attending. If the patient lives in a province hours away, agree which nearby hospital can '
               'take the effluent samples and give the first intraperitoneal dose, and how you will be reached.</p>\n'
               '<p><strong>Order the work-up and the first dose.</strong> Send effluent for cell count, differential, Gram stain, and culture '
               'in blood-culture bottles. Start intraperitoneal empiric antibiotics with gram-positive and gram-negative coverage, chosen '
               'from your center&rsquo;s antibiogram, and add antifungal prophylaxis. Check that the drugs are actually stocked in the '
               'pharmacy that will dispense them; a missing vial at night delays the first dose.</p>\n'
               '<p><strong>Follow through.</strong> Review the cultures at 48 to 72 hours and narrow treatment. Ask the PD nurse to send you '
               'the day 3 and day 5 effluent counts. Decide about the catheter by day 5 for refractory infection, and at once for fungi. Plan '
               'hemodialysis access if the catheter comes out.</p>\n'
               '<p><strong>Watch the program.</strong> Each year, calculate the peritonitis rate, the culture-negative proportion, and the '
               'organisms with the PD nurse. Retrain technique when the rate rises.</p>\n'
               '\n'
               '{{fig:an18_a}}\n'
               '\n'
               '{{fig:an18_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the annual PD review &middot; fictional</span><p>You calculate your '
               'program&rsquo;s numbers with the PD nurse: 6 episodes in 18 patient-years, a rate of 0.33 per patient-year, within the '
               'target of 0.40 or less. Two cultures were negative.</p><p>You trace both back to the same problem: effluent sent in a '
               'plain container, not in blood-culture bottles. The nurse rewrites the collection sheet.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> A peritonitis rate is useful only when the cultures behind it are '
               'reliable.</p></div>\n'
               '{{key:The weakest point is the first phone call. Write the pathway for the newest nurse on the night shift, not for '
               'yourself.}}\n'
               '{{call:<ul><li>Septic shock or a rigid abdomen suggesting a surgical cause</li><li>Multiple organisms or anaerobes (possible '
               'bowel perforation)</li><li>Fungal elements on Gram stain</li><li>Effluent not clearing by day 5</li></ul>}}\n')],
 'debrief': ['<p><strong>Now.</strong> Call Mr. Castro and see him today. Ask him to bring the first cloudy bag. Send effluent for cell '
             'count and differential, Gram stain, and culture in blood-culture bottles. Start intraperitoneal antibiotics that cover both '
             'gram-positive and gram-negative organisms, according to your antibiogram, and add antifungal prophylaxis. Review the cultures '
             'at 48 to 72 hours, narrow the treatment, and repeat the effluent count by day 5. If he looks septic or his abdomen is rigid, he '
             'needs a surgical opinion. Several organisms, or anaerobes, suggest a bowel perforation.</p>\n'
             '<p><strong>Why the delay matters.</strong> Peritonitis is an inflammation of the membrane that is his dialyzer. Each episode, '
             'and each day it goes untreated, injures the mesothelium and can lead to scarring and loss of ultrafiltration. Cloudy bags mean '
             'peritonitis until proven otherwise.</p>\n'
             '<p><strong>The program.</strong> Four episodes in about 14 patient-years is roughly 0.29 per patient-year at risk, within the '
             'ISPD target of 0.40 or less. But two of four culture-negative is 50%, far above the target of under 15%. That usually means a '
             'sampling or laboratory problem, so check that effluent goes into blood-culture bottles. Most of all, the after-hours call '
             'failed. Brief Nurse Ruiz kindly, then write a call-back pathway that any staff member can follow: cloudy bag, same-day '
             'assessment, call the attending, no exceptions. Ask the unit to message you about every cloudy-bag call the same night.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Gives the urgent call-back plan', False),
                      ('Specifies studies and the empiric treatment pathway', False),
                      ('Assigns response review and catheter decision dates', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which workflow is most appropriate for cloudy effluent with pain and fever?',
           ['Wait for growth before planning treatment',
            'Same-day evaluation, effluent studies and empiric treatment plus follow-up',
            'Advise a routine exchange and clinic next month',
            'Oral antibiotics without effluent studies'],
           1,
           'Early treatment and reassessment limit membrane injury and help identify refractory or complicated infection.'),
          ('What must happen after starting treatment for suspected PD peritonitis?',
           ['Assign culture review and a timely clinical reassessment',
            'Close the case at first antibiotic administration',
            'Defer all evaluation until the next adequacy test',
            'Stop antibiotics once the bag clears on day 1'],
           0,
           'Follow-up identifies response, the need to narrow treatment, and the catheter decision by day 5.'),
          ('Which effluent finding meets the ISPD 2022 laboratory criterion?',
           ['Any cloudy appearance without a count',
            'WBC 60/µL with 30% neutrophils',
            'WBC 90/µL with 90% lymphocytes',
            'WBC 350/µL with 80% neutrophils after a 4-hour dwell'],
           3,
           'The criterion is &gt;100/µL with &gt;50% neutrophils after a dwell of at least 2 hours.'),
          ('What is the ISPD 2022 target for overall peritonitis rate?',
           ['Zero episodes ever',
            '≤1.0 episode per patient-year',
            '≤0.40 episodes per year at risk',
            '≤0.1 episodes per patient-month'],
           2,
           'ISPD recommends this target (1C); units should calculate it at least yearly.'),
          ('When does ISPD 2022 recommend catheter removal?',
           ['After any first episode',
            'Refractory peritonitis not clearing after 5 days of appropriate antibiotics, or when fungi are identified',
            'When culture is coagulase-negative staphylococcus responding promptly',
            'Whenever the patient asks'],
           1,
           'Removal is recommended for refractory (1D) and fungal (1C) peritonitis. Watching longer than 5 days is reasonable if the '
           'effluent count is falling (2C).')],
 'terms': [('PD', 'Peritoneal dialysis'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('WBC', 'White blood cell count'),
           ('PSN', 'Philippine Society of Nephrology')],
 'readings': [('peritoneal-dialysis-ckd.html', 'Peritoneal Dialysis: Your Complete Guide'),
              ('adding-peritoneal-dialysis-program.html', 'Roadmap to Adding a Peritoneal Dialysis Program')],
 'calcs': ['calc-aminoglycoside-dosing.html', 'calc-vancomycin-auc.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
