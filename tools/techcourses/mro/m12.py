# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 12: Downtime, Recovery, and Reconciliation. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dialysis nurse writing on a paper downtime sheet while a computer screen shows the system is unavailable.",
    "objectives": [
        "Summarize what published studies show about patient safety during electronic record downtime.",
        "Prepare a downtime kit and check its currency before an outage.",
        "State what every paper downtime document must carry.",
        "Reconcile the schedule, the paper sheets, and the electronic record after recovery, and balance the counts.",
        "Hold downtime sessions from claims until they are authenticated and back-entered.",
    ],
    "big": """
{{plain:When the power fails at home, you light candles and carry on. The trouble comes later: food spoiled in the refrigerator, clocks blinking the wrong time, something forgotten in the dark. Downtime in a dialysis unit is the same. The treatments carry on. The trouble is what the dark leaves behind.}}
<p>The picture is useful, and it has one limit. At home, the clocks are reset in a minute. In a dialysis unit, every session treated during the outage now exists in two places that do not agree: on paper, and partly or not at all in the electronic record. Until someone reconciles them, the unit does not know for certain who was treated, with what, and by whom.</p>
<p>Dialysis cannot stop because a server did. When the electronic record goes down, the unit keeps treating patients on paper. The danger lies less in the outage than in the improvisation that follows: sheets without identifiers, values remembered later, and sessions entered twice. The records officer&rsquo;s job is to make sure the paper created during downtime is complete enough to reconcile, and then to reconcile it entry by entry.</p>
{{cards:Key terms for this module|Downtime::A period when the electronic system is fully or partly unavailable, planned or unplanned.|Downtime kit::The printed forms, lists, orders, and contacts kept ready at each station for an outage.|Downtime ID::A pre-printed serial number on each paper sheet, so every sheet can be counted.|Back-entry::Entering paper-documented care into the electronic record after recovery, as an attributable late entry.|Reconciliation::Matching records from different sources until every item is accounted for.|Electronic medical record (EMR)::The digital record of patient care within the unit.}}
""",
    "case": {"title": "Six hours dark", "html": """
<p>On a Saturday, the electronic medical record (EMR) goes down at 6:15 a.m. and comes back at 12:20 p.m. Both morning shifts dialyze on paper. On Monday, four completed downtime sheets reach your desk.</p>
<ul>
<li>DT-01, for Mr. Victor Mercado, matches an entry already in the EMR exactly. The nurse had started the electronic entry at 6:05 a.m., before the outage.</li>
<li>DT-02, for Mrs. Adelaida Flores, is complete and signed. There is no electronic entry.</li>
<li>DT-03, for Mr. Ronaldo Uy, is complete except for the nurse&rsquo;s signature.</li>
<li>DT-04 says only &ldquo;Rodriguez, F.&rdquo; Two patients match: Felipe Rodriguez and Fernando Rodriguez, brothers who dialyze on the same Saturday shift.</li>
</ul>
<p>Mr. Boyet Ramos from claims stops by. &ldquo;Can I bill all four Saturday sessions today? The batch closes this afternoon.&rdquo;</p>
""", "questions": ["What is the disposition of each sheet?",
                  "Do the counts balance?",
                  "What do you tell Mr. Ramos?"]},
    "sections": [
        ("evidence", "Why it matters", "What downtime studies show", """
<p>Downtime is not rare, and the evidence says it is dangerous mainly because procedures are missing or not followed.</p>
<p>In an analysis of 76 patient-safety reports tied to electronic health record downtime, 46% said downtime procedures were either not followed or not in place, and only 27.6% described a procedure carried out successfully. Patient identification and communication of clinical information were the main hazards.[[mro_larsen2018]] In a two-hospital study, laboratory results were delayed by an average of 62% during downtime, and the paper downtime records were themselves incomplete.[[mro_larsen2019]] Downtime is also common: one hospital logged 204 events over four and a half years, 96% of them unplanned.[[mro_fang2025]]</p>
<p>These studies come from hospitals, and safety reports capture only what someone chose to report, so the true picture may be worse. The same hazards apply to a dialysis unit, where every patient is treated on a fixed schedule: sheets with no identifiers, sessions entered twice, and values filled in from memory days later.</p>
<p>At national scale, the 2023 ransomware attack on the Philippine Health Insurance Corporation (PhilHealth) forced the payer itself into manual operations.[[mro_ph2023medusa]] If the payer can go dark, so can any dialysis unit.</p>
"""),
        ("during", "Before and during", "Readiness and downtime documentation", """
<h3>Before</h3>
<p>Keep a printed downtime kit at each station. It should hold:</p>
<ul>
<li>blank run sheets with pre-numbered downtime IDs;</li>
<li>the current patient list with two identifiers for each patient;</li>
<li>current standing orders, printed at a set interval such as every shift, so they are never more than a day old;</li>
<li>the contact list: IT, the charge nurse, the attending nephrologist, the records officer;</li>
<li>the downtime procedure, short enough to read in two minutes.</li>
</ul>
<p>Check the kit monthly. A kit with last quarter&rsquo;s standing orders is worse than none, because it looks trustworthy. Run a drill at least yearly, and use it to check documentation quality: did every drill sheet carry its ID, two identifiers, a time, and a signature?</p>
<h3>During</h3>
<p>Every paper document carries its downtime ID, the patient&rsquo;s two identifiers, the date and time, and the author&rsquo;s signature. &ldquo;Rodriguez, F.&rdquo; is one identifier, and an ambiguous one. Sheets are collected and secured each shift. A downtime log tracks each sheet: issued, completed, collected. Clinical questions go to the clinical team. The records officer never reconstructs missing values.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usual improvisation</th><th>Safer practice</th></tr></thead>
<tbody>
<tr><td>Writing on whatever paper is at hand</td><td>Using the numbered sheets from the kit</td></tr>
<tr><td>Surname only, or chair number</td><td>Two person-level identifiers on every sheet (Module 3)</td></tr>
<tr><td>&ldquo;I&rsquo;ll fill in the times later&rdquo;</td><td>Times written as events happen</td></tr>
<tr><td>Sheets left at stations overnight</td><td>Collected and secured each shift</td></tr>
<tr><td>Sharing one emergency password</td><td>The approved, logged emergency-access procedure</td></tr>
</tbody></table></div>
{{call:A shared emergency password to speed up recovery destroys attribution. Use the approved, logged emergency-access procedure, and report any pressure to do otherwise. If an outage affects a patient&rsquo;s treatment, the clinical decisions belong to the charge nurse and the attending nephrologist, per unit protocol.}}
"""),
        ("after", "After recovery", "Three lists, one truth", """
{{fig:mro12_lists}}
<p>For every expected encounter during the outage, compare three lists: the schedule, the paper sheets, and the electronic record, including entries started just before the outage. Each sheet ends up in exactly one of these situations.</p>
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
<p>The last row of the table is the easiest to miss. A patient who was scheduled, has no paper sheet, and has no electronic entry may have been sent home, sent to the emergency room, or treated on a sheet that was lost. Only the clinical team can say which. The pre-numbered downtime IDs are what make a lost sheet visible: a gap in the sequence is a question.</p>
<p>A two-person reconciliation, one reading and one checking, is a strong local control. Close the event with a short report: duration, encounters affected, counts, open exceptions, and lessons for the next drill. Sessions captured on paper are claimable only after they are authenticated and back-entered.</p>
{{key:Downtime paper is a parallel record. Reconcile it; do not just file it.}}
"""),
    ],
    "debrief": ["""
<p><strong>Dispositions.</strong> DT-01: matched; record it as such and create no new session. DT-02: back-entered as an attributable late entry by the authorized person, carrying both the service date and the entry date. DT-03: author query to Mr. Uy&rsquo;s nurse; held. DT-04: identity exception. With the brothers on the same shift, the charge nurse and the nurse who wrote the sheet must establish which Rodriguez it describes before it is filed anywhere.</p>
<p><strong>Counts.</strong> Four sheets = 1 matched + 1 back-entered + 1 pending query + 1 identity exception. Balanced. Then check the other way: were any patients scheduled on Saturday morning with no sheet and no electronic entry? Check the downtime IDs for gaps.</p>
<p><strong>Mr. Ramos.</strong> DT-01 is already in the record. DT-02 can be claimed once it is back-entered. DT-03 and DT-04 stay on hold until they are resolved; the batch can close without them, and they go in the next one.</p>
<p>The easy mistake would have been to back-enter all four sheets on Monday morning, creating a duplicate session for Mr. Victor Mercado and possibly giving one brother&rsquo;s treatment to the other. Part of your role is to make the dark hours add up before anyone bills for them.</p>
"""],
    "skills": {"title": "Downtime reconciliation",
               "intro": "Reconcile a fictional set of downtime sheets against a schedule and a restored record while your preceptor observes.",
               "items": [
                   ("Checks a downtime kit for current patient lists and standing orders.", False),
                   ("Checks that each sheet has a downtime ID, two identifiers, time, and signature.", False),
                   ("Records a match without creating a duplicate session.", True),
                   ("Back-enters only authenticated sheets as attributable late entries.", True),
                   ("Routes an ambiguous identity to the identity exception workflow.", True),
                   ("Balances the counts, checks for gaps in downtime IDs, and lists open exceptions.", False),
                   ("Holds downtime sessions from claims until authenticated and back-entered.", True),
               ],
               "placement": "Open your unit&rsquo;s downtime kit. Check that the patient list and standing orders are current, and that the sheets are pre-numbered."},
    "terms": [("Downtime", "A period when the electronic system is unavailable."), ("Downtime kit", "Printed forms, lists, orders, and contacts kept ready for an outage."),
              ("Downtime ID", "A pre-printed number on each paper sheet."),
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
