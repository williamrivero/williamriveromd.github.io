# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 04: The CAPD exchange, measurement and contamination response. Generated from PD Nurse v2 blueprint (modules/pd04-*.md). Edit here."""

MODULE = {'image_alt': '',
 'objectives': ['Explain why the "flush before fill" step in a twin-bag (double-bag) system protects the peritoneum, and the trial '
                'evidence behind it.',
                'Verify an exchange against the written order and reject a compromised supply.',
                'Demonstrate a CAPD exchange in simulation using the unit&rsquo;s approved checklist for the actual device.',
                'Calculate and interpret net ultrafiltration for an exchange and for a day, including the measurement errors that distort '
                'it.',
                'Classify a contamination event as dry or wet, and run the contamination call with the details the team needs.'],
 'big': '<p>A CAPD patient performs more than a thousand exchanges a year. Each one is a moment when the sterile inside of the system is '
        'briefly opened to the room. Nearly all peritonitis from touch contamination starts with one lapse in one of those moments. Your '
        'work is to teach a technique that is the same every time, to make measurement honest, and to make sure that when a lapse happens, '
        'the patient stops and calls rather than hoping it will be fine.</p>\n'
        '{{plain:Think of an exchange as a sealed water system with one valve you must open by hand. As long as nothing touches the '
        'valve&rsquo;s inner surfaces, the system stays clean. The moment a finger, a sleeve or a drop of tap water touches the inside of '
        'a connector, the system is no longer closed.}}\n'
        '<p>The picture has a limit. PD solution is not just water: it is a warm, glucose-rich fluid, an excellent culture medium. A few '
        'bacteria introduced at connection can multiply during a four-hour dwell inside the abdomen. That is why a single touch matters '
        'and why the response is time-sensitive.</p>',
 'case': {'title': 'A sleeve and a connector',
          'html': '<p><strong>Tita Carmen, 63</strong>, is in her second week of CAPD training. Nurse <strong>Bea</strong> observes.</p>\n'
                  '<p>Carmen checks her bag, washes her hands and connects. During the drain phase she reaches to scratch her nose and her '
                  'sleeve brushes the open connector of the new bag line before she connects it. She pauses, then reaches for an alcohol '
                  'swab.</p>',
          'questions': ['What kind of contamination is this, dry or wet?',
                        'What do you do with the bag and the exchange?',
                        'What do you say to Carmen so she keeps reporting?']},
 'sections': [('the-physiology-and',
               'The physiology and',
               'The physiology and the engineering',
               '\n'
               '<p><strong>Why "flush before fill" works.</strong> Modern CAPD uses a Y-shaped twin-bag system: one tube to a fresh bag, '
               'one to a drainage bag, joined to the patient&rsquo;s transfer set. After connecting, the patient first drains the abdomen, '
               'then flushes a small amount of fresh solution directly into the drainage bag. Any bacteria introduced at the moment of '
               'connection are washed out to the drain bag instead of being pushed into the peritoneum. Only then does fresh solution fill '
               'the abdomen.</p>\n'
               '{{fig:pd04_flush}}\n'
               '\n'
               '<p><strong>The evidence.</strong> A Cochrane systematic review of 12 randomized or quasi-randomized trials (991 patients) '
               'found that Y-set or double-bag systems reduced the proportion of patients who developed peritonitis compared with older '
               'standard spike systems (odds ratio 0.33, 95% CI 0.24–0.46). Double-bag systems also outperformed Y-sets (odds ratio 0.44, '
               '95% CI 0.27–0.71). This is strong, replicated randomized evidence on a patient-important outcome, and it is why twin-bag '
               'systems are the standard. The trials are old and conducted mostly in high-income settings, but the mechanism is direct and '
               'the effect large.[[pd_daly2001]]</p>\n'
               '<p><strong>What the patient controls.</strong> Hand hygiene, a clean surface, no fan or open window blowing toward the '
               'connection, no pets in the room, a mask if the program requires one, never touching the connector tips, and checking every '
               'bag before using it.</p>\n'),
              ('before-the-exchange',
               'Before the exchange',
               'Before the exchange',
               '\n'
               '<p>Use the approved checklist for the system the patient actually has. The steps below are principles, not a '
               'procedure.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Check</th><th>Why</th></tr></thead>\n'
               '<tbody><tr><td>Patient identity and current written order</td><td>Orders change; an outdated card at home is a common '
               'error</td></tr><tr><td>Solution type and strength (for example 1.5%, 2.5% or 4.25% dextrose, or icodextrin)</td><td>Wrong '
               'strength changes fluid removal; wrong product can cause harm</td></tr><tr><td>Fill volume and dwell '
               'timing</td><td>Prescribed by the nephrologist</td></tr><tr><td>Expiry, clarity, seals, pull rings, package '
               'integrity</td><td>A leaking or cloudy bag may be contaminated</td></tr><tr><td>Warming method</td><td>Only approved dry '
               'warming methods; never a microwave or hot water bath unless the device instructions allow it</td></tr><tr><td>Environment '
               'and hand hygiene</td><td>Clean, closed room; hands washed and dried per program</td></tr></tbody></table></div>\n'
               '{{key:Replace any questionable supply before you begin. A doubtful bag is never "probably fine."}}\n'),
              ('during-and-after',
               'During and after',
               'During and after',
               '\n'
               '<p>Follow the device instructions for connection, drain, flush, fill and disconnection. Protect critical parts from touch. '
               'Observe comfort and flow. Look at the drained effluent against a printed text or a white background: you should be able to '
               'read through it. Cloudy effluent is a same-day call (PD07).</p>\n'
               '<p>Record actual fill and drain volumes, dwell timing, effluent appearance, symptoms, and any deviation.</p>\n'),
              ('measuring-ultrafiltration-honestly',
               'Measuring ultrafiltration honestly',
               'Measuring ultrafiltration honestly',
               '\n'
               '<p><strong>Net ultrafiltration (UF) for one exchange = drained volume − instilled volume.</strong> A positive number means '
               'fluid was removed; a negative number means fluid was absorbed.</p>\n'
               '{{key:Daily net UF = the sum of all exchanges in 24 hours.}}\n'
               '<p>Most errors come from measurement, not physiology:</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Source of error</th><th>Effect</th><th>Fix</th></tr></thead>\n'
               '<tbody><tr><td>Bag overfill (manufacturers may add volume beyond the labeled fill)</td><td>Overestimates or distorts UF '
               'depending on method</td><td>Use the unit&rsquo;s standard method (weighing bags, or labeled volume) '
               'consistently</td></tr><tr><td>Flush volume going to drain bag</td><td>Inflates "drain" if not accounted for</td><td>Teach '
               'the unit&rsquo;s convention</td></tr><tr><td>Incomplete drain</td><td>Underestimates UF; leaves fluid in '
               'abdomen</td><td>Check position, drain time; report persistent incomplete drain</td></tr><tr><td>Spills or '
               'leaks</td><td>Unknown loss</td><td>Record as a deviation</td></tr><tr><td>Different scales or methods day to '
               'day</td><td>False trends</td><td>Same scale, same method, same time</td></tr></tbody></table></div>\n'
               '<p><strong>Worked calculation.</strong> Fill 2,000 mL, drain 2,350 mL: net UF = +350 mL. Fill 2,000 mL, drain 1,850 mL: '
               'net UF = −150 mL (fluid absorbed). A negative long dwell may be expected physiology with glucose (PD01) or may signal a '
               'problem; trend it and report it.</p>\n'),
              ('contamination-dry-or',
               'Contamination: dry or wet',
               'Contamination: dry or wet',
               '\n'
               '<p>The 2022 ISPD peritonitis recommendations revised the guidance on managing contamination of the PD system. Programs '
               'commonly classify events this way:[[pd_li2022]]</p>\n'
               '{{fig:pd04_contam}}\n'
               '\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Type</th><th>What happened</th><th>Typical program response (per protocol and '
               'prescriber)</th></tr></thead>\n'
               '<tbody><tr><td><strong>Dry contamination</strong></td><td>A break in sterile technique occurred but the system was closed '
               '(clamp shut) and no fluid was infused after the break</td><td>Stop. Do not proceed with that connection. Replace the '
               'affected component (for example cap or transfer set) as the program directs. Report.</td></tr><tr><td><strong>Wet '
               'contamination</strong></td><td>The system was open, or fluid was infused after the break, or there is a leak in the '
               'system</td><td>Stop. Clamp. Do not fill (or stop filling). Call the PD team at once. The team may send effluent for '
               'testing and may prescribe prophylactic antibiotics.</td></tr></tbody></table></div>\n'
               '<p><strong>The contamination call.</strong> State exactly what touched what, when, whether the clamp was closed, whether '
               'any fluid entered after the touch, whether the transfer set or catheter is damaged, and whether there are any symptoms. '
               'Record the time of the call, who accepted it, and the instructions given, read back.</p>\n'
               '<p><strong>The teaching message.</strong> "If anything touches the tip, stop and call. Do not wipe it and continue." '
               'Patients who fear blame hide contamination. Make calling feel safe.</p>\n'),
              ('red-flags-in',
               'Red flags in this module',
               'Red flags in this module',
               '\n'
               '{{stop:<ul><li>Cloudy effluent at any exchange.</li><li>Fluid leaking around the exit site during fill.</li><li>Severe '
               'pain on inflow or outflow.</li><li>A cracked transfer set or catheter.</li></ul>}}\n')],
 'debrief': ['<p><strong>Bea stops the exchange.</strong> The clamp on the new line is closed and no fresh fluid has been infused. This is '
             'dry contamination of the new bag&rsquo;s connector. Bea discards that bag, has Carmen re-wash her hands, uses a fresh bag '
             'and completes the exchange. She records the event and tells the PD nurse coordinator. Then she uses the moment: "You did the '
             'right thing by stopping. Next time, call me before you swab anything."</p>\n'
             '<p>Later in the week the drained volume of Carmen&rsquo;s exchange reads 2,350 mL from a 2,000 mL fill: net UF +350 mL, '
             'clear effluent. Bea asks her to say aloud what she would do if the drained fluid were cloudy. Carmen: "Save the bag and call '
             'the PD unit today."</p>'],
 'skills': {'title': 'CAPD exchange with a compromised bag (OSCE station 1)',
            'intro': 'Using a mock order and a training kit, identify a seeded packaging defect, perform the exchange with the approved '
                     'checklist, and rehearse both a dry and a wet contamination call with your preceptor acting as the on-call nurse.',
            'items': [('Verifies patient identity and the written prescription.', True),
                      ('Rejects a compromised supply.', True),
                      ('Protects critical parts and stops at a breach.', True),
                      ('Demonstrates the device-specific flow using the approved checklist.', False),
                      ('Records volumes and effluent appearance.', False)]},
 'quiz': [('Why does flushing fresh solution to the drain bag before filling reduce peritonitis risk?',
           ['It washes bacteria introduced at connection into the drain bag instead of the peritoneum',
            'It warms the solution',
            'It removes glucose',
            'It measures the fill volume'],
           0,
           'That is the mechanism of flush before fill.'),
          ('In the Cochrane review of 12 trials, Y-set or double-bag systems compared with standard systems:',
           ['Increased peritonitis',
            'Had no effect',
            'Reduced the proportion of patients with peritonitis (odds ratio 0.33)',
            'Were never tested in trials'],
           2,
           'Randomized evidence showed a large reduction.'),
          ('Fill 2,000 mL, drain 1,850 mL. What is net UF?',
           ['+150 mL', '3,850 mL', '0 mL', '−150 mL'],
           3,
           '1,850 − 2,000 = −150 mL; fluid was absorbed.'),
          ('Fill 2,000 mL, drain 2,350 mL. What is net UF?',
           ['−350 mL', '+350 mL', '+2,350 mL', '+4,350 mL'],
           1,
           '2,350 − 2,000 = +350 mL.'),
          ('A bag has a small leak at the seal. Best action?',
           ['Use it quickly', 'Replace it before beginning and report the defect', 'Tape the leak', 'Use it for the drain bag only'],
           1,
           'A compromised bag may be contaminated.'),
          ('The patient touches the tip of the new bag connector; the clamp is closed and no fluid has entered. This is:',
           ['Wet contamination', 'Not contamination', 'Peritonitis', 'Dry contamination'],
           3,
           'System closed, no infusion after the break.'),
          ('The transfer set disconnects while the clamp is open and fluid drips out. This is best classified as:',
           ['Wet contamination; clamp and call the PD team at once', 'Dry contamination', 'A normal event', 'A drain alarm'],
           0,
           'The system was open.'),
          ('What information matters most in a contamination call?',
           ['The patient&rsquo;s favorite food',
            'Only the time',
            'What touched what, when, clamp status, whether fluid entered, damage and symptoms',
            'The brand of solution only'],
           2,
           'These details guide the team&rsquo;s response.'),
          ('Which warming method is acceptable?',
           ['Microwave', 'Hot water bath', 'Only the approved dry warming method per device instructions', 'Direct sunlight'],
           2,
           'Other methods risk overheating or contamination.'),
          ('Why should the same scale and method be used every day?',
           ['To avoid false UF trends from measurement differences', 'To save time', 'Because scales are expensive', 'It does not matter'],
           0,
           'Consistency makes trends meaningful.'),
          ('A patient wipes the touched connector with alcohol and continues. The best teaching response is:',
           ['Praise them for cleaning it',
            'Explain that a touched sterile part requires stopping and calling, and make calling feel safe',
            'Ignore it',
            'Report them for noncompliance'],
           1,
           'Wiping does not restore sterility; blame discourages reporting.'),
          ('How can a patient check effluent clarity simply?',
           ['Smell it', 'Taste it', 'Shake it', 'Look through it at printed text or a white background'],
           3,
           'Inability to read through it suggests cloudiness.'),
          ('Which is a measurement error rather than physiology?',
           ['Negative UF after a long glucose dwell',
            'Higher UF with 4.25% dextrose',
            'Lower UF during peritonitis',
            'A different scale used on alternate days'],
           3,
           'The others reflect physiology.'),
          ('Who decides whether prophylactic antibiotics are given after wet contamination?',
           ['The patient', 'The prescriber, per the unit&rsquo;s protocol', 'The nurse alone', 'The supplier'],
           1,
           'Antibiotic decisions belong to the prescriber or standing protocol.'),
          ('Why is a single touch contamination significant in PD?',
           ['It changes solution strength',
            'It damages the catheter',
            'PD solution is a glucose-rich medium where bacteria can multiply during a dwell',
            'It is not significant'],
           2,
           'Bacteria introduced can grow in the warm, glucose-rich fluid.')],
 'terms': [('Peritoneal dialysis (PD)',
            'Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter.'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis: manual exchanges through the day.'),
           ('Dwell', 'The time dialysis solution stays in the abdomen between fill and drain.'),
           ('Ultrafiltration (UF)', 'Fluid removed by dialysis; net UF is drained volume minus instilled volume.'),
           ('Icodextrin', 'A large glucose polymer solution absorbed slowly, used for long dwells.'),
           ('Exit site', 'The point where the PD catheter leaves the skin.'),
           ('Flush before fill',
            'Sending a little fresh solution straight to the drain bag before filling, to wash out bacteria introduced at connection.'),
           ('Dry contamination', 'A break in sterile technique with the system closed and no fluid infused after the break.'),
           ('Wet contamination', 'A break with the system open, fluid infused after the break, or a leak.'),
           ('Peritonitis', 'Infection or inflammation of the peritoneum, usually shown by cloudy effluent.'),
           ('Effluent', 'Fluid drained from the abdomen after a dwell.')],
 'readings': [('peritoneal-dialysis-ckd.html', 'What patients learn about exchanges at home.')],
 'calcs': ['calc-pd-glucose-absorption.html']}
