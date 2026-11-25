# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 1: The owner role and the governance charter. Written for this course from published sources."""

MODULE = {
    "image_alt": "A dialysis unit owner at the head of a boardroom table, with the treatment floor visible through a glass wall behind her.",
    "objectives": [
        "Separate the legal entity, the licensed service, and the people appointed to run it.",
        "Sort decisions into reserved, delegated, and protected, and write a delegation that works when you are unreachable.",
        "Rank the evidence you receive, from a verbal promise to a re-audit that shows a fix held.",
        "Explain why no owner, shareholder, or manager may override a clinical or technical hold.",
    ],
    "big": """
{{plain:Think of a ship. The owner pays for the ship, chooses the captain, and decides which routes are worth sailing. The captain decides whether it is safe to leave port today. An owner who orders the ship out into a storm because the cargo is valuable has not saved money. The owner has risked everything aboard.}}
<p>The picture has a limit. A ship has one captain, and a dialysis unit has several people whose judgment is protected: the attending nephrologist for each patient&rsquo;s prescription, the clinical head for the service, the nursing lead for assignments, and the technical lead for water and machines. Each of them can say &ldquo;not today&rdquo; for reasons the owner may not be able to judge.</p>
{{cards:Key terms for this module|Legal entity::The company, foundation, or partnership that owns the unit and signs its contracts.|Licensed service::The facility the Department of Health (DOH) has licensed, at a stated address, with a stated number of stations.|Reserved decision::A decision only the governing owner or board may take, such as borrowing or appointing a clinical head.|Delegated decision::A decision handed to a named person within a written limit, with a backup and a way to escalate.|Protected decision::A clinical or technical judgment no commercial authority may override.|Assurance::Evidence that a control actually works, not a promise that it does.}}
<p>Most of an owner&rsquo;s power is real and useful: money, appointments, and priorities. A small part of it is a trap. Your work in this module is to know which is which, write it down, and build a meeting that tells you the truth.</p>
""",
    "case": {"title": "The machine on hold", "html": """
<p>It is 6:40 on a Monday morning at a 12-station unit in Malolos, Bulacan. The biomedical technician, Mr. Rodel Santos, has tagged Machine 7 &ldquo;Do not use&rdquo; after its conductivity alarm failed a test. Eleven patients are booked for the first shift, and the unit has no spare machine.</p>
<p>Mr. Victor Lim owns 40% of the company. He arrives early, sees the tag, and tells the unit manager, Ms. Grace Dizon, to put the machine back in service. &ldquo;Every session we cancel costs us 6,350 pesos, and the alarm was probably fine last week.&rdquo; Ms. Dizon calls you, the chair of the board, before she does anything.</p>
""", "questions": ["What do you tell Ms. Dizon in the next two minutes?", "Who decides when Machine 7 is safe, and what evidence will they need?",
                  "What will you change in the governance charter after today?"]},
    "sections": [
        ("entity", "Who is who", "The entity, the license, and the people", """
<p>Start with three names that are often different. The <strong>legal entity</strong> owns the assets and signs contracts. The <strong>licensed service</strong> is what the Department of Health (DOH) has licensed: a facility at an address, with stated stations, staff, and equipment.[[doh2012]] The <strong>appointees</strong> are the people who run it: a clinical head under a written contract, a nursing lead, a technical lead, and a manager.[[psn2024]]</p>
<p>The license belongs to the facility, but the duties it carries land on the entity. A shareholder cannot assume that a manager&rsquo;s signature or a nephrologist&rsquo;s professional license moves the facility&rsquo;s obligations off the company. If the unit dialyzes beyond its licensed stations, or without the staff the license assumes, the entity answers for it.</p>
<p>Other countries write this down plainly. United States rules place responsibility for a dialysis facility on a governing body, which must appoint an administrator to run staffing and money.[[dch_cfr494]] That rule is not Philippine law, but the idea transfers: the board owns the outcome, and the people it appoints own the daily decisions.</p>
{{key:Write down three things for your unit: the legal entity, the licensed service, and each appointee&rsquo;s name and scope. If any of the three is unclear, nothing else in this course will hold.}}
"""),
        ("charter", "The charter", "Reserved, delegated, and protected decisions", """
{{fig:duo01a}}
<p>A governance charter is a short document that says who decides what. It should fit on two pages. Sort every recurring decision into one of three kinds.</p>
<div class="table-wrap"><table>
<thead><tr><th>Kind</th><th>Examples</th><th>Who decides</th></tr></thead>
<tbody>
<tr><td>Reserved</td><td>Borrowing, capital spending above a limit, owner distributions, appointing or removing the clinical head or manager, opening or closing a site</td><td>The owner or the board</td></tr>
<tr><td>Delegated</td><td>Ordering stock, shift rosters, vendor coordination, the claims workflow, routine repairs under a spending limit</td><td>A named appointee, within a written limit</td></tr>
<tr><td>Protected</td><td>A prescription, whether a patient is fit to dialyze, a machine or water hold, isolation precautions, nurse assignments</td><td>The qualified clinician or technician; never overridden for money</td></tr>
</tbody></table></div>
<p>A delegation that works has five parts: the role, the scope, the spending limit, a named backup, and a condition that triggers escalation. &ldquo;Grace handles operations&rdquo; is not a delegation. &ldquo;The unit manager may approve repairs up to 50,000 pesos; above that, the board chair; if the chair is unreachable for two hours, the vice-chair&rdquo; is one.</p>
{{key:Every delegation needs a role, a scope, a limit, a backup, and an escalation trigger. A delegation without a backup fails on the first holiday.}}
"""),
        ("assurance", "Assurance", "Assurance: how an owner knows", """
{{fig:duo01b}}
<p>An owner rarely sees a control working. You hear about it. That makes the quality of what you hear the whole game. Rank the evidence on a simple ladder: a verbal reassurance at the bottom, then a written policy, then a current roster and competency record, then a signed record that a check was done, and at the top a re-audit that shows a fixed problem stayed fixed.</p>
<p>Boards differ in how seriously they take this. In a national survey of hospital board chairs, Jha and Epstein found that many did not rate their own expertise in quality of care as strong, fewer than half of some groups made quality a top priority, and fewer than one in ten examined quality data broken down by patient group.[[duo_jha2012]] The survey measured attitudes, not outcomes, so it does not show that engaged boards save lives. It does show how easily quality drops off a board&rsquo;s agenda.</p>
<p>A monthly governance meeting of an hour can hold the whole picture if it looks at the same few things every time: major risks, safety trends with their denominators, cash, staffing gaps, and overdue actions. Record each decision with the person responsible, the due date, and the evidence that will show it is done. That cadence is this course&rsquo;s recommendation, not a regulation.</p>
{{key:Ask for the highest rung of evidence you can get. &ldquo;The staff know what to do&rdquo; is the bottom rung.}}
"""),
        ("holds", "The hold rule", "The hold no owner overrides", """
<p>The most dangerous moment in owner governance is a held machine, a held water loop, or a patient a nurse says is not safe to start, on a day when the schedule is full. The commercial pressure is real. A cancelled session loses its revenue while fixed costs continue.</p>
<p>The answer is the same every time. The hold stands until the qualified person releases it, with the evidence their protocol requires. The owner&rsquo;s job is to make the hold cheap to keep: fund the repair today, arrange a loaned machine or a partner-unit transfer, and ask the attending nephrologists which patients can safely wait and which cannot.</p>
<p>Then protect the person who held. If staff learn that a hold earns an angry phone call from a shareholder, the next fault will not be reported. Write a stop-work clause into the charter and the appointment letters: any staff member may stop an unsafe treatment, and no one is penalized for a good-faith hold.</p>
{{stop:An owner, shareholder, or manager who orders a held machine, water loop, or treatment back into use has crossed the protected line. Stop, keep the hold, and escalate to the clinical head.}}
{{key:Ownership buys the right to fund the fix, not the right to skip it.}}
"""),
    ],
    "debrief": ["""
<p><strong>What to tell Ms. Dizon.</strong> Keep the hold. Machine 7 returns to service only when Mr. Santos documents a passed test and releases it under the unit&rsquo;s technical procedure. Ask the attending nephrologist on duty to decide which of the eleven patients can move to the second shift and which need another unit today. Approve the cost of an urgent repair or a loaned machine now; that decision is yours.</p>
<p><strong>Mr. Lim.</strong> Speak to him yourself, privately and the same day. Explain that the charter reserves technical release to the technical lead and that the board will fund the fix. Record the attempted override in the board minutes, factually.</p>
<p><strong>The charter.</strong> Add the stop-work clause, name a backup biomedical technician, and add a standing rule: a held machine triggers an automatic repair authority up to a set peso limit, so nobody has to ask.</p>
"""],
    "skills": {"title": "Governance charter and decision-rights map",
               "intro": "Draft a two-page charter for a real or fictional unit and run a five-person board huddle that routes ten decisions.",
               "items": [("Names the legal entity, the licensed service, and each appointee with scope.", False),
                         ("Sorts ten decisions correctly into reserved, delegated, and protected.", False),
                         ("Writes each delegation with role, scope, limit, backup, and escalation trigger.", False),
                         ("States that no owner or shareholder may override a clinical or technical hold.", True),
                         ("Includes a stop-work clause and protection for staff who hold in good faith.", True),
                         ("Sets a monthly meeting agenda with risks, safety trends, cash, staffing gaps, and overdue actions.", False)],
               "placement": "Compare your draft with your unit&rsquo;s actual appointment letters. List every gap and who would fix it."},
    "quiz": [
        ("A biomedical technician has held a machine after a failed alarm test. Who may return it to service?",
         ["The largest shareholder", "The designated technical lead, with the required test evidence", "The billing officer, once the schedule is full", "Any vendor representative"],
         1, "Technical release belongs to the qualified technical lead under the unit&rsquo;s procedure. Ownership and commercial pressure confer no technical competence."),
        ("Which delegation will still work on a holiday?",
         ["&ldquo;The manager handles operations.&rdquo;", "A signature with no limit", "A named role, a scope, a spending limit, a backup, and an escalation trigger", "Verbal permission to do whatever is needed"],
         2, "Without a limit, a backup, and a trigger for escalation, the delegation fails exactly when the delegate is absent or the decision is too big."),
        ("Which is the strongest evidence that a corrective action worked?",
         ["The invoice for the repair was paid", "A re-audit showing the problem stayed fixed", "An optimistic verbal update", "No complaint was received this month"],
         1, "Payment, optimism, and silence are low on the assurance ladder. A re-audit against the closure criterion shows the control works."),
        ("Which of these is a protected decision?",
         ["Approving the annual budget", "Choosing a new rent location", "Deciding whether a patient is fit to start dialysis today", "Setting the owner distribution policy"],
         2, "Fitness to dialyze is a clinical judgment. The others are reserved owner decisions."),
        ("A shareholder orders a held water loop back into use. What should the board record and do?",
         ["Nothing, if no patient was harmed", "Discipline the technician who held it", "Keep the hold, fund the fix, and record the attempted override factually", "Ask the vendor to decide"],
         2, "The hold stands, the owner&rsquo;s role is to fund the recovery, and the attempt is recorded so the charter can be corrected."),
        ("In the national survey of hospital board chairs by Jha and Epstein, what did the data show?",
         ["Engaged boards reduced mortality", "Few boards examined quality data broken down by patient group", "All boards rated quality as their top priority", "Board size predicted infection rates"],
         1, "The survey described attitudes and practices, including that fewer than one in ten chairs examined stratified quality data. It did not measure patient outcomes."),
    ],
    "terms": [("Governance charter", "A short document stating who decides what in the organization."),
              ("Stop-work clause", "A written rule that any staff member may stop an unsafe treatment without penalty.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": [],
}


def _balance(quiz):
    """Spread the keyed answers across A to D, deterministically (same as tools/techcourses/uom/quizutil.py)."""
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        target = (i * 3 + 1) % 4
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out


MODULE["quiz"] = _balance(MODULE["quiz"])
