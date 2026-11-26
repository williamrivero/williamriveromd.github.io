# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 02: The Opening Sweep. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse walking a quiet dialysis floor at dawn, pausing at a machine with a red tag while a technician checks the water room.",
    "objectives": [
        "Run the five opening gates in a fixed order and say what each one protects.",
        "Treat a missing result as an abnormal result.",
        "Check that an emergency cart is complete, sealed, and ready in about five minutes.",
        "Prepare isolation stations and keep tagged machines out of use before patients arrive.",
        "Hold the first connection when a gate is closed, tell waiting patients why, and name an owner and a time.",
    ],
    "big": """
{{plain:A pilot does not take off because the plane looked fine yesterday. She walks around it, reads a checklist aloud, and waits for the tower. The checklist exists because the most dangerous errors are the ones nobody notices on an ordinary morning.}}
<p>The picture has a limit. A pilot does every check on her own plane. On a dialysis floor the checks belong to several people: the technician tests the water, the biomedical staff release the machines, the head nurse builds the roster, and the physician answers the phone. The charge nurse does not perform all five checks herself. Your work in this module is to confirm that each one was done, signed, and is current before the first needle goes in, and to hold the start when one is not.</p>
{{cards:Key terms for this module|Opening gate::A condition that must be true before the first patient connects.|Hold::A decision not to start, with a named owner and a time to look again.|Total chlorine::A water test for chlorine and chloramine, done before treatment each day under the unit&rsquo;s protocol.|Machine release::The biomedical staff&rsquo;s signed statement that a machine passed its checks.|Red tag::A label that takes a machine out of use until it is repaired and released.|Isolation station::A dedicated area, machine, and equipment for a patient with hepatitis B.}}
""",
    "case": {"title": "It&rsquo;s 5:55 and the chlorine log is blank", "html": """
<p>At a freestanding unit in Bulacan, Nurse Paolo Mendoza takes charge at 5:30. By 5:55, eleven patients are seated in their chairs. The total chlorine test for the morning has not been entered; the water technician, Mang Ruben, texts that he is stuck in traffic on MacArthur Highway. The night nurse says, &ldquo;It was fine last night.&rdquo;</p>
<p>The emergency cart seal is intact, but yesterday&rsquo;s defibrillator check strip is missing from the log. A patient in Bed 3 says she has work at noon and asks why they are not starting.</p>
""", "questions": ["Can Paolo start the first connections?",
                  "What does he do about the emergency cart?",
                  "What does he tell the eleven waiting patients?"]},
    "sections": [
        ("gates", "The five gates", "Five gates before the first connection", """
<p>Run the same five gates in the same order every morning, so a busy day cannot skip one.</p>
{{fig:cn02_gates}}
<div class="table-wrap"><table>
<thead><tr><th>Gate</th><th>What must be true</th><th>Who owns it</th></tr></thead>
<tbody>
<tr><td>1. People</td><td>Enough nurses who can work alone for the stations you will run; at least one ACLS-trained nurse on the floor; nobody counted who is not cleared</td><td>Head nurse (roster); charge nurse (today&rsquo;s check)</td></tr>
<tr><td>2. Physician</td><td>The physician on duty is present, or reachable within the unit&rsquo;s agreed time, by a number tested this morning</td><td>Medical director (schedule); charge nurse (the test call)</td></tr>
<tr><td>3. Water and machines</td><td>Today&rsquo;s water checks done and signed; every machine in use released; tagged machines set apart</td><td>Water and biomedical staff</td></tr>
<tr><td>4. Emergency readiness</td><td>Cart sealed and in date; defibrillator checked; suction and oxygen working</td><td>Charge nurse or the nurse assigned</td></tr>
<tr><td>5. Patients and stations</td><td>Isolation stations prepared; each patient&rsquo;s order current; flags from the previous shift reviewed</td><td>Charge nurse with the staff nurses</td></tr>
</tbody></table></div>
<p>The United States Centers for Disease Control and Prevention (CDC) core interventions for dialysis units rest on the same idea: a few checks done reliably every day protect more patients than many checks done occasionally.[[hn_cdc_core]] The order of the five gates matters less than doing them the same way every day.</p>
{{key:A gate is either open or closed. &ldquo;Probably fine&rdquo; is closed.}}
"""),
        ("blank", "A blank is red", "Why a blank result is a red result", """
<p>Chlorine and chloramine in city water are harmless to drink. In dialysis they are not. They cross the dialyzer membrane into the blood, where chloramine damages red cells and causes hemolysis, the bursting of red cells. Outbreaks have followed exhausted carbon filters and changes in the city water supply.[[tipple1991]][[ward1996]]</p>
<p>The difference is volume. A person drinks about two liters of water a day. A patient on dialysis is exposed to well over a hundred liters of dialysis fluid in one session, across a membrane thinner than paper, directly into the blood. Small amounts that the gut would never notice can harm a dialysis patient.</p>
<p>So a missing test means &ldquo;unknown,&rdquo; and unknown water is treated as unsafe until the technician tests it and signs the result. The limits themselves are in the unit&rsquo;s approved water protocol under DOH AO 2013-0003; the charge nurse does not set or change them.[[hn_doh2013]] Module 11 goes deeper into water.</p>
{{scene:&ldquo;It was fine last night&rdquo;|<p>At a hospital unit in Quezon City, the night nurse tells the incoming charge nurse that the water was tested at 9 p.m. and was fine. The morning test is not done. The charge nurse asks: &ldquo;Was the carbon tank backwashed after 9 p.m.?&rdquo; It was, at 11 p.m.</p>
<p>A backwash, a change in the city water, or a long weekend can change the result overnight. Last night&rsquo;s result describes last night&rsquo;s water. The morning test is done at 5:50, inside the unit&rsquo;s limit, and signed. The first patient connects at 6:00.</p>}}
"""),
        ("cart", "The cart", "The emergency cart in five minutes", """
<p>Five checks, in the same order:</p>
{{fig:cn02_cart}}
{{flow:The five-minute cart check|Seal::The seal number matches the log. If it is broken or does not match, do the full content check before patients connect.|First expiry::The item due to expire first is still in date.|Defibrillator::The self-test or manual check is done and logged. If it fails, borrow one and tell the head nurse.|Suction::It turns on and pulls.|Oxygen::The cylinder pressure is enough for the shift, per the unit&rsquo;s rule.}}
<p>Why this matters: in a registry of 398 cardiac arrests in United States dialysis clinics, staff started cardiopulmonary resuscitation (CPR) before the ambulance arrived in most cases, and staff-started CPR was associated with about three times the odds of leaving hospital alive.[[hn_pun2019]] That only works when the cart and the defibrillator are ready at 6:01, not at 6:30.</p>
{{scene:The seal that did not match|<p>Nurse Liza Cruz finds seal number 41207 on the cart. The log says 41206. Nobody remembers opening it. She does the full content check before the first connection and finds the adrenaline box missing, used during a ward emergency the evening before and never replaced. She gets a replacement from the pharmacy, reseals the cart, logs the new number, and writes a near-miss report. Ten minutes, and the next arrest will have adrenaline.</p>}}
"""),
        ("stations", "Stations and machines", "Stations and machines before patients arrive", """
<p>Patients with hepatitis B surface antigen (HBsAg) need a dedicated room or area, machine, equipment, and staff member, as the CDC recommends; hepatitis B can survive on surfaces for at least seven days.[[cdc2001]] Prepare that station before the patient walks in. A patient who arrives to find his station not ready sits in the waiting area while staff hurry, and hurrying is when boundaries slip.</p>
<p>A machine with a red tag stays out of the bay. Move it physically, or block it, so nobody plugs it in at 6:10 because it is the only free one. Confirm that every machine you will use today has a current release.</p>
<p>Read the previous shift&rsquo;s flags: a patient who was admitted, a new dry weight, a pending potassium, a new access. Those flags are why the order you are about to run may already be out of date.</p>
"""),
        ("hold", "Holding well", "Holding with an owner and a time", """
<p>A closed gate is a hold, not a failure. A good hold has three parts: who will open it (&ldquo;Mang Ruben, testing at 6:10&rdquo;), what you tell the waiting patients, and whether the minutes lost can be added back at the end.</p>
<p>Tell patients plainly: &ldquo;The water test for this morning is not done yet. We will start about twenty minutes late. You will get your full time.&rdquo; Patients accept a delay when they understand it. They lose trust when they see staff hide it, or when they are rushed off the machine at the end to make up the time.</p>
<p>Count the cost honestly. Fifteen minutes lost for eleven patients is 165 patient-minutes, close to one full session in a single morning. If the minutes are not added back, they are dialysis that never happened (Module 6). Agree with the next shift&rsquo;s charge nurse on a later start for her first chairs, so the morning patients get their full time.</p>
{{scene:The patient with work at noon|<p>Mrs. Joanna Lim, 44, works the noon shift at a mall pharmacy. She asks to start now or to come off twenty minutes early. The charge nurse explains why the hold exists, offers to call her supervisor to explain the delay, and asks the attending nephrologist whether any change is safe. She does not quietly shorten Mrs. Lim&rsquo;s treatment to keep her happy. The supervisor agrees to a later start for the day.</p>}}
{{key:A hold has a name and a time. Without both, it is just a delay.}}
"""),
    ],
    "debrief": ["""
<p><strong>Can Paolo start?</strong> No. A missing water result is an abnormal result. He holds every connection until Mang Ruben tests and signs. He does not accept &ldquo;it was fine last night,&rdquo; because the carbon tanks and the city water can change overnight.</p>
<p><strong>The cart.</strong> The seal is intact, so a full content count is not needed, but the defibrillator check is. He runs it now. If it fails, he borrows one from the ward and tells the head nurse before the first connection.</p>
<p><strong>The patients.</strong> He tells them the reason, the expected delay, and that their full time will be given. Mang Ruben arrives at 6:05; the result is entered at 6:12. Eleven patients start between 6:15 and 6:40 instead of 6:00 to 6:25. Paolo asks the second-shift charge nurse to start her first four chairs fifteen minutes later so the morning patients get their full four hours (Toolkit #c4 counts the minutes).</p>
<p><strong>The system fix.</strong> Paolo writes one line in the shift log and one in the improvement file: &ldquo;Water test delayed by traffic; no backup tester.&rdquo; The head nurse trains a second staff member to run the morning test under the technician&rsquo;s protocol. That second line is how a habit changes.</p>
"""],
    "skills": {"title": "The opening sweep",
               "intro": "Run the five gates on a real morning with a facilitator watching, then a second time on a simulated morning with one gate deliberately closed.",
               "items": [
                   ("Runs the five gates in the same order and states what each protects.", True),
                   ("Treats a missing water result as a hold and does not connect.", True),
                   ("Completes the five-minute cart check and logs the seal number.", False),
                   ("Runs or confirms the defibrillator check and knows where to borrow one.", True),
                   ("Places a red-tagged machine out of the bay.", True),
                   ("Prepares the isolation station before the patient arrives.", False),
                   ("Tests the physician&rsquo;s number and has the backup number ready.", False),
                   ("Gives waiting patients a hold message with the reason, the delay, and the plan for full time.", True),
                   ("Writes a one-line improvement note when a gate was closed by a system gap.", False),
               ],
               "placement": "For one week, record each morning&rsquo;s gates and any gate that was closed, why, and for how long. Review the list with the head nurse."},
    "quiz": [
        ("The water test is not entered at opening. How do you treat it?",
         ["As normal", "As abnormal until tested and signed", "As optional on Mondays", "As the technician&rsquo;s problem only"], 1,
         "Unknown water is treated as unsafe until it is tested."),
        ("Why is dialysis water riskier than drinking water?",
         ["It is colder", "A patient is exposed to far more water across a membrane directly into the blood", "It contains more salt", "It is reused"], 1,
         "Over a hundred liters a session reach the blood across the dialyzer."),
        ("What is the charge nurse&rsquo;s job at the water-and-machines gate?",
         ["Test the water herself", "Confirm that testing and release are done and signed", "Set the limits", "Repair the machines"], 1,
         "The technical staff test and release; the charge nurse confirms."),
        ("In clinic cardiac arrests, staff-started CPR was associated with:",
         ["No difference", "About three times the odds of leaving hospital alive", "Worse outcomes", "Fewer shockable rhythms"], 1,
         "Readiness at the first connection is what makes early CPR possible."),
        ("Where should a patient with hepatitis B surface antigen dialyze?",
         ["Any open chair", "A dedicated area with a dedicated machine, equipment, and staff", "The last chair in the row", "Only at home"], 1,
         "The CDC recommends dedicated rooms or areas, machines, and staff."),
        ("A good hold message to patients contains:",
         ["Only an apology", "The reason, the expected delay, and the plan for full time", "Nothing; it is not their concern", "The technician&rsquo;s name only"], 1,
         "Patients accept a delay they understand."),
        ("The defibrillator check is missing from the log. What do you do?",
         ["Ignore it", "Run the check now and borrow one if it fails", "Wait for the head nurse", "Close the unit"], 1,
         "Readiness is checked before the first connection."),
        ("Fifteen minutes lost for 11 patients equals:",
         ["26 minutes", "110 minutes", "165 minutes", "11 minutes"], 2,
         "11 &times; 15 = 165 patient-minutes, close to one full session."),
        ("The cart seal number does not match the log. What next?",
         ["Use it anyway", "Do the full content check before patients connect", "Replace the seal without checking", "Ignore it until a code"], 1,
         "A mismatched seal means the cart may have been opened."),
        ("Why does chloramine harm dialysis patients?",
         ["It raises blood sugar", "It damages red cells and causes hemolysis", "It lowers potassium", "It clots the dialyzer"], 1,
         "Chloramine oxidizes hemoglobin when it reaches the blood."),
        ("Who sets the numerical water limits?",
         ["The charge nurse", "The unit&rsquo;s approved water protocol under the DOH order", "The patients", "PhilHealth"], 1,
         "The charge nurse follows them; she does not set or change them."),
        ("A machine has a red tag. Where should it be?",
         ["In the bay, unplugged", "Out of the bay or blocked so nobody uses it", "At the isolation station", "In the waiting area"], 1,
         "Physical separation prevents a rushed mistake."),
        ("The physician&rsquo;s phone goes to voicemail at 5:50. What do you do?",
         ["Start anyway", "Call the backup number; do not start the first connection until a physician is reachable, per protocol", "Send a text and start", "Wait until noon"], 1,
         "The physician gate is open only when someone can answer."),
        ("What does the previous shift&rsquo;s flag list protect against?",
         ["Nothing", "Running an order that is already out of date", "Late lunches", "PhilHealth denials"], 1,
         "A new dry weight or a pending result can change today&rsquo;s plan."),
        ("Why run the gates in the same order every day?",
         ["It looks professional", "So a busy morning cannot skip one", "Because DOH lists them in that order", "It is faster"], 1,
         "Habit protects the check that would otherwise be forgotten."),
    ],
    "terms": [("Opening gate", "A condition that must be true before the first patient connects."),
              ("Hold", "A decision not to start, with a named owner and a time to look again."),
              ("Total chlorine", "A water test for chlorine and chloramine."),
              ("Hemolysis", "The bursting of red blood cells."),
              ("Red tag", "A label that takes a machine out of use until repaired and released."),
              ("Isolation station", "A dedicated area, machine, and equipment for a patient with hepatitis B.")],
    "readings": [("dialysis-water-treatment-systems.html", "How dialysis water is treated and tested."),
                 ("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit."),
                 ("dialysis-machine-assignment.html", "Machine allocation for hepatitis B, hepatitis C, and HIV.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c4"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
