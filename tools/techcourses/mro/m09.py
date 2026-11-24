# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 09: Certificates, Clinical Abstracts, and Patient Requests. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer handing a draft clinical abstract with a source sheet to a nephrologist for review and signature.",
    "objectives": [
        "Recognize the common document requests a dialysis unit receives.",
        "Prepare a draft from the authenticated chart, with a source sheet, for physician authorship.",
        "Compute and verify the facts a certificate usually states: first dialysis date, vintage, frequency, and serology dates.",
        "Release the signed document through the five checks of Module 8, and log turnaround.",
    ],
    "big": """
{{plain:A certificate carries the physician&rsquo;s signature and license number, so it is the physician&rsquo;s statement. But it is built from the record the records officer keeps.}}
<p>People with chronic kidney disease (CKD) on dialysis need paperwork constantly: a clinical abstract for PhilHealth or a health maintenance organization (HMO), a certification for a transient unit while traveling, a letter for an employer, support for a persons-with-disability (PWD) application, a transplant referral. A wrong start date or an outdated hepatitis result on any of these is a false statement under the physician&rsquo;s name.</p>
{{cards:Key terms for this module|Clinical abstract::A physician-signed summary of a patient&rsquo;s condition and care.|Dialysis vintage::Time since the first-ever dialysis.|Transient dialysis::Treatment at another unit while traveling.|Source sheet::A list of each fact on a draft, the document it came from, and that document&rsquo;s date.|Person with disability (PWD)::Person with disability.|Health maintenance organization (HMO)::Health maintenance organization.}}
""",
    "case": {"title": "Cebu on December 10", "html": """
<p>Fictional patient SIM-045 flies to Cebu on December 10 and needs a transient dialysis certification. The receiving unit requires hepatitis serologies collected within 90 days. The referral packet shows first-ever hemodialysis on March 3, 2021; the first session at your unit was January 12, 2024. The latest hepatitis B surface antigen and anti-hepatitis C results are negative, collected July 30, 2026. Today is November 24, 2026.</p>
""", "questions": ["What dialysis vintage goes on the draft?",
                  "Are the serologies acceptable for the receiving unit?",
                  "Who signs, and how is the certificate released?"]},
    "sections": [
        ("roles", "Who does what", "Prepare, author, release", """
{{fig:mro09_cert}}
<p>The records officer <strong>prepares</strong>: pulls verified facts from the authenticated chart, fills the facility template, attaches a source sheet, and flags gaps. The attending physician <strong>authors</strong>: reviews, edits, decides what is clinically stated, and signs with license and professional tax receipt numbers. Release then follows identity, authority, purpose, scope, and channel. The records officer never signs, never stamps a pre-signed form, and never adds a clinical statement the physician did not make.</p>
{{call:No pre-signed blank certificates, ever. A signature belongs to a reviewed document.}}
"""),
        ("requests", "Common requests", "What each request usually needs", """
<div class="table-wrap"><table>
<thead><tr><th>Request</th><th>Facts drawn from the chart</th></tr></thead>
<tbody>
<tr><td>Clinical abstract for PhilHealth, an HMO, or a registry</td><td>Diagnosis with ICD-10 code; documented cause of kidney failure; first dialysis date and vintage; modality and frequency; vascular access; medications; latest serologies with dates; isolation status</td></tr>
<tr><td>Transient dialysis certification</td><td>Current prescription; dry weight; access; latest serologies and dates; allergies; recent events</td></tr>
<tr><td>Employer or school letter</td><td>Schedule and frequency; any functional statement only as the physician writes it</td></tr>
<tr><td>PWD application support</td><td>Diagnosis and chronicity as documented; the physician completes any disability statement</td></tr>
<tr><td>Transplant referral</td><td>Full clinical summary assembled with the clinical team</td></tr>
</tbody></table></div>
"""),
        ("dates", "Getting dates right", "Vintage, serologies, and the request log", """
<p><strong>Dialysis vintage</strong> counts from the <em>first-ever</em> dialysis, not the first session at this unit &mdash; the same distinction as registry start dates in Module 7. Take the first-ever date from the referral documents, record its source, and compute vintage as of the certificate date. State each serology with its collection date. If the latest result is older than the receiving unit requires, flag it for the physician rather than quietly writing &ldquo;negative.&rdquo;</p>
<p>Keep a request log: date received, requester and authority, purpose, document type, who prepared the draft, physician, date signed, date released, channel, and copy retained. Turnaround time is a service measure worth tracking. Follow the facility&rsquo;s posted fee policy, and route any dispute about release for continuity of care to the unit manager rather than withholding a document as leverage.</p>
{{key:Attach a source sheet to every draft. The physician can verify it in minutes.}}
"""),
    ],
    "debrief": ["""
<p><strong>Vintage.</strong> From March 3, 2021: 5 years, 8 months, and 21 days as of November 24, 2026, with the referral packet as the recorded source. Not from 2024.</p>
<p><strong>Serologies.</strong> Collected July 30, they will be 133 days old on December 10 &mdash; beyond the 90-day requirement. Flag this for the physician, who may order repeat tests and update the draft when results return.</p>
<p><strong>Signing and release.</strong> The physician reviews the draft and source sheet and signs. Release it to the patient in person after checking ID, and log the request through release.</p>
"""],
    "skills": {"title": "Certificate preparation and release",
               "intro": "Prepare a fictional clinical abstract and a transient certification with a preceptor.",
               "items": [
                   ("Drafts from the authenticated chart and attaches a source sheet.", False),
                   ("Computes vintage from the first-ever dialysis date and records its source.", False),
                   ("Flags serologies older than the receiving unit&rsquo;s requirement.", True),
                   ("Leaves authorship and signature to the physician; refuses pre-signed blanks.", True),
                   ("Releases through the five checks and logs turnaround.", False),
               ],
               "placement": "Review your unit&rsquo;s certificate templates and check that each one names the source of every fact."},
    "terms": [("Clinical abstract", "A physician-signed summary of a patient&rsquo;s condition and care."),
              ("Dialysis vintage", "Time since the first-ever dialysis."), ("Transient dialysis", "Treatment at another unit while traveling."),
              ("Source sheet", "Each fact on a draft with its source document and date."),
              ("PWD", "Person with disability."), ("HMO", "Health maintenance organization.")],
    "readings": [("travel-dialysis-ckd.html", "Planning dialysis while traveling."),
                 ("pwd-card-ckd.html", "The PWD card for people with chronic kidney disease.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["09"])
