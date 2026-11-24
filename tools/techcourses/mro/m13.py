# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 13: Inspection Readiness, Metrics, and Improvement. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and a quality lead reviewing a run chart and an evidence binder in a small dialysis office.",
    "objectives": [
        "Map each inspection requirement to a piece of evidence.",
        "Define a metric&rsquo;s numerator, denominator, period, and sampling method before sampling.",
        "Report a rate honestly, with its 95% confidence interval.",
        "Run a corrective action through a repeat measurement.",
    ],
    "big": """
{{plain:Inspection readiness is not a performance put on the week before the inspector arrives. It is the habit of being able to show, on any day, the evidence behind every requirement.}}
<p>Metrics are how the unit learns whether it is improving. But a rate from a small sample can mislead in both directions, and a rate whose denominator shifts from month to month measures nothing.</p>
{{cards:Key terms for this module|Evidence index::A table linking each requirement to its evidence, owner, and verification date.|Numerator::The counted successes.|Denominator::The eligible total.|Confidence interval (CI)::Confidence interval; the range in which the true rate plausibly lies.|Corrective action::A change made to fix a verified cause, followed by re-measurement.}}
""",
    "case": {"title": "Eighty percent", "html": """
<p>You review 20 eligible sessions from November: 16 were authenticated by the unit&rsquo;s deadline. The four late notes all fall on Saturday afternoons. The unit manager wants to report &ldquo;80% compliance&rdquo; to the owner and move on.</p>
""", "questions": ["How should the result be reported?",
                  "What would you do about the Saturday pattern?",
                  "How will anyone know whether the fix worked?"]},
    "sections": [
        ("index", "The evidence index", "Requirement, evidence, owner, date", """
<p>Keep one row per requirement: requirement, authority and version, evidence artifact, location, owner, and date last verified. Typical rows include the MRO designation and training certificate, the approved records manual, standing orders updated quarterly, consents updated annually or as needed, sample complete charts, registry acknowledgments, release, retrieval, and disposition logs, access reviews, the downtime drill report, indexed dialyzer and water logs, and PhilHealth accreditation and the DOH license on file.[[dch_doh_rao_tool]][[mro_ph2025acc]] On inspection day, verify the inspector&rsquo;s authority, follow the disclosure procedure, and log exactly what was shown or copied.</p>
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
<p>Write the period, the selection method, and any exclusions <strong>first</strong>. Items that are legitimately not applicable are excluded from the denominator under a written rule, not counted as failures and not quietly dropped. PhilHealth&rsquo;s quality-standards circular for maintenance hemodialysis is a useful source of documentation items to audit.[[dch_philhealth2024q]]</p>
"""),
        ("uncertainty", "Uncertainty", "Report the interval with the rate", """
{{fig:mro13_loop}}
<p>Small samples give wide ranges. If 16 of 20 sessions are authenticated on time, the rate is 80%, but the 95% confidence interval (Wilson method) runs from about <strong>58% to 92%</strong>. With 48 of 60, the rate is still 80%, but the interval narrows to about <strong>68% to 88%</strong>. To estimate a rate near 80% within 10 percentage points, you need about <strong>62</strong> eligible items; near 50%, about <strong>97</strong>. The toolkit calculator does the arithmetic; always report numerator, denominator, and interval together.</p>
<p>Some findings cannot wait for the monthly report: a wrong-patient document, a privacy incident, or a pattern suggesting billing for care not delivered goes to the right owner immediately. For everything else, close the loop: a cause verified with staff, an intervention, an owner, a due date, and a <strong>repeat measurement</strong> with the same definition and sampling. Store metrics as aggregates; keep patient-level worksheets protected.</p>
{{key:Same definition, same sampling, before and after &mdash; or the comparison means nothing.}}
"""),
    ],
    "debrief": ["""
<p><strong>Reporting.</strong> 16 of 20, 80% (95% CI 58% to 92%), with the period and sampling method stated. Say plainly that the true rate could be anywhere in that range.</p>
<p><strong>The pattern.</strong> Confirm the cause with the Saturday charge nurse rather than assuming it, then test a fix such as a weekend handover queue for unsigned run sheets, with an owner and a due date.</p>
<p><strong>Did it work?</strong> Repeat the same sampling a month later with the same definition, and report both results with numerators, denominators, and intervals.</p>
"""],
    "skills": {"title": "Evidence index and metric",
               "intro": "Build a mock evidence index and report one metric with its interval with a preceptor.",
               "items": [
                   ("Links each requirement to authority, artifact, owner, and verification date.", False),
                   ("Defines numerator, denominator, period, and exclusions before sampling.", False),
                   ("Reports the rate with its 95% confidence interval.", False),
                   ("Escalates a patient-safety, privacy, or billing-integrity finding immediately.", True),
                   ("Plans a repeat measurement with the same definition and sampling.", False),
               ],
               "placement": "Take one indicator your unit already reports and write down its numerator, denominator, and exclusions."},
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
