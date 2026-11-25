# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 21: PhilHealth documentation and ethical claims.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. PhilHealth figures checked against philhealth.gov.ph (PC 2023-0009, PC 2024-0023, PA 2024-0036, 2024 and
2025 news releases); PSN duties against the 2024 PSN hemodialysis guidelines."""

MODULE = {'image_alt': 'A clipboard with a treatment flowsheet, a claim form and a calendar on a desk, with a pen ready to sign.',
 'objectives': ['Reconcile delivered services with records before attesting.',
                'Resolve mismatches through a traceable correction workflow.',
                'Protect patient privacy and declare financial conflicts.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you provide a complete clinical abstract with the prescription and current '
        'medicines when needed (b5); you meet the documentary requirements of the Philippine Health Insurance Corporation (PhilHealth), '
        'the Philippine Charity Sweepstakes Office (PCSO), the Department of Social Welfare and Development (DSWD), and other payers '
        '(b11); and you accept no gift or rebate from the unit (b14).[[an01_1]]</div>\n'
        '{{plain:Think of a claim as a receipt you sign for someone else&rsquo;s purchase. You did not stand at the counter, but your name '
        'says the goods changed hands, on that date, in that amount.}}\n'
        '<p>The picture has a limit. A receipt records one sale. A dialysis claim lists a month of sessions for one patient, built by '
        'billing staff from records you did not write, at a unit you visit perhaps once a month. Each date is a separate statement. One '
        'wrong date makes the whole claim inaccurate, however honest everyone meant to be.</p>\n'
        '{{cards:Key numbers|Hemodialysis (HD) sessions covered per year::Up to 156, three a week for 52 weeks (PhilHealth Circular '
        '2023-0009)|HD package rate::PHP 6,350 per session, up to PHP 990,600 a year, from October 2024 (Circular 2024-0023). Confirm on the '
        'date of service.}}\n'
        '<p>In Philippine practice you sign the PhilHealth claims for every one of your patients, often at several units, usually as a '
        'stack on your monthly visit. Your work in this module is to sign only what has been checked against the treatment record, to '
        'correct errors in a way an auditor can follow, and to write abstracts that certify one patient&rsquo;s facts.</p>\n',
 'case': {'title': 'The claim you are asked to sign on Friday',
          'html': '<p>It is your monthly visit, on the last Friday of the month. You have twelve patients at this unit and nine more at '
                  'two others. The billing clerk hands you a stack of Philippine Health Insurance Corporation (PhilHealth) claim forms for '
                  'all twelve, to sign before the 5 p.m. courier. &ldquo;They are all correct, Doc. Just sign on the flags.&rdquo; You '
                  'pull one at random: Mr. Lopez, 12 sessions.</p>\n'
                  '<p>You compare it with the treatment flowsheets. On the 9th, his session was cancelled because the water system was '
                  'down, but the date is on the claim. The 16th appears twice. The clerk explains that the system bills from the schedule, '
                  'and that the server crashed on the 16th and the entries were typed again. &ldquo;It is only two sessions, Doc, and '
                  'we have done it this way for years.&rdquo;</p>\n',
          'questions': ['Do you sign the stack?',
                        'How is the claim corrected, and by whom?',
                        'What is the real problem, and how will you fix it?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>A claim is the last step of a pipeline. Upstream sits the treatment record: the machine log, the nursing flowsheet, the '
               'physician note. Midstream sit the dialysis log and the statement of account. The claim is the outlet. Each step copies from '
               'the one before it.</p>\n'
               '<p>Errors enter at predictable points. A session is scheduled but cancelled, and the system bills the schedule. A patient '
               'transfers mid-month. Entries are typed again after a server crash and appear twice. Someone edits a record without an audit '
               'trail. In Philippine units, water and power interruptions after storms add cancelled sessions that a schedule-based system '
               'will still bill. Reconciliation means checking the outlet against the source, one date at a time.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Where the error enters</th><th>Why it happens</th><th>What you see on the claim</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Schedule copied into billing</td><td>The system bills planned sessions, not delivered ones</td><td>A date with '
               'no flowsheet or machine log</td></tr>\n'
               '<tr><td>Re-entry after downtime</td><td>Entries typed again without a duplicate check</td><td>The same date twice</td></tr>\n'
               '<tr><td>Mid-month transfer or admission</td><td>The sending and receiving records do not meet</td><td>Sessions billed '
               'while the patient was admitted elsewhere</td></tr>\n'
               '<tr><td>Untracked edit</td><td>Records changed with no audit trail</td><td>A claim that matches a log you cannot trust</td>'
               '</tr>\n'
               '</tbody></table></div>\n'
               '<div class="tc-scene"><span class="tc-lab">Tracing one date &middot; fictional</span><p>You pick one date from Mr. '
               'Lopez&rsquo;s claim, the 9th, and follow it upstream. The claim says a session happened. The statement of account says the '
               'same. The dialysis log says &ldquo;cancelled, water system down.&rdquo; There is no machine log and no nursing '
               'flowsheet.</p><p>The error entered at the first step, where the system copied the schedule into the billing file.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> Reconciliation means checking the outlet against the source, one date at a '
               'time.</p></div>\n'
               '{{key:The treatment record is the source. The claim follows it, never the other way around.}}\n'
               '\n'
               '{{fig:an21_b}}\n'),
              ('evidence',
               'Evidence',
               'What the rules say',
               '<p>This module rests on regulation, not trials. Read each rule as current only on the date you check it.</p>\n'
               '<p><strong>Sessions.</strong> PhilHealth Circular 2023-0009 expanded the hemodialysis (HD) benefit from 90 to 156 sessions '
               'a year, matching three sessions a week for 52 weeks, for members and dependents with chronic kidney disease (CKD) stage '
               '5.[[an21_2]] Patients must be registered in the PhilHealth Dialysis Database (PDD).[[an21_3]]</p>\n'
               '<p><strong>Rate and inclusions.</strong> Circular 2024-0023 (Revision 2) raised the package to PHP 6,350 per session, up to '
               'PHP 990,600 a year.[[an21_1]] PhilHealth states that the package includes anticoagulation and anemia medicines, laboratory '
               'tests, dialyzers, HD solutions and a dialysis kit per session.[[an21_10]] Its own releases give the effective date as '
               'October 9, 2024; some news reports said October 7.[[an21_3]] Earlier, PhilHealth clarified that it covers only the services '
               'listed in the minimum standards of the benefit, and that those services fall under the policy&rsquo;s no co-payment '
               'provision.[[an21_11]] Patients still pay for whatever lies outside the package, which is why many also carry guarantee '
               'letters from PCSO, DSWD or their local government unit (LGU).</p>\n'
               '<p><strong>Quality and other benefits.</strong> Circular 2024-0029 sets quality standards for maintenance HD as a reference '
               'for the corporation.[[an21_4]] Peritoneal dialysis has its own Z Benefits package.[[an21_6]] Forms and annexes change; '
               'download them from PhilHealth, not from last year&rsquo;s folder.[[an21_5]] Check the circulars index before you rely on '
               'any figure.[[an21_7]]</p>\n'
               '<p><strong>Professional rules.</strong> The PSN 2024 guidelines ask you to meet each payer&rsquo;s documentary '
               'requirements, make the unit&rsquo;s operations manager responsible for forms being filled out properly and truthfully, and '
               'forbid any rebate or gift from the unit to the physician.[[an21_8]] The Data Privacy Act of 2012 governs how claim data '
               'are shared.[[an21_9]]</p>\n'
               '{{key:Quote PhilHealth figures with the circular number and the date you checked it. Rates and forms change faster than '
               'training material.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Before you sign.</strong> Ask the unit to show you its reconciliation: each claimed date matched to a flowsheet '
               'or machine log, then to the dialysis log, the statement of account and the claim. If the unit has none, sample. Pull two '
               'or three claims at random each visit and trace every date yourself. Confirm the patient&rsquo;s PDD registration, the '
               'facility&rsquo;s accreditation and your own, and the package-specific forms.</p>\n'
               '<p><strong>When a date does not match.</strong> Hold that claim. Notify authorized billing staff. Correct it through the '
               'approved workflow, with an audit trail that shows who changed what, when and why. Never overwrite a source record to match '
               'a claim.</p>\n'
               '<p><strong>Privacy and conflicts.</strong> Send claim data only through approved, privacy-compliant channels, not through '
               'group chats.[[an21_9]] Declare any financial relationship with suppliers or with the facility. You do not own most of the '
               'units where you sign, so put your concerns in writing to the operations manager and the clinical head.</p>\n'
               '\n'
               '{{fig:an21_a}}\n'
               '<div class="tc-scene"><span class="tc-lab">The correction, done properly &middot; fictional</span><p>The billing clerk '
               'deletes the two wrong dates and prints a new claim. You ask her to undo it and use the correction workflow instead, so the '
               'record shows the original entry, the change, who made it, and why.</p><p>A month later, a PhilHealth auditor asks about '
               'that claim. The audit trail answers the question in two minutes.</p><p class="tc-scene-take"><b>What this shows.</b> A '
               'correction without a trail looks the same as an alteration.</p></div>\n'
               '{{key:Sample a few claims at every visit. A sample you trace yourself is worth more than a stack someone tells you is '
               'correct.}}\n'
               '{{call:<ul><li>Claimed date with no treatment record</li><li>Duplicate dates after system downtime</li><li>Requests to '
               '&ldquo;adjust&rdquo; logs to match a claim</li><li>Rebate or incentive offers tied to referrals or supplies</li></ul>}}\n'),
              ('abstract',
               'Abstracts and claims',
               'The abstract and the claims you sign',
               '\n'
               '<p>You rarely sit at the dialysis center&rsquo;s billing desk, but your name is on its paperwork. Two documents carry it '
               'most often.</p>\n'
               '<p><strong>The clinical abstract.</strong> When a patient needs one, you provide a complete abstract with the dialysis '
               'prescription and current medicines, and the unit keeps a duplicate abstract and a medical certificate on '
               'file.[[an21_8]] Patients ask for abstracts for PDD registration, for travel or transfer, for PCSO, DSWD and LGU '
               'assistance, and for work or disability papers. An abstract is a summary you certify, so write it from the record and date '
               'it. Most payers and receiving units also look for the diagnosis and its cause, the date dialysis started, the access, and '
               'recent serologies; ask the requesting office what it needs.</p>\n'
               '<p><strong>The claims you sign.</strong> The PSN text does not name the signatory of the claim. It asks you to meet the '
               'payers&rsquo; documentary requirements and makes the operations manager responsible for truthful forms.[[an21_8]] Your '
               'signature still states that each listed session happened. Sign what you have checked against the treatment record, or what '
               'the unit&rsquo;s reconciliation has checked and shown you, and nothing else.</p>\n'
               '<p><strong>No rebates.</strong> The guidelines are explicit: no physician accepts any gift or monetary consideration from '
               'the dialysis center in the form of rebate fees or the like. Your professional fee is the one set in the current PSN '
               'guidelines.[[an21_8]]</p>\n'
               '<div class="tc-scene"><span class="tc-lab">In your clinic &middot; fictional</span><p>Mr. Lopez needs an abstract for a '
               'disability card and a PCSO guarantee letter. His daughter brings a sample from another patient and asks you to &ldquo;just '
               'copy this and change the name.&rdquo;</p><p>You write his from his own record instead: his diagnosis and its cause, the '
               'date he started dialysis, his access, his current prescription and medicines, and his latest serologies. You date it, sign '
               'it, and send a duplicate to the unit for its file.</p><p class="tc-scene-take"><b>What this shows.</b> An abstract '
               'certifies one patient&rsquo;s facts on one date. A copied template certifies someone else&rsquo;s.</p></div>\n'
               '{{key:Sign every claim as if you had to explain each date to an auditor, because one day you may.}}\n')],
 'debrief': ['<p><strong>Do you sign?</strong> Not this claim, and not the stack until it has been checked. Your signature states that '
             'each listed session happened on that date. A cancelled session and a duplicate are two false statements, however small, and '
             'the attending&rsquo;s name is what gives the claim its credibility.</p>\n'
             '<p><strong>The correction.</strong> Hold the claim. Ask authorized billing staff to remove the cancelled and duplicated '
             'dates through the approved correction workflow, so the audit trail shows who changed what, when, and why. Nobody edits or '
             'rewrites the flowsheets to match a claim; the treatment record is the source, and the claim follows it. Recheck the '
             'corrected claim against the flowsheets and machine logs, and record who reviewed it and when.</p>\n'
             '<p><strong>The real problem.</strong> A system that bills the schedule rather than delivered treatments will produce this '
             'error every month, for every patient who misses a session, and more often after every storm. You do not run this unit, so '
             'write to the operations manager and the clinical head: claims should be generated only from completed treatment records, '
             'with a duplicate check after any downtime. Keep sampling a few claims at each visit, here and at your other units. Tell the '
             'clerk plainly why the 5 p.m. courier will carry fewer forms today.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Matches session dates to source records', False),
                      ('Holds the discrepant claim', False),
                      ('Logs the reviewer, correction and result', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What should the attending do first when records conflict?',
           ['Sign to meet the deadline',
            'Hold attestation and reconcile source records',
            'Ask staff to overwrite the treatment log',
            'Submit and correct next year'],
           1,
           'A truthful attestation depends on a traceable reconciliation of delivered services.'),
          ('Which records support verification of an actual dialysis session?',
           ['The treatment record and corresponding claim documentation',
            'A future chair reservation alone',
            'A monthly billing estimate',
            'The patient&rsquo;s appointment card'],
           0,
           'Claims attest to services delivered on verifiable dates.'),
          ('How many HD sessions per year does PhilHealth cover under Circular 2023-0009?',
           ['Unlimited', '90', '144', 'Up to 156'],
           3,
           'The circular expanded the benefit from 90 to 156 sessions, three a week for 52 weeks. Confirm the current rule on the date of '
           'service.'),
          ('What is the correct way to fix a duplicated claim entry?',
           ['Ask the patient to sign a new form',
            'Delete the treatment record',
            'Correct it through the approved workflow with an audit trail',
            'Ignore it if the amount is small'],
           2,
           'A traceable correction preserves integrity and protects staff.'),
          ('Which principle governs sharing claims data?',
           ['Posting lists in group chats for speed',
            'Minimum necessary disclosure through approved channels under the Data Privacy Act',
            'Emailing full charts to any requester',
            'Printing records for every staff member'],
           1,
           'Proportional, secure processing protects patients and the facility.')],
 'terms': [('PhilHealth', 'Philippine Health Insurance Corporation'),
           ('PSN', 'Philippine Society of Nephrology'),
           ('PCSO', 'Philippine Charity Sweepstakes Office'),
           ('DSWD', 'Department of Social Welfare and Development'),
           ('LGU', 'Local government unit'),
           ('HD', 'Hemodialysis'),
           ('CKD', 'Chronic kidney disease'),
           ('PDD', 'PhilHealth Dialysis Database')],
 'readings': [('philhealth-acr-to-drg.html', 'From All Case Rates to DRG'),
              ('zero-balance-billing-philhealth.html', '"Zero Balance" Doesn\'t Mean Zero Worries')],
 'calcs': []}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
