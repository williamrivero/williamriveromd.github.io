# -*- coding: utf-8 -*-
"""Physician on Duty, Module 01: Your Role on the Dialysis Floor. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty talking with a nurse at the nurses' station of a hemodialysis unit.",
    "objectives": [
        "Describe what a physician on duty is responsible for, and what belongs to the attending nephrologist.",
        "Name the members of the dialysis team and what each one decides.",
        "Follow one shift from before the first patient arrives to the last handoff.",
        "Separate what your unit&rsquo;s protocol lets you do at once from what needs a call first.",
        "Report to the attending nephrologist with a clear, structured message, and record what was done.",
        "Apply professional conduct on the floor: confidentiality, consent, boundaries, and speaking up.",
    ],
    "big": """
{{plain:Think of a dialysis shift as a flight. The attending nephrologist wrote the flight plan for each patient. The nurses and technicians fly the aircraft. You are the doctor on board. You do not rewrite the flight plan in mid-air, but when a passenger becomes ill, you are the one who examines, acts in the first minutes, and radios the ground with exactly what is happening.}}
{{cards:Key terms for this module|Physician on duty (POD)::The doctor who is physically present in the unit while patients are on dialysis.|Attending nephrologist::The kidney specialist responsible for a patient&rsquo;s dialysis prescription and long-term care.|Dialysis prescription::The nephrologist&rsquo;s order for one patient: time, flows, dialysis fluid, fluid removal target, and blood thinner.|Unit protocol::A written, approved instruction that says what staff may do in a defined situation without a new order.|Escalate::Tell the right person now, clearly, because the problem is beyond your role or is not improving.|SBAR::A four-part way to report: Situation, Background, Assessment, Recommendation.|Dry weight::The target weight at the end of dialysis, when extra fluid has been removed. It is set by the nephrologist.}}
{{flow:Three habits this module teaches|Look first::See the patient yourself before you decide anything.|Act within protocol::Do what your unit&rsquo;s protocol allows for this situation.|Call early::Tell the attending nephrologist what you found, what you did, and what you need.}}
""",
    "case": {"title": "The first Monday", "html": """
<p>It is your first morning as physician on duty. Mrs. Santos, 61, arrives for her Monday session. She dialyzes twice a week, and her last session was on Thursday. She is short of breath when she walks from the scale to her chair. She is 4.5 kilograms above her dry weight, her blood pressure is 180/100 mm Hg, and her oxygen saturation is 91% on room air.</p>
<p>The nurse, who has worked in the unit for nine years, says: &ldquo;Doctor, her dry weight is too high. She is always like this on Mondays. Can you just lower it by one kilogram and write the order so we can start?&rdquo; Three other patients are waiting to be seen.</p>
""", "questions": ["What do you do in the next five minutes?",
                  "Is changing the dry weight your decision to make?",
                  "What will you say when you call the attending nephrologist?"]},
    "sections": [
        ("role", "Your role", "What a physician on duty is, and is not", """
<p>A hemodialysis (HD) unit treats many patients at once, each connected to a machine that moves about 300 milliliters of blood a minute outside the body. Serious problems are uncommon, but they develop within minutes. For that reason, Philippine standards expect a physician to be physically present whenever the unit is operating.[[psn2024]]</p>
<p>The Philippine Society of Nephrology (PSN) standards for hemodialysis clinics describe the physician on duty (POD) as a licensed physician who gives acute care to patients during treatment, under the supervision of each patient&rsquo;s attending nephrologist and the clinical head of the unit.[[psn2024]] The same standards expect the POD to hold a current advanced cardiac life support (ACLS) certificate and a certificate from a recognized course for physicians on duty, and they describe one POD for about 15 treatment stations as the ideal.[[psn2024]]</p>
{{cards:What the standards expect of you|See every patient::Evaluate all patients during your tour of duty and write down what you find.|Give acute care::Manage urgent problems before, during, and after dialysis.|Carry out the prescription::Follow the attending nephrologist&rsquo;s orders; you do not replace them.|Keep the nephrologist informed::Report acute problems and emergencies.|Review::Read the previous treatment records and new laboratory results, and interpret them with the nephrologist.|Refer or admit::Send a patient to the hospital when needed, with the nephrologist&rsquo;s knowledge.}}
<p>Two limits follow from this. First, the dialysis prescription belongs to the attending nephrologist, who provides both the first and the ongoing prescription.[[psn2024]] Second, the standards say that no referral to another specialty is made without the knowledge of the attending nephrologist or the clinical head.[[psn2024]] The reason is practical: the nephrologist knows the patient&rsquo;s history over months and years, and you are seeing one day of it.</p>
{{key:You are responsible for what happens during your shift. The attending nephrologist is responsible for the plan. Good care needs both, and the link between them is your phone call.}}
"""),
        ("team", "The team", "Who does what on the dialysis floor", """
<p>You will be the newest person in a team that has worked together for years. Knowing what each member decides helps you ask the right person the right question.</p>
{{fig:pod01_team}}
<div class="table-wrap"><table>
<thead><tr><th>Team member</th><th>Decides or does</th><th>Ask them about</th></tr></thead>
<tbody>
<tr><td>Attending nephrologist</td><td>The dialysis prescription, dry weight, medicines, access plan, long-term care</td><td>Any change to the plan; any problem that is serious, new, or not improving</td></tr>
<tr><td>Medical director or clinical head</td><td>Unit protocols, quality and safety, staff privileges</td><td>Protocol questions; events that affect several patients; anything you cannot resolve with the attending nephrologist</td></tr>
<tr><td>Physician on duty</td><td>Assessment and acute care during the shift, within protocol</td><td>&mdash;</td></tr>
<tr><td>Dialysis nurse</td><td>Patient assessment, needle insertion, machine settings as ordered, monitoring, medicines as ordered</td><td>How this patient usually behaves on dialysis; what has changed today</td></tr>
<tr><td>Head or charge nurse</td><td>Staffing, patient flow, station assignment, isolation</td><td>Where to put an unstable or infectious patient; who can help</td></tr>
<tr><td>Dialysis technician</td><td>Machine preparation, water system checks, equipment problems</td><td>Alarms that will not clear; water and dialysis fluid checks</td></tr>
<tr><td>Renal dietitian</td><td>Diet and fluid advice</td><td>High weight gains, high potassium or phosphate, weight loss</td></tr>
<tr><td>Social worker or patient navigator</td><td>Financing, transport, family support</td><td>Missed sessions, money problems, caregiver strain</td></tr>
</tbody></table></div>
<p>Dialysis nurses often know a patient far better than you will after one examination. A nurse who says &ldquo;he is not himself today&rdquo; is giving you a clinical finding. Take it seriously and go and look.</p>
{{key:Respect for the nurses&rsquo; experience and responsibility for your own decisions go together. Listen to the nurse, examine the patient yourself, then decide what is yours to decide.}}
"""),
        ("shift", "The shift", "The shape of one shift", """
<p>A unit usually runs two or three shifts a day, each about four hours of treatment plus the time to connect and disconnect patients. The work comes in waves. Most problems appear at three points: before the session starts, in the last hour when the most fluid has been removed, and when needles come out.</p>
{{flow:One shift from start to finish|Before patients arrive::Check the emergency cart, oxygen, suction, and defibrillator. Read the handoff notes. Ask the charge nurse who worries her today.|Arrival and weighing::See each patient: weight gain, blood pressure, breathing, the access, and any new complaint.|First hour::Stay on the floor. Reactions to the dialyzer and access problems show early.|Middle hours::Review laboratory results and records. Write notes. Walk the floor again.|Last hour::Blood pressure falls and cramps are most likely now. Be visible.|Disconnection::Check bleeding from needle sites, standing blood pressure, and how the patient feels before leaving.|Handoff::Tell the next physician and the attending nephrologists what happened and what is pending.}}
{{fig:pod01_floor}}
<p>Learn the room before you need it. On your first day, find the emergency cart, the oxygen outlets, the suction, the defibrillator, the isolation station, and the list of telephone numbers for every attending nephrologist. Ask a nurse to show you how a treatment is stopped and blood is returned to the patient. In an emergency you will not have time to look.</p>
{{fig:code_readiness|An emergency-ready dialysis unit. Check these items yourself at the start of every shift.}}
"""),
        ("decide", "Act or call", "What you may do at once, and what needs a call", """
<p>Every unit should have written protocols for common problems, such as a fall in blood pressure, muscle cramps, chest pain, or fever. A protocol tells staff what they may do immediately, without waiting for a new order. Read your unit&rsquo;s protocols before your first shift. If your unit has none for a situation, treat the situation as one that needs a call.</p>
<p>The rule for this series is simple. <strong>Follow your unit&rsquo;s protocol, and ask the attending nephrologist for guidance.</strong> The two are not alternatives. The protocol covers the first minutes. The call covers what comes next, and it lets the nephrologist adjust the plan for a patient they know.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Usually within protocol (act, then report)</th><th>Needs the attending nephrologist (call first)</th></tr></thead>
<tbody>
<tr><td>Blood pressure falls during dialysis</td><td>First steps in the unit&rsquo;s hypotension protocol</td><td>Pressure that does not recover; any change to the fluid removal target or dry weight</td></tr>
<tr><td>Patient arrives very overloaded</td><td>Oxygen, positioning, assessment</td><td>Extra time, an extra session, or a new dry weight</td></tr>
<tr><td>Laboratory result out of range</td><td>Repeat or confirm as protocol allows; examine the patient</td><td>Any change to the dialysis fluid (potassium, calcium, bicarbonate) or to medicines</td></tr>
<tr><td>Access problem</td><td>Examine; hold needle insertion if unsafe; control bleeding</td><td>Use of a different access; referral to the access surgeon</td></tr>
<tr><td>Fever or chills</td><td>Assessment and cultures as protocol allows</td><td>Antibiotic choice; catheter removal; admission</td></tr>
<tr><td>Chest pain, new confusion, seizure</td><td>Emergency first steps; call for help</td><td>Call during the first steps, not after; decide transfer together</td></tr>
<tr><td>Patient asks to stop early or skip a session</td><td>Listen; explain the risk; document</td><td>Inform the nephrologist the same day</td></tr>
</tbody></table></div>
{{call:Call the attending nephrologist before you change the dry weight, the dialysis fluid, the treatment time, the blood thinner, or the access plan. Call during, not after, any emergency. If you cannot reach the attending nephrologist, follow your unit&rsquo;s escalation list to the covering nephrologist or the clinical head.}}
{{fig:pod01_ladder}}
<p>New physicians sometimes worry that calling shows weakness. The opposite is true. Nephrologists expect to be called and would rather hear about a problem early. A late call, after an avoidable admission, is the one that damages trust.</p>
"""),
        ("sbar", "Reporting", "How to call the nephrologist: SBAR", """
<p>A telephone report fails in two common ways. The caller tells a long story and the listener cannot find the problem, or the caller gives a number with no context. A fixed structure prevents both. The most widely used is SBAR: Situation, Background, Assessment, Recommendation.</p>
<p>How well does it work? A systematic review of 11 studies found moderate evidence that introducing SBAR improved patient safety, especially for telephone communication, and noted that high-quality studies are few.[[muller2018]] The structure is supported by evidence and by long practice, but it has not been proven in large trials.</p>
{{cards:SBAR for a dialysis call|Situation::Who you are, who the patient is, and the problem in one sentence.|Background::Why the patient is on dialysis, the access, the schedule, and what is relevant from today.|Assessment::What you found and what you think is happening. Give numbers.|Recommendation::What you have done, what you propose, and what you need from the nephrologist.}}
<div class="tc-formula"><strong>Worked example.</strong><br>
<strong>S:</strong> &ldquo;Doctor, this is Dr. Reyes, physician on duty at the morning shift. I am calling about Mrs. Santos. She arrived short of breath and I have not started her dialysis.&rdquo;<br>
<strong>B:</strong> &ldquo;She is on dialysis twice a week through a left arm fistula. Her last session was Thursday. Her dry weight is 52 kilograms.&rdquo;<br>
<strong>A:</strong> &ldquo;She is 4.5 kilograms above dry weight. Blood pressure 180/100, heart rate 104, oxygen saturation 91% on room air, crackles in both lung bases, no chest pain. Her electrocardiogram shows no new changes. I think this is fluid overload after the long gap.&rdquo;<br>
<strong>R:</strong> &ldquo;I have given oxygen and sat her upright. I would like to start dialysis now. May I have your orders for the fluid removal target and treatment time today? The nurse also thinks her dry weight needs review.&rdquo;</div>
<p>Three habits complete the call. Have the chart in front of you before you dial. Repeat the orders back to the nephrologist so that both of you hear the same thing. Write the orders, the time, and the nephrologist&rsquo;s name in the record straight away.</p>
{{key:Before you call, be able to state the weight gain, the vital signs, the access, the last session, and the latest potassium. Most of the nephrologist&rsquo;s questions will be about these.}}
"""),
        ("records", "Records", "What to write, and when", """
<p>Your note is how the attending nephrologist, the next physician, and the patient&rsquo;s future doctors learn what happened. It is also a legal record. Write it during the shift, not from memory afterward.</p>
<div class="table-wrap"><table>
<thead><tr><th>For every patient</th><th>For every event</th></tr></thead>
<tbody>
<tr><td>Complaints since the last session</td><td>The time it started and who noticed it</td></tr>
<tr><td>Weight gain, blood pressure, breathing, access findings</td><td>What you found on examination, with numbers</td></tr>
<tr><td>Whether the session started as ordered, and any change</td><td>What was done, in order, with times</td></tr>
<tr><td>New laboratory results and what was done about them</td><td>Whom you called, when, and the orders received</td></tr>
<tr><td>How the patient was at the end</td><td>The outcome: recovered, sent home, transferred, admitted</td></tr>
</tbody></table></div>
<p>Report events and near misses through your unit&rsquo;s incident system as well as in the chart. A near miss is an error that was caught before it reached the patient. Reporting it is not an admission of fault. It is how a unit finds a weak point before someone is harmed.</p>
"""),
        ("conduct", "Conduct", "Professional conduct on the floor", """
<p>Patients on dialysis come to the same room two or three times a week for years. They know the staff, each other, and each other&rsquo;s families. That closeness is good for care and it creates risks that a ward or clinic does not.</p>
{{cards:Conduct that protects patients and you|Confidentiality::An open floor carries voices. Discuss results, hepatitis or HIV status, money, and family matters quietly at the chair or in private, never across the room.|Consent::Explain what you propose and why before you do it. A patient may refuse a treatment or stop a session early. Explain the risk, record the discussion, and inform the nephrologist.|Boundaries::Be warm and consistent. Decline gifts of value, loans, and private arrangements. Do not treat favorite patients differently.|Photographs and social media::Never post or share a patient&rsquo;s image, record, or story without written consent, even in a private chat group.|Speaking up::If you see something unsafe, say so at once, whoever is involved. If someone corrects you, thank them.|Knowing your limits::Say &ldquo;I do not know, I will find out.&rdquo; It is safer than guessing and it earns trust.}}
<p>Patient information is protected by law. The Data Privacy Act of 2012 treats health information as sensitive personal information, and it applies to photographs and messages on personal telephones as much as to paper charts.[[ra10173]]</p>
{{call:Tell the attending nephrologist and the clinical head the same day if a patient refuses treatment, makes a complaint about care, or says anything that suggests self-harm.}}
"""),
    ],
    "debrief": ["""
<p><strong>What to do in the next five minutes.</strong> See Mrs. Santos before anything else. Sit her upright, give oxygen, and examine her: breathing, heart, lungs, legs, and the fistula. Ask about chest pain, fever, and cough, and ask what she ate and drank over the weekend. Review her recent sessions. Ask for an electrocardiogram if your protocol calls for one in a breathless patient. Fluid overload after a long gap is the most likely cause, but a heart attack, a chest infection, and a rhythm problem can look the same at the door.</p>
<p><strong>Is the dry weight yours to change?</strong> No. Dry weight is part of the prescription and belongs to the attending nephrologist. The nurse may well be right that it needs review. Nine years of Mondays is useful evidence, and you should pass her observation on. But lowering a dry weight means removing more fluid at every session from now on, and if it is wrong the patient pays with low blood pressure, cramps, and a damaged heart over time. That decision needs the person who knows her history.</p>
<p><strong>What to say.</strong> The worked SBAR example in this module is the call. Notice what it contains: the reason you have not started, the numbers, your assessment, what you have already done, and a clear request. It also carries the nurse&rsquo;s concern forward, so the nephrologist can act on it.</p>
<p><strong>And the three patients waiting?</strong> Tell the charge nurse that you are with an unstable patient and ask her to tell you at once if any of the three is unwell. A breathless patient with low oxygen comes first.</p>
"""],
    "skills": {"title": "Start-of-shift readiness round",
               "intro": "Complete this round before the first patient is connected, with the charge nurse.",
               "items": [
                   ("Locates the emergency cart and confirms that it is sealed or checked and signed for the day.", True),
                   ("Confirms that the defibrillator is present, charged, and has pads, and switches it on to test it as the unit allows.", True),
                   ("Confirms working oxygen and suction, with a mask and tubing at hand.", True),
                   ("Finds the contact list for every attending nephrologist on the shift and the escalation list for when one cannot be reached.", True),
                   ("Reads the handoff notes from the previous shift.", False),
                   ("Asks the charge nurse which patients concern her today, and why.", False),
                   ("Identifies the isolation station and which patients use it.", False),
                   ("Knows where the unit&rsquo;s written protocols are kept and has read the protocols for low blood pressure, chest pain, and cardiac arrest.", True),
                   ("Asks a nurse to demonstrate how a treatment is stopped and blood is returned, including by hand if power fails.", False),
                   ("Introduces themselves to the staff and to each patient as the physician on duty.", False),
               ],
               "placement": "On your first observed shift, write one SBAR report for a real problem, give it to your preceptor before you call, and compare it with what the nephrologist asked."},
    "quiz": [
        ("Which statement best describes the physician on duty in a hemodialysis unit?",
         ["The physician who writes each patient&rsquo;s dialysis prescription",
          "A licensed physician who gives acute care during treatment, under the supervision of the attending nephrologist and the clinical head",
          "A physician who is on call by telephone during treatment hours",
          "The physician who replaces the nephrologist for long-term decisions"], 1,
         "The physician on duty is physically present and gives acute care during the shift. The prescription and long-term plan belong to the attending nephrologist."),
        ("A nurse asks you to lower a patient&rsquo;s dry weight. What is the best response?",
         ["Lower it, because the nurse knows the patient better",
          "Refuse, because nurses should not suggest changes",
          "Examine the patient, then call the attending nephrologist and pass on the nurse&rsquo;s observation",
          "Lower it for today only and tell nobody"], 2,
         "Dry weight is part of the prescription. The nurse&rsquo;s observation is useful evidence and should reach the nephrologist, who decides."),
        ("When should you call the attending nephrologist about a patient with chest pain during dialysis?",
         ["After the patient has been transferred", "At the end of the shift, with the other reports",
          "During the first steps of care", "Only if the electrocardiogram is abnormal"], 2,
         "In an emergency, call during the first steps, not after. Someone else can dial while you examine the patient."),
        ("In SBAR, which part contains what you found on examination and what you think is happening?",
         ["Situation", "Background", "Assessment", "Recommendation"], 2,
         "Assessment gives your findings, with numbers, and your working diagnosis."),
        ("What does the published evidence show about SBAR?",
         ["Large randomized trials prove that it lowers mortality",
          "A systematic review found moderate evidence of improved patient safety, especially for telephone calls, with few high-quality studies",
          "It has been shown to be harmful",
          "It has never been studied"], 1,
         "The evidence is moderate and comes mostly from before-and-after studies. It is strongest for telephone communication."),
        ("At which points in a session are problems most likely?",
         ["Only in the first five minutes",
          "Before the start, in the last hour, and when the needles come out",
          "Evenly throughout the session",
          "Only after the patient has gone home"], 1,
         "Assessment before the start finds unstable patients. The last hour brings low pressure and cramps. Disconnection brings bleeding and dizziness on standing."),
        ("Your unit has no written protocol for a situation you face. What is the safest approach?",
         ["Do what you would do on a general ward", "Treat it as a situation that needs a call to the attending nephrologist",
          "Wait until the session ends", "Ask the patient what is usually done"], 1,
         "Without a protocol, give emergency care as any physician would, and call. Do not assume that general ward practice fits a dialysis patient."),
        ("Which of these may a physician on duty change without calling the attending nephrologist?",
         ["The potassium level of the dialysis fluid", "The dry weight",
          "None of these; each is part of the prescription", "The treatment time"], 2,
         "The dialysis fluid, dry weight, and treatment time are all part of the nephrologist&rsquo;s prescription."),
        ("A patient wants to stop the session one hour early. What should you do?",
         ["Refuse and continue the session",
          "Let the patient go without comment",
          "Explain the risk, respect the decision, record the discussion, and inform the nephrologist the same day",
          "Tell the family to persuade the patient"], 2,
         "A patient may decline treatment. Your duties are to make sure the choice is informed, to record it, and to tell the nephrologist."),
        ("You want to share an interesting electrocardiogram from a patient in a private chat group of physicians. What applies?",
         ["It is acceptable because the group is private",
          "It is acceptable if the patient&rsquo;s name is visible so others can follow up",
          "Health information is sensitive personal information; do not share a patient&rsquo;s record or image without consent",
          "It is acceptable if the patient is not told"], 2,
         "The Data Privacy Act of 2012 protects health information wherever it is stored or sent, including personal telephones."),
        ("What is a near miss?",
         ["An error that harmed a patient", "An error that was caught before it reached the patient",
          "A patient who missed a session", "A complaint from a family member"], 1,
         "Near misses are reported because they show where the next harmful error could happen."),
        ("Before you telephone the nephrologist about an overloaded patient, which set of facts should you have ready?",
         ["The patient&rsquo;s home address and occupation",
          "Weight gain, vital signs, access, last session, and latest potassium",
          "The name of the machine and the dialyzer lot number",
          "The patient&rsquo;s insurance details"], 1,
         "These five items answer most of the nephrologist&rsquo;s first questions."),
        ("A nurse says, &ldquo;He is not himself today,&rdquo; about a patient whose vital signs are normal. What should you do?",
         ["Reassure the nurse that the numbers are normal", "Go and examine the patient",
          "Record it and review at the next session", "Ask the patient&rsquo;s family"], 1,
         "An experienced nurse&rsquo;s impression is a clinical finding. Early confusion, infection, and low blood sugar can show before vital signs change."),
        ("Which item is a critical part of the start-of-shift round?",
         ["Checking that the defibrillator, oxygen, suction, and emergency cart are ready",
          "Counting the chairs", "Checking the television", "Reviewing the staff holiday list"], 0,
         "You cannot look for emergency equipment during an emergency."),
        ("You cannot reach the attending nephrologist during an emergency. What do you do?",
         ["Wait and keep trying the same number", "Follow the unit&rsquo;s escalation list to the covering nephrologist or the clinical head while continuing emergency care",
          "Stop all treatment and send every patient home", "Make long-term changes to the prescription yourself"], 1,
         "Every unit should have an escalation list. Emergency care continues while someone else makes the calls."),
    ],
    "terms": [("Physician on duty", "The doctor physically present in the unit while patients are on dialysis."),
              ("Attending nephrologist", "The kidney specialist responsible for a patient&rsquo;s prescription and long-term care."),
              ("Unit protocol", "A written, approved instruction for a defined situation."),
              ("SBAR", "Situation, Background, Assessment, Recommendation: a structure for clinical reports."),
              ("Escalation list", "The order of people to call when the first person cannot be reached."),
              ("Near miss", "An error caught before it reached the patient."),
              ("Dry weight", "The target weight at the end of dialysis, set by the nephrologist."),
              ("Fistula", "A surgical join between an artery and a vein, used for dialysis needles.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "How a unit prepares for and runs a cardiac arrest."),
                 ("hemodialysis-complications.html", "An overview of what can go wrong in a session."),
                 ("dialysis-qapi-vs-cqi.html", "How incident reports feed the unit&rsquo;s quality program.")],
    "calcs": [],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
