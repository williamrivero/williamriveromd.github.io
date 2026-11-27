# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 13: Inspection Readiness, Audits, and Quality Metrics. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer presenting an evidence index binder to an inspector in a dialysis clinic office.",
    "objectives": [
        "Keep an evidence index that links each requirement to its authority, evidence, owner, and verification date.",
        "Conduct an inspection-day disclosure lawfully and log what was shown or copied.",
        "Define a metric&rsquo;s numerator, denominator, period, and exclusions before counting.",
        "Report a rate with its 95% confidence interval and choose a sample size that gives a useful answer.",
        "Close the improvement loop with a verified cause, an owner, and a repeat measurement using the same definition.",
    ],
    "big": """
{{plain:Inspection readiness is like keeping your house tidy. If you clean only when guests ring the doorbell, they find you sweating, with dust under the sofa. If you tidy a little every day, the doorbell is no emergency. An inspector is a guest who checks under the sofa.}}
<p>The picture is useful, and it has one limit. A tidy house only has to look clean. A dialysis unit has to <em>prove</em> it was clean on every day the inspector asks about, including days months ago. Readiness is not a performance put on the week before a visit. It is the habit of being able to show, on any day, the evidence behind every requirement.</p>
<p>Metrics are how the unit learns whether it is improving between visits. But a rate from a small sample can mislead in both directions, and a rate whose definition shifts from month to month measures nothing. This module covers both halves: having the evidence, and measuring honestly.</p>
{{cards:Key terms for this module|Evidence index::A table linking each requirement to its authority, evidence, owner, and the date it was last verified.|Numerator::The counted successes.|Denominator::The eligible total that the successes are counted out of.|Confidence interval (CI)::The range in which the true rate plausibly lies, given the sample.|Corrective action::A change made to fix a verified cause, followed by a repeat measurement.}}
""",
    "case": {"title": "Eighty percent", "html": """
<p>Your unit&rsquo;s policy requires every run sheet to be signed by the end of the next working day. You review a random sample of 20 eligible sessions from November. Sixteen were signed on time. All four late ones fall on Saturday afternoons.</p>
<p>Ms. Teresita Aquino, the unit manager, reads your summary. &ldquo;Eighty percent. That&rsquo;s fine. I&rsquo;ll report &lsquo;80% compliance&rsquo; to the owner and we can move on.&rdquo;</p>
""", "questions": ["How should the result be reported?",
                  "What would you do about the Saturday pattern?",
                  "How will anyone know whether the fix worked?"]},
    "sections": [
        ("index", "The evidence index", "Requirement, evidence, owner, date", """
<p>Keep one row per requirement, with six columns: the requirement, its authority and version, the evidence artifact, where it is kept, its owner, and the date it was last verified. The &ldquo;last verified&rdquo; column is the one that matters on inspection day. It shows that someone looked recently, not just that a document once existed.</p>
<p>Typical rows for a dialysis unit include:</p>
<ul>
<li>the records officer&rsquo;s designation and training certificate (Module 1);</li>
<li>the approved records manual with its revision date;</li>
<li>standing orders updated quarterly and consents updated annually or as needed (Module 2);</li>
<li>sample complete charts;</li>
<li>registry acknowledgments (Module 7);</li>
<li>release, retrieval, and disposition logs (Modules 8 and 10);</li>
<li>access reviews (Module 11) and the downtime drill report (Module 12);</li>
<li>indexed dialyzer and water logs;</li>
<li>the Philippine Health Insurance Corporation (PhilHealth) accreditation and the Department of Health (DOH) license on file.[[dch_doh_rao_tool]][[mro_ph2025acc]]</li>
</ul>
<h3>On inspection day</h3>
<p>Verify the inspector&rsquo;s identity and authority before showing anything, as you would any other requester (Module 8). Follow the facility&rsquo;s disclosure procedure. Show what is requested; do not volunteer whole charts when a sample page will do. Log exactly what was shown or copied, to whom, and when. If an inspector asks for something you cannot find, say so and write it down. A gap honestly acknowledged is a finding. A document produced overnight is a different problem (Module 4).</p>
{{scene:The inspector&rsquo;s first request|<p>An inspector&rsquo;s first request is: &ldquo;Show me the last quarter&rsquo;s standing-order renewals for five patients I choose.&rdquo;</p>
<p>The records officer opens the evidence index, finds the row with its location and last-verified date, and retrieves the five charts in four minutes. The inspector moves on to the next item.</p>
<p class="tc-scene-take">Readiness is measured in minutes, on the day, for the item the inspector chooses.</p>}}
{{fig:mro13_fig_13_evidence_index_last_verified}}
"""),
        ("define", "Define first", "Define before you count", """
<div class="table-wrap"><table>
<thead><tr><th>Metric</th><th>Numerator</th><th>Denominator</th></tr></thead>
<tbody>
<tr><td>Chart completeness</td><td>Charts with all applicable required items</td><td>Eligible charts reviewed</td></tr>
<tr><td>Authentication timeliness</td><td>Sessions authenticated by the local deadline</td><td>Eligible sessions reviewed</td></tr>
<tr><td>Duplicate rate</td><td>Confirmed duplicate pairs</td><td>Master patient index records (per 1,000)</td></tr>
<tr><td>Release turnaround</td><td colspan="2">Median days from complete request to release</td></tr>
</tbody></table></div>
<p>Write the period, the selection method, and any exclusions <strong>first</strong>, before you look at a single chart. If you decide what counts after seeing the results, you will, without meaning to, define the metric in the way that looks best.</p>
<p>Items that are legitimately not applicable are excluded from the denominator under a written rule. They are not counted as failures, and they are not quietly dropped. A session canceled before treatment has no run sheet to sign; it is excluded from authentication timeliness by rule, and the rule says so.</p>
<p>PhilHealth&rsquo;s quality-standards circular for maintenance hemodialysis is a useful source of documentation items to audit.[[dch_philhealth2024q]]</p>
{{scene:The rate that rose by itself|<p>A unit&rsquo;s chart completeness rose from 72% to 91% in one month, and the manager wants to celebrate. The records officer compares the two audit sheets and finds that the second month excluded &ldquo;patients who started this month&rdquo; from the denominator. New patients are the ones most likely to have incomplete charts.</p>
<p>Recomputed with the original definition, the second month was 76%. Still better, but not a celebration.</p>
<p class="tc-scene-take">Write the definition before counting, or the definition will drift toward good news.</p>}}
"""),
        ("uncertainty", "Uncertainty", "Report the interval with the rate", """
{{fig:mro13_loop}}
<p>A rate from a sample is an estimate. The confidence interval (CI) says how far the true rate could plausibly be from it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Sample</th><th>Rate</th><th>95% confidence interval (Wilson method)</th></tr></thead>
<tbody>
<tr><td>16 of 20</td><td>80%</td><td>About 58% to 92%</td></tr>
<tr><td>48 of 60</td><td>80%</td><td>About 68% to 88%</td></tr>
</tbody></table></div>
<p>Both samples give 80%. The first could be hiding a true rate as low as 58%, which no manager would call &ldquo;fine.&rdquo; The second rules that out. Small samples give wide ranges, and a wide range means the sample has not yet answered the question.</p>
<p>How big a sample do you need? To estimate a rate near 80% within 10 percentage points, about <strong>62</strong> eligible items. Near 50%, about <strong>97</strong>. The toolkit calculator does the arithmetic. Always report numerator, denominator, and interval together.</p>
<h3>Some findings cannot wait</h3>
<p>Metrics are for patterns. Some single findings go to the right owner immediately, not into next month&rsquo;s report: a wrong-patient document (Module 3), a privacy incident (Module 8), or a pattern suggesting billing for care not delivered (Module 6).</p>
<h3>Closing the loop</h3>
<p>For everything else, close the loop.</p>
{{flow:Closing the loop|Verify the cause::Ask the people involved; do not assume.|Choose an intervention::Small, specific, testable.|Name an owner and a due date::Someone who can make it happen.|Measure again::Same definition, same sampling, a fixed time later.|Report both results::With numerators, denominators, and intervals.}}
<p>Store metrics as aggregates. Keep the patient-level worksheets protected; they contain personal information and are not needed once the rate is computed and checked.</p>
{{key:Same definition, same sampling, before and after, or the comparison means nothing.}}
{{scene:Twenty, then sixty|<p>After a weekend handover queue for unsigned run sheets is introduced, the records officer resamples. Before: 16 of 20 signed on time, 80% (95% confidence interval 58% to 92%). After: 57 of 62, 92% (about 82% to 96%).</p>
<p>The intervals still overlap, so the improvement is likely but not yet proven. The Saturday-afternoon late signatures have disappeared, which fits the cause the charge nurse described. The manager reports both numbers to the owner, with their intervals and the same definition, and the audit is repeated the following month.</p>
<p class="tc-scene-take">A larger sample and the same definition turned a guess into a measured, honestly qualified result.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>Reporting.</strong> &ldquo;16 of 20 sessions signed on time, 80% (95% confidence interval 58% to 92%), random sample of eligible November sessions.&rdquo; Explain to Ms. Aquino, in one sentence, that with 20 sessions the true rate could be anywhere in that range, and that a sample of about 62 would narrow it to within 10 points.</p>
<p><strong>The pattern.</strong> Four of four late sessions on Saturday afternoons is too neat to ignore, but do not assume the cause. Ask the Saturday charge nurse. It may be a short-staffed shift, a physician who signs only on weekdays, or run sheets that reach the records room on Monday. Then test a specific fix, such as a weekend handover queue for unsigned run sheets, with an owner and a due date.</p>
<p><strong>Did it work?</strong> Repeat the same random sampling a month later, with the same definition and preferably a larger sample. Report both results with their numerators, denominators, and intervals. If the intervals barely overlap, you have evidence of change. If they overlap heavily, you need more data before claiming success.</p>
<p>&ldquo;Eighty percent&rdquo; was not wrong. It was incomplete in a way that could have hidden a real problem on Saturday afternoons. Part of your role is to report what the numbers can and cannot tell the owner.</p>
"""],
    "skills": {"title": "Evidence index and metric",
               "intro": "Build a mock evidence index and report one metric with its interval while your preceptor observes.",
               "items": [
                   ("Links each requirement to authority, artifact, location, owner, and verification date.", False),
                   ("Verifies an inspector&rsquo;s authority and logs what was shown.", False),
                   ("Defines numerator, denominator, period, and exclusions before sampling.", False),
                   ("Reports the rate with its 95% confidence interval and states the sample size needed.", False),
                   ("Escalates a patient-safety, privacy, or billing-integrity finding immediately.", True),
                   ("Verifies a cause with staff before choosing an intervention.", False),
                   ("Plans a repeat measurement with the same definition and sampling.", False),
               ],
               "placement": "Take one indicator your unit already reports and write down its numerator, denominator, and exclusions. Check whether its last report included an interval."},
    "terms": [("Evidence index", "A table linking requirements to evidence."), ("Numerator", "The counted successes."),
              ("Denominator", "The eligible total."), ("CI", "Confidence interval."),
              ("Corrective action", "A change made to fix a verified cause, followed by re-measurement.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["13"])
