# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 08: Staffing, Delegation, and Coaching. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse updating an assignment board with a nurse and an orientee before the shift.",
    "objectives": [
        "Explain how thin staffing reaches the patient, step by step.",
        "Summarize what the research shows about nurse staffing in dialysis, and what it cannot show.",
        "Build an assignment from the staffing rule, verified competencies, and the acuity of today&rsquo;s patients.",
        "Find the single points of failure on a shift and name a backup for each.",
        "Delegate a task using the five rights, and keep the accountability that comes with it.",
        "Give feedback about an observed step that changes how it is done.",
    ],
    "big": """
{{plain:A staffing ratio is like the load rating on an elevator. It tells you the most the cable was certified to carry. It does not tell you whether today&rsquo;s passengers are balanced, whether one of them is carrying something heavy, or whether the operator has ever run this elevator before.}}
<p>The picture has a limit. An elevator over its rating fails all at once. A shift over its safe load fails quietly, one skipped check at a time, and the patients notice before the roster does.</p>
{{fig:hn08_ratio}}
{{cards:Key terms for this module|Staffing rule::The DOH provision of one nurse for every four hemodialysis stations.|Supernumerary::Present but not counted, such as an orientee.|Acuity::How much nursing care a patient needs today.|Single point of failure::A capability held by only one person on the shift.|Delegation::Handing a task to another person while keeping responsibility for the decision to hand it over.|Care left undone::Necessary tasks that were not done because there was no time.|Competency matrix::A table of each nurse&rsquo;s signed-off skills, with dates.}}
""",
    "case": {"title": "The lone ACLS nurse calls in sick", "html": """
<p>At 5:15 on Saturday, Ms. Karen Dela Cruz calls in sick. She is the only nurse on the morning roster with a current ACLS certificate. Twelve stations are scheduled. Present are Mr. Arnel Cruz and Ms. Joy Mercado, both signed off to work alone, and Ms. Bea Santos, an orientee in her second week.</p>
<p>One patient, Mrs. Lourdes Navarro, 80, had two episodes of low pressure last week and the nephrologist has asked for close observation. The reliever list has three names.</p>
""", "questions": ["How many stations can open now, and why?",
                  "Can Ms. Santos fill the gap?",
                  "What do you still check once a reliever arrives?"]},
    "sections": [
        ("mechanism", "How it reaches the patient", "How thin staffing reaches the patient", """
<p>The path from staffing to harm is not mysterious, and it tells you what to watch.</p>
{{fig:hn08_loop}}
<p>Fewer or less experienced nurses per patient leads to care left undone. The tasks dropped first are the ones without an alarm: looking at the access, asking about symptoms, teaching, checking the order against the screen. Those are the safety layers the earlier modules depend on. Sustained overload then produces burnout and turnover, which lowers the experience mix, which leads to more care left undone. The loop feeds itself.</p>
{{scene:The week two nurses resigned|<p>In August, two experienced nurses resign in the same week, and the unit runs on relievers and overtime for a month. No alarm changes. Kt/V results look the same.</p>
<p>When you look at the observation round sheets, the line &ldquo;access visible and needles checked&rdquo; was ticked on 98% of rounds in July and 70% in August. Patient teaching notes fell by half. Nothing on a machine would have shown this. The checks that have no alarm were the first to go, exactly as the mechanism predicts. That month&rsquo;s numbers become your evidence when you ask nursing administration for a reliever pool: the problem is not that the nurses worked less hard, but that the work without an alarm was what got dropped.</p>}}
{{key:Under pressure, nurses drop the checks that have no alarm. Those are the checks that catch the problems the alarms miss.}}
"""),
        ("evidence", "What the evidence shows", "What the research shows about staffing", """
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Data</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>Ratios and care left undone</td><td>More patients per nurse and more tasks left undone were associated with more adverse events reported by nurses[[hn_thomashawkins2008]][[hn_thomashawkins2020]]</td><td>Cross-sectional, reported by nurses</td></tr>
<tr><td>Experience mix</td><td>Units where every nurse had two years of dialysis experience met more dose, pressure, and albumin targets[[hn_jeong2023]]</td><td>Cross-sectional</td></tr>
<tr><td>Trained hours and attendance</td><td>More highly trained staff hours, lower odds of patients skipping[[hn_saran2003]]</td><td>Cohort</td></tr>
<tr><td>Staffing and transplant</td><td>Median 14.4 patients per nurse. The most stretched quartile was associated with 14% lower incidence of transplant in young patients[[hn_bicki2024]]</td><td>Large cohort</td></tr>
<tr><td>Work environment</td><td>Workload and practice environment were related to burnout and intention to leave[[hn_flynn2009]][[hn_iroegbu2025]]</td><td>Cross-sectional</td></tr>
</tbody></table></div>
<p>All of this is observational, and almost all of it comes from the United States and Korea, where technicians do much of the chairside work. It supports a reasonable inference that experience mix and workload are safety variables. It does not identify a correct ratio. No Philippine outcome data were found. You meet the DOH provision of one nurse to four stations because it is the rule,[[doh2012]] not because a trial chose the number.</p>
"""),
        ("assign", "Building the assignment", "Building a safe assignment, step by step", """
{{flow:Five steps|The arithmetic::Stations to open &divide; 4, rounded up. Add the fixed requirement of at least one nurse with current ACLS. Confirm with your regional office how stations are counted.|Who counts::Only nurses with site sign-off to work alone. Orientees are supernumerary. A nurse covering reception or billing is not at the chair.|Weigh the load::Add new patients, catheters, last session&rsquo;s low pressure, isolation, close observation. Subtract breaks and any transfer that will take a nurse off the floor.|Single points of failure::List each critical skill and who holds it today. Any skill held by one person needs a backup or a reliever.|The trigger::Write down in advance the condition that reduces capacity and who you call.}}
{{formula:<strong>Arithmetic illustration.</strong> 12 stations &divide; 4 = 3 nurses. With 2 counted, open at most 8. ACLS cover is a separate gate. If neither present nurse holds it, no station opens until a nurse who does arrives.}}
<p>Which patients can be deferred or moved is the nephrologist&rsquo;s decision. Your part is to give them the facts and the options.</p>
{{scene:Twelve patients, three nurses, one room|<p>On Tuesday morning you have three nurses signed off to work alone and twelve stations, which meets the rule of one nurse to four stations. One station is the hepatitis B room, which needs a dedicated nurse. Two patients started with new catheters this week, and Mrs. Leonora Cruz, 78, is on close observation after low pressures.</p>
<p>A naive split gives each nurse four chairs. A weighted one looks different. The nurse assigned to the hepatitis B room cannot also care for patients outside it, so her assignment is the room plus nothing that crosses the line. The two new catheters go to the nurse with the most catheter experience. Mrs. Cruz goes to the nurse whose stations are nearest the nurses&rsquo; station, and that nurse gets one fewer patient if the roster allows. If it does not, the conversation with the physician about whether anyone can safely start later happens now, not at 10:00.</p>}}
{{call:Stop and call nursing administration, the clinical head, and the physician on duty when you cannot meet the staffing rule or ACLS cover before the scheduled start. Ask the physician which patients can safely be deferred. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("delegate", "Delegation", "Delegating with the five rights", """
{{fig:hn08_rights}}
{{cards:The five rights|Right task::Within the person&rsquo;s scope of practice.|Right circumstance::Appropriate for this patient at this moment.|Right person::Competency verified for this task in your unit.|Right direction::What to do, what to report, and when to stop.|Right supervision::You check the result.}}
<p>You can delegate the task. You cannot delegate the accountability for having delegated it well. The Philippine Nursing Act places supervision among a nurse&rsquo;s responsibilities.[[hn_ra9173]]</p>
{{scene:What the aide was told to report|<p>You ask a nursing aide to weigh the second-shift patients and take their pre-dialysis pressures. A weak handover is &ldquo;Do the weights and vitals.&rdquo; A strong one gives the right direction: &ldquo;Weigh each patient on the same scale, record it on the sheet, and tell me at once if anyone is above the weight gain limit written at the top of the sheet, has a pressure outside the limits on the sheet, or says they are short of breath.&rdquo;</p>
<p>At 11:40 the aide tells you that Mr. Ruben Flores is 4.1 kilograms above his dry weight and says he slept sitting up. Because the aide knew what to report, you hear it before connection, not after. Then you supervise: you check two of the recorded weights yourself, because delegating the task did not delegate the accountability.</p>}}
"""),
        ("coach", "Coaching", "Feedback that changes practice", """
{{fig:hn08_coach}}
{{flow:See it, link it, ask, show, repeat|See it::&ldquo;At station 6, the hub was open for about twenty seconds while you reached for the syringe.&rdquo;|Link it::&ldquo;That is the moment organisms get into the lumen.&rdquo;|Ask::&ldquo;What made that step awkward?&rdquo; The answer is often the setup.|Show::Demonstrate the approved technique, or fix the setup.|Repeat::Watch it done again. Record the result, any restriction, and a date to recheck.}}
<p>Feedback about a specific observed action changes behavior. Feedback about attitude does not. Repeated or serious lapses move to the formal management process.</p>
<p><strong>Keeping the team.</strong> Retention is a safety intervention. The drivers you can influence are workload, a voice in unit decisions, and support from the head nurse.[[hn_flynn2009]][[hn_iroegbu2025]] Protect breaks on the assignment board, rotate the hardest assignments, close the loop on every hazard a nurse reports, and give each new nurse a named preceptor for a defined period.</p>
{{scene:The catheter cluster, every day|<p>Ms. Joy Mercado, a nurse with four years in the unit, asks to speak with you. She has been assigned the four catheter patients at the far end of the floor every shift for two months, because she is the best at catheter care. She is tired, and she has an offer from a hospital.</p>
<p>Her skill was being rewarded with the hardest load, every day. You rotate the catheter cluster across the three most experienced nurses, pair Ms. Mercado with a newer nurse for two weeks so that her skill spreads, and record the rotation on the assignment board where everyone can see it. Ms. Mercado stays. Rotating the hard assignment cost nothing. Replacing her would have cost months.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>How many stations?</strong> Twelve stations need three nurses who count. You have two, so at most eight can open on nursing grounds. Separately, nobody present holds a current ACLS certificate, which is its own failed gate. Until a nurse with ACLS arrives, no station opens. Call the reliever list in order, looking specifically for someone with current ACLS. Call nursing administration and the clinical head. Ask the physician on duty which patients could be deferred or sent elsewhere if relief does not come.</p>
<p><strong>Can Ms. Santos fill the gap?</strong> No. She is in her second week and has no site sign-off, so she is supernumerary. Counting her would put a new nurse alone with four patients, which is exactly the situation the rule exists to prevent. She can still work alongside a signed-off nurse.</p>
<p><strong>Once the reliever arrives.</strong> Recheck the whole board, not only the arithmetic. Who is on close observation with Mrs. Navarro? Who covers her during breaks? Is the only ACLS nurse now also the person most likely to be pulled into an emergency, leaving a gap on the floor? Write the trigger for the rest of the day: if anyone else leaves, which stations close first.</p>
"""],
    "skills": {"title": "Assignment board and coaching",
               "intro": "Build an assignment board for a synthetic shift, then coach an orientee who skipped the pre-start order check while your facilitator observes.",
               "items": [
                   ("Calculates the minimum nurses for the stations planned.", True),
                   ("Counts only signed-off nurses and identifies supernumerary staff.", True),
                   ("Confirms ACLS cover as a separate requirement.", True),
                   ("Adds acuity, isolation, and close-observation needs to the assignment.", False),
                   ("Names a backup for each single point of failure.", True),
                   ("Writes a trigger for reducing capacity and the people to call.", False),
                   ("Does not decide which patients are deferred, and asks the physician.", True),
                   ("Gives feedback on one specific observed step, linked to patient risk.", True),
                   ("Asks what made the correct step difficult.", False),
                   ("Records the result, any restriction, and a recheck date.", False),
               ],
               "placement": "Keep a competency matrix for your unit for one month. Mark every empty and expired cell, and turn them into a teaching plan with dates."},
    "quiz": [
        ("Under the DOH provision, how many signed-off nurses are needed for 16 stations?",
         ["3", "4", "5", "16"], 1,
         "16 &divide; 4 = 4."),
        ("Which staff count toward the staffing rule?",
         ["Everyone in scrubs", "Only nurses with site sign-off to work alone", "Orientees after one week", "The technician"], 1,
         "Orientees are supernumerary."),
        ("Which tasks are dropped first under overload?",
         ["Machine setup", "Tasks without an alarm: looking, asking, teaching, checking", "Documentation of vital signs", "Disconnection"], 1,
         "Those are the safety layers that catch what alarms miss."),
        ("What kind of evidence links staffing to outcomes in dialysis?",
         ["Randomized trials", "Mostly observational studies", "Case reports only", "Animal studies"], 1,
         "They show association and a plausible mechanism, not a proven ratio."),
        ("Among young patients, what was the most stretched nursing quartile associated with?",
         ["More transplants", "14% lower incidence of transplant", "Fewer infections", "Higher Kt/V"], 1,
         "Referral work is among the tasks left undone."),
        ("Two signed-off nurses are present for twelve stations and neither has ACLS. How many stations may open?",
         ["12", "8", "None until ACLS cover arrives", "4"], 2,
         "ACLS cover is a separate gate from the ratio."),
        ("Who decides which waiting patients can be deferred?",
         ["The head nurse", "The physician on duty or attending nephrologist", "The administrator", "The patients"], 1,
         "It is a medical decision about each patient."),
        ("What is a single point of failure on a shift?",
         ["A broken machine", "A critical skill held by only one person", "A late patient", "A missing chart"], 1,
         "Each one needs a backup or a reliever."),
        ("What must follow delegation?",
         ["Nothing", "Supervision matched to the risk and confirmation of the result", "A written exam", "A PhilHealth form"], 1,
         "You keep the accountability for delegating well."),
        ("Which of these is one of the five rights of delegation?",
         ["Right uniform", "Right person, with competency verified for this task", "Right salary", "Right shift"], 1,
         "The others are task, circumstance, direction, and supervision."),
        ("Which feedback is most likely to change a nurse&rsquo;s technique?",
         ["&ldquo;You need a better attitude.&rdquo;", "&ldquo;The hub was open about twenty seconds at station 6. That is when organisms enter. What made it awkward?&rdquo;", "&ldquo;Read the policy again.&rdquo;", "&ldquo;Everyone else does it right.&rdquo;"], 1,
         "Specific, observed, linked to risk, and asking about conditions."),
        ("Why ask what made the correct step difficult?",
         ["To excuse the nurse", "The cause is often the setup, which you can fix", "To fill time", "It is a legal requirement"], 1,
         "Fixing the setup protects every nurse who comes next."),
        ("Why is retention a safety intervention?",
         ["It saves money only", "Turnover lowers the experience mix, which feeds the overload loop", "It is required by DOH", "It shortens shifts"], 1,
         "Experience mix is associated with outcomes."),
        ("What does a competency matrix show?",
         ["Salaries", "Each nurse&rsquo;s signed-off skills with dates", "Patient lists", "Machine serial numbers"], 1,
         "Empty and expired cells become the teaching plan."),
        ("A reliever arrives and the arithmetic now works. What else do you check?",
         ["Nothing", "Close-observation cover, break cover, and whether the ACLS nurse is also a single point of failure", "Only the water", "Only the roster signature"], 1,
         "Arithmetic is where staffing starts, not where it ends."),
    ],
    "terms": [("Staffing rule", "The DOH provision of one nurse for every four hemodialysis stations."),
              ("Supernumerary", "Present but not counted toward the rule."),
              ("Acuity", "How much nursing care a patient needs today."),
              ("Single point of failure", "A critical skill held by only one person on the shift."),
              ("Delegation", "Handing a task to another person while keeping responsibility for that decision."),
              ("Care left undone", "Necessary tasks not done because there was no time."),
              ("Competency matrix", "A table of signed-off skills for each nurse, with dates."),
              ("Burnout", "Exhaustion, detachment, and a sense of ineffectiveness from sustained work stress.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Using staffing data in quality review."),
                 ("hemodialysis-complications.html", "What close observation is watching for."),
                 ("code-blue-acls-dialysis-unit.html", "Why ACLS cover matters on every shift.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c4"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
