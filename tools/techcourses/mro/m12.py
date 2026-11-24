# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 12: Downtime and Recovery. Written for this series from published sources."""

MODULE = {
    "image_alt": "A nurse and a records officer comparing a numbered paper downtime sheet with a laptop at a dialysis nurses' station.",
    "objectives": [
        "Prepare and activate the approved downtime procedure.",
        "Run downtime documentation that can be reconciled later.",
        "Reconcile paper and electronic records after recovery without creating duplicates.",
        "Close the event with counts that balance.",
    ],
    "big": """
{{plain:Dialysis cannot stop because a server did. When the electronic record goes down, the unit keeps treating patients on paper, and for a few hours or days there are two records of the same care.}}
<p>The danger lies less in the outage than in the improvisation that follows. The records officer&rsquo;s job is to make sure the paper record created during downtime is complete enough to reconcile, and then to reconcile it entry by entry.</p>
{{cards:Key terms for this module|Downtime::A period when the electronic system is fully or partly unavailable.|Downtime ID::A pre-printed number on each paper sheet.|Back-entry::Entering paper-documented care into the electronic record after recovery.|Reconciliation::Matching records from different sources until every item is accounted for.|Electronic medical record (EMR)::Electronic medical record.}}
""",
    "case": {"title": "Six hours dark", "html": """
<p>After a six-hour outage, four paper sheets come back to you. DT-01 matches an entry already in the electronic record exactly. DT-02 is signed but has no electronic match. DT-03 lacks the clinician&rsquo;s signature. DT-04 lists a name that matches two patients. The claims clerk wants to bill all four sessions today.</p>
""", "questions": ["What is the disposition of each sheet?",
                  "Do the counts balance?",
                  "What do you tell the claims clerk?"]},
    "sections": [
        ("evidence", "Why it matters", "What downtime studies show", """
<p>In an analysis of 76 patient-safety reports tied to downtime, 46% said downtime procedures were either not followed or not in place, and only 27.6% described a procedure carried out successfully; patient identification and communication of clinical information were the main hazards.[[mro_larsen2018]] In a two-hospital study, laboratory results were delayed by an average of 62% during downtime, and the paper downtime records were themselves incomplete.[[mro_larsen2019]] Downtime is common: one hospital logged 204 events over four and a half years, 96% of them unplanned.[[mro_fang2025]] At national scale, the 2023 ransomware attack on PhilHealth forced the payer itself into manual operations.[[mro_ph2023medusa]]</p>
"""),
        ("during", "Before and during", "Readiness and downtime documentation", """
<p><strong>Before:</strong> a printed downtime kit per station &mdash; blank run sheets with pre-numbered downtime IDs, the current patient list with two identifiers each, current standing orders printed at a set interval such as every shift, the contact list, and the procedure &mdash; and a drill at least yearly, with the records officer checking documentation quality.</p>
<p><strong>During:</strong> every paper document carries its downtime ID, the patient&rsquo;s two identifiers, date and time, and the author&rsquo;s signature. Sheets are collected and secured each shift, a downtime log tracks each sheet issued, completed, and collected, and clinical questions go to the clinical team; the records officer never reconstructs missing values.</p>
{{call:A shared emergency password to speed up recovery destroys attribution. Use the approved, logged emergency-access procedure.}}
"""),
        ("after", "After recovery", "Three lists, one truth", """
{{fig:mro12_lists}}
<p>For every expected encounter during the outage, compare three lists: the schedule, the paper sheets, and the electronic record, including entries made just before the outage.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Paper matches an existing electronic entry</td><td>Record as matched; do not create a second session</td></tr>
<tr><td>Signed paper, no electronic entry</td><td>Back-enter as an attributable late entry; keep the paper per policy</td></tr>
<tr><td>Paper lacks the clinician&rsquo;s signature</td><td>Query the author; hold</td></tr>
<tr><td>Ambiguous identity</td><td>Identity exception (Module 3)</td></tr>
<tr><td>Expected encounter, no paper, no electronic entry</td><td>Ask the clinical team whether the treatment occurred; document the answer</td></tr>
</tbody></table></div>
{{formula:Sheets recovered = matched + back-entered + pending author query + identity exceptions.}}
<p>A two-person reconciliation, one reading and one checking, is a strong local control. Close the event with a short report: duration, encounters affected, counts, open exceptions, and lessons for the next drill. Sessions captured on paper are claimable only after they are authenticated and back-entered.</p>
{{key:Downtime paper is a parallel record. Reconcile it; do not just file it.}}
"""),
    ],
    "debrief": ["""
<p><strong>Dispositions.</strong> DT-01: matched, no new session. DT-02: back-entered as an attributable late entry. DT-03: author query, held. DT-04: identity exception.</p>
<p><strong>Counts.</strong> Four sheets = 1 matched + 1 back-entered + 1 pending query + 1 exception. Balanced.</p>
<p><strong>Claims.</strong> DT-01 is already in the record; DT-02 can be claimed once back-entered; DT-03 and DT-04 stay on hold until resolved.</p>
"""],
    "skills": {"title": "Downtime reconciliation",
               "intro": "Reconcile a fictional set of downtime sheets against a schedule and a restored record with a preceptor.",
               "items": [
                   ("Checks that each sheet has a downtime ID, two identifiers, time, and signature.", False),
                   ("Records a match without creating a duplicate session.", True),
                   ("Back-enters only authenticated sheets as attributable late entries.", True),
                   ("Balances the counts and lists open exceptions.", False),
                   ("Holds downtime sessions from claims until authenticated and back-entered.", True),
               ],
               "placement": "Open your unit&rsquo;s downtime kit. Check that the patient list and standing orders are current."},
    "terms": [("Downtime", "A period when the electronic system is unavailable."), ("Downtime ID", "A pre-printed number on each paper sheet."),
              ("Back-entry", "Entering paper-documented care into the electronic record after recovery."),
              ("Reconciliation", "Matching records from different sources until every item is accounted for."),
              ("EMR", "Electronic medical record.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["12"])
