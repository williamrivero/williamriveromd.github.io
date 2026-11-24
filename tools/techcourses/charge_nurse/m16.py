# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 16: Patients, Families, and Transitions Beyond the Chair. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse holding a picture card while a patient explains it back to him, her son beside her.",
    "objectives": [
        "Teach for action using teach-back.",
        "Ask about treatment burden and the reasons behind missed or shortened sessions.",
        "Make sure a complete summary travels with every admission, transfer, and travel session.",
        "Recognize same-day red flags in patients on peritoneal dialysis or with a kidney transplant.",
        "Respond to a goals-of-care request by listening, recording, and arranging the conversation with the attending.",
    ],
    "big": """
{{plain:Handing a patient a diet sheet is like handing someone a map in a language they do not read. Teach-back is asking them to point to where they are going.}}
<p>Teaching is not finished until the patient can say or show what to do, in their own words. Teach-back finds the gap between what we said and what they understood, and it puts the burden of clarity on the teacher, not the learner.</p>
{{cards:Key terms for this module|Teach-back::Asking the patient to explain or show what they will do, to check your teaching.|Health literacy::The ability to find, understand, and use health information.|Treatment burden::The work dialysis asks of a patient and family: travel, time, cost, diet, medicines.|Transfer summary::The written information that travels with a patient to another unit or hospital.|Peritoneal dialysis (PD)::Dialysis using the lining of the abdomen, done at home.|Goals of care::What matters most to a patient, used to guide treatment choices.}}
""",
    "case": {"title": "The fistula that came back clotted", "html": """
<p>Mrs. Lourdes Ocampo, 60, was admitted to a medical ward for pneumonia. The dialysis unit&rsquo;s summary never reached the ward. The ward nurse did not know which arm held her fistula, and a blood pressure cuff was put on it overnight.</p>
<p>Mrs. Ocampo returned to the dialysis unit five days later with a fistula that had clotted, and a temporary catheter in her neck.</p>
""", "questions": ["What should travel with a patient on admission?",
                  "Who makes sure it goes?",
                  "How do you teach her family to protect the arm?"]},
    "sections": [
        ("teachback", "Teach-back", "Teach-back", """
<p>A systematic review of teach-back in chronic kidney disease found it associated with better knowledge and self-management.[[hn_jagodage2024]] Ask in a way that puts the burden on you: &ldquo;So I know I explained it clearly, can you tell me what you will do if your fistula bleeds at home?&rdquo; If the answer is wrong or partial, teach again, differently, and ask again.</p>
{{fig:cn16_teachback}}
<p>Health literacy varies widely, and it matters. In a United States dialysis cohort, limited health literacy was associated with higher mortality.[[hn_cavanaugh2010]] A patient who nods and says &ldquo;yes&rdquo; to everything may be being polite, not understanding.</p>
"""),
        ("burden", "Treatment burden", "Treatment burden and missed sessions", """
<p>Missed and shortened sessions are associated with higher mortality.[[hn_alsalmi2018]] Their reasons are usually practical: transport, cost, work, symptoms after dialysis, depression, family duties. A charge nurse who asks &ldquo;What makes it hard to come?&rdquo; finds problems a lecture on adherence never will, and many of them have fixable answers: a different slot, a different ride, a referral to the social worker.</p>
"""),
        ("transitions", "Transitions", "Admissions, transfers, and travel", """
<p>Every admission, transfer, or travel session needs a summary that travels with the patient: the prescription, dry weight, access type and the arm rules, last laboratory results, hepatitis status with dates, current medicines, allergies, and the unit&rsquo;s phone number. The charge nurse makes sure it goes, and calls when the patient returns, to reconcile medicines (Module 9) and to check the access.</p>
{{fig:cn16_transition}}
{{scene:The phone call to the ward|<p>When Mr. Peter Uy is admitted from the unit with a fever, the charge nurse sends the summary with him and also calls the ward: &ldquo;He has a right forearm fistula. No blood pressure cuff, IV, or blood draw on the right arm. His dry weight is 58. Please call us before any dialysis decision.&rdquo; The ward nurse writes &ldquo;NO BP/IV RIGHT ARM&rdquo; on the whiteboard above his bed. A five-minute call saves an access.</p>}}
"""),
        ("other", "Other modalities", "Patients on other kinds of kidney replacement", """
<p>Hemodialysis nurses also meet patients on peritoneal dialysis and kidney transplant recipients, at the unit or on the phone. Some findings need the specialist team the same day.</p>
{{fig:cn16_redflags}}
<ul>
<li><strong>Peritoneal dialysis:</strong> cloudy drained fluid or abdominal pain may be peritonitis. Call the PD team the same day. The International Society for Peritoneal Dialysis (ISPD) 2022 update recommends that a program&rsquo;s overall peritonitis rate be no more than 0.40 episodes per patient-year at risk; every episode counts.[[cn_li2022]]</li>
<li><strong>Kidney transplant:</strong> fever, less urine, or missed anti-rejection medicines need the transplant team today.</li>
</ul>
"""),
        ("goals", "Goals of care", "When a patient talks about stopping", """
<p>Some patients want to talk about stopping dialysis or about conservative care without dialysis. The charge nurse listens, writes down what the patient said in their own words, and arranges a conversation with the attending nephrologist and the family. She does not decide, dismiss, or argue. A patient who raises it is asking to be heard.</p>
{{key:Listen, record the patient&rsquo;s words, and arrange the conversation. The decision belongs to the patient and the attending, together.}}
"""),
    ],
    "debrief": ["""
<p><strong>What should travel.</strong> A summary with the access arm and its rules (no blood pressure cuff, intravenous line, or blood draw on that arm), the prescription, dry weight, hepatitis status with dates, current medicines, allergies, recent laboratory results, and the unit&rsquo;s phone number.</p>
<p><strong>Who makes sure it goes.</strong> The charge nurse on the shift when the patient is admitted. She sends the summary and calls the ward. When the patient returns, she reconciles medicines and checks the access.</p>
<p><strong>Teaching the family.</strong> Using teach-back with her son: &ldquo;If anyone reaches for her left arm with a cuff or a needle, what will you say?&rdquo; &ldquo;Not this arm. Use the other one.&rdquo; Mrs. Ocampo also gets a wristband or card that says the same. The charge nurse records the clotted fistula as an incident with the system fix: every admission triggers a summary and a call.</p>
"""],
    "skills": {"title": "Patients, families, and transitions",
               "intro": "Teach one patient and one family member using teach-back, prepare a transfer summary, and role-play a goals-of-care request.",
               "items": [
                   ("Uses teach-back and re-teaches when the answer is incomplete.", True),
                   ("Asks what makes it hard to come, and acts on one practical answer.", False),
                   ("Prepares a complete transfer summary including the access arm rules.", True),
                   ("Calls the receiving ward or unit and confirms the arm rule.", False),
                   ("Recognizes peritoneal dialysis and transplant red flags and calls the right team.", True),
                   ("Records a goals-of-care request in the patient&rsquo;s words and arranges the conversation.", True),
               ],
               "placement": "For one month, check that every admission from your shifts had a summary sent and a call made."},
    "quiz": [
        ("What does teach-back mean?",
         ["Repeating instructions louder", "The patient explains or shows in their own words", "A written quiz", "Giving a leaflet"], 1,
         "It checks the teaching, not the patient."),
        ("Missed and shortened treatments are associated with:",
         ["Better survival", "Higher mortality", "No change", "Lower costs"], 1,
         "Ask about the reasons."),
        ("What overall peritonitis rate does the ISPD 2022 update recommend at most?",
         ["0.10", "0.40", "1.0", "2.0 episodes per patient-year"], 1,
         "Every episode counts."),
        ("Cloudy peritoneal dialysis fluid. What do you do?",
         ["Nothing", "Call the PD team the same day", "Wait for next month", "Ignore it"], 1,
         "Possible peritonitis."),
        ("What must a transfer summary include?",
         ["The bill", "Access arm rules, prescription, hepatitis status, medicines", "The staff schedule", "Nothing"], 1,
         "And the unit&rsquo;s phone number."),
        ("A patient raises stopping dialysis. What do you do?",
         ["Dismiss it", "Listen, record her words, and arrange a talk with the attending and family", "Decide", "Change the subject"], 1,
         "She is asking to be heard."),
        ("Limited health literacy in a dialysis cohort was associated with:",
         ["Lower mortality", "Higher mortality", "No effect", "Better attendance"], 1,
         "Plain language and teach-back matter."),
        ("A transplant recipient has missed anti-rejection medicines. What do you do?",
         ["Wait for the next visit", "Contact the transplant team today", "Ignore it", "Double the next dose"], 1,
         "Same-day red flag."),
        ("A patient says &ldquo;yes&rdquo; to everything. What should you suspect?",
         ["Full understanding", "Possibly politeness, not understanding", "Rudeness", "Nothing"], 1,
         "Ask her to show or say it."),
        ("Who sends the summary when a patient is admitted from the unit?",
         ["Nobody", "The charge nurse on that shift", "The patient", "The ward"], 1,
         "And she calls the ward."),
        ("What question uncovers treatment burden?",
         ["Why don&rsquo;t you follow instructions?", "What makes it hard to come?", "Do you want to die?", "Who is your doctor?"], 1,
         "Practical problems have practical fixes."),
        ("When a patient returns from the hospital, the charge nurse should:",
         ["Do nothing", "Reconcile medicines and check the access", "Only weigh her", "Send her home"], 1,
         "Transitions run both ways."),
        ("What teach-back phrasing puts the burden on the teacher?",
         ["&ldquo;Do you understand?&rdquo;", "&ldquo;So I know I explained it clearly, can you tell me what you will do?&rdquo;", "&ldquo;Repeat after me.&rdquo;", "&ldquo;Any questions?&rdquo;"], 1,
         "It is a check of the teaching."),
        ("A patient travels to another province. What goes ahead of her?",
         ["Nothing", "A transfer summary with hepatitis results and the prescription", "Only her name", "Her bill"], 1,
         "The receiving unit needs it before the first session."),
        ("Who decides about stopping dialysis?",
         ["The charge nurse", "The patient and the attending, together", "The family alone", "PhilHealth"], 1,
         "The charge nurse listens and arranges."),
    ],
    "terms": [("Teach-back", "The patient explains or shows what they will do."),
              ("Health literacy", "The ability to find, understand, and use health information."),
              ("Treatment burden", "The work dialysis asks of a patient and family."),
              ("Transfer summary", "Information that travels with a patient."),
              ("Peritoneal dialysis (PD)", "Dialysis using the lining of the abdomen, done at home."),
              ("International Society for Peritoneal Dialysis (ISPD)", "The international society that publishes peritoneal dialysis guidelines."),
              ("Goals of care", "What matters most to a patient, used to guide treatment choices.")],
    "readings": [("hemodialysis-transfer-guide.html", "What should travel with a patient between units."),
                 ("peritoneal-dialysis-ckd.html", "Peritoneal dialysis explained."),
                 ("kidney-transplant.html", "Kidney transplantation explained."),
                 ("advance-care-planning-dialysis.html", "Advance care planning for people on dialysis.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c6"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
