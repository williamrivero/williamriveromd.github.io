# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 05: APD: cycler setup, the treatment record and alarms. Generated from PD Nurse v2 blueprint (modules/pd05-*.md). Edit here."""

MODULE = {'image_alt': '',
 'objectives': ['Explain how an APD prescription (total volume, fill volume, number of cycles, tidal mode, last fill, day dwell) shapes '
                'clearance and fluid removal.',
                'Cross-check a programmed cycler against the written order and stop on any mismatch.',
                'Read a cycler treatment record (or remote-monitoring summary) for completion, drain patterns, ultrafiltration and alarms.',
                'Respond safely to drain alarms, interruptions and power failure, using only device-permitted checks.',
                'Recognize when an alarm is a symptom of a clinical problem that needs urgent assessment.'],
 'big': '<p>APD moves dialysis into the night. That brings freedom in the day and a new set of risks at 2 AM: a machine programmed '
        'differently from the order, a drain alarm that wakes the patient five times, a brownout in the middle of a cycle, a long day '
        'dwell that quietly absorbs fluid back. Your work is to make sure that what the cycler does is exactly what the nephrologist '
        'ordered, to read its record like a nursing note, and to treat repeated alarms as clinical information.</p>\n'
        '{{plain:Think of the cycler as a very obedient assistant that follows a written recipe exactly, all night, without judgment. If '
        'the recipe card is wrong, it makes the wrong dish perfectly.}}\n'
        '<p>The picture has a limit. A recipe does not change the cook. The cycler&rsquo;s record, though, tells you about the patient: '
        'how well the catheter drains, whether the abdomen tolerates the fill volume, whether the person stayed connected. The machine is '
        'both a delivery device and a monitoring device.</p>',
 'case': {'title': 'Six alarms by morning',
          'html': '<p><strong>Kristine, 29</strong>, public-school teacher in Pampanga, has been on APD for three months with a night '
                  'program and an icodextrin day dwell. Nurse <strong>Arnel</strong> reviews her cycler summary.</p>\n'
                  '<p><strong>Night 1–5.</strong> Therapy completes. Initial drain of the day dwell is about 2,100 mL from a 2,000 mL last '
                  'fill. Total UF is about 800 mL a night.</p>\n'
                  '<p><strong>Night 6.</strong> Four low-drain alarms between 1 and 4 AM; therapy runs 70 minutes longer. Initial drain is '
                  '1,600 mL.</p>\n'
                  '<p><strong>Night 7.</strong> Six alarms; total UF about 300 mL.</p>',
          'questions': ['What does the pattern in the cycler record tell you?',
                        'What is the most likely cause, and what makes peritonitis less likely?',
                        'What do you report, and to whom?']},
 'sections': [('the-physiology-of',
               'The physiology of',
               'The physiology of an APD prescription',
               '\n'
               '<p>APD usually delivers several short exchanges overnight. Short dwells keep the diffusion gradient steep (PD01), which '
               'helps small-solute clearance, and keep the glucose gradient strong, which helps fluid removal during the night. The '
               'trade-offs come in the day:</p>\n'
               '{{fig:pd05_night}}\n'
               '\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Prescription element</th><th>What it does</th><th>What can go wrong</th></tr></thead>\n'
               '<tbody><tr><td>Total night volume and cycle count</td><td>Sets night clearance</td><td>Too many short cycles waste time '
               'draining and filling</td></tr><tr><td>Fill volume</td><td>Larger fills increase membrane contact</td><td>Discomfort, '
               'breathlessness, leak, hernia</td></tr><tr><td>Tidal mode (partial drain each cycle)</td><td>Keeps some fluid in; reduces '
               'drain pain and alarms</td><td>Fluid accumulation if UF is not accounted for</td></tr><tr><td>Last fill / day '
               'dwell</td><td>Adds clearance and middle-molecule removal over the day</td><td>A long glucose day dwell may become '
               'net-positive; icodextrin is often used</td></tr><tr><td>Midday exchange</td><td>Splits a long day dwell</td><td>Adds a '
               'manual connection</td></tr><tr><td>No day dwell ("dry day")</td><td>Comfort, less glucose</td><td>Less clearance; may be '
               'insufficient once urine falls</td></tr></tbody></table></div>\n'
               '<p>The prescription is the nephrologist&rsquo;s. Your role is to know what each element does so you can spot when the '
               'record and the patient do not match.</p>\n'),
              ('what-the-evidence',
               'What the evidence shows',
               'What the evidence shows',
               '\n'
               '<p>In PDOPPS, an observational cohort of 7,051 adults across seven countries, facilities with higher APD use had lower '
               'peritonitis risk (rate ratio 0.95 per 10-percentage-point higher APD use, 95% CI 0.91–1.00). This is an association at the '
               'facility level, at the margin of statistical significance, and does not show that switching any individual to APD prevents '
               'peritonitis.[[pd_perl2020]]</p>\n'
               '<p>The 2021 ISPD membrane recommendations note that APD and icodextrin may mitigate the mortality risk associated with '
               'fast peritoneal solute transfer; that statement is a practice point, not a graded recommendation.[[pd_morelle2021]]</p>\n'),
              ('prepare-and-verify',
               'Prepare and verify',
               'Prepare and verify',
               '\n'
               '<p>Before the first setup and after any order change:</p>\n'
               '<ol><li>Confirm the patient and the current written order.</li><li>Cross-check on the cycler: therapy type, total volume, '
               'fill volume, number of cycles, therapy time, tidal settings if used, last fill volume and solution, patient weight if '
               'entered, and any UF limits set by the team.</li><li>Check solutions: type, strength, volume, expiry, integrity, and that '
               'the bags placed on the cycler match the program.</li><li>Escalate any mismatch before initiation. <strong>Do not "correct" '
               'a program to match your guess of what was meant.</strong></li><li>Prepare the space: clean, stable surface, cycler at the '
               'height the manufacturer specifies relative to the patient, drain line positioned to a toilet, drain or collection '
               'container as the unit approves.</li><li>Set up, prime and connect using the model-specific instructions, protecting '
               'sterile connections.</li></ol>\n'),
              ('read-the-treatment',
               'Read the treatment record',
               'Read the treatment record',
               '\n'
               '<p>A cycler record or remote-monitoring summary is a nursing assessment tool. Review:</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Item</th><th>What to look for</th></tr></thead>\n'
               '<tbody><tr><td>Completion</td><td>Full therapy delivered? Early stops? Bypassed drains?</td></tr><tr><td>Therapy '
               'time</td><td>Much longer than prescribed suggests slow drains</td></tr><tr><td>Initial drain</td><td>Volume of the day '
               'dwell drained at night start; low values suggest day-dwell absorption or catheter problems</td></tr><tr><td>Cycle-by-cycle '
               'drain</td><td>Progressive fall suggests catheter malposition, constipation, fibrin</td></tr><tr><td>Total UF</td><td>Trend '
               'over days against weight and urine</td></tr><tr><td>Alarms</td><td>Type, phase, frequency, time of '
               'night</td></tr><tr><td>Manual interventions</td><td>Bypasses, skipped cycles</td></tr></tbody></table></div>\n'
               '<p>Compare changes with symptoms, morning weights, blood pressure and urine trend. Obtain device logs only with consent '
               'and through the approved data system.</p>\n'),
              ('respond-to-alarms',
               'Respond to alarms',
               'Respond to alarms and interruptions',
               '\n'
               '<p><strong>Assess the person first.</strong> A drain alarm in a patient with severe abdominal pain is not a machine '
               'problem.</p>\n'
               '{{fig:pd05_alarm}}\n'
               '\n'
               '<p>Then:</p>\n'
               '<ol><li>Record the alarm, the phase, recurrence, time and symptoms.</li><li>Use only checks permitted by the device and '
               'the local plan: closed clamps, kinked lines, the patient lying on the line, cycler height, position change if the '
               'patient&rsquo;s condition allows.</li><li>Never override, bypass repeatedly or silence alarms outside the trained '
               'plan.</li><li>Follow the trained safe-disconnection and power-failure plan.</li><li>Backup CAPD is used only when there is '
               'a prescribed backup regimen, suitable supplies at home, and validated competence.</li><li>Repeated unresolved alarms or '
               'lost therapy require a call to the PD team.</li></ol>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Alarm pattern</th><th>Likely mechanisms</th><th>Red flags that change urgency</th></tr></thead>\n'
               '<tbody><tr><td>Low drain, every cycle, from the start</td><td>Catheter malposition, kink, constipation, fibrin, omental '
               'wrap</td><td>Severe pain, fever, cloudy effluent</td></tr><tr><td>Low drain, worsening over nights</td><td>Constipation, '
               'migration, rising fluid absorption</td><td>Breathlessness, weight gain</td></tr><tr><td>Drain pain at end of '
               'drain</td><td>Catheter tip against bowel or bladder</td><td>Persistent pain, cloudy effluent</td></tr><tr><td>Fill '
               'alarm</td><td>Clamp closed, kink, solution bag issue</td><td>Leak at exit site or swelling of genitals or abdominal '
               'wall</td></tr><tr><td>Repeated power interruptions</td><td>Unstable supply</td><td>Lost therapy plus rising '
               'weight</td></tr></tbody></table></div>\n'),
              ('red-flags-in',
               'Red flags in this module',
               'Red flags in this module',
               '\n'
               '{{stop:<ul><li>Severe abdominal pain with any alarm: urgent assessment through the PD pathway; emergency services if '
               'unstable.</li><li>Cloudy effluent in the drain bag or line in the morning.</li><li>Swelling of the abdominal wall, groin '
               'or genitals during therapy (possible leak).</li><li>Breathlessness after the last fill (possible hydrothorax or overfill; '
               'urgent).</li></ul>}}\n')],
 'debrief': ['<p>Arnel calls Kristine. She has had no bowel movement for four days since starting iron tablets. No fever, no abdominal '
             'pain, effluent clear, weight up 0.8 kg.</p>\n'
             '<p><strong>Arnel&rsquo;s reasoning.</strong> The alarm pattern is progressive and started with constipation, a common cause '
             'of catheter malfunction because a loaded bowel displaces the catheter tip. Clear effluent and no pain make peritonitis '
             'unlikely now. He reports the full pattern (alarm count, phase, timing, therapy delivered, initial drain trend, UF trend, '
             'bowel history, weight) to the nephrologist the same day. Bowel management is ordered. He arranges a review and an abdominal '
             'X-ray if drain does not recover, as the team decides. He teaches Kristine to report constipation early.</p>\n'
             '<p><strong>Take-home.</strong> Repeated drain alarms are symptoms. Read them with the bowel, the weight and the '
             'effluent.</p>'],
 'skills': {'title': 'APD setup with a scripted alarm (OSCE station 2)',
            'intro': 'Compare a mock written order against a programmed training cycler. Identify a deliberately mismatched last-fill '
                     'volume and solution. Simulate an unresolved drain alarm and deliver an escalation call with exact alarm, phase, '
                     'frequency, checks tried, symptoms, effluent and therapy delivered.',
            'items': [('Verifies the cycler program against the written order.', True),
                      ('Prevents a contaminated connection.', True),
                      ('Identifies the external checks the device allows.', False),
                      ('Escalates an unresolved alarm without overriding it.', True),
                      ('Records completed and missed treatment.', False)]},
 'quiz': [('The programmed last-fill volume differs from the written order. What should happen?',
           ['Pause initiation and obtain clarification before treatment',
            'Use the program; the machine knows best',
            'Change the order to match the machine',
            'Skip the last fill'],
           0,
           'Never initiate on a mismatch.'),
          ('Why do short overnight dwells help small-solute clearance?',
           ['They increase protein loss',
            'They warm the abdomen',
            'They keep the diffusion gradient steep',
            'They stop glucose absorption completely'],
           2,
           'Frequent fresh fills restore the gradient.'),
          ('A long glucose day dwell may:',
           ['Always remove the most fluid', 'Prevent constipation', 'Have no effect', 'Become net-positive as the osmotic gradient fades'],
           3,
           'Icodextrin is often used for this reason.'),
          ('What does tidal mode do?',
           ['Fully drains every cycle',
            'Leaves a reserve volume to reduce drain pain and alarms',
            'Adds a day dwell',
            'Doubles the fill volume'],
           1,
           'Partial drains keep some fluid in.'),
          ('In PDOPPS, higher facility APD use was:',
           ['Proven to prevent peritonitis in individuals',
            'Associated with modestly lower peritonitis risk at the margin of significance',
            'Associated with higher peritonitis',
            'Not studied'],
           1,
           'Rate ratio 0.95 per 10 percentage points, CI 0.91–1.00, observational.'),
          ('A drain alarm occurs and the patient reports severe abdominal pain. First priority?',
           ['Repeat the drain cycle',
            'Override the alarm',
            'Tell the patient to sleep',
            'Assess the person and arrange urgent assessment through the PD pathway'],
           3,
           'Person first.'),
          ('Which check is usually permitted for a drain alarm?',
           ['Checking for closed clamps or kinked lines', 'Forceful flushing of the catheter', 'Disabling the alarm', 'Cutting the line'],
           0,
           'External checks per device instructions.'),
          ('A progressive fall in drain volumes over several nights with no bowel movement for four days most suggests:',
           ['Peritonitis', 'Normal variation', 'Constipation affecting catheter position', 'Exit-site infection'],
           2,
           'Constipation is a common cause of catheter dysfunction.'),
          ('What must accompany an escalation for recurring low drain?',
           ['Only "the machine keeps alarming"',
            'The patient&rsquo;s address',
            'Alarm type and phase, frequency, checks tried, symptoms, effluent and therapy delivered',
            'Nothing; wait for the morning'],
           2,
           'Complete data support decisions.'),
          ('When may backup CAPD be used during a power failure?',
           ['When a prescribed backup regimen, suitable supplies and validated competence exist',
            'Whenever the patient wishes',
            'Never',
            'Only in the hospital'],
           0,
           'Backup must be planned and validated.'),
          ('Swelling of the genitals during APD fill suggests:',
           ['Normal fill', 'Possible dialysate leak; report promptly', 'Peritonitis', 'Constipation'],
           1,
           'Leaks can track into the abdominal wall and genitals.'),
          ('A low initial drain of the day dwell at the start of night therapy may mean:',
           ['Excellent UF', 'The cycler is broken', 'Nothing', 'Day-dwell fluid absorption or catheter problems'],
           3,
           'Trend and report.'),
          ('Breathlessness soon after the last fill should prompt:',
           ['Ignoring it', 'More fluid', 'A larger fill next time', 'Urgent assessment for overfill or hydrothorax'],
           3,
           'Possible pleural leak or overfill.'),
          ('Who sets the APD prescription?',
           ['The PD nurse', 'The nephrologist', 'The supplier', 'The patient'],
           1,
           'The nurse verifies and monitors.'),
          ('Why is the cycler record described as a monitoring tool?',
           ['It replaces clinic visits',
            'It stores the patient&rsquo;s diet',
            'It shows drain patterns, completion, UF and alarms that reflect the patient&rsquo;s condition',
            'It sets the prescription automatically'],
           2,
           'The record carries clinical signals.')],
 'terms': [('Peritoneal dialysis (PD)',
            'Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter.'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis: manual exchanges through the day.'),
           ('APD', 'Automated peritoneal dialysis: a cycler performs exchanges, usually overnight.'),
           ('Dwell', 'The time dialysis solution stays in the abdomen between fill and drain.'),
           ('Ultrafiltration (UF)', 'Fluid removed by dialysis; net UF is drained volume minus instilled volume.'),
           ('Icodextrin', 'A large glucose polymer solution absorbed slowly, used for long dwells.'),
           ('Exit site', 'The point where the PD catheter leaves the skin.'),
           ('Cycler', 'The machine that performs APD exchanges.'),
           ('Tidal mode', 'An APD setting that leaves a reserve volume in the abdomen at each drain.'),
           ('Last fill', 'The final APD fill that stays in during the day, also called the day dwell.'),
           ('Peritonitis', 'Infection or inflammation of the peritoneum, usually shown by cloudy effluent.'),
           ('Effluent', 'Fluid drained from the abdomen after a dwell.'),
           ('Hydrothorax', 'Dialysate leaking into the chest through a gap in the diaphragm.'),
           ('Hernia', 'Bulging of abdominal contents through a weak point in the wall.')],
 'readings': [('fluid-management-dialysis.html', 'Fluid balance on dialysis.'),
              ('typhoon-disaster-preparedness-dialysis.html', 'Preparing dialysis patients for typhoons and outages.')],
 'calcs': ['calc-pd-adequacy.html', 'calc-dialysis-continuity-planner.html']}
