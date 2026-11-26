# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 17: The Record, the Claim, and Learning From What Went Wrong. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse comparing a nursing record with a machine session log at her desk.",
    "objectives": [
        "Write a record that matches what happened, with times, actions, and who was told.",
        "Explain where the shift record meets the PhilHealth claim, and where it does not.",
        "Correct a record properly, and refuse to fabricate one.",
        "Respond to an incident: protect the patient, preserve evidence, report, and support staff.",
        "Turn one recurring problem into a measured improvement using a run chart.",
    ],
    "big": """
{{plain:A treatment record is a photograph of the session. If someone paints over the photograph to make it look better, it is no longer evidence of anything.}}
<p>The picture has a limit. A photograph is taken in an instant; a treatment record is built over a whole session, by several hands, often from memory at the end of a busy shift. Most false records are not deliberate forgeries but gaps filled in later with what should have happened. That is why the record is written as events happen, and late entries are labeled late.</p>
<p>The record has three readers. The next nurse acts on it. The law relies on it. The payer pays on it, for hemodialysis (HD) sessions and peritoneal dialysis (PD) packages alike. A record that says four hours when the patient had three hours and twenty minutes misleads all three, and the first reader, the next nurse, is the one who can hurt the patient with it.</p>
{{cards:Key terms for this module|Late entry::A record written after the event, labeled late, with the true event time.|Correction::A single line through the error, the correct entry, date, time, and signature.|Incident::An event that harmed or could have harmed a patient.|Run chart::A graph of a measure over time with a median line, used to see whether a change worked.|Median::The middle value when all values are sorted.}}
""",
    "case": {"title": "&ldquo;Just write four hours&rdquo;", "html": """
<p>At the end of the month, a staff nurse asks the charge nurse, Paolo, to &ldquo;fix&rdquo; six records where sessions were shortened, so the PhilHealth claims look complete. She says the claims officer told her short sessions cause problems.</p>
<p>PhilHealth covers up to 156 hemodialysis sessions a year for registered patients with chronic kidney disease stage 5, at 6,350 pesos per session since October 2024.[[hn_philhealth2024]][[cn_philhealth_news2025]]</p>
""", "questions": ["What is Paolo&rsquo;s answer?",
                  "What is the right way to correct a record?",
                  "What improvement project hides inside this request?"]},
    "sections": [
        ("good", "A good record", "A good record", """
<p>Write the times (start, end, events), what you saw, what you did, who you told, what they decided, and how the patient responded. Late entries are labeled late, with the true event time. Corrections are a single line through the error, the correct entry, the date, the time, and your signature. Electronic records keep an audit trail of every change; anyone can see what was changed and when.</p>
"""),
        ("claim", "The claim", "Where the record meets the claim", """
<p>The claim depends on the record, not the other way around. A shortened session is recorded as shortened. How payer rules apply to a short session is a question for the claims officer and the head nurse (the PhilHealth Claims and Head Nurse tracks cover it), not a reason to change what happened.</p>
{{fig:cn17_photo}}
<p>The money is large, which is why accuracy is scrutinized. In the first half of 2025, PhilHealth paid about 27 billion pesos for more than two million hemodialysis claims.[[cn_gma2025]]</p>
"""),
        ("never", "Never fabricate", "Never fabricate", """
<p>Writing four hours when three hours and twenty minutes were delivered is falsification. It harms the patient (the next nurse believes the dose was given), the nurse (her license), and the unit (its accreditation and its claims). The charge nurse says no, explains why, and tells the head nurse about the request so the pressure behind it can be addressed.</p>
{{call:A request to change a record so it no longer matches what happened: refuse, explain, and report the request to the head nurse.}}
"""),
        ("incident", "When something goes wrong", "When something goes wrong", """
<p>Protect the patient first. Tell the physician. Preserve the evidence: lines, dialyzer, labels, syringes, logs. Report through the unit&rsquo;s system. Support the staff involved; the nurse who made the error is often the second person hurt by it.</p>
<p>An investigation asks how the system allowed the error, not only who made it: workload, interruptions, look-alike packaging, unclear orders. The fixes that work best change the system (a separated shelf, a protected task) rather than asking people to try harder.</p>
"""),
        ("improve", "Improve one thing", "Improve one thing", """
<p>Pick one problem that keeps coming back: late starts, shortened sessions, missed glucose checks. Define one measure. Collect it every day or week on a simple run chart. Try one change and watch whether the line moves.[[hn_perla2011]]</p>
{{fig:cn17_runchart}}
<p>Read the run chart with a simple rule: six or more consecutive points on one side of the median suggest a real shift, not noise. One good week proves nothing; a run does.</p>
{{scene:The project that started with a refusal|<p>After Paolo refuses to change the six records, he asks why sessions are being shortened. He counts four weeks of sessions: 31 of 240 shortened, most for cramps on high-gain days, some for late transport, some for alarms. That count becomes his improvement project, below.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>Paolo&rsquo;s answer.</strong> No. The records stay as they are, because they describe what happened. He explains why to the staff nurse, documents the request, and tells the head nurse so that the pressure on short sessions can be dealt with honestly with the claims officer.</p>
<p><strong>Correcting a record.</strong> If a record contains a genuine error, draw a single line through it, write the correct entry, and add the date, time, and signature. Never erase, white out, or rewrite a page.</p>
<p><strong>The improvement project (Head Nurse toolkit #c10).</strong> Baseline over four weeks: 31 of 240 sessions shortened (12.9%), median 10 minutes each; 14 early stops for cramps, 9 late starts from transport, 8 machine alarms. The change tested: a pre-session fluid check and an attending review whenever the planned ultrafiltration rate would exceed the unit&rsquo;s threshold of 13 mL/kg/h, aimed at cramps. (In a secondary analysis of the HEMO trial, rates above 13 mL/kg/h were associated with higher all-cause and cardiovascular mortality; this is observational, and the threshold is set by the unit and the attending.)[[cn_flythe2011]] Next four weeks: 18 of 236 shortened (7.6%), with cramp-related stops down from 14 to 5. The four weekly points after the change all sit below the median of the eight weeks. That is encouraging but not yet six in a row, so he keeps plotting before calling it a real shift. Paolo reports it at the unit meeting and starts on transport next.</p>
"""],
    "skills": {"title": "The record and one improvement",
               "intro": "Audit five of your own records against the machine logs, correct one simulated error properly, and present a run chart.",
               "items": [
                   ("Writes an event entry with times, actions, who was told, and what was decided.", True),
                   ("Corrects a record with a single line, the correct entry, date, time, and signature.", True),
                   ("Refuses a request to falsify a record and reports it.", True),
                   ("Lists what evidence to preserve after an incident.", False),
                   ("Chooses one measure and plots it on a run chart with a median.", False),
                   ("Reads a run chart using the six-point rule.", False),
               ],
               "placement": "Run one improvement measure for at least eight weeks and present the run chart to the head nurse."},
    "quiz": [
        ("How many hemodialysis sessions a year does PhilHealth cover?",
         ["90", "120", "156", "Unlimited"], 2,
         "For registered patients with CKD stage 5."),
        ("What is the PhilHealth payment per session since October 2024?",
         ["2,600 pesos", "4,000 pesos", "6,350 pesos", "10,000 pesos"], 2,
         "Under PhilHealth Circular 2024-0023."),
        ("Writing four hours for a session of three hours twenty minutes is:",
         ["Rounding", "Falsification", "Accepted practice", "Helpful"], 1,
         "The record must match what happened."),
        ("How is a record corrected?",
         ["By erasing", "A single line, the correct entry, date, time, signature", "With correction fluid", "On a new page"], 1,
         "The original stays readable."),
        ("After an incident, what should be preserved?",
         ["Nothing", "Lines, dialyzer, labels, syringes, logs", "Only the chart", "The patient&rsquo;s phone"], 1,
         "The investigation needs them."),
        ("Which run chart pattern suggests a real change?",
         ["One high point", "Six or more consecutive points on one side of the median", "Any change", "The average"], 1,
         "A run, not a single good week."),
        ("What does an investigation mainly ask?",
         ["Who to blame", "How the system allowed it", "What it cost", "Who saw it"], 1,
         "System fixes work better than effort alone."),
        ("The claim depends on:",
         ["The claims officer", "The clinical record", "The patient", "The bank"], 1,
         "Not the other way around."),
        ("What is a late entry?",
         ["A forbidden entry", "A record written after the event, labeled late, with the true time", "A back-dated entry", "An entry by the head nurse"], 1,
         "Honest about when it was written."),
        ("In the case, 31 of 240 sessions were shortened. What percentage is that?",
         ["7.6%", "12.9%", "20%", "31%"], 1,
         "31 &divide; 240 = 12.9%."),
        ("Who should hear about a request to falsify records?",
         ["Nobody", "The head nurse", "The patients", "The newspaper"], 1,
         "So the pressure behind it can be addressed."),
        ("Who is often the second person hurt by an error?",
         ["The physician", "The nurse who made it", "The technician", "The cashier"], 1,
         "Support staff after an incident."),
        ("Which fix works best after a look-alike medicine error?",
         ["Telling everyone to be careful", "Separating the products on the shelf", "Disciplining the nurse", "Doing nothing"], 1,
         "Change the system."),
        ("Why does the record matter most to the next nurse?",
         ["It is required", "She acts on it, and a false record can hurt the patient", "It looks neat", "It is short"], 1,
         "The first reader is clinical."),
        ("PhilHealth paid about how much for hemodialysis claims in the first half of 2025?",
         ["2.7 million pesos", "27 billion pesos", "270 pesos", "2.7 trillion pesos"], 1,
         "More than two million claims."),
    ],
    "terms": [("Late entry", "A record written after the event, labeled late, with the true time."),
              ("Correction", "A single line through the error, the correct entry, date, time, and signature."),
              ("Incident", "An event that harmed or could have harmed a patient."),
              ("Run chart", "A graph of a measure over time with a median line."),
              ("Median", "The middle value when all values are sorted."),
              ("Chronic kidney disease (CKD)", "Long-term loss of kidney function; stage 5 is kidney failure.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality improvement in dialysis units."),
                 ("zero-balance-billing-philhealth.html", "PhilHealth and no-balance billing."),
                 ("philhealth-z-packages.html", "PhilHealth benefit packages explained.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c10", "calc-dialysis-head-nurse-toolkit.html#c9", "calc-dialysis-charge-nurse-toolkit.html#c4"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
