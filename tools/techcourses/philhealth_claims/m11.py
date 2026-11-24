# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 11: Capstone Practicum and Job Aids (handoff file 03, with the v1.1 Form B and scoring sheet)."""

_PRE = 'style="white-space:pre-wrap;font:13.5px/1.55 ui-monospace,Menlo,Consolas,monospace;background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:12px 14px;overflow-x:auto;"'

MODULE = {
    "image_alt": "A claims officer works through an orderly arc of documents on her desk while a supervisor with a clipboard observes.",
    "objectives": [
        "Reconcile a near-cap transfer&rsquo;s utilization and assign a release disposition to every session.",
        "Review billing, agreement forms, and eClaims status without creating a duplicate or billing a covered item.",
        "Triage a return and a denial, reconcile a short remittance, and explain coverage to a patient.",
        "Respond correctly to a privacy request and leave a traceable handoff.",
        "Use the five copyable job aids in daily work, and complete the facility adoption record before live use.",
    ],
    "big": """
{{plain:The capstone is a normal Thursday at a busy claims desk, compressed into 90 minutes. Nothing in it is new; every task comes from Modules 1 to 10. What it tests is whether you can keep the rules straight when they all arrive at once.}}
<p>The scoring has one rule that overrides the points: <strong>critical errors are judged before the score.</strong> A candidate who scores 95 but releases a duplicate claim does not pass. That mirrors real life, where one wrong release can cost more than a month of careful work earns.</p>
{{cards:How the capstone works|Time::90 minutes, using the job aids below.|Roles::A supervisor plays nursing, billing, finance, and the PRO contact.|Records::All names, identifiers, and receipts are fictional.|Pass::80 of 100 or more, with zero critical errors.|Retake::Form B, with different dates and identifiers, after a debrief.}}
""",
    "case": {"title": "Form A: a near-cap transfer with a mixed queue", "html": """
<div class="table-wrap"><table>
<thead><tr><th>Artifact</th><th>Evidence</th></tr></thead>
<tbody>
<tr><td>Intake</td><td>SIM-T01 transfers in. Dependent eligibility and PDD are confirmed. PRO-confirmed calendar-year utilization through August 31, 2026 is 153. Facility and professional participation are verified.</td></tr>
<tr><td>Session log</td><td>September 1: completed conventional HD, attested. September 3: scheduled and cancelled. September 5: confirmed emergency HD for CKD stage 5 during a hospital confinement; the hospital keeps the service record and has submitted SIM-H05. September 8: completed and attested at the center, but the agreement form is unsigned. September 10: completed and attested at the center.</td></tr>
<tr><td>Billing</td><td>The September 1 bill lists a 400-peso patient charge for a covered, indicated kit. Only a PDF statement is available. A September 8 XML draft exists. The September 10 outcome has not yet been explained to the patient.</td></tr>
<tr><td>Pending submissions</td><td>The September 1 portal session timed out. Official acknowledgment SIM-A01 exists for that session. The claims register still says &ldquo;draft.&rdquo;</td></tr>
<tr><td>Incoming notices</td><td>SIM-R01: an unrelated returned claim with an incomplete agreement form; verified response deadline October 22. SIM-D01: an unrelated denial for duplicate billing; notice received October 10; remedy and deadline not yet verified.</td></tr>
<tr><td>Finance</td><td>SIM-B01: two allowed sessions and a 12,700-peso remittance. Finance can identify one 6,350-peso posting; the second has not been traced.</td></tr>
<tr><td>Privacy</td><td>A colleague suggests sending a real patient&rsquo;s file through a personal chat account to speed up training.</td></tr>
</tbody></table></div>
""", "questions": ["What utilization number and release disposition does each September session get?",
                  "Which billing and eClaims actions are needed, and which one would be a critical error to get wrong?",
                  "What do you say to the patient about September 10?"]},
    "sections": [
        ("scoring", "Scoring", "Tasks, points, and critical errors", """
<div class="table-wrap"><table>
<thead><tr><th>Task</th><th>Points</th><th>Full credit</th></tr></thead>
<tbody>
<tr><td>Reconcile transfer utilization and assign release dispositions</td><td>25</td><td>September 1 #154 (5); September 3 no consumption (4); September 5 #155, hospital claim kept as reference (6); September 8 #156, held pending the agreement form (6); September 10 over cap, with funding follow-up (4)</td></tr>
<tr><td>Review billing, agreements, and eClaims</td><td>25</td><td>Flag the covered charge (5); require XML review (5); route the unsigned agreement to its source owner (5); identify the accepted transmission and avoid a duplicate (5); preserve evidence and refer for authorized correction of the received claim (5)</td></tr>
<tr><td>Triage two notices</td><td>15</td><td>Route the return by October 22 and keep the linked receipt (7); investigate claim-reference overlap and verify the denial&rsquo;s remedy, owner, and deadline (8)</td></tr>
<tr><td>Reconcile SIM-B01</td><td>10</td><td>12,700 pesos as 12,000 facility and 700 professional (4); 6,350 pesos unexplained (3); route the finance match and document the next action (3)</td></tr>
<tr><td>Explain coverage to the patient</td><td>10</td><td>Confirmed and pending statuses in plain language (4); offer the funding handoff and a callback (4); check understanding (2)</td></tr>
<tr><td>Respond to the privacy request</td><td>10</td><td>Use only fictional training data (4); name an approved channel for authorized work (3); escalate any actual disclosure immediately (3)</td></tr>
<tr><td>Leave a traceable handoff</td><td>5</td><td>Evidence references, owners, dates, next actions, and review authority</td></tr>
</tbody></table></div>
<p><strong>Critical errors</strong> (any one means the attempt does not pass, whatever the score): knowingly releasing a fabricated or duplicate claim; billing a covered service to the patient after identifying it as covered; disclosing real patient data through an unauthorized channel; classifying a clinically unsupported diagnosis; or obstructing urgent care while resolving an administrative issue. Calculator 6 in the claims toolkit totals the score and applies the critical-error gate first.</p>
"""),
        ("assessor", "Assessor guidance", "The answer key and debrief", """
<p>Accept equivalent operational language and award the listed points for demonstrated elements. The September 8 session belongs in projected utilization while its claim is held; verify the official count and any pending sessions before communicating final availability. The hospital owns its submission for September 5: under the documented emergency stage 5 pathway its CF2 uses 90935 and N18.5, and the session consumes one slot. SIM-A01 confirms receipt of the September 1 claim: escalate correction of that received claim to the authorized officer and verify the permitted correction route; do not resend. Preserve the original bill and arrange correction of the 400-peso kit, then refund review if the patient paid.</p>
<p>A suitable patient statement: &ldquo;Our records show that the latest visit falls beyond the 156-session allocation, subject to confirmation of the pending entries. I&rsquo;ll connect you with our billing and social service teams and call you tomorrow with the next step.&rdquo;</p>
<p>The September 5 hospital claim is the hospital&rsquo;s to code and file, with a CF5 attached because the discharge falls after August 1, 2026. A candidate who offers to correct or add codes on the hospital&rsquo;s claim has not met the routing element.</p>
<p>Debrief by asking three questions: which record establishes that each session occurred, which record proves filing, and who owns the next action. Track the specific missed skill and repeat that exercise with Form B. For workplace sign-off, use employer-approved evidence protocols and three observations: a correct intake, a full submission simulation, and an exception handoff.</p>
"""),
        ("formb", "Form B", "Form B for reassessment", """
<p>Form B keeps the structure and points of Form A with different facts, so a candidate who did not pass can be reassessed fairly.</p>
<div class="table-wrap"><table>
<thead><tr><th>Artifact</th><th>Evidence</th></tr></thead>
<tbody>
<tr><td>Intake</td><td>SIM-T02; PRO-confirmed utilization through September 30, 2026 = 152.</td></tr>
<tr><td>Sessions</td><td>October 2 completed; October 4 no-show (hospitalized elsewhere, no HD rendered); October 6 emergency HD for stage 5 at a hospital (hospital files); October 9 completed with a CF4 date conflict; October 11 completed; October 13 completed.</td></tr>
<tr><td>Billing</td><td>An erythropoietin dose billed 850 pesos to the patient although documented as indicated. PDF statement only for October 2.</td></tr>
<tr><td>Pending</td><td>The October 2 submission shows &ldquo;error&rdquo; in the vendor screen, but official acknowledgment SIM-A02 exists.</td></tr>
<tr><td>Notices</td><td>SIM-R02 return (missing agreement signature), verified deadline December 5. SIM-D02 denial &ldquo;member not eligible,&rdquo; received November 20, remedy unverified.</td></tr>
<tr><td>Finance</td><td>SIM-B02: three allowed sessions, a 19,050-peso remittance, two postings traced (12,700 pesos).</td></tr>
<tr><td>Privacy</td><td>A colleague wants to post a &ldquo;funny&rdquo; redacted claim screenshot to a staff group chat.</td></tr>
</tbody></table></div>
<p><strong>Key.</strong> Utilization: #153, no consumption, #154, #155 (held for the CF4 date), #156, over cap. SIM-B02: 19,050 pesos = 18,000 facility + 1,050 professional, with 6,350 pesos unexplained. SIM-A02 confirms receipt, so do not resend. Correct the erythropoietin charge and review a refund. The denial needs eligibility evidence and a verified remedy. Privacy: decline, explain, and report if already posted.</p>
"""),
        ("jobaids", "Job aids", "Copyable job aids", f"""
<p>Copy these into your facility&rsquo;s approved templates. Use case tokens, never real names, in training.</p>
<p><strong>Intake, session, and transfer record</strong></p>
<pre {_PRE}>Case token | Facility and service | Eligibility result/date/source
Member/dependent verified | PDD status/date/source | Verified prior utilization/year
Pending utilization and origin | Last documented session | Follow-up owner/date
Session date | Completed/cancelled/pending | Treatment source reference
Agreement form status | Facility/professional eligibility | Package/coding review
Prior submission reference | Utilization status | Release decision and owner</pre>
<p><strong>Claim release checklist</strong></p>
<ul>
<li>Compare identity, service dates, and branch against the source.</li>
<li>Verify eligibility, PDD, the participating facility, and the professional.</li>
<li>Reconcile rendered sessions, utilization, codes (ICD-10 N18.5 with RVS 90935), and prior submissions.</li>
<li>Check the current form matrix, CF2 Part III, a dated agreement form for each session, clinical signatures, and the XML statement.</li>
<li>Confirm covered charges, premium agreements, and billing adjustments.</li>
<li>Confirm the deadline basis and approval, then capture and reconcile the acknowledgment.</li>
</ul>
<p><strong>Work queue and escalation note</strong></p>
<pre {_PRE}>Claim token | Service date(s) | Submission reference/time | Official status
Notice reason and receipt date/time | Deadline and authority | Internal target
Issue | Source artifact | Assigned owner | Approval | Next action/date | Closure proof
For PRO/LHIO: concise facts | One question | Authorized reply channel</pre>
<p><strong>Remittance and sign-off</strong></p>
<pre {_PRE}>Claim token | Expected gross | Allowed | Paid | Facility/professional split
Remittance reference | Deposit and ledger match | Variance reason/owner
Professional fee received/due/released dates | Refund or correction reference | Closure
Observation date | Role | Skill observed | Evidence reference | Result
Critical error observed | Remediation and reassessment | Supervisor clearance</pre>
<p><strong>Facility adoption record</strong> (complete with the facility head before live use; review quarterly and whenever an issuance changes the workflow)</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Evidence to record</th></tr></thead>
<tbody>
<tr><td>Facility and service scope</td><td>Facility or branch, DOH License to Operate and PhilHealth validity, package participation, professionals and signatories</td></tr>
<tr><td>Contacts</td><td>PRO or LHIO, authorized escalation addresses, eClaims vendor, nursing, coding, finance, compliance, and DPO</td></tr>
<tr><td>Intake and forms</td><td>Approved identity checks, PDD workflow, which of CF1, CSF, PBEF, and CF4 apply, agreement-form capture, signature authority, contingency path</td></tr>
<tr><td>Filing</td><td>The confirmed trigger for single and grouped sessions, the local internal target, applicable extension conditions, and the official reference</td></tr>
<tr><td>Exceptions</td><td>Status mapping, return and denial channels, notice-specific clocks, evidence of receipt, authorized reconsideration or appeal signer</td></tr>
<tr><td>Systems and audit</td><td>Certified eClaims 3.0 workflow, XML validation, authorized fallback, retention and access rules, audit export, incident routing</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>Utilization and dispositions.</strong> September 1 is #154 (ready, after the billing correction). September 3 consumes nothing. September 5 is #155, filed by the hospital with 90935 and N18.5; keep SIM-H05 as the reference. September 8 is #156, held for the unsigned agreement form. September 10 is over cap: funding follow-up, and the patient is still dialyzed.</p>
<p><strong>Billing and eClaims.</strong> The 400-peso kit is covered: correct it and review a refund; billing it after you identified it as covered is a critical error. Require the XML statement. Route the unsigned agreement form to its owner without backdating. SIM-A01 proves the September 1 claim was received: update the register, do not resend (a resend would be a duplicate, also critical), and refer any correction of the received claim to the authorized officer.</p>
<p><strong>The patient.</strong> Explain that the latest visit appears to be beyond the 156-session allocation, subject to confirmation of pending entries, that billing and social service will help with funding, and that you will call back tomorrow. Then check understanding.</p>
"""],
    "skills": {"title": "Capstone and workplace observations",
               "intro": "Complete Form A in 90 minutes with a supervisor, then three observed tasks at work.",
               "items": [
                   ("Assigns correct utilization numbers and dispositions to every session.", True),
                   ("Avoids resending a claim with an official acknowledgment.", True),
                   ("Corrects a covered item charged to the patient and routes refund review.", True),
                   ("Triages a return and a denial with verified clocks and owners.", False),
                   ("Reconciles a short remittance and classifies the variance.", False),
                   ("Explains coverage, offers funding help and a callback, and checks understanding.", False),
                   ("Declines an unauthorized channel for patient data and escalates any actual disclosure.", True),
                   ("Leaves a handoff with evidence references, owners, dates, and next actions.", False),
               ],
               "placement": "Three supervised observations at work: a correct intake, a full submission simulation, and an exception handoff, each recorded with date, observer, evidence reference, outcome, and any limits on delegated duties."},
    "quiz": [
        ("PRO-confirmed utilization is 153. What number is the next completed session?",
         ["#153", "#154", "#155", "#156"], 1,
         "Count from the confirmed total."),
        ("A scheduled session is cancelled. What does it consume?",
         ["One session", "Nothing", "Half a session", "Two sessions"], 1,
         "Only rendered sessions count."),
        ("Who files a confirmed emergency HD session delivered during a hospital confinement?",
         ["Your center", "The hospital that rendered it", "The patient", "PhilHealth"], 1,
         "Keep the hospital&rsquo;s claim reference."),
        ("An attested session has an unsigned agreement form. What is its disposition?",
         ["Release", "Counts toward utilization; claim held pending the agreement form", "Does not count", "Delete"], 1,
         "Route to the source owner without backdating."),
        ("The register says &ldquo;draft,&rdquo; but official acknowledgment SIM-A01 exists. What do you do?",
         ["Resend", "Update the register, do not resend, and refer any correction of the received claim to the authorized officer", "Delete the acknowledgment", "File a new claim"], 1,
         "A resend would be a duplicate."),
        ("Which of these is a critical error in the capstone?",
         ["Asking the PRO a question", "Billing a covered service to the patient after identifying it as covered", "Using a job aid", "Writing a hold note"], 1,
         "Critical errors are judged before the score."),
        ("A candidate scores 95 but releases a duplicate claim. Result?",
         ["Pass", "Does not pass", "Pass with a warning", "Retake only the privacy task"], 1,
         "The critical-error gate overrides points."),
        ("What is the pass standard?",
         ["70 of 100", "80 of 100 or more with zero critical errors", "90 of 100", "Any score with no critical errors"], 1,
         "Both conditions."),
        ("SIM-B01 allows two sessions. What is the split of 12,700 pesos?",
         ["12,000 facility and 700 professional", "12,350 and 350", "6,350 and 6,350", "11,000 and 1,700"], 0,
         "6,000 and 350 per session."),
        ("A return has a verified deadline of October 22. What earns full credit?",
         ["Ignoring it", "Routing it by October 22 and keeping the linked receipt", "Appealing it", "Refiling it as new"], 1,
         "Returns use the linked process."),
        ("A colleague suggests a personal chat account for a real patient file in training. Response?",
         ["Agree", "Use only fictional data, name an approved channel for real work, and escalate any actual disclosure", "Blur the name and send", "Ask the patient"], 1,
         "Unauthorized disclosure is a critical error."),
        ("Which three questions frame the debrief?",
         ["Who, what, why", "Which record shows the session occurred, which proves filing, and who owns the next action", "Cost, time, quality", "None"], 1,
         "Evidence, filing, ownership."),
        ("When is Form B used?",
         ["Never", "To reassess a candidate with different facts after a debrief", "For managers only", "As homework"], 1,
         "Same structure, new facts."),
        ("What must a claims lead complete before staff use the course for live work?",
         ["Nothing", "The facility adoption record, with the facility head", "A PhilHealth exam", "A vendor contract"], 1,
         "Local settings need written approval."),
        ("How many supervised workplace observations does sign-off require?",
         ["One", "Three: intake, submission simulation, and an exception handoff", "Ten", "None"], 1,
         "Recorded with date, observer, evidence, and outcome."),
    ],
    "terms": [("Capstone", "The 90-minute practical assessment of the whole track."),
              ("Critical error", "An error that fails the attempt regardless of score."),
              ("Disposition", "The release decision for a session: ready, hold, no consumption, or over cap."),
              ("Adoption record", "The facility&rsquo;s written local settings for claims work."),
              ("Form B", "The reassessment version of the capstone.")],
    "readings": [("hemodialysis-transfer-guide.html", "What patients and families need when they transfer to another dialysis unit.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
