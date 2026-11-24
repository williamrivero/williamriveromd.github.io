# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 02: Intake, Eligibility, and the Dialysis Database."""

MODULE = {
    "image_alt": "A liaison in a hijab talks at eye level with an elderly man in a wheelchair and his adult son, who holds a travel bag.",
    "objectives": [
        "Explain in plain words why a missed dialysis session is dangerous, and why a claim hold must never delay treatment.",
        "Recognize six red flags at the intake desk that require an immediate handoff to nursing.",
        "Verify identity and the member or dependent relationship from approved evidence.",
        "Record eligibility and PhilHealth Dialysis Database (PDD) registration as two separate checks with their own dates and sources.",
        "Handle a transfer: confirm prior utilization through an authorized channel and mark every count as confirmed or pending.",
    ],
    "big": """
{{plain:The kidney is a 24-hour filter. Hemodialysis squeezes that work into about 12 hours a week, in three sessions. Between sessions the filter is switched off, so potassium, acid, phosphate, and every glass of water the patient drinks keep building up until the next treatment.}}
<p>The picture has a limit: the build-up is not even through the week. The longest gap, over the weekend, is when potassium and fluid peak, and that peak strains the heart&rsquo;s rhythm and the lungs.[[pc_flythe2012]] In more than 32,000 United States patients on thrice-weekly hemodialysis, deaths from all causes were more frequent on the day after the two-day gap than on other days (22.1 versus 18.0 per 100 patient-years).[[dch_foley2011]] Missed treatments are associated with more hospital stays and deaths in cohorts from the United States and twenty countries.[[pc_obialo2012]][[dch_alsalmi2018]] In a European cohort, missing the first session after the weekend carried about twice the mortality hazard of missing the second session of the week.[[pc_fotheringham2020]]</p>
<p>These are observational studies: patients who miss sessions differ in other ways, and that is not fully adjusted for. But the direction is consistent and the physiology explains it. For a claims desk, the lesson is simple. An eligibility or database problem holds the <em>claim</em>. It never holds the <em>treatment</em>.</p>
{{fig:pc_why}}
{{cards:Key terms for this module|PIN::PhilHealth Identification Number, the member&rsquo;s permanent number.|Member and dependent::The member pays or is covered in their own right; a qualified dependent is covered through a member.|Eligibility::Whether this person is covered by PhilHealth for this service on this date.|PDD::PhilHealth Dialysis Database, the registry of patients with chronic kidney disease stage 5 on dialysis.|PBEF::PhilHealth Benefit Eligibility Form, the printed eligibility result when your workflow uses it.|Utilization::How many covered sessions a patient has already used this calendar year.}}
""",
    "case": {"title": "A transfer from the province", "html": """
<p>Mr. Andres Villanueva (fictional, case token SIM-02), 74, arrives in a wheelchair with his son Rodel, carrying a travel bag. They moved from Iloilo last week to live with Rodel in Marilao. Mr. Villanueva has dialyzed three times a week for four years. He is a dependent on Rodel&rsquo;s PhilHealth membership.</p>
<p>The eligibility check shows him eligible. The PDD check is pending: the system returns a near match under a slightly different surname spelling. Rodel says, &ldquo;The clinic in Iloilo told us he has used about 142 sessions this year.&rdquo; While you talk, Mr. Villanueva rubs his chest and says he feels weak, and that his last session was four days ago because of the move.</p>
""", "questions": ["What is the first thing you do, before any form?",
                  "What do you record about eligibility, PDD, and the 142 sessions?",
                  "Can you treat the near-match PDD record as his?"]},
    "sections": [
        ("redflags", "Call the nurse", "Stop the paperwork, call the nurse", """
<p>Claims staff are often the first people a patient talks to. Some things a patient says or shows at the desk mean the paperwork stops and a nurse comes now. You are not diagnosing; you are recognizing that a clinician must see the patient before anything else.</p>
{{fig:pc_rednurse}}
<p>Weakness, palpitations, or chest discomfort in a dialysis patient can be signs of a high potassium level, which can stop the heart. Breathlessness and swelling after a missed session suggest fluid overload. Fever in a patient with a chest catheter can be a bloodstream infection. Each needs a nurse in minutes, not after the forms.</p>
{{call:If a patient at the desk has any of these signs, or tells you a session was missed or shortened, hand over to the nurse immediately and say exactly what you saw and heard. Eligibility and database checks continue afterward, in parallel.}}
"""),
        ("identity", "Identity and eligibility", "Who is this patient, and are they covered?", """
<p>Every claim starts with the right person. Confirm the patient&rsquo;s identity and, for a dependent, the relationship to the member, from the evidence your facility has approved. Obtain the eligibility result through the approved facility workflow and keep the result with its date and source.</p>
<p>Under PhilHealth&rsquo;s immediate eligibility policy, staff should route registration or verification problems through the authorized process rather than automatically demanding proof of a minimum contribution history.[[pc_pc2022_0013]] Package-specific requirements still apply. The PBEF, where used, is an eligibility artifact. It answers a different question from the PDD.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Question it answers</th><th>Record</th></tr></thead>
<tbody>
<tr><td>Identity</td><td>Is this the person in the record?</td><td>Approved evidence seen, by whom, when</td></tr>
<tr><td>Member or dependent</td><td>Through whom is the patient covered?</td><td>Relationship and its evidence</td></tr>
<tr><td>Eligibility</td><td>Is this person covered on this date?</td><td>Result, date, source</td></tr>
<tr><td>PDD registration</td><td>Is this person registered as chronic kidney disease stage 5 on dialysis?</td><td>Status, date, source (separate field)</td></tr>
<tr><td>Prior utilization</td><td>How many sessions are used this year?</td><td>Confirmed count and its source; pending count separately</td></tr>
</tbody></table></div>
"""),
        ("pdd", "The dialysis database", "Two questions, two records", """
<p>Confirmed eligibility does not establish PDD registration. The hemodialysis benefit requires clinician-documented chronic kidney disease stage 5, registration in the PDD, a participating facility, and sessions remaining.[[pc_pc2024_0023]][[pc_pa2016_0030]] Use the current PDD forms and the authorized registration or update route from PhilHealth&rsquo;s downloads page. The facility may not charge the patient for PDD registration.</p>
{{fig:pc_twolocks}}
<p>A close match is not a match. A surname spelled differently, a different birth date, or a missing middle name can belong to another person. Hold the claim, validate identity with approved evidence, keep the original inquiry result, and use the authorized correction channel. Never merge records because they look alike.</p>
{{key:Two questions, two records, two fields. A claim is released only when both are verified. Treatment never waits for either.}}
"""),
        ("transfer", "Transfers", "When a patient arrives from another unit", """
<p>Transferring patients bring the most uncertainty. Sessions they used elsewhere count against the same 156-session calendar-year allocation, and a verbal count is only a starting point.[[pc_pc2023_0009]]</p>
{{flow:Transfer intake|1. Clinical first::Notify nursing of the last session date and any symptoms.|2. Identity and eligibility::Verify and record with date and source.|3. PDD::Verify registration through the authorized channel; record it separately.|4. Utilization::Request official confirmation of prior sessions; mark the verbal count as unverified.|5. Hold and follow up::Hold claim clearance, assign an owner, and set a follow-up date.}}
<p>A short, specific message works best when you ask your PRO to confirm utilization: the minimum identifiers through an authorized channel, the dates in question, and one clear question. Calculator 2 in the claims toolkit keeps confirmed and pending counts apart so a projected total never looks like a verified one.</p>
"""),
    ],
    "debrief": ["""
<p><strong>First, the nurse.</strong> Mr. Villanueva has chest discomfort and weakness four days after his last session. That is a red flag. Hand over to the nurse immediately and tell them exactly what he said and when he last dialyzed. Every form waits.</p>
<p><strong>What you record.</strong> Dependent eligibility, with its date and source. PDD status as pending, in its own field. The 142 sessions as unverified, reported by the son and attributed to the Iloilo clinic. Request official confirmation of utilization through the designated liaison, hold claim clearance, and set an owner and a follow-up date.</p>
<p><strong>The near match.</strong> No. A similar record cannot establish that it belongs to him. Validate identity with approved evidence, keep the original inquiry result, and use the authorized correction channel.</p>
"""],
    "skills": {"title": "Intake record for a transferring patient",
               "intro": "Using a fictional transfer packet, complete the intake record and hand over one planted red flag to a supervisor playing the nurse.",
               "items": [
                   ("Recognizes a red flag and hands over to nursing before any paperwork.", True),
                   ("Verifies identity and the member or dependent relationship from approved evidence.", False),
                   ("Records eligibility and PDD status as separate fields, each with date and source.", True),
                   ("Refuses to treat a near-match record as the patient&rsquo;s.", True),
                   ("Marks transferred utilization as confirmed or pending and requests official confirmation.", False),
                   ("Holds claim clearance with an owner and a follow-up date.", False),
               ],
               "placement": "Complete three intake records at your unit with your claims lead, using approved evidence only."},
    "quiz": [
        ("Does confirmed eligibility establish PDD enrollment?",
         ["Yes", "No; PDD registration needs its own verification", "Only for dependents", "Only after 90 days"], 1,
         "Two questions, two records."),
        ("A patient needs urgent assessment while PDD is pending. What do you do?",
         ["Finish the PDD check first", "Notify the clinical team immediately and continue verification in parallel", "Send the patient home", "Ask PhilHealth to approve"], 1,
         "Treatment never waits for paperwork."),
        ("Can the facility charge a patient for PDD registration?",
         ["Yes, a small fee", "No", "Only for transfers", "Only if the patient agrees"], 1,
         "The benefit rules do not allow a registration charge."),
        ("A relative reports &ldquo;about 150 sessions so far.&rdquo; How do you record it?",
         ["As confirmed", "As pending and unverified until confirmed through an authorized channel", "Ignore it", "As 156"], 1,
         "Verbal counts are starting points."),
        ("Which sign at the desk is a reason to call the nurse now?",
         ["A misspelled name", "Breathlessness after a missed session", "An expired ID", "A long queue"], 1,
         "Fluid overload can be dangerous within hours."),
        ("Why can weakness or palpitations in a dialysis patient be urgent?",
         ["They mean the patient is tired", "They can be signs of high potassium, which can stop the heart", "They are always anxiety", "They mean low blood sugar"], 1,
         "Potassium builds up between sessions."),
        ("In a large US cohort, when were deaths more frequent among thrice-weekly hemodialysis patients?",
         ["On Fridays", "On the day after the two-day gap", "Evenly through the week", "After holidays only"], 1,
         "Foley and colleagues, 2011."),
        ("What kind of evidence links missed sessions to hospital stays and deaths?",
         ["Randomized trials", "Observational cohort studies", "Laboratory studies only", "None"], 1,
         "So the wording is &ldquo;associated with.&rdquo;"),
        ("The PDD search returns a record with a slightly different surname. What do you do?",
         ["Use it", "Hold, validate identity with approved evidence, and use the authorized correction channel", "Create a duplicate", "Change the patient&rsquo;s surname"], 1,
         "A close match is not a match."),
        ("Under immediate eligibility, what should staff avoid doing automatically?",
         ["Checking identity", "Demanding proof of a minimum contribution history", "Recording dates", "Calling the PRO"], 1,
         "Route issues through the authorized process."),
        ("Do sessions used at another unit count toward the patient&rsquo;s annual allocation?",
         ["No", "Yes, they count toward the same calendar-year allocation", "Only half count", "Only if in the same region"], 1,
         "Ask about other units at every transfer."),
        ("What should a message to the PRO about utilization contain?",
         ["The full chart", "Minimum identifiers, the dates, one clear question, and an authorized channel", "A complaint", "Nothing in writing"], 1,
         "Minimum necessary data, one question."),
        ("Which record answers &ldquo;Is this person covered on this date?&rdquo;",
         ["PDD", "Eligibility result", "Treatment sheet", "Remittance"], 1,
         "PDD answers a different question."),
        ("What must the hemodialysis benefit have, besides eligibility?",
         ["A transplant referral", "Documented chronic kidney disease stage 5, PDD registration, a participating facility, and sessions remaining", "A second opinion", "A cash deposit"], 1,
         "All four apply."),
        ("A patient says his last session was four days ago. What is your first step?",
         ["Finish intake", "Tell the nurse now, with exactly what he said", "Book next week", "Call PhilHealth"], 1,
         "A long gap raises potassium and fluid risk."),
    ],
    "terms": [("PIN", "PhilHealth Identification Number."),
              ("Eligibility", "Whether a person is covered by PhilHealth for a service on a date."),
              ("PDD", "PhilHealth Dialysis Database."),
              ("PBEF", "PhilHealth Benefit Eligibility Form."),
              ("Utilization", "Covered sessions already used this calendar year."),
              ("Red flag", "A sign or symptom at the desk that requires a nurse now.")],
    "readings": [("hemodialysis-transfer-guide.html", "What patients and families need when they transfer to another dialysis unit.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
