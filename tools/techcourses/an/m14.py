# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 14: The hemodialysis prescription and adequacy.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. KDOQI 2015 grade checked against the guideline statement; HEMO, CONVINCE and the ultrafiltration-rate review
against PubMed abstracts; H4RT status against the ISRCTN registry and trial website."""

MODULE = {'image_alt': 'Close-up of a hollow-fiber dialyzer cartridge standing upright.',
 'objectives': ['Write a complete hemodialysis (HD) order within unit capability.',
                'Investigate discordance between prescribed and delivered dialysis.',
                'Interpret Kt/V, ultrafiltration rate and hemodiafiltration evidence correctly.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the Philippine '
        'Society of Nephrology (PSN) guidelines, you provide the initial and maintenance dialysis prescription (b4) and review it at least '
        'monthly, face to face or by telemedicine if necessary (b6).[[an14_1]]</div>\n'
        '{{plain:Think of a car wash on a timer. You pay for ten minutes of spray. If the attendant turns the pressure down, or the car '
        'leaves at minute seven, the car comes out dirtier, although the receipt still says ten minutes.}}\n'
        '<p>The picture has a limit. Kt/V counts how many times body water was cleared of urea in one session. It is a surrogate: it says '
        'nothing about fluid, middle molecules or how the patient feels.</p>\n'
        '{{cards:Key numbers|Single-pool Kt/V, thrice-weekly HD (KDOQI 2015)::Target 1.4; minimum delivered 1.2 (1B)|High-dose '
        'hemodiafiltration (CONVINCE)::Deaths 17.3% vs 21.9% with high-flux hemodialysis over a median 30 months|PhilHealth hemodialysis '
        'benefit::Up to 156 sessions a year, enough for three a week}}\n'
        '<p>You are rarely at the chair when the dose is lost; you see it on your monthly visit. Your work is to write an order the unit '
        'can deliver, and to find out why when it is not.</p>\n',
 'case': {'title': 'The Kt/V that fell',
          'html': '<p>On your monthly visit, the head nurse shows you the results of Mrs. Panganiban, one of your patients. Her '
                  'single-pool Kt/V has fallen from 1.45 to 1.05 over two months. Her prescription has not changed. The nurses&rsquo; '
                  'notes show she cramps most sessions and has gone home 30 to 45 minutes early four times this month.</p>\n'
                  '<p>The night-shift notes say &ldquo;arterial pressure alarm, blood flow reduced to 250&rdquo; several times a week. The '
                  'physician on duty proposes a larger dialyzer. The administrator stops by and asks why her numbers are pulling the '
                  'unit&rsquo;s adequacy figures down just before the PhilHealth quality review.</p>\n',
          'questions': ['Did her dose fall, or did her delivery fall?',
                        'What are the four checks before anyone changes the prescription?',
                        'What will you tell the administrator?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Urea clearance (K) depends on blood flow, dialysate flow and dialyzer surface area. Time (t) multiplies it. The urea '
               'distribution volume (V), close to total body water, sets how much clearing is needed. After the session, urea moves back '
               'from the cells into the blood, so equilibrated Kt/V is lower than single-pool Kt/V.</p>\n'
               '<p>Delivery fails in predictable ways. If the arterial needle cannot draw the set flow, the pump runs slower or the nurse '
               'turns it down. If the access recirculates, cleaned blood goes straight back into the arterial needle. If the session ends '
               'early, t shrinks. Each one lowers Kt/V with no change on the order sheet.</p>\n'
               '<p>Fluid follows another rule. When removal outpaces refill from the tissues, blood volume falls, and cramps, hypotension '
               'and repeated stunning of heart and brain follow.</p>\n'
               '{{key:Kt/V falls when time, flow or the access fails. Look at the machine and the access before you change the order.}}\n'
               '<div class="tc-scene"><span class="tc-lab">On your monthly visit, the alarm that was silenced &middot; '
               'fictional</span><p>You stay to watch Mrs. Panganiban&rsquo;s session. Every few minutes the arterial pressure alarm '
               'sounds, and the nurse turns the blood pump down from 350 to 250 mL/min. The screen still shows the prescribed four '
               'hours.</p><p>At 250 mL/min for three and a half hours, she receives far less clearance than the order assumes. Nothing on '
               'the prescription sheet has changed.</p><p class="tc-scene-take"><b>What this shows.</b> A dose that is not delivered is '
               'not a dose.</p></div>\n'
               '\n'
               '{{fig:an14_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Small-solute dose.</strong> The Kidney Disease Outcomes Quality Initiative (KDOQI) 2015 recommends a target '
               'single-pool Kt/V of 1.4 per session for patients treated three times a week, with a minimum delivered value of 1.2 '
               '(1B).[[an14_3]] More is not better. The HEMO trial randomized 1,846 thrice-weekly patients to single-pool Kt/V about 1.71 '
               'or 1.32. Death did not differ (relative risk 0.96, 95% confidence interval 0.84 to 1.10).[[an14_7]] UK guidance recommends '
               'at least 12 hours a week for most thrice-weekly patients with little residual function.[[an14_4]] A patient dialyzing '
               'twice a week receives less weekly clearance at the same per-session Kt/V.</p>\n'
               '<p><strong>Fluid.</strong> Observational studies associate higher ultrafiltration rates with higher mortality. Large '
               'weight gains may confound the link, so it does not prove that capping the rate saves lives.[[an14_8]]</p>\n'
               '<p><strong>Hemodiafiltration (HDF).</strong> CONVINCE randomized 1,360 European patients who could achieve a convection '
               'volume of at least 23 liters to high-dose HDF or high-flux hemodialysis. Over a median 30 months, 17.3% died with HDF and '
               '21.9% with hemodialysis (hazard ratio 0.77, 95% confidence interval 0.65 to 0.93), an absolute difference of 4.6 '
               'percentage points.[[an14_5]] It is one trial, in patients selected for high convection volumes. The UK H4RT trial finished '
               'follow-up in May 2025; its results had not been published when this module was reviewed.[[an14_6]] The 2019 UK guideline, '
               'written before CONVINCE, judged HDF as good as but not better than hemodialysis.[[an14_4]]</p>\n'
               '<p>PhilHealth covers up to 156 sessions a year[[an14_9]] and has issued quality standards for maintenance '
               'hemodialysis.[[an14_2]]</p>\n'
               '{{key:Kt/V is a floor, not a goal. Above it, fluid, time and the access matter more.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Write the whole order.</strong> Schedule and duration, access and needle size, blood and dialysate flow, '
               'dialyzer, dialysate sodium, potassium, calcium and bicarbonate, anticoagulation, target weight with a maximum '
               'ultrafiltration rate, and monitoring. Write it so the physician on duty can follow it at night.</p>\n'
               '<p><strong>When Kt/V falls, check four things first.</strong> Time actually delivered (late starts, early stops). Sampling '
               'technique and timing of the post-dialysis sample. Achieved blood flow and arterial pressures. Access recirculation or '
               'stenosis. Only then change the dose.</p>\n'
               '<p><strong>Fit it to the patient&rsquo;s week.</strong> Cap the ultrafiltration rate. When weight gains are high, lengthen '
               'or add sessions rather than pulling fluid harder. If a patient dialyzes twice a week because of transport or cost, ask '
               'what would make a third session possible and document the reason.</p>\n'
               '\n'
               '{{fig:an14_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the quality meeting &middot; fictional</span><p>Nurse Cabral shows you the '
               'adequacy of your patients at the unit: 82% at or above a single-pool Kt/V of 1.2. You ask a second question: how many '
               'sessions ended early because of cramps or low pressure? The answer is 14% last month.</p><p>You agree to review two '
               'measures for your patients each month: Kt/V and minutes lost per session.</p><p class="tc-scene-take"><b>What this '
               'shows.</b> Measure what was delivered, not only what was ordered.</p></div>\n'
               '{{key:Review delivered minutes and the access with every Kt/V.}}\n'
               '{{call:<ul><li>Kt/V falling with repeated arterial pressure alarms (access dysfunction)</li><li>Interdialytic weight gain '
               'consistently &gt;4% of body weight</li><li>Repeated sessions shortened by cramps or hypotension</li><li>Pre-dialysis '
               'potassium &gt;6.0 mmol/L</li></ul>}}\n')],
 'debrief': ['<p><strong>Dose or delivery?</strong> Delivery. The order did not change, but she is getting less of it: shorter sessions '
             'and a slower blood pump. A larger dialyzer will not fix a pump that cannot draw blood.</p>\n'
             '<p><strong>The four checks.</strong> Count the minutes actually delivered. Confirm the post-dialysis sample was drawn at the '
             'right time with the right technique. Read the arterial pressures: alarms with the pump turned down point to an inflow '
             'stenosis or a needle problem. Refer the access for examination, flow measurement and imaging, and coordinate with the access '
             'surgeon. Then reassess her target weight and cap the ultrafiltration rate; the cramps mean fluid is pulled too fast.</p>\n'
             '<p><strong>The administrator.</strong> Tell him the truth: the number fell because the access and the fluid plan need '
             'attention, and both are fixable. Show him the plan and the date of the next correctly timed sample. A quality number is '
             'worth something only if it describes the patient. Adjusting the sampling to pass the review would hide a failing fistula '
             'until it clots.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Reviews a complete order for safety and feasibility', False),
                      ('Identifies a delivery discrepancy and its cause', False),
                      ('Sets a repeat measurement plan', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What is a sound first step in falling adequacy with frequent alarms?',
           ['Increase clearance targets without investigation',
            'Check delivered time, sampling and access function',
            'Ignore shortened sessions',
            'Switch dialyzer brand'],
           1,
           'Confirm why delivery fell before changing the prescription.'),
          ('What should a target-weight revision consider?',
           ['Symptoms, examination, blood pressure trend and treatment tolerance',
            'The lowest weight ever achieved',
            'A single predialysis weight without context',
            'The family&rsquo;s preferred weight'],
           0,
           'Volume goals balance congestion against the harms of fluid removed too fast.'),
          ('What is the KDOQI 2015 minimum delivered spKt/V for thrice-weekly HD?',
           ['2.0', '0.9', '1.7', '1.2'],
           3,
           'KDOQI 2015 recommends a target of 1.4 and a minimum delivered value of 1.2 (1B).'),
          ('Why is equilibrated Kt/V lower than single-pool Kt/V?',
           ['Blood samples are diluted',
            'The dialyzer loses efficiency over time',
            'Urea rebounds from tissues into blood after dialysis ends',
            'Urea is produced faster during dialysis'],
           2,
           'Delayed transfer from the cells raises post-dialysis urea.'),
          ('Which statement about hemodiafiltration evidence is accurate?',
           ['HDF has been proven harmful',
            'CONVINCE showed lower mortality with high-dose HDF; confirmation from H4RT is pending',
            'All trials show no effect',
            'HDF benefit requires low convection volumes'],
           1,
           'One large trial, in patients able to reach at least 23 liters of convection, showed 17.3% vs 21.9% mortality.')],
 'terms': [('KDOQI', 'Kidney Disease Outcomes Quality Initiative'),
           ('eKt/V', 'Equilibrated Kt/V'),
           ('spKt/V', 'Single-pool Kt/V'),
           ('HDF', 'Hemodiafiltration'),
           ('HD', 'Hemodialysis'),
           ('HEMO', 'Hemodialysis (HEMO) Study'),
           ('CONVINCE', 'Comparison of high-dose HDF with high-flux HD trial'),
           ('H4RT', 'High-volume Haemodiafiltration vs High-flux Haemodialysis Registry Trial'),
           ('PSN', 'Philippine Society of Nephrology')],
 'readings': [('dialysis-adequacy.html', 'Dialysis Adequacy'),
              ('hemodiafiltration-new-standard.html', 'Is Hemodiafiltration the New Standard? High-Volume HDF vs High-Flux Hemodialysis')],
 'calcs': ['calc-dialysis-adequacy-ktv.html',
           'calc-dialysis-kinetics.html',
           'calc-hd-adequacy-npcr.html',
           'calc-ultrafiltration-rate.html',
           'calc-ufr-ceiling.html',
           'calc-idwg-fluid.html',
           'calc-dialysis-prescription.html',
           'calc-hd-session-review.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
