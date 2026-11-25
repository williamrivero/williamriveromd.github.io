# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 01: Taking attending responsibility.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice (attending off site, reached by phone and Viber, monthly face-to-face review). PhilHealth figures checked
against the PhilHealth news release; handoff figures against the PubMed abstract (I-PASS, 2014)."""

MODULE = {'image_alt': 'A physician takes a phone call at a corridor window, looking toward a lit dialysis unit across the courtyard.',
 'objectives': ['Verify registration, appointment, privileges and facility capability before accepting a dialysis panel.',
                'Name a primary attending, a backup and an after-hours escalation route in writing.',
                'Separate the longitudinal plan, the bedside response and the facility response in every handoff.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, to be an attending nephrologist (AN) of a hemodialysis center (HDC) you must '
        'be a physician licensed by the Professional Regulation Commission (PRC), trained in nephrology at a PSN-accredited or recognized '
        'institution, practicing in the area and easily reached by the unit, and affiliated with an updated Philippine Health Insurance '
        'Corporation (PhilHealth) accreditation and a PSN or chapter endorsement (items a1&ndash;a3). You see each patient at least once a '
        'month, preferably face to face, or by telemedicine if necessary (b6), and you are paid only the professional fee set in PSN '
        'guidelines (b13).[[an01_1]]</div>\n'
        '{{plain:Think of the dialysis unit at night as a circulation. The facility&rsquo;s license is the vessel wall: it sets what the '
        'unit may safely do. Your privileges are the pump: they set what you may order there. The roster and the escalation route are the '
        'conduction system: they decide whether a signal from the bedside reaches someone who can act.}}\n'
        '<p>The picture has a limit. A heart conducts on its own. A dialysis unit conducts only what people have written down and '
        'rehearsed. A call from the physician on duty (POD) reaches you only if a named person, a working phone number and a time limit '
        'carry it, and it reaches a backup only if someone agreed in advance to be one.</p>\n'
        '{{cards:Key numbers|AN review, maintenance hemodialysis (HD)::At least monthly, preferably face to face (PSN 2024, b6)|PhilHealth '
        'HD sessions per year::Up to 156 for patients registered in the PhilHealth Dialysis Database|PhilHealth HD package rate::PHP 6,350 '
        'per session, effective October 9, 2024; confirm the current rate on the date of service}}\n'
        '<p>In Philippine practice you are rarely in the unit when trouble starts. Several attendings share one center, each patient chooses '
        'his own, and the POD and the nurses reach you by phone and Viber. Your work in this module is to make sure that, before you accept a '
        'single patient, every call has somewhere to go.</p>\n',
 'case': {'title': 'The panel that starts on Monday',
          'html': '<p>Bagong Pag-asa Dialysis Center, a freestanding unit in Bulacan with 18 stations and three shifts, asks you to take '
                  'over a panel of 22 patients. Their attending nephrologist emigrated last month. The administrator, Ms. Lagman, wants '
                  'you to start on Monday.</p>\n'
                  '<p>You hold clinic in Quezon City and can visit the unit once a week. The night shift runs until 11 p.m., and the '
                  'physician on duty for that shift has been told to &ldquo;just Viber the doctor&rdquo; if something happens. When you ask '
                  'who covers you when you cannot answer, Ms. Lagman says, &ldquo;The last doctor never needed a backup.&rdquo; Nobody can '
                  'tell you which hospital accepts their emergency transfers. The License to Operate on the wall expired three weeks ago; '
                  'she says the renewal is &ldquo;being processed.&rdquo;</p>\n',
          'questions': ['Would you start on Monday? What must be in writing first?',
                        'What will the physician on duty do at 9 p.m. if you do not answer?',
                        'Which of these gaps belong to you, and which belong to the facility?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Three separate authorities have to line up before a patient is safe in your care. The PRC license says you may practice '
               'medicine.[[an01_4]] The Department of Health (DOH) License to Operate (LTO) says the facility may run a hemodialysis '
               'service, with the staffing and the referral arrangements the licensing rules require.[[an01_2]][[an01_3]] PhilHealth '
               'accreditation says the payer will recognize the care.[[an01_6]] The PSN adds its own conditions for the attending: '
               'nephrology training, membership or chapter endorsement, and being near enough to be reached.[[an01_1]][[an01_5]] Each '
               'authority covers something the others do not. A gap in any one leaves the POD holding a decision nobody owns.</p>\n'
               '<p>Most night failures are failures of conduction, not knowledge.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Link in the chain</th><th>What breaks it</th><th>What the POD sees at 9 p.m.</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Primary attending</td><td>Phone on silent, no time limit before escalation</td><td>Three unanswered calls and a '
               'patient still on the floor</td></tr>\n'
               '<tr><td>Backup</td><td>Never named, or named but never told</td><td>Nobody to call next</td></tr>\n'
               '<tr><td>Receiving hospital</td><td>No written transfer arrangement or contact person</td><td>An ambulance with no '
               'destination</td></tr>\n'
               '<tr><td>Facility license</td><td>Expired, or the service capability does not cover the patients enrolled</td><td>Care the '
               'unit is not licensed to give</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Before you accept a panel, trace one night call from the bedside to a decision and to an ambulance. Every link must have '
               'a name.}}\n'
               '<div class="tc-scene"><span class="tc-lab">By phone, 9:20 p.m. &middot; fictional</span><p>Dr. Salonga, the physician on '
               'duty, calls your mobile three times. You are in a cinema with the phone on silent. At 9:35 he sends a Viber message to the '
               'clinical head, who is abroad. At 9:50 the patient with chest pain is still on the floor, because nobody told him which '
               'hospital accepts the unit&rsquo;s transfers.</p><p>Nobody in this story lacked knowledge. Dr. Salonga knew the patient '
               'needed a hospital. The signal simply had nowhere to go.</p><p class="tc-scene-take"><b>What this shows.</b> Your job begins '
               'before the call: a named backup, a time limit, and a confirmed receiving hospital.</p></div>\n'
               '\n'
               '{{fig:an01_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p>Most of this module rests on regulation, not trials. The PSN guideline, the DOH licensing rules and the PhilHealth '
               'circulars are binding requirements to be checked on the date of service. They are not graded recommendations, and no study '
               'tested them.[[an01_1]][[an01_2]][[an01_7]]</p>\n'
               '<p>The evidence on handoffs is observational but consistent. In the I-PASS study, a structured handoff program was introduced '
               'for pediatric residents in nine hospitals. Across 10,740 admissions, medical errors fell from 24.5 to 18.8 per 100 '
               'admissions, a 23% relative reduction, and preventable adverse events fell from 4.7 to 3.3 per 100 admissions. '
               'Nonpreventable adverse events did not change.[[an03_4]] The design was before and after, in teaching wards, not dialysis units. It '
               'suggests that structure matters; it does not show the size of the effect on a night shift in Bulacan.</p>\n'
               '<p>The PhilHealth figures in the key numbers come from its circulars and news release; confirm them before you quote them to '
               'a patient.[[an01_6]][[an01_8]]</p>\n'
               '{{key:Treat Philippine requirements as rules to verify, not evidence to weigh. Treat handoff structure as a well-supported '
               'safety habit, not a guarantee.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>File your credentials first.</strong> Before your first shift, file the packet: PRC identification card, the '
               'facility appointment and privilege letter, the PSN or chapter endorsement, your PhilHealth accreditation status, and a copy '
               'of the unit&rsquo;s current License to Operate.[[an01_4]][[an01_5]][[an01_3]]</p>\n'
               '<p><strong>Map one night call.</strong> Walk through a simulated call with the head nurse and a POD. Who receives it? How '
               'many minutes before the backup is called? Which hospital accepts, who is the contact there, and who arranges transport? Agree what '
               'the POD sends you by Viber: the trend, what was done, and the decision he needs. If the unit cannot name a backup or an accepting hospital, do not accept the '
               'panel yet. Ask for a written arrangement first.</p>\n'
               '<p><strong>Know which hat you are wearing.</strong> In many Philippine units one nephrologist is both an attending and the '
               'medical director or clinical head. Patient care and facility oversight carry different duties. Write which role you are '
               'acting in when you sign.</p>\n'
               '\n'
               '{{fig:an01_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the administrator&rsquo;s office &middot; fictional</span><p>Before signing, '
               'you ask Ms. Lagman for four things: the current License to Operate, the transfer agreement, next month&rsquo;s roster, and '
               'the escalation sheet posted at the nurses&rsquo; station. She finds the first two. The roster lists no backup, and the '
               'escalation sheet still carries the name of the attending who emigrated.</p><p>You agree on a start date two weeks away. '
               'Together you write whom the physician on duty calls first, whom after 10 minutes, and whom after 20.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> A two-week delay with a working escalation route is safer than a Monday start '
               'without one.</p></div>\n'
               '{{key:Accept a panel only when your coverage, the backup and the receiving hospital are on paper. The patients depend on the '
               'arrangement, not on your good intentions.}}\n'
               '{{call:<ul><li>No named backup consultant</li><li>No written transfer agreement</li><li>POD told to &lsquo;message the '
               'doctor&rsquo; with no time limit before escalation</li><li>License to Operate expired or service capability not covering '
               'the patients enrolled</li></ul>}}\n')],
 'debrief': ['<p><strong>Would you start on Monday?</strong> Not on these terms. Three things must be in writing before you accept a '
             'single patient: who covers when you cannot answer, with response times; an escalation rule the physician on duty can follow '
             'without you (for example, the backup is called at 10 minutes, and an unstable patient goes to the emergency transfer at 20); '
             'and a named accepting hospital with a contact person.</p>\n'
             '<p><strong>What happens at 9 p.m.?</strong> As things stand, the physician on duty sends a Viber message and waits. That is '
             'the conduction failure this module describes. Before you start, walk through one simulated night call with the head nurse and '
             'the physician on duty, from the first symptom to a patient in an ambulance.</p>\n'
             '<p><strong>Whose gaps are these?</strong> The license and the transfer agreement belong to the facility and its medical '
             'director. The coverage arrangement and your credentials belong to you. Offer to start once both sides are in writing, and say '
             'why: twenty-two patients are about to depend on a promise that someone will answer.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Verifies the credential packet against originals', False),
                      ('Maps a sample after-hours call with time limits', False),
                      ('Confirms backup cover and the accepting pathway in writing', False),
                      ('States which role is acting (AN, Medical Director or Clinical Head)', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What should be settled before the first shift?',
           ['A standing saline order alone',
            'Written primary, backup and transfer arrangements',
            'The monthly billing deadline',
            'A list of preferred dialyzer brands'],
           1,
           'An order set cannot assign responsibility when a clinician is unavailable or a patient needs transfer.'),
          ('Which document defines whether the facility may operate an HD service?',
           ['The facility&rsquo;s applicable DOH License to Operate',
            'An individual PSN membership certificate',
            'A list of reimbursed claims',
            'The attending&rsquo;s PRC identification card'],
           0,
           'A facility license, physician credentials and payer accreditation are separate authorities.'),
          ('Under the PSN 2024 HD guidelines, how often should the AN review a maintenance HD patient?',
           ['Only at initiation and annual renewal',
            'Only when the POD calls',
            'Every six months',
            'At least monthly, preferably face to face, with telemedicine when necessary'],
           3,
           'Section 1.2 sets a minimum monthly consultation. A documented review supports continuity and the claim you sign.'),
          ('A clinic&rsquo;s night POD cannot reach you during an emergency. What design element was missing?',
           ['A larger dialysate inventory',
            'A second copy of the HD prescription',
            'A time-limited escalation rule to a named backup and an emergency transfer pathway',
            'A quarterly staff meeting'],
           2,
           'Escalation must not depend on one person answering. A time trigger turns an unanswered call into an action.'),
          ('One physician serves as both the AN and the unit&rsquo;s Medical Director. What should the record show?',
           ['Nothing, since the roles are identical',
            'Which role is acting for each decision',
            'Only the Medical Director signature',
            'Only the PhilHealth accreditation number'],
           1,
           'Patient care and facility oversight carry different duties; naming the acting role keeps accountability clear.')],
 'terms': [('AN', 'Attending nephrologist'),
           ('HDC', 'Hemodialysis center'),
           ('HD', 'Hemodialysis'),
           ('PRC', 'Professional Regulation Commission'),
           ('PSN', 'Philippine Society of Nephrology'),
           ('DOH', 'Department of Health'),
           ('LTO', 'License to Operate'),
           ('PIC', 'Professional identification card'),
           ('PDD', 'PhilHealth Dialysis Database'),
           ('POD', 'Physician on duty')],
 'readings': [('hemodialysis-transfer-guide.html', 'Hemodialysis Transfer Guide: How to Change Dialysis Centers or Nephrologists Safely')],
 'calcs': ['calc-dialysis-shift-coverage.html', 'calc-dialysis-continuity-planner.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
