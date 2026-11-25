# -*- coding: utf-8 -*-
"""OT/PT track, Module 19: Documentation, Quality and International Service Models. Written for this series from published sources."""

MODULE = {
    "image_alt": "Two therapists reviewing a run chart of patient sit-to-stand scores on a monitor in a quiet office.",
    "objectives": [
        "Write notes that carry the clinical decision, the measures and the plan, so the next clinician can act on them.",
        "Choose a small set of service measures (process and outcome) for a renal rehabilitation program.",
        "Use a run chart to tell whether a change is an improvement.",
        "Audit deferral and stop reasons to improve safety.",
        "Compare renal rehabilitation service models in the United States, United Kingdom, Australia and Canada, and judge what transfers to the Philippines.",
    ],
    "big": """
{{plain:A note is a baton in a relay (Module 1). A quality program is the coach watching the whole race from the stands, noticing that the team always drops the baton at the same corner.}}
<p>The picture has a limit. A coach can see the race. You usually cannot see your whole service: you see one patient at a time. So you need a few measures, collected the same way, plotted over time, to see the corner where the baton drops. This module is about writing each note well and then stepping back to look at the pattern.</p>
<p>What should you measure? Choose what matters to patients and what your service can change. Gait speed and sit-to-stand performance are good candidates because they are quick, repeatable, sensitive to rehabilitation, and associated with outcomes in kidney disease and older adults.[[otpt_roshanravan2013]][[otpt_studenski2011]] Adherence and safety events tell you whether the program is being delivered (Module 10).</p>
{{fig:otpt19_runchart}}
{{cards:Key terms for this module|Process measure::Whether the service did what it planned (screens done, sessions delivered).|Outcome measure::Whether patients changed (STS60, gait speed, goal attainment).|Balancing measure::An unintended effect to watch (falls, hypotension during sessions).|Run chart::Data plotted over time with a median line, to see change.|Audit::A structured review of practice against a standard.}}
""",
    "case": {"title": "Is the program working?", "html": """
<p><strong>Friday, 2:00 p.m.</strong> Six months after starting intradialytic exercise on the morning shift (Module 10), Dr. Ramon Uy asks PT Carlo Dizon and OT Bea Santiago: &ldquo;Is it working? The hospital wants to know whether to buy four more bikes.&rdquo;</p>
<p>They have monthly records: number of eligible patients, sessions offered and done, median STS60 for patients tested that month, and stops for dizziness. They also have a folder of session notes in which several deferrals say only &ldquo;not done.&rdquo;</p>
""", "questions": ["Which measures would you present, and how?",
                  "What would make you confident that STS60 changes are real?",
                  "What is wrong with the deferral notes, and how would you fix it?"]},
    "sections": [
        ("notes", "Notes that carry the decision", "Documentation that the next clinician can use", """
<p>A therapy note in renal care should answer six questions (Module 1): under what authority, with what consent, after what handoff, what was found, what was decided and why, and what happens next. Two common failures make notes useless: recording an activity without the decision (&ldquo;cycling 10 min&rdquo;), and recording a deferral without the reason (&ldquo;not done&rdquo;).</p>
<div class="table-wrap"><table>
<thead><tr><th>Weak note</th><th>Useful note</th></tr></thead>
<tbody>
<tr><td>&ldquo;Not done.&rdquo;</td><td>&ldquo;Deferred: dizzy on standing after 3.1 kg UF; nurse informed; BP per nurse; rebooked Thursday, non-dialysis day.&rdquo;</td></tr>
<tr><td>&ldquo;Exercise done, tolerated.&rdquo;</td><td>&ldquo;Pedal cycle 18 min at RPE 12, minutes 40&ndash;58 of HD; leg band 2 &times; 12; no symptoms; access undisturbed per nurse.&rdquo;</td></tr>
<tr><td>&ldquo;Improving.&rdquo;</td><td>&ldquo;STS60 15 (baseline 12, 3 months ago, same chair, non-dialysis morning); goal: rise from bleachers without help.&rdquo;</td></tr>
</tbody></table></div>
{{key:If it is not written with its reason, the next clinician cannot trust it and the audit cannot learn from it.}}
"""),
        ("measures", "Measuring a service", "Choosing measures and reading a run chart", """
<p>Pick a few measures and define them exactly: who is counted, when, how.</p>
<ul>
<li><strong>Process:</strong> percentage of eligible patients screened before each session; sessions done as a share of sessions offered; median minutes per session.</li>
<li><strong>Outcome:</strong> median STS60 or five-times sit-to-stand at 3, 6 and 12 months (same conditions); goal attainment.</li>
<li><strong>Balancing:</strong> sessions stopped for symptoms; falls; access events.</li>
</ul>
<p>A run chart plots a measure over time with its median. Common rules of thumb for a non-random signal include six or more consecutive points above or below the median (a shift) and five or more consecutive points going up or down (a trend). The site&rsquo;s <a href="calc-qapi-run-chart-spc.html">run chart tool</a> applies such rules. Annotate the chart with changes you made, so you can see whether a shift followed a change.</p>
{{formula:<strong>Illustrative interpretation.</strong> Median STS60 on the morning shift was 12 to 13 for the three months before the program (baseline median 12.5). After the program started, the monthly median ran 13, 14, 14, 15, 15, 16: six consecutive points above the baseline median, a shift. Sessions done were 70 percent of those offered; stops for dizziness were 2 per 100 sessions and did not rise. The shift is consistent with a real improvement, although patients joining and leaving the shift could also move the median; report who was tested each month.}}
{{key:Plot over time, annotate the changes, and count who was measured. A median that moves because the population changed is not an improvement.}}
"""),
        ("international", "Other countries", "International service models: what to borrow", """
<p>No country has a universal renal OT or PT credential, and models differ.</p>
<div class="table-wrap"><table>
<thead><tr><th>System</th><th>What the sources show</th><th>What may transfer</th><th>What needs separate checking</th></tr></thead>
<tbody>
<tr><td>United States</td><td>Federal conditions for dialysis facilities require comprehensive assessment including physical and functional status and referral for rehabilitation as needed; OT and PT are not listed as minimum team members.[[otpt_cfr494]]</td><td>Functional assessment built into the dialysis care plan; rehabilitation referral as a routine step</td><td>State licensing, direct-access rules, payer rules</td></tr>
<tr><td>United Kingdom</td><td>Health and Care Professions Council standards for OTs and physiotherapists; some kidney units employ specialist renal OTs.[[otpt_hcpc_ot]][[otpt_hcpc_pt]]</td><td>Integrated frailty, symptom and rehabilitation work within the renal team</td><td>Registration, banding and referral pathways</td></tr>
<tr><td>Australia</td><td>Government recognition of OTs and physiotherapists depends on board registration.[[otpt_aus_allied]]</td><td>Clear separation of registration and payment eligibility</td><td>Current board and payer conditions</td></tr>
<tr><td>Canada</td><td>A provincial renal program described an OT service covering home safety, mobility equipment, positioning and coping (a historical example).[[otpt_manitoba]]</td><td>Home and community focus within renal programs</td><td>Provincial registration and current staffing</td></tr>
</tbody></table></div>
<p>Borrow ideas, not rules. A practice that works in another system still has to pass Philippine law, local resources and the renal team&rsquo;s judgment.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What to present.</strong> A run chart of monthly median STS60 with the program start annotated; adherence (sessions done as a share of offered, minutes); and balancing measures (stops for symptoms, falls, access events). One slide, with definitions and the number of patients tested each month.</p>
<p><strong>Confidence that change is real.</strong> Standard test conditions; the same patients tracked where possible; a shift or trend on the run chart; stable or explained changes in who was tested; and no rise in harms. That supports a decision about more bikes, while being honest that a single unit&rsquo;s data are not a trial.</p>
<p><strong>The deferral notes.</strong> &ldquo;Not done&rdquo; hides whether the deferral was for safety, staffing, refusal or equipment. Carlo and Bea add a short reason field to the session template (for example: symptoms, observations outside parameters, patient declined, staff unavailable, equipment) and audit it monthly. Staffing and equipment deferrals are fixable service problems; symptom deferrals tell the renal team something about the sessions.</p>
"""],
    "skills": {"title": "Documentation and a service measure",
               "intro": "Rewrite weak notes and build a run chart from a simulated data set with your preceptor.",
               "items": [
                   ("Rewrites three weak notes to include authority, findings, decision, reason and plan.", False),
                   ("Defines one process, one outcome and one balancing measure exactly.", False),
                   ("Builds a run chart with a median and annotates a change.", False),
                   ("Interprets a shift or trend and names an alternative explanation.", False),
                   ("Codes deferral reasons and identifies which are fixable service problems.", False),
                   ("Explains one international model and what would need checking before adopting it.", False),
               ],
               "placement": "Collect three months of one measure in your service and present a run chart to your team."},
    "terms": [("Run chart", "A measure plotted over time with its median."), ("Shift", "Several consecutive points on one side of the median."),
              ("Balancing measure", "An unintended effect monitored alongside the main measure."), ("Audit", "A structured review against a standard.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality management in dialysis units."),
                 ("nephrology-workforce-crisis-or-opportunity.html", "Workforce models in nephrology.")],
    "calcs": ["calc-qapi-run-chart-spc.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["19"])
