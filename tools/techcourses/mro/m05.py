# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 05: Diagnosis Coding and Physician Queries. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer comparing a signed discharge abstract with a coding reference book.",
    "objectives": [
        "Code only from authenticated physician documentation, and explain why treatment patterns and reimbursement never establish a diagnosis.",
        "Confirm a code in the tabular list and record its classification and version.",
        "Place diagnosis and procedure codes in their correct fields.",
        "Explain the current position on the International Classification of Diseases, 10th Revision (ICD-10) and its successor ICD-11 for Philippine Health Insurance Corporation (PhilHealth) claims, and what is still unconfirmed.",
        "Write a compliant, non-leading physician query and hold the claim while it is open.",
    ],
    "big": """
{{plain:A code is a translation. The physician writes a diagnosis in words; the code translates it into a language that payers, registries, and statisticians can count. Like any translation, it can only be as faithful as the original. A translator who improves on the author has stopped translating.}}
<p>The picture is useful, and it has one limit. A translator who finds a vague sentence can usually ask the author what they meant, and so can you. But in a busy unit the author is often not at the desk, the claim is due, and someone nearby is sure they know the answer. That is the moment this module is about.</p>
<p>When the source note is vague, the temptation is to help: to pick the code that pays, or the one that seems clinically likely. That turns a translation into an invention, which is the exact failure payer audits are designed to catch. When the note is unclear, the records officer&rsquo;s tool is a question to the physician, never a guess.</p>
{{cards:Key terms for this module|International Classification of Diseases, 10th Revision (ICD-10)::The classification most Philippine claims and statistics use today.|ICD-11::The 11th Revision, in effect globally since January 1, 2022.|Alphabetic index::The part of the classification where you look a term up first.|Tabular list::The main body of the classification, where a code is confirmed and its notes are read.|Query::A written request to a clinician to clarify documentation.|Acute kidney injury (AKI)::A sudden loss of kidney function, which may recover.|Chronic kidney disease (CKD)::Kidney damage or reduced function lasting more than three months; stage 5 is kidney failure.}}
""",
    "case": {"title": "AKI or CKD5?", "html": """
<p>Mrs. Leonora Castillo, 54, started hemodialysis at your unit on November 2 after a hospital stay. Her signed hospital discharge abstract, dated October 28, gives the diagnosis as &ldquo;AKI.&rdquo; An intake note in your unit, dated November 2 and not yet signed, says &ldquo;CKD5?&rdquo;</p>
<p>The claims staging list already shows her sessions with procedure code 90935 and diagnosis code N18.5, chronic kidney disease stage 5.</p>
<p>Mr. Boyet Ramos, the claims clerk, shrugs. &ldquo;She dialyzes three times a week. It&rsquo;s obviously CKD5. If we put AKI, PhilHealth will just ask more questions. Can you sign off so I can send the batch today?&rdquo;</p>
""", "questions": ["Can the claim go out as staged?",
                  "What does a compliant query to the physician look like?",
                  "What happens to the claim while the query is open?"]},
    "sections": [
        ("source", "The source", "Start from the authenticated note", """
<p>The diagnosis comes from the physician&rsquo;s signed documentation. It never comes from a laboratory value, a treatment pattern, a previous code, or the expected payment.</p>
<p>Why be so strict? Because each of those other sources can be right most of the time and dangerously wrong some of the time. A patient on dialysis three times a week usually has chronic kidney disease (CKD) stage 5. But some patients start dialysis for acute kidney injury (AKI) and recover enough to stop. If the record calls them CKD stage 5 from day one, the error follows them into registries, insurance, employment paperwork, and the clinical thinking of every physician who reads the chart later.</p>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Can it prompt a query?</th><th>Can it establish a diagnosis?</th></tr></thead>
<tbody>
<tr><td>Signed physician diagnosis</td><td>&mdash;</td><td>Yes</td></tr>
<tr><td>Unsigned or draft note</td><td>Yes</td><td>No, until authenticated</td></tr>
<tr><td>Laboratory result (a high creatinine, a low hemoglobin)</td><td>Yes</td><td>No</td></tr>
<tr><td>Treatment pattern (three sessions a week)</td><td>Yes</td><td>No</td></tr>
<tr><td>Last year&rsquo;s code</td><td>Yes</td><td>No</td></tr>
<tr><td>What the claim needs to pay</td><td>No</td><td>Never</td></tr>
</tbody></table></div>
<h3>Two steps for every code</h3>
<p>Verify every code in two steps. First, look up the term in the alphabetic index. Second, <strong>confirm the code in the tabular list</strong>, reading its inclusion and exclusion notes, any &ldquo;use additional code&rdquo; instructions, and the level of specificity required. The index points you to a neighborhood; the tabular list tells you whether you are at the right address. Record the source note, the service date, the classification and version, and who verified it.</p>
{{fig:mro05_code}}
{{scene:The patient who stopped dialysis|<p>Mr. Wilfredo Cajucom started dialysis after a severe infection. His intake note said &ldquo;CKD5?&rdquo;; his signed discharge abstract said &ldquo;AKI.&rdquo; The records officer coded nothing until the physician answered her query: &ldquo;AKI, monitor for recovery.&rdquo;</p>
<p>Six weeks later his urine output returned and dialysis was stopped. His record, registry entry, and PhilHealth claims all said AKI, so nothing had to be unwound.</p>
<p class="tc-scene-take">A treatment pattern suggested chronic kidney failure. The physician knew better, and the query let the record say so.</p>}}
"""),
        ("fields", "Fields and versions", "Diagnosis, procedure, and which classification", """
<p>Diagnosis codes and procedure codes answer different questions, and they live in different fields.</p>
<div class="table-wrap"><table>
<thead><tr><th>Code</th><th>Kind</th><th>Answers</th></tr></thead>
<tbody>
<tr><td>N18.5</td><td>Diagnosis (ICD-10)</td><td>What the patient has: CKD stage 5</td></tr>
<tr><td>N17 category</td><td>Diagnosis (ICD-10)</td><td>What the patient has: AKI</td></tr>
<tr><td>90935</td><td>Procedure (relative value scale)</td><td>What was done: hemodialysis</td></tr>
</tbody></table></div>
<p>A claim with the two swapped will reject. The Philippine Health Insurance Corporation (PhilHealth) hemodialysis circular distinguishes CKD stage 5 (N18.5) from AKI (the N17 category) for emergency hemodialysis, so the distinction in Mrs. Castillo&rsquo;s case is not academic.[[dch_philhealth2024]]</p>
<h3>ICD-10, ICD-11, and the claim</h3>
<p>Claims follow the code lists in PhilHealth&rsquo;s own issuances, not the newest edition of the classification. When the Department of Health (DOH) updated ICD-10 for statistics in 2016, PhilHealth told providers to keep using the codes in its case-rate circulars until it issued a new instruction.[[mro_ph2017icd]]</p>
<p>ICD-11 took effect globally on January 1, 2022, and the World Health Organization allows countries to keep ICD-10 during transition.[[mro_who_icd11]] DOH Administrative Order 2025-0021, dated October 14, 2025, sets ICD-11 implementation guidelines and covers DOH offices, PhilHealth, local governments, and public and private facilities.[[mro_doh2025icd11]] Its claims switch-over and dual-coding dates are not confirmed in this course.</p>
<p>So the rule for now is simple. Wait for PhilHealth&rsquo;s written instruction, through your claims lead, before changing any code on a claim. Meanwhile, record the classification and version on every coded record, so that when the switch comes, every code can be traced to the classification it was assigned in.</p>
{{scene:The swapped fields|<p>A batch of claims comes back rejected. On every one, the clerk had typed N18.5 into the procedure field and 90935 into the diagnosis field, after a change to the claims software rearranged the screen.</p>
<p>The records officer shows the clerk the difference: one code says what the patient has, the other what was done. The claims lead asks the vendor to label the fields clearly, and the batch is corrected and resubmitted with both original and corrected copies kept.</p>
<p class="tc-scene-take">Diagnosis and procedure codes answer different questions. A screen change does not change which is which.</p>}}
"""),
        ("query", "Queries", "Asking without leading", """
<p>When documentation is unclear, conflicting, or incomplete, ask the responsible physician in writing, in the chart&rsquo;s query workflow. A good query has four features.</p>
<ul>
<li>It presents the facts already in the record, each with its source and date.</li>
<li>It asks an open question, or offers clinically reasonable options that include &ldquo;other&rdquo; and &ldquo;unable to determine.&rdquo;</li>
<li>It never mentions reimbursement, the claim, or the deadline.</li>
<li>It never suggests a diagnosis the record does not support.</li>
</ul>
<div class="table-wrap"><table>
<thead><tr><th>Leading (do not use)</th><th>Non-leading</th></tr></thead>
<tbody>
<tr><td>&ldquo;Please document CKD stage 5 so the claim can be filed.&rdquo;</td><td>&ldquo;The discharge abstract (October 28, signed) states AKI. The intake note (November 2, unsigned) states CKD5?. Please clarify the diagnosis and, if applicable, the CKD stage: AKI / CKD (stage __) / both / other / unable to determine.&rdquo;</td></tr>
<tr><td>&ldquo;Patient is on HD 3x a week. CKD5, right?&rdquo;</td><td>&ldquo;Please clarify the diagnosis supporting maintenance dialysis, based on your clinical judgment.&rdquo;</td></tr>
<tr><td>&ldquo;PhilHealth will deny AKI. Can we use N18.5?&rdquo;</td><td>Do not send. A query never discusses payment.</td></tr>
</tbody></table></div>
<p>Keep the query, the physician&rsquo;s response, and the final code together in the record. An unanswered query stays pending. It never defaults to the coder&rsquo;s guess, and it never expires into a code.</p>
<p>Why does leading matter so much? Because a physician answering a leading query is no longer giving an independent clinical opinion. They are agreeing with yours. If an auditor later sees a query that names the answer and mentions the claim, the code that followed looks like a code chosen for payment, whatever the truth.</p>
{{key:Code only what an authenticated note says. Ask; do not lead. Never mention money in a query.}}
{{scene:The query that changed nothing, and everything|<p>A query asks Dr. Salvador Ilagan to clarify Mrs. Josefina Mercado&rsquo;s diagnosis: &ldquo;AKI / CKD (stage __) / both / other / unable to determine.&rdquo; He writes back: &ldquo;Both. CKD stage 4 at baseline, AKI on CKD this admission.&rdquo;</p>
<p>That answer was not among the guesses anyone in the office had made. It changed her code, her registry status, and the plan to recheck her kidney function in three months.</p>
<p class="tc-scene-take">Offering &ldquo;both&rdquo; and &ldquo;other&rdquo; is not politeness. It is how the record gets the answer no one expected.</p>}}
{{fig:mro05_fig_05_leading_vs_nonleading_query}}
"""),
        ("pressure", "Under pressure", "When someone wants the code changed", """
<p>Pressure to change a code rarely sounds like fraud. It sounds like common sense, deadlines, and kindness to the patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>What you may hear</th><th>A good response</th></tr></thead>
<tbody>
<tr><td>&ldquo;It&rsquo;s obviously CKD5.&rdquo;</td><td>&ldquo;It may well be. The physician needs to write it, and I&rsquo;ll send the query now.&rdquo;</td></tr>
<tr><td>&ldquo;The batch goes out today.&rdquo;</td><td>&ldquo;Then we hold this one claim and send the rest. A late claim can be filed; a wrong one has to be explained.&rdquo;</td></tr>
<tr><td>&ldquo;The patient can&rsquo;t afford a denial.&rdquo;</td><td>&ldquo;Agreed. That&rsquo;s why we&rsquo;ll get the documentation right, so the claim holds up.&rdquo;</td></tr>
<tr><td>&ldquo;The doctor said verbally it&rsquo;s CKD5.&rdquo;</td><td>&ldquo;Good. Can you ask the doctor to sign the intake note or answer the query? Then I can code it.&rdquo;</td></tr>
</tbody></table></div>
<p>If pressure continues, or comes from someone senior, write down what was asked and escalate to the claims lead and the Dialysis Clinical Head. You are not being difficult. You are protecting the unit, the physician, and the patient from a record that cannot be defended.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Can the claim go out as staged?</strong> No. The only authenticated diagnosis says AKI. N18.5 is unsupported until the physician clarifies. The treatment pattern can prompt a question; it cannot answer it.</p>
<p><strong>The query.</strong> Send it to the attending physician through the query workflow. Cite both notes with their dates and authentication status, and offer AKI, CKD (stage __), both, other, or unable to determine. Do not mention the claim, PhilHealth, or the batch date.</p>
<p><strong>While it is open.</strong> Hold Mrs. Castillo&rsquo;s staged claims and tell the claims lead why. The rest of the batch can go. When the signed answer arrives, the authorized coder validates the code for each service date against the current PhilHealth list and the approved form.</p>
<p><strong>And Mr. Ramos?</strong> Explain kindly, and without lecturing, that you can only code what the physician has signed. He is trying to help the patient and the unit. So are you.</p>
<p>The physician may well answer &ldquo;CKD stage 5.&rdquo; If so, nothing was lost except a day. If the answer is &ldquo;AKI, recovering,&rdquo; the query may have changed the course of her care. Part of your role is to make sure the record reflects what the physician actually decided.</p>
"""],
    "skills": {"title": "Code validation and compliant query",
               "intro": "Validate two fictional coded encounters and write one query while your preceptor observes.",
               "items": [
                   ("Codes only from authenticated documentation.", True),
                   ("States why a treatment pattern or laboratory value cannot establish a diagnosis.", False),
                   ("Confirms the code in the tabular list and records classification and version.", False),
                   ("Places diagnosis and procedure codes in the correct fields.", False),
                   ("Writes a query that presents facts, offers options including other and unable to determine, and omits reimbursement.", True),
                   ("Holds the claim while the query is pending and tells the claims lead.", True),
                   ("Responds to pressure to change a code without conceding and escalates if it continues.", False),
               ],
               "placement": "Ask your claims lead for PhilHealth&rsquo;s latest written instruction on ICD-10 and ICD-11 for claims and file it in your source register."},
    "terms": [("ICD-10", "International Classification of Diseases, 10th Revision."), ("ICD-11", "International Classification of Diseases, 11th Revision."),
              ("Alphabetic index", "The part of the classification where a term is looked up first."),
              ("Tabular list", "The main body of the classification, where codes are confirmed."), ("Query", "A written request to clarify documentation."),
              ("Dual coding", "Coding the same record in two classifications during a transition."),
              ("AKI", "Acute kidney injury."), ("CKD", "Chronic kidney disease.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["05"])
