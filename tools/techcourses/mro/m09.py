# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 09: Certificates, Clinical Abstracts, and Patient Requests. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer preparing a draft clinical abstract with a source sheet for a physician's review.",
    "objectives": [
        "Explain who prepares, who authors, and who releases a certificate, and why the records officer never signs.",
        "List the facts each common request usually needs, drawn from the authenticated chart.",
        "Compute dialysis vintage from the first-ever dialysis date and record its source.",
        "Check the age of serology results against the receiving unit&rsquo;s requirement and flag them when they are too old.",
        "Keep a request log and release certificates through the five checks.",
    ],
    "big": """
{{plain:A certificate is a promise written in the physician&rsquo;s name. The physician signs it, so it is the physician&rsquo;s statement. But the physician usually writes it from a draft, and the draft is built from the record you keep. If the record is wrong, the promise is broken before anyone signs.}}
<p>The picture is useful, and it has one limit. A broken promise between friends can be explained. A wrong certificate travels to the payer, to an insurer, to an employer, to another dialysis unit in another city, and the physician whose license number is printed on it cannot explain it to people they will never meet.</p>
<p>People with chronic kidney disease (CKD) on dialysis need paperwork constantly: a clinical abstract for the Philippine Health Insurance Corporation (PhilHealth) or a health maintenance organization (HMO), a certification for a transient unit while traveling, a letter for an employer, support for a person-with-disability (PWD) application, a transplant referral. A wrong start date or an outdated hepatitis result on any of these is a false statement under the physician&rsquo;s name, and at a transient unit it can be a safety problem too.</p>
{{cards:Key terms for this module|Clinical abstract::A physician-signed summary of a patient&rsquo;s condition and care.|Dialysis vintage::Time since the first-ever dialysis, wherever it happened.|Transient dialysis::Treatment at another unit while the patient is traveling.|Serology::Blood tests for infections such as hepatitis B and hepatitis C, each with a collection date.|Source sheet::A list of each fact on a draft, the document it came from, and that document&rsquo;s date.|Turnaround time::Days from a complete request to release.}}
""",
    "case": {"title": "Cebu on December 10", "html": """
<p>Mrs. Gloria Santiago, 63, comes to the records window on Tuesday, November 24, 2026. Her granddaughter is getting married in Cebu, and Mrs. Santiago flies there on December 10 for two weeks. She needs a transient dialysis certification. She hands you a printed checklist from the receiving unit in Cebu: it requires hepatitis serologies collected within 90 days.</p>
<p>You open her chart. The referral packet from her previous unit shows her first-ever hemodialysis on March 3, 2021. Her first session at your unit was January 12, 2024. Her latest hepatitis B surface antigen and anti-hepatitis C results are both negative, collected July 30, 2026.</p>
<p>&ldquo;Can you just print it today?&rdquo; she asks. &ldquo;Dr. Mendoza usually signs these on Thursdays.&rdquo;</p>
""", "questions": ["What dialysis vintage goes on the draft?",
                  "Are the serologies acceptable for the receiving unit?",
                  "Who signs, and how is the certificate released?"]},
    "sections": [
        ("roles", "Who does what", "Prepare, author, release", """
{{fig:mro09_cert}}
<p>Every certificate passes through three stages, and each stage belongs to a different person.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Who</th><th>What they do</th></tr></thead>
<tbody>
<tr><td>Prepare</td><td>The records officer</td><td>Pulls verified facts from the authenticated chart, fills the facility template, attaches a source sheet, and flags gaps</td></tr>
<tr><td>Author</td><td>The attending physician</td><td>Reviews, edits, decides what is clinically stated, and signs with license and professional tax receipt numbers</td></tr>
<tr><td>Release</td><td>The records officer</td><td>Releases through identity, authority, purpose, scope, and channel (Module 8), and logs it</td></tr>
</tbody></table></div>
<p>The records officer never signs, never stamps a pre-signed form, and never adds a clinical statement the physician did not make. &ldquo;Fit to travel,&rdquo; &ldquo;stable,&rdquo; &ldquo;unable to work,&rdquo; and &ldquo;no contraindication&rdquo; are clinical judgments. If the template has a blank for them, it stays blank on the draft for the physician to fill.</p>
{{call:No pre-signed blank certificates, ever, not even &ldquo;for emergencies while the doctor is away.&rdquo; A signature belongs to a reviewed document. If a certificate is urgent and the physician is unavailable, ask the covering physician on the unit&rsquo;s escalation list.}}
{{scene:The certificate in the drawer|<p>A new records officer finds a folder of blank certificate forms, each already signed and stamped by a physician who left the unit last year, &ldquo;for emergencies.&rdquo;</p>
<p>She gives the folder to the unit manager, who has the forms destroyed with a witness and a disposition record, and writes to the former physician to explain. The unit&rsquo;s procedure now names a covering physician for urgent certificates.</p>
<p class="tc-scene-take">A signature belongs to a document someone reviewed. Pre-signed blanks belong to no one.</p>}}
"""),
        ("requests", "Common requests", "What each request usually needs", """
<div class="table-wrap"><table>
<thead><tr><th>Request</th><th>Facts drawn from the chart</th><th>Watch for</th></tr></thead>
<tbody>
<tr><td>Clinical abstract for PhilHealth, an HMO, or a registry</td><td>Diagnosis with International Classification of Diseases, 10th Revision (ICD-10) code; documented cause of kidney failure; first dialysis date and vintage; modality and frequency; vascular access; medications; latest serologies with dates; isolation status</td><td>An unsigned diagnosis (Module 5); a first-at-this-unit date used as the first-ever date</td></tr>
<tr><td>Transient dialysis certification</td><td>Current prescription; dry weight; access; latest serologies and dates; allergies; recent events</td><td>Serologies older than the receiving unit allows</td></tr>
<tr><td>Employer or school letter</td><td>Schedule and frequency; any functional statement only as the physician writes it</td><td>Requests for diagnoses or test results the purpose does not need</td></tr>
<tr><td>PWD application support</td><td>Diagnosis and chronicity as documented; the physician completes any disability statement</td><td>Staff filling in disability wording themselves</td></tr>
<tr><td>Transplant referral</td><td>A full clinical summary assembled with the clinical team</td><td>Missing access history and transfusion records</td></tr>
</tbody></table></div>
<p>An employer letter is a common scope trap. The employer needs to know that the patient dialyzes on Monday, Wednesday, and Friday mornings and cannot work those hours. The employer does not need the hepatitis status or the cause of kidney failure. The physician decides what goes in; your draft should not offer more than the purpose requires.</p>
{{scene:What the employer needed|<p>Mr. Reynaldo Pascua&rsquo;s employer asks for &ldquo;a medical certificate&rdquo; to justify his absences. The draft template includes diagnosis, cause of kidney failure, hepatitis status, and medications.</p>
<p>The records officer prepares a draft limited to his dialysis schedule and the physician&rsquo;s statement on working hours, and leaves the rest for the physician to decide. The physician signs it as drafted. Mr. Pascua keeps his job, and his hepatitis status stays private.</p>
<p class="tc-scene-take">Scope is set by purpose. An employer needs to plan around a schedule, not to know a diagnosis.</p>}}
"""),
        ("dates", "Getting dates right", "Vintage, serologies, and the request log", """
<h3>Dialysis vintage</h3>
<p>Dialysis vintage counts from the <em>first-ever</em> dialysis, not the first session at this unit. This is the same distinction as registry start dates in Module 7, and it is the most common error on Philippine certificates. Take the first-ever date from the referral documents, record its source on the source sheet, and compute vintage as of the certificate date.</p>
{{formula:<strong>Vintage</strong> = certificate date &minus; first-ever dialysis date.<br>Example: first-ever dialysis March 3, 2021, certificate dated November 24, 2026: 5 years, 8 months, and 21 days.}}
<p>Why does it matter so much? Vintage affects how other clinicians judge a patient&rsquo;s vascular access history, their risks, and in some programs their place on a transplant waiting list. A patient who has dialyzed for five years but is certified as dialyzing for two loses three years of their own history.</p>
<h3>Serology dates</h3>
<p>State each serology with its collection date, never as a bare &ldquo;negative.&rdquo; A hepatitis result is a fact about one day. Receiving units set their own limits on how old a result may be, because a patient who was negative in July could have been infected since. If the latest result is older than the receiving unit requires, flag it for the physician. Do not quietly write &ldquo;negative&rdquo; and leave the receiving unit to discover the date.</p>
<p>The toolkit&rsquo;s vintage and serology-age calculator does both computations.</p>
<h3>The request log</h3>
<p>Keep a log of every request: date received, requester and authority, purpose, document type, who prepared the draft, the physician, date signed, date released, channel, and copy retained. Turnaround time, from complete request to release, is a service measure worth tracking, because a certificate that arrives after the flight is no help to anyone.</p>
<p>Follow the facility&rsquo;s posted fee policy. Route any dispute about releasing records needed for continuity of care to the unit manager rather than withholding a document as leverage. A patient who owes the unit money still needs her transfer orders.</p>
{{key:Attach a source sheet to every draft. The physician can verify it in minutes, and every fact on the certificate can be traced back to a page in the chart.}}
{{scene:Five years, not two|<p>Mrs. Corazon Gatdula needs a clinical abstract for a transplant work-up. The unit&rsquo;s template pulls her &ldquo;dialysis start&rdquo; from her first session at this unit, two years ago.</p>
<p>The records officer checks the referral packet: first-ever hemodialysis five years earlier, at a hospital in Quezon City. She corrects the source sheet, the physician signs the corrected vintage, and the transplant program receives an accurate history.</p>
<p class="tc-scene-take">Three missing years would have been three years of her history erased from the decision.</p>}}
{{fig:mro09_fig_09_dialysis_vintage_serology_dates}}
"""),
    ],
    "debrief": ["""
<p><strong>Vintage.</strong> From March 3, 2021: 5 years, 8 months, and 21 days as of November 24, 2026, with the referral packet recorded as the source. Not from January 12, 2024, which would cut almost three years from her history.</p>
<p><strong>Serologies.</strong> Collected July 30, they will be 133 days old on December 10, well beyond the Cebu unit&rsquo;s 90-day requirement. Flag this on the draft for Dr. Mendoza, who may order repeat tests. Tell Mrs. Santiago now, so there is time to collect blood and get results before she flies. If repeat results return in early December, update the draft with the new dates.</p>
<p><strong>Signing and release.</strong> Not today. Prepare the draft and the source sheet, and give them to Dr. Mendoza on Thursday. After she reviews and signs, release the certificate to Mrs. Santiago in person after checking her ID, or send it through the approved channel to the Cebu unit if she authorizes that. Log the request from receipt to release.</p>
<p>Printing it today would have sent Mrs. Santiago to Cebu with a certificate the receiving unit would reject at the door, two days before a wedding. Part of your role is to find the problem in November, when there is still time to fix it.</p>
"""],
    "skills": {"title": "Certificate preparation and release",
               "intro": "Prepare a fictional clinical abstract and a transient certification while your preceptor observes.",
               "items": [
                   ("Drafts from the authenticated chart and attaches a source sheet.", False),
                   ("Leaves every clinical judgment blank for the physician to complete.", True),
                   ("Computes vintage from the first-ever dialysis date and records its source.", False),
                   ("States each serology with its collection date and flags results older than the receiving unit&rsquo;s requirement.", True),
                   ("Limits an employer letter to what its purpose requires.", False),
                   ("Leaves authorship and signature to the physician; refuses pre-signed blanks.", True),
                   ("Releases through the five checks and logs turnaround.", False),
               ],
               "placement": "Review your unit&rsquo;s certificate templates and check that each one names the source of every fact."},
    "terms": [("Clinical abstract", "A physician-signed summary of a patient&rsquo;s condition and care."),
              ("Dialysis vintage", "Time since the first-ever dialysis."), ("Transient dialysis", "Treatment at another unit while traveling."),
              ("Source sheet", "Each fact on a draft with its source document and date."),
              ("Serology", "Blood tests for infections, each with a collection date."),
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
