# -*- coding: utf-8 -*-
"""Renal Social Worker, Module 19: Quality Improvement, Supervision, and Workload. Written for this series from published sources."""

MODULE = {
    "image_alt": "A social worker and a supervisor reviewing a simple run chart together in a small office.",
    "objectives": [
        "Define a social work quality measure with a clear numerator, denominator, time period, and stated limits.",
        "Plot a measure over time on a run chart and avoid claiming that a change caused an improvement without evidence.",
        "Choose measures that reflect what matters to patients, and avoid ranking workers by money raised or applications filed.",
        "Use supervision for case review, reflection, ethical dilemmas, and your own well-being.",
        "Estimate workload in hours, compare it with capacity, and report shortfalls in writing.",
    ],
    "big": """
{{plain:A measure is like a thermometer on a wall. It tells you the temperature in one place at one time. It does not tell you why the room is hot, and if someone holds a lighter under it, it will tell you a lie. A good measure is a well-placed thermometer that nobody can easily fool.}}
{{fig:sw19_measure}}
<p>The picture has a limit. A thermometer measures one thing that everyone agrees on. Social work outcomes are harder: a family&rsquo;s sense of being helped, a session not missed, a crisis that did not happen. You will rarely measure those directly. Instead you will measure processes (how fast referrals are answered, how many reach an outcome) and some outcomes (sessions missed, patient feedback), and you will be honest about what each can and cannot show.</p>
<p>Your job in this module is to show what the service does in numbers that mean something, to use supervision well, and to make workload visible. Measured psychosocial care is becoming part of kidney service standards elsewhere: a United Kingdom Delphi consensus of 26 experts and patient representatives recommended a holistic wellbeing assessment with validated tools for people approaching dialysis or transplant listing, with scores reported on a renal data dashboard.[[sw_coyne2023]] That is an English commissioning recommendation, not a Philippine rule, but it shows where the field is heading.</p>
{{cards:Key terms for this module|Measure::A defined count or rate tracked over time.|Numerator::The cases that met the measure (for example, referrals with a confirmed outcome).|Denominator::All the eligible cases (for example, all referrals due for an outcome).|Run chart::A simple line chart of a measure over time, with its median.|Supervision::Regular, structured time with a senior social worker for case review, reflection, and support.|Workload::The hours of work a caseload generates, compared with the hours available.}}
""",
    "case": {"title": "&ldquo;Our success rate is 100%&rdquo;", "html": """
<p>Friday, 2:00 p.m. The hospital&rsquo;s monthly quality report includes a slide from the previous social worker: &ldquo;Social Work Service: 100% success rate. All 45 assistance applications were submitted.&rdquo; The administrator asks you to keep the figure at 100% and to add &ldquo;total pesos raised&rdquo; as a performance measure for each social worker.</p>
<p>Your own records show that of 45 applications submitted in the quarter, 30 received a decision, 22 were approved in full or part, and you can confirm that support reached the household for 18. Separately, 12 patients missed three or more sessions in the quarter; you saw 7 of them.</p>
<p>You also notice that you worked 14 hours of overtime last month and have had no supervision session since you started four months ago.</p>
""", "questions": ["What is wrong with &ldquo;100% success rate,&rdquo; and what measures would you propose instead?",
                  "How do you respond to &ldquo;pesos raised&rdquo; as a performance measure?",
                  "What do you do about your overtime and the missing supervision?"]},
    "sections": [
        ("define", "Measures that mean something", "Numerator, denominator, period, limits", """
<p>A measure needs four parts: a numerator, a denominator, a time period, and a statement of what it cannot show. Without a defined denominator, a number is just a count; without stated limits, it invites false conclusions.</p>
{{formula:<strong>Worked example, illustrative.</strong> Rate = numerator &divide; denominator &times; 100.<br>Measure: referrals with a confirmed outcome within 30 days. Numerator: 10. Denominator: 12 referrals due in the month.<br>Rate = 10 &divide; 12 &times; 100 = 83.3%.<br>If the denominator is 0, the rate is not calculable (not 0%).<br>What the number tells you: how reliably referrals reached an outcome. What it does not tell you: whether the outcome helped, or why the other two did not close.}}
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>Type</th><th>What it can show</th><th>What it cannot</th></tr></thead>
<tbody>
<tr><td>Referrals acknowledged within 2 working days</td><td>Process</td><td>Responsiveness</td><td>Quality of the help</td></tr>
<tr><td>Referrals with a confirmed outcome</td><td>Process</td><td>Loop closure (Module 6)</td><td>Whether the outcome was good</td></tr>
<tr><td>New patients assessed within 10 working days</td><td>Process</td><td>Coverage of new starts</td><td>Depth of assessment</td></tr>
<tr><td>Patients with 3+ missed sessions seen by social work</td><td>Process</td><td>Reach to those at risk</td><td>Whether attendance improved</td></tr>
<tr><td>Patients screened for depression in the period</td><td>Process</td><td>Screening coverage</td><td>Treatment or recovery</td></tr>
<tr><td>Patient and family feedback</td><td>Experience</td><td>How help felt</td><td>Representativeness if few respond</td></tr>
</tbody></table></div>
<p>The toolkit&rsquo;s <a href="calc-social-worker-toolkit.html#tool-6">quality measure tool</a> computes a rate and refuses an impossible one (a numerator larger than the denominator, or a zero denominator).</p>
{{key:Every measure has a numerator, a denominator, a period, and stated limits. Zero over zero is not calculable.}}
"""),
        ("trend", "Trends, causes, and fair comparisons", "What a chart can and cannot claim", """
<p>Plot a measure monthly on a run chart, with its median. A single month up or down is usually noise. A sustained shift (several points in a row on one side of the median) suggests something real has changed. Even then, a chart does not prove that your change caused it. A new shift schedule, a new assistance program, a typhoon, or a change in patient mix could explain the movement.</p>
<p>Comparisons between workers or units are especially risky. Assistance approvals depend on agency budgets and policies. Attendance depends on poverty, distance, illness, and weather. A worker serving a poorer, sicker, more distant population will look worse on almost any raw measure.</p>
<div class="table-wrap"><table>
<thead><tr><th>Tempting measure</th><th>Problem</th><th>Better use</th></tr></thead>
<tbody>
<tr><td>Pesos raised per worker</td><td>Depends on agency budgets and patient need; rewards chasing money over care</td><td>Track household gaps closed, as a service measure, not a ranking</td></tr>
<tr><td>Applications submitted</td><td>Counts activity, not help</td><td>Decisions received and support confirmed (Module 8)</td></tr>
<tr><td>Attendance by worker</td><td>Driven by factors outside the worker&rsquo;s control</td><td>Reach and follow-up for patients at risk</td></tr>
</tbody></table></div>
{{key:A run chart shows change, not its cause. Never rank social workers by money raised or forms filed.}}
"""),
        ("supervision", "Supervision", "Time to think, protected", """
<p>Social work in kidney care brings hard material every week: poverty, violence, grief, death, families in conflict, decisions about stopping treatment. Supervision is where you take that material to think clearly about it. It is part of professional practice, not a sign of weakness.</p>
<div class="table-wrap"><table>
<thead><tr><th>Use supervision for</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>Case review</td><td>A stuck plan, a formulation you are unsure of</td></tr>
<tr><td>Ethical dilemmas</td><td>A conflict of interest, a confidentiality limit, a family pressing against the patient&rsquo;s wishes</td></tr>
<tr><td>Safety decisions</td><td>Safeguarding concerns, donor coercion signals</td></tr>
<tr><td>Your own reactions</td><td>A death that affected you, anger at a family, exhaustion</td></tr>
<tr><td>Workload and development</td><td>Priorities, learning goals, the development plan (Module 20)</td></tr>
</tbody></table></div>
<p>If your unit has no senior social worker, arrange supervision with your hospital&rsquo;s social work department, a peer in another facility, or a professional network, and agree a regular schedule in writing. Record supervision dates and decisions as your service requires.</p>
{{key:Book supervision regularly and use it for cases, ethics, safety, your reactions, and workload.}}
"""),
        ("workload", "Workload and safe caseloads", "Hours, not ratios", """
<p>No social worker staffing ratio for Philippine dialysis was identified in the documents reviewed (Module 3), and borrowing one from abroad would not fit local work. Instead, measure demand in hours. The <a href="calc-social-worker-toolkit.html#tool-5">workload tool</a> adds routine and complex episodes and fixed duties, and compares the total with the hours available.</p>
{{formula:<strong>Worked example, illustrative.</strong> Demand = (8 routine episodes &times; 45 min + 2 complex &times; 120 min) &divide; 60 + 5 fixed hours = 6 + 4 + 5 = 15 hours.<br>Available: 12 hours. Balance: &minus;3 hours. At 30 productive hours per FTE: 0.50 FTE.<br>What the number tells you: the gap between work and time. What it does not tell you: the right staffing, which is a management decision.}}
<p>When demand exceeds capacity, three things happen in order: triage by risk (Module 3), a written report to your head with the numbers and what is waiting, and a request for a decision (more hours, a covering worker, or explicit agreement on what will not be done). Chronic unpaid overtime hides the shortfall from the people who could fix it and burns out the person carrying it.</p>
{{key:Count workload in hours. Report a shortfall in writing with what is waiting and the risk.}}
{{scene:The overtime log|<p>Social worker Ms. Ivy Santos keeps a simple log of her overtime and of referrals waiting more than two weeks. After three months she brings it to her head.</p>
<p>The hospital assigns a second social worker to the dialysis unit two mornings a week.</p>
<p class="tc-scene-take">The shortfall became visible when it was written down in hours.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>&ldquo;100% success.&rdquo;</strong> It counts submissions, not help: every submission &ldquo;succeeded&rdquo; by definition. Propose instead: decisions received (30 of 45, 66.7%), approvals (22 of 30 decided, 73.3%), support confirmed reaching the household (18 of 45 submitted, 40.0%), and reach to patients with three or more missed sessions (7 of 12, 58.3%). State the limits: approvals depend on agency budgets, and reach does not show whether attendance improved. Plot them monthly.</p>
<p><strong>&ldquo;Pesos raised.&rdquo;</strong> Explain respectfully that money raised depends on agency budgets and patients&rsquo; needs, not only on the worker, and that ranking workers by it would reward chasing money over care and penalize workers serving the poorest patients. Offer a service-level measure instead: household gaps closed for patients at risk of missing treatment.</p>
<p><strong>Overtime and supervision.</strong> Run the workload tool with your real numbers and report the shortfall in writing to your head, with what is waiting and the risk. Ask for a supervision arrangement in writing: with the hospital&rsquo;s social work department head or a peer, on a regular schedule. Both protect patients as much as they protect you.</p>
"""],
    "skills": {"title": "A measure card and a workload report",
               "intro": "Define a measure, compute it, and present a workload report to a simulated manager while your supervisor observes.",
               "items": [
                   ("Defines a measure with numerator, denominator, period, and stated limits.", False),
                   ("Computes a rate correctly and states that 0 over 0 is not calculable.", False),
                   ("Explains why a run chart shows change but not its cause.", False),
                   ("Declines to rank workers by money raised or forms filed, and proposes a fair alternative.", True),
                   ("Estimates workload in hours and reports a shortfall in writing with risks.", False),
                   ("Arranges regular supervision and brings a case, an ethical question, and a personal reaction to it.", False),
               ],
               "placement": "Choose one measure for your service. Collect three months of data, plot a run chart, and discuss it with your supervisor."},
    "terms": [("Measure", "A defined count or rate tracked over time."),
              ("Numerator", "The cases that met the measure."),
              ("Denominator", "All the eligible cases."),
              ("Run chart", "A line chart of a measure over time with its median."),
              ("Supervision", "Regular structured time with a senior social worker."),
              ("Workload", "The hours of work a caseload generates.")],
    "readings": [("nephrology-workforce-crisis-or-opportunity.html", "The guide on nephrology workforce gaps.")],
    "calcs": ["calc-social-worker-toolkit.html#tool-6", "calc-social-worker-toolkit.html#tool-5"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["19"])
