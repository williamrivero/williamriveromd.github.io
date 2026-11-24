# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 06: PhilHealth Eligibility, the 156-Session Ledger, and the Claim Packet. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and a claims clerk comparing a session ledger with signed Annex A forms.",
    "objectives": [
        "State the main facts of the Philippine Health Insurance Corporation (PhilHealth) hemodialysis (HD) package and attach each to its source and effective date.",
        "Prove eligibility, delivery, and documentation separately for every claimed session.",
        "Detect a canceled session or a duplicate service before it reaches a claim.",
        "Keep a per-patient session ledger and project the date the annual cap will be reached.",
        "Handle a returned claim so that both the original and the corrected submission remain traceable.",
    ],
    "big": """
{{plain:A dialysis claim makes three promises at once. This person is covered. This treatment happened. The paperwork matches. Think of it as a three-legged stool: each leg needs its own proof, and a stool with two strong legs still falls over.}}
<p>The picture is useful, and it has one limit. A wobbly stool is noticed the moment someone sits on it. A wobbly claim may be paid, and the problem appears months later in an audit, when the people who could have fixed it have moved on. By then, a gap in one claim often turns out to be a pattern across hundreds.</p>
<p>Most denials and audit findings trace to one proof being assumed from another: treating registration in the PhilHealth Dialysis Database (PDD) as if it proved a session happened, or treating a schedule as if it proved a treatment. The records officer does not file claims. Claims staff do. Your part is to make sure that every claimed session stands on three legs of evidence that you can retrieve on request.</p>
{{cards:Key terms for this module|PhilHealth Dialysis Database (PDD)::The registry of patients eligible for the Philippine Health Insurance Corporation hemodialysis package.|Annex A::The PhilHealth Hemodialysis Benefits Package Agreement Form, signed for every session.|Statement of account (SOA)::The itemized bill for the session; electronic statement of account (eSOA) when filed electronically.|Session ledger::A per-patient count of covered sessions used and remaining in the calendar year.|Return to hospital::A claim sent back to the facility for correction.|Service date::The date the treatment was given, which decides which rules apply.}}
""",
    "case": {"title": "Four rows, one patient", "html": """
<p>It is Monday, November 9. Ms. Marites Lopez, the claims lead, sends you the staging list for Mrs. Carmelita Ramos, 58, who dialyzes on Monday, Wednesday, and Friday. There are four rows.</p>
<div class="table-wrap"><table>
<thead><tr><th>Row</th><th>Service date</th><th>What the paperwork shows</th></tr></thead>
<tbody>
<tr><td>D1</td><td>November 3</td><td>Run sheet signed and complete; Annex A signed</td></tr>
<tr><td>D2</td><td>November 5</td><td>Staged by the scheduler; the run sheet says &ldquo;canceled before start, fever, sent to the emergency room&rdquo;</td></tr>
<tr><td>D3</td><td>November 7</td><td>Run sheet signed and complete; Annex A missing</td></tr>
<tr><td>D4</td><td>November 3</td><td>Same service ID as D1; already in accepted batch B-14</td></tr>
</tbody></table></div>
<p>Her PDD eligibility is verified. Her ledger shows 141 sessions accepted for 2026, including November 3, and 2 delivered sessions pending: October 31, sent in batch B-15 and awaiting acknowledgment, and D3.</p>
""", "questions": ["What is the disposition of each row?",
                  "What does batch B-14 mean for D1?",
                  "Will Mrs. Ramos reach 156 sessions before December 31, and who should know now?"]},
    "sections": [
        ("package", "The package", "The package, as of November 2026", """
<p>Know the main facts of the Philippine Health Insurance Corporation (PhilHealth) hemodialysis package, and know where each one comes from.</p>
<div class="table-wrap"><table>
<thead><tr><th>Fact</th><th>Detail</th></tr></thead>
<tbody>
<tr><td>Rate</td><td>&#8369;6,350 per session, effective October 9, 2024 (&#8369;990,600 a year at 156 sessions)[[dch_philhealth2024]][[mro_ph2025news]]</td></tr>
<tr><td>Annual cap</td><td>Up to 156 sessions per calendar year; unused sessions do not carry over[[mro_ph2023]]</td></tr>
<tr><td>45-day rule</td><td>Lifted for confinements effective April 4, 2025; hemodialysis stays capped at 156[[mro_ph2025_45day]]</td></tr>
<tr><td>Eligibility</td><td>Chronic kidney disease (CKD) stage 5, International Classification of Diseases, 10th Revision (ICD-10) code N18.5, registered in the PDD[[mro_ph2016pdd]]</td></tr>
<tr><td>Per-session form</td><td>Annex A for every session, whether or not extra services or co-payment occurred[[mro_ph2024ts]]</td></tr>
<tr><td>Minimum standard</td><td>Erythropoiesis-stimulating agent, iron sucrose, unfractionated heparin; scheduled laboratory tests; up to 32 dialyzers a year, each reusable up to 5 times[[mro_ph2024ts]]</td></tr>
<tr><td>Co-payment</td><td>No co-payment for services in the circular&rsquo;s tables; a professional-fee co-payment of up to &#8369;450 for listed additional services, itemized on Annex A[[mro_ph2024ts]]</td></tr>
</tbody></table></div>
<p>Rates and forms change, and they changed twice in 2024 alone. Attach the circular revision to the <strong>service date</strong> in your ledger, not the filing date. A session given before a rate change is paid at the old rate even if the claim is filed after it. Confirm current rules with your claims lead, and record each change in your source register (Module 1).</p>
{{scene:The October filing|<p>A unit files September sessions in mid-October. The clerk uses the new form version released on October 1, which asks for a field the September form did not have.</p>
<p>The records officer checks the advisory: the new form applies to sessions from its effective date, not to filings after it. The September claims are refiled on the version in force on their service dates, and the source register gets a note: &ldquo;Forms follow the service date.&rdquo;</p>
<p class="tc-scene-take">Rates and forms change on a date. The date that matters is the day of treatment.</p>}}
"""),
        ("proofs", "Three proofs", "Eligibility, delivery, documentation", """
{{fig:mro06_proofs}}
<div class="table-wrap"><table>
<thead><tr><th>Proof</th><th>Question</th><th>Evidence</th><th>Not enough on its own</th></tr></thead>
<tbody>
<tr><td>Eligibility</td><td>Is this person covered on this date?</td><td>Current PDD registration and the verification result for the service date</td><td>&ldquo;She was registered last year&rdquo;</td></tr>
<tr><td>Delivery</td><td>Did the treatment happen?</td><td>The authenticated run sheet for that date, signed and complete</td><td>The schedule; the attendance list; a registered patient</td></tr>
<tr><td>Documentation</td><td>Does the paperwork match?</td><td>Signed Annex A; the SOA and claim form per current specifications; any co-payment itemized exactly as on Annex A</td><td>A complete run sheet with no Annex A</td></tr>
</tbody></table></div>
{{flow:The claim packet|Eligibility::Current PDD registration and the verification result for the service date, with proof of the check.|Delivery::The authenticated run sheet for that date, signed and complete.|Documentation::The signed Annex A; the SOA and claim form per current specifications; any co-payment itemized exactly as on Annex A.|Duplicate check::Has this patient, date, and service appeared in any sent or accepted batch? If so, stop and reconcile.}}
<h3>Cancellations and partial sessions</h3>
<p>Patients are sent to the emergency room before needling. Machines fail. Patients arrive, feel unwell, and go home. The scheduler may still have staged the session, because the schedule does not know what happened at the chair.</p>
<p>A session canceled before treatment is not a delivered service, however complete the rest of its paperwork looks. A session that started and ended early is a clinical question: the run sheet shows what was delivered, and the claims lead decides, under current PhilHealth rules, how it is handled. Your job is to make sure the run sheet says clearly which of the two happened.</p>
{{call:A session canceled before treatment goes on exception with the documented cancellation. It is never claimed, whatever the staging list says. If you are told to claim it anyway, write down who asked and escalate to the facility head.}}
<h3>Duplicates</h3>
<p>Duplicates usually come from honest causes: a batch resent after a network error, a service staged twice by two staff members, or a corrected claim filed without retiring the original. Before any batch goes out, check every row against every sent and accepted batch for the same patient, date, and service. Claiming one session twice, even by accident, is a payment the unit will have to explain and return.</p>
{{scene:Registered, scheduled, not treated|<p>Mr. Gregorio Santos is registered in the PhilHealth Dialysis Database and booked for Friday morning. On Friday his daughter calls: he was admitted to hospital overnight. The schedule still shows him, and the staging list picks up the session.</p>
<p>The records officer checks the three proofs. Eligibility: yes. Delivery: no run sheet, because no treatment happened. The session is removed from the batch with the daughter&rsquo;s call documented.</p>
<p class="tc-scene-take">Eligibility and a booking are two of three legs. Without the run sheet, the stool falls.</p>}}
"""),
        ("ledger", "The ledger", "The session ledger and corrections", """
<p>For each patient, per calendar year, keep a session ledger.</p>
<div class="table-wrap"><table>
<thead><tr><th>Column</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Sessions accepted</td><td>Paid; counted against the cap</td></tr>
<tr><td>Sessions pending</td><td>Delivered and sent or held; will count when accepted</td></tr>
<tr><td>Sessions returned</td><td>Need correction; still delivered</td></tr>
<tr><td>Sessions remaining of 156</td><td>What is left for the year</td></tr>
<tr><td>Projected cap date</td><td>When coverage will run out at the current schedule</td></tr>
</tbody></table></div>
{{formula:<strong>Remaining</strong> = 156 &minus; accepted &minus; pending.<br>Three sessions a week use about 13 a month; 156 sessions at that pace reach the cap near the end of December. One extra session a month brings the cap forward by about a month.}}
<p>The projection matters to people, not only to claims. Sessions beyond 156 are not covered, and a family that learns this in the third week of December has no time to plan. Tell the patient, the social worker, and the claims lead early, ideally by October for anyone whose ledger is ahead of pace. Extra sessions for fluid overload, a hospital stay that used dialysis sessions, or a transfer-in partway through the year are the usual reasons a patient runs ahead.</p>
<p>The toolkit&rsquo;s session-ledger calculator does the counting and the projection.</p>
<h3>Returned claims</h3>
<p>For a return to hospital, log the reason, fix the underlying document through its owner, keep both the original submission and the corrected one, and mark the item corrected only when the amended document and the new acknowledgment are both traceable. Never resubmit an unchanged batch under a new identifier. That is not a correction; it is a second claim for the same service.</p>
{{key:Eligibility is not delivery, and delivery is not documentation. Prove each, then check for duplicates.}}
<p>Claims staff take the packet from here. The Academy&rsquo;s <a href="philhealth-claims.html">PhilHealth Liaison, Claims Officer and Clerk track</a> covers filing, returns, and denials in depth.</p>
{{scene:The family told in October|<p>Mrs. Adoracion Villafuerte needed extra sessions in June and July for fluid overload. On October 5 her ledger shows 138 sessions used, and the projection puts her cap in the third week of November.</p>
<p>The records officer tells the claims lead, who tells the social worker, who meets the family. They apply for assistance from the local government and a charity program, and when the cap arrives, the remaining sessions are covered.</p>
<p class="tc-scene-take">The same number on December 15 would have been a crisis. On October 5, it was a plan.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>D1 and D4.</strong> They are the same November 3 service. Batch B-14 already accepted it, so D1 must not be submitted again. Reconcile the two identifiers with Ms. Lopez and find out how the service came to be staged twice, so the cause can be fixed.</p>
<p><strong>D2.</strong> Exception: canceled before treatment, with the run sheet note as evidence. Never claimed.</p>
<p><strong>D3.</strong> Held until Annex A is signed. Ask the charge nurse to have Mrs. Ramos sign at her next session, and check that the date on the form is the service date.</p>
<p><strong>The cap.</strong> 156 &minus; 141 accepted &minus; 2 pending leaves 13 sessions. At three a week from November 9, the last covered session is Monday, December 7. Mrs. Ramos will have about three and a half weeks of uncovered sessions before the new year. Tell Ms. Lopez, the social worker, and Mrs. Ramos now, while there is still time to plan.</p>
<p>The four rows looked like a claims problem. The most important finding was a family about to face three weeks of uncovered dialysis. Part of your role is to see that in a ledger before December does.</p>
"""],
    "skills": {"title": "Claims readiness and the session ledger",
               "intro": "Disposition a fictional claims staging list and update the session ledger while your preceptor observes.",
               "items": [
                   ("States the rate, cap, eligibility rule, and per-session form, each with its source and effective date.", False),
                   ("Proves eligibility, delivery, and documentation separately for each session.", False),
                   ("Excludes a session canceled before treatment.", True),
                   ("Detects a service already in a sent or accepted batch and stops resubmission.", True),
                   ("Computes sessions remaining and projects the cap date.", False),
                   ("Notifies the claims lead, patient, and social worker of an early cap.", False),
                   ("Preserves original and corrected submissions for a returned claim.", False),
               ],
               "placement": "Pick three patients and reconcile their session ledgers against this year&rsquo;s accepted batches. Project each one&rsquo;s cap date."},
    "terms": [("PDD", "PhilHealth Dialysis Database."), ("Annex A", "The per-session HD Benefits Package Agreement Form."),
              ("SOA", "Statement of Account."), ("eSOA", "Electronic Statement of Account."),
              ("Session ledger", "Covered sessions used and remaining in the calendar year."),
              ("Service date", "The date a treatment was given."),
              ("Return to hospital", "A claim sent back for correction.")],
    "readings": [("zero-balance-billing-philhealth.html", "How PhilHealth zero balance billing works for patients.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["06"])
