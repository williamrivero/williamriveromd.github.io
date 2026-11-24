# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 01: How peritoneal dialysis works, and what the PD nurse does. Generated from PD Nurse v2 blueprint (modules/pd01-*.md). Edit here."""

MODULE = {'image_alt': '',
 'objectives': ['Explain diffusion, osmotic ultrafiltration and fluid reabsorption across the peritoneal membrane, and why each changes '
                'during a dwell.',
                'Explain why water removal and small-solute clearance can move in different directions in the same patient.',
                'Explain the role of residual kidney function in volume and solute control, and why its loss changes how you read a PD '
                'record.',
                'Distinguish continuous ambulatory PD (CAPD) and automated PD (APD) by workflow, dwell pattern, equipment and failure '
                'modes.',
                'Separate what you observe, record and teach from what requires a prescriber&rsquo;s order, and state when to escalate.'],
 'big': '<p>Most of what goes wrong in peritoneal dialysis (PD) is slow and quiet. A drain volume falls by a few hundred milliliters a '
        'day. Urine output halves over two months. Ankles swell a little more each week. Very little of it announces itself as an '
        'emergency. Your work is to understand the physiology well enough that small numbers mean something to you, to put the pieces '
        'together before the patient becomes unwell, and to bring the whole pattern to the nephrologist early.</p>\n'
        '{{plain:Picture a tea bag in a cup of hot water. Flavor moves from where it is concentrated (the leaves) to where it is not (the '
        'water). Leave the bag longer and the cup darkens, but more and more slowly, because the difference between inside and outside '
        'keeps shrinking. That is diffusion, and it is how urea, creatinine and potassium move from blood into dialysate.}}\n'
        '<p>The picture has a limit. A tea bag does not pull water. PD solution does: its glucose (or icodextrin) draws water out of the '
        'blood by osmosis. And unlike a tea bag, the abdomen keeps absorbing fluid back into the body through lymphatics and tissue the '
        'whole time the solution sits there. So a PD dwell has three processes running at once: solute diffusion, osmotic water removal, '
        'and constant fluid reabsorption.</p>',
 'case': {'title': 'Positive numbers, rising weight',
          'html': '<p><strong>Aling Rosario, 58</strong>, has been on CAPD for seven months with four 2-liter exchanges a day. Nurse '
                  '<strong>Paolo</strong> reviews her diary at a routine visit. Each exchange shows positive net ultrafiltration (drain '
                  'greater than fill), totaling about 600 mL a day, much as it did three months ago. But her morning weight has climbed '
                  '2.4 kg over five weeks, her ankles pit to mid-shin, and her urine diary has gone from about 700 mL to about 250 mL a '
                  'day.</p>',
          'questions': ['Is a positive ultrafiltration total enough to call her volume status stable?',
                        'What four questions would you ask before you call?',
                        'What belongs to you, and what belongs to the nephrologist?']},
 'sections': [('the-physiology',
               'The physiology',
               'The physiology',
               '\n'
               '<p><strong>The membrane is not a single sheet.</strong> The peritoneum is a large, folded serous membrane lining the '
               'abdominal wall and the bowel. What actually limits transport is the wall of the peritoneal capillaries, which behaves as '
               'if it has pores of three sizes. Large numbers of small pores let water and small solutes pass. A few large pores let '
               'proteins leak out, which is why PD patients lose albumin into the effluent every day. Water-only channels (aquaporin-1) in '
               'the capillary endothelium let water cross without sodium. This is established physiology.[[pd_morelle2021]]</p>\n'
               '{{fig:pd01_pores}}\n'
               '\n'
               '<p><strong>Diffusion runs down a gradient that dissipates.</strong> At the start of a dwell the urea concentration in '
               'dialysate is near zero, so the gradient is steep. Within a few hours the dialysate approaches the plasma value and '
               'transport slows. Larger molecules diffuse more slowly and keep gaining for longer. This is why the prescriber chooses '
               'dwell length and number of exchanges deliberately.</p>\n'
               '<p><strong>Osmotic ultrafiltration also fades.</strong> Glucose draws water, but glucose itself is absorbed across the '
               'membrane into the blood. The osmotic gradient therefore falls during the dwell. Early in a glucose dwell, about half the '
               'water moves through the aquaporins, leaving sodium behind. This produces the "sodium sieving" seen at one hour of a '
               'hypertonic dwell. As the gradient fades, net water removal slows and eventually reverses: fluid reabsorption continues '
               'while osmotic pull has disappeared. A long glucose dwell can end with less fluid out than went in. Icodextrin is a large '
               'glucose polymer that is absorbed slowly, so it keeps pulling water through the small pores over a long dwell. That is why '
               'it is often prescribed for the long night dwell in CAPD or the long day dwell in APD.[[pd_morelle2021]]</p>\n'
               '<p><strong>Water removal and clearance can diverge.</strong> A patient can have good urea removal and poor fluid removal, '
               'or the reverse. Fast transporters equilibrate small solutes quickly (good clearance in short dwells) but also absorb '
               'glucose quickly and lose their osmotic gradient early (poor ultrafiltration in long dwells). Slow transporters keep their '
               'glucose gradient longer but clear small solutes more slowly. You will meet the formal measurement of this, the peritoneal '
               'equilibration test, in PD06.</p>\n'
               '<p><strong>Residual kidney function carries more weight in PD than most nurses expect.</strong> Many people start PD still '
               'passing several hundred milliliters of urine a day. That urine removes sodium, water and middle molecules continuously, '
               'and in observational studies its preservation is associated with better survival in PD. When urine output falls, the '
               'patient loses a fluid-removal route that the PD prescription was never designed to replace. The same drain volumes that '
               'kept them euvolemic last quarter may no longer be enough. <strong>Whenever you read a PD record, ask what the kidneys are '
               'still contributing.</strong>[[pd_brown2020]]</p>\n'
               '<h3>What this means at the bedside</h3>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Process</th><th>What normally happens</th><th>What weakens it</th><th>What you may '
               'notice</th></tr></thead>\n'
               '<tbody><tr><td>Diffusion of small solutes</td><td>Gradient steep early, flattens over hours</td><td>Missed exchanges, '
               'short total therapy time, membrane change, low drain volume</td><td>Fatigue, poor appetite, nausea, itch; laboratory '
               'trends the team reviews</td></tr><tr><td>Osmotic ultrafiltration</td><td>Strong early, fades as glucose is '
               'absorbed</td><td>Long glucose dwell, fast transport, peritonitis, wrong solution strength</td><td>Falling drain volumes, '
               'rising weight, edema, dyspnea</td></tr><tr><td>Fluid reabsorption</td><td>Continuous through lymphatics and '
               'tissue</td><td>Increases in some patients; makes long dwells net-positive</td><td>Drain less than fill after a long '
               'dwell</td></tr><tr><td>Residual urine</td><td>Removes sodium and water daily</td><td>Nephrotoxins, hypotension, infection, '
               'time</td><td>Falling urine volume in the diary, new edema despite unchanged PD</td></tr></tbody></table></div>\n'),
              ('capd-and-apd',
               'CAPD and APD',
               'CAPD and APD',
               '\n'
               '<p>Continuous ambulatory PD (CAPD) uses manual exchanges, usually three to five times a day, with dialysate in the abdomen '
               'almost continuously. Each exchange is drain, then fill, then dwell. The patient is free between exchanges but must stop '
               'for each one. Failure modes are human: rushed technique, missed exchanges, touch contamination, mislabeled solution '
               'strength.</p>\n'
               '{{fig:pd01_day}}\n'
               '\n'
               '<p>Automated PD (APD) uses a cycler, usually overnight, to perform several short exchanges while the patient sleeps. Many '
               'prescriptions add a long day dwell ("last fill") or a midday exchange. Daytime is free, which suits work and school. '
               'Failure modes add the machine: programming mismatches with the order, drain alarms that interrupt sleep, power '
               'interruption, and a long day dwell that may absorb fluid back if the wrong solution is used.</p>\n'
               '<p>Neither modality is "better" for every person. Choice depends on the person&rsquo;s life, home, transport, electricity, '
               'storage and their membrane characteristics. The prescriber selects the regimen; you make sure the person can carry it out '
               'safely and that what is delivered matches what is ordered.</p>\n'
               '{{key:Both modalities share three requirements: a working catheter, consistent aseptic technique, and a reliable plan for '
               'when something goes wrong.}}\n'),
              ('what-the-pd',
               'What the PD',
               'What the PD nurse does, and where the line sits',
               '\n'
               '<p>Under the Philippine Nursing Act (Republic Act 9173), nursing practice includes assessment, health teaching, '
               'collaboration with the team, and carrying out written orders. In PD that becomes a clear division:[[pd_ra9173]]</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>You do</th><th>You route to the prescriber</th></tr></thead>\n'
               '<tbody><tr><td>Verify patient, modality, solution, strength and volumes against the written order</td><td>Any change in '
               'solution strength, dwell, cycler program, icodextrin use</td></tr><tr><td>Compare what was actually delivered with what '
               'was ordered</td><td>Any medication start, stop or dose change, including antibiotics</td></tr><tr><td>Assess volume '
               'status, symptoms, exit site and effluent</td><td>Interpretation of PET and adequacy results for prescription '
               'change</td></tr><tr><td>Teach, observe return demonstration, judge readiness under program criteria</td><td>Modality '
               'change, catheter procedures, admission decisions</td></tr><tr><td>Triage calls, activate the PD pathway, document '
               'closed-loop handoff</td><td>Diagnosis of peritonitis and treatment choice</td></tr></tbody></table></div>\n'
               '<p>The line is not about importance. Your observations are often the first warning the team gets. <strong>Report a pattern '
               'with numbers, times and what has already been checked; leave the decision on the prescription with the '
               'prescriber.</strong></p>\n'),
              ('red-flags-in',
               'Red flags in this module',
               'Red flags in this module',
               '\n'
               '{{stop:<ul><li>Positive ultrafiltration on paper, yet weight rising and urine falling: the total fluid picture is '
               'worsening.</li><li>New breathlessness at rest, orthopnea or chest pain: emergency pathway, not routine review.</li><li>Any '
               'cloudy effluent, even with no pain: same-day PD team contact (PD07).</li></ul>}}\n')],
 'debrief': ['<p>Paolo does not stop at "UF is positive." He asks four questions. Is she breathless lying flat? (Mildly, two pillows now '
             'instead of one.) Are all four exchanges being done? (Yes, she has not missed any.) Has her fluid and salt intake changed? '
             '(She admits more <em>sabaw</em> since the rains started.) Are drain volumes measured the same way? (Same bathroom scale, '
             'same method.)</p>\n'
             '<p><strong>What the pattern means.</strong> The PD prescription has not changed, but one of her fluid-removal routes, her '
             'own kidneys, has. Positive exchange UF alone told an incomplete story. Paolo records weight, blood pressure, edema, urine '
             'trend and diary totals, screens for emergency features (none at rest), and calls the nephrologist the same day with the full '
             'pattern. The decision about solution strength, icodextrin or diuretics belongs to the nephrologist. The teaching about salt '
             'and fluid is his.</p>'],
 'skills': {'title': 'Practice drill',
            'intro': 'Using a simple drawing, explain fill, dwell and drain to a peer acting as a new patient. Include why the long dwell '
                     'may return less fluid than it received.Sort ten statements supplied by your preceptor into "nursing observation to '
                     'record and report" and "change that requires a new order."',
            'items': [('Using a simple drawing, explain fill, dwell and drain to a peer acting as a new patient. Include why the long '
                       'dwell may return less fluid than it received.',
                       False),
                      ('Sort ten statements supplied by your preceptor into "nursing observation to record and report" and "change that '
                       'requires a new order."',
                       False)]},
 'quiz': [('Which process moves urea from blood into dialysate during a dwell?',
           ['Diffusion down a concentration gradient',
            'Osmotic ultrafiltration through aquaporins',
            'Lymphatic absorption',
            'Active tubular secretion'],
           0,
           'Urea moves by diffusion from high plasma concentration to low dialysate concentration. B moves water, not urea in a meaningful '
           'amount by itself. C returns fluid to the body. D is a kidney tubule process, not peritoneal.'),
          ('Why does net ultrafiltration slow and may reverse late in a long glucose dwell?',
           ['The catheter becomes obstructed',
            'Urea concentration rises in the blood',
            'Glucose is absorbed, the osmotic gradient fades, and fluid reabsorption continues',
            'The patient&rsquo;s urine output increases'],
           2,
           'Glucose crosses into the blood, so the osmotic pull fades while reabsorption continues. A causes poor drain, not reversal of '
           'UF. B does not drive water removal. D is unrelated to dwell physiology.'),
          ('Why is icodextrin often used for the long dwell?',
           ['It clears potassium faster than glucose',
            'It prevents peritonitis',
            'It replaces residual kidney function',
            'It is absorbed slowly and sustains osmotic water removal over many hours'],
           3,
           'Icodextrin&rsquo;s large molecules are absorbed slowly and keep drawing water through small pores. A is not its purpose. B and '
           'C are false claims.'),
          ('A patient&rsquo;s exchanges show positive net ultrafiltration, but weight is rising and urine output has fallen. What is the '
           'best interpretation?',
           ['Volume status is fine because UF is positive',
            'Total fluid removal may have fallen; assess the whole balance and report the trend',
            'The scale is broken',
            'The patient should skip an exchange to rest the membrane'],
           1,
           'Falling residual urine removes a fluid route; total balance matters. A ignores urine and weight. C is possible but not the '
           'first conclusion without checking. D is unsafe and not a nursing decision.'),
          ('Which statement about CAPD and APD is correct?',
           ['APD has no day dwell in any prescription',
            'APD adds programming and machine-related failure modes to the human ones',
            'CAPD uses a cycler overnight',
            'CAPD is always better for working adults'],
           1,
           'APD introduces program mismatch, alarms and power dependence. A is false because many APD prescriptions include a day dwell. C '
           'describes APD. D ignores individual choice.'),
          ('What does sodium sieving early in a hypertonic glucose dwell reflect?',
           ['Protein leak through large pores',
            'Potassium secretion into dialysate',
            'Contamination of the bag',
            'Water crossing aquaporins without sodium'],
           3,
           'Aquaporin water transport leaves sodium behind, lowering dialysate sodium transiently. A, B and C are unrelated.'),
          ('Why do PD patients lose albumin into effluent daily?',
           ['Through large pores in peritoneal capillaries',
            'Because glucose binds albumin',
            'Because of tubular damage',
            'Only during peritonitis'],
           0,
           'A small number of large pores allows protein loss. Losses rise during peritonitis but occur daily, so D is incomplete. B and C '
           'are incorrect mechanisms.'),
          ('A fast transporter typically has which pattern?',
           ['Slow solute clearance and excellent UF in long dwells',
            'No difference from slow transporters',
            'Rapid small-solute equilibration and early loss of the glucose gradient in long dwells',
            'No glucose absorption'],
           2,
           'Fast transport clears small solutes quickly but dissipates the glucose gradient early. A describes slow transport. B and D are '
           'false.'),
          ('Which action is within the PD nurse&rsquo;s role without a new order?',
           ['Changing the solution from 1.5% to 2.5% dextrose',
            'Starting intraperitoneal antibiotics on suspicion',
            'Comparing delivered therapy with the written order and reporting discrepancies',
            'Adding icodextrin for the night dwell'],
           2,
           'Verification and reporting are core nursing work. A, B and D are prescription changes that require an order (B may be under a '
           'written standing protocol, but not on the nurse&rsquo;s own decision).'),
          ('Why does loss of residual urine matter more in PD planning than many expect?',
           ['Urine contributes sodium and water removal that PD alone may not replace',
            'Urine has no role once dialysis starts',
            'Urine output determines catheter position',
            'Urine prevents peritonitis'],
           0,
           'Residual urine removes sodium, water and solutes continuously. B is false. C and D are unrelated.'),
          ('Which finding in this module requires an emergency pathway rather than routine review?',
           ['Mild ankle edema', 'New breathlessness at rest', 'Slightly lower drain volume on one day', 'A question about diet'],
           1,
           'Breathlessness at rest signals possible acute fluid overload or cardiac event. A and C warrant assessment and trend review. D '
           'is routine teaching.'),
          ('How should you report a worsening volume pattern?',
           ['"She seems puffy."',
            'Only the last exchange volume',
            'Wait until the next clinic visit',
            'Weight trend, blood pressure, edema, urine and UF totals, intake change, and what was checked'],
           3,
           'A complete, numerical pattern lets the prescriber decide. A is vague. B is incomplete. C delays care.'),
          ('Which best describes the relationship between water removal and small-solute clearance?',
           ['They always rise and fall together',
            'Clearance determines UF exactly',
            'Water removal has no effect on clearance',
            'They are related but can diverge'],
           3,
           'They share the membrane and drain volume but can move independently. A and B overstate the link. C is false because drained '
           'volume contributes to clearance.'),
          ('In observational studies, preserved residual kidney function in PD is:',
           ['Proven by randomized trials to double survival', 'Associated with better survival', 'Unrelated to outcomes', 'Harmful'],
           1,
           'The evidence is observational; association, not proven causation. A overstates. C and D contradict the data.'),
          ('A patient asks why they cannot simply leave the night dwell in longer "for more cleaning." The best answer explains that:',
           ['Longer dwells always clean better',
            'The catheter will block',
            'Small-solute transport slows as the gradient flattens and fluid may be absorbed back, so the prescriber sets the dwell length',
            'Longer dwells cause peritonitis'],
           2,
           'Transport plateaus and long glucose dwells can become net-positive. A is false. B and D are not the reason.')],
 'terms': [('Peritoneal dialysis (PD)',
            'Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter.'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis: manual exchanges through the day.'),
           ('APD', 'Automated peritoneal dialysis: a cycler performs exchanges, usually overnight.'),
           ('Dwell', 'The time dialysis solution stays in the abdomen between fill and drain.'),
           ('Ultrafiltration (UF)', 'Fluid removed by dialysis; net UF is drained volume minus instilled volume.'),
           ('Icodextrin', 'A large glucose polymer solution absorbed slowly, used for long dwells.'),
           ('Residual kidney function', "The filtering and urine output the patient's own kidneys still provide."),
           ('Aquaporin', 'A water-only channel in capillary walls that lets water cross without sodium.'),
           ('Sodium sieving', 'The early fall in dialysate sodium when water crosses aquaporins without sodium.'),
           ('Exit site', 'The point where the PD catheter leaves the skin.'),
           ('Cycler', 'The machine that performs APD exchanges.'),
           ('Last fill', 'The final APD fill that stays in during the day, also called the day dwell.'),
           ('Peritoneal equilibration test (PET)',
            'A standardized 4-hour dwell that measures how fast solutes cross the membrane and how much water is removed.'),
           ('Peritonitis', 'Infection or inflammation of the peritoneum, usually shown by cloudy effluent.'),
           ('Effluent', 'Fluid drained from the abdomen after a dwell.'),
           ('Return demonstration', 'The learner performs the skill while the trainer observes.')],
 'readings': [('peritoneal-dialysis-ckd.html', 'The patient-facing guide to PD that your patients may read.'),
              ('dialysis-adequacy.html', 'How dialysis dose is measured and why it is only part of the picture.')],
 'calcs': ['calc-pd-adequacy.html']}
