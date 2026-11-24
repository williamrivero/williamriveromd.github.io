# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 07: Peritonitis: recognition, sampling, escalation and prevention. Generated from PD Nurse v2 blueprint (modules/pd07-*.md). Edit here."""

MODULE = {'image_alt': '',
 'objectives': ['Explain how peritonitis develops through the intraluminal, periluminal, transmural (enteric) and hematogenous routes, and '
                'what each implies for prevention.',
                'Apply the 2022 ISPD diagnostic criteria to understand the team&rsquo;s assessment, including the short-dwell APD caveat.',
                'Activate the PD pathway on suspicion, screen for instability, and coordinate effluent sampling so that culture-negative '
                'results stay rare.',
                'Use the 2022 ISPD outcome definitions (refractory, relapsing, recurrent, repeat, catheter-related, enteric, pre-PD) in '
                'follow-up documentation.',
                'Lead post-episode prevention: technique review, retraining and modifiable risk factors.'],
 'big': '<p>Peritonitis is the complication that most often ends PD. It drives hospitalization, catheter removal, transfer to hemodialysis '
        'and, in severe or fungal cases, death. In PDOPPS, an international cohort of 7,051 adults, the crude rate was 0.28 episodes per '
        'patient-year, and one facility in ten exceeded 0.50. Most episodes respond to prompt antibiotics. The difference between a cured '
        'episode and a lost catheter is often hours: how fast the patient calls, how fast the sample is taken, how fast treatment starts. '
        'Your work is to make those hours short.[[pd_perl2020]]</p>\n'
        '{{plain:Think of the peritoneal cavity as a sealed, warm room stocked with sugar. Bacteria that get in have food and time.}}\n'
        '<p>The picture has a limit. The peritoneum is not passive: it has macrophages and recruits neutrophils within hours. That is why '
        'effluent turns cloudy. Cloudiness is the body&rsquo;s defense made visible, white cells by the billions. It is the alarm, not the '
        'damage itself. The damage comes when the defense is overwhelmed or the organism is hard to kill.</p>',
 'case': {'title': 'Coconut milk at 6:40 AM',
          'html': '<p><strong>Lola Aida, 74</strong>, on APD, assisted by her granddaughter <strong>Mika</strong>, calls at 6:40 AM. Nurse '
                  '<strong>Ramon</strong> is on call.</p>\n'
                  '<p><strong>6:40.</strong> Mika reports the drain bag "looks like <em>gata</em>" (coconut milk). Lola Aida has chills '
                  'and mild abdominal discomfort. No vomiting. She is alert and talking.</p>',
          'questions': ['Is this peritonitis until proven otherwise?',
                        'What do you screen for in the first five minutes?',
                        'What must be in your handoff before you hang up?']},
 'sections': [('the-physiology',
               'The physiology',
               'The physiology',
               '\n'
               '{{key:Routes of entry.}}\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Route</th><th>How</th><th>Typical organisms</th><th>Prevention focus</th></tr></thead>\n'
               '<tbody><tr><td>Intraluminal (touch)</td><td>Contamination at connection</td><td>Skin flora, coagulase-negative '
               'staphylococci</td><td>Technique, flush before fill, contamination response '
               '(PD04)</td></tr><tr><td>Periluminal</td><td>Along the outside of the catheter from an infected exit site or '
               'tunnel</td><td><em>S. aureus</em>, <em>P. aeruginosa</em></td><td>Exit-site care (PD03)</td></tr><tr><td>Transmural '
               '(enteric)</td><td>Across the bowel wall in constipation, diverticulitis, colitis</td><td>Gram-negative rods, mixed enteric '
               'flora, anaerobes</td><td>Bowel care, hypokalemia correction, antibiotic prophylaxis before invasive '
               'procedures</td></tr><tr><td>Hematogenous / ascending</td><td>Bloodstream, gynecologic</td><td>Streptococci, '
               'others</td><td>Procedure prophylaxis</td></tr></tbody></table></div>\n'
               '<p><strong>Why the abdomen hurts.</strong> Inflammation of the parietal peritoneum stimulates somatic pain fibers. Pain '
               'can be absent early, especially in APD or in older or diabetic patients. That is why cloudy effluent without pain still '
               'counts.</p>\n'
               '{{fig:pd07_routes}}\n'
               '\n'
               '<p><strong>Why ultrafiltration falls.</strong> Inflammation increases capillary surface area and permeability. Glucose is '
               'absorbed faster, the osmotic gradient fades faster, and UF falls. Patients may become fluid overloaded during an episode. '
               'Protein loss rises.</p>\n'),
              ('diagnosis-ispd-2022',
               'Diagnosis',
               'Diagnosis (ISPD 2022)',
               '\n'
               '<p>The 2022 ISPD recommendations diagnose peritonitis when at least two of the following are present (GRADE '
               '1C):[[pd_li2022]]</p>\n'
               '<ol><li>Clinical features consistent with peritonitis: abdominal pain and/or cloudy dialysis effluent.</li><li>Dialysis '
               'effluent white cell count above 100/µL (above 0.1 × 10⁹/L) after a dwell of at least 2 hours, with more than 50% '
               'polymorphonuclear leukocytes.</li><li>Positive dialysis effluent culture.</li></ol>\n'
               '<p><strong>Short APD dwells.</strong> Because cycler dwells are short, the absolute white cell count may be lower than '
               '100/µL even during real peritonitis. The proportion of polymorphonuclear cells above 50% remains meaningful. This is why '
               'you always record dwell duration with the sample.</p>\n'
               '<p><strong>Not all cloudy effluent is infection.</strong> Other causes include chemical irritation, eosinophilic effluent '
               '(often early after insertion), chylous effluent (milky, lipid-rich), hemoperitoneum (blood-tinged, for example during '
               'menstruation), malignancy, and reactions associated with some solutions or medications. The team sorts these out. '
               '<strong>You treat every cloudy bag as possible peritonitis until the team says otherwise.</strong></p>\n'),
              ('what-you-do',
               'What you do',
               'What you do: the first hour',
               '\n'
               '\n'
               '{{fig:pd07_hour}}\n'
               '{{key:On the call or at the bedside:}}\n'
               '<ol><li><strong>Recognize and activate.</strong> Cloudy effluent, with or without pain, means immediate PD team '
               'contact.</li><li><strong>Screen for instability.</strong> Fever with rigors, hypotension, confusion, severe pain, vomiting '
               'preventing oral intake, rapid breathing. Use emergency services or the emergency department per the local '
               'pathway.</li><li><strong>Gather the facts.</strong> Onset; last exchange and dwell length; recent contamination or breach; '
               'exit-site changes; constipation or diarrhea; recent procedures (colonoscopy, dental, gynecologic); recent antibiotics; '
               'allergies; prior episodes and organisms.</li><li><strong>Preserve the effluent.</strong> Instruct the patient to keep the '
               'cloudy bag, closed and labeled, and bring it, or follow the program&rsquo;s instructions for the first bag. If the patient '
               'presents with a dry abdomen (for example APD with no day dwell), the unit protocol may call for a fill and a short dwell '
               'before sampling.</li><li><strong>Coordinate sampling.</strong> Cell count and differential, Gram stain and culture, per '
               'protocol. Blood-culture bottle inoculation of effluent is the preferred culture technique in ISPD guidance; follow your '
               'laboratory&rsquo;s exact volumes and transport times. Label with dwell duration and collection time.</li><li><strong>Do '
               'not delay treatment.</strong> Empirical antibiotics, usually intraperitoneal, covering both gram-positive and '
               'gram-negative organisms, should start as soon as possible after specimens are taken. Collection before antibiotics is '
               'preferred when feasible, but must not delay urgent care. Antibiotic choice and dose are the prescriber&rsquo;s; '
               'administration follows the written order or standing protocol.</li><li><strong>Close the loop.</strong> SBAR to the '
               'accepting clinician, read-back, time stamp, disposition (admit, treat at home with return visit, emergency), and who will '
               'follow the culture.</li></ol>\n'),
              ('program-quality-markers',
               'Program quality markers',
               'Program quality markers (ISPD 2022)',
               '\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Marker</th><th>2022 target</th></tr></thead>\n'
               '<tbody><tr><td>Overall peritonitis rate</td><td>No more than 0.40 episodes per year at risk</td></tr><tr><td>Patients free '
               'of peritonitis per year</td><td>More than 80%</td></tr><tr><td>Culture-negative episodes</td><td>Less than 15% of all '
               'episodes (GRADE 1C)</td></tr></tbody></table></div>\n'
               '<p>A culture-negative rate above 15% usually points to sampling or laboratory problems, or to antibiotics given before '
               'sampling. Nurses control much of that.</p>\n'
               '<p>PDOPPS country rates ranged from 0.26 episodes per patient-year in the United States to 0.40 in Thailand; Thailand had '
               'more gram-negative and culture-negative episodes. Philippine program data should be compared against these figures with '
               'care, because definitions and case-finding differ.[[pd_perl2020]]</p>\n'),
              ('follow-through-and',
               'Follow-through and outcome',
               'Follow-through and outcome definitions',
               '\n'
               '<p>The 2022 update revised and clarified these definitions. Use them in documentation so episodes are counted '
               'consistently:[[pd_li2022]]</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Term</th><th>Meaning</th></tr></thead>\n'
               '<tbody><tr><td>Refractory</td><td>Failure of the effluent to clear after 5 days of appropriate antibiotics. The 2022 '
               'update allows expectant management beyond day 5 if the effluent white cell count is falling toward normal, rather than '
               'mandatory catheter removal.</td></tr><tr><td>Relapsing</td><td>An episode within 4 weeks of completing therapy for a prior '
               'episode, with the same organism or one sterile episode</td></tr><tr><td>Recurrent</td><td>An episode within 4 weeks of '
               'completing therapy, with a different organism</td></tr><tr><td>Repeat</td><td>An episode more than 4 weeks after '
               'completing therapy, with the same organism</td></tr><tr><td>Catheter-related</td><td>Peritonitis with an exit-site or '
               'tunnel infection with the same organism (or one site sterile)</td></tr><tr><td>Enteric</td><td>Peritonitis arising from an '
               'intestinal source (inflammation, perforation or ischemia)</td></tr><tr><td>Pre-PD</td><td>Peritonitis after catheter '
               'insertion but before PD training or treatment begins</td></tr><tr><td>Medical cure</td><td>Resolution without '
               'complications such as relapse, catheter removal, hemodialysis transfer or death</td></tr></tbody></table></div>\n'
               '<p><strong>Nursing follow-through:</strong> repeat cell counts as ordered, track culture and sensitivities, confirm the '
               'antibiotic course is complete, watch UF and weight during the episode (UF often falls), watch for hearing changes if '
               'aminoglycosides are used (the 2022 update added a recommendation on adjunctive oral N-acetylcysteine to mitigate '
               'aminoglycoside ototoxicity, a prescriber decision), and confirm antifungal prophylaxis if the program uses it whenever '
               'antibiotics are given.[[pd_li2022]]</p>\n'),
              ('prevention-after-every',
               'Prevention after every',
               'Prevention after every episode',
               '\n'
               '<p>Every episode is a signal. Review it as a team:</p>\n'
               '<ul><li><strong>Root cause.</strong> Which route? Touch, exit site, bowel, procedure?</li><li><strong>Technique.</strong> '
               'Observe a full exchange. The 2022 ISPD update revised its recommendations on training and reassessment; retraining after '
               'peritonitis is standard practice.</li><li><strong>Modifiable risk factors named in 2022:</strong> domestic pets in the '
               'exchange area, hypokalemia, and histamine-2 receptor antagonist use. Report these to the prescriber; do not change '
               'medicines yourself.</li><li><strong>Procedures.</strong> Antibiotic prophylaxis before invasive procedures such as '
               'colonoscopy or gynecologic procedures, and emptying the abdomen beforehand, per the revised recommendations and the '
               'prescriber&rsquo;s order.</li></ul>\n'
               '{{key:Every cloudy bag gets a call. Every episode gets a review.}}\n')],
 'debrief': ['<p><strong>6:45.</strong> Ramon screens: temperature 38.2 °C on their thermometer, no confusion, no dizziness on standing, '
             'pulse 96 by Mika&rsquo;s count. Last night&rsquo;s cycler dwell was about 1 hour 30 minutes. No known contamination. Exit '
             'site dry. Last bowel movement three days ago. No recent procedures. Allergy: none known.</p>\n'
             '<p><strong>6:52.</strong> Ramon activates the PD pathway: calls the nephrologist on duty with SBAR. Situation: cloudy '
             'effluent, chills, fever 38.2 °C, hemodynamically stable by home assessment. Background: 74, APD, assisted by granddaughter, '
             'no prior peritonitis. Assessment: suspected peritonitis, short APD dwell (record for cell count interpretation), possible '
             'constipation. Recommendation: urgent same-morning assessment at the PD unit for sampling and empirical treatment; emergency '
             'department if she becomes unstable before arrival.</p>\n'
             '<p><strong>6:58.</strong> The nephrologist accepts. Ramon reads back the plan. He tells Mika to clamp and bring the drain '
             'bag (or a sample per protocol), to bring Lola&rsquo;s medicines, and to call 911 or go to the nearest emergency department '
             'if Lola becomes confused, faint or breathless on the way.</p>\n'
             '<p><strong>8:10.</strong> At the unit, samples are sent, labeled with dwell duration and collection time. Empirical '
             'intraperitoneal antibiotics start per order at 8:25. Ramon documents times from call to sample to first dose, the accepting '
             'clinician, and who will review the culture at 48 hours. He schedules technique review with Mika after the episode.</p>'],
 'skills': {'title': 'Cloudy bag with pain (OSCE station 3)',
            'intro': 'Run a timed mock call. Deliver SBAR, document read-back, disposition and time stamps. Faculty scores against OSCE '
                     'station 3 in FACULTY.md.',
            'items': [('Recognizes urgency and activates the PD pathway.', True),
                      ('Checks for systemic instability and routes emergency care as indicated.', True),
                      ('Preserves the specimen and coordinates timely sampling under protocol.', False),
                      ('Relays SBAR and obtains read-back.', False),
                      ('Time-stamps contact and disposition.', False)]},
 'quiz': [('A patient feels well but reports cloudy effluent. What is the response?',
           ['Activate urgent PD assessment, screen for instability and arrange sampling',
            'Wait to see if it clears',
            'Drink more water',
            'Skip the next exchange'],
           0,
           'Cloudy effluent without pain still counts.'),
          ('How many of the three ISPD 2022 criteria are needed to diagnose peritonitis?',
           ['One', 'All three', 'At least two', 'None; diagnosis is clinical only'],
           2,
           'At least two of three.'),
          ('Which effluent result meets the cell-count criterion after a dwell of at least 2 hours?',
           ['White cells above 10/µL with any differential',
            'Red cells above 100/µL',
            'Lymphocytes above 50%',
            'White cells above 100/µL with more than 50% polymorphonuclear cells'],
           3,
           'That is the criterion.'),
          ('Why record dwell duration with the sample?',
           ['For billing',
            'Short APD dwells may give a lower absolute count; the differential remains meaningful',
            'It determines the antibiotic',
            'It is not needed'],
           1,
           'Interpretation depends on dwell length.'),
          ('What is the ISPD 2022 target for culture-negative peritonitis?',
           ['Less than 50%', 'Less than 15% of episodes', 'Less than 1%', 'No target'],
           1,
           'GRADE 1C.'),
          ('Collection before antibiotics is preferred. What if the patient is septic and sampling is delayed?',
           ['Delay treatment until sampling',
            'Skip sampling entirely',
            'Send the patient home',
            'Do not delay urgent care; coordinate sampling as quickly as possible'],
           3,
           'Treatment must not wait.'),
          ('Which route is most associated with gram-negative and mixed enteric organisms?',
           ['Transmural from the bowel', 'Intraluminal touch', 'Periluminal from the exit site', 'Hematogenous from the skin'],
           0,
           'Enteric peritonitis.'),
          ('Peritonitis within 4 weeks of completing therapy with the same organism is:',
           ['Recurrent', 'Repeat', 'Relapsing', 'Refractory'],
           2,
           'Same organism, within 4 weeks.'),
          ('Peritonitis within 4 weeks of completing therapy with a different organism is:',
           ['Relapsing', 'Repeat', 'Recurrent', 'Pre-PD'],
           2,
           'Different organism, within 4 weeks.'),
          ('What did the 2022 update change about refractory peritonitis?',
           ['Expectant management beyond day 5 may be considered if the effluent white cell count is falling toward normal',
            'Catheter removal is now required on day 2',
            'Refractory peritonitis no longer exists',
            'Antibiotics are no longer used'],
           0,
           'A revised recommendation.'),
          ('Which is a modifiable peritonitis risk factor named in the 2022 ISPD update?',
           ['Blood type', 'Hypokalemia', 'Height', 'Eye color'],
           1,
           'Along with pets and H2-receptor antagonists.'),
          ('What is the 2022 ISPD target for the overall peritonitis rate?',
           ['No more than 1.0', 'No more than 0.10', 'No target', 'No more than 0.40 episodes per year at risk'],
           3,
           ''),
          ('Why does UF often fall during peritonitis?',
           ['Antibiotics block water',
            'The catheter is removed',
            'Patients drink less',
            'Inflammation increases membrane permeability and glucose absorption, dissipating the osmotic gradient'],
           3,
           'Physiology of inflamed peritoneum.'),
          ('Cloudy, blood-tinged effluent in a menstruating patient without pain or fever should be:',
           ['Ignored because it is menstrual',
            'Reported; the team decides whether it is hemoperitoneum or infection',
            'Treated with antibiotics by the nurse',
            'Flushed until clear'],
           1,
           'Treat as possible peritonitis until the team decides.'),
          ('Which element makes a peritonitis handoff closed-loop?',
           ['Sending an email',
            'Telling the patient to wait',
            'Accepting clinician named, read-back, time stamp, disposition and a named person to follow the culture',
            'Writing "endorsed"'],
           2,
           '')],
 'terms': [('Peritoneal dialysis (PD)',
            'Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter.'),
           ('APD', 'Automated peritoneal dialysis: a cycler performs exchanges, usually overnight.'),
           ('Dwell', 'The time dialysis solution stays in the abdomen between fill and drain.'),
           ('Ultrafiltration (UF)', 'Fluid removed by dialysis; net UF is drained volume minus instilled volume.'),
           ('Exit site', 'The point where the PD catheter leaves the skin.'),
           ('Tunnel', 'The path of the catheter under the skin between the cuffs.'),
           ('Tunnel infection', 'Inflammation along the catheter tunnel, with or without a fluid collection on ultrasound.'),
           ('Flush before fill',
            'Sending a little fresh solution straight to the drain bag before filling, to wash out bacteria introduced at connection.'),
           ('Cycler', 'The machine that performs APD exchanges.'),
           ('Peritonitis', 'Infection or inflammation of the peritoneum, usually shown by cloudy effluent.'),
           ('Effluent', 'Fluid drained from the abdomen after a dwell.'),
           ('SBAR', 'Situation, Background, Assessment, Recommendation: a structured handoff.')],
 'readings': [('antibiotic-stewardship-dialysis.html', 'Antibiotic stewardship in dialysis units.'),
              ('dialysis-access-infection.html', 'Dialysis access infections.')],
 'calcs': ['calc-qapi-run-chart-spc.html']}
