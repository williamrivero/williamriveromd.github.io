# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 09: Leading the Workforce Under Pressure. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician speaking quietly with a charge nurse at the edge of a busy dialysis floor, an assignment board behind them.",
    "objectives": [
        "Recalculate safe slots after an absence, counting only assignments within each person&rsquo;s validated competency.",
        "Resolve an ambiguous order through the responsible physician and document the confirmed plan.",
        "Refuse a request to falsify a record, and protect the person who raised it.",
        "Keep patient protection and competency assessment on a separate track from employment investigation.",
        "Recognize the signs of overload and burnout in a dialysis workforce, and break the loop that feeds them.",
        "Negotiate coverage with an owner using the limiting resource, not volume.",
    ],
    "big": """
{{plain:Staffing a dialysis floor is like seating guests at a table where some dishes can only be served by certain waiters. Counting waiters tells you nothing until you know who can serve what.}}
{{fig:dch09_match}}
<p>The picture has a limit. Waiters can learn a dish in an afternoon. A nurse needs observed, signed practice in your unit before she can safely connect a catheter alone, and a shortcut taken under pressure tends to become the habit that harms a patient months later.</p>
{{cards:Key terms for this module|Validated competency::A skill observed and signed in your unit, with a date to check again.|Float nurse::A nurse moved in from another unit or pool for a shift.|Supernumerary::Present on the shift but not counted toward staffing.|Just culture::An approach that separates honest error, at-risk behavior, and reckless conduct, and responds to each differently.|Retaliation::Any adverse treatment of a person because they raised a safety concern.|Burnout::Emotional exhaustion, detachment, and a reduced sense of accomplishment caused by chronic work stress.}}
""",
    "case": {"title": "The nurse who calls out", "html": """
<p>At 5:30 on a Saturday, nurse Mr. Rodel Aquino calls in sick. The float nurse sent by nursing administration, Ms. Jenny Lopez, is experienced in the ward but has no validated catheter-care competency in dialysis. Four of the shift&rsquo;s patients dialyze through catheters. An order for Mrs. Estrella Gomez says &ldquo;UF 3.5&rdquo; (ultrafiltration) without units or time, and her attending nephrologist is not answering.</p>
<p>The owner, Mrs. Cynthia Sy, texts: &ldquo;Fill all twelve chairs. We cannot afford cancellations this month.&rdquo; At 5:50 the charge nurse, Ms. Liza Ramos, tells you quietly that a senior staff member has asked her to sign Ms. Lopez&rsquo;s catheter competency &ldquo;as of last month&rdquo; so the roster looks complete.</p>
""", "questions": ["Which assignments can Ms. Lopez safely take?",
                  "What do you do about Mrs. Gomez&rsquo;s order, and about the backdating request?",
                  "What do you say to Mrs. Sy?"]},
    "sections": [
        ("slots", "Counting safely", "Count competencies, not bodies", """
<p>After an absence or a change in acuity, recalculate. Usable slots per shift are the smallest of released stations, competence-matched nursing, physician coverage, and any isolation or other restriction (Module 8). A float nurse counts toward the assignments she has been validated to do, with the supervision those assignments require, and no others.</p>
<p>Start with centrally approved backup staff. Then consider limiting capacity, clinically prioritized rescheduling, and confirmed transfers. A qualified physician decides which patients need urgent treatment and whose schedule can safely change; operations arranges transport and tells families through agreed channels.</p>
{{call:Stop any assignment outside a staff member&rsquo;s validated competency. Hold treatment on any order that is ambiguous until the responsible physician, or the covering physician named in your protocol, confirms it. Follow your unit&rsquo;s protocol and record the escalation.}}
"""),
        ("records", "Records", "A record that lies makes every record suspect", """
<p>Backdating a competency sign-off is falsifying a record. It puts the patient in the hands of someone whose competence has not been shown, and it destroys the value of every other signature on the roster. Refuse it plainly, assess the competency properly, and escalate the request through human resources.</p>
{{fig:dch09_twotracks}}
<p>Keep two tracks apart. On the safety track, protect patients now, assess the competency that is in question, and set temporary supervision or scope restrictions if needed, with objective criteria for return. On the personnel track, interview the people involved separately, compare accounts with records, and decide with human resources or medical staff leadership under your procedures. Mixing the tracks teaches staff that reporting a problem gets someone disciplined, and they stop reporting.</p>
<p>Protect the person who spoke up. Ms. Ramos did exactly what the system needs. Thank her, tell her what you will do, and watch for retaliation, including subtle forms such as worse shifts.</p>
{{key:The first job after someone reports a problem is to make sure they would report the next one.}}
"""),
        ("burnout", "Burnout", "The overload loop", """
<p>Dialysis work is repetitive, physically demanding, and emotionally heavy, with patients who are chronically ill and sometimes angry. In a national United States survey of the interdisciplinary dialysis workforce, most staff were satisfied with their jobs, yet only 54% met criteria for professional fulfillment and 33% met criteria for burnout, driven by work exhaustion. Respondents commonly reported high workloads, lack of respect, including violence and hostility, and limited autonomy.[[dch_plantinga2023]] In Italian renal units surveyed ten years apart, violence remained frequent despite training and reporting systems.[[dch_debarbieri2022]]</p>
{{fig:dch09_loop}}
<p>Philippine data on dialysis staff burnout were not found. The mechanism, though, does not depend on country. Thin staffing leaves care undone; care left undone produces near misses; near misses and overtime produce exhaustion; exhausted experienced staff leave; and the remaining staff are thinner still.[[dch_thomashawkins2008]] Break the loop where you can: protect breaks, spread difficult shifts instead of leaning on the same reliable people, close the loop on every hazard reported, and treat violence against staff as a safety event.</p>
"""),
        ("owner", "The owner", "Negotiating with the owner", """
<p>The owner&rsquo;s concern is real: cancellations cost money, and money pays staff. Your job is to show the trade-off clearly, not to win an argument.</p>
<div class="table-wrap"><table>
<thead><tr><th>Say</th><th>Why</th></tr></thead>
<tbody>
<tr><td>&ldquo;We can treat nine safely this morning. Here is the one thing that limits us.&rdquo;</td><td>Names the limiting resource</td></tr>
<tr><td>&ldquo;These three patients will be treated this afternoon or at our partner unit; their nephrologists agreed.&rdquo;</td><td>Shows nobody is abandoned</td></tr>
<tr><td>&ldquo;If we approve one relief nurse with catheter competency, we recover all twelve.&rdquo;</td><td>Gives a decision with a cost</td></tr>
<tr><td>&ldquo;I cannot sign off an assignment that is outside a nurse&rsquo;s competency.&rdquo;</td><td>States the line once, without heat</td></tr>
</tbody></table></div>
<p>In a small unit, you may have a conflict, for example if the person asking for the backdated record is a relative of the owner. Arrange an alternate reviewer.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Ms. Lopez&rsquo;s assignments.</strong> She can take patients with fistulas or grafts if she is validated for those tasks in your unit, or work supernumerary alongside a validated nurse. The four catheter patients go to validated nurses. If that leaves fewer safe slots than patients, the physicians prioritize, and some patients move to the afternoon or a partner unit.</p>
<p><strong>The order and the backdating.</strong> Mrs. Gomez&rsquo;s treatment waits for her attending nephrologist or the covering physician to confirm the ultrafiltration goal in units and time; record each call. Refuse the backdating, thank Ms. Ramos, and escalate the request to human resources on the personnel track. Ms. Lopez&rsquo;s competency is assessed properly, on a later day, by an observer.</p>
<p><strong>What to tell Mrs. Sy.</strong> The safe number, the limiting resource, where each remaining patient will be treated, and the decision that would recover full capacity: approving a validated relief nurse. Then review, over the next month, whether the same people keep absorbing these gaps.</p>
"""],
    "skills": {"title": "Staffing decision and protected escalation",
               "intro": "Role-play the first fifteen minutes of the case and the owner meeting with a preceptor and two role players.",
               "items": [
                   ("Identifies the limiting resource and recalculates safe slots.", False),
                   ("Assigns the float nurse only within validated competency, with supervision as required.", True),
                   ("Holds treatment on an ambiguous order until the responsible physician confirms it.", True),
                   ("Refuses to falsify or backdate any record.", True),
                   ("Thanks and protects the person who raised the concern.", True),
                   ("Separates the safety track from the personnel track.", False),
                   ("Presents the owner with the safe number, the plan for every patient, and a decision with a cost.", False),
                   ("Arranges an alternate reviewer when there is a conflict.", False),
               ],
               "placement": "Track for one month who covers short shifts on your unit. If the same few people carry most of them, present a plan to spread the load."},
    "quiz": [
        ("A float nurse lacks validated catheter competency. Which assignments may she take?",
         ["Any", "Only those within her validated competency, with required supervision", "Catheter patients if supervised by phone", "None"], 1,
         "Count competencies, not bodies."),
        ("An order reads &ldquo;UF 3.5&rdquo; with no units or time. What do you do?",
         ["Guess the usual", "Hold that treatment until the responsible or covering physician confirms it", "Use 3.5 liters", "Skip ultrafiltration"], 1,
         "Ambiguous orders are not executed on assumption."),
        ("A senior staff member asks the charge nurse to backdate a competency sign-off. What is it?",
         ["A shortcut", "Falsification of a record", "A routine correction", "Acceptable under pressure"], 1,
         "Refuse, assess properly, and escalate."),
        ("Why keep the safety track and the personnel track separate?",
         ["To save time", "So reporting a problem does not automatically lead to discipline, and people keep reporting", "Because human resources (HR) insists", "They should be merged"], 1,
         "Separate patient protection from employment decisions."),
        ("What should happen to the person who raised the concern?",
         ["Nothing", "Thanks, information about what will happen, and protection from retaliation", "Transfer", "A warning"], 1,
         "Protect the reporter."),
        ("In a national United States survey, about what share of dialysis staff met burnout criteria?",
         ["5%", "One third", "Two thirds", "All"], 1,
         "33%, driven by work exhaustion."),
        ("Which is a sign of hidden overload?",
         ["High satisfaction scores", "The same few people absorbing every short shift", "Low overtime", "Few complaints"], 1,
         "The most reliable staff burn out first."),
        ("Who decides which patients can safely move to a later shift?",
         ["Operations", "A qualified physician", "The receptionist", "The owner"], 1,
         "Operations coordinates; the physician decides."),
        ("What should a return-to-duty decision cite?",
         ["Seniority", "Defined competencies, observed performance, reviewer approval, and any continued supervision", "A verbal promise", "Time elapsed"], 1,
         "Objective criteria."),
        ("How should violence against staff be treated?",
         ["As part of the job", "As a safety event with reporting and response", "As a personnel issue only", "Ignored if minor"], 1,
         "Violence remains frequent in renal units."),
        ("What is the most useful thing to tell an owner who wants every chair filled?",
         ["That it is impossible", "The safe number, the limiting resource, the plan for each patient, and the decision that would restore capacity", "Nothing", "That staff refuse"], 1,
         "Give a choice with a cost."),
        ("You have a personal conflict in a staff investigation. What should you do?",
         ["Proceed carefully", "Arrange an alternate reviewer", "Drop the investigation", "Ask the staff to decide"], 1,
         "Conflicts need a neutral reviewer."),
        ("What is supernumerary status?",
         ["Overtime", "Present but not counted toward staffing", "A senior title", "A disciplinary status"], 1,
         "Use it for orientees and unvalidated staff."),
        ("Which action helps break the overload loop?",
         ["More overtime for reliable staff", "Protecting breaks and spreading difficult shifts", "Cutting training", "Hiding near misses"], 1,
         "Break the loop where you can."),
        ("Can the owner authorize a nurse&rsquo;s competency by approving the roster?",
         ["Yes", "No; competency is shown by observed, signed performance", "Yes in emergencies", "Only for floats"], 1,
         "Authority over money is not authority over competence."),
    ],
    "terms": [("Validated competency", "A skill observed and signed in your unit."),
              ("Float nurse", "A nurse moved in from another unit or pool."),
              ("Supernumerary", "Present but not counted toward staffing."),
              ("Just culture", "Responding differently to honest error, at-risk behavior, and reckless conduct."),
              ("Retaliation", "Adverse treatment because someone raised a safety concern."),
              ("Burnout", "Exhaustion, detachment, and reduced accomplishment from chronic work stress.")],
    "readings": [("nephrology-workforce-crisis-or-opportunity.html", "Workforce issues in nephrology: crisis or opportunity.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
