# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 08: Safe Capacity, Supply, and the Board Brief. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician presenting a one-page brief to two clinic owners at a small conference table, a capacity chart on the screen.",
    "objectives": [
        "Calculate safe capacity from the narrowest gate: released machines, competence-matched staffing, physician coverage, and isolation needs.",
        "Reserve capacity for patients with time-sensitive needs, and test the margin against foreseeable losses.",
        "Calculate a reorder point and days of cover, and recalculate when lead time changes.",
        "Control critical supplies: expiry rotation, recalls, approved substitutes, and verified lead times.",
        "Write a one-page board brief that asks for a decision, with its cost, effect on patients, and owner.",
        "State the lost capacity and activate a transfer plan when operational targets conflict with safety.",
    ],
    "big": """
{{plain:Capacity is like a funnel with several narrow points. However wide the top, only as much passes as the narrowest point allows.}}
{{fig:dch08_limit}}
<p>The picture has a limit. In a funnel the narrow point never moves. In a dialysis unit it moves every day: a machine fails its disinfection, a nurse calls in sick, a patient needs isolation. Safe capacity is a number you recalculate whenever one of the gates changes, not a number painted on the door.</p>
{{cards:Key terms for this module|Safe slot::A treatment place that is released, staffed by a validated nurse, covered by a physician, and suitable for the patient assigned to it.|Limiting resource::The gate that sets the number of safe slots today.|Lead time::Days from placing an order to having verified stock on the shelf.|Safety stock::A buffer held for unexpected demand or delay.|Reorder point::The stock level at which you order, equal to daily use times lead time plus safety stock.|Board brief::A one-page document that asks the governing body for one decision.}}
""",
    "case": {"title": "Eighteen on the schedule", "html": """
<p>Your unit in Quezon City has ten stations and runs two shifts. Two machines are quarantined after failed disinfection tests. The head nurse, Ms. Rowena Lim, tells you that the cleared nurses on today&rsquo;s roster can safely cover seven patients per shift. Eighteen sessions are scheduled.</p>
<p>The stockroom reports 30 dialyzer kits used a day, a supplier lead time of four days, and a policy of 60 kits of safety stock. The supplier has just warned that a courier strike may double the lead time. The owner, Mr. Victor Tan, asks: &ldquo;We have ten machines. Why are we not treating twenty?&rdquo;</p>
""", "questions": ["How many patients can you safely treat today?",
                  "What is your plan for those who still need a place?",
                  "What do you take to Mr. Tan, and what do you ask him to decide?"]},
    "sections": [
        ("capacity", "Safe capacity", "Count what you can run safely", """
<p>Count each gate per shift, then take the smallest.</p>
<div class="table-wrap"><table>
<thead><tr><th>Gate</th><th>Today</th></tr></thead>
<tbody>
<tr><td>Machines released for use</td><td>10 &minus; 2 quarantined = 8</td></tr>
<tr><td>Patients the cleared nurses can safely cover</td><td>7</td></tr>
<tr><td>Physician coverage</td><td>Adequate for both shifts</td></tr>
<tr><td>Isolation or other restrictions</td><td>None today</td></tr>
<tr><td><strong>Safe slots per shift</strong></td><td><strong>7 (staffing is the limiting resource)</strong></td></tr>
</tbody></table></div>
{{formula:<strong>Today.</strong> 7 safe slots &times; 2 shifts = 14. Demand is 18, so 4 patients need a plan before any further loss. If one more nurse calls in, the number falls again. Calculator 1 does this with your own numbers.}}
<p>Reserve room for patients whose treatment cannot move: those after a missed session, those returning from hospital, and those needing isolation. Then test the margin. What happens if one more machine fails, or one more nurse is absent? Write the trigger at which you activate transfers, before you need it.</p>
{{call:Stop booking beyond the safe number. Ask the attending nephrologists which of the patients without a slot can safely move, and which must be placed today. Confirm any transfer by name with the receiving unit.}}
"""),
        ("supply", "Supply", "Order before the shelf looks low", """
{{fig:dch08_reorder}}
<p>A reorder point protects you from running out while an order is in transit. It is daily use multiplied by lead time, plus safety stock.</p>
{{formula:<strong>Reorder point.</strong> 30 kits a day &times; 4 days + 60 = 180 kits. If lead time doubles to 8 days: 30 &times; 8 + 60 = 300 kits. The day the supplier warns you, your reorder point rises by 120 kits. Calculator 2 recalculates it and shows days of cover.}}
<p>Check the units (kits, not boxes), use the actual daily use over recent weeks, and review the safety stock if demand or lead time varies. Rotate stock by expiry, keep recall traceability to the lot, and qualify substitutes before a shortage, not during it (Module 11). Maintain service agreements for water and machines with response times that match your risk.</p>
"""),
        ("brief", "The board brief", "Give the owner a decision, not a worry", """
{{fig:dch08_brief}}
<p>Owners act on choices. A memo that lists problems without asking for anything leaves the decision to whoever reads it last. A one-page brief has six parts.</p>
{{flow:The one-page brief|1. Decision needed and deadline::Approve overtime for two relief nurses for two weeks, by Friday.|2. Facts and uncertainties::Seven safe slots per shift; four patients without a place; supplier lead time may double.|3. Options::Relief nurses; transfer four patients to a partner unit; extend a third shift with existing staff.|4. Effect on patients and staff::Which patients move, how far, and the risk to staff of repeated overtime.|5. Recommendation and cost::With a range when assumptions are uncertain.|6. Owner and review::Who carries it out and when the board hears whether it worked.}}
<p>Include equity. If transfers fall on patients without transport or money for fares, the cheapest option on paper may be the most harmful in practice.</p>
{{key:When a target conflicts with safety, state the capacity you are losing and activate the plan for it. Do not let the gap be absorbed silently by the floor.}}
"""),
        ("rhythm", "Operating rhythm", "A rhythm that finds problems early", """
<p>Lead short readiness huddles every shift (Module 4), review incidents and trends at fixed intervals, and invite patient feedback. Resolve complaints with a named owner, immediate safety triage, and timely feedback to the patient. Keep confidential incident and personnel records separate from operational reports.</p>
<div class="table-wrap"><table>
<thead><tr><th>Interval</th><th>Review</th></tr></thead>
<tbody>
<tr><td>Every shift</td><td>Safe slots, holds, patients without a place</td></tr>
<tr><td>Weekly</td><td>Stock against reorder points, lead-time changes, open complaints</td></tr>
<tr><td>Monthly</td><td>Quality measures with denominators, incidents, staffing gaps, claims returns</td></tr>
<tr><td>Quarterly</td><td>Board brief on capacity, risks, and decisions needed</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>How many today?</strong> Fourteen: seven per shift, because staffing, not machines, is the limiting resource. The two quarantined machines would not help even if released, until more cleared nurses are available.</p>
<p><strong>The four without a place.</strong> Ask the attending nephrologists to review all four. Those who cannot wait are placed today at a partner unit, confirmed by name, with transport arranged. Those who can safely move are rescheduled within the window the physician sets. Every one has a named owner until treated.</p>
<p><strong>What to take to Mr. Tan.</strong> A one-page brief: the safe number and why, the four patients&rsquo; plan, the options to restore capacity with costs, and a request to approve the reorder at 300 kits now because of the courier warning. Ask for a decision by a date, and name who will report back.</p>
"""],
    "skills": {"title": "Safe capacity, reorder point, and board brief",
               "intro": "Calculate safe capacity and reorder points for a fictional unit, then present a one-page brief to a preceptor playing the owner.",
               "items": [
                   ("Counts each gate and identifies the limiting resource.", True),
                   ("Books no more than the safe number of slots.", True),
                   ("Asks physicians to prioritize patients without a slot and confirms transfers by name.", True),
                   ("Calculates the reorder point with correct units and recalculates for a longer lead time.", False),
                   ("Writes a brief with a decision, options, effect on patients, cost, and owner.", False),
                   ("Considers equity in transfer options.", False),
                   ("Sets a review date to confirm the decision worked.", False),
               ],
               "placement": "Calculate your own unit&rsquo;s safe capacity every day for two weeks and record the limiting resource. Bring the pattern to your next board meeting."},
    "quiz": [
        ("Ten stations, two quarantined, staffing for seven per shift. How many safe slots per shift?",
         ["10", "8", "7", "5"], 2,
         "Staffing is the narrowest gate."),
        ("With seven safe slots and two shifts, how many patients can be treated today?",
         ["10", "14", "16", "20"], 1,
         "7 times 2."),
        ("Demand is 18 sessions and safe capacity is 14. What happens to the other 4?",
         ["They are squeezed in", "Physicians prioritize them and each gets a confirmed plan and owner", "They are sent home", "They wait for tomorrow automatically"], 1,
         "No patient leaves without a plan."),
        ("What is the reorder point at 30 kits a day, 4 days lead time, and 60 kits safety stock?",
         ["120", "150", "180", "240"], 2,
         "30 times 4, plus 60."),
        ("If lead time doubles to 8 days with the same buffer, what is the reorder point?",
         ["180", "240", "300", "360"], 2,
         "30 times 8, plus 60."),
        ("What sets safe capacity?",
         ["The number of machines", "The narrowest of the gates", "The owner&rsquo;s target", "The waiting list"], 1,
         "Released machines, staffing, coverage, restrictions."),
        ("Why reserve capacity for some patients?",
         ["For VIPs", "Patients after a missed session, back from hospital, or needing isolation cannot easily move", "For staff", "For audits"], 1,
         "Plan for time-sensitive needs first."),
        ("What should a board brief do?",
         ["List all problems", "Ask for one decision with options, cost, effect, and owner", "Praise staff", "Repeat the minutes"], 1,
         "Owners act on choices."),
        ("Why include equity in a transfer decision?",
         ["It is fashionable", "Transfers can fall hardest on patients without transport or money", "PhilHealth requires it", "It lowers cost"], 1,
         "The cheapest option on paper can harm most in practice."),
        ("When should you recalculate safe capacity?",
         ["Once a year", "Whenever a gate changes", "Only during inspections", "Never"], 1,
         "It moves daily."),
        ("A supplier warns of delay. When should you act?",
         ["When the shelf is empty", "Now, by recalculating the reorder point and ordering the difference", "Next month", "After the delay"], 1,
         "The math changes before the shelf does."),
        ("What should the board approve?",
         ["A general concern", "A specific action, owner, resources, deadline, and how impact will be checked", "A slogan", "Nothing"], 1,
         "Make it verifiable."),
        ("When targets conflict with safety, what should the clinical head do?",
         ["Absorb the gap quietly", "State the lost capacity and activate the escalation or transfer plan", "Meet the target", "Resign"], 1,
         "Make the trade-off visible."),
        ("Which is a balancing concern of repeated overtime?",
         ["Lower costs", "Staff fatigue and burnout", "Fewer complaints", "Better attendance"], 1,
         "Overtime fixes today and can break next month."),
        ("What should happen weekly for supplies?",
         ["Nothing", "Stock compared with reorder points and lead-time changes", "A full inventory recount", "Vendor dinners"], 1,
         "A weekly check catches drift."),
    ],
    "terms": [("Safe slot", "A released, staffed, covered, suitable treatment place."),
              ("Limiting resource", "The gate that sets today&rsquo;s safe capacity."),
              ("Lead time", "Days from order to verified stock."),
              ("Safety stock", "A buffer for unexpected demand or delay."),
              ("Reorder point", "Daily use times lead time plus safety stock."),
              ("Days of cover", "Current stock divided by daily use."),
              ("Board brief", "A one-page request for one decision.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "How dialyzer reprocessing affects supply, cost, and safety.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
