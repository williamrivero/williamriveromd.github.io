# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 20: The integrated vascular access service (capstone). Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon presents a patient&rsquo;s access pathway on a whiteboard to a panel of a nephrologist, a dialysis nurse and a quality lead.",
    "objectives": [
        "Map a complete access pathway from referral to rescue, with an owner, an action and an escalation route at every transition.",
        "Defend one patient&rsquo;s plan, including uncertainty, resources, geography and affordability.",
        "Propose and measure one practical service improvement.",
        "Describe how the Academy uses competency-based assessment without claiming equivalence to accredited training.",
    ],
    "big": """
{{plain:An access service is a chain of handoffs: referral, assessment, operation, maturation, first use, maintenance, rescue. Like any chain, it is as strong as its weakest link, and the weak links are rarely in the operating room.}}
<p>The picture has a limit. A chain&rsquo;s links are fixed; a service&rsquo;s links depend on people, schedules and geography that change. A pathway that works on weekdays in Manila may fail on a Saturday in a province three hours away. A safe service is honest about what is available overnight and where patients go when it is not.</p>
{{cards:Key terms for this module|Access pathway::The sequence of steps from referral to a working access and its maintenance.|Pathway owner::The person who tracks a patient through the pathway and escalates delays.|Access coordinator::A role that tracks completion; it does not carry operative authority.|Entrustable activity::A unit of work a trainee can be trusted to perform at a given level of supervision.|Capstone::The final assessment in which the learner defends a patient&rsquo;s plan and a service improvement.}}
<p>This module brings the track together. Your work is to show that every step of a patient&rsquo;s pathway has an owner, and to change one thing in your service and measure whether it worked.</p>
""",
    "case": {"title": "Three sites, no pathway", "html": """
<p>Mr. Honorio Alcantara, 58, has diabetes and lives in Nueva Ecija, three hours from your hospital. He was referred for access eight months ago. Since then he has had a mapping study at one clinic, an access consultation at another, and two emergency catheter placements at a third hospital after missed sessions. Nobody holds the whole plan. He wants to keep working as a tricycle driver. His right internal jugular vein was used for his first catheter.</p>
<p>His daughter tells you, &ldquo;Every place says another place is handling it.&rdquo;</p>
""", "questions": [
        "Where did his pathway break, and who should own it now?",
        "What plan would you defend for him, considering distance, cost and his work?",
        "What service change would prevent the next Mr. Alcantara, and how would you measure it?"]},
    "sections": [
        ("pathway", "The pathway", "Every transition needs an owner", """
<p>Across this track the same failure has recurred: a handoff that nobody closed. A referral sent but not accepted; a fistula created with no follow-up owner; a mature fistula never used because no one told the unit; a clotted graft waiting between teams. Each transition needs an accountable person, an expected action, a time, and a route for escalation if the action does not happen.</p>
{{fig:vs20_a}}
{{flow:The integrated access pathway|Referral::Accepted by a named surgeon with a date; urgent threats triaged.|Planning::Life-Plan with contingency and successor, shared with the unit.|Readiness and creation::Consent, operation, written handoff.|Maturation::Assessment at 2 to 6 weeks; investigation if not mature by 6.|First use::Written plan, experienced cannulator, catheter removal date.|Maintenance::Clinical monitoring, triggers for referral.|Rescue::Emergency pathway, coverage arrangement, transfer destination.}}
<p>A pathway owner, often an access coordinator nurse, tracks each patient through these steps and escalates delays. The coordinator does not acquire operative authority; the surgeon still makes surgical decisions, and the nephrologist still owns the dialysis plan.</p>
{{key:A pathway is complete only when the next urgent step has an accepting service. A plan with an orphaned step is not a plan.}}
"""),
        ("capstone", "The capstone", "Defending a patient&rsquo;s plan", """
<p>For the capstone, you defend one patient&rsquo;s pathway and one service improvement before a panel. The examiner introduces new developments: delayed maturation, threatened skin, an access interruption. You respond as you would in practice, naming owners and contingencies. Explain uncertainty and resource limits honestly, including geography, cost, follow-up access and what the patient can manage, and use the patient&rsquo;s priorities to judge whether the plan is workable.</p>
{{fig:vs20_b}}
<p>The Academy borrows educational principles from competency-based frameworks, such as those of the Accreditation Council for Graduate Medical Education (ACGME), which assess clinical judgment, communication, professionalism and quality improvement.[[vs_acgme]] It does not claim equivalence to accredited surgical training, and passing the capstone grants no privileges. Your hospital&rsquo;s credentialing committee decides what you may do.</p>
<div class="table-wrap"><table>
<thead><tr><th>Capstone domain (0 to 2 each)</th><th>What the panel looks for</th></tr></thead>
<tbody>
<tr><td>Patient goals and alternatives</td><td>The Life-Plan reflects what the patient wants; feasible alternatives compared</td></tr>
<tr><td>Assessment and evidence</td><td>History, examination, imaging; evidence cited with its strength</td></tr>
<tr><td>Justified intervention and future options</td><td>Choice explained; next sites protected</td></tr>
<tr><td>Safety and contingency</td><td>Every emergency recognized and escalated; contingencies named</td></tr>
<tr><td>Communication and improvement</td><td>Handoffs closed; a measurable service change proposed</td></tr>
</tbody></table></div>
<p>A pass is 8 of 10 with every emergency recognized and escalated. A defensible alternative pathway is acceptable when its evidence, feasibility and fit with the patient are explained.</p>
"""),
        ("improve", "Improving the service", "One change, measured", """
<p>Choose one practical improvement that addresses a gap your case exposed, define a measure, and set a review date. Good measures are simple and tied to the gap: median referral-to-assessment time, proportion of new fistulas assessed by six weeks, proportion of mature fistulas with a first-use handoff, catheter days per patient, or the share of urgent referrals accepted the same day. Report counts with rates and include patients lost to follow-up.</p>
{{scene:Service review, fictional|<p>A provincial unit and a city hospital agree that the city access coordinator will call the unit every two weeks about each shared patient, and that urgent problems go to a named on-call surgeon. Six months later, the median time from referral to operation has fallen from 14 weeks to 7, and emergency catheter insertions for missed sessions have halved.</p><p class="tc-scene-take"><b>What this shows.</b> Distance is managed by ownership and communication, not by asking patients to travel more.</p>}}
{{call:Do not declare a pathway complete while an urgent next step has no accepting service. Name it, assign it, and set a time.}}
"""),
    ],
    "debrief": [
        "<p><strong>Where it broke.</strong> No one accepted ownership after the referral: mapping, consultation and emergencies happened at three sites without a shared plan or a pathway owner. Two emergency catheters followed missed sessions that a timely access might have prevented. Ownership now sits with you as the accepting surgeon, together with his nephrologist and a named coordinator.</p>",
        "<p><strong>A plan to defend.</strong> Gather the mapping and history into one Life-Plan. With diabetes, a used right jugular, and a wish to keep driving, a left arm fistula (forearm if the vessels allow) is reasonable, with a left upper-arm option as contingency. Schedule creation, a maturation visit at four to six weeks coordinated with his dialysis days to limit travel, and a first-use handoff to his local unit. Name the on-call surgeon and the nearest emergency destination for bleeding, ischemia or sepsis.</p>",
        "<p><strong>The service change.</strong> Agree with referring units on a single accepting point and a coordinator who tracks shared patients, and measure referral-to-operation time and emergency catheter insertions over six months.</p>",
    ],
    "skills": {"title": "Capstone: pathway and service defense",
               "intro": "Scored by a panel of a surgeon, a nephrologist and a dialysis nurse.",
               "items": [("Presents the complete pathway with an owner and backup at each transition", True),
                         ("Defends the patient&rsquo;s choices with evidence and feasibility", False),
                         ("Recognizes and escalates every emergency introduced by the examiner", True),
                         ("Proposes a defined measure and review date for one service improvement", False),
                         ("States that course completion grants no privileges or certification", False)],
               "placement": "Capstone defense"},
    "quiz": [
        ("What closes a referral handoff?",
         ["Acceptance by a named service with the next action and contingency agreed", "Sending a message without acknowledgment",
          "Adding another copy of the referral", "Telling the patient to call"],
         0, "The pathway requires ownership and follow-through."),
        ("A learner scores highly but misses an emergency safety action. What happens?",
         ["Automatic clinical sign-off", "Targeted feedback and reassessment of that action", "Privileges with a warning", "Nothing; the total passed"],
         1, "Knowledge scores cannot compensate for unaddressed critical errors."),
        ("What authority does an access coordinator hold?",
         ["Operative decisions", "Tracking completion and escalating delays, without operative authority", "Dialysis prescription", "Credentialing surgeons"],
         1, "The coordinator owns tracking, not surgical or dialysis decisions."),
        ("How does the Academy relate to Accreditation Council for Graduate Medical Education (ACGME) competency frameworks?",
         ["It is equivalent to accredited training", "It borrows educational principles without claiming equivalence",
          "It grants ACGME credit", "It replaces board examinations"],
         1, "Principles are used; equivalence is not claimed."),
        ("Which is the best measure for a service change meant to speed access creation?",
         ["Number of meetings held", "Median referral-to-operation time, with counts and missing data", "Number of catheters ordered", "Staff satisfaction alone"],
         1, "A measure tied to the gap, reported transparently, shows whether the change worked."),
    ],
    "terms": [("Pathway owner", "The person who tracks a patient through every step and escalates delays."),
              ("Entrustment", "A decision that a trainee can perform an activity at a given level of supervision.")],
    "readings": [("hemodialysis-access-lifeline.html", "The access as a lifeline that lasts a lifetime."),
                 ("dialysis-qapi-vs-cqi.html", "Quality improvement in dialysis.")],
    "calcs": ["calc-av-access-outcome-audit.html", "calc-catheter-exposure.html", "calc-qapi-run-chart-spc.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
