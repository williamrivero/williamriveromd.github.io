# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 04: Clinical Oversight: Coverage, Pathways, and Rights. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician leading a short huddle with three nurses before the first shift, a patient list on a clipboard.",
    "objectives": [
        "Explain why patients just back from hospital, or who missed a session, carry the highest risk on any shift.",
        "Decide whether a shift can open by matching competencies, coverage, and acuity, not by counting names on a roster.",
        "Run a five-minute readiness huddle that changes the plan while there is still time.",
        "Design care pathways in which every result, missed session, and referral has a named owner.",
        "Audit delivered dialysis dose against the Kidney Disease Outcomes Quality Initiative (KDOQI) target using a valid post-dialysis sample.",
        "Close a transfer handoff, and protect patient rights: consent, privacy, interpreters, and complaints.",
    ],
    "big": """
{{plain:A roster is a guest list. It tells you who is coming. It does not tell you who can carve the roast, who knows where the fire extinguisher is, or who will look after the guest who arrives unwell.}}
<p>The picture has a limit. Guests can improvise. A nurse who has never been validated on catheter care cannot safely improvise a catheter connection, and a physician who is not reachable cannot assess a patient by hope. Oversight means checking the skills and the coverage behind each name.</p>
{{cards:Key terms for this module|Coverage::The physician and nurse arrangements that guarantee someone qualified can assess, decide, and respond during every shift.|Validated competency::A skill a staff member has been observed doing correctly in your unit, signed and dated.|Readiness huddle::A short, structured meeting before the first connection that reviews risks and changes the plan.|Care pathway::The planned route a patient follows from acceptance to transfer, with owners at each step.|spKt/V::Single-pool Kt/V, a measure of the urea clearance delivered in one session, scaled to body water.|Closed-loop handoff::A handoff in which the receiver repeats back and confirms acceptance.}}
""",
    "case": {"title": "Before the first patient connects", "html": """
<p>It is 5:35 on a Monday at a twelve-station unit in Quezon City. The physician on duty, Dr. Paolo Navarro, calls in sick. His reliever cannot arrive before 8:00. Two patients missed Friday: Mrs. Teresita Villanueva because her son&rsquo;s tricycle broke down, and Mr. Efren Santos, who was in hospital with pneumonia until yesterday. Mrs. Villanueva arrives breathless and cannot lie flat.</p>
<p>The head nurse, Ms. Carmela Reyes, calls you. &ldquo;Eleven patients are here. Three nurses are cleared. Do we start?&rdquo;</p>
""", "questions": ["Who sees Mrs. Villanueva now, and where?",
                  "What must be in place before the rest of the shift begins?",
                  "What do you change in the system after today?"]},
    "sections": [
        ("risk", "Who is at risk", "Why some patients carry the shift&rsquo;s risk", """
<p>Patients do not carry equal risk into a shift. Three groups deserve attention before the first connection.</p>
<p><strong>After the long gap.</strong> Potassium and fluid peak before the first session of the week. In a large United States cohort, deaths and admissions for heart failure, arrhythmia, and myocardial infarction were all more frequent on the day after the two-day gap.[[dch_foley2011]]</p>
<p><strong>After a missed session.</strong> Across 20 countries in the Dialysis Outcomes and Practice Patterns Study (DOPPS), missing at least one session in four months was associated with higher mortality (hazard ratio 1.68) and more hospitalization.[[dch_alsalmi2018]] This is observational; patients who miss sessions differ in other ways. It still tells you who to look at first.</p>
<p><strong>After hospital.</strong> Patients return with new medicines, lost muscle that makes the old dry weight wrong, healing access, and sometimes active infection. Their orders need review before they connect.</p>
{{fig:dch04_sawtooth}}
{{key:The patient who arrives breathless after a missed session is not a scheduling problem. That patient is the emergency of the morning.}}
"""),
        ("coverage", "Coverage", "A full roster is not a safe one", """
<p>Plan coverage around scope, validated competencies, current certifications, patient acuity, and the staffing your licensing rules require. Include breaks, foreseeable absences, and alternates. An incomplete roster should trigger a capacity decision before patients connect, not a scramble after.</p>
<div class="table-wrap"><table>
<thead><tr><th>What the evidence shows</th><th>Design</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>Higher patient-to-nurse ratios and more tasks left undone were associated with more frequent hypotension, skipped and shortened treatments, and complaints[[dch_thomashawkins2008]]</td><td>Survey of nurses, United States</td><td>Cross-sectional; events reported by nurses</td></tr>
<tr><td>Each 10% more hours from highly trained staff was associated with lower odds of patients skipping treatment[[dch_saran2003]]</td><td>DOPPS cohort, seven countries</td><td>Observational</td></tr>
<tr><td>Among 54,141 young adults, units with the most patients per nurse had a 14% lower incidence of transplant[[dch_bicki2024]]</td><td>National cohort, United States</td><td>Observational; large and adjusted</td></tr>
</tbody></table></div>
<p>No trial has tested a staffing ratio in dialysis, and Philippine data were not found. Together these studies support a reasonable inference: staffing and skill mix behave like patient-safety variables. They do not prove that any single ratio is correct.</p>
{{call:Stop and hold the opening of any station whose patients cannot be assessed by a qualified physician or cared for by a validated nurse. Ask the attending nephrologists which waiting patients cannot be delayed. Follow your unit&rsquo;s protocol while you arrange cover.}}
"""),
        ("huddle", "The huddle", "Five minutes that change the plan", """
{{fig:dch04_huddle}}
<p>A huddle is useful only if it can change what happens next. Keep it short, run it at the same time every shift, and use the same list.</p>
{{flow:Readiness huddle|Patients::Back from hospital, missed sessions, new orders, high-risk access, pending critical results.|People::Who is cleared for what today, who is on break when, who holds the emergency role.|Physician::Present, or reachable within the time your protocol sets.|Equipment and water::Released, alarms resolved, emergency cart and defibrillator checked.|Transport::Patients who may not get home, or may not get back on Wednesday.}}
<p>The huddle ends with decisions: who starts first, who waits, who is reassigned, who is assessed before connection, and who calls whom.</p>
"""),
        ("pathways", "Pathways", "Care pathways that do not leak", """
{{fig:dch04_pathway}}
<p>Review clinical governance from acceptance to transfer. Most harm in chronic care comes from things that fall between people: an abnormal result filed without being read, a missed session nobody called about, a referral nobody chased.</p>
<div class="table-wrap"><table>
<thead><tr><th>Joint</th><th>Owner to name</th><th>How you know it worked</th></tr></thead>
<tbody>
<tr><td>Critical laboratory result</td><td>A named clinician for each result type and shift</td><td>Time from result to documented decision</td></tr>
<tr><td>Missed session</td><td>Nurse who calls the patient the same day</td><td>Call recorded; next session confirmed</td></tr>
<tr><td>Access problem</td><td>Access coordinator</td><td>Referral date, procedure date, catheter days</td></tr>
<tr><td>Modality and transplant education</td><td>Attending nephrologist</td><td>Documented shared decision</td></tr>
<tr><td>Nutrition and psychosocial referral</td><td>Dietitian or social worker</td><td>Seen within the set time</td></tr>
</tbody></table></div>
<p>Audit the dose. KDOQI recommends a target single-pool Kt/V of 1.4 per session for patients dialyzed three times a week, with a minimum delivered value of 1.2.[[dch_kdoqi2015]] A dose result is only as good as the post-dialysis sample: a sample drawn at full blood flow after rinse-back dilutes the urea and makes the dose look better than it was. Calculator 10 computes Kt/V and the urea reduction ratio from valid samples.</p>
"""),
        ("handoff", "Handoffs and rights", "The transfer handoff and patient rights", """
{{fig:dch04_handoff}}
<p>During acute deterioration, the unit&rsquo;s response protocol runs the first minutes (the Physician on Duty track covers the clinical steps). Your system question is the handoff. Who calls emergency services and the receiving team? What travels with the patient? Who confirms arrival and outcome?</p>
{{flow:A handoff that closes|Send::Last treatment, current concern, access, relevant orders and results, actions taken, code status.|Confirm::The receiver repeats the key facts and accepts the patient by name.|Record::Receiving clinician, time, transport, and outcome when known.|Follow up::A named person calls for the outcome if it is not received.}}
<p>Rights belong in the same system. Patients should consent to treatment with information they understand, have an interpreter or family translator where needed, know how to complain without fear of losing their slot, and have their information shared only with those who need it for care.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Who sees Mrs. Villanueva now?</strong> She needs a physician&rsquo;s assessment immediately, in a monitored chair or the emergency area, and a potassium level and electrocardiogram. With no physician on site, you or the covering nephrologist must assess her by the fastest safe route; if no physician can reach her within your protocol&rsquo;s time, she goes to the emergency department by ambulance. Breathlessness after a missed session is a medical emergency, not a scheduling question.</p>
<p><strong>What must be in place before the rest of the shift starts?</strong> A physician who can assess and respond, either on site or reachable within the protocol&rsquo;s time, and confirmation that the three cleared nurses can cover the stations to be opened. Mr. Santos&rsquo;s orders need review after his hospitalization. The attending nephrologists decide which waiting patients cannot be delayed.</p>
<p><strong>What changes afterward?</strong> A backup physician list with response times, a rule that a missed session triggers a same-day call, and a huddle item for patients back from hospital. Write the escalation for when the physician on duty is absent, so Ms. Reyes does not have to call you to decide whether to start.</p>
"""],
    "skills": {"title": "Shift readiness and closed-loop escalation",
               "intro": "Lead a readiness huddle with a preceptor and two role players, then manage one deteriorating patient through to a confirmed handoff.",
               "items": [
                   ("Identifies patients after a missed session, after hospital, and with pending critical results.", True),
                   ("Matches assignments to validated competencies, not to names on the roster.", True),
                   ("Confirms physician coverage within the protocol&rsquo;s response time.", True),
                   ("Holds stations that cannot be safely covered and records the decision.", True),
                   ("Asks the attending nephrologists which patients cannot be delayed.", False),
                   ("Activates the emergency pathway for an unstable patient without waiting for the schedule.", True),
                   ("Gives a structured handoff and obtains a repeat-back and acceptance.", False),
                   ("Names an owner for each critical result type.", False),
                   ("Uses only the information needed for care in the handoff.", False),
               ],
               "placement": "For one month, record each shift where coverage was incomplete at opening, what was held, and how long it took to resolve. Use the record to set a backup physician list."},
    "quiz": [
        ("Which patients carry the highest risk at the start of a Monday shift?",
         ["Those who travel farthest", "Those after the long gap, after a missed session, or just back from hospital", "Those on the newest machines", "Those with grafts"], 1,
         "Risk concentrates after the longest gap, missed sessions, and hospitalization."),
        ("In DOPPS, missing at least one session in four months was associated with what?",
         ["Lower mortality", "Higher mortality and more hospitalization", "No difference", "Fewer infections"], 1,
         "Hazard ratio 1.68 for death; observational."),
        ("A roster is fully named but the only catheter-competent nurse is on leave. What is the shift?",
         ["Safe", "Not safe for catheter patients until a validated nurse is assigned", "Safe if the physician is present", "Safe after a briefing"], 1,
         "Competency, not attendance, decides."),
        ("What does KDOQI recommend as the target spKt/V for thrice-weekly hemodialysis?",
         ["1.0", "1.2", "1.4", "2.0"], 2,
         "Target 1.4, with a minimum delivered dose of 1.2."),
        ("A post-dialysis sample is drawn at full blood flow after rinse-back. What happens to the dose result?",
         ["It is accurate", "It looks better than it was", "It looks worse than it was", "It is unchanged"], 1,
         "Diluted urea overstates the dose."),
        ("The physician on duty is absent at opening. What is the first decision?",
         ["Start all patients", "Secure physician coverage within the protocol&rsquo;s time, and hold stations that cannot be covered", "Send everyone home", "Ask the owner"], 1,
         "Coverage comes before connection."),
        ("A patient arrives breathless after a missed session. What is it?",
         ["A scheduling issue", "A medical emergency needing immediate assessment", "A billing issue", "Normal"], 1,
         "Treat it as an emergency."),
        ("What makes a huddle useful?",
         ["Length", "It can change who starts, who waits, and who is reassigned", "A printed agenda only", "The owner&rsquo;s presence"], 1,
         "A huddle that changes nothing is a ritual."),
        ("A critical potassium was filed without anyone being called. What is the system fix?",
         ["A reminder memo", "A named owner for each critical result type with a time to decision", "Remove potassium tests", "Blame the clerk"], 1,
         "Pathways leak where nobody owns the joint."),
        ("When is a transfer handoff complete?",
         ["When the ambulance leaves", "When the receiver repeats back and accepts, and the outcome is recorded", "When the form is printed", "When the family is told"], 1,
         "Close the loop."),
        ("Which study linked patient-to-nurse ratios to transplant access?",
         ["HEMO", "A national United States cohort of young adults", "CONVINCE", "A Philippine trial"], 1,
         "Highest ratios: 14% lower incidence of transplant."),
        ("What is the strength of the evidence that staffing affects dialysis outcomes?",
         ["Randomized trials", "Consistent observational associations", "None", "Expert opinion only"], 1,
         "A reasonable inference, not proof of a ratio."),
        ("Who decides whether a specific waiting patient can be delayed?",
         ["The head nurse", "The attending nephrologist or physician", "The receptionist", "The owner"], 1,
         "It is an individual medical judgment."),
        ("What should a missed session trigger?",
         ["Nothing until the next visit", "A same-day call by a named person and a confirmed next session", "A warning letter", "Removal from the schedule"], 1,
         "Ask what happened, then secure the next treatment."),
        ("Which is a patient right your system must protect?",
         ["Choosing any nurse", "A complaint route that does not threaten the patient&rsquo;s slot", "Free transport", "Unlimited sessions"], 1,
         "Fear of losing a slot silences complaints."),
    ],
    "terms": [("Coverage", "Arrangements that guarantee qualified assessment and response every shift."),
              ("Validated competency", "A skill observed and signed in your unit."),
              ("Readiness huddle", "A short meeting before the first connection that can change the plan."),
              ("Care pathway", "The route from acceptance to transfer, with an owner at each step."),
              ("spKt/V", "Single-pool Kt/V, urea clearance delivered in one session scaled to body water."),
              ("URR", "Urea reduction ratio, the percentage fall in blood urea during a session."),
              ("Closed-loop handoff", "A handoff confirmed by the receiver&rsquo;s repeat-back and acceptance."),
              ("Interdialytic gap", "The time between sessions; the longest is usually over the weekend.")],
    "readings": [("hemodialysis-complications.html", "Complications during a session."),
                 ("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
