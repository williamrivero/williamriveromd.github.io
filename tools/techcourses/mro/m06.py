# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 06: PhilHealth: The PDD, the 156-Session Ledger, and the Claim Packet. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and a claims clerk comparing signed session forms with a claims list at a small office desk.",
    "objectives": [
        "State the current hemodialysis package facts and the issuance behind each.",
        "Keep a per-patient session ledger for the calendar year and project when the cap will be reached.",
        "Assemble a claim packet that proves eligibility, delivery, and documentation separately.",
        "Handle returns, corrections, and duplicates without destroying history.",
    ],
    "big": """
{{plain:A dialysis claim makes three claims at once: this person is covered, this treatment happened, and the paperwork matches. Each needs its own proof.}}
<p>Most denials and audit findings trace to one proof being assumed from another &mdash; treating registration in the PhilHealth Dialysis Database (PDD) as if it proved a session happened, or treating a schedule as if it proved a treatment.</p>
{{cards:Key terms for this module|PhilHealth Dialysis Database (PDD)::PhilHealth Dialysis Database; eligibility for the HD package.|Annex A::The PhilHealth Hemodialysis Benefits Package Agreement Form, signed for every session.|Statement of account (SOA)::Statement of Account (eSOA when electronic).|Session ledger::A per-patient count of covered sessions used and remaining in the calendar year.|Return to hospital::A claim sent back for correction.}}
""",
    "case": {"title": "Four rows, one patient", "html": """
<p>The claims staging list for fictional patient SIM-041 has four rows. D1: November 3, signed and complete, Annex A signed. D2: November 5, canceled before treatment, staged by the scheduler. D3: November 7, signed and complete, Annex A missing. D4: November 3 again, the same service ID as D1, already in accepted batch B-14. PDD eligibility is verified. SIM-041 has 141 sessions claimed for 2026 and dialyzes three times a week.</p>
""", "questions": ["What is the disposition of each row?",
                  "What does batch B-14 mean for D1?",
                  "Will SIM-041 reach 156 sessions before December 31, and who should know?"]},
    "sections": [
        ("package", "The package", "The package, as of November 2026", """
<div class="table-wrap"><table>
<thead><tr><th>Fact</th><th>Detail</th></tr></thead>
<tbody>
<tr><td>Rate</td><td>&#8369;6,350 per session, effective October 9, 2024 (&#8369;990,600 a year at 156 sessions)[[dch_philhealth2024]][[mro_ph2025news]]</td></tr>
<tr><td>Annual cap</td><td>Up to 156 sessions per calendar year; unused sessions do not carry over[[mro_ph2023]]</td></tr>
<tr><td>45-day rule</td><td>Lifted for confinements effective April 4, 2025; hemodialysis stays capped at 156[[mro_ph2025_45day]]</td></tr>
<tr><td>Eligibility</td><td>CKD stage 5, registered in the PDD[[mro_ph2016pdd]]</td></tr>
<tr><td>Per-session form</td><td>Annex A for every session, whether or not extra services or co-payment occurred[[mro_ph2024ts]]</td></tr>
<tr><td>Minimum standard</td><td>Erythropoiesis-stimulating agent, iron sucrose, unfractionated heparin; scheduled labs; up to 32 dialyzers a year reusable up to 5 times[[mro_ph2024ts]]</td></tr>
<tr><td>Co-payment</td><td>No co-payment for services in the circular&rsquo;s tables; professional-fee co-payment up to &#8369;450 for listed additional services, itemized on Annex A[[mro_ph2024ts]]</td></tr>
</tbody></table></div>
<p>Rates and forms change. Attach the circular revision to the <strong>service date</strong> in your ledger, not the filing date, and confirm current rules with your claims lead.</p>
"""),
        ("proofs", "Three proofs", "Eligibility, delivery, documentation", """
{{fig:mro06_proofs}}
{{flow:The claim packet|Eligibility::Current PDD registration and the verification result for the service date, with proof of the check.|Delivery::The authenticated run sheet for that date, signed and complete.|Documentation::The signed Annex A; the SOA and claim form per current specifications; any co-payment itemized exactly as on Annex A.|Duplicate check::Has this patient, date, and service appeared in any sent or accepted batch? If so, stop and reconcile.}}
{{call:A session canceled before treatment is not a delivered service, however complete the rest of its paperwork looks. Put it on exception with the documented cancellation.}}
"""),
        ("ledger", "The ledger", "The session ledger and corrections", """
<p>For each patient, per calendar year, track sessions claimed, pending, returned, and remaining of 156, plus the projected date the cap will be reached. Three sessions a week uses about 13 a month and reaches 156 near the end of December; one extra session a month brings the cap forward by about a month. Tell the patient, the social worker, and the claims lead early, because sessions beyond 156 are not covered.</p>
<p>For a return to hospital, log the reason, fix the underlying document through its owner, keep the original submission and the corrected one, and mark the item corrected only when the amended document and the new acknowledgment are both traceable. Never resubmit an unchanged batch under a new identifier.</p>
{{key:Eligibility is not delivery, and delivery is not documentation. Prove each, then check for duplicates.}}
<p>Claims staff take the packet from here. The Academy&rsquo;s <a href="philhealth-claims.html">PhilHealth Liaison, Claims Officer and Clerk track</a> covers filing, returns, and denials in depth.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Dispositions.</strong> D1 and D4 are the same November 3 service; batch B-14 already accepted it, so D1 must not be submitted again &mdash; reconcile the identifiers with the claims lead. D2 goes to exception: canceled before treatment. D3 is held until Annex A is signed.</p>
<p><strong>The cap.</strong> With the November 3 service already counted, about 13 sessions remain. At three a week from November 8, the cap is reached in early December. Tell the claims lead, the patient, and the social worker now.</p>
"""],
    "skills": {"title": "Claims readiness and the session ledger",
               "intro": "Disposition a fictional claims staging list and update the session ledger with a preceptor.",
               "items": [
                   ("Proves eligibility, delivery, and documentation separately for each session.", False),
                   ("Excludes a session canceled before treatment.", True),
                   ("Detects a service already in a sent or accepted batch and stops resubmission.", True),
                   ("Projects the cap date and notifies the claims lead, patient, and social worker.", False),
                   ("Preserves original and corrected submissions for a returned claim.", False),
               ],
               "placement": "Pick three patients and reconcile their session ledgers against this year&rsquo;s accepted batches."},
    "terms": [("PDD", "PhilHealth Dialysis Database."), ("Annex A", "The per-session HD Benefits Package Agreement Form."),
              ("SOA", "Statement of Account."), ("eSOA", "Electronic Statement of Account."),
              ("Session ledger", "Covered sessions used and remaining in the calendar year."),
              ("Return to hospital", "A claim sent back for correction.")],
    "readings": [("zero-balance-billing-philhealth.html", "How PhilHealth zero balance billing works for patients."),
],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["06"])
