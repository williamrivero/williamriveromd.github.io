# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 05: Coding: ICD-10 Today, ICD-11 Tomorrow, and Compliant Queries. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and a nephrologist reviewing a written documentation query together at a nurses' station.",
    "objectives": [
        "Find and verify a diagnosis code in the classification required for a given output and service date.",
        "Tell a diagnosis field from a procedure field.",
        "Explain where the Philippines stands on the move from ICD-10 to ICD-11, and what not to change until PhilHealth instructs.",
        "Write a documentation query that asks without leading.",
    ],
    "big": """
{{plain:A code is a translation of what the physician wrote into a language that payers, registries, and statisticians can count. A translation can only be as faithful as the original.}}
<p>When the source note is vague, the temptation is to help by picking the code that pays or that seems clinically likely. That turns a translation into an invention, the exact failure payer audits are designed to catch. When the note is unclear, the records officer&rsquo;s tool is a question to the physician, not a guess.</p>
{{cards:Key terms for this module|ICD-10::International Classification of Diseases, 10th Revision.|ICD-11::The 11th Revision, in effect globally since January 1, 2022.|Tabular list::The main body of the classification, where a code is confirmed.|Query::A written request to a clinician to clarify documentation.|Acute kidney injury (AKI)::Acute kidney injury.|Chronic kidney disease (CKD)::Chronic kidney disease.}}
""",
    "case": {"title": "AKI or CKD5?", "html": """
<p>Fictional patient SIM-043 has a signed discharge abstract dated October 28 that says &ldquo;AKI.&rdquo; An unsigned intake note dated November 2 says &ldquo;CKD5?&rdquo; The claims staging list already shows procedure 90935 with diagnosis N18.5. The claims clerk says, &ldquo;She dialyzes three times a week. It&rsquo;s obviously CKD5.&rdquo;</p>
""", "questions": ["Can the claim go out as staged?",
                  "What does a compliant query to the physician look like?",
                  "What happens to the claim while the query is open?"]},
    "sections": [
        ("source", "The source", "Start from the authenticated note", """
<p>The diagnosis comes from the physician&rsquo;s signed documentation, never from a laboratory value, a treatment pattern, or the expected reimbursement. Three sessions a week can <em>prompt</em> a query about chronic kidney disease (CKD) stage 5; it cannot <em>establish</em> the diagnosis.</p>
<p>Verify every code in two steps: look up the term in the alphabetic index, then <strong>confirm in the tabular list</strong>, reading inclusion and exclusion notes, &ldquo;use additional code&rdquo; instructions, and the level of specificity required. Record the source note, service date, classification and version, and the verifier.</p>
{{fig:mro05_code}}
"""),
        ("fields", "Fields and versions", "Diagnosis, procedure, and which classification", """
<p>N18.5 is a diagnosis code: what the patient has. 90935 is a procedure code from the relative value scale: what was done. They go in different fields, and a claim with them swapped will reject. PhilHealth&rsquo;s HD circular distinguishes CKD stage 5 (N18.5) from acute kidney injury (AKI, the N17 category) for emergency hemodialysis.[[dch_philhealth2024]]</p>
<p>Claims follow the code lists in PhilHealth&rsquo;s own issuances. When DOH updated ICD-10 for statistics in 2016, PhilHealth told providers to keep using the codes in its case-rate circulars until it issued a new instruction.[[mro_ph2017icd]] The 11th Revision (ICD-11) took effect globally on January 1, 2022, and the World Health Organization lets countries keep ICD-10 during transition.[[mro_who_icd11]] DOH Administrative Order 2025-0021, dated October 14, 2025, sets ICD-11 implementation guidelines and covers DOH offices, PhilHealth, local governments, and public and private facilities.[[mro_doh2025icd11]] Its claims switch-over and dual-coding dates are not confirmed in this course: wait for PhilHealth&rsquo;s written instruction, through your claims lead, before changing any code on a claim. Meanwhile, keep the version field on every coded record so each code can be traced to its classification.</p>
"""),
        ("query", "Queries", "Asking without leading", """
<p>When documentation is unclear, conflicting, or incomplete, ask the responsible physician in writing, in the chart&rsquo;s query workflow. A compliant query presents the facts already in the record with their source and date; asks an open question or offers clinically reasonable options, including &ldquo;other&rdquo; and &ldquo;unable to determine&rdquo;; never mentions reimbursement; and never suggests a diagnosis the record does not support. Keep the query, the response, and the final code together. An unanswered query stays pending; it never defaults to the coder&rsquo;s guess.</p>
<div class="table-wrap"><table>
<thead><tr><th>Leading (do not use)</th><th>Non-leading</th></tr></thead>
<tbody>
<tr><td>&ldquo;Please document CKD stage 5 so the claim can be filed.&rdquo;</td><td>&ldquo;The discharge abstract (October 28, signed) states AKI; the intake note (November 2, unsigned) states CKD5?. Please clarify the diagnosis and, if applicable, the CKD stage: AKI / CKD (stage __) / both / other / unable to determine.&rdquo;</td></tr>
</tbody></table></div>
{{key:Code only what an authenticated note says. Ask; do not lead.}}
"""),
    ],
    "debrief": ["""
<p><strong>The claim.</strong> No. The only authenticated diagnosis says AKI; N18.5 is unsupported until the physician clarifies.</p>
<p><strong>The query.</strong> Cite both notes with their dates and authentication status and offer AKI, CKD (stage), both, other, or unable to determine. Do not mention the claim.</p>
<p><strong>While it is open.</strong> Hold the staged claim and tell the claims lead. When the signed answer arrives, the authorized coder validates the code for the service date and the approved form.</p>
"""],
    "skills": {"title": "Code validation and compliant query",
               "intro": "Validate two fictional coded encounters and write one query with a preceptor.",
               "items": [
                   ("Codes only from authenticated documentation.", True),
                   ("Confirms the code in the tabular list and records classification and version.", False),
                   ("Places diagnosis and procedure codes in the correct fields.", False),
                   ("Writes a query that presents facts, offers options including other and unable to determine, and omits reimbursement.", True),
                   ("Holds the claim while the query is pending.", True),
               ],
               "placement": "Ask your claims lead for PhilHealth&rsquo;s latest written instruction on ICD-10 and ICD-11 for claims and file it in your source register."},
    "terms": [("ICD-10", "International Classification of Diseases, 10th Revision."), ("ICD-11", "International Classification of Diseases, 11th Revision."),
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
