# -*- coding: utf-8 -*-
"""Renal Social Worker, Module 06: Care Plans, Referrals, and Case Management. Written for this series from published sources."""

MODULE = {
    "image_alt": "A social worker on the phone confirming a referral while checking a printed care plan with columns.",
    "objectives": [
        "Write care plan goals in the person&rsquo;s own words, linked to the formulation.",
        "Turn each goal into actions with an owner, a due date, and the evidence that will show it is done.",
        "Track a referral through sent, accepted, decided, delivered, and confirmed, and close it only on evidence.",
        "Set a review date and the triggers that bring a review forward.",
        "Close a case, or step it down, with a clear handover to the person and the team.",
    ],
    "big": """
{{plain:A care plan is a relay race. Each runner carries the baton for one stretch, then hands it on. Races are not lost by slow runners as often as by dropped batons: the handoff where each runner thought the other had it.}}
{{fig:sw06_referral_loop}}
<p>The picture has a limit. In a relay the baton is visible, and everyone knows when it hits the ground. A referral that falls between two services makes no sound. The form was sent; the receiving office never opened it; the patient waited, assumed the answer was no, and stopped asking. Nobody saw the baton drop. That is why case management is mostly about one thing: making handoffs visible and checking that they happened.</p>
<p>Your job in this module is to build plans that belong to the person, to give every action an owner and a date, and to keep each referral open until you have evidence that the help reached the household. Navigation helps people finish steps. In a cluster randomized trial in 23 hemodialysis units, patients who met monthly with trained peer navigators completed more steps toward transplant than those with usual care (3.5 against 1.6 steps); the trial measured steps completed, a process outcome, and did not show more transplants or longer survival.[[sw_sullivan2012]] The lesson for you is the mechanism: someone who knows the next step and follows up.</p>
{{cards:Key terms for this module|Care plan::The agreed goals, actions, owners, dates, and review point for one person.|SMART goal::Specific, measurable, achievable, relevant, and time-bound.|Owner::The one person responsible for an action, by name or role.|Referral::A request to another service to do something for the person.|Closed loop::A referral closed only when the outcome is confirmed, not when the request is sent.|Step-down::Reducing contact once goals are met, with a clear route back.}}
""",
    "case": {"title": "Seven referrals, zero outcomes", "html": """
<p>You take over the caseload of a social worker who resigned. On Wednesday at 3:00 p.m. you open the file of Mrs. Josefina Cruz, 58, on hemodialysis for two years. Her care plan, dated four months ago, lists one goal: &ldquo;Address financial concerns.&rdquo;</p>
<p>The referral log shows seven entries, each marked &ldquo;Referred&rdquo;: a local government medical assistance office, a charity foundation, the PCSO, the hospital Malasakit Center, the dietitian, a psychiatrist, and the barangay for transport. None has an outcome, a date of response, or a contact name.</p>
<p>When you call Mrs. Cruz, she says nobody ever called her back, and that she now borrows money every month from a lender in her neighborhood at what she calls &ldquo;5-6.&rdquo;</p>
""", "questions": ["What is wrong with the existing care plan and log?",
                  "How would you rewrite the plan with Mrs. Cruz?",
                  "How will you track the referrals so this does not happen again?"]},
    "sections": [
        ("goals", "Goals that belong to the person", "Her words, your structure", """
<p>A goal written by the worker, for the worker, is a task list. A goal the person recognizes as theirs is a plan they will help carry out. Start from what they said matters most (Module 1), and connect it to the formulation (Module 5).</p>
{{fig:sw06b_goals}}
<div class="table-wrap"><table>
<thead><tr><th>Weak goal</th><th>Why it fails</th><th>Stronger goal</th></tr></thead>
<tbody>
<tr><td>&ldquo;Address financial concerns.&rdquo;</td><td>No outcome, no time, not the person&rsquo;s words</td><td>&ldquo;Stop borrowing from the lender to pay for transport by January.&rdquo;</td></tr>
<tr><td>&ldquo;Improve compliance.&rdquo;</td><td>Blames, and measures nothing the person cares about</td><td>&ldquo;Keep my job and attend all three sessions a week by changing to the afternoon shift.&rdquo;</td></tr>
<tr><td>&ldquo;Psychiatric evaluation.&rdquo;</td><td>An action, not a goal</td><td>&ldquo;Sleep through the night and feel like myself again.&rdquo; (Action: mental health referral.)</td></tr>
</tbody></table></div>
<p>Use the SMART test on each goal: specific, measurable, achievable, relevant, and time-bound. Two or three goals are enough. A plan with ten goals is a plan nobody follows.</p>
{{key:Write goals in the person&rsquo;s words, linked to the formulation, and keep to two or three at a time.}}
"""),
        ("actions", "Actions with owners and dates", "Who does what by when", """
<p>Each goal needs actions. Each action needs one owner, a due date, and the evidence that will show it is done. The person and the family own actions too; write theirs down as clearly as yours.</p>
<div class="table-wrap"><table>
<thead><tr><th>Action</th><th>Owner</th><th>Due</th><th>Closure evidence</th></tr></thead>
<tbody>
<tr><td>Review the household budget and the lender debt</td><td>Social worker with Mrs. Cruz</td><td>Friday</td><td>Written budget with monthly gap (toolkit)</td></tr>
<tr><td>Ask the unit about an afternoon shift</td><td>Head nurse</td><td>Next Monday</td><td>Shift confirmed in the schedule</td></tr>
<tr><td>Bring barangay certificate of residency and indigency</td><td>Mrs. Cruz&rsquo;s son</td><td>Next Wednesday</td><td>Documents in hand</td></tr>
<tr><td>Submit the Malasakit Center request</td><td>Social worker</td><td>Next Thursday</td><td>Receiving officer&rsquo;s name and reference number</td></tr>
<tr><td>Confirm the decision and what was actually paid</td><td>Social worker</td><td>Two weeks after submission</td><td>Decision letter or billing record; patient confirms</td></tr>
</tbody></table></div>
<p>The last row is the one that is usually missing. A submission is not help. Help is what reached the household. The <a href="calc-social-worker-toolkit.html#tool-1">access cost tool</a> can show the monthly gap before and after, so the person sees what changed.</p>
{{key:Every action has one owner, a due date, and closure evidence. The person&rsquo;s own actions are written down too.}}
"""),
        ("loop", "The referral loop", "Sent is not done", """
<p>A referral passes through five stations. Only the last one closes it.</p>
{{flow:The five stations of a referral|Sent::You sent the request. Record date, channel, recipient name.|Received and accepted::The service confirms it has the request and will act. Record who confirmed.|Decided::The service decides (accepted, declined, partial, waitlisted). Record the decision and reason.|Delivered::The help happened: the appointment took place, the funds were applied, the device arrived.|Confirmed::The person confirms it reached them and made the difference intended.}}
<p>Track each open referral by age. A referral that has not moved for longer than you agreed is an escalation, not a waiting game. The <a href="calc-social-worker-toolkit.html#tool-4">referral aging tool</a> turns the open date and due date into days open, days overdue, and a tier: on track, due soon, overdue, or escalate.</p>
{{formula:<strong>Worked example, illustrative.</strong> Days open = today &minus; date sent. Days overdue = today &minus; due date (if positive).<br>Sent March 3. Due March 13. Today March 20.<br>Days open = 17. Days overdue = 7.<br>Tier: overdue (7 days or fewer past due); more than 7 days past due would be &ldquo;escalate.&rdquo;<br>What the number tells you: this referral needs a call today. What it does not tell you: whether the service lost it, declined it, or is waiting for a document.}}
<p>When a referral is declined, the loop still closes, with a reason. A declined request with a reason is useful; it tells you what to try next. A request that simply vanished tells you nothing and costs the person weeks.</p>
{{key:Close a referral only on a confirmed outcome. A declined request with a reason closes the loop; silence never does.}}
{{scene:The dietitian referral|<p>Social worker Ms. Nina Garcia refers a patient to the dietitian for weight loss on March 1. On March 8 her log shows &ldquo;sent.&rdquo; She calls: the request went to a dietitian on leave.</p>
<p>She resends it to the covering dietitian, who sees the patient on March 10. She closes the referral on March 11, after the patient tells her the meal plan fits her budget.</p>
<p class="tc-scene-take">One phone call found a referral that would have waited another month.</p>}}
"""),
        ("review", "Review, step-down, and closure", "Keeping the plan alive", """
<p>Set a review date when you write the plan. Most stable cases can be reviewed every three months; set a shorter interval for complex cases. Some events should bring the review forward at once.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trigger</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Hospital admission or a fall</td><td>Function, money, and caregiving may all change</td></tr>
<tr><td>Missed or shortened sessions</td><td>A barrier has appeared or grown</td></tr>
<tr><td>Change of modality, transplant listing, or transfer</td><td>New demands on the household</td></tr>
<tr><td>Benefit sessions running out, job loss, death in the family</td><td>Financial and emotional shock</td></tr>
<tr><td>New distress, safety concern, or caregiver collapse</td><td>Risk has changed</td></tr>
</tbody></table></div>
<p>Step a case down when its goals are met, and tell the person how to come back: whom to ask, and what kind of problem should bring them back. Closing a case is not abandoning it; it is handing the person back their own plan, with a door left open.</p>
{{key:Every plan has a review date and named triggers. Every closure leaves a clear way back.}}
"""),
    ],
    "debrief": ["""
<p><strong>What is wrong.</strong> The goal is the worker&rsquo;s, not Mrs. Cruz&rsquo;s, and it measures nothing. The log records actions (&ldquo;referred&rdquo;) and no outcomes: no recipient, no response date, no decision. Seven referrals sent at once, with none followed up, probably wasted the family&rsquo;s documents and trust. And the plan missed a growing harm: monthly borrowing from an informal lender at high interest.</p>
<p><strong>The rewritten plan.</strong> Start with an apology for the delay, then ask what she wants. A goal such as &ldquo;Stop borrowing to pay for dialysis transport by January.&rdquo; Actions: a budget review with the access cost tool this week; a check of which of the seven requests is still alive (call each, starting with the oldest); one or two well-prepared applications rather than seven thin ones; a referral to the dietitian or psychiatrist only if those needs are still present, assessed afresh; and a review date in four weeks.</p>
<p><strong>Tracking.</strong> One row per referral with the five stations, a named contact, and a due date. Check the aging tool weekly. Close each only on a confirmed outcome, including a decline with its reason.</p>
"""],
    "skills": {"title": "A care plan and a referral log",
               "intro": "From a fictional formulation, write a care plan and track two referrals while your supervisor observes.",
               "items": [
                   ("Writes two or three goals in the person&rsquo;s own words, linked to the formulation.", False),
                   ("Gives each action one owner, a due date, and closure evidence, including the person&rsquo;s own actions.", False),
                   ("Records each referral through sent, accepted, decided, delivered, and confirmed.", True),
                   ("Uses the referral aging tool and escalates an overdue referral the same day.", False),
                   ("Closes a referral only on a confirmed outcome, including a decline with its reason.", True),
                   ("Sets a review date and names the triggers that bring it forward.", False),
               ],
               "placement": "Audit five of your own open referrals. For each, find the evidence for its current station and call the owner of any that has not moved in two weeks."},
    "terms": [("Care plan", "Agreed goals, actions, owners, dates, and review point."),
              ("SMART goal", "Specific, measurable, achievable, relevant, time-bound."),
              ("Owner", "The one person responsible for an action."),
              ("Closed loop", "A referral closed only on a confirmed outcome."),
              ("Referral aging", "Days a referral has been open and overdue."),
              ("Step-down", "Reducing contact when goals are met, with a clear way back.")],
    "readings": [("personal-medical-journal-health-history.html", "The patient guide to keeping a personal health journal, useful for people tracking their own plan.")],
    "calcs": ["calc-social-worker-toolkit.html#tool-4", "calc-social-worker-toolkit.html#tool-1"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["06"])
