# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 22: Disasters, outbreaks and service continuity.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Hurricane studies checked against PubMed (Anderson 2009; Kelman 2015)."""

MODULE = {'image_alt': 'A dialysis patient in a raincoat, holding her documents, is helped from a tricycle toward a clinic after a storm.',
 'objectives': ['Prepare patients and the unit for typhoons, floods, outages and outbreaks.',
                'Triage missed treatments by clinical risk and confirm receiving capacity.',
                'Track every deferred patient until care resumes or is formally transferred.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you coordinate with the nurses and the physician on duty in emergencies (b8), '
        'and you provide endorsement documents and coordinate with any receiving unit when a patient must dialyze elsewhere '
        '(b10).[[an22_4]]</div>\n'
        '{{plain:Think of a dialysis patient as a household that can no longer throw out its garbage. Collection comes three times a '
        'week. Miss one pickup and the house is crowded. Miss two and it becomes dangerous to live in.}}\n'
        '<p>The picture has a limit. Garbage piles up at a steady rate, and the danger in a patient does not. Potassium can reach a '
        'level that stops the heart while the patient still looks well, and fluid can flood the lungs overnight. How fast this happens '
        'depends on how much urine the patient still makes, how long since the last session, and what he ate and drank. That is why '
        'two patients who missed the same session can need very different answers.</p>\n'
        '{{cards:Key numbers|Emergency card contents::Prescription, access, dry weight, serologies, medicines, contacts|Hurricane Katrina, '
        'New Orleans::44% of 386 patients missed at least one session; missing 3 or more was associated with twice the odds of '
        'hospitalization|Pre-storm action::Extra or early sessions before forecast landfall (practice, not trial-tested)}}\n'
        '<p>In the Philippines the threat is not one storm a decade. It is a typhoon season every year, plus floods, power cuts and water '
        'interruptions that close units for days. You are usually off site when it happens, with patients at several units. Your work '
        'in this module is to prepare your patients before the season, triage them by risk when sessions are lost, and keep a list until '
        'every one of them is dialyzed or safely transferred.</p>\n',
 'case': {'title': 'The satellite unit that went under water',
          'html': '<p>A typhoon passed overnight. At 6 a.m., the head nurse of your main unit calls you on Viber: the satellite unit in '
                  'the next town is flooded and closed, probably for a week. Its 30 patients, under five attending nephrologists, normally '
                  'dialyze across three shifts. Eight of them are yours. Three of yours have already missed a session. One, Mr. Bernardo, '
                  'has no urine output and told the nurse on the phone that he is breathless and cannot lie flat.</p>\n'
                  '<p>Your main unit can add two extra slots tomorrow morning. The roads to the hospital are partly flooded, cell signal '
                  'comes and goes, and two patients cannot be reached by phone.</p>\n',
          'questions': ['Who is seen first, and is that a slot decision?',
                        'How do you decide who gets the two slots?',
                        'How will you know when every patient is safe?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Between sessions, potassium, fluid and acid accumulate. Dialysis removes them; a missed session lets the rise continue '
               'past the point the next session was built to correct. Potassium is the most immediate danger, because a high level slows '
               'conduction in the heart and can stop it without warning symptoms. The risk is highest in patients who make no urine, and '
               'after the long gap at the end of the week, when the load is already at its peak.</p>\n'
               '<p>Residual urine output changes the slope. A patient who still passes a liter a day keeps excreting some potassium, salt '
               'and water. An anuric patient keeps everything he takes in. Diet changes the slope too: a strict low-potassium, low-salt, '
               'low-fluid emergency diet slows the rise, and an extra session before a storm starts the clock from a lower level.</p>\n'
               '<p>Disasters add their own illnesses. Floodwater carries leptospirosis. Collapsed structures cause crush injury and '
               'rhabdomyolysis. Crowded evacuation centers spread respiratory and diarrheal infection, which a dialysis patient tolerates '
               'poorly.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Factor</th><th>Why it speeds the danger</th><th>What you ask on the phone</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Days since the last session</td><td>More time for potassium and fluid to rise</td><td>&ldquo;When was your last '
               'dialysis?&rdquo;</td></tr>\n'
               '<tr><td>No urine output</td><td>No other route to excrete potassium and water</td><td>&ldquo;Do you still pass '
               'urine? How much?&rdquo;</td></tr>\n'
               '<tr><td>Past high potassium</td><td>A pattern that tends to repeat</td><td>Check the record or the patient&rsquo;s '
               'last results</td></tr>\n'
               '<tr><td>Breathlessness, chest pain, weakness</td><td>Signs that fluid or potassium is already dangerous</td><td>&ldquo;Can '
               'you lie flat? Are your legs weak?&rdquo;</td></tr>\n'
               '</tbody></table></div>\n'
               '<div class="tc-scene"><span class="tc-lab">During a power outage &middot; fictional</span><p>Your unit loses power for '
               'three days after a storm. Mr. Bernardo, anuric, last dialyzed on Friday. Ms. Cruz still passes a liter of urine a day and '
               'dialyzed on Saturday.</p><p>You send Mr. Bernardo to the first available slot. He cannot excrete potassium, and the long '
               'gap after Friday is when risk peaks. Ms. Cruz can wait one more day with a strict emergency diet and a potassium '
               'binder.</p><p class="tc-scene-take"><b>What this shows.</b> Triage by days since the last session, urine output, and '
               'potassium history.</p></div>\n'
               '{{key:At every missed session, ask three things: how long since the last treatment, how much urine, and how high the '
               'potassium has run before.}}\n'
               '\n'
               '{{fig:an22_b}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p>No trial tells us how to run dialysis through a disaster. The evidence is observational, mostly from United States '
               'hurricanes, and it shows association, not cause.</p>\n'
               '<p>After Hurricane Katrina, investigators interviewed 386 patients from nine New Orleans units. 44% missed at least one '
               'session and almost 17% missed three or more. Missing three or more was associated with about twice the odds of '
               'hospitalization (adjusted odds ratio 2.16). Patients who did not know their unit&rsquo;s emergency plan, or who did not '
               'evacuate before landfall, were more likely to miss sessions.[[an22_5]]</p>\n'
               '<p>After Hurricane Sandy, an analysis of 13,264 patients found that 59% received early dialysis before landfall. '
               'Emergency department visits (4.1%), hospitalizations (4.5%) and 30-day deaths (1.83%) were still higher than in '
               'comparison groups.[[an22_6]] The study did not compare patients who did and did not get early dialysis, so it does not '
               'show that the early session itself prevented harm. Early sessions remain sensible practice built on physiology, not a '
               'proven intervention.</p>\n'
               '<p>Outbreak responses in a unit, such as isolation, cohorting and hepatitis B segregation, follow Centers for Disease '
               'Control and Prevention (CDC) guidance[[an22_3]] and the Department of Health (DOH) rules for dialysis '
               'facilities.[[an22_1]] Regional DOH offices publish the assessment tools units are inspected against.[[an22_2]]</p>\n'
               '{{key:The strongest lesson from the hurricanes is not a drug or a machine. It is that patients who knew the plan, and left '
               'early, missed fewer sessions.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Before typhoon season.</strong> Make sure each of your patients carries an emergency card: diagnosis, access, dry '
               'weight, prescription, medicines, serologies and unit contacts. Give them a three-day emergency diet and, where you '
               'prescribe one, a supply of potassium binder they can afford. Name an alternative unit on the card. You do not run the '
               'units, so ask the clinical head and the head nurse to check the cards and to agree mutual-aid slots with nearby '
               'units.</p>\n'
               '<p><strong>When a storm is forecast.</strong> Agree with the unit on extra or early sessions before landfall for your '
               'highest-risk patients, and tell families which signs mean the emergency room rather than waiting.</p>\n'
               '<p><strong>During an outage.</strong> Route anyone breathless, with chest pain or with new weakness to emergency care '
               'first. Triage the rest by days since the last treatment, urine output and potassium history. For each patient you place, '
               'confirm acceptance by the receiving unit and the transport, and send the endorsement and serologies ahead. Keep a '
               'deferred-treatment list until every patient has a disposition. Where cell signal fails, ask the barangay health office or '
               'the family to check on the patients you cannot reach. During an infection cluster, involve infection prevention and keep '
               'the incident data.</p>\n'
               '\n'
               '{{fig:an22_a}}\n'
               '<div class="tc-scene"><span class="tc-lab">Before typhoon season &middot; fictional</span><p>In May you ask the head nurse '
               'to check your patients&rsquo; emergency cards. Twelve cards are missing their dry weight, and four list a unit that has '
               'closed. The head nurse updates them during the next week&rsquo;s sessions.</p><p>The clinical head signs a mutual-aid '
               'agreement with a unit across the river, listing how many extra slots each can offer the other, and you make sure your '
               'patients&rsquo; cards name that unit.</p><p class="tc-scene-take"><b>What this shows.</b> Preparation in May decides who '
               'is safe in September.</p></div>\n'
               '{{key:A name comes off the list only when that patient has been dialyzed or formally transferred, never when a message '
               'has merely been sent.}}\n'
               '{{call:<ul><li>Breathlessness or chest pain after missed sessions</li><li>Anuric patient missing 2 or more sessions</li>'
               '<li>Patient unreachable after the event</li><li>Evacuation-center fever or diarrhea cluster among dialysis '
               'patients</li></ul>}}\n')],
 'debrief': ['<p><strong>First.</strong> Mr. Bernardo goes to emergency assessment now. Breathlessness and orthopnea in an anuric patient '
             'who has missed dialysis can mean pulmonary edema or dangerous potassium. That is not a decision about a slot tomorrow. '
             'Arrange transport, call the receiving hospital yourself, and confirm that it will accept him.</p>\n'
             '<p><strong>The two slots.</strong> Agree with the clinical head and the other attending nephrologists that the slots go to '
             'whoever is in most danger, not to whoever&rsquo;s doctor calls first. Triage by days since the last session, whether they '
             'still make urine, and their potassium history. Potassium is the most immediate danger, and anuric patients after the long '
             'gap are at highest risk. Confirm acceptance and transport for each patient you place. Give everyone waiting interim advice: '
             'the emergency low-potassium, low-salt, low-fluid diet, their potassium binder if they have one, and the warning signs '
             '(breathlessness, chest pain, weakness) that mean going to an emergency department instead of waiting.</p>\n'
             '<p><strong>Every patient safe.</strong> Ask the clinical head to keep one deferred-treatment list for all 30 patients, and '
             'make sure each of your eight has a plan on it. Remove a name only when that patient has been dialyzed or formally '
             'transferred. Keep calling the two who cannot be reached, and ask the barangay health office or the family to check on them. '
             'The hurricane studies are observational, but they point the same way: missed sessions were associated with more '
             'admissions, and patients who knew the plan missed fewer. After the water recedes, review why three patients missed sessions '
             'before you knew, and plan extra sessions before the next forecast landfall.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Prioritizes by clinical risk', False),
                      ('Names alternate sites and confirms acceptance', False),
                      ('Closes the follow-up list', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What determines disposition during an outage?',
           ['Routine appointment order alone',
            'Clinical urgency and confirmed receiving capability',
            'Who returns the first phone call',
            'Alphabetical order'],
           1,
           'Safe continuity depends on risk-based triage and a verified handoff.'),
          ('When can the unit close an outage tracker entry?',
           ['When treatment has resumed or disposition and acceptance are confirmed',
            'When a referral message is sent',
            'When the prior appointment time passes',
            'When the storm ends'],
           0,
           'Confirmed disposition closes the continuity gap.'),
          ('Which patient is at highest risk after missed sessions?',
           ['A peritoneal dialysis (PD) patient with normal drainage',
            'A patient with 1 L/day urine output who missed one session',
            'A newly started incremental hemodialysis (HD) patient with good urine output',
            'An anuric patient with prior hyperkalemia who missed two sessions'],
           3,
           'No urine output and a history of high potassium predict rapid, dangerous accumulation.'),
          ('What does the Hurricane Katrina study of 386 New Orleans patients show?',
           ['Extra sessions before landfall prevented all hospitalizations',
            'Missed sessions had no link to outcomes',
            'Missing 3 or more sessions was associated with higher odds of hospitalization',
            'Patients in shelters missed fewer sessions'],
           2,
           'The adjusted odds ratio was 2.16. The design was observational, so it shows association, not cause.'),
          ('Why include serologies on the emergency card?',
           ['To speed Philippine Health Insurance Corporation (PhilHealth) claims',
            'Receiving units need hepatitis B status to place patients safely',
            'To avoid the need for a prescription',
            'To replace the dry weight'],
           1,
           'Hepatitis B segregation is an infection-prevention requirement in every unit.')],
 'terms': [('PSN', 'Philippine Society of Nephrology'),
           ('CDC', 'Centers for Disease Control and Prevention'),
           ('DOH', 'Department of Health'),
           ('HD', 'Hemodialysis'),
           ('PD', 'Peritoneal dialysis')],
 'readings': [('typhoon-disaster-preparedness-dialysis.html', 'Typhoon & Disaster Preparedness for Dialysis Patients'),
              ('climate-extremes-kidney-care.html', 'Green, Prepared and Resilient: Kidney Care in an Era of Climate Extremes')],
 'calcs': ['calc-dialysis-continuity-planner.html',
           'calc-potassium-load.html',
           'calc-leptospirosis-aki-risk.html',
           'calc-mcmahon-rhabdo.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
