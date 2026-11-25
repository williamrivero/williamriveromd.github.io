# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 04: Recipient Workup and Multidisciplinary Decisions. Written for this series from published sources."""

MODULE = {
    "image_alt": "A transplant team case conference around a table, with a coordinator presenting a one-page summary on a screen.",
    "objectives": [
        "Organize a recipient workup by the clinical questions it must answer, each with an owner.",
        "Track the validity window of each result and flag expiry before a decision meeting.",
        "Prepare a one-page case-conference summary built around the decision requested.",
        "Explain a team decision, including a deferral, in plain and truthful language.",
        "Explain why adherence and psychosocial assessment are part of the medical workup.",
    ],
    "big": """
{{plain:A recipient workup is like a building inspection before a big renovation. The inspector does not just collect papers. Each check answers a question: Will the foundation hold the load? Is there hidden water damage? Is the wiring safe? Will someone live here and maintain it? A stack of papers is not an inspection; an answered question is.}}
{{fig:rtc04_questions}}
<p>The picture has a limit. A building does not change while you inspect it. A person on dialysis does: a heart test from last year may no longer describe today&rsquo;s heart, an infection can appear after a clean screen, and a person&rsquo;s home support can change in a week. So a workup is not a checklist you finish once. It is a set of questions, each answered by its owner on results that are still current on the day of the decision.</p>
<p>KDIGO&rsquo;s 2020 candidate guideline organizes the evaluation by domain: age and frailty, psychosocial assessment, adherence, cardiac and vascular disease, infection, cancer, and other organ systems, among others.[[rtc_kdigo2020]] Your job is not to interpret any of these. Your job is to make sure each question has an owner, each result is current, and the team meets with everything it needs to decide.</p>
{{cards:Key terms for this module|Workup::The set of tests and reviews that answer whether transplant is safe and appropriate for this person.|Multidisciplinary team (MDT)::The group that decides candidacy: transplant nephrology, surgery, and others such as cardiology, infectious diseases, psychiatry, social work, and nutrition.|Validity window::How long a result counts as current under the program&rsquo;s protocol.|Deferral::A decision that transplant is not possible now, with a reason and a condition for review.|Case conference::The meeting where the team reviews a candidate and records a decision.}}
""",
    "case": {"title": "The conference on Tuesday", "html": """
<p>Ms. Marites Gonzales, 38, has been on peritoneal dialysis for two years. Her case is listed for Tuesday&rsquo;s transplant case conference. It is Thursday. You open her folder.</p>
<p>Her chest X-ray is from four months ago. Her stress echocardiogram is from fourteen months ago; the program protocol accepts twelve. A dental note from last week says &ldquo;tooth 36: periapical abscess, for extraction.&rdquo; The psychosocial assessment form is blank except for her name. Her cervical cancer screening result is &ldquo;to follow.&rdquo;</p>
<p>The transplant nephrologist, Dr. Liza Soriano, asks you for &ldquo;the usual summary&rdquo; by Monday noon.</p>
""", "questions": ["Which questions are already answered, which are open, and which are answered on expired results?",
                  "What do you route, to whom, and by when?",
                  "What will the one-page summary open with?"]},
    "sections": [
        ("question", "Organize by question", "Each question has an owner", """
<p>A test list invites a dangerous shortcut: &ldquo;all tests done&rdquo; sounds like &ldquo;cleared.&rdquo; A question list does not. Rewrite the workup as the questions the team must answer, each with its owner and its status.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Typical owner</th><th>What the coordinator tracks</th></tr></thead>
<tbody>
<tr><td>Is the heart safe for surgery?</td><td>Cardiology, with the transplant team</td><td>Which tests were ordered, dates, whether the cardiologist has written an opinion</td></tr>
<tr><td>Is there an infection to treat first?</td><td>Infectious diseases, transplant team</td><td>Screening dates; dental and other infection sources; treatment completion</td></tr>
<tr><td>Is there a cancer to find or treat first?</td><td>Transplant team, with screening services</td><td>Age- and sex-appropriate screening dates and results</td></tr>
<tr><td>Can the person take the medicines every day, and do they have support?</td><td>Psychosocial assessor, social work</td><td>Assessment completed by an experienced professional; barriers listed</td></tr>
<tr><td>Is the anatomy suitable (vessels, bladder)?</td><td>Transplant surgery, urology</td><td>Imaging and surgical review dates</td></tr>
<tr><td>Are other organs or conditions a concern?</td><td>Transplant nephrology</td><td>Specialist opinions requested and received</td></tr>
</tbody></table></div>
<p>KDIGO advises a psychosocial assessment for every candidate by a professional experienced in transplant, and an assessment of adherence and its barriers before transplant.[[rtc_kdigo2020]] The reason is practical, not moral. Medicine-taking problems after transplant are common and are associated with graft loss (Module 15); a barrier found before surgery &mdash; cost, literacy, no one to help at home &mdash; can often be fixed. It is not a test the person passes or fails.</p>
{{key:A normal result answers nothing until its owner reviews it. Track questions and owners, not just tests.}}
"""),
        ("current", "Keep results current", "Validity windows and expiry", """
<p>Every result ages. Your program&rsquo;s protocol sets how long each one counts as current for a decision, and the team can always ask for more. Track two dates for each result: when it was done and when it expires under protocol. Flag anything that expires before the decision meeting, and anything that will expire before a likely surgery date.</p>
<p>Flagging is not ordering. If the stress test is two months past the window, your SBAR asks the transplant physician whether to repeat it before the conference; the physician decides. Never present an expired result as current, and never leave it off the summary to avoid a delay.</p>
{{scene:The stale echo|<p>Coordinator Ms. Ruth Javier builds the summary for a conference and notices that a candidate&rsquo;s echocardiogram is 13 months old against a 12-month window. She sends the transplant nephrologist a one-line SBAR on Thursday.</p>
<p>The physician replies that a repeat is needed but the case can still be discussed for a provisional decision. Ms. Javier books the echo for Monday and marks the summary: &ldquo;Echo repeated Monday; result to be reviewed before final listing.&rdquo;</p>
<p class="tc-scene-take">The conference went ahead honestly, and the gap had an owner and a date.</p>}}
{{key:Flag expiry before the meeting, not after the decision. The physician decides whether to repeat.}}
"""),
        ("conference", "Prepare the decision", "The one-page summary", """
<p>A case conference is a decision meeting. Busy specialists decide better when the decision is stated first and the evidence is arranged around it.</p>
{{flow:A one-page conference summary|Decision requested::For example, accept as a candidate, defer, or decline, and whether a living donor is under evaluation.|Snapshot::Age, cause of kidney failure, dialysis type and start date, blood group.|Questions and answers::Each domain from the table, with owner, date, and status: answered, open, or expired.|Open items::What is missing, who owns it, and when it will be ready.|Barriers::Practical and psychosocial barriers found, and what is being done.|Donor status::Only that a separate donor evaluation is or is not in progress; no donor health details.}}
<p>Two things never go on the recipient&rsquo;s summary: the donor&rsquo;s health information and the coordinator&rsquo;s opinion on suitability. The donor has their own evaluation and their own conference. Your view on whether the person &ldquo;deserves&rdquo; a transplant has no place in a clinical decision.</p>
<p>After the meeting, record the decision exactly as the team states it, with conditions and the date of the next review, and close or open register rows to match.</p>
{{key:Open the summary with the decision requested. Close the meeting with a recorded decision and dated conditions.}}
"""),
        ("explain", "Make decisions understandable", "Deferral is not rejection", """
<p>Most team decisions are not yes or no. Many are &ldquo;not yet&rdquo;: treat a dental abscess, lose some weight safely, finish a cancer screening, stabilize the heart. A deferral explained badly sounds like a rejection; explained well, it is a plan.</p>
<div class="table-wrap"><table>
<thead><tr><th>Instead of</th><th>Say</th></tr></thead>
<tbody>
<tr><td>&ldquo;You were rejected.&rdquo;</td><td>&ldquo;The team wants your tooth infection treated first. After that, they will review you again.&rdquo;</td></tr>
<tr><td>&ldquo;It&rsquo;s just paperwork.&rdquo;</td><td>&ldquo;There is a medical reason: an infection can become dangerous with transplant medicines.&rdquo;</td></tr>
<tr><td>&ldquo;You&rsquo;ll definitely get a transplant after this.&rdquo;</td><td>&ldquo;Once this is done, the team will look at everything again. I&rsquo;ll call you with the date.&rdquo;</td></tr>
</tbody></table></div>
<p>If a person disagrees with a decision, explain how to ask for a second opinion or a review under hospital policy, and route the request. Use teach-back: ask the person to tell you in their own words what the next step is.</p>
{{key:A deferral is a reason, a next step, and a review date. Give all three, in plain words, and check understanding.}}
"""),
    ],
    "debrief": ["""
<p><strong>Answered, open, expired.</strong> The chest X-ray is current. The stress echocardiogram is two months past the window: answered on an expired result. Infection is open: a dental abscess needs extraction and review. Psychosocial assessment is open: the form is blank. Cancer screening is open: result to follow.</p>
<p><strong>Routing.</strong> SBAR to Dr. Soriano today: the echo is outside the window; does she want it repeated before Tuesday, or will the team give a provisional decision? Confirm with the dental service when the extraction is scheduled and ask that the note reach the infection reviewer. Book the psychosocial assessment with the program&rsquo;s assessor and the social worker. Chase the screening result with the laboratory, by name, with a due date of Monday.</p>
<p><strong>The summary.</strong> It opens with the decision requested &mdash; likely &ldquo;provisional acceptance pending dental clearance, repeat echocardiogram, psychosocial assessment, and screening result&rdquo; &mdash; and lists each open item with owner and date. After the conference, explain the outcome to Ms. Gonzales as a plan, not a verdict, and confirm her understanding with teach-back.</p>
"""],
    "skills": {"title": "Workup tracker and conference summary",
               "intro": "Using a fictional candidate folder, build the question-based tracker and the one-page summary while your preceptor observes.",
               "items": [
                   ("Converts a test list into questions with owners and statuses.", False),
                   ("Identifies every result outside its validity window and sends an SBAR to the decision owner.", True),
                   ("Writes a summary that opens with the decision requested and excludes donor health details.", True),
                   ("Records the team decision with conditions and next review date.", False),
                   ("Explains a deferral in plain language and confirms understanding with teach-back.", True),
               ],
               "placement": "Attend one case conference. Afterward, list every decision made and check whether each condition has an owner and date in the register."},
    "terms": [("Workup", "Tests and reviews answering whether transplant is safe and appropriate."),
              ("MDT", "Multidisciplinary team."), ("Validity window", "How long a result counts as current under protocol."),
              ("Deferral", "Not now, with a reason and a review condition."), ("Teach-back", "The person explains the plan in their own words.")],
    "readings": [("transplant-prehabilitation.html", "What candidates can do to get fit while they wait."),
                 ("highly-sensitized-kidney-transplant-candidates-clinician.html", "A clinician guide to candidates with many antibodies.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-1"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["04"])
