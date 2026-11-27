# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 01: Scope, supervision and safe learning.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
RA 2382 Section 11(a) checked against the PRC text; DOH AO 2012-0001 POD ratio (not more than 1:15) checked against the
order's published text; Landrigan 2004, Starmer 2014 and Kennedy 2009 checked against PubMed. No doses. Fictional case."""

MODULE = {
    "image_alt": "A young Filipino intern in a white coat stands at the nurses&rsquo; station of a small dialysis unit, phone to her ear, while a dialysis nurse points to a patient&rsquo;s chair and the wall clock reads a quarter past six.",
    "objectives": [
        "<strong>Intern:</strong> Name your supervising physician on every rotation, list the renal tasks you may do only under direct supervision, and say aloud what you will not do when asked to work beyond your training status.",
        "<strong>Resident:</strong> Verify your appointment, your signatory rights and the escalation chain before you take renal duty or a paid Physician-on-Duty (POD) shift, including the Department of Health (DOH) and Philippine Society of Nephrology (PSN) requirements for the unit.",
        "<strong>Fellow:</strong> Write a supervised learning plan with your attending nephrologist, and keep your training status separate from specialist credentials in every note, signature and introduction.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; knowing what your status lets you do</span>An <strong>intern</strong> owns the history, the intake and output chart, the medicine list, the first recognition of danger and a clear call upward; an intern does not prescribe, sign orders or cover a unit. A <strong>resident</strong> owns supervised plans and orders within the hospital&rsquo;s privileges, and must check before taking any outside renal duty. A <strong>fellow</strong> owns consults, dialysis rounds and teaching, under an attending nephrologist, and must never let a training title stand in for a specialist credential.</div>
{{plain:Think of a jeepney with a student driver. The student holds the wheel, works the pedals and learns the route. A licensed driver sits beside the student, watches the road and can take over at once. The student is truly driving, and still the licensed driver answers for the trip.}}
<p>The picture has a limit. In a jeepney the licensed driver is always in the next seat. In a hospital, supervision is often a phone call away, the supervisor may be asleep or in another building, and the patient cannot see who is accountable. Supervision is not a seat; it is a chain of permissions and a promise that someone with authority will answer in time. Your safety and your patient&rsquo;s safety depend on knowing exactly where that chain is strong and where it has gaps on a given night.</p>
<p>Three separate things decide what you may do. <strong>Licensure</strong> is whether the Professional Regulation Commission (PRC) has registered you as a physician. <strong>Appointment and privileges</strong> are what your hospital or unit has formally allowed you to do there. <strong>Supervision</strong> is who is answerable with you for each task. Completing a course, including this one, changes none of the three.</p>
{{cards:Key numbers and rules|Graduate under training (RA 2382, Section 11(a))::Exempt from the licensure requirement only when serving without professional fee and under the direct supervision and control of a registered physician|POD ratio (DOH AO 2012-0001)::Not more than one POD to 15 hemodialysis patient stations|Long shifts and errors (Landrigan 2004, randomized intensive care unit (ICU) study)::Serious errors 136.0 versus 100.1 per 1,000 patient-days on a schedule with shifts of 24 hours or more|Structured handoff (I-PASS, 9 hospitals)::Medical errors 24.5 to 18.8 per 100 admissions after the program (prospective intervention study, not randomized)}}
<p>Most nights on renal duty pass within everyone&rsquo;s authority. A few create pressure to step outside it: a late POD, a nurse who needs a signature, an order sent by chat. Your work is to know your limits before the night starts, to stay at the bedside doing what you are allowed to do, and to call the person with authority early enough that nothing waits on paperwork.</p>
""",
    "case": {"title": "The POD is late", "html": """
<p>Saturday, 6:10 a.m., a freestanding hemodialysis unit in Malolos, Bulacan. Dr. Bea Santiago is a post-graduate intern on her community rotation. She came to observe the morning shift. The physician on duty, who was due at 6:00, has texted that he is stuck in traffic on the North Luzon Expressway and will arrive &ldquo;around 7.&rdquo; Twelve patients are already connected.</p>
<p>The charge nurse, Ms. Liza Pangilinan, is calm but busy. She asks Dr. Santiago to &ldquo;just watch the unit for now, Doc, and sign the treatment sheets so we can start the last two.&rdquo; At 6:25, Mr. Romeo Dizon, 67, in chair 4, says he feels lightheaded. His blood pressure has fallen from 150/88 to 94/60. The nurse has laid him back and stopped fluid removal under the unit&rsquo;s protocol. The unit&rsquo;s attending nephrologist and medical director, Dr. Carmela Reyes, is at home in Quezon City, and her number is on the wall.</p>
""", "questions": [
        "What may Dr. Santiago do in this unit this morning, and what must she decline?",
        "Whom does she call, in what order, and what does she say?",
        "What should happen afterward so the unit and the intern learn from the morning?"]},
    "sections": [
        ("authority", "Who may do what", "Who may do what: licensure, privileges and supervision", """
<p>Start with the law. The Medical Act of 1959, Republic Act (RA) 2382, defines the practice of medicine broadly: examining, diagnosing, treating or prescribing for any human condition, whether or not a fee is paid. Section 11(a) exempts a medical student enrolled in an approved school, or a graduate under training, but only on two conditions: the service is given without professional fee, and it is given <em>under the direct supervision and control of a registered physician</em>.[[ntr01_1]] That clause is the legal floor for every post-graduate intern in the country. It is permission to learn by doing, tied to a supervisor; it is not permission to stand alone.</p>
<p>The chain of reasoning is simple. Because the intern is not yet licensed, the law borrows the license of the supervising physician. Because the license is borrowed, the supervisor must be able to see and control what the intern does. Because control is required, an intern who works where no supervisor can see or reach is working outside the exemption, whatever the staff ask and however good the intent.</p>
<p>A resident is a licensed physician, so the law no longer limits what a resident may do in general. The hospital does. Your appointment letter and the privileges your department grants say which orders you may write, which procedures you may do alone, and which need an attending present. A fellow has the same license and wider privileges, still under a named attending nephrologist. None of these permissions travel with you to another facility.</p>
{{fig:ntr01_a}}
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What sets your authority</th><th>What you may usually do on renal duty</th><th>What you do not do on this course&rsquo;s authority</th></tr></thead>
<tbody>
<tr><td>Post-graduate intern</td><td>RA 2382 Section 11(a); your hospital&rsquo;s internship rules</td><td>History, examination, intake and output, medicine lists, supervised notes, presenting, first recognition of danger, calling for help</td><td>Prescribe, sign orders or treatment sheets as the physician, certify forms, cover a dialysis unit</td></tr>
<tr><td>Resident (internal medicine or pediatrics)</td><td>PRC license; appointment and departmental privileges</td><td>Admit, co-manage, write orders within privileges, supervise interns</td><td>Take freestanding-unit POD duty without checking the unit&rsquo;s DOH and PSN requirements</td></tr>
<tr><td>Nephrology fellow</td><td>PRC license; fellowship appointment; privileges for consults, dialysis rounds and procedures</td><td>Consults, dialysis prescriptions as delegated, procedures where privileged, teaching</td><td>Sign as the attending, or introduce yourself as a specialist</td></tr>
<tr><td>Attending nephrologist</td><td>License, specialty credentials, medical staff appointment</td><td>Final responsibility for the plan and the patient</td><td>&mdash;</td></tr>
</tbody></table></div>
<h3>Titles that confuse patients and staff</h3>
<p>In the PSN, &ldquo;Fellow&rdquo; is a membership category defined by the society&rsquo;s constitution, granted to qualified nephrologists.[[ntr01_4]] A trainee in a nephrology fellowship is not a &ldquo;Fellow of the PSN.&rdquo; Introduce yourself as &ldquo;the nephrology fellow in training&rdquo; or &ldquo;the resident on the renal service,&rdquo; and sign notes the same way. Patients and their families make decisions based on who they think is advising them.</p>
<h3>Signatures carry weight</h3>
<p>A signature says that the signer did, saw or decided what the document states. A treatment sheet signed as the physician tells the next reader that a physician assessed the patient and ordered the treatment. A claim form tells the payer that a named, accredited physician gave the care. Signing for someone else, signing before you have seen the patient, or signing a form you are not entitled to sign turns a paperwork shortcut into a false record. When asked, say: &ldquo;I can examine him and report to Dr. Reyes now. I cannot sign as the physician.&rdquo;</p>
<p>Orders sent by chat or text are now common. They are real orders only when your institution&rsquo;s policy accepts them, when they come from a physician entitled to give them, and when they are written into the chart, read back and countersigned as the policy requires. Keep the message, write the order exactly as sent, and record who sent it and when.</p>
{{key:Before any renal duty, answer three questions in writing: Am I licensed for this? Has this facility given me the privilege? Who is supervising me tonight, and how do I reach them?}}
"""),
        ("pod-shift", "The moonlighting shift", "The moonlighting shift: verify before you accept", """
<p>Many residents and fellows work paid shifts as the physician on duty in freestanding hemodialysis units. The work is valuable, the pay helps, and the units need you. It is also the setting where training status, licensure and regulation collide most often, because you are alone, at night or at dawn, with patients connected to machines.</p>
<p>The DOH regulates dialysis facilities through Administrative Order (AO) 2012-0001. The order lists the qualifications, duties and responsibilities of the POD in a hemodialysis center, sets the ratio of POD to hemodialysis patient stations at not more than 1:15, and requires each shift to have nursing staff trained in Advanced Cardiovascular Life Support (ACLS).[[ntr01_2]] The PSN&rsquo;s 2024 hemodialysis guidelines describe what the society expects of attending nephrologists and PODs, including current ACLS training and a POD course conducted or accredited by the society.[[ntr01_3]] Regional DOH inspection tools and later issuances may add requirements, and units interpret them locally. That is why the rule is to verify, not to assume.</p>
<p>The reasoning runs like this. The unit&rsquo;s license depends on staffing the shift with a qualified POD. If you are not qualified under the order and the PSN guidelines as the unit applies them, the unit is unlicensed for that shift, your patients lack the physician the regulation intended, and you carry the risk personally. A residency program&rsquo;s approval to moonlight is not the same as meeting the unit&rsquo;s regulatory requirements.</p>
{{cards:Before you accept a POD shift|License::Your PRC license is current and you can show it.|Qualification::The unit has checked your training route against DOH AO 2012-0001 and the PSN 2024 guidelines, and recorded it.|Life support::Your ACLS card is current.|Program::Your training program allows outside duty, in writing, and the hours fit its rules.|Attending::You know the name and number of the attending nephrologist for each patient and the medical director.|Protocols::You have read the unit&rsquo;s standing protocols for low blood pressure, chest pain, fever, bleeding and emergencies.|Ratio::The number of stations you will cover does not exceed one POD to 15.}}
<p>Payment rules add a second layer. The Philippine Health Insurance Corporation (PhilHealth) hemodialysis benefit covers up to 156 sessions a year for registered patients, and PhilHealth announced a rate of PHP 6,350 per session effective October 9, 2024.[[ntr01_8]][[ntr01_9]] Claims depend on correct documentation by the right physicians. A POD does not certify what the attending nephrologist must certify, and an unqualified POD can put a unit&rsquo;s claims at risk. Confirm current rules with the unit on the date of service.</p>
<p>Some requests should stop you. &ldquo;Just be here, the nurses will run it.&rdquo; &ldquo;You don&rsquo;t need to call the nephrologist, she doesn&rsquo;t like being disturbed.&rdquo; &ldquo;Sign the sessions from last week, the other doctor forgot.&rdquo; Each one asks you to lend your name to care you did not give or cannot supervise. Decline politely and call the medical director.</p>
<p>The Physician on Duty track on this site teaches the clinical work of the shift in detail; this module only asks whether you should be there at all. Read its first module before your first shift.</p>
<p><strong>For interns:</strong> you may never be the POD. You may observe a shift with a qualified POD present. If you arrive and there is no POD, you are a visitor, not the coverage.</p>
{{key:A program&rsquo;s permission to moonlight is not a unit&rsquo;s permission to staff you. Verify your eligibility for that unit, in writing, before the first shift.}}
"""),
        ("escalate", "Escalate, don&rsquo;t abandon", "Escalate without abandoning care", """
<p>Declining a task you are not authorized to do is not the same as walking away. The patient in front of you still needs whatever help you can lawfully give. The skill is to do two things at once: stay at the bedside within your scope, and bring the person with authority into the room by phone or in person.</p>
<p>Escalation fails for predictable reasons. Kennedy and colleagues observed and interviewed 124 members of internal medicine and emergency teams in three Canadian teaching hospitals. Trainees weighed not only the clinical question but also the supervisor&rsquo;s availability and approachability, and their own wish to look competent and independent. They saw frequent requests for help as a threat to their credibility, and they delayed calls, saved them for &ldquo;opportune moments,&rdquo; or built a case before calling.[[ntr01_7]] This was a qualitative study; it describes why trainees hesitate, not how often harm follows. The lesson is that your own reluctance is expected, and you should plan against it.</p>
<div class="table-wrap"><table>
<thead><tr><th>What pulls you away from calling</th><th>What it costs the patient</th><th>What you do instead</th></tr></thead>
<tbody>
<tr><td>&ldquo;I don&rsquo;t want to wake her for something small.&rdquo;</td><td>A delay while a small problem grows</td><td>Use the unit&rsquo;s call criteria. If the criteria are met, the call is expected, not optional</td></tr>
<tr><td>&ldquo;I should be able to handle this.&rdquo;</td><td>Care beyond your training, given alone</td><td>Separate what you can do (assess, monitor, follow protocol) from what needs authority (orders, decisions to stop or transfer)</td></tr>
<tr><td>&ldquo;The paperwork isn&rsquo;t clear about who is responsible.&rdquo;</td><td>Nobody acts while roles are argued</td><td>Treat the emergency first under protocol; settle the paperwork after</td></tr>
<tr><td>&ldquo;He didn&rsquo;t answer, so I&rsquo;ll wait.&rdquo;</td><td>A silent chain</td><td>Go to the next name on the escalation list and keep going until someone answers</td></tr>
</tbody></table></div>
{{fig:ntr01_b}}
<h3>The call itself</h3>
<p>Use a structure your listener expects. SBAR (situation, background, assessment, recommendation) suits an urgent call: &ldquo;This is Dr. Santiago, intern, at the Malolos unit. Mr. Dizon in chair 4 has a blood pressure of 94/60 from 150/88, with lightheadedness, one hour into his session. He is 67, diabetic, with no chest pain. The nurse has laid him back and stopped fluid removal per protocol. The POD has not arrived. I am not able to give orders. I need you to give the nurse instructions and tell me whether to call an ambulance.&rdquo; Then read back what you hear.</p>
<p>For handoffs, structure reduces errors. In the I-PASS study (the mnemonic stands for illness severity, patient summary, action list, situation awareness and contingency planning, and synthesis by receiver), a resident handoff program in nine hospitals (standardized mnemonic, training, faculty observation) was followed by fewer medical errors, from 24.5 to 18.8 per 100 admissions, and fewer preventable adverse events, from 4.7 to 3.3 per 100 admissions, with no change in handoff duration or workflow.[[ntr01_6]] It compared periods before and after, not randomized groups, so it shows an association, not proof. It is still the best multicenter evidence that how we hand over matters.</p>
<h3>When the chain is silent</h3>
<p>Every unit should have a written escalation list: attending nephrologist, medical director, the nearest hospital emergency room for transfer. If the first name does not answer in a few minutes, go to the next. If none answers and the patient is deteriorating, the unit&rsquo;s emergency protocol and transfer to a hospital proceed. Write down each call: time, name, what you said, what you were told.</p>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>you are asked to cover, sign or order beyond your training status or privileges;</li><li>a patient&rsquo;s blood pressure, breathing, consciousness or rhythm changes and no qualified physician is present;</li><li>a protocol step has been taken and the patient has not recovered;</li><li>the POD or supervising physician is absent at the start of a shift.</li></ul>Keep helping within your scope while you call.}}
{{key:Say what you can do, say what you cannot, and call the person who can, in the same minute. Never let a disagreement about roles delay the first look at a sick patient.}}
"""),
        ("learning", "Plan learning, fatigue, speaking up", "Plan your learning, protect against fatigue, and speak up", """
<p>Supervision is also how you learn. A rotation without a plan becomes a series of nights. A plan turns the same nights into skills you can name and a supervisor can sign.</p>
<h3>A supervised learning plan</h3>
<p>At the start of each rotation, write three to five goals with your supervisor, each tied to something observable: &ldquo;Present a renal consult with a timeline and a problem representation (Module 3) and get feedback on two.&rdquo; &ldquo;Examine a urine sediment with the fellow (Module 4).&rdquo; &ldquo;Lead the handoff of the renal service using I-PASS twice a week.&rdquo; Agree how you will be observed, and record the feedback. Fellows should do the same with the program director, and add teaching goals for the residents and interns below them.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Example goal for one month</th><th>How it is observed</th></tr></thead>
<tbody>
<tr><td>Intern</td><td>Present three renal admissions with a complete medicine list, including herbal products</td><td>Resident or fellow listens and gives feedback on the spot</td></tr>
<tr><td>Resident</td><td>Write five supervised AKI plans with monitoring and escalation triggers</td><td>Fellow reviews the note before it is final</td></tr>
<tr><td>Fellow</td><td>Run the renal consult service for a week and teach one sediment session</td><td>Attending observes one consult and one teaching session</td></tr>
</tbody></table></div>
<h3>Fatigue is a safety hazard, not a character test</h3>
<p>The mechanism is ordinary physiology. Sleep loss slows reaction time, narrows attention and weakens working memory. A tired brain anchors on the first explanation and misses the second. Landrigan and colleagues randomized interns in two ICUs between a traditional schedule with extended shifts of 24 hours or more every other shift and a schedule that eliminated extended shifts. On the traditional schedule, interns made 35.9% more serious medical errors (136.0 versus 100.1 per 1,000 patient-days) and 5.6 times as many serious diagnostic errors (18.6 versus 3.3 per 1,000 patient-days).[[ntr01_5]] The study was small, set in two US units and over two decades old, and it measured errors rather than patient deaths. It still gives a direct, randomized link between long shifts and error.</p>
<p>A moonlighting shift after a 24-hour hospital duty stacks fatigue on fatigue. If your program&rsquo;s duty-hour rules would be broken by the shift, do not take it. If you are too tired on arrival, say so to the medical director before the shift starts, not after an error.</p>
<h3>Learning from synthetic and de-identified cases</h3>
<p>Keep teaching material out of personal chats and public groups. Use fictional cases like those in this course, or de-identified records within your institution&rsquo;s approved system. A photograph of a monitor or a laboratory slip in a group chat can identify a patient by the date, the bed and the name in the corner.</p>
<h3>Speaking up</h3>
<p>You will see unsafe things: a unit running without a POD, an order that seems wrong, a supervisor who will not come. Raise it first with the person, then with your chief resident or program director, then through the institution&rsquo;s reporting channel. Report the event, not the person, and write what you saw. Units that learn from reports become safer; units that punish them stay quiet until someone is hurt.</p>
{{key:A rotation is finished when your goals are signed, not when the calendar says so. Plan the learning, protect your sleep, and report what is unsafe through the channel that can fix it.}}
"""),
    ],
    "debrief": ["""
<p><strong>What she may do.</strong> Dr. Santiago is a graduate under training. RA 2382 lets her serve only under the direct supervision and control of a registered physician, and no physician is present. She may stay, help the nurse within the unit&rsquo;s protocol, examine Mr. Dizon, count his pulse, ask about chest pain and breathlessness, and check the access and lines. She must decline to &ldquo;watch the unit&rdquo; as its physician, to sign treatment sheets, or to authorize starting the last two patients. She says so kindly and at once: &ldquo;I can help assess patients and call Dr. Reyes. I cannot be the doctor on duty or sign.&rdquo;</p>
""", """
<p><strong>Whom she calls.</strong> First Dr. Reyes, the attending nephrologist and medical director, because she has authority over the unit and the patients. She uses SBAR: who she is and her status, Mr. Dizon&rsquo;s pressure and symptoms, what the nurse has done, that no POD is present, and what she needs (instructions to the nurse and a decision about starting the remaining patients). If Dr. Reyes does not answer within a few minutes, she goes to the next name on the escalation list, and if Mr. Dizon does not recover, the unit&rsquo;s emergency and transfer protocol proceeds. She calls the late POD too, so he knows the unit is waiting. She writes down every call.</p>
""", """
<p><strong>Afterward.</strong> Dr. Reyes asks the charge nurse to hold new connections until a qualified physician is present, gives the nurse instructions for Mr. Dizon, who recovers to 128/76, and arrives herself by 7:20. Later that week the unit reviews the morning: a written backup plan for a late POD, a phone tree on the wall, and a rule that observers are never counted as coverage. Dr. Santiago tells her internship coordinator what happened. Her rotation goal for the month becomes &ldquo;present one SBAR call to the attending for feedback.&rdquo; Nobody is blamed for asking; the system is fixed so the next intern is not asked.</p>
"""],
    "skills": {"title": "Scope and escalation map",
               "intro": "Complete with your supervisor before your first renal duty or POD shift. Sign-off is local.",
               "items": [
                   ("States own training status, license status and the name of the supervising physician for the rotation", False),
                   ("Lists the renal tasks allowed without direct supervision and those that need it, as the institution defines them", False),
                   ("Shows the written escalation list for the service or unit, with names and working numbers", False),
                   ("Delivers a simulated SBAR call to an attending about a deteriorating patient and reads back the instructions", False),
                   ("For residents and fellows: shows the written record that the unit verified POD eligibility against DOH AO 2012-0001 and the PSN 2024 guidelines", False),
                   ("Writes a one-month supervised learning plan with three observable goals", False),
               ],
               "placement": "Any renal rotation, dialysis unit or simulation; repeat when changing institutions"},
    "quiz": [
        ("An intern is asked by a dialysis nurse to sign the physician&rsquo;s section of treatment sheets because the POD is late. What does RA 2382 Section 11(a) mean for this request?",
         ["The intern may sign if the nurse countersigns",
          "The intern may sign because the intern holds a medical degree",
          "The intern serves lawfully only under the direct supervision and control of a registered physician, so the intern should decline and call the supervising physician",
          "The intern may sign if the sessions are covered by PhilHealth"], 2,
         "Section 11(a) exempts a graduate under training only when serving without professional fee and under the direct supervision and control of a registered physician. With no physician present, signing as the physician falls outside the exemption. A nurse&rsquo;s countersignature does not supply a physician&rsquo;s supervision."),
        ("A second-year internal medicine resident is offered a paid POD shift at a freestanding unit. Her program allows moonlighting. What should she confirm before accepting?",
         ["Nothing further; the program&rsquo;s approval is sufficient",
          "That the unit has verified her eligibility against DOH AO 2012-0001 and the PSN 2024 guidelines, that her ACLS is current, and who the attending nephrologist and medical director are",
          "Only that the pay is above the local rate",
          "Only that she has completed this Academy track"], 1,
         "The unit&rsquo;s license depends on a qualified POD under the DOH order as the unit applies it, with the PSN guidelines setting society expectations such as ACLS and a POD course. A program&rsquo;s permission is about training rules, not the unit&rsquo;s regulatory staffing. Completing this course confers no eligibility."),
        ("A first-year nephrology fellow is introduced to a family as &ldquo;Fellow of the PSN, the kidney specialist.&rdquo; What should the fellow do?",
         ["Accept the title, because the fellow is in a PSN-accredited program",
          "Correct it: explain that he is a nephrology fellow in training working under the attending nephrologist, and sign notes the same way",
          "Ask the family to wait for the attending before speaking",
          "Say nothing, to avoid embarrassing the referring doctor"], 1,
         "In the PSN, Fellow is a membership category for qualified nephrologists, not a training status. Families decide based on who they think is advising them. The fellow can still help; he simply states his status accurately."),
        ("At 2 a.m. a resident covering the renal ward calls the attending nephrologist about a patient with a potassium of 7.2 mmol/L and ECG changes. There is no answer after two attempts over five minutes. What is the best next step?",
         ["Wait 30 minutes and try again",
          "Start the hospital&rsquo;s hyperkalemia protocol within privileges and call the next person on the escalation list now",
          "Leave a chat message and continue rounds",
          "Ask the intern to decide"], 1,
         "A silent chain is a reason to move down the list, not to wait. Emergency care within privileges and protocol proceeds while escalation continues. A chat message without acknowledgment does not transfer responsibility, and an intern cannot carry the decision."),
        ("A fellow has worked 26 hours in the hospital and is offered a 12-hour POD shift starting in one hour. What does the evidence on extended shifts suggest?",
         ["Experienced fellows are immune to fatigue effects",
          "Fatigue mainly affects procedures, not diagnosis",
          "A randomized ICU study found more serious medical errors and 5.6 times as many serious diagnostic errors on schedules with shifts of 24 hours or more, so the fellow should decline",
          "Coffee fully offsets sleep loss"], 2,
         "Landrigan and colleagues found 136.0 versus 100.1 serious errors per 1,000 patient-days and serious diagnostic errors of 18.6 versus 3.3 per 1,000 patient-days. The study measured errors, not deaths, and was in interns, but nothing suggests seniority removes the effect of sleep loss."),
    ],
    "terms": [
        ("ACLS", "Advanced Cardiovascular Life Support"),
        ("AO", "Administrative Order"),
        ("DOH", "Department of Health"),
        ("ECG", "Electrocardiogram"),
        ("ICU", "Intensive care unit"),
        ("I-PASS", "Illness severity, Patient summary, Action list, Situation awareness and contingency planning, Synthesis by receiver (handoff mnemonic)"),
        ("PhilHealth", "Philippine Health Insurance Corporation"),
        ("POD", "Physician on duty"),
        ("PRC", "Professional Regulation Commission"),
        ("PSN", "Philippine Society of Nephrology"),
        ("RA", "Republic Act"),
        ("SBAR", "Situation, background, assessment, recommendation"),
    ],
    "readings": [
        ("physician-on-duty-01-your-role-on-the-dialysis-floor.html", "Physician on Duty, Module 1: Your role on the dialysis floor"),
        ("attending-nephrologist-01-taking-responsibility.html", "Attending Nephrologist, Module 1: Taking responsibility"),
        ("dialysis-clinical-head-01-governance-and-appointment.html", "Dialysis Clinical Head, Module 1: Governance and appointment"),
    ],
    "calcs": ["calc-dialysis-shift-coverage.html", "calc-dialysis-continuity-planner.html", "calc-qsofa-sofa.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
