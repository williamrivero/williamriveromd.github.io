# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 02: The Dialysis Chart and Its Technical Records. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer cross-checking a run sheet against a dialyzer reprocessing log beside a records cabinet.",
    "objectives": [
        "Map the longitudinal chart and the per-session record.",
        "Explain what the order, the run sheet, and the technical logs each prove.",
        "Index dialyzer reprocessing, water treatment, and machine maintenance records and cross-reference them to sessions.",
        "Mark every expected item present, deficient, unavailable, or not applicable, and route each deficiency to its owner.",
    ],
    "big": """
{{plain:Every dialysis session must answer three questions. Was it authorized? Was it delivered? Was it safe? A different document answers each one, and an inspector, a payer, or a court may ask all three.}}
<p>The signed dialysis order answers the first. The run sheet and nursing notes answer the second. The third answer lives outside the patient&rsquo;s folder: in the dialyzer reprocessing log, the water-quality log, and the machine maintenance record. A records officer who indexes only the first two leaves the unit unable to prove the third.</p>
{{cards:Key terms for this module|Run sheet::The per-treatment flow sheet: weights, blood pressures, duration, events, signatures.|Standing order::The current dialysis prescription that applies to every session until changed.|Reprocessing::Cleaning, testing, and disinfecting a dialyzer for reuse by the same patient.|Deficiency::A required item that is unsigned, illegible, outdated, incomplete, or missing.|PhilHealth Dialysis Database (PDD)::PhilHealth Dialysis Database.}}
""",
    "case": {"title": "Reuse five, entry missing", "html": """
<p>During a weekly audit you open a fictional chart, SIM-044. The November 18 run sheet is signed, shows a pre-dialysis weight and both blood pressures, and lists dialyzer D-044-07, reuse 5. The final weight box is blank. In the reprocessing log, D-044-07 shows reuse 4 on November 15 and nothing afterward. The patient has been issued 26 dialyzers this year.</p>
""", "questions": ["Which items are deficient, and who owns each one?",
                  "Why is the missing reprocessing entry more than a paperwork gap?",
                  "How many dialyzers remain in this patient&rsquo;s annual allowance?"]},
    "sections": [
        ("longitudinal", "The chart", "The longitudinal chart", """
<p>The longitudinal chart is kept for as long as the patient dialyzes with you. It holds intake demographics and identifiers; the referral and clinical abstract; the initial physician assessment and problem list; standing dialysis orders, which the posted DOH assessment tool expects to be updated <strong>quarterly</strong>; consent for hemodialysis (HD), updated <strong>annually or as needed</strong>; laboratory and imaging results; the medication list; nutrition, education, and social-work notes; vascular access history; hospitalizations; an advance directive or a documented statement that none exists; and PhilHealth Dialysis Database (PDD) registration.[[dch_doh_rao_tool]]</p>
<p>PhilHealth&rsquo;s minimum standard of care for the HD package names scheduled laboratory tests, including albumin every three months and a hepatitis profile every six months as indicated, so the laboratory section is also claims evidence.[[mro_ph2024ts]]</p>
"""),
        ("layers", "Three layers", "Authorized, delivered, safe", """
{{fig:mro02_layers}}
<p>The <strong>run sheet</strong> is the primary proof that care was delivered: date and shift, station and machine, pre- and post-dialysis weight and blood pressure, duration, events, medications given, the dialyzer and its reuse number, and the authenticating signatures. A schedule entry or attendance list is much weaker evidence.</p>
<p>The <strong>technical logs</strong> belong to technical staff; the records officer makes sure they are complete, dated, attributed, retrievable, and cross-referenced to sessions. PhilHealth&rsquo;s minimum standard allows up to 32 dialyzers per patient per calendar year, each reusable up to five times.[[mro_ph2024ts]] Every reuse must link to the right patient and show the reprocessing date, germicide and contact time, residual-germicide test, and a performance test such as fiber bundle volume. A reprocessed dialyzer used on the wrong patient is a bloodborne-infection event, so this log is an <strong>identity</strong> record as much as a technical one.</p>
{{key:Order proves authorized. Run sheet proves delivered. Technical logs prove safe.}}
"""),
        ("deficiency", "Deficiencies", "Four states, one owner each", """
<div class="table-wrap"><table>
<thead><tr><th>State</th><th>Meaning</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Present</td><td>Exists, current, complete, authenticated</td><td>Signed standing order within the quarter</td></tr>
<tr><td>Deficient</td><td>Exists but unsigned, illegible, outdated, or incomplete</td><td>Run sheet with a blank final weight</td></tr>
<tr><td>Unavailable</td><td>Should exist; cannot be found</td><td>Reprocessing entry for a logged reuse</td></tr>
<tr><td>Not applicable</td><td>Excluded under a written applicability rule</td><td>Item that the rule says does not apply</td></tr>
</tbody></table></div>
<p>Each deficiency gets an owner, a due date, and closure evidence.</p>
{{call:Anything that could affect the next treatment &mdash; an expired standing order, a missing current prescription, an unsigned order after a dose change, a dialyzer that cannot be traced to its patient &mdash; goes to the clinical team before that session. Never fill a clinical field yourself, even when the value seems obvious from another document.}}
"""),
    ],
    "debrief": ["""
<p><strong>Deficiencies.</strong> The blank final weight goes to the assigned nurse for review of contemporaneous evidence and an attributed late entry if appropriate. The missing reprocessing entry for reuse 5 goes the same day to the reprocessing technician and supervisor.</p>
<p><strong>Why it matters.</strong> Without the entry, no one can show that the dialyzer used on November 18 was tested and belonged to this patient. That is a possible identity and infection risk, not only missing paperwork. Do not create the entry yourself.</p>
<p><strong>The allowance.</strong> 32 minus 26 leaves 6 dialyzers for the rest of the year.</p>
"""],
    "skills": {"title": "Chart and technical-log audit",
               "intro": "Audit a fictional chart and trace one session to its dialyzer, water, and machine records with a preceptor.",
               "items": [
                   ("Marks each expected item present, deficient, unavailable, or not applicable under a written rule.", False),
                   ("Routes every clinical deficiency to its author without filling any clinical field.", True),
                   ("Escalates a deficiency affecting the next treatment before that session.", True),
                   ("Traces a session to its dialyzer reprocessing entry, water log, and machine record.", False),
                   ("Retrieves the current standing order and its superseded version.", False),
               ],
               "placement": "Pick one session from last week and trace it from run sheet to dialyzer, water, and machine records."},
    "terms": [("Run sheet", "The per-treatment flow sheet."), ("Standing order", "The current dialysis prescription."),
              ("Reprocessing", "Cleaning, testing, and disinfecting a dialyzer for reuse by the same patient."),
              ("Fiber bundle volume", "A test of how much of a dialyzer&rsquo;s blood path remains open after reuse."),
              ("Deficiency", "A required item that is unsigned, illegible, outdated, incomplete, or missing."),
              ("PDD", "PhilHealth Dialysis Database.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "How dialyzers are reprocessed and reused safely.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["02"])
