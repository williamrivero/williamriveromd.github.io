# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 06: Monitoring, membrane testing and goal-directed PD. Generated from PD Nurse v2 blueprint (modules/pd06-*.md). Edit here."""

MODULE = {'image_alt': '',
 'objectives': ['Explain what "goal-directed PD" means and why the 2020 ISPD recommendations moved away from a single clearance target.',
                'Describe what the ADEMEX and Hong Kong randomized trials showed about increasing peritoneal small-solute clearance.',
                'Explain what a peritoneal equilibration test (PET) measures, when it is done, and how fast solute transfer and low '
                'ultrafiltration capacity change management.',
                'Collect timed effluent, urine and blood samples so that the results can be trusted.',
                'Prepare a structured nursing review that puts trends, delivered therapy and the person&rsquo;s goals in one picture for '
                'the team.'],
 'big': '<p>For years, PD quality was judged by one number: weekly Kt/V urea. Randomized trials showed that pushing that number higher did '
        'not help people live longer. The field moved to a broader question: is this person feeling well, in fluid balance, eating, '
        'functioning and living the life they want, with the safest prescription that achieves it? Your work is to bring the evidence for '
        'that question to every review: trends, delivered therapy, symptoms, nutrition, residual urine, and test results that were '
        'collected properly.</p>\n'
        '{{plain:Think of a car&rsquo;s dashboard. Speed matters, but you also watch fuel, temperature and the warning lights, and the '
        'point of the journey is where the passengers want to go.}}\n'
        '<p>The picture has a limit. A dashboard reports a machine. A person on PD has a membrane that changes with time and infection, '
        'kidneys that lose function, appetite that waxes and wanes, and goals that shift. The readings must be interpreted against that '
        'person, not against a fixed specification.</p>',
 'case': {'title': 'The first PET',
          'html': '<p><strong>Mr. Benjamin Cruz, 52</strong>, has been on CAPD for 10 weeks. Nurse <strong>Hazel</strong> is preparing his '
                  'first PET and a nursing review.</p>\n'
                  '<p><strong>PET day.</strong> Hazel confirms the protocol and solution strength with the order. The night dwell was done '
                  'as instructed. The pre-test drain is complete. Samples are drawn at the ordered times. The final 4-hour drain measures '
                  '2,350 mL from 2,000 mL of 2.27% glucose solution: net UF +350 mL. D/P creatinine at 4 hours is reported as high '
                  'relative to the unit&rsquo;s reference ranges.</p>\n'
                  '<p><strong>Trend data.</strong> Over five days, his weight rises from 68.0 to 70.0 kg, daily UF falls from about 750 to '
                  '450 mL, and urine falls from about 600 to 350 mL. He reports mild exertional breathlessness. All exchanges were done. '
                  'His night dwell drains less than it was filled most days.</p>',
          'questions': ['Is the PET result valid? What could have spoiled it?',
                        'What does the five-day trend show?',
                        'What do you bring to the nephrologist, and what do you leave to them?']},
 'sections': [('what-the-evidence',
               'What the evidence',
               'What the evidence showed about clearance',
               '\n'
               '<p><strong>ADEMEX</strong> (Mexico, 2002) randomized 965 CAPD patients either to continue four 2-liter exchanges daily or '
               'to a modified prescription aimed at a higher peritoneal creatinine clearance. Peritoneal clearance rose and stayed higher '
               'in the intervention group, but survival was the same (relative risk of death 1.00, 95% CI 0.80–1.24). Two-year survival '
               'was about 68% in the control group and 69% in the intervention group.[[pd_paniagua2002]]</p>\n'
               '<p><strong>The Hong Kong trial</strong> (2003) randomized 320 new CAPD patients with little residual function to total '
               'weekly Kt/V targets of 1.5–1.7, 1.7–2.0 or above 2.0. Two-year survival did not differ significantly (87%, 86% and 82%). '
               'More patients in the lowest-target group were withdrawn by their physicians for clinical problems, and more needed '
               'erythropoietin. The authors recommended a minimum total Kt/V above 1.7.[[pd_lo2003]]</p>\n'
               '<p><strong>What this means.</strong> Above a modest floor, more small-solute clearance does not buy survival. Kt/V is a '
               'surrogate: a laboratory measure of dose, not an outcome patients feel. The 2020 ISPD practice recommendations on '
               'prescribing high-quality goal-directed PD therefore treat Kt/V and creatinine clearance as one input among several, not as '
               'the definition of adequate dialysis. These recommendations are practice points, not graded recommendations, because the '
               'evidence base is limited.[[pd_brown2020]]</p>\n'),
              ('goal-directed-pd',
               'Goal-directed PD',
               'Goal-directed PD',
               '\n'
               '<p>The 2020 ISPD recommendations describe care goals agreed through shared decision-making between the person and the '
               'team, aiming both to let the person achieve their own life goals and to deliver high-quality care. In practice, the review '
               'covers:[[pd_brown2020]]</p>\n'
               '{{fig:pd06_dash}}\n'
               '\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Domain</th><th>What you bring to the review</th></tr></thead>\n'
               '<tbody><tr><td>Person&rsquo;s goals and symptoms</td><td>Energy, sleep, appetite, nausea, itch, restless legs, mood, '
               'ability to work or care for family</td></tr><tr><td>Fluid status</td><td>Weight trend, blood pressure, edema, '
               'breathlessness, daily UF, urine volume</td></tr><tr><td>Residual kidney function</td><td>Urine volume trend; timed urine '
               'collection when ordered</td></tr><tr><td>Delivered therapy</td><td>Exchanges done versus ordered, cycler completion, '
               'missed treatments</td></tr><tr><td>Nutrition</td><td>Appetite, weight change, diet history; the 2026 joint ISRNM–ISPD '
               'nutrition recommendations emphasize screening and monitoring nutrition status, managing protein-energy wasting, and '
               'education to build food literacy</td></tr><tr><td>Metabolic</td><td>Potassium (hypokalemia is common in PD and is a '
               'modifiable peritonitis risk factor in the 2022 ISPD recommendations), glucose in people with '
               'diabetes</td></tr><tr><td>Solute clearance</td><td>Kt/V and creatinine clearance results, interpreted with the '
               'rest</td></tr><tr><td>Membrane function</td><td>PET results and UF capacity</td></tr></tbody></table></div>\n'),
              ('the-peritoneal-equilibration',
               'The peritoneal equilibration',
               'The peritoneal equilibration test',
               '\n'
               '<p><strong>What it measures.</strong> The PET characterizes how quickly small solutes cross the membrane (peritoneal '
               'solute transfer rate, PSTR) and how much water a standard dwell removes.</p>\n'
               '{{fig:pd06_pet}}\n'
               '\n'
               '<p><strong>How it is done (ISPD 2021).</strong> A 4-hour dwell with either 2.27% glucose (2.5% dextrose) or 3.86% glucose '
               '(4.25% dextrose), using creatinine as the index solute. The key result is the dialysate-to-plasma creatinine ratio at 4 '
               'hours (D/P creatinine). Higher values mean faster transfer.[[pd_morelle2021]]</p>\n'
               '<p><strong>When.</strong> Early, between 6 and 12 weeks after starting PD (GRADE 1A for timing), and later when clinically '
               'indicated, for example after a fall in UF or after severe peritonitis.[[pd_morelle2021]]</p>\n'
               '{{key:Why it matters.}}\n'
               '<ul><li>A faster PSTR is associated with lower survival on PD (GRADE 1A in the 2021 recommendations). Part of the reason '
               'is lower UF and more fluid reabsorption in long dwells.</li><li>That fluid problem can be mitigated by shortening glucose '
               'dwells, using icodextrin, or using higher glucose concentrations (GRADE 1A). Icodextrin, compared with glucose, can '
               'improve fluid status and reduce episodes of fluid overload (GRADE 1A).</li><li><strong>Low UF capacity</strong> should be '
               'suspected when net UF from a 4-hour PET is less than 400 mL with 3.86% glucose (4.25% dextrose) or less than 100 mL with '
               '2.27% glucose (2.5% dextrose) (GRADE 1B), or when daily UF is not enough to keep the person euvolemic (practice point). '
               'Low UF can also come from mechanical problems or leaks.</li><li>When low UF is suspected, a 3.86% PET with measurement of '
               'the <strong>sodium dip at 1 hour</strong> helps identify intrinsic membrane dysfunction (reduced aquaporin-mediated water '
               'transport).</li></ul>\n'
               '<p><strong>The nurse&rsquo;s part is accuracy.</strong> The result is only as good as the timing of the samples, the '
               'completeness of the drain, the dwell length and the solution strength actually used.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Step</th><th>What can spoil it</th></tr></thead>\n'
               '<tbody><tr><td>Overnight dwell before the test</td><td>Wrong solution or length per protocol</td></tr><tr><td>Drain before '
               'the test dwell</td><td>Incomplete drain leaves residual fluid that dilutes results</td></tr><tr><td>Infusion</td><td>Wrong '
               'strength; slow infusion shifts timing</td></tr><tr><td>Samples at specified times</td><td>Missed or late '
               'samples</td></tr><tr><td>Blood sample</td><td>Not drawn at the specified time</td></tr><tr><td>Final '
               'drain</td><td>Incomplete; drain volume not measured accurately</td></tr><tr><td>Glucose correction for creatinine '
               'assay</td><td>Some laboratory methods need correction for high dialysate glucose; confirm with the '
               'laboratory</td></tr></tbody></table></div>\n'),
              ('adequacy-collections',
               'Adequacy collections',
               'Adequacy collections',
               '\n'
               '<p>Weekly Kt/V and creatinine clearance in PD combine a 24-hour effluent collection, a 24-hour urine collection and a '
               'blood sample. Teach the patient exactly how to collect: start and end times, all bags or a measured aliquot per protocol, '
               'urine container, storage and transport. Document missed samples. Ask the team whether an incomplete collection should be '
               'repeated. <strong>An invalid collection is worse than none, because it looks like evidence.</strong></p>\n'),
              ('reading-trends',
               'Reading trends',
               'Reading trends',
               '\n'
               '<p>State the baseline, the interval and the current value. Then give context: missed exchanges, changes in intake, falling '
               'urine, measurement changes, intercurrent illness, symptoms. A trend over a week is more informative than a single '
               'day.</p>\n')],
 'debrief': ['<p><strong>Hazel&rsquo;s review.</strong> She screens for emergency signs (none at rest), records the trends with dates, '
             'notes that the long night glucose dwell is net-negative most days, and presents the PET result with the observation that the '
             'pattern fits faster solute transfer with fluid reabsorption in the long dwell. She does not suggest a specific prescription. '
             'The nephrologist reviews and considers changes to the long dwell. Hazel teaches salt restriction and arranges a weight and '
             'symptom check in three days.</p>'],
 'skills': {'title': 'Practice drill',
            'intro': 'Using the trend table in WORKSHEETS.md, plot seven days of weight, UF and urine. Mark the missed dwell. Write a '
                     'five-line handoff that states what can be inferred, what needs verification and what needs escalation.',
            'items': [('Using the trend table in WORKSHEETS.md, plot seven days of weight, UF and urine.', False),
                      ('Mark the missed dwell.', False),
                      ('Write a five-line handoff that states what can be inferred, what needs verification and what needs escalation.',
                       False)]},
 'quiz': [('In ADEMEX, increasing peritoneal creatinine clearance:',
           ['Did not change survival (relative risk 1.00)', 'Reduced mortality by half', 'Increased mortality', 'Was never achieved'],
           0,
           'Clearance rose; survival was the same.'),
          ('Kt/V urea is best described as:',
           ['A patient-important outcome', 'A measure of fluid removal', 'A surrogate measure of dose', 'A measure of membrane transport'],
           2,
           'It is a laboratory surrogate.'),
          ('The 2020 ISPD goal-directed prescribing recommendations are:',
           ['GRADE 1A recommendations', 'Regulations', 'Withdrawn', 'Practice points'],
           3,
           'Labeled practice points.'),
          ('When should the first PET be done according to the 2021 ISPD recommendations?',
           ['On day 1 of PD', 'Between 6 and 12 weeks after starting PD', 'After 5 years', 'Only after peritonitis'],
           1,
           'GRADE 1A for timing.'),
          ('A faster peritoneal solute transfer rate is associated with:',
           ['Better survival', 'Lower survival on PD, partly through lower UF in long dwells', 'No effect', 'Fewer infections'],
           1,
           'GRADE 1A association.'),
          ('Which 4-hour PET result suggests low UF capacity with 3.86% glucose?',
           ['Net UF more than 800 mL', 'Net UF of exactly 1,000 mL', 'Any positive UF', 'Net UF less than 400 mL'],
           3,
           'The ISPD 2021 threshold (GRADE 1B).'),
          ('And with 2.27% glucose?',
           ['Net UF less than 100 mL', 'Net UF less than 1,000 mL', 'Net UF greater than 400 mL', 'Not defined'],
           0,
           'The 2.27% threshold is less than 100 mL.'),
          ('What does the sodium dip at 1 hour of a 3.86% dwell help assess?',
           ['Infection', 'Potassium balance', 'Aquaporin-mediated free-water transport (intrinsic membrane function)', 'Catheter position'],
           2,
           'Reduced dip suggests impaired free-water transport.'),
          ('Which step most often spoils a PET?',
           ['Labeling the patient&rsquo;s name', 'Using a clean table', 'Incomplete drain or mistimed samples', 'Measuring blood pressure'],
           2,
           'Timing and drain completeness drive accuracy.'),
          ('A 24-hour effluent collection missed one bag. Best action?',
           ['Record the omission, inform the team, and ask whether to repeat',
            'Report the result as complete',
            'Estimate the missing bag',
            'Discard the whole result silently'],
           0,
           'Transparency preserves the result&rsquo;s meaning.'),
          ('Which is a modifiable peritonitis risk factor named in the 2022 ISPD recommendations that also appears in metabolic '
           'monitoring?',
           ['Hypernatremia', 'Hypokalemia', 'Hypercalcemia', 'Anemia'],
           1,
           'Hypokalemia is common in PD and a named modifiable risk.'),
          ('In the Hong Kong trial, patients assigned to the lowest Kt/V target (1.5–1.7):',
           ['Had markedly lower survival',
            'Had better nutrition',
            'Were all transferred to hemodialysis',
            'Had similar survival but more clinical problems and erythropoietin needs'],
           3,
           'Survival did not differ significantly.'),
          ('What should accompany a clearance result in a nursing review?',
           ['Nothing else',
            'Only the patient&rsquo;s age',
            'Only the PET result',
            'Symptoms, fluid status, residual urine, nutrition, delivered therapy and collection quality'],
           3,
           'Clearance is one input among many.'),
          ('Icodextrin compared with glucose for the long dwell:',
           ['Worsens fluid status',
            'Can improve fluid status and reduce fluid-overload episodes (GRADE 1A)',
            'Prevents peritonitis',
            'Has no role'],
           1,
           'Per ISPD 2021.'),
          ('When reporting a trend, which statement is most useful?',
           ['"Weight is up."',
            '"He is doing okay."',
            '"Weight rose from 68.0 to 70.0 kg over five days while daily UF fell from about 750 to 450 mL and urine from about 600 to 350 '
            'mL; all exchanges done; mild exertional dyspnea."',
            '"See chart."'],
           2,
           'Baseline, interval, current values and context.')],
 'terms': [('Peritoneal dialysis (PD)',
            'Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter.'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis: manual exchanges through the day.'),
           ('Dwell', 'The time dialysis solution stays in the abdomen between fill and drain.'),
           ('Ultrafiltration (UF)', 'Fluid removed by dialysis; net UF is drained volume minus instilled volume.'),
           ('Icodextrin', 'A large glucose polymer solution absorbed slowly, used for long dwells.'),
           ('Residual kidney function', "The filtering and urine output the patient's own kidneys still provide."),
           ('Aquaporin', 'A water-only channel in capillary walls that lets water cross without sodium.'),
           ('Cycler', 'The machine that performs APD exchanges.'),
           ('Peritoneal equilibration test (PET)',
            'A standardized 4-hour dwell that measures how fast solutes cross the membrane and how much water is removed.'),
           ('D/P creatinine', 'Dialysate-to-plasma creatinine ratio; higher values mean faster solute transfer.'),
           ('Kt/V', 'A laboratory measure of urea clearance used as a surrogate for dialysis dose.'),
           ('Peritonitis', 'Infection or inflammation of the peritoneum, usually shown by cloudy effluent.'),
           ('Effluent', 'Fluid drained from the abdomen after a dwell.')],
 'readings': [('dialysis-adequacy.html', 'Dialysis adequacy measures and their limits.'),
              ('eating-on-dialysis.html', 'Nutrition on dialysis.')],
 'calcs': ['calc-pd-adequacy.html', 'calc-pd-glucose-absorption.html', 'calc-nutrition-screening.html']}
