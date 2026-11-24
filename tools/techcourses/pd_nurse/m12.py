# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 12: Philippine practice, records and quality improvement. Generated from PD Nurse v2 blueprint (modules/pd12-*.md). Edit here."""

MODULE = {'image_alt': '',
 'objectives': ['Distinguish the roles of the Professional Regulation Commission (PRC) and Board of Nursing, the Department of Health '
                '(DOH) and its Health Facilities and Services Regulatory Bureau (HFSRB), PhilHealth, and professional societies in a '
                'Philippine PD program.',
                'Support PhilHealth PD Z-benefit documentation within your scope, routing eligibility and payment decisions to authorized '
                'staff.',
                'Calculate peritonitis and exit-site infection rates, months between episodes, percentage of patients peritonitis-free and '
                'culture-negative percentage, and compare them with ISPD targets.',
                'Apply the 2026 ISPD framework for tracking loss from PD therapy.',
                'Design a small, measurable improvement with a run chart and a balancing measure.'],
 'big': '<p>A PD program is more than a group of patients doing exchanges. It is licensed, contracted, staffed, audited and, ideally, '
        'improving. Your daily documentation is what lets the program prove eligibility, receive payment, meet standards and see its own '
        'performance. Your work is to keep records that are complete and honest, to know which authority governs which question, and to '
        'turn the numbers into one improvement at a time.</p>\n'
        '{{plain:Think of the program as a jeepney route with a franchise, a vehicle inspection and a fare matrix. The driver (the nurse) '
        'does the daily work, but the route survives only if the paperwork, the vehicle and the service all pass.}}\n'
        '<p>The picture has a limit. Patients are not passengers who can switch routes easily, and quality numbers are not just '
        'compliance. A peritonitis rate is a count of people who suffered. Treat it with that weight.</p>',
 'case': {'title': 'A year of numbers',
          'html': '<p>The PD unit at a provincial hospital has 32 patients. Nurse coordinator <strong>Mylene</strong> reviews last year: 9 '
                  'peritonitis episodes over 28.5 patient-years; 3 culture-negative; 24 of 32 patients peritonitis-free; exits: 2 '
                  'transplants, 4 transfers to hemodialysis, 3 deaths.</p>',
          'questions': ['Is the unit within the ISPD targets?',
                        'Which indicator needs work first?',
                        'What would you change, and how would you know it did not cause harm?']},
 'sections': [('who-governs-what',
               'Who governs what',
               'Who governs what (verify current issuances)',
               '\n'
               '<p>Use REQUIREMENTS.md, dated 24 November 2026, with your unit&rsquo;s credentialing and benefits leads. Summary:</p>\n'
               '{{fig:pd12_gov}}\n'
               '\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Authority</th><th>Question it answers</th><th>Your evidence</th></tr></thead>\n'
               '<tbody><tr><td>PRC / Board of Nursing (Republic Act 9173)</td><td>Are you lawfully authorized to practice '
               'nursing?</td><td>Current PRC license and facility privilege record</td></tr><tr><td>DOH / HFSRB</td><td>Is the facility '
               'licensed for the service it provides?</td><td>Facility license to operate or written applicability determination; '
               'PD-specific licensing route confirmed with HFSRB or the regional Center for Health Development</td></tr><tr><td>PhilHealth '
               'PD Z-benefit contracting (Circular 2024-0036 and current annexes)</td><td>Is the facility contracted, the patient '
               'eligible, the episode documented?</td><td>Contract, self-assessment tool, rosters, training certificates, patient records '
               'per current annexes</td></tr><tr><td>PhilHealth PD First self-assessment tool</td><td>Staffing and training '
               'standard</td><td>At least one full-time PD nurse; nurse-to-patient ratio stated as 1:20; PRC licensure; recognized PD '
               'training per listed pathways; head validation</td></tr><tr><td>Philippine Society of Nephrology, National Kidney and '
               'Transplant Institute</td><td>Recognized training pathways</td><td>Course title, dates, duration, CPD listing, acceptance '
               'for the specific setting</td></tr></tbody></table></div>\n'
               '<p><strong>Benefit amounts and coverage change.</strong> Press reports in 2024 described a PD First Z-benefit package of '
               '₱270,000 per year covering solutions, accessories and 90 to 120 exchanges a month depending on the prescription. Confirm '
               'the current amount, inclusions and annexes with the PhilHealth Regional Office before counseling a patient.</p>\n'
               '<p><strong>Scope.</strong> You help patients and the team assemble documentation, check CKD stage 5 and PhilHealth '
               'Dialysis Database status as instructed, and record initiation, follow-up, infection episodes, and exit or transfer. '
               'Eligibility determinations and payment decisions remain with authorized personnel.</p>\n'),
              ('measuring-infection',
               'Measuring infection',
               'Measuring infection',
               '\n'
               '<p><strong>Peritonitis rate (episodes per year at risk)</strong> = number of episodes ÷ total patient-years at risk.</p>\n'
               '<p>Patient-years at risk = sum of each patient&rsquo;s days on PD in the period ÷ 365.25. Count time from the start of PD '
               'training or treatment; report pre-PD peritonitis (after insertion but before PD starts) separately per the 2022 '
               'definitions. Count relapsing peritonitis as one episode, per ISPD counting conventions.[[pd_li2022]]</p>\n'
               '<p><strong>Months between episodes</strong> = 12 ÷ rate.</p>\n'
               '<p><strong>Percentage of patients peritonitis-free</strong> = patients with no episode in the period ÷ patients at risk in '
               'the period × 100.</p>\n'
               '<p><strong>Culture-negative percentage</strong> = culture-negative episodes ÷ all episodes × 100.</p>\n'
               '<p><strong>Exit-site infection rate</strong> = episodes ÷ patient-years at risk.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Indicator</th><th>ISPD target</th></tr></thead>\n'
               '<tbody><tr><td>Peritonitis rate</td><td>≤ 0.40 episodes per year at risk (2022)</td></tr><tr><td>Patients peritonitis-free '
               'per year</td><td>&gt; 80% (2022)</td></tr><tr><td>Culture-negative peritonitis</td><td>&lt; 15% of episodes (2022, GRADE '
               '1C)</td></tr><tr><td>Exit-site infection rate</td><td>≤ 0.40 episodes per year at risk '
               '(2023)</td></tr></tbody></table></div>\n'
               '{{key:Worked calculations.}}\n'
               '<ul><li>6 episodes over 20 patient-years: 6 ÷ 20 = <strong>0.30 episodes per patient-year</strong>; 12 ÷ 0.30 = <strong>40 '
               'months between episodes</strong>. Below the 0.40 target.</li><li>4 episodes over 8 patient-years: 4 ÷ 8 = <strong>0.50 per '
               'patient-year</strong>; 12 ÷ 0.50 = <strong>24 months between episodes</strong>. Above target.</li><li>3 of 14 episodes '
               'culture-negative: 3 ÷ 14 × 100 = <strong>21%</strong>. Above the 15% target; review sampling and laboratory '
               'methods.</li></ul>\n'
               '<p><strong>Small numbers mislead.</strong> A unit with 25 patients may see the rate jump from 0.20 to 0.60 because of two '
               'extra episodes. Report confidence intervals where possible, look at trends over 12 months, and read each episode&rsquo;s '
               'root cause.</p>\n'
               '<p><strong>International comparison.</strong> In PDOPPS, crude peritonitis rates were 0.28 episodes per patient-year '
               'overall, ranging from 0.26 in the United States to 0.40 in Thailand, and 10% of facilities exceeded 0.50. These are '
               'observational data from seven countries, not including the Philippines.[[pd_perl2020]]</p>\n'),
              ('tracking-loss-from',
               'Tracking loss from PD',
               'Tracking loss from PD',
               '\n'
               '<p>The 2026 ISPD position statement notes that nearly half of people who start PD are no longer on it at two years. The '
               'most common causes are transfer to hemodialysis, death and kidney transplantation; others include recovery of kidney '
               'function, transfer to another dialysis program and loss to follow-up. The statement replaces the inconsistently defined '
               'term "technique failure" with standardized definitions of causes of loss, recommendations on measurement, analysis and '
               'reporting, and key performance indicators for benchmarking and improvement.[[pd_quinn2026]]</p>\n'
               '<p>For your program: record the date and cause of every exit using the agreed definitions; distinguish clinically '
               'different outcomes (transplant is a success; death and hemodialysis transfer need review); and review hemodialysis '
               'transfers for preventable causes such as peritonitis, catheter dysfunction, inadequate fluid removal, burnout or caregiver '
               'loss.</p>\n'),
              ('improving-one-thing',
               'Improving one thing',
               'Improving one thing at a time',
               '\n'
               '\n'
               '{{fig:pd12_run}}\n'
               '<ol><li><strong>Pick a problem with data.</strong> For example, culture-negative rate 21%, or median time from '
               'cloudy-fluid call to first antibiotic dose of 9 hours.</li><li><strong>Write an aim.</strong> "Reduce median '
               'call-to-antibiotic time from 9 hours to under 4 hours within 6 months."</li><li><strong>Choose measures.</strong> Outcome '
               '(peritonitis cure without catheter loss), process (time stamps from call to sample to dose), balancing (after-hours staff '
               'workload, unnecessary emergency visits).</li><li><strong>Test a change.</strong> A one-page cloudy-bag pathway, a '
               'pre-labeled sample kit at home, an after-hours phone tree.</li><li><strong>Plot a run chart.</strong> Monthly values, a '
               'median line, and the date of each change.</li><li><strong>Review and adapt.</strong></li></ol>\n')],
 'debrief': ['<p><strong>Mylene&rsquo;s calculations.</strong> Rate 9 ÷ 28.5 = 0.32 per patient-year (≈ 38 months between episodes), under '
             'target. Peritonitis-free 24 ÷ 32 = 75%, under the &gt;80% target. Culture-negative 3 ÷ 9 = 33%, well above the 15% '
             'target.</p>\n'
             '<p><strong>Mylene&rsquo;s plan.</strong> She reviews the three culture-negative episodes: two had antibiotics before '
             'sampling after emergency department visits, and one sample sat for 14 hours before reaching the laboratory. Her aim: '
             'culture-negative below 15% within 12 months. Change: an emergency-department alert card carried by every patient ("Send PD '
             'effluent for cell count, Gram stain and culture before antibiotics when feasible; call the PD unit") and a courier '
             'arrangement with the laboratory. Balancing measure: time to first antibiotic dose, so that sampling does not delay '
             'treatment. She plots both monthly.</p>\n'
             '<p>She also reviews the four hemodialysis transfers using the 2026 definitions: two after refractory peritonitis, one for '
             'inadequate fluid removal, one after caregiver loss.</p>'],
 'skills': {'title': 'Practice drill',
            'intro': 'Build a mock contracted-provider document packet (facility record, nurse qualifications, eligibility workflow per '
                     'current annexes). Then calculate peritonitis rate, months between episodes, percentage peritonitis-free and '
                     'culture-negative percentage for a supplied data set, and propose one improvement aim with a numerator, denominator, '
                     'reporting interval, owner and balancing measure.',
            'items': [('Build a mock contracted-provider document packet (facility record, nurse qualifications, eligibility workflow per '
                       'current annexes).',
                       False),
                      ('Then calculate peritonitis rate, months between episodes, percentage peritonitis-free and culture-negative '
                       'percentage for a supplied data set, and propose one improvement aim with a numerator, denominator, reporting '
                       'interval, owner and balancing measure.',
                       False)]},
 'quiz': [('What is the peritonitis rate for 4 episodes over 8 patient-years?',
           ['0.50 episodes per patient-year', '0.25', '2.0', '32'],
           0,
           '4 ÷ 8 = 0.50.'),
          ('At a rate of 0.50 episodes per patient-year, how many months between episodes?', ['6', '12', '24', '50'], 2, '12 ÷ 0.50 = 24.'),
          ('6 episodes over 20 patient-years gives:', ['3.3', '0.12', '1.2', '0.30 episodes per patient-year'], 3, ''),
          ('3 of 14 episodes are culture-negative. Is the unit within the ISPD 2022 target?',
           ['Yes, 21% is below 30%', 'No, 21% exceeds the &lt;15% target', 'Yes, any value is acceptable', 'Cannot be determined'],
           1,
           ''),
          ('What evidence should the head verify when hiring under a PD Z contract?',
           ['Only a résumé',
            'Current PRC authority, training evidence accepted for that facility, validation, staffing and contract evidence under current '
            'requirements',
            'A recommendation letter',
            'Social media profile'],
           1,
           ''),
          ('Who decides PhilHealth eligibility and payment?',
           ['The PD nurse alone', 'The patient', 'The supplier', 'Authorized benefits personnel under the contract and current annexes'],
           3,
           ''),
          ('Which body licenses health facilities?', ['DOH through HFSRB', 'PRC', 'PhilHealth', 'A professional society'], 0, ''),
          ('What nurse-to-patient ratio does the PhilHealth PD First self-assessment tool state?',
           ['1:4', '1:100', '1:20', 'None'],
           2,
           'Do not import the hemodialysis 1:4 ratio into PD.'),
          ('How should relapsing peritonitis be counted in the rate?',
           ['As two episodes', 'Not at all', 'As one episode, per ISPD counting conventions', 'As three episodes'],
           2,
           ''),
          ('What does the 2026 ISPD position statement recommend instead of "technique failure"?',
           ['Standardized definitions for each cause of loss from PD, with key performance indicators',
            'Counting only deaths',
            'No tracking',
            'Using "dropout"'],
           0,
           ''),
          ('Why can a small unit&rsquo;s peritonitis rate swing widely year to year?',
           ['The formula changes', 'Small numbers; one or two episodes change the rate greatly', 'ISPD targets change yearly', 'It cannot'],
           1,
           ''),
          ('Which is a balancing measure for an initiative to sample before antibiotics?',
           ['Number of patients', 'Solution brand', 'Clinic paint color', 'Time to first antibiotic dose'],
           3,
           ''),
          ('24 of 32 patients were peritonitis-free last year. Against the ISPD 2022 target:',
           ['75%, above target', '92%', 'No target exists', '75%, below the &gt;80% target'],
           3,
           ''),
          ('How are patient-years at risk calculated?',
           ['Number of patients',
            'Sum of each patient&rsquo;s days on PD in the period divided by 365.25',
            'Number of exchanges',
            'Number of episodes'],
           1,
           ''),
          ('Before counseling a patient on the PD Z-benefit amount, you should:',
           ['Quote a press report',
            'Guess',
            'Confirm the current amount and inclusions with the PhilHealth Regional Office',
            'Avoid the topic entirely'],
           2,
           '')],
 'terms': [('Peritoneal dialysis (PD)',
            'Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter.'),
           ('Exit-site infection', 'Purulent discharge at the exit site, with or without redness (ISPD 2023).'),
           ('Peritonitis', 'Infection or inflammation of the peritoneum, usually shown by cloudy effluent.'),
           ('Culture-negative peritonitis', 'Peritonitis in which no organism grows from the effluent culture.'),
           ('Relapsing peritonitis', 'A new episode within 4 weeks of finishing therapy, same organism or one sterile episode.'),
           ('Run chart', 'A graph of a measure over time with a median line, used to see whether a change made a difference.')],
 'readings': [('adding-peritoneal-dialysis-program.html', 'Starting and running a PD program.'),
              ('dialysis-qapi-vs-cqi.html', 'Quality assessment and improvement in dialysis.')],
 'calcs': ['calc-qapi-run-chart-spc.html', 'calc-qapi-cqi-toolkit.html', 'calc-dialysis-qapi-scorecard.html']}
