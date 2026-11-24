# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 01: Your Role on the Dialysis Floor. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse briefing four nurses at the entrance of a hemodialysis unit before the first patients arrive.",
    "objectives": [
        "Describe what a head nurse decides, and what belongs to the attending nephrologist, the clinical head, and the technical staff.",
        "Explain why a small process failure becomes a clinical event faster in a dialysis unit than on a general ward.",
        "Check the five gates before a shift opens, and hold the stations that fail one.",
        "Match each qualification on the roster to the rule that requires it.",
        "Summarize what the research shows about nurse staffing and experience, and how strong that evidence is.",
        "Build an evidence register that an inspector or a payer can follow.",
    ],
    "big": """
{{plain:Think of the unit as a machine with a control loop. Policies are the limits. Staff observations are the sensors. You are the part that compares the two every shift and acts when a reading crosses a limit.}}
<p>The picture has a limit. A machine acts on its own. A person acts only with the authority, the information, and the willingness to stop the line. This module is about giving you all three.</p>
{{cards:Key terms for this module|Head nurse::The registered nurse who plans, organizes, and evaluates nursing care across the shifts of a dialysis unit.|Attending nephrologist::The kidney specialist responsible for each patient&rsquo;s dialysis prescription and long-term care.|Clinical head::The physician who authorizes the unit&rsquo;s clinical policies and leads its quality program with the head nurse.|Independent nurse::A nurse with site competency sign-off to care for patients without direct supervision. Only independent nurses count toward the staffing rule.|ACLS::Advanced cardiovascular life support. DOH expects at least one nurse with a current certificate on every shift.|Technical release::A signed record that water or a machine passed its tests and may be used.|Evidence register::A list of every requirement, the document that proves it, who owns it, and when it expires.}}
{{flow:Three habits this module teaches|Check before you open::Five gates, every shift, before the first connection.|Hold, do not hope::A failed gate becomes a named hold with an owner.|Call the right person::The decision belongs to whoever owns it. Your job is to make sure they know.}}
""",
    "case": {"title": "Two problems before six", "html": """
<p>It is 5:40 on a Monday morning at a twelve-station freestanding unit. You are the head nurse. Three nurses are rostered. While checking the roster, you see that the ACLS certificate of Mr. Carlo Reyes, the only nurse on the shift with one, expired last week. The technician, Mr. Dante Flores, tells you that machine 7 was repaired on Saturday, but the release sheet is not signed.</p>
<p>The administrator, Ms. Liza Ramos, arrives at 5:50. &ldquo;Twelve patients are outside. Some came by tricycle from two towns away. Can we just start and sort the paperwork later?&rdquo;</p>
""", "questions": ["What do you say at the huddle at 5:55?",
                  "Who can resolve each of the two problems, and who decides which patients wait?",
                  "What will you write down, and where?"]},
    "sections": [
        ("why", "Why it matters", "Why small failures become clinical events here", """
<p>Every session, a patient sends their blood through a circuit outside the body several times over, across a thin membrane bathed in about 120 liters of fluid your unit prepared. The patient cannot excrete potassium, cannot shed two days of water, and often cannot hold their blood pressure when fluid comes off quickly. Module 2 explains each of these.</p>
<p>That is why a missing check matters more here than on a ward. An untested water system, an unreleased machine, a needle under a blanket, or a shift with no one trained in advanced life support each removes one layer between a fragile physiology and harm.</p>
{{fig:hn01_huddle}}
<p>The workload is growing. Press reports citing national registry figures put 64,845 Filipinos on dialysis in 2024, up 22% from 53,296 in 2023. Press reports also quoted PhilHealth as paying about PHP 27 billion for more than 2 million hemodialysis claims in the first half of 2025. More chairs, more new staff, and more payer review all land on the nurse who runs the floor. These figures come from news reports, not from the registry itself.</p>
{{key:A dialysis unit is safe because many small checks hold at once. Your job is to know, every morning, which ones are holding.}}
"""),
        ("evidence", "What the evidence shows", "What the research shows about nurses and outcomes", """
<p>No trial has tested what happens when a unit has a good head nurse. What exists is a set of observational studies that link the things a head nurse controls to how patients fare.</p>
<div class="table-wrap"><table>
<thead><tr><th>What was studied</th><th>What was found</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>Experience mix, Korea</td><td>Units where every nurse had at least two years of dialysis experience met more targets for dose, blood pressure, and albumin than units where fewer than half did[[hn_jeong2023]]</td><td>Cross-sectional. Better-resourced units may both keep nurses and have healthier patients</td></tr>
<tr><td>Trained staff hours, 7 countries</td><td>A higher share of highly trained staff hours was associated with fewer skipped sessions. Skipping was associated with 30% higher mortality[[hn_saran2003]]</td><td>Cohort</td></tr>
<tr><td>Workload, United States</td><td>More patients per nurse and more care left undone were associated with more adverse events reported by nurses[[hn_thomashawkins2008]][[hn_thomashawkins2020]]</td><td>Cross-sectional. Events were reported by the nurses, not measured</td></tr>
<tr><td>Staffing and transplant, United States</td><td>Among 54,141 young patients, units with the most patients per nurse had 14% lower incidence of transplant[[hn_bicki2024]]</td><td>Large cohort</td></tr>
</tbody></table></div>
<p>Philippine data on staffing and outcomes were not found. Taken together, these studies support a reasonable inference: the mix of experience and the workload on the floor are patient-safety variables. They do not prove that any particular ratio is correct.</p>
"""),
        ("rules", "The rules", "Which rule governs what", """
<p>Your unit answers to several authorities at once. Each governs a different question. Keep them apart, because a document that satisfies one does not satisfy another.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Source</th><th>What to keep in the register</th></tr></thead>
<tbody>
<tr><td>May this person practice and supervise nursing?</td><td>Philippine Nursing Act, sections 28 and 29[[hn_ra9173]]</td><td>License, how HR classifies the post, management units, service record</td></tr>
<tr><td>May this facility operate, and with what nursing cover?</td><td>DOH licensing order for dialysis facilities[[doh2012]]</td><td>Renal dialysis training certificates, basic life support for all, at least one nurse per shift with current ACLS, a roster showing one nurse per four stations</td></tr>
<tr><td>Is the water fit for dialysis?</td><td>DOH water order[[hn_doh2013]]</td><td>Adopted limits, test logs, corrective actions, release decisions</td></tr>
<tr><td>What should a head nurse be and do?</td><td>PSN standards for hemodialysis clinics[[psn2024]]</td><td>Structured renal dialysis training of at least three months, at least two years as a dialysis nurse, evidence of the duties</td></tr>
<tr><td>Will the session be paid, and to what standard?</td><td>PhilHealth circulars[[hn_philhealth2024]][[hn_philhealth2024q]]</td><td>Dialysis database registration, agreement forms, session counts, the quality tracer</td></tr>
</tbody></table></div>
<p>Older PhilHealth circulars listed head nurse credentials for freestanding clinics. Whether those clauses still apply could not be confirmed from public documents. Ask your regional office in writing and file the answer.</p>
<p>A certificate proves that someone attended a course. It does not prove they can do the task in your unit. Competence is shown by watching the nurse work, giving feedback, and recording a date to check again. Keep certificates and competency sign-offs in separate columns.</p>
"""),
        ("decides", "Who decides", "What is yours to decide, and what is not", """
<p>You will be asked to decide things that are not yours. The answer is never to refuse to help. It is to get the decision to the person who owns it, quickly, with the facts.</p>
{{fig:hn01_decides}}
<div class="table-wrap"><table>
<thead><tr><th>Who</th><th>Decides</th><th>Your part</th></tr></thead>
<tbody>
<tr><td>Attending nephrologist or physician on duty</td><td>Anything about one patient: the prescription, the dry weight, whether a patient can safely wait, transfer</td><td>Give the facts, ask for a decision, record it</td></tr>
<tr><td>Clinical head</td><td>Unit policies and protocols, the quality program</td><td>Bring problems that affect several patients or the whole unit</td></tr>
<tr><td>Water and biomedical staff</td><td>Testing, repair, and technical release</td><td>Confirm that the signed release exists before a station is used</td></tr>
<tr><td>Nursing administration and HR</td><td>Hiring, rosters, relievers, discipline</td><td>Escalate gaps you cannot fill</td></tr>
<tr><td>Head nurse</td><td>Nursing assignments, holding a station, stopping the opening, coaching, the evidence register</td><td>&mdash;</td></tr>
</tbody></table></div>
<p>The rule for this series is the same in every module. <strong>Follow your unit&rsquo;s protocol, and ask the attending nephrologist for guidance.</strong> Where a limit is not written down, do not invent one. Ask.</p>
{{key:You cannot release a machine, change a prescription, or decide that a patient can wait. You can, and must, stop anything from starting until the people who can have done so.}}
"""),
        ("gates", "Five gates", "Five gates before the first connection", """
<p>Every shift, before the first patient connects, check five gates. Do it in the same order each time, so that nothing is skipped on a busy morning.</p>
{{fig:hn01_gates}}
{{flow:The five gates|Nurses cleared::Count only nurses with site sign-off to work alone. Stations planned divided by four, rounded up, is the minimum.|ACLS cover::At least one nurse on the shift with a current certificate.|Physician reachable::The physician on duty is present, or the attending nephrologist answers.|Water and machines released::Today&rsquo;s water tests are within limit and signed. Every machine back from repair has a signed release.|Emergency cart ready::Checked, stocked, sealed, and the defibrillator tested.}}
<p>When a gate fails, the stations that depend on it stay closed. Say it aloud at the huddle, name the owner, and write down the time. A hold is temporary. Hoping is not a plan.</p>
{{formula:<strong>Arithmetic illustration.</strong> 12 stations &divide; 4 = 3 nurses with sign-off. With 2, you may open 8 stations on nursing grounds. A missing ACLS nurse is a separate gate that the third nurse may or may not fill.}}
{{call:Stop and call nursing administration and the clinical head when a gate cannot be closed before the scheduled start. Ask the attending nephrologist or physician on duty which waiting patients cannot safely be delayed. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("register", "The register", "The evidence register", """
<p>An inspector, a payer, or a lawyer will ask the same question in different words: show me. The evidence register is how you answer without a scramble.</p>
<div class="table-wrap"><table>
<thead><tr><th>Column</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Requirement</td><td>At least one nurse with current ACLS per shift</td></tr>
<tr><td>Source and version</td><td>DOH licensing order and the current assessment tool</td></tr>
<tr><td>Owner</td><td>Head nurse</td></tr>
<tr><td>Where the evidence is</td><td>Personnel file, roster folder</td></tr>
<tr><td>Date checked</td><td>2026-11-23</td></tr>
<tr><td>Expiry</td><td>Certificate dates, by nurse</td></tr>
<tr><td>Follow-up</td><td>Renewal booked for two nurses in January</td></tr>
</tbody></table></div>
<p>Start with personnel files, roster cover, emergency and referral documents, approved policies, water records, and quality meeting minutes. Review the register monthly, and look ahead ninety days for anything about to expire.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What do you say at the huddle?</strong> Name both problems in plain words. &ldquo;We have no nurse with current ACLS this morning, and machine 7 has no signed release. We will not open the stations that depend on either until they are fixed.&rdquo; Then give each a name and a time. Machine 7 is tagged out of service. You are calling a reliever with a current certificate.</p>
<p><strong>Who resolves what?</strong> Mr. Flores or the biomedical lead signs the release after the checks, or the machine stays out. Nursing administration or the reliever list fills ACLS cover. You cannot do either yourself. Which of the twelve patients can wait, and for how long, is a medical decision. Mrs. Ramos is right that patients have travelled far, which is why you call the physician on duty now. Monday patients are at their highest risk of the week (Module 2), so the physician may want some of them to start first once cover is secured.</p>
<p><strong>What do you write?</strong> The time each problem was found, who was called and when, the decision made, and when each gate closed. Update the evidence register: the expired certificate is a gap in the personnel file that should have been caught by the ninety-day look-ahead. Tell the waiting patients what is happening and roughly how long it will take. If the reliever declines, the decision about capacity moves up the escalation list. It does not turn into &ldquo;start anyway.&rdquo;</p>
"""],
    "skills": {"title": "Opening-gate check and huddle",
               "intro": "Lead the pre-opening check and huddle on a real or simulated morning while your facilitator observes.",
               "items": [
                   ("Counts only nurses with site sign-off and calculates the minimum for the stations planned.", True),
                   ("Confirms at least one nurse on the shift holds a current ACLS certificate.", True),
                   ("Confirms the physician on duty is present or the attending nephrologist is reachable.", False),
                   ("Sees the signed water results for today and the release for every machine returned from repair.", True),
                   ("Checks the emergency cart seal and defibrillator test log.", False),
                   ("States each failed gate aloud at the huddle, with an owner and a time.", True),
                   ("Keeps affected stations closed until the gate is closed.", True),
                   ("Asks the physician which waiting patients cannot safely be delayed, without deciding it herself.", True),
                   ("Calls the reliever and nursing administration and records each call.", False),
                   ("Tells waiting patients what is happening and when to expect a start.", False),
                   ("Updates the evidence register with the gap found and the follow-up.", False),
               ],
               "placement": "For two weeks, run the five-gate check at every opening on your shifts. Record any gate that failed, the cause, and the time it closed. Review the list with your facilitator and pick one recurring failure to fix."},
    "quiz": [
        ("Why can a small process failure harm a dialysis patient faster than a ward patient?",
         ["Dialysis patients are always older", "The patient&rsquo;s blood meets a large volume of prepared fluid, and the patient cannot correct water, potassium, or pressure on their own", "Dialysis units have fewer nurses", "Wards have no protocols"], 1,
         "The circuit, the fluid, and the missing kidney function remove the body&rsquo;s own safety margin."),
        ("Which source sets out the three-month structured renal dialysis training for a head nurse?",
         ["PhilHealth Circular 2024-0023", "The DOH water order", "The PSN standards for hemodialysis clinics", "The Philippine Nursing Act"], 2,
         "The PSN standards describe the head nurse&rsquo;s preparation. DOH and the Nursing Act set other requirements."),
        ("A nurse holds a renal dialysis training certificate but has not been observed connecting a patient in your unit. How is she counted today?",
         ["As an independent nurse", "As supernumerary until site sign-off", "As half a nurse", "As the ACLS nurse"], 1,
         "A certificate and a site sign-off are different evidence. Only signed-off nurses count toward the rule."),
        ("Twelve stations are planned. How many nurses with sign-off does the DOH provision require?",
         ["2", "3", "4", "6"], 1,
         "Twelve divided by four is three."),
        ("Two signed-off nurses are present for twelve planned stations. How many stations may open on nursing grounds alone?",
         ["4", "6", "8", "12"], 2,
         "Each nurse covers four stations under the provision."),
        ("The only ACLS-certified nurse on the roster has an expired certificate. What is the status of that gate?",
         ["Open, because the nurse was trained", "Closed until a nurse with a current certificate is on the shift", "Open if the physician is present", "Not a requirement"], 1,
         "The licensing order expects a nurse with an updated certificate on each shift."),
        ("Machine 7 was repaired but its release is unsigned. Who may put it back into use?",
         ["The head nurse, after a visual check", "The nurse assigned to station 7", "The designated technical staff, by signing the release", "The administrator"], 2,
         "Technical release belongs to the technical staff. You confirm it exists."),
        ("Which decision belongs to the attending nephrologist or physician on duty, not the head nurse?",
         ["Holding a station", "Which waiting patient can safely be delayed", "Calling a reliever", "Updating the register"], 1,
         "Whether a patient can wait is a medical judgment about that patient."),
        ("Units where every nurse had two years of dialysis experience met more targets. What kind of evidence is this?",
         ["A randomized trial", "Cross-sectional, showing association only", "A case report", "A meta-analysis of trials"], 1,
         "Better-resourced units may have both experienced nurses and healthier patients."),
        ("What did the DOPPS analysis find about highly trained staff hours?",
         ["They raised costs without benefit", "A higher share was associated with fewer skipped sessions", "They had no association with attendance", "They reduced mortality in a trial"], 1,
         "Skipping was itself associated with 30% higher mortality in the same cohort."),
        ("The administrator asks you to start now and fix the paperwork later. What is the best response?",
         ["Start all twelve", "Hold the affected stations, call the owners of each gate, and ask the physician who cannot wait", "Send everyone home", "Ask the patients to vote"], 1,
         "A hold with an owner protects patients without abandoning them."),
        ("What is the main purpose of an evidence register?",
         ["To store patient charts", "To show each requirement, the proof, the owner, and the expiry in one place", "To replace the roster", "To list complaints"], 1,
         "It turns &ldquo;show me&rdquo; into a two-minute answer."),
        ("How far ahead should the register be reviewed for expiring certificates?",
         ["Only on the expiry date", "About ninety days", "Once a year", "Only when inspected"], 1,
         "Ninety days leaves time to book renewal courses."),
        ("Older PhilHealth circulars listed head nurse credentials. What should you do about them?",
         ["Ignore them", "Assume they still apply", "Ask the regional office in writing and file the answer", "Copy them into the job description"], 2,
         "Their current status could not be confirmed from public documents."),
        ("Where a limit is not written in your unit&rsquo;s protocol, what does this series ask you to do?",
         ["Use the limit you learned elsewhere", "Follow the protocol, and ask the attending nephrologist for guidance", "Leave it to the newest nurse", "Wait until the end of the shift"], 1,
         "Inventing a limit at the chairside is how errors start."),
    ],
    "terms": [("Head nurse", "The registered nurse who plans, organizes, and evaluates nursing care across the shifts of a dialysis unit."),
              ("Independent nurse", "A nurse with site competency sign-off to care for patients without direct supervision."),
              ("Supernumerary", "Present on the shift but not counted toward the staffing rule, such as an orientee."),
              ("ACLS", "Advanced cardiovascular life support."),
              ("Technical release", "A signed record that water or a machine passed its tests and may be used."),
              ("Evidence register", "A list of every requirement, the document that proves it, who owns it, and when it expires."),
              ("Hold", "A deliberate pause on a station or a start, with a named owner and a recorded time."),
              ("Cross-sectional study", "A study that looks at many units or people at one point in time. It shows association, not cause.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement."),
                 ("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit, and why ACLS cover matters."),
                 ("hemodialysis-complications.html", "The main complications of a session.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c4"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
