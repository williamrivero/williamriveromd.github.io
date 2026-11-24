# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 07: Registries: PRDR, REDCOP, PDD, and Data Quality. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer reviewing a printed event ledger with a highlighter beside a computer in a quiet records room.",
    "objectives": [
        "Distinguish the Philippine Renal Disease Registry, which supports the DOH Renal Disease Control Program, from the PhilHealth Dialysis Database.",
        "Define each destination&rsquo;s population, events, fields, channel, signatory, and cadence.",
        "Build an event ledger from authenticated charts.",
        "Close a submission cycle only when every row has a disposition and an acknowledgment.",
    ],
    "big": """
{{plain:Registries are how a country learns how many people start dialysis, how they fare, and where services are missing. They are only as accurate as the charts behind them.}}
<p>A registry form filled from memory or from the scheduler quietly drops what the chart would have shown. The records officer&rsquo;s remedy is to extract from the authenticated chart, field by field, and to chase every row until the receiver confirms it.</p>
{{cards:Key terms for this module|Philippine Renal Disease Registry (PRDR)::Philippine Renal Disease Registry.|Renal Disease Control Program (REDCOP)::Renal Disease Control Program of the DOH.|PhilHealth Dialysis Database (PDD)::PhilHealth Dialysis Database.|Transfer-in::Arrival of a patient already on dialysis elsewhere.|Acknowledgment::The receiver&rsquo;s confirmation of what it accepted or rejected.|End-stage renal disease (ESRD)::End-stage renal disease.}}
""",
    "case": {"title": "Three events, four rows", "html": """
<p>Your event queue has fictional patient SIM-051, first-ever maintenance hemodialysis on November 2; SIM-052, transferred in on November 5 after starting dialysis elsewhere on June 18; and SIM-053, changed to peritoneal dialysis (PD) on November 11, with a second SIM-053 row repeating that event. The receiver&rsquo;s first acknowledgment shows two accepted and one rejected: SIM-052&rsquo;s local start date had been entered in the original-start field.</p>
""", "questions": ["How many rows should have been sent?",
                  "How do you correct SIM-052?",
                  "When is this cycle closed?"]},
    "sections": [
        ("two", "Two registries", "Two destinations, two rulebooks", """
<p>The DOH assessment tool calls for registration in the Philippine Renal Disease Registry (PRDR) in support of the Renal Disease Control Program (REDCOP), coordinated with PSN.[[dch_doh_rao_tool]] The PhilHealth Dialysis Database (PDD) is PhilHealth&rsquo;s eligibility database for the HD package.[[mro_ph2016pdd]] They differ in purpose, owner, fields, and timing; reporting to one does not satisfy the other. For each destination, write down the population, event definitions, required fields, authorized users, channel, signatory, cadence, and how acknowledgment arrives, and confirm them with the receiving authority.</p>
{{fig:mro07_registry}}
"""),
        ("quality", "Data quality", "Registries inherit the chart&rsquo;s gaps", """
<p>The best-known validation study compared the United States end-stage renal disease (ESRD) Medical Evidence Report against clinical records for 1,005 new dialysis patients. Averaged across 17 conditions, the form captured only 59% of the comorbidities actually present (sensitivity 0.59, 95% confidence interval 0.43 to 0.75), while specificity was above 0.95 for 16 of the 17.[[mro_longenecker2000]] Conditions were <strong>left out</strong> far more often than they were <strong>made up</strong>. That is what happens when forms are completed from memory or from incomplete charts.</p>
<p>The most common Philippine-unit error is confusing <strong>first-ever dialysis</strong> with <strong>first treatment at this center</strong>. A patient who transfers in after starting elsewhere is a transfer-in event, with the original start date carried over from the referring facility&rsquo;s documents.</p>
"""),
        ("ledger", "The ledger", "Build, balance, and close", """
<p>From the master patient index and authenticated charts, keep one row per event: patient identifier, event, event date, source document, destination, deduplication key, field validation, batch, status, rejection reason, correction, and acknowledgment. Validate identifiers, modality, and dates, and look for duplicates before sending.</p>
{{formula:Sent = accepted + rejected + pending. Any row without a disposition is a variance to investigate.}}
<p>A rejected row closes only when corrected, source-backed data are resubmitted and accepted, with both receipts kept. Export only the fields the destination requires, through the approved channel.</p>
{{key:A sent file is not a closed cycle. Keep the acknowledgment, and chase every row that lacks one.}}
"""),
    ],
    "debrief": ["""
<p><strong>Rows.</strong> Three: one per event. The second SIM-053 row is a duplicate and should have been removed before sending.</p>
<p><strong>SIM-052.</strong> Record the original start as June 18 from the referral documents and the transfer-in as November 5, then resubmit.</p>
<p><strong>Closed when</strong> all three unique events are accepted, the first rejection and the corrected acceptance are both filed, and sent equals accepted plus rejected plus pending with nothing unexplained.</p>
"""],
    "skills": {"title": "Registry event ledger and batch reconciliation",
               "intro": "Build and close a fictional registry batch with a preceptor.",
               "items": [
                   ("Distinguishes PRDR reporting from PDD registration.", False),
                   ("Records a transfer-in with the original start date and its source.", True),
                   ("Removes duplicate event rows before submission.", False),
                   ("Balances sent against accepted, rejected, and pending.", False),
                   ("Closes a rejection only with corrected, source-backed data and both receipts.", True),
               ],
               "placement": "Find last cycle&rsquo;s registry acknowledgments and check that every sent row has a disposition."},
    "terms": [("PRDR", "Philippine Renal Disease Registry."), ("REDCOP", "Renal Disease Control Program."),
              ("PDD", "PhilHealth Dialysis Database."), ("ESRD", "End-stage renal disease."), ("PD", "Peritoneal dialysis."),
              ("Sensitivity of a form", "The share of true conditions a form captures."),
              ("Transfer-in", "Arrival of a patient already on dialysis elsewhere.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["07"])
