# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 10: From the Chart to the PhilHealth Claim. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse and a billing officer comparing a nursing record with a machine log at a desk.",
    "objectives": [
        "Explain why a session note is a clinical record first and a billing record second.",
        "State the current PhilHealth rules for maintenance hemodialysis: who is covered, how many sessions, and at what rate.",
        "Separate accreditation, coverage, and quality assurance, and name the evidence each needs.",
        "Trace one claim back through every record that supports it.",
        "Project when a patient will use up the year&rsquo;s sessions, and plan before it happens.",
        "Correct a record by amendment, never by erasing.",
    ],
    "big": """
{{plain:A claim is a promise that a session happened, to a named patient, on a stated date, as described. The chart is the evidence for that promise. Picture the claim at the top of a ladder whose rungs are the order, the machine log, the nursing note, the medicine record, and the signed agreement form.}}
<p>If any rung is missing, the claim is standing on air, however tidy the paperwork above it looks. The picture has a limit: a ladder fails from the bottom, but a claim fails wherever a reviewer looks first.</p>
{{fig:hn10_ladder}}
{{cards:Key terms for this module|PhilHealth Dialysis Database (PDD)::The registry a patient with CKD stage 5 must be enrolled in to claim the hemodialysis benefit.|Package rate::The fixed amount PhilHealth pays per session, covering facility and professional fees and the listed services.|Balance billing::Charging the patient for a covered service above the package rate.|Accreditation::PhilHealth&rsquo;s recognition that a facility may claim at all.|Amendment::A correction that keeps the original visible and records who changed it and when.|Claims tracer::Following one claim back through every supporting record.}}
""",
    "case": {"title": "Monday that did not happen", "html": """
<p>On Thursday, the billing officer, Ms. Rowena Garcia, brings you a claim prepared for Mr. Felix Bautista, 63, for Monday&rsquo;s session. The signed nursing summary for Monday reads &ldquo;Session completed, 4 hours, UF 2.5 L, tolerated well.&rdquo;</p>
<p>The machine log for station 11 shows no treatment on Monday morning. The charge nurse that day, Ms. Lea Vergara, remembers that Mr. Bautista was sent to the hospital emergency room with chest pain before he was connected.</p>
""", "questions": ["What happens to the claim, and what happens to the records?",
                  "What clinical problem is hiding inside this billing problem?",
                  "How did a completed note appear for a session that never happened, and how will you stop it?"]},
    "sections": [
        ("clinical", "Clinical first", "Documentation is a clinical act first", """
<p>The session note is how the next nurse, the physician, and the patient&rsquo;s next unit find out what happened. A copied note does two kinds of harm at once. It invents a session that a reviewer will pay for, and it hides a missed session from the team caring for the patient. Module 2 showed that missed sessions carry a mortality signal.[[hn_foley2011]][[hn_alsalmi2018]] The billing error and the clinical error are the same error.</p>
<p><strong>What a session note must carry:</strong> the current order version, consent, the pre-treatment assessment, the access, actual start and end times, fluid removed, any interruption and its reason, medicines given, the response, teaching, the condition at discharge, and the handoff.</p>
<p>Write it during or right after the session. A late entry is allowed when it is labeled as late, with the real time and the real author. Never back-date.</p>
"""),
        ("rules", "The rules", "What PhilHealth covers, as verified on November 23, 2026", """
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>Current position</th></tr></thead>
<tbody>
<tr><td>Who is covered</td><td>Members and dependents with CKD stage 5 registered in the PhilHealth Dialysis Database[[hn_philhealth2024]]</td></tr>
<tr><td>Sessions per year</td><td>Up to 156 per calendar year, three a week for 52 weeks. Raised from 90 effective June 22, 2023. Unused sessions do not carry over to the next year[[hn_philhealth2023]]</td></tr>
<tr><td>Rate</td><td>PHP 6,350 per session, effective October 9, 2024, up from PHP 2,600 and then PHP 4,000 earlier in 2024. Up to PHP 990,600 a year[[hn_philhealth_form]]</td></tr>
<tr><td>What the rate covers</td><td>Facility and professional fees and the services and supplies listed in Table 2 of Circular 2024-0023. No balance billing or co-payment for those covered services[[hn_philhealth2024]]</td></tr>
<tr><td>Services on demand?</td><td>No. Services are given when clinically indicated for that session, not at the patient&rsquo;s request</td></tr>
<tr><td>Agreement form</td><td>Records the session number and date, and the patient&rsquo;s acknowledgment of the rules[[hn_philhealth_form]]</td></tr>
<tr><td>Quality</td><td>Circular 2024-0029 sets the quality expectations for maintenance hemodialysis[[hn_philhealth2024q]]</td></tr>
</tbody></table></div>
<p>Three different questions sit inside these rules. <strong>Accreditation</strong> asks whether the facility may claim at all. <strong>Coverage</strong> asks whether this patient and this session qualify. <strong>Quality assurance</strong> asks whether care met the standard. A unit can pass one and fail another.</p>
<p>Rules change. Billing and compliance confirm current forms and exceptions. Check the PhilHealth circulars page before every annual review.</p>
"""),
        ("tracer", "Claims tracer", "Tracing a claim, rung by rung", """
<p>Each month, pick five claims at random. Follow each one, using the patient, the date, and the session number, down every rung.</p>
{{flow:Five rungs|Agreement form::Signed, with the right session number and date.|Order::Current on the date of the session.|Machine log::A treatment on that station, at that time, for about that length.|Nursing note::Assessment, times, fluid removed, condition at discharge.|Medicine record::Every medicine claimed was ordered and given.}}
{{formula:<strong>Tracer completeness</strong> = rungs verified &divide; rungs checked.<br>5 claims &times; 5 rungs = 25. If 23 are verified, completeness is 92%. Report the two failures by rung, not by patient.}}
<p>Route every missing or disagreeing rung to billing or compliance, with an owner. Use synthetic identifiers in any training material.</p>
{{call:Stop the claim and call billing, compliance, and the clinical head when a prepared claim does not match the clinical record. Never submit a claim that the records do not support. Follow your unit&rsquo;s protocol while you reconcile.}}
"""),
        ("ledger", "Session ledger", "Know who will run out before December", """
<p>A patient who dialyzes three times a week all year, plus any extra sessions, can use up 156 before December. Know who is at risk by the third quarter, so the nephrologist, the social worker, and the patient can plan.</p>
{{formula:<strong>Arithmetic illustration.</strong> 140 sessions used by November 1, at three a week.<br>156 &minus; 140 = 16 left. 16 &divide; 3 = about 5.3 weeks.<br>The allocation runs out around December 8, more than three weeks before the year ends. Remaining value: 16 &times; PHP 6,350 = PHP 101,600.}}
{{fig:hn10_ledger}}
<p>The calculator does this for each patient. Bring the list to the monthly review in September, October, and November.</p>
"""),
        ("amend", "Correct, never erase", "Correcting a record", """
{{fig:hn10_amend}}
<p>Correct an error by an authenticated addendum that shows the original, the correction, who made it, and when. Deleting or overwriting is what turns an error into misconduct.</p>
<p>Ask why the error was possible. Copy functions, templates that pre-fill &ldquo;session completed,&rdquo; and notes written before the session ends are common sources. Each is a system problem that Module 11 can fix.</p>
{{key:An error corrected openly is a record of honesty. An error erased is a record of something else.}}
"""),
    ],
    "debrief": ["""
<p><strong>The claim and the records.</strong> Hold the claim. Preserve every record exactly as it is: the nursing summary, the machine log, the roster, any transfer note. Ask Ms. Vergara and the nurse who signed the summary for written accounts. Correct the nursing record by authenticated amendment, keeping the original visible, and document what actually happened: transfer before connection. Billing and compliance withdraw or correct the claim through their process.</p>
<p><strong>The hidden clinical problem.</strong> Mr. Bautista missed a session and went to the emergency room with chest pain. Who knows what happened to him? Was he admitted? Did he dialyze in the hospital, or did he go home undialyzed until Wednesday? Call the physician on duty and the attending nephrologist today, and make sure someone has spoken to him or his family.</p>
<p><strong>How it happened.</strong> Find out whether the summary came from a template or a copy function that pre-fills a completed session, or whether a note was written in advance. Either way, the system allowed a completed-session note without a delivered treatment. Fix the system, so the record cannot say &ldquo;completed&rdquo; until the times and fluid removed are entered. Then run the tracer on the same shift for the past month.</p>
"""],
    "skills": {"title": "Claims tracer",
               "intro": "Trace three synthetic claims against their records while your facilitator observes.",
               "items": [
                   ("Matches patient identity, date, and session number on every rung.", True),
                   ("Confirms the order was current on the date of the session.", False),
                   ("Compares the machine log with the nursing note for time and fluid removed.", True),
                   ("Identifies any covered item claimed without a supporting record.", False),
                   ("Holds a claim that the records do not support.", True),
                   ("Corrects a record by amendment, keeping the original visible.", True),
                   ("Identifies the clinical follow-up needed for a session that did not happen.", True),
                   ("Reports completeness by rung, without patient identifiers.", False),
                   ("Projects the year&rsquo;s session use for one patient.", False),
               ],
               "placement": "Run the five-claim tracer each month for three months. Present the completeness, the failing rungs, and one system fix to your facilitator."},
    "quiz": [
        ("How many hemodialysis sessions does PhilHealth cover per calendar year?",
         ["90", "104", "156", "Unlimited"], 2,
         "Three a week for 52 weeks."),
        ("What is the current rate per session?",
         ["PHP 2,600", "PHP 4,000", "PHP 6,350", "PHP 9,000"], 2,
         "Effective October 9, 2024."),
        ("Can unused sessions be carried to the next year?",
         ["Yes, all of them", "Yes, up to 10", "No", "Only with a doctor&rsquo;s letter"], 2,
         "The allocation is per calendar year."),
        ("Where is the list of covered services?",
         ["The agreement form", "Table 2 of Circular 2024-0023, checked against any newer changes", "The unit&rsquo;s price list", "The DOH licensing order"], 1,
         "No balance billing or co-payment for those services."),
        ("A prepared claim conflicts with the machine log. What do you do?",
         ["Submit and fix next month", "Hold and reconcile through clinical, billing, and compliance channels", "Delete the machine log", "Copy a note from another day"], 1,
         "A claim must rest on verified evidence."),
        ("How should an error in a signed note be corrected?",
         ["Overwrite it", "Delete and re-enter", "An authenticated addendum showing the original, the correction, author, and time", "Ask a colleague to sign a new note"], 2,
         "Correct, never erase."),
        ("Why is a copied note a clinical hazard?",
         ["It wastes paper", "It hides a missed session from the team", "It is too long", "It uses the wrong format"], 1,
         "The billing error and the clinical error are the same error."),
        ("What does accreditation answer?",
         ["Whether this patient is covered", "Whether the facility may claim at all", "Whether care met the standard", "Whether the nurse is licensed"], 1,
         "Coverage and quality are separate questions."),
        ("A patient has used 140 sessions by November 1 and dialyzes three times a week. When will the allocation run out?",
         ["It will last the year", "Around December 8", "In mid-November", "On December 31"], 1,
         "16 sessions remain, about five weeks."),
        ("Five claims with five rungs each are traced, and 23 rungs are verified. What is the completeness?",
         ["23%", "46%", "92%", "100%"], 2,
         "23 &divide; 25."),
        ("Are PhilHealth hemodialysis services given on the patient&rsquo;s request?",
         ["Yes, any service listed", "No, when clinically indicated for that session", "Only on weekends", "Only if paid separately"], 1,
         "Clinical indication governs each service."),
        ("When is a late entry acceptable?",
         ["Never", "When labeled as late, with the real time and author", "Only on the same day", "When the original author is absent"], 1,
         "Never back-date."),
        ("What should training materials for the claims tracer contain?",
         ["Real patient names", "Synthetic identifiers only", "Photocopies of real charts", "PhilHealth numbers"], 1,
         "Patient privacy applies to training too."),
        ("What must a patient have before the hemodialysis benefit can be claimed?",
         ["A referral letter", "Registration in the PhilHealth Dialysis Database", "A fistula", "Three months on dialysis"], 1,
         "Registration is a condition of coverage."),
        ("A template pre-fills &ldquo;session completed.&rdquo; What kind of problem is this?",
         ["A nurse&rsquo;s attitude problem", "A system problem that allows false records", "A billing preference", "Not a problem"], 1,
         "Fix the system so the record cannot say completed without times and fluid entered."),
    ],
    "terms": [("PhilHealth Dialysis Database", "The registry a patient with CKD stage 5 must be enrolled in to claim the hemodialysis benefit."),
              ("Package rate", "The fixed amount paid per session."),
              ("Balance billing", "Charging the patient for a covered service above the package rate."),
              ("Accreditation", "Recognition that a facility may claim."),
              ("Amendment", "A correction that keeps the original visible."),
              ("Late entry", "A record written after the event, labeled with the real time and author."),
              ("Claims tracer", "Following one claim back through every supporting record."),
              ("Back-dating", "Writing a false date on a record. Never acceptable.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How records feed quality review."),
                 ("starting-dialysis-new-beginning.html", "What patients are told about coverage and starting dialysis."),
                 ("hemodialysis-complications.html", "What a session note must capture when something goes wrong.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c9"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
