# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 15: Claims integrity and revenue assurance. Written for this course from published sources."""

MODULE = {
    "image_alt": "Two stacks of claim forms, one shorter, joined by teal threads to a laptop, with a magnifying glass over the gap.",
    "objectives": [
        "Trace a session from delivery to cash and find where claims leak.",
        "Run an exceptions log that fixes causes, not numbers.",
        "Manage returned and denied claims within the filing rules.",
        "Draw the line between lawful correction and claims that must never be made.",
    ],
    "big": """
{{plain:A claim is like a relay race. The session is the start, and the baton passes through the nurse&rsquo;s record, the agreement form, the claims officer, and PhilHealth before it reaches the bank. A dropped baton at any handoff means no payment, however well the session went.}}
<p>The picture has a limit. In a relay, you can blame the runner who dropped the baton. In a unit, a dropped claim usually points to a system: a form designed badly, a step nobody owns, a deadline nobody watches. Fix the system and the drops stop.</p>
{{cards:Key terms for this module|Reconciliation::Matching sessions delivered with sessions claimed, accepted, and paid.|Exception::A session that did not move cleanly to payment.|Returned claim::A claim sent back for correction.|Denied claim::A claim refused.|Upcoding::Claiming for a more expensive service than was delivered.}}
<p>Your work is to know your leakage, fix its causes, and make sure that every claim the unit files is true.</p>
""",
    "case": {"title": "Thirty-eight and thirty-one", "html": """
<p>At a unit in Bacolod, the monthly report shows 38 sessions delivered to new patients in October but only 31 claimed. The claims officer says seven agreement forms were unsigned or incomplete. The manager suggests asking the patients to sign the forms now and dating them to the session days.</p>
""", "questions": ["What is wrong with the manager&rsquo;s suggestion?", "What is the right correction?", "How do you stop it happening again?"]},
    "sections": [
        ("chain", "The chain", "Session to cash", """
{{fig:duo15a}}
<p>Follow every session through five counts: delivered, fully documented, claimed, accepted, and paid. Each count should equal the one before it. Where a count drops, there is a reason: a missing signature, a patient not yet in the PhilHealth Dialysis Database, a late filing, an eligibility problem, a returned claim.[[pc_pa2016_0030]][[pc_pc2025_0019]]</p>
<p>Ask for this reconciliation monthly, as five numbers and a list of reasons. The gap between delivered and paid is your leakage, and every peso of it is a session the unit gave and was not paid for.</p>
{{key:Delivered, documented, claimed, accepted, paid: five counts every month.}}
"""),
        ("exceptions", "Exceptions", "Fix the cause, not the number", """
<p>Keep an exceptions log: each session that did not move cleanly, why, who fixed it, and how. Then look for patterns. If agreement forms go unsigned on the evening shift, the fix is a step in the evening workflow, not a lecture. If new patients are not in the database before their first session, the fix is in intake.</p>
<p>Filing periods and rules change; PhilHealth has issued circulars on filing deadlines and extensions after disasters.[[pc_pc2025_0019]][[pc_pa2024_0057]] Assign someone to watch them. PhilHealth is also piloting shadow billing by diagnosis-related group (DRG) for hospital care; that pilot does not by itself change the hemodialysis package.[[pc_pc2026_0012]]</p>
{{key:Every exception has a cause. Fix the cause and the exception stops repeating.}}
"""),
        ("denials", "Returns and denials", "Returned and denied claims", """
<p>A returned claim can usually be corrected and refiled within the period the rules allow. A denied claim needs a reason and a decision: appeal with evidence, correct and resubmit where allowed, or write it off and fix the cause. Track the age of every open claim, because a claim not followed up becomes a claim lost.</p>
<p>Days to collect is an owner&rsquo;s number. It decides how much working capital the unit needs (Module 17).</p>
{{key:Every open claim has an age and an owner.}}
"""),
        ("integrity", "Integrity", "The integrity line", """
{{fig:duo15b}}
<p>Correcting a claim means completing true documentation of what happened, within the rules, and refiling on time. It never means creating documentation after the fact that implies something happened when it did not, changing a date or a diagnosis to fit a rule, claiming a session not delivered, or charging a patient for what the package covers.</p>
<p>A form signed today and dated to a past session is a false record, even if the session happened. The honest correction is a late signature dated today, with a note explaining why, if the rules allow it, or an accepted loss and a fixed workflow if they do not.</p>
{{stop:Never backdate a signature, claim an undelivered session, or change a date or diagnosis to fit a payment rule.}}
{{key:A true claim filed late is a problem. A false claim filed on time is fraud.}}
"""),
    ],
    "debrief": ["""
<p><strong>The suggestion.</strong> Backdating signatures creates false records. It must not happen.</p>
<p><strong>The right correction.</strong> Check what the rules allow for late completion. If allowed, obtain signatures dated today with an explanatory note and refile within the period. If not, accept the loss.</p>
<p><strong>Prevention.</strong> Find where the forms went unsigned, add a step at the end of each session to check the form, and track the exception rate monthly.</p>
"""],
    "skills": {"title": "Session-to-cash reconciliation and claims exception log",
               "intro": "Reconcile one fictional month of sessions from delivery to payment and build an exceptions log.",
               "items": [("Reports delivered, documented, claimed, accepted, and paid counts.", False),
                         ("Lists the cause of each exception and the system fix.", False),
                         ("Tracks the age and owner of every open claim.", False),
                         ("Refuses to backdate a signature or change a record to fit a rule.", True),
                         ("Refuses to claim an undelivered session.", True),
                         ("Reports days to collect to the board.", False)],
               "placement": "Ask your claims officer for last month&rsquo;s five counts and the reasons for each gap."},
    "quiz": [
        ("Which five counts make up a session-to-cash reconciliation?",
         ["Patients, nurses, machines, chairs, shifts", "Delivered, documented, claimed, accepted, paid", "Revenue, cost, profit, tax, cash", "Morning, afternoon, evening, night, weekend"],
         1, "Each count should equal the one before it."),
        ("Seven agreement forms were unsigned. A manager suggests backdated signatures. This is:",
         ["Acceptable if the sessions happened", "A false record that must not be made", "Required by PhilHealth", "A good workflow fix"],
         1, "Backdating creates a false record."),
        ("What does an exceptions log help the unit do?",
         ["Blame staff", "Find patterns and fix the cause", "Hide losses", "Avoid filing claims"],
         1, "Patterns point to system fixes."),
        ("Why track the age of every open claim?",
         ["To impress the board", "A claim not followed up within the filing rules can be lost", "To charge interest", "PhilHealth requires color codes"],
         1, "Age and ownership keep claims from expiring."),
        ("Which is a lawful correction?",
         ["Changing a diagnosis to fit a rule", "Completing true documentation and refiling within the period", "Claiming an extra session", "Charging the patient the denied amount"],
         1, "Correction means true documentation within the rules."),
        ("What number links claims to working capital?",
         ["Days to collect", "Number of chairs", "Staff age", "Water hardness"],
         0, "The longer collections take, the more cash the unit must finance."),
    ],
    "terms": [("Filing period", "The time allowed to submit a claim after a service.")],
    "readings": [("philhealth-acr-to-drg.html", "How PhilHealth payment is changing.")],
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
