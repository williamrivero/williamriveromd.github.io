# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 07: Registries and Data Quality. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer reconciling a registry acknowledgment report against an event ledger on a computer.",
    "objectives": [
        "Distinguish reporting to the Philippine Renal Disease Registry from registration in the Philippine Health Insurance Corporation (PhilHealth) Dialysis Database.",
        "Explain, using published evidence, why registry forms filled from memory miss conditions.",
        "Record first-ever dialysis, transfer-in, and modality change as distinct events with their sources.",
        "Keep an event ledger, remove duplicates before sending, and balance every batch.",
        "Close a rejection only with corrected, source-backed data and both receipts.",
    ],
    "big": """
{{plain:A registry is how a country counts its dialysis patients: how many start each year, how they fare, and where services are missing. Imagine a census taker who writes down only the people who happen to be home when he knocks. The numbers look complete. They are not.}}
<p>The picture is useful, and it has one limit. A census taker can come back. A registry row, once accepted, is usually counted, published, and used to plan services, and few people ever check it against the chart again. An error at your desk becomes a national statistic.</p>
<p>A registry form filled from memory, or from the scheduler, quietly drops what the chart would have shown. The records officer&rsquo;s remedy is to extract from the authenticated chart, field by field, and to chase every row until the receiver confirms it.</p>
{{cards:Key terms for this module|Philippine Renal Disease Registry (PRDR)::The national registry of people with kidney failure on dialysis or with a transplant.|Renal Disease Control Program (REDCOP)::The Department of Health program the registry supports.|PhilHealth Dialysis Database (PDD)::The payer&rsquo;s eligibility database for the hemodialysis package.|Event::Something that changes a patient&rsquo;s registry status: first-ever dialysis, transfer-in, transfer-out, modality change, transplant, recovery, death.|Transfer-in::Arrival of a patient already on dialysis elsewhere.|Acknowledgment::The receiver&rsquo;s confirmation of what it accepted or rejected.|End-stage renal disease (ESRD)::The older term for kidney failure treated with dialysis or transplant, still used in some registries.}}
""",
    "case": {"title": "Three events, four rows", "html": """
<p>It is the end of the month and you are sending your registry batch. Your event queue holds three patients.</p>
<ul>
<li>Mr. Arnel Domingo started his first-ever maintenance hemodialysis (HD) with you on November 2.</li>
<li>Mrs. Virginia Salazar transferred in on November 5. Her referral packet shows she started dialysis at a hospital in Pampanga on June 18.</li>
<li>Mr. Jose Manalo changed from hemodialysis to peritoneal dialysis (PD) on November 11. A second row for Mr. Manalo repeats the same event; a staff member entered it again when the first entry seemed not to save.</li>
</ul>
<p>Two days after you send four rows, the receiver&rsquo;s acknowledgment arrives: two accepted, one rejected. Mrs. Salazar&rsquo;s November 5 date had been entered in the &ldquo;original start of dialysis&rdquo; field.</p>
""", "questions": ["How many rows should have been sent?",
                  "How do you correct Mrs. Salazar&rsquo;s row?",
                  "Four rows were sent and three acknowledged. What happened to the fourth, and when is this cycle closed?"]},
    "sections": [
        ("two", "Two registries", "Two destinations, two rulebooks", """
<p>Dialysis units in the Philippines report to two different databases that are easy to confuse.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>PRDR</th><th>PDD</th></tr></thead>
<tbody>
<tr><td>Owner</td><td>Department of Health (DOH) program, coordinated with the Philippine Society of Nephrology (PSN)</td><td>Philippine Health Insurance Corporation (PhilHealth)</td></tr>
<tr><td>Purpose</td><td>Public health: counting patients, outcomes, and service gaps</td><td>Payment: eligibility for the hemodialysis package</td></tr>
<tr><td>Required by</td><td>The DOH licensing assessment tool[[dch_doh_rao_tool]]</td><td>PhilHealth circulars[[mro_ph2016pdd]]</td></tr>
<tr><td>What happens if it is wrong</td><td>National statistics and planning are wrong</td><td>Claims are denied or questioned</td></tr>
</tbody></table></div>
<p>The DOH assessment tool calls for registration in the Philippine Renal Disease Registry (PRDR) in support of the Renal Disease Control Program (REDCOP), coordinated with PSN.[[dch_doh_rao_tool]] The PhilHealth Dialysis Database (PDD) is PhilHealth&rsquo;s eligibility database for the hemodialysis package.[[mro_ph2016pdd]] They differ in purpose, owner, fields, and timing. Reporting to one does not satisfy the other.</p>
<p>For each destination, write down the population it covers, its event definitions, its required fields, who may submit, the channel, the signatory, the cadence, and how acknowledgment arrives. Confirm them with the receiving authority, because registry definitions change and a field that meant one thing last year may mean another now.</p>
{{fig:mro07_registry}}
{{scene:Reported once, counted nowhere|<p>A unit proudly reports that every patient is &ldquo;registered.&rdquo; On inspection, every patient is in the PhilHealth Dialysis Database, and none of the year&rsquo;s new starts appear in the Philippine Renal Disease Registry.</p>
<p>The clerk had assumed one submission covered both. The records officer builds two extracts, each to its own specification, and adds both destinations to the event ledger.</p>
<p class="tc-scene-take">Two databases, two purposes, two rulebooks. One list does not serve both.</p>}}
"""),
        ("quality", "Data quality", "Registries inherit the chart&rsquo;s gaps", """
<p>How accurate are registry forms? The best-known validation study comes from the United States. Investigators compared the national end-stage renal disease (ESRD) Medical Evidence Report, the form filed when a patient starts dialysis, against the clinical records of 1,005 new dialysis patients.</p>
<p>Averaged across 17 conditions, the form captured only 59% of the conditions actually present (sensitivity 0.59, 95% confidence interval 0.43 to 0.75). Specificity was above 0.95 for 16 of the 17.[[mro_longenecker2000]] In plain terms: conditions were <strong>left out</strong> far more often than they were <strong>made up</strong>. When the form said a patient had heart failure, they almost always did. When it said nothing, it was often wrong.</p>
<p>That pattern is what you would expect when forms are completed from memory, from the referral letter alone, or by someone who never opened the full chart. It is not a United States problem. It is what happens anywhere a form is easier to fill than a chart is to read.</p>
<h3>The most common Philippine error</h3>
<p>The error most often seen in Philippine units is confusing <strong>first-ever dialysis</strong> with <strong>first treatment at this center</strong>. A patient who transfers in after starting elsewhere is a transfer-in event, with the original start date carried over from the referring facility&rsquo;s documents. Recording the transfer date as the start date makes the patient look newer than they are, which corrupts survival statistics and, as Module 9 explains, every certificate that states their dialysis vintage.</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Date to record</th><th>Source</th></tr></thead>
<tbody>
<tr><td>First-ever dialysis at your unit</td><td>The first session date</td><td>Your run sheet</td></tr>
<tr><td>Transfer-in</td><td>The arrival date, plus the original start date in its own field</td><td>Your run sheet; the referring facility&rsquo;s documents</td></tr>
<tr><td>Modality change</td><td>The first treatment on the new modality</td><td>The order and the first treatment record</td></tr>
<tr><td>Transfer-out, transplant, recovery, death</td><td>The event date</td><td>The documented event</td></tr>
</tbody></table></div>
{{scene:The diabetes that was missing|<p>A registry form for Mr. Teodoro Navarro, completed from his referral letter, lists hypertension as his only condition. His chart shows type 2 diabetes for twelve years, heart failure, and a below-knee amputation.</p>
<p>The records officer redoes the form from the authenticated chart and problem list. The corrected entry now describes a patient at much higher risk than the first form suggested.</p>
<p class="tc-scene-take">The form was not false. It was incomplete in exactly the way the research predicts: conditions left out, not made up.</p>}}
"""),
        ("ledger", "The ledger", "Build, balance, and close", """
<p>From the master patient index and the authenticated charts, keep one row per event with these columns: patient identifier, event, event date, source document, destination, deduplication key, field validation, batch, status, rejection reason, correction, and acknowledgment.</p>
<p>Before sending, validate identifiers, modality, and dates, and look for duplicates. The deduplication key is usually patient, event type, and event date together. Two rows with the same key are one event entered twice.</p>
{{formula:Sent = accepted + rejected + pending. Any row without a disposition is a variance to investigate.}}
<p>A row can go missing in silence. The receiver may drop it as a duplicate without saying so, or fail to process it. The balance equation is how you notice. If you sent four rows and the acknowledgment accounts for three, one row has no disposition, and you need to know which one and why.</p>
<p>A rejected row closes only when corrected, source-backed data are resubmitted and accepted, with both receipts kept. Export only the fields the destination requires, through the approved channel. A registry does not need a patient&rsquo;s full chart, and sending more than it needs is a privacy problem (Module 8).</p>
{{key:A sent file is not a closed cycle. Keep the acknowledgment, and chase every row that lacks one.}}
<p>The toolkit&rsquo;s batch reconciliation calculator does the balance for you.</p>
{{scene:Twelve sent, ten heard from|<p>A batch of 12 registry rows returns an acknowledgment for 10. The balance check shows two rows with no disposition.</p>
<p>The records officer calls the receiving office. One row was held because a date field was blank; the other had been silently dropped as a duplicate of a row sent the month before. She corrects the first, documents the second as withdrawn, and the batch balances.</p>
<p class="tc-scene-take">Without the balance check, the blank date would have stayed blank for a year.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>How many rows?</strong> Three, one per event. The second row for Mr. Manalo was a duplicate with the same patient, event, and date, and should have been removed before sending.</p>
<p><strong>Mrs. Salazar.</strong> Record her original start as June 18, from the Pampanga hospital&rsquo;s referral documents, in the original-start field, and the transfer-in as November 5. Resubmit, and keep both the rejection and the new acknowledgment.</p>
<p><strong>The fourth row.</strong> The duplicate was probably dropped silently by the receiver. Confirm that with the receiving office rather than assuming it, record the answer, and mark the row as a withdrawn duplicate so that sent equals accepted plus rejected plus pending.</p>
<p><strong>Closed when</strong> all three unique events are accepted, the first rejection and the corrected acceptance are both filed, the duplicate is explained, and nothing remains without a disposition.</p>
<p>Mrs. Salazar&rsquo;s wrong date would have made her five months newer to dialysis than she is, in a national registry, for years. Part of your role is to send the country the same truth your charts hold.</p>
"""],
    "skills": {"title": "Registry event ledger and batch reconciliation",
               "intro": "Build and close a fictional registry batch while your preceptor observes.",
               "items": [
                   ("Distinguishes PRDR reporting from PDD registration.", False),
                   ("Extracts registry fields from the authenticated chart, not from memory or the schedule.", False),
                   ("Records a transfer-in with the original start date and its source.", True),
                   ("Removes duplicate event rows before submission using a deduplication key.", False),
                   ("Balances sent against accepted, rejected, and pending, and investigates any variance.", False),
                   ("Closes a rejection only with corrected, source-backed data and both receipts.", True),
               ],
               "placement": "Find last cycle&rsquo;s registry acknowledgments and check that every sent row has a disposition."},
    "terms": [("PRDR", "Philippine Renal Disease Registry."), ("REDCOP", "Renal Disease Control Program."),
              ("PDD", "PhilHealth Dialysis Database."), ("ESRD", "End-stage renal disease."), ("PD", "Peritoneal dialysis."),
              ("Sensitivity of a form", "The share of true conditions a form captures."),
              ("Transfer-in", "Arrival of a patient already on dialysis elsewhere."),
              ("Deduplication key", "The fields that together identify one event, used to catch duplicates.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["07"])
